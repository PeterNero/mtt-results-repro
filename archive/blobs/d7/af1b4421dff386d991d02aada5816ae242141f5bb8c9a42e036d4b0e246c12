"""Audit serious BN27 direct connection-table emission attempt."""

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
BUILDER = ROOT / "scripts" / "build_selected_sqasu3bn27_strictprinciplesource_or_directconnectiontables.py"

SLUG = "selected_sqasu3bn27_strictprinciplesource_or_directconnectiontables"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_SQaSU3BN27_StrictPrincipleSourceTheorem_or_DirectConnectionTables_v1.md"
TABLES = PACKET_DIR / "direct_eight_connection_table_emission_attempt.packet.json"
CHECKS = PACKET_DIR / "candidate_table_exact_checks.packet.json"
VALIDATOR = PACKET_DIR / "same_source_connection_table_acceptance_result.packet.json"
NEXT_PACKET = PACKET_DIR / "next_selected_values_or_source_theorem_contract.packet.json"

STATUS = (
    "MTT_SELECTED_SQASU3BN27_STRICTPRINCIPLESOURCE_OR_DIRECTCONNECTIONTABLES_"
    "EIGHT_CANDIDATE_TABLES_EMITTED_FINAL_ACCEPTANCE_ZERO"
)
NEXT = "MTT_Selected_QaSU3_SelectedMonadDEValues_or_BN27StrictSourceTheorem_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    tables = load(TABLES)
    checks = load(CHECKS)
    validator = load(VALIDATOR)
    next_packet = load(NEXT_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(next_packet["next_required_artifact"] == NEXT, "next packet mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem flag missing")

    for payload in [candidate, cert, tables, checks, validator, next_packet]:
        require(payload["closure_claimed"] is True, "closure boundary missing")
        require(payload["observed_data_used_as_selector"] is False, "observed selector used")
        require(payload["target_fitting_used"] is False, "target fitting used")

    decision = candidate["closure_decision"]
    require(decision["serious_direct_table_attempt_executed"] is True, "serious attempt missing")
    require(decision["candidate_connection_tables_emitted"] == 8, "candidate table count mismatch")
    require(decision["required_connection_tables"] == 8, "required table count mismatch")
    require(decision["accepted_final_same_source_connection_tables"] == 0, "final tables overaccepted")
    require(decision["formal_typed_f_g_tables_built"] is True, "f/g candidate tables missing")
    require(decision["candidate_g_after_f_zero_exact"] is True, "g after f exact check failed")
    require(decision["ctwist_product_typing_closed"] is True, "c-twist product typing failed")
    require(decision["D_E_Riesz_Green_gap_layer_imported"] is True, "D_E/Riesz/Green import missing")
    require(decision["premised_logdet_and_no_lift_replay_available"] is True, "premised replay missing")
    for key in [
        "strict_BN27_connection_tables_closed",
        "strict_source_emission_principle_derived",
        "direct_H_K_row_emitted",
        "strict_no_knob_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"overclosed: {key}")

    require(
        tables["status"] == "ALL_EIGHT_CANDIDATE_TABLES_EMITTED_NOT_SELECTED_FINAL_VALUES",
        "tables status mismatch",
    )
    require(len(tables["tables"]) == 8, "emitted table dictionary count mismatch")
    for name, row in tables["tables"].items():
        require(row["emitted_candidate_table"] is True, f"{name} not emitted as candidate")
        require(row["accepted_as_final_connection_table"] is False, f"{name} overaccepted")

    require(
        checks["status"] == "CANDIDATE_INTERNAL_CHECKS_PASS_FINAL_SOURCE_SELECTION_FAILS",
        "checks status mismatch",
    )
    require(checks["candidate_table_count"] == 8, "checks table count mismatch")
    require(checks["candidate_tables_emitted"] == 8, "checks emitted count mismatch")
    exact = checks["candidate_exact_checks"]
    require(exact["five_product_charge_typings_pass"] is True, "charge typing failed")
    require(exact["five_ctwist_product_typings_pass"] is True, "c-twist typing failed")
    require(exact["candidate_g_after_f_zero_exact"] is True, "g after f check failed")
    require(exact["selected_D_E_Riesz_Green_gap_layer_closed"] is True, "D_E gap layer not closed")
    require(exact["premised_logdet_matches_BN27_value"] is True, "premised logdet mismatch")
    failed = checks["failed_final_source_checks"]
    for key in [
        "selected_f_g_entries_supplied",
        "selected_multiplication_constants_supplied",
        "selected_DE_or_rhoE_supplied",
        "actual_good_cover_and_cocycles_supplied",
        "operator_exit_promoted",
        "fullsector_payload_closed",
        "unconditional_BN27_source_principle_derived",
    ]:
        require(failed[key] is False, f"final source check unexpectedly passed: {key}")

    require(
        validator["status"] == "VALIDATOR_EXECUTED_EIGHT_CANDIDATES_FINAL_ACCEPTANCE_ZERO",
        "validator status mismatch",
    )
    require(validator["candidate_tables_emitted"] == 8, "validator emitted count mismatch")
    require(validator["accepted_final_same_source_connection_tables"] == 0, "validator overaccepted")
    require(validator["required_final_same_source_connection_tables"] == 8, "validator required count mismatch")
    require(validator["partial_progress"]["candidate_g_after_f_zero_exact"] is True, "validator exact check missing")
    require(validator["strict_BN27_connection_tables_closed"] is False, "validator overclosed tables")
    require(validator["strict_source_emission_principle_derived"] is False, "validator overderived source")

    require("Candidate tables emitted: `8/8`" in note, "note missing candidate count")
    require("Final accepted same-source connection tables: `0/8`" in note, "note missing acceptance result")
    require(NEXT in note, "note missing next artifact")

    print("S_QaSU3^BN27 direct connection-table attempt audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
