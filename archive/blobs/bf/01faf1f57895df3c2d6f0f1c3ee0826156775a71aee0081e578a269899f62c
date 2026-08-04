"""Audit q79 alpha1 retarded-kernel formula N_MTT bridge."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "import_q79_alpha1_retarded_kernel_formula_nmtt_bridge.py"
PACKET = ROOT / "candidate_data" / "q79_alpha1_retarded_kernel_formula_nmtt_bridge.candidate.json"
CERT = ROOT / "certificates" / "q79_alpha1_retarded_kernel_formula_nmtt_bridge_certificate.json"
NOTE = ROOT / "proof_corpus" / "Q79_Alpha1_Retarded_Kernel_Formula_NMTT_Bridge_v1.md"
STATUS = "Q79_ALPHA1_RETARDED_KERNEL_FORMULA_IMPORTED_NMTT_BRIDGE_VALUES_OPEN"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(label: str, condition: bool, detail: object) -> None:
    status = "PASS" if condition else "FAIL"
    print(f"{status}: {label} -- {detail}")
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
    check("packet and certificate theorem agree", packet["theorem"] == cert["theorem"], cert["theorem"])
    check("bridge theorem proved as scoped bridge", cert["theorem"]["proved"] is True, cert["theorem"])

    checks = packet["bridge_checks"]
    check(
        "closed inputs imported",
        checks["B0_finite_raw_NMTT_terminal_operator_closed"]
        and checks["B1_NMTT_selects_L3_K2_and_c2_400"]
        and checks["B2_q79_analytic_retarded_kernel_formula_proved"],
        checks,
    )
    check(
        "value gates remain open",
        checks["B3_q79_selected_tangent_values_still_open"]
        and checks["B4_naive_ext_scale_to_alpha1_rejected"]
        and checks["B5_End0_sector_route_is_remaining_legal_route"]
        and checks["B6_raw_NMTT_does_not_emit_End0_sector_functor_values"] is False
        and checks["B7_raw_NMTT_does_not_emit_selected_transfer_normalization"] is False
        and checks["B8_raw_NMTT_does_not_emit_primitive_C1_contractions"] is False,
        checks,
    )

    nmtt = packet["raw_nmtt_contribution"]
    check(
        "N_MTT contribution scoped",
        nmtt["selected_terminal_lane"] == "L3-K2"
        and nmtt["selected_c2_row"] == [4, 0, 0]
        and "selected transfer normalization" in nmtt["does_not_close"],
        nmtt,
    )
    kernel = packet["q79_kernel_contribution"]
    check(
        "q79 kernel imports response formula not values",
        kernel["closes"]["duhamel_retarded_kernel_derivative_formula"]
        and kernel["closes"]["reduced_green_horizontal_response_identity"]
        and kernel["does_not_close"]["selected_alpha1_tangent_parameter"],
        kernel,
    )
    gate = packet["value_gate"]
    check(
        "value gate points to End0 route",
        gate["route_A_naive_source_normalization_rejected"]
        and gate["route_B_primary"]
        and gate["route_B_next_contract"]["next_required_artifact"]
        == "Q79_Selected_End0_to_SectorFunctor_Source_and_Value_Packet_v1",
        gate,
    )
    check(
        "frontier updated",
        packet["frontier_update"]["current_next"]
        == "Q79_Selected_End0_to_SectorFunctor_Source_and_Value_Packet_v1",
        packet["frontier_update"],
    )
    check(
        "guardrails retained",
        all(v is True for v in cert["guardrails"].values()),
        cert["guardrails"],
    )
    note = NOTE.read_text(encoding="utf-8")
    for phrase in (
        "N_MTT_terminal_q79",
        "dotPsi_i = - G Q dotD_alpha1 Psi_i",
        "selected value emission",
        "not the response values",
    ):
        check(f"note records {phrase}", phrase in note, NOTE)

    print("\nQ79 alpha1 retarded-kernel formula N_MTT bridge audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
