"""Build CONST-HIGGS-01 H7B1T UV Higgs-plane binding/minimal-lift theorem gate."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
SM_PARITY = TEXPAPERS / "mtt-sm-parity-closure"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_higgs_01_h7b1t_uv_higgs_plane_binding_or_minimal_lift_theorem"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
FORMAL_SEQUENCE = BASE / "formal_uv_exact_sequence_scaffold.packet.json"
MINIMAL_LIFT = BASE / "conditional_metric_minimal_lift_formula.packet.json"
BINDING_ATTEMPT = BASE / "actual_source_binding_attempt.packet.json"
NO_CYCLE = BASE / "non_circulation_ledger.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_HIGGS_01_H7B1T_UVHiggsPlaneBindingOrMinimalLiftTheorem_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7B1T_FORMAL_SEQUENCE_AND_MINIMAL_LIFT_FORMULA_CLOSED_SOURCE_BINDING_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def clean_flags() -> dict[str, bool]:
    return {
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    h7b1s_path = DATA / "const_higgs_01_h7b1s_huv_bridge_functor_or_nonlinear_hym_row_execution.candidate.json"
    h7b1s_minimal_path = DATA / "const_higgs_01_h7b1s_huv_bridge_functor_or_nonlinear_hym_row_execution" / "minimal_uv_higgs_plane_binding_theorem.packet.json"
    h7b1a_single_path = DATA / "const_higgs_01_h7b1a_selected_two_higgs_metric_or_light_projector_source" / "single_higgs_quotient_map_import.packet.json"
    h7b1a_contract_path = DATA / "const_higgs_01_h7b1a_selected_two_higgs_metric_or_light_projector_source" / "selected_splitting_or_projector_source_contract.packet.json"
    h7b1d_import_path = DATA / "const_higgs_01_h7b1d_diagonal_hym_rank2_metric_candidate" / "diagonal_hym_rank2_import.packet.json"
    h7b1d_conditional_path = DATA / "const_higgs_01_h7b1d_diagonal_hym_rank2_metric_candidate" / "conditional_huv_readout.packet.json"
    h7b1f_functor_path = DATA / "const_higgs_01_h7b1f_nonsplit_valpha_to_huv_omega_packet" / "basis_invariant_huv_functor_theorem.packet.json"
    h7b1g_bhuv_path = DATA / "const_higgs_01_h7b1g_fill_bhuv_or_msource" / "bhuv_minimal_lift_payload_request.packet.json"
    hym_payload_path = SM_PARITY / "candidate_data" / "selected_hym_operator_payload_extraction_from_diagonal_replay.candidate.json"

    h7b1s = load(h7b1s_path)
    h7b1s_minimal = load(h7b1s_minimal_path)
    single = load(h7b1a_single_path)
    contract = load(h7b1a_contract_path)
    diagonal_import = load(h7b1d_import_path)
    diagonal_conditional = load(h7b1d_conditional_path)
    huv_functor = load(h7b1f_functor_path)
    bhuv_request = load(h7b1g_bhuv_path)
    hym_payload = load(hym_payload_path)

    quotient = single["q79_low_energy_projection"]["quotient_map_q"]
    plane = single["UV_two_Higgs_plane"]
    basis = plane["basis"]
    formal_sequence_closed = all(
        [
            basis == ["H_u", "H_d^dagger"],
            plane["basis_labels_closed"] is True,
            quotient["rank"] == 1,
            quotient["q(H_u)"] == "H",
            quotient["q(H_d^dagger)"] == "H",
            quotient["kernel_generator"] == "H_u - H_d^dagger",
            single["classification"]["is_low_energy_quotient_or_identification"] is True,
        ]
    )

    metric_payload = diagonal_import["rank2_diagonal_HYM_metric"]
    diagonal_metric_candidate_available = all(
        [
            metric_payload["closed"] is True,
            metric_payload["found"] is True,
            metric_payload["metric"] == ["exp(u)", "exp(-u)"],
            metric_payload["nonzero_rank2_strain"] is True,
            metric_payload["continuous_parameters_added"] == 0,
            hym_payload["diagonal_metric_payload"]["closed"] is True,
            hym_payload["curvature_residual_payload"]["closed"] is True,
        ]
    )

    u_min = float(metric_payload["u_min"])
    u_max = float(metric_payload["u_max"])
    u_abs_max = max(abs(u_min), abs(u_max))
    conditional_s_beta_local_max = math.tanh(2.0 * u_abs_max) ** 2
    conditional_s_beta_crosses_zero = u_min <= 0.0 <= u_max

    source_metric_bound_to_E_H_UV = False
    selected_minimal_lift_rule_emitted = False
    direct_Herm2_payload_emitted = False
    finite_Huv_scalar_reduction_emitted = False
    selected_s_beta_value_found = False
    numeric_lambda_H_derived = False

    formal_sequence = {
        "schema": "MTTConstHiggs01H7B1TFormalUVExactSequenceScaffold.v1",
        "status": "FORMAL_UV_EXACT_SEQUENCE_SCAFFOLD_CLOSED_NOT_ACTION_BINDING",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1T-A-FORMAL-UV-EXACT-SEQUENCE",
        "input_sources": {
            "H7B1S_minimal_theorem": rel(h7b1s_minimal_path),
            "H7B1A_single_Higgs_quotient": rel(h7b1a_single_path),
            "H7B1A_splitting_contract": rel(h7b1a_contract_path),
        },
        "closed_formal_scaffold": {
            "ordered_UV_basis": basis,
            "basis_labels_closed": plane["basis_labels_closed"],
            "exact_sequence": contract["exact_sequence"],
            "quotient_rank": quotient["rank"],
            "q_Hu": quotient["q(H_u)"],
            "q_Hd_dagger": quotient["q(H_d^dagger)"],
            "kernel_generator": quotient["kernel_generator"],
            "formal_UV_exact_sequence_scaffold_closed": formal_sequence_closed,
        },
        "not_yet_closed": {
            "same_source_action_binding_to_selected_terminal_source": False,
            "selected_Hermitian_metric_on_plane": plane["selected_metric_on_plane_filled"],
            "selected_horizontal_lift_or_splitting": single["classification"]["selects_horizontal_lift_or_splitting"],
            "selected_light_projector": single["classification"]["is_selected_Hermitian_projector_on_UV_two_Higgs_plane"],
            "selected_s_beta": single["classification"]["emits_s_beta"],
        },
        "theorem_boundary": {
            "what_is_closed": "The formal two-Higgs exact-sequence scaffold E_H^UV -> span(H) is available with ordered basis labels and kernel.",
            "what_is_not_closed": "This scaffold is not yet a source-owned action binding of the selected HYM/End0 metric to E_H^UV and cannot select P_L by itself.",
        },
        **clean_flags(),
    }

    minimal_lift = {
        "schema": "MTTConstHiggs01H7B1TConditionalMetricMinimalLiftFormula.v1",
        "status": "CONDITIONAL_G_MINIMAL_LIFT_FORMULA_PROVED_SOURCE_BINDING_OPEN",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1T-B-CONDITIONAL-METRIC-MINIMAL-LIFT",
        "input_sources": {
            "H7B1D_diagonal_HYM_import": rel(h7b1d_import_path),
            "H7B1D_conditional_Huv_readout": rel(h7b1d_conditional_path),
            "H7B1F_basis_invariant_Huv_functor": rel(h7b1f_functor_path),
            "diagonal_HYM_operator_payload": rel(hym_payload_path),
        },
        "general_positive_diagonal_metric_formula": {
            "metric": "G=diag(g_u,g_d), g_u>0, g_d>0",
            "quotient_constraint": "q(c_u H_u+c_d H_d^dagger)=H, so c_u+c_d=1",
            "minimality": "minimize g_u |c_u|^2 + g_d |c_d|^2 subject to c_u+c_d=1",
            "c_u": "g_d/(g_u+g_d)",
            "c_d": "g_u/(g_u+g_d)",
            "proof": "Lagrange multiplier gives g_u c_u = g_d c_d and c_u+c_d=1.",
            "conditional_formula_proved": True,
        },
        "diagonal_HYM_specialization_if_bound_to_E_H_UV": {
            "metric_candidate": metric_payload["metric"],
            "c_u": "1/(1+exp(2u))",
            "c_d": "exp(2u)/(1+exp(2u))",
            "Euclidean_rank_one_projector_trace_JD": "-tanh(2u)",
            "conditional_local_s_beta": "tanh(2u)^2",
            "u_min": u_min,
            "u_max": u_max,
            "u_abs_max": u_abs_max,
            "conditional_local_s_beta_max_from_current_u_bounds": conditional_s_beta_local_max,
            "conditional_local_s_beta_can_vanish_on_zero_crossing": conditional_s_beta_crosses_zero,
            "finite_scalar_reduction_emitted": finite_Huv_scalar_reduction_emitted,
        },
        "required_before_promotion": {
            "same_source_binds_metric_to_E_H_UV": source_metric_bound_to_E_H_UV,
            "same_source_declares_G_minimal_lift_rule": selected_minimal_lift_rule_emitted,
            "source_emits_finite_scalar_reduction_or_integral_policy": finite_Huv_scalar_reduction_emitted,
            "source_emits_projector_phase_covariance": False,
        },
        "decision": {
            "conditional_minimal_lift_formula_proved": True,
            "selected_minimal_lift_promoted": False,
            "selected_s_beta_promoted": False,
            "reason": "The algebraic lift is now solved once a selected metric and minimal-lift rule are source-bound, but the current packets do not yet emit that binding or the finite reduction.",
        },
        **clean_flags(),
    }

    binding_attempt = {
        "schema": "MTTConstHiggs01H7B1TActualSourceBindingAttempt.v1",
        "status": "ACTUAL_UV_HIGGS_PLANE_BINDING_ATTEMPT_FAILS_SOURCE_BINDING",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1T-C-ACTUAL-SOURCE-BINDING-ATTEMPT",
        "input_sources": {
            "H7B1S_candidate": rel(h7b1s_path),
            "H7B1G_BHuv_payload_request": rel(h7b1g_bhuv_path),
            "H7B1F_Huv_functor": rel(h7b1f_functor_path),
            "H7B1D_diagonal_conditional_readout": rel(h7b1d_conditional_path),
        },
        "H7B1S_minimal_theorem_clauses": h7b1s_minimal["theorem_to_prove_next"]["clauses"],
        "clause_status": {
            "formal_ordered_UV_basis_and_quotient_scaffold_closed": formal_sequence_closed,
            "selected_terminal_source_action_binding_to_E_H_UV_closed": source_metric_bound_to_E_H_UV,
            "selected_diagonal_HYM_metric_candidate_available": diagonal_metric_candidate_available,
            "selected_diagonal_HYM_metric_proven_as_metric_on_E_H_UV": source_metric_bound_to_E_H_UV,
            "same_source_minimal_lift_rule_emitted": selected_minimal_lift_rule_emitted,
            "same_source_rank_one_projector_emitted": False,
            "direct_Herm2_Huv_payload_emitted": direct_Herm2_payload_emitted,
            "finite_Huv_reduction_exactness_certificate_emitted": finite_Huv_scalar_reduction_emitted,
            "no_measured_Higgs_or_beta_selector_used": True,
        },
        "actual_outputs": {
            "B_Huv": None,
            "M_source": None,
            "Huu": None,
            "Hud": None,
            "Hdd": None,
            "P_L": None,
            "s_beta": None,
            "lambda_H": None,
        },
        "why_not_closed": {
            "H7B1D_required_A1_basis_binding": diagonal_conditional["conditional_assumptions_required"]["A1_two_Higgs_basis_binding"],
            "H7B1D_required_A2_finite_reduction": diagonal_conditional["conditional_assumptions_required"]["A2_finite_scalar_reduction"],
            "H7B1G_BHuv_current_payload_emitted": bhuv_request["acceptance_tests"]["current_payload_emitted"],
            "H7B1F_functor_conditional_values_open": huv_functor["conditional_values_open"],
        },
        "decision": {
            "UV_Higgs_plane_binding_closed": False,
            "H7B1T_closes_formal_scaffold_and_conditional_formula_only": True,
            "strict_no_knob_Higgs_closure": False,
        },
        **clean_flags(),
    }

    no_cycle = {
        "schema": "MTTConstHiggs01H7B1TNonCirculationLedger.v1",
        "status": "NO_CIRCULATION_LEDGER_UPDATED_H7B1T",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1T-NO-CYCLE",
        "retired_or_do_not_reopen": {
            "quotient_map_q_alone_selects_projector": True,
            "diagonal_HYM_metric_without_binding_is_Huv": True,
            "first_C1_row_as_Huv_row": True,
            "lambda12_as_lambda_H": True,
        },
        "new_information_added": [
            "formal UV exact sequence scaffold is separated from source action binding",
            "G-minimal lift formula is proved for any positive diagonal metric on E_H^UV",
            "diagonal HYM specialization gives conditional local s_beta=tanh(2u)^2",
            "finite scalar reduction and source-bound metric/lift remain explicit blockers",
        ],
        "active_not_retired": {
            "same_source_metric_binding_to_E_H_UV": True,
            "source_emitted_minimal_lift_policy": True,
            "finite_reduction_or_direct_Herm2_Huv_rows": True,
            "EW_boundary_RG_after_s_beta": True,
        },
        "circulation_test": {
            "is_reopening_H7B1A_underdetermination": False,
            "is_reopening_H7B1D_conditional_diagonal_endpoint": False,
            "is_promoting_conditional_formula_as_value": False,
            "is_using_observed_lambda_or_tan_beta": False,
        },
        **clean_flags(),
    }

    next_work = {
        "schema": "MTTConstHiggs01H7B1TNextWork.v1",
        "status": "NEXT_WORKORDER_H7B1U_SOURCE_BOUND_METRIC_AND_FINITE_REDUCTION",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1T-NEXT",
        "primary_next": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1U-SOURCE-BOUND-METRIC-AND-FINITE-REDUCTION",
            "task": "Emit a same-source certificate binding the selected diagonal HYM metric/action to E_H^UV and either declare the G-minimal lift rule plus finite reduction, or emit direct Herm(2) Huv rows.",
        },
        "legal_exits": [
            {
                "id": "H7B1U-A",
                "label": "source-bound metric plus G-minimal lift",
                "must_emit": "metric binding to E_H^UV, selected G-minimal lift policy, projector covariance, finite reduction for s_beta",
            },
            {
                "id": "H7B1U-B",
                "label": "direct Herm2 Huv payload",
                "must_emit": "B_Huv+M_source or Huu,Hud,Hdd with exactness/residual certificate",
            },
        ],
        "superset_strategy": {
            "using_one_straight_way": False,
            "combining_paths": True,
            "straight_path": "formal UV quotient exact sequence plus selected diagonal HYM metric candidate",
            "support_path": "basis-invariant Huv functor and B_Huv request used as locked acceptance target",
            "locked_target": "source-owned metric/lift or Herm(2) Huv payload, not fitted beta or measured lambda_H",
        },
        **clean_flags(),
    }

    theorem = {
        "name": "H7B1TFormalSequenceAndMinimalLiftFormulaTheorem",
        "proved": True,
        "statement": (
            "H7B1T closes the formal UV Higgs exact-sequence scaffold and the conditional metric-minimal-lift algebra. The q79 quotient supplies E_H^UV=span(H_u,H_d^dagger), q(H_u)=q(H_d^dagger)=H, and Ker(q)=span(H_u-H_d^dagger). For any positive diagonal metric G=diag(g_u,g_d) on this plane, the G-minimal lift of H is sigma_G(H)=g_d/(g_u+g_d) H_u + g_u/(g_u+g_d) H_d^dagger. If the selected diagonal HYM metric diag(exp(u),exp(-u)) is later source-bound to E_H^UV and the G-minimal rule is source-selected, the conditional local D-term invariant is s_beta(u)=tanh(2u)^2. Current packets do not yet emit the source binding, finite scalar reduction, B_Huv, M_source, direct Huv rows, selected s_beta, or lambda_H."
        ),
    }

    candidate = {
        "candidate": "MTTConstHiggs01H7B1TUVHiggsPlaneBindingOrMinimalLiftTheorem",
        "status": STATUS,
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1T-UV-HIGGS-PLANE-BINDING-OR-MINIMAL-LIFT-THEOREM",
        "output_packets": {
            "formal_uv_exact_sequence_scaffold": rel(FORMAL_SEQUENCE),
            "conditional_metric_minimal_lift_formula": rel(MINIMAL_LIFT),
            "actual_source_binding_attempt": rel(BINDING_ATTEMPT),
            "non_circulation_ledger": rel(NO_CYCLE),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": theorem,
        "H7B1S_imported": h7b1s["status"] == "MTT_CONST_HIGGS_01_H7B1S_NEARHITS_TESTED_UV_HIGGS_PLANE_BINDING_OPEN",
        "formal_UV_exact_sequence_scaffold_closed": formal_sequence_closed,
        "conditional_G_minimal_lift_formula_proved": True,
        "diagonal_HYM_metric_candidate_available": diagonal_metric_candidate_available,
        "source_metric_bound_to_E_H_UV": source_metric_bound_to_E_H_UV,
        "selected_minimal_lift_rule_emitted": selected_minimal_lift_rule_emitted,
        "finite_Huv_scalar_reduction_emitted": finite_Huv_scalar_reduction_emitted,
        "direct_Herm2_Huv_payload_emitted": direct_Herm2_payload_emitted,
        "B_Huv_value_emitted": False,
        "M_source_value_emitted": False,
        "direct_Huv_entries_emitted": False,
        "selected_s_beta_value_found": selected_s_beta_value_found,
        "numeric_lambda_H_derived": numeric_lambda_H_derived,
        "strict_no_knob_Higgs_closure": False,
        "new_Higgs_specific_parameters": 0,
        "selected_next_artifact": "MTT_CONST_HIGGS_01_H7B1U_SourceBoundMetricAndFiniteReduction_v1",
        **clean_flags(),
    }

    cert = {
        "certificate": "MTT_CONST_HIGGS_01_H7B1T_UVHiggsPlaneBindingOrMinimalLiftTheorem_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "active_label": candidate["active_label"],
        "formal_UV_exact_sequence_scaffold_closed": formal_sequence_closed,
        "conditional_G_minimal_lift_formula_proved": True,
        "diagonal_HYM_metric_candidate_available": diagonal_metric_candidate_available,
        "source_metric_bound_to_E_H_UV": source_metric_bound_to_E_H_UV,
        "selected_minimal_lift_rule_emitted": selected_minimal_lift_rule_emitted,
        "finite_Huv_scalar_reduction_emitted": finite_Huv_scalar_reduction_emitted,
        "selected_s_beta_value_found": selected_s_beta_value_found,
        "numeric_lambda_H_derived": numeric_lambda_H_derived,
        "strict_no_knob_Higgs_closure": False,
        "new_Higgs_specific_parameters": 0,
        **clean_flags(),
    }

    note = f"""# MTT CONST HIGGS 01 H7B1T UV Higgs Plane Binding Or Minimal Lift Theorem v1

