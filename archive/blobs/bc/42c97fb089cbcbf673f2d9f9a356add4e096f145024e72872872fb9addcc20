"""Audit heterotic/Strominger source-operator torsion or direct H K-row packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_heteroticstromingersourceoperatortorsion_or_directhkrow"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
LANE_REDUCTION = PACKET_DIR / "heterotic_source_operator_torsion_lane_reduction.packet.json"
FINITE_SUPPORT = PACKET_DIR / "projective_rhoe_finite_internal_support_import.packet.json"
PHYSICAL_BLOCKER = PACKET_DIR / "physical_threshold_blocker_contract.packet.json"
NEXT_CUTSET = PACKET_DIR / "next_cutset_after_heterotic_source_operator_torsion.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HeteroticStromingerSourceOperatorTorsion_or_DirectHKRow_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_HETEROTICSTROMINGERSOURCEOPERATORTORSION_OR_DIRECTHKROW_"
    "FINITE_INTERNAL_SUPPORT_CLOSED_PHYSICAL_VALUES_OPEN"
)
NEXT = "MTT_Selected_ProjectiveRhoESmoothOperatorSourceValues_or_DirectHKRow_v1"


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
    lane = load(LANE_REDUCTION)
    finite = load(FINITE_SUPPORT)
    blocker = load(PHYSICAL_BLOCKER)
    cutset = load(NEXT_CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("lane reduction", lane),
        ("finite support", finite),
        ("physical blocker", blocker),
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
        "HYM_invariant_mu_extremum_refuted",
        "gerbe_response_interface_built",
        "gerbe_response_fill_partial_source_support",
        "projective_rhoe_finite_internal_support_closed",
        "direct_HK_exit_still_allowed",
    ]:
        require(decision[key] is True, f"decision missing closure/support {key}")
    for key in [
        "HYM_full_deltaA_spectrum_computed",
        "projective_rhoe_physical_threshold_value_computed",
        "smooth_operator_identity_or_physical_normalization_closed",
        "selected_R_H_RG_emitted",
        "selected_K_threshold_Omega_H_lambda",
        "strict_H_K_threshold_row_emitted",
        "full_no_knob_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"decision overclosed {key}")
    require(decision["accepted_selected_K_source_row_count"] == 9, "K row count")
    require(decision["selected_K_threshold_row_count_required"] == 10, "required K rows")

    hym = lane["hym_invariant_block"]
    require(hym["invariant_block_mu_extremum_refuted"] is True, "HYM extremum refuted")
    require(hym["mu_selected"] is False, "mu overselected")
    require(hym["full_deltaA_spectrum_computed"] is False, "Delta_A overcomputed")
    require(hym["threshold_payload_closed"] is False, "HYM payload overclosed")

    gerbe = lane["gerbe_torsion_lane"]
    require(gerbe["interface_primary_route_confirmed"] is True, "gerbe route")
    require(gerbe["twist_cancellation_table_filled"] is True, "twist cancellation")
    require(gerbe["global_gerbe_curvature_available"] is True, "global gerbe")
    require(gerbe["primitive_complex_central_support_filled"] is True, "primitive support")
    for key in [
        "same_branch_representative_filled",
        "same_branch_rhoE_or_local_system_filled",
        "finite_response_filled",
    ]:
        require(gerbe[key] is False, f"gerbe overclosed {key}")

    support = finite["closed_internal_support"]
    for key in [
        "finite_physical_quotient_domain_closed",
        "finite_trace_admissibility_closed",
        "selected_finite_internal_packet_emitted",
        "finite_rhoE_packet_selected_not_validator_only",
        "direct_finite_internal_operator_payload_closed",
        "all_acceptance_fields_filled_at_finite_internal_scope",
        "selected_internal_threshold_finitepart_closed",
        "selected_internal_logdet_retained",
    ]:
        require(support[key] is True, f"finite support not imported {key}")
    not_physical = finite["not_physical_H_row"]
    for key in [
        "E_Qa_computed",
        "threshold_value_computed",
        "physical_threshold_normalization_closed",
        "smooth_operator_identity_proved",
        "smooth_transition_matrices_emitted",
    ]:
        require(not_physical[key] is False, f"finite support overpromoted {key}")

    nogo = blocker["minimal_smooth_nogo"]
    require(nogo["direct_current_corpus_nogo_proved"] is True, "smooth no-go")
    require(nogo["finite_internal_closure_preserved"] is True, "internal preserved")
    require(nogo["requires_new_source_insertion"] is True, "source insertion")
    require(nogo["source_request_locked"] is True, "request locked")
    require(nogo["smooth_finitepart_can_close_now"] is False, "smooth finitepart overclosed")
    fill = blocker["smooth_operator_fill_attempt"]
    require(fill["support_context_filled"] is True, "support context")
    for key in [
        "smooth_projective_source_values_filled",
        "bundle_operator_values_filled",
        "admissibility_values_filled",
        "finite_part_values_filled",
        "smooth_finitepart_computed",
        "threshold_value_computed",
    ]:
        require(fill[key] is False, f"smooth fill overclosed {key}")
    leaves = blocker["missing_source_leaves"]
    require(all(value is False for value in leaves.values()), "source leaves overfilled")
    require(blocker["direct_source_native_HK_exit_still_allowed"] is True, "direct H exit")

    require(
        cutset["status"] == "NEXT_FRONTIER_PROJECTIVE_RHOE_SMOOTH_OPERATOR_VALUES_OR_DIRECT_HK",
        "cutset status",
    )
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    for phrase in [
        "HYM invariant-block mu extremum refuted as a source selector",
        "selected finite internal projective-rhoE packet imported as selected support",
        "selected internal threshold finite part imported as closed internal support",
    ]:
        require(phrase in cutset["closed_here"], f"closed phrase missing {phrase}")
    for phrase in [
        "same-branch smooth/projective representative and representation action",
        "E_Qa matrix or equivalent threshold finite response value",
        "physical threshold normalization and smooth operator identity",
        "direct source-native K_threshold.Omega_H.lambda",
    ]:
        require(phrase in cutset["still_open"], f"open phrase missing {phrase}")

    for phrase in [
        "HeteroticStromingerSourceOperatorTorsionOrDirectHKRowTheorem",
        "finite internal quotient/operator/finite-part layer only",
        "Strict selected `K_threshold` rows remain",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: heterotic/Strominger branch imports finite internal rhoE support; physical H row remains open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
