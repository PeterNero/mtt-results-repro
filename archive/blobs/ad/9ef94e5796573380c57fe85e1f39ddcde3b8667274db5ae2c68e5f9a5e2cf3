from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT_PATH = ROOT / "certificates" / "gr_dependency_matrix_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT_PATH.read_text(encoding="utf-8"))
    require(
        cert["status"] == "GR_DEPENDENCY_MATRIX_BUILT_FULL_GR_REACHES_OPEN_RESPONSE_GATES",
        "unexpected matrix status",
    )
    reachable = set(cert["full_GR_numeric_closure_reachable_nodes"])
    for node in [
        "proto_spinor_binary_loop_closure",
        "selected_internal_rho_uv_branch",
        "dimensionful_GR_normalization",
        "finite_C1_response_matrices",
        "selected_visible_source_packet",
        "selected_GR_Hessian_kernel",
        "matter_gauge_stress_response",
    ]:
        require(node in reachable, f"full GR target does not reach required node: {node}")

    closed = set(cert["reachable_closed_nodes"])
    open_nodes = set(cert["reachable_open_nodes"])
    require("proto_spinor_binary_loop_closure" in closed, "closed protospinor invariant not reached")
    require("selected_internal_rho_uv_branch" in closed, "closed rho_UV branch not reached")
    require("dimensionful_GR_normalization" in open_nodes, "normalization gate should remain open")
    require("selected_GR_Hessian_kernel" in open_nodes, "Hessian kernel gate should remain open")
    require(cert["guardrails"]["claims_full_GR_numeric_closure"] is False, "matrix overclaims GR")
    require(cert["counts"]["edges"] > 0, "empty graph")

    print("AUDIT_PASS: GR dependency matrix reaches the right closed and open gates")


if __name__ == "__main__":
    main()

