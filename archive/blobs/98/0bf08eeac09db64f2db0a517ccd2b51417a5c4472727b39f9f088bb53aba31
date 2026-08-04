"""Audit H radial source value or direct N_H execution packet."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_hradialsourcevalue_or_directnhexecution"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
STRICT_PACKET = PACKET_DIR / "strict_radial_NH_source_execution.packet.json"
CONTROLLED_PACKET = PACKET_DIR / "controlled_one_parameter_radial_NH_closure.packet.json"
CUTSET_PACKET = PACKET_DIR / "next_strict_source_or_crossuse_cutset.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HRadialSourceValue_or_DirectNHExecution_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_HRADIALSOURCEVALUE_OR_DIRECTNH_STRICT_OPEN_CONTROLLED_ONE_PARAMETER_CLOSED"
NEXT = "MTT_Selected_StrictFiniteHActionSource_or_UPRetOverlapHRGCrossUse_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("closure_claimed") is True, f"{label} closure flag")
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    strict = load(STRICT_PACKET)
    controlled = load(CONTROLLED_PACKET)
    cutset = load(CUTSET_PACKET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("strict", strict),
        ("controlled", controlled),
        ("cutset", cutset),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "certificate status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(cert["next_required_artifact"] == NEXT, "certificate next")
    require(data["theorem"]["proved"] is True, "candidate theorem")
    require(cert["theorem_proved"] is True, "certificate theorem")
    require(data["full_no_knob_closure_claimed"] is False, "candidate no-knob")
    require(data["true_SM_equivalence_claimed"] is False, "candidate true SM")

    current = strict["current_emission"]
    for key in [
        "finite_H_action_selected",
        "M_source_values_selected",
        "primitive_H_response_kernel_values_selected",
        "direct_N_H_value_emitted",
    ]:
        require(current[key] is False, f"strict overemitted {key}")
    require(current["accepted_direct_radial_hessian_value_rows"] == 0, "strict rows")
    require(strict["strict_R_H_RG_source_constructed"] is False, "strict R_H")
    require(strict["all_strict_R_H_RG_gates_satisfied"] is False, "strict gates")
    require(strict["strict_selected_K_rows"] == {"accepted": 9, "required": 10}, "K count")

    values = controlled["derived_controlled_values"]
    r_h = values["r_H"]
    n_h = values["N_H_equals_r_H_squared"]
    require(r_h > 0, "r_H positive")
    require(math.isclose(n_h, r_h * r_h, rel_tol=0.0, abs_tol=1e-9), "N_H square")
    require(values["conditional_K_row_count"] == 10, "conditional K count")
    boundary = controlled["claim_boundary"]
    require(boundary["minimal_parameter_H_layer_closed"] is True, "minimal layer")
    require(boundary["lambda_H_calibrated"] is True, "lambda calibrated")
    require(boundary["lambda_H_predicted"] is False, "lambda predicted")
    require(boundary["strict_no_knob_closure_claimed"] is False, "controlled no-knob")
    require(boundary["full_SM_closure_claimed"] is False, "controlled full SM")
    primitive = controlled["primitive"]
    require(primitive["id"] == "UP-RET-OVERLAP.HRG", "primitive id")
    require(primitive["new_universal_parameter_count_in_this_layer"] == 1, "parameter count")
    require(primitive["selected_as_strict_source_parameter"] is False, "strict parameter")

    require(cutset["status"] == "STRICT_SOURCE_OR_CROSSUSE_REQUIRED", "cutset status")
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    for phrase in [
        "derive selected finite H-sector action F_H and compute N_H",
        "derive selected same-source Hermitian M_source restricted to B_Huv",
        "derive selected primitive H-response kernel K_H with row-level exactness/error bound",
        "derive strict R_H^RG source operator without calibration",
    ]:
        require(phrase in cutset["strict_no_knob_exits"], f"strict exit {phrase}")
    for phrase in [
        "declare UP-RET-OVERLAP.HRG once",
        "keep lambda_H as calibration, not prediction",
        "use r_H=391.39140285811936 and N_H=r_H^2 as controlled values",
        "audit at least one non-Higgs cross-use prediction without retuning",
    ]:
        require(phrase in cutset["minimal_parameter_exit"], f"minimal exit {phrase}")

    decision = data["closure_decision"]
    for key in [
        "strict_radial_source_execution_attempted",
        "controlled_one_parameter_radial_layer_closed",
        "lambda_H_calibrated",
        "crossuse_prediction_required_for_credibility_upgrade",
    ]:
        require(decision[key] is True, f"decision missing {key}")
    for key in [
        "strict_N_H_value_emitted",
        "strict_r_H_source_emitted",
        "strict_R_H_RG_source_constructed",
        "selected_L_rowlocal_Omega_H_lambda_emitted",
        "selected_T_scheme_Omega_H_lambda_emitted",
        "direct_K_threshold_Omega_H_lambda_emitted",
        "strict_H_K_threshold_row_emitted",
        "lambda_H_predicted",
        "full_no_knob_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"decision overclosed {key}")
    require(decision["minimal_parameter_count_added_if_adopted"] == 1, "decision parameter count")
    require(decision["accepted_selected_K_source_row_count"] == 9, "decision K")
    require(decision["selected_K_threshold_row_count_required"] == 10, "decision K required")
    require(math.isclose(decision["controlled_N_H"], decision["controlled_r_H"] ** 2, abs_tol=1e-9), "decision N_H")

    for phrase in [
        "HRadialSourceValueOrDirectNHExecutionTheorem",
        "Strict `N_H=Hess(F_H)[U_H,U_H]` emitted: `false`",
        "controlled `N_H=r_H^2`",
        "This closes a controlled/minimal H layer only",
        "does not predict `lambda_H`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print("AUDIT_PASS: strict radial source remains open; controlled one-parameter N_H layer closed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
