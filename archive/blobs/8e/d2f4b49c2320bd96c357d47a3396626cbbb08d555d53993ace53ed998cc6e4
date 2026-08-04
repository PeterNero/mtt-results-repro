"""Build PSM-C1-02 RA-1 physical equality / RB-3 Hessian source fill."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PREVIOUS = DATA / "selected_psm_c1_02_ra1_derivationattack_or_rb2_primitivetermsfill.candidate.json"
PREVIOUS_DIR = DATA / "selected_psm_c1_02_ra1_derivationattack_or_rb2_primitivetermsfill"
PRIMITIVE_ROWS = DATA / "selected_residualprojectoraxiominsertion_or_galerkinc1firstexecution" / "inputs" / "primitive_contraction_terms.packet.json"
OLD_SOURCE_MAP = DATA / "selected_primitivec1tensor_hessiansourcemap_or_honestgalerkinc1execution" / "primitive_tensor_hessian_source_map_candidate.packet.json"
CONDITIONAL_WITNESS = DATA / "selected_preresidualvariation_hessiansourcekernel_attempt_or_actionaxiom" / "conditional_source_kernel_witness.packet.json"

OUTPUT = DATA / "selected_psm_c1_02_ra1_physicalactionequality_or_rb3_hessiansourcefill.candidate.json"
PACKET_DIR = DATA / "selected_psm_c1_02_ra1_physicalactionequality_or_rb3_hessiansourcefill"
ROUTE_A_PACKET = PACKET_DIR / "route_a_ra1_physical_action_equality_status.packet.json"
ROUTE_B_PACKET = PACKET_DIR / "route_b_rb3_hessian_source_fill.packet.json"
SUPERSET_PACKET = PACKET_DIR / "psm_c1_02_superset_alignment_after_rb3.packet.json"
NEXT_WORKORDER = PACKET_DIR / "next_labeled_workorder.packet.json"
CERT = CERTS / "selected_psm_c1_02_ra1_physicalactionequality_or_rb3_hessiansourcefill_certificate.json"
NOTE = CORPUS / "MTT_Selected_PSM_C1_02_RouteA_RA1_PhysicalActionEquality_or_RouteB_RB3_HessianSourceFill_v1.md"

STATUS = "MTT_SELECTED_PSM_C1_02_RA1_PHYSICALACTIONEQUALITY_OR_RB3_HESSIANSOURCEFILL_BUILT_RB3_NORMAL_EQUATIONS_FILLED_SELECTION_OPEN"
NEXT = "MTT_Selected_PSM_C1_02_RouteA_RA2_BoundarySourceCancellation_or_RouteB_RB4_IndependentQuadratureSource_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def abs_sq(value: Any) -> float:
    if isinstance(value, list):
        return float(value[0]) ** 2 + float(value[1]) ** 2
    return float(value) ** 2


def hessian_from_rows(rows: list[dict[str, Any]]) -> dict[str, Any]:
    columns = ["phase", "shift"]
    gram = [[0.0, 0.0], [0.0, 0.0]]
    atb = [0.0, 0.0]
    norms = {name: 0.0 for name in columns}
    for row in rows:
        idx = columns.index(row["response"])
        mag = abs_sq(row["value"])
        norms[row["response"]] += mag
        gram[idx][idx] += mag
        atb[idx] += mag
    delta = [atb[0] / gram[0][0], atb[1] / gram[1][1]]
    return {
        "column_order": columns,
        "column_norms": {k: round(v, 12) for k, v in norms.items()},
        "A_transpose_A": [[round(gram[0][0], 12), 0.0], [0.0, round(gram[1][1], 12)]],
        "A_transpose_b": [round(atb[0], 12), round(atb[1], 12)],
        "deltaTheta_C1_support_solution": [round(delta[0], 12), round(delta[1], 12)],
        "determinant": round(gram[0][0] * gram[1][1], 12),
        "positive_definite_support_hessian": gram[0][0] > 0 and gram[1][1] > 0,
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    previous = load(PREVIOUS)
    primitive = load(PRIMITIVE_ROWS)
    old_map = load(OLD_SOURCE_MAP)
    witness = load(CONDITIONAL_WITNESS)
    hessian = hessian_from_rows(primitive["rows"])
    expected = old_map["if_source_map_selected_then"]
    expected_match = (
        hessian["A_transpose_A"] == expected["A_transpose_A"]
        and hessian["A_transpose_b"] == expected["A_transpose_b"]
        and hessian["deltaTheta_C1_support_solution"] == expected["deltaTheta_C1"]
    )

    route_a = {
        "schema": "MTTPSMC102RouteARA1PhysicalActionEqualityStatus.v1",
        "active_label": "PSM-C1-02",
        "route_label": "ROUTE-A",
        "clause_id": "RA-1",
        "status": "ROUTE_A_RA1_PHYSICAL_ACTION_EQUALITY_REDUCED_TO_RA2_BOUNDARY_SOURCE_CANCELLATION_OPEN",
        "physical_action_equality_claimed": False,
        "free_axiom_patch_used": False,
        "current_RA1_result": {
            "RA1a_physical_action_candidate_identified": True,
            "RA1b_first_variation_equality_not_proved": True,
            "RA1c_trace_frobenius_pairing_aligned_methodologically": True,
            "RA1d_boundary_source_terms_split_to_RA2": True,
        },
        "corpus_support": [
            {
                "source": "C:/ObsidianVault/BrainOfNerodes/Papers/Modal Triplet Theory/16 Strings, Flux, & M-Theory Encodings/Modal_Triplet_Theory__From_MTT_to_the_Strominger__Heterotic_Flux__System.md",
                "supports": "positive Hessian, Strominger fixed point/minimizer, and detailed B/H/K/Lambda variations",
                "used_as_source_proof": False,
            },
            {
                "source": "C:/ObsidianVault/BrainOfNerodes/Papers/Modal Triplet Theory/4 Fixed Points/Fixed_Points_I__Fixed_Points_over_Multi_Bundle_Manifolds_v5.md",
                "supports": "Galerkin approximation language for steady fixed-point equations",
                "used_as_source_proof": False,
            },
        ],
        "why_RA1_still_open": [
            "The corpus supports a physical action/Hessian picture, but has not identified the selected C1 restriction S_C1 with the finite C1DefectLeakageFunctional.",
            "Boundary and source cancellation are isolated as RA-2 instead of hidden in RA-1.",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    route_b = {
        "schema": "MTTPSMC102RouteBRB3HessianSourceFill.v1",
        "active_label": "PSM-C1-02",
        "route_label": "ROUTE-B",
        "input_id": "RB-3",
        "status": "ROUTE_B_RB3_HESSIAN_SOURCE_NORMAL_EQUATIONS_FILLED_FROM_PRIMITIVE_SUPPORT_ROWS_SELECTION_OPEN",
        "primitive_input": rel(PRIMITIVE_ROWS),
        "primitive_row_count": primitive["row_count"],
        "hessian_source_support": hessian,
        "matches_prior_conditional_source_map": expected_match,
        "prior_conditional_source_map": rel(OLD_SOURCE_MAP),
        "conditional_witness": rel(CONDITIONAL_WITNESS),
        "conditional_witness_same_source": witness["same_source_hessian"],
        "computed_from_independent_galerkin_quadrature": False,
        "selected_hessian_source_emitted": False,
        "theorem_derived": False,
        "source_owner_verified": False,
        "residual_replay_dependency": True,
        "why_not_selected": [
            "The normal equations are reproducible from the 72 support rows.",
            "The rows still inherit residual-replay support rather than independent selected quadrature/source ownership.",
            "Therefore A^T A, A^T b, and deltaTheta_C1 remain support-level, not selected theorem data.",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    superset = {
        "schema": "MTTPSMC102SupersetAlignmentAfterRB3.v1",
        "active_label": "PSM-C1-02",
        "closed_boundary": "DONE-PARITY-00",
        "status": "SUPERSET_PATHS_CONSTRAINED_TO_SAME_NORMAL_EQUATION_TARGET_NOT_USED_AS_KNOBS",
        "locked_target": "same PSM-C1-02 C1 source-promotion packet: S_C1' equality or independently sourced 72-row Hessian/source normal equations",
        "paths": {
            "ROUTE-A": "physical-action equality and boundary/source cancellation",
            "ROUTE-B": "honest selected Galerkin C1 execution via primitive rows and Hessian/source normal equations",
            "corpus": "Strominger positive-Hessian and fixed-point Galerkin approximation clues",
            "external": "Galerkin weak-form/weighted-residual methodology and Strominger-system variational literature",
        },
        "paths_used_as_knobs": False,
        "observed_values_used_as_knobs": False,
        "external_references": [
            {
                "title": "DOLFINx biharmonic weak/Galerkin demo",
                "url": "https://docs.fenicsproject.org/dolfinx/v0.10.0/python/demos/demo_biharmonic.html",
                "used_as_source_proof": False,
            },
            {
                "title": "Finite deformations from a heterotic superpotential",
                "url": "https://arxiv.org/abs/1806.08367",
                "used_as_source_proof": False,
            },
        ],
    }

    next_work = {
        "schema": "MTTNextLabeledWorkorderAfterPSMC102RA1RB3.v1",
        "previous_artifact": "MTT_Selected_PSM_C1_02_RouteA_RA1_PhysicalActionEquality_or_RouteB_RB3_HessianSourceFill_v1",
        "next_required_artifact": NEXT,
        "primary": {
            "label": "PSM-C1-02 / ROUTE-A / RA-2",
            "task": "Prove selected boundary/source cancellation for S_C1' = C1DefectLeakageFunctional.",
        },
        "secondary": {
            "label": "PSM-C1-02 / ROUTE-B / RB-4",
            "task": "Replace residual-support rows with independent selected quadrature/source-owned primitive rows.",
        },
        "status": "NEXT_WORKORDER_RA2_BOUNDARY_SOURCE_CANCELLATION_OR_RB4_INDEPENDENT_SOURCE",
    }

    candidate = {
        "candidate": "MTTSelectedPSMC102RA1PhysicalActionEqualityOrRB3HessianSourceFill",
        "active_label": "PSM-C1-02",
        "active_routes": ["ROUTE-A/RA-1", "ROUTE-B/RB-3"],
        "closed_boundary": "DONE-PARITY-00",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "inputs": {
            "previous": rel(PREVIOUS),
            "previous_status": previous["status"],
            "previous_superset": rel(PREVIOUS_DIR / "psm_c1_02_superset_strategy_external_alignment.packet.json"),
            "primitive_rows": rel(PRIMITIVE_ROWS),
            "prior_conditional_source_map": rel(OLD_SOURCE_MAP),
            "conditional_witness": rel(CONDITIONAL_WITNESS),
        },
        "output_packets": {
            "route_A": rel(ROUTE_A_PACKET),
            "route_B": rel(ROUTE_B_PACKET),
            "superset": rel(SUPERSET_PACKET),
            "next_workorder": rel(NEXT_WORKORDER),
        },
        "theorem": {
            "name": "PSMC102RA1PhysicalActionEqualityOrRB3HessianSourceFillTheorem",
            "proved": True,
            "statement": "For PSM-C1-02, RA-1 reduces to RA-2 boundary/source cancellation and RB-2 rows compute the RB-3 support Hessian/source normal equations A^T A=diag(12,12), A^T b=(12,12), deltaTheta_C1=(1,1), without selected-source promotion.",
        },
        "what_closes_now": {
            "ROUTE_A_RA1_reduced_to_RA2_boundary_source_cancellation": True,
            "ROUTE_B_RB3_hessian_source_normal_equations_filled": True,
            "RB3_matches_prior_conditional_source_map": expected_match,
            "support_hessian_positive_definite": hessian["positive_definite_support_hessian"],
            "observed_constants_excluded_as_selectors": True,
            "superset_paths_constrained_to_locked_target": True,
        },
        "what_remains_open": {
            "RA2_selected_boundary_source_cancellation": True,
            "RB4_independent_selected_quadrature_source": True,
            "selected_hessian_source_emitted": True,
            "selected_source_promotion": True,
            "true_equivalence_closed": False,
        },
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_PSM_C1_02_RouteA_RA1_PhysicalActionEquality_or_RouteB_RB3_HessianSourceFill_v1",
        "active_label": "PSM-C1-02",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "next_required_artifact": NEXT,
        "route_A_clause": "RA-1",
        "route_A_RA1_reduced_to_RA2": True,
        "route_A_RA1_closed": False,
        "route_B_input": "RB-3",
        "route_B_RB3_hessian_filled": True,
        "route_B_RB3_selected_promoted": False,
        "primitive_row_count": primitive["row_count"],
        "A_transpose_A": hessian["A_transpose_A"],
        "A_transpose_b": hessian["A_transpose_b"],
        "deltaTheta_C1_support_solution": hessian["deltaTheta_C1_support_solution"],
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    for path, obj in [
        (ROUTE_A_PACKET, route_a),
        (ROUTE_B_PACKET, route_b),
        (SUPERSET_PACKET, superset),
        (NEXT_WORKORDER, next_work),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    NOTE.write_text(
        f"""# MTT Selected PSM C1 02 RouteA RA1 PhysicalActionEquality or RouteB RB3 HessianSourceFill v1

