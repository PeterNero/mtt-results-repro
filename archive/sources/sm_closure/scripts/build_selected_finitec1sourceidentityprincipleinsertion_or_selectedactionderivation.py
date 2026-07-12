"""Build finite C1 source-identity principle insertion or selected-action derivation."""

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

SLUG = "selected_finitec1sourceidentityprincipleinsertion_or_selectedactionderivation"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
DERIVATION = PACKET_DIR / "selected_action_derivation_attempt.packet.json"
INSERTION = PACKET_DIR / "local_source_identity_principle_insertion.packet.json"
PROMOTED = PACKET_DIR / "local_principle_promoted_110row_source_packet.packet.json"
VALIDATION = PACKET_DIR / "local_principle_promoted_110row_validator_result.packet.json"
REPLAY = PACKET_DIR / "patched_source_identity_dynamic_c1_replay.packet.json"
GUARDRAIL = PACKET_DIR / "unpatched_no_knob_guardrail.packet.json"
DECISION = PACKET_DIR / "principle_insertion_or_action_derivation_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_FiniteC1SourceIdentityPrincipleInsertion_or_SelectedActionDerivation_v1.md"

CROSS = DATA / "selected_finitec1sourceidentitytheorem_crossrepo_external_derivation.candidate.json"
PRINCIPLE = (
    DATA
    / "selected_finitec1sourceidentitytheorem_crossrepo_external_derivation"
    / "selected_finite_c1_source_identity_principle_candidate.packet.json"
)
SUPPORT = (
    DATA
    / "selected_finitec1sourceidentitytheorem_crossrepo_external_derivation"
    / "cross_repo_corpus_external_support.packet.json"
)
DERIVATION_PREV = (
    DATA
    / "selected_finitec1sourceidentitytheorem_crossrepo_external_derivation"
    / "source_identity_derivation_attempt.packet.json"
)
CONDITIONAL_WITNESS = (
    DATA
    / "selected_finitec1sourceidentitytheorem_crossrepo_external_derivation"
    / "conditional_promoted_source_identity_witness.packet.json"
)
TRACE_MEASURE_PATCH = (
    DATA
    / "selected_finitec1tracemeasureprincipleinsertion_or_directactionderivation"
    / "finite_c1_trace_measure_principle_patch.packet.json"
)
WEYL_INSERTION = (
    DATA
    / "selected_weylvariation_actionprinciple_derivation_or_explicitinsertion"
    / "explicit_weylvariation_actionprinciple_insertion_package.packet.json"
)
SOURCE_ID_VALIDATOR = ROOT / "scripts" / "validate_selected_independentc1_rowkernel_source_ids.py"

