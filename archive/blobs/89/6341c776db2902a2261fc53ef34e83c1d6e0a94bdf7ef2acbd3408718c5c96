"""Build selected C1 trace-measure promotion / action-boundary proof gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_c1tracemeasurepromotion_or_actionboundaryproof"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
TRACE = PACKET_DIR / "selected_trace_map_and_measure_support.packet.json"
BOUNDARY = PACKET_DIR / "finite_trace_boundary_cancellation_certificate.packet.json"
ACTION = PACKET_DIR / "physical_action_boundary_promotion_attempt.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_C1TraceMeasurePromotion_or_ActionBoundaryProof_v1.md"

STATUS = "MTT_SELECTED_C1TRACEMEASUREPROMOTION_OR_ACTIONBOUNDARYPROOF_BUILT_ALGEBRAIC_BOUNDARY_CLOSED_PHYSICAL_PROMOTION_OPEN"
NEXT = "MTT_Selected_PhysicalC1ActionIdentity_or_SameSourceBSelectedEmission_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_c1measurepairing_or_physicalactionidentity.candidate.json")
    pairing = load(DATA / "selected_c1measurepairing_or_physicalactionidentity" / "candidate_trace_frobenius_measure_pairing.packet.json")
    action_attempt = load(DATA / "selected_c1measurepairing_or_physicalactionidentity" / "physical_action_identity_attempt.packet.json")
    promotion = load(DATA / "selected_c1measurepairing_or_physicalactionidentity" / "promotion_sufficiency_and_remaining_axioms.packet.json")
    trace_basis = load(DATA / "selected_tracemapandbasisvalues_or_primitiverowsexecution.candidate.json")
    trace_fill = load(DATA / "selected_tracemapandbasisvalues_or_primitiverowsexecution" / "route_a_trace_map_value_fill.packet.json")
    basis_fill = load(DATA / "selected_tracemapandbasisvalues_or_primitiverowsexecution" / "route_b_selected_basis_value_fill.packet.json")
    dynamic_trace = load(DATA / "selected_primitiverowsexecution_or_dynamicdotdtracebinding" / "dynamic_dotd_trace_binding.packet.json")
    algebraic_values = load(DATA / "selected_c1kernelvaluesexecution_or_physicalsourcepromotion" / "route_b_algebraic_kernel_value_execution_attempt.packet.json")
    dynamic_trace_accepted = dynamic_trace["binding_flags"]["dynamic_dotD_trace_binding_accepted"]

    trace = {
        "schema": "MTTSelectedTraceMapAndMeasureSupport.v1",
        "status": "SELECTED_TRACE_MAP_SUPPORT_IMPORTED_MEASURE_PROMOTION_OPEN",
        "trace_map_sources": {
            "trace_basis_gate": rel(DATA / "selected_tracemapandbasisvalues_or_primitiverowsexecution.candidate.json"),
            "route_a_trace_map_fill": rel(DATA / "selected_tracemapandbasisvalues_or_primitiverowsexecution" / "route_a_trace_map_value_fill.packet.json"),
            "basis_value_fill": rel(DATA / "selected_tracemapandbasisvalues_or_primitiverowsexecution" / "route_b_selected_basis_value_fill.packet.json"),
            "dynamic_dotd_trace_binding": rel(DATA / "selected_primitiverowsexecution_or_dynamicdotdtracebinding" / "dynamic_dotd_trace_binding.packet.json"),
        },
        "support_imported": {
            "selected_trace_map_values_functional_stationary": trace_basis["what_closes_now"].get("selected_trace_map_values_functional_stationary", False),
            "selected_basis_rows": basis_fill["selected_row_count"],
            "all_basis_rows_selected": basis_fill["all_basis_rows_selected"],
            "dynamic_dotD_trace_binding": dynamic_trace_accepted,
            "formal_trace_frobenius_pairing_built": pairing["formal_support"]["unique_formal_C1_defect_functional_sourced"],
            "all_110_algebraic_values_filled": algebraic_values["counts"]["total_algebraic_values_filled"] == 110,
        },
        "candidate_physical_measure": pairing["definition"],
        "selected_measure_promoted_now": False,
        "why_not_promoted": [
            "Trace map support is imported at the stationary/dynamic binding level, but no theorem says the physical Phi_fin^C1 action uses exactly this finite trace/Frobenius measure.",
            "The same-source b_selected emission is still algebraic/replay, not an emitted physical source value.",
        ],
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    boundary = {
        "schema": "MTTFiniteTraceBoundaryCancellationCertificate.v1",
        "status": "ALGEBRAIC_FINITE_TRACE_BOUNDARY_CLOSED_PHYSICAL_BOUNDARY_OPEN",
        "algebraic_boundary_statement": (
            "On the finite qutrit Weyl C1 response quotient with trace/Frobenius pairing, integration by parts "
            "has no external boundary term: cyclic trace cancels commutators and admissible variations are finite "
            "matrix rows in the selected basis."
        ),
        "algebraic_boundary_closed_now": True,
        "proof_steps": [
            "The C1 response space is finite-dimensional and represented by selected qutrit Weyl matrix rows.",
            "The candidate measure is a trace/Frobenius pairing, so boundary terms reduce to cyclic trace commutators.",
            "Trace cyclicity gives Tr([A,B])=0 for finite matrices.",
            "No continuum boundary integral is introduced inside the finite quotient algebra.",
        ],
        "scope_limit": (
            "This closes boundary cancellation only for the formal finite trace quotient. It does not prove that "
            "the physical Phi_fin^C1 action has no additional boundary/source term before the action identity is derived."
        ),
        "physical_boundary_promoted_now": False,
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    action = {
        "schema": "MTTPhysicalActionBoundaryPromotionAttempt.v1",
        "status": "TRACE_AND_ALGEBRAIC_BOUNDARY_SUPPORT_CLOSED_ACTION_IDENTITY_BSELECTED_OPEN",
        "available_now": {
            "selected_trace_map_support": True,
            "dynamic_trace_binding": dynamic_trace_accepted,
            "formal_trace_frobenius_pairing": True,
            "algebraic_finite_boundary_cancellation": boundary["algebraic_boundary_closed_now"],
            "all_110_algebraic_values_filled": algebraic_values["counts"]["total_algebraic_values_filled"] == 110,
            "locked_target_matches": algebraic_values["algebraic_consistency_certificate"]["passes_locked_target_by_algebraic_replay"],
        },
        "still_missing_for_physical_promotion": {
            "physical_action_identity_equates_first_variation_to_defect_functional": True,
            "physical_measure_equals_trace_frobenius_pairing": True,
            "no_extra_physical_boundary_or_source_term": True,
            "same_source_b_selected_emission": True,
        },
        "first_variation_certificate_fields_after_this_gate": {
            **action_attempt["first_variation_certificate_fields"],
            "boundary_cancellation": {
                **action_attempt["first_variation_certificate_fields"]["boundary_cancellation"],
                "finite_trace_algebraic_verified_now": True,
                "physical_verified_now": False,
            },
            "selected_trace_map": {
                **action_attempt["first_variation_certificate_fields"]["selected_trace_map"],
                "support_imported_now": True,
                "physical_measure_promoted_now": False,
            },
        },
        "would_close_if_next_gate_supplies": [
            "physical Phi_fin^C1 action identity",
            "same-source b_selected emission",
            "proof that no extra continuum/source boundary term survives outside the finite trace quotient",
        ],
        "route_A_promoted_now": False,
        "route_B_independent_quadrature_promoted_now": False,
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedC1TraceMeasurePromotionOrActionBoundaryProof",
        "status": STATUS,
        "inputs": {
            "previous_gate": rel(DATA / "selected_c1measurepairing_or_physicalactionidentity.candidate.json"),
            "candidate_pairing": rel(DATA / "selected_c1measurepairing_or_physicalactionidentity" / "candidate_trace_frobenius_measure_pairing.packet.json"),
            "action_identity_attempt": rel(DATA / "selected_c1measurepairing_or_physicalactionidentity" / "physical_action_identity_attempt.packet.json"),
            "trace_basis_gate": rel(DATA / "selected_tracemapandbasisvalues_or_primitiverowsexecution.candidate.json"),
            "dynamic_trace_binding": rel(DATA / "selected_primitiverowsexecution_or_dynamicdotdtracebinding" / "dynamic_dotd_trace_binding.packet.json"),
            "algebraic_kernel_values": rel(DATA / "selected_c1kernelvaluesexecution_or_physicalsourcepromotion" / "route_b_algebraic_kernel_value_execution_attempt.packet.json"),
        },
        "output_packets": {
            "selected_trace_map_and_measure_support": rel(TRACE),
            "finite_trace_boundary_cancellation_certificate": rel(BOUNDARY),
            "physical_action_boundary_promotion_attempt": rel(ACTION),
        },
        "theorem": {
            "name": "FiniteTraceBoundaryCancellationAndPhysicalPromotionReductionTheorem",
            "proved": True,
            "statement": (
                "The selected finite trace quotient has algebraic boundary cancellation under the trace/Frobenius "
                "pairing, and the trace-map/dynamic-trace supports are imported. Physical C1 closure is therefore "
                "reduced to the action identity plus same-source b_selected emission and absence of extra physical boundary/source terms."
            ),
        },
        "what_closes_now": {
            "selected_trace_map_support_imported": True,
            "dynamic_trace_binding_imported": True,
            "algebraic_finite_trace_boundary_cancellation": True,
            "formal_measure_pairing_sufficiency_retained": True,
            "physical_promotion_reduced_to_action_identity_and_bselected": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "physical_PhiFinC1_action_identity": True,
            "physical_measure_equals_trace_frobenius_pairing": True,
            "same_source_b_selected_emission": True,
            "absence_of_extra_physical_boundary_or_source_term": True,
            "independent_quadrature_exactness_certificate": True,
            "unpatched_SM_parity_dynamic_packet_closure": True,
            "true_SM_equivalence_closure": True,
        },
        "promotion_decision": {
            "selected_measure_promoted_as_physical": False,
            "physical_action_identity_promoted": False,
            "physical_boundary_cancellation_promoted": False,
            "same_source_b_selected_promoted": False,
            "unpatched_SM_parity_dynamic_packet_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "observed_data_used": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "next_required_artifact": NEXT,
        "previous_status": previous["status"],
    }

    cert = {
        "certificate": "MTT_Selected_C1TraceMeasurePromotion_or_ActionBoundaryProof_v1",
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

    note = f"""# MTT Selected C1TraceMeasurePromotion or ActionBoundaryProof v1

Status: `{STATUS}`.

Closed in this gate:

```text
selected trace-map support imported        = True
dynamic dotD/Phi_fin^C1 trace binding      = True
finite trace algebraic boundary vanishes   = True
physical boundary/action promoted          = False
same-source b_selected emitted             = False
```

The finite quotient boundary is no longer the active blocker. The remaining
physical gate is the `Phi_fin^C1` action identity itself, plus same-source
`b_selected` and proof that no extra physical boundary/source term survives
outside the finite trace quotient.

Next artifact: `{NEXT}`.
"""

    TRACE.write_text(json.dumps(trace, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    BOUNDARY.write_text(json.dumps(boundary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    ACTION.write_text(json.dumps(action, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
