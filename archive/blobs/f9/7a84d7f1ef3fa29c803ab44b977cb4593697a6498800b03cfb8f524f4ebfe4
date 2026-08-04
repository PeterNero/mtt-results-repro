"""Audit threshold/pole-running maps or R_theta convention source artifact."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_thresholdpolerunningmaps_or_rthetaconventionsource"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
GAUGE_BRIDGE = PACKET_DIR / "gauge_bridge_policy_validation_status.packet.json"
MAP_DECOMP = PACKET_DIR / "threshold_pole_running_map_decomposition.packet.json"
TOP_HIGGS_TARGET = PACKET_DIR / "top_higgs_threshold_map_target.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_threshold_map_decomposition.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_ThresholdPoleRunningMaps_or_RThetaConventionSource_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_THRESHOLDPOLERUNNINGMAPS_OR_RTHETACONVENTIONSOURCE_"
    "BUILT_GAUGE_BRIDGE_ACCEPTED_TOP_HIGGS_MAPS_OPEN"
)
NEXT = "MTT_Selected_TopHiggsThresholdMapRows_or_ExternalPrecisionTable_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    gauge = load(GAUGE_BRIDGE)
    maps = load(MAP_DECOMP)
    top_higgs = load(TOP_HIGGS_TARGET)
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

    require(
        gauge["status"] == "ONE_LOOP_GAUGE_BRIDGE_ACCEPTED_AS_POLICY_VALIDATION_NOT_PRECISION_MATCH",
        "gauge bridge status mismatch",
    )
    require(gauge["passes_coarse_gauge_bridge"] is True, "coarse gauge bridge did not pass")
    require(gauge["accepted_as_policy_validation_scaffold"] is True, "gauge bridge not accepted as scaffold")
    require(gauge["accepted_as_precision_threshold_match"] is False, "gauge bridge overaccepted")
    require(gauge["max_absolute_delta_to_literature"] > 0, "gauge deltas missing")
    require(gauge["closure_claimed"] is True, "gauge local closure missing")

    require(
        maps["status"] == "MAP_DECOMPOSITION_BUILT_ONLY_GAUGE_SCAFFOLD_ACCEPTED",
        "map decomposition status mismatch",
    )
    require(maps["same_branch_convention_source_theorem_closed"] is False, "same branch source overclosed")
    require(maps["accepted_policy_validation_row_count"] == 1, "wrong policy validation row count")
    require(maps["accepted_precision_threshold_row_count"] == 0, "precision threshold rows overaccepted")
    row_ids = {row["id"]: row for row in maps["map_rows"]}
    require(row_ids["gauge_MZ_to_Mt_one_loop_bridge"]["accepted_now"] is True, "gauge bridge row not accepted")
    require(
        row_ids["gauge_MZ_to_Mt_one_loop_bridge"]["accepted_as_precision_threshold_row"] is False,
        "gauge bridge row overaccepted as precision",
    )
    for key in [
        "top_direct_or_pole_to_MSbar_running_y_t",
        "Higgs_pole_to_running_lambda_H",
        "bottom_charm_native_MSbar_scale_transport",
        "tau_pole_rest_to_running_lepton_map",
        "W_Z_H_electroweak_matching_rows",
    ]:
        require(row_ids[key]["accepted_now"] is False, f"map row overaccepted: {key}")
        require(row_ids[key]["accepted_as_precision_threshold_row"] is False, f"precision row overaccepted: {key}")
    require(maps["closure_claimed"] is False, "map decomposition overclosed")

    require(
        top_higgs["status"] == "TOP_HIGGS_THRESHOLD_MAP_TARGETS_EXTRACTED_VALUES_OPEN",
        "top/Higgs target status mismatch",
    )
    require("central_value" in top_higgs["top_targets"]["literature_y_t_Mt"], "top literature value missing")
    require("central_value" in top_higgs["higgs_targets"]["literature_lambda_Mt"], "lambda literature value missing")
    require(len(top_higgs["top_targets"]["residual_slots"]) == 2, "wrong top residual slot count")
    require(len(top_higgs["higgs_targets"]["residual_slots"]) == 2, "wrong lambda residual slot count")
    require(
        top_higgs["residuals_are_requirements_not_fitted_corrections"] is True,
        "residual guard missing",
    )
    require(top_higgs["can_accept_top_higgs_maps_now"] is False, "top/Higgs maps overaccepted")
    require(top_higgs["closure_claimed"] is True, "top/Higgs local target closure missing")

    require(
        cutset["status"] == "NEXT_ATTACK_TOP_HIGGS_THRESHOLD_MAP_ROWS_OR_EXTERNAL_PRECISION_TABLE",
        "cutset status mismatch",
    )
    for key in [
        "one_loop_gauge_bridge_policy_validation_status",
        "threshold_pole_running_map_decomposition",
        "top_higgs_threshold_map_targets_extracted",
    ]:
        require(cutset["closed_now"][key] is True, f"cutset closed flag missing: {key}")
    for key in [
        "same_branch_Rtheta_convention_source_theorem",
        "top_direct_or_pole_to_MSbar_running_y_t_map",
        "Higgs_pole_to_running_lambda_H_map",
        "bottom_charm_tau_mass_scheme_maps",
        "W_Z_H_electroweak_matching_rows",
        "precision_covariance_or_diagonal_limitation",
        "accepted_precision_threshold_row_count_positive",
    ]:
        require(cutset["still_open"][key] is True, f"cutset open flag missing: {key}")
    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    require(cutset["closure_claimed"] is False, "cutset overclosed")

    closure = data["closure_decision"]
    require(closure["one_loop_gauge_bridge_policy_validation_closed"] is True, "candidate gauge bridge not closed")
    require(closure["top_higgs_threshold_map_targets_extracted"] is True, "candidate top/Higgs targets missing")
    require(closure["accepted_precision_threshold_row_count"] == 0, "candidate precision rows overaccepted")
    for key in [
        "same_branch_Rtheta_convention_source_theorem_closed",
        "top_higgs_threshold_maps_closed",
        "bottom_charm_tau_mass_scheme_maps_closed",
        "W_Z_H_electroweak_matching_rows_closed",
        "profile_covariance_or_diagonal_limitation_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(closure[key] is False, f"candidate overclosed: {key}")
    require("one-loop gauge bridge accepted as policy validation : true" in note, "note missing gauge line")
    require("accepted precision threshold row count              : 0" in note, "note missing zero precision row")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