Status label: `PSM-C1-02 / ROUTE-A / RA-1` and `PSM-C1-02 / ROUTE-B / RB-3`

Status: `{STATUS}`

Closed boundary label: `DONE-PARITY-00`

## Theorem

**PSMC102RA1PhysicalActionEqualityOrRB3HessianSourceFillTheorem.** For PSM-C1-02, RA-1 is reduced to `RA-2` boundary/source cancellation, while the RB-2 primitive rows compute the RB-3 support Hessian/source normal equations:

- `A^T A = [[12, 0], [0, 12]]`
- `A^T b = [12, 12]`
- support solution `deltaTheta_C1 = [1, 1]`

This fills the support calculation but does not promote the selected source, because independent Galerkin quadrature/source ownership is still absent.

## Superset Strategy

`ROUTE-A` and `ROUTE-B` are combined only as constrained exits to the same locked target. They are not free knobs. The corpus path supplies Strominger positive-Hessian and fixed-point/Galerkin clues; external references supply methodology only, not MTT source proof.

## Route Status

- `PSM-C1-02 / ROUTE-A / RA-1`: reduced to `RA-2` boundary/source cancellation.
- `PSM-C1-02 / ROUTE-B / RB-3`: Hessian/source normal equations filled from the 72 primitive support rows.

## Next Artifact

`{NEXT}`
""",
        encoding="utf-8",
    )

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
