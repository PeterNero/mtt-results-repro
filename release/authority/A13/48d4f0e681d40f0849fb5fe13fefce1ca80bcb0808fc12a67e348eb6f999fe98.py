from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "gr_tt_support_final_theorem_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")
    checks = cert["chain_checks"]
    conclusion = cert["conclusion"]
    guards = cert["guardrails"]

    require(
        cert["status"] == "GR_TT_SUPPORT_FINAL_THEOREM_CLOSED_PHYSICAL_NORMALIZATION_NEXT",
        "unexpected final theorem status",
    )
    require(all(checks.values()), "all proof-chain checks must pass")
    require(cert["theorem"]["status"] == "CLOSED", "theorem should be closed")
    require(
        conclusion["support_identity"] == "Pi_exact64 B^*P_TT = B^*P_TT",
        "support identity mismatch",
    )
    require(conclusion["support"] == "|d_*> tensor span{c2,s2}", "support mismatch")
    require(conclusion["lambda_GR_TT_internal_exact_branch"] == 15, "lambda mismatch")

    require(guards["uses_observed_GR_data"] is False, "must not use observed GR data")
    require(guards["uses_observed_Newton_or_Planck_data"] is False, "must not use Newton/Planck data")
    require(guards["adds_numeric_knob"] is False, "must not add numeric knob")
    require(guards["C_is_physical_parameter"] is False, "C must remain a basis normalization")
    require(guards["claims_full_physical_GR_closed"] is False, "must not overclaim full physical GR")
    require(guards["claims_SI_Newton_prediction"] is False, "must not claim SI Newton prediction")

    require("lambda_GR,TT=15" in note, "note must state final internal lambda")
    require("Those are now the next real gates" in note, "note must identify next gates")
    print("AUDIT_PASS: GR TT support final theorem closed; physical normalization remains next")


if __name__ == "__main__":
    main()
