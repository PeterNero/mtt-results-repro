from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "selected_core_b0_tt_source_theorem_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")
    theorem = cert["theorem"]
    packet = cert["packet_status"]
    implications = cert["implications"]
    guards = cert["guardrails"]

    require(cert["status"] == "FINAL_BTT_SUPPORT_CLOSED_SOURCE_ACCEPTED", "unexpected status")
    require(cert["final_closed"] is True, "final theorem should close")
    require(theorem["source_acceptance"] is True, "source theorem should accept selected core")
    require("B0^*P_TT=U_TT C" in theorem["statement"], "source theorem statement missing factorization")
    require("not a physical parameter" in theorem["normalization_clause"], "C guard missing")
    require(packet["packet_tests_pass"] is True, "packet tests must pass")
    require(packet["residuals_pass"] is True, "packet residuals must pass")

    require(implications["B0_factorization_closed"] is True, "B0 factorization should close")
    require(implications["dressed_factorization_closed"] is True, "dressed reduction should close")
    require(implications["equivariant_support_algebra_closed"] is True, "equivariant algebra should close")
    require(implications["adjoint_typing_closed"] is True, "adjoint typing should close")
    require(implications["final_support_identity"] == "Pi_exact64 B^*P_TT = B^*P_TT", "support identity wrong")
    require(implications["support"] == "|d_*> tensor span{c2,s2}", "support wrong")
    require(implications["lambda_GR_TT"] == 15, "lambda wrong")

    require(guards["C_is_basis_normalization_not_physical_parameter"] is True, "C normalization guard missing")
    require(guards["uses_observed_GR_data"] is False, "must not use observed data")
    require(guards["adds_numeric_knob"] is False, "must not add knob")
    require(guards["claims_independent_numeric_B0_entries_computed"] is False, "must not claim independent entries")
    require(guards["source_acceptance_is_the_new_selected_branch_theorem"] is True, "source acceptance should be theorem")

    require("C = I_2" in note, "canonical normalization missing")
    require("lambda_GR,TT=15" in note, "lambda consequence missing")
    print("AUDIT_PASS: selected core B0 source theorem closes final BTT support with C as normalization")


if __name__ == "__main__":
    main()
