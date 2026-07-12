"""Audit Phi_fin transported sector payload integration into scalar-row gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_phifinminimizertracesectorpayload_or_internalscalarrows"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PAYLOAD_UPDATE = PACKET_DIR / "transported_phifin_sector_payload_update.packet.json"
SCALAR_GATE = PACKET_DIR / "internal_scalar_row_gate_after_transport_payload.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_phifin_sector_payload_update.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PhiFinMinimizerTraceSectorPayload_or_InternalScalarRows_v1.md"

STATUS = (
    "MTT_SELECTED_PHIFINMINIMIZERTRACESECTORPAYLOAD_OR_INTERNALSCALARROWS_"
    "BUILT_TRANSPORT_REPLAY_IMPORTED_SECTOR_SOURCE_PAYLOAD_OPEN"
)
NEXT = "MTT_Selected_U10Ubar5_1M_SourcePromotion_SameBranch_Emission_v1"


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
    payload = load(PAYLOAD_UPDATE)
    scalar = load(SCALAR_GATE)
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
    guard(payload, errors, "payload update", closure=False)
    guard(scalar, errors, "scalar gate", closure=False)
    guard(cutset, errors, "cutset", closure=False)

    for key in [
        "functional_PhiFin_trace_closed",
        "symbolic_transport_finite_morphism_valid",
        "transport_closed_validator_replay_closed",
        "validator_ready_sector_rho_s_packet",
        "same_branch_alpha1_derivative_closed",
    ]:
        expect(payload.get(key) is True, f"payload import missing: {key}", errors)
    remaining = payload.get("remaining_sector_source_payload", {})
    for key in [
        "selected_U10_clock_source",
        "selected_Ubar5_shift_source",
        "selected_1M_Dirac_neutrino_shift_source",
        "selected_ordered_matter_slot_packet",
        "actual_QaSU3_operator_packet",
        "selected_dynamic_PhiFin_C1_payload",
    ]:
        expect(remaining.get(key) is True, f"remaining sector payload missing: {key}", errors)

    expect(scalar.get("codomain_scalar_row_count") == 10, "scalar codomain count mismatch", errors)
    expect(scalar.get("accepted_internal_scalar_row_count") == 0, "scalar rows overaccepted", errors)
    expect(scalar.get("lambda_H_row_emitted") is False, "lambda_H overemitted", errors)
    readiness = scalar.get("updated_readiness", {})
    expect(readiness.get("stationary_projector_riesz_green_rhos_layer") is True, "stationary layer not imported", errors)
    expect(readiness.get("transport_closed_validator_layer") is True, "transport layer not imported", errors)
    expect(readiness.get("same_branch_matter_slot_source_layer") is False, "matter-slot layer overclosed", errors)
    expect(readiness.get("dynamic_PhiFin_C1_payload_layer") is False, "dynamic payload overclosed", errors)
    expect(readiness.get("internal_Rtheta_scalar_rows") is False, "internal scalar rows overclosed", errors)

    closed = cutset.get("closed_now", {})
    for key in [
        "functional_PhiFin_trace_imported",
        "symbolic_transport_validator_imported",
        "validator_ready_sector_rho_s_imported",
        "alpha1_not_reopened_as_scalar_knob",
    ]:
        expect(closed.get(key) is True, f"cutset close missing: {key}", errors)
    remains = cutset.get("still_open", {})
    for key in [
        "selected_U10_clock_source",
        "selected_Ubar5_shift_source",
        "selected_1M_Dirac_neutrino_shift_source",
        "selected_ordered_matter_slot_packet",
        "selected_dynamic_PhiFin_C1_payload",
        "actual_QaSU3_operator_packet",
        "internal_Rtheta_scalar_rows",
        "true_SM_equivalence",
        "full_no_knob_closure",
    ]:
        expect(remains.get(key) is True, f"cutset blocker missing: {key}", errors)
    expect(cutset.get("recommended_next", {}).get("artifact") == NEXT, "cutset next mismatch", errors)

    decision = data.get("closure_decision", {})
    expect(decision.get("transported_sector_payload_imported") is True, "decision import missing", errors)
    expect(decision.get("accepted_internal_scalar_row_count") == 0, "decision scalar rows overaccepted", errors)
    expect(decision.get("lambda_H_row_emitted") is False, "decision lambda_H overemitted", errors)
    expect(decision.get("same_branch_matter_slot_source_closed") is False, "decision matter source overclosed", errors)
    expect(decision.get("dynamic_PhiFin_C1_payload_closed") is False, "decision dynamic payload overclosed", errors)
    expect(decision.get("true_SM_equivalence_closed") is False, "decision true SM overclosed", errors)
    expect(decision.get("full_no_knob_closed") is False, "decision no-knob overclosed", errors)

    expect("transport validator replay imported     : true" in note, "note missing transport import", errors)
    expect("same-branch matter-slot source closed   : false" in note, "note missing matter-source guard", errors)
    expect("accepted internal scalar rows           : 0" in note, "note missing scalar zero", errors)

    if errors:
        print("Phi_fin sector payload integration audit FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Phi_fin sector payload integration audit passed")
    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
