"""Audit static U10/Ubar5/1M matter-slot source promotion integration."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_u10ubar5_1m_sourcepromotion_samebranch_emission"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
STATIC_PROMOTION = PACKET_DIR / "static_matter_slot_source_promotion_update.packet.json"
SCALAR_GATE = PACKET_DIR / "internal_scalar_row_gate_after_static_matter_slot_readout.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_static_matter_slot_source_promotion.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_U10Ubar5_1M_SourcePromotion_SameBranch_Emission_v1.md"

STATUS = (
    "MTT_SELECTED_U10UBAR5_1M_SOURCEPROMOTION_SAMEBRANCH_EMISSION_"
    "BUILT_STATIC_MATTERSLOT_READOUT_CLOSED_DYNAMIC_PAYLOAD_OPEN"
)
NEXT = "MTT_Selected_DynamicOverlapKernel_or_C1Primitive_SourceEmission_v1"


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
    static = load(STATIC_PROMOTION)
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
    guard(static, errors, "static promotion", closure=False)
    guard(scalar, errors, "scalar gate", closure=False)
    guard(cutset, errors, "cutset", closure=False)

    outputs = static.get("selected_static_tier_outputs", {})
    for key in [
        "selected_matter_slot_transversality_readout",
        "selected_U10_clock_source",
        "selected_Ubar5_shift_source",
        "selected_1M_Dirac_neutrino_shift_source",
        "selected_ordered_matter_slot_packet",
        "selected_overlap_transfer_normalization_static_tier",
    ]:
        expect(outputs.get(key) is True, f"static output missing: {key}", errors)
    expect(static.get("static_phase_shift_partition") == {"phase": ["u", "e"], "shift": ["d", "nuD"]}, "phase/shift partition mismatch", errors)

    expect(scalar.get("codomain_scalar_row_count") == 10, "scalar codomain count mismatch", errors)
    expect(scalar.get("accepted_internal_scalar_row_count") == 0, "scalar rows overaccepted", errors)
    expect(scalar.get("lambda_H_row_emitted") is False, "lambda_H overemitted", errors)
    readiness = scalar.get("updated_readiness", {})
    expect(readiness.get("transported_projector_riesz_green_rhos_layer") is True, "transport layer missing", errors)
    expect(readiness.get("static_matter_slot_readout_layer") is True, "static readout missing", errors)
    expect(readiness.get("static_U10_Ubar5_1M_layer") is True, "static U10/Ubar5/1M missing", errors)
    expect(readiness.get("dynamic_overlap_kernel_layer") is False, "dynamic overlap overclosed", errors)
    expect(readiness.get("dynamic_PhiFin_C1_payload_layer") is False, "dynamic payload overclosed", errors)
    expect(readiness.get("internal_Rtheta_scalar_rows") is False, "scalar rows overclosed", errors)

    closed = cutset.get("closed_now", {})
    for key in [
        "selected_matter_slot_transversality_readout_static_tier",
        "selected_U10_clock_source_static_tier",
        "selected_Ubar5_shift_source_static_tier",
        "selected_1M_Dirac_shift_source_static_tier",
        "selected_overlap_transfer_normalization_static_tier",
        "locked_C1_target_not_used_as_selector",
    ]:
        expect(closed.get(key) is True, f"cutset close missing: {key}", errors)
    remains = cutset.get("still_open", {})
    for key in [
        "dynamic_visible_routec_operator_source_identity",
        "selected_D_E_Riesz_Green_dotD_dynamic_payload",
        "selected_dynamic_overlap_tensor_or_transfer_functor",
        "selected_primitive_C1_contractions",
        "A_selected",
        "b_selected",
        "internal_Rtheta_scalar_rows",
        "true_SM_equivalence",
        "full_no_knob_closure",
    ]:
        expect(remains.get(key) is True, f"cutset blocker missing: {key}", errors)
    expect(cutset.get("recommended_next", {}).get("artifact") == NEXT, "cutset next mismatch", errors)

    decision = data.get("closure_decision", {})
    expect(decision.get("static_matter_slot_readout_closed") is True, "decision static readout missing", errors)
    expect(decision.get("static_U10_Ubar5_1M_source_closed") is True, "decision static source missing", errors)
    expect(decision.get("dynamic_overlap_kernel_closed") is False, "decision dynamic overlap overclosed", errors)
    expect(decision.get("accepted_internal_scalar_row_count") == 0, "decision scalar rows overaccepted", errors)
    expect(decision.get("lambda_H_row_emitted") is False, "decision lambda_H overemitted", errors)
    expect(decision.get("true_SM_equivalence_closed") is False, "decision true SM overclosed", errors)
    expect(decision.get("full_no_knob_closed") is False, "decision no-knob overclosed", errors)

    expect("matter-slot readout static tier   : true" in note, "note missing static readout", errors)
    expect("dynamic overlap/C1 payload closed : false" in note, "note missing dynamic guard", errors)
    expect("accepted internal scalar rows     : 0" in note, "note missing scalar zero", errors)

    if errors:
        print("U10/Ubar5/1M source promotion audit FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("U10/Ubar5/1M source promotion audit passed")
    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
