"""Audit minimizer-trace C1 payload theorem / quadrature values gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_minimizertracec1payloadtheorem_or_quadraturetablevalues"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PAYLOAD_CONTRACT = PACKET_DIR / "i10_minimizer_trace_c1_payload_contract.packet.json"
QUADRATURE_VALUES = PACKET_DIR / "quadrature_values_staging_tables.packet.json"
ACCEPTANCE_MANIFEST = PACKET_DIR / "closure_acceptance_manifest.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_MinimizerTraceC1PayloadTheorem_or_QuadratureTableValues_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_MINIMIZERTRACE_C1_PAYLOAD_OR_QUADRATURE_VALUES_CONTRACT_BUILT_OPEN"
NEXT = "MTT_Selected_I10_PayloadCertificate_or_IndependentQuadratureValuesFill_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    payload = load(PAYLOAD_CONTRACT)
    quadrature = load(QUADRATURE_VALUES)
    manifest = load(ACCEPTANCE_MANIFEST)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")

    require(payload["theorem_slot"] == "I10_phifinc1_minimizes_c1_defect_functional", "payload theorem slot mismatch")
    required = payload["payload_certificate_required"]
    for key in [
        "selected_minimizer_trace_payload",
        "selected_c1_response_payload",
        "defect_functional_minimizer_payload",
    ]:
        require(required[key]["required"] is True, f"payload requirement missing: {key}")
        require(len(required[key]["must_emit"]) == 4, f"payload must_emit mismatch: {key}")
        require(len(required[key]["forbidden"]) == 2, f"payload guardrail mismatch: {key}")
    require(payload["promotion_rule"]["current_all_payload_certificates_verified"] is False, "payload overaccepted")

    require(quadrature["status"] == "TABLES_STAGED_VALUES_EMPTY", "quadrature status mismatch")
    require(quadrature["values_filled_now"] is False, "quadrature values overfilled")
    require(quadrature["expected_minimum_counts"]["zero_mode_basis_rows"] == 8, "zero-mode row count mismatch")
    require(quadrature["expected_minimum_counts"]["primitive_contraction_rows"] == 18, "primitive row count mismatch")
    require(quadrature["expected_minimum_counts"]["hessian_source_rows"] == 2, "hessian row count mismatch")
    require(quadrature["expected_minimum_counts"]["sector_matrix_rows"] == 18, "sector row count mismatch")
    for rows in quadrature["tables"].values():
        require(rows == [], "quadrature table unexpectedly filled")

    require(manifest["route_A_i10_payload_certificate"]["accepted_now"] is False, "route A overaccepted")
    require(manifest["route_B_independent_quadrature_values"]["accepted_now"] is False, "route B overaccepted")
    require(manifest["closure_claimed_now"] is False, "manifest closure overclaimed")
    require(manifest["replay_target_if_accepted"] == data["replay_if_route_A_or_B_accepted"], "replay mismatch")
    require("deltaTheta_solve_matches_replay" in manifest["route_B_independent_quadrature_values"]["required_checks"], "solve check missing")

    for key in [
        "I10_payload_certificate_schema_fixed",
        "independent_quadrature_value_tables_staged",
        "dual_route_acceptance_manifest_built",
        "unpatched_closure_conditions_are_machine_checkable",
        "observed_constants_excluded_as_selectors",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing: {key}")
    for key in [
        "selected_minimizer_trace_payload_verified",
        "selected_c1_response_payload_verified",
        "defect_functional_minimizer_payload_verified",
        "independent_quadrature_values_filled",
        "unpatched_SM_parity_dynamic_packet_closure",
        "true_SM_equivalence_closure",
    ]:
        require(data["what_remains_open"][key] is True, f"open flag missing: {key}")
    decision = data["promotion_decision"]
    for key in [
        "route_A_i10_payload_certificate_accepted",
        "route_B_independent_quadrature_values_accepted",
        "I10_proved",
        "unpatched_SM_parity_dynamic_packet_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"promotion overclaimed: {key}")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "reduction theorem missing")
    require(data["observed_data_used"] is False and data["target_fitting_used"] is False, "data guardrail violated")
    require(data["closure_claimed"] is False and data["unpatched_theorem_closure_claimed"] is False, "closure overclaimed")
    require("Route A" in note and "Route B" in note, "note missing route summary")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
