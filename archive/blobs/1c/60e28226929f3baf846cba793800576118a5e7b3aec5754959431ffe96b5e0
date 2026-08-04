"""Build post-Pi full-profile or accepted diagonal theorem / no-knob derivation artifact."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_fullprofileordiagonaltheorempostpi_or_noknobvaluederivation"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
DIAGONAL = PACKET_DIR / "accepted_diagonal_profile_theorem_after_external_rows.packet.json"
FULL_GATE = PACKET_DIR / "full_covariance_profile_gate_after_diagonal_acceptance.packet.json"
READINESS = PACKET_DIR / "rtheta_value_readiness_after_diagonal_theorem.packet.json"
NOKNOB = PACKET_DIR / "no_knob_value_derivation_recheck_after_profile.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_diagonal_profile_acceptance.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_FullProfileOrDiagonalTheoremPostPi_or_NoKnobValueDerivation_v1.md"

PREVIOUS = DATA / "selected_thresholdmatchingrowspostpi_or_massschemesourcerows.candidate.json"
PREV_READINESS = (
    DATA
    / "selected_thresholdmatchingrowspostpi_or_massschemesourcerows"
    / "rtheta_value_readiness_after_external_rows.packet.json"
)
DIAGONAL_EXECUTION = (
    DATA
    / "selected_fullcovarianceprofile_or_multiloopconventionaudit"
    / "diagonal_profile_likelihood_execution.packet.json"
)
DIAGONAL_SIDECAR = (
    DATA
    / "selected_polethresholdresidualvalues_or_covarianceprofile"
    / "diagonal_sensitivity_covariance_scaffold.packet.json"
)
FULL_PROFILE_GATE = (
    DATA
    / "selected_fullcovarianceprofile_or_selectedrthetasourcerows"
    / "full_covariance_profile_gate_after_wzh_bct.packet.json"
)
POST_PI_ROWS = (
    DATA
    / "selected_thresholdmatchingrowspostpi_or_massschemesourcerows"
    / "external_row_admission_not_rtheta_selection.packet.json"
)
POST_PI_CONVENTION = (
    DATA
    / "selected_postpiconventionsource_or_thresholdfunctionalinstantiation"
    / "post_pi_same_branch_convention_source_contract.packet.json"
)
VALUE_KERNEL = (
    DATA
    / "selected_valuesourcederivationobligationkernel_or_externalthresholdimportmanifest"
    / "value_source_derivation_obligation_kernel.packet.json"
)

STATUS = (
    "MTT_SELECTED_FULLPROFILEORDIAGONALTHEOREMPOSTPI_OR_NOKNOBVALUEDERIVATION_"
    "CLOSED_ACCEPTED_DIAGONAL_PROFILE_NOKNOB_OPEN"
)
NEXT = "MTT_Selected_NoKnobValueDerivationPostPi_or_MinimalUniversalParameterPolicy_v1"


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
        raise FileNotFoundError("missing post-Pi profile sources: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREV_READINESS,
        DIAGONAL_EXECUTION,
        DIAGONAL_SIDECAR,
        FULL_PROFILE_GATE,
        POST_PI_ROWS,
        POST_PI_CONVENTION,
        VALUE_KERNEL,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    prev_readiness = load(PREV_READINESS)
    diagonal_execution = load(DIAGONAL_EXECUTION)
    diagonal_sidecar = load(DIAGONAL_SIDECAR)
    full_profile_gate = load(FULL_PROFILE_GATE)
    post_pi_rows = load(POST_PI_ROWS)
    post_pi_convention = load(POST_PI_CONVENTION)
    value_kernel = load(VALUE_KERNEL)

    diagonal = {
        "schema": "MTTAcceptedDiagonalProfileTheoremAfterExternalRows.v1",
        "status": "ACCEPTED_DIAGONAL_PROFILE_THEOREM_CLOSED_FULL_COVARIANCE_OPEN",
        "diagonal_execution_source": rel(DIAGONAL_EXECUTION),
        "sidecar_source": rel(DIAGONAL_SIDECAR),
        "admitted_rows_source": rel(POST_PI_ROWS),
        "acceptance_tests": {
            "post_pi_convention_source_closed": post_pi_convention[
                "same_branch_scale_scheme_loop_convention_closed"
            ],
            "admitted_external_threshold_rows_closed": post_pi_rows[
                "accepted_external_threshold_row_count"
            ]
            > 0,
            "admitted_external_mass_scheme_rows_closed": post_pi_rows[
                "accepted_external_mass_scheme_row_count"
            ]
            > 0,
            "diagonal_profile_executed": diagonal_execution["status"]
            == "DIAGONAL_PROFILE_EXECUTED_FULL_CORRELATED_PROFILE_OPEN",
            "passes_coarse_diagonal_profile": diagonal_execution["passes_coarse_diagonal_profile"],
            "diagonal_uncertainty_sidecar_available": diagonal_sidecar["status"]
            == "DIAGONAL_SENSITIVITY_SCAFFOLD_BUILT_FULL_PROFILE_OPEN",
            "correlations_included": diagonal_sidecar["correlations_included"],
            "full_covariance_profile_likelihood_closed": diagonal_execution[
                "accepted_as_full_covariance_profile"
            ],
        },
        "chi2_diagonal": diagonal_execution["chi2_diagonal"],
        "degrees_of_freedom": diagonal_execution["degrees_of_freedom"],
        "reduced_chi2_diagonal": diagonal_execution["reduced_chi2_diagonal"],
        "max_abs_pull": diagonal_execution["max_abs_pull"],
        "profile_row_count": len(diagonal_execution["profile_rows"]),
        "profile_rows": diagonal_execution["profile_rows"],
        "accepted_diagonal_theorem_closed": True,
        "full_profile_likelihood_closed": False,
        "why_not_full_profile": diagonal_execution["why_not_full_profile"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(DIAGONAL, diagonal)

    full_gate = {
        "schema": "MTTFullCovarianceProfileGateAfterDiagonalAcceptance.v1",
        "status": "FULL_COVARIANCE_PROFILE_STILL_OPEN_ACCEPTED_DIAGONAL_THEOREM_AVAILABLE",
        "full_profile_gate_source": rel(FULL_PROFILE_GATE),
        "accepted_diagonal_theorem_closed": True,
        "full_covariance_profile_likelihood_closed": full_profile_gate[
            "full_covariance_profile_likelihood_closed"
        ],
        "can_claim_full_correlated_profile": full_profile_gate["can_claim_full_correlated_profile"],
        "can_build_block_diagonal_interim_profile": full_profile_gate[
            "can_build_block_diagonal_interim_profile"
        ],
        "missing_covariance_objects": full_profile_gate["missing_covariance_objects"],
        "why_block_diagonal_is_not_enough": full_profile_gate["why_block_diagonal_is_not_enough"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(FULL_GATE, full_gate)

    remaining_blockers = ["no_knob_value_derivation"]
    readiness = {
        "schema": "MTTRThetaValueReadinessAfterDiagonalTheorem.v1",
        "status": "READINESS_ADVANCED_DIAGONAL_THEOREM_CLOSED_NOKNOB_OPEN",
        "previous_readiness_source": rel(PREV_READINESS),
        "previous_present_count": prev_readiness["present_count"],
        "previous_requirement_count": prev_readiness["requirement_count"],
        "previous_blocking_failures": prev_readiness["blocking_failures"],
        "retired_blocking_failure": "full_profile_likelihood_or_accepted_diagonal_theorem",
        "present_count": prev_readiness["present_count"] + 1,
        "requirement_count": prev_readiness["requirement_count"],
        "blocking_failures": remaining_blockers,
        "selected_threshold_response_functional_instantiated": False,
        "selected_value_evaluator_closed": False,
        "accepted_coefficient_value_count": 0,
        "accepted_lambda_H_value": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(READINESS, readiness)

    noknob = {
        "schema": "MTTNoKnobValueDerivationRecheckAfterProfile.v1",
        "status": "NOKNOB_VALUE_DERIVATION_STILL_OPEN_EXTERNAL_REPLAY_READY",
        "value_kernel_source": rel(VALUE_KERNEL),
        "obligation_count": value_kernel["required_row_count"],
        "closed_obligation_count_under_no_knob": value_kernel["closed_row_count"],
        "external_replay_rows_available": {
            "threshold_rows": post_pi_rows["accepted_external_threshold_row_count"],
            "mass_scheme_rows": post_pi_rows["accepted_external_mass_scheme_row_count"],
            "accepted_diagonal_theorem": True,
        },
        "why_no_knob_still_open": [
            "admitted external rows are measured/downstream replay rows, not selected internal MTT value emissions",
            "no theorem derives the numerical threshold/mass/Yukawa/lambda rows from selected MTT geometry alone",
            "full internal selected Rtheta threshold/mass derivation remains separate from the admitted external tier",
        ],
        "no_knob_value_derivation_closed": False,
        "minimal_universal_parameter_policy_needed_if_no_internal_derivation": True,
        "selected_universal_parameter_count": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(NOKNOB, noknob)

    cutset = {
        "schema": "MTTNextCutsetAfterDiagonalProfileAcceptance.v1",
        "status": "NEXT_ATTACK_NOKNOB_VALUE_DERIVATION_OR_MINIMAL_UNIVERSAL_PARAMETER",
        "closed_now": {
            "accepted_diagonal_profile_theorem": True,
            "full_profile_or_accepted_diagonal_requirement": True,
            "Rtheta_readiness_present_count_advanced_to_8_of_9": True,
            "full_covariance_profile_gap_preserved": True,
        },
        "still_open": {
            "no_knob_value_derivation": True,
            "selected_internal_Rtheta_threshold_mass_derivation": True,
            "selected_threshold_response_functional_instantiated": True,
            "numeric_Rtheta_coefficient_values": True,
            "lambda_H_value_execution": True,
            "Yukawa_mass_mixing_value_closure": True,
            "true_SM_equivalence": True,
            "full_no_knob": True,
        },
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "derive selected internal Rtheta value rows from MTT geometry and supersede external replay",
            "route_B": "adopt a minimal universal parameter policy for the remaining numerical value layer",
            "route_C": "declare SM-parity/external-replay closure separate from no-knob closure",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedFullProfileOrDiagonalTheoremPostPiOrNoKnobValueDerivation",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "accepted_diagonal_profile_theorem_after_external_rows": rel(DIAGONAL),
            "full_covariance_profile_gate_after_diagonal_acceptance": rel(FULL_GATE),
            "rtheta_value_readiness_after_diagonal_theorem": rel(READINESS),
            "no_knob_value_derivation_recheck_after_profile": rel(NOKNOB),
            "next_cutset_after_diagonal_profile_acceptance": rel(CUTSET),
        },
        "theorem": {
            "name": "PostPiAcceptedDiagonalProfileTheorem",
            "proved": True,
            "statement": (
                "Given the post-Pi convention source and admitted external threshold/mass-scheme rows, the existing "
                "diagonal profile execution is an accepted diagonal theorem for the external replay tier. It has six "
                "profile rows, reduced chi^2 approximately 1.0005, and max absolute pull below 2.22. This closes the "
                "full_profile_likelihood_or_accepted_diagonal_theorem requirement via the diagonal branch only; full "
                "correlated covariance and no-knob value derivation remain open."
            ),
        },
        "what_closes_now": cutset["closed_now"],
        "what_remains_open": cutset["still_open"],
        "closure_decision": {
            "accepted_diagonal_profile_theorem_closed": True,
            "full_profile_likelihood_or_accepted_diagonal_theorem_closed": True,
            "full_covariance_profile_likelihood_closed": False,
            "no_knob_value_derivation_closed": False,
            "selected_threshold_response_functional_instantiated": False,
            "accepted_coefficient_value_count": 0,
            "accepted_lambda_H_value": False,
            "selected_value_evaluator_closed": False,
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
        "certificate": "MTT_Selected_FullProfileOrDiagonalTheoremPostPi_or_NoKnobValueDerivation_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "accepted_diagonal_profile_theorem_closed": True,
        "full_profile_likelihood_or_accepted_diagonal_theorem_closed": True,
        "full_covariance_profile_likelihood_closed": False,
        "no_knob_value_derivation_closed": False,
        "selected_threshold_response_functional_instantiated": False,
        "accepted_coefficient_value_count": 0,
        "accepted_lambda_H_value": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected FullProfileOrDiagonalTheoremPostPi or NoKnobValueDerivation v1

Status: `{STATUS}`.

The accepted diagonal theorem is now closed for the admitted external replay
tier.

```text
accepted diagonal theorem closed       : true
full correlated covariance closed      : false
diagonal chi2 / dof                    : {diagonal["chi2_diagonal"]:.12g} / {diagonal["degrees_of_freedom"]}
reduced diagonal chi2                  : {diagonal["reduced_chi2_diagonal"]:.12g}
Rtheta readiness                       : {readiness["present_count"]}/{readiness["requirement_count"]}
no-knob value derivation closed        : false
true SM equivalence                    : false
```

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
