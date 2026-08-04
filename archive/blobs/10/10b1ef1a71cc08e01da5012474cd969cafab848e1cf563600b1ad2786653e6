"""Audit same-source connection value table frontier packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_samesourceconnectionvaluetable_or_directhkrow"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
TABLE_PACKET = PACKET_DIR / "eight_field_connection_value_table.packet.json"
ROUTE_PACKET = PACKET_DIR / "three_route_field_alignment.packet.json"
VALIDATOR_PACKET = PACKET_DIR / "same_source_connection_table_validator.packet.json"
NEXT_CONTRACT = PACKET_DIR / "next_first_same_source_field_or_direct_hkrow_contract.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_SameSourceConnectionValueTable_or_DirectHKRow_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_SAMESOURCE_CONNECTION_VALUE_TABLE_BUILT_SUPPORT2_ACCEPTED0_DIRECT_HK_OPEN"
NEXT = "MTT_Selected_FirstSameSourceConnectionFieldEmission_or_DirectHKRow_v1"
FIELDS = [
    "source_id",
    "carrier_or_cover_id",
    "transition_or_connection_representative",
    "D_E_action",
    "rho_E_or_projective_character_table",
    "Riesz_projector",
    "reduced_Green_operator",
    "dotD_alpha1_or_threshold_derivative",
]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("closure_claimed") is True, f"{label} closure flag")
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    table = load(TABLE_PACKET)
    route = load(ROUTE_PACKET)
    validator = load(VALIDATOR_PACKET)
    contract = load(NEXT_CONTRACT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("table", table),
        ("route", route),
        ("validator", validator),
        ("contract", contract),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "certificate status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(cert["next_required_artifact"] == NEXT, "certificate next")
    require(data["theorem"]["proved"] is True, "candidate theorem")
    require(cert["theorem_proved"] is True, "certificate theorem")
    require(data["full_no_knob_closure_claimed"] is False, "candidate no-knob")
    require(data["true_SM_equivalence_claimed"] is False, "candidate true SM")

    require(table["field_count"] == 8, "table field count")
    require([row["field"] for row in table["rows"]] == FIELDS, "field order")
    require(table["support_field_count"] == 2, "support count")
    require(table["accepted_same_source_connection_value_count"] == 0, "accepted count")
    support_fields = [row["field"] for row in table["rows"] if row["support_present"]]
    require(support_fields == ["source_id", "carrier_or_cover_id"], "support fields")
    for row in table["rows"]:
        require(row["accepted_as_same_source_connection_value"] is False, f"overaccepted {row['field']}")
        require(row["blocking_reason"], f"missing blocker {row['field']}")

    require(route["status"] == "THREE_LEGAL_ROUTES_ALIGNED_TO_EIGHT_FIELDS", "route status")
    require(
        set(route["acceptable_minimal_values"])
        == {"source_identity_transport", "typed_connection_values", "direct_connection_values"},
        "minimal route families",
    )
    require(route["null_payload_slot_counts"]["typed_monad_cech_payload_null_slots"] == 9, "typed nulls")
    require(route["null_payload_slot_counts"]["direct_hym_payload_null_slots"] == 6, "hym nulls")
    require(route["null_payload_slot_counts"]["finite_routec_solve_payload_null_slots"] == 10, "routec nulls")

    require(validator["status"] == "VALIDATOR_EXECUTED_REJECTED_FINAL_CONNECTION_VALUES", "validator")
    require(validator["source_object_required_field_count"] == 11, "source required")
    require(validator["source_object_filled_field_count"] == 0, "source filled")
    require(validator["connection_values_required_field_count"] == 8, "connection required")
    require(validator["connection_values_filled_field_count_before_this_table"] == 0, "connection prior")
    require(validator["table_support_field_count"] == 2, "validator support")
    require(validator["accepted_same_source_connection_value_count"] == 0, "validator accepted")
    require(validator["accepted_as_full_connection_table"] is False, "table overaccepted")
    require(validator["direct_H_K_row_emitted"] is False, "direct H K overemitted")

    require(contract["status"] == "FIRST_SOURCE_FIELD_OR_DIRECT_HKROW_REQUIRED", "contract status")
    require(contract["recommended_first_field"] == "transition_or_connection_representative", "first field")
    require(contract["alternative_first_field"] == "source_id", "alternative field")
    require(contract["direct_exit"] == "K_threshold.Omega_H.lambda", "direct exit")
    require(contract["strict_K_threshold_count"] == {"accepted": 9, "required": 10}, "K count")

    decision = data["closure_decision"]
    for key in ["eight_field_table_built", "three_legal_routes_aligned_to_fields"]:
        require(decision[key] is True, f"decision missing {key}")
        require(cert[key] is True, f"cert missing {key}")
    require(decision["support_field_count"] == 2, "decision support")
    require(cert["support_field_count"] == 2, "cert support")
    require(decision["accepted_same_source_connection_value_count"] == 0, "decision accepted")
    require(cert["accepted_same_source_connection_value_count"] == 0, "cert accepted")
    for key in [
        "accepted_as_full_connection_table",
        "typed_monad_cech_values_present",
        "direct_hym_values_present",
        "finite_routec_solve_values_present",
        "same_source_certificate_present",
        "selected_K_threshold_Omega_H_lambda",
        "strict_H_K_threshold_row_emitted",
        "full_no_knob_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"decision overclosed {key}")
    require(decision["payload_missing_leaf_count"] == 29, "missing leaves")
    require(decision["accepted_selected_K_source_row_count"] == 9, "K accepted")
    require(decision["selected_K_threshold_row_count_required"] == 10, "K required")

    for phrase in [
        "SameSourceConnectionValueTableNormalFormTheorem",
        "concrete `8`-field table",
        "Support fields present: `source_id`, `carrier_or_cover_id`",
        "Accepted same-source connection values: `0`",
        "The next attempt must fill one row",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print("AUDIT_PASS: same-source connection table built; 2 support fields, 0 accepted values.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
