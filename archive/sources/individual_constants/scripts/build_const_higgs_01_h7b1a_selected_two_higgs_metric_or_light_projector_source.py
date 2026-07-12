"""Build CONST-HIGGS-01 H7B1A selected two-Higgs metric or projector source."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
Q79_REPO = TEXPAPERS / "mtt-q79-proof-repro"
SM_PARITY_REPO = TEXPAPERS / "mtt-sm-parity-closure"
PROTO_REPO = TEXPAPERS / "mtt-protospinor-gr-response-proof"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_higgs_01_h7b1a_selected_two_higgs_metric_or_light_projector_source"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
QUOTIENT_IMPORT = BASE / "single_higgs_quotient_map_import.packet.json"
NEARMISS_TRIAGE = BASE / "projector_source_nearmiss_triage.packet.json"
UNDERDETERMINATION = BASE / "quotient_to_projector_underdetermination_proof.packet.json"
SPLITTING_CONTRACT = BASE / "selected_splitting_or_projector_source_contract.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_HIGGS_01_H7B1A_SelectedTwoHiggsMetricOrLightProjectorSource_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7B1A_QUOTIENT_TO_PROJECTOR_UNDERDETERMINED_SPLITTING_SOURCE_OPEN"


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

    h7b1_path = DATA / "const_higgs_01_h7b1_dterm_projection_invariant_functor.candidate.json"
    h7b1_functor_path = DATA / "const_higgs_01_h7b1_dterm_projection_invariant_functor" / "uv_two_higgs_projector_to_sbeta_functor.packet.json"
    h7b1_contract_path = DATA / "const_higgs_01_h7b1_dterm_projection_invariant_functor" / "selected_projector_acceptance_contract.packet.json"
    q79_single_path = Q79_REPO / "certificates" / "single_higgs_channel_projection_certificate.json"
    q79_weight_protocol_path = Q79_REPO / "certificates" / "selected_channel_weight_extraction_protocol_certificate.json"
    q79_rank_attempt_path = Q79_REPO / "certificates" / "rank_one_lift_operator_attempt_certificate.json"
    sm_transport_path = SM_PARITY_REPO / "candidate_data" / "selected_transport_conjugation_validator_replay.candidate.json"
    proto_transport_path = PROTO_REPO / "candidate_data" / "post_alpha_symbolic_transport_projector_replay.packet.json"

    h7b1 = load(h7b1_path)
    h7b1_functor = load(h7b1_functor_path)
    h7b1_contract = load(h7b1_contract_path)
    q79_single = load(q79_single_path)
    q79_weight_protocol = load(q79_weight_protocol_path)
    q79_rank_attempt = load(q79_rank_attempt_path)
    sm_transport = load(sm_transport_path)
    proto_transport = load(proto_transport_path)

    quotient_import = {
        "schema": "MTTConstHiggs01H7B1ASingleHiggsQuotientMapImport.v1",
        "status": "Q79_SINGLE_HIGGS_QUOTIENT_IMPORTED_NOT_LIGHT_PROJECTOR",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1A-SINGLE-HIGGS-QUOTIENT-MAP-IMPORT",
        "inputs": {
            "H7B1_projector_functor": rel(h7b1_functor_path),
            "q79_single_Higgs_channel_projection": rel(q79_single_path),
        },
        "UV_two_Higgs_plane": h7b1_functor["two_higgs_plane"],
        "q79_low_energy_projection": {
            "basis": ["H_u", "H_d^dagger"],
            "quotient_map_q": {
                "q(H_u)": "H",
                "q(H_d^dagger)": "H",
                "rank": 1,
                "kernel_generator": "H_u - H_d^dagger",
            },
            "source_statement": q79_single["audited_balances"]["single_higgs_rule"],
            "closed": {
                "basis_channel_labels": q79_single["closed"]["single_higgs_channel_projection"],
                "low_energy_higgs_doublet_embedding": q79_single["closed"]["low_energy_higgs_doublet_embedding"],
                "two_independent_low_energy_Higgs_alignment_references": q79_single["closed"]["two_independent_low_energy_higgs_alignment_references"],
            },
        },
        "classification": {
            "is_low_energy_quotient_or_identification": True,
            "is_selected_Hermitian_projector_on_UV_two_Higgs_plane": False,
            "selects_horizontal_lift_or_splitting": False,
            "emits_s_beta": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    nearmiss_triage = {
        "schema": "MTTConstHiggs01H7B1AProjectorSourceNearmissTriage.v1",
        "status": "NEARMISSES_CLASSIFIED_NO_SELECTED_TWO_HIGGS_PROJECTOR_SOURCE",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1A-PROJECTOR-SOURCE-NEARMISS-TRIAGE",
        "candidate_sources": [
            {
                "id": "q79_single_higgs_projection",
                "source": rel(q79_single_path),
                "what_it_closes": "low-energy H_u/H_d channel quotient",
                "why_rejected_for_P_L": "does not select a UV Hermitian metric, horizontal lift, splitting, or rank-one light-line projector",
                "accepted_as_H7B1A_source": False,
            },
            {
                "id": "q79_channel_weight_protocol",
                "source": rel(q79_weight_protocol_path),
                "what_it_closes": "finite no-proxy channel-weight protocol and allowed sources",
                "why_rejected_for_P_L": "explicitly leaves numerical A_gamma, S_gamma, family kinetic metrics, and RG matching open",
                "accepted_as_H7B1A_source": False,
            },
            {
                "id": "q79_rank_one_lift_operator_attempt",
                "source": rel(q79_rank_attempt_path),
                "what_it_closes": "rank/CP algebraic gates and finite selected-data checklist",
                "why_rejected_for_P_L": "family_kinetic_metrics and channel_weights are null/open, and Higgs VEV/mass prediction remains open",
                "accepted_as_H7B1A_source": False,
            },
            {
                "id": "sm_parity_transport_projectors",
                "source": rel(sm_transport_path),
                "what_it_closes": "sector projector/Riesz/Green symbolic transport for Q,u,d,L,e,N,H sectors",
                "why_rejected_for_P_L": "P_L there denotes the lepton-sector projector, not the UV two-Higgs light-line projector",
                "accepted_as_H7B1A_source": False,
            },
            {
                "id": "protospinor_symbolic_transport_projectors",
                "source": rel(proto_transport_path),
                "what_it_closes": "stationary sector projector replay under symbolic transport",
                "why_rejected_for_P_L": "again P_L is sector-L projector; the H sector is rank-one but not a selected UV two-Higgs splitting",
                "accepted_as_H7B1A_source": False,
            },
        ],
        "source_name_collision_guardrail": {
            "P_L_symbol_collision_detected": True,
            "H7B1A_P_L_meaning": "rank-one light-Higgs projector on span(H_u,H_d^dagger)",
            "other_repo_P_L_meaning": "sector-L/lepton projector under transport",
            "collision_promoted": False,
        },
        "open_fields_confirmed": {
            "q79_channel_weights_open": q79_single["open"]["channel_weights"],
            "q79_family_kinetic_metrics_open": q79_single["open"]["family_kinetic_metrics"],
            "weight_protocol_numerical_A_gamma_open": q79_weight_protocol["open"]["numerical_A_gamma"],
            "weight_protocol_family_kinetic_metrics_open": q79_weight_protocol["open"]["family_kinetic_metrics"],
            "rank_attempt_channel_weights_null": q79_rank_attempt["required_selected_data"]["channel_weights"] is None,
            "rank_attempt_family_kinetic_metrics_null": q79_rank_attempt["required_selected_data"]["family_kinetic_metrics"] is None,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    underdetermination = {
        "schema": "MTTConstHiggs01H7B1AQuotientToProjectorUnderdeterminationProof.v1",
        "status": "SINGLE_HIGGS_QUOTIENT_UNDERDETERMINES_LIGHT_PROJECTOR_AND_SBETA",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1A-QUOTIENT-TO-PROJECTOR-UNDERDETERMINATION-PROOF",
        "setup": {
            "basis": ["e_u=H_u", "e_d=H_d^dagger"],
            "quotient_map": "q(e_u)=H, q(e_d)=H",
            "Dterm_involution": "J_D=diag(1,-1)",
            "projector_invariant": "s_beta=(Tr(J_D P_L))^2",
        },
        "two_witness_light_lines_same_quotient_different_s_beta": [
            {
                "name": "up_axis_line",
                "unit_vector": [1, 0],
                "projector": [[1, 0], [0, 0]],
                "q_image": "H",
                "s_beta": 1,
            },
            {
                "name": "diagonal_line",
                "unit_vector": ["1/sqrt(2)", "1/sqrt(2)"],
                "projector": [["1/2", "1/2"], ["1/2", "1/2"]],
                "q_image": "sqrt(2) H",
                "s_beta": 0,
            },
        ],
        "family_statement": {
            "unit_vector": "c=(c_u,c_d), |c_u|^2+|c_d|^2=1",
            "quotient_image": "q(c)=(c_u+c_d)H",
            "same_low_energy_channel_when": "c_u+c_d != 0, up to low-energy normalization",
            "s_beta": "(|c_u|^2-|c_d|^2)^2",
            "range": "0 <= s_beta <= 1",
        },
        "proof_result": {
            "single_Higgs_projection_determines_channel_labels": True,
            "single_Higgs_projection_determines_light_line_projector": False,
            "single_Higgs_projection_determines_s_beta": False,
            "selected_metric_or_splitting_required": True,
            "numeric_lambda_H_derived": False,
            "strict_no_knob_Higgs_closure": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    splitting_contract = {
        "schema": "MTTConstHiggs01H7B1ASelectedSplittingOrProjectorSourceContract.v1",
        "status": "SELECTED_SPLITTING_PROJECTOR_CONTRACT_BUILT_CURRENT_PACKET_FAILS",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1A-SELECTED-SPLITTING-OR-PROJECTOR-SOURCE-CONTRACT",
        "exact_sequence": "0 -> Ker(q)=span(H_u-H_d^dagger) -> E_H^UV -> span(H) -> 0",
        "accepted_equivalent_payloads": {
            "selected_horizontal_lift": {
                "object": "sigma: span(H) -> E_H^UV with q sigma = id",
                "filled": False,
            },
            "selected_rank_one_projector": {
                "object": "P_L on E_H^UV with image complementary to Ker(q)",
                "filled": False,
            },
            "selected_Hermitian_metric_plus_minimal_lift_rule": {
                "object": "G_H^UV plus rule choosing the G-orthogonal or action-minimizing lift",
                "filled": False,
            },
            "selected_two_Higgs_mass_or_strain_matrix": {
                "object": "a source-side 2x2 operator whose light eigenline is P_L",
                "filled": False,
            },
            "direct_selected_s_beta": {
                "object": "same-branch source emits s_beta=(Tr(J_D P_L))^2",
                "filled": False,
            },
        },
        "current_filled_fields": {
            "quotient_map_q": True,
            "Dterm_involution_J_D": h7b1_contract["required_before_s_beta_emission"]["Dterm_charge_involution_J_D"]["filled"],
            "projector_to_sbeta_functor": h7b1["projector_to_sbeta_functor_built"],
            "source_guardrail": True,
        },
        "current_packet_evaluation": {
            "selected_projector_source_found": False,
            "selected_splitting_source_found": False,
            "selected_s_beta_emitted": False,
            "selected_EW_boundary_RG_packet_closed": False,
            "numeric_lambda_H_derived": False,
            "strict_no_knob_Higgs_closure": False,
        },
        "forbidden_promotions": [
            "quotient map q alone -> P_L",
            "sector-L projector symbol P_L -> Higgs light-line projector",
            "tan_beta=10 representative -> selected P_L",
            "measured Higgs mass/lambda -> selected P_L",
            "threshold residual scan -> selected P_L",
        ],
        "superset_use": {
            "straight_way": "exact sequence splitting for the UV two-Higgs plane",
            "superset_paths_used_for_exclusion": [
                "q79 quotient map",
                "q79 channel-weight/kinetic-metric protocols",
                "SM-parity/protospinor symbolic transport projectors",
            ],
            "combined_paths_with_locked_target": True,
            "combined_as_numeric_knobs": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstHiggs01H7B1ANextWork.v1",
        "status": "NEXT_WORKORDER_H7B1B_SELECTED_SPLITTING_SOURCE_OR_H7B2_EW_BOUNDARY",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1A-NEXT",
        "primary_next": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1B-SELECTED-TWO-HIGGS-SPLITTING-SOURCE",
            "task": "Search monad/HYM/section-ring and q79 channel-weight data for a selected horizontal lift, Hermitian metric plus minimal-lift rule, or two-Higgs mass/strain matrix that emits P_L.",
        },
        "parallel_next": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B2-SELECTED-EW-BOUNDARY-RG-PACKET",
            "task": "Continue the separate selected gauge boundary, matching scale, and threshold/RG source packet.",
        },
        "paper_insert_section": {
            "label": "CONST-HIGGS-01 / PAPER-INSERT / SINGLE-HIGGS-QUOTIENT-VS-LIGHT-LINE-SPLITTING",
            "task": "Explain why H_u -> H and H_d^dagger -> H is a quotient map and cannot determine s_beta without a selected splitting.",
        },
    }

    candidate = {
        "candidate": "MTTConstHiggs01H7B1ASelectedTwoHiggsMetricOrLightProjectorSource",
        "status": STATUS,
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1A-SELECTED-TWO-HIGGS-METRIC-OR-LIGHT-PROJECTOR-SOURCE",
        "output_packets": {
            "single_higgs_quotient_map_import": rel(QUOTIENT_IMPORT),
            "projector_source_nearmiss_triage": rel(NEARMISS_TRIAGE),
            "quotient_to_projector_underdetermination_proof": rel(UNDERDETERMINATION),
            "selected_splitting_or_projector_source_contract": rel(SPLITTING_CONTRACT),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTHiggs01H7B1AQuotientDoesNotSelectProjectorTheorem",
            "proved": True,
            "statement": (
                "The q79 single-Higgs projection is a low-energy quotient q:E_H^UV -> span(H) with q(H_u)=H and q(H_d^dagger)=H. It fixes the channel labels but not a Hermitian metric, horizontal splitting, or rank-one light-line projector P_L on E_H^UV. Indeed P_u=diag(1,0) and P_+=(1/2)[[1,1],[1,1]] both map to the same low-energy Higgs channel while giving s_beta=1 and s_beta=0 respectively. Therefore H7B1A proves that current closed data underdetermine P_L and s_beta; strict closure requires a selected splitting/projector source or a direct selected s_beta source, plus the separate EW boundary/RG packet."
            ),
        },
        "single_Higgs_quotient_imported": True,
        "quotient_to_projector_underdetermination_proved": True,
        "selected_metric_on_two_Higgs_plane_found": False,
        "selected_rank_one_light_projector_P_L_found": False,
        "selected_splitting_source_found": False,
        "selected_s_beta_value_found": False,
        "selected_EW_boundary_RG_packet_closed": False,
        "new_Higgs_specific_parameters": 0,
        "numeric_lambda_H_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "selected_next_artifact": "MTT_CONST_HIGGS_01_H7B1B_SelectedTwoHiggsSplittingSource_or_H7B2_SelectedEWBoundaryRGPacket_v1",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_HIGGS_01_H7B1A_SelectedTwoHiggsMetricOrLightProjectorSource_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "active_label": candidate["active_label"],
        "single_Higgs_quotient_imported": True,
        "quotient_to_projector_underdetermination_proved": True,
        "selected_metric_on_two_Higgs_plane_found": False,
        "selected_rank_one_light_projector_P_L_found": False,
        "selected_splitting_source_found": False,
        "selected_s_beta_value_found": False,
        "selected_EW_boundary_RG_packet_closed": False,
        "new_Higgs_specific_parameters": 0,
        "numeric_lambda_H_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    note = f"""# MTT CONST HIGGS 01 H7B1A Selected Two-Higgs Metric Or Light Projector Source v1

