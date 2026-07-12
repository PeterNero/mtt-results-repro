"""Audit Step53 response-functional contract replay / atomic routes."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step53_responsefunctional_contract_replay_or_atomicroutes"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
CONTRACT_REPLAY = PACKET_DIR / "step53_response_functional_contract_replay.packet.json"
ATOMIC_ROUTES = PACKET_DIR / "step53_atomic_route_frontier.packet.json"
VALUE_RECHECK = PACKET_DIR / "step53_value_execution_recheck.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step53_ResponseFunctionalContractReplay_or_AtomicRoutes_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP53_RESPONSE_FUNCTIONAL_CONTRACT_REPLAYED_ATOMIC_ROUTES_OPEN"
NEXT = "MTT_Selected_ResponseFunctionalAtomicRoutes_or_ExternalLikelihoodAcquisition_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    replay = load(CONTRACT_REPLAY)
    routes = load(ATOMIC_ROUTES)
    values = load(VALUE_RECHECK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "Step53 theorem not proved")

    for packet in [data, replay, routes, values, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    require(replay["step52_frontier_locked"] is True, "Step52 frontier not imported")
    require(replay["functional_contract_closed"] is True, "functional contract not closed")
    require(replay["selected_threshold_response_functional_contract_closed"] is True, "threshold contract missing")
    require(
        replay["stale_selected_dynamic_operator_source_owner_failure_retired"] is True,
        "stale dynamic-owner failure not retired",
    )
    require(
        "selected_dynamic_operator_source_owner" not in replay["current_blocking_failures"],
        "stale dynamic-owner failure still blocking",
    )
    for key in [
        "same_branch_scale_scheme_loop_convention",
        "threshold_matching_source_rows",
        "mass_scheme_conversion_source_rows",
        "no_knob_value_derivation",
        "full_profile_likelihood_or_accepted_diagonal_theorem",
    ]:
        require(key in replay["current_blocking_failures"], f"real blocker missing: {key}")

    require(routes["recommended_next"] == NEXT, "routes next mismatch")
    require(routes["accepted_routes_now"] == [], "atomic route overaccepted")
    require(
        routes["internal_selected_response_functional"]["accepted_now"] is False,
        "internal route overaccepted",
    )
    require(
        routes["external_likelihood_or_threshold_source_import"]["accepted_now"] is False,
        "external route overaccepted",
    )
    require(
        routes["minimal_universal_parameter_policy"]["accepted_now"] is False,
        "parameter route overaccepted",
    )

    require(values["accepted_vsd02_source_row_count"] == 0, "VSD02 rows overaccepted")
    require(values["selected_threshold_response_functional_instantiated"] is False, "functional overinstantiated")
    require(values["external_likelihood_workspace_acquired"] is False, "workspace overacquired")
    require(values["accepted_internal_Rtheta_coefficient_row_count"] == 0, "Rtheta rows overaccepted")
    require(values["accepted_internal_scalar_row_count"] == 0, "scalar rows overaccepted")
    for key in [
        "selected_lambda_H_row_closed",
        "minimal_parameter_closure_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(values[key] is False, f"value recheck overclosed: {key}")

    decision = data["closure_decision"]
    for key in [
        "response_functional_contract_replayed",
        "stale_selected_dynamic_operator_source_owner_failure_retired",
        "atomic_routes_locked",
    ]:
        require(decision[key] is True, f"candidate closure missing: {key}")
        require(cert[key] is True, f"certificate closure missing: {key}")
    require(decision["accepted_vsd02_source_row_count"] == 0, "candidate VSD02 rows overaccepted")
    for key in [
        "selected_threshold_response_functional_instantiated",
        "external_likelihood_workspace_acquired",
        "selected_lambda_H_row_closed",
        "minimal_parameter_closure_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"candidate overclosed: {key}")
        require(cert[key] is False, f"certificate overclosed: {key}")
    require(data["minimal_parameter_closure_claimed"] is False, "minimal closure overclaimed")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaimed")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaimed")

    for phrase in [
        "contract replayed                       : true",
        "stale dynamic-owner failure retired     : true",
        "accepted VSD02 source rows              : 0",
        "response functional instantiated        : false",
        NEXT,
    ]:
        require(phrase in note, f"note missing phrase: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
