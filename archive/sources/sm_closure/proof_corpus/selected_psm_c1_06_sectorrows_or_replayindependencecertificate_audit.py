"""Audit PSM-C1-06 sector-row/replay-independence certificate gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_psm_c1_06_sectorrows_or_replayindependencecertificate"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
UNPATCHED = PACKET_DIR / "unpatched_sector_rows_and_replay_independence_status.packet.json"
CONDITIONAL_PAYLOAD = PACKET_DIR / "route_b_full_conditional_validator_payload.packet.json"
CONDITIONAL_RESULT = PACKET_DIR / "route_b_full_conditional_validator_result.packet.json"
FINAL_GATE = PACKET_DIR / "final_unpatched_source_identity_gate.packet.json"
NEXT = PACKET_DIR / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PSM_C1_06_SectorRows_or_ReplayIndependenceCertificate_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_PSM_C1_06_SECTORROWS_OR_REPLAYINDEPENDENCECERTIFICATE_BUILT_CONDITIONAL_ROUTEB_VALIDATES"
NEXT_ARTIFACT = "MTT_Selected_UnpatchedFiniteC1SourceIdentityPrinciple_or_HonestIndependentKernelExport_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    unpatched = load(UNPATCHED)
    conditional_payload = load(CONDITIONAL_PAYLOAD)
    conditional_result = load(CONDITIONAL_RESULT)
    final_gate = load(FINAL_GATE)
    next_work = load(NEXT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem mismatch")
    require(data["closure_claimed"] is False, "candidate should not claim unpatched closure")
    require(data["conditional_only"] is True, "candidate should be conditional")
    require(data["next_required_artifact"] == NEXT_ARTIFACT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT_ARTIFACT, "certificate next mismatch")

    require(unpatched["status"] == "UNPATCHED_SECTOR_ROWS_FORMAL_REPLAY_INDEPENDENCE_OPEN", "unpatched status mismatch")
    for key, value in unpatched["unpatched_support"].items():
        require(value is True, f"unpatched support false: {key}")
    for key, value in unpatched["unpatched_blockers"].items():
        require(value is False, f"unpatched blocker unexpectedly true: {key}")
    require(unpatched["conditional_support"]["sector_rows_physical_source_promotion"] is True, "conditional sector support missing")
    require(unpatched["conditional_support"]["independence_from_residual_projector_replay"] is True, "conditional replay independence missing")
    require(unpatched["conditional_support"]["residual_projector_replay_used_as_source"] is False, "conditional replay source violation")

    route_b = conditional_payload["route_B_independent_rowkernel_source"]
    for key in [
        "same_branch",
        "selected_basis_feeds_all_72_row_functionals",
        "pre_residual_phase_shift_variation_operators",
        "independent_hessian_counterterm_source_rows",
        "sector_rows_assembled_from_source_rows",
        "no_residual_projector_replay_or_locked_target_as_source",
    ]:
        require(route_b[key] is True, f"conditional Route-B field false: {key}")
    require(len(route_b["attached_source_evidence"]) >= 5, "conditional evidence count low")
    require(conditional_result["passes"] is True, "conditional validator should pass")
    require(conditional_result["returncode"] == 0, "conditional validator return mismatch")

    require(final_gate["status"] == "UNPATCHED_C1_REDUCED_TO_SOURCE_IDENTITY_OR_INDEPENDENT_KERNEL_EXPORT", "final gate status mismatch")
    require(final_gate["conditional_routeB_validates"] is True, "conditional gate missing")
    require(final_gate["unpatched_routeB_validates"] is False, "unpatched overclosed")
    require(len(final_gate["two_legal_finishing_routes"]) == 2, "finishing route count mismatch")
    require(final_gate["two_legal_finishing_routes"][0]["route"] == "SOURCE_IDENTITY", "first route mismatch")
    require(final_gate["two_legal_finishing_routes"][1]["route"] == "HONEST_KERNEL_EXPORT", "second route mismatch")

    require(next_work["next_required_artifact"] == NEXT_ARTIFACT, "next artifact mismatch")
    require(next_work["recommended_primary"]["route"] == "SOURCE_IDENTITY", "primary route mismatch")
    require(next_work["alternative"]["route"] == "HONEST_KERNEL_EXPORT", "alternative route mismatch")

    closure = data["closure_decision"]
    require(closure["conditional_RouteB_validator_passes"] is True, "conditional closure missing")
    for key in ["unpatched_RouteB_validator_passes", "unpatched_dynamic_C1_packet_closed", "true_SM_equivalence_closed", "no_knob_closed"]:
        require(closure[key] is False, f"overclosed: {key}")

    require("Conditional Route B now validates all five strict fields" in note, "note conditional pass missing")
    require("Unpatched Route B does not validate" in note, "note unpatched guardrail missing")
    require("Superset Use" in note, "note superset missing")
    require(NEXT_ARTIFACT in note, "note next missing")

    for packet in [data, unpatched, conditional_payload, conditional_result, final_gate, next_work, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
