from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_neutrallensnildeterminantholonomyexecution_or_onescalefinality"
STATUS = (
    "MTT_NEUTRAL_FLAVOR_DETERMINANT_TYPE_SEPARATED_U3_LIFT_TORSOR_PROVED_"
    "ONE_HOLONOMY_PLUS_ONE_SCALE_CURRENT_CORPUS_FINALITY"
)
NEXT = "MTT_Selected_NeutralOneHolonomyOneScaleOntologyClosure_and_U5TierDecision_v1"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_NeutralLensNilDeterminantHolonomyExecution_or_OneScaleFinality_v1.md"


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
    types = outputs["type_separation"]
    torsor = outputs["central_lift_torsor"]
    exhaustion = outputs["source_exhaustion"]
    profile = outputs["one_holonomy_profile"]
    tier = outputs["U5_tier"]

    require(candidate["status"] == cert["status"] == STATUS, "A93 status changed")
    require(candidate["next_required_artifact"] == cert["next_required_artifact"] == NEXT, "A93 next changed")
    require(all(candidate["checks"].values()), "one or more A93 checks failed")
    require(types["ordinary_flavor_determinant"]["object"].startswith("det(E_nu)"), "wrong flavor determinant")
    require(types["analytic_Dirac_determinant"]["same_as_det_E_nu_by_definition"] is False, "determinants conflated")
    require(types["current_bridge_status"]["APS_route_rejected_as_mathematics"] is False, "APS overrejected")
    require(types["current_bridge_status"]["APS_route_rejected_as_current_direct_MTT_phase_source"] is True, "APS direct source retained")
    require(torsor["identifiability"]["number_of_surviving_continuous_shape_coordinates"] == 1, "torsor dimension")
    require(torsor["identifiability"]["additional_family_local_phase_coordinates"] == 0, "extra phase coordinates")
    require(all(exhaustion["source_markers"].values()), "source exhaustion marker missing")
    require(exhaustion["conclusion"]["one_holonomy_primitive_is_irreducible_in_current_formalization"] is True, "finality not proved")
    require(profile["A40_profile_identity"]["absolute_phi_residual"] < 1e-14, "profile inverse mismatch")
    require(profile["A40_profile_identity"]["absolute_ratio_residual"] < 1e-14, "profile roundtrip mismatch")
    require(profile["coordinate_accounting"]["net_profile_coordinate_reduction"] == 0, "false count reduction")
    require(tier["adoptable_standard"]["continuous_neutrino_specific_shape_primitives"] == 1, "shape primitive count")
    require(tier["adoptable_standard"]["dimensionful_neutral_scale_primitives"] == 1, "scale primitive count")
    require(tier["adoptable_standard"]["strict_no_knob"] is False, "strict no-knob overclosed")
    require(tier["new_continuous_parameters_added"] == 0, "A93 added parameter")
    for item in candidate["authority_hashes"]:
        path = Path(item["path"])
        require(path.exists(), f"missing A93 authority: {path}")
        require(hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"], f"A93 authority hash mismatch: {path}")
    note = NOTE.read_text(encoding="utf-8")
    for phrase in ["Determinant type correction", "Exact one-coordinate finality", "profile count is unchanged", "Strict no-knob U5 remains open", NEXT]:
        require(phrase in note, f"A93 note missing: {phrase}")

    print(json.dumps(cert, indent=2, sort_keys=True))
    print("neutral determinant typing and one-holonomy finality audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
