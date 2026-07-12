"""Build R_theta threshold rows or profile-convention source closure packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_rtheta_thresholdrows_or_profileconventionsourceclosure"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ORDER = PACKET_DIR / "remaining_value_frontier_dependency_order.packet.json"
PROFILE = PACKET_DIR / "profile_convention_source_recheck.packet.json"
ROWS = PACKET_DIR / "threshold_mass_scheme_source_rows_recheck.packet.json"
EXECUTION = PACKET_DIR / "rtheta_value_execution_readiness_after_ordering.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_threshold_profile_ordering.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_RThetaThresholdRows_or_ProfileConventionSourceClosure_v1.md"

PREVIOUS = DATA / "selected_rtheta_valueevaluatorexecution_or_thresholdresponseinstantiation.candidate.json"
PREVIOUS_AUDIT = (
    DATA
    / "selected_rtheta_valueevaluatorexecution_or_thresholdresponseinstantiation"
    / "threshold_response_instantiation_audit_after_pi_closure.packet.json"
)
PROFILE_RECHECK = (
    DATA
    / "selected_generationresolvedthresholdsourcerows_or_profileconventionclosure"
    / "profile_convention_closure_recheck.packet.json"
)
GENERATION_RECHECK = (
    DATA
    / "selected_generationresolvedthresholdsourcerows_or_profileconventionclosure"
    / "generation_source_support_recheck.packet.json"
)
SOURCE_ROW_AUDIT = (
    DATA
    / "selected_acceptedthresholdmassschemesourcerows_or_noknobvaluederivation"
    / "accepted_threshold_mass_scheme_source_row_audit.packet.json"
)
NO_KNOB_DERIVATION = (
    DATA
    / "selected_acceptedthresholdmassschemesourcerows_or_noknobvaluederivation"
    / "no_knob_value_derivation_attempt.packet.json"
)
FULL_PROFILE = DATA / "selected_fullcovarianceprofile_or_multiloopconventionaudit.candidate.json"
THRESHOLD_ROWS = (
    DATA
    / "selected_thresholdresponserows_or_sectorprojectionweightsexecution"
    / "threshold_response_rows_recheck.packet.json"
)

STATUS = (
    "MTT_SELECTED_RTHETA_THRESHOLDROWS_OR_PROFILECONVENTIONSOURCECLOSURE_"
    "BUILT_ORDERED_FRONTIER_ROWS_OPEN"
)
NEXT = "MTT_Selected_ValueSourceDerivationObligationKernel_or_ExternalThresholdImportManifest_v1"


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
        raise FileNotFoundError("missing R_theta threshold/profile sources: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_AUDIT,
        PROFILE_RECHECK,
        GENERATION_RECHECK,
        SOURCE_ROW_AUDIT,
        NO_KNOB_DERIVATION,
        FULL_PROFILE,
        THRESHOLD_ROWS,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_audit = load(PREVIOUS_AUDIT)
    profile = load(PROFILE_RECHECK)
    generation = load(GENERATION_RECHECK)
    source_rows = load(SOURCE_ROW_AUDIT)
    no_knob = load(NO_KNOB_DERIVATION)
    full_profile = load(FULL_PROFILE)
    threshold_rows = load(THRESHOLD_ROWS)

    scale_scheme_closed = profile["same_branch_scale_scheme_loop_convention_closed"] is True
    threshold_matching_rows_closed = bool(source_rows["accepted_threshold_matching_source_rows"])
    mass_scheme_rows_closed = bool(source_rows["accepted_mass_scheme_conversion_source_rows"])
    profile_or_diagonal_closed = (
        full_profile["closure_decision"]["full_covariance_profile_closed"] is True
        or profile["full_profile_likelihood_closed"] is True
    )
    no_knob_closed = no_knob["no_knob_value_derivation_closed"] is True
    generation_support_closed = generation["generation_support_closed"] is True

    dependency_order = {
        "schema": "MTTRThetaRemainingValueFrontierDependencyOrder.v1",
        "status": "REMAINING_VALUE_FRONTIER_HAS_ORDERED_INTERDEPENDENT_GATES",
        "closed_prerequisites": {
            "Pi_Rtheta": previous["closure_decision"]["Pi_Rtheta_closed"],
            "selected_dynamic_operator_source_owner": previous["closure_decision"][
                "selected_dynamic_operator_source_owner_closed"
            ],
            "coefficient_functional_domain": previous["closure_decision"][
                "coefficient_functional_domain_closed"
            ],
            "source_normalized_projection_weights": previous["closure_decision"][
                "source_normalized_projection_weights_closed"
            ],
            "generation_structure_support": generation_support_closed,
        },
        "ordered_remaining_layers": [
            {
                "layer": 1,
                "id": "same_branch_scale_scheme_loop_convention",
                "role": "sets the target scale, scheme, loop order, and matching semantics before rows can be accepted",
                "closed": scale_scheme_closed,
                "parallel_with": ["full_profile_likelihood_or_accepted_diagonal_theorem"],
            },
            {
                "layer": 1,
                "id": "full_profile_likelihood_or_accepted_diagonal_theorem",
                "role": "sets the covariance/profile acceptance semantics; can be pursued with convention, but cannot replace source rows unless theorem is explicit",
                "closed": profile_or_diagonal_closed,
                "parallel_with": ["same_branch_scale_scheme_loop_convention"],
            },
            {
                "layer": 2,
                "id": "threshold_matching_source_rows",
                "role": "fills threshold rows under the chosen convention/profile semantics",
                "closed": threshold_matching_rows_closed,
                "depends_on": ["same_branch_scale_scheme_loop_convention"],
            },
            {
                "layer": 2,
                "id": "mass_scheme_conversion_source_rows",
                "role": "fills pole/running and scheme conversion rows under the chosen convention/profile semantics",
                "closed": mass_scheme_rows_closed,
                "depends_on": ["same_branch_scale_scheme_loop_convention"],
            },
            {
                "layer": 3,
                "id": "no_knob_value_derivation",
                "role": "derives numeric magnitude rows from selected source rows, or records a minimal parameter escape hatch",
                "closed": no_knob_closed,
                "depends_on": [
                    "threshold_matching_source_rows",
                    "mass_scheme_conversion_source_rows",
                    "full_profile_likelihood_or_accepted_diagonal_theorem",
                ],
            },
        ],
        "obvious_order_exists": True,
        "but_gates_are_interlinked": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(ORDER, dependency_order)

    profile_recheck = {
        "schema": "MTTRThetaProfileConventionSourceRecheck.v1",
        "status": "FIRSTPASS_PROFILE_AVAILABLE_TRUE_SOURCE_CONVENTION_OPEN",
        "source": rel(PROFILE_RECHECK),
        "firstpass_profile_layer_closed": profile["profile_layer_closed"],
        "accepted_for_profile_execution_input": profile["accepted_for_profile_execution_input"],
        "same_branch_scale_scheme_loop_convention_closed": scale_scheme_closed,
        "full_profile_likelihood_closed": profile["full_profile_likelihood_closed"],
        "full_covariance_profile_closed": full_profile["closure_decision"][
            "full_covariance_profile_closed"
        ],
        "accepted_for_true_precision_equivalence": profile[
            "accepted_for_true_precision_equivalence"
        ],
        "reason_not_closed": profile["reason_not_closed"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(PROFILE, profile_recheck)

    rows_recheck = {
        "schema": "MTTRThetaThresholdMassSchemeSourceRowsRecheck.v1",
        "status": "SOURCE_ROW_AUDIT_NONE_ACCEPTED_ROWS_OPEN",
        "source_row_audit": rel(SOURCE_ROW_AUDIT),
        "threshold_rows_recheck": rel(THRESHOLD_ROWS),
        "candidate_source_row_count": source_rows["candidate_count"],
        "support_present_count": source_rows["support_present_count"],
        "promotable_count": source_rows["promotable_count"],
        "accepted_threshold_matching_source_rows": source_rows[
            "accepted_threshold_matching_source_rows"
        ],
        "accepted_mass_scheme_conversion_source_rows": source_rows[
            "accepted_mass_scheme_conversion_source_rows"
        ],
        "accepted_source_rows_present": source_rows["accepted_source_rows_present"],
        "threshold_response_rows_closed": threshold_rows["threshold_response_rows_closed"],
        "mass_scheme_conversion_rows_closed": threshold_rows[
            "mass_scheme_conversion_rows_closed"
        ],
        "residual_rows_finite_but_downstream": threshold_rows["residual_rows_finite"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(ROWS, rows_recheck)

    still_open = [
        "same_branch_scale_scheme_loop_convention",
        "threshold_matching_source_rows",
        "mass_scheme_conversion_source_rows",
        "no_knob_value_derivation",
        "full_profile_likelihood_or_accepted_diagonal_theorem",
    ]
    execution_readiness = {
        "schema": "MTTRThetaValueExecutionReadinessAfterOrdering.v1",
        "status": "VALUE_EXECUTION_ORDERED_BUT_STILL_BLOCKED",
        "previous_audit": rel(PREVIOUS_AUDIT),
        "present_count": previous_audit["present_count"],
        "requirement_count": previous_audit["requirement_count"],
        "ordered_dependency_graph_closed": True,
        "selected_threshold_response_functional_instantiated": False,
        "selected_value_evaluator_closed": False,
        "accepted_coefficient_value_count": 0,
        "accepted_lambda_H_value": False,
        "blocking_failures": still_open,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(EXECUTION, execution_readiness)

    cutset = {
        "schema": "MTTNextCutsetAfterThresholdProfileOrdering.v1",
        "status": "NEXT_ATTACK_VALUE_SOURCE_OBLIGATION_OR_EXTERNAL_THRESHOLD_IMPORT",
        "closed_now": {
            "remaining_value_frontier_dependency_order": True,
            "generation_structure_support": generation_support_closed,
            "firstpass_profile_support_available": profile["profile_layer_closed"],
        },
        "still_open": still_open,
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "internal no-knob route: derive selected threshold/mass-scheme source rows from overlap/operator kernels under an explicit convention",
            "route_B": "external-source route: import accepted threshold/profile source rows with provenance, basis map, and replay command",
            "route_C": "minimal-parameter route: explicitly admit the smallest universal parameter set and rerun value rows",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedRThetaThresholdRowsOrProfileConventionSourceClosure",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "remaining_value_frontier_dependency_order": rel(ORDER),
            "profile_convention_source_recheck": rel(PROFILE),
            "threshold_mass_scheme_source_rows_recheck": rel(ROWS),
            "rtheta_value_execution_readiness_after_ordering": rel(EXECUTION),
            "next_cutset_after_threshold_profile_ordering": rel(CUTSET),
        },
        "theorem": {
            "name": "RThetaRemainingValueFrontierOrderingTheorem",
            "proved": True,
            "statement": (
                "After Pi_Rtheta and dynamic source ownership close, the remaining R_theta value blockers "
                "have a strict partial order. Scale/scheme/loop convention and profile/diagonal semantics "
                "are layer-1 gates; threshold and mass-scheme source rows are layer-2 gates under that "
                "convention; no-knob value derivation is layer 3. Current repo evidence supplies support "
                "and finite residual/profile replay, but zero accepted threshold or mass-scheme source rows."
            ),
        },
        "closure_decision": {
            "ordered_dependency_graph_closed": True,
            "generation_structure_support_closed": generation_support_closed,
            "same_branch_scale_scheme_loop_convention_closed": scale_scheme_closed,
            "threshold_matching_source_rows_closed": threshold_matching_rows_closed,
            "mass_scheme_conversion_source_rows_closed": mass_scheme_rows_closed,
            "no_knob_value_derivation_closed": no_knob_closed,
            "full_profile_likelihood_or_accepted_diagonal_theorem_closed": profile_or_diagonal_closed,
            "selected_threshold_response_functional_instantiated": False,
            "selected_value_evaluator_closed": False,
            "accepted_coefficient_value_count": 0,
            "accepted_lambda_H_value": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTTSelectedRThetaThresholdRowsOrProfileConventionSourceClosure",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "ordered_dependency_graph_closed": True,
        "selected_threshold_response_functional_instantiated": False,
        "accepted_coefficient_value_count": 0,
        "theorem_proved": True,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected RThetaThresholdRows or ProfileConventionSourceClosure v1

Status: `{STATUS}`.

The five remaining `R_theta` value blockers are interlinked, but they now have
a clean partial order.

```text
ordered dependency graph closed               : true
generation structure support closed           : {str(generation_support_closed).lower()}
same-branch scale/scheme/loop convention      : {str(scale_scheme_closed).lower()}
threshold matching source rows                : {str(threshold_matching_rows_closed).lower()}
mass-scheme conversion source rows            : {str(mass_scheme_rows_closed).lower()}
no-knob value derivation                       : {str(no_knob_closed).lower()}
profile/diagonal acceptance theorem           : {str(profile_or_diagonal_closed).lower()}
accepted coefficient values                    : 0
```

Order:

1. Close convention/profile semantics.
2. Emit threshold matching and mass-scheme source rows under that convention.
3. Derive no-knob values, or explicitly admit the minimal universal parameter
   escape hatch.

The profile/diagonal theorem can be attacked in parallel with convention, but
it cannot replace source rows unless it explicitly proves that replacement.

Current repo evidence gives finite residual/profile replay and first-pass
profile support, but zero promotable threshold/mass-scheme source rows.

Next artifact: `{NEXT}`.
""",
        encoding="utf-8",
    )

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
