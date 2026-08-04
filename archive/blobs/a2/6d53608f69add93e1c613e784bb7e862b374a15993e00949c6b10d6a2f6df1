from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "routec_correction_source_emission_import_certificate.json"
STATUS = "ROUTEC_CORRECTION_SOURCE_EMISSION_IMPORTED_SPLITTER_NOT_EMITTED_CONTRACT_OPEN"
NEXT_ARTIFACT = "MTT_Selected_RouteC_Splitter_Source_Emission_Contract_or_Selected_DeltaTheta_C1_Solve_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["theorem"]["proved"] is True, "source-emission import theorem should be proved")
    require(all(cert["closed_now"].values()), "all closed-now checks should pass")
    require(all(cert["emission_checks"].values()), "all emission checks should pass")
    require(all(cert["payload_checks"].values()), "all payload checks should pass")
    require(all(cert["source_galerkin_checks"].values()), "all source/Galerkin checks should pass")
    require(all(cert["contract_checks"].values()), "all contract checks should pass")
    require(all(cert["open_gate_checks"].values()), "all open-gate checks should pass")
    require(all(cert["still_open_checks"].values()), "all still-open checks should pass")
    require(cert["verdict"]["diagnostic_splitter_source_emitted"] is False, "splitter must not source-emit")
    require(cert["verdict"]["selected_values_emitted"] is False, "selected values must remain absent")
    require(cert["verdict"]["honest_galerkin_values_promoted"] is False, "honest Galerkin must remain open")
    require(cert["verdict"]["source_emission_contract_built"] is True, "contract should be built")
    require(cert["verdict"]["observed_flavor_data_used"] is False, "observed flavor data must not be used")
    require(cert["verdict"]["next_required_artifact"] == NEXT_ARTIFACT, "wrong next artifact")

    contract = packet["source_emission_contract"]
    require(
        contract["minimum_acceptance_tests"]["selected_deltaTheta_C1_or_equivalent_present"] is True,
        "contract must require selected deltaTheta/equivalent",
    )
    require(
        contract["minimum_acceptance_tests"]["sector_response_matrices_M_u_M_d_M_e_M_nuD_present"] is True,
        "contract must require sector matrices",
    )
    require("not source-emitted" in note, "note must state non-emission")
    require("no observed flavor targets" in note, "note must state target guardrail")

    print("AUDIT_PASS: correction source-emission audit imported; selected emission contract remains open")


if __name__ == "__main__":
    main()
