"""Import Route-C R1 source or R4 B_N basis fill attempt."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SM = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure")

PREVIOUS = CERTS / "phifin_or_bn_emission_contracts_import_certificate.json"
UPSTREAM_PACKET = SM / "candidate_data" / "selected_routec_r1_source_or_r4_bn_basis_fill.candidate.json"
UPSTREAM_CERT = SM / "certificates" / "selected_routec_r1_source_or_r4_bn_basis_fill_certificate.json"

OUTPUT_PACKET = DATA / "routec_r1_r4_fill_attempt_import.candidate.json"
OUTPUT_CERT = CERTS / "routec_r1_r4_fill_attempt_import_certificate.json"
OUTPUT_NOTE = CORPUS / "RouteC_R1_R4_FillAttempt_Import_v1.md"

STATUS = "ROUTEC_R1_R4_FILL_ATTEMPT_IMPORTED_PRIMITIVE_SEARCH_OPEN"
PREVIOUS_STATUS = "PHIFIN_OR_BN_EMISSION_CONTRACTS_IMPORTED_R1_OR_R4_OPEN"
UPSTREAM_STATUS = "MTT_SELECTED_ROUTEC_R1_R4_FILL_ATTEMPT_BLOCKED_BY_UNEMITTED_SELECTED_PRIMITIVES"
NEXT = "MTT_Selected_RouteC_Selected_Primitive_Emission_Search_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    upstream = load(UPSTREAM_PACKET)
    upstream_cert = load(UPSTREAM_CERT)
    r1 = upstream["R1_source_certificate_attempt"]
    r4 = upstream["R4_BN_basis_attempt"]

    checks = {
        "F0_previous_import_matches": previous["status"] == PREVIOUS_STATUS
        and previous["next_required_artifact"] == "MTT_Selected_RouteC_R1_Source_Certificate_or_R4_BN_Basis_Fill_v1",
        "F1_upstream_fill_attempt_proved": upstream["status"] == UPSTREAM_STATUS
        and upstream["theorem"]["proved"] is True
        and upstream["closure_claimed"] is False
        and upstream["target_fitting_used"] is False
        and upstream["next_required_artifact"] == NEXT,
        "F2_certificate_agrees": upstream_cert["status"] == UPSTREAM_STATUS
        and upstream_cert["closure_claimed"] is False
        and upstream_cert["target_fitting_used"] is False
        and upstream_cert["primary_next_artifact"] == NEXT,
        "F3_R1_attempt_strictly_blocked": r1["closed"] is False
        and r1["fillable_from_current_artifacts"]["strominger_selection_support"] is True
        and r1["blocking_missing_fields"]["Phi_fin_selected_values"] is True
        and r1["blocking_missing_fields"]["selected_minimizer_identifier"] is True,
        "F4_R4_attempt_strictly_blocked": r4["closed"] is False
        and r4["fillable_from_current_artifacts"]["candidate_deck_generators"] is True
        and r4["blocking_missing_fields"]["scalar_basis_functions_phi_m"] is True
        and r4["blocking_missing_fields"]["selected_D_E_action_on_basis"] is True,
        "F5_R6_replay_not_ready": upstream["R6_honest_replay"]["ready"] is False
        and upstream["what_remains_open"]["R6_replay_without_lifted_flags"] is True,
        "F6_support_not_values": upstream["what_closes_now"]["R1_support_fields_collected"] is True
        and upstream["what_closes_now"]["R4_support_fields_collected"] is True
        and upstream["what_closes_now"]["unemitted_selected_primitives_identified"] is True,
        "F7_no_overclaim": upstream_cert["R1_closed"] is False
        and upstream_cert["R4_closed"] is False
        and upstream_cert["R6_ready"] is False
        and upstream_cert["closure_claimed"] is False,
    }

    return {
        "packet": "RouteC_R1_R4_FillAttempt_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous_local_import": str(PREVIOUS.relative_to(ROOT)),
            "upstream_candidate": str(UPSTREAM_PACKET),
            "upstream_certificate": str(UPSTREAM_CERT),
        },
        "theorem": {
            "name": "RouteCR1R4FillAttemptImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "The R1 selected source certificate and R4 quotient/deck-valid "
                "B_N basis fill were both attempted strictly.  Both support "
                "stacks are usable, but neither emits selected values; honest "
                "replay remains blocked.  The next legal object is selected "
                "primitive emission search."
            ),
        },
        "checks": checks,
        "upstream_fill_attempt": upstream,
        "what_closes_now": upstream["what_closes_now"],
        "what_remains_open": upstream["what_remains_open"],
        "guardrails": {
            "claims_R1_closed": False,
            "claims_R4_closed": False,
            "claims_R6_ready": False,
            "claims_selected_Phi_fin_values": False,
            "claims_selected_minimizer_identifier": False,
            "claims_scalar_basis_functions_phi_m": False,
            "claims_selected_DE_action_on_basis": False,
            "claims_full_SM_or_no_knob_closure": False,
            "uses_observed_or_benchmark_inputs": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": NEXT,
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "RouteCR1R4FillAttemptImport",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "what_closes_now": packet["what_closes_now"],
        "what_remains_open": packet["what_remains_open"],
        "guardrails": packet["guardrails"],
        "next_required_artifact": packet["next_required_artifact"],
    }


def render_note(cert: dict[str, Any]) -> str:
    return f"""# RouteC R1 R4 FillAttempt Import v1

Status: `{cert["status"]}`.

The R1 and R4 fills were attempted strictly:

- R1 source-certificate support is present, but selected `Phi_fin` values,
  selected minimizer identity, and selected HYM/operator source values are not
  emitted.
- R4 basis support is present, but selected scalar basis functions, deck/cover,
  bundle equivariance, quadrature, and selected `D_E` action are not emitted.

Honest replay remains blocked.  The next move is selected primitive emission
search, not a replay or lifted-flag promotion.

Next artifact: `{cert["next_required_artifact"]}`.
"""


def main() -> int:
    packet = build_packet()
    cert = build_certificate(packet)
    if "--write" in sys.argv:
        OUTPUT_PACKET.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(render_note(cert), encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
