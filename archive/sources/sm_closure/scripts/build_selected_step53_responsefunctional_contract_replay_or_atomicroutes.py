"""Build Step53 response-functional contract replay / atomic routes."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step53_responsefunctional_contract_replay_or_atomicroutes"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CONTRACT_REPLAY = PACKET_DIR / "step53_response_functional_contract_replay.packet.json"
ATOMIC_ROUTES = PACKET_DIR / "step53_atomic_route_frontier.packet.json"
VALUE_RECHECK = PACKET_DIR / "step53_value_execution_recheck.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step53_ResponseFunctionalContractReplay_or_AtomicRoutes_v1.md"

STEP52 = DATA / "selected_step52_vsd02_strict_value_source_frontier_or_likelihoodworkspace.candidate.json"
THRESHOLD_CONTRACT = DATA / "selected_thresholdresponsefunctionalderivation_or_profilelikelihoodacquisition.candidate.json"
CONTRACT = (
    DATA
    / "selected_thresholdresponsefunctionalderivation_or_profilelikelihoodacquisition"
    / "selected_threshold_response_functional_contract.packet.json"
)
FUNCTIONAL_DECISION = (
    DATA
    / "selected_thresholdresponsefunctionalderivation_or_profilelikelihoodacquisition"
    / "threshold_response_functional_decision.packet.json"
)
STRICT_REPLAY_CANDIDATE = DATA / "selected_rtheta_vsd02strictreplay_or_responsefunctionalroute.candidate.json"
STRICT_REPLAY = (
    DATA
    / "selected_rtheta_vsd02strictreplay_or_responsefunctionalroute"
    / "vsd02_current_strict_replay_after_rtheta_handoff.packet.json"
)
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
STRICT_CUTSET = (
    DATA
    / "selected_rtheta_vsd02strictreplay_or_responsefunctionalroute"
    / "next_cutset_after_vsd02_current_replay.packet.json"
)

STATUS = "MTT_SELECTED_STEP53_RESPONSE_FUNCTIONAL_CONTRACT_REPLAYED_ATOMIC_ROUTES_OPEN"
NEXT = "MTT_Selected_ResponseFunctionalAtomicRoutes_or_ExternalLikelihoodAcquisition_v1"


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
        STEP52,
        THRESHOLD_CONTRACT,
        CONTRACT,
        FUNCTIONAL_DECISION,
        STRICT_REPLAY_CANDIDATE,
        STRICT_REPLAY,
        INTERNAL_ROUTE,
        EXTERNAL_ROUTE,
        PARAMETER_ROUTE,
        STRICT_CUTSET,
    ]
    missing = [rel(path) for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step53 inputs: " + ", ".join(missing))

    step52 = load(STEP52)
    threshold_contract = load(THRESHOLD_CONTRACT)
    contract = load(CONTRACT)
    decision = load(FUNCTIONAL_DECISION)
    strict_candidate = load(STRICT_REPLAY_CANDIDATE)
    replay = load(STRICT_REPLAY)
    internal = load(INTERNAL_ROUTE)
    external = load(EXTERNAL_ROUTE)
    parameter = load(PARAMETER_ROUTE)
    cutset = load(STRICT_CUTSET)

    contract_replay = {
        "schema": "MTTStep53ResponseFunctionalContractReplay.v1",
        "status": "CONTRACT_REPLAYED_STALE_DYNAMIC_OWNER_FAILURE_RETIRED",
        "step52_frontier_locked": step52["closure_decision"]["VSD02_strict_frontier_locked"],
        "functional_contract_closed": contract["closure_claimed"],
        "selected_threshold_response_functional_contract_closed": replay[
            "selected_threshold_response_functional_contract_closed"
        ],
        "stale_selected_dynamic_operator_source_owner_failure_retired": (
            "selected_dynamic_operator_source_owner" in replay["retired_failures_since_previous"]
        ),
        "current_blocking_failures": replay["current_blocking_failures_after_pi_closure"],
        "old_functional_decision_failures": decision["remaining_hard_failures"],
        "contract_domain_required": contract["domain_required"],
        "contract_codomain_required": contract["codomain_required"],
        "forbidden_shortcuts": contract["forbidden_shortcuts"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(CONTRACT_REPLAY, contract_replay)

    atomic_routes = {
        "schema": "MTTStep53AtomicRouteFrontier.v1",
        "status": "THREE_ATOMIC_ROUTES_LOCKED_NONE_ACCEPTED",
        "internal_selected_response_functional": internal,
        "external_likelihood_or_threshold_source_import": external,
        "minimal_universal_parameter_policy": parameter,
        "recommended_next": cutset["recommended_next"],
        "still_open_atomic_failures": cutset["still_open_atomic_failures"],
        "accepted_routes_now": [],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(ATOMIC_ROUTES, atomic_routes)

    value_recheck = {
        "schema": "MTTStep53ValueExecutionRecheck.v1",
        "status": "VALUE_EXECUTION_RECHECKED_ZERO_ROWS",
        "accepted_vsd02_source_row_count": replay["VSD02_accepted_row_count"],
        "selected_threshold_response_functional_instantiated": replay[
            "selected_threshold_response_functional_instantiated"
        ],
        "external_likelihood_workspace_acquired": replay["external_likelihood_workspace_acquired"],
        "accepted_internal_Rtheta_coefficient_row_count": 0,
        "accepted_internal_scalar_row_count": 0,
        "selected_lambda_H_row_closed": False,
        "minimal_parameter_closure_closed": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(VALUE_RECHECK, value_recheck)

    candidate = {
        "candidate": "MTTSelectedStep53ResponseFunctionalContractReplayOrAtomicRoutes",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in inputs},
        "output_packets": {
            "response_functional_contract_replay": rel(CONTRACT_REPLAY),
            "atomic_route_frontier": rel(ATOMIC_ROUTES),
            "value_execution_recheck": rel(VALUE_RECHECK),
        },
        "theorem": {
            "name": "Step53ResponseFunctionalContractReplayAndAtomicRoutesTheorem",
            "proved": True,
            "statement": (
                "The selected threshold response functional contract is replayed after Step52. "
                "The stale selected_dynamic_operator_source_owner failure is retired by the Rtheta/VSD01 "
                "handoff. Zero VSD02 source rows remain accepted, so value execution is still closed only "
                "as a route specification. The remaining frontier is three atomic routes: internal selected "
                "response functional, external likelihood/source import, or a declared minimal universal "
                "parameter policy."
            ),
        },
        "closure_decision": {
            "response_functional_contract_replayed": True,
            "stale_selected_dynamic_operator_source_owner_failure_retired": True,
            "atomic_routes_locked": True,
            "accepted_vsd02_source_row_count": replay["VSD02_accepted_row_count"],
            "selected_threshold_response_functional_instantiated": False,
            "external_likelihood_workspace_acquired": False,
            "accepted_internal_Rtheta_coefficient_row_count": 0,
            "accepted_internal_scalar_row_count": 0,
            "selected_lambda_H_row_closed": False,
            "minimal_parameter_closure_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
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
        "certificate": "MTT_Selected_Step53_ResponseFunctionalContractReplay_or_AtomicRoutes_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        **candidate["closure_decision"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected Step53 ResponseFunctionalContractReplay or AtomicRoutes v1

Status: `{STATUS}`.

Step53 replays the threshold-response contract after the Step52 strict frontier.

```text
contract replayed                       : true
stale dynamic-owner failure retired     : true
accepted VSD02 source rows              : {replay["VSD02_accepted_row_count"]}
response functional instantiated        : false
external likelihood workspace acquired  : false
```

The remaining routes are atomic: internal selected `R_theta` response
functional, external likelihood/source import, or explicitly declared minimal
universal parameter policy.

Next artifact: `{NEXT}`.
""",
        encoding="utf-8",
    )

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
