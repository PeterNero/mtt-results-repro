"""Audit cross-block covariance or Rtheta coefficient value fill artifact."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_crossblockcovariance_or_rthetacoefficientvaluefill"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
BASIS = PACKET_DIR / "deduplicated_cross_block_covariance_basis.packet.json"
DEPENDENCIES = PACKET_DIR / "cross_block_covariance_dependency_graph.packet.json"
RTHETA = PACKET_DIR / "rtheta_coefficient_value_fill_gate.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_cross_block_basis_map.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_CrossBlockCovariance_or_RThetaCoefficientValueFill_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_CROSSBLOCKCOVARIANCE_OR_RTHETACOEFFICIENTVALUEFILL_"
    "BUILT_DEDUP_BASIS_DEPENDENCY_GRAPH_VALUES_OPEN"
)
NEXT = "MTT_Selected_CrossBlockCovarianceValues_or_RThetaCoefficientExecution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    basis = load(BASIS)
    deps = load(DEPENDENCIES)
    rtheta = load(RTHETA)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    for key in [
        "closure_claimed",
        "unpatched_theorem_closure_claimed",
        "observed_data_used_as_selector",
        "target_fitting_used",
    ]:
        require(data[key] is False, f"candidate guardrail overclaimed: {key}")
    require(data["theorem"]["proved"] is True, "candidate theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")

    require(basis["status"] == "DEDUPLICATED_CROSS_BLOCK_BASIS_BUILT_VALUES_OPEN", "basis status mismatch")
    require(basis["basis_map_closed"] is True, "basis map not closed")
    require(basis["numeric_cross_block_covariance_values_filled"] is False, "numeric covariance overfilled")
    require(basis["row_counts"]["deduplicated_interim_total"] == 19, "dedup row count mismatch")
    require(len(basis["deduplicated_interim_basis"]) == 19, "dedup basis length mismatch")
    require(len(set(basis["deduplicated_interim_basis"])) == 19, "dedup basis has duplicates")
    for row_id in ["lambda_Mt", "g_2_Mt", "g_Y_Mt", "v_from_G_F_tree_reference"]:
        require(row_id in basis["deduplicated_interim_basis"], f"basis missing row: {row_id}")
    require("g_1_GUT_Mt" not in basis["deduplicated_interim_basis"], "g1 alias double-counted")
    overlap_rule = next(row for row in basis["deduplication_rules"] if row["id"] == "merge_WZH_weak_overlap")
    require(overlap_rule["overlap_rows"] == ["g_2_Mt", "g_Y_Mt", "lambda_Mt"], "wrong overlap rows")
    for rule in basis["deduplication_rules"]:
        require(rule["closed"] is True, f"dedup rule not closed: {rule['id']}")
    require(basis["closure_claimed"] is True, "basis packet should close locally")

    require(
        deps["status"] == "CROSS_BLOCK_DEPENDENCY_GRAPH_BUILT_NUMERIC_VALUES_OPEN",
        "dependency graph status mismatch",
    )
    require(deps["structural_cross_block_map_closed"] is True, "structural graph not closed")
    require(deps["numeric_cross_block_covariance_values_filled"] is False, "numeric graph overfilled")
    require(deps["full_covariance_profile_likelihood_closed"] is False, "full profile overclosed")
    edge_ids = {edge["edge"] for edge in deps["dependency_edges"]}
    for edge in [
        "weak_to_wzh_overlap",
        "weak_to_BCT_common_scale",
        "weak_to_Higgs_decay_inputs",
        "BCT_to_Higgs_decay_yukawa_inputs",
        "Higgs_decay_internal",
    ]:
        require(edge in edge_ids, f"missing dependency edge: {edge}")
    require(len(deps["remaining_numeric_requirements"]) == 4, "numeric requirement count changed")
    require(deps["closure_claimed"] is True, "dependency graph should close locally")

    require(
        rtheta["status"] == "RTHETA_COEFFICIENT_VALUE_FILL_GATE_BUILT_VALUES_STILL_OPEN",
        "Rtheta gate status mismatch",
    )
    require(rtheta["deduplicated_covariance_basis_map_closed"] is True, "dedup basis not visible to Rtheta gate")
    require(rtheta["basis_map_closed_in_rtheta_manifest"] is False, "Rtheta basis overclosed")
    require(rtheta["slot_count"] == 10, "slot count mismatch")
    require(rtheta["filled_slot_count"] == 0, "Rtheta slots unexpectedly filled")
    require(len(rtheta["wzh_relevant_slots"]) == 2, "wrong WZH-relevant slot count")
    require(rtheta["Rtheta_coefficient_values_closed"] is False, "Rtheta coefficients overclosed")
    require(rtheta["selected_Rtheta_source_rows_closed"] is False, "Rtheta source rows overclosed")
    require(rtheta["accepted_Rtheta_source_row_count"] == 0, "accepted Rtheta row count mismatch")
    require(rtheta["closure_claimed"] is False, "Rtheta gate overclosed")

    require(
        cutset["status"] == "NEXT_ATTACK_NUMERIC_CROSS_BLOCK_COVARIANCE_OR_RTHETA_COEFFICIENT_EXECUTION",
        "cutset status mismatch",
    )
    for key in [
        "deduplicated_cross_block_covariance_basis",
        "WZH_weak_overlap_and_g1_alias_removed",
        "cross_block_dependency_graph",
        "Rtheta_coefficient_value_fill_gate",
    ]:
        require(cutset["closed_now"][key] is True, f"cutset closed flag missing: {key}")
    for key in [
        "numeric_cross_block_covariance_values",
        "full_covariance_profile_likelihood",
        "Rtheta_coefficient_values",
        "selected_threshold_response_functional",
        "selected_Rtheta_source_rows",
        "common_scale_convention_map",
        "EW_formula_kernels_for_WW_ZZ_Zgamma",
        "true_SM_equivalence",
        "full_no_knob",
    ]:
        require(cutset["still_open"][key] is True, f"cutset open flag missing: {key}")
    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    require(cutset["closure_claimed"] is False, "cutset overclosed")

    closure = data["closure_decision"]
    require(closure["deduplicated_cross_block_covariance_basis_closed"] is True, "candidate basis not closed")
    require(closure["cross_block_dependency_graph_closed"] is True, "candidate dependency graph not closed")
    for key in [
        "numeric_cross_block_covariance_values_closed",
        "full_covariance_profile_likelihood_closed",
        "Rtheta_coefficient_values_closed",
        "selected_Rtheta_source_rows_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(closure[key] is False, f"candidate overclosed: {key}")
    require(cert["deduplicated_interim_row_count"] == 19, "certificate row count mismatch")
    require("deduplicated interim row count        : 19" in note, "note missing row count")
    require("numeric cross-block covariance closed : false" in note, "note missing numeric covariance guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
