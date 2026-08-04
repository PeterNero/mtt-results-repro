"""Build CONST-HIGGS-01 H6 selected Phi_fin^C1 pre-residual action-kernel gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
SM_PARITY_REPO = TEXPAPERS / "mtt-sm-parity-closure"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_higgs_01_h6_selected_phifinc1_preresidual_action_kernel_theorem"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
LOCAL_KERNEL = BASE / "local_principle_kernel_import.packet.json"
UNPATCHED_STATUS = BASE / "unpatched_kernel_theorem_status.packet.json"
HIGGS_IMPLICATION = BASE / "higgs_quartic_local_implication.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_HIGGS_01_H6_SelectedPhiFinC1PreResidualActionKernelTheorem_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H6_LOCAL_PRERESIDUAL_KERNEL_CLOSED_UNPATCHED_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    h5_path = DATA / "const_higgs_01_h5_physical_action_owns_finite_trace_kernel.candidate.json"
    h5b_path = DATA / "const_higgs_01_h5b_selected_higgs_nonlinear_amplitude_projection.candidate.json"
    h5b_projection_path = DATA / "const_higgs_01_h5b_selected_higgs_nonlinear_amplitude_projection" / "nonlinear_amplitude_projection_contract.packet.json"
    sm_h6_path = SM_PARITY_REPO / "candidate_data" / "selected_psm_c1_02_selectedphifinc1_preresidualactionkernel_theorem_or_localprincipledecision.candidate.json"
    local_import_path = SM_PARITY_REPO / "candidate_data" / "selected_psm_c1_02_selectedphifinc1_preresidualactionkernel_theorem_or_localprincipledecision" / "local_principle_kernel_closure_import.packet.json"
    si1c_decision_path = SM_PARITY_REPO / "candidate_data" / "selected_psm_c1_02_selectedphifinc1_preresidualactionkernel_theorem_or_localprincipledecision" / "si1c_decision.packet.json"
    unpatched_attempt_path = SM_PARITY_REPO / "candidate_data" / "selected_psm_c1_02_selectedphifinc1_preresidualactionkernel_theorem_or_localprincipledecision" / "unpatched_theorem_derivation_attempt.packet.json"
    sm_next_path = SM_PARITY_REPO / "candidate_data" / "selected_psm_c1_02_selectedphifinc1_preresidualactionkernel_theorem_or_localprincipledecision" / "next_labeled_workorder.packet.json"

    h5 = load(h5_path)
    h5b = load(h5b_path)
    h5b_projection = load(h5b_projection_path)
    sm_h6 = load(sm_h6_path)
    local_import = load(local_import_path)
    si1c_decision = load(si1c_decision_path)
    unpatched_attempt = load(unpatched_attempt_path)
    sm_next = load(sm_next_path)

    local_kernel = {
        "schema": "MTTConstHiggs01H6LocalPrincipleKernelImport.v1",
        "status": "LOCAL_PRINCIPLE_PRERESIDUAL_ACTION_KERNEL_IMPORTED",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6-LOCAL-PRERESIDUAL-ACTION-KERNEL",
        "inputs": {
            "H5_action_ownership_guardrail": rel(h5_path),
            "SM_parity_SI1c_candidate": rel(sm_h6_path),
            "local_principle_kernel_closure_import": rel(local_import_path),
            "SI1c_decision": rel(si1c_decision_path),
        },
        "local_kernel_closure": {
            "local_principle_accepted": local_import["local_principle_accepted"],
            "accepted_as": local_import["accepted_as"],
            "strict_kernel_closed_under_local_principle": local_import["strict_kernel_closed_under_local_principle"],
            "strict_kernel_validator_ok": local_import["strict_kernel_validator_ok"],
            "audit_ok": local_import["audit_ok"],
            "promoted_inside_local_spine": local_import["promoted_inside_local_spine"],
            "local_principle_scope": local_import["local_principle_scope"],
        },
        "si1c_decision": {
            "status": si1c_decision["status"],
            "source_identity_lemma_status": si1c_decision["source_identity_lemma_status"],
            "local_pre_residual_action_kernel_closed": si1c_decision["local_pre_residual_action_kernel_closed"],
            "unpatched_source_identity_lemma_status": si1c_decision["unpatched_source_identity_lemma_status"],
            "unpatched_theorem_derived_now": si1c_decision["unpatched_theorem_derived_now"],
            "superset_strategy": si1c_decision["superset_strategy"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    unpatched_status = {
        "schema": "MTTConstHiggs01H6UnpatchedKernelTheoremStatus.v1",
        "status": "UNPATCHED_PRERESIDUAL_ACTION_KERNEL_THEOREM_REMAINS_OPEN",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6-UNPATCHED-KERNEL-THEOREM-STATUS",
        "inputs": {
            "unpatched_theorem_derivation_attempt": rel(unpatched_attempt_path),
            "SM_parity_SI1c_candidate": rel(sm_h6_path),
        },
        "unpatched_attempt": {
            "theorem_name": unpatched_attempt["theorem_name"],
            "statement": unpatched_attempt["statement"],
            "unpatched_theorem_derived_now": unpatched_attempt["unpatched_theorem_derived_now"],
            "derivation_attempt_status": unpatched_attempt["derivation_attempt_status"],
            "why_not_derived": unpatched_attempt["why_not_derived"],
            "acceptable_proof_sources": unpatched_attempt["acceptable_proof_sources"],
            "forbidden_shortcuts": unpatched_attempt["forbidden_shortcuts"],
        },
        "sm_h6_remaining_open": sm_h6["what_remains_open"],
        "tier_decision": {
            "local_premise_tier_closed": True,
            "strict_no_knob_tier_closed": False,
            "unpatched_theorem_closed": False,
            "independent_kernel_execution_closed": False,
            "true_SM_equivalence_without_local_principle_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    higgs_implication = {
        "schema": "MTTConstHiggs01H6HiggsQuarticLocalImplication.v1",
        "status": "OBJECT1_CLOSED_IN_LOCAL_TIER_HIGGS_QUARTIC_ROWS_STILL_OPEN",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6-HIGGS-QUARTIC-LOCAL-IMPLICATION",
        "inputs": {
            "H5B_projection_contract": rel(h5b_projection_path),
            "H5B_candidate": rel(h5b_path),
        },
        "H4_H5_cutset_update": {
            "object_1_PhysicalActionOwnsFiniteTraceKernel_local_tier": True,
            "object_1_PhysicalActionOwnsFiniteTraceKernel_strict_unpatched": False,
            "object_2_SelectedHiggsNonlinearAmplitudeProjection_template": h5b["selected_Higgs_projection_functional_template_closed"],
            "selected_Higgs_amplitude_coordinate": h5b_projection["projection_functional"]["coordinate_index"],
            "future_quartic_row_address": h5b_projection["projection_functional"]["quartic_row_address"],
        },
        "why_Higgs_quartic_still_not_closed": {
            "local_SI1c_kernel_emits_C1_source-identity rows, not an actual H-sector fourth-variation row": True,
            "actual_nonlinear_Higgs_source_rows_emitted": False,
            "projection_on_actual_source_kernel_closed": False,
            "lambda_H_coefficient_convention_closed": False,
            "strict_no_knob_Higgs_closure": False,
        },
        "allowed_next_use": {
            "local_tier": "Use H6 local kernel as source-ownership premise for a conditional H6B projection test if actual H-sector nonlinear rows are emitted.",
            "strict_tier": "Continue unpatched derivation or independent kernel execution before claiming no-knob closure.",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstHiggs01H6NextWork.v1",
        "status": "NEXT_WORKORDER_H6B_LOCAL_SOURCE_IDENTITY_INTEGRATION_OR_H7_UNPATCHED",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6-NEXT",
        "primary_local_tier": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6B-LOCAL-SOURCE-IDENTITY-TO-HIGGS-ROW-EXPORT",
            "task": "Integrate the local SI-1c closure with the H5B coordinate projector and test whether any actual H-sector nonlinear fourth-variation row is emitted for [12,12,12,12].",
        },
        "strict_upgrade": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7-UNPATCHED-PHIFINC1-PRERESIDUAL-ACTION-KERNEL",
            "task": "Derive the Weyl-variation action principle unpatched or execute independent finite kernels, preserving no-observed-selector guardrails.",
        },
        "source_repo_next": {
            "next_required_artifact": sm_next["next_required_artifact"],
            "primary_label": sm_next["primary"]["label"],
            "secondary_label": sm_next["secondary"]["label"],
        },
    }

    candidate = {
        "candidate": "MTTConstHiggs01H6SelectedPhiFinC1PreResidualActionKernelTheorem",
        "status": STATUS,
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6-SELECTED-PHIFINC1-PRERESIDUAL-ACTION-KERNEL-THEOREM",
        "output_packets": {
            "local_principle_kernel_import": rel(LOCAL_KERNEL),
            "unpatched_kernel_theorem_status": rel(UNPATCHED_STATUS),
            "higgs_quartic_local_implication": rel(HIGGS_IMPLICATION),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTHiggs01H6LocalPreResidualActionKernelClosureTheorem",
            "proved": True,
            "statement": (
                "Relative to the accepted local SelectedWeylVariationActionPrinciple, the selected Phi_fin^C1 pre-residual action kernel closes the SI-1c source-kernel validator and promotes the local pre-residual phase/shift operator source, same-source Hessian b_selected rows, sector physical source promotion, and residual-projector independence inside the local proof spine. The unpatched SelectedPhiFinC1PreResidualActionKernelTheorem, independent kernel execution, no-knob closure, and actual Higgs fourth-variation row remain open."
            ),
        },
        "superset_strategy": {
            "local_route_C": "accepted local Weyl-variation principle supplies constrained local closure",
            "route_A_unpatched": "derive physical Phi_fin^C1 action identity and zero extra boundary/source term",
            "route_B_independent": "execute independent finite Galerkin/quadrature kernels",
            "locked_target": "SelectedPhiFinC1PreResidualActionKernelTheorem as source-ownership object for Higgs quartic program",
            "paths_used_as_free_parameters": False,
            "locked_target_used_only_as_postcheck": True,
        },
        "local_premise_pre_residual_action_kernel_closed": True,
        "local_strict_kernel_validator_ok": True,
        "PhysicalActionOwnsFiniteTraceKernel_local_tier_closed": True,
        "PhysicalActionOwnsFiniteTraceKernel_strict_unpatched_closed": False,
        "SelectedPhiFinC1PreResidualActionKernelTheorem_unpatched_closed": False,
        "independent_kernel_execution_closed": False,
        "selected_Higgs_projection_functional_template_closed": True,
        "actual_nonlinear_Higgs_source_rows_emitted": False,
        "projection_on_actual_source_kernel_closed": False,
        "selected_Higgs_quartic_threshold_kernel_emitted": False,
        "Higgs_quartic_numeric_value_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "new_Higgs_specific_parameters": 0,
        "selected_next_artifact": "MTT_CONST_HIGGS_01_H6B_LocalSourceIdentityToHiggsRowExport_v1",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_HIGGS_01_H6_SelectedPhiFinC1PreResidualActionKernelTheorem_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "active_label": candidate["active_label"],
        "local_premise_pre_residual_action_kernel_closed": True,
        "local_strict_kernel_validator_ok": True,
        "PhysicalActionOwnsFiniteTraceKernel_local_tier_closed": True,
        "PhysicalActionOwnsFiniteTraceKernel_strict_unpatched_closed": False,
        "SelectedPhiFinC1PreResidualActionKernelTheorem_unpatched_closed": False,
        "actual_nonlinear_Higgs_source_rows_emitted": False,
        "selected_Higgs_quartic_threshold_kernel_emitted": False,
        "Higgs_quartic_numeric_value_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    note = f"""# MTT CONST HIGGS 01 H6 Selected PhiFinC1 PreResidual Action Kernel Theorem v1

