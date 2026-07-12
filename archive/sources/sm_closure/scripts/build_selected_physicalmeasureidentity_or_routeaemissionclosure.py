"""Build physical measure-identity or Route A emission closure gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_physicalmeasureidentity_or_routeaemissionclosure"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
IDENTITY = PACKET_DIR / "physical_measure_identity_theorem_slot.packet.json"
AXIOM = PACKET_DIR / "finite_c1_trace_measure_principle_draft.packet.json"
ROUTE_A = PACKET_DIR / "routea_same_source_emission_closure_attempt.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PhysicalMeasureIdentity_or_RouteAEmissionClosure_v1.md"

STATUS = "MTT_SELECTED_PHYSICALMEASUREIDENTITY_OR_ROUTEAEMISSIONCLOSURE_BUILT_THEOREM_SLOT_AXIOM_DRAFT_OPEN"
NEXT = "MTT_Selected_FiniteC1TraceMeasurePrincipleInsertion_or_DirectActionDerivation_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_physicalmeasure_or_finitegalerkinpromotion.candidate.json")
    measure_gate = load(
        DATA
        / "selected_physicalmeasure_or_finitegalerkinpromotion"
        / "physical_measure_identity_gate.packet.json"
    )
    promotion_theorem = load(
        DATA
        / "selected_physicalmeasure_or_finitegalerkinpromotion"
        / "finite_galerkin_promotion_theorem.packet.json"
    )
    pairing = load(
        DATA
        / "selected_c1measurepairing_or_physicalactionidentity"
        / "candidate_trace_frobenius_measure_pairing.packet.json"
    )
    sufficiency = load(
        DATA
        / "selected_c1measurepairing_or_physicalactionidentity"
        / "promotion_sufficiency_and_remaining_axioms.packet.json"
    )
    action_validator = load(
        DATA
        / "selected_physicalactionsourceemission_or_honestgalerkinreplacement"
        / "route_a_physical_source_emission_validator.packet.json"
    )
    finite_rows = load(
        DATA
        / "selected_routeaemission_or_routebgalerkinrows_execution"
        / "formal_110_row_execution.packet.json"
    )

    direct_derivation_available = False
    principle_inserted = False
    route_a_closed = action_validator["route_A_closes_now"]

    identity = {
        "schema": "MTTPhysicalMeasureIdentityTheoremSlot.v1",
        "status": "PHYSICAL_MEASURE_IDENTITY_THEOREM_SLOT_BUILT_NOT_PROVED",
        "theorem_name": "SelectedFiniteC1TraceMeasureIdentityTheorem",
        "target_statement": measure_gate["candidate_identity"],
        "closed_support": {
            "formal_trace_frobenius_pairing_built": pairing["formal_support"][
                "unique_formal_C1_defect_functional_sourced"
            ],
            "all_basis_rows_selected": pairing["formal_support"][
                "all_basis_rows_selected"
            ],
            "all_110_rows_executed": finite_rows["row_counts"]["total_rows"] == 110,
            "finite_to_physical_promotion_theorem_ready": promotion_theorem[
                "conditional_consequences"
            ]["unpatched_SM_parity_dynamic_packet_would_close"],
            "boundary_algebraic_closed": measure_gate["not_missing_anymore"][
                "finite_boundary_algebraic_cancellation"
            ],
        },
        "missing_for_direct_proof": {
            "derive_from_selected_PhiFinC1_action_definition": True,
            "show_no_extra_physical_boundary_or_source_term": True,
            "show_same_source_b_selected_emission_or_routeB_measure_identity": True,
        },
        "legal_closure_routes": {
            "direct_action_derivation": "prove the target statement from the selected Phi_fin^C1 action definition",
            "principle_insertion": "add or derive a finite C1 trace-measure principle in the MTT axiomatic spine",
            "Route_A_emission": "emit R_Z, R_X, b_selected, measure identity, and no-boundary from the same physical source",
        },
        "direct_derivation_available_now": direct_derivation_available,
        "principle_inserted_now": principle_inserted,
        "route_A_closed_now": route_a_closed,
        "identity_promoted_now": False,
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    axiom = {
        "schema": "MTTFiniteC1TraceMeasurePrincipleDraft.v1",
        "status": "INSERTION_READY_PRINCIPLE_DRAFT_NOT_APPLIED",
        "principle_name": "SelectedFiniteC1TraceMeasurePrinciple",
        "principle_text": (
            "For a selected finite C1 quotient whose admissible variations are exactly represented "
            "by the selected qutrit Weyl response algebra, the physical Phi_fin^C1 first variation "
            "uses the normalized trace/Frobenius measure on that quotient. Continuum or external "
            "boundary/source terms are absent unless separately emitted by the selected source packet."
        ),
        "why_this_principle_is_minimal": [
            "It names only the finite selected C1 quotient, not measured masses or mixings.",
            "It preserves the already-proved finite trace boundary cancellation.",
            "It converts the executed finite Weyl rows into physical Galerkin rows without adding numerical knobs.",
            "It leaves any extra boundary/source term as an explicit emitted-source exception.",
        ],
        "would_promote_if_inserted_or_derived": {
            "physical_measure_equals_finite_trace_quadrature": True,
            "selected_Galerkin_replacement_promotes_formal_rows": True,
            "Route_B_physical_Galerkin_replacement_closed": True,
            "physical_A_selected": [[12.0, 0.0], [0.0, 12.0]],
            "physical_b_selected": [12.0, 12.0],
            "physical_deltaTheta_C1": [1.0, 1.0],
            "physical_sector_response_matrices": True,
            "unpatched_SM_parity_dynamic_packet_closed": True,
        },
        "applied_now": False,
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    route_a = {
        "schema": "MTTRouteASameSourceEmissionClosureAttempt.v1",
        "status": "ROUTE_A_RECHECKED_STILL_OPEN",
        "required_emissions": action_validator["required_emissions"],
        "current_emissions": action_validator["current_emissions"],
        "all_required_emitted_now": action_validator["all_required_emitted_now"],
        "route_A_closes_now": action_validator["route_A_closes_now"],
        "why_not_closed": [
            "No selected physical Phi_fin^C1 action derivation is emitted.",
            "No same-source physical measure identity is emitted.",
            "No same-source b_selected source term is emitted.",
        ],
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedPhysicalMeasureIdentityOrRouteAEmissionClosure",
        "status": STATUS,
        "inputs": {
            "previous_promotion_theorem": rel(
                DATA / "selected_physicalmeasure_or_finitegalerkinpromotion.candidate.json"
            ),
            "measure_identity_gate": rel(
                DATA
                / "selected_physicalmeasure_or_finitegalerkinpromotion"
                / "physical_measure_identity_gate.packet.json"
            ),
            "formal_pairing": rel(
                DATA
                / "selected_c1measurepairing_or_physicalactionidentity"
                / "candidate_trace_frobenius_measure_pairing.packet.json"
            ),
            "route_a_validator": rel(
                DATA
                / "selected_physicalactionsourceemission_or_honestgalerkinreplacement"
                / "route_a_physical_source_emission_validator.packet.json"
            ),
        },
        "output_packets": {
            "physical_measure_identity_theorem_slot": rel(IDENTITY),
            "finite_c1_trace_measure_principle_draft": rel(AXIOM),
            "routea_same_source_emission_closure_attempt": rel(ROUTE_A),
        },
        "theorem": {
            "name": "PhysicalMeasureIdentityClosureDichotomyTheorem",
            "proved": True,
            "statement": (
                "Given the finite Weyl row execution and conditional promotion theorem, physical "
                "dynamic C1 closure is reduced to exactly one of: direct derivation of the selected "
                "finite C1 trace-measure identity from Phi_fin^C1, insertion/derivation of the "
                "SelectedFiniteC1TraceMeasurePrinciple, or Route A same-source emission."
            ),
        },
        "what_closes_now": {
            "physical_measure_identity_theorem_slot_built": True,
            "finite_C1_trace_measure_principle_drafted": True,
            "route_A_rechecked": True,
            "closure_routes_reduced_to_three_legal_options": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "direct_PhiFinC1_action_derivation": True,
            "principle_insertion_or_derivation": True,
            "Route_A_same_source_emission": True,
            "physical_measure_identity": True,
            "Route_B_physical_Galerkin_replacement": True,
            "unpatched_SM_parity_dynamic_packet_closure": True,
            "true_SM_equivalence_closure": True,
        },
        "promotion_decision": {
            "physical_measure_identity_promoted": False,
            "principle_applied": False,
            "Route_A_same_source_emission_closed": False,
            "Route_B_physical_Galerkin_replacement_closed": False,
            "unpatched_SM_parity_dynamic_packet_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "observed_data_used": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "previous_status": previous["status"],
        "sufficiency_status_imported": sufficiency["status"],
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_PhysicalMeasureIdentity_or_RouteAEmissionClosure_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PhysicalMeasureIdentity or RouteAEmissionClosure v1

Status: `{STATUS}`.

The promotion theorem is now sharpened into a closure dichotomy:

```text
direct Phi_fin^C1 action derivation available = {identity["direct_derivation_available_now"]}
finite C1 trace-measure principle applied     = {axiom["applied_now"]}
Route A same-source emission closed           = {route_a["route_A_closes_now"]}
physical measure identity promoted            = {identity["identity_promoted_now"]}
```

The insertion-ready principle is drafted but not applied. If it is derived from
the corpus or explicitly inserted into the MTT axiomatic spine, Route B promotes
the executed finite Weyl rows to physical Galerkin rows and closes the dynamic
C1 packet under the SM-parity standard.

Next artifact: `{NEXT}`.
"""

    IDENTITY.write_text(json.dumps(identity, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    AXIOM.write_text(json.dumps(axiom, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    ROUTE_A.write_text(json.dumps(route_a, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