Status: `{STATUS}`

Label: `CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1T-UV-HIGGS-PLANE-BINDING-OR-MINIMAL-LIFT-THEOREM`

## Result

```text
formal UV exact-sequence scaffold closed        {formal_sequence_closed}
conditional G-minimal lift formula proved       True
diagonal HYM metric candidate available         {diagonal_metric_candidate_available}
source metric bound to E_H^UV                   {source_metric_bound_to_E_H_UV}
selected minimal-lift rule emitted              {selected_minimal_lift_rule_emitted}
finite Huv scalar reduction emitted             {finite_Huv_scalar_reduction_emitted}
B_Huv / M_source / direct Huv emitted           False
s_beta / lambda_H promoted                      False
```

## What Moved Forward

H7B1T separates the problem cleanly.  The formal UV Higgs exact sequence is now
closed as a scaffold:

`0 -> Ker(q)=span(H_u-H_d^dagger) -> E_H^UV -> span(H) -> 0`.

It also proves the conditional metric-minimal lift formula.  For
`G=diag(g_u,g_d)`, the `G`-minimal lift of `H` is

`sigma_G(H)=g_d/(g_u+g_d) H_u + g_u/(g_u+g_d) H_d^dagger`.

If the selected diagonal HYM metric `diag(exp(u),exp(-u))` is later bound by
the same source to `E_H^UV`, this gives the conditional local invariant

`s_beta(u)=tanh(2u)^2`.

## Remaining Boundary

This is still not Higgs closure.  The missing object is now narrower:

`SelectedSourceBoundMetricAndFiniteReductionTheorem`

It must emit the same-source binding of the selected metric/action to
`E_H^UV`, declare the minimal-lift or projector policy, and provide a finite
reduction or direct `Herm(2)` Huv rows.

Next label:

`CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1U-SOURCE-BOUND-METRIC-AND-FINITE-REDUCTION`
"""

    for path, payload in [
        (FORMAL_SEQUENCE, formal_sequence),
        (MINIMAL_LIFT, minimal_lift),
        (BINDING_ATTEMPT, binding_attempt),
        (NO_CYCLE, no_cycle),
        (NEXT_WORK, next_work),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        write_json(path, payload)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
