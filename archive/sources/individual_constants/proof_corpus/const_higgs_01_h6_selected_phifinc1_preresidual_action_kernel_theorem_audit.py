"""Audit CONST-HIGGS-01 H6 selected Phi_fin^C1 pre-residual action-kernel gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_higgs_01_h6_selected_phifinc1_preresidual_action_kernel_theorem"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
LOCAL_KERNEL = BASE / "local_principle_kernel_import.packet.json"
UNPATCHED_STATUS = BASE / "unpatched_kernel_theorem_status.packet.json"
HIGGS_IMPLICATION = BASE / "higgs_quartic_local_implication.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_HIGGS_01_H6_SelectedPhiFinC1PreResidualActionKernelTheorem_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H6_LOCAL_PRERESIDUAL_KERNEL_CLOSED_UNPATCHED_OPEN"


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
    local_kernel = load(LOCAL_KERNEL)
    unpatched_status = load(UNPATCHED_STATUS)
    higgs_implication = load(HIGGS_IMPLICATION)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, item in [
        ("candidate", candidate),
        ("local_kernel", local_kernel),
        ("unpatched_status", unpatched_status),
        ("higgs_implication", higgs_implication),
    ]:
        clean(item, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["local_premise_pre_residual_action_kernel_closed"] is True, "local kernel")
    require(candidate["local_strict_kernel_validator_ok"] is True, "validator")
    require(candidate["PhysicalActionOwnsFiniteTraceKernel_local_tier_closed"] is True, "local action")
    require(candidate["PhysicalActionOwnsFiniteTraceKernel_strict_unpatched_closed"] is False, "strict action overclosed")
    require(candidate["SelectedPhiFinC1PreResidualActionKernelTheorem_unpatched_closed"] is False, "unpatched theorem overclosed")
    require(candidate["independent_kernel_execution_closed"] is False, "independent overclosed")
    require(candidate["selected_Higgs_projection_functional_template_closed"] is True, "projection template")
    require(candidate["actual_nonlinear_Higgs_source_rows_emitted"] is False, "source rows overemitted")
    require(candidate["projection_on_actual_source_kernel_closed"] is False, "projection overclosed")
    require(candidate["selected_Higgs_quartic_threshold_kernel_emitted"] is False, "quartic overemitted")
    require(candidate["Higgs_quartic_numeric_value_derived"] is False, "lambda overderived")
    require(candidate["strict_no_knob_Higgs_closure"] is False, "strict no-knob")
    require(candidate["new_Higgs_specific_parameters"] == 0, "Higgs params")
    require(candidate["superset_strategy"]["paths_used_as_free_parameters"] is False, "superset free parameter")
    require(candidate["superset_strategy"]["locked_target_used_only_as_postcheck"] is True, "locked target postcheck")

    closure = local_kernel["local_kernel_closure"]
    require(closure["local_principle_accepted"] is True, "local principle")
    require(closure["accepted_as"] == "explicit local premise, not unpatched theorem", "accepted as")
    require(closure["strict_kernel_closed_under_local_principle"] is True, "strict kernel local")
    require(closure["strict_kernel_validator_ok"] is True, "kernel validator")
    require(closure["audit_ok"] is True, "audit ok")
    promoted = closure["promoted_inside_local_spine"]
    require(promoted["pre_residual_phase_shift_operator_source"] is True, "phase/shift")
    require(promoted["same_source_hessian_b_selected_rows"] is True, "hessian b")
    require(promoted["sector_rows_physical_source_promotion"] is True, "sector source")
    require(promoted["independence_from_residual_projector_replay"] is True, "independence")
    decision = local_kernel["si1c_decision"]
    require(decision["local_pre_residual_action_kernel_closed"] is True, "decision local")
    require(decision["unpatched_theorem_derived_now"] is False, "decision unpatched")
    require(decision["unpatched_source_identity_lemma_status"] == "OPEN", "unpatched status")
    require(decision["superset_strategy"]["paths_used_as_free_parameters"] is False, "decision superset")

    attempt = unpatched_status["unpatched_attempt"]
    require(attempt["theorem_name"] == "SelectedPhiFinC1PreResidualActionKernelTheorem", "attempt theorem")
    require(attempt["unpatched_theorem_derived_now"] is False, "attempt unpatched")
    require(attempt["derivation_attempt_status"] == "UNPATCHED_DERIVATION_SUPPORT_CLOSED_PHYSICAL_SELECTION_OPEN", "attempt status")
    require("reuse exact R_Z/R_X decomposition as source selection" in attempt["forbidden_shortcuts"], "RZ shortcut")
    tier = unpatched_status["tier_decision"]
    require(tier["local_premise_tier_closed"] is True, "tier local")
    require(tier["strict_no_knob_tier_closed"] is False, "tier no-knob")
    require(tier["unpatched_theorem_closed"] is False, "tier unpatched")
    require(tier["independent_kernel_execution_closed"] is False, "tier independent")
    require(tier["true_SM_equivalence_without_local_principle_closed"] is False, "tier true eq")

    update = higgs_implication["H4_H5_cutset_update"]
    require(update["object_1_PhysicalActionOwnsFiniteTraceKernel_local_tier"] is True, "object1 local")
    require(update["object_1_PhysicalActionOwnsFiniteTraceKernel_strict_unpatched"] is False, "object1 strict")
    require(update["object_2_SelectedHiggsNonlinearAmplitudeProjection_template"] is True, "object2 template")
    require(update["selected_Higgs_amplitude_coordinate"] == 12, "coordinate")
    require(update["future_quartic_row_address"] == [12, 12, 12, 12], "row address")
    why = higgs_implication["why_Higgs_quartic_still_not_closed"]
    require(why["local_SI1c_kernel_emits_C1_source-identity rows, not an actual H-sector fourth-variation row"] is True, "row distinction")
    require(why["actual_nonlinear_Higgs_source_rows_emitted"] is False, "Higgs rows")
    require(why["projection_on_actual_source_kernel_closed"] is False, "actual projection")
    require(why["lambda_H_coefficient_convention_closed"] is False, "lambda convention")
    require(why["strict_no_knob_Higgs_closure"] is False, "Higgs closure")

    require(next_work["primary_local_tier"]["label"] == "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6B-LOCAL-SOURCE-IDENTITY-TO-HIGGS-ROW-EXPORT", "primary local")
    require(next_work["strict_upgrade"]["label"] == "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7-UNPATCHED-PHIFINC1-PRERESIDUAL-ACTION-KERNEL", "strict upgrade")

    require(cert["status"] == STATUS, "cert status")
    require(cert["local_premise_pre_residual_action_kernel_closed"] is True, "cert local")
    require(cert["PhysicalActionOwnsFiniteTraceKernel_local_tier_closed"] is True, "cert action local")
    require(cert["PhysicalActionOwnsFiniteTraceKernel_strict_unpatched_closed"] is False, "cert action strict")
    require(cert["SelectedPhiFinC1PreResidualActionKernelTheorem_unpatched_closed"] is False, "cert unpatched")
    require(cert["actual_nonlinear_Higgs_source_rows_emitted"] is False, "cert rows")
    require(cert["Higgs_quartic_numeric_value_derived"] is False, "cert numeric")
    require("H6-SELECTED-PHIFINC1" in note and "H7-UNPATCHED" in note, "note")

    print("CONST-HIGGS-01 H6 selected Phi_fin^C1 pre-residual action-kernel audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
