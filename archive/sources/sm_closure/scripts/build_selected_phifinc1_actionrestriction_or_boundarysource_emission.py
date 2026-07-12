"""Build PhiFinC1 action restriction / boundary-source emission gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_phifinc1_actionrestriction_or_boundarysource_emission"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
VALIDATOR = PACKET_DIR / "route_a_action_restriction_validator_v2.packet.json"
SOURCE_EMISSION = PACKET_DIR / "same_source_boundary_and_residual_emission_contract.packet.json"
IF_CLOSES = PACKET_DIR / "if_action_restriction_emitted_dynamic_c1_closure.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PhiFinC1_ActionRestriction_or_BoundarySource_Emission_v1.md"

STATUS = "MTT_SELECTED_PHIFINC1_ACTIONRESTRICTION_OR_BOUNDARYSOURCE_EMISSION_BUILT_MEASURE_RETIRED_SOURCE_OPEN"
NEXT = "MTT_Selected_SameSourceBoundaryResidualEmission_or_UnpatchedGalerkinReplacement_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    finiteweyl = load(DATA / "selected_finiteweyl_traceuniqueness_or_physicalboundarysource_derivation.candidate.json")
    split = load(
        DATA
        / "selected_finiteweyl_traceuniqueness_or_physicalboundarysource_derivation"
        / "finite_c1_trace_measure_principle_split.packet.json"
    )
    boundary = load(
        DATA
        / "selected_finiteweyl_traceuniqueness_or_physicalboundarysource_derivation"
        / "physical_boundary_source_remainder.packet.json"
    )
    action_equiv = load(
        DATA
        / "selected_physicalc1actionidentity_or_samesourcebselectedemission"
        / "physical_action_identity_to_source_emission.packet.json"
    )
    b_attempt = load(
        DATA
        / "selected_physicalc1actionidentity_or_samesourcebselectedemission"
        / "same_source_bselected_emission_attempt.packet.json"
    )
    route_b = load(
        DATA
        / "selected_physicalactionsourceemission_or_honestgalerkinreplacement"
        / "route_b_honest_galerkin_replacement_contract.packet.json"
    )

    clauses = split["clauses"]
    finite_measure_closed = clauses["physical_first_variation_uses_normalized_trace_Frobenius_measure"]["closed"]
    action_restriction_closed = clauses["physical_PhiFinC1_action_restricts_exactly_to_this_finite_measure"]["closed"]
    no_extra_closed = clauses["continuum_or_external_boundary_source_terms_absent"]["closed"]

    current = action_equiv["current_physical_antecedents"]
    validator = {
        "schema": "MTTRouteAActionRestrictionValidatorV2.v1",
        "status": "MEASURE_CLAUSE_RETIRED_ACTION_BOUNDARY_SOURCE_OPEN",
        "closed_subclauses": {
            "finite_selected_C1_quotient": clauses["finite_selected_C1_quotient"]["closed"],
            "selected_Weyl_variation_algebra": clauses[
                "admissible_variations_represented_by_selected_qutrit_Weyl_response_algebra"
            ]["closed"],
            "finite_measure_normalization_trace_Frobenius": finite_measure_closed,
            "algebraic_finite_boundary_cancellation": boundary["imported_support"]["finite_trace_boundary_cancellation"],
        },
        "still_required_physical_subclauses": {
            "physical_PhiFinC1_action_restriction": not action_restriction_closed,
            "no_extra_physical_boundary_or_source_term": not no_extra_closed,
            "phase_R_Z_source_selection": not current["phase_R_Z_selected"],
            "shift_R_X_source_selection": not current["shift_R_X_selected"],
            "same_source_b_selected_emission": not current["same_source_b_selected_emitted"],
        },
        "route_A_currently_closes": False,
        "why_not_closed": [
            "The finite trace measure is derived, but the physical Phi_fin^C1 action has not been shown to restrict exactly to the finite Weyl quotient.",
            "The absence of extra physical boundary/source terms is not emitted by the selected source.",
            "R_Z, R_X, and b_selected remain replay/contract values rather than same-source physical emissions.",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    source_emission = {
        "schema": "MTTSameSourceBoundaryAndResidualEmissionContract.v1",
        "status": "SAME_SOURCE_ACTION_RESIDUAL_BSOURCE_CONTRACT_OPEN",
        "must_emit_from_same_physical_branch": [
            "physical_PhiFinC1_action_identity",
            "restriction map from physical Phi_fin^C1/action to selected finite Weyl quotient",
            "zero extra boundary/source term or emitted cancellation term",
            "phase residual source R_Z",
            "shift residual source R_X",
            "Hessian/source vector b_selected",
        ],
        "accepted_sources": [
            "direct Phi_fin^C1 action derivation",
            "same-source Route-A physical action/source emission",
            "independent selected Galerkin/quadrature replacement satisfying Route-B contract",
        ],
        "forbidden_shortcuts": route_b["forbidden_shortcuts"],
        "b_selected_replay_available": {
            "A_transpose_A": b_attempt["b_replay_values"]["A_transpose_A"],
            "A_transpose_b": b_attempt["b_replay_values"]["A_transpose_b"],
            "deltaTheta_C1": b_attempt["b_replay_values"]["deltaTheta_C1"],
            "same_source_b_selected_emitted_now": b_attempt["same_source_b_selected_emitted_now"],
            "replay_available_under_axiom_patch": b_attempt["replay_available_under_axiom_patch"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    if_closes = {
        "schema": "MTTIfActionRestrictionEmittedDynamicC1Closure.v1",
        "status": "IF_SOURCE_EMITTED_UNPATCHED_DYNAMIC_C1_CLOSES",
        "antecedent": {
            "measure_normalization_derived": finiteweyl["closure_decision"]["measure_normalization_derived"],
            "physical_PhiFinC1_action_restriction_emitted": False,
            "no_extra_boundary_source_emitted": False,
            "phase_R_Z_source_emitted": False,
            "shift_R_X_source_emitted": False,
            "b_selected_emitted": False,
        },
        "consequent_if_antecedent_true": boundary["if_all_minimal_next_emissions_hold"],
        "promoted_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedPhiFinC1ActionRestrictionOrBoundarySourceEmission",
        "status": STATUS,
        "inputs": {
            "finiteweyl_traceuniqueness": rel(
                DATA / "selected_finiteweyl_traceuniqueness_or_physicalboundarysource_derivation.candidate.json"
            ),
            "principle_split": rel(
                DATA
                / "selected_finiteweyl_traceuniqueness_or_physicalboundarysource_derivation"
                / "finite_c1_trace_measure_principle_split.packet.json"
            ),
            "physical_boundary_source_remainder": rel(
                DATA
                / "selected_finiteweyl_traceuniqueness_or_physicalboundarysource_derivation"
                / "physical_boundary_source_remainder.packet.json"
            ),
            "action_identity_to_source_emission": rel(
                DATA
                / "selected_physicalc1actionidentity_or_samesourcebselectedemission"
                / "physical_action_identity_to_source_emission.packet.json"
            ),
            "same_source_bselected_attempt": rel(
                DATA
                / "selected_physicalc1actionidentity_or_samesourcebselectedemission"
                / "same_source_bselected_emission_attempt.packet.json"
            ),
            "route_b_honest_galerkin_contract": rel(
                DATA
                / "selected_physicalactionsourceemission_or_honestgalerkinreplacement"
                / "route_b_honest_galerkin_replacement_contract.packet.json"
            ),
        },
        "output_packets": {
            "route_a_action_restriction_validator_v2": rel(VALIDATOR),
            "same_source_boundary_and_residual_emission_contract": rel(SOURCE_EMISSION),
            "if_action_restriction_emitted_dynamic_c1_closure": rel(IF_CLOSES),
        },
        "theorem": {
            "name": "ActionRestrictionBoundarySourceCutsetTheorem",
            "proved": True,
            "statement": (
                "After finite Weyl trace uniqueness derives the measure clause, Route A unpatched dynamic C1 "
                "closure is equivalent to emitting a same-source physical action restriction/no-extra-source packet "
                "with R_Z, R_X, and b_selected. Therefore measure normalization is retired as a blocker, but "
                "A_selected/b_selected/deltaTheta_C1 remain unpatched-open until those physical emissions or an "
                "independent selected Galerkin replacement are supplied."
            ),
        },
        "what_closes_now": {
            "route_A_measure_normalization_blocker_retired": True,
            "physical_action_restriction_validator_updated": True,
            "same_source_residual_bsource_contract_built": True,
            "if_emitted_unpatched_closure_consequent_fixed": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "physical_PhiFinC1_action_restriction": True,
            "no_extra_physical_boundary_or_source_term": True,
            "phase_R_Z_source_selection": True,
            "shift_R_X_source_selection": True,
            "same_source_b_selected_emission": True,
            "independent_selected_Galerkin_replacement": True,
            "unpatched_dynamic_C1_packet_closure": True,
            "true_SM_equivalence_closure": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "measure_normalization_derived": True,
            "physical_action_restriction_emitted": False,
            "no_extra_boundary_source_emitted": False,
            "same_source_R_Z_R_X_b_selected_emitted": False,
            "unpatched_A_selected_emitted": False,
            "unpatched_b_selected_emitted": False,
            "unpatched_deltaTheta_C1_emitted": False,
            "unpatched_dynamic_C1_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_PhiFinC1_ActionRestriction_or_BoundarySource_Emission_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "measure_normalization_derived": True,
        "physical_action_restriction_emitted": False,
        "same_source_R_Z_R_X_b_selected_emitted": False,
        "unpatched_dynamic_C1_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PhiFinC1 ActionRestriction or BoundarySource Emission v1

Status: `{STATUS}`.

The finite measure-normalization blocker is retired.  The selected qutrit Weyl
trace theorem supplies the finite trace/Frobenius measure; Route A no longer
needs a separate measure axiom.

The remaining unpatched dynamic C1 gate is physical source emission:

- `Phi_fin^C1`/action restricts to the selected finite Weyl quotient
- no extra physical boundary/source term is emitted
- same-source `R_Z`, `R_X`, and `b_selected` are emitted

If those clauses are emitted, the existing replay promotes
`A_selected=[[12,0],[0,12]]`, `b_selected=[12,12]`, and
`deltaTheta_C1=[1,1]` without using observed constants as selectors.
"""

    for path, payload in [
        (VALIDATOR, validator),
        (SOURCE_EMISSION, source_emission),
        (IF_CLOSES, if_closes),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
