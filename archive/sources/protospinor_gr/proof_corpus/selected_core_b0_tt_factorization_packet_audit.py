from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "selected_core_b0_tt_factorization_packet_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")
    tests = cert["tests"]
    residuals = cert["test_residuals"]
    guards = cert["guardrails"]
    implications = cert["conditional_implications"]

    require(
        cert["status"] == "SELECTED_CORE_B0_PACKET_CANONICALLY_FILLED_SOURCE_ACCEPTANCE_OPEN",
        "unexpected status",
    )
    require(packet["status"] == "CANONICAL_PACKET_FILLED_TESTS_PASS_SOURCE_ACCEPTANCE_OPEN", "packet status wrong")
    require(packet["fill_type"] == "canonical_same_angle_equivariant_fill", "wrong fill type")
    require(packet["normalization"]["selected_core_matrix_C"] == [[1.0, 0.0], [0.0, 1.0]], "canonical C changed")
    require(all(tests.values()), "all canonical packet tests must pass")
    require(residuals["rank"] == 2, "rank must be 2")
    require(residuals["no_leakage_residual"] < 1e-12, "leakage residual too large")
    require(residuals["same_angle_intertwining_residual"] < 1e-12, "intertwining residual too large")
    require(residuals["core_support_identity_residual"] < 1e-12, "support residual too large")

    require("Accept or source" in packet["source_acceptance_required"], "source acceptance should remain explicit")
    require("source acceptance that actual selected metric core B0 is this canonical fill" in implications["currently_open"], "open source acceptance missing")
    require("lambda_GR,TT=15" in implications["if_source_acceptance_granted"][-1], "lambda implication missing")

    require(guards["claims_actual_B0_entries_sourced"] is False, "must not claim B0 entries sourced")
    require(guards["claims_unconditional_final_support"] is False, "must not claim unconditional final support")
    require(guards["uses_observed_GR_data"] is False, "must not use observed data")
    require(guards["adds_numeric_knob"] is False, "must not add numeric knob")
    require(guards["marks_C_as_basis_normalization_not_fit"] is True, "C must be basis normalization")

    require("canonical fill, not an" in note, "note should not overclaim")
    print("AUDIT_PASS: selected core B0 TT packet canonically filled; source acceptance remains open")


if __name__ == "__main__":
    main()
