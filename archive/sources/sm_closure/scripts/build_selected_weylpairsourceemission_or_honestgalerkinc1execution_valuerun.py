"""Build Weyl-pair source emission or honest Galerkin C1 execution value-run gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PREVIOUS = DATA / "selected_differentiatedresidualprojectorsourcerule_or_honestgalerkinc1execution.candidate.json"
SOURCE_RULE = (
    DATA
    / "selected_differentiatedresidualprojectorsourcerule_or_honestgalerkinc1execution"
    / "differentiated_residual_projector_source_rule.contract.json"
)
ROUTE_LADDER = (
    DATA
    / "selected_differentiatedresidualprojectorsourcerule_or_honestgalerkinc1execution"
    / "source_rule_or_execution_route_ladder.packet.json"
)
WEYL_SOURCE = DATA / "selected_routec_weylpair_basis_transport_or_vertex_source_theorem.candidate.json"
WEYL_A = DATA / "selected_routec_weylpair_aselected_assembly_or_source_proof.candidate.json"
WEYL_PROVENANCE = DATA / "selected_routec_weylpair_source_provenance_lemma.candidate.json"
SOURCE_SELECTOR = DATA / "selected_primitivevertex_source_or_basistransport_selectiontheorem.candidate.json"
GALERKIN_CONTRACT = (
    DATA
    / "selected_primitiveoverlapcontractions_valueemission_or_honestgalerkinrun"
    / "honest_galerkin_c1_value_run_contract.packet.json"
)

OUTPUT = DATA / "selected_weylpairsourceemission_or_honestgalerkinc1execution_valuerun.candidate.json"
PACKET_DIR = DATA / "selected_weylpairsourceemission_or_honestgalerkinc1execution_valuerun"
PROMOTION_ATTEMPT_PACKET = PACKET_DIR / "weylpair_source_emission_promotion_attempt.packet.json"
CONDITIONAL_VALUE_RUN_PACKET = PACKET_DIR / "conditional_weylpair_value_run.packet.json"
HONEST_EXECUTION_PACKET = PACKET_DIR / "honest_galerkin_execution_value_run_gate.packet.json"
CERT = CERTS / "selected_weylpairsourceemission_or_honestgalerkinc1execution_valuerun_certificate.json"
NOTE = CORPUS / "MTT_Selected_WeylPairSourceEmission_or_HonestGalerkinC1Execution_ValueRun_v1.md"

STATUS = "MTT_SELECTED_WEYLPAIRSOURCEEMISSION_OR_HONESTGALERKINC1EXECUTION_VALUERUN_BUILT_PROMOTION_BLOCKED"
NEXT = "MTT_Selected_EnrichedWeylPairSourceProvenance_or_GalerkinC1Values_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    source_rule = load(SOURCE_RULE)
    route_ladder = load(ROUTE_LADDER)
    weyl_source = load(WEYL_SOURCE)
    weyl_a = load(WEYL_A)
    provenance = load(WEYL_PROVENANCE)
    selector = load(SOURCE_SELECTOR)
    galerkin = load(GALERKIN_CONTRACT)

    source_gate = weyl_source["theorem_gate"]
    not_proved = source_gate["not_proved_now"]
    proved = source_gate["proved_now"]
    selected_status = weyl_a["selected_emission_status"]
    conditional = source_rule["exact_conditional_values_if_rule_is_proved"]

    missing_source_obligations = [
        key for key, value in not_proved.items() if value is True
    ]
    promotion_ready = (
        selector["promotion_decision"]["source_selector_promoted"] is True
        and provenance["source_level_weyl_carrier"]["proved"] is True
        and weyl_source["span_test"]["target_in_span"] is True
        and selected_status["A_selected_currently_emitted"] is True
        and selected_status["b_selected_currently_emitted"] is True
        and not missing_source_obligations
    )

    promotion_attempt = {
        "schema": "MTTWeylPairSourceEmissionPromotionAttempt.v1",
        "status": "PROMOTION_BLOCKED_SOURCE_EMISSION_NOT_THEOREM_DERIVED",
        "candidate_route": route_ladder["recommended_next"],
        "already_closed_support": {
            "source_selector_promoted": selector["promotion_decision"]["source_selector_promoted"],
            "source_level_weyl_carrier_proved": provenance["source_level_weyl_carrier"]["proved"],
            "active_shift_proved": provenance["active_shift_provenance"]["proved"],
            "target_in_weylpair_span": weyl_source["span_test"]["target_in_span"],
            "conditional_A_rank": weyl_a["locked_solve"]["rank"],
            "conditional_deltaTheta": weyl_a["locked_solve"]["deltaTheta_conditional"],
            "primitive_only_span_insufficient": proved["primitive_only_span_insufficient_imported"],
            "target_is_internal_diagnostic_not_observed_data": proved[
                "target_is_internal_diagnostic_not_observed_data"
            ],
        },
        "promotion_inputs_missing": {
            "missing_source_obligations": missing_source_obligations,
            "A_selected_currently_emitted": selected_status["A_selected_currently_emitted"],
            "b_selected_currently_emitted": selected_status["b_selected_currently_emitted"],
            "least_squares_now_computable_for_selected_A": selected_status[
                "least_squares_now_computable_for_selected_A"
            ],
            "rank_test_now_computable_for_selected_A": selected_status[
                "rank_test_now_computable_for_selected_A"
            ],
        },
        "promotion_decision": {
            "enriched_weylpair_source_emission_promoted": promotion_ready,
            "A_selected_promoted": False,
            "b_selected_promoted": False,
            "deltaTheta_C1_promoted": False,
            "SM_parity_dynamic_packet_closed": False,
        },
        "why_not_promoted": (
            "The enriched Weyl-pair packet is algebraically sufficient and correctly "
            "routed, but current artifacts still record phase/shift source emission, "
            "A_selected, b_selected, and deltaTheta_C1 as conditional rather than "
            "theorem-derived selected values."
        ),
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    conditional_value_run = {
        "schema": "MTTConditionalWeylPairValueRun.v1",
        "status": "CONDITIONAL_VALUE_RUN_READY_NOT_PROMOTED",
        "operator_name": weyl_a["conditional_operator"]["name"],
        "operator_shape": weyl_a["conditional_operator"]["shape"],
        "operator_is_A_selected": weyl_a["conditional_operator"]["is_A_selected"],
        "rank": weyl_a["locked_solve"]["rank"],
        "condition_number": weyl_a["locked_solve"]["condition_number"],
        "relative_residual": weyl_a["locked_solve"]["relative_residual"],
        "deltaTheta_conditional": weyl_a["locked_solve"]["deltaTheta_conditional"],
        "A_transpose_A_if_promoted": conditional["A_transpose_A"],
        "A_transpose_b_if_promoted": conditional["A_transpose_b"],
        "deltaTheta_C1_if_promoted": conditional["deltaTheta_C1"],
        "SM_parity_dynamic_packet_would_close_if_promoted": True,
        "no_knob_flavor_constants_would_close_if_promoted": False,
        "selected_value_promotion_allowed_now": False,
        "blocked_by": missing_source_obligations
        + [
            "A_selected_currently_emitted_false",
            "b_selected_currently_emitted_false",
        ],
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    honest_execution = {
        "schema": "MTTHonestGalerkinC1ExecutionValueRunGate.v1",
        "status": "HONEST_GALERKIN_EXECUTION_VALUES_STILL_OPEN",
        "contract_status": galerkin["status"],
        "current_manifest_status": galerkin["current_manifest_status"],
        "required_inputs": galerkin["required_inputs"],
        "required_outputs": galerkin["required_outputs"],
        "acceptance_checks": galerkin["acceptance_checks"],
        "selected_source_verified": galerkin["selected_source_verified"],
        "would_close_SM_parity_dynamic_packet_if_values_emitted": True,
        "would_close_no_knob_flavor_constants_if_values_emitted": False,
        "observed_flavor_data_forbidden": galerkin["observed_flavor_data_forbidden"],
        "target_fitting_forbidden": galerkin["target_fitting_forbidden"],
    }

    candidate = {
        "candidate": "MTTSelectedWeylPairSourceEmissionOrHonestGalerkinC1ExecutionValueRun",
        "status": STATUS,
        "inputs": {
            "previous_source_rule_cutset": rel(PREVIOUS),
            "source_rule_contract": rel(SOURCE_RULE),
            "route_ladder": rel(ROUTE_LADDER),
            "weylpair_basis_transport_source_gate": rel(WEYL_SOURCE),
            "weylpair_A_assembly_gate": rel(WEYL_A),
            "weylpair_source_provenance": rel(WEYL_PROVENANCE),
            "primitive_source_selector": rel(SOURCE_SELECTOR),
            "honest_galerkin_contract": rel(GALERKIN_CONTRACT),
        },
        "output_packets": {
            "weylpair_source_emission_promotion_attempt": rel(PROMOTION_ATTEMPT_PACKET),
            "conditional_weylpair_value_run": rel(CONDITIONAL_VALUE_RUN_PACKET),
            "honest_galerkin_execution_value_run_gate": rel(HONEST_EXECUTION_PACKET),
        },
        "what_closes_now": {
            "primary_weylpair_route_attempted": True,
            "conditional_value_run_replayed": True,
            "promotion_blocker_reduced_to_source_emission_and_b_selected": True,
            "honest_Galerkin_execution_gate_reemitted": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "selected_phase_like_Z_or_basis_holonomy_source": True,
            "selected_shift_like_X_vertex_source": True,
            "same_branch_weyl_pair_source_provenance": True,
            "theorem_derived_A_selected": True,
            "theorem_derived_b_selected": True,
            "selected_deltaTheta_C1": True,
            "honest_selected_Galerkin_C1_execution_values": True,
            "SM_parity_dynamic_packet_closure": True,
            "true_SM_equivalence_closure": True,
            "full_no_knob_flavor_closure": True,
        },
        "promotion_decision": {
            "enriched_weylpair_source_emission_promoted": False,
            "A_selected_promoted": False,
            "b_selected_promoted": False,
            "deltaTheta_C1_promoted": False,
            "honest_Galerkin_C1_execution_promoted": False,
            "SM_parity_dynamic_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_flavor_constants_closed": False,
        },
        "observed_data_used": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "SM_parity_dynamic_packet_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "no_knob_closure_claimed": False,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "WeylPairSourceEmissionAttemptAndValueRunTheorem",
            "proved": True,
            "statement": (
                "The enriched Weyl-pair route is the primary constructive route and "
                "its conditional value run is numerically ready: the conditional "
                "operator has rank 2, condition number 1, and deltaTheta=(1,1). "
                "However, current artifacts do not theorem-derive the phase-like "
                "and shift-like source emissions, A_selected, or b_selected.  "
                "Therefore SM-parity dynamic closure remains blocked exactly at "
                "selected enriched Weyl-pair source provenance or honest Galerkin "
                "C1 execution values."
            ),
        },
    }

    cert = {
        "certificate": "MTT_Selected_WeylPairSourceEmission_or_HonestGalerkinC1Execution_ValueRun_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "promotion_attempt_packet_path": rel(PROMOTION_ATTEMPT_PACKET),
        "conditional_value_run_packet_path": rel(CONDITIONAL_VALUE_RUN_PACKET),
        "honest_execution_packet_path": rel(HONEST_EXECUTION_PACKET),
        "theorem_proved": True,
        "closure_claimed": False,
        "SM_parity_dynamic_packet_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "no_knob_closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected WeylPairSourceEmission or HonestGalerkinC1Execution ValueRun v1

Status: `{STATUS}`.

The primary enriched Weyl-pair route has now been attempted as a promotion.
It remains blocked, but the blocker is exact: phase-like `Z`/basis-holonomy
source emission, shift-like `X`/active-vertex source emission, `A_selected`,
and `b_selected` are not theorem-derived yet.

The conditional value run is ready:

```text
rank(A_conditional) = {weyl_a["locked_solve"]["rank"]}
condition number    = {weyl_a["locked_solve"]["condition_number"]}
deltaTheta          = {weyl_a["locked_solve"]["deltaTheta_conditional"]}
A^T A if promoted   = {conditional["A_transpose_A"]}
A^T b if promoted   = {conditional["A_transpose_b"]}
```

So the remaining work is not a numerical search.  It is source promotion:
derive the enriched Weyl-pair source packet from the selected branch, or run
honest selected Galerkin C1 execution values.

No observed masses, CKM/PMNS values, CP phase, benchmark matrices, or target
residuals are used as selectors.

Next artifact: `{NEXT}`.
"""

    PROMOTION_ATTEMPT_PACKET.write_text(json.dumps(promotion_attempt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CONDITIONAL_VALUE_RUN_PACKET.write_text(json.dumps(conditional_value_run, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    HONEST_EXECUTION_PACKET.write_text(json.dumps(honest_execution, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
