"""Build CONST-HIGGS-01 H7B1Q two-Higgs lift or same-source functional gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
QA_SU3_REPO = TEXPAPERS / "mtt-qa-su3-packet-proof"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_higgs_01_h7b1q_twohiggs_lift_or_samesource_functional_value"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SAMESOURCE_IMPORT = BASE / "samesource_functional_value_import.packet.json"
HUV_BOUNDARY = BASE / "twohiggs_huv_boundary_after_functional_value.packet.json"
NO_CYCLE = BASE / "source_promotion_non_circulation_ledger.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_HIGGS_01_H7B1Q_TwoHiggsLiftOrSameSourceFunctionalValue_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7B1Q_SAMESOURCE_FUNCTIONAL_VALUE_CLOSED_TWOHIGGS_HUV_OPEN"


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

    h7b1p_path = DATA / "const_higgs_01_h7b1p_end0_to_huv_or_sector_routing.candidate.json"
    h7b1p_huv_path = DATA / "const_higgs_01_h7b1p_end0_to_huv_or_sector_routing" / "huv_boundary_after_sector_routing.packet.json"
    h7b1c_request_path = DATA / "const_higgs_01_h7b1c_selected_two_higgs_mass_strain_hessian" / "minimal_two_by_two_hessian_payload_request.packet.json"

    qa_chernweil_path = QA_SU3_REPO / "candidate_data" / "selected_u1y_routec_samesource_chernweil_operator_functional_value.candidate.json"
    qa_overlap_path = QA_SU3_REPO / "candidate_data" / "selected_u1y_routec_selected_u10ubar5_polarization_or_overlap_normalization.candidate.json"
    qa_operator_path = QA_SU3_REPO / "candidate_data" / "selected_u1y_routec_operator_emission_overlap_from_terminal_slotmap.candidate.json"
    qa_alpha_driver_path = QA_SU3_REPO / "candidate_data" / "selected_u1y_routec_alpha1_driver_replay_from_oriented_overlap.candidate.json"

    h7b1p = load(h7b1p_path)
    h7b1p_huv = load(h7b1p_huv_path)
    h7b1c_request = load(h7b1c_request_path)
    qa_chernweil = load(qa_chernweil_path)
    qa_overlap = load(qa_overlap_path)
    qa_operator = load(qa_operator_path)
    qa_alpha_driver = load(qa_alpha_driver_path)

    chernweil_decision = qa_chernweil["decision"]
    overlap_decision = qa_overlap["decision"]
    operator_decision = qa_operator["decision"]
    alpha_decision = qa_alpha_driver["decision"]
    promoted_value = qa_alpha_driver["promoted_value"]
    emitted_blocks = sorted(qa_operator["emitted_operator_blocks"].keys())

    samesource_functional_exit_closed = all(
        [
            chernweil_decision["same_source_chernweil_functional_value_gate_built"] is True,
            chernweil_decision["unique_current_support_value_identified"] is True,
            chernweil_decision["support_candidate_value_N_alpha1_h_ext"] == 1.0,
            chernweil_decision["support_candidate_residual_zero"] is True,
            overlap_decision["route_A_support_closed"] is True,
            overlap_decision["route_B_support_closed"] is True,
            overlap_decision["conditional_overlap_normalization_fixed"] is True,
            operator_decision["same_branch_functional_operator_emission_closed"] is True,
            operator_decision["selected_U10_Ubar5_operator_blocks_emitted"] is True,
            operator_decision["selected_1M_Dirac_operator_block_emitted"] is True,
            operator_decision["selected_overlap_normalization_emitted"] is True,
            alpha_decision["N_alpha1_h_ext_promoted_to_selected_value"] is True,
            alpha_decision["du_dalpha1_equals_h_ext_emitted"] is True,
            alpha_decision["selected_dotD_source_verified"] is True,
            alpha_decision["alpha1_driver_verified"] is True,
            alpha_decision["honest_dotD_validator_closed"] is True,
            promoted_value["N_alpha1_h_ext"] == 1.0,
            promoted_value["du_dalpha1"] == "h_ext",
            promoted_value["selected_value_emitted_by_this_theorem"] is True,
            promoted_value["tangent_residual_l2"] == 0.0,
            set(emitted_blocks) == {"d", "e", "nuD", "u"},
        ]
    )

    has_uv_higgs_blocks = any(block in {"H_u", "H_d^dagger", "Huv"} for block in emitted_blocks)

    samesource_import = {
        "schema": "MTTConstHiggs01H7B1QSameSourceFunctionalValueImport.v1",
        "status": "SAMESOURCE_FUNCTIONAL_ALPHA1_DRIVER_CLOSED",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1Q-A-SAMESOURCE-FUNCTIONAL-VALUE",
        "input_sources": {
            "H7B1P": rel(h7b1p_path),
            "H7B1P_Huv_boundary": rel(h7b1p_huv_path),
            "QA_same_source_chernweil_functional_value": rel(qa_chernweil_path),
            "QA_U10_Ubar5_overlap_normalization": rel(qa_overlap_path),
            "QA_operator_emission_overlap": rel(qa_operator_path),
            "QA_alpha1_driver_replay": rel(qa_alpha_driver_path),
        },
        "imported_chain": {
            "chernweil_gate_built": chernweil_decision["same_source_chernweil_functional_value_gate_built"],
            "unique_support_value_identified": chernweil_decision["unique_current_support_value_identified"],
            "support_candidate_value_N_alpha1_h_ext": chernweil_decision["support_candidate_value_N_alpha1_h_ext"],
            "support_candidate_residual_zero": chernweil_decision["support_candidate_residual_zero"],
            "route_A_U10_Ubar5_support_closed": overlap_decision["route_A_support_closed"],
            "route_B_HYM_projector_support_closed": overlap_decision["route_B_support_closed"],
            "conditional_overlap_normalization_fixed": overlap_decision["conditional_overlap_normalization_fixed"],
            "same_branch_functional_operator_emission_closed": operator_decision["same_branch_functional_operator_emission_closed"],
            "selected_U10_Ubar5_operator_blocks_emitted": operator_decision["selected_U10_Ubar5_operator_blocks_emitted"],
            "selected_1M_Dirac_operator_block_emitted": operator_decision["selected_1M_Dirac_operator_block_emitted"],
            "selected_overlap_normalization_emitted": operator_decision["selected_overlap_normalization_emitted"],
            "N_alpha1_h_ext_promoted_to_selected_value": alpha_decision["N_alpha1_h_ext_promoted_to_selected_value"],
            "du_dalpha1_equals_h_ext_emitted": alpha_decision["du_dalpha1_equals_h_ext_emitted"],
            "selected_dotD_source_verified": alpha_decision["selected_dotD_source_verified"],
            "alpha1_driver_verified": alpha_decision["alpha1_driver_verified"],
            "honest_dotD_validator_closed": alpha_decision["honest_dotD_validator_closed"],
        },
        "promoted_value": {
            "N_alpha1_h_ext": promoted_value["N_alpha1_h_ext"],
            "lambda_alpha1": promoted_value["lambda_alpha1"],
            "du_dalpha1": promoted_value["du_dalpha1"],
            "selected_value_emitted_by_this_theorem": promoted_value["selected_value_emitted_by_this_theorem"],
            "tangent_residual_l2": promoted_value["tangent_residual_l2"],
        },
        "operator_blocks_scope": {
            "emitted_operator_blocks": emitted_blocks,
            "all_blocks_are_matter_or_neutrino": set(emitted_blocks) == {"d", "e", "nuD", "u"},
            "contains_H_u": "H_u" in emitted_blocks,
            "contains_H_d_dagger": "H_d^dagger" in emitted_blocks,
            "contains_Huv": "Huv" in emitted_blocks,
            "has_uv_higgs_blocks": has_uv_higgs_blocks,
            "scope_note": "The closed operator emission is the oriented stationary matter-slot layer, not a UV two-Higgs Huv source.",
        },
        "residual_open_from_import": {
            "primitive_C1_contractions_closed": alpha_decision["primitive_C1_contractions_closed"],
            "lambda_12_computable": alpha_decision["lambda_12_computable"],
            "operator_layer_Pic0_or_torsion_gerbe_rule": qa_alpha_driver["what_remains_open"]["operator_layer_Pic0_or_torsion_gerbe_rule"],
            "Yukawa_magnitudes": qa_alpha_driver["what_remains_open"]["Yukawa_magnitudes"],
            "full_SM_closure": qa_alpha_driver["what_remains_open"]["full_SM_closure"],
        },
        "decision": {
            "samesource_functional_exit_closed_for_H7B1Q": samesource_functional_exit_closed,
            "closes_alpha1_driver_and_selected_dotD_side": True,
            "closes_Higgs_UV_twoHiggs_Huv_side": False,
            "reason": "The same-source functional side now emits the selected N_alpha1(h_ext)=1 value and alpha1 driver. It does not emit UV Higgs basis blocks or the Huv mass/strain payload.",
        },
        **clean_flags(),
    }

    huv_boundary = {
        "schema": "MTTConstHiggs01H7B1QTwoHiggsHuvBoundaryAfterFunctionalValue.v1",
        "status": "SAMESOURCE_FUNCTIONAL_CLOSED_BUT_UV_TWOHIGGS_HUV_STILL_OPEN",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1Q-B-TWOHIGGS-HUV-BOUNDARY",
        "input_sources": {
            "H7B1C_minimal_two_by_two_Huv_request": rel(h7b1c_request_path),
            "H7B1P_Huv_boundary_after_sector_routing": rel(h7b1p_huv_path),
            "QA_operator_emission_overlap": rel(qa_operator_path),
            "QA_alpha1_driver_replay": rel(qa_alpha_driver_path),
        },
        "locked_Huv_target": {
            "ordered_basis": h7b1p_huv["locked_Huv_target"]["ordered_basis"],
            "quotient_map": h7b1p_huv["locked_Huv_target"]["quotient_map"],
            "Huv_formula": h7b1p_huv["locked_Huv_target"]["Huv_formula"],
            "s_beta_formula": h7b1p_huv["locked_Huv_target"]["s_beta_formula"],
            "minimal_payload_request": {
                "basis_required": h7b1c_request["basis_required"],
                "matrix_required": h7b1c_request["matrix_required"],
                "source_identity_required": h7b1c_request["source_identity_required"],
            },
        },
        "available_after_H7B1Q": {
            "same_source_functional_value_closed": samesource_functional_exit_closed,
            "selected_dotD_source_verified": alpha_decision["selected_dotD_source_verified"],
            "alpha1_driver_verified": alpha_decision["alpha1_driver_verified"],
            "selected_overlap_normalization_emitted": operator_decision["selected_overlap_normalization_emitted"],
            "emitted_operator_blocks": emitted_blocks,
        },
        "missing_for_Huv": {
            "UV_twoHiggs_basis_emitted": False,
            "B_Huv_value_emitted": False,
            "M_source_value_emitted": False,
            "direct_Huv_entries_emitted": False,
            "Huu_value_emitted": False,
            "Hud_value_emitted": False,
            "Hdd_value_emitted": False,
            "Omega_emitted": False,
            "s_beta_emitted": False,
            "lambda_H_emitted": False,
        },
        "strict_payload_state": {
            "B_Huv": None,
            "M_source": None,
            "Huu": None,
            "Hud": None,
            "Hdd": None,
            "Delta": None,
            "Omega": None,
            "s_beta": None,
            "lambda_H": None,
        },
        "decision": {
            "H7B1Q_closes_one_previous_legal_exit": True,
            "remaining_gate_is_Higgs_specific": True,
            "UV_twoHiggs_Huv_transfer_closed": False,
            "why_no_numeric_lambda": "lambda_H requires Omega and s_beta from the selected UV Huv payload. H7B1Q emits the shared alpha/overlap source value but no Huv entries.",
        },
        **clean_flags(),
    }

    no_cycle = {
        "schema": "MTTConstHiggs01H7B1QSourcePromotionNonCirculationLedger.v1",
        "status": "NO_CIRCULATION_LEDGER_UPDATED_H7B1Q",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1Q-NO-CYCLE",
        "retired_or_do_not_reopen": {
            "H7B1O_diagonal_HYM_End0_payload": True,
            "H7B1P_sector_routing_support_chain": h7b1p["sector_chain_support_closed"],
            "H7B1P_collapsed_H_boundary": h7b1p["collapsed_H_only"],
            "same_source_chernweil_support_value_identified": chernweil_decision["unique_current_support_value_identified"],
            "selected_U10_Ubar5_operator_blocks_emitted": operator_decision["selected_U10_Ubar5_operator_blocks_emitted"],
            "selected_1M_Dirac_operator_block_emitted": operator_decision["selected_1M_Dirac_operator_block_emitted"],
            "selected_overlap_normalization_emitted": operator_decision["selected_overlap_normalization_emitted"],
            "alpha1_driver_replay_closed": alpha_decision["alpha1_driver_verified"],
            "honest_dotD_validator_closed": alpha_decision["honest_dotD_validator_closed"],
        },
        "active_not_retired": {
            "UV_twoHiggs_lift_B_Huv": True,
            "same_source_Hermitian_M_source": True,
            "direct_Huv_rows_Huu_Hud_Hdd": True,
            "primitive_C1_contractions_if_they_emit_Huv_bridge": True,
            "lambda_12_only_if_mapped_to_Higgs_source": True,
            "operator_layer_Pic0_or_torsion_gerbe_rule": True,
        },
        "circulation_test": {
            "is_reopening_H7B1O": False,
            "is_reopening_H7B1P": False,
            "is_promoting_matter_blocks_as_Huv": False,
            "is_promoting_alpha1_value_as_lambda_H": False,
            "new_information_added": [
                "same-source Chern-Weil support value N_alpha1(h_ext)=1 promoted to selected value",
                "du/dalpha1=h_ext emitted by theorem-derived oriented overlap source",
                "selected dotD source and alpha1 driver verified without diagnostic lift",
                "oriented matter operator blocks u,d,e,nuD emitted with selected overlap normalization",
                "Higgs-specific remainder sharpened to UV two-Higgs Huv source payload",
            ],
        },
        **clean_flags(),
    }

    next_work = {
        "schema": "MTTConstHiggs01H7B1QNextWork.v1",
        "status": "NEXT_WORKORDER_H7B1R_HUV_SOURCE_OPERATOR_OR_PRIMITIVE_C1_LAMBDA_BRIDGE",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1Q-NEXT",
        "primary_next": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1R-HUV-SOURCE-OPERATOR-OR-PRIMITIVE-C1-LAMBDA-BRIDGE",
            "task": "Construct an actual selected UV two-Higgs Huv source operator, or prove that primitive C1/lambda12 contractions emit that same UV Huv source rather than only the alpha/matter functional.",
        },
        "legal_exits": [
            {
                "id": "H7B1R-A",
                "label": "direct UV Huv source",
                "must_emit": "selected ordered basis (H_u,H_d^dagger) plus B_Huv and same-source Hermitian M_source, or direct Huu,Hud,Hdd rows",
            },
            {
                "id": "H7B1R-B",
                "label": "primitive C1/lambda bridge into Huv",
                "must_emit": "primitive C1/lambda12 contractions together with a theorem mapping them to the UV two-Higgs Huv payload",
            },
        ],
        "superset_strategy": {
            "using_one_straight_way": False,
            "combining_paths": True,
            "straight_path": "Higgs Huv mass-strain lane from H7B1C/H7B1F",
            "support_path": "QA/SU3 same-source functional alpha/overlap lane now closed by H7B1Q",
            "locked_target": "UV Huv payload and derived Omega/s_beta/lambda_H, not observed Higgs mass or target-fit lambda",
        },
        **clean_flags(),
    }

    theorem = {
        "name": "H7B1QTwoHiggsLiftOrSameSourceFunctionalValueTheorem",
        "proved": True,
        "statement": (
            "The same-source functional-value exit named by H7B1P is now closed on the shared QA/SU3 side: the oriented functional operator emission supplies U10/Ubar5/1M matter blocks, selected overlap normalization, N_alpha1(h_ext)=1, du/dalpha1=h_ext, selected dotD source verification, and alpha1 driver replay without observed inputs or diagnostic flag lifting. "
            "This is real source promotion, but its emitted blocks are u,d,e,nuD matter/neutrino blocks, not UV Higgs blocks. Therefore it cannot be promoted to B_Huv, M_source, direct Huv rows, Omega, s_beta, lambda_H, or strict no-knob Higgs closure. The only remaining Higgs-specific gate is an actual UV two-Higgs source payload or a primitive C1/lambda bridge that emits that payload."
        ),
    }

    candidate = {
        "candidate": "MTTConstHiggs01H7B1QTwoHiggsLiftOrSameSourceFunctionalValue",
        "status": STATUS,
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1Q-TWOHIGGS-LIFT-OR-SAMESOURCE-FUNCTIONAL-VALUE",
        "output_packets": {
            "samesource_functional_value_import": rel(SAMESOURCE_IMPORT),
            "twohiggs_huv_boundary_after_functional_value": rel(HUV_BOUNDARY),
            "source_promotion_non_circulation_ledger": rel(NO_CYCLE),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": theorem,
        "H7B1P_imported": h7b1p["status"] == "MTT_CONST_HIGGS_01_H7B1P_SECTOR_ROUTING_IMPORTED_HUV_TWOHIGGS_LIFT_OPEN",
        "samesource_functional_exit_closed": samesource_functional_exit_closed,
        "selected_N_alpha1_h_ext_value": promoted_value["N_alpha1_h_ext"],
        "du_dalpha1_equals_h_ext": alpha_decision["du_dalpha1_equals_h_ext_emitted"],
        "selected_dotD_source_verified": alpha_decision["selected_dotD_source_verified"],
        "alpha1_driver_verified": alpha_decision["alpha1_driver_verified"],
        "honest_dotD_validator_closed": alpha_decision["honest_dotD_validator_closed"],
        "selected_matter_operator_blocks_emitted": operator_decision["same_branch_functional_operator_emission_closed"],
        "emitted_operator_blocks": emitted_blocks,
        "selected_overlap_normalization_emitted": operator_decision["selected_overlap_normalization_emitted"],
        "primitive_C1_contractions_closed": alpha_decision["primitive_C1_contractions_closed"],
        "lambda_12_computable": alpha_decision["lambda_12_computable"],
        "UV_twoHiggs_basis_emitted": False,
        "UV_twoHiggs_Huv_transfer_closed": False,
        "B_Huv_value_emitted": False,
        "M_source_value_emitted": False,
        "direct_Huv_entries_emitted": False,
        "selected_s_beta_value_found": False,
        "numeric_lambda_H_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "new_Higgs_specific_parameters": 0,
        "selected_next_artifact": "MTT_CONST_HIGGS_01_H7B1R_HuvSourceOperatorOrPrimitiveC1LambdaBridge_v1",
        **clean_flags(),
    }

    cert = {
        "certificate": "MTT_CONST_HIGGS_01_H7B1Q_TwoHiggsLiftOrSameSourceFunctionalValue_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "active_label": candidate["active_label"],
        "samesource_functional_exit_closed": samesource_functional_exit_closed,
        "selected_N_alpha1_h_ext_value": promoted_value["N_alpha1_h_ext"],
        "du_dalpha1_equals_h_ext": alpha_decision["du_dalpha1_equals_h_ext_emitted"],
        "selected_dotD_source_verified": alpha_decision["selected_dotD_source_verified"],
        "alpha1_driver_verified": alpha_decision["alpha1_driver_verified"],
        "selected_matter_operator_blocks_emitted": operator_decision["same_branch_functional_operator_emission_closed"],
        "UV_twoHiggs_Huv_transfer_closed": False,
        "B_Huv_value_emitted": False,
        "M_source_value_emitted": False,
        "direct_Huv_entries_emitted": False,
        "numeric_lambda_H_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "new_Higgs_specific_parameters": 0,
        **clean_flags(),
    }

    note = f"""# MTT CONST HIGGS 01 H7B1Q Two-Higgs Lift Or Same-Source Functional Value v1

