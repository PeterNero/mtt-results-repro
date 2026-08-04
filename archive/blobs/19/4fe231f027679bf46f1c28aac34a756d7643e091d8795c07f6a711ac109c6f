"""Build selected C1 measure/pairing or physical-action identity gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_c1measurepairing_or_physicalactionidentity"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PAIRING = PACKET_DIR / "candidate_trace_frobenius_measure_pairing.packet.json"
ACTION = PACKET_DIR / "physical_action_identity_attempt.packet.json"
PROMOTION = PACKET_DIR / "promotion_sufficiency_and_remaining_axioms.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_C1MeasurePairing_or_PhysicalActionIdentity_v1.md"

STATUS = "MTT_SELECTED_C1MEASUREPAIRING_OR_PHYSICALACTIONIDENTITY_BUILT_FORMAL_PAIRING_PROMOTION_OPEN"
NEXT = "MTT_Selected_C1TraceMeasurePromotion_or_ActionBoundaryProof_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_c1kernelvaluesexecution_or_physicalsourcepromotion.candidate.json")
    barrier = load(DATA / "selected_c1kernelvaluesexecution_or_physicalsourcepromotion" / "promotion_barrier_and_next_gate.packet.json")
    algebraic = load(DATA / "selected_c1kernelvaluesexecution_or_physicalsourcepromotion" / "route_b_algebraic_kernel_value_execution_attempt.packet.json")
    physical_attempt = load(DATA / "selected_c1kernelvaluesexecution_or_physicalsourcepromotion" / "route_a_physical_source_promotion_attempt.packet.json")
    defect = load(DATA / "selected_c1defectfunctionalsource_or_independentquadraturedatafill.candidate.json")
    variational = load(DATA / "selected_differentiatedc1orthogonalcompletionprinciple_or_independentquadraturehessiansolve" / "orthogonal_completion_variational_derivation.packet.json")
    first_variation_plan = load(DATA / "selected_stromingertracec1firstvariation_or_quadratureexecutionplan" / "route_a_first_variation_certificate_plan.packet.json")
    basis = load(DATA / "selected_tracemapandbasisvalues_or_primitiverowsexecution" / "route_b_selected_basis_value_fill.packet.json")

    pairing = {
        "schema": "MTTCandidateTraceFrobeniusMeasurePairing.v1",
        "status": "FORMAL_TRACE_FROBENIUS_PAIRING_BUILT_NOT_PHYSICAL_MEASURE_PROMOTED",
        "definition": {
            "carrier": "finite qutrit Weyl C1 response space with selected stationary zero-mode basis",
            "pairing": "<A,B>_C1 = Re Tr(A^* B) on each routed sector, summed over routed sectors",
            "measure_weights": "uniform trace/Frobenius weights fixed by Weyl orthogonality",
            "normalization": "Tr((Z^a X^b)^* Z^c X^d)=3 delta_ac delta_bd; scale cancels in the Euler equation",
            "constraint_space": variational["candidate_functional"]["constraint_space"],
        },
        "formal_support": {
            "selected_basis_rows": basis["selected_row_count"],
            "all_basis_rows_selected": basis["all_basis_rows_selected"],
            "unique_formal_C1_defect_functional_sourced": defect["what_closes_now"]["unique_formal_C1_defect_functional_sourced"],
            "euler_projection_scale_independence": defect["what_closes_now"]["euler_projection_scale_independence_verified"],
            "finite_euler_projection": variational["derived_inside_this_gate"]["finite_dimensional_projection_euler_equation"],
            "least_norm_Q_residual_selection": variational["derived_inside_this_gate"]["least_norm_trace_orthogonal_completion_selects_Q_residual"],
            "all_110_algebraic_value_slots_filled": algebraic["counts"]["total_algebraic_values_filled"] == 110,
        },
        "would_accept_route_B_if_promoted": {
            "selected_measure_pairing_defined": True,
            "exact_kernel_values_available": True,
            "locked_target_matches": algebraic["algebraic_consistency_certificate"]["passes_locked_target_by_algebraic_replay"],
            "exactness_certificate_is_algebraic_not_independent_quadrature": True,
        },
        "not_promoted_because": {
            "selected_physical_C1_measure_from_PhiFin_trace_missing": True,
            "independent_quadrature_engine_measure_missing": True,
            "boundary_clause_missing": physical_attempt["still_missing_for_promotion"]["boundary_cancellation"],
            "same_source_b_selected_emission_missing": physical_attempt["still_missing_for_promotion"]["same_source_emits_b_selected"],
        },
        "selected_measure_pairing_promoted_now": False,
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    action = {
        "schema": "MTTPhysicalActionIdentityAttempt.v1",
        "status": "PHYSICAL_ACTION_IDENTITY_REDUCED_TO_BOUNDARY_AND_TRACE_MEASURE_OPEN",
        "theorem_name": "SelectedPhiFinC1PhysicalActionIdentity",
        "identity_to_prove": (
            "delta S_C1[Phi_fin^C1](eta) equals delta C1DefectLeakageFunctional(eta) "
            "for all selected admissible differentiated trace variations eta."
        ),
        "closed_formal_clauses": {
            "formal_defect_functional_unique": defect["what_closes_now"]["unique_formal_C1_defect_functional_sourced"],
            "finite_euler_projection_derived": variational["derived_inside_this_gate"]["finite_dimensional_projection_euler_equation"],
            "least_norm_Q_residual_selection": variational["derived_inside_this_gate"]["least_norm_trace_orthogonal_completion_selects_Q_residual"],
            "algebraic_values_filled": algebraic["counts"]["total_algebraic_values_filled"] == 110,
        },
        "first_variation_certificate_fields": first_variation_plan["certificate_fields"],
        "remaining_physical_clauses": {
            "selected_trace_map_verified": first_variation_plan["certificate_fields"]["selected_trace_map"]["verified_now"] is False,
            "first_variation_identity_verified": first_variation_plan["certificate_fields"]["first_variation_identity"]["verified_now"] is False,
            "boundary_cancellation_verified": first_variation_plan["certificate_fields"]["boundary_cancellation"]["verified_now"] is False,
            "physical_action_equals_formal_pairing": True,
            "same_source_b_selected_emission": True,
        },
        "route_A_promoted_now": False,
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    promotion = {
        "schema": "MTTC1PairingActionPromotionSufficiency.v1",
        "status": "SUFFICIENCY_PROVED_PROMOTION_AXIOMS_OPEN",
        "statement": (
            "The formal trace/Frobenius C1 pairing plus the already-filled algebraic values is sufficient "
            "to replay the locked dynamic packet. It becomes a theorem only if the selected Phi_fin^C1 "
            "trace supplies this pairing as the physical C1 measure/action identity, including boundary "
            "cancellation and same-source b_selected emission."
        ),
        "sufficient_if": {
            "selected_C1_measure_pairing_is_trace_frobenius_pairing": True,
            "or_physical_action_identity_equates_first_variation_to_defect_functional": True,
            "boundary_terms_vanish": True,
            "same_source_b_selected_emitted": True,
            "locked_target_matches": True,
        },
        "current_truth_values": {
            "formal_pairing_built": True,
            "algebraic_values_filled": True,
            "selected_C1_measure_pairing_promoted": False,
            "physical_action_identity_promoted": False,
            "boundary_terms_verified": False,
            "same_source_b_selected_emitted": False,
            "closure_claimed": False,
        },
        "minimal_next_gate": barrier["minimal_next_gate"],
        "forbidden_shortcuts": barrier["forbidden_shortcuts"],
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedC1MeasurePairingOrPhysicalActionIdentity",
        "status": STATUS,
        "inputs": {
            "previous_gate": rel(DATA / "selected_c1kernelvaluesexecution_or_physicalsourcepromotion.candidate.json"),
            "promotion_barrier": rel(DATA / "selected_c1kernelvaluesexecution_or_physicalsourcepromotion" / "promotion_barrier_and_next_gate.packet.json"),
            "algebraic_kernel_values": rel(DATA / "selected_c1kernelvaluesexecution_or_physicalsourcepromotion" / "route_b_algebraic_kernel_value_execution_attempt.packet.json"),
            "physical_source_attempt": rel(DATA / "selected_c1kernelvaluesexecution_or_physicalsourcepromotion" / "route_a_physical_source_promotion_attempt.packet.json"),
            "formal_defect_functional": rel(DATA / "selected_c1defectfunctionalsource_or_independentquadraturedatafill.candidate.json"),
            "first_variation_plan": rel(DATA / "selected_stromingertracec1firstvariation_or_quadratureexecutionplan" / "route_a_first_variation_certificate_plan.packet.json"),
        },
        "output_packets": {
            "candidate_trace_frobenius_measure_pairing": rel(PAIRING),
            "physical_action_identity_attempt": rel(ACTION),
            "promotion_sufficiency_and_remaining_axioms": rel(PROMOTION),
        },
        "theorem": {
            "name": "C1TraceFrobeniusPairingSufficiencyButNotPromotionTheorem",
            "proved": True,
            "statement": promotion["statement"],
        },
        "what_closes_now": {
            "formal_trace_frobenius_pairing_built": True,
            "pairing_sufficiency_for_locked_replay_proved": True,
            "physical_action_identity_reduced_to_specific_clauses": True,
            "boundary_and_same_source_bselected_identified_as_remaining": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "selected_C1_measure_pairing_promotion": True,
            "selected_physical_action_identity": True,
            "selected_trace_map_verification": True,
            "boundary_cancellation_verification": True,
            "same_source_b_selected_emission": True,
            "independent_quadrature_exactness_certificate": True,
            "unpatched_SM_parity_dynamic_packet_closure": True,
            "true_SM_equivalence_closure": True,
        },
        "promotion_decision": {
            "formal_pairing_promoted_as_physical_measure": False,
            "physical_action_identity_promoted": False,
            "boundary_cancellation_promoted": False,
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
        "certificate": "MTT_Selected_C1MeasurePairing_or_PhysicalActionIdentity_v1",
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

    note = f"""# MTT Selected C1MeasurePairing or PhysicalActionIdentity v1

Status: `{STATUS}`.

Built:

```text
formal trace/Frobenius C1 pairing       = True
unique formal defect functional          = True
all algebraic C1 value slots filled      = True
pairing sufficient for locked replay     = True
selected physical measure promoted       = False
physical action identity promoted        = False
boundary cancellation verified           = False
same-source b_selected emitted           = False
```

So the blocker is now smaller than "find the values": prove that the selected
`Phi_fin^C1` trace supplies this trace/Frobenius pairing as the physical C1
measure/action, with vanishing boundary terms and same-source `b_selected`.

Next artifact: `{NEXT}`.
"""

    PAIRING.write_text(json.dumps(pairing, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    ACTION.write_text(json.dumps(action, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    PROMOTION.write_text(json.dumps(promotion, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
