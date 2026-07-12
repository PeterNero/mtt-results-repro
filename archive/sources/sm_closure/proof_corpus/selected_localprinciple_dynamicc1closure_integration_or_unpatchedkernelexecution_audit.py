"""Audit local principle dynamic-C1 closure integration."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_localprinciple_dynamicc1closure_integration_or_unpatchedkernelexecution"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SOURCE_CHAIN = PACKET_DIR / "local_source_kernel_to_dynamicc1_chain.packet.json"
LOCAL_CLOSURE = PACKET_DIR / "local_principle_dynamicc1_closure_theorem.packet.json"
UNPATCHED_EXIT = PACKET_DIR / "unpatched_kernel_execution_exit_status.packet.json"
LEDGER = PACKET_DIR / "local_vs_unpatched_closure_ledger.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_LocalPrincipleDynamicC1Closure_Integration_or_UnpatchedKernelExecution_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_LOCALPRINCIPLE_DYNAMICC1CLOSURE_INTEGRATED_UNPATCHED_OPEN"
NEXT = "MTT_Selected_LocalDynamicC1PaperAppendix_or_UnpatchedKernelExecutionPlan_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict) -> None:
    require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
    require(packet.get("target_fitting_used") is False, "target fitting violation")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    chain = load(SOURCE_CHAIN)
    closure = load(LOCAL_CLOSURE)
    unpatched = load(UNPATCHED_EXIT)
    ledger = load(LEDGER)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")

    require(chain["status"] == "LOCAL_SOURCE_KERNEL_CHAIN_COMPLETE", "chain status mismatch")
    require(chain["validator_ok"] is True, "kernel validator not ok")
    for key, value in chain["kernel_fields"].items():
        require(value is True, f"kernel field missing: {key}")
    for key, value in chain["dynamic_value_support"].items():
        require(value is True, f"dynamic value support missing: {key}")

    require(closure["status"] == "LOCAL_PRINCIPLE_DYNAMIC_C1_PACKET_CLOSED", "closure status mismatch")
    require(closure["scientific_status"] == "local-premise-conditional dynamic C1 closure", "scientific status mismatch")
    for key, value in closure["promoted_objects_inside_local_spine"].items():
        require(value is True, f"local promoted object missing: {key}")
    exact = closure["exact_values"]
    require(exact["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "A^T A mismatch")
    require(exact["A_transpose_b"] == [12.0, 12.0], "A^T b mismatch")
    require(exact["b_norm_sq"] == 24.0, "b norm mismatch")
    require(exact["deltaTheta_C1"] == [1.0, 1.0], "delta mismatch")
    require(exact["rank"] == 2, "rank mismatch")
    require(exact["phase_R_Z_residual_norm_sq"] == 4.0, "phase norm mismatch")
    require(exact["shift_R_X_residual_norm_sq"] == 2.0, "shift norm mismatch")
    for key, value in closure["does_not_close"].items():
        require(value is True, f"does-not-close guard missing: {key}")

    require(unpatched["status"] == "UNPATCHED_AND_INDEPENDENT_EXECUTION_REMAIN_OPEN_AFTER_LOCAL_INTEGRATION", "unpatched status mismatch")
    require(unpatched["unpatched_dynamic_C1_closed"] is False, "unpatched dynamic C1 overclosed")
    require(unpatched["local_dynamic_C1_closed"] is True, "local dynamic C1 not closed")
    require(unpatched["route_A_accepts_without_local_principle"] is False, "Route A overaccepted")
    require(unpatched["route_B_accepts_without_local_principle"] is False, "Route B overaccepted")
    require(unpatched["independent_kernel_execution_supplied"] is False, "independent execution overclaimed")
    require(len(unpatched["remaining_exits"]) == 2, "remaining exits mismatch")

    require(ledger["status"] == "LOCAL_CLOSURE_YES_UNPATCHED_CLOSURE_NO", "ledger status mismatch")
    for key, value in ledger["local_closure"].items():
        require(value is True, f"ledger local flag missing: {key}")
    require(ledger["unpatched_closure"]["principle_derived"] is False, "ledger principle overderived")
    require(ledger["unpatched_closure"]["independent_kernel_execution_supplied"] is False, "ledger independent execution overclaimed")
    require(ledger["unpatched_closure"]["dynamic_C1_packet_closed"] is False, "ledger unpatched dynamic overclosed")
    require(ledger["comparison_to_prior_final_gate"]["new_local_principle_mode_closes_stricter_source_kernel"] is True, "comparison missing stronger kernel")

    require(data["theorem"]["proved"] is True, "integration theorem missing")
    closure_decision = data["closure_decision"]
    require(closure_decision["local_dynamic_C1_closed"] is True, "candidate local dynamic not closed")
    require(closure_decision["unpatched_dynamic_C1_closed"] is False, "candidate unpatched overclosed")
    require(closure_decision["independent_kernel_execution_supplied"] is False, "candidate independent execution overclaimed")
    require(closure_decision["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(closure_decision["no_knob_closed"] is False, "no-knob overclosed")
    require(closure_decision["global_closure_claimed"] is False, "global closure overclaimed")
    for key in [
        "local_source_kernel_integrated_with_dynamic_c1",
        "local_dynamic_C1_packet_closed_from_strict_kernel",
        "local_vs_unpatched_ledger_created",
        "unpatched_exits_preserved",
    ]:
        require(data["what_closes_now"][key] is True, f"achievement missing: {key}")

    require("local-premise-conditional closure" in note, "note missing local premise guard")
    require("does not derive the principle" in note, "note missing unpatched guard")

    for packet in [data, chain, closure, unpatched, ledger, cert]:
        guard(packet)

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
