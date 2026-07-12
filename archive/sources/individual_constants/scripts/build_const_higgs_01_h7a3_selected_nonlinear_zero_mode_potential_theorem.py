"""Build CONST-HIGGS-01 H7A3 selected nonlinear zero-mode potential theorem attempt."""

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

SLUG = "const_higgs_01_h7a3_selected_nonlinear_zero_mode_potential_theorem"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SEARCH = BASE / "selected_zero_mode_potential_search.packet.json"
UNDERDETERMINATION = BASE / "analytic_zero_mode_potential_underdetermination_proof.packet.json"
ROUTE_DECISION = BASE / "route_a_decision_after_h7a3.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_HIGGS_01_H7A3_SelectedNonlinearZeroModePotentialTheorem_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7A3_ZERO_MODE_POTENTIAL_UNDERDETERMINED_ROUTEA_PARKED"


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

    h7a2_path = DATA / "const_higgs_01_h7a2_selected_nonlinear_higgs_source_kernel.candidate.json"
    h7a2_contract_path = DATA / "const_higgs_01_h7a2_selected_nonlinear_higgs_source_kernel" / "selected_nonlinear_kernel_acceptance_contract.packet.json"
    h7a2_obstruction_path = DATA / "const_higgs_01_h7a2_selected_nonlinear_higgs_source_kernel" / "zero_mode_spectral_determinant_obstruction.packet.json"
    h7a_support_path = DATA / "const_higgs_01_h7a_intrinsic_k4_row_execution_payload" / "same_source_trace_and_h_projector_support_import.packet.json"
    h5b_projection_path = DATA / "const_higgs_01_h5b_selected_higgs_nonlinear_amplitude_projection" / "nonlinear_amplitude_projection_contract.packet.json"
    h3_path = DATA / "const_higgs_01_h3_selected_higgs_quadratic_stiffness_and_quartic_gate" / "selected_quadratic_stiffness_kernel.packet.json"
    sm_measured_replay_path = SM_PARITY_REPO / "candidate_data" / "sm_equivalence_measured_replay_admission.candidate.json"
    sm_common_scale_path = SM_PARITY_REPO / "candidate_data" / "sm_equivalence_commonscale_value_transport_and_final_packet_certificate.candidate.json"

    h7a2 = load(h7a2_path)
    h7a2_contract = load(h7a2_contract_path)
    h7a2_obstruction = load(h7a2_obstruction_path)
    h7a_support = load(h7a_support_path)
    h5b_projection = load(h5b_projection_path)
    h3 = load(h3_path)
    sm_measured_replay = load(sm_measured_replay_path)
    sm_common_scale = load(sm_common_scale_path)

    row_address = h5b_projection["projection_functional"]["quartic_row_address"]
    coordinate_index = h5b_projection["projection_functional"]["coordinate_index"]
    basis_id = h7a_support["imported_same_source_support"]["basis_id"]
    zero_cluster = h3["selected_source_kernel"]["zero_cluster_indices"]

    search = {
        "schema": "MTTConstHiggs01H7A3SelectedZeroModePotentialSearch.v1",
        "status": "NO_SELECTED_ANALYTIC_ZERO_MODE_POTENTIAL_PACKET_FOUND",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7A3-SELECTED-ZERO-MODE-POTENTIAL-SEARCH",
        "inputs": {
            "H7A2_nonlinear_kernel_gate": rel(h7a2_path),
            "H7A2_acceptance_contract": rel(h7a2_contract_path),
            "H7A2_spectral_obstruction": rel(h7a2_obstruction_path),
            "H7A_same_source_support": rel(h7a_support_path),
            "H5B_projection_contract": rel(h5b_projection_path),
            "H3_quadratic_stiffness_kernel": rel(h3_path),
            "SM_parity_measured_replay_admission": rel(sm_measured_replay_path),
            "SM_parity_common_scale_values": rel(sm_common_scale_path),
        },
        "searched_candidate_classes": {
            "selected_DE_gap_layer": {
                "found": True,
                "accepted_as_Veff": False,
                "reason": "Quadratic/gap-layer support only; H7A already proves it cannot emit K4.",
            },
            "finite_heat_or_logdet_spectral_action": {
                "found": True,
                "accepted_as_Veff": False,
                "reason": "H7A2 proves positive-complement/zero-mode nonanalytic obstruction.",
            },
            "selected_HYM_expS_nonlinear_replay": {
                "found": True,
                "accepted_as_Veff": False,
                "reason": "Connection/metric nonlinear replay support, not an analytic scalar zero-mode potential for a_H.",
            },
            "fixed_point_effective_potential_language": {
                "found": True,
                "accepted_as_Veff": False,
                "reason": "Corpus-level effective-potential language is not a selected q79/F,m=1 finite zero-mode functional with row/exactness certificate.",
            },
            "SM_measured_lambda_or_Higgs_mass": {
                "found": sm_measured_replay["what_closes_now"]["measured_Yukawa_CKM_PMNS_Higgs_slots_admitted_downstream"],
                "accepted_as_Veff": False,
                "reason": "Measured Higgs slots are downstream SM-parity inputs; using them would select by target.",
            },
            "SM_common_scale_lambda_replay": {
                "found": "lambda_H_tree_native" in sm_common_scale["common_scale_packet"]["native_values_carried_but_not_common_scale"],
                "accepted_as_Veff": False,
                "reason": "Native lambda replay exists, while common-scale Higgs transport remains open; neither is a no-knob source selection.",
            },
        },
        "selected_analytic_zero_mode_potential_found": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    underdetermination = {
        "schema": "MTTConstHiggs01H7A3AnalyticZeroModePotentialUnderdeterminationProof.v1",
        "status": "CURRENT_CLOSED_DATA_DO_NOT_DETERMINE_K4",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7A3-ANALYTIC-ZERO-MODE-POTENTIAL-UNDERDETERMINATION",
        "closed_data_held_fixed": {
            "basis_id": basis_id,
            "Higgs_coordinate_index": coordinate_index,
            "zero_cluster_indices": zero_cluster,
            "quartic_row_address": row_address,
            "same_source_trace_and_H_projector_support": h7a_support["imported_same_source_support"]["selected_trace_equality_proved_for_D_E_gap_layer"],
            "spectral_determinant_obstruction_proved": h7a2["zero_mode_spectral_determinant_obstruction_proved"],
            "nonlinear_kernel_acceptance_contract_ready": h7a2["nonlinear_kernel_acceptance_contract_ready"],
        },
        "countermodel_family": {
            "description": "For any real c, V_c(a_H)=V_closed_support + c*a_H^4/24 is analytic and preserves all currently closed projector, gap-layer, positive-complement heat/logdet, and no-observed-selector fields because no current selected source constrains c.",
            "V_0": {
                "quartic_coefficient_c": 0,
                "K_H_4_row": 0,
                "agrees_with_closed_data": True,
            },
            "V_1": {
                "quartic_coefficient_c": 1,
                "K_H_4_row": 1,
                "agrees_with_closed_data": True,
            },
            "same_closed_data_different_K4": True,
        },
        "logical_consequence": {
            "K4_unique_from_current_closed_data": False,
            "K4_theorem_derived_now": False,
            "requires_extra_selected_source_rule": True,
            "extra_rule_name": h7a2_contract["required_source_theorem"]["name"],
        },
        "guardrail": {
            "does_not_deny_future_zero_mode_potential_theorem": True,
            "denies_only_current_derivation_from_existing_closed_packets": True,
            "no_measured_lambda_or_mass_used": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    route_decision = {
        "schema": "MTTConstHiggs01H7A3RouteADecision.v1",
        "status": "ROUTE_A_PARKED_PENDING_NEW_SELECTED_ZERO_MODE_POTENTIAL_THEOREM",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7A3-ROUTE-A-DECISION",
        "route_A_status": {
            "same_source_projector_support": True,
            "intrinsic_K4_row_address_ready": True,
            "quadratic_gap_false_route_closed": True,
            "zero_mode_logdet_false_route_closed": True,
            "selected_analytic_zero_mode_potential_found": False,
            "current_K4_derivation_underdetermined": True,
            "route_A_strict_closure": False,
        },
        "decision": {
            "park_route_A_as_active_waiting_for_new_source_theorem": True,
            "promote_route_B_as_near_term_primary": True,
            "route_B_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B-UV-BETA-OR-TWO-HIGGS-PROJECTION-THEOREM",
            "reason": "Route A now needs genuinely new source content, while Route B has a concrete D-term boundary formula and needs selected beta/gauge/RG inputs.",
        },
        "superset_strategy": {
            "straight_path_currently_exhausted": "Route A intrinsic K4 from existing finite gap/logdet/H-projector packets",
            "parallel_path_to_continue": "Route B selected UV beta/two-Higgs projection",
            "paths_combined_as_free_parameters": False,
            "universal_primitive_still_separate": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstHiggs01H7A3NextWork.v1",
        "status": "NEXT_WORKORDER_H7B_UV_BETA_OR_TWO_HIGGS_PROJECTION",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7A3-NEXT",
        "primary_next": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B-UV-BETA-OR-TWO-HIGGS-PROJECTION-THEOREM",
            "task": "Search for or construct a selected UV beta/tan_beta, two-Higgs projection angle, or heavy-Higgs decoupling theorem for the D-term boundary route.",
        },
        "parked_route_A_resume_condition": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7A4-NEW-ZERO-MODE-POTENTIAL-SOURCE-RULE",
            "task": "Resume Route A only if a new selected analytic zero-mode potential source rule is found.",
        },
        "paper_insert_section": {
            "label": "CONST-HIGGS-01 / PAPER-INSERT / ROUTE-A-UNDERDETERMINATION",
            "task": "Add the countermodel family V_c(a_H) to explain why current closed data cannot determine K_H^(4).",
        },
    }

    candidate = {
        "candidate": "MTTConstHiggs01H7A3SelectedNonlinearZeroModePotentialTheorem",
        "status": STATUS,
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7A3-SELECTED-NONLINEAR-ZERO-MODE-POTENTIAL-THEOREM",
        "output_packets": {
            "selected_zero_mode_potential_search": rel(SEARCH),
            "analytic_zero_mode_potential_underdetermination_proof": rel(UNDERDETERMINATION),
            "route_a_decision_after_h7a3": rel(ROUTE_DECISION),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTHiggs01H7A3RouteAUnderdeterminationTheorem",
            "proved": True,
            "statement": (
                "No current corpus or repo packet emits a selected analytic q79/F,m=1 zero-mode potential V_eff(a_H). More strongly, the current closed data underdetermine K_H^(4): for any real c, V_c(a_H)=V_closed_support+c a_H^4/24 preserves the closed projector, D_E gap-layer, positive-complement heat/logdet, and selector-guardrail data while changing K_H^(4)[12,12,12,12]=c. Therefore Route A cannot derive a unique Higgs quartic from current material; it is parked pending a new selected zero-mode potential source theorem, and Route B becomes the near-term primary strict route."
            ),
        },
        "selected_analytic_zero_mode_potential_found": False,
        "current_closed_data_underdetermine_K4": True,
        "route_A_parked_pending_new_source_theorem": True,
        "route_B_promoted_as_near_term_primary": True,
        "same_source_H_sector_fourth_variation_row_emitted": False,
        "numeric_lambda_H_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "new_Higgs_specific_parameters": 0,
        "selected_next_artifact": "MTT_CONST_HIGGS_01_H7B_UVBetaOrTwoHiggsProjectionTheorem_v1",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_HIGGS_01_H7A3_SelectedNonlinearZeroModePotentialTheorem_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "active_label": candidate["active_label"],
        "selected_analytic_zero_mode_potential_found": False,
        "current_closed_data_underdetermine_K4": True,
        "route_A_parked_pending_new_source_theorem": True,
        "route_B_promoted_as_near_term_primary": True,
        "same_source_H_sector_fourth_variation_row_emitted": False,
        "numeric_lambda_H_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "new_Higgs_specific_parameters": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    note = f"""# MTT CONST HIGGS 01 H7A3 Selected Nonlinear Zero-Mode Potential Theorem v1

Status: `{STATUS}`

Label: `CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7A3-SELECTED-NONLINEAR-ZERO-MODE-POTENTIAL-THEOREM`

## Result

```text
selected analytic zero-mode potential found      False
current closed data underdetermine K4            True
Route A parked pending new source theorem        True
Route B promoted near-term primary               True
K_H^(4)[12,12,12,12] emitted                     False
numeric lambda_H                                 False
strict no-knob Higgs closure                     False
```

## Underdetermination

The current closed data fix the H-sector projector, selected coordinate `[12]`,
quadratic/gap-layer data, and positive-complement heat/logdet response.  They
do not fix an analytic zero-mode quartic coefficient.

```text
V_c(a_H) = V_closed_support + c a_H^4 / 24
K_H^(4)[12,12,12,12] = c
```

Different `c` values preserve all currently closed packets.  So Route A needs
new source content, not more replay of the same quadratic/logdet material.

## Next

`CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B-UV-BETA-OR-TWO-HIGGS-PROJECTION-THEOREM`
"""

    for path, payload in [
        (SEARCH, search),
        (UNDERDETERMINATION, underdetermination),
        (ROUTE_DECISION, route_decision),
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
