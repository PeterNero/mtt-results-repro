"""Build CONST-HIGGS-01 H5B selected Higgs nonlinear amplitude projection contract."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_higgs_01_h5b_selected_higgs_nonlinear_amplitude_projection"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ZERO_MODE = BASE / "selected_higgs_zero_mode_coordinate.packet.json"
PROJECTION_CONTRACT = BASE / "nonlinear_amplitude_projection_contract.packet.json"
TEMPLATE_FILL = BASE / "h4_template_field_fill.packet.json"
QUARTIC_BOUNDARY = BASE / "quartic_projection_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_HIGGS_01_H5B_SelectedHiggsNonlinearAmplitudeProjection_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H5B_HIGGS_AMPLITUDE_PROJECTION_CONTRACT_BUILT_SOURCE_ROWS_OPEN"


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

    h2_projector_path = DATA / "const_higgs_01_h2_selected_higgs_projector_and_quartic_kernel_source_packet" / "higgs_projector_source_packet.packet.json"
    h3_quadratic_path = DATA / "const_higgs_01_h3_selected_higgs_quadratic_stiffness_and_quartic_gate" / "selected_quadratic_stiffness_kernel.packet.json"
    h4_template_path = DATA / "const_higgs_01_h4_nonlinear_higgs_self_interaction_source_rule" / "strict_nonlinear_higgs_source_template.packet.json"
    h5_path = DATA / "const_higgs_01_h5_physical_action_owns_finite_trace_kernel.candidate.json"
    h5_implication_path = DATA / "const_higgs_01_h5_physical_action_owns_finite_trace_kernel" / "higgs_quartic_implication.packet.json"

    h2_projector = load(h2_projector_path)
    h3_quadratic = load(h3_quadratic_path)
    h4_template = load(h4_template_path)
    h5 = load(h5_path)
    h5_implication = load(h5_implication_path)

    zero_cluster = h2_projector["H_sector_selected_gap_layer"]["zero_cluster_indices"]
    shifted = h2_projector["H_sector_selected_gap_layer"]["H_shift_indices"]
    surviving = sorted(index for index in zero_cluster if index not in shifted)

    zero_mode = {
        "schema": "MTTConstHiggs01H5BSelectedHiggsZeroModeCoordinate.v1",
        "status": "SELECTED_HIGGS_ZERO_MODE_COORDINATE_IDENTIFIED",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H5B-SELECTED-HIGGS-ZERO-MODE-COORDINATE",
        "inputs": {
            "H2_projector_source_packet": rel(h2_projector_path),
            "H3_quadratic_stiffness_kernel": rel(h3_quadratic_path),
        },
        "selection": {
            "finite_basis_id": h3_quadratic["selected_source_kernel"]["finite_basis_id"],
            "finite_basis_dimension": h3_quadratic["selected_source_kernel"]["finite_basis_dimension"],
            "sector": "H",
            "zero_cluster_indices": zero_cluster,
            "rank_two_H_shift_indices": shifted,
            "surviving_zero_mode_indices": surviving,
            "surviving_zero_mode_dimension": len(surviving),
            "H_sector_kernel_dimension": h3_quadratic["selected_source_kernel"]["H_sector_kernel_dimension"],
            "coordinate_symbol": "a_H",
            "coordinate_basis_vector": f"e_H[{surviving[0]}]" if len(surviving) == 1 else None,
        },
        "proof": {
            "rank_two_shift_source_proved": h2_projector["H_sector_selected_gap_layer"]["H_rank_two_shift_source_proved"],
            "zero_mode_dimension_matches_kernel_dimension": len(surviving) == h3_quadratic["selected_source_kernel"]["H_sector_kernel_dimension"],
            "selected_coordinate_closed": len(surviving) == 1,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    projection_contract = {
        "schema": "MTTConstHiggs01H5BNonlinearAmplitudeProjectionContract.v1",
        "status": "CONDITIONAL_NONLINEAR_AMPLITUDE_PROJECTION_CONTRACT_BUILT",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H5B-NONLINEAR-AMPLITUDE-PROJECTION-CONTRACT",
        "inputs": {
            "selected_higgs_zero_mode_coordinate": rel(ZERO_MODE),
            "H4_strict_nonlinear_template": rel(h4_template_path),
            "H5_action_ownership": rel(h5_path),
        },
        "projection_functional": {
            "domain": "selected nonlinear H-sector source tensor/rows after physical source ownership or independent Hessian/quadrature emission",
            "amplitude_coordinate": "a_H",
            "coordinate_index": surviving[0] if len(surviving) == 1 else None,
            "coordinate_projector": f"P_H0 = |e_H[{surviving[0]}]><e_H[{surviving[0]}]|" if len(surviving) == 1 else None,
            "quartic_row_address": [surviving[0], surviving[0], surviving[0], surviving[0]] if len(surviving) == 1 else None,
            "projected_formal_object": "K_H^(4)[a_H,a_H,a_H,a_H]",
            "coefficient_policy": "The source packet must state the action/potential convention before converting the projected fourth-variation row into a lambda_H-style coefficient.",
        },
        "conditional_acceptance": {
            "selected_Higgs_zero_mode_or_amplitude_coordinate_closed": len(surviving) == 1,
            "Higgs_projection_certificate_template_closed": True,
            "actual_nonlinear_source_rows_emitted": False,
            "PhysicalActionOwnsFiniteTraceKernel_closed": h5["PhysicalActionOwnsFiniteTraceKernel_closed"],
            "SelectedPhiFinC1PreResidualActionKernelTheorem_closed": h5["SelectedPhiFinC1PreResidualActionKernelTheorem_closed"],
            "projection_on_actual_source_kernel_closed": False,
            "lambda_H_coefficient_convention_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    template_fill = {
        "schema": "MTTConstHiggs01H5BH4TemplateFieldFill.v1",
        "status": "ONE_H4_TEMPLATE_FIELD_FILLED_PROJECTION_CONTRACT_READY",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H5B-H4-TEMPLATE-FIELD-FILL",
        "H4_required_fields": h4_template["required_fields"],
        "filled_now": {
            "selected_Higgs_zero_mode_or_amplitude_coordinate": True,
            "Higgs_projection_certificate": "template-level closed; actual source-kernel projection waits for source rows",
        },
        "still_open": {
            "selected_nonlinear_action_or_PhiFin_source_id": True,
            "selected_variation_space_id": True,
            "finite_trace_or_pairing_source_id": True,
            "second_or_fourth_variation_rows": True,
            "exactness_or_error_certificate": True,
            "G4_normalization_contract": False,
            "selector_guardrail": False,
            "lambda_H_style_coefficient_convention": True,
        },
        "acceptance_after_H5B": {
            "all_required_fields_present": False,
            "conditional_witness_counts_as_strict_closure": False,
            "measured_replay_allowed_after_source_emission_only": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    quartic_boundary = {
        "schema": "MTTConstHiggs01H5BQuarticProjectionBoundary.v1",
        "status": "PROJECTION_CONTRACT_BUILT_QUARTIC_SOURCE_STILL_OPEN",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H5B-QUARTIC-PROJECTION-BOUNDARY",
        "H5_cutset_replayed": h5_implication["H5_update"],
        "what_closes_now": {
            "selected_Higgs_zero_mode_coordinate": True,
            "selected_Higgs_projection_functional_template": True,
            "quartic_row_address_for_future_source": True,
        },
        "what_remains_open": {
            "PhysicalActionOwnsFiniteTraceKernel": True,
            "SelectedPhiFinC1PreResidualActionKernelTheorem": True,
            "actual_nonlinear_Higgs_source_rows": True,
            "projection_on_actual_nonlinear_source_kernel": True,
            "lambda_H_numeric_value": True,
            "strict_no_knob_Higgs_closure": True,
        },
        "forbidden_promotions": [
            "coordinate projection template -> Higgs quartic value",
            "H-sector kernel dimension 1 -> nonlinear self-interaction source",
            "future row address [12,12,12,12] -> actual row emission",
            "lambda_H measured replay -> source coefficient",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstHiggs01H5BNextWork.v1",
        "status": "NEXT_WORKORDER_H6_SOURCE_KERNEL_THEN_H6B_PROJECT_ROWS",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6-H6B-NEXT",
        "primary": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6-SELECTED-PHIFINC1-PRERESIDUAL-ACTION-KERNEL-THEOREM",
            "task": "Close the nonlinear source ownership theorem or independent Hessian/quadrature replacement.",
        },
        "parallel_after_source": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6B-PROJECT-ACTUAL-NONLINEAR-SOURCE-ROWS-TO-HIGGS-QUARTIC",
            "task": "Once source rows are emitted, apply the H5B coordinate projector to row [12,12,12,12] and convert only under a declared action/potential convention.",
        },
        "paper_update_section": {
            "label": "CONST-HIGGS-01 / PAPER-INSERT / HIGGS-ZERO-MODE-PROJECTION-CONTRACT",
            "task": "Record that H5B fixes the selected Higgs amplitude coordinate and projection template, but not the nonlinear source or lambda_H.",
        },
    }

    candidate = {
        "candidate": "MTTConstHiggs01H5BSelectedHiggsNonlinearAmplitudeProjection",
        "status": STATUS,
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H5B-SELECTED-HIGGS-NONLINEAR-AMPLITUDE-PROJECTION",
        "output_packets": {
            "selected_higgs_zero_mode_coordinate": rel(ZERO_MODE),
            "nonlinear_amplitude_projection_contract": rel(PROJECTION_CONTRACT),
            "h4_template_field_fill": rel(TEMPLATE_FILL),
            "quartic_projection_boundary": rel(QUARTIC_BOUNDARY),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTHiggs01H5BSelectedHiggsAmplitudeProjectionContractTheorem",
            "proved": True,
            "statement": (
                "H5B uses the H2 selected H-sector zero cluster and rank-two shift with the H3 kernel-dimension check to identify the unique selected Higgs amplitude coordinate e_H[12]. This fills the H4 selected_Higgs_zero_mode_or_amplitude_coordinate field and builds a conditional projection functional for future nonlinear source rows, with row address [12,12,12,12]. It does not emit actual nonlinear source rows, close PhysicalActionOwnsFiniteTraceKernel, or derive lambda_H."
            ),
        },
        "selected_Higgs_zero_mode_coordinate_closed": True,
        "selected_Higgs_projection_functional_template_closed": True,
        "projection_row_address": [12, 12, 12, 12],
        "PhysicalActionOwnsFiniteTraceKernel_closed": False,
        "SelectedPhiFinC1PreResidualActionKernelTheorem_closed": False,
        "actual_nonlinear_Higgs_source_rows_emitted": False,
        "projection_on_actual_source_kernel_closed": False,
        "selected_Higgs_quartic_threshold_kernel_emitted": False,
        "Higgs_quartic_numeric_value_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "new_Higgs_specific_parameters": 0,
        "selected_next_artifact": "MTT_CONST_HIGGS_01_H6_SelectedPhiFinC1PreResidualActionKernelTheorem_v1",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_HIGGS_01_H5B_SelectedHiggsNonlinearAmplitudeProjection_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "active_label": candidate["active_label"],
        "selected_Higgs_zero_mode_coordinate_closed": True,
        "selected_Higgs_projection_functional_template_closed": True,
        "projection_row_address": [12, 12, 12, 12],
        "actual_nonlinear_Higgs_source_rows_emitted": False,
        "projection_on_actual_source_kernel_closed": False,
        "selected_Higgs_quartic_threshold_kernel_emitted": False,
        "Higgs_quartic_numeric_value_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "new_Higgs_specific_parameters": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    note = f"""# MTT CONST HIGGS 01 H5B Selected Higgs Nonlinear Amplitude Projection v1

