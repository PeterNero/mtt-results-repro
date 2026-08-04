"""Build proof attempt/countermodel for the minimal finite C1 source-promotion lemma."""

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

SLUG = "selected_minimalfinitec1sourcepromotionlemma_proof_or_countermodel"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
OBLIGATIONS = PACKET_DIR / "minimal_lemma_obligation_status.packet.json"
SUBLEMMA = PACKET_DIR / "typed_row_functor_sublemma.packet.json"
COUNTERMODEL = PACKET_DIR / "closed_support_not_enough_countermodel.packet.json"
NEXT_KERNEL = PACKET_DIR / "next_source_promotion_kernel.packet.json"
VALIDATOR_RESULT = PACKET_DIR / "countermodel_validator_result.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_MinimalFiniteC1SourcePromotionLemma_Proof_or_Countermodel_v1.md"
VALIDATOR = ROOT / "scripts" / "validate_selected_physicalphifinc1_action_or_independent_rowkernel_source.py"

STATUS = "MTT_SELECTED_MINIMALFINITEC1SOURCEPROMOTIONLEMMA_PARTIAL_PROOF_COUNTERMODEL_BUILT"
NEXT = "MTT_Selected_PreResidualVariationAndHessianSourceKernel_Proof_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def run_validator(path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(path)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return {
        "payload": rel(path),
        "validator": rel(VALIDATOR),
        "returncode": proc.returncode,
        "stdout": proc.stdout.strip(),
        "stderr_lines": proc.stderr.splitlines(),
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_sourcetheorem_push_attempt_or_minimalnewlemma.candidate.json")
    lemma = load(
        DATA
        / "selected_sourcetheorem_push_attempt_or_minimalnewlemma"
        / "minimal_selected_finitec1_source_promotion_lemma.packet.json"
    )
    current = load(
        DATA
        / "selected_physicalphifinc1action_or_independentrowkernelsource_theorem"
        / "current_two_exit_source_attempt.packet.json"
    )
    basis = load(
        DATA
        / "selected_routeb_selectedbasisindependencefill_or_rowsourcegap"
        / "route_b_selected_basis_independence_fill.packet.json"
    )
    shape = load(
        DATA
        / "selected_variationoperatorshapecompatibility_or_hessiansourcegap"
        / "variation_operator_shape_compatibility.packet.json"
    )
    row_exec = load(
        DATA
        / "selected_firstrowprovenancepromotion_or_allrowsweylexecution"
        / "all_72_exact_weyl_row_execution.packet.json"
    )
    formal_110 = load(
        DATA
        / "selected_allrowsprovenancepromotion_or_physicalphifinc1actionsource"
        / "formal_110_row_replay_integrated.packet.json"
    )
    hessian_gap = load(
        DATA
        / "selected_hessiancountertermsource_bvector_theoremtemplate"
        / "remaining_hessian_bvector_source_gap.packet.json"
    )
    weyl_poly = load(
        DATA
        / "selected_residual_weylpolynomial_source_theorem_attempt"
        / "residual_weyl_polynomial_decomposition.packet.json"
    )

    basis_summary = basis["route_B_independent_execution"]["selected_basis_independence_certificate"]["basis_summary"]
    required_sector_basis = ["Q", "u", "d", "L", "e", "N", "H"]
    typed_row_functor_proved = (
        all(basis_summary[name]["source_verified_by_transport_conjugation"] for name in required_sector_basis)
        and row_exec["row_count"] == 72
        and row_exec["response_counts"]["phase"] == 36
        and row_exec["response_counts"]["shift"] == 36
        and formal_110["row_counts"]["primitive_rows"] == 72
        and formal_110["row_counts"]["sector_matrix_rows"] == 36
        and formal_110["row_counts"]["hessian_source_rows"] == 2
    )

    sublemma = {
        "schema": "MTTTypedFiniteC1RowFunctorSublemma.v1",
        "status": "TYPED_ROW_FUNCTOR_PROVED_SOURCE_VALUES_NOT_PROMOTED",
        "sublemma_name": "TypedFiniteC1RowFunctorSublemma",
        "proved": typed_row_functor_proved,
        "statement": (
            "The transported selected bases and finite C1 trace/Frobenius pairing define the typed 72 primitive "
            "row-functional slots and the 110-row target shape: 72 primitive rows, 36 sector rows, and 2 Hessian/source rows."
        ),
        "basis_sectors_checked": required_sector_basis,
        "row_counts": formal_110["row_counts"],
        "primitive_response_counts": row_exec["response_counts"],
        "closes_for_minimal_lemma": {
            "basis_to_rows_typing": True,
            "row_count_and_coordinate_contract": True,
            "sector_and_hessian_slot_count": True,
        },
        "does_not_close": {
            "pre_residual_variation_operator_source": True,
            "same_source_hessian_b_selected_emission": True,
            "sector_rows_source_assembly": True,
            "full_independence_from_residual_projector_replay": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    countermodel = {
        "schema": "MTTClosedSupportNotEnoughCountermodel.v1",
        "status": "COUNTERMODEL_TO_DERIVING_SOURCE_PROMOTION_FROM_CLOSED_SUPPORT_ONLY",
        "description": (
            "This is the existing current two-exit packet read as a model of the closed support facts. It satisfies "
            "finite quotient, trace measure, selected basis independence, shape compatibility, formal Hessian target, "
            "and all 110 algebraic values, while the source-promotion fields remain false and the strict validator rejects it."
        ),
        "closed_support_facts_true": lemma["support_already_available"],
        "additional_structural_support_true": {
            "typed_row_functor_sublemma": typed_row_functor_proved,
            "all_72_exact_values": row_exec["computed_value_clause_closed_for_all_rows"],
            "weyl_polynomial_decomposition_exact": weyl_poly["status"] == "EXACT_LOW_DEGREE_WEYL_POLYNOMIAL_DECOMPOSITION_COMPUTED",
            "formal_110_replay_integrated": formal_110["formal_110_rows_executed"],
        },
        "source_promotion_fields_false": {
            "pre_residual_phase_shift_source": shape["operator_shapes_selected_as_source_now"],
            "source_map_selected_by_MTT_now": shape["source_map_selected_by_MTT_now"],
            "hessian_b_selected_source": not hessian_gap["not_closed"]["selected_b_vector_source"],
            "sector_rows_physical_source_promoted": formal_110["sector_matrix_rows"]["physical_source_promoted"],
            "primitive_rows_provenance_independent_of_residual_projector": row_exec[
                "provenance_independent_of_residual_projector_replay_for_all_rows"
            ],
        },
        "therefore": (
            "The full SelectedFiniteC1SourcePromotionLemma cannot be proved from the already-closed support facts alone. "
            "A genuinely new source kernel must promote pre-residual variation operators and the Hessian/source vector."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    obligations = {
        "schema": "MTTMinimalFiniteC1SourcePromotionLemmaObligationStatus.v1",
        "status": "MAXIMAL_SAFE_PROGRESS_RECORDED_FULL_LEMMA_OPEN",
        "lemma": lemma["lemma_name"],
        "obligations": [
            {
                "id": "basis_to_rows",
                "status": "PARTIALLY_PROVED_AS_TYPED_ROW_FUNCTOR",
                "proved": True,
                "source": rel(SUBLEMMA),
                "limitation": "typing/counting and selected basis feed are proved; source values are not promoted by this alone",
            },
            {
                "id": "pre_residual_operators",
                "status": "OPEN_SOURCE_SELECTION_NOT_PROVED",
                "proved": False,
                "support": rel(
                    DATA
                    / "selected_residual_weylpolynomial_source_theorem_attempt"
                    / "residual_weyl_polynomial_decomposition.packet.json"
                ),
                "limitation": "exact Weyl polynomial and shape compatibility exist, but operator source selection remains false",
            },
            {
                "id": "hessian_source_rows",
                "status": "OPEN_FORMAL_TARGET_ONLY",
                "proved": False,
                "support": rel(
                    DATA
                    / "selected_hessiancountertermsource_bvector_theoremtemplate"
                    / "remaining_hessian_bvector_source_gap.packet.json"
                ),
                "limitation": "formal b/Hessian target exists, but same-source b_selected emission is still open",
            },
            {
                "id": "sector_assembly",
                "status": "PARTIALLY_PROVED_AS_SLOT_ASSEMBLY_SOURCE_PROMOTION_OPEN",
                "proved": False,
                "source": rel(SUBLEMMA),
                "limitation": "36 sector slots are integrated in the 110-row packet, but physical/source promotion is false",
            },
            {
                "id": "independence_guardrail",
                "status": "OPEN_FOR_VALUES_CLOSED_FOR_MEASURE_AND_BASIS",
                "proved": False,
                "limitation": "measure and basis are independent; primitive values still report residual-projector provenance dependence",
            },
        ],
        "full_lemma_proved": False,
        "countermodel_to_closed_support_only": rel(COUNTERMODEL),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_kernel = {
        "schema": "MTTNextPreResidualVariationAndHessianSourceKernel.v1",
        "status": "NEXT_KERNEL_SHARPENED",
        "kernel_name": "PreResidualVariationAndHessianSourceKernel",
        "must_emit": [
            {
                "id": "selected_variation_functional",
                "statement": "a source-selected finite C1 first-variation functional D Phi_fin^C1 whose phase/shift columns are R_Z/R_X before residual projection",
            },
            {
                "id": "same_source_hessian",
                "statement": "the Hessian counterterm/source vector b_selected emitted by the same functional, not by the locked A^T b target",
            },
            {
                "id": "sector_functor",
                "statement": "36 sector rows functorially assembled from the promoted primitive and Hessian source rows",
            },
            {
                "id": "independence_certificate",
                "statement": "a certificate that residual projector replay, benchmark constants, and locked target values are postchecks only",
            },
        ],
        "accepted_proof_routes": [
            "derive from physical Phi_fin^C1 action restriction with zero boundary/source term",
            "derive from independent selected Galerkin/quadrature execution of the finite C1 row kernels",
            "derive from a new selected pre-residual Weyl variation principle plus same-source Hessian emission",
        ],
        "rejected_routes": [
            "reuse exact R_Z/R_X decomposition as source selection",
            "reuse A^T b=(12,12) or deltaTheta=(1,1) as b_selected source",
            "reuse observed SM values or benchmark profiles as source selectors",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    SUBLEMMA.write_text(json.dumps(sublemma, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    COUNTERMODEL.write_text(json.dumps(countermodel, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OBLIGATIONS.write_text(json.dumps(obligations, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NEXT_KERNEL.write_text(json.dumps(next_kernel, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    validator_result = run_validator(
        DATA
        / "selected_physicalphifinc1action_or_independentrowkernelsource_theorem"
        / "current_two_exit_source_attempt.packet.json"
    )
    VALIDATOR_RESULT.write_text(json.dumps(validator_result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    candidate = {
        "candidate": "MTTSelectedMinimalFiniteC1SourcePromotionLemmaProofOrCountermodel",
        "status": STATUS,
        "inputs": {
            "previous_conditional_lemma": previous["output_packets"]["minimal_new_lemma"],
            "current_two_exit_packet": rel(
                DATA
                / "selected_physicalphifinc1action_or_independentrowkernelsource_theorem"
                / "current_two_exit_source_attempt.packet.json"
            ),
            "all_72_exact_rows": rel(
                DATA
                / "selected_firstrowprovenancepromotion_or_allrowsweylexecution"
                / "all_72_exact_weyl_row_execution.packet.json"
            ),
            "formal_110_rows": rel(
                DATA
                / "selected_allrowsprovenancepromotion_or_physicalphifinc1actionsource"
                / "formal_110_row_replay_integrated.packet.json"
            ),
        },
        "output_packets": {
            "obligation_status": rel(OBLIGATIONS),
            "typed_row_functor_sublemma": rel(SUBLEMMA),
            "closed_support_not_enough_countermodel": rel(COUNTERMODEL),
            "next_source_promotion_kernel": rel(NEXT_KERNEL),
            "countermodel_validator_result": rel(VALIDATOR_RESULT),
        },
        "theorem": {
            "name": "ClosedSupportNotEnoughAndTypedRowFunctorTheorem",
            "proved": True,
            "statement": (
                "The selected basis and finite trace pairing prove the typed row-functor/slot structure, but the closed support facts "
                "do not imply the full source-promotion lemma. The current two-exit packet is a countermodel: it satisfies the closed "
                "support facts while failing the source-promotion fields and strict validator."
            ),
        },
        "what_closes_now": {
            "typed_row_functor_sublemma": typed_row_functor_proved,
            "closed_support_not_enough_countermodel": validator_result["returncode"] == 1,
            "next_source_kernel_identified": True,
        },
        "what_remains_open": {
            "pre_residual_variation_operator_source": True,
            "same_source_hessian_b_selected_emission": True,
            "sector_rows_source_assembly": True,
            "full_independence_from_residual_projector_replay": True,
        },
        "full_minimal_lemma_proved": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_MinimalFiniteC1SourcePromotionLemma_Proof_or_Countermodel_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "typed_row_functor_sublemma_proved": typed_row_functor_proved,
        "full_minimal_lemma_proved": False,
        "countermodel_validator_rejects": validator_result["returncode"] == 1,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected MinimalFiniteC1SourcePromotionLemma Proof or Countermodel v1

Status: `{STATUS}`.

We tried to prove the minimal source-promotion lemma. The maximal safe result is
sharper and more useful:

```text
typed row-functor sublemma proved       = {typed_row_functor_proved}
full source-promotion lemma proved      = False
current packet still rejected           = {validator_result["returncode"] == 1}
closure claimed                         = False
```

What is proved: the transported selected bases plus finite C1 trace/Frobenius
pairing define the typed row-functional shape: `72` primitive rows, `36` sector
rows, and `2` Hessian/source rows.

What is not proved: the values are not yet selected source emissions. Exact
`R_Z/R_X` Weyl polynomials and formal `b_selected` targets remain support unless
a new source kernel emits them before residual replay and locked-target
postchecks.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
