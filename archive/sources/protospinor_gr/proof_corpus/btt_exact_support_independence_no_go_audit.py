from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "btt_exact_support_independence_no_go_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(
        cert["status"] == "EXACT_SUPPORT_IDENTITY_INDEPENDENT_OF_CURRENT_SOURCED_ASSUMPTIONS",
        "unexpected status",
    )
    shared = cert["shared_assumptions"]
    models = cert["toy_models"]
    result = cert["logical_result"]
    guards = cert["guardrails"]

    require(shared["Delta_TT_equals_B_Ainv_Bstar_nonzero"] is True, "both models should be nonzero")
    require(shared["TT_weight2_and_BRST_closed"] is True, "weight/BRST should be shared")
    require(shared["exact_Z64_branch_available"] is True, "Z64 branch should be available")

    require(models["model_A_exact_support"]["Delta_TT"] == 1.0, "model A propagator mismatch")
    require(models["model_B_other_coherent_support"]["Delta_TT"] == 1.0, "model B propagator mismatch")
    require(models["model_A_exact_support"]["exact_support_identity"] is True, "model A should satisfy support")
    require(models["model_B_other_coherent_support"]["exact_support_identity"] is False, "model B should refute support")

    require(result["current_assumptions_force_nonzero_TT_adjoint_support"] is True, "nonzero should be forced")
    require(result["current_assumptions_force_exact_dstar_support"] is False, "exact support should not be forced")
    require("independent" in result["reason"], "reason should state independence")
    require("Countermodel" in note, "note should include countermodel")

    require(guards["claims_final_lambda_GR_TT_15"] is False, "must not claim final lambda")
    require(guards["claims_exact_support_sourced"] is False, "must not claim support sourced")
    require(guards["uses_observed_GR_data"] is False, "must not use observed data")

    print("AUDIT_PASS: exact BTT adjoint support is independent of current sourced assumptions")


if __name__ == "__main__":
    main()
