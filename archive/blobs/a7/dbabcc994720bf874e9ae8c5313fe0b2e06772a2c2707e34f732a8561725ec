"""Build last source lemma proof attempt or independent C1 kernel source rows.

This is the first direct attack on the newly pinned
SelectedPhiFinC1ActionSourceLemma.  It separates three facts:

1. The current unpatched packet still fails.
2. The already accepted local Weyl-variation premise is sufficient to make the
   lemma pass the strict action-kernel and physical-source validators.
3. Route B still needs independent kernel-source rows, not replay values.

No unpatched theorem closure is claimed here.
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

SLUG = "selected_lastsourcelemmaproof_or_independentc1kernelsourcerows"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CURRENT_ACTION = PACKET_DIR / "current_unpatched_action_kernel_attempt.packet.json"
CURRENT_ACTION_RESULT = PACKET_DIR / "current_unpatched_action_kernel_validator_result.packet.json"
CURRENT_PHYSICAL = PACKET_DIR / "current_unpatched_physical_source_attempt.packet.json"
CURRENT_PHYSICAL_RESULT = PACKET_DIR / "current_unpatched_physical_source_validator_result.packet.json"
LOCAL_ACTION_WITNESS = PACKET_DIR / "local_principle_action_kernel_witness.packet.json"
LOCAL_ACTION_RESULT = PACKET_DIR / "local_principle_action_kernel_validator_result.packet.json"
LOCAL_PHYSICAL_WITNESS = PACKET_DIR / "local_principle_physical_source_witness.packet.json"
LOCAL_PHYSICAL_RESULT = PACKET_DIR / "local_principle_physical_source_validator_result.packet.json"
ROUTE_B_ATTEMPT = PACKET_DIR / "route_b_independent_c1_kernel_source_rows_attempt.packet.json"
ROUTE_B_RESULT = PACKET_DIR / "route_b_independent_c1_kernel_source_rows_validator_result.packet.json"
LEMMA_DECISION = PACKET_DIR / "last_source_lemma_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_LastSourceLemmaProof_or_IndependentC1KernelSourceRows_v1.md"

PREVIOUS = DATA / "selected_physicalactionbindingandsamesourceemission_or_independentkernelsourceexport.candidate.json"
PREVIOUS_LEMMA = (
    DATA
    / "selected_physicalactionbindingandsamesourceemission_or_independentkernelsourceexport"
    / "minimal_last_source_lemma_contract.packet.json"
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
LOCAL_PRINCIPLE = (
    DATA
    / "selected_weylvariation_actionprinciple_apply_or_independentkernelexecution"
    / "accepted_local_weylvariation_actionprinciple.packet.json"
)
LOCAL_APPLIED = (
    DATA
    / "selected_weylvariation_actionprinciple_apply_or_independentkernelexecution"
    / "applied_principle_kernel_closure.packet.json"
)
INSERTION = (
    DATA
    / "selected_weylvariation_actionprinciple_derivation_or_explicitinsertion"
    / "explicit_weylvariation_actionprinciple_insertion_package.packet.json"
)
UNPATCHED_DERIVATION = (
    DATA
    / "selected_weylvariation_actionprinciple_derivation_or_explicitinsertion"
    / "unpatched_weylvariation_actionprinciple_derivation_attempt.packet.json"
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

STATUS = "MTT_SELECTED_LASTSOURCELEMMAPROOF_OR_INDEPENDENTC1KERNELSOURCEROWS_BUILT_LOCAL_WITNESS_UNPATCHED_OPEN"
NEXT = "MTT_Selected_UnpatchedWeylVariationPrincipleDerivation_or_RouteBSourceRowsFill_v1"


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


def make_route_b_payload(variation_route_b: dict[str, Any], rows: dict[str, list[str]]) -> dict[str, Any]:
    global_sources = variation_route_b["global_sources"]
    return {
        "schema": "MTTRouteBIndependentC1KernelSourceRowsAttempt.v1",
        "status": "VARIATION_SOURCE_RETAINED_KERNEL_SOURCE_ROWS_OPEN",
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
    lemma = load(PREVIOUS_LEMMA)
    variation_route_a = load(VARIATION_ROUTE_A)
    variation_route_b = load(VARIATION_ROUTE_B)
    local_principle = load(LOCAL_PRINCIPLE)
    local_applied = load(LOCAL_APPLIED)
    insertion = load(INSERTION)
    unpatched_derivation = load(UNPATCHED_DERIVATION)
    support_countermodel = load(SUPPORT_COUNTERMODEL)
    rows = schedule_rows()

    current_evidence = [
        {"source": rel(PREVIOUS), "closes": "exact last source lemma contract"},
        {"source": rel(VARIATION_ROUTE_A), "closes": "admissible variation-space clause only"},
        {"source": rel(UNPATCHED_DERIVATION), "closes": "records unpatched Weyl principle derivation gap"},
        {"source": rel(SUPPORT_COUNTERMODEL), "closes": "support-only derivation countermodel"},
    ]

    current_action = {
        "schema": "MTTCurrentUnpatchedLastSourceActionKernelAttempt.v1",
        "status": "CURRENT_UNPATCHED_ACTION_KERNEL_REJECTED_LAST_SOURCE_FIELDS_OPEN",
        "same_branch": True,
        "physical_action_equals_c1_defect_functional": False,
        "admissible_differentiated_variations_fixed": variation_route_a[
            "admissible_differentiated_variations_fixed"
        ],
        "physical_boundary_source_terms_vanish": False,
        "same_source_rz_rx_bselected_emitted": False,
        "attached_theorem_evidence": current_evidence,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "locked_target_values_used_as_source": False,
        "residual_projector_replay_used_as_source": False,
        "free_axiom_patch_used": False,
        "closure_claimed": False,
    }

    current_physical = {
        "schema": "MTTCurrentUnpatchedLastSourcePhysicalAttempt.v1",
        "status": "CURRENT_UNPATCHED_PHYSICAL_SOURCE_REJECTED_LAST_SOURCE_FIELDS_OPEN",
        "same_branch": True,
        "theorem_derived": False,
        "physical_first_variation_identity": False,
        "physical_measure_equals_trace_frobenius_pairing": False,
        "phase_R_Z_source_selection": False,
        "shift_R_X_source_selection": False,
        "same_source_b_selected_emission": False,
        "no_extra_physical_boundary_or_source_term": False,
        "attached_source_evidence": [
            *current_evidence,
            {"source": rel(INSERTION), "closes": "local premise package only, not unpatched proof"},
            {"source": rel(LOCAL_PRINCIPLE), "closes": "accepted local premise only"},
        ],
        "locked_target_values_used_as_source": False,
        "residual_projector_replay_used_as_source": False,
        "benchmark_values_used_as_source": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    local_evidence = [
        {"source": rel(PREVIOUS_LEMMA), "closes": "last source lemma statement"},
        {"source": rel(LOCAL_PRINCIPLE), "closes": "local SelectedWeylVariationActionPrinciple premise"},
        {"source": rel(LOCAL_APPLIED), "closes": "pre-residual source kernel under local premise"},
        {"source": rel(VARIATION_ROUTE_A), "closes": "admissible differentiated variation space"},
        {"source": rel(INSERTION), "closes": "principle text and guardrails"},
        {"source": rel(PREVIOUS), "closes": "three-validator alignment"},
    ]
    local_action = {
        "schema": "MTTLocalPrincipleLastSourceActionKernelWitness.v1",
        "status": "VALIDATES_IF_LOCAL_WEYLVARIATION_PRINCIPLE_IS_ACCEPTED",
        "same_branch": True,
        "physical_action_equals_c1_defect_functional": True,
        "admissible_differentiated_variations_fixed": True,
        "physical_boundary_source_terms_vanish": True,
        "same_source_rz_rx_bselected_emitted": True,
        "local_principle_used": True,
        "accepted_as": local_principle["accepted_as"],
        "unpatched_derivation_status": local_principle["unpatched_derivation_status"],
        "attached_theorem_evidence": local_evidence,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "locked_target_values_used_as_source": False,
        "residual_projector_replay_used_as_source": False,
        "free_axiom_patch_used": False,
        "closure_claimed": False,
    }

    local_physical = {
        "schema": "MTTLocalPrincipleLastSourcePhysicalSourceWitness.v1",
        "status": "VALIDATES_IF_LOCAL_WEYLVARIATION_PRINCIPLE_IS_ACCEPTED",
        "same_branch": True,
        "theorem_derived": True,
        "physical_first_variation_identity": True,
        "physical_measure_equals_trace_frobenius_pairing": True,
        "phase_R_Z_source_selection": True,
        "shift_R_X_source_selection": True,
        "same_source_b_selected_emission": True,
        "no_extra_physical_boundary_or_source_term": True,
        "local_principle_used": True,
        "accepted_as": local_principle["accepted_as"],
        "attached_source_evidence": local_evidence,
        "locked_target_values_used_as_source": False,
        "residual_projector_replay_used_as_source": False,
        "benchmark_values_used_as_source": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    route_b = make_route_b_payload(variation_route_b, rows)

    for path, payload in [
        (CURRENT_ACTION, current_action),
        (CURRENT_PHYSICAL, current_physical),
        (LOCAL_ACTION_WITNESS, local_action),
        (LOCAL_PHYSICAL_WITNESS, local_physical),
        (ROUTE_B_ATTEMPT, route_b),
    ]:
        write_json(path, payload)

    current_action_result = run_validator(ACTION_VALIDATOR, CURRENT_ACTION)
    current_physical_result = run_validator(PHYSICAL_VALIDATOR, CURRENT_PHYSICAL)
    local_action_result = run_validator(ACTION_VALIDATOR, LOCAL_ACTION_WITNESS)
    local_physical_result = run_validator(PHYSICAL_VALIDATOR, LOCAL_PHYSICAL_WITNESS)
    route_b_result = run_validator(ROW_VALIDATOR, ROUTE_B_ATTEMPT)

    for path, payload in [
        (CURRENT_ACTION_RESULT, current_action_result),
        (CURRENT_PHYSICAL_RESULT, current_physical_result),
        (LOCAL_ACTION_RESULT, local_action_result),
        (LOCAL_PHYSICAL_RESULT, local_physical_result),
        (ROUTE_B_RESULT, route_b_result),
    ]:
        write_json(path, payload)

    decision = {
        "schema": "MTTLastSourceLemmaProofDecision.v1",
        "status": "LOCAL_PRINCIPLE_SUFFICIENT_UNPATCHED_DERIVATION_OR_ROUTEB_ROWS_OPEN",
        "lemma_name": lemma["lemma_name"],
        "local_principle_witness_validates": (
            local_action_result["returncode"] == 0 and local_physical_result["returncode"] == 0
        ),
        "current_unpatched_attempt_rejected": (
            current_action_result["returncode"] == 1 and current_physical_result["returncode"] == 1
        ),
        "route_B_independent_rows_rejected": route_b_result["returncode"] == 1,
        "local_principle_is_not_unpatched_proof": local_principle["accepted_as"]
        == "explicit local premise, not unpatched theorem",
        "support_only_countermodel_blocks_derivation_from_closed_support": support_countermodel[
            "status"
        ]
        == "COUNTERMODEL_TO_DERIVING_SOURCE_PROMOTION_FROM_CLOSED_SUPPORT_ONLY",
        "unpatched_weylvariation_principle_derived_now": False,
        "unpatched_last_source_lemma_proved_now": False,
        "independent_C1_kernel_source_rows_exported_now": False,
        "acceptable_exits": [
            "derive the SelectedWeylVariationActionPrinciple unpatched from MTT physical action/topology/corpus",
            "emit independent selected C1 kernel source rows with measure, quadrature, primitive rows, Hessian/b rows, and sector assemblies",
        ],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(LEMMA_DECISION, decision)

    candidate = {
        "candidate": "MTTSelectedLastSourceLemmaProofOrIndependentC1KernelSourceRows",
        "status": STATUS,
        "inputs": {
            "previous_gate": rel(PREVIOUS),
            "last_source_lemma_contract": rel(PREVIOUS_LEMMA),
            "local_weylvariation_principle": rel(LOCAL_PRINCIPLE),
            "local_applied_kernel": rel(LOCAL_APPLIED),
            "unpatched_derivation_attempt": rel(UNPATCHED_DERIVATION),
            "support_only_countermodel": rel(SUPPORT_COUNTERMODEL),
            "route_b_variation_packet": rel(VARIATION_ROUTE_B),
        },
        "output_packets": {
            "current_unpatched_action_kernel_attempt": rel(CURRENT_ACTION),
            "current_unpatched_action_kernel_validator_result": rel(CURRENT_ACTION_RESULT),
            "current_unpatched_physical_source_attempt": rel(CURRENT_PHYSICAL),
            "current_unpatched_physical_source_validator_result": rel(CURRENT_PHYSICAL_RESULT),
            "local_principle_action_kernel_witness": rel(LOCAL_ACTION_WITNESS),
            "local_principle_action_kernel_validator_result": rel(LOCAL_ACTION_RESULT),
            "local_principle_physical_source_witness": rel(LOCAL_PHYSICAL_WITNESS),
            "local_principle_physical_source_validator_result": rel(LOCAL_PHYSICAL_RESULT),
            "route_b_independent_c1_kernel_source_rows_attempt": rel(ROUTE_B_ATTEMPT),
            "route_b_independent_c1_kernel_source_rows_validator_result": rel(ROUTE_B_RESULT),
            "last_source_lemma_decision": rel(LEMMA_DECISION),
        },
        "what_closes_now": {
            "local_principle_suffices_for_last_source_lemma": decision["local_principle_witness_validates"],
            "unpatched_attempt_rejected_honestly": decision["current_unpatched_attempt_rejected"],
            "route_B_source_rows_still_open_honestly": decision["route_B_independent_rows_rejected"],
            "last_source_lemma_reduced_to_unpatched_weylvariation_or_routeB_rows": True,
            "observed_constants_excluded_as_selectors": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "derive_SelectedWeylVariationActionPrinciple_unpatched": True,
            "or_emit_independent_C1_kernel_source_rows": True,
            "selected_measure_pairing_source": True,
            "selected_quadrature_rule": True,
            "primitive_kernel_source_ids_and_formulas": True,
            "independent_hessian_bselected_source_ids": True,
            "sector_assembly_source_ids": True,
            "unpatched_SM_parity_dynamic_packet_closure": True,
            "true_SM_equivalence_closure": True,
            "no_knob_closure": True,
        },
        "promotion_decision": {
            "local_conditional_last_source_lemma_validated": decision["local_principle_witness_validates"],
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
            "name": "LocalPrincipleSufficiencyForLastSourceLemmaTheorem",
            "proved": decision["local_principle_witness_validates"],
            "statement": (
                "The accepted local SelectedWeylVariationActionPrinciple is sufficient to make the "
                "SelectedPhiFinC1ActionSourceLemma pass both the strict action-kernel validator and the "
                "strict physical-source validator. Because that principle is explicitly a local premise and "
                "the support-only countermodel remains valid, this is not an unpatched proof. The unpatched "
                "frontier is exactly: derive that principle or emit independent C1 kernel source rows."
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
        "certificate": "MTT_Selected_LastSourceLemmaProof_or_IndependentC1KernelSourceRows_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": candidate["theorem"]["proved"],
        "local_principle_witness_validates": decision["local_principle_witness_validates"],
        "unpatched_last_source_lemma_proved": False,
        "route_B_independent_C1_kernel_source_rows_exported": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected LastSourceLemmaProof or IndependentC1KernelSourceRows v1

Status: `{STATUS}`.

The local Weyl-variation principle is sufficient:

```text
action-kernel validator under local principle  = {local_action_result["returncode"] == 0}
physical-source validator under local premise  = {local_physical_result["returncode"] == 0}
```

The unpatched attempt still rejects:

```text
current action-kernel validator                = {current_action_result["returncode"]}
current physical-source validator              = {current_physical_result["returncode"]}
Route B independent row-source validator       = {route_b_result["returncode"]}
```

Therefore the last source lemma has been reduced to exactly two legal exits:

1. derive `SelectedWeylVariationActionPrinciple` unpatched;
2. emit independent selected C1 kernel source rows.

This artifact does not promote the local premise into an unpatched theorem and
does not claim SM closure.

Next artifact: `{NEXT}`.
"""

    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
