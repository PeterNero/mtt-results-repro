"""Audit PSM-C1-01 source-rule emission test with PSM-C1-04 sidecar."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_psm_c1_01_sourceruleemission_or_psm_c1_04_bselectedsidecar"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
UNPATCHED = PACKET_DIR / "route_a_unpatched_source_rule_validator.packet.json"
PATCHED_PAYLOAD = PACKET_DIR / "route_a_patched_axiom_validator_payload.packet.json"
PATCHED_RESULT = PACKET_DIR / "route_a_patched_axiom_validator_result.packet.json"
B_SIDECAR = PACKET_DIR / "psm_c1_04_bselected_sidecar.packet.json"
LABEL_STATUS = PACKET_DIR / "label_status_after_source_rule_sidecar.packet.json"
NEXT = PACKET_DIR / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PSM_C1_01_SourceRuleEmission_or_PSM_C1_04_bSelectedSidecar_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_PSM_C1_01_SOURCERULEEMISSION_OR_PSM_C1_04_BSELECTEDSIDECAR_BUILT_PATCHED_PASS_UNPATCHED_OPEN"
NEXT_ARTIFACT = "MTT_Selected_PSM_C1_01_UnpatchedSourceLemma_or_ROUTE_B_RowKernelExecution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    unpatched = load(UNPATCHED)
    patched_payload = load(PATCHED_PAYLOAD)
    patched_result = load(PATCHED_RESULT)
    b_sidecar = load(B_SIDECAR)
    label_status = load(LABEL_STATUS)
    next_work = load(NEXT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem mismatch")
    require(data["closure_claimed"] is False, "candidate should not claim unpatched closure")
    require(data["next_required_artifact"] == NEXT_ARTIFACT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT_ARTIFACT, "cert next mismatch")

    require(unpatched["status"] == "UNPATCHED_ROUTE_A_STRICT_VALIDATOR_STILL_FAILS", "unpatched status mismatch")
    require(unpatched["unpatched_PSM_C1_01_closed"] is False, "unpatched PSM-C1-01 overclosed")
    require(unpatched["unpatched_PSM_C1_04_closed"] is False, "unpatched PSM-C1-04 overclosed")
    for key, missing in unpatched["strict_missing_route_A"].items():
        require(missing is True, f"Route A missing flag false: {key}")
    require(unpatched["validator_result"]["returncode"] == 1, "unpatched validator should fail")

    require(patched_payload["scientific_status"] == "axiom-conditional validator pass, not unpatched derivation", "patched status mismatch")
    route_a = patched_payload["route_A_physical_action_restriction"]
    for key in [
        "same_branch",
        "physical_action_restricts_to_finite_weyl_quotient",
        "zero_extra_boundary_or_source_term",
        "phase_R_Z_source_selection",
        "shift_R_X_source_selection",
        "same_source_b_selected_emission",
    ]:
        require(route_a[key] is True, f"patched Route A field false: {key}")
    require(len(route_a["attached_source_evidence"]) >= 5, "patched Route A evidence count low")
    require(patched_result["passes"] is True and patched_result["returncode"] == 0, "patched validator should pass")

    require(b_sidecar["patched_status"]["patched_b_selected_emitted"] is True, "patched b not emitted")
    require(b_sidecar["patched_status"]["patched_A_transpose_b"] == [12.0, 12.0], "patched A^T b mismatch")
    require(b_sidecar["patched_status"]["patched_deltaTheta_C1"] == [1.0, 1.0], "patched delta mismatch")
    require(b_sidecar["unpatched_status"]["source_rule_derived_unpatched"] is False, "unpatched source overderived")
    require(b_sidecar["unpatched_status"]["same_source_b_selected_emission"] is False, "unpatched b overemitted")
    require(b_sidecar["unpatched_status"]["route_B_can_replace_now"] is False, "Route B overready")

    labels = {item["id"]: item for item in label_status["labels"]}
    require(labels["PSM-C1-01"]["patched_status"] == "PATCHED_CLOSED_BY_EXPLICIT_LOCAL_AXIOM", "PSM-C1-01 patched mismatch")
    require(labels["PSM-C1-01"]["unpatched_status"] == "OPEN_NEEDS_SELECTED_PHYSICAL_ACTION_RESTRICTION", "PSM-C1-01 unpatched mismatch")
    require(labels["PSM-C1-04"]["unpatched_status"] == "OPEN_NEEDS_SAME_SOURCE_B_SELECTED_EMISSION", "PSM-C1-04 unpatched mismatch")
    require(labels["PSM-C1-05"]["patched_status"] == "PATCHED_DELTA_THETA_1_1_AVAILABLE", "PSM-C1-05 patched mismatch")

    require(next_work["next_required_artifact"] == NEXT_ARTIFACT, "next work artifact mismatch")
    require(next_work["primary_unpatched_label"] == "PSM-C1-01", "primary unpatched label mismatch")
    require(next_work["sidecar_unpatched_label"] == "PSM-C1-04", "sidecar unpatched label mismatch")
    require(len(next_work["route_A_minimal_lemma"]["required_fields"]) == 5, "Route A field count mismatch")
    require(len(next_work["work_items"]) == 2, "next work item count mismatch")

    closure = data["closure_decision"]
    require(closure["patched_dynamic_C1_packet_closed"] is True, "patched closure missing")
    for key in [
        "unpatched_dynamic_C1_packet_closed",
        "PSM-C1-01_closed_unpatched",
        "PSM-C1-04_closed_unpatched",
        "ROUTE_B_ready_now",
        "true_SM_equivalence_closed",
        "no_knob_closed",
    ]:
        require(closure[key] is False, f"overclosed: {key}")

    require("Patched lane:" in note and "Unpatched lane:" in note, "note lane split missing")
    require("not an unpatched true-equivalence closure" in note, "note guardrail missing")
    require(NEXT_ARTIFACT in note, "note next missing")

    for packet in [data, unpatched, patched_payload, patched_result, b_sidecar, label_status, next_work, cert]:
        require(packet.get("observed_data_used_as_selector") is False or packet.get("observed_data_used") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
