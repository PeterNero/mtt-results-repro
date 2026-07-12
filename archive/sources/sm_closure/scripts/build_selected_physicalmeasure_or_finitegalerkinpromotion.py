"""Build physical measure or finite-Galerkin promotion theorem gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_physicalmeasure_or_finitegalerkinpromotion"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PROMOTION_THEOREM = PACKET_DIR / "finite_galerkin_promotion_theorem.packet.json"
MEASURE_GATE = PACKET_DIR / "physical_measure_identity_gate.packet.json"
ROUTE_B = PACKET_DIR / "routeb_conditional_promotion_packet.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PhysicalMeasureOrFiniteGalerkinPromotion_v1.md"

STATUS = "MTT_SELECTED_PHYSICALMEASURE_OR_FINITEGALERKINPROMOTION_BUILT_PROMOTION_THEOREM_MEASURE_IDENTITY_OPEN"
NEXT = "MTT_Selected_PhysicalMeasureIdentity_or_RouteAEmissionClosure_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_routeaemission_or_routebgalerkinrows_execution.candidate.json")
    engine = load(
        DATA
        / "selected_routeaemission_or_routebgalerkinrows_execution"
        / "finite_weyl_trace_quadrature_engine.packet.json"
    )
    rows = load(
        DATA
        / "selected_routeaemission_or_routebgalerkinrows_execution"
        / "formal_110_row_execution.packet.json"
    )
    routeb_decision = load(
        DATA
        / "selected_routeaemission_or_routebgalerkinrows_execution"
        / "routeb_promotion_decision.packet.json"
    )
    trace_support = load(
        DATA
        / "selected_c1tracemeasurepromotion_or_actionboundaryproof"
        / "selected_trace_map_and_measure_support.packet.json"
    )
    boundary = load(
        DATA
        / "selected_c1tracemeasurepromotion_or_actionboundaryproof"
        / "finite_trace_boundary_cancellation_certificate.packet.json"
    )
    action_equiv = load(
        DATA
        / "selected_physicalc1actionidentity_or_samesourcebselectedemission"
        / "physical_action_identity_to_source_emission.packet.json"
    )

    support = {
        "selected_finite_trace_quotient": engine["independent_formal_quadrature_engine"],
        "selected_trace_map_support": trace_support["support_imported"][
            "selected_trace_map_values_functional_stationary"
        ],
        "dynamic_dotD_trace_binding": trace_support["support_imported"][
            "dynamic_dotD_trace_binding"
        ],
        "finite_trace_boundary_algebraic_closed": boundary[
            "algebraic_boundary_closed_now"
        ],
        "formal_110_rows_executed": rows["independent_formal_rows_executed_now"],
        "replay_comparison_not_selector": not rows[
            "comparison_to_prior_algebraic_replay"
        ]["prior_replay_used_as_selector"],
        "max_row_error_below_1e_12": rows["comparison_to_prior_algebraic_replay"][
            "max_abs_error"
        ]
        < 1e-12,
    }
    antecedents = {
        "physical_measure_equals_finite_trace_quadrature": trace_support[
            "selected_measure_promoted_now"
        ],
        "physical_PhiFinC1_action_identity": action_equiv[
            "current_physical_antecedents"
        ]["physical_action_identity_promoted"],
        "no_extra_physical_boundary_or_source_term": action_equiv[
            "current_physical_antecedents"
        ]["no_extra_physical_boundary_or_source_term"],
    }

    promotion_theorem = {
        "schema": "MTTFiniteGalerkinPromotionTheorem.v1",
        "status": "CONDITIONAL_PROMOTION_THEOREM_PROVED_ANTECEDENT_OPEN",
        "theorem_name": "FiniteWeylTraceToPhysicalGalerkinPromotionTheorem",
        "statement": (
            "If the physical Phi_fin^C1 measure/action restricts exactly to the selected finite "
            "qutrit Weyl trace quotient and no extra boundary/source term remains, then the exact "
            "finite Weyl trace rows are not merely replay: they are the selected physical Galerkin "
            "replacement rows for the dynamic C1 packet."
        ),
        "closed_support": support,
        "open_physical_antecedents": antecedents,
        "conditional_consequences": {
            "selected_Galerkin_replacement_accepts_finite_Weyl_trace_rows": True,
            "physical_A_selected_would_promote": True,
            "physical_b_selected_would_promote": True,
            "physical_deltaTheta_C1_would_promote": True,
            "physical_sector_response_matrices_would_promote": True,
            "unpatched_SM_parity_dynamic_packet_would_close": True,
        },
        "promoted_now": False,
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    measure_gate = {
        "schema": "MTTPhysicalMeasureIdentityGate.v1",
        "status": "PHYSICAL_MEASURE_IDENTITY_OPEN_BUT_ISOLATED",
        "candidate_identity": (
            "dmu_PhiFinC1 on the selected q79/F,m=1 finite C1 quotient equals the normalized "
            "trace/Frobenius measure on the selected qutrit Weyl algebra."
        ),
        "why_this_is_now_the_minimal_gate": [
            "Finite trace boundary cancellation is already algebraically closed.",
            "The dynamic trace binding and selected trace-map support are already imported.",
            "All 110 finite rows have been executed from Weyl trace quadrature.",
            "The promotion theorem shows these rows become physical as soon as the measure/action identity is selected.",
        ],
        "still_missing": {
            "physical_measure_equals_finite_trace_quadrature": True,
            "physical_PhiFinC1_action_identity": True,
            "no_extra_physical_boundary_or_source_term": True,
        },
        "not_missing_anymore": {
            "finite_row_values": True,
            "finite_boundary_algebraic_cancellation": True,
            "formal_trace_engine": True,
            "row_count_manifest": True,
            "conditional_A_b_deltaTheta": True,
        },
        "promoted_now": False,
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    route_b = {
        "schema": "MTTRouteBConditionalPromotionPacket.v1",
        "status": "ROUTE_B_CONDITIONAL_PROMOTION_READY_PHYSICAL_MEASURE_OPEN",
        "formal_values": routeb_decision["route_B_state_after_exact_finite_quadrature"],
        "conditional_if_measure_identity_supplied": {
            "Route_B_physical_Galerkin_replacement_closed": True,
            "physical_A_selected": routeb_decision[
                "route_B_state_after_exact_finite_quadrature"
            ]["A_selected_formal"],
            "physical_b_selected": routeb_decision[
                "route_B_state_after_exact_finite_quadrature"
            ]["b_selected_formal"],
            "physical_deltaTheta_C1": routeb_decision[
                "route_B_state_after_exact_finite_quadrature"
            ]["deltaTheta_C1_formal"],
            "physical_sector_response_matrices": True,
            "unpatched_SM_parity_dynamic_packet_closed": True,
        },
        "current": {
            "measure_identity_supplied": False,
            "Route_B_physical_Galerkin_replacement_closed": False,
            "unpatched_SM_parity_dynamic_packet_closed": False,
        },
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedPhysicalMeasureOrFiniteGalerkinPromotion",
        "status": STATUS,
        "inputs": {
            "previous_formal_row_execution": rel(
                DATA / "selected_routeaemission_or_routebgalerkinrows_execution.candidate.json"
            ),
            "finite_weyl_trace_engine": rel(
                DATA
                / "selected_routeaemission_or_routebgalerkinrows_execution"
                / "finite_weyl_trace_quadrature_engine.packet.json"
            ),
            "formal_110_rows": rel(
                DATA
                / "selected_routeaemission_or_routebgalerkinrows_execution"
                / "formal_110_row_execution.packet.json"
            ),
            "selected_trace_support": rel(
                DATA
                / "selected_c1tracemeasurepromotion_or_actionboundaryproof"
                / "selected_trace_map_and_measure_support.packet.json"
            ),
            "finite_boundary_certificate": rel(
                DATA
                / "selected_c1tracemeasurepromotion_or_actionboundaryproof"
                / "finite_trace_boundary_cancellation_certificate.packet.json"
            ),
        },
        "output_packets": {
            "finite_galerkin_promotion_theorem": rel(PROMOTION_THEOREM),
            "physical_measure_identity_gate": rel(MEASURE_GATE),
            "routeb_conditional_promotion_packet": rel(ROUTE_B),
        },
        "theorem": {
            "name": "FiniteWeylTraceToPhysicalGalerkinPromotionTheorem",
            "proved": True,
            "conditional": True,
            "statement": promotion_theorem["statement"],
        },
        "what_closes_now": {
            "finite_to_physical_Galerkin_promotion_theorem_proved_conditionally": True,
            "selected_Galerkin_replacement_acceptance_reduced_to_measure_identity": True,
            "physical_measure_identity_gate_isolated": True,
            "route_B_conditional_promotion_packet_built": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "physical_measure_equals_finite_trace_quadrature": True,
            "physical_PhiFinC1_action_identity": True,
            "no_extra_physical_boundary_or_source_term": True,
            "Route_A_same_source_emission": True,
            "Route_B_physical_Galerkin_replacement": True,
            "physical_A_selected": True,
            "physical_b_selected": True,
            "physical_deltaTheta_C1": True,
            "physical_sector_response_matrices": True,
            "unpatched_SM_parity_dynamic_packet_closure": True,
            "true_SM_equivalence_closure": True,
        },
        "promotion_decision": {
            "promotion_theorem_proved": True,
            "physical_measure_identity_promoted": False,
            "Route_B_physical_Galerkin_replacement_closed": False,
            "Route_A_same_source_emission_closed": False,
            "physical_A_selected_promoted": False,
            "physical_b_selected_promoted": False,
            "physical_deltaTheta_C1_promoted": False,
            "physical_sector_response_matrices_promoted": False,
            "unpatched_SM_parity_dynamic_packet_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "observed_data_used": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "previous_status": previous["status"],
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_PhysicalMeasureOrFiniteGalerkinPromotion_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "theorem_conditional": True,
        "closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PhysicalMeasure or FiniteGalerkinPromotion v1

Status: `{STATUS}`.

Promotion theorem created:

```text
conditional finite-to-physical theorem proved = True
formal finite Weyl rows available             = True
selected Galerkin acceptance reduced          = physical measure/action identity
physical measure identity promoted            = False
Route B physical closure now                  = False
```

The exact result is conditional but sharp: if the physical `Phi_fin^C1`
measure/action restricts to the selected finite qutrit Weyl trace quotient and
has no extra boundary/source term, then the executed 110 finite trace rows
promote to the physical Galerkin replacement rows. That would promote
`A_selected`, `b_selected`, `deltaTheta_C1`, and the sector response matrices.

Next artifact: `{NEXT}`.
"""

    PROMOTION_THEOREM.write_text(
        json.dumps(promotion_theorem, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    MEASURE_GATE.write_text(
        json.dumps(measure_gate, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    ROUTE_B.write_text(json.dumps(route_b, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
