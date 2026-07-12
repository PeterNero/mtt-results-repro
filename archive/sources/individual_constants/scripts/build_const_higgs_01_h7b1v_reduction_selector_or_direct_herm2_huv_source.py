"""Build CONST-HIGGS-01 H7B1V reduction selector or direct Herm2 Huv source gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
SM_PARITY = TEXPAPERS / "mtt-sm-parity-closure"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_higgs_01_h7b1v_reduction_selector_or_direct_herm2_huv_source"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
REDUCTION_SELECTOR = BASE / "reduction_selector_triage.packet.json"
TRACE_BINDING = BASE / "finite_trace_to_hym_grid_binding_attempt.packet.json"
DIRECT_HERM2 = BASE / "direct_herm2_huv_source_attempt.packet.json"
NO_CYCLE = BASE / "non_circulation_ledger.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_HIGGS_01_H7B1V_ReductionSelectorOrDirectHerm2HuvSource_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7B1V_TRACE_SELECTOR_TRIAGED_BINDING_OPEN"


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

    h7b1u_path = DATA / "const_higgs_01_h7b1u_source_bound_metric_and_finite_reduction.candidate.json"
    h7b1u_reduction_path = DATA / "const_higgs_01_h7b1u_source_bound_metric_and_finite_reduction" / "conditional_finite_reduction_execution.packet.json"
    h7b1u_direct_path = DATA / "const_higgs_01_h7b1u_source_bound_metric_and_finite_reduction" / "direct_herm2_payload_attempt.packet.json"
    finite_weyl_path = SM_PARITY / "candidate_data" / "selected_finiteweyl_traceuniqueness_or_physicalboundarysource_derivation.candidate.json"
    trace_payload_path = SM_PARITY / "candidate_data" / "selected_tracepayload_or_fullhymoperatoremission.candidate.json"
    c1_trace_path = SM_PARITY / "candidate_data" / "selected_c1tracemeasurepromotion_or_actionboundaryproof.candidate.json"

    h7b1u = load(h7b1u_path)
    h7b1u_reduction = load(h7b1u_reduction_path)
    h7b1u_direct = load(h7b1u_direct_path)
    finite_weyl = load(finite_weyl_path)
    trace_payload = load(trace_payload_path)
    c1_trace = load(c1_trace_path)

    values = h7b1u_reduction["conditional_reduction_candidates_not_selected"]
    finite_weyl_trace_derived = finite_weyl["what_closes_now"]["finite_Weyl_invariant_trace_measure_derived"]
    trace_payload_layer_closed = trace_payload["what_closes_now"]["transition_rhoE_or_Cech_Dolbeault_DE_data"]
    physical_measure_promoted = c1_trace["promotion_decision"]["selected_measure_promoted_as_physical"]
    trace_to_HYM_grid_binding_closed = False
    source_metric_bound_to_E_H_UV = h7b1u["source_metric_bound_to_E_H_UV"]
    selected_reduction_selector_emitted = False
    direct_herm2_payload_emitted = False

    reduction_selector = {
        "schema": "MTTConstHiggs01H7B1VReductionSelectorTriage.v1",
        "status": "REDUCTION_SELECTOR_TRIAGED_UNIFORM_SUPPORT_BINDING_OPEN",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1V-A-REDUCTION-SELECTOR-TRIAGE",
        "input_sources": {
            "H7B1U_conditional_reduction": rel(h7b1u_reduction_path),
            "finite_Weyl_trace_uniqueness": rel(finite_weyl_path),
            "selected_trace_payload": rel(trace_payload_path),
            "C1_trace_measure_promotion": rel(c1_trace_path),
        },
        "candidate_reductions": {
            "uniform_mean": {
                "value": values["uniform_mean"],
                "support": "matches normalized finite trace/Frobenius intuition if the HYM grid is the selected finite trace discretization",
                "finite_Weyl_trace_support": finite_weyl_trace_derived,
                "trace_to_HYM_grid_binding_closed": trace_to_HYM_grid_binding_closed,
                "promoted": False,
            },
            "rho_weighted_mean": {
                "value": values["rho_weighted_mean"],
                "support": "uses selected eta_00 density rho as a diagnostic weight",
                "projection_measure_theorem_emitted": False,
                "promoted": False,
            },
            "exp_density_weighted_mean": {
                "value": values["exp_density_weighted_mean"],
                "support": "uses the nonlinear HYM equation density rho*exp(-2u) as a diagnostic weight",
                "projection_measure_theorem_emitted": False,
                "promoted": False,
            },
        },
        "selector_decision": {
            "finite_Weyl_normalized_trace_measure_derived": finite_weyl_trace_derived,
            "selected_trace_payload_DE_gap_layer_closed": trace_payload_layer_closed,
            "physical_measure_promoted_as_Higgs_projection": False,
            "uniform_reduction_best_current_source_aligned_candidate": True,
            "selected_reduction_selector_emitted": selected_reduction_selector_emitted,
            "selected_s_beta_promoted": False,
            "reason": "Finite Weyl trace uniqueness supports normalized/uniform finite trace only after the HYM grid is identified with the selected finite trace quotient. Current artifacts do not emit that trace-to-grid/Higgs projection binding.",
        },
        **clean_flags(),
    }

    trace_binding = {
        "schema": "MTTConstHiggs01H7B1VFiniteTraceToHYMGridBindingAttempt.v1",
        "status": "FINITE_TRACE_TO_HYM_GRID_BINDING_ATTEMPT_OPEN",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1V-B-FINITE-TRACE-TO-HYM-GRID-BINDING",
        "closed_support": {
            "finite_Weyl_trace_measure_derived": finite_weyl_trace_derived,
            "selected_trace_payload_DE_gap_layer_closed": trace_payload_layer_closed,
            "H7B1U_grid_replay_matches_stored_certificate": h7b1u["grid_replay_matches_stored_certificate"],
            "conditional_finite_reduction_executable": h7b1u["conditional_finite_reduction_executable"],
        },
        "blocked_fields": {
            "trace_to_HYM_grid_binding_closed": trace_to_HYM_grid_binding_closed,
            "same_source_metric_bound_to_E_H_UV": source_metric_bound_to_E_H_UV,
            "physical_measure_equals_Higgs_projection_measure": physical_measure_promoted,
            "same_source_no_extra_boundary_or_source_term": c1_trace["what_remains_open"]["absence_of_extra_physical_boundary_or_source_term"] is False,
        },
        "minimal_binding_theorem_needed": {
            "name": "SelectedFiniteTraceHYMGridHiggsProjectionBindingTheorem",
            "clauses": [
                "identify the H7B1U HYM grid quadrature with the selected finite trace/Frobenius quotient",
                "prove the bound metric is the metric on E_H^UV, not only End0 T3 support",
                "prove the Higgs projection/reduction measure is normalized trace rather than rho or exp-density weighted",
                "exclude extra physical boundary/source terms and observed Higgs/beta selectors",
            ],
        },
        "decision": {
            "uniform_mean_can_be_promoted_now": False,
            "trace_to_HYM_grid_binding_closed": trace_to_HYM_grid_binding_closed,
            "reason": "The uniform mean is the best trace-aligned candidate, but the required trace-to-HYM-grid and E_H^UV metric bindings are not emitted.",
        },
        **clean_flags(),
    }

    direct_herm2 = {
        "schema": "MTTConstHiggs01H7B1VDirectHerm2HuvSourceAttempt.v1",
        "status": "DIRECT_HERM2_HUV_SOURCE_ATTEMPT_STILL_OPEN",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1V-C-DIRECT-HERM2-HUV-SOURCE",
        "input_sources": {
            "H7B1U_direct_Herm2_attempt": rel(h7b1u_direct_path),
        },
        "payload_status": {
            "conditional_functor_ready": h7b1u_direct["conditional_functor_ready"],
            "B_Huv_request_ready": h7b1u_direct["payload_requests_ready"]["B_Huv_request_ready"],
            "M_source_request_ready": h7b1u_direct["payload_requests_ready"]["M_source_request_ready"],
            "B_Huv_value_emitted": False,
            "M_source_value_emitted": False,
            "direct_Huu_Hud_Hdd_emitted": False,
        },
        "actual_outputs": h7b1u_direct["actual_outputs"],
        "decision": {
            "direct_Herm2_Huv_payload_emitted": direct_herm2_payload_emitted,
            "selected_s_beta_promoted": False,
            "numeric_lambda_H_derived": False,
        },
        **clean_flags(),
    }

    no_cycle = {
        "schema": "MTTConstHiggs01H7B1VNonCirculationLedger.v1",
        "status": "NO_CIRCULATION_LEDGER_UPDATED_H7B1V",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1V-NO-CYCLE",
        "retired_or_do_not_reopen": {
            "conditional_reduction_values_as_selected_s_beta": True,
            "finite_Weyl_trace_measure_as_HYM_grid_binding_without_theorem": True,
            "rho_density_weight_as_Higgs_projection_without_theorem": True,
            "direct_Herm2_functor_as_values_without_payload": True,
        },
        "new_information_added": [
            "finite Weyl trace uniqueness is imported as support for the uniform candidate",
            "uniform mean is ranked as the best trace-aligned candidate but not promoted",
            "rho and exp-density weights are explicitly classified as diagnostics without projection-measure theorems",
            "the next missing object is trace-to-HYM-grid/Higgs projection binding or direct Herm2 payload",
        ],
        "active_not_retired": {
            "trace_to_HYM_grid_binding": True,
            "source_metric_binding_to_E_H_UV": True,
            "direct_Herm2_Huv_rows": True,
            "EW_boundary_RG_after_selected_s_beta": True,
        },
        "circulation_test": {
            "is_reopening_H7B1U_grid_replay": False,
            "is_promoting_uniform_mean_without_binding": False,
            "is_using_measured_Higgs_or_beta": False,
            "is_reusing_C1_trace_as_Higgs_measure_without_projection": False,
        },
        **clean_flags(),
    }

    next_work = {
        "schema": "MTTConstHiggs01H7B1VNextWork.v1",
        "status": "NEXT_WORKORDER_H7B1W_FINITE_TRACE_HYM_BINDING_OR_DIRECT_HUV_PAYLOAD",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1V-NEXT",
        "primary_next": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1W-FINITE-TRACE-HYM-BINDING-OR-DIRECT-HUV-PAYLOAD",
            "task": "Prove the selected finite trace/Frobenius measure is the H7B1U HYM-grid Higgs projection measure, or emit direct B_Huv+M_source/Huu,Hud,Hdd.",
        },
        "legal_exits": [
            {
                "id": "H7B1W-A",
                "label": "finite trace to HYM-grid projection binding",
                "must_emit": "same-source trace-to-grid quadrature identity, E_H^UV metric binding, and no-extra-boundary/source proof",
            },
            {
                "id": "H7B1W-B",
                "label": "direct Herm2 Huv source payload",
                "must_emit": "B_Huv+M_source or direct Huu,Hud,Hdd with exactness/residual certificate",
            },
        ],
        "superset_strategy": {
            "using_one_straight_way": False,
            "combining_paths": True,
            "straight_path": "finite Weyl trace uniqueness plus H7B1U HYM grid replay",
            "support_path": "direct Herm2 Huv functor remains alternative exit",
            "locked_target": "source-selected Higgs projection measure or direct Huv payload, not a fitted Higgs quartic",
        },
        **clean_flags(),
    }

    theorem = {
        "name": "H7B1VReductionSelectorTriageTheorem",
        "proved": True,
        "statement": (
            "H7B1V imports the finite Weyl trace uniqueness theorem and tests it against the H7B1U conditional reductions. The normalized finite trace supports the uniform mean as the best source-aligned candidate, while rho-weighted and exp-density-weighted means remain diagnostic density choices without a Higgs projection-measure theorem. No reduction is selected, because the finite Weyl trace quotient has not been identified with the H7B1U HYM grid measure or the E_H^UV Higgs projection. Direct Herm(2) Huv payloads remain un-emitted."
        ),
    }

    candidate = {
        "candidate": "MTTConstHiggs01H7B1VReductionSelectorOrDirectHerm2HuvSource",
        "status": STATUS,
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1V-REDUCTION-SELECTOR-OR-DIRECT-HERM2-HUV-SOURCE",
        "output_packets": {
            "reduction_selector_triage": rel(REDUCTION_SELECTOR),
            "finite_trace_to_hym_grid_binding_attempt": rel(TRACE_BINDING),
            "direct_herm2_huv_source_attempt": rel(DIRECT_HERM2),
            "non_circulation_ledger": rel(NO_CYCLE),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": theorem,
        "H7B1U_imported": h7b1u["status"] == "MTT_CONST_HIGGS_01_H7B1U_CONDITIONAL_REDUCTION_EXECUTED_SOURCE_REDUCTION_OPEN",
        "finite_Weyl_trace_measure_derived": finite_weyl_trace_derived,
        "selected_trace_payload_DE_gap_layer_closed": trace_payload_layer_closed,
        "uniform_reduction_best_current_source_aligned_candidate": True,
        "uniform_mean_conditional_s_beta": values["uniform_mean"],
        "rho_weighted_mean_conditional_s_beta": values["rho_weighted_mean"],
        "exp_density_weighted_mean_conditional_s_beta": values["exp_density_weighted_mean"],
        "trace_to_HYM_grid_binding_closed": trace_to_HYM_grid_binding_closed,
        "source_metric_bound_to_E_H_UV": source_metric_bound_to_E_H_UV,
        "selected_reduction_selector_emitted": selected_reduction_selector_emitted,
        "direct_Herm2_Huv_payload_emitted": direct_herm2_payload_emitted,
        "B_Huv_value_emitted": False,
        "M_source_value_emitted": False,
        "direct_Huv_entries_emitted": False,
        "selected_s_beta_value_found": False,
        "numeric_lambda_H_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "new_Higgs_specific_parameters": 0,
        "selected_next_artifact": "MTT_CONST_HIGGS_01_H7B1W_FiniteTraceHYMBindingOrDirectHuvPayload_v1",
        **clean_flags(),
    }

    cert = {
        "certificate": "MTT_CONST_HIGGS_01_H7B1V_ReductionSelectorOrDirectHerm2HuvSource_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "active_label": candidate["active_label"],
        "finite_Weyl_trace_measure_derived": finite_weyl_trace_derived,
        "uniform_reduction_best_current_source_aligned_candidate": True,
        "uniform_mean_conditional_s_beta": values["uniform_mean"],
        "trace_to_HYM_grid_binding_closed": trace_to_HYM_grid_binding_closed,
        "selected_reduction_selector_emitted": selected_reduction_selector_emitted,
        "direct_Herm2_Huv_payload_emitted": direct_herm2_payload_emitted,
        "selected_s_beta_value_found": False,
        "numeric_lambda_H_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "new_Higgs_specific_parameters": 0,
        **clean_flags(),
    }

    note = f"""# MTT CONST HIGGS 01 H7B1V Reduction Selector Or Direct Herm2 Huv Source v1

