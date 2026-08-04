"""Audit Route-C differentiated PhiFinC1 contract import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "routec_differentiated_phifinc1_contract_import.candidate.json"
CERT = ROOT / "certificates" / "routec_differentiated_phifinc1_contract_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "RouteC_DifferentiatedPhiFinC1_Contract_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_routec_differentiated_phifinc1_contract.py"

STATUS = "ROUTEC_DIFFERENTIATED_PHIFINC1_CONTRACT_IMPORTED_LANES_OPEN"
NEXT = "MTT_Selected_ResidualProjectorAxiomInsertion_or_GalerkinC1FirstExecution_v1"


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

    summary = data["differentiated_phifinc1_contract_summary"]
    require(summary["lane_A_axiom_contract_ready"] is True, "lane A not ready")
    require(summary["lane_A_inserted_now"] is False, "lane A inserted overclaimed")
    require(summary["lane_A_selected_now"] is False, "lane A selected overclaimed")
    require(summary["lane_A_would_emit_PhiFinC1_applies_Q"] is True, "lane A PhiFin implication missing")
    require(summary["lane_A_would_emit_b_source"] is True, "lane A b implication missing")
    require(summary["lane_B_galerkin_contract_ready"] is True, "lane B not ready")
    require(summary["lane_B_selected_source_verified"] is False, "lane B source oververified")
    require(summary["routed_total_residual_norm_sq"] == 12.0, "residual norm mismatch")
    require(summary["conditional_b_norm_sq"] == 24.0, "conditional b norm mismatch")
    require(summary["replay_rank"] == 2, "replay rank mismatch")
    require(summary["replay_A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "ATA mismatch")
    require(summary["replay_A_transpose_b"] == [12.0, 12.0], "ATb mismatch")
    require(summary["replay_deltaTheta_C1"] == [1.0, 1.0], "delta mismatch")

    upstream = data["upstream_differentiated_phifinc1_contract"]
    for key in [
        "derive_or_insert_residual_projector_axiom",
        "prove_selected_differentiated_PhiFinC1_application_rule",
        "emit_selected_b_source_vector",
        "run_honest_selected_Galerkin_C1_execution",
        "promote_A_selected",
        "promote_b_selected",
        "promote_deltaTheta_C1",
        "emit_sector_response_matrices",
        "SM_parity_dynamic_packet_closure",
        "true_SM_equivalence_closure",
        "full_no_knob_flavor_closure",
    ]:
        require(upstream["what_remains_open"][key] is True, f"remaining gate missing: {key}")
    for key in [
        "residual_projector_axiom_inserted_now",
        "differentiated_PhiFinC1_application_rule_proved_now",
        "honest_Galerkin_C1_execution_run_now",
        "A_selected_promoted",
        "b_selected_promoted",
        "deltaTheta_C1_promoted",
        "sector_response_matrices_promoted",
        "SM_parity_dynamic_packet_closed",
        "true_SM_equivalence_closed",
        "no_knob_flavor_constants_closed",
    ]:
        require(upstream["promotion_decision"][key] is False, f"promotion overclaimed: {key}")

    guard = data["guardrails"]
    for key in [
        "claims_residual_projector_axiom_inserted",
        "claims_differentiated_PhiFinC1_application_rule",
        "claims_honest_Galerkin_C1_execution",
        "claims_A_selected",
        "claims_b_selected",
        "claims_deltaTheta_C1",
        "claims_sector_response_matrices",
        "claims_SM_parity_dynamic_packet_closure",
        "claims_full_no_knob_flavor_closure",
        "uses_observed_or_benchmark_inputs",
        "target_fitting_used",
    ]:
        require(guard[key] is False, f"guardrail overclaimed: {key}")

    require("two-lane contract" in note, "note missing two-lane statement")
    require("Neither lane is selected yet" in note, "note missing lane caveat")
    require(NEXT in note, "note missing next artifact")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
