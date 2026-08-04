"""Audit source-operator/torsion plus full-Fourier co-emission frontier packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_heteroticstromingersourceoperator_or_localsystemtorsion_or_fullfourierorbit_or_directhkrow"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
OPERATOR_GATE = PACKET_DIR / "operator_torsion_source_gate.packet.json"
FOURIER_GATE = PACKET_DIR / "full_fourier_orbit_coemission_gate.packet.json"
ACCEPTANCE = PACKET_DIR / "remaining_acceptance_contract.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HeteroticStromingerSourceOperatorOrLocalSystemTorsion_or_FullFourierOrbitSourceEmission_or_DirectHKRow_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_HETEROTICSTROMINGERSOURCEOPERATOR_OR_LOCALSYSTEMTORSION_OR_FULLFOURIERORBIT_"
    "GATE_TIGHTENED_ENDOMORPHISM_PRIMARY_COEMISSION_OPEN"
)
NEXT = "MTT_Selected_OrientationMagnitudeCoEmission_or_EndomorphismThresholdFinitePart_or_DirectHKRow_v1"


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
    operator = load(OPERATOR_GATE)
    fourier = load(FOURIER_GATE)
    acceptance = load(ACCEPTANCE)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("operator gate", operator),
        ("Fourier gate", fourier),
        ("acceptance", acceptance),
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
        "ordinary_rank_one_torsion_route_closed_negative_for_q64",
        "compact_nil_scalar_proxy_rejected",
        "hym_printed_route_retired",
        "source_certified_endomorphism_operator_primary",
        "full_positive_fourier_orbit_selected_at_gap_layer_scope",
        "orientation_functor_closed",
        "trace_identity_closed_relative_to_coemission",
    ]:
        require(decision[key] is True, f"decision support missing {key}")
    require(decision["oriented_abs_sector_product"] == 92160000, "oriented product")
    require(decision["oriented_abs_sector_logdet_exact"] == "log(92160000)", "oriented logdet")
    require(decision["accepted_selected_K_source_row_count"] == 9, "K count")
    require(decision["selected_K_threshold_row_count_required"] == 10, "K required")
    for key in [
        "orientation_magnitude_coemission_closed",
        "oriented_logdet_promoted",
        "full_oriented_phi_fin_threshold_closed",
        "selected_threshold_operator_finite_part_emitted",
        "selected_local_system_torsion_finite_part_emitted",
        "selected_projective_twisted_module_response_emitted",
        "selected_physical_normalization_mu_rg_emitted",
        "selected_K_threshold_Omega_H_lambda",
        "strict_H_K_threshold_row_emitted",
        "full_no_knob_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"decision overclosed {key}")

    reduction = operator["threshold_payload_reduction"]
    require(reduction["payload_closed"] is False, "payload not closed")
    require(reduction["strict_no_knob_route_still_live"] is True, "strict route live")
    require(reduction["primary_next_exit"] == "C_hym_monad_threshold_operator", "primary exit")
    require(
        reduction["parallel_next_exit"] == "B_ray_singer_or_reidemeister_local_system",
        "parallel exit",
    )
    route = operator["post_hym_route_tightening"]
    require(route["ordinary_rank_one_torsion_route_closed_negative_for_q64"] is True, "rank one no-go")
    require(route["selected_primary_route"] == "source_certified_endomorphism_E_full_operator", "primary route")
    require(route["q64_projective_route_open_auxiliary"] is True, "q64 auxiliary")
    for forbidden in [
        "ordinary rank-one U1 local-system q64 character",
        "q64 phase as an SU3 scalar center element",
        "internal lambda_12 as physical threshold data",
    ]:
        require(forbidden in operator["rejected_value_exits_now"], f"forbidden missing {forbidden}")

    trace = fourier["trace_identity"]
    require(trace["identity_closed_relative_to_full_orbit_source"] is True, "trace relative")
    require(trace["oriented_abs_sector_product"] == 92160000, "trace product")
    require(trace["oriented_abs_sector_logdet_exact"] == "log(92160000)", "trace logdet")
    require(trace["plus_sector_count"] == 8, "plus count")
    require(trace["minus_sector_count"] == 8, "minus count")
    source = fourier["source_selection_tightening"]
    require(source["full_positive_fourier_orbit_selected_at_gap_layer_scope"] is True, "magnitude selected")
    require(source["routec_magnitude_source_selected_for_27mode_DE_gap_layer"] is True, "Route-C magnitude")
    require(source["orientation_functor_closed"] is True, "orientation functor")
    require(source["remaining_single_leaf"] == "same_source_orientation_magnitude_coemission", "leaf")
    for key in [
        "orientation_magnitude_coemission_closed",
        "full_oriented_phi_fin_threshold_closed",
        "oriented_logdet_promoted",
    ]:
        require(source[key] is False, f"Fourier overclosed {key}")
    for req in [
        "same_source_identity_between_routec_gap_layer_and_heterotic_oriented_phifin",
        "proof_C_tau_commutes_with_selected_routec_DE_as_source_operator",
        "finitepart_trace_identity_inherits_source_ownership",
    ]:
        require(req in fourier["coemission_contract"], f"coemission field missing {req}")

    require(acceptance["status"] == "TWO_EXITS_PLUS_DIRECT_HK_ROW_REMAIN", "acceptance status")
    require(acceptance["strict_K_threshold_count"] == {"accepted": 9, "required": 10}, "acceptance count")
    for phrase in [
        "ordinary rank-one torsion is closed negative for selected q64",
        "source-certified Endomorphism_E/full threshold operator is primary",
        "log(92160000) trace identity is algebraically closed relative to co-emission",
    ]:
        require(phrase in acceptance["closed_now"], f"closed phrase missing {phrase}")
    for phrase in [
        "same-source orientation-magnitude co-emission",
        "Endomorphism_E/Laplace-type threshold finite part",
        "direct K_threshold.Omega_H.lambda source row",
    ]:
        require(any(phrase in item for item in acceptance["still_open"]), f"open phrase missing {phrase}")

    for phrase in [
        "SourceOperatorTorsionOrFullFourierCoEmissionTighteningTheorem",
        "`log(92160000)`",
        "Ordinary rank-one local-system torsion is closed negative",
        "`9/10`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: operator/torsion route tightened; full-Fourier trace relative closed; co-emission and H row remain open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
