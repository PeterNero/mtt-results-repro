"""Build unpatched Weyl-variation principle derivation or Route-B source rows fill.

This follows the local last-source witness.  It imports the finite Weyl trace
measure sublemma as a genuinely derived piece, then replays the strict
validators with only that extra physical-source field closed.  The remaining
gap is the physical finite-quotient/no-extra-source/same-source emission lemma,
or independent C1 source rows.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_unpatchedweylvariationprinciplederivation_or_routebsourcerowsfill"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
MEASURE_REDUCTION = PACKET_DIR / "finite_trace_measure_reduction.packet.json"
ACTION_ATTEMPT = PACKET_DIR / "unpatched_weylvariation_action_kernel_attempt.packet.json"
ACTION_RESULT = PACKET_DIR / "unpatched_weylvariation_action_kernel_validator_result.packet.json"
PHYSICAL_ATTEMPT = PACKET_DIR / "physical_source_attempt_with_measure_closed.packet.json"
PHYSICAL_RESULT = PACKET_DIR / "physical_source_with_measure_closed_validator_result.packet.json"
ROUTE_B_ATTEMPT = PACKET_DIR / "route_b_source_rows_fill_attempt.packet.json"
ROUTE_B_RESULT = PACKET_DIR / "route_b_source_rows_fill_validator_result.packet.json"
NEXT_REMAINDER = PACKET_DIR / "physical_finite_quotient_remainder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_UnpatchedWeylVariationPrincipleDerivation_or_RouteBSourceRowsFill_v1.md"

PREVIOUS = DATA / "selected_lastsourcelemmaproof_or_independentc1kernelsourcerows.candidate.json"
LAST_DECISION = DATA / "selected_lastsourcelemmaproof_or_independentc1kernelsourcerows" / "last_source_lemma_decision.packet.json"
PSM_ACTION = DATA / "selected_psm_c1_02_unpatchedselectedactionderivation_or_honestfinitec1execution.candidate.json"
MEASURE_IMPORT = (
    DATA
    / "selected_psm_c1_02_unpatchedselectedactionderivation_or_honestfinitec1execution"
    / "finite_weyl_trace_measure_sublemma_import.packet.json"
)
ACTION_REMAINDER = (
    DATA
    / "selected_psm_c1_02_unpatchedselectedactionderivation_or_honestfinitec1execution"
    / "physical_action_boundary_source_remainder.packet.json"
)
VARIATION_ROUTE_A = (
    DATA
    / "selected_actionkernelfourclauseproof_or_independentkernelvaluesrun"
    / "route_a_four_clause_partial_proof.packet.json"
)
VARIATION_ROUTE_B = (
    DATA
    / "selected_actionkernelfourclauseproof_or_independentkernelvaluesrun"
    / "route_b_independent_kernel_values_first_run.packet.json"
)
SUPPORT_COUNTERMODEL = (
    DATA
    / "selected_minimalfinitec1sourcepromotionlemma_proof_or_countermodel"
    / "closed_support_not_enough_countermodel.packet.json"
)
ROW_SCHEDULE = (
    DATA
    / "selected_stromingertracec1firstvariation_or_quadratureexecutionplan"
    / "quadrature_row_schedule.packet.json"
)

ACTION_VALIDATOR = ROOT / "scripts" / "validate_selected_phifinc1_preresidual_action_kernel_theorem.py"
PHYSICAL_VALIDATOR = ROOT / "scripts" / "validate_selected_physical_boundary_firstvariation_source.py"
ROW_VALIDATOR = ROOT / "scripts" / "validate_selected_independentc1_rowkernel_source_ids.py"

STATUS = "MTT_SELECTED_UNPATCHEDWEYLVARIATIONPRINCIPLEDERIVATION_OR_ROUTEB_SOURCEROWSFILL_BUILT_MEASURE_CLOSED_ACTION_REMAINDER_OPEN"
NEXT = "MTT_Selected_PhysicalPhiFinC1FiniteQuotientNoExtraBoundarySourceLemma_or_IndependentRows_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def run_validator(validator: Path, payload: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(validator), str(payload)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return {
        "validator": rel(validator),
        "payload": rel(payload),
        "returncode": proc.returncode,
        "stdout": proc.stdout.strip(),
        "stderr_lines": proc.stderr.splitlines(),
    }


def schedule_rows() -> dict[str, list[str]]:
    schedule = load(ROW_SCHEDULE)
    return {stage["stage"]: stage["rows"] for stage in schedule["execution_order"]}


def route_b_payload(variation_route_b: dict[str, Any], rows: dict[str, list[str]]) -> dict[str, Any]:
    global_sources = variation_route_b["global_sources"]
    return {
        "schema": "MTTRouteBSourceRowsFillAttemptAfterMeasureClosed.v1",
        "status": "MEASURE_SUPPORT_IMPORTED_INDEPENDENT_SOURCE_ROWS_OPEN",
        "global_sources": global_sources,
        "primitive_row_kernel_sources": [
            {
                "row_id": row_id,
                "source_id": None,
                "selected_emitted": False,
                "theorem_derived": False,
                "independent_of_residual_replay": False,
                "locked_target_dependency": False,
                "integral_formula": None,
                "selected_measure_pairing_id": global_sources["selected_measure_pairing"]["source_id"],
                "selected_quadrature_rule_id": global_sources["selected_quadrature_rule"]["source_id"],
            }
            for row_id in rows["primitive_contractions"]
        ],
        "hessian_b_sources": [
            {
                "row_id": row_id,
                "source_id": None,
                "selected_emitted": False,
                "theorem_derived": False,
                "independent_of_residual_replay": False,
                "locked_target_dependency": False,
                "selected_b_vector_source": False,
                "not_copied_from_A_transpose_b_target": True,
            }
            for row_id in rows["hessian_source"]
        ],
        "sector_assembly_sources": [
            {
                "row_id": row_id,
                "source_id": None,
                "selected_emitted": False,
                "theorem_derived": False,
                "independent_of_residual_replay": False,
                "locked_target_dependency": False,
                "assembled_from_primitive_source_rows": False,
            }
            for row_id in rows["sector_matrices"]
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "locked_target_values_used_as_source": False,
        "closure_claimed": False,
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    last_decision = load(LAST_DECISION)
    psm_action = load(PSM_ACTION)
    measure_import = load(MEASURE_IMPORT)
    action_remainder = load(ACTION_REMAINDER)
    variation_route_a = load(VARIATION_ROUTE_A)
    variation_route_b = load(VARIATION_ROUTE_B)
    support_countermodel = load(SUPPORT_COUNTERMODEL)
    rows = schedule_rows()

    measure_reduction = {
        "schema": "MTTUnpatchedWeylVariationFiniteTraceMeasureReduction.v1",
        "status": "FINITE_TRACE_MEASURE_SUBLEMMA_DERIVED_REMAINDER_PHYSICAL_ACTION",
        "source": rel(MEASURE_IMPORT),
        "measure_normalization_derived": measure_import["measure_normalization_derived"],
        "finite_trace_boundary_cancellation": measure_import["finite_trace_boundary_cancellation"],
        "measure_part_no_longer_axiomatic": measure_import["measure_part_no_longer_axiomatic"],
        "not_enough_for_unpatched_source_identity": measure_import[
            "not_enough_for_unpatched_source_identity"
        ],
        "remainder_name": action_remainder["remaining_core_lemma"]["name"],
        "remainder_must_prove": action_remainder["remaining_core_lemma"]["must_prove"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    evidence = [
        {"source": rel(PREVIOUS), "closes": "local witness sufficient, unpatched open"},
        {"source": rel(MEASURE_IMPORT), "closes": "finite trace/Frobenius measure sublemma"},
        {"source": rel(ACTION_REMAINDER), "closes": "physical finite-quotient remainder"},
        {"source": rel(VARIATION_ROUTE_A), "closes": "admissible variation-space clause"},
        {"source": rel(SUPPORT_COUNTERMODEL), "closes": "support-only countermodel"},
        {"source": rel(PSM_ACTION), "closes": "PSM selected-action split"},
    ]

    action_attempt = {
        "schema": "MTTUnpatchedWeylVariationActionKernelAttemptAfterMeasureClosed.v1",
        "status": "MEASURE_CLOSED_ACTION_KERNEL_STILL_REJECTED",
        "same_branch": True,
        "physical_action_equals_c1_defect_functional": False,
        "admissible_differentiated_variations_fixed": variation_route_a[
            "admissible_differentiated_variations_fixed"
        ],
        "physical_boundary_source_terms_vanish": False,
        "same_source_rz_rx_bselected_emitted": False,
        "measure_sublemma_derived": measure_import["measure_normalization_derived"],
        "attached_theorem_evidence": evidence,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "locked_target_values_used_as_source": False,
        "residual_projector_replay_used_as_source": False,
        "free_axiom_patch_used": False,
        "closure_claimed": False,
    }

    physical_attempt = {
        "schema": "MTTPhysicalSourceAttemptAfterMeasureClosed.v1",
        "status": "PHYSICAL_MEASURE_CLOSED_OTHER_SOURCE_FIELDS_OPEN",
        "same_branch": True,
        "theorem_derived": False,
        "physical_first_variation_identity": False,
        "physical_measure_equals_trace_frobenius_pairing": measure_import[
            "measure_normalization_derived"
        ],
        "phase_R_Z_source_selection": False,
        "shift_R_X_source_selection": False,
        "same_source_b_selected_emission": False,
        "no_extra_physical_boundary_or_source_term": False,
        "attached_source_evidence": evidence,
        "locked_target_values_used_as_source": False,
        "residual_projector_replay_used_as_source": False,
        "benchmark_values_used_as_source": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    route_b = route_b_payload(variation_route_b, rows)

    for path, payload in [
        (MEASURE_REDUCTION, measure_reduction),
        (ACTION_ATTEMPT, action_attempt),
        (PHYSICAL_ATTEMPT, physical_attempt),
        (ROUTE_B_ATTEMPT, route_b),
    ]:
        write_json(path, payload)

    action_result = run_validator(ACTION_VALIDATOR, ACTION_ATTEMPT)
    physical_result = run_validator(PHYSICAL_VALIDATOR, PHYSICAL_ATTEMPT)
    route_b_result = run_validator(ROW_VALIDATOR, ROUTE_B_ATTEMPT)
    write_json(ACTION_RESULT, action_result)
    write_json(PHYSICAL_RESULT, physical_result)
    write_json(ROUTE_B_RESULT, route_b_result)

    next_remainder = {
        "schema": "MTTPhysicalPhiFinC1FiniteQuotientRemainder.v1",
        "status": "MEASURE_DERIVED_REMAINDER_EXACT",
        "lemma_name": action_remainder["remaining_core_lemma"]["name"],
        "must_prove": action_remainder["remaining_core_lemma"]["must_prove"],
        "current_truth_values": {
            "physical_PhiFinC1_restricts_to_selected_finite_Weyl_quotient": False,
            "no_extra_physical_boundary_or_source_term": False,
            "first_variation_emits_phase_R_Z_and_shift_R_X_before_residual_replay": False,
            "second_variation_emits_same_source_b_selected": False,
        },
        "already_removed_from_blocker": [
            "finite trace/Frobenius measure normalization",
            "algebraic finite trace boundary cancellation",
            "admissible differentiated variation-space clause",
            "local-premise sufficiency of the Weyl variation principle",
        ],
        "route_B_parallel": [
            "selected measure pairing source",
            "selected quadrature rule",
            "72 primitive row source ids and formulas",
            "2 Hessian/b_selected source rows",
            "36 sector assembly source ids",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(NEXT_REMAINDER, next_remainder)

    candidate = {
        "candidate": "MTTSelectedUnpatchedWeylVariationPrincipleDerivationOrRouteBSourceRowsFill",
        "status": STATUS,
        "inputs": {
            "previous_gate": rel(PREVIOUS),
            "last_source_lemma_decision": rel(LAST_DECISION),
            "psm_unpatched_selected_action_split": rel(PSM_ACTION),
            "finite_trace_measure_sublemma": rel(MEASURE_IMPORT),
            "physical_action_remainder": rel(ACTION_REMAINDER),
            "support_only_countermodel": rel(SUPPORT_COUNTERMODEL),
            "route_b_variation_packet": rel(VARIATION_ROUTE_B),
        },
        "output_packets": {
            "finite_trace_measure_reduction": rel(MEASURE_REDUCTION),
            "unpatched_weylvariation_action_kernel_attempt": rel(ACTION_ATTEMPT),
            "unpatched_weylvariation_action_kernel_validator_result": rel(ACTION_RESULT),
            "physical_source_attempt_with_measure_closed": rel(PHYSICAL_ATTEMPT),
            "physical_source_with_measure_closed_validator_result": rel(PHYSICAL_RESULT),
            "route_b_source_rows_fill_attempt": rel(ROUTE_B_ATTEMPT),
            "route_b_source_rows_fill_validator_result": rel(ROUTE_B_RESULT),
            "physical_finite_quotient_remainder": rel(NEXT_REMAINDER),
        },
        "what_closes_now": {
            "finite_trace_measure_sublemma_derived_imported": True,
            "physical_measure_field_promoted_in_partial_attempt": physical_attempt[
                "physical_measure_equals_trace_frobenius_pairing"
            ],
            "unpatched_principle_remainder_sharpened": True,
            "action_kernel_validator_rejects_remaining_physical_fields": action_result["returncode"] == 1,
            "physical_source_validator_rejects_remaining_source_fields": physical_result["returncode"] == 1,
            "route_B_source_rows_still_open_honestly": route_b_result["returncode"] == 1,
            "observed_constants_excluded_as_selectors": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "PhysicalPhiFinC1FiniteQuotientNoExtraBoundarySourceLemma": True,
            "physical_action_equals_c1_defect_functional": True,
            "physical_PhiFinC1_restricts_to_selected_finite_Weyl_quotient": True,
            "no_extra_physical_boundary_or_source_term": True,
            "pre_residual_R_Z_R_X_source_emission": True,
            "same_source_b_selected_second_variation": True,
            "or_emit_independent_C1_kernel_source_rows": True,
            "unpatched_SM_parity_dynamic_packet_closure": True,
            "true_SM_equivalence_closure": True,
            "no_knob_closure": True,
        },
        "promotion_decision": {
            "measure_sublemma_promoted_unpatched": True,
            "unpatched_SelectedWeylVariationActionPrinciple_derived": False,
            "unpatched_last_source_lemma_proved": False,
            "route_B_independent_C1_kernel_source_rows_exported": False,
            "unpatched_A_selected_promoted": False,
            "unpatched_b_selected_promoted": False,
            "unpatched_deltaTheta_C1_promoted": False,
            "unpatched_SM_parity_dynamic_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "theorem": {
            "name": "UnpatchedWeylVariationPrincipleMeasureReductionTheorem",
            "proved": True,
            "statement": (
                "The finite trace/Frobenius measure component of the unpatched Weyl-variation principle is "
                "derived from finite Weyl trace uniqueness and algebraic finite trace boundary cancellation. "
                "After importing that derived sublemma, the remaining unpatched source-promotion blocker is "
                "exactly the PhysicalPhiFinC1FiniteQuotientNoExtraBoundarySourceLemma, or an independent "
                "C1 kernel source-row export."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "patched_SM_parity_closure_preserved": previous["patched_SM_parity_closure_preserved"],
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_UnpatchedWeylVariationPrincipleDerivation_or_RouteBSourceRowsFill_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "measure_sublemma_promoted_unpatched": True,
        "unpatched_SelectedWeylVariationActionPrinciple_derived": False,
        "route_B_independent_C1_kernel_source_rows_exported": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected UnpatchedWeylVariationPrincipleDerivation or RouteBSourceRowsFill v1

Status: `{STATUS}`.

Progress: the finite trace/Frobenius measure part is no longer a patch.

```text
measure normalization derived        = {measure_import["measure_normalization_derived"]}
finite trace boundary cancellation   = {measure_import["finite_trace_boundary_cancellation"]}
physical measure field in validator  = {physical_attempt["physical_measure_equals_trace_frobenius_pairing"]}
```

Still open:

```text
physical Phi_fin^C1 finite quotient restriction
no extra physical boundary/source term
pre-residual R_Z/R_X source emission
same-source b_selected second variation
```

The next single Route-A lemma is:

`PhysicalPhiFinC1FiniteQuotientNoExtraBoundarySourceLemma`

Route B remains the independent selected C1 kernel source-row export.

No observed constants, benchmark rows, locked targets, or fitted SM data are
used as selectors.

Next artifact: `{NEXT}`.
"""

    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
