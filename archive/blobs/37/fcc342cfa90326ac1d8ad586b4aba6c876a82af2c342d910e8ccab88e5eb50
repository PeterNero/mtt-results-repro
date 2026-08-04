"""Audit the HYM connection to finite-operator extraction contract."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = ROOT / "candidate_data" / "selected_hym_connection_to_finite_operator_extraction.candidate.json"
CERT = ROOT / "certificates" / "selected_hym_connection_to_finite_operator_extraction_certificate.json"
PROOF = ROOT / "proof_corpus" / "MTT_Selected_HYM_Connection_to_Finite_Operator_Extraction_v1.md"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    proof = PROOF.read_text(encoding="utf-8")

    require(
        data["status"] == "MTT_SELECTED_HYM_CONNECTION_TO_FINITE_OPERATOR_EXTRACTION_CONTRACT_BUILT_CONNECTION_REPRESENTATIVE_OPEN",
        "unexpected status",
    )
    require(data["closure_claimed"] is False, "must not claim closure")
    require(data["target_fitting_used"] is False, "must not use target fitting")
    require(data["straight_path"]["stage_E0_selected_bundle_and_metric"]["closed"] is True, "E0 should be closed")
    require(data["straight_path"]["stage_E1_connection_representative"]["closed"] is False, "E1 should remain open")
    require(data["straight_path"]["stage_E2_finite_basis_quadrature"]["closed"] is False, "E2 should remain open")
    require(data["straight_path"]["stage_E3_DE_emission"]["closed"] is False, "D_E emission must remain open")
    require(data["first_DE_emission_attempt"]["attempted"] is True, "first D_E attempt missing")
    require(data["first_DE_emission_attempt"]["closed"] is False, "first D_E attempt must not close")
    require(
        data["first_DE_emission_attempt"]["minimal_missing_primitive"] == "gauge_fixed_selected_HYM_connection_representative",
        "wrong missing primitive",
    )
    require(data["what_closes_now"]["extraction_contract_formalized"] is True, "contract not formalized")
    require(data["what_closes_now"]["missing_primitive_identified"] is True, "missing primitive not identified")
    require(data["what_remains_open"]["selected_D_E_matrices_from_connection"] is True, "D_E should remain open")
    require(
        data["next_required_artifact"] == "MTT_Selected_HYM_GaugeFixed_Connection_Representative_or_Galerkin_Solve_v1",
        "wrong next artifact",
    )
    require(cert["first_DE_emission_closed"] is False, "certificate must keep D_E open")
    require("Smoke matrices and lifted selected flags remain validator-schema support only" in proof, "proof must state guardrail")
    require("gauge-fixed HYM representative" in proof, "proof must name next computation")

    print("PASS selected HYM connection to finite-operator extraction audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
