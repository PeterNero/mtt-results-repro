"""Build CONST-HIGGS-01 H7A2 selected nonlinear Higgs source-kernel gate."""

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

SLUG = "const_higgs_01_h7a2_selected_nonlinear_higgs_source_kernel"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SPECTRAL_OBSTRUCTION = BASE / "zero_mode_spectral_determinant_obstruction.packet.json"
NONLINEAR_CANDIDATES = BASE / "nonlinear_source_candidate_hunt.packet.json"
KERNEL_CONTRACT = BASE / "selected_nonlinear_kernel_acceptance_contract.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_HIGGS_01_H7A2_SelectedNonlinearHiggsSourceKernel_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7A2_NONLINEAR_SOURCE_KERNEL_GATE_BUILT_SOURCE_OPEN"


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

    h7a_path = DATA / "const_higgs_01_h7a_intrinsic_k4_row_execution_payload.candidate.json"
    h7a_schema_path = DATA / "const_higgs_01_h7a_intrinsic_k4_row_execution_payload" / "intrinsic_k4_execution_payload_schema.packet.json"
    h7a_nogo_path = DATA / "const_higgs_01_h7a_intrinsic_k4_row_execution_payload" / "quadratic_gap_layer_to_k4_nogo.packet.json"
    h7a_support_path = DATA / "const_higgs_01_h7a_intrinsic_k4_row_execution_payload" / "same_source_trace_and_h_projector_support_import.packet.json"
    h2_heat_path = DATA / "const_higgs_01_h2_selected_higgs_projector_and_quartic_kernel_source_packet" / "finite_heat_spectrum_response_import.packet.json"
    sm_heat_response_path = SM_PARITY_REPO / "candidate_data" / "selected_heattorsionresponse_finalgate" / "selected_finite_heat_spectrum_response.packet.json"
    h3_path = DATA / "const_higgs_01_h3_selected_higgs_quadratic_stiffness_and_quartic_gate" / "selected_quadratic_stiffness_kernel.packet.json"
    h5b_projection_path = DATA / "const_higgs_01_h5b_selected_higgs_nonlinear_amplitude_projection" / "nonlinear_amplitude_projection_contract.packet.json"
    sm_nonlinear_hym_path = SM_PARITY_REPO / "candidate_data" / "selected_nonlinear_hym_correction_coefficient_solve.candidate.json"
    sm_full_exps_path = SM_PARITY_REPO / "candidate_data" / "selected_full_exps_hym_newton_replay.candidate.json"

    h7a = load(h7a_path)
    h7a_schema = load(h7a_schema_path)
    h7a_nogo = load(h7a_nogo_path)
    h7a_support = load(h7a_support_path)
    h2_heat = load(h2_heat_path)
    sm_heat_response = load(sm_heat_response_path)
    h3 = load(h3_path)
    h5b_projection = load(h5b_projection_path)
    sm_nonlinear_hym = load(sm_nonlinear_hym_path)
    sm_full_exps = load(sm_full_exps_path)

    heat_imported = h2_heat["imported_response"]
    h3_source = h3["selected_source_kernel"]
    row_address = h5b_projection["projection_functional"]["quartic_row_address"]

    spectral_obstruction = {
        "schema": "MTTConstHiggs01H7A2ZeroModeSpectralDeterminantObstruction.v1",
        "status": "NAIVE_SPECTRAL_DETERMINANT_CANNOT_SUPPLY_ANALYTIC_ZERO_MODE_K4",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7A2-ZERO-MODE-SPECTRAL-DETERMINANT-OBSTRUCTION",
        "inputs": {
            "H7A_execution_payload": rel(h7a_path),
            "H7A_quadratic_gap_nogo": rel(h7a_nogo_path),
            "H2_heat_spectrum_response_import": rel(h2_heat_path),
            "SM_parity_selected_finite_heat_spectrum_response": rel(sm_heat_response_path),
            "H3_quadratic_stiffness_kernel": rel(h3_path),
            "H5B_projection_contract": rel(h5b_projection_path),
        },
        "selected_finite_spectral_data": {
            "finite_heat_spectrum_response_slot_closed": heat_imported["finite_determinant_heat_spectrum_or_torsion_response_closed"],
            "regularization": sm_heat_response["finite_spectrum_convention"]["regularization"],
            "H_sector_kernel_dimension": h3_source["H_sector_kernel_dimension"],
            "H_sector_zero_cluster_indices": h3_source["zero_cluster_indices"],
            "Higgs_amplitude_coordinate": h5b_projection["projection_functional"]["coordinate_index"],
            "Higgs_coordinate_is_zero_mode": h5b_projection["projection_functional"]["coordinate_index"] in h3_source["zero_cluster_indices"],
            "positive_complement_eigenvalues": h3_source["H_sector_positive_eigenvalues"],
        },
        "two_naive_determinant_routes": {
            "positive_complement_only": {
                "description": "Use the already selected positive-complement pseudodeterminant/heat trace exactly as emitted.",
                "depends_on_Higgs_zero_mode_amplitude": False,
                "emits_K4_for_a_H": False,
            },
            "reinsert_zero_mode_as_mass_shift": {
                "description": "Pretend the Higgs amplitude enters as a_H^2 on the zero-mode eigenvalue.",
                "local_form": "log det'(K + a_H^2 P_H) would contain log(a_H^2) if the zero mode is reinserted",
                "analytic_at_a_H_0": False,
                "emits_finite_fourth_derivative_at_origin": False,
            },
        },
        "verdict": {
            "spectral_heat_logdet_support_remains_valid": True,
            "naive_logdet_promoted_to_Higgs_quartic": False,
            "separate_selected_nonlinear_zero_mode_potential_required": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    nonlinear_candidates = {
        "schema": "MTTConstHiggs01H7A2NonlinearSourceCandidateHunt.v1",
        "status": "NONLINEAR_SOURCE_CANDIDATES_CLASSIFIED_NONE_PROMOTED",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7A2-NONLINEAR-SOURCE-CANDIDATE-HUNT",
        "candidates": {
            "selected_DE_gap_layer": {
                "source": rel(h7a_support_path),
                "classification": "SAME_SOURCE_PROJECTOR_AND_QUADRATIC_SUPPORT_ONLY",
                "promoted_to_nonlinear_kernel": False,
                "reason": "H7A proves the D_E gap layer is quadratic support, not a nonlinear fourth-variation source.",
            },
            "finite_heat_or_pseudodeterminant_spectral_action": {
                "source": rel(h2_heat_path),
                "classification": "VALID_SPECTRAL_SUPPORT_ZERO_MODE_K4_OBSTRUCTED",
                "promoted_to_nonlinear_kernel": False,
                "reason": "The emitted determinant is positive-complement/zero-projected; reinserting the Higgs zero mode gives nonanalytic log(a_H^2).",
            },
            "selected_nonlinear_HYM_expS_replay": {
                "source": rel(sm_nonlinear_hym_path),
                "classification": "NONLINEAR_METHODOLOGY_SUPPORT_NOT_HIGGS_ZERO_MODE_POTENTIAL",
                "promoted_to_nonlinear_kernel": False,
                "support_status": sm_nonlinear_hym["status"],
                "reason": "The nonlinear HYM solve is a selected connection/metric correction replay, not a same-source scalar Higgs zero-mode fourth potential.",
            },
            "full_expS_HYM_Newton_replay": {
                "source": rel(sm_full_exps_path),
                "classification": "NONLINEAR_SOLVE_SCAFFOLD_NOT_K4_ROW_SOURCE",
                "promoted_to_nonlinear_kernel": False,
                "support_status": sm_full_exps["status"],
                "reason": "It includes nonlinear metric factors but does not emit the H-sector K_H^(4)[12,12,12,12] row.",
            },
            "measured_SM_lambda_or_Higgs_mass": {
                "source": "SM parity measured replay layer",
                "classification": "FORBIDDEN_SOURCE_SELECTOR",
                "promoted_to_nonlinear_kernel": False,
                "reason": "Measured Higgs values are downstream parity inputs and cannot select a no-knob source kernel.",
            },
        },
        "best_current_strict_route_A_candidate": "selected nonlinear zero-mode effective potential from same q79/F,m=1 source",
        "candidate_promoted": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    kernel_contract = {
        "schema": "MTTConstHiggs01H7A2SelectedNonlinearKernelAcceptanceContract.v1",
        "status": "NONLINEAR_KERNEL_ACCEPTANCE_CONTRACT_READY_VALUES_OPEN",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7A2-SELECTED-NONLINEAR-KERNEL-ACCEPTANCE-CONTRACT",
        "target_row": {
            "formal_object": h7a_schema["target"]["formal_object"],
            "row_address": row_address,
            "basis_id": h7a_schema["target"]["basis_id"],
            "amplitude_coordinate": h7a_schema["target"]["amplitude_coordinate"],
        },
        "required_source_theorem": {
            "name": "SelectedNonlinearHiggsZeroModePotentialTheorem",
            "must_prove": [
                "same q79/F,m=1 source selects an analytic nonlinear zero-mode potential V_eff(a_H)",
                "V_eff is analytic at a_H=0 after zero-mode projection/renormalization",
                "the fourth derivative d^4 V_eff/da_H^4 at a_H=0 exists and is source-selected",
                "the row is independent of residual-projector replay and measured Higgs data",
                "the coefficient convention maps the fourth derivative to lambda_H without a hidden normalization knob",
            ],
        },
        "current_field_status": {
            "selected_nonlinear_source_functional_id": False,
            "analytic_zero_mode_potential": False,
            "same_source_H_sector_fourth_variation_row": False,
            "row_exactness_certificate": False,
            "row_specific_residual_independence_certificate": False,
            "lambda_H_coefficient_convention": False,
            "numeric_lambda_H_derived": False,
            "strict_no_knob_Higgs_closure": False,
        },
        "conditional_exact_formula_slot": {
            "if_functional_supplied": "K_H^(4)[12,12,12,12] = d^4/da_H^4 V_eff(a_H)|_{a_H=0}",
            "coefficient_template": "If V_eff includes (1/24)K4 a_H^4 and a_H is proven to be the canonically normalized real Higgs amplitude, then lambda_H still requires the complex-doublet normalization map.",
            "filled_now": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstHiggs01H7A2NextWork.v1",
        "status": "NEXT_WORKORDER_H7B_OR_H7A3_ZERO_MODE_POTENTIAL_THEOREM",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7A2-NEXT",
        "route_A_next": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7A3-SELECTED-NONLINEAR-ZERO-MODE-POTENTIAL-THEOREM",
            "task": "Try to prove or import a same-source analytic nonlinear zero-mode potential V_eff(a_H) and its fourth derivative.",
        },
        "route_B_parallel": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B-UV-BETA-OR-TWO-HIGGS-PROJECTION-THEOREM",
            "task": "Run the D-term route in parallel because Route A now requires a genuinely new nonlinear zero-mode theorem.",
        },
        "paper_insert_section": {
            "label": "CONST-HIGGS-01 / PAPER-INSERT / ZERO-MODE-DETERMINANT-OBSTRUCTION",
            "task": "Explain why finite heat/logdet support cannot by itself derive the Higgs quartic row.",
        },
    }

    candidate = {
        "candidate": "MTTConstHiggs01H7A2SelectedNonlinearHiggsSourceKernel",
        "status": STATUS,
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7A2-SELECTED-NONLINEAR-HIGGS-SOURCE-KERNEL",
        "output_packets": {
            "zero_mode_spectral_determinant_obstruction": rel(SPECTRAL_OBSTRUCTION),
            "nonlinear_source_candidate_hunt": rel(NONLINEAR_CANDIDATES),
            "selected_nonlinear_kernel_acceptance_contract": rel(KERNEL_CONTRACT),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTHiggs01H7A2ZeroModeSpectralObstructionAndNonlinearKernelContractTheorem",
            "proved": True,
            "statement": (
                "The selected finite heat/pseudodeterminant response is valuable same-source spectral support, but because it is defined on the positive complement after zero-mode projection and the Higgs amplitude is the zero-mode coordinate [12], it cannot by itself emit an analytic Higgs quartic row. Positive-complement replay ignores a_H; reinserting the zero mode produces a nonanalytic log(a_H^2) obstruction. Therefore strict Route A now requires a separate selected analytic nonlinear zero-mode potential theorem. No current candidate is promoted, no K4 row is emitted, and no numerical lambda_H is derived."
            ),
        },
        "zero_mode_spectral_determinant_obstruction_proved": True,
        "nonlinear_source_candidates_classified": True,
        "nonlinear_kernel_acceptance_contract_ready": True,
        "selected_nonlinear_source_kernel_found": False,
        "same_source_H_sector_fourth_variation_row_emitted": False,
        "numeric_lambda_H_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "new_Higgs_specific_parameters": 0,
        "selected_next_artifact": "MTT_CONST_HIGGS_01_H7A3_SelectedNonlinearZeroModePotentialTheorem_or_H7B_UVBetaTheorem_v1",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_HIGGS_01_H7A2_SelectedNonlinearHiggsSourceKernel_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "active_label": candidate["active_label"],
        "zero_mode_spectral_determinant_obstruction_proved": True,
        "nonlinear_source_candidates_classified": True,
        "nonlinear_kernel_acceptance_contract_ready": True,
        "selected_nonlinear_source_kernel_found": False,
        "same_source_H_sector_fourth_variation_row_emitted": False,
        "numeric_lambda_H_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "new_Higgs_specific_parameters": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    note = f"""# MTT CONST HIGGS 01 H7A2 Selected Nonlinear Higgs Source Kernel v1

Status: `{STATUS}`

Label: `CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7A2-SELECTED-NONLINEAR-HIGGS-SOURCE-KERNEL`

## Result

```text
zero-mode spectral determinant obstruction      True
nonlinear candidates classified                 True
nonlinear kernel acceptance contract ready      True
selected nonlinear source kernel found          False
K_H^(4)[12,12,12,12] emitted                    False
numeric lambda_H                                False
strict no-knob Higgs closure                    False
```

## Key Point

The selected heat/logdet object is positive-complement data.  The Higgs
amplitude is the zero-mode coordinate `[12]`.

```text
positive complement only: no a_H dependence
zero mode reinserted:     log(a_H^2), nonanalytic at a_H=0
```

So the spectral determinant route needs an additional selected analytic
zero-mode potential theorem before it can produce a Higgs quartic row.

## Next

`CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7A3-SELECTED-NONLINEAR-ZERO-MODE-POTENTIAL-THEOREM`

Parallel:

`CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B-UV-BETA-OR-TWO-HIGGS-PROJECTION-THEOREM`
"""

    for path, payload in [
        (SPECTRAL_OBSTRUCTION, spectral_obstruction),
        (NONLINEAR_CANDIDATES, nonlinear_candidates),
        (KERNEL_CONTRACT, kernel_contract),
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
