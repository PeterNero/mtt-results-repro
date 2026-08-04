"""Audit direct internal Rtheta scalar-row emission attempt or universal-anchor selection."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_internalrthetascalarrowemission_or_universalanchorselection"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
DIRECT_ATTEMPT = PACKET_DIR / "direct_internal_rtheta_scalar_row_emission_attempt.packet.json"
STRUCTURAL_ROWS = PACKET_DIR / "structural_orbit_scalar_row_candidates_not_accepted.packet.json"
FULLS2_BLOCKER = PACKET_DIR / "full_s2_operator_payload_blocker_for_direct_emission.packet.json"
ANCHOR_SELECTION = PACKET_DIR / "universal_anchor_selection_recheck_for_direct_emission.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_direct_scalar_row_emission_attempt.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_InternalRThetaScalarRowEmission_or_UniversalAnchorSelection_v1.md"

STATUS = (
    "MTT_SELECTED_INTERNALRTHETASCALARROWEMISSION_OR_UNIVERSALANCHORSELECTION_"
    "BUILT_DIRECT_EMISSION_ATTEMPT_BLOCKED_BY_FULLS2_PAYLOAD"
)
NEXT = "MTT_Selected_PhiFinMinimizerTraceSectorPayload_or_InternalScalarRows_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def expect(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def guard(packet: dict[str, Any], errors: list[str], label: str, *, closure: bool = False) -> None:
    expect(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector violation", errors)
    expect(packet.get("target_fitting_used") is False, f"{label} target fitting violation", errors)
    expect(packet.get("closure_claimed") is closure, f"{label} closure flag mismatch", errors)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    direct = load(DIRECT_ATTEMPT)
    structural = load(STRUCTURAL_ROWS)
    blocker = load(FULLS2_BLOCKER)
    anchor = load(ANCHOR_SELECTION)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")
    errors: list[str] = []

    expect(data.get("status") == STATUS, "candidate status mismatch", errors)
    expect(cert.get("status") == STATUS, "certificate status mismatch", errors)
    expect(data.get("next_required_artifact") == NEXT, "candidate next mismatch", errors)
    expect(cert.get("next_required_artifact") == NEXT, "certificate next mismatch", errors)
    expect(data.get("theorem", {}).get("proved") is True, "theorem should be proved", errors)
    expect(cert.get("theorem_proved") is True, "certificate theorem should be proved", errors)

    guard(data, errors, "candidate", closure=False)
    guard(cert, errors, "certificate", closure=False)
    guard(direct, errors, "direct attempt", closure=False)
    guard(structural, errors, "structural rows", closure=False)
    guard(blocker, errors, "fullS2 blocker", closure=False)
    guard(anchor, errors, "anchor selection", closure=False)
    guard(cutset, errors, "cutset", closure=False)

    expect(direct.get("source_domain_closed") is True, "source domain should be closed", errors)
    expect(direct.get("basis_map_closed") is True, "basis map should be closed", errors)
    expect(direct.get("orbit_matrix_packet_closed") is True, "orbit matrix should be closed", errors)
    expect(direct.get("full_S2_scalar_execution_ready") is False, "fullS2 overready", errors)
    expect(direct.get("selected_universal_parameter_count") == 0, "universal parameter overselected", errors)
    expect(direct.get("codomain_scalar_row_count") == 10, "codomain scalar row count mismatch", errors)
    expect(direct.get("accepted_internal_scalar_row_count") == 0, "internal scalar rows overaccepted", errors)
    expect(direct.get("accepted_internal_scalar_rows") == [], "accepted scalar list should be empty", errors)
    expect(direct.get("lambda_H_row_emitted") is False, "lambda_H overemitted", errors)
    expect(len(direct.get("blocked_scalar_rows", [])) == 10, "blocked row count mismatch", errors)
    expect(direct.get("direct_rows_allowed") is False, "direct rows should not be allowed", errors)

    expect(structural.get("candidate_row_count") == 9, "structural candidate count mismatch", errors)
    expect(structural.get("diagnostic_profile_coefficients_still_rejected") is True, "diagnostic rejection missing", errors)
    for row in structural.get("candidate_rows", []):
        expect(row.get("accepted_as_internal_selected_scalar_row") is False, f"structural row overaccepted: {row.get('coefficient_slot')}", errors)
        expect("full-S2 rhoE/D_E/operator payload gate is not ready" in row.get("why_not_accepted", []), f"structural blocker missing: {row.get('coefficient_slot')}", errors)

    ready = blocker.get("ready", {})
    expect(ready.get("full_S2_scalar_execution_ready") is False, "fullS2 blocker overready", errors)
    for key in [
        "PhiFin_selected_minimizer_trace_ready",
        "selected_projector_promotion_ready",
        "End0_to_sector_routing_ready",
        "validator_ready_sector_rhoE_DE_Riesz_Green_dotD_C1",
    ]:
        expect(ready.get(key) is False, f"fullS2 ready flag overclosed: {key}", errors)
    for row in [
        "Phi_fin_selected_minimizer_trace",
        "selected_P_s_K_s_projector_promotion",
        "selected_rho_s_matrix_values",
        "selected_End0_to_sector_routing_values",
        "physical_dotD_alpha1_same_branch_driver",
        "validator_ready_sector_rhoE_DE_Riesz_Green_dotD_C1",
    ]:
        expect(row in blocker.get("next_required_for_direct_emission", []), f"missing direct-emission prerequisite: {row}", errors)

    expect(anchor.get("selected_universal_parameter_count") == 0, "anchor parameter overselected", errors)
    expect(anchor.get("selected_candidates_now") == [], "anchor candidates should be empty", errors)
    expect(anchor.get("can_substitute_for_fullS2_payload") is False, "anchor should not substitute", errors)

    closed = cutset.get("closed_now", {})
    for key in [
        "direct_emission_attempt_executed",
        "structural_orbit_rows_tested_and_rejected_as_values",
        "fullS2_blocker_identified",
        "universal_anchor_rechecked_not_selected",
    ]:
        expect(closed.get(key) is True, f"cutset closed missing: {key}", errors)
    remains = cutset.get("still_open", {})
    for key in [
        "internal_Rtheta_scalar_row_emission",
        "lambda_H_row_emission",
        "Phi_fin_selected_minimizer_trace",
        "selected_sector_projector_promotion",
        "selected_rho_s_End0_sector_routing_values",
        "candidate_specific_universal_source_anchor",
        "true_SM_equivalence",
        "full_no_knob_closure",
    ]:
        expect(remains.get(key) is True, f"cutset blocker missing: {key}", errors)
    expect(cutset.get("recommended_next", {}).get("artifact") == NEXT, "cutset next mismatch", errors)

    decision = data.get("closure_decision", {})
    expect(decision.get("direct_emission_attempt_executed") is True, "decision attempt missing", errors)
    expect(decision.get("accepted_internal_scalar_row_count") == 0, "decision scalar rows overaccepted", errors)
    expect(decision.get("lambda_H_row_emitted") is False, "decision lambda_H overemitted", errors)
    expect(decision.get("fullS2_payload_ready") is False, "decision fullS2 overready", errors)
    expect(decision.get("universal_anchor_selected") is False, "decision universal anchor overselected", errors)
    expect(decision.get("true_SM_equivalence_closed") is False, "decision true SM overclosed", errors)
    expect(decision.get("full_no_knob_closed") is False, "decision no-knob overclosed", errors)

    expect("full-S2 scalar execution ready    : false" in note, "note missing fullS2 guard", errors)
    expect("accepted internal scalar rows     : 0" in note, "note missing scalar zero", errors)
    expect("lambda_H row emitted              : false" in note, "note missing lambda_H guard", errors)

    if errors:
        print("Internal Rtheta scalar row emission audit FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Internal Rtheta scalar row emission audit passed")
    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
