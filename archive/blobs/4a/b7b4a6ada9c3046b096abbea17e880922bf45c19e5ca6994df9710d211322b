from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_4dgreenschwarzaxionreductionandsurvivingcurrent"
STATUS = (
    "MTT_U6_MODEL_INDEPENDENT_HETEROTIC_AXION_REDUCTION_AND_INDEX_ONE_"
    "COLOR_COUPLING_CLOSED_QUALITY_BOUND_OPEN"
)
NEXT = "MTT_Selected_AxionQualityInstantonSuppressionBound_v1"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_4DGreenSchwarzAxionReductionAndSurvivingCurrent_v1.md"


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
    reduction = outputs["reduction"]
    index = outputs["embedding_index"]
    current = outputs["current"]
    current_map = outputs["current_map"]
    frontier = outputs["U6_frontier"]

    require(candidate["status"] == cert["status"] == STATUS, "A97 status changed")
    require(candidate["next_required_artifact"] == cert["next_required_artifact"] == NEXT, "A97 next changed")
    require(all(candidate["checks"].values()), "one or more A97 checks failed")
    require(reduction["selected_background"]["compact_connected_oriented_six_manifold"], "X6 orientation")
    require(reduction["mode"]["not_the_flat_Z3_gerbe"], "continuous/discrete type separation")
    require(reduction["normalization_boundary"]["canonical_formula_closed"], "f_MI formula")
    require(not reduction["normalization_boundary"]["physical_absolute_f_MI_derived_without_anchor"], "absolute scale overclaim")
    require(index["E8_to_E6"]["embedding_index"] == 1, "E8/E6 index")
    require(index["E6_to_SU3c"]["embedding_index"] == 1, "E6/SU3 index")
    require(index["composition"]["k3"] == index["composition"]["periodic_axion_domain_wall_number"] == 1, "k3 or N_DW")
    require(not index["composition"]["uses_matter_Qpsi_anomaly"], "Qpsi anomaly reused")
    require(current["threshold_matching_retained"]["pure_Qpsi_matched_total"] == 0, "Qpsi matching")
    require(current_map["readiness"] == {"filled": 9, "required": 10}, "A97 current map")
    require(current_map["final_fields"]["quality_breaking_bound"] is False, "quality overclosed")
    require(frontier["U6_structural_axion_map_closed"] is True, "structural map")
    require(frontier["U6_strong_CP_closed"] is False, "U6 overclosed")
    require(frontier["diagnostic_only"]["selected_prediction"] is False, "benchmark promoted")
    require(candidate["results"]["new_continuous_parameters"] == 0, "A97 added parameter")
    for item in candidate["authority_hashes"]:
        path = Path(item["path"])
        require(path.exists(), f"missing A97 authority: {path}")
        require(hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"], f"A97 authority hash mismatch: {path}")
    note = NOTE.read_text(encoding="utf-8")
    for phrase in ["Correct continuous mode", "Exact color index", "`N_DW=1`", "`9/10`", NEXT]:
        require(phrase in note, f"A97 note missing: {phrase}")

    print(json.dumps(cert, indent=2, sort_keys=True))
    print("4D Green-Schwarz axion reduction audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
