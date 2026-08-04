"""Audit profile likelihood source import or Qa/SU3 packet candidate mining."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_profilelikelihoodsourceimport_or_qasu3packetcandidatemining"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PROFILE_IMPORT = PACKET_DIR / "profile_likelihood_source_import_status.packet.json"
QASU3_MINING = PACKET_DIR / "qasu3_packet_candidate_mining.packet.json"
PROMOTION = PACKET_DIR / "promotion_decision_after_import_and_mining.packet.json"
CUTSET = PACKET_DIR / "next_import_or_payload_fill_cutset.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_ProfileLikelihoodSourceImport_or_QaSU3PacketCandidateMining_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_PROFILELIKELIHOODSOURCEIMPORT_OR_QASU3PACKETCANDIDATEMINING_BUILT_IMPORT_ABSENT_MINING_READY"
NEXT = "MTT_Selected_QaSU3CandidatePayloadFill_or_ProfileSourceAcquisition_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    profile = load(PROFILE_IMPORT)
    mining = load(QASU3_MINING)
    promotion = load(PROMOTION)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, "next artifact mismatch")

    require(profile["published_or_reconstructed_profile_imported"] is False, "profile import overclaimed")
    require(profile["surrogate_profile_retained"] is True, "surrogate not retained")
    require(profile["accepted_as_full_profile_likelihood"] is False, "profile likelihood overaccepted")
    require(profile["accepted_for_true_SM_equivalence"] is False, "profile overaccepted for true equivalence")
    require(len(profile["required_import_payload"]) >= 5, "profile import payload underspecified")

    require(mining["candidate_count"] == 4, "mined candidate count mismatch")
    require(mining["all_candidates_present"] is True, "mined candidate missing support")
    require(mining["any_candidate_promotable_now"] is False, "candidate overpromoted")
    require(mining["accepted_as_actual_QaSU3_packet"] is False, "Qa/SU3 packet overaccepted")
    require(mining["accepted_for_true_SM_equivalence"] is False, "Qa/SU3 true equivalence overaccepted")
    for row in mining["mined_candidates"]:
        require(row["present"] is True, f"candidate support missing: {row['candidate_id']}")
        require(row["promotable_now"] is False, f"candidate overpromoted: {row['candidate_id']}")

    require(promotion["route_A_profile_import"]["published_or_reconstructed_profile_imported"] is False, "route A overimported")
    require(promotion["route_A_profile_import"]["can_close_true_SM_equivalence_now"] is False, "route A overcloses")
    require(promotion["route_B_qasu3_mining"]["candidate_support_mined"] is True, "route B mining missing")
    require(promotion["route_B_qasu3_mining"]["any_candidate_promotable_now"] is False, "route B overpromoted")
    require(promotion["true_SM_equivalence_closed"] is False, "promotion true equivalence overclosed")
    require(promotion["no_knob_closed"] is False, "promotion no-knob overclosed")

    require(cutset["recommended_next_artifact"] == NEXT, "cutset next artifact mismatch")
    require("actual non-Higgs profile likelihood/covariance source import" in cutset["remaining_minimal_payloads"], "profile payload missing")
    require("or fill one mined Qa/SU3 candidate with selected operator maps and anomaly certificate" in cutset["remaining_minimal_payloads"], "Qa/SU3 payload missing")

    require(data["closure_decision"]["profile_likelihood_imported"] is False, "candidate profile import overclaimed")
    require(data["closure_decision"]["qasu3_candidates_mined"] is True, "candidate mining missing")
    require(data["closure_decision"]["any_qasu3_candidate_promotable_now"] is False, "candidate promotion overclaimed")
    require(data["closure_decision"]["true_SM_equivalence_closed"] is False, "candidate true equivalence overclosed")
    require(cert["profile_likelihood_imported"] is False, "certificate profile import overclaimed")
    require(cert["qasu3_candidates_mined"] is True, "certificate mining missing")
    require(cert["any_qasu3_candidate_promotable_now"] is False, "certificate overpromoted")
    require("none has the non-null selected operator payload" in note, "note missing operator payload guardrail")

    for packet in [profile, mining, promotion, cutset, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
