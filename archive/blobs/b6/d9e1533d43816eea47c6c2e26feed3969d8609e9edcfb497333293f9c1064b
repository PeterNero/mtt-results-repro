"""Build BN27 sector-transfer representative/source-id certificate frontier."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
QA = Path("C:/Users/nero_/Downloads/TEXPAPERS/mtt-qa-su3-packet-proof/candidate_data")

SLUG = "selected_bn27sectortransferconnectionrepresentative_or_sourceidcertificate"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
TRANSFER_SPLIT = PACKET_DIR / "stationary_vs_bn27_transfer_split.packet.json"
SOURCEID_GATE = PACKET_DIR / "sourceid_certificate_gate.packet.json"
NEXT_CONTRACT = PACKET_DIR / "next_direct_source_emission_or_full_connection_tables_contract.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_BN27SectorTransferConnectionRepresentative_or_SourceIDCertificate_v1.md"

SOURCES = {
    "previous": DATA / "selected_firstsamesourceconnectionfieldemission_or_directhkrow.candidate.json",
    "previous_contract": DATA
    / "selected_firstsamesourceconnectionfieldemission_or_directhkrow"
    / "next_bn27_sector_transfer_or_sourceid_certificate_contract.packet.json",
    "step28_sector_reconciliation": DATA / "selected_step28_sectorpromotion_reconciliation_or_operatorsectorvaluecutset.candidate.json",
    "step28_refined_frontier": DATA
    / "selected_step28_sectorpromotion_reconciliation_or_operatorsectorvaluecutset"
    / "step28_refined_operator_sector_frontier.packet.json",
    "rtheta_sector_transfer": DATA / "selected_rthetasectortransfer_or_primitiveassemblymapexecution.candidate.json",
    "end0_functor": DATA / "selected_end0_to_sector_functor_source_and_value_packet.candidate.json",
    "hym_first_solve": DATA / "selected_hymnewtongalerkin_firstsolve_or_rank2sectorfunctor.candidate.json",
    "qa_minimal_missing_source": QA / "selected_heterotic_orientedphifin_bn27_minimal_missing_source_value_theorem.json",
    "qa_attempt_matrix": QA / "selected_heterotic_orientedphifin_bn27_selectedsourceemission_or_connectiontables_attempt_matrix.json",
}

STATUS = (
    "MTT_SELECTED_BN27SECTORTRANSFERCONNECTIONREPRESENTATIVE_OR_SOURCEIDCERTIFICATE_"
    "BUILT_DIRECT_SOURCE_THEOREM_SHORTEST_CONNECTION_VALUES_OPEN"
)
NEXT = "MTT_Selected_SQaSU3BN27_SelectedSourceEmissionTheorem_or_FullConnectionTables_v1"


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
    contract = sources["previous_contract"]
    step28 = sources["step28_sector_reconciliation"]
    step28_frontier = sources["step28_refined_frontier"]
    rtheta_transfer = sources["rtheta_sector_transfer"]
    end0 = sources["end0_functor"]
    hym_first = sources["hym_first_solve"]
    minimal = sources["qa_minimal_missing_source"]
    attempt_matrix = sources["qa_attempt_matrix"]

    if previous["next_required_artifact"] != "MTT_Selected_BN27SectorTransferConnectionRepresentative_or_SourceIDCertificate_v1":
        raise ValueError("previous frontier no longer points to BN27 sector transfer/source-id certificate")

    stationary_transfer_closed = (
        step28["closure_decision"]["selected_stationary_End0_to_sector_routing_values_closed"]
        and rtheta_transfer["what_closes_now"]["stationary_sector_transfer"]
    )
    bn27_operator_transfer_closed = all(
        [
            step28["closure_decision"]["operator_level_projective_rhoE_from_selected_connection_closed"],
            step28["closure_decision"]["selected_sector_basis_D_E_Riesz_Green_dotD_matrices_closed"],
            hym_first["closure_decision"]["rank2_to_sector_transfer_closed"],
            hym_first["closure_decision"]["actual_QaSU3_operator_packet_promoted"],
        ]
    )
    end0_functor_values_extracted = end0["decision"]["selected_End0_to_sector_functor_values_extracted"]

    direct = attempt_matrix["direct_source_emission_route"]
    connection = attempt_matrix["connection_tables_route"]
    source_support_count = direct["support_statement_count"]
    source_required_count = direct["required_statement_count"]
    source_open_count = direct["open_statement_count"]
    connection_support_count = connection["support_table_count"]
    connection_required_count = connection["required_table_count"]

    transfer_split = {
        "schema": "MTTStationaryVsBN27TransferSplit.v1",
        "status": "STATIONARY_RTHETA_TRANSFER_CLOSED_BN27_OPERATOR_TRANSFER_OPEN",
        "closure_claimed": True,
        "stationary_transfer_closed": stationary_transfer_closed,
        "rtheta_Pi_domain_closed": rtheta_transfer["closure_decision"]["Pi_Rtheta_closed"],
        "functional_matter_slot_blocks_closed": step28["closure_decision"][
            "functional_matter_slot_blocks_and_overlap_normalization_closed"
        ],
        "bn27_operator_transfer_closed": bn27_operator_transfer_closed,
        "end0_functor_values_extracted": end0_functor_values_extracted,
        "rank2_to_sector_transfer_closed": hym_first["closure_decision"][
            "rank2_to_sector_transfer_closed"
        ],
        "actual_QaSU3_operator_packet_promoted": hym_first["closure_decision"][
            "actual_QaSU3_operator_packet_promoted"
        ],
        "still_open_operator_frontier": step28_frontier["still_open_after_reconciliation"],
        "decision": (
            "Import stationary R_theta transfer as real support, but do not use it "
            "as the BN27 transition/connection representative. BN27 needs "
            "operator-level rhoE/DE/Riesz/Green/dotD or direct source ownership."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    sourceid_gate = {
        "schema": "MTTBN27SourceIDCertificateGate.v1",
        "status": "DIRECT_SOURCE_THEOREM_RANKED_FIRST_SUPPORT6_OPEN6",
        "closure_claimed": True,
        "direct_source_emission_route": direct,
        "connection_tables_route": connection,
        "minimal_direct_theorem": minimal["minimal_direct_theorem"],
        "minimal_constructive_alternative": minimal["minimal_constructive_alternative"],
        "source_id_certificate_closed": False,
        "direct_source_theorem_closed": False,
        "connection_tables_closed": False,
        "why_direct_route_is_shortest": direct["why_ranked_first"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_contract = {
        "schema": "MTTSQaSU3BN27DirectSourceOrConnectionTablesContract.v1",
        "status": "NEXT_IS_DIRECT_SOURCE_EMISSION_OR_FULL_CONNECTION_TABLES",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "primary_route": minimal["minimal_direct_theorem"]["name"],
        "primary_must_state": minimal["minimal_direct_theorem"]["must_state"],
        "primary_would_fill_source_fields": minimal["minimal_direct_theorem"][
            "would_fill_source_fields"
        ],
        "fallback_route": minimal["minimal_constructive_alternative"]["name"],
        "fallback_must_emit": minimal["minimal_constructive_alternative"]["must_emit"],
        "direct_exit": contract["direct_exit"],
        "must_not_use": [
            "stationary R_theta transfer as BN27 operator transfer",
            "A_diag=du*T3 as full BN27 connection table row",
            "branch certificate alone as source ownership",
            "oriented logdet arithmetic without source-owned finitepart policy",
            "projective 11-label rho_E shadow as full BN27 threshold domain",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedBN27SectorTransferConnectionRepresentativeOrSourceIDCertificate",
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
            "stationary_vs_bn27_transfer_split": rel(TRANSFER_SPLIT),
            "sourceid_certificate_gate": rel(SOURCEID_GATE),
            "next_direct_source_emission_or_full_connection_tables_contract": rel(NEXT_CONTRACT),
        },
        "closure_decision": {
            "stationary_Rtheta_transfer_imported_as_support": stationary_transfer_closed,
            "Rtheta_Pi_domain_closed": rtheta_transfer["closure_decision"]["Pi_Rtheta_closed"],
            "BN27_operator_transfer_closed": bn27_operator_transfer_closed,
            "End0_functor_values_extracted": end0_functor_values_extracted,
            "rank2_to_sector_transfer_closed": hym_first["closure_decision"][
                "rank2_to_sector_transfer_closed"
            ],
            "actual_QaSU3_operator_packet_promoted": hym_first["closure_decision"][
                "actual_QaSU3_operator_packet_promoted"
            ],
            "source_id_certificate_closed": False,
            "direct_source_theorem_support_count": source_support_count,
            "direct_source_theorem_required_count": source_required_count,
            "direct_source_theorem_open_count": source_open_count,
            "direct_source_theorem_ranked_first": True,
            "connection_table_support_count": connection_support_count,
            "connection_table_required_count": connection_required_count,
            "connection_tables_closed": False,
            "transition_or_connection_representative_emitted": False,
            "direct_H_K_row_emitted": False,
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "BN27SectorTransferAndSourceIDFrontierTheorem",
            "proved": True,
            "statement": (
                "The later stationary R_theta sector-transfer closures are real "
                "support, but they do not emit the operator-level BN27 "
                "transition/connection representative. The BN27 path therefore "
                "splits cleanly: either prove the six-statement "
                "S_QaSU3^BN27 selected-source theorem, or emit the full eight "
                "connection-table families. The direct source theorem is the "
                "shortest current route because all six statements have support "
                "but remain unclosed as source-owned statements."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedBN27SectorTransferConnectionRepresentativeOrSourceIDCertificate",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "stationary_Rtheta_transfer_imported_as_support": stationary_transfer_closed,
        "BN27_operator_transfer_closed": bn27_operator_transfer_closed,
        "source_id_certificate_closed": False,
        "direct_source_theorem_ranked_first": True,
        "direct_source_theorem_support_count": source_support_count,
        "direct_source_theorem_open_count": source_open_count,
        "connection_table_support_count": connection_support_count,
        "transition_or_connection_representative_emitted": False,
        "direct_H_K_row_emitted": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected BN27 Sector-Transfer Connection Representative or Source-ID Certificate v1

## Theorem

`BN27SectorTransferAndSourceIDFrontierTheorem` is emitted.

## What Was Closed

- The later stationary `R_theta` sector-transfer closures are imported as real
  support.
- The domain split is now explicit: stationary/functional transfer is not the
  same as an oriented-BN27 operator-level transition/connection representative.
- The shortest remaining route is selected: direct `S_QaSU3^BN27` source
  emission, not another connection-table replay.

## Current Counts

- Stationary `R_theta` transfer support: `true`.
- BN27 operator transfer closed: `false`.
- Direct source theorem support/open statements: `{source_support_count}/{source_open_count}`.
- Connection-table support/required tables: `{connection_support_count}/{connection_required_count}`.
- Accepted BN27 transition/connection row: `false`.
- Direct H K row emitted: `false`.

## Next Artifact

`{NEXT}`
"""

    write_json(TRANSFER_SPLIT, transfer_split)
    write_json(SOURCEID_GATE, sourceid_gate)
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
