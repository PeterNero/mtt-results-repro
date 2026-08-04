from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_axionqualityinstantonsuppressionbound"
STATUS = (
    "MTT_U6_PERTURBATIVE_AXION_QUALITY_EXACT_AND_NONPERTURBATIVE_"
    "QUALITY_INEQUALITY_CLOSED_SELECTED_INSTANTON_AMPLITUDES_OPEN"
)
NEXT = "MTT_Selected_q79HiddenGaugeAndNS5InstantonActionPacket_v1"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_AxionQualityInstantonSuppressionBound_v1.md"


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
    theorem = outputs["quality_theorem"]
    census = outputs["source_census"]
    diagnostic = outputs["action_diagnostic"]
    frontier = outputs["U6_frontier"]

    require(candidate["status"] == cert["status"] == STATUS, "A98 status changed")
    require(candidate["next_required_artifact"] == cert["next_required_artifact"] == NEXT, "A98 next changed")
    require(all(candidate["checks"].values()), "one or more A98 checks failed")
    require(theorem["theorem"]["proved"], "quality theorem")
    require(not theorem["theorem"]["uses_small_angle_linearization"], "linearization used")
    require(set(theorem["sufficient_conditions"]) == {"derivative", "local_convexity", "exclude_opposite_QCD_extremum"}, "quality conditions")
    require(census["closed"]["perturbative_local_potential_for_theta_MI"] == 0, "perturbative quality")
    require(census["closed"]["q79_flat_Z3_gerbe_de_Rham_H"] == "0", "flat gerbe H")
    require(census["readiness"] == {"filled": 0, "required": 9}, "selected instanton source census")
    require(all(census["corpus_markers"].values()), "corpus quality markers")
    require(not diagnostic["selected_prediction"], "diagnostic promoted")
    require(180 < diagnostic["thresholds"][0]["required_action_max"] < 182, "1e16 action diagnostic")
    require(189 < diagnostic["thresholds"][1]["required_action_max"] < 191, "1e17 action diagnostic")
    require(frontier["new_closure"]["perturbative_axion_quality"], "perturbative closure")
    require(frontier["U6_strong_CP_closed"] is False, "U6 overclosed")
    require(candidate["results"]["new_continuous_parameters"] == 0, "A98 added parameter")
    for item in candidate["authority_hashes"]:
        path = Path(item["path"])
        require(path.exists(), f"missing A98 authority: {path}")
        require(hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"], f"A98 authority hash mismatch: {path}")
    note = NOTE.read_text(encoding="utf-8")
    for phrase in ["Exact quality theorem", "perturbative quality", "`0/9`", "`9/10`", NEXT]:
        require(phrase in note, f"A98 note missing: {phrase}")

    print(json.dumps(cert, indent=2, sort_keys=True))
    print("axion-quality instanton suppression audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
