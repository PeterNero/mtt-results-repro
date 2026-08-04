"""Build finite Weyl trace uniqueness derivation for the C1 measure patch."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_finiteweyl_traceuniqueness_or_physicalboundarysource_derivation"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
TRACE_UNIQUENESS = PACKET_DIR / "finite_weyl_trace_uniqueness_derivation.packet.json"
PRINCIPLE_SPLIT = PACKET_DIR / "finite_c1_trace_measure_principle_split.packet.json"
BOUNDARY_SOURCE = PACKET_DIR / "physical_boundary_source_remainder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_FiniteWeylTraceUniqueness_or_PhysicalBoundarySource_Derivation_v1.md"

STATUS = "MTT_SELECTED_FINITEWEYL_TRACEUNIQUENESS_BUILT_MEASURE_DERIVED_BOUNDARY_SOURCE_OPEN"
NEXT = "MTT_Selected_PhysicalPhiFinC1ActionRestriction_or_NoExtraBoundarySource_ValueEmission_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    dynamic_packet = load(
        DATA / "selected_dynamicc1parityvaluepacket_after_stationarydotd_integration.candidate.json"
    )
    guardrail = load(
        DATA
        / "selected_dynamicc1parityvaluepacket_after_stationarydotd_integration"
        / "parity_patch_vs_unpatched_guardrail.packet.json"
    )
    principle = load(
        DATA
        / "selected_physicalmeasureidentity_or_routeaemissionclosure"
        / "finite_c1_trace_measure_principle_draft.packet.json"
    )
    trace_support = load(
        DATA
        / "selected_c1tracemeasurepromotion_or_actionboundaryproof"
        / "selected_trace_map_and_measure_support.packet.json"
    )
    finite_boundary = load(
        DATA
        / "selected_c1tracemeasurepromotion_or_actionboundaryproof"
        / "finite_trace_boundary_cancellation_certificate.packet.json"
    )
    route_a = load(
        DATA
        / "selected_physicalactionsourceemission_or_honestgalerkinreplacement"
        / "route_a_physical_source_emission_validator.packet.json"
    )

    trace_uniqueness = {
        "schema": "MTTFiniteWeylTraceUniquenessDerivation.v1",
        "status": "FINITE_WEYL_INVARIANT_MEASURE_UNIQUELY_NORMALIZED_TRACE",
        "finite_algebra": {
            "carrier": "selected qutrit Weyl response algebra",
            "generators": ["Z/clock", "X/shift"],
            "representation": "irreducible 3x3 Weyl pair; four routed sectors use the same normalized trace law",
            "commutant": "scalar multiples of identity",
            "invariant_functional": "tau(A)=Tr(A)/3 per qutrit block",
        },
        "derivation_steps": [
            "X and Z generate the full finite qutrit matrix algebra on the selected response block.",
            "Any normalized positive functional invariant under conjugation by X and Z has density matrix rho commuting with X and Z.",
            "By irreducibility / Schur commutant, rho is a scalar multiple of identity.",
            "Normalization fixes rho=I/3, hence the finite measure is the normalized trace.",
            "The induced quadratic C1 pairing is the trace/Frobenius pairing used by the finite Weyl row execution.",
        ],
        "derived_now": {
            "finite_measure_equals_normalized_trace": True,
            "trace_frobenius_pairing_for_finite_quotient": True,
            "measure_choice_is_not_a_new_knob": True,
            "measured_data_used": False,
        },
        "not_derived_now": {
            "physical_PhiFinC1_action_restricts_to_finite_quotient": True,
            "no_extra_physical_boundary_or_source_term": True,
            "same_source_b_selected_emission": True,
            "unpatched_dynamic_C1_packet_closed": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    principle_split = {
        "schema": "MTTFiniteC1TraceMeasurePrincipleSplit.v1",
        "status": "PRINCIPLE_SPLIT_MEASURE_DERIVED_ACTION_BOUNDARY_OPEN",
        "principle_name": principle["principle_name"],
        "original_principle_status": principle["status"],
        "clauses": {
            "finite_selected_C1_quotient": {
                "closed": True,
                "source": "previous stationary/dotD integration plus finite Weyl response packets",
            },
            "admissible_variations_represented_by_selected_qutrit_Weyl_response_algebra": {
                "closed": True,
                "source": "static routing plus finite Weyl trace row execution",
            },
            "physical_first_variation_uses_normalized_trace_Frobenius_measure": {
                "closed": True,
                "source": "finite Weyl invariant trace uniqueness derivation",
            },
            "physical_PhiFinC1_action_restricts_exactly_to_this_finite_measure": {
                "closed": False,
                "source_required": "same-source Phi_fin^C1 action restriction theorem or selected action rows",
            },
            "continuum_or_external_boundary_source_terms_absent": {
                "closed": False,
                "source_required": "physical boundary/source no-emission theorem or emitted zero boundary/source term",
            },
        },
        "what_this_improves": {
            "patch_measure_part_no_longer_axiomatic": True,
            "remaining_patch_gap_is_not_measure_normalization": True,
            "remaining_patch_gap_is_physical_action_boundary_source_binding": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    boundary_source = {
        "schema": "MTTPhysicalBoundarySourceRemainder.v1",
        "status": "PHYSICAL_ACTION_RESTRICTION_AND_BOUNDARY_SOURCE_REMAIN_OPEN",
        "imported_support": {
            "selected_trace_map_support_imported": trace_support["support_imported"][
                "selected_trace_map_values_functional_stationary"
            ],
            "dynamic_trace_binding_imported": trace_support["support_imported"]["dynamic_dotD_trace_binding"],
            "finite_trace_boundary_cancellation": finite_boundary["algebraic_boundary_closed_now"],
            "patched_dynamic_C1_values_available": dynamic_packet["closure_decision"][
                "SM_parity_patched_dynamic_C1_value_packet_available"
            ],
        },
        "route_A_current_emissions": route_a["current_emissions"],
        "minimal_next_emissions": [
            "physical_PhiFinC1_action_identity",
            "physical_action_restricts_to_selected_finite_Weyl_quotient",
            "no_extra_physical_boundary_or_source_term",
            "same_source_b_selected_emission",
            "phase_R_Z_source_selection",
            "shift_R_X_source_selection",
        ],
        "if_all_minimal_next_emissions_hold": principle["would_promote_if_inserted_or_derived"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedFiniteWeylTraceUniquenessOrPhysicalBoundarySourceDerivation",
        "status": STATUS,
        "inputs": {
            "dynamic_c1_parity_value_packet": rel(
                DATA / "selected_dynamicc1parityvaluepacket_after_stationarydotd_integration.candidate.json"
            ),
            "parity_patch_guardrail": rel(
                DATA
                / "selected_dynamicc1parityvaluepacket_after_stationarydotd_integration"
                / "parity_patch_vs_unpatched_guardrail.packet.json"
            ),
            "finite_c1_trace_measure_principle_draft": rel(
                DATA
                / "selected_physicalmeasureidentity_or_routeaemissionclosure"
                / "finite_c1_trace_measure_principle_draft.packet.json"
            ),
            "selected_trace_map_and_measure_support": rel(
                DATA
                / "selected_c1tracemeasurepromotion_or_actionboundaryproof"
                / "selected_trace_map_and_measure_support.packet.json"
            ),
            "finite_trace_boundary_cancellation_certificate": rel(
                DATA
                / "selected_c1tracemeasurepromotion_or_actionboundaryproof"
                / "finite_trace_boundary_cancellation_certificate.packet.json"
            ),
            "route_a_physical_source_emission_validator": rel(
                DATA
                / "selected_physicalactionsourceemission_or_honestgalerkinreplacement"
                / "route_a_physical_source_emission_validator.packet.json"
            ),
        },
        "output_packets": {
            "finite_weyl_trace_uniqueness_derivation": rel(TRACE_UNIQUENESS),
            "finite_c1_trace_measure_principle_split": rel(PRINCIPLE_SPLIT),
            "physical_boundary_source_remainder": rel(BOUNDARY_SOURCE),
        },
        "theorem": {
            "name": "FiniteWeylTraceUniquenessDerivationTheorem",
            "proved": True,
            "statement": (
                "For the selected finite qutrit Weyl response algebra, the normalized trace/Frobenius C1 measure "
                "is forced by Weyl-conjugation invariance and irreducibility, so the measure-normalization part "
                "of the SelectedFiniteC1TraceMeasurePrinciple is not a free patch knob. The remaining unpatched "
                "gap is physical: prove that Phi_fin^C1/action restricts to this finite quotient with no extra "
                "boundary/source term and emits the same-source b_selected/R_Z/R_X data."
            ),
        },
        "what_closes_now": {
            "finite_Weyl_invariant_trace_measure_derived": True,
            "trace_Frobenius_pairing_measure_part_not_free": True,
            "patched_values_reinterpreted_with_derived_measure_normalization": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "physical_PhiFinC1_action_identity": True,
            "physical_action_restriction_to_finite_Weyl_quotient": True,
            "no_extra_physical_boundary_or_source_term": True,
            "same_source_b_selected_emission": True,
            "phase_R_Z_source_selection": True,
            "shift_R_X_source_selection": True,
            "unpatched_dynamic_C1_packet_closure": True,
            "true_SM_equivalence_closure": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "measure_normalization_derived": True,
            "SelectedFiniteC1TraceMeasurePrinciple_fully_derived": False,
            "unpatched_A_selected_emitted": False,
            "unpatched_b_selected_emitted": False,
            "unpatched_deltaTheta_C1_emitted": False,
            "unpatched_dynamic_C1_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "superset_strategy": {
            "combining_paths": guardrail["superset_strategy"]["combining_paths"],
            "locked_target": "derive the measure-normalization clause, then isolate physical action/boundary source",
            "paths_used": [
                "finite qutrit Weyl algebra / Schur trace uniqueness",
                "stationary/dotD integrated source spine",
                "patched dynamic C1 value packet as consistency target only",
                "finite boundary cancellation support",
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_FiniteWeylTraceUniqueness_or_PhysicalBoundarySource_Derivation_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "measure_normalization_derived": True,
        "SelectedFiniteC1TraceMeasurePrinciple_fully_derived": False,
        "unpatched_dynamic_C1_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected FiniteWeyl TraceUniqueness or PhysicalBoundarySource Derivation v1

Status: `{STATUS}`.

This artifact derives the measure-normalization part of the local dynamic C1
patch.  On the selected qutrit Weyl response algebra, any normalized positive
functional invariant under `X` and `Z` conjugation has scalar density by the
Weyl commutant, hence is the normalized trace.  The trace/Frobenius pairing is
therefore not a new knob.

This does not yet prove the full unpatched dynamic C1 theorem.  What remains is
the physical binding clause: `Phi_fin^C1`/action must restrict to this finite
Weyl quotient with no extra boundary/source term and must emit the same-source
`b_selected`, `R_Z`, and `R_X` data.
"""

    for path, payload in [
        (TRACE_UNIQUENESS, trace_uniqueness),
        (PRINCIPLE_SPLIT, principle_split),
        (BOUNDARY_SOURCE, boundary_source),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
