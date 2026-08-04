"""Audit selected_psm_c1_02_variationalprojectionbridge_or_rowsource."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
SLUG = "selected_psm_c1_02_variationalprojectionbridge_or_rowsource"
BASE = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
EXTERNAL = BASE / "external_variational_support.packet.json"
BRIDGE = BASE / "selected_variational_projection_bridge_theorem.packet.json"
ROUTE_A = BASE / "route_a_physical_source_projection_bridge.packet.json"
ROUTE_B = BASE / "route_b_rowsource_projection_bridge.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PSM_C1_02_VariationalProjectionBridge_or_RowSource_v1.md"
BUILD = ROOT / "scripts" / "build_selected_psm_c1_02_variationalprojectionbridge_or_rowsource.py"

STATUS = "MTT_SELECTED_PSM_C1_02_VARIATIONAL_PROJECTION_BRIDGE_BUILT_SELECTED_SOURCE_BRIDGE_OPEN"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict) -> None:
    require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
    require(packet.get("target_fitting_used") is False, "target fitting violation")
    require(packet.get("closure_claimed") is False, "closure overclaim")


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(BUILD)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if proc.returncode != 0:
        print(proc.stdout)
        return 1

    candidate = load(CANDIDATE)
    external = load(EXTERNAL)
    bridge = load(BRIDGE)
    route_a = load(ROUTE_A)
    route_b = load(ROUTE_B)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["active_routes"] == ["SOURCE-IDENTITY/VPB-1", "SOURCE-IDENTITY/SI-1u-B2-ROWSOURCE"], "active routes mismatch")
    require(candidate["theorem"]["proved"] is True, "reduction theorem missing")
    require(candidate["superset_strategy"]["paths_used_as_free_parameters"] is False, "superset used as knobs")

    require(external["external_supports"]["first_variation_shape"] is True, "external first variation support missing")
    require(external["external_supports"]["hym_operator_reformulation_shape"] is True, "external HYM operator support missing")
    require(external["external_supports"]["selected_finite_projection_identity"] is False, "external support overclosed selected bridge")
    require(len(external["sources"]) == 3, "external source count mismatch")

    require(bridge["status"] == "BRIDGE_THEOREM_TARGET_BUILT_NOT_PROVED", "bridge status mismatch")
    require(bridge["proved_now"] is False, "bridge overproved")
    require(bridge["still_missing"]["selected_projection_from_physical_action_to_finite_row_kernel_packet"] is True, "selected projection gap missing")
    require(bridge["if_proved_closes"]["SelectedFiniteC1SourcePromotionLemma"] is True, "source promotion consequence missing")

    require(route_a["status"] == "ROUTE_A_REDUCED_TO_SELECTED_VARIATIONAL_PROJECTION_BRIDGE", "route A status mismatch")
    require(route_a["bridge_proved_now"] is False, "route A overclosed")
    require("physical_first_variation_identity" in route_a["bridge_field_replaces"], "route A first variation missing")
    require("same_source_RZ_RX_bselected_emission" in route_a["bridge_field_replaces"], "route A source emission missing")

    require(route_b["status"] == "ROUTE_B_REDUCED_TO_SAME_SELECTED_FINITE_C1_SOURCE_PACKET", "route B status mismatch")
    require(route_b["bridge_proved_now"] is False, "route B overclosed")
    require("no_residual_projector_replay_or_locked_target_as_source" in route_b["bridge_field_replaces"], "route B residual guard missing")

    require(next_work["primary"]["label"] == "PSM-C1-02 / SOURCE-IDENTITY / VPB-1", "next primary mismatch")
    require(cert["bridge_proved_now"] is False, "cert overproved")
    require("SelectedFiniteC1VariationalProjectionBridge" in note, "note bridge missing")
    require("No closure is claimed" in note, "note guard missing")

    for item in [candidate, external, bridge, route_a, route_b, cert]:
        guard(item)

    print(f"PASS {CANDIDATE.name}: {candidate['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
