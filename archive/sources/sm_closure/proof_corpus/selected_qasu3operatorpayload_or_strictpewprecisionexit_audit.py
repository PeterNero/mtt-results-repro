"""Audit Qa/SU3 operator payload or strict P_EW precision exit."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_qasu3operatorpayload_or_strictpewprecisionexit"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PAYLOAD_FORK = PACKET_DIR / "qasu3_payload_vs_strict_pew_fork.packet.json"
STEP10_CONTRACT = PACKET_DIR / "step10_payload_execution_contract.packet.json"
STRICT_PEW_EXIT = PACKET_DIR / "strict_pew_precision_exit_recheck.packet.json"
NEXT_TARGET = PACKET_DIR / "next_after_qasu3_payload_fork.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_QaSU3OperatorPayload_or_StrictPEWPrecisionExit_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_QASU3OPERATORPAYLOAD_OR_STRICTPEWPRECISIONEXIT_"
    "STEP10_SELECTED_STRICT_PEW_PARALLEL_OPEN"
)
NEXT = "MTT_Selected_Step10_PhysicalPhiFinC1SourceRule_or_IndependentGalerkinRows_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("closure_claimed") is True, f"{label} closure")
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    fork = load(PAYLOAD_FORK)
    step10 = load(STEP10_CONTRACT)
    strict = load(STRICT_PEW_EXIT)
    next_target = load(NEXT_TARGET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("fork", fork),
        ("step10", step10),
        ("strict", strict),
        ("next", next_target),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "cert status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(next_target["next_required_artifact"] == NEXT, "next packet")
    require(data["theorem"]["proved"] is True, "theorem")
    require(data["theorem"]["name"] == "QaSU3OperatorPayloadOrStrictPEWPrecisionExitTheorem", "name")

    decision = data["closure_decision"]
    require(decision["qasu3_source_slot_layer_closed"] is True, "source slot layer")
    require(decision["operator_source_slots_closed"] == 8, "source slots")
    require(decision["operator_source_slots_remaining"] == 0, "remaining source slots")
    require(decision["C1_support_layer_closed"] is True, "C1 support")
    require(decision["actual_dynamic_QaSU3_operator_packet_closed"] is False, "dynamic packet overclaim")
    require(decision["selected_C1_response_closed"] is False, "C1 response overclaim")
    require(decision["full_S2_value_emission_closed"] is False, "S2 overclaim")
    require(decision["route_A_selected_physical_PhiFinC1_source_rule_closed"] is False, "route A overclaim")
    require(decision["route_B_independent_selected_Galerkin_or_row_kernel_execution_closed"] is False, "route B overclaim")
    require(decision["strict_P_EW_source_theorem_closed"] is False, "strict P_EW overclaim")
    require(decision["strict_P_EW_source_rows"] == 0, "strict P_EW rows")
    require(decision["direct_K_threshold_Omega_H_lambda_rows"] == 0, "direct K rows")
    require(decision["P_EW_count_reduction_available_now"] is False, "count reduction overclaim")
    require(decision["true_SM_equivalence_closed"] is False, "true overclaim")
    require(decision["full_no_knob_closed"] is False, "no-knob overclaim")

    require(fork["qa_su3_side"]["operator_source_slots_closed"] == 8, "fork slots")
    require(fork["qa_su3_side"]["operator_source_slots_remaining"] == 0, "fork remaining")
    require(fork["qa_su3_side"]["actual_dynamic_QaSU3_operator_packet_closed"] is False, "fork dynamic")
    require(fork["strict_pew_side"]["strict_P_EW_source_rows"] == 0, "fork strict rows")
    require(fork["strict_pew_side"]["direct_K_threshold_Omega_H_lambda_rows"] == 0, "fork direct rows")
    require(fork["selected_next_route"] == NEXT, "fork next")
    require("Step10 selected physical Phi_fin^C1 source rule" in fork["route_priority"], "route A priority")
    require(
        "Step10 independent selected Galerkin or row-kernel execution" in fork["route_priority"],
        "route B priority",
    )

    require(step10["step10_must_close_one_of"]["route_A_selected_physical_PhiFinC1_source_rule"] is True, "step10 route A")
    require(
        step10["step10_must_close_one_of"]["route_B_independent_selected_Galerkin_or_row_kernel_execution"]
        is True,
        "step10 route B",
    )
    for field in [
        "A_selected",
        "b_selected",
        "deltaTheta_C1",
        "sector_response_matrices",
        "full_S2_value_rows",
        "Yukawa_CKM_PMNS_Higgs_mass_value_rows_without_proxy_fitting",
    ]:
        require(step10["step10_then_must_emit"][field] is True, f"missing {field}")
    require(step10["must_not_use_as_selectors"]["measured_Yukawa_CKM_PMNS_lambdaH_values"] is True, "selector guard")

    require(strict["strict_P_EW_source_rows"] == 0, "strict packet rows")
    require(strict["direct_K_threshold_Omega_H_lambda_rows"] == 0, "strict packet direct rows")
    require(strict["strict_P_EW_source_theorem_closed"] is False, "strict packet overclaim")
    require(strict["P_EW_count_reduction_available_now"] is False, "strict packet reduction overclaim")
    require(strict["strict_precision_exit_parallel_retained"] is True, "strict parallel")

    require(cert["qasu3_source_slot_layer_closed"] is True, "cert source layer")
    require(cert["operator_source_slots_closed"] == 8, "cert slots")
    require(cert["actual_dynamic_QaSU3_operator_packet_closed"] is False, "cert dynamic overclaim")
    require(cert["strict_P_EW_source_theorem_closed"] is False, "cert strict overclaim")
    require(cert["true_SM_equivalence_claimed"] is False, "cert true overclaim")
    require(cert["full_no_knob_closure_claimed"] is False, "cert no-knob overclaim")

    for phrase in [
        "QaSU3OperatorPayloadOrStrictPEWPrecisionExitTheorem",
        "operator source slots closed = 8",
        "operator source slots remaining = 0",
        "actual dynamic Qa/SU3 operator packet closed = false",
        "strict P_EW source rows = 0",
        "route A: selected physical Phi_fin^C1 source rule",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: Qa/SU3 source-slot layer is 8/8 closed, but dynamic "
        "payload, Step10 routes, full S2 values, strict P_EW/direct-K, true "
        "equivalence, and no-knob closure remain open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
