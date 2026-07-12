"""Build residual-projector axiom insertion / Galerkin C1 first-execution gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
DRAFT_DIR = CORPUS / "paper_appendix_drafts" / "selected_source"

PREVIOUS = DATA / "selected_differentiatedphifinc1_residualprojectoraxiom_or_galerkinc1execution.candidate.json"
AXIOM_CONTRACT = (
    DATA
    / "selected_differentiatedphifinc1_residualprojectoraxiom_or_galerkinc1execution"
    / "residual_projector_axiom_patch_contract.packet.json"
)
GALERKIN_CONTRACT = (
    DATA
    / "selected_differentiatedphifinc1_residualprojectoraxiom_or_galerkinc1execution"
    / "honest_galerkin_execution_acceptance_contract.packet.json"
)
IMPLICATION = (
    DATA
    / "selected_differentiatedphifinc1_residualprojectoraxiom_or_galerkinc1execution"
    / "closure_implication_replay.packet.json"
)

SLUG = "selected_residualprojectoraxiominsertion_or_galerkinc1firstexecution"
OUTPUT = DATA / f"{SLUG}.candidate.json"
PACKET_DIR = DATA / SLUG
AXIOM_INSERTION = PACKET_DIR / "residual_projector_axiom_insertion_package.packet.json"
GALERKIN_SPEC = PACKET_DIR / "galerkin_c1_first_execution_spec.packet.json"
DECISION = PACKET_DIR / "route_decision_and_next_inputs.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_ResidualProjectorAxiomInsertion_or_GalerkinC1FirstExecution_v1.md"

STATUS = "MTT_SELECTED_RESIDUALPROJECTORAXIOMINSERTION_OR_GALERKINC1FIRSTEXECUTION_BUILT_INSERTION_SPEC_OPEN"
NEXT = "MTT_Selected_GalerkinC1InputBasisFill_or_ResidualProjectorAxiomCorpusPatch_v1"

DRAFTS = {
    "theta_execution_flavor": DRAFT_DIR / "theta_execution_flavor__i9_differentiated_phifinc1_residual_projector_axiom.md",
    "theta_nonabelian_overlaps": DRAFT_DIR / "theta_nonabelian_overlaps__i9_differentiated_phifinc1_residual_projector_axiom.md",
    "strominger_system": DRAFT_DIR / "strominger_system__i9_differentiated_phifinc1_residual_projector_axiom.md",
}


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def draft_text(paper_key: str, axiom_name: str, replay: dict[str, Any]) -> str:
    title = {
        "theta_execution_flavor": "Theta Execution Flavor",
        "theta_nonabelian_overlaps": "Theta Nonabelian Overlaps",
        "strominger_system": "Strominger System",
    }[paper_key]
    return f"""# Appendix Slot I9: Differentiated Phi_fin C1 Residual-Projector Axiom

Target paper family: {title}.

## Theorem Slot I9

Let the selected q79/F,m=1 Route-C static source packet be fixed, with the
selected qutrit Weyl carrier, active shift `(1,1)`, the selected fixed-fiber
quotient class, static routing `Z -> u,e`, static routing `X -> d,nuD`, finite
trace normalization, and the selected alpha1/dotD driver.

The missing source statement is the `{axiom_name}`:

```text
differentiated Phi_fin^C1 applies Q_residual on the selected C1 packet,
Q_residual emits R_Z on the phase/clock lane and R_X on the shift/vertex lane,
and the same differentiated source rule emits b_selected.
```

If this theorem slot is proved or explicitly admitted as a guarded local axiom,
the already-verified replay gives:

```text
A^T A      = {replay["A_transpose_A"]}
A^T b      = {replay["A_transpose_b"]}
deltaTheta = {replay["deltaTheta_C1"]}
rank       = {replay["rank"]}
```

## Guardrail

