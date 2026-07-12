"""Audit dynamic-overlap / Hessian / Galerkin C1 value emission."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "selected_dynamicoverlaptensor_hessiannormalization_or_galerkinc1contractions_valueemission.candidate.json"
CERT = ROOT / "certificates" / "selected_dynamicoverlaptensor_hessiannormalization_or_galerkinc1contractions_valueemission_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_DynamicOverlapTensor_HessianNormalization_or_GalerkinC1Contractions_ValueEmission_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_dynamicoverlaptensor_hessiannormalization_or_galerkinc1contractions_valueemission.py"

STATUS = (
    "MTT_SELECTED_DYNAMICOVERLAPTENSOR_HESSIANNORMALIZATION_OR_GALERKINC1CONTRACTIONS_"
    "VALUEEMISSION_BUILT_DEGENERATE_LAYER_VALUES_OPEN"
)
NEXT = "MTT_Selected_NonScalarDynamicOverlap_or_FullResponseCorrection_ValueEmission_v1"
SECTORS = ["u", "d", "e", "nuD"]
TOL = 1e-12


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
    require(data["next_required_artifact"] == NEXT, "candidate next artifact mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next artifact mismatch")
    require(NEXT in note, "note missing next artifact")

    selected = data["selected_inputs"]
    for key in [
        "alpha1_driver_verified",
        "selected_dotD_source_verified",
        "honest_dotD_alpha1_replay",
        "static_overlap_transfer_normalization_selected",
        "all_smslot_source_arrows_closed",
        "primitive_active_shift_selected",
        "fixed_fiber_quotient_selected_for_current_observables",
        "current_primitive_class_valid_C1_observable_layer",
    ]:
        require(selected[key] is True, f"selected input missing: {key}")
    require(
        selected["current_primitive_class_flavor_closure"] is False,
        "current layer overclaimed as flavor closure",
    )

    packet = data["current_layer_value_packet"]
    require(packet["emitted_as_current_C1_observable_class"] is True, "value packet not emitted")
    require(packet["representative_fiber_shift"] == 0, "representative shift mismatch")
    require(packet["full_flavor_closure_from_current_layer"] is False, "flavor closure overclaimed")

    quotient = packet["quotient_checks"]
    require(quotient["fixed_fiber_shifts"] == [0, 1, 2], "fixed fiber shifts mismatch")
    require(quotient["all_fixed_fiber_ranks_three"] is True, "fixed fibers not rank three")
    require(quotient["all_YYstar_scalar_identity"] is True, "YY* scalar identity failed")
    require(quotient["all_YYstar_equal_to_representative"] is True, "YY* quotient equality failed")
    require(
        quotient["quotient_invariant_for_current_spectral_observables"] is True,
        "quotient invariance missing",
    )

    for shift in ["0", "1", "2"]:
        shift_data = packet["fixed_fiber_values"][shift]
        require(shift_data["primitive_active_shift"] == [1, 1], "active shift mismatch")
        require(shift_data["selected_by_theorem"] is False, "absolute fiber shift overselected")
        for sector in SECTORS:
            inv = shift_data["sectors"][sector]["invariants"]
            require(inv["rank"] == 3, f"rank mismatch for {shift}:{sector}")
            require(inv["YYstar_is_scalar_identity"] is True, f"YY* non-scalar for {shift}:{sector}")
            require(inv["YYstar_traceless_norm_sq"] <= TOL, f"traceless residual too large for {shift}:{sector}")

    degeneracy = packet["sector_degeneracy_checks"]
    require(
        degeneracy["all_sector_matrices_identical_in_representative"] is True,
        "representative sector matrices differ unexpectedly",
    )
    require(degeneracy["all_sector_YYstar_identical"] is True, "sector YY* mismatch")
    require(degeneracy["commutator_norm_sq_u_d"] <= TOL, "u/d commutator nonzero")
    require(degeneracy["commutator_norm_sq_e_nuD"] <= TOL, "e/nuD commutator nonzero")
    require(
        degeneracy["nondegenerate_mass_hierarchy_possible_from_current_layer"] is False,
        "mass hierarchy overclaimed",
    )
    require(degeneracy["CKM_PMNS_possible_from_current_layer"] is False, "mixing overclaimed")
    require(degeneracy["CP_odd_invariant_possible_from_current_layer"] is False, "CP overclaimed")

    dynamic = data["dynamic_overlap_tensor_route"]
    require(dynamic["current_layer_overlap_values_constructed"] is True, "current layer route missing")
    require(dynamic["selected_dynamic_overlap_tensor_emitted"] is False, "dynamic tensor overclaimed")
    require(
        dynamic["operator_level_basis_transport_or_vertex_source_emitted"] is False,
        "operator source overclaimed",
    )

    hessian = data["hessian_normalization_route"]
    require(hessian["static_trace_gram_normalization_selected"] is True, "trace normalization missing")
    require(hessian["selected_Hessian_blocks_emitted"] is False, "Hessian blocks overclaimed")
    require(hessian["selected_b_selected_emitted"] is False, "b_selected overclaimed")
    require(
        hessian["promoted_as_selected_Hessian_normalization"] is False,
        "Hessian normalization overpromoted",
    )

    galerkin = data["galerkin_C1_contractions_route"]
    require(
        galerkin["finite_current_layer_contraction_values_computed"] is True,
        "finite contraction values missing",
    )
    require(
        galerkin["honest_galerkin_manifest_status"] == "OPEN_C1_PRIMITIVE_CONTRACTIONS_MISSING",
        "honest Galerkin status mismatch",
    )
    require(
        galerkin["honest_galerkin_selected_source_verified"] is False,
        "honest Galerkin source oververified",
    )
    require(
        galerkin["selected_Galerkin_C1_contractions_emitted"] is False,
        "Galerkin contractions overclaimed",
    )

    promotion = data["promotion_decision"]
    require(
        promotion["current_layer_values_selected_as_C1_observable_class"] is True,
        "current layer observable class not selected",
    )
    for key in [
        "current_layer_values_promoted_as_dynamic_overlap_tensor",
        "current_layer_values_promoted_as_A_selected",
        "current_layer_values_promoted_as_b_selected",
        "current_layer_values_promoted_as_flavor_closure",
    ]:
        require(promotion[key] is False, f"promotion overclaimed: {key}")

    kernel = data["acceptance_kernel_for_next_values"]
    require(kernel["current_values_fail_these_tests"] is True, "current no-go not recorded")
    require(kernel["compatible_with_higher_order_criterion"] is True, "higher-order criterion missing")

    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(data["dynamic_overlap_tensor_claimed"] is False, "dynamic overlap claimed")
    require(data["A_selected_claimed"] is False, "A_selected claimed")
    require(data["b_selected_claimed"] is False, "b_selected claimed")
    require(data["Galerkin_C1_contractions_claimed"] is False, "Galerkin contractions claimed")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
