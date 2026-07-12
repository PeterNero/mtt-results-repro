"""Audit electroweak gauge-kinetic/RG or BN27 repair frontier packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_electroweakgaugekineticnormalizationandrg_or_bn27repairsourceamendment_or_directhkrow"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
EW_LANE = PACKET_DIR / "electroweak_gaugekinetic_rg_route_lane.packet.json"
BN27_LANE = PACKET_DIR / "bn27_repair_sourceamendment_lane.packet.json"
NEXT_CUTSET = PACKET_DIR / "next_cutset_after_ew_rg_bn27_repair.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_ElectroweakGaugeKineticNormalizationAndRGScheme_or_BN27RepairSourceAmendment_or_DirectHKRow_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_ELECTROWEAKGAUGEKINETICNORMALIZATIONANDRG_OR_BN27REPAIRSOURCEAMENDMENT_"
    "ROUTE_SELECTED_KERNEL_VALUES_OPEN"
)
NEXT = "MTT_Selected_HeteroticStromingerElectroweakThresholdKernel_or_BN27DirectCarrierSourceTheorem_or_DirectHKRow_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("closure_claimed") is True, f"{label} closure flag")
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    ew = load(EW_LANE)
    bn27 = load(BN27_LANE)
    cutset = load(NEXT_CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("EW lane", ew),
        ("BN27 lane", bn27),
        ("next cutset", cutset),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "certificate status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(cert["next_required_artifact"] == NEXT, "certificate next")
    require(data["theorem"]["proved"] is True, "candidate theorem")
    require(cert["theorem_proved"] is True, "certificate theorem")
    require(data["full_no_knob_closure_claimed"] is False, "candidate no-knob")
    require(data["true_SM_equivalence_claimed"] is False, "candidate true SM")

    decision = data["closure_decision"]
    for key in [
        "strict_primary_route_selected",
        "internal_lambda_12_available",
        "electroweak_matching_interface_built",
        "BN27_logdet_implication_DAG_closed_conditionally",
        "BN27_source_amendment_template_built",
        "BN27_minimal_source_amendment_plan_built",
        "direct_HK_exit_still_allowed",
    ]:
        require(decision[key] is True, f"decision support missing {key}")
    require(decision["strict_primary_route"] == "B_flux_strominger_threshold", "primary route")
    require(decision["internal_lambda_12_value"] == 2.6179362173268497, "internal lambda")
    require(decision["internal_Delta_G12_value"] == 0.08450302790361214, "internal delta")
    require(decision["accepted_selected_K_source_row_count"] == 9, "K count")
    require(decision["selected_K_threshold_row_count_required"] == 10, "required K")
    for key in [
        "gaugekinetic_normalization_closed",
        "matching_scale_closed",
        "RG_scheme_closed",
        "measured_electroweak_closure",
        "ctwist_period_selector_found",
        "BN27_source_identity_closed",
        "BN27_kernel_trace_ownership_closed",
        "selected_R_H_RG_emitted",
        "selected_K_threshold_Omega_H_lambda",
        "strict_H_K_threshold_row_emitted",
        "full_no_knob_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"decision overclosed {key}")

    require(ew["strict_primary_route_selected"] == "B_flux_strominger_threshold", "EW primary route")
    require(ew["internal_lambda_12_available"] is True, "lambda available")
    require(ew["internal_lambda_12_value"] == 2.6179362173268497, "EW lambda")
    require(ew["internal_Delta_G12_value"] == 0.08450302790361214, "EW delta")
    for key in [
        "gaugekinetic_normalization_closed",
        "matching_scale_closed",
        "RG_scheme_closed",
        "measured_electroweak_closure",
    ]:
        require(ew[key] is False, f"EW overclosed {key}")
    match = ew["matching_interface"]
    require(match["electroweak_matching_interface"] == "BUILT", "matching interface")
    require(match["Qa_SU3_internal_payload_for_matching"] == "CLOSED_LOG_2008", "matching payload")
    require(match["absolute_gauge_normalization_K_gauge"] == "OPEN", "K gauge open")
    require(match["U1_SU2_same_scheme_payloads"] == "OPEN", "old U1/SU2 interface open")
    require(match["no_knob_measured_electroweak_closure_now"] is False, "EW no-knob")
    ctwist = ew["ctwist_scalar_gate"]
    require(ctwist["period_selector_found"] is False, "period selector")
    require(ctwist["period_selector_open_not_contradicted"] is True, "period open")

    logdet = bn27["logdet_emission"]
    require(logdet["attempt_executed"] is True, "logdet attempt")
    require(logdet["conditional_implication_theorem_closed"] is True, "implication DAG")
    require(logdet["source_amendment_template_built"] is True, "source amendment")
    for key in [
        "source_owned_logdet_closed",
        "BN27_source_identity_closed",
        "direct_source_theorem_closed",
        "connection_or_smooth_source_closed",
        "kernel_trace_ownership_closed",
        "oriented_logdet_promoted",
    ]:
        require(logdet[key] is False, f"logdet overclosed {key}")
    repair = bn27["repair_attack"]
    require(repair["repair_attack_executed"] is True, "repair")
    require(repair["primary_lane"] == "selected_connection_values_alternative", "primary repair")
    require(repair["projective_rhoE_primary"] is True, "projective primary")
    require(repair["projective_finite_candidate_available"] is True, "projective candidate")
    for key in [
        "projective_BN27_lift_closed",
        "BN27_domain_emission_closed",
        "source_branch_identity_closed",
    ]:
        require(repair[key] is False, f"repair overclosed {key}")
    discovery = bn27["sourceleaf_discovery"]
    require(discovery["corpus_discovery_executed"] is True, "discovery")
    require(discovery["support_only_matches_found"] is True, "support matches")
    require(discovery["direct_existing_packet_found"] is False, "direct packet")
    require(discovery["smooth_existing_packet_found"] is False, "smooth packet")
    require(discovery["minimal_source_amendment_plan_built"] is True, "amendment plan")
    require(discovery["next_lane"] == "direct_carrier_constructive_attempt", "next lane")

    require(
        cutset["status"] == "NEXT_FRONTIER_STROMINGER_EW_KERNEL_OR_BN27_DIRECT_CARRIER_OR_DIRECT_HK_ROW",
        "cutset status",
    )
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    for phrase in [
        "strict electroweak no-knob primary route selected as B_flux/Strominger threshold kernel",
        "BN27 source-owned logdet implication DAG closed conditionally",
        "minimal source amendment plan built with direct carrier constructive attempt",
    ]:
        require(phrase in cutset["closed_here"], f"closed phrase missing {phrase}")
    for phrase in [
        "selected heterotic/Strominger electroweak threshold kernel values",
        "physical gauge kinetic normalization K_gauge",
        "BN27 direct carrier/source theorem or selected connection export",
        "direct source-native K_threshold.Omega_H.lambda",
    ]:
        require(phrase in cutset["still_open"], f"open phrase missing {phrase}")

    for phrase in [
        "ElectroweakGaugeKineticRGOrBN27RepairReductionTheorem",
        "`B_flux/Strominger threshold`",
        "`1/g_Qa^2(mu_match) = K_gauge * log(2008)`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: EW route selected and BN27 repair implication ready; kernel values, physical RG, and H row open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
