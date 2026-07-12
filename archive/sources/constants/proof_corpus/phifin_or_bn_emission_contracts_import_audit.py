"""Audit selected Phi_fin or B_N emission contracts import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "phifin_or_bn_emission_contracts_import.candidate.json"
CERT = ROOT / "certificates" / "phifin_or_bn_emission_contracts_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "PhiFin_or_BN_EmissionContracts_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_phifin_or_bn_emission_contracts.py"

STATUS = "PHIFIN_OR_BN_EMISSION_CONTRACTS_IMPORTED_R1_OR_R4_OPEN"
NEXT = "MTT_Selected_RouteC_R1_Source_Certificate_or_R4_BN_Basis_Fill_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    phifin = load(ROOT / data["local_contracts"]["selected_phifin_payload"])
    bn = load(ROOT / data["local_contracts"]["selected_bn_basis"])

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["theorem"]["closure_claimed"] is False, "closure overclaimed")
    require(all(data["checks"].values()), "not all checks passed")

    upstream = data["upstream_contract_gate"]
    require(upstream["dependency_order"] == [
        "R1_selected_source_certificate",
        "R2_selected_rhoE_metric_connection",
        "R4_selected_basis_data",
        "R3_selected_operator_spectral_data",
        "R5_selected_C1_response",
        "R6_replay_without_lifted_flags",
    ], "dependency order mismatch")
    require(all(value is False for value in upstream["closure_vector"].values()), "closure vector overclosed")
    require(phifin["status"] == "OPEN_SELECTED_VALUES_NOT_EMITTED", "Phi_fin contract overclosed")
    require(bn["status"] == "OPEN_SELECTED_BASIS_NOT_EMITTED", "BN contract overclosed")
    require(bn["required_success_gates"]["kernel_dimension_is_three"] is False, "BN success gate overclosed")

    guard = data["guardrails"]
    for key in [
        "claims_R1_selected_source_certificate",
        "claims_R2_selected_rhoE_metric_connection",
        "claims_R3_selected_operator_spectral_data",
        "claims_R4_selected_basis_data",
        "claims_R5_selected_C1_response",
        "claims_R6_replay_without_lifted_flags",
        "claims_selected_values_emitted",
        "claims_full_SM_or_no_knob_closure",
        "uses_observed_or_benchmark_inputs",
        "target_fitting_used",
    ]:
        require(guard[key] is False, f"guardrail overclaimed: {key}")

    require("R1 -> R2 -> R4 -> R3 -> R5 -> R6" in note, "note missing dependency order")
    require("No selected values are emitted" in note, "note missing no-values guardrail")
    require(NEXT in note, "note missing next artifact")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
