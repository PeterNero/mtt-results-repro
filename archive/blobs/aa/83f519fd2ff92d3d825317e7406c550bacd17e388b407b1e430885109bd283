"""Audit source-branch identity / Qa-stack physical-anchor frontier packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_sourcebranchidentityemission_or_qastackphysicalanchor_or_directhkrow"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SOURCE_BRANCH_LANE = PACKET_DIR / "source_branch_identity_emission_lane.packet.json"
WEAK_SPLIT_LANE = PACKET_DIR / "qastack_internal_weak_split_lane.packet.json"
PHYSICAL_LANE = PACKET_DIR / "physical_anchor_rg_matching_lane.packet.json"
NEXT_CUTSET = PACKET_DIR / "next_cutset_after_sourcebranch_internalweaksplit.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_SourceBranchIdentityEmission_or_QaStackPhysicalAnchor_or_DirectHKRow_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_SOURCEBRANCHIDENTITYEMISSION_OR_QASTACKPHYSICALANCHOR_"
    "INTERNAL_WEAKSPLIT_CLOSED_PHYSICAL_GAUGE_RG_OPEN"
)
NEXT = "MTT_Selected_ElectroweakGaugeKineticNormalizationAndRGScheme_or_BN27RepairSourceAmendment_or_DirectHKRow_v1"


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
    source = load(SOURCE_BRANCH_LANE)
    weak = load(WEAK_SPLIT_LANE)
    physical = load(PHYSICAL_LANE)
    cutset = load(NEXT_CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("source branch lane", source),
        ("weak split lane", weak),
        ("physical lane", physical),
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
        "BN27_sourcebranch_current_source_nogo",
        "BN27_repair_packet_built",
        "internal_Qa_stack_p_a_source_closed",
        "typed_hypercharge_map_closed",
        "same_scheme_SU2_row_or_cancellation_closed",
        "lambda_12_internal_closed",
        "old_Qa_or_U1Y_promotion_gate_superseded_for_internal_lambda12",
        "Omega0_symbol_convention_chi_equals_1",
        "relative_GR_metrology_family_imported",
        "direct_HK_exit_still_allowed",
    ]:
        require(decision[key] is True, f"decision support missing {key}")
    require(decision["lambda_12_internal_value"] == 2.6179362173268497, "internal lambda")
    require(decision["Delta_G12_internal_value"] == 0.08450302790361214, "internal delta")
    require(decision["accepted_selected_K_source_row_count"] == 9, "K count")
    require(decision["selected_K_threshold_row_count_required"] == 10, "required K")
    for key in [
        "BN27_source_branch_identity_closed",
        "BN27_oriented_logdet_promoted",
        "physical_gauge_action_anchor_closed",
        "matching_scale_closed",
        "RG_scheme_closed",
        "measured_electroweak_closure",
        "full_SM_closure",
        "selected_R_H_RG_emitted",
        "selected_K_threshold_Omega_H_lambda",
        "strict_H_K_threshold_row_emitted",
        "full_no_knob_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"decision overclosed {key}")

    require(source["sourcebranchidentity_attempted"] is True, "sourcebranch attempted")
    require(source["current_source_nogo"] is True, "current source no-go")
    require(source["support_count"] == 3, "support count")
    require(source["required_clause_count"] == 3, "required clauses")
    require(source["emitted_count"] == 0, "emitted count")
    require(source["repair_packet_built"] is True, "repair packet")
    for key in [
        "transport_reduced_leaf_resolved",
        "source_branch_identity_closed",
        "selected_connection_witness_export_closed",
        "oriented_logdet_promoted",
    ]:
        require(source[key] is False, f"sourcebranch overclosed {key}")

    for key in [
        "Qa_stack_p_a_source_closed",
        "typed_hypercharge_map_closed",
        "Qc_row_closed_for_weaksplit",
        "SU2_row_closed_for_weaksplit",
        "same_scheme_SU2_row_or_cancellation_closed",
        "lambda_12_internal_closed",
    ]:
        require(weak[key] is True, f"weak split missing {key}")
    require(weak["lambda_12_internal_value"] == 2.6179362173268497, "weak lambda")
    require(weak["Delta_G12_internal_value"] == 0.08450302790361214, "weak delta")
    require(weak["old_gate_reconciled"]["superseded_by_internal_weak_split_packet"] is True, "old gate supersession")
    require(weak["old_gate_reconciled"]["previous_gate_lambda_12_closed"] is False, "old gate not closed")
    require(
        weak["old_gate_reconciled"]["previous_gate_selected_Qa_or_pY_source_payload_found"] is False,
        "old gate source payload",
    )
    for key in [
        "physical_K_gauge_anchor_closed",
        "matching_scale_and_RG_scheme_closed",
        "measured_electroweak_closure",
    ]:
        require(weak[key] is False, f"weak physical overclosed {key}")

    require(physical["internal_lambda_12_closed"] is True, "physical lane internal lambda")
    require(physical["internal_lambda_12_value"] == 2.6179362173268497, "physical lambda value")
    require(physical["internal_Delta_G12_value"] == 0.08450302790361214, "physical delta value")
    require(physical["Omega0_symbol_convention_chi_equals_1"] is True, "Omega0 convention")
    require(physical["relative_GR_metrology_family"] is True, "relative GR")
    require(physical["one_anchor_GR_propagation_family"] is True, "one-anchor GR")
    for key in [
        "physical_gauge_action_anchor_closed",
        "matching_scale_closed",
        "RG_scheme_closed",
        "measured_electroweak_closure",
        "full_SM_closure",
    ]:
        require(physical[key] is False, f"physical overclosed {key}")

    require(
        cutset["status"] == "NEXT_FRONTIER_GAUGE_KINETIC_RG_OR_BN27_REPAIR_OR_DIRECT_HK_ROW",
        "cutset status",
    )
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    for phrase in [
        "BN27 source-branch identity attempted and current-source no-go proved",
        "internal lambda_12=2.6179362173268497 closed",
        "internal Delta_G12=0.08450302790361214 closed",
    ]:
        require(phrase in cutset["closed_here"], f"closed phrase missing {phrase}")
    for phrase in [
        "physical gauge/action normalization",
        "matching scale mu_match",
        "RG and threshold scheme",
        "direct source-native K_threshold.Omega_H.lambda",
    ]:
        require(phrase in cutset["still_open"], f"open phrase missing {phrase}")

    for phrase in [
        "SourceBranchIdentityNoGoAndInternalWeakSplitClosureTheorem",
        "`lambda_12 = 2.6179362173268497`",
        "Physical gauge/action normalization",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: source-branch no-go recorded; internal weak-split lambda closed; physical gauge/RG and H row open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