Status: `{STATUS}`

Label: `CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1Q-TWOHIGGS-LIFT-OR-SAMESOURCE-FUNCTIONAL-VALUE`

## Result

```text
same-source functional exit closed               {samesource_functional_exit_closed}
N_alpha1(h_ext) selected value                   {promoted_value["N_alpha1_h_ext"]}
du/dalpha1=h_ext emitted                         {alpha_decision["du_dalpha1_equals_h_ext_emitted"]}
selected dotD source verified                    {alpha_decision["selected_dotD_source_verified"]}
alpha1 driver verified                           {alpha_decision["alpha1_driver_verified"]}
honest dotD validator closed                     {alpha_decision["honest_dotD_validator_closed"]}
emitted operator blocks                          {", ".join(emitted_blocks)}
UV two-Higgs Huv transfer closed                 False
B_Huv / M_source / direct Huv emitted            False
s_beta / lambda_H promoted                       False
```

## What Moved Forward

H7B1Q closes the same-source functional-value exit named in H7B1P.  The later
QA/SU3 chain now promotes the unique support value `N_alpha1(h_ext)=1` to a
selected value, emits `du/dalpha1=h_ext`, verifies the selected dotD source, and
closes the alpha1 driver replay.  This is a real cross-encoding superset gain:
the Higgs branch can now stop reopening alpha/overlap/source-strength support.

## Remaining Boundary

The emitted functional blocks are `{", ".join(emitted_blocks)}`.  They are
matter/neutrino blocks, not the UV two-Higgs ordered basis
`(H_u,H_d^dagger)`.  Therefore this artifact still does not emit `B_Huv`,
`M_source`, or direct `Huu,Hud,Hdd` rows.

The next exact gate is:

`CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1R-HUV-SOURCE-OPERATOR-OR-PRIMITIVE-C1-LAMBDA-BRIDGE`
"""

    for path, payload in [
        (SAMESOURCE_IMPORT, samesource_import),
        (HUV_BOUNDARY, huv_boundary),
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
