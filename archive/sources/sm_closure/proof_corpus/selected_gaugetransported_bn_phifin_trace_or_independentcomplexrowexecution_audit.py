"""Audit gauge-transported BN/PhiFin trace or independent complex-row execution."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_gaugetransported_bn_phifin_trace_or_independentcomplexrowexecution"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
TRACE = PACKET_DIR / "gauge_transported_trace_closure.packet.json"
PROMOTION = PACKET_DIR / "psm_c1_02_source_promotion_closure.packet.json"
NEXT = PACKET_DIR / "post_source_fullsm_gap.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_GaugeTransported_BN_PhiFin_Trace_or_IndependentComplexRowExecution_v1.md"

STATUS = (
    "MTT_SELECTED_GAUGETRANSPORTED_BN_PHIFIN_TRACE_OR_INDEPENDENTCOMPLEXROWEXECUTION_"
    "ROUTE_A_SOURCE_PROMOTION_CLOSED_FULLSM_OPEN"
)
NEXT_ARTIFACT = "MTT_Selected_PostSourcePromotionFullSMGapAudit_or_DotDAlpha1MatterRoutingClosure_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def guard(packet: dict[str, Any], label: str) -> None:
    require(packet.get("closure_claimed") is True, f"{label} closure")
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    trace = load(TRACE)
    promotion = load(PROMOTION)
    next_packet = load(NEXT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", candidate),
        ("trace", trace),
        ("promotion", promotion),
        ("next", next_packet),
        ("cert", cert),
    ]:
        guard(packet, label)

    require(candidate["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "cert status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["theorem"]["name"] == "GaugeTransportedBNPhiFinTraceOrIndependentComplexRowExecutionTheorem", "theorem")
    require(cert["theorem_proved"] is True, "cert theorem")
    require(candidate["next_required_artifact"] == NEXT_ARTIFACT, "candidate next")
    require(next_packet["next_required_artifact"] == NEXT_ARTIFACT, "next packet")
    require(cert["next_required_artifact"] == NEXT_ARTIFACT, "cert next")

    require(trace["status"] == "GAUGE_TRANSPORTED_BN_PHIFIN_TRACE_PROVED", "trace status")
    require(trace["upstream_primary_target"] is True, "upstream primary target")
    require(trace["gauge_transported_PhiFin_trace"] is True, "gauge trace")
    require(trace["rank_gap_Riesz_Green_transfer_by_conjugation"] is True, "rank gap transfer")
    require(trace["selected_functional_projectors"] is True, "projectors")
    require(trace["selected_functional_zero_mode_bases"] is True, "zero modes")
    require(trace["functional_rho_s_promotion"] is True, "rho_s")

    require(promotion["status"] == "PSM_C1_02_SOURCE_PROMOTION_CLOSED_BY_TRANSPORT_IMPORT", "promotion status")
    require(promotion["PSM_C1_02_unpatched_source_promotion_closed"] is True, "PSM source promotion")
    require(promotion["Route_A_transport_closed_import_validates"] is True, "Route A import")
    require(promotion["Route_B_independent_rows_required_for_PSM_closure"] is False, "Route B should be retired")
    require(promotion["A_selected_promoted"] is True, "A selected")
    require(promotion["b_selected_promoted"] is True, "b selected")
    require(promotion["deltaTheta_C1_promoted"] is True, "deltaTheta")
    require(promotion["narrowed_phifinc1_emission_validator_passes"] is True, "PhiFin validator")
    require(promotion["psm_c1_02_source_promotion_validator_passes"] is True, "PSM validator")

    require(next_packet["status"] == "POST_SOURCE_FULLSM_GAP_SELECTED", "next status")
    require(next_packet["post_source_fullsm_gap_selected"] is True, "post-source gap")
    require(next_packet["full_SM_no_knob_closed"] is False, "no-knob overclosed")
    require(next_packet["true_SM_equivalence_closed"] is False, "true SM overclosed")

    decision = candidate["closure_decision"]
    require(decision["gauge_transported_BN_PhiFin_trace_closed"] is True, "decision trace")
    require(decision["PSM_C1_02_unpatched_source_promotion_closed"] is True, "decision source promotion")
    require(decision["A_selected_promoted"] is True, "decision A")
    require(decision["b_selected_promoted"] is True, "decision b")
    require(decision["deltaTheta_C1_promoted"] is True, "decision delta")
    require(decision["post_source_fullsm_gap_selected"] is True, "decision post-source")
    for key in [
        "Route_B_independent_rows_required_for_PSM_closure",
        "actual_dynamic_QaSU3_payload_values_closed",
        "Yukawa_mass_mixing_value_closure_without_proxy_fitting",
        "selected_dotD_alpha1_with_transport_derivative",
        "selected_matter_slot_routing_and_normalization",
        "final_no_knob_constants_and_covariance_RG_linkage",
        "true_SM_equivalence_closed",
        "full_SM_no_knob_closed",
    ]:
        require(decision[key] is False, f"{key} overclosed")

    for phrase in [
        "gauge transported BN/PhiFin trace closed          true",
        "PSM-C1-02 unpatched source promotion closed       true",
        "A_selected promoted                              true",
        "deltaTheta_C1 promoted                           true",
        "true SM equivalence                               false",
        NEXT_ARTIFACT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
