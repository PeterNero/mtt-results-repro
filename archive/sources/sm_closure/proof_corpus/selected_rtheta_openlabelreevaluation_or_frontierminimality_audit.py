"""Audit R_theta open-label re-evaluation / frontier minimality."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_rtheta_openlabelreevaluation_or_frontierminimality"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
OPEN_INVENTORY = PACKET_DIR / "open_label_inventory.packet.json"
REEVALUATION = PACKET_DIR / "open_label_reevaluation_results.packet.json"
MINIMAL_FRONTIER = PACKET_DIR / "minimal_rtheta_frontier_after_open_recheck.packet.json"
DECISION = PACKET_DIR / "open_label_frontier_minimality_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_open_label_recheck.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_RThetaOpenLabelReevaluation_or_FrontierMinimality_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_RTHETA_OPENLABELREEVALUATION_OR_FRONTIERMINIMALITY_"
    "BUILT_STALE_OPEN_LABELS_RETIRED_FRONTIER_MINIMAL"
)
NEXT = "MTT_Selected_RThetaCoefficientFormulaDerivation_or_SelectedOwnerBridge_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    inventory = load(OPEN_INVENTORY)
    reevaluation = load(REEVALUATION)
    minimal = load(MINIMAL_FRONTIER)
    decision = load(DECISION)
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

    require(inventory["status"] == "OPEN_LABEL_INVENTORY_BUILT", "inventory status mismatch")
    for key in [
        "support_open_labels",
        "owner_candidate_open_labels",
        "terminal_smslot_open_labels",
        "dynamic_value_phenomenology_open_labels",
        "dynamic_c1_open_labels",
        "actual_sm_packet_open_labels",
    ]:
        require(inventory[key], f"inventory bucket unexpectedly empty: {key}")
    require(
        "gauge_threshold_no_knob_backlog" in inventory["support_open_labels"],
        "gauge duplicate not inventoried",
    )
    require(
        "yukawa_higgs_no_knob_backlog" in inventory["support_open_labels"],
        "yukawa duplicate not inventoried",
    )
    require(inventory["closure_claimed"] is False, "inventory overclaimed")

    require(
        reevaluation["status"] == "OPEN_LABELS_REEVALUATED_STALE_AND_DUPLICATE_LABELS_RETIRED",
        "reevaluation status mismatch",
    )
    require(reevaluation["rechecked_label_count"] == 11, "wrong rechecked label count")
    require(reevaluation["duplicate_retired_count"] == 2, "wrong duplicate retired count")
    require(
        reevaluation["closed_for_dynamic_matter_route_count"] == 2,
        "wrong dynamic route closure count",
    )
    require(
        reevaluation["downstream_not_rtheta_owner_blocker_count"] == 3,
        "wrong downstream classification count",
    )
    require(
        reevaluation["dynamic_packet_closes_overlap_transfer_normalization_for_current_route"] is True,
        "dynamic packet did not close overlap/normalization for current route",
    )
    rows = {row["label"]: row for row in reevaluation["results"]}
    require(
        rows["gauge_threshold_no_knob_backlog"]["new_classification"]
        == "duplicate_retired_into_route_evidence",
        "gauge duplicate not retired",
    )
    require(
        rows["yukawa_higgs_no_knob_backlog"]["new_classification"]
        == "duplicate_retired_into_route_evidence",
        "yukawa duplicate not retired",
    )
    for label in ["primitive_C1_overlap_contractions", "selected_overlap_transfer_normalization"]:
        require(
            rows[label]["new_classification"]
            == "closed_for_dynamic_matter_route_open_only_for_terminal_six_arrow_route",
            f"{label} not narrowed correctly",
        )
    require(
        rows["full_profile_likelihood_or_accepted_diagonal_theorem"][
            "new_classification"
        ]
        == "active_top_level_frontier",
        "profile response incorrectly retired",
    )
    require(reevaluation["closure_claimed"] is False, "reevaluation overclaimed")

    require(
        minimal["status"] == "MINIMAL_RTHETA_FRONTIER_CONFIRMED_AFTER_OPEN_LABEL_RECHECK",
        "minimal frontier status mismatch",
    )
    require(len(minimal["active_frontier"]) == 4, "frontier should have four obligations")
    require(minimal["minimal_frontier_changed"] is False, "frontier changed unexpectedly")
    for item in [
        "bridge same-source dynamic matter/overlap packet to VSD02 threshold response owner",
        "derive threshold and mass-scheme coefficient formulas",
        "select precision convention before measured-value comparison",
        "attach full profile response or accepted diagonal limitation theorem",
    ]:
        require(item in minimal["active_frontier"], f"frontier item missing: {item}")
    require(
        "Yukawa magnitude closure" in minimal["not_on_immediate_rtheta_frontier"],
        "downstream Yukawa label not removed from immediate frontier",
    )
    require(minimal["closure_claimed"] is False, "minimal frontier overclaimed")

    require(
        decision["status"] == "OPEN_LABEL_RECHECK_CLOSED_FRONTIER_REMAINS_FOUR_OBLIGATIONS",
        "decision status mismatch",
    )
    for key in [
        "open_label_inventory_closed",
        "stale_duplicate_open_labels_retired",
        "dynamic_matter_route_reclassifications_closed",
        "minimal_frontier_confirmed",
    ]:
        require(decision[key] is True, f"decision close flag missing: {key}")
    for key in [
        "rtheta_packet_constructed",
        "selected_threshold_response_functional_instantiated",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed: {key}")
    require(len(decision["active_frontier"]) == 4, "decision frontier should have four obligations")
    require(decision["closure_claimed"] is False, "decision overclaimed")

    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    require(cutset["closed_now"]["minimal_frontier_confirmed"] is True, "cutset missing frontier confirmation")
    require(cutset["closure_claimed"] is False, "cutset overclaimed")

    final = data["closure_decision"]
    for key in [
        "open_label_recheck_closed",
        "stale_duplicate_open_labels_retired",
        "minimal_frontier_confirmed",
    ]:
        require(final[key] is True, f"candidate final close missing: {key}")
    for key in [
        "rtheta_packet_constructed",
        "selected_threshold_response_functional_instantiated",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(final[key] is False, f"candidate final overclosed: {key}")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require(cert["duplicate_retired_count"] == 2, "certificate duplicate count mismatch")
    require(cert["closed_for_dynamic_matter_route_count"] == 2, "certificate dynamic route count mismatch")
    require("minimal frontier obligations       : 4" in note, "note missing four-obligation guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
