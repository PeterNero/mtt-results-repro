"""Audit selected Route-C smooth B_N Galerkin lift import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "routec_smooth_bn_galerkin_lift_import.candidate.json"
CERT = ROOT / "certificates" / "routec_smooth_bn_galerkin_lift_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "RouteC_Smooth_BN_GalerkinLift_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_routec_smooth_bn_galerkin_lift.py"

STATUS = "ROUTEC_SMOOTH_BN_GALERKIN_LIFT_IMPORTED_SELECTED_DE_OPEN"
NEXT = "MTT_Selected_RouteC_DE_Action_on_Smooth_BN_v1"


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

    summary = data["smooth_bn_summary"]
    require(summary["dimension"] == 27, "wrong B_N dimension")
    require(summary["basis_count"] == 27, "wrong B_N basis count")
    require(summary["quadrature_nodes"] == 9, "wrong quadrature count")
    require(summary["zero_cluster_dimension"] == 3, "wrong zero-cluster dimension")
    require(summary["complement_gap"] > 0, "nonpositive complement gap")
    require(summary["ordinary_bundle_equivariance"] is False, "ordinary equivariance overclaimed")
    require(
        summary["projective_equivariance_up_to_central_phase"] is True,
        "projective equivariance missing",
    )
    require(summary["selected_DE_action_on_basis"] is False, "selected D_E overclaimed")
    require(summary["sector_projection_maps_constructed"] is False, "sector projectors overclaimed")
    require(summary["dotD_alpha1_and_Green_operator_constructed"] is False, "dotD overclaimed")
    require(
        summary["full_iwasawa_truncation_error_certified"] is False,
        "full truncation error overclaimed",
    )

    upstream = data["upstream_smooth_bn_lift"]
    gates = upstream["gates"]
    fields = upstream["contract_comparison"]["fields_emitted_now"]
    missing = upstream["contract_comparison"]["still_missing_for_full_contract"]
    require(gates["Gram_matrix_positive_definite"] is True, "Gram gate not passed")
    require(gates["stiffness_matrix_positive_semidefinite"] is True, "stiffness gate not passed")
    require(gates["Riesz_projector_constructed"] is True, "Riesz not constructed")
    require(gates["reduced_Green_operator_constructed"] is True, "Green not constructed")
    require(upstream["target_fitting_used"] is False, "target fitting not excluded")
    require(missing["selected_D_E_action_on_basis"] is True, "missing D_E not preserved")
    require(
        missing["sector_projection_maps_constructed"] is True,
        "missing sector projectors not preserved",
    )
    require(missing["dotD_alpha1_in_same_basis"] is True, "missing dotD not preserved")

    guard = data["guardrails"]
    for key in [
        "claims_selected_DE_action_on_basis",
        "claims_sector_projectors_constructed",
        "claims_dotD_alpha1_in_same_basis",
        "claims_full_iwasawa_truncation_error",
        "claims_full_BN_payload_gate",
        "claims_honest_replay_ready",
        "claims_full_SM_or_no_knob_closure",
        "uses_observed_or_benchmark_inputs",
        "target_fitting_used",
    ]:
        require(guard[key] is False, f"guardrail overclaimed: {key}")

    require("smooth `B_N` Galerkin scaffold" in note, "note missing scaffold statement")
    require("This is not a full straight proof" in note, "note missing guardrail")
    require(NEXT in note, "note missing next artifact")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
