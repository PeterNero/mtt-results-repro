"""Audit the Higgs promotion-priority and profile-blueprint artifact."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_higgspromotionpriority_or_correlatedprofileblueprint"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PRIORITY = PACKET_DIR / "higgs_precision_promotion_priority.packet.json"
BLUEPRINT = PACKET_DIR / "higgs_correlated_profile_blueprint.packet.json"
STRATEGY = PACKET_DIR / "higgs_two_lane_precision_upgrade_strategy.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HiggsPromotionPriority_or_CorrelatedProfileBlueprint_v1.md"

STATUS = "MTT_SELECTED_HIGGSPROMOTIONPRIORITY_OR_CORRELATEDPROFILEBLUEPRINT_BUILT_NEXT_GATE_PRIORITIZED"
NEXT = "MTT_Selected_HiggsGammaGammaCorrection_or_QCDThresholdRows_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    priority = load(PRIORITY)
    blueprint = load(BLUEPRINT)
    strategy = load(STRATEGY)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["target_fitting_used"] is False, "target fitting overclaimed")
    require(priority["summary"]["observed_widths_used_as_selectors"] is False, "selector guard missing")
    require(priority["summary"]["precision_rows_promoted"] == 0, "precision row overpromoted")
    require(priority["summary"]["row_count"] == 10, "priority rows incomplete")
    require(priority["summary"]["top_priority_channels"][0] == "H_to_gamma_gamma", "top priority should be gamma gamma")
    require("H_to_ss" in priority["summary"]["high_tension_proxy_channels"], "ss high-tension row missing")
    require("H_to_gg" in priority["summary"]["high_tension_proxy_channels"] or any(row["channel"] == "H_to_gg" for row in priority["rows"]), "gg row missing")
    require(set(priority["summary"]["benchmark_replay_only_channels"]) == {"H_to_WW_star", "H_to_ZZ_star", "H_to_Z_gamma"}, "benchmark-only channels mismatch")
    require(blueprint["full_matrix"]["dimension"] == 10, "profile dimension mismatch")
    require(blueprint["full_matrix"]["required_entries"] == 100, "profile entry count mismatch")
    require(blueprint["full_matrix"]["filled_entries"] == 0, "profile values overfilled")
    require(blueprint["full_matrix"]["accepted_as_full_covariance_profile"] is False, "covariance overclaimed")
    require(len(strategy["lanes"]) == 2, "two-lane strategy missing")
    require(strategy["recommended_next_artifact"] == NEXT, "recommended next mismatch")
    require(data["closure_decision"]["precision_rows_promoted"] == 0, "candidate precision overclaim")
    require(data["closure_decision"]["true_SM_equivalence_closed"] is False, "true equivalence overclaimed")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require("does not promote any row" in note, "note missing guardrail")
    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
