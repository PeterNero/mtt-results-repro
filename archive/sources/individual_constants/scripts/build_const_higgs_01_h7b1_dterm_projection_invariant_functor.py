"""Build CONST-HIGGS-01 H7B1 D-term projection invariant functor."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
Q79_REPO = TEXPAPERS / "mtt-q79-proof-repro"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_higgs_01_h7b1_dterm_projection_invariant_functor"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PROJECTOR_FUNCTOR = BASE / "uv_two_higgs_projector_to_sbeta_functor.packet.json"
SOURCE_SEARCH = BASE / "selected_projector_source_search.packet.json"
ACCEPTANCE = BASE / "selected_projector_acceptance_contract.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_HIGGS_01_H7B1_DTermProjectionInvariantFunctor_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7B1_DTERM_PROJECTOR_FUNCTOR_BUILT_VALUES_OPEN"


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

    h7b_path = DATA / "const_higgs_01_h7b_uv_beta_or_two_higgs_projection_theorem.candidate.json"
    h7b_contract_path = DATA / "const_higgs_01_h7b_uv_beta_or_two_higgs_projection_theorem" / "minimal_route_b_payload_contract.packet.json"
    h7b_under_path = DATA / "const_higgs_01_h7b_uv_beta_or_two_higgs_projection_theorem" / "projection_invariant_underdetermination_proof.packet.json"
    h6f_boundary_path = DATA / "const_higgs_01_h6f_symbolic_dterm_boundary_replay" / "symbolic_boundary_replay_functor.packet.json"
    ew_b41_path = DATA / "const_ew_02_weak_mixing_b41_gauge_action_rg_matching" / "rg_matching_threshold_scheme_status.packet.json"
    q79_single_path = Q79_REPO / "certificates" / "single_higgs_channel_projection_certificate.json"

    h7b = load(h7b_path)
    h7b_contract = load(h7b_contract_path)
    h7b_under = load(h7b_under_path)
    h6f_boundary = load(h6f_boundary_path)
    ew_b41 = load(ew_b41_path)
    q79_single = load(q79_single_path)

    projector_functor = {
        "schema": "MTTConstHiggs01H7B1UVTwoHiggsProjectorToSBetaFunctor.v1",
        "status": "FORMAL_PROJECTOR_TO_SBETA_FUNCTOR_BUILT_SELECTED_PROJECTOR_VALUES_OPEN",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1-UV-TWO-HIGGS-PROJECTOR-TO-SBETA-FUNCTOR",
        "inputs": {
            "H7B_minimal_payload_contract": rel(h7b_contract_path),
            "H6F_symbolic_Dterm_boundary": rel(h6f_boundary_path),
            "q79_single_Higgs_projection": rel(q79_single_path),
        },
        "two_higgs_plane": {
            "name": "E_H^UV",
            "basis": ["H_u", "H_d^dagger"],
            "reason_for_conjugating_Hd": "Both basis elements then carry the low-energy H hypercharge +1/2 channel.",
            "basis_labels_closed": q79_single["closed"]["single_higgs_channel_projection"],
            "selected_metric_on_plane_filled": False,
        },
        "Dterm_charge_involution": {
            "symbol": "J_D",
            "matrix_in_ordered_basis": [[1, 0], [0, -1]],
            "source_status": "formal from H_u/H_d D-term signs; value selection still needs the selected two-Higgs plane metric/projector",
            "filled_as_formal_operator": True,
        },
        "light_line_projector": {
            "symbol": "P_L",
            "type": "rank-one Hermitian projector on E_H^UV",
            "selected_projector_values_filled": False,
            "equivalent_coordinate_form_if_metric_is_orthonormal": "P_L=|c><c| with |c_u|^2+|c_d|^2=1",
        },
        "projection_invariant": {
            "cos2beta_without_beta": "Tr(J_D P_L)",
            "s_beta": "(Tr(J_D P_L))^2",
            "coordinate_form_if_metric_is_orthonormal": "s_beta=(|c_u|^2-|c_d|^2)^2",
            "feeds_boundary": h6f_boundary["boundary_functor"]["tree_boundary"],
            "boundary_rewrite": "lambda_H(mu_match)=((g_2^2+g_Y^2)/8)*(Tr(J_D P_L))^2",
        },
        "formal_checks": {
            "does_not_require_full_beta_angle": True,
            "phase_invariant_under_cu_cd_rephasing": True,
            "only_uses_rank_one_light_line": True,
            "emits_exact_s_beta_if_selected_P_L_is_emitted": True,
            "emits_numeric_s_beta_now": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    source_search = {
        "schema": "MTTConstHiggs01H7B1SelectedProjectorSourceSearch.v1",
        "status": "SELECTED_TWO_HIGGS_PROJECTOR_VALUES_NOT_FOUND",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1-SELECTED-PROJECTOR-SOURCE-SEARCH",
        "closed_support": {
            "H7B_minimal_object_is_s_beta": h7b["route_B_projection_invariant_reduction_built"],
            "H7B_route_B_underdetermined": h7b["current_closed_data_underdetermine_route_B"],
            "low_energy_Hu_Hd_projection_closed": q79_single["closed"]["single_higgs_channel_projection"],
            "Hu_maps_to_H": q79_single["higgs_doublet_embedding"]["H_u"] == "H",
            "Hd_maps_to_Hdagger": q79_single["higgs_doublet_embedding"]["H_d"] == "H^dagger",
            "Dterm_boundary_formula_ready": h7b_contract["minimal_payload"]["potential_and_Dterm_convention"]["filled"],
        },
        "open_source_fields_from_q79_certificate": {
            "channel_weights": q79_single["open"]["channel_weights"],
            "family_kinetic_metrics": q79_single["open"]["family_kinetic_metrics"],
            "rg_threshold_matching": q79_single["open"]["rg_threshold_matching"],
            "higgs_mass_and_vev_prediction": q79_single["open"]["higgs_mass_and_vev_prediction"],
        },
        "negative_result": {
            "selected_metric_on_two_Higgs_plane_found": False,
            "selected_rank_one_light_projector_P_L_found": False,
            "selected_coefficients_cu_cd_found": False,
            "selected_s_beta_value_found": False,
            "numeric_lambda_H_derived": False,
        },
        "why_this_is_not_the_old_beta_knob": {
            "target_object": "basis-free projector invariant s_beta=(Tr(J_D P_L))^2",
            "not_a_measured_Higgs_backsolve": True,
            "not_representative_tan_beta_10": True,
            "not_full_angle_parameterization": True,
            "requires_same_branch_selected_projector_source": True,
        },
        "superset_strategy": {
            "straight_way": "D-term boundary route with projector invariant",
            "superset_paths_used": [
                "q79 single-Higgs projection supplies the two channel labels",
                "H7B supplies the minimal invariant target",
                "EW branch supplies the separate boundary/RG requirements",
            ],
            "combined_paths_with_locked_target": True,
            "combined_as_numeric_knobs": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    acceptance = {
        "schema": "MTTConstHiggs01H7B1SelectedProjectorAcceptanceContract.v1",
        "status": "PROJECTOR_ACCEPTANCE_CONTRACT_BUILT_CURRENT_PACKET_FAILS_VALUES_OPEN",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1-SELECTED-PROJECTOR-ACCEPTANCE-CONTRACT",
        "required_before_s_beta_emission": {
            "UV_two_Higgs_plane_basis_labels": {
                "filled": True,
                "source": rel(q79_single_path),
            },
            "Hermitian_metric_on_EH_UV": {
                "filled": False,
                "reason": "q79 currently marks family kinetic metrics/channel weights open.",
            },
            "rank_one_light_line_projector_P_L": {
                "filled": False,
                "reason": "No selected projector weights or light-heavy diagonalization packet is emitted.",
            },
            "basis_invariance_certificate": {
                "filled": False,
                "reason": "Formal functor is invariant, but no selected metric/projector source has been certified.",
            },
            "Dterm_charge_involution_J_D": {
                "filled": True,
                "source": "formal H_u/H_d D-term sign structure",
            },
            "EW_boundary_RG_transport": {
                "filled": ew_b41["decision"]["source_selected_mu_match_closed"]
                and ew_b41["decision"]["source_selected_threshold_vector_closed"]
                and ew_b41["decision"]["precision_RG_threshold_values_closed"],
                "source": rel(ew_b41_path),
            },
        },
        "current_packet_evaluation": {
            "formal_projector_to_sbeta_functor_valid": True,
            "selected_projector_values_filled": False,
            "selected_s_beta_emitted": False,
            "selected_EW_boundary_RG_packet_closed": False,
            "numeric_lambda_H_derived": False,
            "strict_no_knob_Higgs_closure": False,
        },
        "conditional_witness": {
            "if_selected_projector_P_L_emitted_then": [
                "compute cos2beta=Tr(J_D P_L)",
                "compute s_beta=(Tr(J_D P_L))^2",
                "feed H7B2 EW boundary/RG packet to compute lambda_H boundary/transport",
            ],
            "still_forbidden": [
                "choose P_L from measured Higgs mass",
                "choose P_L by minimizing residual to observed lambda_H",
                "promote tan_beta=10 as P_L source",
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstHiggs01H7B1NextWork.v1",
        "status": "NEXT_WORKORDER_H7B1A_SELECTED_TWO_HIGGS_METRIC_OR_PROJECTOR_SOURCE",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1-NEXT",
        "primary_next": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1A-SELECTED-TWO-HIGGS-METRIC-OR-LIGHT-PROJECTOR-SOURCE",
            "task": "Search monad/HYM/section-ring/q79 channel data for a selected Hermitian metric and light-line projector P_L on span(H_u,H_d^dagger).",
        },
        "parallel_next": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B2-SELECTED-EW-BOUNDARY-RG-PACKET",
            "task": "Continue the separate selected gauge boundary, matching scale, and threshold/RG source packet.",
        },
        "paper_insert_section": {
            "label": "CONST-HIGGS-01 / PAPER-INSERT / BETA-FREE-DTERM-PROJECTION-INVARIANT",
            "task": "Add the formula s_beta=(Tr(J_D P_L))^2 to show beta is just a coordinate description of the selected light-line projector.",
        },
    }

    candidate = {
        "candidate": "MTTConstHiggs01H7B1DTermProjectionInvariantFunctor",
        "status": STATUS,
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1-DTERM-PROJECTION-INVARIANT-FUNCTOR",
        "output_packets": {
            "uv_two_higgs_projector_to_sbeta_functor": rel(PROJECTOR_FUNCTOR),
            "selected_projector_source_search": rel(SOURCE_SEARCH),
            "selected_projector_acceptance_contract": rel(ACCEPTANCE),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTHiggs01H7B1DTermProjectionInvariantFunctorTheorem",
            "proved": True,
            "statement": (
                "The H7B D-term invariant can be emitted without selecting a full beta angle. On the UV two-Higgs plane E_H^UV=span(H_u,H_d^dagger), define the D-term involution J_D=diag(1,-1) and let P_L be the selected rank-one projector onto the light Higgs line. Then s_beta=(Tr(J_D P_L))^2, and lambda_H(mu_match)=((g_2^2+g_Y^2)/8)s_beta. Current q79 support closes the H_u/H_d channel labels but leaves channel weights, kinetic metrics, and the light-line projector open, so H7B1 builds the exact functor and acceptance contract while leaving selected values and strict no-knob Higgs closure open."
            ),
        },
        "projector_to_sbeta_functor_built": True,
        "basis_free_s_beta_formula_built": True,
        "full_beta_angle_required": False,
        "selected_metric_on_two_Higgs_plane_found": False,
        "selected_rank_one_light_projector_P_L_found": False,
        "selected_s_beta_value_found": False,
        "selected_EW_boundary_RG_packet_closed": False,
        "new_Higgs_specific_parameters": 0,
        "numeric_lambda_H_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "selected_next_artifact": "MTT_CONST_HIGGS_01_H7B1A_SelectedTwoHiggsMetricOrLightProjectorSource_v1",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_HIGGS_01_H7B1_DTermProjectionInvariantFunctor_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "active_label": candidate["active_label"],
        "projector_to_sbeta_functor_built": True,
        "basis_free_s_beta_formula_built": True,
        "full_beta_angle_required": False,
        "selected_metric_on_two_Higgs_plane_found": False,
        "selected_rank_one_light_projector_P_L_found": False,
        "selected_s_beta_value_found": False,
        "selected_EW_boundary_RG_packet_closed": False,
        "new_Higgs_specific_parameters": 0,
        "numeric_lambda_H_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    note = f"""# MTT CONST HIGGS 01 H7B1 DTerm Projection Invariant Functor v1

