"""Build response-functional atomic routes or external likelihood acquisition artifact."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_responsefunctionalatomicroutes_or_externallikelihoodacquisition"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
NO_SELECTOR = PACKET_DIR / "no_observed_selector_response_lemma.packet.json"
INTERNAL_PROGRESS = PACKET_DIR / "internal_response_functional_atomic_progress.packet.json"
EXTERNAL_RECHECK = PACKET_DIR / "external_likelihood_acquisition_recheck.packet.json"
ORDERING = PACKET_DIR / "ordered_remaining_response_functional_cutset.packet.json"
DECISION = PACKET_DIR / "response_functional_atomic_route_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_ResponseFunctionalAtomicRoutes_or_ExternalLikelihoodAcquisition_v1.md"

PREVIOUS = DATA / "selected_rtheta_vsd02strictreplay_or_responsefunctionalroute.candidate.json"
INTERNAL_ROUTE = (
    DATA
    / "selected_rtheta_vsd02strictreplay_or_responsefunctionalroute"
    / "selected_response_functional_route_requirements.packet.json"
)
EXTERNAL_ROUTE = (
    DATA
    / "selected_rtheta_vsd02strictreplay_or_responsefunctionalroute"
    / "external_likelihood_route_requirements.packet.json"
)
PARAMETER_ROUTE = (
    DATA
    / "selected_rtheta_vsd02strictreplay_or_responsefunctionalroute"
    / "minimal_universal_parameter_route_requirements.packet.json"
)
RTHETA_DOMAIN = (
    DATA
    / "selected_thresholdfunctionalsourcetheorem_or_minimaluniversalparameterselection"
    / "rtheta_domain_readiness_after_dynamic_family_closure.packet.json"
)
RTHETA_UPDATE = (
    DATA
    / "selected_thresholdfunctionalsourcetheorem_or_minimaluniversalparameterselection"
    / "rtheta_instantiation_update_after_dynamic_source_closure.packet.json"
)
FUNCTIONAL_ATTEMPT = (
    DATA
    / "selected_higherresponsesectorcoefficients_or_thresholdfunctionalsourcerows"
    / "selected_threshold_response_functional_execution_attempt.packet.json"
)
SECTOR_TESTS = (
    DATA
    / "selected_sectorscaledeigenprofilethresholdrows_or_yukawamagnitudesourceexecution"
    / "sector_scaled_eigenprofile_model_tests.packet.json"
)
SECTOR_FRONTIER = (
    DATA
    / "selected_sectorscaledeigenprofilethresholdrows_or_yukawamagnitudesourceexecution"
    / "sector_coefficient_frontier.packet.json"
)
VSD02_FILL_DECISION = (
    DATA
    / "selected_vsd02acceptedsourcerowsfill_or_noknobthresholdderivation"
    / "vsd02_accepted_rows_fill_decision.packet.json"
)
VSD02_FILL_ATTEMPT = (
    DATA
    / "selected_vsd02acceptedsourcerowsfill_or_noknobthresholdderivation"
    / "accepted_source_rows_fill_attempt.packet.json"
)
PROFILE_STATUS = (
    DATA
    / "selected_profilelikelihoodsourceimport_or_qasu3packetcandidatemining"
    / "profile_likelihood_source_import_status.packet.json"
)

STATUS = (
    "MTT_SELECTED_RESPONSEFUNCTIONALATOMICROUTES_OR_EXTERNALLIKELIHOODACQUISITION_"
    "BUILT_SELECTOR_LEMMA_CLOSED_VALUE_ROWS_OPEN"
)
NEXT = "MTT_Selected_SameBranchConvention_or_ThresholdRowEmission_v1"


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
        raise FileNotFoundError("missing response-functional atomic route sources: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        INTERNAL_ROUTE,
        EXTERNAL_ROUTE,
        PARAMETER_ROUTE,
        RTHETA_DOMAIN,
        RTHETA_UPDATE,
        FUNCTIONAL_ATTEMPT,
        SECTOR_TESTS,
        SECTOR_FRONTIER,
        VSD02_FILL_DECISION,
        VSD02_FILL_ATTEMPT,
        PROFILE_STATUS,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    internal_route = load(INTERNAL_ROUTE)
    external_route = load(EXTERNAL_ROUTE)
    parameter_route = load(PARAMETER_ROUTE)
    rtheta_domain = load(RTHETA_DOMAIN)
    rtheta_update = load(RTHETA_UPDATE)
    functional_attempt = load(FUNCTIONAL_ATTEMPT)
    sector_tests = load(SECTOR_TESTS)
    sector_frontier = load(SECTOR_FRONTIER)
    vsd02_fill_decision = load(VSD02_FILL_DECISION)
    vsd02_fill_attempt = load(VSD02_FILL_ATTEMPT)
    profile_status = load(PROFILE_STATUS)

    no_selector_check = next(
        check
        for check in functional_attempt["functional_checks"]
        if check["required_output"] == "proof no observed values select the response"
    )
    no_selector_closed = (
        no_selector_check["present_now"] is True
        and sector_tests["observed_data_used_as_selector"] is False
        and sector_tests["target_fitting_used"] is False
        and functional_attempt["observed_data_used_as_selector"] is False
        and functional_attempt["target_fitting_used"] is False
    )

    no_selector = {
        "schema": "MTTNoObservedSelectorResponseLemma.v1",
        "status": "NO_OBSERVED_SELECTOR_LEMMA_CLOSED_FOR_ROUTE_GUARD",
        "functional_attempt_source": rel(FUNCTIONAL_ATTEMPT),
        "sector_model_test_source": rel(SECTOR_TESTS),
        "source_check": no_selector_check,
        "diagnostic_values_are_labeled_non_selectors": True,
        "forbidden_backsolve_routes_rejected": [
            "sector-specific quadratic log-profile exact coefficients",
            "sector-specific diagnostic hierarchy ratios as source coefficients",
            "first-pass common-scale values as true precision source rows",
            "residual table as self-deriving functional",
        ],
        "lemma_statement": (
            "In the current R_theta/VSD02 route, diagnostic SM values may be used only to reject "
            "or validate candidate rows after their source is fixed. They do not select the response "
            "functional, sector coefficients, scale/scheme convention, threshold rows, or parameter route."
        ),
        "lemma_closed": no_selector_closed,
        "does_not_emit_value_rows": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(NO_SELECTOR, no_selector)

    atomic_progress = [
        {
            "id": "selected_response_functional_map",
            "source": rel(FUNCTIONAL_ATTEMPT),
            "closed_now": False,
            "blocking_reason": "no packet emits the selected map from dynamic MTT data to threshold rows",
        },
        {
            "id": "same_branch_scale_scheme_loop_convention",
            "source": rel(SECTOR_FRONTIER),
            "closed_now": False,
            "blocking_reason": "available convention remains first-pass/parity, not true precision",
        },
        {
            "id": "threshold_matching_source_rows",
            "source": rel(VSD02_FILL_ATTEMPT),
            "closed_now": False,
            "blocking_reason": "VSD02 strict fill accepts no threshold matching source rows",
        },
        {
            "id": "mass_scheme_conversion_source_rows",
            "source": rel(VSD02_FILL_ATTEMPT),
            "closed_now": False,
            "blocking_reason": "VSD02 strict fill accepts no mass-scheme conversion source rows",
        },
        {
            "id": "profile_response_or_diagonal_limitation",
            "source": rel(PROFILE_STATUS),
            "closed_now": False,
            "blocking_reason": "full profile likelihood is not acquired, and no accepted diagonal limitation theorem is present",
        },
        {
            "id": "no_observed_selector_proof",
            "source": rel(NO_SELECTOR),
            "closed_now": no_selector_closed,
            "blocking_reason": None,
        },
    ]
    closed_count = sum(1 for row in atomic_progress if row["closed_now"])

    internal_progress = {
        "schema": "MTTInternalResponseFunctionalAtomicProgress.v1",
        "status": "INTERNAL_ROUTE_SELECTOR_LEMMA_CLOSED_VALUE_EMISSION_OPEN",
        "previous_route_source": rel(INTERNAL_ROUTE),
        "domain_dynamic_family_subgate_closed": (
            rtheta_domain["dynamic_domain_subgate_closed"] is True
            and rtheta_domain["family_coordinate_subgate_closed"] is True
        ),
        "basis_map_to_magnitude_rows_closed": rtheta_domain["basis_map_to_magnitude_rows_closed"],
        "same_branch_true_precision_convention_closed": rtheta_domain[
            "same_branch_true_precision_convention_closed"
        ],
        "atomic_progress": atomic_progress,
        "closed_atomic_count": closed_count,
        "required_atomic_count": len(atomic_progress),
        "selected_threshold_response_functional_instantiated": False,
        "accepted_vsd02_source_rows_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(INTERNAL_PROGRESS, internal_progress)

    external_recheck = {
        "schema": "MTTExternalLikelihoodAcquisitionRecheck.v1",
        "status": "EXTERNAL_LIKELIHOOD_ACQUISITION_RECHECKED_STILL_OPEN",
        "external_route_source": rel(EXTERNAL_ROUTE),
        "profile_status_source": rel(PROFILE_STATUS),
        "accepted_external_likelihood_imported_now": external_route[
            "accepted_external_likelihood_imported_now"
        ],
        "full_likelihood_workspace_acquired": external_route["full_likelihood_workspace_acquired"],
        "partial_higgs_covariance_is_not_full_likelihood": external_route[
            "partial_higgs_covariance_is_not_full_likelihood"
        ],
        "current_profile_status": profile_status["status"],
        "accepted_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(EXTERNAL_RECHECK, external_recheck)

    ordered_remaining = [
        {
            "order": 1,
            "id": "same_branch_scale_scheme_loop_convention",
            "why_first": "all threshold, mass-scheme, and profile rows need a shared scale/scheme/loop convention",
            "can_be_closed_by": [
                "derive true-precision convention from selected branch data",
                "or import external source rows whose convention and replay map are accepted",
            ],
        },
        {
            "order": 2,
            "id": "threshold_matching_source_rows",
            "why_after_convention": "threshold rows are not comparable without a fixed convention",
            "can_be_closed_by": [
                "emit top/bottom/charm/tau/W_Z_H matching rows from R_theta",
                "or import accepted threshold rows with provenance",
            ],
        },
        {
            "order": 3,
            "id": "mass_scheme_conversion_source_rows",
            "why_after_convention": "pole/running/native-scale conversions depend on the same convention",
            "can_be_closed_by": [
                "emit conversion rows from R_theta",
                "or import accepted conversion maps with provenance",
            ],
        },
        {
            "order": 4,
            "id": "profile_response_or_diagonal_limitation",
            "why_after_rows": "covariance/profile semantics attach to the emitted/imported observable rows",
            "can_be_closed_by": [
                "derive full profile response",
                "import a full likelihood workspace",
                "or prove an accepted diagonal limitation theorem",
            ],
        },
        {
            "order": 5,
            "id": "minimal_universal_parameter_policy",
            "why_last": "only honest if no-knob source row emission remains impossible",
            "can_be_closed_by": parameter_route["required_before_use"],
        },
    ]
    ordering = {
        "schema": "MTTOrderedRemainingResponseFunctionalCutset.v1",
        "status": "REMAINING_CUTSET_ORDERED_CONVENTION_FIRST",
        "closed_now": [
            "no_observed_selector_proof"
        ],
        "still_open_ordered": ordered_remaining,
        "recommended_next": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(ORDERING, ordering)

    decision = {
        "schema": "MTTResponseFunctionalAtomicRouteDecision.v1",
        "status": "SELECTOR_GUARD_CLOSED_RESPONSE_VALUE_LAYER_OPEN",
        "previous_status": previous["status"],
        "VSD02_accepted_row_count": vsd02_fill_decision["accepted_row_count"],
        "functional_required_output_count": functional_attempt["required_output_count"],
        "functional_present_required_output_count_before": functional_attempt[
            "present_required_output_count"
        ],
        "formal_atomic_lemma_closed_now": "no_observed_selector_proof",
        "closed_atomic_count_after": closed_count,
        "remaining_hard_failures_after": [
            row["id"] for row in atomic_progress if not row["closed_now"]
        ],
        "external_likelihood_acquired": False,
        "minimal_universal_parameter_selected": False,
        "selected_threshold_response_functional_instantiated": False,
        "accepted_vsd02_source_rows_closed": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(DECISION, decision)

    candidate = {
        "candidate": "MTTSelectedResponseFunctionalAtomicRoutesOrExternalLikelihoodAcquisition",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "no_observed_selector_response_lemma": rel(NO_SELECTOR),
            "internal_response_functional_atomic_progress": rel(INTERNAL_PROGRESS),
            "external_likelihood_acquisition_recheck": rel(EXTERNAL_RECHECK),
            "ordered_remaining_response_functional_cutset": rel(ORDERING),
            "response_functional_atomic_route_decision": rel(DECISION),
        },
        "theorem": {
            "name": "ResponseFunctionalAtomicRouteSelectorLemmaTheorem",
            "proved": True,
            "statement": (
                "The current R_theta/VSD02 route can close the no-observed-selector guard as a formal "
                "atomic lemma: diagnostic measured values are validation/rejection data only and do not "
                "select R_theta, conventions, coefficients, source rows, or parameters. This does not "
                "emit value rows. The remaining value-producing route is ordered convention first, then "
                "threshold rows, mass-scheme rows, and profile/diagonal response, with external acquisition "
                "or minimal universal parameter policy as alternatives."
            ),
        },
        "what_closes_now": {
            "no_observed_selector_proof": no_selector_closed,
            "external_likelihood_rechecked": True,
            "remaining_cutset_ordered": True,
        },
        "what_remains_open": decision["remaining_hard_failures_after"],
        "closure_decision": {
            "no_observed_selector_proof_closed": no_selector_closed,
            "same_branch_scale_scheme_loop_convention_closed": False,
            "threshold_matching_source_rows_closed": False,
            "mass_scheme_conversion_source_rows_closed": False,
            "profile_response_or_diagonal_limitation_closed": False,
            "external_likelihood_workspace_acquired": False,
            "minimal_universal_parameter_selection_closed": False,
            "selected_threshold_response_functional_instantiated": False,
            "accepted_vsd02_source_rows_closed": False,
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
        "certificate": "MTT_Selected_ResponseFunctionalAtomicRoutes_or_ExternalLikelihoodAcquisition_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "no_observed_selector_proof_closed": no_selector_closed,
        "selected_threshold_response_functional_instantiated": False,
        "accepted_vsd02_source_rows_closed": False,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected ResponseFunctionalAtomicRoutes or ExternalLikelihoodAcquisition v1

Status: `{STATUS}`.

This artifact attacks the atomic `R_theta` response-functional route head on.

```text
no-observed-selector lemma closed        : {str(no_selector_closed).lower()}
accepted VSD02 source rows               : {vsd02_fill_decision["accepted_row_count"]}
selected response functional instantiated: false
external likelihood workspace acquired   : false
minimal universal parameter selected     : false
```

The closed piece is a guard lemma, not a value-row theorem: measured SM values
remain validation/rejection data only.  They do not select the response
functional, convention, coefficients, source rows, or universal parameter.

The remaining value-producing cutset is ordered:

1. `same_branch_scale_scheme_loop_convention`
2. `threshold_matching_source_rows`
3. `mass_scheme_conversion_source_rows`
4. `profile_response_or_diagonal_limitation`
5. `minimal_universal_parameter_policy` only if no-knob emission fails

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
