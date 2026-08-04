"""Audit PSM-C1-02 SI-1u honest Galerkin export attempt."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_psm_c1_02_unpatchedkernelexecutionplan_or_honestgalerkinexport"
BASE = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
INPUT_IMPORT = BASE / "route_b_existing_input_import_status.packet.json"
HONEST_ATTEMPT = BASE / "route_b_honest_galerkin_export_attempt.packet.json"
UNPATCHED_GUARD = BASE / "unpatched_source_promotion_guardrail.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PSM_C1_02_UnpatchedKernelExecutionPlan_or_HonestGalerkinExport_v1.md"

STATUS = "MTT_SELECTED_PSM_C1_02_SI1U_HONEST_GALERKIN_EXPORT_ATTEMPTED_REPLAY_HARNESS_ONLY"
NEXT = "MTT_Selected_PSM_C1_02_HonestGalerkinZeroModeBasisSource_or_PrimitiveQuadratureExport_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict) -> None:
    require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
    require(packet.get("target_fitting_used") is False, "target fitting violation")
    require(packet.get("closure_claimed") is False, "global closure overclaim")


def main() -> int:
    candidate = load(CANDIDATE)
    input_import = load(INPUT_IMPORT)
    honest = load(HONEST_ATTEMPT)
    guardrail = load(UNPATCHED_GUARD)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["active_label"] == "PSM-C1-02", "active label mismatch")
    require(candidate["active_routes"] == ["SOURCE-IDENTITY/SI-1u-B", "SOURCE-IDENTITY/SI-1u-A"], "routes mismatch")
    require(candidate["closed_boundary"] == "DONE-PARITY-00", "closed boundary mismatch")
    require(candidate["next_required_artifact"] == NEXT, "next artifact mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem missing")

    closure = candidate["closure_decision"]
    require(closure["strict_replay_harness_passes"] is True, "strict replay should pass")
    require(closure["honest_independent_galerkin_export_closed"] is False, "honest export overclosed")
    require(closure["unpatched_source_promotion_packet_passes"] is False, "unpatched packet overaccepted")
    require(closure["conditional_unpatched_packet_passes_if_theorem_supplied"] is True, "conditional target missing")
    require(closure["true_SM_equivalence_closed"] is False, "true equivalence overclosed")
    require(closure["no_knob_closed"] is False, "no-knob overclosed")

    require(input_import["status"] == "EXISTING_GALERKIN_INPUT_PACKETS_IMPORTED_AS_REPLAY_HARNESS_NOT_HONEST_EXPORT", "input import status mismatch")
    require(input_import["new_input_fill_audit"]["returncode"] == 0, "input fill audit failed")
    require(input_import["all_input_packets_exist"] is True, "input packets should exist")
    require(input_import["all_input_packets_honest_independent"] is False, "input packets overclaimed honest")
    require(input_import["input_packets"]["zero_mode_basis"]["selected_source_verified"] is False, "zero basis oververified")
    require(input_import["input_packets"]["primitive_contraction_terms"]["computed_from_independent_galerkin_quadrature"] is False, "primitive overindependent")
    require(input_import["input_packets"]["hessian_source_vector"]["b_selected_emitted_by_independent_hessian"] is False, "hessian overindependent")
    require(input_import["input_packets"]["sector_response_matrices"]["independent_sector_matrices_emitted"] is False, "sector overindependent")

    require(honest["status"] == "STRICT_REPLAY_PASSES_BUT_HONEST_GALERKIN_EXPORT_NOT_CLOSED", "honest attempt status mismatch")
    require(honest["strict_replay_passes"] is True, "strict replay did not pass")
    require(honest["honest_independent_galerkin_execution_passes"] is False, "honest execution overclosed")
    require(honest["route_B_result_from_input_fill"]["input_packets_filled"] is True, "input fill missing")
    require(honest["route_B_result_from_input_fill"]["strict_replay_passes"] is True, "route B strict replay missing")
    require(honest["route_B_result_from_input_fill"]["honest_independent_galerkin_execution_passes"] is False, "route B honest overclosed")
    require(len(honest["required_honest_exports"]) == 5, "required export count mismatch")
    require(honest["free_axiom_patch_used"] is False, "free patch flag should be false for this attempt")

    require(guardrail["status"] == "UNPATCHED_SOURCE_PROMOTION_STILL_OPEN_CONDITIONAL_TARGET_PRESERVED", "guardrail status mismatch")
    require(guardrail["current_unpatched_packet_passes"] is False, "current packet overaccepted")
    require(guardrail["patched_local_axiom_packet_passes_unpatched_validator"] is False, "patched packet overaccepted")
    require(guardrail["conditional_unpatched_packet_passes"] is True, "conditional packet missing")

    require(next_work["primary"]["label"] == "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-B1", "next primary mismatch")
    require(next_work["secondary"]["label"] == "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-B2", "next secondary mismatch")
    require(next_work["parallel"]["label"] == "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-A", "parallel route mismatch")
    require(next_work["next_required_artifact"] == NEXT, "next work artifact mismatch")

    require(cert["status"] == STATUS, "cert status mismatch")
    require(cert["strict_replay_harness_passes"] is True, "cert replay missing")
    require(cert["honest_independent_galerkin_export_closed"] is False, "cert honest overclosed")
    require(cert["unpatched_source_promotion_packet_passes"] is False, "cert unpatched overaccepted")

    require("Status label: `PSM-C1-02 / SOURCE-IDENTITY / SI-1u-B`" in note, "note label missing")
    require("strict replay harness, but not an honest independent Galerkin export" in note, "note guard missing")
    require("They are not knobs" in note, "note superset guard missing")

    for packet in [candidate, input_import, honest, guardrail, cert]:
        guard(packet)

    print(f"PASS {CANDIDATE.name}: {candidate['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
