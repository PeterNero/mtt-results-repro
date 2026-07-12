"""Audit H gauge-kinetic normalization / mu_match or direct H K-row packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_hgaugekineticnormalizationmumatch_or_directhkthresholdrow"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ROUTE_IMPORT = PACKET_DIR / "heterotic_strominger_route_import.packet.json"
H_GATE = PACKET_DIR / "h_gauge_action_transport_gate.packet.json"
NEXT_CUTSET = PACKET_DIR / "next_cutset_after_h_gauge_action_layer.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HGaugeKineticNormalizationMuMatch_or_DirectHKThresholdRow_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_HGAUGEKINETICNORMALIZATIONMUMATCH_OR_DIRECTHKTHRESHOLDROW_"
    "HETEROTIC_STROMINGER_ROUTE_SELECTED_VALUES_OPEN"
)
NEXT = "MTT_Selected_HeteroticStromingerSourceOperatorTorsion_or_DirectHKRow_v1"


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
    route_import = load(ROUTE_IMPORT)
    h_gate = load(H_GATE)
    next_cutset = load(NEXT_CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("route import", route_import),
        ("H gate", h_gate),
        ("next cutset", next_cutset),
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
    require(decision["heterotic_strominger_primary_route_selected"] is True, "primary route")
    require(decision["tree_level_gauge_kinetic_slot_filled"] is True, "tree-level slot")
    require(decision["primary_HYM_monad_lane_selected"] is True, "HYM lane")
    require(decision["local_system_torsion_parallel_lane_open"] is True, "torsion lane")
    require(decision["direct_HK_exit_still_allowed"] is True, "direct H exit")
    require(decision["accepted_selected_K_source_row_count"] == 9, "K count")
    require(decision["selected_K_threshold_row_count_required"] == 10, "required K")
    for key in [
        "analytic_torsion_or_threshold_operator_closed",
        "physical_gauge_action_anchor_closed",
        "matching_scale_closed",
        "RG_scheme_closed",
        "selected_R_H_RG_emitted",
        "selected_K_threshold_Omega_H_lambda",
        "strict_H_K_threshold_row_emitted",
        "full_no_knob_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"decision overclosed {key}")

    imported = route_import["imported_route_discriminator"]
    require(imported["strict_primary_route_selected"] == "B_flux_strominger_threshold", "import primary")
    require(imported["internal_lambda_12_available"] is True, "lambda available")
    require(imported["internal_lambda_12_value"] == 2.6179362173268497, "lambda value")
    for key in ["gaugekinetic_normalization_closed", "matching_scale_closed", "RG_scheme_closed"]:
        require(imported[key] is False, f"route import overclosed {key}")

    kernel = route_import["heterotic_kernel_status"]
    require(kernel["tree_level_gauge_kinetic_slot_filled"] is True, "kernel tree slot")
    for key in [
        "physical_normalization_closed",
        "matching_scale_closed",
        "RG_scheme_closed",
        "analytic_torsion_or_threshold_operator_closed",
        "stack_threshold_determinants_closed",
    ]:
        require(kernel[key] is False, f"kernel overclosed {key}")

    payload = route_import["payload_reduction"]
    require(payload["primary_next_exit"] == "C_hym_monad_threshold_operator", "primary next exit")
    require(payload["parallel_next_exit"] == "B_ray_singer_or_reidemeister_local_system", "parallel next")
    require(payload["strict_no_knob_route_still_live"] is True, "route live")
    require(payload["payload_closed"] is False, "payload overclosed")
    require(payload["internal_replay_retired_as_physical_threshold_source"] is True, "internal replay retired")

    require(h_gate["status"] == "PRIMARY_HYM_MONAD_OPERATOR_LANE_SELECTED_H_ROW_OPEN", "H gate status")
    for key in [
        "selected_physical_gauge_action_anchor",
        "selected_mu_match",
        "selected_RG_scheme",
        "selected_R_H_RG",
        "selected_K_threshold_Omega_H_lambda",
    ]:
        require(h_gate["path_2_gate"][key] is False, f"H gate overclosed {key}")
    primary = h_gate["selected_primary_lane"]
    require(primary["lane_id"] == "C_hym_monad_threshold_operator", "primary lane id")
    require(primary["operator_domain_selected_for_next_gate"] is True, "operator domain")
    require(primary["selected_connection_candidate_found"] is True, "connection candidate")
    require(primary["mu_selected"] is False, "mu overclosed")
    require(primary["selected_spectrum_or_torsion_available"] is False, "spectrum overclosed")
    require(primary["next_required_artifact"] == "Selected_Qa_SU3_HYM_Delta_A_Mu_Spectrum_Computation_v1", "HYM next")
    parallel = h_gate["parallel_lane"]
    require(parallel["lane_id"] == "B_ray_singer_or_reidemeister_local_system", "parallel lane")
    require(parallel["selected_candidates_count"] == 0, "torsion candidates")
    require(parallel["computable_now"] is False, "torsion computable")
    require(h_gate["direct_HK_exit_still_allowed"] is True, "direct exit")

    require(
        next_cutset["status"] == "NEXT_FRONTIER_HETEROTIC_SOURCE_OPERATOR_TORSION_OR_DIRECT_HK",
        "next cutset status",
    )
    require(next_cutset["next_required_artifact"] == NEXT, "next cutset artifact")
    for phrase in [
        "gauge/action layer route discriminator imported",
        "heterotic/Strominger threshold-kernel route selected as primary strict route",
        "tree-level f=S slot filled but not promoted to one-loop threshold values",
        "analytic-torsion/threshold payload reduced to HYM operator lane or local-system torsion lane",
    ]:
        require(phrase in next_cutset["closed_here"], f"closed missing {phrase}")
    for phrase in [
        "HYM/monad Delta_A(mu) spectrum and selected mu",
        "positive spectrum, heat coefficients, or zeta/torsion finite part",
        "physical gauge/action normalization and matching scale",
        "RG scheme and threshold convention",
        "selected R_H^RG row and same-scheme Omega_H.lambda certificate",
        "direct source-native K_threshold.Omega_H.lambda",
    ]:
        require(phrase in next_cutset["still_open"], f"open missing {phrase}")

    for phrase in [
        "HGaugeKineticNormalizationMuMatchOrDirectHKThresholdRowTheorem",
        "heterotic/Strominger threshold-kernel route",
        "Tree-level gauge kinetic slot `f=S` filled",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: gauge/action layer selects heterotic/Strominger HYM threshold lane; H row remains open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
