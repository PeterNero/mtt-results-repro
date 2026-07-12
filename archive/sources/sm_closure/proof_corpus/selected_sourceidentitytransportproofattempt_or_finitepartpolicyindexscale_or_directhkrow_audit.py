"""Audit source-identity transport / finitepart policy frontier packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_sourceidentitytransportproofattempt_or_finitepartpolicyindexscale_or_directhkrow"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SOURCE_LANE = PACKET_DIR / "source_identity_transport_reduction_lane.packet.json"
FINITEPART_LANE = PACKET_DIR / "finitepart_policy_indexscale_lane.packet.json"
NEXT_CUTSET = PACKET_DIR / "next_cutset_after_transport_finitepart_policy.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_SourceIdentityTransportProofAttempt_or_FinitePartPolicyIndexScaleSourceTheorem_or_DirectHKRow_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_SOURCEIDENTITYTRANSPORTPROOFATTEMPT_OR_FINITEPARTPOLICYINDEXSCALE_"
    "INTERNAL_PA_CLOSED_SOURCEBRANCH_PHYSICALANCHOR_OPEN"
)
NEXT = "MTT_Selected_SourceBranchIdentityEmission_or_QaStackPhysicalAnchor_or_DirectHKRow_v1"


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
    source = load(SOURCE_LANE)
    finite = load(FINITEPART_LANE)
    cutset = load(NEXT_CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("source lane", source),
        ("finitepart lane", finite),
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
        "source_identity_transport_reduced_to_single_leaf",
        "operator_coemission_conditional_closed",
        "no_lift_replay_conditional_closed",
        "internal_finitepart_policy_closed",
        "internal_determinant_index_weights_closed",
        "internal_mu_scale_closed",
        "selected_p_a_internal_promoted",
        "typed_hypercharge_convention_map_closed",
        "direct_HK_exit_still_allowed",
    ]:
        require(decision[key] is True, f"decision support missing {key}")
    require(decision["selected_p_a_internal_value"] == 29.201650332199108, "p_a value")
    require(
        decision["conditional_lambda12_if_quotient_is_p_a"] == 2.6179362173268497,
        "conditional lambda",
    )
    require(
        decision["conditional_Delta_G12_if_quotient_is_p_a"] == 0.08450302790361214,
        "conditional Delta",
    )
    require(decision["accepted_selected_K_source_row_count"] == 9, "K count")
    require(decision["selected_K_threshold_row_count_required"] == 10, "required K")
    for key in [
        "source_branch_identity_closed",
        "selected_connection_witness_export_closed",
        "oriented_logdet_promoted",
        "Qa_stack_p_a_source_closed",
        "direct_U1Y_row_promoted",
        "physical_K_gauge_anchor_closed",
        "lambda_12_closed",
        "measured_electroweak_closure",
        "selected_R_H_RG_emitted",
        "selected_K_threshold_Omega_H_lambda",
        "strict_H_K_threshold_row_emitted",
        "full_no_knob_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"decision overclosed {key}")

    require(source["proof_attempt_executed"] is True, "proof attempt")
    require(source["transport_reduced_to_single_leaf"] is True, "single leaf reduction")
    require(source["single_remaining_leaf"] == "source_branch_identity", "leaf name")
    require(source["operator_coemission_conditional_closed"] is True, "operator conditional")
    require(source["no_lift_replay_conditional_closed"] is True, "no-lift conditional")
    for key in [
        "operator_coemission_unconditional_closed",
        "no_lift_replay_unconditional_closed",
        "source_branch_identity_closed",
        "selected_connection_witness_export_closed",
        "oriented_logdet_promoted",
    ]:
        require(source[key] is False, f"source lane overclosed {key}")

    internal = finite["internal_policy"]
    for key in [
        "regularization_finite_part_selected_internal",
        "determinant_index_weights_selected_internal",
        "determinant_scale_mu_selected_internal",
        "kernel_policy_selected_internal",
        "H_zero_cluster_value_invariant_current_branch",
        "selected_p_a_internal_promoted",
    ]:
        require(internal[key] is True, f"internal policy missing {key}")
    require(internal["selected_p_a_internal_value"] == 29.201650332199108, "internal p_a")
    physical = finite["physical_boundary"]
    for key in [
        "lambda_12_closed",
        "same_scheme_SU2_row_or_cancellation_closed",
        "physical_K_gauge_anchor_closed",
        "measured_electroweak_closure",
    ]:
        require(physical[key] is False, f"physical boundary overclosed {key}")
    hyper = finite["hypercharge_convention"]
    require(hyper["typed_hypercharge_convention_map_closed"] is True, "typed convention")
    require(
        hyper["hypercharge_index_weights_closed_structurally"] is True,
        "structural hypercharge",
    )
    require(hyper["Qc_row_closed_for_weaksplit"] is True, "Qc")
    require(hyper["SU2_row_closed_for_weaksplit"] is True, "SU2")
    require(hyper["conditional_lambda12_if_quotient_is_p_a"] == 2.6179362173268497, "hyper lambda")
    require(hyper["conditional_Delta_G12_if_quotient_is_p_a"] == 0.08450302790361214, "hyper delta")
    for key in [
        "Qa_stack_p_a_source_closed",
        "direct_U1Y_row_promoted",
        "lambda_12_closed",
        "measured_electroweak_closure",
    ]:
        require(hyper[key] is False, f"hypercharge overclosed {key}")

    require(
        cutset["status"] == "NEXT_FRONTIER_SOURCEBRANCH_IDENTITY_OR_PHYSICAL_ANCHOR_OR_DIRECT_HK_ROW",
        "cutset status",
    )
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    for phrase in [
        "source-identity transport proof attempt reduced to source_branch_identity",
        "internal p_a promoted to 29.201650332199108",
        "typed hypercharge convention map closed structurally",
    ]:
        require(phrase in cutset["closed_here"], f"closed phrase missing {phrase}")
    for phrase in [
        "source_branch_identity emission theorem for BN27 threshold complex",
        "Qa-stack p_a source emission into the electroweak row",
        "physical K_gauge/action-unit or Omega0/K_phys anchor",
        "direct source-native K_threshold.Omega_H.lambda",
    ]:
        require(phrase in cutset["still_open"], f"open phrase missing {phrase}")

    for phrase in [
        "SourceIdentityTransportOrFinitepartPolicyIndexScaleTheorem",
        "`p_a^int = 29.201650332199108`",
        "`lambda_12 = 2.6179362173268497`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: source-identity transport reduced to source-branch identity; internal p_a closed; physical lambda/H row open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
