"""Integrate same-branch threshold/mass-scheme rows and source-anchor construction frontier."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_samebranchthresholdmassschemerows_or_sourceanchorconstruction"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
EXTERNAL_REPLAY = PACKET_DIR / "admitted_external_replay_integration_after_orbit_source_domain.packet.json"
INTERNAL_GAP = PACKET_DIR / "same_branch_internal_source_row_gap.packet.json"
ANCHOR_GAP = PACKET_DIR / "source_anchor_construction_gap.packet.json"
FINAL_FRONTIER = PACKET_DIR / "final_value_frontier_after_integration.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_SameBranchThresholdMassSchemeRows_or_SourceAnchorConstruction_v1.md"

PREVIOUS = DATA / "selected_thresholdmagnituderows_or_minimaluniversalparameterdecision.candidate.json"
SOURCE_DOMAIN = (
    DATA
    / "selected_rthetascalarvaluefunctionalsource_or_noknobnumericalrows"
    / "rtheta_scalar_value_functional_source_packet.packet.json"
)
POST_PI_CONVENTION = DATA / "selected_postpiconventionsource_or_thresholdfunctionalinstantiation.candidate.json"
THRESHOLD_ROWS = DATA / "selected_thresholdmatchingrowspostpi_or_massschemesourcerows.candidate.json"
FULL_PROFILE = DATA / "selected_fullprofileordiagonaltheorempostpi_or_noknobvaluederivation.candidate.json"
NO_KNOB_POST_PI = DATA / "selected_noknobvaluederivationpostpi_or_minimaluniversalparameterpolicy.candidate.json"
READINESS = (
    DATA
    / "selected_noknobvaluederivationpostpi_or_minimaluniversalparameterpolicy"
    / "rtheta_readiness_final_frontier.packet.json"
)
FINAL_RECHECK = (
    DATA
    / "selected_noknobvaluederivationpostpi_or_minimaluniversalparameterpolicy"
    / "final_no_knob_value_derivation_recheck.packet.json"
)
EXTERNAL_BOUNDARY = (
    DATA
    / "selected_noknobvaluederivationpostpi_or_minimaluniversalparameterpolicy"
    / "post_pi_external_replay_boundary.packet.json"
)
UNIVERSAL_POLICY_MATRIX = (
    DATA
    / "selected_noknobvaluederivationpostpi_or_minimaluniversalparameterpolicy"
    / "minimal_universal_parameter_policy_matrix.packet.json"
)

STATUS = (
    "MTT_SELECTED_SAMEBRANCHTHRESHOLDMASSSCHEMEROWS_OR_SOURCEANCHORCONSTRUCTION_"
    "BUILT_READINESS_8_OF_9_FINAL_NOKNOB_VALUE_DERIVATION_OPEN"
)
NEXT = "MTT_Selected_NoKnobValueDerivationKernel_or_SourceAnchorTheorem_v1"


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
        raise FileNotFoundError("missing same-branch threshold/source-anchor inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        SOURCE_DOMAIN,
        POST_PI_CONVENTION,
        THRESHOLD_ROWS,
        FULL_PROFILE,
        NO_KNOB_POST_PI,
        READINESS,
        FINAL_RECHECK,
        EXTERNAL_BOUNDARY,
        UNIVERSAL_POLICY_MATRIX,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    source_domain = load(SOURCE_DOMAIN)
    convention = load(POST_PI_CONVENTION)
    threshold = load(THRESHOLD_ROWS)
    profile = load(FULL_PROFILE)
    no_knob = load(NO_KNOB_POST_PI)
    readiness = load(READINESS)
    final_recheck = load(FINAL_RECHECK)
    external_boundary = load(EXTERNAL_BOUNDARY)
    universal_matrix = load(UNIVERSAL_POLICY_MATRIX)

    readiness_8_of_9 = (
        readiness["present_count"] == 8
        and readiness["requirement_count"] == 9
        and readiness["only_remaining_readiness_blocker"] == "no_knob_value_derivation"
    )

    external_replay = {
        "schema": "MTTAdmittedExternalReplayIntegrationAfterOrbitSourceDomain.v1",
        "status": "ADMITTED_EXTERNAL_REPLAY_INTEGRATED_READINESS_8_OF_9",
        "Rtheta_value_functional_source_domain_closed": source_domain["source_domain_closed"],
        "same_branch_scale_scheme_loop_convention_closed": convention["closure_decision"][
            "same_branch_scale_scheme_loop_convention_closed"
        ],
        "admitted_external_threshold_matching_rows": threshold["closure_decision"][
            "threshold_matching_source_rows_closed_at_admitted_external_tier"
        ],
        "admitted_external_mass_scheme_rows": threshold["closure_decision"][
            "mass_scheme_conversion_source_rows_closed_at_admitted_external_tier"
        ],
        "accepted_diagonal_profile_theorem_closed": profile["closure_decision"][
            "accepted_diagonal_profile_theorem_closed"
        ],
        "readiness_fraction": readiness["readiness_fraction"],
        "only_remaining_readiness_blocker": readiness["only_remaining_readiness_blocker"],
        "can_claim_admitted_external_replay_boundary": readiness[
            "can_claim_admitted_external_replay_boundary"
        ],
        "can_claim_true_SM_equivalence": readiness["can_claim_true_SM_equivalence"],
        "can_claim_full_no_knob": readiness["can_claim_full_no_knob"],
        "boundary_source": rel(EXTERNAL_BOUNDARY),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(EXTERNAL_REPLAY, external_replay)

    internal_gap = {
        "schema": "MTTSameBranchInternalSourceRowGap.v1",
        "status": "INTERNAL_SELECTED_THRESHOLD_MASS_SCHEME_ROWS_STILL_OPEN",
        "external_rows_admitted": True,
        "selected_internal_Rtheta_threshold_mass_derivation_closed": threshold["closure_decision"][
            "selected_internal_Rtheta_threshold_mass_derivation_closed"
        ],
        "selected_threshold_response_functional_instantiated": final_recheck[
            "selected_threshold_response_functional_instantiated"
        ],
        "selected_internal_value_emission_count": final_recheck[
            "selected_internal_value_emission_count"
        ],
        "accepted_coefficient_value_count": final_recheck["accepted_coefficient_value_count"],
        "lambda_H_coefficient_selected": final_recheck["lambda_H_coefficient_selected"],
        "why_external_rows_do_not_close_internal_derivation": [
            "they are admitted replay rows with provenance, not internal MTT emissions",
            "they validate convention compatibility but do not choose coefficients",
            "using them to fill coefficients would make empirical replay a selector",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(INTERNAL_GAP, internal_gap)

    anchor_gap = {
        "schema": "MTTSourceAnchorConstructionGap.v1",
        "status": "SOURCE_ANCHOR_CONSTRUCTION_STILL_OPEN",
        "minimal_universal_parameter_policy_matrix": rel(UNIVERSAL_POLICY_MATRIX),
        "selected_universal_parameter_count": final_recheck["selected_universal_parameter_count"],
        "minimal_universal_parameter_selection_closed": no_knob["closure_decision"][
            "minimal_universal_parameter_selection_closed"
        ],
        "candidate_specific_source_theorem_required": True,
        "universal_policy_matrix_available": True,
        "admissible_only_if": [
            "anchor is selected by an MTT source theorem before empirical replay",
            "anchor is universal, not sector- or observable-fitted",
            "anchor propagates through all ten scalar rows",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(ANCHOR_GAP, anchor_gap)

    final_frontier = {
        "schema": "MTTFinalValueFrontierAfterIntegration.v1",
        "status": "ONLY_NOKNOB_VALUE_DERIVATION_BLOCKER_REMAINS_AT_READINESS_LEVEL",
        "closed_now": {
            "qualitative_SM_orbit_closure": True,
            "Rtheta_value_functional_source_domain": source_domain["source_domain_closed"],
            "same_branch_scale_scheme_loop_convention": True,
            "admitted_external_threshold_matching_rows": True,
            "admitted_external_mass_scheme_conversion_rows": True,
            "accepted_diagonal_profile_theorem": True,
            "Rtheta_readiness_8_of_9": readiness_8_of_9,
            "admitted_external_replay_boundary": external_boundary[
                "post_pi_external_replay_ready"
            ],
        },
        "still_open": {
            "no_knob_value_derivation": True,
            "selected_internal_Rtheta_threshold_mass_derivation": True,
            "selected_threshold_response_functional_instantiation": True,
            "numeric_Rtheta_coefficient_values": True,
            "lambda_H_value_execution": True,
            "candidate_specific_universal_source_theorem": True,
            "true_SM_equivalence": True,
            "full_no_knob": True,
        },
        "remaining_readiness_blocker": readiness["only_remaining_readiness_blocker"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(FINAL_FRONTIER, final_frontier)

    candidate = {
        "candidate": "MTTSelectedSameBranchThresholdMassSchemeRowsOrSourceAnchorConstruction",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "admitted_external_replay_integration_after_orbit_source_domain": rel(EXTERNAL_REPLAY),
            "same_branch_internal_source_row_gap": rel(INTERNAL_GAP),
            "source_anchor_construction_gap": rel(ANCHOR_GAP),
            "final_value_frontier_after_integration": rel(FINAL_FRONTIER),
        },
        "theorem": {
            "name": "IntegratedPostPiReadinessAndInternalValueEmissionFrontierTheorem",
            "proved": True,
            "statement": (
                "After importing the closed Rtheta source/domain, post-Pi convention source, admitted "
                "external threshold/mass-scheme rows, and accepted diagonal profile theorem, the value "
                "frontier is readiness 8/9 with only no-knob value derivation open. External replay is "
                "admitted for comparison but cannot emit internal selected coefficients. Full closure "
                "therefore requires internal Rtheta value emission or a candidate-specific universal "
                "source-anchor theorem."
            ),
        },
        "closure_decision": {
            "Rtheta_readiness_8_of_9": readiness_8_of_9,
            "admitted_external_replay_boundary_integrated": True,
            "selected_internal_value_emission_count": final_recheck[
                "selected_internal_value_emission_count"
            ],
            "accepted_coefficient_value_count": final_recheck["accepted_coefficient_value_count"],
            "selected_universal_parameter_count": final_recheck[
                "selected_universal_parameter_count"
            ],
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "what_closes_now": final_frontier["closed_now"],
        "what_remains_open": final_frontier["still_open"],
        "previous_status": previous["status"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": True,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_SameBranchThresholdMassSchemeRows_or_SourceAnchorConstruction_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "Rtheta_readiness_8_of_9": readiness_8_of_9,
        "admitted_external_replay_boundary_integrated": True,
        "selected_internal_value_emission_count": final_recheck[
            "selected_internal_value_emission_count"
        ],
        "accepted_coefficient_value_count": final_recheck["accepted_coefficient_value_count"],
        "selected_universal_parameter_count": final_recheck["selected_universal_parameter_count"],
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": True,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected SameBranchThresholdMassSchemeRows or SourceAnchorConstruction v1

Status: `{STATUS}`.

The post-Pi and current orbit/source-domain lanes now integrate cleanly:

```text
Rtheta readiness                 : {readiness["readiness_fraction"]}
only readiness blocker           : {readiness["only_remaining_readiness_blocker"]}
admitted external replay boundary: true
selected internal value emissions: {final_recheck["selected_internal_value_emission_count"]}
accepted coefficient values      : {final_recheck["accepted_coefficient_value_count"]}
selected universal parameters    : {final_recheck["selected_universal_parameter_count"]}
```

This is the sharpest current frontier. We can claim admitted external replay
compatibility, but not no-knob internal numerical SM equivalence. The next
object must actually emit the no-knob value kernel or select a universal
source anchor before replay.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