Status: `{STATUS}`

Label: `CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6-SELECTED-PHIFINC1-PRERESIDUAL-ACTION-KERNEL-THEOREM`

## Result

```text
local pre-residual action kernel closed          True
strict kernel validator ok                       True
unpatched theorem derived                        False
independent kernel execution                     False
actual nonlinear Higgs source rows emitted       False
Higgs quartic numeric value                      False
strict no-knob Higgs closure                     False
```

## Meaning

H6 closes the source-ownership object only in the local-premise tier:

```text
accepted local SelectedWeylVariationActionPrinciple
  => selected Phi_fin^C1 pre-residual action kernel
  => SI-1c validator passes inside the local proof spine
```

This is progress, but it is not unpatched/no-knob closure.

## Higgs Consequence

Together with H5B, the local tier now has:

```text
source-ownership premise: local closed
Higgs coordinate: [12]
future quartic row address: [12,12,12,12]
```

But H6 does not emit an actual H-sector fourth-variation row.  So `lambda_H`
is still not derived.

## Next

Local tier:

`CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6B-LOCAL-SOURCE-IDENTITY-TO-HIGGS-ROW-EXPORT`

Strict tier:

`CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7-UNPATCHED-PHIFINC1-PRERESIDUAL-ACTION-KERNEL`
"""

    for path, payload in [
        (LOCAL_KERNEL, local_kernel),
        (UNPATCHED_STATUS, unpatched_status),
        (HIGGS_IMPLICATION, higgs_implication),
        (NEXT_WORK, next_work),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        write_json(path, payload)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
