"""Audit dynamic-overlap/Hessian/Galerkin C1 degenerate-layer import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "dynamicoverlaptensor_hessiannormalization_or_galerkinc1contractions_valueemission_import.candidate.json"
CERT = ROOT / "certificates" / "dynamicoverlaptensor_hessiannormalization_or_galerkinc1contractions_valueemission_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "DynamicOverlapTensor_HessianNormalization_or_GalerkinC1Contractions_ValueEmission_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_dynamicoverlaptensor_hessiannormalization_or_galerkinc1contractions_valueemission.py"

STATUS = "DYNAMIC_OVERLAP_HESSIAN_GALERKIN_VALUE_LAYER_IMPORTED_DEGENERATE_VALUES_OPEN"
NEXT = "Selected_U1Y_RouteC_NonScalarDynamicOverlap_or_FullResponseCorrection_ValueEmission_v1"
SECTORS = ["u", "d", "e", "nuD"]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER), "--write"], cwd=ROOT, check=True)
    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["theorem"]["closure_claimed"] is False, "closure overclaimed")

    for name, value in data["checks"].items():
        require(value is True, f"failed check: {name}")

    packet = data["current_layer_value_packet"]
    require(packet["emitted_as_current_C1_observable_class"] is True, "value packet not emitted")
    require(packet["representative_fiber_shift"] == 0, "representative mismatch")
    require(packet["full_flavor_closure_from_current_layer"] is False, "flavor closure overclaimed")

    quotient = packet["quotient_checks"]
    require(quotient["fixed_fiber_shifts"] == [0, 1, 2], "fiber shifts mismatch")
    require(quotient["all_fixed_fiber_ranks_three"] is True, "rank check failed")
    require(quotient["all_YYstar_scalar_identity"] is True, "YY* scalar check failed")
    require(quotient["distinct_YYstar_scalars"] == [0.116935954119764], "YY* scalar mismatch")

    for shift in ["0", "1", "2"]:
        shift_data = packet["fixed_fiber_values"][shift]
        require(shift_data["selected_by_theorem"] is False, "absolute fiber shift overselected")
        for sector in SECTORS:
            inv = shift_data["sectors"][sector]["invariants"]
            require(inv["rank"] == 3, f"rank mismatch {shift}:{sector}")
            require(inv["YYstar_is_scalar_identity"] is True, f"YY* not scalar {shift}:{sector}")
            require(inv["YYstar_traceless_norm_sq"] == 0.0, f"traceless residual {shift}:{sector}")

    degeneracy = packet["sector_degeneracy_checks"]
    require(degeneracy["all_sector_YYstar_identical"] is True, "sector YY* mismatch")
    require(degeneracy["commutator_norm_sq_u_d"] == 0.0, "u/d commutator nonzero")
    require(degeneracy["commutator_norm_sq_e_nuD"] == 0.0, "e/nuD commutator nonzero")
    require(
        degeneracy["nondegenerate_mass_hierarchy_possible_from_current_layer"] is False,
        "mass hierarchy overclaimed",
    )
    require(degeneracy["CKM_PMNS_possible_from_current_layer"] is False, "mixing overclaimed")
    require(degeneracy["CP_odd_invariant_possible_from_current_layer"] is False, "CP overclaimed")

    dynamic = data["dynamic_overlap_tensor_route"]
    require(dynamic["selected_dynamic_overlap_tensor_emitted"] is False, "dynamic tensor emitted")
    require(
        dynamic["operator_level_basis_transport_or_vertex_source_emitted"] is False,
        "operator-level source emitted",
    )

    hessian = data["hessian_normalization_route"]
    require(hessian["static_trace_gram_normalization_selected"] is True, "trace gram missing")
    require(hessian["selected_Hessian_blocks_emitted"] is False, "Hessian blocks emitted")
    require(hessian["selected_b_selected_emitted"] is False, "b_selected emitted")

    galerkin = data["galerkin_C1_contractions_route"]
    require(galerkin["finite_current_layer_contraction_values_computed"] is True, "finite values missing")
    require(
        galerkin["honest_galerkin_manifest_status"] == "OPEN_C1_PRIMITIVE_CONTRACTIONS_MISSING",
        "honest Galerkin status mismatch",
    )
    require(galerkin["selected_Galerkin_C1_contractions_emitted"] is False, "Galerkin emitted")

    acceptance = data["acceptance_kernel_for_next_values"]
    require(acceptance["current_values_fail_these_tests"] is True, "no-go not recorded")
    require(acceptance["compatible_with_higher_order_criterion"] is True, "criterion missing")
    require(all(acceptance["minimum_next_value_packet"].values()), "minimum next packet incomplete")

    guardrails = data["guardrails"]
    require(guardrails["current_layer_value_packet_emitted"] is True, "guardrail value missing")
    require(guardrails["current_layer_flavor_no_go"] is True, "guardrail no-go missing")
    require(guardrails["selected_dynamic_overlap_tensor_claimed"] is False, "dynamic tensor claimed")
    require(guardrails["selected_Hessian_blocks_claimed"] is False, "Hessian claimed")
    require(guardrails["selected_Galerkin_C1_contractions_claimed"] is False, "Galerkin claimed")
    require(guardrails["A_selected_claimed"] is False, "A_selected claimed")
    require(guardrails["b_selected_claimed"] is False, "b_selected claimed")
    require(guardrails["observed_data_used"] is False, "observed data used")
    require(guardrails["target_fitting_used"] is False, "target fitting used")
    require(guardrails["full_SM_closure_claimed"] is False, "full closure claimed")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
