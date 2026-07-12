"""Audit Step 31 visible Chern-Weil source to same-source symmetry breaking."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step31_visiblecwsource_to_samesourcesymmetrybreaking"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
REDUCTION = PACKET_DIR / "step31_visible_source_reduction.packet.json"
LANES = PACKET_DIR / "step31_two_lane_construction_frontier.packet.json"
NEXT_CONTRACT = PACKET_DIR / "step31_samesource_symmetrybreaking_contract.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step31_VisibleCWSource_to_SameSourceSymmetryBreaking_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP31_VISIBLECWSOURCE_REDUCED_TO_SAMESOURCE_SYMMETRYBREAKING"
NEXT = "MTT_SameSource_SymmetryBreaking_Source_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    reduction = load(REDUCTION)
    lanes = load(LANES)
    contract = load(NEXT_CONTRACT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaimed")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaimed")

    require(reduction["step30_import"]["projective_BN_mechanical_lift_fields_closed"] is True, "Step30 lift not imported")
    require(reduction["step30_import"]["selected_visible_operator_source_closed"] is False, "visible source overclosed")
    require(reduction["visible_green_schwarz_gate"]["selected_s3_source_closed"] is True, "S3 source not closed")
    require(reduction["visible_green_schwarz_gate"]["visible_green_schwarz_curvature_closed"] is True, "GS row not closed")
    require(reduction["visible_green_schwarz_gate"]["first_blocking_layer_is_selected_operator_source"] is True, "wrong blocking layer")
    require(reduction["reduction_theorem"]["visible_cw_theorem_proved"] is True, "visible CW theorem not proved")
    require(reduction["reduction_theorem"]["nonsplit_or_routec_theorem_proved"] is True, "nonsplit theorem not proved")
    require(reduction["reduction_theorem"]["selected_visible_operator_source_closed"] is False, "source overclosed")
    require(reduction["reduction_theorem"]["next_object"] == "SameSourceSymmetryBreakingSource.v1", "wrong next object")

    rank2 = lanes["rank2_lane"]
    routec = lanes["route_c_lane"]
    require(rank2["classification"] == "SUPERSET_CONVERGENCE_PRIMARY_FILL_LANE", "rank2 not primary")
    require(rank2["priority"] == 1, "rank2 priority mismatch")
    for key in [
        "appell_humbert_automorphy_exists",
        "h1_validator_formulated",
        "ordered_source_validator_formulated",
        "ordinary_integral_c1_matrix_realized",
        "topological_c2_target",
    ]:
        require(rank2["closed"][key] is True, f"rank2 closed support missing: {key}")
    for key in [
        "base_swap_pic0_selector_obstruction",
        "branch_orientation_not_selected",
        "nonzero_ext_not_selected",
        "selected_l2_cochain_packet_absent",
        "stability_not_proved",
    ]:
        require(rank2["blocked_by"][key] is True, f"rank2 blocker missing: {key}")
    require(routec["classification"] == "SUPERSET_REPAIR_PARALLEL_FILL_LANE", "routec classification mismatch")
    require(routec["priority"] == 2, "routec priority mismatch")
    require(routec["current_scaffold_fill_nogo"] is True, "routec no-go not imported")
    require(routec["selected_emitted_current_scaffold"] == 0, "routec scaffold overemitted selected data")
    terminal = lanes["terminal_pic0_gate"]
    require(terminal["terminal_lane_conditional_uniqueness_imported"] is True, "terminal uniqueness missing")
    require(terminal["selected_terminal_lane_pic0_source_proved"] is False, "terminal Pic0 overproved")
    require(terminal["naive_pic0_quotient_rejected"] is True, "Pic0 shortcut not rejected")
    require(terminal["finite_gerbe_torsion_route_live"] is True, "gerbe route not live")
    require(terminal["same_source_operator_selector_still_open"] is True, "operator selector overclosed")

    require(contract["next_required_artifact"] == NEXT, "contract next mismatch")
    require(contract["closure_claimed"] is False, "contract overclaimed")
    for phrase in [
        "selected q79/F,m=1 source identity",
        "base-factor ordering or a physical quotient proving order irrelevance",
        "Pic0 character selection or a physical Pic0 quotient rule",
        "same-source link from S3/Green-Schwarz support to V_alpha or Route-C residual",
        "holonomy-sensitive D_E/dotD/Hessian response that breaks or quotients the current degeneracy",
    ]:
        require(phrase in contract["must_emit_next"], f"must emit missing: {phrase}")
    for phrase in [
        "source-level S3 projective gerbe rho_E",
        "visible Green-Schwarz curvature row",
        "smooth projective B_N mechanical lift fields",
        "rank-two Appell-Humbert/topological target data",
        "identity rho_E smoke route",
    ]:
        require(phrase in contract["must_not_reopen"], f"anti-reopen missing: {phrase}")

    decision = data["closure_decision"]
    for key in [
        "visible_CW_operator_source_reduced_to_common_source",
        "rank2_non_split_lane_prioritized",
        "routec_lane_retained_as_parallel_repair",
        "same_source_symmetrybreaking_contract_emitted",
    ]:
        require(decision[key] is True, f"decision close missing: {key}")
    for key in [
        "selected_visible_operator_source_closed",
        "same_source_symmetrybreaking_source_closed",
        "operator_level_projective_rhoE_transition_closed",
        "selected_D_E_Riesz_Green_dotD_values_closed",
        "fullS2_operator_payload_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed: {key}")
    require(decision["accepted_internal_scalar_row_count"] == 0, "scalar rows overaccepted")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["visible_CW_operator_source_reduced_to_common_source"] is True, "certificate reduction missing")
    require(cert["same_source_symmetrybreaking_source_closed"] is False, "certificate overclosed source")
    require(cert["operator_sector_values_closed"] is False, "certificate overclosed values")

    for phrase in [
        "rank-two non-split V_alpha lane                    priority 1",
        "Route-C finite HYM/Strominger lane                 priority 2 fallback",
        "same-source symmetry-breaking source               open",
        NEXT,
    ]:
        require(phrase in note, f"note missing phrase: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
