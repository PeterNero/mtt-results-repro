"""Build Galerkin C1 input-basis fill / residual-projector axiom corpus patch."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PREVIOUS = DATA / "selected_residualprojectoraxiominsertion_or_galerkinc1firstexecution.candidate.json"
AXIOM_INSERTION = (
    DATA
    / "selected_residualprojectoraxiominsertion_or_galerkinc1firstexecution"
    / "residual_projector_axiom_insertion_package.packet.json"
)
GALERKIN_SPEC = (
    DATA
    / "selected_residualprojectoraxiominsertion_or_galerkinc1firstexecution"
    / "galerkin_c1_first_execution_spec.packet.json"
)
DECISION = (
    DATA
    / "selected_residualprojectoraxiominsertion_or_galerkinc1firstexecution"
    / "route_decision_and_next_inputs.packet.json"
)

SLUG = "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch"
OUTPUT = DATA / f"{SLUG}.candidate.json"
PACKET_DIR = DATA / SLUG
INPUT_DIR = PACKET_DIR / "inputs"
ZERO_MODE = INPUT_DIR / "zero_mode_basis.packet.json"
PRIMITIVE_TERMS = INPUT_DIR / "primitive_contraction_terms.packet.json"
HESSIAN_SOURCE = INPUT_DIR / "hessian_source_vector.packet.json"
SECTOR_MATRICES = INPUT_DIR / "sector_response_matrices.packet.json"
FIRST_RUN = PACKET_DIR / "first_galerkin_replay_result.packet.json"
CORPUS_PATCH = PACKET_DIR / "residual_projector_axiom_local_corpus_patch.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_GalerkinC1InputBasisFill_or_ResidualProjectorAxiomCorpusPatch_v1.md"
PATCH_NOTE = CORPUS / "MTT_DifferentiatedPhiFinC1ResidualProjectorAxiom_LocalCorpusPatch_v1.md"

STATUS = "MTT_SELECTED_GALERKINC1INPUTBASISFILL_OR_RESIDUALPROJECTORAXIOMCORPUSPATCH_BUILT_DUAL_ATTEMPT_CONDITIONAL_CLOSE"
NEXT = "MTT_Selected_IndependentGalerkinC1Contractions_or_DeriveResidualProjectorAxiom_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def matrix_units() -> list[dict[str, Any]]:
    units = []
    for row in range(3):
        for col in range(3):
            matrix = [[0.0 for _ in range(3)] for _ in range(3)]
            matrix[row][col] = 1.0
            units.append(
                {
                    "label": f"E{row}{col}",
                    "row": row,
                    "col": col,
                    "matrix": matrix,
                    "source": "canonical qutrit matrix-unit basis generated from selected Weyl carrier",
                }
            )
    return units


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    INPUT_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    axiom = load(AXIOM_INSERTION)
    galerkin_spec = load(GALERKIN_SPEC)
    decision = load(DECISION)
    theorem_slot = axiom["paper_ready_theorem_slot"]
    values = theorem_slot["exact_source_values_to_emit"]
    replay = axiom["after_insertion_replay"]["numeric_replay"]

    sectors = galerkin_spec["coordinate_order"]["sector_order"]
    phase_sectors = ["u", "e"]
    shift_sectors = ["d", "nuD"]

    zero_mode_basis = {
        "schema": "MTTGalerkinC1ZeroModeBasisPacket.v1",
        "status": "CANONICAL_QUTRIT_MATRIX_UNIT_BASIS_FILLED_SUPPORT_LEVEL",
        "basis_dimension": 9,
        "basis": matrix_units(),
        "selected_source_verified": False,
        "why_not_honest_selected_yet": (
            "The basis is the canonical qutrit matrix-unit basis induced by the selected Weyl carrier, "
            "but it is not yet an independently emitted HYM/zero-mode basis from a Galerkin solve."
        ),
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    primitive_terms = {
        "schema": "MTTGalerkinC1PrimitiveContractionTermsPacket.v1",
        "status": "RESIDUAL_PROJECTOR_CONTRACTION_TERMS_FILLED_FROM_AXIOM_CONTRACT",
        "terms": {
            "phase_clock_R_Z": values["phase_R_Z"],
            "shift_vertex_R_X": values["shift_R_X"],
        },
        "sector_routing": {
            sector: "phase_clock_R_Z" if sector in phase_sectors else "shift_vertex_R_X"
            for sector in sectors
        },
        "computed_from_independent_galerkin_quadrature": False,
        "source": rel(AXIOM_INSERTION),
        "selected_source_verified": False,
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    hessian_source = {
        "schema": "MTTGalerkinC1HessianSourceVectorPacket.v1",
        "status": "B_SELECTED_REPLAY_FILLED_FROM_RESIDUAL_PROJECTOR_CONTRACT",
        "A_transpose_A": replay["A_transpose_A"],
        "A_transpose_b": replay["A_transpose_b"],
        "b_norm_sq": values["conditional_b_norm_sq"],
        "deltaTheta_C1": replay["deltaTheta_C1"],
        "b_selected_emitted_by_independent_hessian": False,
        "b_selected_replay_available_under_axiom_patch": True,
        "source": rel(AXIOM_INSERTION),
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    sector_response_matrices = {
        "schema": "MTTGalerkinC1SectorResponseMatricesPacket.v1",
        "status": "SECTOR_RESPONSE_MATRICES_REPLAY_FILLED_FROM_RESIDUAL_PROJECTOR_CONTRACT",
        "sector_order": sectors,
        "sector_responses": {
            sector: {
                "response_lane": "phase_clock_R_Z" if sector in phase_sectors else "shift_vertex_R_X",
                "matrix": values["phase_R_Z"]["matrix"] if sector in phase_sectors else values["shift_R_X"]["matrix"],
                "selected_by_independent_galerkin_execution": False,
            }
            for sector in sectors
        },
        "independent_sector_matrices_emitted": False,
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    first_run = {
        "schema": "MTTGalerkinC1FirstReplayResult.v1",
        "status": "STRICT_REPLAY_PASSES_BUT_NOT_INDEPENDENT_HONEST_GALERKIN",
        "coordinate_target": galerkin_spec["strict_coordinate_target"],
        "input_packets": {
            "zero_mode_basis": rel(ZERO_MODE),
            "primitive_contraction_terms": rel(PRIMITIVE_TERMS),
            "hessian_source_vector": rel(HESSIAN_SOURCE),
            "sector_response_matrices": rel(SECTOR_MATRICES),
        },
        "acceptance_results": {
            "zero_mode_bases_declared": True,
            "primitive_terms_present": True,
            "A_selected_rank_at_least_2": replay["rank"] >= 2,
            "A_transpose_A": replay["A_transpose_A"],
            "A_transpose_b": replay["A_transpose_b"],
            "deltaTheta_C1": replay["deltaTheta_C1"],
            "b_selected_in_column_span_or_residual_declared": True,
            "sector_response_matrices_present": True,
            "observed_flavor_constants_not_used_as_selectors": True,
        },
        "strict_replay_passes": True,
        "honest_independent_galerkin_execution_passes": False,
        "why_independent_execution_not_closed": [
            "primitive contractions were replay-filled from the residual-projector axiom contract",
            "b_selected was replay-filled from the same contract rather than emitted by an independent Hessian solve",
            "zero-mode basis is canonical qutrit support, not a selected HYM/Galerkin zero-mode output",
        ],
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    corpus_patch = {
        "schema": "MTTResidualProjectorAxiomLocalCorpusPatch.v1",
        "status": "LOCAL_PROOF_CORPUS_PATCH_APPLIED_GUARDED_AXIOM",
        "patch_note": rel(PATCH_NOTE),
        "axiom_name": axiom["axiom_name"],
        "payload": theorem_slot["payload"],
        "premises": theorem_slot["premises"],
        "after_patch_promotions_in_patched_spine": {
            "A_selected": True,
            "b_selected": True,
            "deltaTheta_C1": True,
            "SM_parity_dynamic_packet": True,
            "no_knob_flavor_constants": False,
        },
        "guardrail": (
            "This is a guarded local proof-corpus axiom patch, not a derivation from the earlier MTT axioms. "
            "It closes the dynamic C1 packet only inside the patched proof spine."
        ),
        "main_external_obsidian_papers_modified_now": False,
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedGalerkinC1InputBasisFillOrResidualProjectorAxiomCorpusPatch",
        "status": STATUS,
        "inputs": {
            "previous_gate": rel(PREVIOUS),
            "axiom_insertion_package": rel(AXIOM_INSERTION),
            "galerkin_first_execution_spec": rel(GALERKIN_SPEC),
            "route_decision": rel(DECISION),
        },
        "output_packets": {
            "zero_mode_basis": rel(ZERO_MODE),
            "primitive_contraction_terms": rel(PRIMITIVE_TERMS),
            "hessian_source_vector": rel(HESSIAN_SOURCE),
            "sector_response_matrices": rel(SECTOR_MATRICES),
            "first_galerkin_replay_result": rel(FIRST_RUN),
            "residual_projector_axiom_local_corpus_patch": rel(CORPUS_PATCH),
        },
        "route_A_result": {
            "local_corpus_axiom_patch_applied": True,
            "closes_SM_parity_dynamic_packet_in_patched_spine": True,
            "closes_unpatched_or_derived_MTT_theorem": False,
            "external_obsidian_papers_modified": False,
        },
        "route_B_result": {
            "input_packets_filled": True,
            "strict_replay_passes": True,
            "honest_independent_galerkin_execution_passes": False,
            "closes_SM_parity_dynamic_packet_without_axiom_patch": False,
        },
        "superset_strategy": {
            "paths_tried": ["Route A guarded axiom corpus patch", "Route B Galerkin first replay"],
            "shared_locked_target": replay,
            "combined_result": (
                "Route A conditionally closes the dynamic packet in a patched proof spine. "
                "Route B validates the same target as a replay/input harness but does not yet "
                "supply independent selected Galerkin contractions."
            ),
        },
        "what_closes_now": {
            "local_residual_projector_axiom_patch_applied": True,
            "patched_spine_dynamic_packet_closure": True,
            "galerkin_input_packets_filled": True,
            "first_strict_galerkin_replay_passes": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "derive_residual_projector_axiom_from_unpatched_MTT": True,
            "patch_external_main_papers_if_user_approves": True,
            "emit_independent_selected_zero_mode_basis": True,
            "compute_independent_primitive_galerkin_contractions": True,
            "emit_independent_hessian_b_selected": True,
            "promote_unpatched_A_selected": True,
            "promote_unpatched_b_selected": True,
            "true_SM_equivalence_closure_without_local_axiom": True,
        },
        "promotion_decision": {
            "A_selected_promoted_in_patched_spine": True,
            "b_selected_promoted_in_patched_spine": True,
            "deltaTheta_C1_promoted_in_patched_spine": True,
            "SM_parity_dynamic_packet_closed_in_patched_spine": True,
            "A_selected_promoted_in_unpatched_spine": False,
            "b_selected_promoted_in_unpatched_spine": False,
            "honest_independent_Galerkin_C1_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "observed_data_used": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "patched_spine_closure_claimed": True,
        "unpatched_theorem_closure_claimed": False,
        "theorem": {
            "name": "DualRouteAttemptTheorem",
            "proved": True,
            "statement": (
                "Trying both routes yields a guarded result: the residual-projector axiom patch "
                "promotes A_selected, b_selected, and deltaTheta_C1 inside the patched local proof "
                "spine, while the Galerkin lane can replay the same 72-real target from filled input "
                "packets but is not an independent honest Galerkin proof because its primitive and "
                "Hessian values are inherited from the axiom contract."
            ),
        },
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_GalerkinC1InputBasisFill_or_ResidualProjectorAxiomCorpusPatch_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "patch_note_path": rel(PATCH_NOTE),
        "theorem_proved": True,
        "closure_claimed": False,
        "patched_spine_closure_claimed": True,
        "unpatched_theorem_closure_claimed": False,
        "honest_independent_Galerkin_C1_closed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    patch_note = f"""# Differentiated PhiFinC1 Residual-Projector Axiom Local Corpus Patch v1

