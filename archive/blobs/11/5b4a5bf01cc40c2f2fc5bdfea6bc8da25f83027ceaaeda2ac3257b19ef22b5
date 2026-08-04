"""Build PSM-C1-02 RA-1 derivation attack or RB-2 primitive terms fill."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_psm_c1_02_ra1_derivationattack_or_rb2_primitivetermsfill"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROUTE_A = PACKET_DIR / "route_a_ra1_derivation_attack_with_external_variational_support.packet.json"
ROUTE_B = PACKET_DIR / "route_b_rb2_primitive_contraction_terms_fill.packet.json"
RB2_INPUT = DATA / "selected_residualprojectoraxiominsertion_or_galerkinc1firstexecution" / "inputs" / "primitive_contraction_terms.packet.json"
SUPERSET = PACKET_DIR / "psm_c1_02_superset_strategy_external_alignment.packet.json"
NEXT = PACKET_DIR / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PSM_C1_02_RouteA_RA1_DerivationAttack_or_RouteB_RB2_PrimitiveTermsFill_v1.md"

STATUS = "MTT_SELECTED_PSM_C1_02_RA1_DERIVATIONATTACK_OR_RB2_PRIMITIVETERMSFILL_BUILT_RB2_INPUT_FILLED_SELECTION_OPEN"
PREVIOUS_SLUG = "selected_psm_c1_02_routea_clause1_or_routeb_inputbasisfill"
NEXT_ARTIFACT = "MTT_Selected_PSM_C1_02_RouteA_RA1_PhysicalActionEquality_or_RouteB_RB3_HessianSourceFill_v1"

POST_SM_LABEL_CONTEXT = {
    "tier": "tier_2_post_sm_parity_true_equivalence",
    "preferred_phrase": "post-SM-parity frontier",
    "closed_boundary": "DONE-PARITY-00",
    "active_label": "PSM-C1-02",
    "active_label_name": "selected primitive C1 overlap contractions",
    "primary_routes": ["ROUTE-A", "ROUTE-B"],
    "route_A": "same-source dynamic Phi_fin^C1 source rule",
    "route_B": "honest selected Galerkin C1 execution",
    "language_guardrail": "Do not call this an SM-parity blocker; SM-parity replay is frozen closed.",
}

EXTERNAL_REFERENCES = [
    {
        "label": "Galerkin/Ritz variational and weighted-residual split",
        "url": "https://en.wikipedia.org/wiki/Galerkin_method",
        "use": "methodological support for keeping ROUTE-A variational and ROUTE-B weighted-residual/Galerkin separate",
        "used_as_source_proof": False,
    },
    {
        "label": "FEniCS variational/Galerkin finite-element formulation examples",
        "url": "https://docs.fenicsproject.org/dolfinx/v0.10.0/python/demos/demo_biharmonic.html",
        "use": "methodological support for weak-form/Galerkin execution inputs and boundary-term bookkeeping",
        "used_as_source_proof": False,
    },
    {
        "label": "Finite deformations of Hull-Strominger systems and variational/superpotential structure",
        "url": "https://arxiv.org/abs/1806.08367",
        "use": "external inspiration for treating Strominger/HYM finite deformation data as a structured source problem",
        "used_as_source_proof": False,
    },
]


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


def matrix_entry(matrix: list[Any], row: int, col: int) -> Any:
    return matrix[row][col]


def build_primitive_rows(workorder: dict[str, Any], support_terms: dict[str, Any]) -> list[dict[str, Any]]:
    stage = next(item for item in workorder["execution_order"] if item["stage"] == "primitive_contractions")
    rows: list[dict[str, Any]] = []
    sector_routing = support_terms["sector_routing"]
    term_map = support_terms["terms"]
    for row_id in stage["rows"]:
        sector, response, coord = row_id.split(":")
        row = int(coord[1])
        col = int(coord[3])
        term_key = sector_routing[sector]
        term = term_map[term_key]
        rows.append(
            {
                "row_id": row_id,
                "stage": "primitive_contractions",
                "sector": sector,
                "response": response,
                "coordinate": coord,
                "source_term": term_key,
                "value": matrix_entry(term["matrix"], row, col),
                "kernel_source_id": f"K_C1_support::{row_id}",
                "quadrature_rule_id": "selected_finite_C1_independent_quadrature_rule",
                "basis_input": "candidate_data/selected_residualprojectoraxiominsertion_or_galerkinc1firstexecution/inputs/zero_mode_basis.packet.json",
                "independent_source_emitted": False,
                "computed_from_independent_galerkin_quadrature": False,
                "residual_replay_dependency": True,
                "locked_target_dependency": False,
                "exactness_certificate": None,
                "error_bound": None,
                "selected_emitted": False,
                "theorem_derived": False,
                "source_owner_verified": False,
                "why_not_selected": "Filled from residual-projector/formula support; no independent contraction exactness or error-bound certificate is emitted.",
            }
        )
    return rows


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / f"{PREVIOUS_SLUG}.candidate.json")
    previous_decision = load(DATA / PREVIOUS_SLUG / "psm_c1_02_ra1_rb1_decision.packet.json")
    source_rule_attempt = load(DATA / "selected_differentiatedphifinc1_sourcerule_derivation_or_axiompromotion" / "unpatched_source_rule_derivation_attempt.packet.json")
    first_row_formula = load(DATA / "selected_differentiatedphifinc1primitiveoverlap_or_firstrowkernelformulasource.candidate.json")
    support_terms = load(DATA / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch" / "inputs" / "primitive_contraction_terms.packet.json")
    workorder = load(DATA / "selected_routeb_independentquadraturepayload_schema_or_executionworkorder" / "routeb_independent_quadrature_execution_workorder.packet.json")

    route_a = {
        "schema": "MTTPSMC102RouteARA1DerivationAttackWithExternalVariationalSupport.v1",
        "status": "ROUTE_A_RA1_VARIATIONAL_ATTACK_REFINED_PHYSICAL_EQUALITY_OPEN",
        "post_sm_parity_label_context": POST_SM_LABEL_CONTEXT,
        "active_label": "PSM-C1-02",
        "route_label": "ROUTE-A",
        "clause_id": "RA-1",
        "clause_name": "physical_C1_variation_principle",
        "closed_now": False,
        "free_axiom_patch_used": False,
        "internal_support": source_rule_attempt["closed_support"],
        "external_alignment": EXTERNAL_REFERENCES,
        "refined_RA1_target": {
            "RA1a": "identify the unpatched physical C1 action functional S_C1 on the selected branch",
            "RA1b": "prove first variation of S_C1 equals the C1DefectLeakageFunctional weak form on admissible variations",
            "RA1c": "show the selected trace/Frobenius pairing is the physical weak-form pairing, not only finite support",
            "RA1d": "defer boundary/source cancellation to RA-2 rather than hiding it inside RA-1",
        },
        "why_still_open": [
            "External Galerkin/Ritz references justify the shape of the split, not MTT source ownership.",
            "Internal corpus provides a candidate leakage functional and finite pairing, but not unpatched equality to physical S_C1.",
            "The local source axiom would close this only as a patch, so it remains excluded.",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    primitive_rows = build_primitive_rows(workorder, support_terms)
    rb2_packet = {
        "schema": "MTTPSMC102RouteBRB2PrimitiveContractionTermsInputPacket.v1",
        "status": "ROUTE_B_RB2_PRIMITIVE_TERMS_FILLED_SUPPORT_LEVEL_SELECTION_OPEN",
        "post_sm_parity_label_context": POST_SM_LABEL_CONTEXT,
        "active_label": "PSM-C1-02",
        "route_label": "ROUTE-B",
        "input_id": "RB-2",
        "input_name": "primitive contraction terms input packet for honest Galerkin execution",
        "row_count": len(primitive_rows),
        "rows": primitive_rows,
        "support_source": rel(DATA / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch" / "inputs" / "primitive_contraction_terms.packet.json"),
        "first_row_formula_source": rel(DATA / "selected_differentiatedphifinc1primitiveoverlap_or_firstrowkernelformulasource.candidate.json"),
        "first_row_formula_status": first_row_formula["status"],
        "computed_from_independent_galerkin_quadrature": False,
        "selected_emitted": False,
        "theorem_derived": False,
        "source_owner_verified": False,
        "all_rows_have_values": all(row["value"] is not None for row in primitive_rows),
        "all_rows_selected": all(row["selected_emitted"] for row in primitive_rows),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(RB2_INPUT, rb2_packet)

    route_b = {
        "schema": "MTTPSMC102RouteBRB2PrimitiveTermsFill.v1",
        "status": "ROUTE_B_RB2_INPUT_PATH_FILLED_SUPPORT_LEVEL_SELECTION_OPEN",
        "post_sm_parity_label_context": POST_SM_LABEL_CONTEXT,
        "active_label": "PSM-C1-02",
        "route_label": "ROUTE-B",
        "input_id": "RB-2",
        "filled_input_path": rel(RB2_INPUT),
        "input_file_exists_now": RB2_INPUT.exists(),
        "primitive_row_count": len(primitive_rows),
        "selected_emitted": False,
        "theorem_derived": False,
        "source_owner_verified": False,
        "remaining_route_b_inputs_after_rb2": [
            "candidate_data/selected_residualprojectoraxiominsertion_or_galerkinc1firstexecution/inputs/hessian_source_vector.packet.json",
            "candidate_data/selected_residualprojectoraxiominsertion_or_galerkinc1firstexecution/inputs/sector_response_matrices.packet.json",
        ],
        "remaining_route_b_input_count_after_rb2": 2,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    superset = {
        "schema": "MTTPSMC102SupersetStrategyExternalAlignment.v1",
        "status": "SUPERSET_PATHS_ALIGNED_TO_LOCKED_TARGET_NO_SOURCE_PROOF_IMPORTED",
        "active_label": "PSM-C1-02",
        "closed_boundary": "DONE-PARITY-00",
        "combined_paths": {
            "ROUTE-A/RA-1": "variational physical-action equality inspired by Ritz/Galerkin weak-form structure",
            "ROUTE-B/RB-2": "weighted-residual/Galerkin primitive terms fill from existing finite support",
            "corpus_path": "C1DefectLeakageFunctional plus finite trace/Frobenius pairing plus qutrit Weyl residual terms",
            "external_path": "Galerkin/Ritz/weak-form literature used only as methodology",
        },
        "locked_target": "same PSM-C1-02 selected source-promotion packet and 72 primitive row contract",
        "paths_used_as_knobs": False,
        "external_references": EXTERNAL_REFERENCES,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    theorem = {
        "name": "PSMC102RA1DerivationAttackOrRB2PrimitiveTermsFillTheorem",
        "proved": True,
        "statement": (
            "For PSM-C1-02, external variational/Galerkin literature supports the methodological split between ROUTE-A "
            "physical-action derivation and ROUTE-B weighted-residual execution, but supplies no MTT source proof. ROUTE-A/RA-1 "
            "is refined to the physical equality S_C1' = C1DefectLeakageFunctional on selected admissible variations. ROUTE-B/RB-2 "
            "is filled with all 72 primitive contraction support rows from the existing qutrit Weyl residual terms, while remaining "
            "open as selected Galerkin proof because the rows are not independent quadrature/source emissions."
        ),
    }

    candidate = {
        "candidate": "MTTSelectedPSMC102RA1DerivationAttackOrRB2PrimitiveTermsFill",
        "status": STATUS,
        "previous_artifact": rel(DATA / f"{PREVIOUS_SLUG}.candidate.json"),
        "previous_status": previous["status"],
        "previous_decision_status": previous_decision["status"],
        "post_sm_parity_label_context": POST_SM_LABEL_CONTEXT,
        "active_post_sm_parity_label": "PSM-C1-02",
        "active_routes": ["ROUTE-A/RA-1", "ROUTE-B/RB-2"],
        "theorem": theorem,
        "what_closes_now": {
            "ROUTE_A_RA1_external_variational_alignment_recorded": True,
            "ROUTE_A_RA1_refined_to_physical_action_equality": True,
            "ROUTE_B_RB2_primitive_terms_input_file_filled": True,
            "all_72_primitive_support_rows_materialized": True,
            "superset_strategy_locked_no_external_source_import": True,
        },
        "what_remains_open": {
            "ROUTE_A_RA1_unpatched_physical_action_equality": True,
            "ROUTE_B_RB2_independent_quadrature_exactness": True,
            "ROUTE_B_RB2_selected_source_promotion": True,
            "ROUTE_B_RB3_hessian_source_vector": True,
            "ROUTE_B_RB4_sector_response_matrices": True,
        },
        "output_packets": {
            "route_a_ra1_derivation_attack": rel(ROUTE_A),
            "route_b_rb2_fill": rel(ROUTE_B),
            "route_b_rb2_input_file": rel(RB2_INPUT),
            "superset_strategy_external_alignment": rel(SUPERSET),
            "next_labeled_workorder": rel(NEXT),
        },
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT_ARTIFACT,
    }

    next_packet = {
        "schema": "MTTNextLabeledWorkorderAfterPSMC102RA1RB2.v1",
        "status": "NEXT_WORKORDER_RA1_PHYSICAL_ACTION_EQUALITY_OR_RB3_HESSIAN_SOURCE_FILL",
        "active_label": "PSM-C1-02",
        "route_labels": ["ROUTE-A", "ROUTE-B"],
        "next_required_artifact": NEXT_ARTIFACT,
        "primary": {
            "route_label": "ROUTE-A",
            "clause_id": "RA-1",
            "task": "Try to prove unpatched physical action equality S_C1' = C1DefectLeakageFunctional.",
        },
        "secondary": {
            "route_label": "ROUTE-B",
            "input_id": "RB-3",
            "task": "Fill hessian source vector input packet for honest Galerkin execution.",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    certificate = {
        "certificate": "MTT_Selected_PSM_C1_02_RouteA_RA1_DerivationAttack_or_RouteB_RB2_PrimitiveTermsFill_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "closure_claimed": False,
        "active_label": "PSM-C1-02",
        "route_A_clause": "RA-1",
        "route_A_RA1_closed": False,
        "route_B_input": "RB-2",
        "route_B_RB2_input_filled": True,
        "route_B_RB2_selected_promoted": False,
        "primitive_row_count": len(primitive_rows),
        "next_required_artifact": NEXT_ARTIFACT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected PSM C1 02 RouteA RA1 DerivationAttack or RouteB RB2 PrimitiveTermsFill v1

Status label: `PSM-C1-02 / ROUTE-A / RA-1` and `PSM-C1-02 / ROUTE-B / RB-2`

Status: `{STATUS}`

Closed boundary label: `DONE-PARITY-00`

## Theorem

**{theorem["name"]}.** {theorem["statement"]}

## Superset Strategy

`ROUTE-A` uses the variational/physical-action path. `ROUTE-B` uses the weighted-residual/Galerkin execution path. External references are methodological only and do not count as selected MTT source proof.

## External References

- [Galerkin method](https://en.wikipedia.org/wiki/Galerkin_method)
- [FEniCS biharmonic variational/Galerkin demo](https://docs.fenicsproject.org/dolfinx/v0.10.0/python/demos/demo_biharmonic.html)
- [Finite deformations from a heterotic superpotential](https://arxiv.org/abs/1806.08367)

## Route Status

- `PSM-C1-02 / ROUTE-A / RA-1`: refined, still open.
- `PSM-C1-02 / ROUTE-B / RB-2`: 72 primitive support rows filled, selected-source promotion still open.

## Next Artifact

`{NEXT_ARTIFACT}`
"""

    write_json(ROUTE_A, route_a)
    write_json(ROUTE_B, route_b)
    write_json(SUPERSET, superset)
    write_json(NEXT, next_packet)
    write_json(OUTPUT, candidate)
    write_json(CERT, certificate)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
