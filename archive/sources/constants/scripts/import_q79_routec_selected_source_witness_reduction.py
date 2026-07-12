"""Import the q79 Route-C selected-source witness-reduction artifact."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")

PREVIOUS = DATA / "q79_selected_de_green_dotd_source_gate_import.candidate.json"
Q79_CERT = (
    Q79
    / "certificates"
    / "q79_routec_selected_source_certificate_or_typed_de_construction_certificate.json"
)
Q79_CANDIDATE = (
    Q79
    / "candidate_data"
    / "q79_routec_selected_source_certificate_or_typed_de_construction.candidate.json"
)
Q79_WITNESS = (
    Q79
    / "candidate_data"
    / "q79_routec_selected_source_certificate_or_typed_de_construction"
    / "selected_connection_witness_contract.open.json"
)
Q79_TYPED = (
    Q79
    / "candidate_data"
    / "q79_routec_selected_source_certificate_or_typed_de_construction"
    / "typed_de_witness_contract.open.json"
)

OUTPUT_PACKET = DATA / "q79_routec_selected_source_witness_reduction_import.candidate.json"
OUTPUT_CERT = CERTS / "q79_routec_selected_source_witness_reduction_import_certificate.json"
OUTPUT_NOTE = CORPUS / "Q79_RouteC_Selected_Source_Witness_Reduction_Import_v1.md"

STATUS = "Q79_ROUTEC_SELECTED_SOURCE_WITNESS_REDUCTION_IMPORTED"
Q79_STATUS = "Q79_ROUTEC_SELECTED_SOURCE_OR_TYPED_DE_CONSTRUCTION_OPEN_WITNESS_CONTRACT_CREATED"
NEXT = "Q79_Typed_Monad_Cech_or_HYM_Connection_Witness_v1"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def q79_rel(path: Path) -> str:
    try:
        return path.relative_to(Q79).as_posix()
    except ValueError:
        return str(path)


def build_packet() -> dict[str, Any]:
    previous = load_json(PREVIOUS)
    q79_cert = load_json(Q79_CERT)
    q79_candidate = load_json(Q79_CANDIDATE)
    witness = load_json(Q79_WITNESS)
    typed = load_json(Q79_TYPED)

    closes = q79_cert["what_closes_now"]
    remains = q79_cert["what_remains_open"]
    honest = q79_cert["honest_routec_selected_source_attempt"]
    diagnostic = q79_cert["hypothetical_selected_source_diagnostic"]
    routes = q79_cert["route_evaluation"]

    checks = {
        "R0_previous_next_matches_q79_routec_source_target": previous["verdict"][
            "next_required_artifact"
        ]
        == "Q79_RouteC_Selected_Source_Certificate_or_Typed_DE_Construction_v1",
        "R1_q79_candidate_and_certificate_match": q79_candidate == q79_cert,
        "R2_q79_status_is_witness_contract_created": q79_cert["status"] == Q79_STATUS,
        "R3_witness_reduction_theorem_proved_without_closure": q79_cert["theorem"][
            "proved"
        ]
        is True
        and q79_cert["theorem"]["closure_claimed"] is False
        and q79_cert["closure_claimed"] is False,
        "R4_honest_selected_source_attempt_fails": honest["validator_exit_code"] == 1
        and honest["selected_hym_operator_source_verified"] is False,
        "R5_hypothetical_selected_flags_packet_is_diagnostic_only": diagnostic[
            "validator_exit_code"
        ]
        == 0
        and diagnostic["diagnostic_not_proof"] is True,
        "R6_routes_are_classified": routes["route_A_selected_routec_source_certificate"][
            "status"
        ]
        == "BLOCKED_CURRENT_HONEST_PACKET_FAILS"
        and routes["route_B_typed_monad_cech_de_construction"]["status"] == "BLOCKED"
        and routes["route_C_direct_HYM_connection"]["status"]
        == "ABSTRACT_EXISTENCE_ONLY",
        "R7_contracts_are_created": witness["schema"]
        == "Q79SelectedConnectionWitnessContract.v1"
        and typed["schema"] == "Q79TypedDEWitnessContract.v1"
        and closes["selected_connection_witness_contract_created"] is True
        and closes["typed_de_witness_contract_created"] is True,
        "R8_remaining_open_items_are_not_overclaimed": remains[
            "selected_connection_witness_values"
        ]
        is True
        and remains["selected_visible_sm_bundle_model"] is True
        and remains["honest_selected_DE_Riesz_Green_dotD_packets"] is True
        and remains["selected_C1_response_matrices"] is True
        and remains["full_SM_or_no_knob_closure"] is True,
        "R9_next_artifact_is_typed_monad_cech_or_hym_witness": q79_cert[
            "next_required_artifact"
        ]
        == NEXT,
        "R10_guardrails_all_negative": all(
            value is False for value in q79_cert["guardrails"].values()
        ),
    }
    proved = all(checks.values())

    return {
        "packet": "Q79_RouteC_Selected_Source_Witness_Reduction_Import_v1",
        "status": STATUS if proved else "Q79_ROUTEC_SELECTED_SOURCE_WITNESS_REDUCTION_IMPORT_FAILED",
        "inputs": {
            "previous": str(PREVIOUS.relative_to(ROOT)),
            "q79_certificate": q79_rel(Q79_CERT),
            "q79_candidate": q79_rel(Q79_CANDIDATE),
            "q79_selected_connection_witness_contract": q79_rel(Q79_WITNESS),
            "q79_typed_de_witness_contract": q79_rel(Q79_TYPED),
        },
        "import_checks": checks,
        "theorem": {
            "name": "Q79RouteCSelectedSourceWitnessReductionImport",
            "proved": proved,
            "closure_claimed": False,
            "statement": (
                "The exact q79 Route-C selected-source/typed-D_E target is now "
                "imported as a witness-reduction theorem. It proves that the "
                "honest current selected-source packet fails, a selected-flags "
                "packet passes only diagnostically, all current routes are "
                "classified, and the remaining proof object is precisely a "
                "typed monad/Cech D_E witness or selected HYM/Route-C connection "
                "with residual bounds."
            ),
        },
        "q79_status": q79_cert["status"],
        "route_evaluation": routes,
        "honest_routec_selected_source_attempt": {
            "packet": honest["packet"],
            "validator_exit_code": honest["validator_exit_code"],
            "selected_hym_operator_source_verified": honest[
                "selected_hym_operator_source_verified"
            ],
        },
        "hypothetical_selected_source_diagnostic": {
            "packet": diagnostic["packet"],
            "validator_exit_code": diagnostic["validator_exit_code"],
            "diagnostic_not_proof": diagnostic["diagnostic_not_proof"],
            "interpretation": diagnostic["interpretation"],
        },
        "selected_connection_witness_contract": {
            "path": q79_rel(Q79_WITNESS),
            "schema": witness["schema"],
            "status": witness["status"],
            "accepted_witness_routes": sorted(witness["accepted_witness_routes"]),
            "forbidden_shortcuts": witness["forbidden_shortcuts"],
        },
        "typed_de_witness_contract": {
            "path": q79_rel(Q79_TYPED),
            "schema": typed["schema"],
            "status": typed["status"],
            "currently_computable": typed["currently_computable"],
            "one_of_count": len(typed["one_of"]),
            "validator_targets_after_witness": typed["validator_targets_after_witness"],
        },
        "what_closes_now": closes,
        "what_remains_open": remains,
        "guardrails": q79_cert["guardrails"],
        "verdict": {
            "what_closes_now": (
                "The target is no longer a broad source-search decision. The "
                "exact q79 witness-reduction theorem is imported: current honest "
                "packets do not close, diagnostic plumbing works, and witness "
                "contracts are explicit."
            ),
            "what_remains": (
                "Supply the typed monad/Cech D_E data or a selected HYM/Route-C "
                "connection witness with residual bounds, then emit honest "
                "D_E/Riesz/Green/dotD and C1 response matrices."
            ),
            "next_required_artifact": NEXT,
        },
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "Q79RouteCSelectedSourceWitnessReductionImport",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "import_checks": packet["import_checks"],
        "route_evaluation": packet["route_evaluation"],
        "selected_connection_witness_contract": packet[
            "selected_connection_witness_contract"
        ],
        "typed_de_witness_contract": packet["typed_de_witness_contract"],
        "what_remains_open": packet["what_remains_open"],
        "guardrails": packet["guardrails"],
        "verdict": packet["verdict"],
    }


def render_note(cert: dict[str, Any], packet: dict[str, Any]) -> str:
    return f"""# Q79 Route-C Selected Source Witness Reduction Import v1

