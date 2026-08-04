"""Import selected Route-C primitive emission search."""

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

PREVIOUS = CERTS / "routec_r1_r4_fill_attempt_import_certificate.json"
UPSTREAM_PACKET = SM / "candidate_data" / "selected_routec_selected_primitive_emission_search.candidate.json"
UPSTREAM_CERT = SM / "certificates" / "selected_routec_selected_primitive_emission_search_certificate.json"

OUTPUT_PACKET = DATA / "routec_selected_primitive_emission_search_import.candidate.json"
OUTPUT_CERT = CERTS / "routec_selected_primitive_emission_search_import_certificate.json"
OUTPUT_NOTE = CORPUS / "RouteC_SelectedPrimitiveEmissionSearch_Import_v1.md"

STATUS = "ROUTEC_SELECTED_PRIMITIVE_SEARCH_IMPORTED_NONIDENTITY_RHOE_BN_OPEN"
PREVIOUS_STATUS = "ROUTEC_R1_R4_FILL_ATTEMPT_IMPORTED_PRIMITIVE_SEARCH_OPEN"
UPSTREAM_STATUS = "MTT_SELECTED_ROUTEC_PRIMITIVE_EMISSION_SEARCH_EXECUTED_NO_LEGAL_EMISSION_FOUND"
NEXT = "MTT_Selected_RouteC_NonIdentity_RhoE_and_BN_Construction_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    upstream = load(UPSTREAM_PACKET)
    upstream_cert = load(UPSTREAM_CERT)
    results = upstream["search_results"]
    straight = upstream["superset_mode"]["straight_path"]

    checks = {
        "F0_previous_import_matches": previous["status"] == PREVIOUS_STATUS
        and previous["next_required_artifact"] == "MTT_Selected_RouteC_Selected_Primitive_Emission_Search_v1",
        "F1_upstream_search_proved": upstream["status"] == UPSTREAM_STATUS
        and upstream["theorem"]["proved"] is True
        and upstream["closure_claimed"] is False
        and upstream["target_fitting_used"] is False
        and upstream["next_required_artifact"] == NEXT,
        "F2_certificate_agrees": upstream_cert["status"] == UPSTREAM_STATUS
        and upstream_cert["candidate_path"].endswith("selected_routec_selected_primitive_emission_search.candidate.json"),
        "F3_phifin_not_emitted": results["Phi_fin_payload"]["selected_values_emitted"] is False
        and results["Phi_fin_payload"]["minimum_payload_fields_still_null"] is True
        and results["Phi_fin_payload"]["selected_by_mtt"] is False,
        "F4_identity_rhoE_rejected": results["Phi_fin_payload"]["identity_smoke_rejected"] is True
        and results["Phi_fin_payload"]["candidate_kind"] == "identity_rhoE_smoke_unselected",
        "F5_bn_not_emitted": results["B_N_basis"]["minimum_basis_payload_fields_still_null"] is True
        and results["B_N_basis"]["required_success_gates_pass"] is False
        and results["B_N_basis"]["selected_source_verified"] is False,
        "F6_deck_scaffold_partial": results["B_N_basis"]["selected_deck_map_present"] is True
        and results["B_N_basis"]["selected_deck_rank_over_F3"] == 2
        and results["B_N_basis"]["selected_deck_is_partial_execution_scaffold"] is True,
        "F7_formal_lift_rejected": results["formal_lift_diagnostic"]["can_validate_downstream_algebra"] is True
        and results["formal_lift_diagnostic"]["promotion_allowed"] is False
        and results["formal_lift_diagnostic"]["claims_physical_selected_source"] is False,
        "F8_straight_path_blocked": straight["R1_promotes"] is False
        and straight["R4_promotes"] is False
        and straight["R6_ready"] is False,
        "F9_no_overclaim": upstream_cert["what_remains_open"]["full_SM_or_no_knob_closure"] is True
        and upstream["what_closes_now"]["primitive_search_executed"] is True,
    }

    return {
        "packet": "RouteC_SelectedPrimitiveEmissionSearch_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous_local_import": str(PREVIOUS.relative_to(ROOT)),
            "upstream_candidate": str(UPSTREAM_PACKET),
            "upstream_certificate": str(UPSTREAM_CERT),
        },
        "theorem": {
            "name": "RouteCSelectedPrimitiveEmissionSearchImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "The strict selected primitive search found no legal selected "
                "Phi_fin payload and no quotient-valid B_N basis payload in "
                "existing artifacts.  Identity rho_E smoke and formal lifted "
                "flags are rejected as proof sources.  The next construction is "
                "selected non-identity projective/twisted rho_E plus quotient-"
                "valid non-invariant Galerkin B_N from the same q79/F,m=1 branch."
            ),
        },
        "checks": checks,
        "upstream_primitive_search": upstream,
        "what_closes_now": upstream["what_closes_now"],
        "what_remains_open": upstream["what_remains_open"],
        "guardrails": {
            "claims_legal_primitive_found": False,
            "claims_selected_Phi_fin_payload": False,
            "claims_quotient_valid_BN_payload": False,
            "claims_identity_rhoE_selected": False,
            "claims_formal_lift_is_proof": False,
            "claims_R1_R4_R6_closed": False,
            "claims_full_SM_or_no_knob_closure": False,
            "uses_observed_or_benchmark_inputs": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": NEXT,
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "RouteCSelectedPrimitiveEmissionSearchImport",
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
    return f"""# RouteC SelectedPrimitiveEmissionSearch Import v1

Status: `{cert["status"]}`.

The strict primitive search was executed and found no legal selected primitive
already present in the artifacts:

- selected `Phi_fin` payload values: not emitted
- quotient/deck-valid `B_N` basis payload: not emitted
- identity `rho_E` smoke: rejected as selected payload
- formal-lift algebra: diagnostic only, rejected as proof

The next construction must build selected non-identity projective/twisted
`rho_E` and quotient-valid non-invariant Galerkin `B_N` from the same q79/F,m=1
branch.

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
