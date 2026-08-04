"""Audit selected HYM metric moment tau_H search."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_hymmetricmomenttauhsearch_or_finitepartexport"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
MOMENTS = PACKET_DIR / "selected_hym_metric_moment_inventory.packet.json"
SEARCH = PACKET_DIR / "hym_metric_tauh_candidate_search.packet.json"
FRONTIER = PACKET_DIR / "finitepart_export_frontier.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HYMMetricMomentTauHSearch_or_FinitePartExport_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_HYMMETRICMOMENTTAUHSEARCH_OR_FINITEPARTEXPORT_"
    "METRIC_MOMENT_NEARMISSES_REJECTED_FINITEPART_EXPORT_REQUIRED"
)
NEXT = "MTT_Selected_HWeightedFinitePartTauHExport_or_DirectRadialOperator_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("closure_claimed") is True, f"{label} closure")
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    moments = load(MOMENTS)
    search = load(SEARCH)
    frontier = load(FRONTIER)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("moments", moments),
        ("search", search),
        ("frontier", frontier),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "certificate status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(frontier["next_required_artifact"] == NEXT, "frontier next")
    require(data["theorem"]["proved"] is True, "theorem")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaim")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaim")

    require(moments["mesh"] == 24, "mesh")
    require(moments["replay_residual_l2"] < 1e-11, "residual")
    for key in ["x1_l2", "y1_l2", "mean_exp_minus_u", "std_q", "s_beta"]:
        require(key in moments["moments"], f"missing moment {key}")

    require(search["accepted_tau_H_source_count"] == 0, "search accepted")
    require(len(search["best_near_misses"]) == 24, "near miss count")
    require(all(row["accepted_as_tau_H_source"] is False for row in search["best_near_misses"]), "overaccepted")
    require(search["special_clues"]["anisotropy_angular_relative_residual"] < 1e-5, "anisotropy clue")

    decision = data["closure_decision"]
    require(decision["selected_HYM_grid_replayed"] is True, "grid replay")
    require(decision["anisotropy_angular_clue_isolated"] is True, "clue isolated")
    require(decision["finitepart_export_required"] is True, "finitepart required")
    require(decision["strict_r_H_promoted"] is False, "rH overpromoted")

    for key in [
        "finite_part_operator",
        "H_weighted_metric_integral",
        "anisotropy_functional_source_rule",
        "tau_H_or_r_H_export",
    ]:
        require(frontier["required_export_rows"][key] is False, f"frontier overfilled {key}")

    for phrase in [
        "HYMMetricMomentSearchAndFinitePartFrontierTheorem",
        "Accepted HYM metric-moment source rows: `0`",
        "4 + (x1_l2/y1_l2)/(3 - 4*s_beta)",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print("AUDIT_PASS: HYM metric moment tau_H search found sharp clues but no accepted source export.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
