"""Build CONST-HIGGS-01 H7B1G B_Huv or M_source fill attempt."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
Q79_REPO = TEXPAPERS / "mtt-q79-proof-repro"
SM_PARITY_REPO = TEXPAPERS / "mtt-sm-parity-closure"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_higgs_01_h7b1g_fill_bhuv_or_msource"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SUPPORT_SPLIT = BASE / "support_split_theorem.packet.json"
CURRENT_FILL = BASE / "current_fill_attempt.packet.json"
BHUV_REQUEST = BASE / "bhuv_minimal_lift_payload_request.packet.json"
MSOURCE_REQUEST = BASE / "msource_minimal_operator_payload_request.packet.json"
NO_CURRENT_SOURCE = BASE / "no_current_source_value_emission.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_HIGGS_01_H7B1G_FillBHuvOrMSource_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7B1G_FILL_ATTEMPT_SUPPORT_SPLIT_VALUES_OPEN"


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


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    h7b1a_path = DATA / "const_higgs_01_h7b1a_selected_two_higgs_metric_or_light_projector_source.candidate.json"
    h7b1f_path = DATA / "const_higgs_01_h7b1f_nonsplit_valpha_to_huv_omega_packet.candidate.json"
    h7b1f_contract_path = DATA / "const_higgs_01_h7b1f_nonsplit_valpha_to_huv_omega_packet" / "nonsplit_to_huv_reduction_contract.packet.json"
    e6_dictionary_path = Q79_REPO / "certificates" / "e6_to_sm_yukawa_operator_dictionary_certificate.json"
    valpha_path = Q79_REPO / "candidate_data" / "all_remaining_valpha_gates" / "selected_valpha_chern_weil_operator_source.after_terminal_lockdown.json"
    smslot_path = SM_PARITY_REPO / "candidate_data" / "selected_smslotfunctor_overlapkernel_source_emission.candidate.json"
    downstream_path = SM_PARITY_REPO / "candidate_data" / "selected_smslotfunctor_downstream_operator_payloads_or_smparity_ledger.candidate.json"
    visible_payload_path = SM_PARITY_REPO / "candidate_data" / "selected_visibleoperatorpayload_or_routechymresidual.candidate.json"
    extraction_contract_path = SM_PARITY_REPO / "candidate_data" / "selected_visibleoperatorpayload_or_routechymresidual" / "hym_operator_extraction_contract.packet.json"
    promotion_decision_path = SM_PARITY_REPO / "candidate_data" / "selected_visibleoperatorpayload_or_routechymresidual" / "promotion_decision_after_operator_payload.packet.json"
    primitive_selector_path = SM_PARITY_REPO / "candidate_data" / "selected_primitivevertex_source_or_basistransport_selectiontheorem.candidate.json"

    h7b1a = load(h7b1a_path)
    h7b1f = load(h7b1f_path)
    h7b1f_contract = load(h7b1f_contract_path)
    e6_dictionary = load(e6_dictionary_path)
    valpha = load(valpha_path)
    smslot = load(smslot_path)
    downstream = load(downstream_path)
    visible_payload = load(visible_payload_path)
    extraction_contract = load(extraction_contract_path)
    promotion_decision = load(promotion_decision_path)
    primitive_selector = load(primitive_selector_path)

    e6_open = e6_dictionary["open"]
    e6_closed = e6_dictionary["closed"]
    sm_assignments = e6_dictionary["representation_dictionary"]["sm_assignments"]
    operator_execution = valpha["operator_execution"]
    valpha_extension = valpha["valpha_extension"]

    bhuv_support = {
        "representation_dictionary_source": rel(e6_dictionary_path),
        "sm_slot_functor_source": rel(smslot_path),
        "downstream_static_ledger_source": rel(downstream_path),
        "single_higgs_quotient_source": rel(h7b1a_path),
        "support_closed": {
            "E6_representation_bridge": e6_closed["representation_theory_bridge"],
            "SM_yukawa_operator_forms": e6_closed["sm_yukawa_operator_forms"],
            "five_H_slot_label": sm_assignments["5_H"],
            "barfive_H_slot_label": sm_assignments["bar5_H"],
            "SM_slot_functor_all_six_arrows": smslot["arrow_status"]["all_six_closed"],
            "static_SM_slot_tier": downstream["payload_tiers"]["static_sm_slot_tier"]["closed"],
            "single_Higgs_quotient_imported": h7b1a["single_Higgs_quotient_imported"],
            "quotient_to_projector_underdetermined": h7b1a["quotient_to_projector_underdetermination_proved"],
        },
        "still_missing_for_B_Huv": {
            "physical_light_higgs_doublet_selection": e6_open["physical_light_higgs_doublet_selection"],
            "color_triplet_projection_or_decoupling": e6_open["color_triplet_projection_or_decoupling"],
            "channel_weights": e6_open["channel_weights"],
            "family_or_Higgs_kinetic_metrics": e6_open["family_kinetic_metrics"],
            "selected_metric_on_two_Higgs_plane": h7b1a["selected_metric_on_two_Higgs_plane_found"] is False,
            "selected_rank_one_light_projector": h7b1a["selected_rank_one_light_projector_P_L_found"] is False,
            "selected_splitting_source": h7b1a["selected_splitting_source_found"] is False,
            "two_column_source_orthonormal_lift_B_Huv": h7b1f["selected_Higgs_lift_B_Huv_found"] is False,
        },
        "value_emitted": False,
    }

    msource_support = {
        "valpha_source": rel(valpha_path),
        "visible_payload_source": rel(visible_payload_path),
        "extraction_contract_source": rel(extraction_contract_path),
        "promotion_decision_source": rel(promotion_decision_path),
        "primitive_selector_source": rel(primitive_selector_path),
        "support_closed": {
            "rank2_valpha_model_selected": valpha_extension["rank2_valpha_model_selected"],
            "terminal_L_L2_source_closed": valpha_extension["terminal_monad_difference_L3_minus_K2_selector_closed"],
            "nonzero_ext_class_selected": valpha_extension["nonzero_ext_class_selected"],
            "abstract_HYM_no_longer_blocker": visible_payload["what_closes_now"]["abstract_HYM_no_longer_blocker"],
            "finite_operator_extraction_contract_built": visible_payload["what_closes_now"]["finite_operator_extraction_contract_built"],
            "routec_hym_pipeline_replayed": visible_payload["what_closes_now"]["routec_hym_pipeline_replayed"],
            "rhoE_mesh_shape_passes": extraction_contract["validator_results_on_honest_smoke"]["rhoE_mesh"]["pass"],
            "rhoE_metric_shape_passes": extraction_contract["validator_results_on_honest_smoke"]["rhoE_metric"]["pass"],
            "sector_maps_shape_passes": extraction_contract["validator_results_on_honest_smoke"]["sector_maps"]["pass"],
            "primitive_vertex_source_selector_promoted": primitive_selector["promotion_decision"]["source_selector_promoted"],
        },
        "still_missing_for_M_source": {
            "selected_source_identity": valpha["source_identity"]["selected_by_mtt"] is False,
            "source_certificate": valpha["source_identity"]["source_certificate"] is None,
            "pic0_selected_or_quotiented": valpha_extension["pic0_selected_or_quotiented"] is False,
            "non_split_stability_or_hym_proved": valpha_extension["non_split_stability_or_hym_proved"] is False,
            "route_c_residual_selected_source_verified": extraction_contract["source_flags_on_honest_smoke"]["route_c_residual_selected_source_verified"] is False,
            "selected_operator_values_closed": extraction_contract["selected_operator_values_closed"] is False,
            "actual_extraction_theorem_supplied": extraction_contract["actual_extraction_theorem_supplied"] is False,
            "actual_visible_operator_payload_emitted": extraction_contract["actual_visible_operator_payload_emitted"] is False,
            "honest_operator_pipeline_pass": promotion_decision["route_B_routec_hym_residual"]["honest_operator_pipeline_pass"] is False,
            "sector_D_E_packets_pass": operator_execution["sector_D_E_packets_pass"] is False,
            "reduced_green_packets_pass": operator_execution["reduced_green_packets_pass"] is False,
            "dotD_packets_pass": operator_execution["dotD_packets_pass"] is False,
            "primitive_C1_or_Yukawa_contractions": operator_execution["primitive_C1_or_Yukawa_contractions"] is False,
            "selected_Hermitian_mass_strain_operator": h7b1f["selected_Hermitian_M_source_found"] is False,
        },
        "value_emitted": False,
    }

    support_split = {
        "schema": "MTTConstHiggs01H7B1GSupportSplitTheorem.v1",
        "status": "BHUV_AND_MSOURCE_SUPPORT_SPLIT_PROVED_VALUES_OPEN",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1G-SUPPORT-SPLIT-THEOREM",
        "theorem": {
            "name": "H7B1GSelectedBHuvOrMSourceSupportSplitTheorem",
            "proved": True,
            "statement": (
                "The H7B1F reduction H_uv=B_Huv^* M_source B_Huv splits the remaining Higgs boundary problem into two independent same-source payloads. "
                "The corpus/repo support closes representation labels, the low-energy Higgs quotient, static SM-slot arrows, non-split V_alpha support, and the Route-C/HYM extraction contract. "
                "It does not emit either the source-orthonormal two-column Higgs lift B_Huv or a theorem-derived Hermitian source operator M_source. Therefore H7B1G reduces the next work to two exact payload requests and proves no current H_uv, Omega, s_beta, or lambda_H value is selected."
            ),
        },
        "proof_steps": [
            "H7B1F proves the only accepted finite two-Higgs reduction has the form H_uv=B_Huv^* M_source B_Huv.",
            "E6/q79/SM-slot material fixes Higgs labels and static source routing, but H7B1A proves the quotient q(H_u)=q(H_d^dagger)=H does not choose a metric, splitting, light projector, or source-orthonormal two-column lift.",
            "V_alpha/Route-C material fixes a live non-split operator route and an extraction contract, but current honest packets do not theorem-derive selected D_E/Riesz/Green/dotD/operator values or a Hermitian H-sector mass/strain operator.",
            "Since B_Huv and M_source enter multiplicatively, either one can be filled first, but H_uv cannot be evaluated until both same-source payloads exist with exactness certificates.",
        ],
        "bhuv_support": bhuv_support,
        "msource_support": msource_support,
        **clean_flags(),
    }

    bhuv_request = {
        "schema": "MTTConstHiggs01H7B1GBHuvMinimalLiftPayloadRequest.v1",
        "status": "BHUV_MINIMAL_LIFT_PAYLOAD_REQUESTED_NOT_EMITTED",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1G-BHUV-MINIMAL-LIFT-PAYLOAD",
        "same_source_branch": "q79/F,m=1",
        "input_support": {
            "E6_Higgs_slots": {
                "5_H": sm_assignments["5_H"],
                "bar5_H": sm_assignments["bar5_H"],
            },
            "single_Higgs_quotient": "q(H_u)=H and q(H_d^dagger)=H, but quotient does not select a projector",
            "static_SM_slot_arrows_closed": smslot["arrow_status"]["all_six_closed"],
        },
        "must_emit": [
            "source id matching the selected q79/F,m=1 non-split/Route-C branch",
            "two finite source-space column vectors representing H_u and H_d^dagger before quotient",
            "the source Hermitian inner product or Gram matrix used to test B_Huv^* G B_Huv=I_2",
            "color-triplet projection or decoupling certificate so the columns are physical Higgs doublet slots",
            "quotient-admissibility check q(H_u)=H, q(H_d^dagger)=H, and q restricted to the selected light line is nonzero",
            "basis/phase covariance rule showing Huv phase changes are conjugations only",
            "finite exactness or truncation certificate for the two-column lift",
        ],
        "acceptance_tests": {
            "same_source_with_M_source_required_for_Huv": True,
            "source_orthonormality_required": "B_Huv^* G_source B_Huv = I_2 or an emitted whitening map",
            "forbid_observed_selectors": [
                "measured Higgs mass",
                "measured lambda_H",
                "tan_beta backsolve",
                "electroweak threshold residual",
            ],
            "current_payload_emitted": False,
        },
        "would_close_when_emitted": {
            "selected_Higgs_lift_B_Huv": True,
            "selected_Huv_basis_binding": True,
            "Huv_values": "only if M_source is also emitted",
        },
        **clean_flags(),
    }

    msource_request = {
        "schema": "MTTConstHiggs01H7B1GMSourceMinimalOperatorPayloadRequest.v1",
        "status": "MSOURCE_MINIMAL_OPERATOR_PAYLOAD_REQUESTED_NOT_EMITTED",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1G-MSOURCE-MINIMAL-OPERATOR-PAYLOAD",
        "same_source_branch": "q79/F,m=1",
        "input_support": {
            "non_split_valpha_route": "0 -> L -> V_alpha -> L^-1 -> 0",
            "selected_L": valpha_extension["selected_L"],
            "selected_L2": valpha_extension["selected_L2"],
            "h1_L2": valpha_extension["h1_L2"],
            "c2_valpha": valpha_extension["c2_valpha"],
            "finite_operator_extraction_contract_built": visible_payload["what_closes_now"]["finite_operator_extraction_contract_built"],
            "shape_validators_ready": {
                "rhoE_mesh": extraction_contract["validator_results_on_honest_smoke"]["rhoE_mesh"]["pass"],
                "rhoE_metric": extraction_contract["validator_results_on_honest_smoke"]["rhoE_metric"]["pass"],
                "sector_maps": extraction_contract["validator_results_on_honest_smoke"]["sector_maps"]["pass"],
            },
        },
        "must_emit": [
            "selected_source_verified true for the same V_alpha/Route-C source",
            "theorem-derived finite rho_E/metric tables or an equivalent exact operator representation",
            "selected D_E action, Riesz projector, reduced Green, and dotD response from that same source",
            "Hermitian mass/strain or Hessian operator M_source on the same finite source space used by B_Huv",
            "H-sector restriction map proving that B_Huv^* M_source B_Huv is the accepted two-Higgs Hessian block",
            "Hermiticity check M_source^*=M_source and finite residual/error certificate",
            "proof that lifted flags or smoke matrices are not being promoted as selected values",
        ],
        "acceptance_tests": {
            "same_source_with_B_Huv_required_for_Huv": True,
            "Hermiticity_required": True,
            "no_lifted_flag_promotion": True,
            "forbid_observed_selectors": [
                "measured Higgs mass",
                "measured lambda_H",
                "tan_beta backsolve",
                "benchmark Yukawa or CKM entries",
            ],
            "current_payload_emitted": False,
        },
        "would_close_when_emitted": {
            "selected_Hermitian_M_source": True,
            "selected_operator_payload_for_Huv": True,
            "Huv_values": "only if B_Huv is also emitted",
        },
        **clean_flags(),
    }

    no_current_source = {
        "schema": "MTTConstHiggs01H7B1GNoCurrentSourceValueEmission.v1",
        "status": "NO_CURRENT_SOURCE_EMITS_BHUV_OR_MSOURCE_VALUES",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1G-NO-CURRENT-SOURCE-VALUE-EMISSION",
        "checked_inputs": {
            "H7B1A": rel(h7b1a_path),
            "H7B1F": rel(h7b1f_path),
            "E6_dictionary": rel(e6_dictionary_path),
            "V_alpha": rel(valpha_path),
            "SM_slot_functor": rel(smslot_path),
            "downstream_operator_ledger": rel(downstream_path),
            "visible_operator_payload": rel(visible_payload_path),
            "HYM_extraction_contract": rel(extraction_contract_path),
            "primitive_vertex_selector": rel(primitive_selector_path),
        },
        "value_emission_matrix": {
            "B_Huv": {
                "support_present": True,
                "value_emitted": False,
                "reason": "closed labels/static routing plus low-energy quotient do not select the two-column physical UV lift",
            },
            "M_source": {
                "support_present": True,
                "value_emitted": False,
                "reason": "Route-C/HYM extraction contract and shape support do not emit selected Hermitian operator values",
            },
            "H_uv": {
                "support_present": True,
                "value_emitted": False,
                "reason": "H_uv requires both B_Huv and M_source from the same source",
            },
            "Omega": {"support_present": True, "value_emitted": False},
            "s_beta": {"support_present": True, "value_emitted": False},
            "lambda_H": {"support_present": True, "value_emitted": False},
        },
        **clean_flags(),
    }

    current_fill = {
        "schema": "MTTConstHiggs01H7B1GCurrentFillAttempt.v1",
        "status": "CURRENT_FILL_ATTEMPT_SUPPORT_SPLIT_VALUES_OPEN",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1G-CURRENT-FILL-ATTEMPT",
        "attempted_routes": {
            "route_A_fill_B_Huv": {
                "route_label": "static Higgs slot labels plus low-energy quotient plus selected SM-slot functor",
                "support_closed": True,
                "value_emitted": False,
                "blocked_by": [
                    "physical light Higgs doublet selection",
                    "color-triplet projection/decoupling",
                    "two-column source-orthonormal lift",
                    "selected two-Higgs metric/projector source",
                ],
            },
            "route_B_fill_M_source": {
                "route_label": "non-split V_alpha plus Route-C/HYM finite operator extraction",
                "support_closed": True,
                "value_emitted": False,
                "blocked_by": [
                    "selected source identity for operator payload",
                    "finite HYM/Route-C extraction theorem",
                    "selected D_E/Riesz/Green/dotD payload",
                    "H-sector Hermitian mass/strain operator",
                ],
            },
        },
        "computed_values": {
            "Huv": None,
            "Delta": None,
            "Omega": None,
            "s_beta": None,
            "lambda_H": None,
        },
        "new_Higgs_specific_parameters": 0,
        **clean_flags(),
    }

    next_work = {
        "schema": "MTTConstHiggs01H7B1GNextWork.v1",
        "status": "NEXT_WORKORDER_H7B1H_SOURCE_EXPORT_FIRST_ACTUAL_PAYLOAD",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1G-NEXT",
        "primary_next": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1H-SOURCE-EXPORT-FIRST-ACTUAL-PAYLOAD",
            "task": "Try to emit one actual source-derived payload: either B_Huv from selected Higgs-slot lift data or M_source from selected HYM/Route-C operator extraction.",
        },
        "recommended_order": [
            "Attack B_Huv first if a corpus/source theorem can promote physical light-doublet lift or two-Higgs metric/projector data.",
            "Attack M_source first if Route-C/HYM extraction can emit same-source Hermitian operator data with selected_source_verified true.",
            "Do not compute H_uv, Omega, s_beta, or lambda_H until both same-source payloads exist.",
        ],
        "parallel_watch": {
            "label": "CONST-EW-02 / UNIVERSAL-PRIMITIVE-PORTFOLIO",
            "task": "Keep the one-to-three universal primitive tier separate from strict no-knob Higgs closure.",
        },
    }

    candidate = {
        "candidate": "MTTConstHiggs01H7B1GFillBHuvOrMSource",
        "status": STATUS,
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1G-FILL-BHUV-OR-MSOURCE",
        "output_packets": {
            "support_split_theorem": rel(SUPPORT_SPLIT),
            "current_fill_attempt": rel(CURRENT_FILL),
            "bhuv_minimal_lift_payload_request": rel(BHUV_REQUEST),
            "msource_minimal_operator_payload_request": rel(MSOURCE_REQUEST),
            "no_current_source_value_emission": rel(NO_CURRENT_SOURCE),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": support_split["theorem"],
        "H7B1F_reduction_contract_imported": h7b1f["reduction_contract_built"],
        "support_split_theorem_proved": True,
        "B_Huv_support_present": True,
        "B_Huv_value_emitted": False,
        "M_source_support_present": True,
        "M_source_value_emitted": False,
        "both_payloads_required_for_Huv": True,
        "selected_Huv_basis_binding_found": False,
        "selected_Higgs_lift_B_Huv_found": False,
        "selected_Hermitian_M_source_found": False,
        "selected_finite_Huv_reduction_found": False,
        "selected_offdiagonal_Omega_found": False,
        "selected_Huu_Hud_Hdd_found": False,
        "selected_Delta_Omega_found": False,
        "selected_s_beta_value_found": False,
        "numeric_lambda_H_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "new_Higgs_specific_parameters": 0,
        "selected_next_artifact": "MTT_CONST_HIGGS_01_H7B1H_SourceExportFirstActualPayload_v1",
        **clean_flags(),
    }

    cert = {
        "certificate": "MTT_CONST_HIGGS_01_H7B1G_FillBHuvOrMSource_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "active_label": candidate["active_label"],
        "support_split_theorem_proved": True,
        "B_Huv_support_present": True,
        "B_Huv_value_emitted": False,
        "M_source_support_present": True,
        "M_source_value_emitted": False,
        "selected_finite_Huv_reduction_found": False,
        "selected_offdiagonal_Omega_found": False,
        "selected_s_beta_value_found": False,
        "numeric_lambda_H_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "new_Higgs_specific_parameters": 0,
        **clean_flags(),
    }

    note = f"""# MTT CONST HIGGS 01 H7B1G Fill B_Huv or M_source v1

