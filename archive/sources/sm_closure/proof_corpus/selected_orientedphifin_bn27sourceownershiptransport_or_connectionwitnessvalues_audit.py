"""Audit oriented Phi_fin BN27 transport bridge/supersession theorem."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
BUILDER = ROOT / "scripts" / "build_selected_orientedphifin_bn27sourceownershiptransport_or_connectionwitnessvalues.py"

SLUG = "selected_orientedphifin_bn27sourceownershiptransport_or_connectionwitnessvalues"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_OrientedPhiFin_BN27SourceOwnershipTransport_or_ConnectionWitnessValues_v1.md"
SUPERSESSION = PACKET_DIR / "supersession_alignment.packet.json"
TRANSPORT_GATE = PACKET_DIR / "bn27_transport_value_gate.packet.json"
NEXT_CONTRACT = PACKET_DIR / "next_first_same_source_field_or_direct_hkrow_contract.packet.json"

STATUS = (
    "MTT_SELECTED_ORIENTEDPHIFIN_BN27SOURCEOWNERSHIPTRANSPORT_OR_"
    "CONNECTIONWITNESSVALUES_BUILT_SUPERSEDED_TO_SAMESOURCE_FIELD_OPEN"
)
NEXT = "MTT_Selected_FirstSameSourceConnectionFieldEmission_or_DirectHKRow_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    supersession = load(SUPERSESSION)
    transport = load(TRANSPORT_GATE)
    next_contract = load(NEXT_CONTRACT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(next_contract["next_required_artifact"] == NEXT, "next contract mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem flag missing")

    for payload in [candidate, cert, supersession, transport, next_contract]:
        require(payload["closure_claimed"] is True, "closure boundary missing")
        require(payload["observed_data_used_as_selector"] is False, "observed selector used")
        require(payload["target_fitting_used"] is False, "target fitting used")

    decision = candidate["closure_decision"]
    require(decision["requested_frontier_constructed"] is True, "requested frontier not constructed")
    require(
        decision["existing_same_source_chain_supersedes_replay"] is True,
        "existing chain not used as supersession",
    )
    require(decision["branch_certificate_closed"] is True, "branch certificate lost")
    require(decision["eight_field_table_built"] is True, "eight-field table missing")
    require(decision["required_same_source_connection_field_count"] == 8, "field count mismatch")
    require(decision["support_field_count"] == 2, "support field count mismatch")
    require(decision["accepted_same_source_connection_value_count"] == 0, "accepted values overcounted")
    for key in [
        "BN27_source_ownership_transport_closed",
        "selected_connection_witness_values_closed",
        "direct_BN27_source_declaration_closed",
        "strict_H_K_threshold_row_emitted",
        "selected_K_threshold_Omega_H_lambda",
        "projective_rhoE_lift_reopened",
        "oriented_logdet_promoted",
        "full_no_knob_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"overclosed: {key}")

    require(
        supersession["status"] == "REQUESTED_FRONTIER_MATCHES_EXISTING_SAMESOURCE_TABLE_CHAIN",
        "supersession status mismatch",
    )
    require(len(supersession["existing_chain"]) == 3, "existing chain length mismatch")
    require("same_source_table" in supersession["chain_statuses"], "same-source status missing")
    require("field emission" in supersession["why_not_a_loop"], "anti-loop explanation missing")

    require(
        transport["status"] == "BN27_TRANSPORT_VALUE_GATE_EXECUTED_ACCEPTED0",
        "transport status mismatch",
    )
    require(transport["branch_certificate_closed"] is True, "transport branch cert lost")
    require(transport["eight_field_table_built"] is True, "transport table missing")
    require(transport["required_same_source_connection_field_count"] == 8, "transport field count mismatch")
    require(transport["support_field_count"] == 2, "transport support count mismatch")
    require(transport["accepted_same_source_connection_value_count"] == 0, "transport accepted count mismatch")
    require(transport["support_fields"] == ["source_id", "carrier_or_cover_id"], "support fields mismatch")
    require(transport["accepted_fields"] == [], "accepted fields should be empty")
    require(transport["first_value_field"] == "transition_or_connection_representative", "first field mismatch")
    for shortcut in [
        "branch certificate alone",
        "typed Cech gap-layer support",
        "Route-C/projective extraction scaffold",
        "projective 11-label rho_E shadow",
    ]:
        require(shortcut in transport["must_not_replay_as_new"], f"missing guard: {shortcut}")

    require(
        next_contract["status"] == "NEXT_IS_FIRST_SAMESOURCE_FIELD_EMISSION_OR_DIRECT_HKROW",
        "next contract status mismatch",
    )
    require(
        next_contract["recommended_first_field"] == "transition_or_connection_representative",
        "recommended first field mismatch",
    )
    require(next_contract["alternative_first_field"] == "source_id", "alternative field mismatch")
    require(next_contract["direct_exit"] == "K_threshold.Omega_H.lambda", "direct exit mismatch")

    require("Accepted same-source connection values: `0/8`" in note, "note missing accepted count")
    require("Anti-Loop Rule" in note, "note missing anti-loop rule")
    require(NEXT in note, "note missing next artifact")

    print("Oriented Phi_fin BN27 transport bridge audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
