"""Audit CONST-HIGGS-01 H6E UV beta source no-go and primitive policy."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_higgs_01_h6e_uv_two_higgs_projection_angle_or_primitive_beta_policy"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
UV_SOURCE_AUDIT = BASE / "uv_two_higgs_projection_angle_source_audit.packet.json"
PRIMITIVE_POLICY = BASE / "primitive_beta_policy.packet.json"
SYMBOLIC_BOUNDARY = BASE / "symbolic_dterm_boundary_packet.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_HIGGS_01_H6E_UVTwoHiggsProjectionAngleOrPrimitiveBetaPolicy_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H6E_UV_BETA_SOURCE_NOGO_PRIMITIVE_POLICY_BUILT"


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
    uv_audit = load(UV_SOURCE_AUDIT)
    primitive = load(PRIMITIVE_POLICY)
    symbolic = load(SYMBOLIC_BOUNDARY)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, item in [
        ("candidate", candidate),
        ("uv_audit", uv_audit),
        ("primitive", primitive),
        ("symbolic", symbolic),
    ]:
        clean(item, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["low_energy_single_Higgs_projection_closed"] is True, "single Higgs")
    require(candidate["symbolic_Dterm_boundary_ready"] is True, "symbolic ready")
    require(candidate["selected_UV_beta_source_found"] is False, "UV beta overfound")
    require(candidate["beta_primitive_policy_built"] is True, "primitive policy")
    require(candidate["beta_primitive_declared_now"] is False, "primitive declared")
    require(candidate["new_Higgs_specific_parameters"] == 0, "params now")
    require(candidate["new_Higgs_specific_parameters_if_beta_declared"] == 1, "params if beta")
    require(candidate["DTerm_boundary_numeric_value_derived"] is False, "D-term numeric")
    require(candidate["Higgs_quartic_numeric_value_derived"] is False, "lambda numeric")
    require(candidate["strict_no_knob_Higgs_closure"] is False, "no-knob")

    support = uv_audit["current_closed_support"]
    require(support["low_energy_single_Higgs_projection"] is True, "support single Higgs")
    require(support["H_u_to_H"] is True, "support Hu")
    require(support["H_d_to_Hdagger"] is True, "support Hd")
    require(support["two_independent_low_energy_Higgs_alignment_references"] is False, "support two Higgs")
    require(support["Dterm_formula_ready"] is True, "support D-term")
    absences = uv_audit["strict_source_absences"]
    for key in [
        "selected_UV_two_Higgs_VEV_ratio",
        "selected_beta_or_tan_beta",
        "selected_two_Higgs_projection_angle",
        "selected_heavy_Higgs_decoupling_angle",
        "selected_color_triplet_decoupling",
        "selected_Higgs_VEV_or_mass_prediction",
    ]:
        require(absences[key] is True, f"strict absence {key}")
    obstruction = uv_audit["proof_obstruction"]
    require(obstruction["single_Higgs_projection_is_low_energy_not_UV_angle"] is True, "single-Higgs obstruction")
    require(obstruction["Theta_tan_beta_10_is_representative_not_selected"] is True, "tan beta obstruction")
    verdict = uv_audit["strict_no_knob_verdict"]
    require(verdict["selected_beta_source_closed"] is False, "verdict beta")
    require(verdict["Dterm_boundary_numeric_value_derived"] is False, "verdict numeric")
    require(verdict["strict_no_knob_Higgs_closure"] is False, "verdict no-knob")

    policy = primitive["policy"]
    require(policy["allowed_tier"] == "EXPLICIT_PRIMITIVE_NON_NO_KNOB", "allowed tier")
    require(policy["strict_no_knob_tier"] is False, "policy no-knob")
    require(policy["new_Higgs_specific_parameters_if_declared"] == 1, "policy params if declared")
    require(policy["new_parameters_declared_now"] == 0, "policy params now")
    require("declared once before any Higgs-mass/lambda comparison" in policy["may_be_used_only_if"], "declare once")
    require("renamed no-knob closure" in policy["forbidden_if"], "forbid no-knob rename")
    decision = primitive["current_decision"]
    require(decision["declare_beta_primitive_now"] is False, "declare beta now")
    require(decision["recommended_use_now"] == "symbolic conditional replay only", "recommended use")
    require(primitive["superset_strategy"]["paths_combined_as_free_parameters"] is False, "superset params")

    boundary = symbolic["symbolic_boundary"]
    require(boundary["formula"] == "lambda = (g^2 + g'^2) * cos^2(2 beta) / 8", "symbolic formula")
    require(boundary["equivalent_cos2beta_from_tanbeta"] == "cos(2 beta)^2 = ((tan_beta^2 - 1)/(tan_beta^2 + 1))^2", "tan formula")
    require("beta_H" in boundary["inputs_required"], "beta input")
    diagnostic = symbolic["diagnostic_example_retained_only_for_replay"]
    require(diagnostic["tan_beta"] == 10, "diagnostic tan")
    require(diagnostic["counts_as_source"] is False, "diagnostic source")
    numeric = symbolic["numeric_status"]
    for key in [
        "selected_gauge_boundary_values_filled",
        "selected_beta_filled",
        "matching_scale_policy_filled",
        "threshold_RG_transport_filled",
        "numeric_lambda_H_derived",
    ]:
        require(numeric[key] is False, f"numeric {key}")

    require("H7-INTRINSIC-H-SECTOR-K4-ROW-OR-UV-BETA-THEOREM" in next_work["primary_strict"]["label"], "next strict")
    require("H6F-SYMBOLIC-DTERM-BOUNDARY-REPLAY" in next_work["conditional_replay"]["label"], "next conditional")
    require(cert["status"] == STATUS, "cert status")
    require(cert["selected_UV_beta_source_found"] is False, "cert UV beta")
    require(cert["beta_primitive_policy_built"] is True, "cert primitive")
    require(cert["beta_primitive_declared_now"] is False, "cert declared")
    require(cert["new_Higgs_specific_parameters"] == 0, "cert params now")
    require(cert["new_Higgs_specific_parameters_if_beta_declared"] == 1, "cert params if beta")
    require(cert["Higgs_quartic_numeric_value_derived"] is False, "cert lambda")
    require(cert["strict_no_knob_Higgs_closure"] is False, "cert no-knob")
    require("H6E-UV-TWO-HIGGS" in note and "H6F-SYMBOLIC-DTERM" in note, "note")

    print("CONST-HIGGS-01 H6E UV beta source / primitive policy audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
