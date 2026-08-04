"""Audit orientation-carrying D_E/dotD reduction import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "orientation_carrying_de_dotd_reduction_import.candidate.json"
CERT = ROOT / "certificates" / "orientation_carrying_de_dotd_reduction_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "OrientationCarrying_DE_DotD_Reduction_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_orientation_carrying_de_dotd_reduction.py"

STATUS = "ORIENTATION_CARRYING_DE_DOTD_IMPORTED_SOURCE_ORIGIN_ALPHA1_OPEN"
NEXT = "MTT_Selected_Source_Origin_and_Alpha1_Driver_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["theorem"]["closure_claimed"] is False, "closure overclaimed")
    require(all(data["checks"].values()), "not all checks passed")

    upstream = data["upstream_orientation_carrying_de_dotd"]
    audit = upstream["finite_payload_audit"]
    require(audit["q79_residuals_zero"] is True, "q79 residual smoke not zero")
    require(audit["q79_positive_gates"]["mtt_hessian_min_eigenvalue"] is True, "Hessian gate not positive")
    require(audit["q79_positive_gates"]["riesz_gap_min"] is True, "Riesz gate not positive")
    require(audit["q79_de_action_flags"]["boundary_conditions_verified"] is True, "D_E boundary not verified")
    require(audit["q79_reduced_green_flags"]["operator_data_verified"] is True, "Green operator data not verified")
    require(audit["q79_dotd_response_flags"]["horizontal_gauge_verified"] is True, "horizontal gauge not verified")
    require(audit["q369_conjugate_shape_present"] is True, "q369 conjugate shape missing")
    for key in [
        "selected_source_origin",
        "selected_by_mtt",
        "visible_bundle_or_twisted_gerbe_source",
        "pic0_selected_or_quotiented",
        "same_branch_derivative_verified",
        "alpha1_driver_provenance",
        "primitive_C1_contractions",
    ]:
        require(upstream["what_remains_open"][key] is True, f"upstream open item missing: {key}")

    for key in [
        "selected_by_mtt must be true",
        "visible_bundle_or_twisted_gerbe_source must be true",
        "same_branch_derivative_verified must be true",
        "selected_dotD_alpha1 validator did not pass (exit 1)",
    ]:
        require(key in upstream["validator_open_items"], f"validator blocker missing: {key}")

    guard = data["guardrails"]
    for key in [
        "claims_selected_source_origin",
        "claims_selected_by_mtt",
        "claims_pic0_resolution",
        "claims_same_branch_derivative",
        "claims_selected_DE_Green_dotD_flags",
        "claims_alpha1_driver_provenance",
        "claims_primitive_C1_contractions",
        "claims_A_selected_or_b_selected",
        "claims_Yukawa_or_full_SM_closure",
        "uses_observed_cp_sign",
        "uses_observed_or_benchmark_inputs",
        "uses_lifted_selected_flags_as_proof",
        "target_fitting_used",
    ]:
        require(guard[key] is False, f"guardrail overclaimed: {key}")

    require("source-origin and" in note, "note missing source-origin reduction")
    require("does not promote the smoke data" in note, "note missing smoke guardrail")
    require(NEXT in note, "note missing next artifact")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