Status: `{STATUS}`

Label: `CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1-DTERM-PROJECTION-INVARIANT-FUNCTOR`

## Result

```text
projector-to-s_beta functor built          True
basis-free s_beta formula built            True
full beta angle required                   False
selected two-Higgs metric                  False
selected light-line projector P_L          False
selected s_beta value                      False
numeric lambda_H                           False
strict no-knob Higgs closure               False
```

## Formula

On the UV two-Higgs plane

```text
E_H^UV = span(H_u, H_d^dagger)
J_D = diag(1,-1)
P_L = selected rank-one light-Higgs projector
```

the needed invariant is

```text
s_beta = (Tr(J_D P_L))^2
lambda_H(mu_match)=((g_2^2+g_Y^2)/8) s_beta
```

In orthonormal coordinates this is

```text
s_beta=(|c_u|^2-|c_d|^2)^2
```

so the full angle beta is only a coordinate representation, not the real
source object.

## Current Status

q79 closes the low-energy channel labels `H_u -> H` and `H_d -> H^dagger`,
but its own certificate keeps channel weights and family kinetic metrics open.
Therefore H7B1 builds the exact functor, not a numerical Higgs quartic.

## Next

`CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1A-SELECTED-TWO-HIGGS-METRIC-OR-LIGHT-PROJECTOR-SOURCE`
"""

    for path, payload in [
        (PROJECTOR_FUNCTOR, projector_functor),
        (SOURCE_SEARCH, source_search),
        (ACCEPTANCE, acceptance),
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