This theorem slot must not be filled by observed masses, CKM/PMNS data, CP
phase, benchmark matrices, or target residual fitting. It must be proved from
the selected differentiated Phi_fin/C1 source rule or replaced by an honest
selected Galerkin C1 execution.
"""


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    DRAFT_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    axiom = load(AXIOM_CONTRACT)
    galerkin = load(GALERKIN_CONTRACT)
    implication = load(IMPLICATION)
    replay = implication["current_numeric_replay_if_axiom_accepted"]

    draft_paths = {}
    for key, path in DRAFTS.items():
        path.write_text(draft_text(key, axiom["axiom_name"], replay), encoding="utf-8")
        draft_paths[key] = rel(path)

    insertion_package = {
        "schema": "MTTResidualProjectorAxiomInsertionPackage.v1",
        "status": "PAPER_APPENDIX_DRAFTS_READY_NOT_CORPUS_PATCHED",
        "axiom_name": axiom["axiom_name"],
        "target_drafts": draft_paths,
        "paper_ready_theorem_slot": {
            "premises": axiom["premises_required"],
            "payload": axiom["new_axiom_payload_if_accepted"],
            "exact_source_values_to_emit": axiom["exact_source_values_to_emit"],
            "acceptance_tests": axiom["acceptance_tests"],
        },
        "after_insertion_replay": {
            "can_promote_A_selected_b_selected_deltaTheta_after_guarded_insertion": True,
            "numeric_replay": replay,
            "SM_parity_dynamic_packet_would_close": implication["if_axiom_contract_accepted_then"][
                "SM_parity_dynamic_packet_would_close"
            ],
            "no_knob_flavor_constants_would_close": implication["if_axiom_contract_accepted_then"][
                "no_knob_flavor_constants_would_close"
            ],
        },
        "inserted_into_main_corpus_now": False,
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    galerkin_spec = {
        "schema": "MTTSelectedGalerkinC1FirstExecutionSpec.v1",
        "status": "FIRST_EXECUTION_SPEC_READY_INPUT_BASIS_VALUES_MISSING",
        "strict_coordinate_target": galerkin["strict_coordinate_target"],
        "coordinate_order": {
            "sector_order": ["u", "e", "d", "nuD"],
            "per_sector_real_order": "Re(row-major 3x3) then Im(row-major 3x3)",
            "response_column_order": ["phase_clock_R_Z", "shift_vertex_R_X"],
        },
        "required_input_files": {
            "zero_mode_basis_packet": "candidate_data/selected_residualprojectoraxiominsertion_or_galerkinc1firstexecution/inputs/zero_mode_basis.packet.json",
            "primitive_contraction_terms_packet": "candidate_data/selected_residualprojectoraxiominsertion_or_galerkinc1firstexecution/inputs/primitive_contraction_terms.packet.json",
            "hessian_or_source_vector_packet": "candidate_data/selected_residualprojectoraxiominsertion_or_galerkinc1firstexecution/inputs/hessian_source_vector.packet.json",
            "sector_response_matrix_packet": "candidate_data/selected_residualprojectoraxiominsertion_or_galerkinc1firstexecution/inputs/sector_response_matrices.packet.json",
        },
        "required_outputs": galerkin["minimal_required_outputs"],
        "acceptance_tests": galerkin["acceptance_tests"],
        "first_execution_run_now": False,
        "why_not_run_now": [
            "zero-mode basis values are not yet present in this repo packet",
            "primitive 3x3 contraction terms are not yet emitted as selected source data",
            "hessian/source vector b_selected is not yet theorem-derived",
        ],
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    decision_packet = {
        "schema": "MTTResidualProjectorInsertionOrGalerkinFirstExecutionDecision.v1",
        "status": "TWO_ROUTES_READY_NEXT_INPUTS_SHARP",
        "route_A_residual_projector_axiom": {
            "ready_as_paper_appendix_draft": True,
            "main_corpus_patched_now": False,
            "would_close_dynamic_packet_after_guarded_acceptance": True,
            "risk": "adds a local axiom unless later derived from differentiated Phi_fin source theory",
        },
        "route_B_honest_galerkin_execution": {
            "ready_as_execution_spec": True,
            "run_now": False,
            "next_missing_inputs": list(galerkin_spec["required_input_files"].values()),
            "would_close_dynamic_packet_if_values_pass": True,
            "risk": "requires concrete selected basis and contraction values rather than structural support",
        },
        "recommended_next": NEXT,
        "superset_strategy": (
            "Two superset paths are kept in parallel but locked to the same 72-real target: "
            "Route A is the selected differentiated Phi_fin axiom/theorem path; Route B is "
            "the honest Galerkin execution path. Either may close SM-parity dynamic replay, "
            "but neither may use observed flavor constants as selectors."
        ),
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedResidualProjectorAxiomInsertionOrGalerkinC1FirstExecution",
        "status": STATUS,
        "inputs": {
            "previous_gate": rel(PREVIOUS),
            "axiom_contract": rel(AXIOM_CONTRACT),
            "galerkin_contract": rel(GALERKIN_CONTRACT),
            "closure_implication": rel(IMPLICATION),
        },
        "output_packets": {
            "residual_projector_axiom_insertion_package": rel(AXIOM_INSERTION),
            "galerkin_c1_first_execution_spec": rel(GALERKIN_SPEC),
            "route_decision_and_next_inputs": rel(DECISION),
        },
        "what_closes_now": {
            "residual_projector_axiom_appendix_drafts_written": True,
            "galerkin_first_execution_schema_fixed": True,
            "route_A_and_route_B_locked_to_same_72_real_target": True,
            "next_input_files_declared": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "patch_main_corpus_with_residual_projector_axiom_or_prove_it": True,
            "fill_zero_mode_basis_packet": True,
            "fill_primitive_contraction_terms_packet": True,
            "fill_hessian_source_vector_packet": True,
            "fill_sector_response_matrix_packet": True,
            "run_first_honest_Galerkin_C1_execution": True,
            "promote_A_selected": True,
            "promote_b_selected": True,
            "promote_deltaTheta_C1": True,
            "SM_parity_dynamic_packet_closure": True,
            "true_SM_equivalence_closure": True,
        },
        "promotion_decision": {
            "main_corpus_axiom_patch_applied_now": False,
            "residual_projector_axiom_proved_now": False,
            "first_Galerkin_C1_execution_run_now": False,
            "A_selected_promoted": False,
            "b_selected_promoted": False,
            "deltaTheta_C1_promoted": False,
            "SM_parity_dynamic_packet_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "ResidualProjectorInsertionOrFirstExecutionPreparationTheorem",
            "proved": True,
            "statement": (
                "The residual-projector axiom lane is now paper-insertion-ready and the honest "
                "Galerkin lane is now execution-spec-ready, both locked to the same 72-real C1 "
                "target and replay. This closes the preparation problem but not the source "
                "promotion problem: the main corpus patch/proof or concrete Galerkin input values "
                "are still required."
            ),
        },
        "observed_data_used": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_ResidualProjectorAxiomInsertion_or_GalerkinC1FirstExecution_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "axiom_insertion_packet_path": rel(AXIOM_INSERTION),
        "galerkin_spec_packet_path": rel(GALERKIN_SPEC),
        "decision_packet_path": rel(DECISION),
        "theorem_proved": True,
        "closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected ResidualProjectorAxiomInsertion or GalerkinC1FirstExecution v1

Status: `{STATUS}`.

This artifact prepares the two real ways forward.

Route A now has insertion-ready appendix drafts:

```text
{draft_paths["theta_execution_flavor"]}
{draft_paths["theta_nonabelian_overlaps"]}
{draft_paths["strominger_system"]}
```

Route B now has a first-execution schema with required packets for zero modes,
primitive contractions, `b_selected`, and sector matrices.

Both routes are locked to the same replay:

```text
A^T A      = {replay["A_transpose_A"]}
A^T b      = {replay["A_transpose_b"]}
deltaTheta = {replay["deltaTheta_C1"]}
rank       = {replay["rank"]}
```

Nothing is promoted yet. The next actual closure step is either to patch/prove
the residual-projector axiom in the main corpus or fill the first Galerkin input
packets and run the execution.

Next artifact: `{NEXT}`.
"""

    AXIOM_INSERTION.write_text(json.dumps(insertion_package, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    GALERKIN_SPEC.write_text(json.dumps(galerkin_spec, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    DECISION.write_text(json.dumps(decision_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
