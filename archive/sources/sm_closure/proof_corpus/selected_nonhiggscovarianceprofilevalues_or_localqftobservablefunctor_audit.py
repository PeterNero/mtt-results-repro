"""Audit non-Higgs covariance profile values or local QFT observable functor."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_nonhiggscovarianceprofilevalues_or_localqftobservablefunctor"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PROFILE = PACKET_DIR / "nonhiggs_precision_profile_status.packet.json"
FUNCTOR = PACKET_DIR / "local_qft_observable_functor_status.packet.json"
NEXT = PACKET_DIR / "next_true_equivalence_cutset.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_NonHiggsCovarianceProfileValues_or_LocalQFTObservableFunctor_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_NONHIGGSCOVARIANCEPROFILEVALUES_OR_LOCALQFTOBSERVABLEFUNCTOR_BUILT_ENVELOPE_TREEFUNCTOR_CLOSED_PRECISION_OPEN"
NEXT_ARTIFACT = "MTT_Selected_TrueEquivalencePrecisionValueTable_or_ActualQaSU3OperatorUpgrade_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    profile = load(PROFILE)
    functor = load(FUNCTOR)
    next_cutset = load(NEXT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["next_required_artifact"] == NEXT_ARTIFACT, "candidate next artifact mismatch")
    require(cert["next_required_artifact"] == NEXT_ARTIFACT, "certificate next artifact mismatch")

    require(profile["diagonal_profile_executed"] is True, "diagonal profile not executed")
    require(profile["coarse_profile_passes"] is True, "coarse profile does not pass")
    require(profile["correlation_envelope_built"] is True, "correlation envelope missing")
    require(profile["full_correlated_profile_closed"] is False, "full correlated profile overclosed")
    require(profile["accepted_for_SM_parity_replay"] is True, "profile not accepted for parity")
    require(profile["accepted_for_true_SM_equivalence"] is False, "profile overaccepted for true equivalence")

    require(functor["tree_QFT_identity_tier_closed"] is True, "tree QFT tier not closed")
    require(functor["precision_local_QFT_observable_values_closed"] is False, "precision QFT overclosed")
    require(functor["accepted_for_SM_parity_replay"] is True, "functor not accepted for parity")
    require(functor["accepted_for_true_SM_equivalence"] is False, "functor overaccepted")
    require(len(functor["covered_tree_rows"]) >= 6, "tree row coverage too small")
    require(len(functor["missing_precision_rows"]) >= 5, "missing precision rows not tracked")

    require(next_cutset["SM_parity_closed"] is True, "SM parity not closed")
    require(next_cutset["true_SM_equivalence_closed"] is False, "true equivalence overclosed")
    require(next_cutset["no_knob_closed"] is False, "no-knob overclosed")
    require(next_cutset["recommended_next_artifact"] == NEXT_ARTIFACT, "next cutset artifact mismatch")
    require("actual selected Qa/SU3 operator/source packet" in next_cutset["remaining_cutset"], "Qa/SU3 cutset missing")

    require(data["closure_decision"]["SM_parity_closed"] is True, "candidate parity closure missing")
    require(data["closure_decision"]["nonHiggs_envelope_integrated"] is True, "candidate profile integration missing")
    require(data["closure_decision"]["tree_QFT_functor_integrated"] is True, "candidate functor integration missing")
    require(data["closure_decision"]["true_SM_equivalence_closed"] is False, "candidate true overclosed")
    require(cert["nonHiggs_envelope_integrated"] is True, "certificate profile integration missing")
    require(cert["tree_QFT_functor_integrated"] is True, "certificate functor integration missing")
    require("not enough for true SM equivalence" in note, "note missing guardrail")

    for packet in [profile, functor, next_cutset, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
