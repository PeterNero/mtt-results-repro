from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_neutraloneholonomyonescaleontologyclosure_and_u5tierdecision"
STATUS = (
    "MTT_NEUTRAL_ONEHOLONOMY_ONESCALE_PROFILE_ONTOLOGY_AND_ORDER_CLOSED_"
    "STRICT_SOURCE_AND_NIL_SATURATION_OPEN"
)
NEXT = "MTT_Selected_PostU5TierLedger_and_U9GlobalBranchMeasure_v1"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_NeutralOneHolonomyOneScaleOntologyClosure_and_U5TierDecision_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")],
        cwd=ROOT,
        check=True,
    )
    candidate = load(CANDIDATE)
    cert = load(CERT)
    outputs = {key: load(ROOT / value) for key, value in candidate["outputs"].items()}
    real = outputs["real_structure"]
    ordering = outputs["ordering"]
    profile = outputs["profile"]
    count = outputs["count"]
    decision = outputs["decision"]

    require(candidate["status"] == cert["status"] == STATUS, "A94 status changed")
    require(candidate["next_required_artifact"] == cert["next_required_artifact"] == NEXT, "A94 next changed")
    require(all(candidate["checks"].values()), "one or more A94 checks failed")
    require(real["Majorana_invariance"]["self_conjugate_phi_mod_2pi_over_3"] == ["0", "pi/3"], "self-conjugate points")
    require(real["Majorana_invariance"]["Z1344_self_characters"] == [0, 672], "self-character gate")
    require(real["same_source_profile_theorem"]["Dirac_only_profile_ontology_closed"] is True, "Dirac profile not closed")
    require(real["same_source_profile_theorem"]["strict_MTT_holonomy_value_selected"] is False, "holonomy overclosed")
    require(ordering["A40_orientation_pair"]["sorted_spectra_equal"] is True, "orientation spectra differ")
    require(ordering["A40_orientation_pair"]["both_normal_ordering"] is True, "A40 ordering")
    require(ordering["strict_ordering_selected_without_holonomy_value"] is False, "strict ordering overclosed")
    require(profile["derived_at_profile_tier"]["all_A40_rows_inherited"] is True, "A40 rows missing")
    require(profile["derived_at_profile_tier"]["row_counts"]["total_rows_filled"] == 36, "row count")
    require(profile["strict_boundaries"]["strict_no_knob_U5"] is False, "strict U5 overclosed")
    require(count["minimal_PMNS_breakdown"]["total"] == 6, "PMNS count")
    require(count["comparison"]["net_coordinate_reduction"] == 0, "false count reduction")
    require(decision["adopted_profile_standard"]["closed"] is True, "adopted U5 not closed")
    require(decision["strict_source_standard"]["closed"] is False, "strict U5 overclosed")
    require(decision["new_continuous_parameters_added"] == 0, "A94 added parameter")
    for item in candidate["authority_hashes"]:
        path = Path(item["path"])
        require(path.exists(), f"missing A94 authority: {path}")
        require(hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"], f"A94 authority hash mismatch: {path}")
    note = NOTE.read_text(encoding="utf-8")
    for phrase in ["Same-source ontology theorem", "Ordering theorem", "minimal PMNS count remains six", "Strict no-knob U5 remains open", NEXT]:
        require(phrase in note, f"A94 note missing: {phrase}")

    print(json.dumps(cert, indent=2, sort_keys=True))
    print("neutral one-holonomy one-scale U5 tier audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