Status: `{STATUS}`

Label: `CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1V-REDUCTION-SELECTOR-OR-DIRECT-HERM2-HUV-SOURCE`

## Result

```text
finite Weyl trace measure derived             {finite_weyl_trace_derived}
uniform reduction best trace-aligned candidate True
trace-to-HYM-grid binding closed              {trace_to_HYM_grid_binding_closed}
source metric bound to E_H^UV                 {source_metric_bound_to_E_H_UV}
selected reduction selector emitted           {selected_reduction_selector_emitted}
B_Huv / M_source / direct Huv emitted         False
s_beta / lambda_H promoted                    False
```

## Reduction Triage

H7B1V imports finite Weyl trace uniqueness.  This makes the H7B1U uniform mean
the best current source-aligned candidate:

```text
uniform mean                       {values["uniform_mean"]:.18g}
rho-weighted mean                  {values["rho_weighted_mean"]:.18g}
exp-density-weighted mean          {values["exp_density_weighted_mean"]:.18g}
```

But this is still not a selected Higgs value.  The finite Weyl trace lives on
the finite C1/Weyl quotient.  The H7B1U values live on the replayed diagonal HYM
grid.  We still need a same-source theorem identifying the HYM-grid Higgs
projection measure with that finite trace.

## Remaining Boundary

The next theorem is:

`SelectedFiniteTraceHYMGridHiggsProjectionBindingTheorem`

It must bind the finite trace/Frobenius measure to the H7B1U HYM grid and to
`E_H^UV`, or the branch must instead emit direct `B_Huv+M_source` /
`Huu,Hud,Hdd` payload.

Next label:

`CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1W-FINITE-TRACE-HYM-BINDING-OR-DIRECT-HUV-PAYLOAD`
"""

    for path, payload in [
        (REDUCTION_SELECTOR, reduction_selector),
        (TRACE_BINDING, trace_binding),
        (DIRECT_HERM2, direct_herm2),
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
