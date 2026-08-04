"""Audit true-equivalence precision value table or actual Qa/SU3 operator upgrade."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_trueequivalenceprecisionvaluetable_or_actualqasu3operatorupgrade"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PRECISION_TABLE = PACKET_DIR / "true_equivalence_precision_value_table_manifest.packet.json"
QASU3_CONTRACT = PACKET_DIR / "actual_qasu3_operator_upgrade_contract.packet.json"
ROUTE = PACKET_DIR / "dual_route_true_equivalence_decision.packet.json"
CUTSET = PACKET_DIR / "next_value_emission_cutset.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_TrueEquivalencePrecisionValueTable_or_ActualQaSU3OperatorUpgrade_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_TRUEEQUIVALENCEPRECISIONVALUETABLE_OR_ACTUALQASU3OPERATORUPGRADE_BUILT_DUAL_ROUTE_CONTRACT_VALUES_OPEN"
NEXT = "MTT_Selected_PrecisionValueEmissionAttempt_or_QaSU3SourcePayloadFill_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    precision = load(PRECISION_TABLE)
    qasu3 = load(QASU3_CONTRACT)
    route = load(ROUTE)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, "next artifact mismatch")

    require(precision["precision_value_table_contract_ready"] is True, "precision contract not ready")
    require(precision["precision_values_filled"] is False, "precision values overfilled")
    require(precision["accepted_for_true_SM_equivalence"] is False, "precision overaccepted")
    require(precision["all_current_rows_classified"] is True, "promotion matrix not classified")
    require(precision["any_row_promoted_to_true_precision_equivalence"] is False, "row overpromoted")
    require(len(precision["row_contracts"]) == 3, "precision row contract count mismatch")

    require(qasu3["actual_packet_closed_now"] is False, "Qa/SU3 packet overclosed")
    require(qasu3["qft_rows_change_source_status"] is False, "QFT rows changed source status")
    require(qasu3["accepted_for_true_SM_equivalence"] is False, "Qa/SU3 overaccepted for true equivalence")
    require(qasu3["accepted_for_no_knob"] is False, "Qa/SU3 overaccepted for no-knob")
    require(len(qasu3["required_source_payload"]) >= 5, "Qa/SU3 payload underspecified")

    require(route["route_A_precision_value_table"]["contract_ready"] is True, "route A contract missing")
    require(route["route_A_precision_value_table"]["values_filled"] is False, "route A overfilled")
    require(route["route_B_actual_QaSU3_operator_upgrade"]["contract_ready"] is True, "route B contract missing")
    require(route["route_B_actual_QaSU3_operator_upgrade"]["source_values_filled"] is False, "route B overfilled")
    require(route["true_SM_equivalence_closed"] is False, "route overclosed true equivalence")
    require(route["no_knob_closed"] is False, "route overclosed no-knob")

    require(cutset["bookkeeping_remaining"] is False, "bookkeeping still marked remaining")
    require(cutset["value_emission_required"] is True, "value emission not required")
    require(cutset["recommended_next_artifact"] == NEXT, "cutset next artifact mismatch")
    require(cutset["true_SM_equivalence_closed"] is False, "cutset true equivalence overclosed")

    require(data["closure_decision"]["SM_parity_closed"] is True, "candidate SM parity missing")
    require(data["closure_decision"]["precision_value_table_contract_ready"] is True, "candidate precision contract missing")
    require(data["closure_decision"]["actual_QaSU3_operator_upgrade_contract_ready"] is True, "candidate Qa/SU3 contract missing")
    require(data["closure_decision"]["true_SM_equivalence_closed"] is False, "candidate true equivalence overclosed")
    require(data["dependency_flags"]["qasu3_gate_still_open"] is True, "dependency Qa/SU3 gate not open")
    require(cert["precision_value_table_contract_ready"] is True, "certificate precision contract missing")
    require(cert["actual_QaSU3_operator_upgrade_contract_ready"] is True, "certificate Qa/SU3 contract missing")
    require("no longer bookkeeping" in note, "note missing value-emission boundary")

    for packet in [precision, qasu3, route, cutset, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
