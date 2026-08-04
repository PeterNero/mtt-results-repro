"""Audit the frozen SM-parity boundary and post-SM-parity frontier artifact."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_smparityfrozenboundary_or_postsmparityfrontier"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
BOUNDARY = PACKET_DIR / "frozen_smparity_boundary.packet.json"
TAXONOMY = PACKET_DIR / "post_smparity_tier_taxonomy.packet.json"
NEXT = PACKET_DIR / "next_work_after_frozen_boundary.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_SMParityFrozenBoundary_or_PostSMParityFrontier_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_SMPARITY_FROZEN_BOUNDARY_BUILT_POST_SMPARITY_FRONTIER_LOCKED"
NEXT_ARTIFACT = "MTT_Selected_DynamicQaSU3_or_C1Response_PostSourceFrontier_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    boundary = load(BOUNDARY)
    taxonomy = load(TAXONOMY)
    next_work = load(NEXT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem not proved")
    require(data["next_required_artifact"] == NEXT_ARTIFACT, "candidate next artifact mismatch")
    require(cert["next_required_artifact"] == NEXT_ARTIFACT, "cert next artifact mismatch")

    require(boundary["boundary_locks"] is True, "boundary not locked")
    require(boundary["closed_tiers"]["SM_parity_replay_under_declared_standard"] is True, "SM-parity tier not closed")
    require(boundary["closed_tiers"]["finite_operator_source_slot_layer"] is True, "source slot tier not closed")
    for key, value in boundary["proof_inputs"].items():
        require(value is True, f"proof input false: {key}")
    for reason in [
        "true SM equivalence is still open",
        "no-knob constants derivation is still open",
        "dynamic Qa/SU3 or C1 source upgrades remain open",
        "precision RG/threshold/covariance work remains open",
    ]:
        require(reason in boundary["reopen_policy"]["must_not_reopen_SM_parity_because"], f"missing no-reopen reason: {reason}")
    require(boundary["reopen_policy"]["active_label_for_remaining_work"] == "post-SM-parity true-equivalence/no-knob frontier", "active label mismatch")
    require(boundary["guardrails"]["true_SM_equivalence_closed"] is False, "true equivalence overclosed")
    require(boundary["guardrails"]["no_knob_closed"] is False, "no-knob overclosed")

    tiers = {tier["id"]: tier for tier in taxonomy["tiers"]}
    require(tiers["tier_0_sm_parity_replay"]["status"] == "CLOSED_FROZEN", "tier 0 not frozen")
    require(tiers["tier_1_finite_source_slot_layer"]["status"] == "CLOSED_FROZEN", "tier 1 not frozen")
    require(tiers["tier_2_post_sm_parity_true_equivalence"]["status"] == "OPEN_ACTIVE", "tier 2 not active")
    require(tiers["tier_2_post_sm_parity_true_equivalence"]["primary_next"] == NEXT_ARTIFACT, "tier 2 next mismatch")
    require(tiers["tier_3_no_knob_derivation"]["status"] == "OPEN_SEPARATE_STRONGER_THAN_SM", "tier 3 status mismatch")
    require(taxonomy["language_rule"]["preferred_phrase"] == "post-SM-parity frontier", "preferred phrase mismatch")
    require(taxonomy["language_rule"]["forbidden_regression_phrase"] == "SM-parity is still blocked", "forbidden phrase mismatch")

    require(next_work["next_required_artifact"] == NEXT_ARTIFACT, "next packet artifact mismatch")
    require("actual dynamic Qa/SU3 operator packet" in next_work["active_open_items"], "dynamic open item missing")
    require("selected dotD_alpha1 and primitive C1 response source identity" in next_work["active_open_items"], "C1 open item missing")
    require(next_work["superset_strategy"]["mode"] == "combine several source lanes with a locked post-SM-parity target", "superset mode mismatch")
    require(next_work["superset_strategy"]["locked_target"] == "dynamic selected operator/value machinery, not another SM-parity replay proof", "locked target mismatch")

    closure = data["closure_decision"]
    require(closure["SM_parity_closed_frozen"] is True, "candidate SM-parity not frozen")
    require(closure["finite_operator_source_slot_layer_closed_frozen"] is True, "candidate source slot not frozen")
    require(closure["true_SM_equivalence_closed"] is False, "candidate true equivalence overclosed")
    require(closure["no_knob_closed"] is False, "candidate no-knob overclosed")
    require(data["what_closes_now"]["post_SM_parity_language_rule_locked"] is True, "language rule not closed")

    require("This artifact freezes the boundary" in note, "note boundary statement missing")
    require("Do not say SM-parity is blocked" in note, "note language rule missing")
    require(NEXT_ARTIFACT in note, "note next artifact missing")

    for packet in [data, boundary, taxonomy, next_work, cert]:
        require(packet.get("observed_data_used_as_selector") is False or packet.get("guardrails", {}).get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False or packet.get("guardrails", {}).get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
