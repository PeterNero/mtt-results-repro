"""Build PhiFinC1 minimization / independent quadrature table gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
DRAFT_DIR = CORPUS / "paper_appendix_drafts" / "selected_source"

PREVIOUS = DATA / "selected_c1defectfunctionalsource_or_independentquadraturedatafill.candidate.json"
FUNCTIONAL_SOURCE = (
    DATA
    / "selected_c1defectfunctionalsource_or_independentquadraturedatafill"
    / "c1_defect_functional_uniqueness_source.packet.json"
)
APPLICATION_GAP = (
    DATA
    / "selected_c1defectfunctionalsource_or_independentquadraturedatafill"
    / "phifinc1_physical_application_source_gap.packet.json"
)
QUADRATURE_ATTEMPT = (
    DATA
    / "selected_c1defectfunctionalsource_or_independentquadraturedatafill"
    / "independent_quadrature_data_fill_attempt.packet.json"
)
SOURCE_DRAFTS = DATA / "selected_source_paper_appendix_drafts.candidate.json"

SLUG = "selected_phifinc1minimizesdefectfunctional_or_independentquadraturetable"
OUTPUT = DATA / f"{SLUG}.candidate.json"
PACKET_DIR = DATA / SLUG
MINIMIZER_BINDING = PACKET_DIR / "phifinc1_minimizer_binding_reduction.packet.json"
QUADRATURE_TEMPLATE = PACKET_DIR / "independent_quadrature_table_template.packet.json"
PAPER_DRAFT = DRAFT_DIR / "theta_execution_flavor__i10_phifinc1_minimizes_c1_defect_functional.md"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PhiFinC1MinimizesDefectFunctional_or_IndependentQuadratureTable_v1.md"

STATUS = "MTT_SELECTED_PHIFINC1MINIMIZESDEFECTFUNCTIONAL_OR_INDEPENDENTQUADRATURETABLE_BUILT_BINDING_REDUCTION_OPEN"
NEXT = "MTT_Selected_MinimizerTraceC1PayloadTheorem_or_QuadratureTableValues_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    DRAFT_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    functional = load(FUNCTIONAL_SOURCE)
    application = load(APPLICATION_GAP)
    quadrature = load(QUADRATURE_ATTEMPT)
    source_drafts = load(SOURCE_DRAFTS)
    replay = previous["replay_if_physical_application_or_independent_data_supplied"]

    insertion_index = source_drafts["insertion_index"]
    i1 = insertion_index["I1_selected_strominger_minimizer_to_phifin_trace"]
    i5 = insertion_index["I5_dotD_alpha1_and_C1_response"]

    minimizer_binding = {
        "schema": "MTTPhiFinC1MinimizerBindingReduction.v1",
        "status": "REDUCED_TO_MINIMIZER_TRACE_AND_C1_RESPONSE_THEOREM_SLOTS",
        "physical_application_needed": application["remaining_physical_application_rule"]["needed_statement"],
        "formal_functional_available": functional["functional_name"],
        "existing_source_theorem_slots": {
            "I1_selected_strominger_minimizer_to_phifin_trace": {
                "status": i1["status"],
                "dependencies": i1["dependencies"],
                "target_papers": i1["target_papers"],
                "validation_artifacts": i1["validation_artifacts"],
            },
            "I5_dotD_alpha1_and_C1_response": {
                "status": i5["status"],
                "dependencies": i5["dependencies"],
                "target_papers": i5["target_papers"],
                "validation_artifacts": i5["validation_artifacts"],
            },
        },
        "new_binding_theorem_slot": {
            "id": "I10_phifinc1_minimizes_c1_defect_functional",
            "statement": (
                "The C1 component of the selected Phi_fin trace of the q79/F,m=1 Strominger/HYM "
                "minimizer is the stationary/minimizing response of the unique C1DefectLeakageFunctional "
                "under selected boundary, static routing, and finite trace/Frobenius constraints."
            ),
            "dependencies": [
                "I1_selected_strominger_minimizer_to_phifin_trace",
                "I5_dotD_alpha1_and_C1_response",
                "C1DefectFunctionalUniquenessTheorem",
            ],
            "target_papers": ["theta_execution_flavor", "theta_nonabelian_overlaps", "strominger_system"],
            "draft_path": rel(PAPER_DRAFT),
        },
        "would_close_if_proved": application["if_supplied_then"],
        "proved_now": False,
        "why_not_proved_now": [
            "I1 minimizer-to-finite Phi_fin trace remains a proof slot, not a closed theorem",
            "I5 selected dotD/C1 response remains a proof slot, not a closed theorem",
            "the new I10 binding theorem is drafted here but not inserted/proved in the main corpus",
        ],
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    quadrature_template = {
        "schema": "MTTIndependentQuadratureTableTemplate.v1",
        "status": "TEMPLATE_READY_VALUES_EMPTY",
        "table_schema": {
            "zero_mode_basis_rows": ["basis_id", "sector", "normalization", "source_certificate", "coordinates"],
            "primitive_contraction_rows": [
                "sector",
                "response_column",
                "row",
                "col",
                "real_part",
                "imag_part",
                "quadrature_error_bound",
                "source_certificate",
            ],
            "hessian_source_rows": ["coordinate_index", "real_value", "error_bound", "source_certificate"],
            "sector_matrix_rows": ["sector", "row", "col", "real_part", "imag_part", "error_bound"],
        },
        "required_values": quadrature["required_values"],
        "acceptance_tests": quadrature["acceptance_tests"],
        "forbidden_shortcuts": quadrature["forbidden_shortcuts"],
        "values_filled_now": False,
        "would_close_if_filled": quadrature["if_supplied_then"],
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    draft = f"""# Appendix Slot I10: Phi_fin C1 Minimizes the Selected Defect Functional

