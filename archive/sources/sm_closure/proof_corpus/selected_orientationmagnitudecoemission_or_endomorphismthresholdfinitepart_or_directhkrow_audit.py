"""Audit orientation/magnitude co-emission or endomorphism finitepart frontier packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_orientationmagnitudecoemission_or_endomorphismthresholdfinitepart_or_directhkrow"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
COEMISSION_GATE = PACKET_DIR / "orientation_magnitude_coemission_reduction.packet.json"
OPERATOR_GATE = PACKET_DIR / "endomorphism_threshold_finitepart_reduction.packet.json"
CTAU_GATE = PACKET_DIR / "ctau_phifin_threshold_identity_gate.packet.json"
NEXT_CONTRACT = PACKET_DIR / "next_frontier_acceptance_contract.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_OrientationMagnitudeCoEmission_or_EndomorphismThresholdFinitePart_or_DirectHKRow_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_ORIENTATIONMAGNITUDECOEMISSION_OR_ENDOMORPHISMTHRESHOLDFINITEPART_"
    "CTAU_SIGNED_CLOSED_MAGNITUDE_SOURCE_IDENTITY_OPEN"
)
NEXT = "MTT_Selected_FiniteRhoEToOrientedBNFunctor_or_SmoothEQaRepresentative_or_DirectHKRow_v1"


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
    coemission = load(COEMISSION_GATE)
    operator = load(OPERATOR_GATE)
    ctau = load(CTAU_GATE)
    contract = load(NEXT_CONTRACT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("coemission gate", coemission),
        ("operator gate", operator),
        ("ctau gate", ctau),
        ("contract", contract),
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
        "five_field_coemission_request_reduced_to_single_leaf",
        "finite_projective_rhoE_source_value_inserted",
        "internal_projective_rhoE_finitepart_log2008_closed",
        "label_embedding_27x11_built",
        "rhoE_character_intertwines",
        "C_tau_source_selected_as_BN_operator",
        "C_tau_signed_intertwiner_closed",
        "C_tau_positive_finitepart_convention_closed",
        "C_tau_PhiFin_commutation_closed",
        "oriented_PhiFin_finitepart_exactly_computed",
    ]:
        require(decision[key] is True, f"decision support missing {key}")
    for key in [
        "same_source_orientation_magnitude_branch_identity_closed",
        "finite_rhoE_to_oriented_BN_functor_closed",
        "physical_threshold_normalization_closed",
        "smooth_operator_identity_closed",
        "endomorphism_value_packet_filled",
        "selected_PhiFin_laplacian_intertwines_internal_signed_operator",
        "C_tau_nonzero_threshold_magnitude_source",
        "oriented_logdet_promoted",
        "smooth_EQa_constructed",
        "selected_K_threshold_Omega_H_lambda",
        "strict_H_K_threshold_row_emitted",
        "full_no_knob_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"decision overclosed {key}")
    require(decision["accepted_selected_K_source_row_count"] == 9, "K count")
    require(decision["selected_K_threshold_row_count_required"] == 10, "K required")

    support = coemission["support_reduction"]
    require(support["support_reduction_closed"] is True, "coemission support")
    require(support["closed_support_count"] == 10, "coemission support count")
    require(support["support_required_count"] == 10, "coemission required")
    branch = coemission["branch_identity_fill"]
    require(branch["minimal_source_certificate_fill_attempted"] is True, "branch fill")
    require(branch["filled_count"] == 1, "branch filled count")
    require(branch["required_count"] == 7, "branch required count")
    require(branch["minimal_new_leaf"] == "selected_BN27_source_domain_bridge", "minimal leaf")
    bn27 = coemission["bn27_constructive_route"]
    require(bn27["conditional_replay_ready"] is True, "BN27 conditional replay")
    require(bn27["direct_open_statement_count"] == 6, "BN27 direct opens")
    require(bn27["connection_open_table_count"] == 8, "BN27 table opens")
    finite_rhoe = coemission["finite_rhoe_value_insertion"]
    require(finite_rhoe["finite_projective_rhoE_source_value_inserted"] is True, "finite rhoE insertion")
    require(finite_rhoe["EndE_or_rhoE_to_oriented_BN_functor_closed"] is False, "rhoe functor not closed")

    internal = operator["internal_projective_rhoe_finitepart"]
    require(internal["selected_internal_threshold_finitepart_closed"] is True, "internal finitepart")
    require(internal["Delta_selected_internal_exact"] == "log(2008)", "internal log")
    require(internal["determinant"] == 2008, "internal determinant")
    require(internal["E_Qa_computed"] is False, "E_Qa not computed")
    physical = operator["physical_normalization"]
    require(physical["internal_interface_closed"] is True, "internal interface")
    require(physical["best_next_lane"] == "smooth_operator_identity_bridge", "best lane")
    bundle = operator["bundle_trace_policy"]
    require(bundle["finite_internal_trace_and_quotient_policy_closed"] is True, "bundle trace")
    require(bundle["standard_embedding_route_retired_for_current_branch"] is True, "standard embedding retired")
    end = operator["endomorphism_value_packet"]
    require(end["template_filled_enough_for_determinant"] is False, "endomorphism not filled")
    require(end["selected_values_available"] is False, "endomorphism values unavailable")

    label = ctau["label_embedding"]
    require(label["label_embedding_candidate_built"] is True, "label embedding")
    require(label["rhoE_character_intertwines"] is True, "rhoE intertwines")
    require(label["D_E_or_EQa_intertwines"] is False, "D/EQa not intertwined")
    central = ctau["central_rank_intertwiner"]
    require(central["central_rank_operator_candidate_intertwines"] is True, "central intertwines")
    require(central["C_tau_source_selected_as_BN_operator"] is True, "C_tau source")
    require(central["operator_identity_closed_for_signed_layer"] is True, "signed identity")
    require(central["positive_finitepart_for_C_tau_closed"] is False, "source ctau finitepart not before convention")
    chiral = ctau["ctau_chiral_positive_convention"]
    require(chiral["ctau_positive_finitepart_convention_closed"] is True, "chiral convention")
    require(chiral["ctau_logdet_value_full_BN"] == 0.0, "ctau logdet")
    require(chiral["ctau_eta_value_full_BN"] == 0, "ctau eta")
    require(chiral["ctau_supplies_orientation"] is True, "ctau orientation")
    require(chiral["ctau_supplies_nonzero_threshold_magnitude"] is False, "ctau no magnitude")
    magnitude = ctau["phifin_magnitude"]
    require(magnitude["commutation_or_simultaneous_functional_calculus_closed"] is True, "commutation")
    require(magnitude["oriented_table_magnitude_finitepart_computed"] is True, "magnitude finitepart")
    require(magnitude["oriented_abs_sector_logdet_exact"] == "log(92160000)", "oriented log")
    require(magnitude["full_positive_logdet_exact"] == "log(884736000000)", "full log")
    threshold = ctau["threshold_identity_fill"]
    require(threshold["fill_attempt_executed"] is True, "threshold fill")
    require(threshold["closed_required_leaf_count"] == 0, "threshold closed leaves")
    require(threshold["required_leaf_count"] == 6, "threshold required leaves")
    require(threshold["heterotic_threshold_magnitude_promoted"] is False, "threshold not promoted")

    require(contract["status"] == "FINITE_RHOE_TO_ORIENTED_BN_OR_SMOOTH_EQA_REPRESENTATIVE_REQUIRED", "contract status")
    require(contract["strict_K_threshold_count"] == {"accepted": 9, "required": 10}, "contract count")
    for phrase in [
        "C_tau selected as BN signed central-rank operator",
        "P^T C_tau P signed operator identity closed",
        "oriented Phi_fin finitepart table computed exactly",
    ]:
        require(phrase in contract["closed_now"], f"closed phrase missing {phrase}")
    for phrase in [
        "finite rhoE to oriented BN functor",
        "smooth projective representative or smooth E_Qa quotient",
        "direct K_threshold.Omega_H.lambda source row",
    ]:
        require(any(phrase in item for item in contract["still_open"]), f"open phrase missing {phrase}")

    for phrase in [
        "OrientationMagnitudeOrEndomorphismFinitepartFrontierTheorem",
        "`Delta_selected_internal = log(2008)`",
        "`P^T C_tau P`",
        "`log(92160000)`",
        "`9/10`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: C_tau signed source closed, internal finiteparts closed, Phi_fin magnitude exact; finite rhoE->BN/smooth EQa bridge remains."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
