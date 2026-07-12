"""Audit R_theta/VSD-02 strict replay or response-functional route artifact."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_rtheta_vsd02strictreplay_or_responsefunctionalroute"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
STRICT_REPLAY = PACKET_DIR / "vsd02_current_strict_replay_after_rtheta_handoff.packet.json"
INTERNAL_ROUTE = PACKET_DIR / "selected_response_functional_route_requirements.packet.json"
EXTERNAL_ROUTE = PACKET_DIR / "external_likelihood_route_requirements.packet.json"
PARAMETER_ROUTE = PACKET_DIR / "minimal_universal_parameter_route_requirements.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_vsd02_current_replay.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_RThetaVSD02StrictReplay_or_ResponseFunctionalRoute_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_RTHETA_VSD02STRICTREPLAY_OR_RESPONSEFUNCTIONALROUTE_"
    "BUILT_NO_ROWS_ACCEPTED_ROUTE_ATOMIC"
)
NEXT = "MTT_Selected_ResponseFunctionalAtomicRoutes_or_ExternalLikelihoodAcquisition_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    replay = load(STRICT_REPLAY)
    internal = load(INTERNAL_ROUTE)
    external = load(EXTERNAL_ROUTE)
    parameter = load(PARAMETER_ROUTE)
    cutset = load(CUTSET)
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
    require(data["accepted_row_count"] == 0, "candidate accepted rows overclaimed")

    require(
        replay["status"] == "RTHETA_HANDOFF_REPLAYED_VSD02_ZERO_ROWS_RECONFIRMED",
        "strict replay status mismatch",
    )
    require(
        replay["VSD01_legacy_dynamic_absence_blocker_retired"] is True,
        "source-owner retirement not replayed",
    )
    require(
        "selected_dynamic_operator_source_owner" in replay["retired_failures_since_previous"],
        "retired source-owner failure missing",
    )
    require(
        "selected_dynamic_operator_source_owner"
        not in replay["current_blocking_failures_after_pi_closure"],
        "stale source-owner failure still present",
    )
    require(replay["VSD02_row_route_count"] == 6, "wrong VSD02 route count")
    require(replay["VSD02_accepted_row_count"] == 0, "replay accepted rows overclaimed")
    require(replay["zero_accepted_rows_reconfirmed"] is True, "zero-row replay not confirmed")
    require(replay["strict_fill_attempt_closed"] is True, "strict fill not closed")
    require(
        replay["selected_threshold_response_functional_contract_closed"] is True,
        "functional contract not closed",
    )
    for key in [
        "selected_threshold_response_functional_instantiated",
        "external_likelihood_workspace_acquired",
        "closure_claimed",
        "observed_data_used_as_selector",
        "target_fitting_used",
    ]:
        require(replay[key] is False, f"replay overclaimed: {key}")

    require(
        internal["status"] == "INTERNAL_SELECTED_RESPONSE_FUNCTIONAL_ROUTE_ATOMIZED_OPEN",
        "internal route status mismatch",
    )
    require(internal["functional_symbol"] == "R_theta", "wrong functional symbol")
    require(len(internal["domain_required"]) >= 5, "domain contract too small")
    require(len(internal["codomain_required"]) >= 5, "codomain contract too small")
    lemma_ids = {lemma["id"] for lemma in internal["atomic_lemmas_required"]}
    for key in [
        "same_branch_scale_scheme_loop_convention",
        "threshold_matching_source_rows",
        "mass_scheme_conversion_source_rows",
        "profile_response_payload",
        "no_observed_selector_proof",
    ]:
        require(key in lemma_ids, f"internal route lemma missing: {key}")
    require(internal["accepted_now"] is False, "internal route overaccepted")
    require(internal["closure_claimed"] is False, "internal route overclosed")

    require(
        external["status"] == "EXTERNAL_FULL_PROFILE_OR_THRESHOLD_SOURCE_IMPORT_ROUTE_OPEN",
        "external route status mismatch",
    )
    require(
        external["accepted_external_likelihood_imported_now"] is False,
        "external import overclaimed",
    )
    require(
        external["full_likelihood_workspace_acquired"] is False,
        "external workspace overclaimed",
    )
    require(
        external["partial_higgs_covariance_is_not_full_likelihood"] is True,
        "partial covariance guard missing",
    )
    require(len(external["required_import_payload"]) >= 5, "external payload contract too small")
    require(external["accepted_now"] is False, "external route overaccepted")
    require(external["closure_claimed"] is False, "external route overclosed")

    require(
        parameter["status"] == "MINIMAL_UNIVERSAL_PARAMETER_ROUTE_OPEN_ONLY_IF_NOKNOB_ROUTE_FAILS",
        "parameter route status mismatch",
    )
    require(len(parameter["required_before_use"]) == 4, "parameter route requirements changed")
    require(parameter["accepted_now"] is False, "parameter route overaccepted")
    require(parameter["closure_claimed"] is False, "parameter route overclosed")

    require(cutset["status"] == "NEXT_ATTACK_ATOMIC_RESPONSE_FUNCTIONAL_OR_EXTERNAL_ACQUISITION", "cutset status mismatch")
    require(cutset["recommended_next"] == NEXT, "cutset next mismatch")
    require(len(cutset["atomic_routes"]) == 3, "atomic route count mismatch")
    route_ids = {route["id"] for route in cutset["atomic_routes"]}
    for key in [
        "internal_selected_response_functional",
        "external_likelihood_or_threshold_source_import",
        "minimal_universal_parameter_policy",
    ]:
        require(key in route_ids, f"atomic route missing: {key}")
    closed = cutset["closed_now"]
    for key in [
        "RTheta_VSD01_handoff_replayed",
        "stale_selected_dynamic_operator_source_owner_failure_retired",
        "VSD02_route_classification_confirmed",
        "VSD02_strict_fill_attempt_confirmed",
        "selected_threshold_response_functional_contract_confirmed",
    ]:
        require(closed[key] is True, f"closed flag missing: {key}")
    require("same_branch_scale_scheme_loop_convention" in cutset["still_open_atomic_failures"], "scale/scheme blocker missing")
    require("threshold_matching_source_rows" in cutset["still_open_atomic_failures"], "threshold blocker missing")
    require("mass_scheme_conversion_source_rows" in cutset["still_open_atomic_failures"], "mass-scheme blocker missing")
    require(cutset["closure_claimed"] is False, "cutset overclosed")

    decision = data["closure_decision"]
    for key in [
        "rtheta_vsd01_handoff_closed",
        "stale_selected_dynamic_operator_source_owner_failure_retired",
        "vsd02_route_classification_closed",
        "strict_fill_attempt_closed",
        "selected_threshold_response_functional_contract_closed",
    ]:
        require(decision[key] is True, f"candidate closure flag missing: {key}")
    for key in [
        "accepted_vsd02_source_rows_closed",
        "selected_threshold_response_functional_instantiated",
        "external_likelihood_workspace_acquired",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"candidate overclosed: {key}")
    require(len(data["atomic_routes"]) == 3, "candidate route count mismatch")
    require("accepted VSD02 source rows                  : 0" in note, "note missing zero-row line")
    require("response functional instantiated            : false" in note, "note missing functional-open line")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
