"""Audit CONST-HIGGS-01 H7B1 D-term projection invariant functor."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_higgs_01_h7b1_dterm_projection_invariant_functor"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
PROJECTOR_FUNCTOR = BASE / "uv_two_higgs_projector_to_sbeta_functor.packet.json"
SOURCE_SEARCH = BASE / "selected_projector_source_search.packet.json"
ACCEPTANCE = BASE / "selected_projector_acceptance_contract.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_HIGGS_01_H7B1_DTermProjectionInvariantFunctor_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7B1_DTERM_PROJECTOR_FUNCTOR_BUILT_VALUES_OPEN"


def load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def clean(packet: dict[str, object], name: str) -> None:
    require(packet["observed_data_used_as_selector"] is False, f"{name} observed selector")
    require(packet["target_fitting_used"] is False, f"{name} target fitting")
    require(packet["closure_claimed"] is False, f"{name} closure overclaim")


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    computed = json.loads(proc.stdout)
    require(computed["status"] == STATUS, "builder status mismatch")

    candidate = load(DATA)
    functor = load(PROJECTOR_FUNCTOR)
    source = load(SOURCE_SEARCH)
    acceptance = load(ACCEPTANCE)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, item in [
        ("candidate", candidate),
        ("functor", functor),
        ("source", source),
        ("acceptance", acceptance),
    ]:
        clean(item, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["projector_to_sbeta_functor_built"] is True, "functor built")
    require(candidate["basis_free_s_beta_formula_built"] is True, "basis formula")
    require(candidate["full_beta_angle_required"] is False, "beta required")
    require(candidate["selected_metric_on_two_Higgs_plane_found"] is False, "metric overfound")
    require(candidate["selected_rank_one_light_projector_P_L_found"] is False, "P_L overfound")
    require(candidate["selected_s_beta_value_found"] is False, "s_beta overfound")
    require(candidate["selected_EW_boundary_RG_packet_closed"] is False, "EW overclosed")
    require(candidate["new_Higgs_specific_parameters"] == 0, "new params")
    require(candidate["numeric_lambda_H_derived"] is False, "lambda")
    require(candidate["strict_no_knob_Higgs_closure"] is False, "no-knob")

    plane = functor["two_higgs_plane"]
    require(plane["basis"] == ["H_u", "H_d^dagger"], "basis")
    require(plane["basis_labels_closed"] is True, "basis closed")
    require(plane["selected_metric_on_plane_filled"] is False, "metric filled")
    jd = functor["Dterm_charge_involution"]
    require(jd["matrix_in_ordered_basis"] == [[1, 0], [0, -1]], "JD")
    require(jd["filled_as_formal_operator"] is True, "JD formal")
    pl = functor["light_line_projector"]
    require(pl["symbol"] == "P_L", "P_L symbol")
    require(pl["selected_projector_values_filled"] is False, "P_L values")
    invariant = functor["projection_invariant"]
    require(invariant["cos2beta_without_beta"] == "Tr(J_D P_L)", "cos2")
    require(invariant["s_beta"] == "(Tr(J_D P_L))^2", "s_beta")
    require(invariant["coordinate_form_if_metric_is_orthonormal"] == "s_beta=(|c_u|^2-|c_d|^2)^2", "coordinate")
    require("Tr(J_D P_L)" in invariant["boundary_rewrite"], "boundary rewrite")
    checks = functor["formal_checks"]
    require(checks["does_not_require_full_beta_angle"] is True, "no beta")
    require(checks["phase_invariant_under_cu_cd_rephasing"] is True, "phase")
    require(checks["only_uses_rank_one_light_line"] is True, "rank one")
    require(checks["emits_exact_s_beta_if_selected_P_L_is_emitted"] is True, "conditional exact")
    require(checks["emits_numeric_s_beta_now"] is False, "numeric s")

    support = source["closed_support"]
    require(support["H7B_minimal_object_is_s_beta"] is True, "H7B minimal")
    require(support["H7B_route_B_underdetermined"] is True, "H7B under")
    require(support["low_energy_Hu_Hd_projection_closed"] is True, "low energy")
    require(support["Hu_maps_to_H"] is True, "Hu")
    require(support["Hd_maps_to_Hdagger"] is True, "Hd")
    open_fields = source["open_source_fields_from_q79_certificate"]
    require(open_fields["channel_weights"] is True, "channel weights open")
    require(open_fields["family_kinetic_metrics"] is True, "kinetic metrics open")
    require(open_fields["rg_threshold_matching"] is True, "rg open")
    neg = source["negative_result"]
    for key in [
        "selected_metric_on_two_Higgs_plane_found",
        "selected_rank_one_light_projector_P_L_found",
        "selected_coefficients_cu_cd_found",
        "selected_s_beta_value_found",
        "numeric_lambda_H_derived",
    ]:
        require(neg[key] is False, f"negative {key}")
    why = source["why_this_is_not_the_old_beta_knob"]
    require(why["target_object"] == "basis-free projector invariant s_beta=(Tr(J_D P_L))^2", "target object")
    require(why["not_a_measured_Higgs_backsolve"] is True, "not backsolve")
    require(why["not_representative_tan_beta_10"] is True, "not tan10")
    require(why["not_full_angle_parameterization"] is True, "not full angle")
    require(why["requires_same_branch_selected_projector_source"] is True, "same branch")
    superset = source["superset_strategy"]
    require(superset["combined_paths_with_locked_target"] is True, "locked")
    require(superset["combined_as_numeric_knobs"] is False, "knobs")

    required = acceptance["required_before_s_beta_emission"]
    require(required["UV_two_Higgs_plane_basis_labels"]["filled"] is True, "req basis")
    require(required["Hermitian_metric_on_EH_UV"]["filled"] is False, "req metric")
    require(required["rank_one_light_line_projector_P_L"]["filled"] is False, "req P_L")
    require(required["basis_invariance_certificate"]["filled"] is False, "req basis cert")
    require(required["Dterm_charge_involution_J_D"]["filled"] is True, "req JD")
    require(required["EW_boundary_RG_transport"]["filled"] is False, "req EW")
    eval_ = acceptance["current_packet_evaluation"]
    require(eval_["formal_projector_to_sbeta_functor_valid"] is True, "eval functor")
    require(eval_["selected_projector_values_filled"] is False, "eval values")
    require(eval_["selected_s_beta_emitted"] is False, "eval s")
    require(eval_["selected_EW_boundary_RG_packet_closed"] is False, "eval EW")
    require(eval_["numeric_lambda_H_derived"] is False, "eval lambda")
    require(eval_["strict_no_knob_Higgs_closure"] is False, "eval no-knob")
    witness = acceptance["conditional_witness"]
    require("compute s_beta=(Tr(J_D P_L))^2" in witness["if_selected_projector_P_L_emitted_then"], "witness s")
    require("choose P_L from measured Higgs mass" in witness["still_forbidden"], "forbid measured")

    require("H7B1A-SELECTED-TWO-HIGGS-METRIC-OR-LIGHT-PROJECTOR-SOURCE" in next_work["primary_next"]["label"], "next primary")
    require("H7B2-SELECTED-EW-BOUNDARY-RG-PACKET" in next_work["parallel_next"]["label"], "next parallel")
    require(cert["status"] == STATUS, "cert status")
    require(cert["projector_to_sbeta_functor_built"] is True, "cert functor")
    require(cert["selected_rank_one_light_projector_P_L_found"] is False, "cert P_L")
    require(cert["numeric_lambda_H_derived"] is False, "cert lambda")
    require(cert["strict_no_knob_Higgs_closure"] is False, "cert no-knob")
    require("H7B1-DTERM-PROJECTION" in note and "s_beta = (Tr(J_D P_L))^2" in note, "note")

    print("CONST-HIGGS-01 H7B1 D-term projection invariant functor audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