Status: `{STATUS}`

Label: `CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1G-FILL-BHUV-OR-MSOURCE`

## Result

```text
H7B1F reduction imported                 True
support split theorem proved             True
B_Huv support present                    True
B_Huv value emitted                      False
M_source support present                 True
M_source value emitted                   False
H_uv values emitted                      False
Omega emitted                            False
s_beta emitted                           False
lambda_H emitted                         False
strict no-knob Higgs closure             False
```

## What Changed

H7B1G does not add a number.  It makes the remaining fill precise:

```text
H_uv = B_Huv^* M_source B_Huv
```

`B_Huv` is the source-orthonormal two-column Higgs lift with columns
`(H_u,H_d^dagger)`.  `M_source` is the same-source Hermitian mass/strain
operator.  Either payload can be constructed first, but both are required
before `H_uv`, `Omega`, `s_beta`, or `lambda_H` can be computed.

## Current Verdict

The corpus/repo support is real but split:

* `B_Huv`: representation labels, static SM-slot routing, and the low-energy
  Higgs quotient are supported; physical doublet lift, color-triplet
  decoupling, and two-column metric/projector data are not emitted.
* `M_source`: non-split `V_alpha` and Route-C/HYM extraction scaffolding are
  supported; selected finite operator values and the Hermitian H-sector
  mass/strain operator are not emitted.

No observed Higgs mass, measured quartic, beta backsolve, Yukawa benchmark, or
threshold residual is used as a selector.
"""

    for path, payload in [
        (SUPPORT_SPLIT, support_split),
        (BHUV_REQUEST, bhuv_request),
        (MSOURCE_REQUEST, msource_request),
        (NO_CURRENT_SOURCE, no_current_source),
        (CURRENT_FILL, current_fill),
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
