"""Audit unpatched PSM-C1-01 exit audit against Route B row-kernel execution."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_psm_c1_01_unpatchedsourcelemma_or_routeb_rowkernelexecution"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ROUTE_A = PACKET_DIR / "route_a_unpatched_source_lemma_field_audit.packet.json"
ROUTE_B = PACKET_DIR / "route_b_rowkernel_execution_field_audit.packet.json"
DELTA = PACKET_DIR / "two_exit_validator_delta.packet.json"
LABEL_STATUS = PACKET_DIR / "label_status_after_unpatched_exit_audit.packet.json"
NEXT = PACKET_DIR / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PSM_C1_01_UnpatchedSourceLemma_or_ROUTE_B_RowKernelExecution_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_PSM_C1_01_UNPATCHEDSOURCELEMMA_OR_ROUTE_B_ROWKERNELEXECUTION_BUILT_ROUTEB_ONE_FIELD_CLOSED"
NEXT_ARTIFACT = "MTT_Selected_PSM_C1_02_ROUTE_B_PreResidualOperators_or_PSM_C1_01_PhysicalRestriction_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    route_a = load(ROUTE_A)
    route_b = load(ROUTE_B)
    delta = load(DELTA)
    labels = load(LABEL_STATUS)
    next_work = load(NEXT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem not proved")
    require(data["closure_claimed"] is False, "candidate should not claim closure")
    require(data["next_required_artifact"] == NEXT_ARTIFACT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT_ARTIFACT, "certificate next mismatch")

    require(route_a["status"] == "ROUTE_A_UNPATCHED_SOURCE_LEMMA_STILL_OPEN_MEASURE_RETIRED", "Route A status mismatch")
    require(route_a["field_closure_count"] == 0, "Route A overclosed")
    require(route_a["open_field_count"] == 5, "Route A open count mismatch")
    require(route_a["support_count"] == 4, "Route A support count mismatch")
    require(route_a["unpatched_route_A_passes"] is False, "Route A should not pass")
    for key, value in route_a["strict_route_A_fields"].items():
        require(value is False, f"Route A field unexpectedly true: {key}")
    for key, value in route_a["retired_support"].items():
        require(value is True, f"Route A support unexpectedly false: {key}")

    require(route_b["status"] == "ROUTE_B_ONE_STRICT_FIELD_CLOSED_FOUR_OPEN", "Route B status mismatch")
    require(route_b["field_closure_count"] == 1, "Route B field count mismatch")
    require(route_b["open_field_count"] == 4, "Route B open count mismatch")
    require(route_b["route_B_passes"] is False, "Route B should not pass")
    require(route_b["strict_route_B_fields"]["selected_basis_feeds_all_72_row_functionals"] is True, "selected basis field not closed")
    for key in [
        "pre_residual_phase_shift_variation_operators",
        "independent_hessian_counterterm_source_rows",
        "sector_rows_assembled_from_source_rows",
        "no_residual_projector_replay_or_locked_target_as_source",
    ]:
        require(route_b["strict_route_B_fields"][key] is False, f"Route B field overclosed: {key}")
    require(len(route_b["evidence"]) >= 5, "Route B evidence count low")
    require(route_b["validator_result"]["returncode"] == 1, "Route B validator should still fail")
    require(route_b["validator_result"]["passes"] is False, "Route B validator pass mismatch")

    require(delta["net_progress"]["route_A_same_branch_precondition_improved"] is True, "Route A delta missing")
    require(delta["net_progress"]["route_B_selected_basis_field_closed"] is True, "Route B delta missing")
    require(delta["net_progress"]["route_B_evidence_count_precondition_met"] is True, "Route B evidence delta missing")
    require(delta["net_progress"]["strict_validator_still_fails"] is True, "validator delta should fail")

    label_map = {item["id"]: item for item in labels["remaining_labels"]}
    require(label_map["PSM-C1-01"]["status"] == "OPEN_UNPATCHED_ACTION_RESTRICTION_REQUIRED", "PSM-C1-01 label mismatch")
    require(label_map["PSM-C1-02"]["status"] == "OPEN_ROUTE_B_ONE_FIELD_CLOSED_FOUR_OPEN", "PSM-C1-02 label mismatch")
    require(label_map["PSM-C1-02"]["closed_field"] == "selected_basis_feeds_all_72_row_functionals", "closed field mismatch")
    require(label_map["PSM-C1-04"]["status"] == "OPEN_UNPATCHED_BSELECTED_REQUIRED", "PSM-C1-04 label mismatch")
    require(labels["closed_frozen_labels_preserved"] == ["DONE-PARITY-00", "DONE-SOURCE-00", "DONE-DYN-SUPPORT-00"], "frozen label mismatch")

    require(next_work["next_required_artifact"] == NEXT_ARTIFACT, "next work artifact mismatch")
    require(next_work["recommended_primary"]["label"] == "PSM-C1-02", "next primary label mismatch")
    require(next_work["recommended_primary"]["field"] == "pre_residual_phase_shift_variation_operators", "next primary field mismatch")
    require(next_work["parallel_sidecar"]["label"] == "PSM-C1-01", "sidecar label mismatch")
    require(len(next_work["work_items"]) == 3, "work item count mismatch")

    closure = data["closure_decision"]
    require(closure["SM_parity_reopened"] is False, "SM parity should stay frozen")
    require(closure["route_B_selected_basis_field_closed"] is True, "Route B closure missing")
    for key in [
        "unpatched_dynamic_C1_packet_closed",
        "route_A_unpatched_passes",
        "route_B_unpatched_passes",
        "true_SM_equivalence_closed",
        "no_knob_closed",
    ]:
        require(closure[key] is False, f"overclosed: {key}")

    require("0 of 5 strict unpatched physical fields" in note, "note Route A field count missing")
    require("selected_basis_feeds_all_72_row_functionals" in note, "note Route B closure missing")
    require("Conditional/local-principle evidence is recorded as support" in note, "note superset guardrail missing")
    require(NEXT_ARTIFACT in note, "note next artifact missing")

    for packet in [data, route_a, route_b, delta, labels, next_work, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
