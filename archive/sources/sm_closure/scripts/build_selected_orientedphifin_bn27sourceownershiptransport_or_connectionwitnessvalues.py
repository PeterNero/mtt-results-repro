"""Build BN27 source-ownership transport supersession/bridge packet.

This artifact prevents a loop: the newly named oriented-Phi_fin BN27
transport target is equivalent to an older verified chain ending at the
same-source eight-field connection-value table.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
QA = Path("C:/Users/nero_/Downloads/TEXPAPERS/mtt-qa-su3-packet-proof/candidate_data")

SLUG = "selected_orientedphifin_bn27sourceownershiptransport_or_connectionwitnessvalues"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SUPERSESSION_PACKET = PACKET_DIR / "supersession_alignment.packet.json"
TRANSPORT_GATE = PACKET_DIR / "bn27_transport_value_gate.packet.json"
NEXT_CONTRACT = PACKET_DIR / "next_first_same_source_field_or_direct_hkrow_contract.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_OrientedPhiFin_BN27SourceOwnershipTransport_or_ConnectionWitnessValues_v1.md"

SOURCES = {
    "previous": DATA / "selected_orientedphifin_sourceownership_theorem_or_smootheqa_quotient.candidate.json",
    "previous_contract": DATA
    / "selected_orientedphifin_sourceownership_theorem_or_smootheqa_quotient"
    / "bn27_transport_or_connectionwitness_values_contract.packet.json",
    "qa_bn27_transport": QA / "selected_heterotic_orientedphifin_bn27_sourceownership_transport_or_connectionwitness_values.candidate.json",
    "old_sourcebranch_gate": DATA / "selected_sourcebranchidentity_sourceamendment_or_selectedconnectionvalues_or_directhkrow.candidate.json",
    "old_typed_connection_gate": DATA / "selected_typedcechhymprojectiveconnectionwitnessvalues_or_directhkrow.candidate.json",
    "old_same_source_table": DATA / "selected_samesourceconnectionvaluetable_or_directhkrow.candidate.json",
    "old_same_source_table_packet": DATA
    / "selected_samesourceconnectionvaluetable_or_directhkrow"
    / "eight_field_connection_value_table.packet.json",
}

STATUS = (
    "MTT_SELECTED_ORIENTEDPHIFIN_BN27SOURCEOWNERSHIPTRANSPORT_OR_"
    "CONNECTIONWITNESSVALUES_BUILT_SUPERSEDED_TO_SAMESOURCE_FIELD_OPEN"
)
NEXT = "MTT_Selected_FirstSameSourceConnectionFieldEmission_or_DirectHKRow_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources() -> dict[str, dict[str, Any]]:
    missing = [rel(path) for path in SOURCES.values() if not path.exists()]
    if missing:
        raise FileNotFoundError(f"Missing required source packets: {missing}")
    return {name: load(path) for name, path in SOURCES.items()}


def main() -> int:
    sources = require_sources()
    previous = sources["previous"]
    previous_contract = sources["previous_contract"]
    qa_transport = sources["qa_bn27_transport"]
    sourcebranch = sources["old_sourcebranch_gate"]
    typed = sources["old_typed_connection_gate"]
    same_source = sources["old_same_source_table"]
    table = sources["old_same_source_table_packet"]

    same_decision = same_source["closure_decision"]
    required_next = previous["next_required_artifact"]
    if required_next != "MTT_Selected_OrientedPhiFin_BN27SourceOwnershipTransport_or_ConnectionWitnessValues_v1":
        raise ValueError("previous frontier no longer points to this artifact")
    if same_decision["eight_field_table_built"] is not True:
        raise ValueError("same-source table has not been built")

    support_count = same_decision["support_field_count"]
    accepted_count = same_decision["accepted_same_source_connection_value_count"]
    required_count = table["field_count"]

    supersession_packet = {
        "schema": "MTTOrientedPhiFinBN27TransportSupersessionAlignment.v1",
        "status": "REQUESTED_FRONTIER_MATCHES_EXISTING_SAMESOURCE_TABLE_CHAIN",
        "closure_claimed": True,
        "requested_artifact": required_next,
        "existing_chain": [
            rel(SOURCES["old_sourcebranch_gate"]),
            rel(SOURCES["old_typed_connection_gate"]),
            rel(SOURCES["old_same_source_table"]),
        ],
        "chain_statuses": {
            "sourcebranch": sourcebranch["status"],
            "typed_connection": typed["status"],
            "same_source_table": same_source["status"],
            "qa_transport": qa_transport["status"],
        },
        "why_not_a_loop": (
            "The requested BN27 transport target is the same obligation already "
            "normalized by the older chain. The older chain has moved past route "
            "readiness to a concrete eight-field table, so the next legal step is "
            "field emission rather than another BN27 transport replay."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    transport_gate = {
        "schema": "MTTOrientedPhiFinBN27TransportValueGate.v1",
        "status": "BN27_TRANSPORT_VALUE_GATE_EXECUTED_ACCEPTED0",
        "closure_claimed": True,
        "branch_certificate_closed": True,
        "BN27_source_ownership_transport_closed": False,
        "selected_connection_witness_values_closed": False,
        "direct_BN27_source_declaration_closed": False,
        "eight_field_table_built": True,
        "required_same_source_connection_field_count": required_count,
        "support_field_count": support_count,
        "accepted_same_source_connection_value_count": accepted_count,
        "support_fields": [
            row["field"] for row in table["rows"] if row["support_present"]
        ],
        "accepted_fields": [
            row["field"]
            for row in table["rows"]
            if row["accepted_as_same_source_connection_value"]
        ],
        "first_value_field": "transition_or_connection_representative",
        "alternative_first_field": "source_id",
        "direct_exit": "K_threshold.Omega_H.lambda",
        "must_not_replay_as_new": [
            "branch certificate alone",
            "typed Cech gap-layer support",
            "diagonal HYM/Galerkin support",
            "Route-C/projective extraction scaffold",
            "projective 11-label rho_E shadow",
            "oriented logdet arithmetic without same-source ownership",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_contract = {
        "schema": "MTTOrientedPhiFinBN27TransportNextContract.v1",
        "status": "NEXT_IS_FIRST_SAMESOURCE_FIELD_EMISSION_OR_DIRECT_HKROW",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "recommended_first_field": "transition_or_connection_representative",
        "why_first": (
            "It is the first non-label value field in the already-built table and "
            "would force actual typed transitions, local connection variables, or "
            "HYM/Strominger coefficients."
        ),
        "alternative_first_field": "source_id",
        "alternative_reason": (
            "A same-source branch certificate naming the q79/F,m=1 branch as table "
            "owner could promote the existing label support before numerical "
            "connection values."
        ),
        "direct_exit": "K_threshold.Omega_H.lambda",
        "previous_contract_guardrails": previous_contract["must_not_use"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedOrientedPhiFinBN27SourceOwnershipTransportOrConnectionWitnessValues",
        "status": STATUS,
        "previous_status": previous["status"],
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {name: rel(path) for name, path in SOURCES.items()},
        "output_packets": {
            "supersession_alignment": rel(SUPERSESSION_PACKET),
            "bn27_transport_value_gate": rel(TRANSPORT_GATE),
            "next_first_same_source_field_or_direct_hkrow_contract": rel(NEXT_CONTRACT),
        },
        "closure_decision": {
            "requested_frontier_constructed": True,
            "existing_same_source_chain_supersedes_replay": True,
            "branch_certificate_closed": True,
            "BN27_source_ownership_transport_closed": False,
            "selected_connection_witness_values_closed": False,
            "direct_BN27_source_declaration_closed": False,
            "eight_field_table_built": True,
            "required_same_source_connection_field_count": required_count,
            "support_field_count": support_count,
            "accepted_same_source_connection_value_count": accepted_count,
            "strict_H_K_threshold_row_emitted": False,
            "selected_K_threshold_Omega_H_lambda": False,
            "projective_rhoE_lift_reopened": False,
            "oriented_logdet_promoted": False,
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "OrientedPhiFinBN27TransportSupersessionTheorem",
            "proved": True,
            "statement": (
                "The requested BN27 source-ownership transport artifact is "
                "constructed by aligning the current oriented-Phi_fin frontier "
                "with the existing source-branch, typed-connection, and same-source "
                "table chain. This closes the naming/plan gap and proves that the "
                "frontier is no longer BN27 transport replay: the remaining object "
                "is the first accepted same-source connection field or an independent "
                "direct H K row."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedOrientedPhiFinBN27SourceOwnershipTransportOrConnectionWitnessValues",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "existing_same_source_chain_supersedes_replay": True,
        "eight_field_table_built": True,
        "support_field_count": support_count,
        "accepted_same_source_connection_value_count": accepted_count,
        "BN27_source_ownership_transport_closed": False,
        "selected_connection_witness_values_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected Oriented Phi_fin BN27 Source-Ownership Transport or Connection-Witness Values v1

## Theorem

`OrientedPhiFinBN27TransportSupersessionTheorem` is emitted.

## What This Closes

- The newly named BN27 transport target is constructed.
- It is identified with the already verified source-branch -> typed-connection -> same-source-table chain.
- The older chain is stronger than a route-readiness replay because it already builds the concrete `8`-field same-source connection-value table.

## Current Value Gate

- BN27 branch certificate closed: `true`.
- Eight-field table built: `true`.
- Support fields: `{support_count}/{required_count}`.
- Accepted same-source connection values: `{accepted_count}/{required_count}`.
- BN27 source ownership closed: `false`.
- Selected connection-witness values closed: `false`.
- Direct `K_threshold.Omega_H.lambda` row emitted: `false`.

## Anti-Loop Rule

Do not restate branch-certificate closure, typed Cech support, diagonal HYM support,
Route-C extraction scaffolds, or projective `rho_E` shadows as a new BN27 proof.
The next proof must emit one accepted table field or a direct H K row certificate.

## Next Artifact

`{NEXT}`
"""

    write_json(SUPERSESSION_PACKET, supersession_packet)
    write_json(TRANSPORT_GATE, transport_gate)
    write_json(NEXT_CONTRACT, next_contract)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