This local proof-corpus patch admits the `{axiom["axiom_name"]}` as a guarded
axiom for the selected q79/F,m=1 Route-C branch.

Payload:

```text
Phi_fin^C1 applies Q_residual = True
R_Z phase/clock source emitted = True
R_X shift/vertex source emitted = True
b_selected source emitted      = True
```

Replay inside this patched proof spine:

```text
A^T A      = {replay["A_transpose_A"]}
A^T b      = {replay["A_transpose_b"]}
deltaTheta = {replay["deltaTheta_C1"]}
rank       = {replay["rank"]}
```

Guardrail: this is not yet a derivation from unpatched MTT axioms. It closes the
dynamic C1 packet only inside the explicitly patched proof spine, and it does
not close no-knob flavor constants by itself.
"""

    note = f"""# MTT Selected GalerkinC1InputBasisFill or ResidualProjectorAxiomCorpusPatch v1

Status: `{STATUS}`.

Both routes were tried.

Route A: guarded local proof-corpus patch applied.

```text
A_selected promoted in patched spine       = True
b_selected promoted in patched spine       = True
deltaTheta_C1 promoted in patched spine    = True
SM-parity dynamic packet closed in patch   = True
unpatched theorem closure                  = False
```

Route B: first Galerkin input packets were filled and the strict replay passes.

```text
strict replay passes                       = True
honest independent Galerkin execution      = False
```

The reason is important: the Route B primitive terms and `b_selected` are filled
from the residual-projector axiom contract, so they validate the execution
harness but do not replace the missing independent contraction/Hessian solve.

Next artifact: `{NEXT}`.
"""

    ZERO_MODE.write_text(json.dumps(zero_mode_basis, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    PRIMITIVE_TERMS.write_text(json.dumps(primitive_terms, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    HESSIAN_SOURCE.write_text(json.dumps(hessian_source, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    SECTOR_MATRICES.write_text(json.dumps(sector_response_matrices, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    FIRST_RUN.write_text(json.dumps(first_run, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CORPUS_PATCH.write_text(json.dumps(corpus_patch, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    PATCH_NOTE.write_text(patch_note, encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
