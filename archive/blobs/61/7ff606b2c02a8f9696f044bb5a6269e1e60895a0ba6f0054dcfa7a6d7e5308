"""Validate a selected Qa/SU3 typed-monad D_E or rho_E data packet.

Exit codes:
  0 complete packet passes implemented structural checks
  1 complete-looking packet fails a structural check
  2 packet is open or incomplete
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PACKET = ROOT / "certificates" / "typed_monad_de_or_rhoe_data.template.json"


def is_number(x: Any) -> bool:
    return isinstance(x, int | float) and not isinstance(x, bool)


def is_matrix(value: Any) -> bool:
    return (
        isinstance(value, list)
        and bool(value)
        and all(isinstance(row, list) and bool(row) for row in value)
        and len({len(row) for row in value}) == 1
        and all(is_number(x) for row in value for x in row)
    )


def matmul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def zero_matrix(m: list[list[float]], tol: float = 1e-9) -> bool:
    return all(abs(x) <= tol for row in m for x in row)


def incomplete(reason: str) -> int:
    print(f"OPEN: {reason}")
    return 2


def fail(reason: str) -> int:
    print(f"FAIL: {reason}")
    return 1


def ok(message: str) -> int:
    print(f"PASS: {message}")
    return 0


def main(argv: list[str]) -> int:
    path = Path(argv[1]) if len(argv) > 1 else DEFAULT_PACKET
    data = json.loads(path.read_text(encoding="utf-8"))
    if str(data.get("status", "")).startswith("OPEN_"):
        return incomplete("packet status is open")

    selected = data.get("selected_branch", {})
    if not selected.get("source_certificate") or not selected.get("selection_rule"):
        return incomplete("selected source certificate or selection rule missing")
    if selected.get("target_residual_used") is not False:
        return fail("target residual is marked as used")

    monad = data.get("typed_monad", {})
    f = monad.get("f_map", {}).get("matrix")
    g = monad.get("g_map", {}).get("matrix")
    if not is_matrix(f) or not is_matrix(g):
        return incomplete("typed f/g monad matrices missing or non-numeric")
    if len(f) != len(g[0]):
        return fail("f target dimension does not match g source dimension")
    if not zero_matrix(matmul(g, f)):
        return fail("g*f is not zero")

    checks = monad.get("monad_checks", {})
    for key in ("g_f_zero", "locally_free", "stable_or_hym_source", "c1_zero", "c2_zero"):
        if checks.get(key) is not True:
            return incomplete(f"monad check {key} is not certified true")
    if checks.get("c3_integral") != 6:
        return fail("c3_integral is not 6")

    rep = data.get("representation_and_trace", {})
    if rep.get("representation") not in rep.get("allowed_representations", []):
        return incomplete("selected representation is missing or not allowed")
    for key in ("trace_normalization", "gauge_quotient_scheme", "zero_mode_policy"):
        if not rep.get(key):
            return incomplete(f"{key} missing")

    de = data.get("de_operator_packet", {})
    rhoe = data.get("rhoE_packet", {})
    de_available = de.get("available") is True
    rhoe_available = rhoe.get("available") is True
    if not de_available and not rhoe_available:
        return incomplete("neither D_E nor rho_E packet is available")

    if de_available:
        for key in ("principal_symbol", "connection_data", "endomorphism_E"):
            if de.get(key) is None:
                return incomplete(f"D_E packet missing {key}")
        if not any(de.get(key) is not None for key in ("heat_coefficient_table", "spectrum", "analytic_or_reidemeister_torsion")):
            return incomplete("D_E packet has no finite-part object")

    if rhoe_available:
        if rhoe.get("validator_passed") is not True:
            return fail("rho_E packet did not pass validator")
        for key in ("generator_data", "metric_compatibility", "selected_bundle_origin"):
            if rhoe.get(key) is None:
                return incomplete(f"rho_E packet missing {key}")

    return ok("selected Qa/SU3 typed monad packet passes implemented checks")


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
