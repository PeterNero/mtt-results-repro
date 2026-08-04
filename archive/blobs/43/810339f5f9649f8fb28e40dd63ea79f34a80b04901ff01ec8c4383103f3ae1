"""Audit full SM-parity replay closure refresh or non-Higgs profile policy."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_fullsmparityreplayclosure_or_nonhiggsprofilepolicy"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
REFRESH = PACKET_DIR / "full_smparity_replay_closure_refresh.packet.json"
NONHIGGS = PACKET_DIR / "nonhiggs_profile_policy.packet.json"
GAP = PACKET_DIR / "remaining_true_equivalence_gap_after_replay_closure.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_FullSMParityReplayClosure_or_NonHiggsProfilePolicy_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_FULLSMPARITYREPLAYCLOSURE_OR_NONHIGGSPROFILEPOLICY_BUILT_REFRESHED_CLOSURE_TRUE_EQ_OPEN"
NEXT = "MTT_Selected_NonHiggsCovarianceProfileValues_or_LocalQFTObservableFunctor_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    refresh = load(REFRESH)
    nonhiggs = load(NONHIGGS)
    gap = load(GAP)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, "next artifact mismatch")

    require(refresh["SM_parity_closed"] is True, "prior SM parity not closed")
    require(refresh["SM_parity_closed_after_higgs_refresh"] is True, "refreshed closure missing")
    require(refresh["all_sector_rows_closed_for_SM_parity_replay"] is True, "sector replay row open")
    require(refresh["true_SM_equivalence_closed"] is False, "true equivalence overclosed")
    require(refresh["no_knob_closed"] is False, "no-knob overclosed")
    require(len(refresh["sector_rows"]) >= 5, "sector rows too small")
    for row in refresh["sector_rows"]:
        require(row["SM_parity_replay_closed"] is True, f"sector row open: {row['sector']}")
        require(row["true_equivalence_closed"] is False, f"sector true equivalence overclosed: {row['sector']}")
        require(row["no_knob_closed"] is False, f"sector no-knob overclosed: {row['sector']}")

    require(nonhiggs["accepted_for_SM_parity_replay"] is True, "non-Higgs parity replay not accepted")
    require(nonhiggs["full_covariance_profile_required_for_SM_parity"] is False, "full covariance required for parity")
    require(nonhiggs["full_covariance_profile_required_for_true_equivalence"] is True, "true-equivalence covariance gate missing")
    require(len(nonhiggs["central_replay_sources"]) >= 4, "non-Higgs sources missing")

    require(gap["SM_parity_closed"] is True, "gap says SM parity open")
    require(gap["true_SM_equivalence_closed"] is False, "gap true equivalence overclosed")
    require(gap["no_knob_closed"] is False, "gap no-knob overclosed")
    require("actual selected Qa/SU3 color/operator packet replacing the parity-interface substitute" in gap["remaining_true_equivalence_gates"], "Qa/SU3 gate missing")
    require("full non-Higgs covariance/profile values and correlations" in gap["remaining_true_equivalence_gates"], "non-Higgs profile gate missing")

    require(data["closure_decision"]["SM_parity_closed"] is True, "candidate closure missing")
    require(data["closure_decision"]["SM_parity_closed_after_Higgs_refresh"] is True, "candidate refresh missing")
    require(data["closure_decision"]["true_SM_equivalence_closed"] is False, "candidate true overclosed")
    require(data["closure_decision"]["no_knob_closed"] is False, "candidate no-knob overclosed")
    require(cert["SM_parity_closed_after_Higgs_refresh"] is True, "certificate refresh missing")
    require("SM-parity replay closure remains true" in note, "note missing closure statement")

    for packet in [refresh, nonhiggs, gap, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