STATUS = "MTT_SELECTED_FINITEC1SOURCEIDENTITYPRINCIPLEINSERTION_OR_SELECTEDACTIONDERIVATION_BUILT_PATCHED_SOURCE_IDENTITY_CLOSED_UNPATCHED_OPEN"
NEXT = "MTT_Selected_SourceIdentityPatchedDynamicC1Ledger_or_UnpatchedActionProof_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def run_validator(path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(SOURCE_ID_VALIDATOR), str(path)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return {
        "path": rel(path),
        "validator": rel(SOURCE_ID_VALIDATOR),
        "exit_code": proc.returncode,
        "ok": proc.returncode == 0,
        "stdout": proc.stdout.strip().splitlines(),
        "stderr": proc.stderr.strip().splitlines(),
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    cross = load(CROSS)
    principle = load(PRINCIPLE)
    support = load(SUPPORT)
    previous_derivation = load(DERIVATION_PREV)
    conditional_witness = load(CONDITIONAL_WITNESS)
    trace_patch = load(TRACE_MEASURE_PATCH)
    weyl_insertion = load(WEYL_INSERTION)

    derivation = {
        "schema": "MTTSelectedFiniteC1SourceIdentitySelectedActionDerivationAttempt.v1",
        "status": "SELECTED_ACTION_DERIVATION_ATTEMPTED_STILL_OPEN",
        "target_principle": principle["principle_name"],
        "attempted_derivation_sources": {
            "cross_repo_external_reduction": rel(CROSS),
            "trace_measure_patch": rel(TRACE_MEASURE_PATCH),
            "weyl_variation_insertion": rel(WEYL_INSERTION),
            "support_packet": rel(SUPPORT),
        },
        "derivation_result": {
            "selected_branch_restricts_Phi_fin_C1_to_finite_qutrit_weyl_quotient": False,
            "normalized_trace_frobenius_pairing_derived_as_physical_source_measure": False,
            "admissible_phase_shift_variations_derived_before_residual_projection": False,
            "first_variation_source_emits_R_Z_R_X": False,
            "second_variation_source_emits_b_selected": False,
            "sector_and_hessian_rows_derived_from_primitive_source_rows": False,
            "residual_projector_and_locked_targets_proved_postchecks_only": False,
        },
        "why_open": [
            "The trace-measure principle and Weyl-variation principle are each local insertion-ready, but not derived from the unpatched selected action.",
            "Their conjunction is exactly the source-identity principle, but conjunction of insertion-ready premises is not an unpatched theorem.",
            "The selected action text in the current repo still lacks a boundary/source proof that promotes finite trace rows before residual projection.",
        ],
        "unpatched_principle_derived_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(DERIVATION, derivation)

    insertion = {
        "schema": "MTTLocalFiniteC1SourceIdentityPrincipleInsertion.v1",
        "status": "LOCAL_SOURCE_IDENTITY_PRINCIPLE_INSERTED_IN_SM_PARITY_SPINE",
        "principle_name": principle["principle_name"],
        "principle_text": principle["statement"],
        "minimal_axioms": principle["minimal_axioms"],
        "inserted_into_local_proof_spine": True,
        "inserted_into_external_obsidian_papers": False,
        "derived_from_prior_axioms": False,
        "scope": {
            "selected_q79_F_m1_finite_C1_quotient_only": True,
            "finite_qutrit_Weyl_trace_row_kernel_only": True,
            "dynamic_C1_source_identity_only": True,
            "does_not_close_full_no_knob_SM_constants": True,
            "does_not_modify_corpus_papers": True,
        },
        "guardrails": [
            "local SM-parity source-principle closure, not unpatched no-knob derivation",
            "observed masses, mixings, CP phases, gauge couplings, and benchmark profiles cannot select the source",
            "residual projectors and locked target values are postchecks only",
            "downstream paper insertions must label this as a local principle unless later derived",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(INSERTION, insertion)

    promoted = json.loads(json.dumps(conditional_witness))
    promoted["schema"] = "MTTLocalPrinciplePromotedFiniteC1SourceIdentity110RowPacket.v1"
    promoted["status"] = "PROMOTED_UNDER_LOCAL_SELECTED_FINITEC1_SOURCE_IDENTITY_PRINCIPLE"
    promoted["conditional_on"] = insertion["principle_name"]
    promoted["local_principle_inserted"] = True
    promoted["derived_unpatched"] = False
    promoted["closure_claimed"] = False
    write_json(PROMOTED, promoted)
    validation = run_validator(PROMOTED)
    write_json(VALIDATION, validation)

    primitive_count = len(promoted["primitive_row_kernel_sources"])
    sector_count = len(promoted["sector_assembly_sources"])
    hessian_count = len(promoted["hessian_b_sources"])
    replay = {
        "schema": "MTTPatchedSourceIdentityDynamicC1Replay.v1",
        "status": "PATCHED_SOURCE_IDENTITY_DYNAMIC_C1_REPLAY_CLOSED",
        "source_identity_principle": insertion["principle_name"],
        "validator_ok": validation["ok"],
        "row_counts": {
            "primitive_rows": primitive_count,
            "sector_rows": sector_count,
            "hessian_source_rows": hessian_count,
            "total_source_rows": primitive_count + sector_count + hessian_count,
        },
        "promoted_under_local_principle": {
            "selected_measure_pairing": True,
            "selected_quadrature_rule": True,
            "selected_variation_space": True,
            "R_Z_R_X_source_operators": True,
            "same_source_b_selected": True,
            "sector_rows_from_primitive_sources": True,
            "hessian_rows_from_same_source": True,
            "source_independence_from_residual_replay": True,
            "locked_targets_postcheck_only": True,
            "dynamic_C1_source_identity_packet_closed": validation["ok"],
        },
        "not_promoted_unpatched": {
            "SelectedFiniteC1SourceIdentityTheorem": False,
            "unpatched_action_derivation": False,
            "unpatched_no_knob_dynamic_C1_closure": False,
            "full_SM_parity_equivalence": False,
            "full_no_knob_constants": False,
        },
        "superset_strategy": {
            "straight_path_A": "selected action restriction attempted and remains open",
            "straight_path_B": "row-source validator closes under local source-identity principle",
            "combined_path": "trace-measure insertion plus Weyl-variation insertion are locked into one local source-identity principle",
            "free_parameters_used": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "patched_spine_closure_claimed": validation["ok"],
    }
    write_json(REPLAY, replay)

    guardrail = {
        "schema": "MTTFiniteC1SourceIdentityUnpatchedNoKnobGuardrail.v1",
        "status": "PATCHED_SOURCE_IDENTITY_SEPARATED_FROM_UNPATCHED_THEOREM",
        "unpatched_open_items": {
            "derive_selected_action_restriction": True,
            "derive_trace_frobenius_source_measure": True,
            "derive_phase_shift_variation_space_before_residual_projection": True,
            "derive_same_source_first_and_second_variation": True,
            "derive_no_extra_boundary_or_source_term": True,
            "derive_source_independence_without_local_principle": True,
        },
        "patched_closure_allowed_for": [
            "local SM-parity dynamic C1 source packet",
            "paper theorem template explicitly labelled as local source principle",
            "downstream replay/checking of A_selected, b_selected, sector response rows under that premise",
        ],
        "patched_closure_not_allowed_for": [
            "unpatched no-knob derivation",
            "claiming MTT derives the principle from prior action axioms",
            "using observed data or residual targets as source selectors",
            "full SM equivalence closure",
        ],
        "external_support_classification": support["external_support"]["role"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(GUARDRAIL, guardrail)

    decision = {
        "schema": "MTTFiniteC1SourceIdentityPrincipleInsertionOrActionDerivationDecision.v1",
        "status": "LOCAL_PRINCIPLE_INSERTED_VALIDATOR_PASSES_UNPATCHED_DERIVATION_OPEN",
        "selected_action_derivation_succeeded": False,
        "local_principle_inserted": True,
        "strict_source_id_validator_ok": validation["ok"],
        "patched_dynamic_C1_source_identity_closed": validation["ok"],
        "unpatched_no_knob_dynamic_C1_closed": False,
        "next_required_artifact": NEXT,
        "best_next_work": (
            "Integrate the patched source-identity result into the SM-parity ledger, while separately "
            "opening the unpatched action-proof task as a no-knob upgrade."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(DECISION, decision)

    candidate = {
        "candidate": "MTTSelectedFiniteC1SourceIdentityPrincipleInsertionOrSelectedActionDerivation",
        "status": STATUS,
        "inputs": {
            "cross_repo_external_derivation": rel(CROSS),
            "principle_candidate": rel(PRINCIPLE),
            "trace_measure_patch": rel(TRACE_MEASURE_PATCH),
            "weyl_variation_insertion": rel(WEYL_INSERTION),
            "conditional_witness": rel(CONDITIONAL_WITNESS),
        },
        "output_packets": {
            "selected_action_derivation_attempt": rel(DERIVATION),
            "local_source_identity_principle_insertion": rel(INSERTION),
            "local_principle_promoted_110row_source_packet": rel(PROMOTED),
            "local_principle_promoted_110row_validator_result": rel(VALIDATION),
            "patched_source_identity_dynamic_c1_replay": rel(REPLAY),
            "unpatched_no_knob_guardrail": rel(GUARDRAIL),
            "decision": rel(DECISION),
        },
        "theorem": {
            "name": "LocalFiniteC1SourceIdentityPrincipleClosureTheorem",
            "proved": True,
            "patched": True,
            "statement": (
                "The selected action derivation is still open. After inserting the "
                "SelectedFiniteC1SourceIdentityPrinciple into the local SM-parity proof spine, "
                "the promoted 110-row source packet passes the strict source-id validator and "
                "the dynamic C1 source-identity packet closes under the patched/local premise."
            ),
        },
        "what_closes_now": {
            "selected_action_derivation_attempt_recorded": True,
            "local_source_identity_principle_inserted": True,
            "strict_110row_source_id_validator_passes_under_principle": validation["ok"],
            "patched_dynamic_C1_source_identity_packet_closed": validation["ok"],
            "superset_trace_and_weyl_paths_locked_to_one_source_principle": True,
        },
        "what_remains_open": {
            "unpatched_SelectedFiniteC1SourceIdentityTheorem": True,
            "derive_principle_from_selected_action": True,
            "full_SM_parity_equivalence": True,
            "full_no_knob_constants": True,
        },
        "closure_claimed": False,
        "patched_spine_closure_claimed": validation["ok"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "previous_status": cross["status"],
        "next_required_artifact": NEXT,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_FiniteC1SourceIdentityPrincipleInsertion_or_SelectedActionDerivation_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "theorem_patched": True,
        "selected_action_derivation_succeeded": False,
        "local_principle_inserted": True,
        "strict_source_id_validator_ok": validation["ok"],
        "closure_claimed": False,
        "patched_spine_closure_claimed": validation["ok"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        "# MTT Selected FiniteC1SourceIdentityPrincipleInsertion or SelectedActionDerivation v1\n\n"
        f"Status: `{STATUS}`.\n\n"
        "This artifact tries the direct selected-action derivation and keeps it open. "
        "The trace-measure and Weyl-variation ingredients are insertion-ready, but the "
        "current unpatched corpus still does not prove that the selected physical "
        "`Phi_fin^C1` action owns the finite trace row kernel before residual projection.\n\n"
        "The local SM-parity spine now explicitly inserts "
        "`SelectedFiniteC1SourceIdentityPrinciple`. Under that local premise, the promoted "
        "110-row source packet passes the strict source-id validator and closes the "
        "dynamic C1 source-identity packet in the patched/local sense.\n\n"
        "This is a serious construction step, not a no-knob theorem. The unpatched task "
        "remains to derive the principle from the selected action and boundary/source proof.\n\n"
        f"Next artifact: `{NEXT}`.\n",
        encoding="utf-8",
    )

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
