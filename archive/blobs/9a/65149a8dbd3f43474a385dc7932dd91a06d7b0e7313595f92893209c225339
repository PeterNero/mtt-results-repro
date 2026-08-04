"""Audit heterotic/Strominger EW kernel or BN27 direct carrier frontier packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_heteroticstromingerewthresholdkernel_or_bn27directcarriersourcetheorem_or_directhkrow"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
EW_LANE = PACKET_DIR / "strominger_ew_kernel_value_lane.packet.json"
BN27_LANE = PACKET_DIR / "bn27_direct_carrier_full_orbit_lane.packet.json"
NEXT_CUTSET = PACKET_DIR / "next_cutset_after_strominger_kernel_bn27_carrier.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HeteroticStromingerElectroweakThresholdKernel_or_BN27DirectCarrierSourceTheorem_or_DirectHKRow_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_HETEROTICSTROMINGEREWTHRESHOLDKERNEL_OR_BN27DIRECTCARRIERSOURCETHEOREM_"
    "VALUES_REDUCED_TO_THRESHOLD_OPERATOR_TORSION_OR_FULL_ORBIT"
)
NEXT = "MTT_Selected_HeteroticStromingerSourceOperatorOrLocalSystemTorsion_or_FullFourierOrbitSourceEmission_or_DirectHKRow_v1"


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
        "tree_level_gauge_kinetic_slot_filled",
        "EW_kernel_values_reduced_to_operator_or_torsion",
        "internal_lambda_12_retired_as_physical_threshold_source",
        "BN27_orientation_functor_closed",
        "BN27_direct_carrier_reduced_to_full_orbit",
        "BN27_11_label_shadow_insufficient",
        "direct_HK_exit_still_allowed",
    ]:
        require(decision[key] is True, f"decision support missing {key}")
    require(decision["BN27_missing_multiplier"] == 5760000, "missing multiplier")
    require(decision["accepted_selected_K_source_row_count"] == 9, "K count")
    require(decision["selected_K_threshold_row_count_required"] == 10, "required K")
    for key in [
        "selected_heterotic_strominger_kernel_closed",
        "analytic_torsion_or_threshold_operator_closed",
        "physical_normalization_closed",
        "matching_scale_closed",
        "RG_scheme_closed",
        "BN27_full_oriented_positive_orbit_closed",
        "BN27_finitepart_trace_identity_closed",
        "selected_R_H_RG_emitted",
        "selected_K_threshold_Omega_H_lambda",
        "strict_H_K_threshold_row_emitted",
        "full_no_knob_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"decision overclosed {key}")

    kfill = ew["kernel_fill_attempt"]
    require(kfill["tree_level_gauge_kinetic_slot_filled"] is True, "tree-level f")
    require(kfill["internal_lambda_12_carried"] is True, "lambda carried")
    require(kfill["internal_lambda_12_value"] == 2.6179362173268497, "lambda value")
    for key in [
        "selected_heterotic_strominger_kernel_closed",
        "source_identity_selected_for_EW_kernel",
        "analytic_torsion_or_threshold_operator_closed",
        "stack_threshold_determinants_closed",
        "physical_normalization_closed",
        "matching_scale_closed",
        "RG_scheme_closed",
        "measured_electroweak_closure",
    ]:
        require(kfill[key] is False, f"kernel overclosed {key}")
    payload = ew["payload_reduction"]
    require(payload["payload_closed"] is False, "payload closed")
    require(payload["strict_no_knob_route_still_live"] is True, "strict route live")
    require(payload["internal_lambda_12_preserved"] is True, "lambda preserved")
    require(payload["retire_internal_replay_as_physical_threshold_source"] is True, "retire replay")
    require(payload["primary_next_exit"] == "C_hym_monad_threshold_operator", "primary exit")
    require(payload["parallel_next_exit"] == "B_ray_singer_or_reidemeister_local_system", "parallel exit")
    require(ew["minimal_payload"]["status"] == "OPEN_SELECTED_THRESHOLD_OPERATOR_OR_TORSION_REQUIRED", "minimal payload")

    sourceleaf = bn27["sourceleaf"]
    require(sourceleaf["source_leaf_attack_executed"] is True, "sourceleaf attack")
    require(sourceleaf["source_theorem_request_built"] is True, "source theorem request")
    require(sourceleaf["direct_first_open_leaf"] == "source_emits_oriented_BN_carrier", "direct open")
    require(sourceleaf["smooth_first_open_leaf"] == "selected_bundle_connection_A", "smooth open")
    require(sourceleaf["direct_carrier_leaf_closed"] is False, "direct carrier leaf")
    require(sourceleaf["bundle_A_leaf_closed"] is False, "bundle A")
    require(sourceleaf["oriented_logdet_promoted"] is False, "sourceleaf logdet")
    attempt = bn27["constructive_attempt"]
    require(attempt["constructive_attempt_executed"] is True, "carrier attempt")
    require(attempt["orientation_functor_closed"] is True, "orientation functor")
    require(attempt["new_minimal_leaf"] == "source_emits_full_oriented_positive_fourier_orbit", "minimal leaf")
    for key in [
        "positive_magnitude_functor_closed",
        "source_emits_oriented_BN_carrier",
        "direct_carrier_theorem_closed",
        "full_oriented_positive_orbit_closed",
        "finitepart_trace_identity_closed",
        "oriented_logdet_promoted",
    ]:
        require(attempt[key] is False, f"carrier overclosed {key}")
    orbit = bn27["orbit_arithmetic"]
    require(orbit["required_full_orbit_product"] == "9600*9600", "full product")
    require(orbit["required_full_orbit_logdet"] == "log(92160000)", "full logdet")
    require(orbit["embedded_11_label_shadow_product"] == 16, "shadow product")
    require(orbit["missing_multiplier"] == 5760000, "orbit multiplier")
    require(orbit["report_status"] == "FULL_ORBIT_SOURCE_EMISSION_REQUIRED", "report status")

    require(
        cutset["status"] == "NEXT_FRONTIER_STROMINGER_OPERATOR_TORSION_OR_FULL_FOURIER_ORBIT_OR_DIRECT_HK_ROW",
        "cutset status",
    )
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    for phrase in [
        "EW kernel value frontier reduced to source-selected HYM/monad threshold operator or acyclic local-system torsion",
        "BN27 positive magnitude requires full oriented positive Fourier orbit",
        "11-label shadow product 16 identified as insufficient against full product 9600*9600",
    ]:
        require(phrase in cutset["closed_here"], f"closed phrase missing {phrase}")
    for phrase in [
        "source-selected HYM/monad Laplace-type threshold operator",
        "source-selected acyclic local-system torsion computation",
        "source emits full oriented positive Fourier orbit",
        "direct source-native K_threshold.Omega_H.lambda",
    ]:
        require(any(phrase in item for item in cutset["still_open"]), f"open phrase missing {phrase}")

    for phrase in [
        "StromingerThresholdKernelOrBN27FullOrbitReductionTheorem",
        "`9600*9600`",
        "`5760000`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: Strominger EW values reduced to operator/torsion; BN27 carrier reduced to full orbit; H row open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
