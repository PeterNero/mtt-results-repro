"""Audit Route-C Weyl variation source-principle construction."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_routec_weylvariation_sourceprinciple_or_kernelclosure"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PRINCIPLE = PACKET_DIR / "routec_weyl_variation_principle_candidate.packet.json"
PROMOTION = PACKET_DIR / "routec_kernel_promotion_test.packet.json"
VALIDATOR_RESULT = PACKET_DIR / "strict_kernel_validator_result.packet.json"
DECISION = PACKET_DIR / "routec_decision_and_next_gate.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_RouteC_WeylVariation_SourcePrinciple_or_KernelClosure_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_ROUTEC_WEYLVARIATION_SOURCEPRINCIPLE_BUILT_KERNEL_SOURCE_OPEN"
NEXT = "MTT_Selected_WeylVariationActionPrinciple_Derivation_or_ExplicitInsertion_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict) -> None:
    require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
    require(packet.get("target_fitting_used") is False, "target fitting violation")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    principle = load(PRINCIPLE)
    promotion = load(PROMOTION)
    validator = load(VALIDATOR_RESULT)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")

    require(principle["status"] == "ROUTE_C_PRINCIPLE_CANDIDATE_BUILT_NOT_DERIVED", "principle status mismatch")
    require(principle["proved_now"] is False, "principle overproved")
    support = principle["support_imported"]
    for key in [
        "source_level_weyl_carrier_selected",
        "static_source_selector_selected",
        "active_shift_selected",
        "static_source_map_candidate_constructed",
        "formal_hessian_target_identified",
    ]:
        require(support[key] is True, f"support missing: {key}")
    selection = principle["source_selection_attempt"]
    for key in [
        "source_map_selected_now",
        "physical_projector_application_promoted_now",
        "phase_R_Z_selected_now",
        "shift_R_X_selected_now",
        "b_source_emitted_now",
    ]:
        require(selection[key] is False, f"selection overclaimed: {key}")

    require(promotion["status"] == "ROUTE_C_PROMOTION_REJECTED_PRINCIPLE_NOT_SELECTED", "promotion status mismatch")
    require(promotion["same_branch"] is True, "same branch lost")
    for key in [
        "selected_variation_functional",
        "same_source_hessian",
        "sector_functor",
        "independence_certificate",
    ]:
        require(promotion[key] is False, f"kernel field overclaimed: {key}")
        require(promotion["conditional_witness_if_principle_inserted_or_derived"][key] is True, f"conditional missing: {key}")
    require(promotion["locked_target_values_used_as_source"] is False, "locked target used as source")
    require(promotion["residual_projector_replay_used_as_source"] is False, "residual replay used as source")
    require(len(promotion["attached_source_evidence"]) == 4, "evidence count mismatch")
    for item in promotion["attached_source_evidence"]:
        require(item["promotes_source"] is False, "support evidence promoted as source")

    require(validator["ok"] is False, "strict kernel validator should reject")
    require(validator["exit_code"] == 1, "validator exit mismatch")
    require(any("missing source-kernel fields" in line for line in validator["stderr"]), "validator missing field error absent")

    require(decision["status"] == "ROUTE_C_SUPPORT_MAXIMIZED_NEW_PRINCIPLE_OR_DERIVATION_REQUIRED", "decision status mismatch")
    require(decision["route_C_promoted_now"] is False, "Route C overpromoted")
    require(decision["strict_kernel_validator_ok"] is False, "decision validator overpassed")
    require(decision["latest_countermodel_blocks_support_only_proof"] is True, "countermodel guard lost")
    require(decision["best_current_final_source_emission_validates"] is False, "best current final source overvalidated")
    for key, value in decision["what_would_close_if_principle_proved"].items():
        require(value is True, f"would-close implication missing: {key}")
    require(decision["superset_strategy"]["locked_target_used_only_as_postcheck"] is True, "locked target misuse")
    require(decision["superset_strategy"]["paths_used_as_free_parameters"] is False, "paths treated as knobs")

    require(data["theorem"]["proved"] is True, "support maximization theorem missing")
    require(data["closure_decision"]["route_C_kernel_closed"] is False, "Route C kernel overclosed")
    require(data["closure_decision"]["pre_residual_kernel_closed"] is False, "pre-residual kernel overclosed")
    require(data["closure_decision"]["unpatched_dynamic_C1_closed"] is False, "unpatched dynamic C1 overclosed")
    for key in [
        "route_C_principle_candidate_constructed",
        "route_C_support_maximized",
        "strict_kernel_validator_rejection_preserved",
        "next_principle_derivation_gate_named",
    ]:
        require(data["what_closes_now"][key] is True, f"achievement missing: {key}")

    require("SelectedWeylVariationActionPrinciple" in note, "note missing principle")
    require(NEXT in note, "note missing next target")

    for packet in [data, principle, promotion, decision, cert]:
        guard(packet)

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
