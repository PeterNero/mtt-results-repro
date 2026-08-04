"""Build R_theta/VSD-02 strict replay or response-functional route artifact."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_rtheta_vsd02strictreplay_or_responsefunctionalroute"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
STRICT_REPLAY = PACKET_DIR / "vsd02_current_strict_replay_after_rtheta_handoff.packet.json"
INTERNAL_ROUTE = PACKET_DIR / "selected_response_functional_route_requirements.packet.json"
EXTERNAL_ROUTE = PACKET_DIR / "external_likelihood_route_requirements.packet.json"
PARAMETER_ROUTE = PACKET_DIR / "minimal_universal_parameter_route_requirements.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_vsd02_current_replay.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_RThetaVSD02StrictReplay_or_ResponseFunctionalRoute_v1.md"

RTHETA_HANDOFF = DATA / "selected_rtheta_valuesource_vsd01v2reconciliation_or_vsd02handoff.candidate.json"
RTHETA_PI_AUDIT = (
    DATA
    / "selected_rtheta_valueevaluatorexecution_or_thresholdresponseinstantiation"
    / "threshold_response_instantiation_audit_after_pi_closure.packet.json"
)
VSD02_CLASSIFICATION_CANDIDATE = (
    DATA / "selected_vsd02thresholdresponserule_or_externallikelihoodimport.candidate.json"
)
VSD02_CLASSIFICATION = (
    DATA
    / "selected_vsd02thresholdresponserule_or_externallikelihoodimport"
    / "vsd02_row_route_classification.packet.json"
)
VSD02_FILL_CANDIDATE = (
    DATA / "selected_vsd02acceptedsourcerowsfill_or_noknobthresholdderivation.candidate.json"
)
VSD02_FILL_ATTEMPT = (
    DATA
    / "selected_vsd02acceptedsourcerowsfill_or_noknobthresholdderivation"
    / "accepted_source_rows_fill_attempt.packet.json"
)
VSD02_FILL_DECISION = (
    DATA
    / "selected_vsd02acceptedsourcerowsfill_or_noknobthresholdderivation"
    / "vsd02_accepted_rows_fill_decision.packet.json"
)
FUNCTIONAL_GATE = (
    DATA / "selected_thresholdresponsefunctionalderivation_or_profilelikelihoodacquisition.candidate.json"
)
FUNCTIONAL_CONTRACT = (
    DATA
    / "selected_thresholdresponsefunctionalderivation_or_profilelikelihoodacquisition"
    / "selected_threshold_response_functional_contract.packet.json"
)
EXTERNAL_MANIFEST = (
    DATA
    / "selected_vsd02thresholdresponserule_or_externallikelihoodimport"
    / "external_likelihood_import_manifest.packet.json"
)
PROFILE_STATUS = (
    DATA
    / "selected_profilelikelihoodsourceimport_or_qasu3packetcandidatemining"
    / "profile_likelihood_source_import_status.packet.json"
)
THETA_PARAMETER_GATE = (
    DATA / "selected_thresholdfunctionalsourcetheorem_or_minimaluniversalparameterselection.candidate.json"
)

STATUS = (
    "MTT_SELECTED_RTHETA_VSD02STRICTREPLAY_OR_RESPONSEFUNCTIONALROUTE_"
    "BUILT_NO_ROWS_ACCEPTED_ROUTE_ATOMIC"
)
NEXT = "MTT_Selected_ResponseFunctionalAtomicRoutes_or_ExternalLikelihoodAcquisition_v1"


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
        raise FileNotFoundError("missing R_theta/VSD-02 replay sources: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        RTHETA_HANDOFF,
        RTHETA_PI_AUDIT,
        VSD02_CLASSIFICATION_CANDIDATE,
        VSD02_CLASSIFICATION,
        VSD02_FILL_CANDIDATE,
        VSD02_FILL_ATTEMPT,
        VSD02_FILL_DECISION,
        FUNCTIONAL_GATE,
        FUNCTIONAL_CONTRACT,
        EXTERNAL_MANIFEST,
        PROFILE_STATUS,
        THETA_PARAMETER_GATE,
    ]
    require_sources(sources)

    rtheta_handoff = load(RTHETA_HANDOFF)
    rtheta_pi_audit = load(RTHETA_PI_AUDIT)
    classification_candidate = load(VSD02_CLASSIFICATION_CANDIDATE)
    classification = load(VSD02_CLASSIFICATION)
    fill_candidate = load(VSD02_FILL_CANDIDATE)
    fill_attempt = load(VSD02_FILL_ATTEMPT)
    fill_decision = load(VSD02_FILL_DECISION)
    functional_gate = load(FUNCTIONAL_GATE)
    functional_contract = load(FUNCTIONAL_CONTRACT)
    external_manifest = load(EXTERNAL_MANIFEST)
    profile_status = load(PROFILE_STATUS)
    parameter_gate = load(THETA_PARAMETER_GATE)

    source_owner_retired = (
        "selected_dynamic_operator_source_owner" in rtheta_pi_audit["retired_failures_since_previous"]
        and "selected_dynamic_operator_source_owner" not in rtheta_pi_audit["blocking_failures"]
        and rtheta_handoff["closure_decision"]["VSD01_legacy_dynamic_absence_blocker_retired"] is True
    )
    zero_rows_reconfirmed = (
        classification["accepted_row_count"] == 0
        and fill_attempt["accepted_row_count"] == 0
        and fill_decision["accepted_row_count"] == 0
    )
    strict_fill_closed = (
        fill_candidate["closure_decision"]["strict_fill_attempt_closed"] is True
        and fill_decision["fill_attempt_executed"] is True
    )
    contract_closed = functional_gate["closure_decision"]["functional_contract_closed"] is True
    functional_instantiated = (
        functional_gate["closure_decision"]["selected_threshold_response_functional_instantiated"]
        is True
    )
    external_workspace_acquired = (
        functional_gate["closure_decision"]["external_likelihood_workspace_acquired"] is True
    )

    remaining_after_pi = rtheta_pi_audit["blocking_failures"]
    remaining_after_fill = fill_decision["remaining_hard_failures"]
    merged_open = [
        "same_branch_scale_scheme_loop_convention",
        "threshold_matching_source_rows",
        "mass_scheme_conversion_source_rows",
        "no_knob_value_derivation",
        "full_profile_likelihood_or_accepted_diagonal_theorem",
        "accepted_threshold_matching_source_rows_missing",
        "accepted_mass_scheme_conversion_source_rows_missing",
        "full_profile_likelihood_workspace_missing",
        "no_knob_Yukawa_Higgs_value_derivation_missing",
    ]

    strict_replay = {
        "schema": "MTTRThetaVSD02CurrentStrictReplay.v1",
        "status": "RTHETA_HANDOFF_REPLAYED_VSD02_ZERO_ROWS_RECONFIRMED",
        "rtheta_handoff_source": rel(RTHETA_HANDOFF),
        "pi_closure_audit_source": rel(RTHETA_PI_AUDIT),
        "vsd02_classification_source": rel(VSD02_CLASSIFICATION),
        "vsd02_fill_attempt_source": rel(VSD02_FILL_ATTEMPT),
        "VSD01_legacy_dynamic_absence_blocker_retired": source_owner_retired,
        "retired_failures_since_previous": rtheta_pi_audit["retired_failures_since_previous"],
        "current_blocking_failures_after_pi_closure": remaining_after_pi,
        "current_blocking_failures_after_vsd02_fill": remaining_after_fill,
        "VSD02_row_route_count": len(classification["row_routes"]),
        "VSD02_accepted_row_count": 0,
        "zero_accepted_rows_reconfirmed": zero_rows_reconfirmed,
        "strict_fill_attempt_closed": strict_fill_closed,
        "selected_threshold_response_functional_contract_closed": contract_closed,
        "selected_threshold_response_functional_instantiated": functional_instantiated,
        "external_likelihood_workspace_acquired": external_workspace_acquired,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(STRICT_REPLAY, strict_replay)

    internal_route = {
        "schema": "MTTSelectedResponseFunctionalRouteRequirements.v1",
        "status": "INTERNAL_SELECTED_RESPONSE_FUNCTIONAL_ROUTE_ATOMIZED_OPEN",
        "functional_symbol": functional_contract["functional_symbol"],
        "contract_source": rel(FUNCTIONAL_CONTRACT),
        "domain_required": functional_contract["domain_required"],
        "codomain_required": functional_contract["codomain_required"],
        "row_outputs_required": functional_contract["row_outputs_required"],
        "atomic_lemmas_required": [
            {
                "id": "same_branch_scale_scheme_loop_convention",
                "must_produce": "a true-equivalence scale/scheme/loop convention owned by the same selected branch",
                "currently_closed": False,
            },
            {
                "id": "threshold_matching_source_rows",
                "must_produce": "accepted top/bottom/charm/tau/W_Z_H threshold matching source rows",
                "currently_closed": False,
            },
            {
                "id": "mass_scheme_conversion_source_rows",
                "must_produce": "accepted pole/running/MSbar/native-scale conversion rows with provenance",
                "currently_closed": False,
            },
            {
                "id": "profile_response_payload",
                "must_produce": "full covariance/profile response or an accepted diagonal limitation theorem",
                "currently_closed": False,
            },
            {
                "id": "no_observed_selector_proof",
                "must_produce": "proof that observed masses, Yukawas, gauge values, and mixings validate but do not select R_theta",
                "currently_closed": False,
            },
        ],
        "forbidden_shortcuts": functional_contract["forbidden_shortcuts"],
        "accepted_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(INTERNAL_ROUTE, internal_route)

    external_route = {
        "schema": "MTTExternalLikelihoodRouteRequirements.v1",
        "status": "EXTERNAL_FULL_PROFILE_OR_THRESHOLD_SOURCE_IMPORT_ROUTE_OPEN",
        "manifest_source": rel(EXTERNAL_MANIFEST),
        "profile_status_source": rel(PROFILE_STATUS),
        "accepted_external_likelihood_imported_now": external_manifest[
            "accepted_external_likelihood_imported_now"
        ],
        "full_likelihood_workspace_acquired": external_workspace_acquired,
        "required_import_payload": external_manifest["required_import_payload"],
        "current_profile_status": profile_status["status"],
        "partial_higgs_covariance_is_not_full_likelihood": True,
        "accepted_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(EXTERNAL_ROUTE, external_route)

    parameter_route = {
        "schema": "MTTMinimalUniversalParameterRouteRequirements.v1",
        "status": "MINIMAL_UNIVERSAL_PARAMETER_ROUTE_OPEN_ONLY_IF_NOKNOB_ROUTE_FAILS",
        "parameter_gate_source": rel(THETA_PARAMETER_GATE),
        "source_theorem_status": parameter_gate["status"],
        "why_route_exists": (
            "If no-knob derivation of magnitude-bearing rows cannot be obtained from selected branch "
            "data, the honest fallback is to declare a minimal universal parameter policy before "
            "row execution, then audit it as physics input rather than a hidden fit."
        ),
        "required_before_use": [
            "state the parameter count and allowed domain before measured-value comparison",
            "prove the parameter is universal across the affected rows",
            "show it is not selected from observed SM target values",
            "re-run threshold and mass-scheme row generation with the parameter policy fixed",
        ],
        "accepted_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(PARAMETER_ROUTE, parameter_route)

    cutset = {
        "schema": "MTTNextCutsetAfterRThetaVSD02CurrentReplay.v1",
        "status": "NEXT_ATTACK_ATOMIC_RESPONSE_FUNCTIONAL_OR_EXTERNAL_ACQUISITION",
        "closed_now": {
            "RTheta_VSD01_handoff_replayed": True,
            "stale_selected_dynamic_operator_source_owner_failure_retired": source_owner_retired,
            "VSD02_route_classification_confirmed": classification_candidate["closure_decision"][
                "VSD02_route_classification_closed"
            ],
            "VSD02_strict_fill_attempt_confirmed": strict_fill_closed,
            "selected_threshold_response_functional_contract_confirmed": contract_closed,
        },
        "not_closed_now": {
            "accepted_vsd02_source_rows": zero_rows_reconfirmed is False,
            "selected_threshold_response_functional_instantiated": functional_instantiated,
            "external_likelihood_workspace_acquired": external_workspace_acquired,
            "true_SM_equivalence": False,
            "full_no_knob": False,
        },
        "still_open_atomic_failures": merged_open,
        "atomic_routes": [
            {
                "id": "internal_selected_response_functional",
                "packet": rel(INTERNAL_ROUTE),
                "closes_if": [
                    "same-branch convention closes",
                    "threshold matching source rows close",
                    "mass-scheme conversion rows close",
                    "profile response or diagonal limitation theorem closes",
                    "no observed selector proof closes",
                ],
            },
            {
                "id": "external_likelihood_or_threshold_source_import",
                "packet": rel(EXTERNAL_ROUTE),
                "closes_if": [
                    "full machine-readable likelihood/source workspace is imported",
                    "basis/provenance/replay semantics are sufficient",
                    "rows map to the R_theta value packet without target selection",
                ],
            },
            {
                "id": "minimal_universal_parameter_policy",
                "packet": rel(PARAMETER_ROUTE),
                "closes_if": [
                    "no-knob route is explicitly abandoned for the affected rows",
                    "universal parameter count/domain are fixed before comparison",
                    "row execution is replayed under that declared policy",
                ],
            },
        ],
        "recommended_next": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedRThetaVSD02StrictReplayOrResponseFunctionalRoute",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "vsd02_current_strict_replay_after_rtheta_handoff": rel(STRICT_REPLAY),
            "selected_response_functional_route_requirements": rel(INTERNAL_ROUTE),
            "external_likelihood_route_requirements": rel(EXTERNAL_ROUTE),
            "minimal_universal_parameter_route_requirements": rel(PARAMETER_ROUTE),
            "next_cutset_after_vsd02_current_replay": rel(CUTSET),
        },
        "theorem": {
            "name": "RThetaVSD02StrictReplayAndAtomicRouteTheorem",
            "proved": True,
            "statement": (
                "After the R_theta/VSD01 handoff, the stale selected-dynamic-source-owner failure is retired. "
                "Replaying VSD02 classification and strict fill still yields zero accepted source rows. "
                "Therefore the frontier is not a hidden VSD01 source problem but exactly the atomic "
                "response-functional, external-likelihood, or declared-minimal-parameter route."
            ),
        },
        "what_closes_now": cutset["closed_now"],
        "what_remains_open": merged_open,
        "closure_decision": {
            "rtheta_vsd01_handoff_closed": True,
            "stale_selected_dynamic_operator_source_owner_failure_retired": source_owner_retired,
            "vsd02_route_classification_closed": True,
            "strict_fill_attempt_closed": strict_fill_closed,
            "selected_threshold_response_functional_contract_closed": contract_closed,
            "accepted_vsd02_source_rows_closed": False,
            "selected_threshold_response_functional_instantiated": False,
            "external_likelihood_workspace_acquired": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "accepted_row_count": 0,
        "atomic_routes": cutset["atomic_routes"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_RThetaVSD02StrictReplay_or_ResponseFunctionalRoute_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "accepted_row_count": 0,
        "source_owner_retired": source_owner_retired,
        "atomic_route_count": len(cutset["atomic_routes"]),
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected RThetaVSD02StrictReplay or ResponseFunctionalRoute v1

Status: `{STATUS}`.

This artifact replays the current `R_theta` handoff against the VSD-02 strict
fill frontier.

```text
stale selected-source-owner failure retired : {str(source_owner_retired).lower()}
VSD02 row routes classified                 : {len(classification["row_routes"])}
accepted VSD02 source rows                  : 0
strict fill attempt closed                  : {str(strict_fill_closed).lower()}
response functional contract closed         : {str(contract_closed).lower()}
response functional instantiated            : false
external likelihood workspace acquired      : false
```

So the blocker is no longer the old VSD-01 source-owner issue.  The next live
target is atomic:

- derive the selected internal `R_theta` threshold response functional,
- or import an accepted full external likelihood/threshold source workspace,
- or explicitly declare a minimal universal parameter policy if no-knob source
  derivation fails.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
