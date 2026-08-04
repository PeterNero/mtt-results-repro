"""Build CONST-HIGGS-01 H7B1R Huv source or primitive-C1/lambda bridge gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
SM_PARITY = TEXPAPERS / "mtt-sm-parity-closure"
NONSM = TEXPAPERS / "mtt-nonsm-constants-no-knob"
Q79 = TEXPAPERS / "mtt-q79-proof-repro"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_higgs_01_h7b1r_huv_source_operator_or_primitive_c1_lambda_bridge"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
DIRECT_HUV = BASE / "direct_huv_source_lane.packet.json"
C1_BRIDGE = BASE / "primitive_c1_lambda_bridge_lane.packet.json"
CONTRACT = BASE / "huv_bridge_acceptance_contract.packet.json"
NO_CYCLE = BASE / "non_circulation_ledger.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_HIGGS_01_H7B1R_HuvSourceOperatorOrPrimitiveC1LambdaBridge_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7B1R_BOTH_EXITS_TESTED_HUV_SOURCE_PAYLOAD_OPEN"


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


def clean_flags() -> dict[str, bool]:
    return {
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }


def sector_order_contains_huv(sectors: list[str]) -> bool:
    return any(sector in {"H", "H_u", "H_d^dagger", "Huv"} for sector in sectors)


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    h7b1q_path = DATA / "const_higgs_01_h7b1q_twohiggs_lift_or_samesource_functional_value.candidate.json"
    h7b1q_boundary_path = DATA / "const_higgs_01_h7b1q_twohiggs_lift_or_samesource_functional_value" / "twohiggs_huv_boundary_after_functional_value.packet.json"
    h7b1f_path = DATA / "const_higgs_01_h7b1f_nonsplit_valpha_to_huv_omega_packet.candidate.json"
    h7b1n_path = DATA / "const_higgs_01_h7b1n_hsector_dynamic_extension_or_honest_huv_rows.candidate.json"
    h7b1n_cutset_path = DATA / "const_higgs_01_h7b1n_hsector_dynamic_extension_or_honest_huv_rows" / "nonlinear_hym_huv_payload_cutset.packet.json"
    h7b1m_c1_audit_path = DATA / "const_higgs_01_h7b1m_c1_to_huv_projection_or_honest_huv_row_export" / "c1_target_sector_support_audit.packet.json"

    q79_single_higgs_path = Q79 / "certificates" / "single_higgs_channel_projection_certificate.json"

    sm_dynamic_identity_path = SM_PARITY / "candidate_data" / "selected_samesource_dynamictransferidentity_or_galerkinc1contractions_emission.candidate.json"
    sm_differentiated_row_path = SM_PARITY / "candidate_data" / "selected_differentiatedphifinc1primitiveoverlap_or_firstrowkernelformulasource.candidate.json"
    sm_c1_operator_emission_path = SM_PARITY / "candidate_data" / "selected_routec_selected_c1_response_operator_emission.candidate.json"
    nonsm_primitive_envelope_path = NONSM / "candidate_data" / "primitivec1_contractions_or_dynamicoverlaptensor_sourceemission_import.candidate.json"
    nonsm_dynamic_layer_path = NONSM / "candidate_data" / "dynamicoverlaptensor_hessiannormalization_or_galerkinc1contractions_valueemission_import.candidate.json"
    nonsm_lambda12_path = NONSM / "certificates" / "selected_hypercharge_normalized_threshold_interface_certificate.json"

    h7b1q = load(h7b1q_path)
    h7b1q_boundary = load(h7b1q_boundary_path)
    h7b1f = load(h7b1f_path)
    h7b1n = load(h7b1n_path)
    h7b1n_cutset = load(h7b1n_cutset_path)
    h7b1m_c1_audit = load(h7b1m_c1_audit_path)
    q79_single_higgs = load(q79_single_higgs_path)
    sm_dynamic_identity = load(sm_dynamic_identity_path)
    sm_differentiated_row = load(sm_differentiated_row_path)
    sm_c1_operator_emission = load(sm_c1_operator_emission_path)
    nonsm_primitive_envelope = load(nonsm_primitive_envelope_path)
    nonsm_dynamic_layer = load(nonsm_dynamic_layer_path)
    nonsm_lambda12 = load(nonsm_lambda12_path)

    c1_coordinate_system = sm_dynamic_identity["normal_form_identity"]["coordinate_system"]
    c1_sector_order = c1_coordinate_system["sector_order"]
    c1_contains_huv = sector_order_contains_huv(c1_sector_order)
    c1_target = h7b1m_c1_audit["c1_response_target"]

    nonsm_dynamic_current = nonsm_dynamic_layer["current_layer_value_packet"]
    nonsm_dynamic_sectors = sorted(
        nonsm_dynamic_current["fixed_fiber_values"]["0"]["sectors"].keys()
    )
    nonsm_dynamic_contains_huv = sector_order_contains_huv(nonsm_dynamic_sectors)

    lambda12_formula = nonsm_lambda12["source_formula"]["weak_split"]
    lambda12_is_higgs_lambda = False

    direct_lane_closed = all(
        [
            h7b1f["basis_invariant_Huv_functor_proved"] is True,
            h7b1q["UV_twoHiggs_Huv_transfer_closed"] is True,
            h7b1q["B_Huv_value_emitted"] is True,
            h7b1q["M_source_value_emitted"] is True,
        ]
    )

    primitive_bridge_closed = all(
        [
            sm_dynamic_identity["promotion_decision"]["selected_A_selected_promoted"] is True,
            sm_dynamic_identity["promotion_decision"]["selected_b_selected_promoted"] is True,
            c1_contains_huv is True,
            lambda12_is_higgs_lambda is True,
        ]
    )

    direct_huv = {
        "schema": "MTTConstHiggs01H7B1RDirectHuvSourceLane.v1",
        "status": "DIRECT_UV_HUV_SOURCE_LANE_TESTED_PAYLOAD_OPEN",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1R-A-DIRECT-HUV-SOURCE",
        "input_sources": {
            "H7B1Q": rel(h7b1q_path),
            "H7B1Q_Huv_boundary": rel(h7b1q_boundary_path),
            "H7B1F_conditional_Huv_functor": rel(h7b1f_path),
            "H7B1N_candidate": rel(h7b1n_path),
            "H7B1N_minimal_cutset": rel(h7b1n_cutset_path),
            "q79_single_Higgs_projection": rel(q79_single_higgs_path),
        },
        "closed_support": {
            "basis_invariant_Huv_functor_proved_conditionally": h7b1f["basis_invariant_Huv_functor_proved"],
            "low_energy_single_Higgs_channel_projection": q79_single_higgs["closed"]["single_higgs_channel_projection"],
            "same_source_functional_exit_closed_by_H7B1Q": h7b1q["samesource_functional_exit_closed"],
            "alpha1_driver_verified_by_H7B1Q": h7b1q["alpha1_driver_verified"],
            "nonlinear_HYM_seed_support_closed": h7b1n["nonlinear_HYM_seed_support_closed"],
        },
        "missing_payload": {
            "UV_twoHiggs_basis_emitted": h7b1q["UV_twoHiggs_basis_emitted"],
            "B_Huv_value_emitted": h7b1q["B_Huv_value_emitted"],
            "M_source_value_emitted": h7b1q["M_source_value_emitted"],
            "direct_Huv_entries_emitted": h7b1q["direct_Huv_entries_emitted"],
            "Huu_Hud_Hdd_emitted": False,
            "Omega_emitted": False,
            "s_beta_emitted": h7b1q["selected_s_beta_value_found"],
            "lambda_H_emitted": h7b1q["numeric_lambda_H_derived"],
        },
        "minimal_payload_to_close": h7b1n_cutset["minimal_payload_to_close"],
        "decision": {
            "direct_Huv_source_exit_closed": direct_lane_closed,
            "rank_one_or_single_H_projection_promoted_to_UV_twoHiggs": False,
            "conditional_Huv_functor_promoted_as_value": False,
            "reason": "The direct lane has the correct conditional functor and low-energy single-Higgs channel, but no selected UV basis/lift, no B_Huv, no M_source, and no direct Huv rows.",
        },
        **clean_flags(),
    }

    c1_bridge = {
        "schema": "MTTConstHiggs01H7B1RPrimitiveC1LambdaBridgeLane.v1",
        "status": "PRIMITIVE_C1_LAMBDA_BRIDGE_TESTED_NO_HUV_CODOMAIN",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1R-B-PRIMITIVE-C1-LAMBDA-BRIDGE",
        "input_sources": {
            "H7B1M_C1_target_audit": rel(h7b1m_c1_audit_path),
            "SM_same_source_dynamic_transfer_identity": rel(sm_dynamic_identity_path),
            "SM_differentiated_first_row_kernel_source": rel(sm_differentiated_row_path),
            "SM_C1_response_operator_emission": rel(sm_c1_operator_emission_path),
            "nonSM_primitive_C1_envelope": rel(nonsm_primitive_envelope_path),
            "nonSM_dynamic_overlap_hessian_layer": rel(nonsm_dynamic_layer_path),
            "nonSM_hypercharge_lambda12_interface": rel(nonsm_lambda12_path),
        },
        "C1_coordinate_system": {
            "codomain_real_dimension": c1_coordinate_system["codomain_real_dimension"],
            "sector_order": c1_sector_order,
            "contains_H_sector": c1_contains_huv,
            "contains_Hu_sector": c1_target["contains_Hu_sector"],
            "contains_Hd_dagger_sector": c1_target["contains_Hd_dagger_sector"],
            "contains_Huv_sector": c1_contains_huv,
        },
        "primitive_C1_status": {
            "same_source_identity_normal_form_built": sm_dynamic_identity["promotion_decision"]["identity_normal_form_built"],
            "selected_A_selected_promoted": sm_dynamic_identity["promotion_decision"]["selected_A_selected_promoted"],
            "selected_b_selected_promoted": sm_dynamic_identity["promotion_decision"]["selected_b_selected_promoted"],
            "honest_Galerkin_C1_contractions_promoted": sm_dynamic_identity["promotion_decision"]["honest_Galerkin_C1_contractions_promoted"],
            "first_row_formula_source_specified": sm_differentiated_row["what_closes_now"]["first_row_kernel_formula_source_specified"],
            "first_row_value_execution_open": sm_differentiated_row["what_remains_open"]["first_row_independent_value_execution"],
            "selected_C1_response_operator_A_emitted": sm_c1_operator_emission["emission_audit"]["selected_operator_A_selected_emitted"],
            "selected_source_vector_b_emitted": sm_c1_operator_emission["emission_audit"]["selected_source_vector_b_selected_emitted"],
        },
        "nonSM_dynamic_layer_status": {
            "current_layer_value_packet_emitted": nonsm_dynamic_layer["guardrails"]["current_layer_value_packet_emitted"],
            "current_layer_flavor_no_go": nonsm_dynamic_layer["guardrails"]["current_layer_flavor_no_go"],
            "sector_order": nonsm_dynamic_sectors,
            "contains_Huv_sector": nonsm_dynamic_contains_huv,
            "selected_dynamic_overlap_tensor_claimed": nonsm_dynamic_layer["guardrails"]["selected_dynamic_overlap_tensor_claimed"],
            "selected_Galerkin_C1_contractions_claimed": nonsm_dynamic_layer["guardrails"]["selected_Galerkin_C1_contractions_claimed"],
        },
        "lambda12_status": {
            "formula": lambda12_formula,
            "is_hypercharge_threshold_split": lambda12_formula == "lambda_12 = p_Y - p_SU2",
            "is_Higgs_lambda_H": lambda12_is_higgs_lambda,
            "required_selected_inputs": nonsm_lambda12["required_selected_inputs"],
            "determinant_amplitudes_selected": nonsm_lambda12["verdict"]["determinant_amplitudes_selected"],
        },
        "decision": {
            "primitive_C1_lambda_bridge_exit_closed": primitive_bridge_closed,
            "lambda12_can_be_used_as_Higgs_lambda_without_bridge": False,
            "matter_sector_C1_rows_can_be_used_as_Huv_without_bridge": False,
            "current_bridge_codomain_missing": True,
            "reason": "The strongest C1/lambda artifacts live in matter/gauge threshold coordinates: u,d,e,nuD 72-real response rows or hypercharge-normalized stack thresholds. None emits a map into Herm(2) on (H_u,H_d^dagger).",
        },
        **clean_flags(),
    }

    contract = {
        "schema": "MTTConstHiggs01H7B1RHuvBridgeAcceptanceContract.v1",
        "status": "HUV_BRIDGE_ACCEPTANCE_CONTRACT_BUILT",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1R-C-HUV-BRIDGE-CONTRACT",
        "necessary_future_object": {
            "name": "Selected_C1_or_NonlinearHYM_to_Huv_BridgeFunctor",
            "must_emit_one_of": [
                "selected B_Huv plus same-source Hermitian M_source",
                "direct source-owned Huu,Hud,Hdd rows in ordered (H_u,H_d^dagger)",
                "a theorem-derived bridge T_Huv from primitive C1/lambda data to Herm(2), with T_Huv(data)=(Huu,Hud,Hdd)",
            ],
            "codomain": "Hermitian 2x2 Higgs mass/strain block on ordered basis (H_u,H_d^dagger)",
            "same_source_required": "same selected q79/F,m=1 or successor Route-C/Strominger source branch",
            "exactness_required": "symbolic proof or finite residual/truncation/error certificate",
        },
        "forbidden_promotions": [
            "using lambda_12=p_Y-p_SU2 as lambda_H",
            "using u,d,e,nuD C1 rows as Huv rows",
            "using rank-one H projection as B_Huv",
            "using conditional Huv functor theorem as Huv values",
            "using observed Higgs mass, v, beta, or target lambda to choose Huv entries",
        ],
        "acceptance_tests": {
            "basis_labels_emitted": "ordered basis exactly [H_u,H_d^dagger]",
            "Hermitian_payload_emitted": "Huu,Hdd real and Hdu=conj(Hud)",
            "non_scalar_payload": "Delta^2+|Omega|^2>0",
            "source_exactness": "same-source id and exactness/error certificate attached",
            "no_target_fit": "no observed Higgs/lambda/beta value used as selector",
            "derive_outputs": "compute Delta, Omega, s_beta, then lambda_H only after EW boundary/RG policy",
        },
        **clean_flags(),
    }

    no_cycle = {
        "schema": "MTTConstHiggs01H7B1RNonCirculationLedger.v1",
        "status": "NO_CIRCULATION_LEDGER_UPDATED_H7B1R",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1R-NO-CYCLE",
        "retired_or_do_not_reopen": {
            "same_source_functional_value_exit": h7b1q["samesource_functional_exit_closed"],
            "alpha1_driver_as_Higgs_blocker": h7b1q["alpha1_driver_verified"],
            "plain_72_real_C1_target_as_Huv_source": h7b1m_c1_audit["target_mismatch_result"]["plain_C1_target_can_supply_Huv_projection_now"] is False,
            "lambda12_as_lambda_H_without_bridge": True,
            "matter_C1_rows_as_UV_Huv_without_bridge": True,
            "rank_one_H_projector_as_two_column_lift": h7b1n_cutset["closed_as_nonstarters"]["rank_one_H_projector_as_B_Huv"],
        },
        "active_not_retired": {
            "selected_UV_twoHiggs_bridge_functor": True,
            "nonlinear_HYM_Huv_row_execution": True,
            "direct_source_owned_Huu_Hud_Hdd_rows": True,
            "primitive_C1_to_Huv_bridge_only_if_codomain_Herm2_emitted": True,
        },
        "circulation_test": {
            "is_reopening_H7B1Q": False,
            "is_reopening_plain_C1_projection": False,
            "is_promoting_lambda12_as_lambda_H": False,
            "is_promoting_matter_rows_as_Huv": False,
            "new_information_added": [
                "primitive C1/lambda lane was tested against the Huv codomain requirement",
                "lambda_12 was classified as hypercharge threshold split, not Higgs lambda_H",
                "current C1 sectors u,d,e,nuD were confirmed absent from UV Huv codomain",
                "future bridge acceptance contract was made explicit and machine-checkable",
            ],
        },
        **clean_flags(),
    }

    next_work = {
        "schema": "MTTConstHiggs01H7B1RNextWork.v1",
        "status": "NEXT_WORKORDER_H7B1S_HUV_BRIDGE_FUNCTOR_OR_NONLINEAR_HYM_ROW_EXECUTION",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1R-NEXT",
        "primary_next": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1S-HUV-BRIDGE-FUNCTOR-OR-NONLINEAR-HYM-ROW-EXECUTION",
            "task": "Either construct the selected C1/nonlinear-HYM-to-Huv bridge functor with Herm(2) codomain, or execute the nonlinear HYM/Huv row solve directly in the selected End0 basis.",
        },
        "legal_exits": [
            {
                "id": "H7B1S-A",
                "label": "bridge functor",
                "must_emit": "T_Huv from selected primitive C1/lambda/nonlinear source data to Huu,Hud,Hdd on (H_u,H_d^dagger)",
            },
            {
                "id": "H7B1S-B",
                "label": "direct nonlinear HYM rows",
                "must_emit": "nonlinear HYM correction coefficients or direct Hermitian Huv rows with residual/exactness certificate",
            },
        ],
        "superset_strategy": {
            "using_one_straight_way": False,
            "combining_paths": True,
            "straight_path": "direct Higgs Huv mass-strain/nonlinear HYM row lane",
            "support_path": "primitive C1/lambda/gauge-threshold lane, admissible only after a Herm(2) Huv bridge is emitted",
            "locked_target": "selected Huv payload, not measured lambda_H or weak lambda_12",
        },
        **clean_flags(),
    }

    theorem = {
        "name": "H7B1RHuvSourceOperatorOrPrimitiveC1LambdaBridgeTheorem",
        "proved": True,
        "statement": (
            "After H7B1Q, the alpha/overlap/source-strength side is no longer the active Higgs blocker. H7B1R tests both remaining exits. The direct Huv lane still lacks selected B_Huv, M_source, or direct Huu/Hud/Hdd rows. The primitive C1/lambda lane has real support, including 72-real matter-sector C1 normal forms and hypercharge-normalized lambda_12 threshold accounting, but these objects do not have codomain Herm(2) on (H_u,H_d^dagger). Therefore lambda_12 and matter C1 rows cannot be promoted to lambda_H or Huv without a new same-source bridge functor. The next exact target is that bridge functor or a direct nonlinear HYM/Huv row execution."
        ),
    }

    candidate = {
        "candidate": "MTTConstHiggs01H7B1RHuvSourceOperatorOrPrimitiveC1LambdaBridge",
        "status": STATUS,
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1R-HUV-SOURCE-OPERATOR-OR-PRIMITIVE-C1-LAMBDA-BRIDGE",
        "output_packets": {
            "direct_huv_source_lane": rel(DIRECT_HUV),
            "primitive_c1_lambda_bridge_lane": rel(C1_BRIDGE),
            "huv_bridge_acceptance_contract": rel(CONTRACT),
            "non_circulation_ledger": rel(NO_CYCLE),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": theorem,
        "H7B1Q_imported": h7b1q["status"] == "MTT_CONST_HIGGS_01_H7B1Q_SAMESOURCE_FUNCTIONAL_VALUE_CLOSED_TWOHIGGS_HUV_OPEN",
        "same_source_functional_exit_closed": h7b1q["samesource_functional_exit_closed"],
        "direct_Huv_source_exit_closed": direct_lane_closed,
        "primitive_C1_lambda_bridge_exit_closed": primitive_bridge_closed,
        "current_C1_codomain_contains_Huv": c1_contains_huv,
        "lambda12_reclassified_as_gauge_threshold_not_Higgs_lambda": True,
        "Huv_bridge_acceptance_contract_built": True,
        "UV_twoHiggs_basis_emitted": False,
        "B_Huv_value_emitted": False,
        "M_source_value_emitted": False,
        "direct_Huv_entries_emitted": False,
        "selected_s_beta_value_found": False,
        "numeric_lambda_H_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "new_Higgs_specific_parameters": 0,
        "selected_next_artifact": "MTT_CONST_HIGGS_01_H7B1S_HuvBridgeFunctorOrNonlinearHYMRowExecution_v1",
        **clean_flags(),
    }

    cert = {
        "certificate": "MTT_CONST_HIGGS_01_H7B1R_HuvSourceOperatorOrPrimitiveC1LambdaBridge_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "active_label": candidate["active_label"],
        "same_source_functional_exit_closed": h7b1q["samesource_functional_exit_closed"],
        "direct_Huv_source_exit_closed": direct_lane_closed,
        "primitive_C1_lambda_bridge_exit_closed": primitive_bridge_closed,
        "current_C1_codomain_contains_Huv": c1_contains_huv,
        "lambda12_reclassified_as_gauge_threshold_not_Higgs_lambda": True,
        "Huv_bridge_acceptance_contract_built": True,
        "UV_twoHiggs_Huv_transfer_closed": False,
        "B_Huv_value_emitted": False,
        "M_source_value_emitted": False,
        "direct_Huv_entries_emitted": False,
        "numeric_lambda_H_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "new_Higgs_specific_parameters": 0,
        **clean_flags(),
    }

    note = f"""# MTT CONST HIGGS 01 H7B1R Huv Source Operator Or Primitive C1 Lambda Bridge v1

