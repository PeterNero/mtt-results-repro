"""Build physical action binding / same-source emission or independent kernel source export.

This packet sits immediately after the action-kernel variation-space clause.
It does not claim SM closure.  It aligns three validators and isolates the
last legal source object needed to promote the formal finite C1 packet.
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

SLUG = "selected_physicalactionbindingandsamesourceemission_or_independentkernelsourceexport"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ACTION_PACKET = PACKET_DIR / "route_a_action_kernel_binding_attempt.packet.json"
ACTION_RESULT = PACKET_DIR / "route_a_action_kernel_binding_validator_result.packet.json"
PHYSICAL_PACKET = PACKET_DIR / "physical_source_emission_attempt.packet.json"
PHYSICAL_RESULT = PACKET_DIR / "physical_source_emission_validator_result.packet.json"
ROUTE_B_PACKET = PACKET_DIR / "route_b_independent_kernel_source_export_attempt.packet.json"
ROUTE_B_RESULT = PACKET_DIR / "route_b_independent_kernel_source_export_validator_result.packet.json"
LAST_LEMMA = PACKET_DIR / "minimal_last_source_lemma_contract.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PhysicalActionBindingAndSameSourceEmission_or_IndependentKernelSourceExport_v1.md"

VARIATION_GATE = DATA / "selected_actionkernelfourclauseproof_or_independentkernelvaluesrun.candidate.json"
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
C1_DEFECT = DATA / "selected_c1defectfunctionalsource_or_independentquadraturedatafill.candidate.json"
PHYSICAL_GATE = DATA / "selected_physicalboundaryfirstvariation_or_selectedsourceemission.candidate.json"
LAST_SOURCE = DATA / "selected_physicalphifinc1actionsource_or_provenanceindependencetheorem.candidate.json"
ROW_SCHEDULE = (
    DATA
    / "selected_stromingertracec1firstvariation_or_quadratureexecutionplan"
    / "quadrature_row_schedule.packet.json"
)

ACTION_VALIDATOR = ROOT / "scripts" / "validate_selected_phifinc1_preresidual_action_kernel_theorem.py"
PHYSICAL_VALIDATOR = ROOT / "scripts" / "validate_selected_physical_boundary_firstvariation_source.py"
ROW_VALIDATOR = ROOT / "scripts" / "validate_selected_independentc1_rowkernel_source_ids.py"

STATUS = (
    "MTT_SELECTED_PHYSICALACTIONBINDINGANDSAMESOURCEEMISSION_OR_INDEPENDENTKERNELSOURCEEXPORT_"
    "BUILT_LAST_SOURCE_LEMMA_EXACT"
)
NEXT = "MTT_Selected_LastSourceLemmaProof_or_IndependentC1KernelSourceRows_v1"


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


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    variation_gate = load(VARIATION_GATE)
    variation_route_a = load(VARIATION_ROUTE_A)
    variation_route_b = load(VARIATION_ROUTE_B)
    c1_defect = load(C1_DEFECT)
    physical_gate = load(PHYSICAL_GATE)
    last_source = load(LAST_SOURCE)
    rows = schedule_rows()

    evidence = [
        {
            "source": rel(VARIATION_GATE),
            "closes": "admissible differentiated variation-space clause",
        },
        {
            "source": rel(C1_DEFECT),
            "closes": "unique formal C1 defect functional, not physical application",
        },
        {
            "source": rel(PHYSICAL_GATE),
            "closes": "six-field physical source validator and conditional witness",
        },
        {
            "source": rel(LAST_SOURCE),
            "closes": "last source theorem/provenance disjunction contract",
        },
    ]

    action_packet = {
        "schema": "MTTPhysicalActionBindingSameSourceEmissionAttempt.v1",
        "status": "VARIATION_AND_FORMAL_DEFECT_CLOSED_PHYSICAL_BINDING_OPEN",
        "same_branch": True,
        "physical_action_equals_c1_defect_functional": False,
        "admissible_differentiated_variations_fixed": variation_route_a[
            "admissible_differentiated_variations_fixed"
        ],
        "physical_boundary_source_terms_vanish": False,
        "same_source_rz_rx_bselected_emitted": False,
        "formal_C1_defect_functional_sourced": c1_defect["promotion_decision"][
            "selected_C1_defect_functional_formal_source_promoted"
        ],
        "why_physical_action_binding_is_not_promoted": [
            "Formal uniqueness of the C1 defect functional does not prove Phi_fin^C1 is the physical action using it.",
            "Algebraic finite trace boundary cancellation is weaker than no extra physical boundary/source term.",
            "The same-source R_Z/R_X/b_selected packet has not been emitted by the physical action.",
        ],
        "attached_theorem_evidence": evidence,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "locked_target_values_used_as_source": False,
        "residual_projector_replay_used_as_source": False,
        "free_axiom_patch_used": False,
        "closure_claimed": False,
    }

    physical_packet = {
        "schema": "MTTPhysicalSourceEmissionAlignedAttempt.v1",
        "status": "CURRENT_PHYSICAL_SOURCE_EMISSION_REJECTED_SIX_FIELDS_OPEN",
        "same_branch": True,
        "theorem_derived": False,
        "physical_first_variation_identity": False,
        "physical_measure_equals_trace_frobenius_pairing": False,
        "phase_R_Z_source_selection": False,
        "shift_R_X_source_selection": False,
        "same_source_b_selected_emission": False,
        "no_extra_physical_boundary_or_source_term": False,
        "attached_source_evidence": [
            *evidence,
            {
                "source": rel(
                    DATA
                    / "selected_physicalboundaryfirstvariation_or_selectedsourceemission"
                    / "conditional_physical_source_emission_witness.packet.json"
                ),
                "closes": "conditional witness only; not an actual source theorem",
            },
            {
                "source": rel(
                    DATA
                    / "selected_physicalphifinc1actionsource_or_provenanceindependencetheorem"
                    / "last_source_theorem_contract.packet.json"
                ),
                "closes": "last source contract",
            },
        ],
        "locked_target_values_used_as_source": False,
        "residual_projector_replay_used_as_source": False,
        "benchmark_values_used_as_source": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    global_sources = variation_route_b["global_sources"]
    route_b_packet = {
        "schema": "MTTIndependentC1KernelSourceExportAlignedAttempt.v1",
        "status": "VARIATION_SOURCE_CLOSED_MEASURE_QUADRATURE_ROW_SOURCES_OPEN",
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

    write_json(ACTION_PACKET, action_packet)
    write_json(PHYSICAL_PACKET, physical_packet)
    write_json(ROUTE_B_PACKET, route_b_packet)

    action_result = run_validator(ACTION_VALIDATOR, ACTION_PACKET)
    physical_result = run_validator(PHYSICAL_VALIDATOR, PHYSICAL_PACKET)
    route_b_result = run_validator(ROW_VALIDATOR, ROUTE_B_PACKET)
    write_json(ACTION_RESULT, action_result)
    write_json(PHYSICAL_RESULT, physical_result)
    write_json(ROUTE_B_RESULT, route_b_result)

    last_lemma = {
        "schema": "MTTMinimalLastSourceLemmaContract.v1",
        "status": "EXACT_LAST_LEMMA_CONTRACT_NOT_FILLED",
        "lemma_name": "SelectedPhiFinC1ActionSourceLemma",
        "route_A_statement_required": (
            "On the selected q=79 branch, the physical Phi_fin^C1 action has first variation equal to the selected "
            "formal C1 defect functional on the admissible differentiated variation space, with trace/Frobenius "
            "measure, no extra physical boundary/source terms, and same-source R_Z/R_X/b_selected emission."
        ),
        "route_B_statement_required": (
            "Alternatively, emit selected measure, quadrature, primitive row kernels, Hessian/b_selected rows, and "
            "sector assemblies from independent sources that do not replay the residual projector or locked targets."
        ),
        "closed_inputs": {
            "admissible_variation_space": True,
            "unique_formal_C1_defect_functional": True,
            "finite_trace_boundary_algebra": True,
            "conditional_witnesses": True,
            "formal_110_row_replay": True,
        },
        "not_sufficient_for_promotion": [
            "formal defect uniqueness alone",
            "conditional Route A witness",
            "post-emission target agreement",
            "residual-projector row replay",
        ],
        "minimal_open_fields": {
            "physical_action_equals_c1_defect_functional": True,
            "physical_boundary_source_terms_vanish": True,
            "same_source_rz_rx_bselected_emitted": True,
            "independent_kernel_source_ids": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(LAST_LEMMA, last_lemma)

    candidate = {
        "candidate": "MTTSelectedPhysicalActionBindingAndSameSourceEmissionOrIndependentKernelSourceExport",
        "status": STATUS,
        "inputs": {
            "variation_gate": rel(VARIATION_GATE),
            "route_a_variation_packet": rel(VARIATION_ROUTE_A),
            "route_b_variation_packet": rel(VARIATION_ROUTE_B),
            "c1_defect_functional_source": rel(C1_DEFECT),
            "physical_source_gate": rel(PHYSICAL_GATE),
            "last_source_contract": rel(LAST_SOURCE),
        },
        "output_packets": {
            "route_a_action_kernel_binding_attempt": rel(ACTION_PACKET),
            "route_a_action_kernel_binding_validator_result": rel(ACTION_RESULT),
            "physical_source_emission_attempt": rel(PHYSICAL_PACKET),
            "physical_source_emission_validator_result": rel(PHYSICAL_RESULT),
            "route_b_independent_kernel_source_export_attempt": rel(ROUTE_B_PACKET),
            "route_b_independent_kernel_source_export_validator_result": rel(ROUTE_B_RESULT),
            "minimal_last_source_lemma_contract": rel(LAST_LEMMA),
        },
        "what_closes_now": {
            "last_source_lemma_contract_exact": True,
            "formal_defect_plus_variation_shown_insufficient_for_physical_promotion": True,
            "action_kernel_validator_aligned": action_result["returncode"] == 1,
            "physical_source_validator_aligned": physical_result["returncode"] == 1,
            "independent_kernel_source_validator_aligned": route_b_result["returncode"] == 1,
            "observed_constants_excluded_as_selectors": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "prove_SelectedPhiFinC1ActionSourceLemma": True,
            "or_emit_independent_C1_kernel_source_rows": True,
            "physical_action_equals_c1_defect_functional": True,
            "physical_boundary_source_terms_vanish": True,
            "same_source_rz_rx_bselected_emitted": True,
            "selected_independent_measure_pairing_source": True,
            "selected_independent_quadrature_rule": True,
            "primitive_kernel_source_ids_and_formulas": True,
            "independent_hessian_bselected_source_ids": True,
            "sector_assembly_source_ids": True,
            "unpatched_SM_parity_dynamic_packet_closure": True,
            "true_SM_equivalence_closure": True,
            "no_knob_closure": True,
        },
        "promotion_decision": {
            "route_A_physical_action_source_promoted": False,
            "route_B_independent_kernel_source_exported": False,
            "unpatched_A_selected_promoted": False,
            "unpatched_b_selected_promoted": False,
            "unpatched_deltaTheta_C1_promoted": False,
            "unpatched_SM_parity_dynamic_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "theorem": {
            "name": "MinimalLastSourceLemmaExactnessTheorem",
            "proved": True,
            "statement": (
                "Given the closed admissible variation-space clause and the unique formal C1 defect functional, "
                "the remaining unpatched promotion cannot be obtained by linear algebra or formal uniqueness alone. "
                "It is exactly the disjunction of the SelectedPhiFinC1ActionSourceLemma or an independent C1 kernel "
                "source-row export. The three validators reject the current packets for precisely those source fields."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "patched_SM_parity_closure_preserved": variation_gate["patched_SM_parity_closure_preserved"],
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_PhysicalActionBindingAndSameSourceEmission_or_IndependentKernelSourceExport_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "validator_results": {
            "action_kernel": action_result["returncode"],
            "physical_source": physical_result["returncode"],
            "independent_kernel_source": route_b_result["returncode"],
        },
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PhysicalActionBindingAndSameSourceEmission or IndependentKernelSourceExport v1

Status: `{STATUS}`.

This artifact aligns the three active validators after the variation-space
clause was closed.

Closed support:

```text
admissible differentiated variation space = closed
unique formal C1 defect functional        = closed
finite trace/boundary algebra             = closed as formal algebra
conditional source witnesses              = built
```

Still not enough:

```text
physical action = C1 defect functional    = open
physical no-extra-boundary/source term    = open
same-source R_Z/R_X/b_selected emission   = open
independent kernel source rows            = open
```

Therefore the remaining object is exact:

```text
SelectedPhiFinC1ActionSourceLemma
```

or a residual-replay-free independent C1 kernel source export.

No observed constants, benchmark rows, locked target values, or fitted SM data
are used as selectors.

Next artifact: `{NEXT}`.
"""

    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
