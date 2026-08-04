"""Build CONST-HIGGS-01 H7B UV beta or two-Higgs projection theorem."""

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

SLUG = "const_higgs_01_h7b_uv_beta_or_two_higgs_projection_theorem"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
EXTERNAL_REF = BASE / "external_susy_eft_boundary_reference.packet.json"
SOURCE_SEARCH = BASE / "selected_route_b_source_search.packet.json"
UNDERDETERMINATION = BASE / "projection_invariant_underdetermination_proof.packet.json"
PAYLOAD_CONTRACT = BASE / "minimal_route_b_payload_contract.packet.json"
NEXT_WORK = BASE / "h7b_decision_and_next_work.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_HIGGS_01_H7B_UVBetaOrTwoHiggsProjectionTheorem_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7B_UV_BETA_ROUTE_UNDERDETERMINED_MINIMAL_PAYLOAD_BUILT"


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

    h7_path = DATA / "const_higgs_01_h7_intrinsic_hsector_k4_row_or_uv_beta_theorem.candidate.json"
    h7_validator_path = DATA / "const_higgs_01_h7_intrinsic_hsector_k4_row_or_uv_beta_theorem" / "strict_higgs_closure_acceptance_validator.packet.json"
    h7a3_path = DATA / "const_higgs_01_h7a3_selected_nonlinear_zero_mode_potential_theorem.candidate.json"
    h7a3_decision_path = DATA / "const_higgs_01_h7a3_selected_nonlinear_zero_mode_potential_theorem" / "route_a_decision_after_h7a3.packet.json"
    h6d_contract_path = DATA / "const_higgs_01_h6d_selected_dterm_boundary_or_beta_source" / "dterm_boundary_acceptance_contract.packet.json"
    h6e_uv_audit_path = DATA / "const_higgs_01_h6e_uv_two_higgs_projection_angle_or_primitive_beta_policy" / "uv_two_higgs_projection_angle_source_audit.packet.json"
    h6e_policy_path = DATA / "const_higgs_01_h6e_uv_two_higgs_projection_angle_or_primitive_beta_policy" / "primitive_beta_policy.packet.json"
    h6f_boundary_path = DATA / "const_higgs_01_h6f_symbolic_dterm_boundary_replay" / "symbolic_boundary_replay_functor.packet.json"
    h6f_rg_path = DATA / "const_higgs_01_h6f_symbolic_dterm_boundary_replay" / "higgs_rg_transport_contract.packet.json"
    h6f_gate_path = DATA / "const_higgs_01_h6f_symbolic_dterm_boundary_replay" / "source_input_gate_ledger.packet.json"
    h6f_superset_path = DATA / "const_higgs_01_h6f_symbolic_dterm_boundary_replay" / "superset_path_map.packet.json"
    ew_b41_path = DATA / "const_ew_02_weak_mixing_b41_gauge_action_rg_matching" / "rg_matching_threshold_scheme_status.packet.json"
    ew_b43_path = DATA / "const_ew_02_weak_mixing_b43_threshold_vector_or_minimal_policy" / "minimal_threshold_replay_policy.packet.json"
    ew_b44_path = DATA / "const_ew_02_weak_mixing_b44_conditional_profile_execution" / "conditional_profile_execution.packet.json"
    q79_single_path = Q79_REPO / "certificates" / "single_higgs_channel_projection_certificate.json"

    h7 = load(h7_path)
    h7_validator = load(h7_validator_path)
    h7a3 = load(h7a3_path)
    h7a3_decision = load(h7a3_decision_path)
    h6d_contract = load(h6d_contract_path)
    h6e_uv_audit = load(h6e_uv_audit_path)
    h6e_policy = load(h6e_policy_path)
    h6f_boundary = load(h6f_boundary_path)
    h6f_rg = load(h6f_rg_path)
    h6f_gate = load(h6f_gate_path)
    h6f_superset = load(h6f_superset_path)
    ew_b41 = load(ew_b41_path)
    ew_b43 = load(ew_b43_path)
    ew_b44 = load(ew_b44_path)
    q79_single = load(q79_single_path)

    boundary_formula = h6f_boundary["boundary_functor"]["tree_boundary"]
    potential_convention = h6f_boundary["boundary_functor"]["potential_convention"]

    external_ref = {
        "schema": "MTTConstHiggs01H7BExternalSUSYEFTBoundaryReference.v1",
        "status": "EXTERNAL_SUSY_EFT_REFERENCES_IMPORTED_AS_GUARDRAILS_NOT_SELECTORS",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B-EXTERNAL-SUSY-EFT-BOUNDARY-REFERENCE",
        "references": [
            {
                "source": "Giudice and Strumia, Probing High-Scale and Split Supersymmetry with Higgs Mass Measurements, arXiv:1108.6077",
                "url": "https://arxiv.org/abs/1108.6077",
                "imported_use": "Confirms that high-scale/split SUSY Higgs predictions use a Higgs-quartic matching condition and require RG and threshold treatment.",
                "value_imported": False,
                "counts_as_MTT_source_selector": False,
            },
            {
                "source": "Bahl et al., Higgs-mass predictions in the MSSM and beyond, EPJC 81, 2021",
                "url": "https://link.springer.com/article/10.1140/epjc/s10052-021-09198-2",
                "imported_use": "Confirms that precision SUSY Higgs predictions are scheme, scale, threshold, spectrum, and uncertainty-policy dependent.",
                "value_imported": False,
                "counts_as_MTT_source_selector": False,
            },
        ],
        "guardrail_result": {
            "standard_boundary_formula_supported_as_methodology": True,
            "numeric_lambda_or_beta_imported": False,
            "external_phenomenology_allowed_to_select_MTT_branch": False,
            "threshold_and_scheme_policy_required_before_precision_claim": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    source_search = {
        "schema": "MTTConstHiggs01H7BSelectedRouteBSourceSearch.v1",
        "status": "NO_SELECTED_ROUTE_B_PROJECTION_INVARIANT_SOURCE_FOUND",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B-SELECTED-ROUTE-B-SOURCE-SEARCH",
        "inputs": {
            "H7_two_exit_frontier": rel(h7_path),
            "H7A3_route_A_decision": rel(h7a3_decision_path),
            "H6D_Dterm_contract": rel(h6d_contract_path),
            "H6E_UV_beta_source_audit": rel(h6e_uv_audit_path),
            "H6F_symbolic_boundary": rel(h6f_boundary_path),
            "EW_B41_RG_matching_scaffold": rel(ew_b41_path),
            "EW_B43_minimal_threshold_policy": rel(ew_b43_path),
            "EW_B44_conditional_profile_execution": rel(ew_b44_path),
            "q79_single_Higgs_projection": rel(q79_single_path),
            "external_SUSY_EFT_reference": rel(EXTERNAL_REF),
        },
        "closed_support": {
            "route_A_parked_pending_new_source": h7a3["route_A_parked_pending_new_source_theorem"],
            "route_B_promoted_as_near_term_primary": h7a3["route_B_promoted_as_near_term_primary"],
            "low_energy_single_Higgs_projection_closed": q79_single["closed"]["single_higgs_channel_projection"],
            "H_u_to_H": q79_single["higgs_doublet_embedding"]["H_u"] == "H",
            "H_d_to_Hdagger": q79_single["higgs_doublet_embedding"]["H_d"] == "H^dagger",
            "Dterm_boundary_formula_ready": h7["route_B_UV_beta_exit_closed"] is False and h6d_contract["current_filled_fields"]["correct_formula_factor"],
            "symbolic_boundary_functor_defined": h6f_boundary["output_status"]["symbolic_boundary_defined"],
            "tree_boundary": boundary_formula,
            "potential_convention": potential_convention,
        },
        "candidate_source_lanes": [
            {
                "id": "selected_two_Higgs_geometry_or_decoupling_metric",
                "minimal_object": "s_beta = cos^2(2 beta)",
                "accepted_as_source_now": False,
                "reason": "No current corpus/repo packet emits a selected UV two-Higgs metric, VEV ratio, decoupling angle, or equivalent projection invariant.",
            },
            {
                "id": "q79_single_Higgs_projection",
                "minimal_object": "H_u -> H, H_d -> H^dagger",
                "accepted_as_source_now": False,
                "reason": "It fixes the low-energy channel but deliberately discards the UV two-Higgs angle.",
            },
            {
                "id": "Theta_representative_tan_beta_10",
                "minimal_object": "tan_beta = 10",
                "accepted_as_source_now": False,
                "reason": "Earlier gates classify it as representative diagnostic text, not a selected MTT source.",
            },
            {
                "id": "EW_B44_conditional_weak_angle_profile",
                "minimal_object": "conditional electroweak profile data",
                "accepted_as_source_now": False,
                "reason": "It is a conditional weak-mixing replay profile; it does not emit the Higgs two-Higgs projection invariant.",
            },
            {
                "id": "external_SUSY_EFT_boundary_literature",
                "minimal_object": "SUSY matching methodology",
                "accepted_as_source_now": False,
                "reason": "It validates the type of boundary condition and required precision policy, but it is not an MTT branch selector.",
            },
            {
                "id": "explicit_beta_primitive_policy",
                "minimal_object": h6e_policy["policy"]["primitive_name"],
                "accepted_as_source_now": False,
                "reason": "The policy is admissible only as an explicitly declared non-no-knob tier; no primitive is declared here.",
            },
        ],
        "negative_result": {
            "selected_Dterm_projection_invariant_s_beta_found": False,
            "selected_UV_beta_or_tan_beta_found": False,
            "selected_two_Higgs_projection_angle_found": False,
            "selected_heavy_Higgs_decoupling_angle_found": False,
            "selected_EW_boundary_RG_packet_closed": False,
            "external_methodology_promoted_to_MTT_source": False,
            "beta_primitive_declared_now": h6e_policy["current_decision"]["declare_beta_primitive_now"],
        },
        "superset_strategy": {
            "paths_compared": [
                "q79/NCG single-Higgs channel",
                "Theta representative tan_beta lane",
                "EW weak-mixing conditional profile",
                "external SUSY-EFT matching methodology",
                "explicit primitive portfolio",
            ],
            "locked_target": "same-branch selected s_beta=cos^2(2 beta) or equivalent two-Higgs projection invariant",
            "paths_combined_as_free_parameters": False,
            "best_current_result": "minimal invariant identified; no selected source emits it yet",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    underdetermination = {
        "schema": "MTTConstHiggs01H7BProjectionInvariantUnderdeterminationProof.v1",
        "status": "ROUTE_B_DTERM_BOUNDARY_UNDERDETERMINED_BY_CURRENT_CLOSED_DATA",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B-PROJECTION-INVARIANT-UNDERDETERMINATION-PROOF",
        "fixed_by_current_closed_packets": [
            "low-energy single-Higgs channel H_u -> H, H_d -> H^dagger",
            "standard potential convention V(H)=-m^2|H|^2+lambda|H|^4",
            "tree boundary shape lambda_H(mu_match)=A_EW(mu_match)*s_beta",
            "A_EW=(g_2^2+g_Y^2)/8 as a symbolic gauge factor",
            "selector guardrail: no observed Higgs lambda/mass backsolve",
        ],
        "not_fixed_by_current_closed_packets": [
            "s_beta=cos^2(2 beta) in [0,1]",
            "selected UV beta/tan_beta or two-Higgs metric",
            "selected EW boundary pair (g_2,g_Y) in the same source scheme",
            "selected matching scale mu_match",
            "selected threshold/RG transport",
        ],
        "countermodel_family": {
            "symbolic_gauge_factor": "A_EW=(g_2^2+g_Y^2)/8",
            "free_projection_invariant": "s_beta in [0,1]",
            "family": "lambda_s(mu_match)=A_EW(mu_match)*s_beta",
            "preserves_all_current_closed_route_B_data": True,
            "changes_lambda_boundary_for_distinct_s_beta_when_A_EW_nonzero": True,
            "therefore_unique_lambda_boundary_determined": False,
        },
        "proof_result": {
            "current_closed_data_underdetermine_route_B": True,
            "selected_s_beta_is_minimal_new_Higgs_object": True,
            "full_beta_angle_stronger_than_needed": True,
            "numeric_lambda_H_derived": False,
            "strict_no_knob_Higgs_closure": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    payload_contract = {
        "schema": "MTTConstHiggs01H7BMinimalRouteBPayloadContract.v1",
        "status": "MINIMAL_ROUTE_B_PAYLOAD_CONTRACT_BUILT_CURRENT_PACKET_FAILS",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B-MINIMAL-ROUTE-B-PAYLOAD-CONTRACT",
        "minimal_payload": {
            "potential_and_Dterm_convention": {
                "filled": True,
                "source": rel(h6d_contract_path),
                "object": boundary_formula,
            },
            "low_energy_single_Higgs_projection": {
                "filled": True,
                "source": rel(q79_single_path),
                "object": "H_u -> H, H_d -> H^dagger",
            },
            "selected_Dterm_projection_invariant_s_beta": {
                "filled": False,
                "accepted_forms": [
                    "direct selected s_beta=cos^2(2 beta)",
                    "selected beta/tan_beta with convention",
                    "selected two-Higgs inner-product/VEV-ratio metric",
                    "selected heavy-Higgs decoupling angle implying s_beta",
                ],
            },
            "selected_EW_boundary_pair": {
                "filled": False,
                "source": rel(ew_b41_path),
                "current_status": "gauge/action normalization and physical anchor remain open",
            },
            "selected_matching_scale": {
                "filled": ew_b41["decision"]["source_selected_mu_match_closed"],
                "source": rel(ew_b41_path),
                "current_status": "source-selected mu_match remains open",
            },
            "selected_threshold_RG_transport": {
                "filled": ew_b41["decision"]["source_selected_threshold_vector_closed"]
                and ew_b41["decision"]["precision_RG_threshold_values_closed"],
                "source": rel(ew_b41_path),
                "current_status": "conditional replay exists, strict threshold/RG values remain open",
            },
            "selector_guardrail": {
                "filled": True,
                "forbids": [
                    "observed Higgs mass/lambda backsolve",
                    "threshold residual fit to Higgs target",
                    "tan_beta=10 representative promotion",
                    "external phenomenology as MTT source selector",
                ],
            },
        },
        "current_packet_evaluation": {
            "route_B_UV_Dterm_beta_passes": h7_validator["current_packet_evaluation"]["route_B_UV_Dterm_beta_passes"],
            "minimal_invariant_contract_passes": False,
            "one_primitive_declared_now": h7_validator["current_packet_evaluation"]["one_primitive_declared_now"],
            "numeric_lambda_H_derived": False,
            "strict_no_knob_Higgs_closure": False,
        },
        "conditional_witness": {
            "would_pass_if": [
                "a same-branch selected source emits s_beta or equivalent UV two-Higgs projection data",
                "selected EW boundary pair and RG/threshold policy are emitted without Higgs-target fitting",
            ],
            "would_still_not_be_strict_if": [
                "s_beta is declared as a Higgs-only primitive",
                "s_beta is inferred from measured Higgs mass or low-scale lambda",
            ],
        },
        "superset_use": {
            "straight_way": "D-term boundary route with locked target s_beta",
            "superset_paths_used_for_exclusion": source_search["superset_strategy"]["paths_compared"],
            "combined_paths_with_locked_target": True,
            "combined_as_numeric_knobs": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstHiggs01H7BDecisionAndNextWork.v1",
        "status": "NEXT_WORKORDER_H7B1_SELECTED_DTERM_PROJECTION_INVARIANT_OR_H7B2_EW_BOUNDARY_RG",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B-NEXT",
        "decision": {
            "route_B_minimal_object": "s_beta=cos^2(2 beta)",
            "route_B_underdetermined_now": True,
            "full_beta_angle_required": False,
            "selected_projection_invariant_required": True,
            "EW_boundary_RG_required": True,
            "strict_no_knob_Higgs_closure": False,
        },
        "primary_next": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1-SELECTED-DTERM-PROJECTION-INVARIANT-SOURCE",
            "task": "Search corpus/repos for a same-branch selected two-Higgs metric, VEV-ratio, decoupling-angle, or projection invariant that emits s_beta before Higgs comparison.",
        },
        "parallel_next": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B2-SELECTED-EW-BOUNDARY-RG-PACKET",
            "task": "Promote gauge boundary, mu_match, and threshold/RG policy from conditional replay to selected source packet without Higgs-target fitting.",
        },
        "portfolio_fallback": {
            "label": "CONST-HIGGS-01 / UNIVERSAL-PRIMITIVE-PORTFOLIO / H7P-SHARED-PRIMITIVE-HIGGS-REPLAY",
            "task": "Only after strict route exhaustion, test whether an already-declared shared universal primitive fixes s_beta or EW boundary without adding a Higgs-only knob.",
        },
        "paper_insert_section": {
            "label": "CONST-HIGGS-01 / PAPER-INSERT / ROUTE-B-PROJECTION-INVARIANT-UNDERDETERMINATION",
            "task": "State the family lambda_s=A_EW*s_beta and explain why the route needs selected s_beta plus selected EW transport.",
        },
    }

    candidate = {
        "candidate": "MTTConstHiggs01H7BUVBetaOrTwoHiggsProjectionTheorem",
        "status": STATUS,
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B-UV-BETA-OR-TWO-HIGGS-PROJECTION-THEOREM",
        "output_packets": {
            "external_susy_eft_boundary_reference": rel(EXTERNAL_REF),
            "selected_route_b_source_search": rel(SOURCE_SEARCH),
            "projection_invariant_underdetermination_proof": rel(UNDERDETERMINATION),
            "minimal_route_b_payload_contract": rel(PAYLOAD_CONTRACT),
            "h7b_decision_and_next_work": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTHiggs01H7BProjectionInvariantUnderdeterminationTheorem",
            "proved": True,
            "statement": (
                "Given H6D-H7A3, Route B reduces to a D-term boundary lambda_H(mu_match)=A_EW(mu_match)*s_beta with A_EW=(g_2^2+g_Y^2)/8 and s_beta=cos^2(2 beta). Current packets select the low-energy single-Higgs channel and the boundary formula, but do not select s_beta, EW boundary values, matching scale, or threshold/RG transport. Therefore the family lambda_s=A_EW*s_beta preserves all current closed Route-B data while changing the Higgs boundary value. H7B builds the minimal payload contract and leaves strict no-knob Higgs closure open."
            ),
        },
        "route_B_minimal_payload_contract_built": True,
        "route_B_projection_invariant_reduction_built": True,
        "current_closed_data_underdetermine_route_B": True,
        "selected_Dterm_projection_invariant_s_beta_found": False,
        "selected_UV_beta_or_tan_beta_found": False,
        "selected_EW_boundary_RG_packet_closed": False,
        "external_methodology_promoted_to_MTT_source": False,
        "beta_primitive_declared_now": False,
        "new_Higgs_specific_parameters": 0,
        "numeric_lambda_H_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "selected_next_artifact": "MTT_CONST_HIGGS_01_H7B1_SelectedDTermProjectionInvariantSource_or_H7B2_SelectedEWBoundaryRGPacket_v1",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_HIGGS_01_H7B_UVBetaOrTwoHiggsProjectionTheorem_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "active_label": candidate["active_label"],
        "route_B_minimal_payload_contract_built": True,
        "route_B_projection_invariant_reduction_built": True,
        "current_closed_data_underdetermine_route_B": True,
        "selected_Dterm_projection_invariant_s_beta_found": False,
        "selected_UV_beta_or_tan_beta_found": False,
        "selected_EW_boundary_RG_packet_closed": False,
        "external_methodology_promoted_to_MTT_source": False,
        "beta_primitive_declared_now": False,
        "new_Higgs_specific_parameters": 0,
        "numeric_lambda_H_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    note = f"""# MTT CONST HIGGS 01 H7B UV Beta Or Two-Higgs Projection Theorem v1

Status: `{STATUS}`

Label: `CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B-UV-BETA-OR-TWO-HIGGS-PROJECTION-THEOREM`

## Result

```text
Route B minimal payload contract built       True
projection-invariant reduction built         True
current Route B data underdetermine lambda   True
selected s_beta source                       False
selected UV beta/tan_beta source             False
selected EW boundary/RG packet               False
numeric lambda_H                             False
strict no-knob Higgs closure                 False
```

## Minimal Object

Route B does not need the full angle as the minimal missing object.  It needs
the invariant

```text
s_beta = cos^2(2 beta)
lambda_H(mu_match) = ((g_2^2 + g_Y^2)/8) s_beta
```

Current packets fix the single-Higgs channel and the formula shape, but not
`s_beta`, the selected gauge boundary, matching scale, or threshold/RG
transport.

## Underdetermination

For fixed symbolic gauge factor `A_EW=(g_2^2+g_Y^2)/8`, the family

```text
lambda_s(mu_match) = A_EW(mu_match) s_beta,  s_beta in [0,1]
```

preserves all current closed Route-B data while changing the boundary value.
So H7B sharpens the missing source object instead of promoting a numerical
quartic.

## Next

`CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1-SELECTED-DTERM-PROJECTION-INVARIANT-SOURCE`

parallel:

`CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B2-SELECTED-EW-BOUNDARY-RG-PACKET`
"""

    for path, payload in [
        (EXTERNAL_REF, external_ref),
        (SOURCE_SEARCH, source_search),
        (UNDERDETERMINATION, underdetermination),
        (PAYLOAD_CONTRACT, payload_contract),
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
