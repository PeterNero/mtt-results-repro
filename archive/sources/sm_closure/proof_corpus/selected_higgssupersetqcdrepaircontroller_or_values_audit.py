"""Audit the superset QCD repair controller."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_higgssupersetqcdrepaircontroller_or_values"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
CONTROLLER = PACKET_DIR / "superset_qcd_repair_controller.packet.json"
ACCEPTANCE = PACKET_DIR / "qcd_repair_value_acceptance_kernel.packet.json"
CUTSET = PACKET_DIR / "minimal_next_value_cutset.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HiggsSupersetQCDRepairController_or_Values_v1.md"

STATUS = "MTT_SELECTED_HIGGSSUPERSETQCDREPAIRCONTROLLER_OR_VALUES_BUILT_LOCKED_TARGET_VALUES_OPEN"
NEXT = "MTT_Selected_HiggsQCDRepairValues_or_ProfileCovarianceBlock_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    controller = load(CONTROLLER)
    acceptance = load(ACCEPTANCE)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["target_fitting_used"] is False, "target fitting overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed selector guard missing")
    require(controller["superset_strategy"]["mode"] == "MULTI_PATH_CONSTRAINTS_TO_LOCKED_TARGET", "wrong superset mode")
    require(controller["superset_strategy"]["paths_combined_as_knobs"] is False, "paths used as knobs")
    require(controller["superset_strategy"]["measured_targets_used_to_lock_source"] is False, "measured target source lock")
    require(len(controller["lanes"]) == 5, "controller lane count mismatch")
    lane_ids = {lane["lane_id"] for lane in controller["lanes"]}
    for lane in ["L0_straight_measured_replay", "L1_threshold_mass_scheme_contract", "L2_qasu3_source_operator", "L3_correlated_profile", "L4_inverse_discovery"]:
        require(lane in lane_ids, f"missing lane {lane}")
    require("benchmark_over_proxy_ratio as correction" in controller["locked_target"]["must_not_use"], "fit-ratio ban missing")
    require(acceptance["all_tests_closed"] is False, "acceptance overclosed")
    require(acceptance["values_promotable_now"] is False, "values overpromoted")
    require(acceptance["qasu3_promotable_packet_found"] is False, "Qa/SU3 overclaim")
    require(acceptance["inverse_search_role"] == "DISCOVERY_ONLY_SPEC", "inverse role mismatch")
    for row in acceptance["forbidden_fit_factors"]:
        require(row["blocked"] is True, f"fit factor not blocked: {row['channel']}")
    require(len(cutset["minimal_value_objects"]) == 3, "cutset count mismatch")
    require(cutset["smallest_next_executable_artifact"] == NEXT, "next artifact mismatch")
    require(data["closure_decision"]["superset_paths_used_as_knobs"] is False, "candidate knob misuse")
    require(data["closure_decision"]["values_promotable_now"] is False, "candidate values overpromoted")
    require(cert["next_required_artifact"] == NEXT, "cert next mismatch")
    require("combined only as constraints" in note, "note missing constraint language")
    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
