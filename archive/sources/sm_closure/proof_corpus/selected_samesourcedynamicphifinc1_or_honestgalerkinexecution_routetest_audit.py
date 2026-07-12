"""Audit Route-A/Route-B test for PSM-C1-01 post-SM-parity work."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_samesourcedynamicphifinc1_or_honestgalerkinexecution_routetest"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ROUTE_A = PACKET_DIR / "route_a_psm_c1_01_source_rule_test.packet.json"
ROUTE_B = PACKET_DIR / "route_b_honest_galerkin_readiness_sidecar.packet.json"
LABEL_STATUS = PACKET_DIR / "label_status_after_route_test.packet.json"
NEXT = PACKET_DIR / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_SameSourceDynamicPhiFinC1_or_HonestGalerkinExecution_RouteTest_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_SAMESOURCEDYNAMICPHIFINC1_OR_HONESTGALERKINEXECUTION_ROUTETEST_BUILT_PSM_C1_01_OPEN"
NEXT_ARTIFACT = "MTT_Selected_PSM_C1_01_SourceRuleEmission_or_PSM_C1_04_bSelectedSidecar_v1"


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
    label_status = load(LABEL_STATUS)
    next_work = load(NEXT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem mismatch")
    require(data["closure_claimed"] is False, "candidate should not close")
    require(data["next_required_artifact"] == NEXT_ARTIFACT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT_ARTIFACT, "cert next mismatch")

    require(route_a["active_label"] == "PSM-C1-01", "route A active label mismatch")
    require(route_a["active_route"] == "ROUTE-A", "route A mismatch")
    for key, value in route_a["support_passed"].items():
        require(value is True, f"route A support false: {key}")
    for key, value in route_a["missing_for_closure"].items():
        require(value is True, f"route A missing flag false: {key}")
    result = route_a["current_result"]
    require(result["PSM-C1-01_closed"] is False, "PSM-C1-01 overclosed")
    require(result["source_rule_contract_exists"] is True, "source rule contract missing")
    require(result["physical_differentiated_application_promoted"] is False, "physical application overpromoted")
    require(result["phase_R_Z_selected_now"] is False, "phase overselected")
    require(result["shift_R_X_selected_now"] is False, "shift overselected")
    require(result["b_source_emitted_now"] is False, "b source overemitted")
    require(result["conditional_values_if_rule_proved"]["deltaTheta_C1"] == [1.0, 1.0], "conditional delta mismatch")
    require(len(route_a["next_needed_emissions"]) == 5, "next emissions count mismatch")

    for key, value in route_b["support_passed"].items():
        require(value is True, f"route B support false: {key}")
    require(route_b["readiness_decision"]["ready_to_execute_selected_value_run_now"] is False, "route B overready")
    require(route_b["readiness_decision"]["can_replace_route_A_now"] is False, "route B overreplacement")
    require(route_b["required_outputs"] == [
        "zero_mode_bases",
        "primitive_three_by_three_contraction_terms",
        "linear_response_matrices",
        "C33/nonzero-family-rank tests",
    ], "route B required outputs mismatch")
    for key, missing in route_b["missing_selected_inputs"].items():
        require(missing is True, f"route B missing input not marked: {key}")

    labels = {item["id"]: item for item in label_status["label_status_after_route_test"]}
    require(labels["PSM-C1-01"]["status_after"] == "OPEN_PRIMARY_REDUCED_TO_SOURCE_RULE_EMISSION", "PSM-C1-01 status mismatch")
    require(labels["PSM-C1-04"]["status_after"] == "OPEN_PRIMARY_SIDECAR_REQUIRED", "PSM-C1-04 status mismatch")
    require(labels["PSM-C1-05"]["status_after"] == "OPEN_CONDITIONAL_VALUE_1_1_NOT_SELECTED", "PSM-C1-05 status mismatch")
    require("PSM-NK-01" in label_status["still_open_labels"], "no-knob label missing")

    require(next_work["primary_label"] == "PSM-C1-01", "next primary label mismatch")
    require(next_work["sidecar_label"] == "PSM-C1-04", "next sidecar mismatch")
    require(next_work["primary_route"] == "ROUTE-A", "next primary route mismatch")
    require(next_work["parallel_route"] == "ROUTE-B", "next parallel route mismatch")
    require(len(next_work["work_items"]) == 3, "work item count mismatch")
    require(next_work["work_items"][0]["id"] == "A1a", "first work item mismatch")

    closure = data["closure_decision"]
    for key in [
        "PSM-C1-01_closed",
        "PSM-C1-04_closed",
        "ROUTE_A_closes_now",
        "ROUTE_B_ready_now",
        "selected_C1_response_closed",
        "actual_dynamic_QaSU3_operator_packet_closed",
        "true_SM_equivalence_closed",
        "no_knob_closed",
    ]:
        require(closure[key] is False, f"overclosed: {key}")

    require("Active label: `PSM-C1-01`" in note, "note active label missing")
    require("Sidecar label: `PSM-C1-04`" in note, "note sidecar missing")
    require("It does not." in note, "note no-close missing")
    require(NEXT_ARTIFACT in note, "note next artifact missing")

    for packet in [data, route_a, route_b, label_status, next_work, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
