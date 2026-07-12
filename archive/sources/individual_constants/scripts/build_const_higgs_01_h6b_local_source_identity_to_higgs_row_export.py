"""Build CONST-HIGGS-01 H6B local source-identity to Higgs-row export gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_higgs_01_h6b_local_source_identity_to_higgs_row_export"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
LOCAL_EXPORT = BASE / "local_source_identity_to_higgs_row_export.packet.json"
TEMPLATE_LEDGER = BASE / "h4_template_field_ledger_after_h6b.packet.json"
ROW_OBSTRUCTION = BASE / "quartic_row_export_obstruction.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_HIGGS_01_H6B_LocalSourceIdentityToHiggsRowExport_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H6B_LOCAL_SOURCE_IDENTITY_EXPORT_BUILT_HIGGS_ROW_OPEN"


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

    h4_template_path = DATA / "const_higgs_01_h4_nonlinear_higgs_self_interaction_source_rule" / "strict_nonlinear_higgs_source_template.packet.json"
    h5b_candidate_path = DATA / "const_higgs_01_h5b_selected_higgs_nonlinear_amplitude_projection.candidate.json"
    h5b_projection_path = DATA / "const_higgs_01_h5b_selected_higgs_nonlinear_amplitude_projection" / "nonlinear_amplitude_projection_contract.packet.json"
    h5b_template_path = DATA / "const_higgs_01_h5b_selected_higgs_nonlinear_amplitude_projection" / "h4_template_field_fill.packet.json"
    h6_candidate_path = DATA / "const_higgs_01_h6_selected_phifinc1_preresidual_action_kernel_theorem.candidate.json"
    h6_local_path = DATA / "const_higgs_01_h6_selected_phifinc1_preresidual_action_kernel_theorem" / "local_principle_kernel_import.packet.json"
    h6_unpatched_path = DATA / "const_higgs_01_h6_selected_phifinc1_preresidual_action_kernel_theorem" / "unpatched_kernel_theorem_status.packet.json"
    h6_implication_path = DATA / "const_higgs_01_h6_selected_phifinc1_preresidual_action_kernel_theorem" / "higgs_quartic_local_implication.packet.json"
    g4_primitive_path = DATA / "const_gr_01_absolute_scale_g4_omega0_physical_unit_or_one_metrology_primitive" / "one_metrology_primitive_contract.packet.json"

    h4_template = load(h4_template_path)
    h5b_candidate = load(h5b_candidate_path)
    h5b_projection = load(h5b_projection_path)
    h5b_template = load(h5b_template_path)
    h6_candidate = load(h6_candidate_path)
    h6_local = load(h6_local_path)
    h6_unpatched = load(h6_unpatched_path)
    h6_implication = load(h6_implication_path)
    g4_primitive = load(g4_primitive_path)

    coordinate = h5b_projection["projection_functional"]["coordinate_index"]
    row_address = h5b_projection["projection_functional"]["quartic_row_address"]
    promoted = h6_local["local_kernel_closure"]["promoted_inside_local_spine"]

    local_export = {
        "schema": "MTTConstHiggs01H6BLocalSourceIdentityToHiggsRowExport.v1",
        "status": "LOCAL_SOURCE_IDENTITY_EXPORT_READY_HIGGS_ROW_NOT_EMITTED",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6B-LOCAL-SOURCE-IDENTITY-TO-HIGGS-ROW-EXPORT",
        "inputs": {
            "H4_strict_template": rel(h4_template_path),
            "H5B_projection_contract": rel(h5b_projection_path),
            "H6_local_kernel_import": rel(h6_local_path),
            "G4_one_metrology_primitive_contract": rel(g4_primitive_path),
        },
        "export_scope": {
            "tier": "LOCAL_PREMISE_TIER_ONLY",
            "accepted_premise": h6_local["local_kernel_closure"]["accepted_as"],
            "local_principle_scope": h6_local["local_kernel_closure"]["local_principle_scope"],
            "strict_no_knob_tier": False,
            "unpatched_theorem_tier": h6_unpatched["tier_decision"]["unpatched_theorem_closed"],
        },
        "source_identity_exports": {
            "selected_nonlinear_action_or_PhiFin_source_id": {
                "filled": True,
                "source_id": "local:SelectedWeylVariationActionPrinciple/Phi_fin^C1/pre-residual-action-kernel",
                "justification": "H6 local kernel imports selected Phi_fin^C1 pre-residual action ownership inside the local proof spine.",
            },
            "selected_variation_space_id": {
                "filled": True,
                "source_id": "local:pre-residual phase/shift variation space",
                "justification": "H6 promotes the pre-residual phase/shift operator source before residual-projector replay.",
            },
            "finite_trace_or_pairing_source_id": {
                "filled": True,
                "source_id": "local:finite-trace/C1 source-kernel pairing",
                "justification": "H6 promotes same-source Hessian b_selected rows and sector-row physical source promotion inside the local spine.",
            },
            "selector_guardrail": {
                "filled": True,
                "forbidden_selectors": [
                    "observed Higgs mass",
                    "observed Higgs vev",
                    "observed Higgs quartic lambda_H",
                    "SM masses, CKM, PMNS",
                    "alpha or weak mixing angle",
                    "RG benchmark or precision-fit row",
                ],
            },
            "G4_normalization_contract": {
                "filled": True,
                "tier": g4_primitive["parameter_budget"]["accepted_tier"],
                "new_Higgs_specific_parameters": g4_primitive["parameter_budget"]["new_sector_specific_parameters"],
            },
            "Higgs_projection_certificate_template": {
                "filled": h5b_candidate["selected_Higgs_projection_functional_template_closed"],
                "coordinate_index": coordinate,
                "quartic_row_address": row_address,
                "actual_row_projection": False,
            },
        },
        "non_exports": {
            "second_or_fourth_variation_rows": False,
            "H_sector_fourth_variation_row": False,
            "exactness_or_error_certificate_for_H_row": False,
            "lambda_H_style_coefficient_convention": False,
            "Higgs_quartic_numeric_value": False,
        },
        "superset_strategy": {
            "paths_combined": [
                "H5B selected H-sector amplitude coordinate",
                "H6 local Phi_fin^C1 pre-residual source identity",
                "G4 shared one-metrology primitive contract",
            ],
            "locked_target": "selected H-sector quartic source row K_H^(4)[12,12,12,12]",
            "used_as_free_parameter_search": False,
            "locked_target_used_only_as_postcheck": True,
        },
        "promoted_inside_local_spine": promoted,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    field_status = {
        "G4_normalization_contract": {
            "filled": True,
            "source": rel(g4_primitive_path),
            "tier": "shared one-metrology primitive; not Higgs-specific and not no-knob",
        },
        "selected_Higgs_zero_mode_or_amplitude_coordinate": {
            "filled": h5b_template["filled_now"]["selected_Higgs_zero_mode_or_amplitude_coordinate"],
            "source": rel(h5b_projection_path),
            "coordinate_index": coordinate,
        },
        "Higgs_projection_certificate": {
            "filled": True,
            "template_level_only": True,
            "actual_source_row_projection": False,
            "source": rel(h5b_projection_path),
        },
        "selected_nonlinear_action_or_PhiFin_source_id": {
            "filled": True,
            "source": rel(h6_local_path),
            "tier": "local premise",
        },
        "selected_variation_space_id": {
            "filled": True,
            "source": rel(h6_local_path),
            "tier": "local premise",
        },
        "finite_trace_or_pairing_source_id": {
            "filled": True,
            "source": rel(h6_local_path),
            "tier": "local premise",
        },
        "selector_guardrail": {
            "filled": True,
            "source": rel(h4_template_path),
            "observed_selectors_forbidden": True,
        },
        "second_or_fourth_variation_rows": {
            "filled": False,
            "missing_payload": "actual selected nonlinear H-sector fourth-variation row or exact finite formula",
            "target_row_address": row_address,
        },
        "exactness_or_error_certificate": {
            "filled": False,
            "missing_payload": "exact arithmetic or certified numerical bound for the H-sector row, not just SI-1c source rows",
        },
        "lambda_H_style_coefficient_convention": {
            "filled": False,
            "missing_payload": "action/potential convention after source-row emission",
        },
    }
    strict_required = [
        "G4_normalization_contract",
        "selected_Higgs_zero_mode_or_amplitude_coordinate",
        "Higgs_projection_certificate",
        "selected_nonlinear_action_or_PhiFin_source_id",
        "selected_variation_space_id",
        "finite_trace_or_pairing_source_id",
        "selector_guardrail",
        "second_or_fourth_variation_rows",
        "exactness_or_error_certificate",
    ]
    filled_required = [name for name in strict_required if field_status[name]["filled"]]
    open_required = [name for name in strict_required if not field_status[name]["filled"]]

    template_ledger = {
        "schema": "MTTConstHiggs01H6BH4TemplateFieldLedger.v1",
        "status": "H4_TEMPLATE_LOCAL_SOURCE_FIELDS_FILLED_ACTUAL_ROW_FIELDS_OPEN",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6B-H4-TEMPLATE-FIELD-LEDGER",
        "H4_required_fields": h4_template["required_fields"],
        "field_status_after_H6B": field_status,
        "counts": {
            "strict_required_field_count": len(strict_required),
            "filled_required_field_count": len(filled_required),
            "open_required_field_count": len(open_required),
            "filled_required_fields": filled_required,
            "open_required_fields": open_required,
        },
        "acceptance_after_H6B": {
            "local_source_identity_fields_present": True,
            "actual_H_sector_row_fields_present": False,
            "all_required_fields_present": False,
            "conditional_witness_counts_as_strict_closure": False,
            "measured_replay_allowed_after_source_emission_only": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    row_obstruction = {
        "schema": "MTTConstHiggs01H6BQuarticRowExportObstruction.v1",
        "status": "QUARTIC_ROW_ADDRESS_OWNED_BUT_VALUE_NOT_EMITTED",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6B-QUARTIC-ROW-EXPORT-OBSTRUCTION",
        "attempted_row": {
            "formal_object": h5b_projection["projection_functional"]["projected_formal_object"],
            "coordinate_index": coordinate,
            "quartic_row_address": row_address,
            "row_owner_source_local_tier": True,
            "actual_row_value_emitted": False,
        },
        "why_the_row_does_not_follow_yet": {
            "H6_SI1c_rows_are_source_identity_rows_not_H_sector_fourth_variation_rows": True,
            "H5B_row_address_is_a_projection_address_not_a_row_value": True,
            "H3_quadratic_stiffness_K2_cannot_be_promoted_to_K4": True,
            "support_only_or_replay_rows_are_forbidden_as_source_selection": True,
            "lambda_H_measured_backsolve_is_forbidden": True,
        },
        "minimal_missing_payload": {
            "same_source_H_sector_fourth_variation_row": "K_H^(4)[12,12,12,12] or exact multilinear formula from the selected pre-residual action",
            "row_exactness_certificate": "exact arithmetic or certified bounded numerical quadrature",
            "coefficient_convention": "conversion from fourth action variation to lambda_H after source-row emission",
            "row_specific_residual_independence": "certificate that the H row is pre-residual and not replay-selected by the residual projector",
        },
        "legal_next_routes": {
            "H6C_local_actual_row_export": "derive the H-sector fourth-variation row under the accepted local Weyl-variation premise",
            "H7_unpatched_kernel_theorem": "derive SelectedPhiFinC1PreResidualActionKernelTheorem without the local premise",
            "RouteB_independent_kernel_execution": "emit an independent finite row packet with source ids and exactness/error certificates",
        },
        "H6_implication_replayed": h6_implication["why_Higgs_quartic_still_not_closed"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstHiggs01H6BNextWork.v1",
        "status": "NEXT_WORKORDER_H6C_ACTUAL_H_ROW_OR_H7_UNPATCHED",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6B-NEXT",
        "primary_local_tier": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6C-LOCAL-ACTUAL-H-SECTOR-FOURTH-VARIATION-ROW",
            "task": "Use the accepted local pre-residual action kernel to emit the actual H-sector fourth-variation row K_H^(4)[12,12,12,12] or an exact finite multilinear formula.",
        },
        "strict_upgrade": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7-UNPATCHED-PHIFINC1-PRERESIDUAL-ACTION-KERNEL",
            "task": "Derive the source-identity/action-kernel theorem without the local Weyl-variation premise.",
        },
        "independent_route": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B-INDEPENDENT-H-SECTOR-ROW-PACKET",
            "task": "Build independent exact/quadrature H-sector fourth-variation rows with source provenance.",
        },
        "paper_insert_section": {
            "label": "CONST-HIGGS-01 / PAPER-INSERT / LOCAL-SOURCE-IDENTITY-EXPORT-BOUNDARY",
            "task": "State that local source ownership and H4 source fields are filled, while row value, exactness, coefficient convention, and lambda_H remain open.",
        },
    }

    candidate = {
        "candidate": "MTTConstHiggs01H6BLocalSourceIdentityToHiggsRowExport",
        "status": STATUS,
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6B-LOCAL-SOURCE-IDENTITY-TO-HIGGS-ROW-EXPORT",
        "output_packets": {
            "local_source_identity_to_higgs_row_export": rel(LOCAL_EXPORT),
            "h4_template_field_ledger_after_h6b": rel(TEMPLATE_LEDGER),
            "quartic_row_export_obstruction": rel(ROW_OBSTRUCTION),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTHiggs01H6BLocalSourceIdentityToHiggsRowExportTheorem",
            "proved": True,
            "statement": (
                "Combining H5B's selected Higgs amplitude coordinate e_H[12], H6's locally accepted Phi_fin^C1 pre-residual source identity, and the G4 shared metrology contract fills the H4 local source-identity fields for the Higgs quartic program: selected nonlinear Phi_fin source id, selected pre-residual variation space id, finite trace/pairing source id, selector guardrail, G4 normalization contract, and a template-level projection certificate. It does not emit the actual H-sector fourth-variation row K_H^(4)[12,12,12,12], an exactness/error certificate for that row, a lambda_H coefficient convention, a numerical Higgs quartic value, or strict no-knob closure."
            ),
        },
        "local_source_identity_fields_filled": True,
        "local_Higgs_row_export_contract_ready": True,
        "selected_Higgs_amplitude_coordinate": coordinate,
        "target_quartic_row_address": row_address,
        "actual_nonlinear_Higgs_source_rows_emitted": False,
        "H_sector_fourth_variation_row_emitted": False,
        "projection_on_actual_source_kernel_closed": False,
        "selected_Higgs_quartic_threshold_kernel_emitted": False,
        "Higgs_quartic_numeric_value_derived": False,
        "lambda_H_coefficient_convention_closed": False,
        "strict_no_knob_Higgs_closure": False,
        "strict_unpatched_action_kernel_closed": h6_candidate["PhysicalActionOwnsFiniteTraceKernel_strict_unpatched_closed"],
        "new_Higgs_specific_parameters": 0,
        "selected_next_artifact": "MTT_CONST_HIGGS_01_H6C_LocalActualHSectorFourthVariationRow_v1",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_HIGGS_01_H6B_LocalSourceIdentityToHiggsRowExport_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "active_label": candidate["active_label"],
        "local_source_identity_fields_filled": True,
        "local_Higgs_row_export_contract_ready": True,
        "selected_Higgs_amplitude_coordinate": coordinate,
        "target_quartic_row_address": row_address,
        "actual_nonlinear_Higgs_source_rows_emitted": False,
        "H_sector_fourth_variation_row_emitted": False,
        "selected_Higgs_quartic_threshold_kernel_emitted": False,
        "Higgs_quartic_numeric_value_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "new_Higgs_specific_parameters": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    note = f"""# MTT CONST HIGGS 01 H6B Local Source Identity To Higgs Row Export v1