Status: `{STATUS}`

Label: `CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1R-HUV-SOURCE-OPERATOR-OR-PRIMITIVE-C1-LAMBDA-BRIDGE`

## Result

```text
same-source functional exit closed               {h7b1q["samesource_functional_exit_closed"]}
direct Huv source exit closed                    {direct_lane_closed}
primitive C1/lambda bridge exit closed           {primitive_bridge_closed}
current C1 sector order                          {", ".join(c1_sector_order)}
current C1 codomain contains Huv                 {c1_contains_huv}
lambda_12 classified as Higgs lambda_H           {lambda12_is_higgs_lambda}
Huv bridge acceptance contract built             True
B_Huv / M_source / direct Huv emitted            False
s_beta / lambda_H promoted                       False
```

## What Moved Forward

H7B1R tests both legal exits from H7B1Q.  The direct Huv lane remains open, but
now the primitive-C1/lambda shortcut is also classified correctly: current C1
objects live in the `u,d,e,nuD` matter-sector coordinate system, and
`lambda_12=p_Y-p_SU2` is a hypercharge threshold split, not the Higgs quartic.

This is still useful progress because it prevents a wrong promotion.  A future
primitive-C1 route is legal only if it emits an actual bridge with codomain
`Herm(2)` on `(H_u,H_d^dagger)`.

## Remaining Boundary

The next exact gate is:

`CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1S-HUV-BRIDGE-FUNCTOR-OR-NONLINEAR-HYM-ROW-EXECUTION`
"""

    for path, payload in [
        (DIRECT_HUV, direct_huv),
        (C1_BRIDGE, c1_bridge),
        (CONTRACT, contract),
        (NO_CYCLE, no_cycle),
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
