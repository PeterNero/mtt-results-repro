from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "selected_gr_hessian_block_source_theorem_certificate.json"
TEMPLATE = ROOT / "candidate_data" / "selected_gr_hessian_block_source.template.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    template = json.loads(TEMPLATE.read_text(encoding="utf-8"))

    require(
        cert["status"] == "SELECTED_GR_HESSIAN_BLOCK_SOURCE_THEOREM_TARGET_CLOSED_SOURCE_OPEN",
        "unexpected theorem status",
    )
    conditions = cert["closure_conditions"]
    require(conditions["symbolic_anchor_found"] is True, "symbolic anchor Hessian should be found")
    require(conditions["tt_target_found"] is True, "TT target should be found")
    require(conditions["proper_time_kernel_class_found"] is True, "proper-time kernel class should be found")
    require(conditions["z64_exact_block_found"] is True, "Z64 exact block should be detected")
    require(conditions["z64_allowed_as_gr_substitute"] is False, "Z64 must not substitute for GR")
    require(
        conditions["selected_h_anchor_to_tt_projection_found"] is False,
        "P_GR projection should remain missing in current corpus",
    )
    require(cert["selected_block_closed"] is False, "selected GR Hessian block must remain open")

    rows = {row["object"]: row for row in cert["theorem_rows"]}
    require(rows["TT/Lichnerowicz target block"]["closed_for_GR"] is True, "TT target row should close")
    require(rows["H_anchor to TT projection P_GR"]["status"] == "MISSING_SELECTED_MAP", "missing map row lost")
    require(rows["exact Z64 Hessian/kernel"]["closed_for_GR"] is False, "Z64 row overclaims closure")

    require(template["K_GR"]["formula"].startswith("P_GR^T H_anchor P_GR"), "template kernel formula mismatch")
    require(template["normalization"]["absolute_G_eff_closed"] is False, "normalization should remain open")

    guardrails = cert["guardrails"]
    require(guardrails["claims_selected_GR_Hessian_closed"] is False, "forbidden selected-Hessian claim")
    require(guardrails["uses_Z64_as_GR_Hessian"] is False, "forbidden Z64 substitution")
    require(guardrails["claims_absolute_G_eff"] is False, "forbidden G_eff claim")

    print("AUDIT_PASS: selected GR Hessian block source theorem is target-closed/source-open")


if __name__ == "__main__":
    main()

