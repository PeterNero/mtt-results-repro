"""Audit VSD-01 all-primitive-row assembly map or physical Phi_fin C1 action source."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_vsd01_allprimitiverowsassemblymap_or_physicalphifinc1actionsource"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SOURCE_IMPORT = PACKET_DIR / "premise_free_physical_source_backimport.packet.json"
ASSEMBLY = PACKET_DIR / "all_primitive_rows_assembly_map.packet.json"
VSD01_DECISION = PACKET_DIR / "vsd01_source_subgate_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_vsd01_source_assembly.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_VSD01_AllPrimitiveRowsAssemblyMap_or_PhysicalPhiFinC1ActionSource_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_VSD01_ALLPRIMITIVEROWSASSEMBLYMAP_OR_PHYSICALPHIFINC1ACTIONSOURCE_"
    "BUILT_SOURCE_ASSEMBLY_AND_DYNAMIC_PACKET_CLOSED_VALUE_ROWS_OPEN"
)
NEXT = "MTT_Selected_AcceptedValueLayerFrontier_or_NonLoopingSourceRows_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    source_import = load(SOURCE_IMPORT)
    assembly = load(ASSEMBLY)
    decision = load(VSD01_DECISION)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["closure_claimed"] is False, "candidate full closure overclaimed")
    require(data["unpatched_theorem_closure_claimed"] is True, "source theorem should be backimported as closed")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")

    require(source_import["target_obligation"] == "VSD-01-selected-overlap-value-kernel", "wrong VSD target")
    require(source_import["premise_free_route_A_certificate_valid"] is True, "Route A certificate not valid")
    require(source_import["premise_free_phi_fin_restriction_morphism_proved"] is True, "morphism not proved")
    quotient = source_import["symbolic_transport_closed_quotient"]
    require(quotient["finite_rank"] == 27, "wrong finite rank")
    require(quotient["symbolic_transport_envelope"] is True, "symbolic envelope missing")
    require(quotient["raw_27_mode_truncation_claimed_closed"] is False, "raw 27-mode overclaimed")
    fields = source_import["route_A_fields"]
    for key in [
        "same_branch",
        "physical_action_restricts_to_selected_finite_Weyl_quotient",
        "no_extra_physical_boundary_or_source_term",
        "phase_R_Z_source_selection",
        "shift_R_X_source_selection",
        "same_source_b_selected_emission",
    ]:
        require(fields[key] is True, f"Route A field missing: {key}")
    require(fields["source_row_premise_used"] is False, "source row used as premise")
    require(fields["attached_same_branch_source_count"] >= 5, "insufficient same-branch sources")
    require(source_import["raw_27mode_guardrail"]["raw_27mode_finite_replay_closed"] is False, "raw replay overclosed")
    require(source_import["raw_27mode_guardrail"]["symbolic_transport_quotient_used"] is True, "symbolic quotient not used")

    rows = assembly["row_evidence"]
    require(rows["all_72_primitive_rows_exact"] is True, "72 primitive rows not exact")
    require(rows["all_72_exactness_certificates"] is True, "72 exactness missing")
    require(rows["all_rows_match_formal_packet"] is True, "formal packet mismatch")
    require(rows["primitive_row_count"] == 72, "wrong primitive row count")
    require(rows["primitive_source_counts"] == {"R_X": 18, "R_Z": 18, "zero_route": 36}, "source counts mismatch")
    require(rows["formal_110_rows_executed"] is True, "formal 110 not executed")
    require(rows["formal_110_matches_prior_replay"] is True, "formal 110 mismatch")
    require(rows["formal_110_row_counts"]["total_rows"] == 110, "wrong formal row count")

    source_fields = assembly["assembly_source_fields"]
    require(source_fields["selected_field_count"] >= 9, "not enough selected source fields")
    for field in [
        "sector_row_assembly",
        "phase_R_Z_source",
        "shift_R_X_source",
        "b_selected_source",
        "source_owner_id",
        "independence_guard",
    ]:
        require(source_fields[field]["selected_emitted"] is True, f"{field} not emitted")
        require(source_fields[field]["theorem_derived"] is True, f"{field} not theorem-derived")
        require(source_fields[field]["same_branch"] is True, f"{field} not same-branch")
        require(source_fields[field]["source_owner_verified"] is True, f"{field} owner not verified")

    replay = assembly["source_stack_replay"]
    require(replay["source_stack_closed"] is True, "source stack not closed")
    for key in ["A_selected", "b_selected", "deltaTheta_C1", "PhysicalPhiFinC1ActionSource"]:
        require(replay["promoted_objects"][key] is True, f"promoted object missing: {key}")
    require(replay["unpatched_A_selected_promoted"] is True, "A not promoted")
    require(replay["unpatched_b_selected_promoted"] is True, "b not promoted")
    require(replay["unpatched_deltaTheta_C1_promoted"] is True, "deltaTheta not promoted")
    require(assembly["same_branch_link_to_versioned_value_packet"] is True, "same-branch link missing")
    require(assembly["closure_claimed"] is True, "assembly subgate should close")

    closed = decision["closed_for_VSD01_now"]
    for key in [
        "physical_PhiFinC1_action_source",
        "all_72_primitive_rows_exact",
        "formal_110_row_assembly",
        "same_branch_source_stack_replay",
        "A_selected_promoted",
        "b_selected_promoted",
        "deltaTheta_C1_promoted",
        "source_owner_verified",
        "selected_dynamic_overlap_tensor_T_selected",
        "same_source_dynamic_matter_overlap_operator_packet",
        "primitive_C1_contractions_first_response_layer",
        "conditional_non_scalar_value_packet_selected",
        "no_observed_data_selector_guard",
    ]:
        require(closed[key] is True, f"VSD-01 close flag missing: {key}")
    open_items = decision["not_closed_for_VSD01_yet"]
    for key in [
        "accepted_Yukawa_magnitudes",
        "running_mass_ratios",
        "CKM_PMNS_measured_angles_phase",
        "lambda_H_and_threshold_value_rows",
        "accepted_threshold_mass_scheme_source_rows",
        "no_knob_value_source_derivation",
    ]:
        require(open_items[key] is True, f"VSD-01 open flag missing: {key}")
    require(decision["VSD01_source_assembly_subgate_closed"] is True, "source subgate not closed")
    require(decision["VSD01_dynamic_overlap_subgate_closed"] is True, "dynamic overlap subgate not closed")
    require(decision["VSD01_full_obligation_closed"] is False, "VSD-01 full closure overclaimed")
    require(decision["closure_claimed"] is False, "decision overclaimed")

    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    require(cutset["closure_claimed"] is False, "cutset overclaimed")
    final = data["closure_decision"]
    require(final["VSD01_source_assembly_subgate_closed"] is True, "candidate subgate not closed")
    require(final["VSD01_dynamic_overlap_subgate_closed"] is True, "candidate dynamic subgate not closed")
    require(final["VSD01_full_obligation_closed"] is False, "candidate VSD-01 overclosed")
    require(final["source_stack_closed"] is True, "candidate source stack not closed")
    require(final["dynamic_matter_overlap_packet_closed"] is True, "dynamic packet not imported as closed")
    require(final["true_SM_equivalence_closed"] is False, "true equivalence overclosed")
    require(final["full_no_knob_closed"] is False, "full no-knob overclosed")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require("full VSD-01 is not closed yet" in note, "note missing VSD-01 guardrail")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
