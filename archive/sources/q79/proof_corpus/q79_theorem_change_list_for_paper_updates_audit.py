"""Audit the q79 theorem-change list for paper updates."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_q79_theorem_change_list_for_paper_updates.py"
CERT = ROOT / "certificates" / "q79_theorem_change_list_for_paper_updates_certificate.json"
CANDIDATE = ROOT / "candidate_data" / "q79_theorem_change_list_for_paper_updates.candidate.json"
PAPER = ROOT / "proof_corpus" / "Q79_Theorem_Change_List_for_Paper_Updates_v1.md"
STATUS = "Q79_THEOREM_CHANGE_LIST_FOR_PAPER_UPDATES_BUILT"
TRACE_TARGET = "Q79_Selected_Trace_Equals_Emitted_27Mode_Operator_or_Full_HYM_Newton_Replay_v1"
DOTD_TARGET = "Q79_Selected_dotD_Alpha1_C1_Response_Emission_v1"
ALPHA1_KERNEL_TARGET = "Q79_Selected_Alpha1_Tangent_or_Retarded_Overlap_Kernel_v1"
PHYSICAL_ALPHA1_VALUE_FILL_TARGET = (
    "Q79_Selected_Physical_Alpha1_SourceNormalization_or_End0SectorRouting_Value_Fill_v1"
)
NEXT = "Q79_Selected_End0_to_SectorFunctor_Source_and_Value_Packet_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def main() -> int:
    failures: list[str] = []
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    require(proc.returncode == 0, f"script failed:\n{proc.stdout}", failures)
    for path in (CERT, CANDIDATE, PAPER):
        require(path.exists(), f"missing artifact: {path}", failures)
    if failures:
        print("\n".join(failures))
        return 1

    cert = load(CERT)
    candidate = load(CANDIDATE)
    paper = PAPER.read_text(encoding="utf-8")
    require(cert == candidate, "certificate and candidate differ", failures)
    require(cert["status"] == STATUS, f"unexpected status: {cert['status']}", failures)
    require(cert["next_required_artifact"] == NEXT, "unexpected next theorem", failures)
    require(len(cert["theorem_changes"]) == 23, "expected twenty-three theorem changes", failures)

    ids = {change["id"] for change in cert["theorem_changes"]}
    for expected in (
        "T0_terminal_q79_exact_charge_branch",
        "T1_conditional_weylpair_A",
        "T2_source_provenance",
        "T3_sector_charge_or_chirality",
        "T4_time_orientation_and_conjugate_branch",
        "T5_full_sm_data",
        "T6_matter_slot_overlap_normalization",
        "T7_samesource_operatorpacket_fill_or_nogo",
        "T8_stability_hym_or_routec_residual_source",
        "T9_global_destabilizer_enumeration_or_selected_residual",
        "T10_selected_ah_goodcover_promotion_hym_certificate",
        "T11_ah_source_selection_or_routec_residual_reduction",
        "T12_selected_monad_l2_source_and_operatorpic0_or_routec_residual",
        "T13_same_source_operator_provenance_or_selected_routec_solve",
        "T14_selected_visible_bundle_operator_source_or_primitive_c1_contractions",
        "T15_selected_de_green_dotd_source_for_primitive_c1",
        "T16_routec_selected_source_certificate_or_typed_de_construction",
        "T17_typed_monad_cech_or_hym_connection_witness",
        "T18_selected_finite_connection_solve_execution",
        "T19_selected_trace_equals_emitted_27mode_operator_or_full_hym_newton_replay",
        "T20_selected_dotd_alpha1_c1_response_emission",
        "T21_selected_alpha1_tangent_or_retarded_overlap_kernel",
        "T22_selected_physical_alpha1_source_normalization_or_end0_sector_value_fill",
    ):
        require(expected in ids, f"missing theorem change: {expected}", failures)

    actions = {change["id"]: change["action"] for change in cert["theorem_changes"]}
    require(actions["T0_terminal_q79_exact_charge_branch"] == "keep", "terminal q79 must be keep", failures)
    require(actions["T1_conditional_weylpair_A"] == "downgrade_to_conditional", "A theorem action wrong", failures)
    require(
        actions["T2_source_provenance"] == "replace_full_lemma_with_reduction_theorem",
        "source provenance action wrong",
        failures,
    )
    require(
        actions["T3_sector_charge_or_chirality"] == "replace_certificate_with_reduction_theorem",
        "sector charge action wrong",
        failures,
    )
    require(actions["T5_full_sm_data"] == "keep_open", "full SM action wrong", failures)
    require(
        actions["T6_matter_slot_overlap_normalization"]
        == "replace_closure_with_same_source_packet_reduction",
        "matter-slot overlap action wrong",
        failures,
    )
    require(
        actions["T7_samesource_operatorpacket_fill_or_nogo"]
        == "replace_bulk_fill_claim_with_validator_nogo_and_frontier_update",
        "same-source no-go action wrong",
        failures,
    )
    require(
        actions["T8_stability_hym_or_routec_residual_source"]
        == "replace_stability_claim_with_central_neutral_subtheorem",
        "stability/HYM action wrong",
        failures,
    )
    require(
        actions["T9_global_destabilizer_enumeration_or_selected_residual"]
        == "promote_frontier_to_reduced_AH_global_enumeration",
        "global enumeration action wrong",
        failures,
    )
    require(
        actions["T10_selected_ah_goodcover_promotion_hym_certificate"]
        == "replace_hym_closure_with_reflexive_hull_and_conditional_hym_bridge",
        "selected AH/good-cover promotion action wrong",
        failures,
    )
    require(
        actions["T11_ah_source_selection_or_routec_residual_reduction"]
        == "replace_goodcover_search_with_source_class_or_residual_reduction",
        "AH source/Route-C reduction action wrong",
        failures,
    )
    require(
        actions["T12_selected_monad_l2_source_and_operatorpic0_or_routec_residual"]
        == "close_monad_l2_source_under_section_principle_keep_operator_provenance_open",
        "selected monad/operator frontier action wrong",
        failures,
    )
    require(
        actions["T13_same_source_operator_provenance_or_selected_routec_solve"]
        == "replace_same_source_theorem_with_patchwork_nogo_and_source_target",
        "same-source operator provenance action wrong",
        failures,
    )
    require(
        actions["T14_selected_visible_bundle_operator_source_or_primitive_c1_contractions"]
        == "create_two_lane_target_keep_both_lanes_open",
        "selected visible operator/primitive C1 target action wrong",
        failures,
    )
    require(
        actions["T15_selected_de_green_dotd_source_for_primitive_c1"]
        == "create_selected_de_green_dotd_gate_provenance_open",
        "selected D_E/Green/dotD gate action wrong",
        failures,
    )
    require(
        actions["T16_routec_selected_source_certificate_or_typed_de_construction"]
        == "create_selected_connection_witness_contract",
        "selected connection witness action wrong",
        failures,
    )
    require(
        actions["T17_typed_monad_cech_or_hym_connection_witness"]
        == "record_witness_construction_attempt_values_absent",
        "typed monad/Cech or HYM witness action wrong",
        failures,
    )
    require(
        actions["T18_selected_finite_connection_solve_execution"]
        == "record_finite_execution_values_imported_source_trace_open",
        "selected finite connection execution action wrong",
        failures,
    )
    require(
        actions["T19_selected_trace_equals_emitted_27mode_operator_or_full_hym_newton_replay"]
        == "prove_selected_trace_equality_gap_layer_keep_dotd_c1_open",
        "selected trace equality gap-layer action wrong",
        failures,
    )
    require(
        actions["T20_selected_dotd_alpha1_c1_response_emission"]
        == "reduce_dotd_alpha1_c1_response_to_selected_tangent_keep_c1_open",
        "selected dotD/C1 response action wrong",
        failures,
    )
    require(
        actions["T21_selected_alpha1_tangent_or_retarded_overlap_kernel"]
        == "prove_analytic_kernel_formula_keep_selected_source_values_open",
        "selected alpha1 kernel action wrong",
        failures,
    )
    require(
        actions["T22_selected_physical_alpha1_source_normalization_or_end0_sector_value_fill"]
        == "replace_value_fill_closure_with_source_nogo_and_end0_functor_target",
        "selected physical alpha1 value-fill action wrong",
        failures,
    )

    guardrails = cert["global_guardrails"]
    for key in (
        "does_not_change_terminal_q79_exact_charge_branch",
        "does_not_claim_A_selected",
        "does_not_claim_b_selected",
        "does_not_claim_selected_sector_charge",
        "does_not_claim_selected_overlap_normalization",
        "does_not_claim_full_sm_closure",
        "does_not_use_observed_masses_or_ckm_inputs",
    ):
        require(guardrails[key] is True, f"guardrail missing: {key}", failures)

    for phrase in (
        "theorem-only update ledger",
        "does not change the terminal q79",
        "A_selected",
        "b_selected",
        "10_M={u,e}",
        "1_M shift rule",
        "full SM data closure is still open",
        "seven required fields",
        "zero selected-emitted fields",
        "validator rejects all seven required fields",
        "rank-two L2/Ext arithmetic input",
        "non-split stability/HYM",
        "central-neutral stability subtheorem",
        "reduced Appell-Humbert",
        "six central-neutral classes",
        "selected AH or literal good-cover",
        "reflexive line-hull",
        "conditional HYM bridge",
        "selected AH/good-cover source",
        "Li-Yau/Gauduchon",
        "representative issue",
        "good-cover/Cech execution representative",
        "operator-layer Pic0 recheck",
        "selected_source_verified",
        "TerminalAdmissibleSectionSourcePrinciple.v1",
        "h1=8",
        "flags-only diagnostic",
        "provenance, not numerical residual arithmetic",
        "patchwork no-go",
        "same-source operator theorem attempt",
        "honest packet",
        "primitive C1 contractions only",
        "not selected-source proofs",
        "selected visible bundle operator source",
        "two-lane gate",
        "24 selected same-source 3x3 matrices",
        "selected_operator_source",
        "Q79_Selected_Visible_Bundle_Operator_Source_or_Primitive_C1_Contractions_v1.md",
        "selected D_E/Green/dotD source gate",
        "honest current Route-C residual",
        "selected-flags-only diagnostic stack",
        "u=(Q,u,H)",
        "nuD=(L,N,H)",
        "gate theorem",
        "Q79_Selected_DE_Green_DotD_Source_for_Primitive_C1_v1.md",
        "selected connection witness",
        "honest selected-HYM/operator-source packet still fails",
        "typed monad/Cech D_E data",
        "direct selected HYM connection with residual bounds",
        "no selected D_E",
        "Q79_RouteC_Selected_Source_Certificate_or_Typed_DE_Construction_v1.md",
        "typed monad/Cech or HYM connection witness has now been",
        "generic constant maps phrase is not globally typed",
        "identity-rho smoke cannot be promoted",
        "actual selected finite connection solve",
        "Q79_Typed_Monad_Cech_or_HYM_Connection_Witness_v1.md",
        "Identity-rho smoke is superseded",
        "smooth 27-mode B_N",
        "first tracefree HYM correction",
        "selected trace equality",
        "Q79_Selected_Finite_Connection_Solve_Execution_v1.md",
        "selected trace equality for the emitted 27-mode D_E operator",
        "D_E gap/Riesz/Green layer",
        "selected eta_N=1.0",
        "selected gap lower bound",
        "selected Green norm bound",
        "Scalar and diagonal expS HYM replay are supporting progress only",
        "dotD_alpha1",
        "primitive C1 response",
        "Q79_Selected_Trace_Equals_Emitted_27Mode_Operator_or_Full_HYM_Newton_Replay_v1.md",
        TRACE_TARGET,
        "same-basis nonzero dotD_alpha1",
        "dotD_alpha1 is a first",
        "operator-level selected alpha1 tangent",
        "retarded-overlap derivative source",
        "does not replay dotD honestly",
        "selected Hess_Xi blocks",
        "primitive C1 contractions",
        "Q79_Selected_dotD_Alpha1_C1_Response_Emission_v1.md",
        DOTD_TARGET,
        "analytic retarded/Riesz kernel formula is proved",
        "dotPsi_i=-G Q dotD_alpha1 Psi_i",
        "Riesz projector derivative",
        "Duhamel retarded semigroup derivative",
        "conditional projector-retention criterion",
        "does not emit the selected alpha1 tangent values",
        "source-normalization",
        "End0-to-sector routing normalization",
        "honest dotD replay",
        "Q79_Selected_Alpha1_Tangent_or_Retarded_Overlap_Kernel_v1.md",
        ALPHA1_KERNEL_TARGET,
        "physical alpha1 value fill has been attempted on both legal",
        "direct Ext-density scale normalization is rejected",
        "does not vary the integral Chern/source row",
        "shared circle remains degree-zero",
        "selected End0-to-sector functor/source/value packet",
        "Existing End0 row response",
        "same-basis dotD/projector matrices",
        "No physical dotD payload",
        "selected sector routing",
        "selected transfer normalization",
        "selected End0-to-sector functor source and value packet",
        "Q79_Selected_Physical_Alpha1_SourceNormalization_or_End0SectorRouting_Value_Fill_v1.md",
        PHYSICAL_ALPHA1_VALUE_FILL_TARGET,
        NEXT,
    ):
        require(phrase in paper, f"paper missing phrase: {phrase}", failures)

    if failures:
        print("Q79 theorem-change list audit FAILED")
        print("\n".join(f"- {failure}" for failure in failures))
        return 1

    print("Q79 theorem-change list audit PASS")
    print(f"status: {cert['status']}")
    print(f"changes: {len(cert['theorem_changes'])}")
    print(f"next: {cert['next_required_artifact']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
