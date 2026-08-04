"""Validate a Hessian/kernel central-cocycle derivation packet."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REQUIRED_TOP_LEVEL = [
    "source_identity",
    "hessian_block",
    "retarded_kernel",
    "twist_projection",
    "tau_extraction",
    "admissibility",
    "response_payload",
    "guardrails",
]


def missing(value: object) -> bool:
    if value is None:
        return True
    if isinstance(value, dict):
        return any(missing(v) for v in value.values())
    if isinstance(value, list):
        return len(value) == 0 or any(missing(v) for v in value)
    return False


def validate_tau(packet: dict[str, object]) -> list[str]:
    errors: list[str] = []
    tau = packet["tau_extraction"]
    if not isinstance(tau, dict):
        return ["tau_extraction must be an object"]
    labels = tau.get("module_twist_values")
    if not isinstance(labels, dict):
        return ["tau_extraction.module_twist_values must be supplied"]
    for idx in range(1, 6):
        f_key = f"F{idx}"
        g_key = f"G{idx}"
        if f_key not in labels or g_key not in labels:
            errors.append(f"missing {f_key}/{g_key} twist values")
            continue
        if labels[f_key] + labels[g_key] != 0:
            errors.append(f"{f_key}+{g_key} twists do not cancel")
    if labels.get("P") != 0:
        errors.append("P twist must be 0")
    return errors


def validate_packet(packet: dict[str, object]) -> tuple[int, list[str]]:
    errors: list[str] = []
    for key in REQUIRED_TOP_LEVEL:
        if key not in packet:
            errors.append(f"missing top-level field: {key}")
    if errors:
        return 2, errors
    open_fields = [key for key in REQUIRED_TOP_LEVEL if missing(packet[key])]
    if open_fields:
        return 2, [f"open or incomplete fields: {', '.join(open_fields)}"]
    guardrails = packet["guardrails"]
    if not isinstance(guardrails, dict):
        return 1, ["guardrails must be an object"]
    for key in ["no_target_fitting", "no_q79_direct_import", "source_selected"]:
        if guardrails.get(key) is not True:
            errors.append(f"guardrail {key} must be true")
    errors.extend(validate_tau(packet))
    if errors:
        return 1, errors
    return 0, ["packet passes implemented Hessian/kernel central-cocycle checks"]


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_hessian_kernel_central_cocycle_derivation.py PACKET.json")
        return 1
    packet = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    code, messages = validate_packet(packet)
    for message in messages:
        print(message)
    return code


if __name__ == "__main__":
    raise SystemExit(main())
