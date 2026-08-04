"""Audit Higgs imported-profile replay or official LHCHXSWG likelihood gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_higgsimportedprofilereplay_or_officiallhchxswglikelihood"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
OBS_REPLAY = PACKET_DIR / "imported_profile_observable_replay.packet.json"
PRECISION_SUMMARY = PACKET_DIR / "imported_profile_precision_summary.packet.json"
OFFICIAL_GATE = PACKET_DIR / "official_lhchxswg_likelihood_gate.packet.json"
UPDATED_TRUE = PACKET_DIR / "updated_true_equivalence_gate_after_imported_profile_replay.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HiggsImportedProfileReplay_or_OfficialLHCHXSWGLikelihood_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_HIGGSIMPORTEDPROFILEREPLAY_OR_OFFICIALLHCHXSWGLIKELIHOOD_BUILT_IMPORTED_PROFILE_REPLAY_OFFICIAL_LIKELIHOOD_OPEN"
NEXT = "MTT_Selected_HiggsRouteAFormulaDerivativeEngines_or_OfficialLikelihoodDecision_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    obs = load(OBS_REPLAY)
    summary = load(PRECISION_SUMMARY)
    official = load(OFFICIAL_GATE)
    updated = load(UPDATED_TRUE)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")

    require(obs["accepted_as_imported_profile_replay"] is True, "imported profile replay not accepted")
    require(obs["accepted_as_official_LHCHXSWG_likelihood"] is False, "official likelihood overaccepted")
    require(len(obs["input_partial_width_basis"]) == 10, "partial width basis mismatch")
    require(len(obs["observable_basis"]) == 11, "observable basis mismatch")
    require(len(obs["observable_covariance"]) == 11, "observable covariance row mismatch")
    require(all(len(row) == 11 for row in obs["observable_covariance"]), "observable covariance col mismatch")
    require(obs["max_covariance_asymmetry"] < 1e-18, "observable covariance not symmetric enough")
    require(obs["observable_sigmas"]["Gamma_total_tracked"] > 0, "total width sigma missing")
    require(obs["observable_relative_sigmas"]["Gamma_total_tracked"] > 0, "relative total width sigma missing")
    require(any(
        abs(obs["observable_correlation"][i][j]) > 0.05
        for i in range(11)
        for j in range(11)
        if i != j
    ), "observable profile lost off-diagonal correlations")

    require(summary["precision_profile_usable_for_SM_parity_replay"] is True, "SM parity replay usability missing")
    require(summary["precision_profile_sufficient_for_no_knob_closure"] is False, "no-knob overclosed")
    require(summary["tracked_total_width_sigma_GeV"] == obs["observable_sigmas"]["Gamma_total_tracked"], "summary sigma mismatch")
    require(len(summary["branching_ratio_sigmas"]) == 10, "BR sigma count mismatch")
    require(len(summary["dominant_observable_correlations"]) >= 6, "dominant correlation summary too small")

    require(official["published_decay_covariance_profile_imported"] is True, "published profile import flag missing")
    require(official["official_machine_readable_likelihood_imported"] is False, "official machine-readable likelihood overclaimed")
    require(official["nuisance_profile_semantics_imported"] is False, "nuisance semantics overclaimed")
    require(official["accepted_as_SM_parity_decay_covariance_replay"] is True, "SM parity acceptance missing")
    require(official["accepted_as_official_LHCHXSWG_likelihood"] is False, "official gate overaccepted")

    require(updated["guardrails"]["imported_profile_replay_built"] is True, "updated gate replay flag missing")
    require(updated["guardrails"]["official_LHCHXSWG_likelihood_imported"] is False, "updated gate official overclaimed")
    require(updated["guardrails"]["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(updated["guardrails"]["no_knob_closed"] is False, "no-knob overclosed")

    require(data["closure_decision"]["imported_profile_replay_closed"] is True, "candidate replay closure missing")
    require(data["closure_decision"]["accepted_as_SM_parity_covariance_replay"] is True, "candidate parity replay missing")
    require(data["closure_decision"]["accepted_as_official_LHCHXSWG_likelihood"] is False, "candidate official overaccepted")
    require(cert["next_required_artifact"] == NEXT, "next artifact mismatch")
    require("official LHCHXSWG machine-readable likelihood" in note, "note missing official-likelihood guard")

    for packet in [obs, summary, official, updated, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
