"""Import selected Phi_fin payload or B_N basis emission contracts."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SM = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure")

PREVIOUS = CERTS / "routec_provenance_or_basis_support_import_certificate.json"
UPSTREAM_PACKET = SM / "candidate_data" / "selected_phifin_payload_or_bn_basis_emission.candidate.json"
UPSTREAM_CERT = SM / "certificates" / "selected_phifin_payload_or_bn_basis_emission_certificate.json"
UPSTREAM_CONTRACT_DIR = SM / "candidate_data" / "selected_phifin_payload_or_bn_basis_emission"

OUTPUT_PACKET = DATA / "phifin_or_bn_emission_contracts_import.candidate.json"
OUTPUT_CERT = CERTS / "phifin_or_bn_emission_contracts_import_certificate.json"
OUTPUT_NOTE = CORPUS / "PhiFin_or_BN_EmissionContracts_Import_v1.md"
OUTPUT_CONTRACT_DIR = DATA / "phifin_or_bn_emission_contracts_import"

STATUS = "PHIFIN_OR_BN_EMISSION_CONTRACTS_IMPORTED_R1_OR_R4_OPEN"
PREVIOUS_STATUS = "ROUTEC_PROVENANCE_OR_BASIS_SUPPORT_IMPORTED_PRIMITIVE_EMISSION_OPEN"
UPSTREAM_STATUS = "MTT_SELECTED_PHIFIN_OR_BN_EMISSION_CONTRACTS_LOCKED_VALUES_OPEN"
NEXT = "MTT_Selected_RouteC_R1_Source_Certificate_or_R4_BN_Basis_Fill_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def contract_paths() -> dict[str, Path]:
    return {
        "selected_phifin_payload": UPSTREAM_CONTRACT_DIR / "selected_phifin_payload.emission_contract.json",
        "selected_bn_basis": UPSTREAM_CONTRACT_DIR / "selected_bn_basis.emission_contract.json",
    }


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    upstream = load(UPSTREAM_PACKET)
    upstream_cert = load(UPSTREAM_CERT)
    phifin = load(contract_paths()["selected_phifin_payload"])
    bn = load(contract_paths()["selected_bn_basis"])

    expected_order = [
        "R1_selected_source_certificate",
        "R2_selected_rhoE_metric_connection",
        "R4_selected_basis_data",
        "R3_selected_operator_spectral_data",
        "R5_selected_C1_response",
        "R6_replay_without_lifted_flags",
    ]

    checks = {
        "F0_previous_import_matches": previous["status"] == PREVIOUS_STATUS
        and previous["next_required_artifact"] == "MTT_Selected_PhiFin_Payload_or_BN_Basis_Emission_v1",
        "F1_upstream_contract_theorem_proved": upstream["status"] == UPSTREAM_STATUS
        and upstream["theorem"]["proved"] is True
        and upstream["closure_claimed"] is False
        and upstream["target_fitting_used"] is False
        and upstream["next_required_artifact"] == NEXT,
        "F2_certificate_agrees": upstream_cert["status"] == UPSTREAM_STATUS
        and upstream_cert["closure_claimed"] is False
        and upstream_cert["target_fitting_used"] is False
        and upstream_cert["primary_next_artifact"] == NEXT,
        "F3_contracts_locked_open": phifin["status"] == "OPEN_SELECTED_VALUES_NOT_EMITTED"
        and bn["status"] == "OPEN_SELECTED_BASIS_NOT_EMITTED"
        and upstream["support_vector"]["phifin_contract_written"] is True
        and upstream["support_vector"]["bn_contract_written"] is True,
        "F4_dependency_order_locked": upstream["dependency_order"] == expected_order
        and set(upstream["remaining_parts"]) == set(expected_order),
        "F5_closure_vector_all_open": all(value is False for value in upstream["closure_vector"].values())
        and all(value is True for value in upstream["what_remains_open"].values()),
        "F6_phifin_required_fields_present": "rho_E transition data" in phifin["required_outputs"]
        and "dotD_alpha1_matrices" in phifin["minimum_selected_payload_fields"]
        and "primitive_C1_contractions" in phifin["minimum_selected_payload_fields"]
        and "route_c_residual.selected_source_verified" in phifin["flags_that_must_be_theorem_derived"],
        "F7_bn_required_fields_present": bn["required_fields"]["scalar_basis_functions_phi_m"] is True
        and bn["required_fields"]["selected_D_E_action_on_basis"] is True
        and bn["required_success_gates"]["kernel_dimension_is_three"] is False
        and bn["closed_support"]["matrix_protocol_formulated"] is True,
        "F8_no_overclaim": upstream_cert["closure_claimed"] is False
        and upstream_cert["target_fitting_used"] is False
        and upstream["what_remains_open"]["full_SM_or_no_knob_closure"] is True,
    }

    return {
        "packet": "PhiFin_or_BN_EmissionContracts_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous_local_import": str(PREVIOUS.relative_to(ROOT)),
            "upstream_candidate": str(UPSTREAM_PACKET),
            "upstream_certificate": str(UPSTREAM_CERT),
            "upstream_contracts": {key: str(path) for key, path in contract_paths().items()},
        },
        "local_contracts": {
            "selected_phifin_payload": str((OUTPUT_CONTRACT_DIR / "selected_phifin_payload.emission_contract.json").relative_to(ROOT)),
            "selected_bn_basis": str((OUTPUT_CONTRACT_DIR / "selected_bn_basis.emission_contract.json").relative_to(ROOT)),
        },
        "theorem": {
            "name": "PhiFinOrBNEmissionContractsImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "The selected Phi_fin payload and selected B_N basis emission "
                "contracts are locked, including the R1-R6 dependency order and "
                "honest replay target.  No selected values are emitted; the next "
                "legal fill is R1 selected source certificate or R4 quotient-valid "
                "B_N basis."
            ),
        },
        "checks": checks,
        "upstream_contract_gate": upstream,
        "selected_phifin_payload_contract": phifin,
        "selected_bn_basis_contract": bn,
        "what_closes_now": upstream["what_closes_now"],
        "what_remains_open": upstream["what_remains_open"],
        "guardrails": {
            "claims_R1_selected_source_certificate": False,
            "claims_R2_selected_rhoE_metric_connection": False,
            "claims_R3_selected_operator_spectral_data": False,
            "claims_R4_selected_basis_data": False,
            "claims_R5_selected_C1_response": False,
            "claims_R6_replay_without_lifted_flags": False,
            "claims_selected_values_emitted": False,
            "claims_full_SM_or_no_knob_closure": False,
            "uses_observed_or_benchmark_inputs": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": NEXT,
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "PhiFinOrBNEmissionContractsImport",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "local_contracts": packet["local_contracts"],
        "theorem": packet["theorem"],
        "what_closes_now": packet["what_closes_now"],
        "what_remains_open": packet["what_remains_open"],
        "guardrails": packet["guardrails"],
        "next_required_artifact": packet["next_required_artifact"],
    }


def render_note(cert: dict[str, Any]) -> str:
    return f"""# PhiFin or BN EmissionContracts Import v1

Status: `{cert["status"]}`.

The primitive-emission contracts are now local and auditable:

- selected `Phi_fin` payload contract
- selected quotient/deck-valid `B_N` basis contract

The R1-R6 dependency order is locked:
`R1 -> R2 -> R4 -> R3 -> R5 -> R6`.

No selected values are emitted by this checkpoint.  The next legal construction
is either the R1 selected source certificate or the R4 quotient-valid `B_N`
basis fill.

Next artifact: `{cert["next_required_artifact"]}`.
"""


def write_contracts() -> None:
    OUTPUT_CONTRACT_DIR.mkdir(parents=True, exist_ok=True)
    for key, upstream_path in contract_paths().items():
        target = OUTPUT_CONTRACT_DIR / upstream_path.name
        target.write_text(upstream_path.read_text(encoding="utf-8"), encoding="utf-8")


def main() -> int:
    packet = build_packet()
    cert = build_certificate(packet)
    if "--write" in sys.argv:
        write_contracts()
        OUTPUT_PACKET.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(render_note(cert), encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
