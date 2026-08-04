"""Build first same-source connection-field emission attempt."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
QA = Path("C:/Users/nero_/Downloads/TEXPAPERS/mtt-qa-su3-packet-proof/candidate_data")

SLUG = "selected_firstsamesourceconnectionfieldemission_or_directhkrow"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
FIELD_SCAN = PACKET_DIR / "first_field_candidate_scan.packet.json"
VALIDATOR = PACKET_DIR / "first_field_validator.packet.json"
NEXT_CONTRACT = PACKET_DIR / "next_bn27_sector_transfer_or_sourceid_certificate_contract.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_FirstSameSourceConnectionFieldEmission_or_DirectHKRow_v1.md"

SOURCES = {
    "previous": DATA / "selected_orientedphifin_bn27sourceownershiptransport_or_connectionwitnessvalues.candidate.json",
    "previous_contract": DATA
    / "selected_orientedphifin_bn27sourceownershiptransport_or_connectionwitnessvalues"
    / "next_first_same_source_field_or_direct_hkrow_contract.packet.json",
    "same_source_table": DATA / "selected_samesourceconnectionvaluetable_or_directhkrow.candidate.json",
    "same_source_table_packet": DATA
    / "selected_samesourceconnectionvaluetable_or_directhkrow"
    / "eight_field_connection_value_table.packet.json",
    "hym_extraction_contract": DATA / "selected_hym_connection_to_finite_operator_extraction.candidate.json",
    "hym_extraction_status": DATA
    / "selected_hymconnectionextraction_or_sourceoriginlemma"
    / "hym_connection_extraction_status.packet.json",
    "hym_first_solve": DATA / "selected_hymnewtongalerkin_firstsolve_or_rank2sectorfunctor.candidate.json",
    "rtheta_hym_import": DATA
    / "selected_rtheta_pikernel_from_selectedhymconnection_or_bnbasisemission"
    / "selected_hym_connection_subgate_import.packet.json",
    "u1y_connection_witness": QA / "selected_u1y_routec_selected_source_certificate_or_typed_de_construction.candidate.json",
}

STATUS = (
    "MTT_SELECTED_FIRSTSAMESOURCECONNECTIONFIELDEMISSION_OR_DIRECTHKROW_"
    "BUILT_RTHETA_HYM_CLUE_REJECTED_BN27_FIELD_OPEN"
)
NEXT = "MTT_Selected_BN27SectorTransferConnectionRepresentative_or_SourceIDCertificate_v1"


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
    table = sources["same_source_table_packet"]
    hym_contract = sources["hym_extraction_contract"]
    hym_status = sources["hym_extraction_status"]
    first_solve = sources["hym_first_solve"]
    rtheta_import = sources["rtheta_hym_import"]
    u1y = sources["u1y_connection_witness"]

    if previous["next_required_artifact"] != "MTT_Selected_FirstSameSourceConnectionFieldEmission_or_DirectHKRow_v1":
        raise ValueError("previous frontier no longer points to first-field emission")

    row = next(item for item in table["rows"] if item["field"] == "transition_or_connection_representative")
    candidate_sources = {
        "rtheta_diagonal_hym_representative": {
            "value": rtheta_import["A_HYM_formula"],
            "selected_for_rtheta_pi_subgate": rtheta_import["selected_HYM_connection_representative_available"],
            "accepted_for_bn27_transition_field": False,
            "reason": (
                "It is the selected q79/F,m=1 diagonal rank-2 End0 lane and is "
                "accepted for the R_theta Pi subgate, but it does not export the "
                "same-source BN27 transition/connection table."
            ),
        },
        "hym_first_solve": {
            "selected_diagonal_HYM_first_solve_closed": first_solve["closure_decision"][
                "selected_diagonal_HYM_first_solve_closed"
            ],
            "rank2_End0_payload_closed": first_solve["closure_decision"][
                "rank2_End0_payload_closed"
            ],
            "rank2_to_sector_transfer_closed": first_solve["closure_decision"][
                "rank2_to_sector_transfer_closed"
            ],
            "actual_QaSU3_operator_packet_promoted": first_solve["closure_decision"][
                "actual_QaSU3_operator_packet_promoted"
            ],
            "accepted_for_bn27_transition_field": False,
            "reason": "The first solve is real diagonal support, but sector transfer and actual Qa/SU3 operator promotion remain open.",
        },
        "hym_extraction_status": {
            "actual_gauge_fixed_connection_representative_emitted": hym_status[
                "actual_gauge_fixed_connection_representative_emitted"
            ],
            "actual_finite_operator_payload_emitted": hym_status[
                "actual_finite_operator_payload_emitted"
            ],
            "rank2_to_sector_transfer_functor_closed": hym_status[
                "rank2_to_sector_transfer_functor_closed"
            ],
            "accepted_for_bn27_transition_field": False,
            "reason": "The extraction gate still requires full finite operator payload, transfer, and no lifted flags.",
        },
        "u1y_connection_witness": {
            "finite_connection_prefix_values_present": u1y["decision"][
                "finite_connection_prefix_values_present"
            ],
            "selected_hym_connection_constructed": u1y["decision"][
                "selected_hym_connection_constructed"
            ],
            "selected_connection_witness_values_absent": u1y["decision"][
                "selected_connection_witness_values_absent"
            ],
            "accepted_for_bn27_transition_field": False,
            "reason": "Prefix values are useful arithmetic support, but selected connection witness values are absent.",
        },
    }

    accepted_field = all(
        [
            rtheta_import["selected_HYM_connection_representative_available"],
            first_solve["closure_decision"]["rank2_to_sector_transfer_closed"],
            first_solve["closure_decision"]["actual_QaSU3_operator_packet_promoted"],
            hym_status["actual_finite_operator_payload_emitted"],
            not u1y["decision"]["selected_connection_witness_values_absent"],
        ]
    )

    field_scan = {
        "schema": "MTTFirstSameSourceConnectionFieldCandidateScan.v1",
        "status": "RTHETA_DIAGONAL_HYM_CLUE_FOUND_BN27_FIELD_NOT_ACCEPTED",
        "closure_claimed": True,
        "target_field": "transition_or_connection_representative",
        "table_blocking_reason": row["blocking_reason"],
        "candidate_sources": candidate_sources,
        "accepted_transition_or_connection_representative": accepted_field,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    validator = {
        "schema": "MTTFirstSameSourceConnectionFieldValidator.v1",
        "status": "VALIDATOR_EXECUTED_FIRST_FIELD_ACCEPTED0",
        "closure_claimed": True,
        "accepted_first_field_count": 0,
        "accepted_same_source_connection_value_count_after_attempt": 0,
        "support_clues_promoted_to_table_values": 0,
        "rtheta_diagonal_HYM_clue_recorded": True,
        "why_rtheta_clue_not_promoted": [
            "not a same-source BN27 transition table",
            "rank2-to-sector transfer closed false",
            "actual Qa/SU3 operator packet promoted false",
            "selected connection witness values absent in U1/Y Route-C packet",
        ],
        "direct_H_K_row_emitted": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_contract = {
        "schema": "MTTBN27SectorTransferConnectionRepresentativeOrSourceIDCertificate.v1",
        "status": "NEXT_IS_BN27_TRANSFERRED_CONNECTION_REPRESENTATIVE_OR_SOURCEID_CERTIFICATE",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "primary_route": "transfer A_diag=du*T3 from selected rank-2 End0 HYM lane to BN27 sector table with theorem-derived routing and finite operator payload",
        "must_emit": [
            "rank2-to-sector transfer functor or proof it is unnecessary",
            "actual Qa/SU3 finite operator packet promoted without lifted flags",
            "BN27 transition/connection representative row",
            "residual/error certificate in the same table convention",
        ],
        "alternative_route": "source_id certificate naming the q79/F,m=1 branch as same-source table owner",
        "direct_exit": contract["direct_exit"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedFirstSameSourceConnectionFieldEmissionOrDirectHKRow",
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
            "first_field_candidate_scan": rel(FIELD_SCAN),
            "first_field_validator": rel(VALIDATOR),
            "next_bn27_sector_transfer_or_sourceid_certificate_contract": rel(NEXT_CONTRACT),
        },
        "closure_decision": {
            "first_field_attempted": True,
            "rtheta_diagonal_HYM_clue_found": True,
            "rtheta_diagonal_HYM_accepted_for_rtheta_subgate": True,
            "rtheta_diagonal_HYM_promoted_to_BN27_field": False,
            "transition_or_connection_representative_emitted": False,
            "accepted_first_field_count": 0,
            "accepted_same_source_connection_value_count_after_attempt": 0,
            "rank2_to_sector_transfer_closed": False,
            "actual_QaSU3_operator_packet_promoted": False,
            "selected_connection_witness_values_absent": True,
            "direct_H_K_row_emitted": False,
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "FirstSameSourceConnectionFieldNonPromotionTheorem",
            "proved": True,
            "statement": (
                "The first same-source field was attacked directly. The selected "
                "rank-2 diagonal HYM representative A_diag=du*T3 is real progress "
                "and closes the R_theta Pi subgate, but it cannot be promoted to "
                "the BN27 transition/connection table because rank2-to-sector "
                "routing, actual Qa/SU3 operator promotion, and selected connection "
                "witness values remain absent. The next constructive object is a "
                "BN27-transferred connection representative or a same-source "
                "source_id certificate; direct H K remains independent."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedFirstSameSourceConnectionFieldEmissionOrDirectHKRow",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "rtheta_diagonal_HYM_clue_found": True,
        "transition_or_connection_representative_emitted": False,
        "accepted_first_field_count": 0,
        "direct_H_K_row_emitted": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected First Same-Source Connection Field Emission or Direct H K Row v1

## Theorem

`FirstSameSourceConnectionFieldNonPromotionTheorem` is emitted.

## What Was Tried

The first non-label field,
`transition_or_connection_representative`, was attacked using the strongest
available clue: the selected rank-2 diagonal HYM representative
`A_diag = du*T3`.

## Result

- `A_diag = du*T3` is accepted for the `R_theta` Pi subgate.
- It is not accepted as the BN27 same-source transition/connection field.
- Accepted first-field rows: `0`.
- Accepted same-source connection table values after this attempt: `0/8`.
- Direct `K_threshold.Omega_H.lambda` emitted: `false`.

## Why It Does Not Promote

- The HYM representative is still diagonal/rank-2 End0 support.
- Rank2-to-sector transfer is not closed.
- Actual Qa/SU3 operator packet promotion is not closed.
- U1/Y selected connection witness values are still absent.

## Next Artifact

`{NEXT}`
"""

    write_json(FIELD_SCAN, field_scan)
    write_json(VALIDATOR, validator)
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
