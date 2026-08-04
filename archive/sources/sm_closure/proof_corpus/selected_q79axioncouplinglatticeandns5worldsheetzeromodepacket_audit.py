from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79axioncouplinglatticeandns5worldsheetzeromodepacket"
STATUS = (
    "MTT_U6_X8_CHARGE_LATTICE_AND_NS5_SPAN_OBSTRUCTION_CLOSED_"
    "SELECTED_Q79_TOPOLOGICAL_AND_AMPLITUDE_VALUES_OPEN"
)
NEXT = "MTT_Selected_q79HiddenE8ConfinementAndNS5QualityAmplitudeCertificate_v1"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_q79AxionCouplingLatticeAndNS5WorldsheetZeroModePacket_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    candidate = load(CANDIDATE)
    cert = load(CERT)
    outputs = {key: load(ROOT / value) for key, value in candidate["outputs"].items()}
    lattice = outputs["lattice"]
    span = outputs["span_obstruction"]
    worldsheet = outputs["worldsheet_gate"]
    ns5 = outputs["NS5_quality"]
    frontier = outputs["U6_frontier"]

    require(candidate["status"] == cert["status"] == STATUS, "A100 status changed")
    require(candidate["next_required_artifact"] == cert["next_required_artifact"] == NEXT, "A100 next changed")
    require(all(candidate["checks"].values()), "one or more A100 checks failed")
    require(lattice["X8_reduction"]["E8_1_MD_after_Bianchi"] == "+3d_i", "visible X8 row")
    require(lattice["X8_reduction"]["E8_2_MD_after_Bianchi"] == "-3d_i", "hidden X8 row")
    require(lattice["X8_reduction"]["hidden_flatness_required"] is False, "flat hidden assumption retained")
    require(span["theorem"]["proved"], "NS5 span theorem")
    require(span["consequences"]["exact_hidden_and_NS5_blind_QCD_direction_exists"] is False, "no-go overruled")
    require(worldsheet["theorem"]["proved"], "worldsheet lift theorem")
    require(worldsheet["curve_lift_theorem"]["sufficiency_claimed"] is False, "worldsheet gate overpromoted")
    require(worldsheet["direct_strong_CP_decoupling"]["proved"], "worldsheet quality decoupling")
    require(worldsheet["direct_strong_CP_decoupling"]["requires_selected_worldsheet_amplitudes"] is False, "worldsheet values retained as direct quality blocker")
    require(worldsheet["minimal_Picard_stratum"]["selected_by_q79_now"] is False, "minimal Picard stratum overpromoted")
    require(ns5["selected_structural_payload"]["wrapped_cycle"] == "the full selected Fu-Yau X6", "NS5 cycle")
    require(ns5["selected_structural_payload"]["harmonic"] == 1, "NS5 harmonic")
    require(ns5["selected_structural_payload"]["action"] == "S_NS5=2*pi/alpha_GUT", "NS5 action")
    require(frontier["strict_readiness"] == {"filled": 0, "required": 6}, "strict readiness inflated")
    require(frontier["A98_nonQCD_payload"]["structural_formula_fields_filled"] == 2, "A98 structural progress")
    require(frontier["A98_nonQCD_payload"]["selected_numerical_amplitude_fields_filled"] == 0, "A98 values overpromoted")
    require(frontier["U6_strong_CP_closed"] is False, "U6 overclosed")
    require(candidate["results"]["new_continuous_parameters"] == 0, "A100 added parameter")
    for item in candidate["authority_hashes"]:
        path = Path(item["path"])
        require(path.exists(), f"missing A100 authority: {path}")
        require(hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"], f"A100 authority hash mismatch: {path}")
    note = NOTE.read_text(encoding="utf-8")
    for phrase in ["Exact `E8 x E8` reduction", "k_vis+k_hid=2 k_NS5", "Fu--Yau worldsheet gate", "S_NS5 = 2 pi / alpha_GUT", NEXT]:
        require(phrase in note, f"A100 note missing: {phrase}")

    print(json.dumps(cert, indent=2, sort_keys=True))
    print("q79 axion coupling lattice and NS5/worldsheet audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