## Result

Status: `{cert["status"]}`

The exact q79 artifact
`Q79_RouteC_Selected_Source_Certificate_or_Typed_DE_Construction_v1` is now
imported.  It does not close full SM/no-knob arithmetic.  It sharply reduces the
remaining proof target to one selected connection witness: either typed
monad/Cech `D_E` data or a selected HYM/Route-C connection with residual bounds.

## Import Checks

```json
{json.dumps(packet["import_checks"], indent=2, sort_keys=True)}
```

## Route Evaluation

```json
{json.dumps(packet["route_evaluation"], indent=2, sort_keys=True)}
```

## Witness Contracts

```json
{json.dumps(packet["selected_connection_witness_contract"], indent=2, sort_keys=True)}
```

```json
{json.dumps(packet["typed_de_witness_contract"], indent=2, sort_keys=True)}
```

## Remaining Frontier

```json
{json.dumps(packet["what_remains_open"], indent=2, sort_keys=True)}
```

Next required artifact: `{packet["verdict"]["next_required_artifact"]}`.
"""


def main() -> int:
    packet = build_packet()
    cert = build_certificate(packet)
    if "--write" in sys.argv:
        OUTPUT_PACKET.write_text(
            json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        OUTPUT_CERT.write_text(
            json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        OUTPUT_NOTE.write_text(render_note(cert, packet), encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
