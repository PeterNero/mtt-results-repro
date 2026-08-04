"""Audit Route-C I10 payload contract import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "routec_i10_payload_contract_import.candidate.json"
CERT = ROOT / "certificates" / "routec_i10_payload_contract_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "RouteC_I10PayloadContract_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_routec_i10_payload_contract.py"

STATUS = "ROUTEC_I10_PAYLOAD_CONTRACT_IMPORTED_VALUES_OPEN"
NEXT = "MTT_Selected_I10_PayloadCertificate_or_IndependentQuadratureValuesFill_v1"


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

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["theorem"]["closure_claimed"] is False, "closure overclaimed")
    require(all(data["checks"].values()), "not all checks passed")

    summary = data["i10_payload_contract_summary"]
    require(summary["route_A_i10_payload_contract_built"] is True, "Route A contract missing")
    require(summary["route_A_accepted_now"] is False, "Route A overaccepted")
    require(summary["route_B_quadrature_tables_staged"] is True, "Route B tables missing")
    require(summary["route_B_values_filled_now"] is False, "Route B overfilled")
    require(summary["closure_claimed_now"] is False, "closure overclaimed")
    require(summary["expected_minimum_counts"] == {
        "hessian_source_rows": 2,
        "primitive_contraction_rows": 18,
        "sector_matrix_rows": 18,
        "zero_mode_basis_rows": 8,
    }, "expected counts mismatch")
    require(summary["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "ATA mismatch")
    require(summary["A_transpose_b"] == [12.0, 12.0], "ATb mismatch")
    require(summary["deltaTheta_C1"] == [1.0, 1.0], "delta mismatch")

    packets = data["upstream_packets"]
    require(packets["i10_minimizer_trace_c1_payload_contract"]["promotion_rule"]["current_all_payload_certificates_verified"] is False, "payload overaccepted")
    require(packets["quadrature_values_staging_tables"]["values_filled_now"] is False, "quadrature overfilled")
    require(packets["closure_acceptance_manifest"]["closure_claimed_now"] is False, "manifest closure overclaimed")

    for key in [
        "claims_route_A_accepted",
        "claims_route_B_accepted",
        "claims_I10_proved",
        "claims_unpatched_A_selected",
        "claims_unpatched_b_selected",
        "claims_unpatched_deltaTheta_C1",
        "claims_unpatched_SM_dynamic_closure",
        "claims_true_SM_equivalence",
        "uses_observed_or_benchmark_inputs",
        "target_fitting_used",
    ]:
        require(data["guardrails"][key] is False, f"guardrail overclaimed: {key}")

    require("machine-checkable" in note, "note missing summary")
    require(NEXT in note, "note missing next artifact")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
