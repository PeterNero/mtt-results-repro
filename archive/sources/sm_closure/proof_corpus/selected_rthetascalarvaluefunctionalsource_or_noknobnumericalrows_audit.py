"""Audit Rtheta scalar value functional source/domain or no-knob numerical rows gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_rthetascalarvaluefunctionalsource_or_noknobnumericalrows"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SOURCE_PACKET = PACKET_DIR / "rtheta_scalar_value_functional_source_packet.packet.json"
CODOMAIN_MAP = PACKET_DIR / "ten_scalar_rows_to_threshold_contract_map.packet.json"
EXECUTION_GATE = PACKET_DIR / "no_knob_numerical_rows_execution_gate.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_rtheta_scalar_value_functional_source.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_RThetaScalarValueFunctionalSource_or_NoKnobNumericalRows_v1.md"

STATUS = (
    "MTT_SELECTED_RTHETASCALARVALUEFUNCTIONALSOURCE_OR_NOKNOBNUMERICALROWS_"
    "BUILT_FUNCTIONAL_SOURCE_DOMAIN_CLOSED_NUMERICAL_ROWS_OPEN"
)
NEXT = "MTT_Selected_ThresholdMagnitudeRows_or_MinimalUniversalParameterDecision_v1"


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
    source = load(SOURCE_PACKET)
    codomain = load(CODOMAIN_MAP)
    execution = load(EXECUTION_GATE)
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
    guard(source, errors, "source packet", closure=True)
    guard(codomain, errors, "codomain map", closure=True)
    guard(execution, errors, "execution gate", closure=False)
    guard(cutset, errors, "cutset", closure=False)

    components = source.get("closed_source_domain_components", {})
    for key in [
        "qualitative_SM_orbit_layer",
        "Pi_Rtheta",
        "coefficient_functional_skeleton",
        "selected_dynamic_operator_source_owner",
        "source_normalized_projection_weights",
        "threshold_response_contract",
        "higher_response_scalar_codomain_contract",
    ]:
        expect(components.get(key) is True, f"source component not closed: {key}", errors)
    expect(source.get("source_domain_closed") is True, "source domain not closed", errors)

    expect(len(codomain.get("ten_scalar_rows", [])) == 10, "ten scalar row count mismatch", errors)
    expect(len(codomain.get("charged_yukawa_rows", [])) == 9, "charged row count mismatch", errors)
    expect(codomain.get("higgs_quartic_row") == "lambda_H", "lambda_H row mismatch", errors)
    alignment = codomain.get("alignment", {})
    for key in [
        "charged_rows_match_contract",
        "lambda_H_row_required",
        "threshold_matching_rows_required",
        "mass_scheme_conversion_rows_required",
        "profile_response_or_diagonal_limitation_required",
    ]:
        expect(alignment.get(key) is True, f"codomain alignment missing: {key}", errors)

    expect(execution.get("source_domain_closed") is True, "execution gate lost source domain", errors)
    expect(execution.get("selected_threshold_response_functional_instantiated") is False, "threshold response overinstantiated", errors)
    expect(execution.get("magnitude_bearing_projection_weights_closed") is False, "magnitude weights overclosed", errors)
    expect(execution.get("accepted_coefficient_value_count") == 0, "coefficient rows overaccepted", errors)
    expect(execution.get("accepted_Yukawa_magnitudes_as_no_knob_predictions") is False, "Yukawa values overaccepted", errors)
    expect(execution.get("lambda_H_value_selected") is False, "lambda_H overselected", errors)
    expect(execution.get("numerical_rows_closed") is False, "numerical rows overclosed", errors)

    closed = cutset.get("closed_now", {})
    for key in [
        "selected_Rtheta_scalar_value_functional_source_domain",
        "ten_scalar_row_codomain_aligned",
        "Pi_Rtheta_imported_into_qualitative_orbit_frontier",
        "coefficient_functional_skeleton_imported",
        "empirical_selector_forbidden_boundary_preserved",
    ]:
        expect(closed.get(key) is True, f"cutset close missing: {key}", errors)
    remains = cutset.get("still_open", {})
    for key in [
        "same_branch_scale_scheme_loop_convention",
        "threshold_matching_source_rows",
        "mass_scheme_conversion_source_rows",
        "magnitude_bearing_projection_weights",
        "selected_threshold_response_functional_instantiation",
        "accepted_numerical_Yukawa_rows",
        "lambda_H_value",
        "true_SM_equivalence",
        "full_no_knob_closure",
    ]:
        expect(remains.get(key) is True, f"remaining blocker missing: {key}", errors)
    expect(cutset.get("recommended_next", {}).get("artifact") == NEXT, "cutset next mismatch", errors)

    decision = data.get("closure_decision", {})
    expect(decision.get("selected_Rtheta_scalar_value_functional_source_domain_closed") is True, "decision source domain missing", errors)
    expect(decision.get("ten_scalar_row_codomain_aligned") is True, "decision codomain missing", errors)
    expect(decision.get("no_knob_numerical_rows_emitted") is False, "decision numerical rows overemitted", errors)
    for key in [
        "accepted_value_layer_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        expect(decision.get(key) is False, f"decision overclosed: {key}", errors)
        expect(cert.get(key) is False, f"certificate overclosed: {key}", errors)

    expect("Pi_Rtheta closed                 : true" in note, "note missing Pi_Rtheta close", errors)
    expect("accepted numerical scalar rows   : 0" in note, "note missing numerical-open guard", errors)
    expect("does not emit no-knob numerical" in note, "note missing no-knob guard", errors)

    if errors:
        print("Rtheta scalar value functional source audit FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Rtheta scalar value functional source audit passed")
    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
