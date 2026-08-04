"""Audit source-map selection theorem / honest Galerkin C1 value-run gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "selected_sourcemapselectiontheorem_or_honestgalerkinc1valuerun.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / "selected_sourcemapselectiontheorem_or_honestgalerkinc1valuerun"
SELECTION_TEST = PACKET_DIR / "source_map_selection_theorem_test.packet.json"
IF_SELECTED = PACKET_DIR / "if_selected_dynamic_packet_closure.packet.json"
GALERKIN_ROUTE = PACKET_DIR / "honest_galerkin_value_run_route.packet.json"
CERT = ROOT / "certificates" / "selected_sourcemapselectiontheorem_or_honestgalerkinc1valuerun_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_SourceMapSelectionTheorem_or_HonestGalerkinC1ValueRun_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_sourcemapselectiontheorem_or_honestgalerkinc1valuerun.py"

STATUS = "MTT_SELECTED_SOURCEMAPSELECTIONTHEOREM_OR_HONESTGALERKINC1VALUERUN_BUILT_SELECTION_TEST_OPEN"
NEXT = "MTT_Selected_DifferentiatedPhiFinC1ResidualProjectorAxiom_or_GalerkinC1Execution_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    selection = load(SELECTION_TEST)
    if_selected = load(IF_SELECTED)
    galerkin = load(GALERKIN_ROUTE)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")

    require(selection["status"] == "SELECTION_TEST_BUILT_DYNAMIC_APPLICATION_OPEN", "selection status mismatch")
    closed = selection["already_selected_or_closed"]
    for key in [
        "terminal_static_source_unconditional",
        "static_source_map_candidate_constructed",
        "weyl_polynomial_residuals_exact",
        "canonical_residual_projector_unique",
        "canonical_projector_replays_RZ_RX",
        "strict_72_real_target_attached",
    ]:
        require(closed[key] is True, f"closed support missing: {key}")
    attempt = selection["selection_attempt"]
    for key in [
        "phase_R_Z_selected_now",
        "shift_R_X_selected_now",
        "b_source_emitted_now",
        "physical_projector_application_promoted_now",
        "source_map_selected_now",
    ]:
        require(attempt[key] is False, f"selection overclaimed: {key}")
    require(len(selection["why_selection_is_not_yet_proved"]) == 4, "selection boundary list mismatch")

    require(if_selected["status"] == "IF_SELECTED_CLOSURE_EXACT_BUT_ANTECEDENT_OPEN", "if-selected status mismatch")
    current = if_selected["current_antecedent"]
    for key in ["phase_R_Z_selected", "shift_R_X_selected", "b_source_emitted", "A_selected_promotes", "b_selected_promotes", "deltaTheta_C1_promotes"]:
        require(current[key] is False, f"current antecedent overclaimed: {key}")
    would = if_selected["would_promote_if_antecedent_met"]
    require(would["A_selected_promotes"] is True, "if-selected A implication missing")
    require(would["b_selected_promotes"] is True, "if-selected b implication missing")
    require(would["deltaTheta_C1_promotes"] is True, "if-selected delta implication missing")
    require(would["SM_parity_dynamic_packet_would_close"] is True, "if-selected SM implication missing")
    replay = if_selected["if_selected_numeric_replay"]
    require(replay["rank"] == 2, "if-selected rank mismatch")
    require(replay["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "if-selected ATA mismatch")
    require(replay["A_transpose_b"] == [12.0, 12.0], "if-selected ATb mismatch")
    require(replay["deltaTheta_C1"] == [1.0, 1.0], "if-selected delta mismatch")
    require(if_selected["promoted_now"] is False, "if-selected overpromoted")

    require(galerkin["status"] == "HONEST_GALERKIN_VALUE_RUN_ROUTE_OPEN", "Galerkin route status mismatch")
    require(galerkin["strict_coordinate_target"]["total_real_coordinates"] == 72, "Galerkin target mismatch")
    require(galerkin["selected_source_verified"] is False, "Galerkin source oververified")
    require(galerkin["can_replace_source_map_now"] is False, "Galerkin overreplaces")
    require(galerkin["would_close_SM_parity_dynamic_packet_if_emitted"] is True, "Galerkin SM implication missing")
    require(galerkin["would_close_no_knob_flavor_constants_by_itself"] is False, "Galerkin no-knob overclaim")

    for key in [
        "source_map_selection_test_built",
        "closed_static_and_projector_support_separated_from_dynamic_application",
        "if_selected_dynamic_packet_closure_exact",
        "honest_Galerkin_value_run_route_restated",
        "observed_constants_excluded_as_selectors",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing: {key}")
    for key in [
        "selected_differentiated_PhiFinC1_applies_Q_residual",
        "selected_phase_R_Z_source",
        "selected_shift_R_X_source",
        "selected_Hessian_or_b_source_vector",
        "selected_A_selected",
        "selected_b_selected",
        "selected_deltaTheta_C1",
        "selected_sector_response_matrices",
        "honest_selected_Galerkin_C1_execution_values",
        "SM_parity_dynamic_packet_closure",
        "true_SM_equivalence_closure",
        "full_no_knob_flavor_closure",
    ]:
        require(data["what_remains_open"][key] is True, f"remaining gate missing: {key}")
    decision = data["promotion_decision"]
    for key in [
        "selection_theorem_proved_now",
        "source_map_selected_by_MTT_now",
        "A_selected_promoted",
        "b_selected_promoted",
        "deltaTheta_C1_promoted",
        "sector_response_matrices_promoted",
        "honest_Galerkin_C1_value_run_promoted",
        "SM_parity_dynamic_packet_closed",
        "true_SM_equivalence_closed",
        "no_knob_flavor_constants_closed",
    ]:
        require(decision[key] is False, f"promotion overclaimed: {key}")
    for key in [
        "observed_data_used",
        "target_fitting_used",
        "closure_claimed",
        "selection_theorem_claimed",
        "A_selected_claimed",
        "b_selected_claimed",
        "deltaTheta_C1_claimed",
        "honest_Galerkin_C1_claimed",
    ]:
        require(data[key] is False, f"guardrail overclaimed: {key}")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require("dynamic selection is still open" in note, "note missing selection boundary")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