Status: `{STATUS}`

Label: `CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1A-SELECTED-TWO-HIGGS-METRIC-OR-LIGHT-PROJECTOR-SOURCE`

## Result

```text
single-Higgs quotient imported              True
quotient -> projector underdetermination    True
selected two-Higgs metric                   False
selected light-line projector P_L           False
selected splitting source                   False
selected s_beta value                       False
numeric lambda_H                            False
strict no-knob Higgs closure                False
```

## The Point

q79 gives the low-energy quotient

```text
q(H_u)=H
q(H_d^dagger)=H
Ker(q)=span(H_u-H_d^dagger)
```

This is not the same thing as selecting the UV light line.

## Counterexample

Both of these lines map to the same low-energy Higgs channel:

```text
P_u   = [[1,0],[0,0]]             -> s_beta = 1
P_+   = (1/2)[[1,1],[1,1]]        -> s_beta = 0
```

So `H_u -> H` and `H_d^dagger -> H` do not determine

```text
s_beta=(Tr(J_D P_L))^2.
```

## Needed Source

One of these equivalent payloads must be selected before Higgs comparison:

```text
selected horizontal lift sigma with q sigma = id
selected rank-one projector P_L
selected Hermitian metric plus minimal-lift rule
selected two-Higgs mass/strain matrix whose light eigenline is P_L
direct selected s_beta
```

## Next

`CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1B-SELECTED-TWO-HIGGS-SPLITTING-SOURCE`
"""

    for path, payload in [
        (QUOTIENT_IMPORT, quotient_import),
        (NEARMISS_TRIAGE, nearmiss_triage),
        (UNDERDETERMINATION, underdetermination),
        (SPLITTING_CONTRACT, splitting_contract),
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