## Theorem Slot I10

For the q79/F,m=1 Route-C branch, assume the selected Strominger/HYM minimizer
and finite `Phi_fin` trace of theorem slot I1, and the selected same-branch
`dotD_alpha1`/C1 response of theorem slot I5.

Then the C1 component of the selected differentiated `Phi_fin` trace is the
stationary response of the unique `C1DefectLeakageFunctional` under:

- selected static routing `Z -> u,e` and `X -> d,nuD`;
- selected finite trace/Frobenius normalization;
- selected fixed-fiber response span;
- no observed masses, mixings, CP phase, benchmark matrices, or target residuals.

If proved, the existing replay promotes:

```text
A^T A      = {replay["A_transpose_A"]}
A^T b      = {replay["A_transpose_b"]}
deltaTheta = {replay["deltaTheta_C1"]}
```

## Guardrail

This theorem may not be filled by copying the residual-projector axiom patch or
by fitting to observed SM flavor data. It must be derived from the selected
minimizer trace and selected differentiated C1 response, or replaced by an
independent quadrature/Hessian table.
"""
    PAPER_DRAFT.write_text(draft, encoding="utf-8")

    candidate = {
        "candidate": "MTTSelectedPhiFinC1MinimizesDefectFunctionalOrIndependentQuadratureTable",
        "status": STATUS,
        "inputs": {
            "previous_gate": rel(PREVIOUS),
            "functional_source": rel(FUNCTIONAL_SOURCE),
            "application_gap": rel(APPLICATION_GAP),
            "quadrature_attempt": rel(QUADRATURE_ATTEMPT),
            "source_appendix_drafts": rel(SOURCE_DRAFTS),
        },
        "output_packets": {
            "phifinc1_minimizer_binding_reduction": rel(MINIMIZER_BINDING),
            "independent_quadrature_table_template": rel(QUADRATURE_TEMPLATE),
            "paper_draft_I10": rel(PAPER_DRAFT),
        },
        "what_closes_now": {
            "physical_application_reduced_to_existing_minimizer_trace_stack": True,
            "new_I10_binding_theorem_slot_created": True,
            "independent_quadrature_table_template_created": True,
            "sufficiency_of_I10_or_quadrature_table_preserved": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "prove_I1_selected_minimizer_to_PhiFin_trace": True,
            "prove_I5_selected_dotD_C1_response": True,
            "prove_I10_PhiFinC1_minimizes_defect_functional": True,
            "fill_independent_quadrature_table_values": True,
            "unpatched_SM_parity_dynamic_packet_closure": True,
            "true_SM_equivalence_closure": True,
        },
        "promotion_decision": {
            "PhiFinC1_minimizes_defect_functional_proved": False,
            "independent_quadrature_table_values_filled": False,
            "unpatched_A_selected_promoted": False,
            "unpatched_b_selected_promoted": False,
            "unpatched_deltaTheta_C1_promoted": False,
            "unpatched_SM_parity_dynamic_packet_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "PhiFinC1BindingReductionTheorem",
            "proved": True,
            "statement": (
                "The physical Phi_fin^C1 minimization problem is reduced to a precise theorem slot: "
                "I10, dependent on the selected minimizer-to-Phi_fin trace I1, selected dotD/C1 response "
                "I5, and the already sourced unique C1 defect functional. Alternatively, the same closure "
                "can be bypassed by filling an independent quadrature/Hessian table with the declared schema."
            ),
        },
        "replay_if_I10_or_quadrature_table_proved": replay,
        "observed_data_used": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "patched_spine_closure_preserved": previous["patched_spine_closure_preserved"],
        "unpatched_theorem_closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_PhiFinC1MinimizesDefectFunctional_or_IndependentQuadratureTable_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "closure_claimed": False,
        "patched_spine_closure_preserved": candidate["patched_spine_closure_preserved"],
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PhiFinC1MinimizesDefectFunctional or IndependentQuadratureTable v1

Status: `{STATUS}`.

This gate reduces physical `Phi_fin^C1` minimization to a named theorem slot.

Closed now:

```text
I10 theorem slot created                    = True
depends on selected minimizer trace I1      = True
depends on selected dotD/C1 response I5     = True
quadrature table template created           = True
```

Still open:

```text
I10 proved                                  = False
independent quadrature values filled        = False
unpatched dynamic closure                   = False
```

Replay if either route is completed:

```text
A^T A      = {replay["A_transpose_A"]}
A^T b      = {replay["A_transpose_b"]}
deltaTheta = {replay["deltaTheta_C1"]}
```

Next artifact: `{NEXT}`.
"""

    MINIMIZER_BINDING.write_text(json.dumps(minimizer_binding, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    QUADRATURE_TEMPLATE.write_text(json.dumps(quadrature_template, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
