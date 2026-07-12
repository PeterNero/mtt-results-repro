"""Audit Higgs route-A derivative engines or official likelihood decision."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_higgsrouteaformuladerivativeengines_or_officiallikelihooddecision"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
OFFICIAL_AUDIT = PACKET_DIR / "official_likelihood_source_audit.packet.json"
ROUTE_A_HANDOFF = PACKET_DIR / "route_a_derivative_engine_handoff.packet.json"
PROFILE_POLICY = PACKET_DIR / "higgs_precision_profile_policy_after_decision.packet.json"
UPDATED_TRUE = PACKET_DIR / "updated_true_equivalence_gate_after_official_likelihood_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HiggsRouteAFormulaDerivativeEngines_or_OfficialLikelihoodDecision_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_HIGGSROUTEAFORMULADERIVATIVEENGINES_OR_OFFICIALLIKELIHOODDECISION_BUILT_OFFICIAL_LIKELIHOOD_RETIRED_ROUTEA_PRIMARY"
NEXT = "MTT_Selected_HiggsRouteADerivativeEngineExecution_or_PrecisionDecision_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    official = load(OFFICIAL_AUDIT)
    handoff = load(ROUTE_A_HANDOFF)
    policy = load(PROFILE_POLICY)
    updated = load(UPDATED_TRUE)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, "next artifact mismatch")

    require(official["official_likelihood_route_retired_for_now"] is True, "official route not retired")
    require(official["retirement_is_reversible_if_artifact_found"] is True, "reversibility missing")
    require(official["accepted_as_official_LHCHXSWG_likelihood"] is False, "official likelihood overaccepted")
    require(official["published_profile_replay_available"] is True, "published replay not retained")
    require(len(official["official_sources_checked"]) >= 4, "source audit too small")
    require(any("RooWorkspace" in item for item in official["required_for_official_likelihood_promotion"]), "workspace requirement missing")
    require(any("not found" in official["status"].lower() or "retired" in official["status"].lower() for _ in [0]), "official decision unclear")

    require(handoff["primary_route"] == "route_A_partial_width_formula_derivative_engines", "route-A not primary")
    require(handoff["secondary_route"] == "official_likelihood_import_if_a_versioned_workspace_is_found", "secondary official route missing")
    require(len(handoff["engine_rows_required"]) == 10, "engine row contract incomplete")
    require({row["row"] for row in handoff["engine_rows_required"]} == {
        "H_to_bb",
        "H_to_cc",
        "H_to_ss",
        "H_to_tau_tau",
        "H_to_mu_mu",
        "H_to_gg",
        "H_to_gamma_gamma",
        "H_to_Z_gamma",
        "H_to_WW_star",
        "H_to_ZZ_star",
    }, "engine row set mismatch")
    require(handoff["locked_inputs_already_available"]["published_decay_covariance_replay"] is True, "published replay input missing")
    require(handoff["superset_strategy_use"]["locked_target"] == "SM-parity Higgs precision replay; no measured value may select MTT source structure", "locked target mismatch")

    require(policy["precision_total_width_closed"] is False, "precision total overclosed")
    require(policy["precision_branching_ratios_closed"] is False, "precision BR overclosed")
    require(policy["current_profile_precision_summary"]["tracked_total_width_sigma_GeV"] > 0, "profile sigma missing")
    require(policy["official_gate_status"] == "OFFICIAL_LHCHXSWG_FULL_LIKELIHOOD_STILL_NOT_IMPORTED", "official gate status mismatch")

    require(updated["guardrails"]["official_LHCHXSWG_likelihood_route_retired_for_now"] is True, "updated retirement missing")
    require(updated["guardrails"]["published_profile_replay_retained_for_SM_parity"] is True, "updated profile retention missing")
    require(updated["guardrails"]["route_A_derivative_engines_selected_as_primary"] is True, "updated route-A primary missing")
    require(updated["guardrails"]["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(updated["guardrails"]["no_knob_closed"] is False, "no-knob overclosed")

    require(data["closure_decision"]["official_likelihood_route_retired_for_now"] is True, "candidate retirement missing")
    require(data["closure_decision"]["published_profile_replay_retained_for_SM_parity"] is True, "candidate profile retention missing")
    require(data["closure_decision"]["route_A_derivative_engines_selected_as_primary"] is True, "candidate route-A missing")
    require(cert["official_likelihood_route_retired_for_now"] is True, "certificate retirement missing")
    require("retired for now" in note and "route-A" in note, "note missing decision")

    for packet in [official, handoff, policy, updated, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
