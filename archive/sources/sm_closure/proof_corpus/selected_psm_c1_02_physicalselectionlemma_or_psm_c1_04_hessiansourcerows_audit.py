"""Audit physical-selection/Hessian-source compression for post-SM-parity C1."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_psm_c1_02_physicalselectionlemma_or_psm_c1_04_hessiansourcerows"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
UNPATCHED = PACKET_DIR / "unpatched_physical_selection_and_hessian_source_status.packet.json"
CONDITIONAL_PAYLOAD = PACKET_DIR / "route_b_conditional_selection_hessian_validator_payload.packet.json"
CONDITIONAL_RESULT = PACKET_DIR / "route_b_conditional_selection_hessian_validator_result.packet.json"
REMAINING = PACKET_DIR / "remaining_two_field_cutset.packet.json"
NEXT = PACKET_DIR / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PSM_C1_02_PhysicalSelectionLemma_or_PSM_C1_04_HessianSourceRows_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_PSM_C1_02_PHYSICALSELECTIONLEMMA_OR_PSM_C1_04_HESSIANSOURCEROWS_BUILT_CONDITIONAL_THREE_FIELD_ROUTEB"
NEXT_ARTIFACT = "MTT_Selected_PSM_C1_06_SectorRows_or_ReplayIndependenceCertificate_v1"


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
    remaining = load(REMAINING)
    next_work = load(NEXT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem mismatch")
    require(data["closure_claimed"] is False, "candidate should not claim closure")
    require(data["conditional_only"] is True, "candidate should be conditional")
    require(data["next_required_artifact"] == NEXT_ARTIFACT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT_ARTIFACT, "cert next mismatch")

    require(unpatched["status"] == "UNPATCHED_SELECTION_AND_HESSIAN_SOURCE_STILL_OPEN", "unpatched status mismatch")
    require(unpatched["PSM_C1_02"]["unpatched_closed"] is False, "PSM-C1-02 overclosed")
    require(unpatched["PSM_C1_02"]["conditional_closed"] is True, "PSM-C1-02 conditional missing")
    require(unpatched["PSM_C1_04"]["unpatched_closed"] is False, "PSM-C1-04 overclosed")
    require(unpatched["PSM_C1_04"]["formal_target_closed"] is True, "Hessian formal target missing")
    require(unpatched["PSM_C1_04"]["physical_source_promoted"] is False, "Hessian source overpromoted")
    require(unpatched["PSM_C1_04"]["formal_A_transpose_b"] == [12.0, 12.0], "A^T b mismatch")
    require(unpatched["PSM_C1_04"]["formal_deltaTheta_C1"] == [1.0, 1.0], "delta mismatch")
    for key, value in unpatched["shared_support"].items():
        require(value is True, f"shared support false: {key}")

    route_b = conditional_payload["route_B_independent_rowkernel_source"]
    require(route_b["selected_basis_feeds_all_72_row_functionals"] is True, "selected basis missing")
    require(route_b["pre_residual_phase_shift_variation_operators"] is True, "PSM-C1-02 conditional missing")
    require(route_b["independent_hessian_counterterm_source_rows"] is True, "PSM-C1-04 conditional missing")
    require(route_b["sector_rows_assembled_from_source_rows"] is False, "sector rows overclosed")
    require(route_b["no_residual_projector_replay_or_locked_target_as_source"] is False, "replay independence overclosed")
    require(len(route_b["attached_source_evidence"]) >= 5, "evidence count low")
    require(conditional_result["passes"] is False, "conditional payload should still fail")
    require(conditional_result["returncode"] == 1, "conditional validator code mismatch")

    require(remaining["status"] == "CONDITIONAL_ROUTE_B_REDUCED_TO_SECTOR_ROWS_AND_REPLAY_INDEPENDENCE", "remaining status mismatch")
    require(remaining["remaining_strict_fields"]["sector_rows_assembled_from_source_rows"] is False, "sector row cutset mismatch")
    require(remaining["remaining_strict_fields"]["no_residual_projector_replay_or_locked_target_as_source"] is False, "replay cutset mismatch")
    require(remaining["unpatched_reality_check"]["conditional_compression_is_not_a_source_theorem"] is True, "guardrail missing")

    require(next_work["next_required_artifact"] == NEXT_ARTIFACT, "next artifact mismatch")
    require(next_work["recommended_primary"]["label"] == "PSM-C1-06", "next primary mismatch")
    require(next_work["co_primary"]["label"] == "PSM-C1-02/PSM-C1-04 guardrail", "next co-primary mismatch")
    require(next_work["unpatched_backfill"]["labels"] == ["PSM-C1-02", "PSM-C1-04"], "backfill labels mismatch")

    closure = data["closure_decision"]
    require(closure["RouteB_three_of_five_fields_conditional"] is True, "conditional compression missing")
    require(closure["RouteB_validator_passes"] is False, "validator pass overclaimed")
    for key in [
        "PSM_C1_02_closed_unpatched",
        "PSM_C1_04_closed_unpatched",
        "unpatched_dynamic_C1_packet_closed",
        "true_SM_equivalence_closed",
        "no_knob_closed",
    ]:
        require(closure[key] is False, f"overclosed: {key}")

    require("3 of 5 Route-B fields" in note, "note compression missing")
    require("does not claim no-knob closure" in note, "note guardrail missing")
    require("Superset Use" in note, "note superset missing")
    require(NEXT_ARTIFACT in note, "note next missing")

    for packet in [data, unpatched, conditional_payload, conditional_result, remaining, next_work, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
