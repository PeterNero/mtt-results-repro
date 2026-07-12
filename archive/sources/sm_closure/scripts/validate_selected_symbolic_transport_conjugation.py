"""Validate a selected symbolic transport-conjugation finite quotient packet."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


REQUIRED_IDENTITIES = [
    "D_selected_U_equals_U_d",
    "P_selected_equals_U_P_model_U_inverse",
    "G_selected_equals_U_G_model_U_inverse_on_complement",
    "trace_cyclicity_for_transport_conjugation",
    "rank_preserved_by_conjugation",
    "gap_preserved_by_unitary_conjugation",
    "finite_trace_restriction_map_equals_constructed_row",
]

REQUIRED_RELATIONS = [
    "U_inverse_U_identity",
    "U_unitary_or_orthogonal",
    "P_selected_conjugation",
    "G_selected_conjugation",
    "trace_cyclicity",
]


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate(payload: dict[str, Any]) -> tuple[bool, list[str]]:
    errors: list[str] = []
    if payload.get("observed_data_used_as_selector") is not False:
        errors.append("observed_data_used_as_selector must be false")
    if payload.get("target_fitting_used") is not False:
        errors.append("target_fitting_used must be false")
    if payload.get("raw_27_mode_truncation_claimed_closed") is not False:
        errors.append("raw_27_mode_truncation_claimed_closed must be false")

    quotient = payload.get("symbolic_finite_quotient", {})
    if quotient.get("finite_rank") != 27:
        errors.append("symbolic finite quotient must keep finite rank 27")
    if quotient.get("symbolic_transport_envelope") is not True:
        errors.append("symbolic transport envelope must be true")

    relations = quotient.get("relations", {})
    for key in REQUIRED_RELATIONS:
        if relations.get(key) is not True:
            errors.append(f"missing symbolic relation: {key}")

    transport = payload.get("transport_operator", {})
    if transport.get("symbol") != "U":
        errors.append("transport symbol must be U")
    if transport.get("unitary_or_orthogonal") is not True:
        errors.append("transport must be unitary_or_orthogonal")
    if "exp(-u" not in str(transport.get("formula", "")):
        errors.append("transport formula must use exp(-u ad(T3))")

    identities = payload.get("validated_identities", {})
    for key in REQUIRED_IDENTITIES:
        if identities.get(key) is not True:
            errors.append(f"missing validated identity: {key}")

    provenance = payload.get("source_provenance", [])
    if not isinstance(provenance, list) or len(provenance) < 5:
        errors.append("at least five source provenance entries are required")
    else:
        for item in provenance:
            source = item.get("source") if isinstance(item, dict) else None
            if not source or not Path(source).exists():
                errors.append(f"missing provenance source: {source}")

    residuals = payload.get("residual_guardrail", {})
    if residuals.get("direct_truncated_relative_residual", 0) <= 0:
        errors.append("direct truncated residual must be recorded as positive")
    if residuals.get("gauge_frame_residual_l2", 1) >= 1e-12:
        errors.append("gauge-frame residual must be below 1e-12")

    return not errors, errors


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_selected_symbolic_transport_conjugation.py <packet.json>", file=sys.stderr)
        return 2
    path = Path(argv[1])
    ok, errors = validate(load(path))
    if ok:
        print(f"PASS {path}")
        return 0
    for error in errors:
        print(f"ERROR {error}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
