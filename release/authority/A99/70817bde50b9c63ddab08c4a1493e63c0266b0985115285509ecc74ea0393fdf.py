from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79multiaxionsupersetandhiddenblinddirection"
STATUS = (
    "MTT_U6_FUYAU_MULTIAXION_SUPERSET_AND_HIDDEN_E8_BLIND_DIRECTION_"
    "THEOREM_CLOSED_SAME_SOURCE_COUPLING_LATTICE_AND_INSTANTON_ZEROMODES_OPEN"
)
NEXT = "MTT_Selected_q79AxionCouplingLatticeAndNS5WorldsheetZeroModePacket_v1"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_q79MultiAxionSupersetAndHiddenBlindDirection_v1.md"


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
    topology = outputs["topology"]
    coupling = outputs["coupling"]
    rank = outputs["rank_theorem"]
    frontier = outputs["U6_frontier"]

    require(candidate["status"] == cert["status"] == STATUS, "A99 status changed")
    require(candidate["next_required_artifact"] == cert["next_required_artifact"] == NEXT, "A99 next changed")
    require(all(candidate["checks"].values()), "one or more A99 checks failed")
    require(topology["conclusion"]["minimum_model_dependent_axions"] == 20, "Fu-Yau b2 lower bound")
    require(topology["conclusion"]["minimum_total_axion_candidates"] == 21, "axion count lower bound")
    require(topology["conclusion"]["exact_selected_Chern_rank_emitted"] is False, "Chern rank overpromoted")
    require(topology["conclusion"]["flux_or_instanton_lifting_already_quotiented"] is False, "physical count overpromoted")
    require(coupling["theorem"]["proved_as_implication"], "opposite-coupling implication")
    require(coupling["theorem"]["antecedent_selected_now"] is False, "coupling antecedent overpromoted")
    require("k_hidden dot v=0" in coupling["conditional_reduction"]["hidden_blind_direction"], "hidden cancellation")
    require("nonzero" in coupling["conditional_reduction"]["visible_coupling_on_v"], "visible coupling")
    require(rank["theorem"]["proved"], "rank theorem")
    require(frontier["readiness"] == {"filled": 0, "required": 6}, "same-source readiness")
    require(frontier["U6_strong_CP_closed"] is False, "U6 overclosed")
    require(candidate["results"]["selected_hidden_blind_direction"] is False, "direction promoted")
    require(candidate["results"]["new_continuous_parameters"] == 0, "A99 added parameter")
    for item in candidate["authority_hashes"]:
        path = Path(item["path"])
        require(path.exists(), f"missing A99 authority: {path}")
        require(hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"], f"A99 authority hash mismatch: {path}")
    note = NOTE.read_text(encoding="utf-8")
    for phrase in ["Topological headroom", "Hidden-blind theorem", "at least `21`", "remains `9/10`", NEXT]:
        require(phrase in note, f"A99 note missing: {phrase}")

    print(json.dumps(cert, indent=2, sort_keys=True))
    print("q79 multi-axion superset audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
