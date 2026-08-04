from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_fluxthresholdaxioncurrentanomalymatchingmap"
STATUS = (
    "MTT_U6_THRESHOLD_ONLY_EXOTIC_DECOUPLING_REJECTED_BY_ANOMALY_MATCHING_"
    "GREEN_SCHWARZ_4D_AXION_CURRENT_CONTRACT_SHARPENED"
)
NEXT = "MTT_Selected_4DGreenSchwarzAxionReductionAndSurvivingCurrent_v1"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_FluxThresholdAxionCurrentAnomalyMatchingMap_v1.md"


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
    matching = outputs["anomaly_matching"]
    gs = outputs["GS_support"]
    current = outputs["current_map"]
    frontier = outputs["U6_frontier"]

    require(candidate["status"] == cert["status"] == STATUS, "A96 status changed")
    require(candidate["next_required_artifact"] == cert["next_required_artifact"] == NEXT, "A96 next changed")
    require(all(candidate["checks"].values()), "one or more A96 checks failed")
    require(matching["UV_trace"] == {"light_16_1_contribution": 12, "heavy_10_minus2_contribution": -12, "complete_three_27_Qpsi_anomaly": 0}, "UV anomaly table")
    require(matching["IR_matching"]["matched_total"] == 0, "IR anomaly matching")
    require(matching["IR_matching"]["matter_only_trace_is_full_IR_anomaly"] is False, "matter trace overpromoted")
    require(all(gs["selected_support"].values()), "GS support missing")
    require(gs["flat_torsion_gerbe_boundary"]["de_Rham_H_curvature"] == "0", "flat gerbe curvature")
    require(gs["flat_torsion_gerbe_boundary"]["adds_continuous_de_Rham_axion_mode"] is False, "flat gerbe overpromoted")
    require(current["readiness"] == {"filled": 0, "required": 10}, "4D map readiness")
    require(frontier["retained_diagnostics"]["selected_prediction"] is False, "N_DW diagnostic promoted")
    require(frontier["U6_strong_CP_closed"] is False, "U6 overclosed")
    require(frontier["new_continuous_parameters_added"] == 0, "A96 added parameter")
    for item in candidate["authority_hashes"]:
        path = Path(item["path"])
        require(path.exists(), f"missing A96 authority: {path}")
        require(hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"], f"A96 authority hash mismatch: {path}")
    note = NOTE.read_text(encoding="utf-8")
    for phrase in ["Threshold no-go", "Wess--Zumino", "Green-Schwarz route", "currently `0/10`", NEXT]:
        require(phrase in note, f"A96 note missing: {phrase}")

    print(json.dumps(cert, indent=2, sort_keys=True))
    print("flux-threshold axion-current anomaly-matching audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
