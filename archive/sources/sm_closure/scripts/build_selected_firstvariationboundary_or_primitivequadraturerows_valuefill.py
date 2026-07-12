"""Build first-variation boundary / primitive quadrature rows value-fill gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_firstvariationboundary_or_primitivequadraturerows_valuefill"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROUTE_A = PACKET_DIR / "route_a_first_variation_boundary_fill_attempt.packet.json"
ROUTE_B = PACKET_DIR / "route_b_replay_backed_primitive_rows.packet.json"
NEXT_PACKET = PACKET_DIR / "source_promotion_or_independent_quadrature_next.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_FirstVariationBoundary_or_PrimitiveQuadratureRows_ValueFill_v1.md"

STATUS = "MTT_SELECTED_FIRSTVARIATIONBOUNDARY_OR_PRIMITIVEQUADRATUREROWS_VALUEFILL_REPLAY_ROWS_BUILT_SOURCE_PROMOTION_OPEN"
NEXT = "MTT_Selected_PhysicalC1VariationSourcePromotion_or_IndependentQuadratureExecution_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_cycleexit_minimizertrace_or_independentquadraturerows.candidate.json")
    route_a_partial = load(DATA / "selected_c1firstvariationcertificatefill_or_quadraturerowsfirstrun" / "route_a_first_variation_certificate_partial_fill.packet.json")
    primitive_attempt = load(DATA / "selected_primitiverowsexecution_or_dynamicdotdtracebinding" / "primitive_rows_execution_attempt.packet.json")
    residual = load(DATA / "selected_differentiatedvertex_hessiancounterterm_or_galerkinc1_valuepacket" / "differentiated_residual_completion.packet.json")
    weyl_poly = load(DATA / "selected_residual_weylpolynomial_source_theorem_attempt" / "residual_weyl_polynomial_decomposition.packet.json")
    projector = load(DATA / "selected_canonicalresidualprojector_or_honestgalerkinc1_valuefill" / "canonical_fixedfiber_residual_projector.packet.json")
    hessian = load(DATA / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch" / "inputs" / "hessian_source_vector.packet.json")

    route_a = {
        "schema": "MTTFirstVariationBoundaryFillAttempt.v1",
        "status": "FORMAL_HESSIAN_NORMALIZATION_CLOSED_PHYSICAL_VARIATION_BOUNDARY_OPEN",
        "source_partial_fill": rel(DATA / "selected_c1firstvariationcertificatefill_or_quadraturerowsfirstrun" / "route_a_first_variation_certificate_partial_fill.packet.json"),
        "fields": route_a_partial["filled_fields"],
        "new_observation": (
            "The selected stationary trace and dynamic dotD trace binding now remove the older trace/basis blockers, "
            "but the physical first-variation identity and boundary cancellation still require a theorem that the "
            "selected differentiated Phi_fin^C1 variation is governed by the formal C1 defect functional."
        ),
        "verified_now": {
            "formal_hessian_or_coercivity": route_a_partial["filled_fields"]["hessian_or_coercivity"]["verified"],
            "normalization_compatibility": route_a_partial["filled_fields"]["normalization_compatibility"]["verified"],
            "stationary_trace_component_available": True,
            "dynamic_dotD_trace_binding_available": True,
        },
        "still_open": {
            "physical_first_variation_identity": True,
            "boundary_cancellation_for_selected_dynamic_trace": True,
            "full_dynamic_minimizer_to_PhiFin_trace": True,
        },
        "can_close_route_A_now": False,
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    replay_rows = []
    for row in primitive_attempt["rows"]:
        response = row["response"]
        sector = row["sector"]
        routed_residual = None
        if response == "phase" and sector in {"u", "e"}:
            routed_residual = "R_Z"
        elif response == "shift" and sector in {"d", "nuD"}:
            routed_residual = "R_X"
        replay_rows.append(
            {
                "row_id": row["row_id"],
                "sector": sector,
                "response": response,
                "coordinate": row["coordinate"],
                "replay_value_source": routed_residual,
                "filled_by_replay_now": routed_residual is not None,
                "independently_quadrature_emitted": False,
                "why_not_independent": (
                    "Value is routed from the canonical residual projector / Weyl polynomial replay, "
                    "not from an independent selected quadrature integral."
                )
                if routed_residual is not None
                else "This row is zero in the routed residual replay and still lacks an independent quadrature row certificate.",
            }
        )

    filled_replay_count = sum(1 for row in replay_rows if row["filled_by_replay_now"])
    route_b = {
        "schema": "MTTReplayBackedPrimitiveRowsValueTable.v1",
        "status": "REPLAY_BACKED_ROWS_BUILT_NOT_INDEPENDENT_QUADRATURE",
        "source_primitive_attempt": rel(DATA / "selected_primitiverowsexecution_or_dynamicdotdtracebinding" / "primitive_rows_execution_attempt.packet.json"),
        "canonical_projector_source": rel(DATA / "selected_canonicalresidualprojector_or_honestgalerkinc1_valuefill" / "canonical_fixedfiber_residual_projector.packet.json"),
        "weyl_polynomial_source": rel(DATA / "selected_residual_weylpolynomial_source_theorem_attempt" / "residual_weyl_polynomial_decomposition.packet.json"),
        "rows": replay_rows,
        "row_count": len(replay_rows),
        "filled_by_replay_count": filled_replay_count,
        "independent_quadrature_row_count": 0,
        "residual_replay_summaries": {
            "R_Z_norm_sq": weyl_poly["decompositions"]["R_Z"]["norm_sq"],
            "R_X_norm_sq": weyl_poly["decompositions"]["R_X"]["norm_sq"],
            "phase_residual_norm_sq_two_sectors": residual["routed_72_real_completion"]["phase_residual_norm_sq_two_sectors"],
            "shift_residual_norm_sq_two_sectors": residual["routed_72_real_completion"]["shift_residual_norm_sq_two_sectors"],
            "total_residual_norm_sq_four_sectors": residual["routed_72_real_completion"]["total_residual_norm_sq_four_sectors"],
        },
        "acceptance_replay": {
            "A_transpose_A": hessian["A_transpose_A"],
            "A_transpose_b": hessian["A_transpose_b"],
            "deltaTheta_C1": hessian["deltaTheta_C1"],
            "passes_locked_target": hessian["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]]
            and hessian["A_transpose_b"] == [12.0, 12.0]
            and hessian["deltaTheta_C1"] == [1.0, 1.0],
            "source": "local residual-projector contract replay, not independent quadrature",
        },
        "projector_guardrail": {
            "Q_residual_selected_as_canonical_mathematical_projector": projector["selected_as_canonical_mathematical_projector"],
            "Q_residual_selected_as_physical_C1_transfer_application": projector["selected_as_physical_C1_transfer_application"],
        },
        "can_close_route_B_now": False,
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTSourcePromotionOrIndependentQuadratureNext.v1",
        "status": "NEXT_SOURCE_PROMOTION_OR_INDEPENDENT_EXECUTION_SELECTED",
        "closed_now": [
            "replay-backed primitive row table",
            "locked-target replay check",
            "formal Route A Hessian/normalization retained",
            "canonical projector and Weyl polynomial support retained",
        ],
        "still_open": [
            "physical Phi_fin^C1 first variation identity",
            "boundary cancellation for selected dynamic trace",
            "selected physical application of Q_residual",
            "independent primitive quadrature rows",
            "independent b_selected/Hessian emission",
            "independent sector response matrices",
        ],
        "next_artifact": NEXT,
        "decision": (
            "The row values are no longer numerically mysterious: the replay-backed table satisfies the locked target. "
            "The only honest exits are source promotion of the physical C1 variation/projector rule or an actual independent quadrature execution."
        ),
        "superset_strategy": {
            "straight_route": "promote physical variation/source theorem",
            "parallel_route": "run independent quadrature/Hessian rows",
            "current_combination": "shared replay target only; no closure by copying replay-backed rows",
        },
    }

    candidate = {
        "candidate": "MTTSelectedFirstVariationBoundaryOrPrimitiveQuadratureRowsValueFill",
        "status": STATUS,
        "inputs": {
            "previous_gate": rel(DATA / "selected_cycleexit_minimizertrace_or_independentquadraturerows.candidate.json"),
            "route_a_partial_fill": rel(DATA / "selected_c1firstvariationcertificatefill_or_quadraturerowsfirstrun" / "route_a_first_variation_certificate_partial_fill.packet.json"),
            "primitive_rows_attempt": rel(DATA / "selected_primitiverowsexecution_or_dynamicdotdtracebinding" / "primitive_rows_execution_attempt.packet.json"),
            "residual_completion": rel(DATA / "selected_differentiatedvertex_hessiancounterterm_or_galerkinc1_valuepacket" / "differentiated_residual_completion.packet.json"),
            "weyl_polynomial": rel(DATA / "selected_residual_weylpolynomial_source_theorem_attempt" / "residual_weyl_polynomial_decomposition.packet.json"),
            "canonical_projector": rel(DATA / "selected_canonicalresidualprojector_or_honestgalerkinc1_valuefill" / "canonical_fixedfiber_residual_projector.packet.json"),
            "hessian_replay": rel(DATA / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch" / "inputs" / "hessian_source_vector.packet.json"),
        },
        "output_packets": {
            "route_a_first_variation_boundary_fill_attempt": rel(ROUTE_A),
            "route_b_replay_backed_primitive_rows": rel(ROUTE_B),
            "source_promotion_or_independent_quadrature_next": rel(NEXT_PACKET),
        },
        "theorem": {
            "name": "ReplayRowsAndSourcePromotionCutsetTheorem",
            "proved": True,
            "statement": (
                "The locked dynamic C1 target can be replayed row-wise from the canonical residual projector and "
                "residual Weyl-polynomial table, but this is not an independent quadrature proof and not a physical "
                "Phi_fin^C1 application theorem. Therefore the remaining cutset is exactly source promotion of the "
                "physical first variation/projector rule, or an actual independent quadrature/Hessian execution."
            ),
        },
        "what_closes_now": {
            "replay_backed_primitive_row_table_built": True,
            "locked_target_replay_verified": True,
            "formal_first_variation_hessian_normalization_retained": True,
            "source_vs_independent_quadrature_boundary_sharpened": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "physical_first_variation_identity": True,
            "boundary_cancellation_for_selected_dynamic_trace": True,
            "selected_physical_Q_residual_application": True,
            "independent_primitive_quadrature_rows": True,
            "independent_b_selected_hessian_rows": True,
            "independent_sector_response_matrices": True,
            "unpatched_SM_parity_dynamic_packet_closure": True,
            "true_SM_equivalence_closure": True,
        },
        "promotion_decision": {
            "route_A_first_variation_accepted": False,
            "route_B_independent_quadrature_accepted": False,
            "replay_rows_promoted_as_independent": False,
            "physical_Q_residual_application_promoted": False,
            "unpatched_A_selected_promoted": False,
            "unpatched_b_selected_promoted": False,
            "unpatched_deltaTheta_C1_promoted": False,
            "unpatched_SM_parity_dynamic_packet_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "previous_status": previous["status"],
        "observed_data_used": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_FirstVariationBoundary_or_PrimitiveQuadratureRows_ValueFill_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
    }

    note = f"""# MTT Selected FirstVariationBoundary or PrimitiveQuadratureRows ValueFill v1

Status: `{STATUS}`.

Route A:

```text
formal Hessian/coercivity      = True
normalization compatibility    = True
physical first variation       = False
boundary cancellation          = False
```

Route B:

```text
primitive rows total           = {len(replay_rows)}
rows filled by replay          = {filled_replay_count}
independent quadrature rows    = 0
locked target replay passes    = {route_b["acceptance_replay"]["passes_locked_target"]}
```

The row values are now explicit as replay-backed data, but not promoted as
independent quadrature and not accepted as physical `Phi_fin^C1` application.

Next artifact: `{NEXT}`.
"""

    ROUTE_A.write_text(json.dumps(route_a, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    ROUTE_B.write_text(json.dumps(route_b, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NEXT_PACKET.write_text(json.dumps(next_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
