"""Audit the dynamic C1 dual-lane derivation/Galerkin progress import."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
JSON_PATH = ROOT / "selected_dynamicc1_duallane_derivation_galerkin_progress.import.json"
MD_PATH = ROOT / "DynamicC1_DualLane_DerivationAndGalerkin_Progress_Import_v1.md"

EXPECTED_STATUS = "DYNAMIC_C1_DUALLANE_PROGRESS_PATCHED_CLOSE_STRICT_UNPATCHED_OPEN"
EXPECTED_NEXT = "MTT_Selected_IndependentGalerkinC1Contractions_or_DeriveResidualProjectorAxiom_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def main() -> None:
    data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    text = MD_PATH.read_text(encoding="utf-8", errors="ignore")

    require(data["status"] == EXPECTED_STATUS, "unexpected status")
    require(data["next_required_artifact"] == EXPECTED_NEXT, "unexpected next artifact")
    require(data["closure_claimed"] is False, "strict closure must not be claimed")
    require(data["patched_spine_closure_claimed"] is True, "patched closure should be recorded")
    require(data["unpatched_theorem_closure_claimed"] is False, "unpatched closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")

    audits = data["verified_audits"]
    require(len(audits) == 8, "expected eight verified audits")
    require(all(status == "PASS" for status in audits.values()), "all imported audits must pass")

    lane_a = data["route_A_derivation_axiom_lane"]
    require(lane_a["formal_hessian_coercivity_on_residual_quotient"] is True, "formal Hessian not closed")
    require(lane_a["dynamic_dotD_trace_binding"] is True, "dynamic dotD binding missing")
    require(lane_a["residual_projector_axiom_inserted_in_local_patch"] is True, "local patch not recorded")
    require(lane_a["residual_projector_axiom_proved_unpatched"] is False, "unpatched axiom overproved")
    require(lane_a["SM_parity_dynamic_packet_closed_in_patched_spine"] is True, "patched spine closure missing")
    require(lane_a["SM_parity_dynamic_packet_closed_in_unpatched_spine"] is False, "unpatched closure overclaimed")

    lane_b = data["route_B_galerkin_lane"]
    require(lane_b["basis_stage_can_advance"] is True, "basis stage should advance")
    require(lane_b["dynamic_trace_binding_accepted"] is True, "dynamic trace binding missing")
    require(lane_b["primitive_rows_attempted"] is True, "primitive rows not attempted")
    require(lane_b["strict_replay_passes"] is True, "strict replay should pass")
    require(lane_b["honest_independent_galerkin_execution_passes"] is False, "honest Galerkin overclaimed")
    require(len(lane_b["why_not_honest"]) == 3, "expected three honesty blockers")

    target = data["shared_locked_target"]
    require(target["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "unexpected A^T A")
    require(target["A_transpose_b"] == [12.0, 12.0], "unexpected A^T b")
    require(target["deltaTheta_C1"] == [1.0, 1.0], "unexpected deltaTheta")
    require(target["rank"] == 2, "unexpected rank")
    require(target["condition_number"] == 1.0, "unexpected condition number")

    for key in [
        "formal_first_variation_side_conditions_partially_closed",
        "stationary_trace_and_basis_values_promoted",
        "dynamic_dotD_trace_binding_closed",
        "minimal_residual_source_packet_template_emitted",
        "two_lane_acceptance_contract_fixed",
        "first_galerkin_replay_passes",
        "local_patched_spine_dynamic_packet_closes",
        "observed_constants_excluded_as_selectors",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing: {key}")

    for key in [
        "derive_residual_projector_axiom_from_unpatched_MTT",
        "prove_selected_differentiated_PhiFinC1_application_rule",
        "compute_independent_primitive_galerkin_contractions",
        "emit_independent_hessian_b_selected",
        "emit_independent_selected_HYM_Galerkin_zero_mode_basis",
        "true_SM_equivalence_closure_without_local_axiom",
        "full_no_knob_flavor_closure",
    ]:
        require(data["what_remains_open"][key] is True, f"open flag missing: {key}")

    for phrase in [
        "local/patched proof spine closes",
        "not yet an honest independent Galerkin computation",
        "derive the residual-projector axiom from unpatched MTT",
        "compute independent selected Galerkin C1 contractions",
    ]:
        require(phrase in text, f"missing markdown phrase: {phrase}")

    print(json.dumps({"status": data["status"], "next": data["next_required_artifact"]}, indent=2))
    print("PASS selected_dynamicc1_duallane_derivation_galerkin_progress.import.json")


if __name__ == "__main__":
    main()
