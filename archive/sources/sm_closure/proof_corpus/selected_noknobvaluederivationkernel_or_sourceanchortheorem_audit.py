"""Audit final no-knob value derivation kernel or source-anchor theorem frontier."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_noknobvaluederivationkernel_or_sourceanchortheorem"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
UPDATED_KERNEL = PACKET_DIR / "updated_no_knob_value_derivation_kernel.packet.json"
OBLIGATION_STATUS = PACKET_DIR / "internal_value_obligation_status_after_readiness_8of9.packet.json"
SOURCE_ANCHOR_TARGET = PACKET_DIR / "candidate_specific_source_anchor_target.packet.json"
FINAL_DECISION = PACKET_DIR / "final_closure_decision_after_kernel_update.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_NoKnobValueDerivationKernel_or_SourceAnchorTheorem_v1.md"

STATUS = (
    "MTT_SELECTED_NOKNOBVALUEDERIVATIONKERNEL_OR_SOURCEANCHORTHEOREM_"
    "BUILT_FINAL_KERNEL_NO_INTERNAL_VALUES_SELECTED"
)
NEXT = "MTT_Selected_InternalRThetaScalarRowEmission_or_UniversalAnchorSelection_v1"


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
    kernel = load(UPDATED_KERNEL)
    obligations = load(OBLIGATION_STATUS)
    anchor = load(SOURCE_ANCHOR_TARGET)
    final = load(FINAL_DECISION)
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
    guard(kernel, errors, "kernel", closure=False)
    guard(obligations, errors, "obligations", closure=False)
    guard(anchor, errors, "anchor target", closure=False)
    guard(final, errors, "final decision", closure=False)

    expect(kernel.get("readiness_fraction") == "8/9", "readiness fraction mismatch", errors)
    expect(kernel.get("only_remaining_readiness_blocker") == "no_knob_value_derivation", "blocker mismatch", errors)
    expect(kernel.get("codomain_scalar_row_count") == 10, "scalar row count mismatch", errors)
    expect(kernel.get("value_source_required_row_count") == 5, "value-source row count mismatch", errors)
    expect(kernel.get("value_source_closed_row_count") == 0, "value-source rows overclosed", errors)
    expect(kernel.get("accepted_coefficient_row_count") == 0, "coefficients overaccepted", errors)
    expect(kernel.get("selected_internal_value_emission_count") == 0, "internal emissions overaccepted", errors)
    expect(kernel.get("selected_universal_parameter_count") == 0, "universal parameter overselected", errors)

    expect(obligations.get("required_row_count") == 5, "obligation count mismatch", errors)
    expect(obligations.get("closed_row_count") == 0, "obligation rows overclosed", errors)
    expect(obligations.get("scalar_value_rows_emitted") == 0, "scalar rows overemitted", errors)
    expect(obligations.get("lambda_H_row_emitted") is False, "lambda_H overemitted", errors)
    expect(obligations.get("diagnostic_coefficients_available_but_rejected") == 9, "diagnostic rejection count mismatch", errors)
    expect(obligations.get("accepted_coefficient_rows") == [], "accepted coefficient list should be empty", errors)

    expect(anchor.get("selected_universal_parameter_count") == 0, "anchor universal overselected", errors)
    expect(anchor.get("selected_candidates_now") == [], "anchor selected candidates should be empty", errors)
    theorem_required = anchor.get("theorem_required", {})
    for key in [
        "must_select_anchor_before_empirical_replay",
        "must_be_universal_across_all_scalar_rows",
        "must_have_typed_Rtheta_gate_role",
        "must_not_be_inferred_from_residuals",
        "must_execute_the_same_ten_row_codomain",
    ]:
        expect(theorem_required.get(key) is True, f"anchor theorem requirement missing: {key}", errors)

    proved = final.get("what_is_proved_now", {})
    for key in [
        "qualitative_SM_orbit_closure",
        "Rtheta_readiness_8_of_9",
        "admitted_external_replay_boundary",
        "external_import_lane_closed_at_admitted_replay_tier",
        "final_no_knob_kernel_typed",
        "diagnostic_value_rows_rejected_as_selectors",
    ]:
        expect(proved.get(key) is True, f"proved-now item missing: {key}", errors)
    not_proved = final.get("what_is_not_proved", {})
    for key in [
        "internal_no_knob_scalar_value_emission",
        "selected_universal_source_anchor",
        "Yukawa_CKM_PMNS_lambdaH_numerical_closure",
        "true_SM_equivalence",
        "full_no_knob_closure",
    ]:
        expect(not_proved.get(key) is True, f"not-proved guard missing: {key}", errors)
    expect(final.get("final_missing_object") == NEXT, "final missing object mismatch", errors)

    decision = data.get("closure_decision", {})
    expect(decision.get("final_no_knob_kernel_typed") is True, "decision final kernel missing", errors)
    expect(decision.get("selected_internal_value_emission_count") == 0, "decision internal emissions overclosed", errors)
    expect(decision.get("accepted_coefficient_row_count") == 0, "decision coefficients overclosed", errors)
    expect(decision.get("selected_universal_parameter_count") == 0, "decision universal overselected", errors)
    expect(decision.get("true_SM_equivalence_closed") is False, "decision true SM overclosed", errors)
    expect(decision.get("full_no_knob_closed") is False, "decision no-knob overclosed", errors)

    expect("Rtheta readiness                 : 8/9" in note, "note missing readiness", errors)
    expect("accepted coefficient rows        : 0" in note, "note missing coefficient zero", errors)
    expect("full SM numerical closure        : false" in note, "note missing closure guard", errors)

    if errors:
        print("No-knob value derivation kernel audit FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("No-knob value derivation kernel audit passed")
    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
