"""Import selected Route-C provenance-or-basis support certificate."""

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

PREVIOUS = CERTS / "routec_source_selector_basis_cutset_import_certificate.json"
UPSTREAM_PACKET = SM / "candidate_data" / "selected_routec_source_provenance_or_basis_certificate.candidate.json"
UPSTREAM_CERT = SM / "certificates" / "selected_routec_source_provenance_or_basis_certificate_certificate.json"

OUTPUT_PACKET = DATA / "routec_provenance_or_basis_support_import.candidate.json"
OUTPUT_CERT = CERTS / "routec_provenance_or_basis_support_import_certificate.json"
OUTPUT_NOTE = CORPUS / "RouteC_Provenance_or_Basis_Support_Import_v1.md"

STATUS = "ROUTEC_PROVENANCE_OR_BASIS_SUPPORT_IMPORTED_PRIMITIVE_EMISSION_OPEN"
PREVIOUS_STATUS = "ROUTEC_SOURCE_SELECTOR_BASIS_CUTSET_IMPORTED_PROVENANCE_OR_BASIS_OPEN"
UPSTREAM_STATUS = "MTT_SELECTED_ROUTEC_PROVENANCE_AND_BASIS_ATTEMPT_SUPPORT_CLOSED_PRIMITIVES_OPEN"
NEXT = "MTT_Selected_PhiFin_Payload_or_BN_Basis_Emission_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    upstream = load(UPSTREAM_PACKET)
    upstream_cert = load(UPSTREAM_CERT)
    calc = upstream["calculation"]
    provenance = upstream["provenance_gate"]
    basis = upstream["basis_gate"]

    checks = {
        "F0_previous_import_matches": previous["status"] == PREVIOUS_STATUS
        and previous["next_required_artifact"] == "MTT_Selected_RouteC_Source_Provenance_or_Basis_Certificate_v1",
        "F1_upstream_support_theorem_proved": upstream["status"] == UPSTREAM_STATUS
        and upstream["theorem"]["proved"] is True
        and upstream["closure_claimed"] is False
        and upstream["target_fitting_used"] is False
        and upstream["next_required_artifact"] == NEXT,
        "F2_certificate_agrees": upstream_cert["status"] == UPSTREAM_STATUS
        and upstream_cert["closure_claimed"] is False
        and upstream_cert["target_fitting_used"] is False
        and upstream_cert["primary_next_artifact"] == NEXT,
        "F3_support_stacks_closed": calc["support_closed"]["provenance_support_closed"] is True
        and calc["support_closed"]["basis_support_closed"] is True
        and upstream_cert["support_closed"]["provenance_support_closed"] is True
        and upstream_cert["support_closed"]["basis_support_closed"] is True,
        "F4_full_gates_remain_open": calc["any_gate_closed"] is False
        and calc["both_gates_closed"] is False
        and upstream_cert["provenance_closed"] is False
        and upstream_cert["basis_closed"] is False,
        "F5_minimal_primitives_identified": provenance["minimal_missing_primitive"] == "Phi_fin_selected_payload"
        and basis["minimal_missing_primitive"] == "quotient_valid_B_N_basis_certificate",
        "F6_no_hidden_shape_obstruction": calc["newly_locked"]["provenance_is_not_blocked_by_downstream_algebra"] is True
        and calc["newly_locked"]["basis_is_not_blocked_by_dimension_or_projector_shape"] is True
        and upstream["what_closes_now"]["no_hidden_matrix_or_dimension_obstruction"] is True,
        "F7_open_items_preserved": upstream["what_remains_open"]["Phi_fin_selected_payload"] is True
        and upstream["what_remains_open"]["quotient_valid_BN_basis_certificate"] is True
        and upstream["what_remains_open"]["honest_manifest_without_lifted_flags"] is True,
        "F8_no_overclaim": upstream["what_remains_open"]["full_SM_or_no_knob_closure"] is True
        and upstream_cert["closure_claimed"] is False,
    }

    return {
        "packet": "RouteC_Provenance_or_Basis_Support_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous_local_import": str(PREVIOUS.relative_to(ROOT)),
            "upstream_candidate": str(UPSTREAM_PACKET),
            "upstream_certificate": str(UPSTREAM_CERT),
        },
        "theorem": {
            "name": "RouteCProvenanceOrBasisSupportImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "The selected Route-C provenance and basis support stacks are "
                "both closed as support, but neither proof gate promotes.  The "
                "minimal missing primitives are selected Phi_fin payload emission "
                "or a quotient/deck-valid B_N basis certificate, followed by "
                "honest replay without lifted flags."
            ),
        },
        "checks": checks,
        "upstream_support": upstream,
        "what_closes_now": upstream["what_closes_now"],
        "what_remains_open": upstream["what_remains_open"],
        "guardrails": {
            "claims_provenance_gate_closed": False,
            "claims_basis_gate_closed": False,
            "claims_selected_Phi_fin_payload": False,
            "claims_quotient_valid_BN_basis_certificate": False,
            "claims_honest_manifest_without_lifted_flags": False,
            "claims_selected_source_flags_promoted": False,
            "claims_full_SM_or_no_knob_closure": False,
            "uses_observed_or_benchmark_inputs": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": NEXT,
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "RouteCProvenanceOrBasisSupportImport",
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
    return f"""# RouteC Provenance or Basis Support Import v1

Status: `{cert["status"]}`.

Both remaining Route-C exits have now been tested as far as current artifacts
allow:

- provenance support stack closed, but the selected `Phi_fin` payload is missing
- basis support stack closed, but the quotient/deck-valid `B_N` certificate is
  missing

This means the next work is primitive emission, not another broad matrix search.
The honest manifest still cannot be replayed without lifted flags.

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
