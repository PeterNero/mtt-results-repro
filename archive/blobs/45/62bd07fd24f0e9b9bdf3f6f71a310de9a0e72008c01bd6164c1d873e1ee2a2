"""Build post-Pi no-knob value derivation / minimal universal parameter policy artifact."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_noknobvaluederivationpostpi_or_minimaluniversalparameterpolicy"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
FINAL_RECHECK = PACKET_DIR / "final_no_knob_value_derivation_recheck.packet.json"
EXTERNAL_BOUNDARY = PACKET_DIR / "post_pi_external_replay_boundary.packet.json"
POLICY_MATRIX = PACKET_DIR / "minimal_universal_parameter_policy_matrix.packet.json"
READINESS = PACKET_DIR / "rtheta_readiness_final_frontier.packet.json"
CUTSET = PACKET_DIR / "final_cutset_after_no_knob_recheck.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_NoKnobValueDerivationPostPi_or_MinimalUniversalParameterPolicy_v1.md"

PREVIOUS = DATA / "selected_fullprofileordiagonaltheorempostpi_or_noknobvaluederivation.candidate.json"
PREV_READINESS = (
    DATA
    / "selected_fullprofileordiagonaltheorempostpi_or_noknobvaluederivation"
    / "rtheta_value_readiness_after_diagonal_theorem.packet.json"
)
PREV_NOKNOB = (
    DATA
    / "selected_fullprofileordiagonaltheorempostpi_or_noknobvaluederivation"
    / "no_knob_value_derivation_recheck_after_profile.packet.json"
)
PREV_DIAGONAL = (
    DATA
    / "selected_fullprofileordiagonaltheorempostpi_or_noknobvaluederivation"
    / "accepted_diagonal_profile_theorem_after_external_rows.packet.json"
)
POST_PI_ROWS = (
    DATA
    / "selected_thresholdmatchingrowspostpi_or_massschemesourcerows"
    / "external_row_admission_not_rtheta_selection.packet.json"
)
VALUE_KERNEL = (
    DATA
    / "selected_valuesourcederivationobligationkernel_or_externalthresholdimportmanifest"
    / "value_source_derivation_obligation_kernel.packet.json"
)
UNIVERSAL_POLICY = DATA / "universal_source_parameter_policy.candidate.json"
UNIVERSAL_CANDIDATES = DATA / "universal_source_parameter_policy" / "candidate_universal_parameters.packet.json"
RTHETA_BASIS_DECISION = (
    DATA
    / "selected_rthetavaluerows_or_universalsourceanchortheorem"
    / "rtheta_value_rows_or_universal_anchor_decision.packet.json"
)
RTHETA_COEFFICIENT_ATTEMPT = (
    DATA
    / "selected_rthetavaluerows_or_universalsourceanchortheorem"
    / "rtheta_value_row_coefficients_attempt.packet.json"
)

STATUS = (
    "MTT_SELECTED_NOKNOBVALUEDERIVATIONPOSTPI_OR_MINIMALUNIVERSALPARAMETERPOLICY_"
    "BUILT_FINAL_FRONTIER_EXTERNAL_REPLAY_READY_NOKNOB_OPEN"
)
NEXT = "MTT_Selected_InternalRThetaValueDerivation_or_MinimalUniversalParameterSelection_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing no-knob frontier sources: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREV_READINESS,
        PREV_NOKNOB,
        PREV_DIAGONAL,
        POST_PI_ROWS,
        VALUE_KERNEL,
        UNIVERSAL_POLICY,
        UNIVERSAL_CANDIDATES,
        RTHETA_BASIS_DECISION,
        RTHETA_COEFFICIENT_ATTEMPT,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    prev_readiness = load(PREV_READINESS)
    prev_noknob = load(PREV_NOKNOB)
    prev_diagonal = load(PREV_DIAGONAL)
    post_pi_rows = load(POST_PI_ROWS)
    value_kernel = load(VALUE_KERNEL)
    universal_policy = load(UNIVERSAL_POLICY)
    universal_candidates = load(UNIVERSAL_CANDIDATES)
    rtheta_basis = load(RTHETA_BASIS_DECISION)
    rtheta_coefficients = load(RTHETA_COEFFICIENT_ATTEMPT)

    external_threshold_rows = post_pi_rows["accepted_external_threshold_row_count"]
    external_mass_rows = post_pi_rows["accepted_external_mass_scheme_row_count"]
    accepted_diagonal = prev_diagonal["accepted_diagonal_theorem_closed"]
    external_replay_ready = external_threshold_rows == 7 and external_mass_rows == 3 and accepted_diagonal

    final_recheck = {
        "schema": "MTTFinalNoKnobValueDerivationRecheck.v1",
        "status": "FINAL_RECHECK_NOKNOB_VALUE_DERIVATION_OPEN",
        "previous_no_knob_source": rel(PREV_NOKNOB),
        "value_kernel_source": rel(VALUE_KERNEL),
        "rtheta_basis_source": rel(RTHETA_BASIS_DECISION),
        "rtheta_coefficient_attempt_source": rel(RTHETA_COEFFICIENT_ATTEMPT),
        "present_count": prev_readiness["present_count"],
        "requirement_count": prev_readiness["requirement_count"],
        "blocking_failures": prev_readiness["blocking_failures"],
        "obligation_count": value_kernel["required_row_count"],
        "closed_obligation_count_under_no_knob": value_kernel["closed_row_count"],
        "basis_map_to_sector_scaled_magnitude_rows_closed": rtheta_basis[
            "basis_map_to_sector_scaled_magnitude_rows_closed"
        ],
        "coefficient_functional_closed": rtheta_basis["coefficient_functional_closed"],
        "accepted_coefficient_value_count": rtheta_coefficients["accepted_coefficient_row_count"],
        "lambda_H_coefficient_selected": rtheta_coefficients["lambda_H_coefficient_selected"],
        "selected_threshold_response_functional_instantiated": prev_readiness[
            "selected_threshold_response_functional_instantiated"
        ],
        "selected_internal_value_emission_count": 0,
        "selected_universal_parameter_count": universal_policy["selected_parameter_count_now"],
        "no_knob_value_derivation_closed": False,
        "full_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
        "why_not_closed": [
            "the selected charged basis exists, but its coefficient functional still has zero accepted selected rows",
            "post-Pi threshold and mass rows are admitted external replay rows, not internal selected MTT emissions",
            "the universal source-parameter tier exists, but no universal parameter is selected in this repo",
            "the value-source obligation kernel still has zero closed no-knob obligations",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(FINAL_RECHECK, final_recheck)

    external_boundary = {
        "schema": "MTTPostPiExternalReplayBoundary.v1",
        "status": "POST_PI_EXTERNAL_REPLAY_READY_TRUE_EQUIVALENCE_AND_NOKNOB_OPEN",
        "post_pi_external_replay_ready": external_replay_ready,
        "SM_parity_external_replay_boundary_declared": True,
        "threshold_rows_at_admitted_external_tier": external_threshold_rows,
        "mass_scheme_rows_at_admitted_external_tier": external_mass_rows,
        "accepted_diagonal_profile_theorem_closed": accepted_diagonal,
        "external_rows_used_as_branch_selector": post_pi_rows["guardrails"][
            "external_rows_used_as_branch_selector"
        ],
        "target_fit_after_residuals": post_pi_rows["guardrails"]["target_fit_after_residuals"],
        "what_is_ready": [
            "post-Pi admitted external threshold rows",
            "post-Pi admitted external mass-scheme rows",
            "accepted diagonal profile theorem for the admitted external replay tier",
        ],
        "what_this_does_not_close": [
            "selected internal Rtheta threshold/mass derivation",
            "selected threshold response functional instantiation",
            "selected coefficient values or lambda_H",
            "Yukawa/mass/mixing no-knob prediction",
            "true SM equivalence",
            "full no-knob closure",
        ],
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(EXTERNAL_BOUNDARY, external_boundary)

    policy_options = [
        {
            "id": "U0-NOKNOB",
            "description": "derive all threshold, mass, Yukawa, mixing, CP, and Higgs rows internally from selected MTT geometry",
            "selected_now": False,
            "would_close_full_no_knob_if_proved": True,
            "current_blocker": "no selected internal coefficient/value functional emits the numeric rows",
        },
        {
            "id": "U1-SINGLE-SOURCE-ANCHOR",
            "description": "one source-selected universal anchor shared across all affected sectors",
            "candidate_classes": ["UP-ACTION-NORM", "UP-RET-OVERLAP", "UP-PHASE"],
            "selected_now": False,
            "would_preserve_credibility_if_source_selected": True,
            "current_blocker": "no candidate-specific source theorem selects one parameter before empirical replay",
        },
        {
            "id": "U2-SCALE-AND-ORIENTATION",
            "description": "two universal source anchors, one absolute/source-strength scale and one finite orientation/phase branch",
            "candidate_classes": ["UP-ABS-SCALE", "UP-RET-OVERLAP", "UP-PHASE"],
            "selected_now": False,
            "would_preserve_credibility_if_source_selected": True,
            "current_blocker": "two anchors are policy-admissible only after independent source selection and cross-use audits",
        },
        {
            "id": "UX-EXTERNAL-REPLAY-PACK",
            "description": "use admitted external threshold/mass/profile rows as replay inputs",
            "selected_now": True,
            "accepted_for_SM_parity_replay": True,
            "accepted_for_full_no_knob": False,
            "current_blocker": "external replay rows are downstream empirical/standard-theory rows, not selected MTT source emissions",
        },
    ]
    policy_matrix = {
        "schema": "MTTMinimalUniversalParameterPolicyMatrix.v1",
        "status": "POLICY_MATRIX_BUILT_NO_UNIVERSAL_PARAMETER_SELECTED",
        "policy_source": rel(UNIVERSAL_POLICY),
        "candidate_classes_source": rel(UNIVERSAL_CANDIDATES),
        "candidate_class_count": len(universal_candidates["candidate_classes"]),
        "selected_universal_parameter_count": universal_policy["selected_parameter_count_now"],
        "maximum_live_universal_parameters": universal_policy["maximum_live_universal_parameters"],
        "minimal_universal_parameter_selection_closed": False,
        "candidate_specific_source_theorem_present": False,
        "policy_options": policy_options,
        "selected_policy_for_no_knob": None,
        "external_replay_policy_ready": True,
        "external_replay_policy_is_no_knob": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(POLICY_MATRIX, policy_matrix)

    readiness = {
        "schema": "MTTRThetaReadinessFinalFrontier.v1",
        "status": "READINESS_HELD_AT_8_OF_9_NOKNOB_VALUE_DERIVATION_OPEN",
        "previous_readiness_source": rel(PREV_READINESS),
        "present_count": prev_readiness["present_count"],
        "requirement_count": prev_readiness["requirement_count"],
        "blocking_failures": prev_readiness["blocking_failures"],
        "only_remaining_readiness_blocker": "no_knob_value_derivation",
        "readiness_fraction": f"{prev_readiness['present_count']}/{prev_readiness['requirement_count']}",
        "can_claim_admitted_external_replay_boundary": True,
        "can_claim_true_SM_equivalence": False,
        "can_claim_full_no_knob": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(READINESS, readiness)

    cutset = {
        "schema": "MTTFinalCutsetAfterNoKnobRecheck.v1",
        "status": "FINAL_CUTSET_INTERNAL_RTHETA_VALUE_DERIVATION_OR_MINIMAL_PARAMETER_SELECTION",
        "closed_now": {
            "post_pi_final_no_knob_recheck": True,
            "SM_parity_external_replay_boundary_declared": True,
            "minimal_universal_parameter_policy_matrix_built": True,
            "Rtheta_readiness_fixed_at_8_of_9": True,
            "basis_vs_coefficient_distinction_preserved": True,
        },
        "still_open": {
            "no_knob_value_derivation": True,
            "selected_internal_Rtheta_threshold_mass_derivation": True,
            "selected_threshold_response_functional_instantiated": True,
            "numeric_Rtheta_coefficient_values": True,
            "lambda_H_value_execution": True,
            "Yukawa_mass_mixing_value_closure": True,
            "minimal_universal_parameter_selection": True,
            "candidate_specific_universal_source_theorem": True,
            "true_SM_equivalence": True,
            "full_no_knob": True,
        },
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "derive selected internal Rtheta coefficient/value rows from the already closed basis map and MTT Hessian/retarded-kernel source",
            "route_B": "prove a candidate-specific universal source-anchor theorem and then replay every affected row without per-observable fitting",
            "route_C": "publish the current result as SM-parity/admitted-external replay boundary, explicitly separate from true no-knob closure",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedNoKnobValueDerivationPostPiOrMinimalUniversalParameterPolicy",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "final_no_knob_value_derivation_recheck": rel(FINAL_RECHECK),
            "post_pi_external_replay_boundary": rel(EXTERNAL_BOUNDARY),
            "minimal_universal_parameter_policy_matrix": rel(POLICY_MATRIX),
            "rtheta_readiness_final_frontier": rel(READINESS),
            "final_cutset_after_no_knob_recheck": rel(CUTSET),
        },
        "theorem": {
            "name": "PostPiNoKnobBoundaryAndMinimalPolicyTheorem",
            "proved": True,
            "statement": (
                "At the post-Pi frontier, MTT has an accepted admitted-external replay boundary and Rtheta "
                "readiness 8/9, but the remaining no-knob gate cannot be closed by external rows, diagnostic "
                "coefficients, or an unselected universal parameter. Full closure now requires either selected "
                "internal Rtheta value emission from the same MTT source branch or a candidate-specific universal "
                "source-anchor theorem declared before empirical replay."
            ),
        },
        "what_closes_now": cutset["closed_now"],
        "what_remains_open": cutset["still_open"],
        "closure_decision": {
            "Rtheta_readiness_present_count": prev_readiness["present_count"],
            "Rtheta_readiness_requirement_count": prev_readiness["requirement_count"],
            "post_pi_external_replay_ready": external_replay_ready,
            "SM_parity_external_replay_boundary_declared": True,
            "no_knob_value_derivation_closed": False,
            "minimal_universal_parameter_selection_closed": False,
            "selected_universal_parameter_count": universal_policy["selected_parameter_count_now"],
            "selected_threshold_response_functional_instantiated": False,
            "selected_internal_value_emission_count": 0,
            "accepted_coefficient_value_count": rtheta_coefficients["accepted_coefficient_row_count"],
            "accepted_lambda_H_value": False,
            "Yukawa_mass_mixing_value_closure": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_NoKnobValueDerivationPostPi_or_MinimalUniversalParameterPolicy_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "Rtheta_readiness_present_count": prev_readiness["present_count"],
        "Rtheta_readiness_requirement_count": prev_readiness["requirement_count"],
        "post_pi_external_replay_ready": external_replay_ready,
        "SM_parity_external_replay_boundary_declared": True,
        "no_knob_value_derivation_closed": False,
        "minimal_universal_parameter_selection_closed": False,
        "selected_universal_parameter_count": universal_policy["selected_parameter_count_now"],
        "selected_threshold_response_functional_instantiated": False,
        "selected_internal_value_emission_count": 0,
        "accepted_coefficient_value_count": rtheta_coefficients["accepted_coefficient_row_count"],
        "accepted_lambda_H_value": False,
        "Yukawa_mass_mixing_value_closure": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected NoKnobValueDerivationPostPi or MinimalUniversalParameterPolicy v1

Status: `{STATUS}`.

This closes the final-frontier classification after the post-Pi diagonal
theorem.  It does not close full no-knob SM derivation.

```text
Rtheta readiness                       : {prev_readiness["present_count"]}/{prev_readiness["requirement_count"]}
post-Pi external replay ready          : {str(external_replay_ready).lower()}
selected internal no-knob rows         : false
selected universal parameters          : {universal_policy["selected_parameter_count_now"]}
minimal universal parameter selected   : false
full no-knob closure                   : false
true SM equivalence                    : false
```

The exact remaining fork is:

1. derive the selected internal `Rtheta` coefficient/value rows from the same
   MTT branch that produced the basis map, or
2. prove a source-selected universal parameter theorem and propagate that
   single source anchor globally without per-observable fitting.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