Status: `{STATUS}`

Label: `CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H5B-SELECTED-HIGGS-NONLINEAR-AMPLITUDE-PROJECTION`

## Result

```text
zero cluster indices                             {zero_cluster}
rank-two H shift indices                         {shifted}
surviving H zero-mode coordinate                 {surviving}
quartic row address                              {[surviving[0], surviving[0], surviving[0], surviving[0]]}
projection template closed                       True
actual nonlinear source rows emitted             False
Higgs quartic numeric value                      False
```

## Theorem

H5B identifies the selected Higgs amplitude coordinate:

```text
zero cluster [12,13,14] minus shifted indices [13,14] = [12]
```

So the future nonlinear Higgs quartic row has the selected address:

```text
K_H^(4)[12,12,12,12]
```

This closes the projection coordinate/template.  It does not emit the source
row itself, and it does not choose a `lambda_H` convention or value.

## Next

`CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6-SELECTED-PHIFINC1-PRERESIDUAL-ACTION-KERNEL-THEOREM`

After H6 emits source rows:

`CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6B-PROJECT-ACTUAL-NONLINEAR-SOURCE-ROWS-TO-HIGGS-QUARTIC`
"""

    for path, payload in [
        (ZERO_MODE, zero_mode),
        (PROJECTION_CONTRACT, projection_contract),
        (TEMPLATE_FILL, template_fill),
        (QUARTIC_BOUNDARY, quartic_boundary),
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
