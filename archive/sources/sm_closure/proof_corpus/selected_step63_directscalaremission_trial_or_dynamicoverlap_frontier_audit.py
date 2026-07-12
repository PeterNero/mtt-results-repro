"""Audit Step63 direct scalar-emission trial / dynamic-overlap frontier."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step63_directscalaremission_trial_or_dynamicoverlap_frontier"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
TRIAL_PACKET = PACKET_DIR / "step63_direct_scalar_emission_trial.packet.json"
CUTSET = PACKET_DIR / "step63_dynamic_overlap_frontier.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step63_DirectScalarEmissionTrial_or_DynamicOverlapFrontier_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP63_DIRECT_SCALAR_EMISSION_TRIED_DYNAMIC_OVERLAP_FRONTIER_OPEN"
NEXT = "MTT_Selected_TypedBN_RetardedDerivative_or_PrimitiveResponse_ValueEmission_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)
    data = load(DATA)
    trial = load(TRIAL_PACKET)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem mismatch")

    for item in [data, trial, cutset, cert]:
        require(item.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(item.get("target_fitting_used") is False, "target fitting violation")

    closed = trial["closed_before_trial"]
    for key in [
        "Step62_Rtheta_functional_source_domain",
        "same_branch_readiness_8_of_9",
        "final_no_knob_kernel_typed",
        "transported_PhiFin_sector_payload_imported",
        "static_U10_Ubar5_1M_source_closed",
    ]:
        require(closed[key] is True, f"pre-trial close missing: {key}")

    result = trial["trial_result"]
    require(result["direct_emission_attempt_executed"] is True, "direct trial not executed")
    require(result["accepted_internal_scalar_row_count"] == 0, "scalar rows overaccepted")
    require(result["lambda_H_row_emitted"] is False, "lambda_H overemitted")
    require(result["fullS2_payload_ready"] is False, "fullS2 overready")
    require(result["universal_anchor_selected"] is False, "universal anchor overselected")

    post = trial["post_trial_imports"]
    for key in [
        "PhiFin_trace_imported",
        "validator_ready_sector_rho_s_imported",
        "static_matter_slot_readout_closed",
        "static_U10_Ubar5_1M_source_closed",
    ]:
        require(post[key] is True, f"post-trial import missing: {key}")

    for key, value in cutset["closed_or_reduced"].items():
        require(value is True, f"dynamic cutset reduction false: {key}")
    for item in [
        "typed dynamic B_N retarded derivative or alpha1 source-strength theorem",
        "selected End0-to-sector realization/functor values",
        "selected dynamic overlap/Hessian normalization and b_selected",
        "selected primitive/vertex/basis-transport response values",
    ]:
        require(item in cutset["remaining_minimal_objects"], f"remaining object missing: {item}")
    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    for key in [
        "dynamic_kernel_emitted",
        "selected_C1_primitive_emitted",
        "A_selected_claimed",
        "b_selected_claimed",
    ]:
        require(cutset[key] is False, f"cutset overclaimed: {key}")

    decision = data["closure_decision"]
    for key in [
        "direct_scalar_emission_trial_executed",
        "PhiFin_trace_and_static_matter_slot_blockers_retired",
        "dynamic_overlap_frontier_pinned",
    ]:
        require(decision[key] is True, f"decision close missing: {key}")
        require(cert[key] is True, f"certificate close missing: {key}")
    for key in [
        "lambda_H_row_emitted",
        "dynamic_kernel_emitted",
        "selected_C1_primitive_emitted",
        "A_selected_claimed",
        "b_selected_claimed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed: {key}")
        require(cert[key] is False, f"certificate overclosed: {key}")
    require(decision["accepted_internal_scalar_row_count"] == 0, "decision scalar rows overaccepted")
    require(cert["accepted_internal_scalar_row_count"] == 0, "certificate scalar rows overaccepted")

    for phrase in [
        "direct scalar emission tried          : true",
        "accepted internal scalar rows         : 0",
        "dynamic kernel emitted                : false",
        "selected C1 primitive emitted         : false",
        "A_selected claimed                    : false",
        "b_selected claimed                    : false",
        NEXT,
    ]:
        require(phrase in note, f"note missing: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
