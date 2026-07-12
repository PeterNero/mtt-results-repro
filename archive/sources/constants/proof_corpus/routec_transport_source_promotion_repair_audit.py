"""Audit Route-C transport source-promotion repair import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "import_routec_transport_source_promotion_repair.py"
PACKET = ROOT / "candidate_data" / "routec_transport_source_promotion_repair.candidate.json"
CERT = ROOT / "certificates" / "routec_transport_source_promotion_repair_certificate.json"
NOTE = ROOT / "proof_corpus" / "RouteC_Transport_Source_Promotion_Repair_v1.md"
STATUS = "ROUTEC_TRANSPORT_SOURCE_PROMOTION_REPAIR_STATIONARY_REPLAY_CLOSED_ALPHA1_DRIVER_OPEN"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(label: str, condition: bool, detail: object) -> None:
    print(f"{'PASS' if condition else 'FAIL'}: {label} -- {detail}")
    if not condition:
        raise SystemExit(1)


def main() -> int:
    packet = load(PACKET)
    cert = load(CERT)
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    check("script runs", proc.returncode == 0, proc.stdout)
    script_cert = json.loads(proc.stdout)

    check("status", cert["status"] == STATUS, cert["status"])
    check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])
    check("theorem proved", packet["theorem"]["proved"] is True, packet["theorem"])
    check("all checks pass", all(packet["checks"].values()), packet["checks"])

    stationary = packet["closed_stationary_replay"]
    check(
        "stationary replay closed",
        stationary["functional_rho_s_promoted"]
        and stationary["gauge_transported_trace_proved"]
        and stationary["symbolic_transport_conjugation_validator_extended"]
        and stationary["finite_validator_replay_closed"]
        and stationary["selected_source_verified"]
        and stationary["selected_rho_s_validator_ready"],
        stationary,
    )

    dynamic = packet["open_dynamic_replay"]
    check(
        "dynamic replay remains alpha driver open",
        dynamic["selected_dotD_source_formula_closed"]
        and dynamic["selected_dotD_source_verified_by_transport_derivative"]
        and dynamic["dotD_validator_full_replay_closed"] is False
        and dynamic["alpha1_driver_verified"] is False
        and dynamic["unit_lambda_candidate"] == 1.0
        and dynamic["unit_candidate_selected"] is False,
        dynamic,
    )

    update = packet["frontier_update"]
    check(
        "frontier returns to alpha1 source-strength value",
        update["old_next"]
        == "MTT_Selected_RouteC_Primitive_SourcePromotion_or_BNBasis_Emission_v1"
        and update["stationary_replay_next"]
        == "MTT_Selected_dotD_alpha1_TransportDerivative_and_Driver_v1"
        and update["current_next"]
        == "MTT_Selected_Alpha1_SourceStrength_Value_or_SameSourcePacket_v1",
        update,
    )
    check("guardrails retained", all(value is True for value in cert["guardrails"].values()), cert["guardrails"])

    note = NOTE.read_text(encoding="utf-8")
    for phrase in (
        "Raw untransported `B_N` equality is rejected",
        "Closed Stationary Replay",
        "Open Dynamic Replay",
    ):
        check(f"note records {phrase}", phrase in note, NOTE)

    print("\nRoute-C transport source-promotion repair audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
