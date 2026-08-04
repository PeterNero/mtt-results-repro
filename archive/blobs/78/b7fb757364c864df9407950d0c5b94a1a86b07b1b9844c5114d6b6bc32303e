from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "conditional_z64_qg_gap_bridge_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    require(cert["status"] == "CONDITIONAL_Z64_QG_GAP_BRIDGE_CLOSED_GR_AINT_IDENTIFICATION_OPEN", "unexpected status")
    source = cert["source_tests"]
    result = cert["conditional_result"]["then"]
    open_gr = cert["still_open_for_gr"]
    guards = cert["guardrails"]

    require(source["exact_schur_has_zero_offblock"] is True, "zero Schur branch should be sourced")
    require(source["exact_schur_has_conditional_lambda_bridge"] is True, "conditional lambda bridge should be sourced")
    require(source["qg_alignment_says_bridge_conditional"] is True, "QG alignment should mark bridge conditional")
    require(source["z64_exact_branch_has_coherent_inclusion_and_commutator"] is True, "Z64 exact branch should be sourced")
    require(result["C_fl"] == 0.0 and result["E_Schur"] == 0.0, "exact branch should have zero correction")
    require(abs(result["lambda_Q_lower_bound"] - 15.0) < 1e-15, "lambda_Q lower bound should be 15 conditionally")
    require(open_gr["GR_Aint_noncoherent_complement_identified_with_Z64_tower"] is False, "GR Aint ID should remain open")
    require(open_gr["physical_dimensionful_gap_selected"] is False, "physical gap should remain open")
    require(guards["claims_z64_gap_is_GR_gap"] is False, "must not claim Z64 gap is GR gap")
    require(guards["forbids_conditional_bridge_as_unconditional_GR_closure"] is True, "conditional guard required")

    print("AUDIT_PASS: conditional Z64/QG gap bridge closed; GR A_int identification remains open")


if __name__ == "__main__":
    main()
