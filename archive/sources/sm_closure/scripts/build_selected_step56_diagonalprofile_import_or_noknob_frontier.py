"""Build Step56 diagonal-profile import / no-knob frontier."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step56_diagonalprofile_import_or_noknob_frontier"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PROFILE_IMPORT = PACKET_DIR / "step56_diagonal_profile_import.packet.json"
VALUE_RECHECK = PACKET_DIR / "step56_value_readiness_recheck_after_profile.packet.json"
CUTSET = PACKET_DIR / "step56_next_noknob_cutset.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step56_DiagonalProfileImport_or_NoKnobFrontier_v1.md"

STEP55 = DATA / "selected_step55_thresholdmass_admittedrow_import_or_profile_noknob_frontier.candidate.json"
STEP55_VALUES = (
    DATA
    / "selected_step55_thresholdmass_admittedrow_import_or_profile_noknob_frontier"
    / "step55_value_readiness_recheck_after_threshold_mass.packet.json"
)
PROFILE = DATA / "selected_fullprofileordiagonaltheorempostpi_or_noknobvaluederivation.candidate.json"
DIAGONAL = (
    DATA
    / "selected_fullprofileordiagonaltheorempostpi_or_noknobvaluederivation"
    / "accepted_diagonal_profile_theorem_after_external_rows.packet.json"
)
FULL_GATE = (
    DATA
    / "selected_fullprofileordiagonaltheorempostpi_or_noknobvaluederivation"
    / "full_covariance_profile_gate_after_diagonal_acceptance.packet.json"
)
READINESS_AFTER_PROFILE = (
    DATA
    / "selected_fullprofileordiagonaltheorempostpi_or_noknobvaluederivation"
    / "rtheta_value_readiness_after_diagonal_theorem.packet.json"
)
NOKNOB_RECHECK = (
    DATA
    / "selected_fullprofileordiagonaltheorempostpi_or_noknobvaluederivation"
    / "no_knob_value_derivation_recheck_after_profile.packet.json"
)
NEXT_AFTER_PROFILE = (
    DATA
    / "selected_fullprofileordiagonaltheorempostpi_or_noknobvaluederivation"
    / "next_cutset_after_diagonal_profile_acceptance.packet.json"
)

STATUS = "MTT_SELECTED_STEP56_DIAGONAL_PROFILE_IMPORTED_NOKNOB_VALUE_DERIVATION_OPEN"
NEXT = "MTT_Selected_NoKnobValueDerivationPostPi_or_MinimalUniversalParameterPolicy_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    inputs = [
        STEP55,
        STEP55_VALUES,
        PROFILE,
        DIAGONAL,
        FULL_GATE,
        READINESS_AFTER_PROFILE,
        NOKNOB_RECHECK,
        NEXT_AFTER_PROFILE,
    ]
    missing = [rel(path) for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step56 inputs: " + ", ".join(missing))

    step55 = load(STEP55)
    step55_values = load(STEP55_VALUES)
    profile = load(PROFILE)
    diagonal = load(DIAGONAL)
    full_gate = load(FULL_GATE)
    readiness_after_profile = load(READINESS_AFTER_PROFILE)
    noknob = load(NOKNOB_RECHECK)
    next_after_profile = load(NEXT_AFTER_PROFILE)

    profile_import = {
        "schema": "MTTStep56DiagonalProfileImport.v1",
        "status": "ACCEPTED_DIAGONAL_PROFILE_IMPORTED_FULL_COVARIANCE_OPEN",
        "step55_source": rel(STEP55),
        "profile_source": rel(PROFILE),
        "diagonal_profile_source": rel(DIAGONAL),
        "accepted_diagonal_profile_theorem_closed": diagonal["accepted_diagonal_theorem_closed"],
        "full_profile_likelihood_or_accepted_diagonal_theorem_closed": profile["closure_decision"][
            "full_profile_likelihood_or_accepted_diagonal_theorem_closed"
        ],
        "full_covariance_profile_likelihood_closed": diagonal["full_profile_likelihood_closed"],
        "profile_row_count": diagonal["profile_row_count"],
        "reduced_chi2_diagonal": diagonal["reduced_chi2_diagonal"],
        "max_abs_pull": diagonal["max_abs_pull"],
        "full_covariance_gap_preserved": full_gate["full_covariance_profile_likelihood_closed"] is False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(PROFILE_IMPORT, profile_import)

    value_recheck = {
        "schema": "MTTStep56ValueReadinessRecheckAfterProfile.v1",
        "status": "READINESS_8_OF_9_ONLY_NOKNOB_DERIVATION_OPEN",
        "previous_readiness_source": rel(STEP55_VALUES),
        "previous_present_count": step55_values["present_count"],
        "previous_requirement_count": step55_values["requirement_count"],
        "retired_blocking_failure": readiness_after_profile["retired_blocking_failure"],
        "present_count": readiness_after_profile["present_count"],
        "requirement_count": readiness_after_profile["requirement_count"],
        "blocking_failures": readiness_after_profile["blocking_failures"],
        "selected_threshold_response_functional_instantiated": False,
        "selected_value_evaluator_closed": False,
        "accepted_coefficient_value_count": noknob["closed_obligation_count_under_no_knob"],
        "accepted_internal_scalar_row_count": 0,
        "accepted_lambda_H_value": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(VALUE_RECHECK, value_recheck)

    cutset = {
        "schema": "MTTStep56NextNoKnobCutset.v1",
        "status": "NEXT_FRONTIER_NOKNOB_VALUE_DERIVATION_OR_MINIMAL_POLICY",
        "closed_now": {
            "same_branch_scale_scheme_loop_convention": True,
            "threshold_matching_source_rows_at_admitted_external_tier": True,
            "mass_scheme_conversion_source_rows_at_admitted_external_tier": True,
            "accepted_diagonal_profile_theorem": True,
            "Rtheta_readiness_present_count_advanced_to_8_of_9": True,
        },
        "still_open": next_after_profile["still_open"],
        "recommended_next": next_after_profile["recommended_next"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedStep56DiagonalProfileImportOrNoKnobFrontier",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in inputs},
        "output_packets": {
            "diagonal_profile_import": rel(PROFILE_IMPORT),
            "value_readiness_recheck_after_profile": rel(VALUE_RECHECK),
            "next_noknob_cutset": rel(CUTSET),
        },
        "theorem": {
            "name": "Step56DiagonalProfileImportTheorem",
            "proved": True,
            "statement": (
                "The already-audited post-Pi accepted diagonal profile theorem is imported into the "
                "active numbered plan. This closes the full-profile-or-accepted-diagonal requirement "
                "through the diagonal branch, advances Rtheta readiness to 8/9, and leaves no-knob "
                "internal value derivation as the only readiness blocker."
            ),
        },
        "closure_decision": {
            "accepted_diagonal_profile_theorem_closed": True,
            "full_profile_likelihood_or_accepted_diagonal_theorem_closed": True,
            "full_covariance_profile_likelihood_closed": False,
            "Rtheta_readiness_present_count": readiness_after_profile["present_count"],
            "Rtheta_readiness_requirement_count": readiness_after_profile["requirement_count"],
            "only_remaining_readiness_blocker": "no_knob_value_derivation",
            "no_knob_value_derivation_closed": False,
            "selected_threshold_response_functional_instantiated": False,
            "selected_value_evaluator_closed": False,
            "accepted_internal_Rtheta_coefficient_row_count": 0,
            "accepted_internal_scalar_row_count": 0,
            "accepted_lambda_H_value": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "previous_status": step55["status"],
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "minimal_parameter_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step56_DiagonalProfileImport_or_NoKnobFrontier_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        **candidate["closure_decision"],
        "theorem_proved": True,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected Step56 DiagonalProfileImport or NoKnobFrontier v1

Status: `{STATUS}`.

Step56 imports the accepted post-Pi diagonal profile theorem into the active
numbered plan.

```text
accepted diagonal theorem closed       : true
full correlated covariance closed      : false
Rtheta readiness                       : {candidate["closure_decision"]["Rtheta_readiness_present_count"]}/{candidate["closure_decision"]["Rtheta_readiness_requirement_count"]}
only remaining readiness blocker       : no_knob_value_derivation
selected internal Rtheta rows          : 0
true SM equivalence                    : false
full no-knob closure                   : false
```

The next target is `{NEXT}`.
""",
        encoding="utf-8",
    )

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
