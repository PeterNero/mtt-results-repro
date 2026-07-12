from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "equivariant_central_circle_tt_support_theorem_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")
    checks = cert["checks"]
    theorem = cert["theorem"]
    remaining = cert["remaining"]
    finite = cert["finite_character_data"]
    guards = cert["guardrails"]

    require(
        cert["status"] == "EQUIVARIANT_SELECTOR_ALGEBRA_CLOSED_ACTUAL_SHAPE_MAP_EQUIVARIANCE_OPEN",
        "unexpected status",
    )
    require(all(checks.values()), "all finite algebra checks must pass")
    require(theorem["proved_algebraically"] is True, "algebraic theorem should be closed")
    require("Pi_exact64 B^*P_TT = B^*P_TT" in theorem["statement"], "support identity consequence missing")
    require("factors through U_TT" in theorem["statement"], "factorization premise missing")
    require(finite["group"] == "Z64", "wrong group")
    require(finite["character_label"] == 2, "wrong character")
    require(finite["character_order"] == 32, "wrong character order")
    require(finite["projection_identity_residual"] < 1e-12, "projection residual too large")
    require(finite["intertwining_residual"] < 1e-12, "intertwining residual too large")

    require(
        remaining["source_status"] == "SOURCE_EQUIVARIANCE_FOR_ACTUAL_BSTAR_PTT_OPEN",
        "actual shape-map source gate must remain open",
    )
    require("actual B=DG(Psi*)Pi_coh" in remaining["actual_missing_statement"], "actual B gate missing")
    require("same-angle equivariance/factorization" in remaining["why_this_is_smaller_than_previous_gap"], "gap not sharpened")

    require(guards["claims_actual_BstarPtt_sourced"] is False, "must not source actual BstarPtt")
    require(guards["claims_unconditional_support_identity"] is False, "must not claim unconditional support")
    require(guards["adds_numeric_knob"] is False, "must not add numeric knob")
    require(guards["uses_observed_GR_data"] is False, "must not use observed GR data")
    require(guards["conflates_zero_mode_with_helicity_character"] is False, "must not conflate zero mode and helicity")

    require("This closes the algebraic part" in note, "note should state algebra closure")
    require("source-level statement is still open" in note, "note should preserve source gate")

    print("AUDIT_PASS: equivariant central-circle TT support algebra closed; actual shape-map equivariance open")


if __name__ == "__main__":
    main()
