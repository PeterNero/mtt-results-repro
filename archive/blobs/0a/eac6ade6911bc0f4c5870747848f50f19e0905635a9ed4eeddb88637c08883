"""Audit PSM-C1-02 pre-residual operator source attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_psm_c1_02_preresidualoperators_or_routea_physicalrestriction"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
CURRENT = PACKET_DIR / "psm_c1_02_current_unpatched_operator_source_audit.packet.json"
CONDITIONAL_PAYLOAD = PACKET_DIR / "route_b_conditional_preresidual_operator_validator_payload.packet.json"
CONDITIONAL_RESULT = PACKET_DIR / "route_b_conditional_preresidual_operator_validator_result.packet.json"
CUTSET = PACKET_DIR / "physical_selection_cutset.packet.json"
NEXT = PACKET_DIR / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PSM_C1_02_PreResidualOperators_or_ROUTE_A_PhysicalRestriction_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_PSM_C1_02_PRERESIDUALOPERATORS_OR_ROUTEA_PHYSICALRESTRICTION_BUILT_CONDITIONAL_CLOSE_UNPATCHED_OPEN"
NEXT_ARTIFACT = "MTT_Selected_PSM_C1_02_PhysicalSelectionLemma_or_PSM_C1_04_HessianSourceRows_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    current = load(CURRENT)
    conditional_payload = load(CONDITIONAL_PAYLOAD)
    conditional_result = load(CONDITIONAL_RESULT)
    cutset = load(CUTSET)
    next_work = load(NEXT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem mismatch")
    require(data["closure_claimed"] is False, "candidate should not claim unpatched closure")
    require(data["conditional_only"] is True, "candidate should be conditional only")
    require(data["next_required_artifact"] == NEXT_ARTIFACT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT_ARTIFACT, "certificate next mismatch")

    require(current["status"] == "PSM_C1_02_UNPATCHED_OPEN_CONDITIONAL_SUPPORT_MAXIMIZED", "current status mismatch")
    require(current["current_unpatched_field_value"] is False, "unpatched PSM-C1-02 overclosed")
    require(current["field_closure_decision"]["unpatched_PSM_C1_02_closed"] is False, "unpatched closure mismatch")
    require(current["field_closure_decision"]["conditional_local_principle_closes_PSM_C1_02"] is True, "conditional support missing")
    require(current["field_closure_decision"]["residual_projector_replay_used_as_source"] is True, "replay guardrail missing")
    for key, value in current["support_closed"].items():
        require(value is True, f"support unexpectedly false: {key}")

    route_b = conditional_payload["route_B_independent_rowkernel_source"]
    require(route_b["selected_basis_feeds_all_72_row_functionals"] is True, "selected basis missing")
    require(route_b["pre_residual_phase_shift_variation_operators"] is True, "conditional pre-residual field missing")
    for key in [
        "independent_hessian_counterterm_source_rows",
        "sector_rows_assembled_from_source_rows",
        "no_residual_projector_replay_or_locked_target_as_source",
    ]:
        require(route_b[key] is False, f"remaining Route B field overclosed: {key}")
    require(len(route_b["attached_source_evidence"]) >= 5, "conditional evidence count low")
    require(conditional_result["passes"] is False, "conditional payload should still fail full validator")
    require(conditional_result["returncode"] == 1, "conditional validator return mismatch")

    require(cutset["status"] == "PSM_C1_02_REDUCED_TO_PHYSICAL_SELECTION_OR_HESSIAN_SOURCE_ROWS", "cutset status mismatch")
    require(len(cutset["minimal_unpatched_cutset"]) == 4, "cutset size mismatch")
    require(cutset["minimal_unpatched_cutset"][0]["label"] == "PSM-C1-02", "cutset first label mismatch")
    require("source promotion" in cutset["why_this_is_progress"], "cutset progress statement missing")

    require(next_work["next_required_artifact"] == NEXT_ARTIFACT, "next artifact mismatch")
    require(next_work["recommended_primary"]["label"] == "PSM-C1-02", "primary label mismatch")
    require(next_work["co_primary"]["label"] == "PSM-C1-04", "co-primary label mismatch")
    require(next_work["route_A_sidecar"]["label"] == "PSM-C1-01", "Route A sidecar mismatch")

    closure = data["closure_decision"]
    require(closure["PSM_C1_02_closed_unpatched"] is False, "PSM-C1-02 unpatched overclosed")
    require(closure["PSM_C1_02_closed_conditional_local_principle"] is True, "conditional closure missing")
    for key in ["unpatched_dynamic_C1_packet_closed", "true_SM_equivalence_closed", "no_knob_closed"]:
        require(closure[key] is False, f"overclosed: {key}")

    require("not closed unpatched" in note, "note unpatched guardrail missing")
    require("conditional lane closes `PSM-C1-02`" in note, "note conditional result missing")
    require("Superset Use" in note, "note superset section missing")
    require(NEXT_ARTIFACT in note, "note next artifact missing")

    for packet in [data, current, conditional_payload, conditional_result, cutset, next_work, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
