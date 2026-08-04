"""Audit response-functional atomic routes or external likelihood acquisition artifact."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_responsefunctionalatomicroutes_or_externallikelihoodacquisition"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
NO_SELECTOR = PACKET_DIR / "no_observed_selector_response_lemma.packet.json"
INTERNAL_PROGRESS = PACKET_DIR / "internal_response_functional_atomic_progress.packet.json"
EXTERNAL_RECHECK = PACKET_DIR / "external_likelihood_acquisition_recheck.packet.json"
ORDERING = PACKET_DIR / "ordered_remaining_response_functional_cutset.packet.json"
DECISION = PACKET_DIR / "response_functional_atomic_route_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_ResponseFunctionalAtomicRoutes_or_ExternalLikelihoodAcquisition_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_RESPONSEFUNCTIONALATOMICROUTES_OR_EXTERNALLIKELIHOODACQUISITION_"
    "BUILT_SELECTOR_LEMMA_CLOSED_VALUE_ROWS_OPEN"
)
NEXT = "MTT_Selected_SameBranchConvention_or_ThresholdRowEmission_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    no_selector = load(NO_SELECTOR)
    internal = load(INTERNAL_PROGRESS)
    external = load(EXTERNAL_RECHECK)
    ordering = load(ORDERING)
    decision = load(DECISION)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    for key in [
        "closure_claimed",
        "unpatched_theorem_closure_claimed",
        "observed_data_used_as_selector",
        "target_fitting_used",
    ]:
        require(data[key] is False, f"candidate guardrail overclaimed: {key}")
    require(data["theorem"]["proved"] is True, "candidate theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")

    require(
        no_selector["status"] == "NO_OBSERVED_SELECTOR_LEMMA_CLOSED_FOR_ROUTE_GUARD",
        "selector lemma status mismatch",
    )
    require(no_selector["lemma_closed"] is True, "selector lemma not closed")
    require(no_selector["does_not_emit_value_rows"] is True, "selector lemma emitted value rows")
    require(no_selector["observed_data_used_as_selector"] is False, "selector lemma used observed selector")
    require(no_selector["target_fitting_used"] is False, "selector lemma used target fitting")
    require(no_selector["closure_claimed"] is True, "selector lemma should claim local closure")
    require(
        "first-pass common-scale values as true precision source rows"
        in no_selector["forbidden_backsolve_routes_rejected"],
        "first-pass shortcut guard missing",
    )

    require(
        internal["status"] == "INTERNAL_ROUTE_SELECTOR_LEMMA_CLOSED_VALUE_EMISSION_OPEN",
        "internal status mismatch",
    )
    require(internal["domain_dynamic_family_subgate_closed"] is True, "dynamic/family domain not closed")
    require(internal["basis_map_to_magnitude_rows_closed"] is False, "basis map overclosed")
    require(
        internal["same_branch_true_precision_convention_closed"] is False,
        "same-branch convention overclosed",
    )
    require(internal["closed_atomic_count"] == 1, "wrong internal closed atomic count")
    require(internal["required_atomic_count"] == 6, "wrong internal required atomic count")
    progress = {row["id"]: row for row in internal["atomic_progress"]}
    require(progress["no_observed_selector_proof"]["closed_now"] is True, "selector proof not closed")
    for key in [
        "selected_response_functional_map",
        "same_branch_scale_scheme_loop_convention",
        "threshold_matching_source_rows",
        "mass_scheme_conversion_source_rows",
        "profile_response_or_diagonal_limitation",
    ]:
        require(progress[key]["closed_now"] is False, f"internal route overclosed: {key}")
        require(progress[key]["blocking_reason"], f"missing blocker reason: {key}")
    for key in [
        "selected_threshold_response_functional_instantiated",
        "accepted_vsd02_source_rows_closed",
        "closure_claimed",
        "observed_data_used_as_selector",
        "target_fitting_used",
    ]:
        require(internal[key] is False, f"internal overclaimed: {key}")

    require(
        external["status"] == "EXTERNAL_LIKELIHOOD_ACQUISITION_RECHECKED_STILL_OPEN",
        "external status mismatch",
    )
    require(external["accepted_external_likelihood_imported_now"] is False, "external import overclaimed")
    require(external["full_likelihood_workspace_acquired"] is False, "external workspace overclaimed")
    require(
        external["partial_higgs_covariance_is_not_full_likelihood"] is True,
        "partial covariance guard missing",
    )
    require(external["accepted_now"] is False, "external accepted overclaimed")
    require(external["closure_claimed"] is False, "external overclosed")

    require(ordering["status"] == "REMAINING_CUTSET_ORDERED_CONVENTION_FIRST", "ordering status mismatch")
    require(ordering["closed_now"] == ["no_observed_selector_proof"], "unexpected closed list")
    require(ordering["recommended_next"] == NEXT, "ordering next mismatch")
    ordered = ordering["still_open_ordered"]
    require(len(ordered) == 5, "wrong ordered cutset length")
    require(ordered[0]["id"] == "same_branch_scale_scheme_loop_convention", "convention not first")
    require(ordered[1]["id"] == "threshold_matching_source_rows", "threshold rows not second")
    require(ordered[2]["id"] == "mass_scheme_conversion_source_rows", "mass-scheme rows not third")
    require(ordered[3]["id"] == "profile_response_or_diagonal_limitation", "profile response not fourth")
    require(ordered[4]["id"] == "minimal_universal_parameter_policy", "parameter policy not last")
    require(ordering["closure_claimed"] is False, "ordering overclosed")

    require(decision["status"] == "SELECTOR_GUARD_CLOSED_RESPONSE_VALUE_LAYER_OPEN", "decision status mismatch")
    require(decision["VSD02_accepted_row_count"] == 0, "decision accepted rows overclaimed")
    require(decision["formal_atomic_lemma_closed_now"] == "no_observed_selector_proof", "wrong closed lemma")
    require(decision["closed_atomic_count_after"] == 1, "wrong closed count after")
    for key in [
        "selected_response_functional_map",
        "same_branch_scale_scheme_loop_convention",
        "threshold_matching_source_rows",
        "mass_scheme_conversion_source_rows",
        "profile_response_or_diagonal_limitation",
    ]:
        require(key in decision["remaining_hard_failures_after"], f"remaining failure missing: {key}")
    for key in [
        "external_likelihood_acquired",
        "minimal_universal_parameter_selected",
        "selected_threshold_response_functional_instantiated",
        "accepted_vsd02_source_rows_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
        "observed_data_used_as_selector",
        "target_fitting_used",
        "closure_claimed",
    ]:
        require(decision[key] is False, f"decision overclaimed: {key}")

    closure = data["closure_decision"]
    require(closure["no_observed_selector_proof_closed"] is True, "candidate selector proof not closed")
    for key in [
        "same_branch_scale_scheme_loop_convention_closed",
        "threshold_matching_source_rows_closed",
        "mass_scheme_conversion_source_rows_closed",
        "profile_response_or_diagonal_limitation_closed",
        "external_likelihood_workspace_acquired",
        "minimal_universal_parameter_selection_closed",
        "selected_threshold_response_functional_instantiated",
        "accepted_vsd02_source_rows_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(closure[key] is False, f"candidate overclosed: {key}")
    require("no-observed-selector lemma closed        : true" in note, "note missing selector line")
    require("1. `same_branch_scale_scheme_loop_convention`" in note, "note missing ordered convention")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