Status: `{STATUS}`

Label: `CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6B-LOCAL-SOURCE-IDENTITY-TO-HIGGS-ROW-EXPORT`

## Result

```text
local source-identity fields filled              True
selected Higgs coordinate                        {coordinate}
target quartic row address                       {row_address}
actual H-sector fourth-variation row emitted     False
Higgs quartic numeric value                      False
strict no-knob Higgs closure                     False
```

## Theorem

H6B combines three already-frozen pieces:

```text
H5B: selected Higgs amplitude coordinate e_H[12]
H6:  local Phi_fin^C1 pre-residual source identity
G4:  shared one-metrology primitive contract
```

This fills the H4 local source-identity side of the Higgs quartic template:

```text
selected nonlinear Phi_fin source id
selected pre-residual variation space id
finite trace / pairing source id
selector guardrail
G4 normalization contract
template-level Higgs projection certificate
```

## Boundary

The actual row is still not emitted:

```text
K_H^(4)[12,12,12,12]
```

So H6B is an export theorem, not a quartic-value theorem.  It does not derive
`lambda_H`, and it does not close the strict no-knob Higgs branch.

## Next

Local tier:

`CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6C-LOCAL-ACTUAL-H-SECTOR-FOURTH-VARIATION-ROW`

Strict tier:

`CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7-UNPATCHED-PHIFINC1-PRERESIDUAL-ACTION-KERNEL`
"""

    for path, payload in [
        (LOCAL_EXPORT, local_export),
        (TEMPLATE_LEDGER, template_ledger),
        (ROW_OBSTRUCTION, row_obstruction),
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
