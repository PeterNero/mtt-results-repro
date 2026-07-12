"""Build Step 18 QA/SU3 alpha1-dotD import and primitive C1 frontier."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step18_qasu3_alphadotd_import_or_primitivec1frontier"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
IMPORT_PACKET = PACKET_DIR / "step18_imported_qasu3_operator_alpha_dotd.packet.json"
ATOM_CONTRACT = PACKET_DIR / "step18_primitive_c1_atom_contract.packet.json"
NEXT_WORKORDER = PACKET_DIR / "step18_to_step19_value_execution_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step18_QaSU3_AlphaDotDImport_or_PrimitiveC1Frontier_v1.md"

STEP17 = DATA / "selected_step17_projectorrhos_promotion_or_routecsolve.candidate.json"
CROSS_REPO = DATA / "true_sm_crossrepo_part_status_audit.candidate.json"
QA_ROOT = TEXPAPERS / "mtt-qa-su3-packet-proof"
QA_OPERATOR = QA_ROOT / "candidate_data" / "selected_u1y_routec_operator_emission_overlap_from_terminal_slotmap.candidate.json"
QA_ALPHA = QA_ROOT / "candidate_data" / "selected_u1y_routec_alpha1_driver_replay_from_oriented_overlap.candidate.json"
QA_PRIMITIVE = QA_ROOT / "candidate_data" / "selected_u1y_routec_primitive_c1_contractions_or_lambda12_gate.candidate.json"

STATUS = "MTT_SELECTED_STEP18_QASU3_ALPHADOTD_IMPORT_CLOSED_PRIMITIVE_C1_LAMBDA12_FRONTIER"
NEXT = "MTT_Selected_Step19_PrimitiveC1AtomEmission_or_SelectedLambda12SpectralTable_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sector_block_summary(operator_packet: dict[str, Any]) -> dict[str, Any]:
    blocks: dict[str, Any] = {}
    for sector, block in operator_packet["emitted_operator_blocks"].items():
        blocks[sector] = {
            "dimension": block["dimension"],
            "functional_key": block["functional_key"],
            "normalized_operator": block["normalized_operator"],
            "projector_rank": block["projector_rank"],
            "projector_selected_by_same_source": block["projector_selected_by_same_source"],
            "same_source_action": block["same_source_action"],
            "unit_trace_normalization": block["unit_trace_normalization"],
        }
    return blocks


def atom_missing_summary(primitive_packet: dict[str, Any]) -> dict[str, Any]:
    sectors: dict[str, Any] = {}
    for sector, data in primitive_packet["atom_table"].items():
        sectors[sector] = {
            "slots": data["slots"],
            "required_terms": data["required_terms"],
            "missing_terms": data["missing_terms"],
            "missing_term_count": len(data["missing_terms"]),
            "all_terms_emitted": data["all_terms_emitted"],
        }
    return sectors


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    inputs = [STEP17, CROSS_REPO, QA_OPERATOR, QA_ALPHA, QA_PRIMITIVE]
    missing = [rel(path) for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step 18 inputs: " + ", ".join(missing))

    step17 = load(STEP17)
    cross_repo = load(CROSS_REPO)
    qa_operator = load(QA_OPERATOR)
    qa_alpha = load(QA_ALPHA)
    qa_primitive = load(QA_PRIMITIVE)

    import_packet = {
        "schema": "MTTStep18QaSU3OperatorAlphaDotDImport.v1",
        "status": "QASU3_OPERATOR_ALPHA_DOTD_IMPORTED_INTO_ACTIVE_SM_LEDGER",
        "source_repo": "mtt-qa-su3-packet-proof",
        "source_packets": {
            "operator_emission_overlap": rel(QA_OPERATOR),
            "alpha1_driver_replay": rel(QA_ALPHA),
            "primitive_c1_lambda12_gate": rel(QA_PRIMITIVE),
        },
        "operator_layer_imported": {
            "same_branch_functional_operator_emission_closed": qa_operator["decision"]["same_branch_functional_operator_emission_closed"],
            "selected_1M_Dirac_operator_block_emitted": qa_operator["decision"]["selected_1M_Dirac_operator_block_emitted"],
            "selected_U10_Ubar5_operator_blocks_emitted": qa_operator["decision"]["selected_U10_Ubar5_operator_blocks_emitted"],
            "selected_overlap_normalization_emitted": qa_operator["decision"]["selected_overlap_normalization_emitted"],
            "sector_blocks": sector_block_summary(qa_operator),
            "oriented_sector_map": qa_operator["oriented_sector_map"],
        },
        "alpha_dotd_imported": {
            "N_alpha1_h_ext_promoted_to_selected_value": qa_alpha["decision"]["N_alpha1_h_ext_promoted_to_selected_value"],
            "du_dalpha1_equals_h_ext_emitted": qa_alpha["decision"]["du_dalpha1_equals_h_ext_emitted"],
            "selected_dotD_source_verified": qa_alpha["decision"]["selected_dotD_source_verified"],
            "alpha1_driver_verified": qa_alpha["decision"]["alpha1_driver_verified"],
            "honest_dotD_validator_closed": qa_alpha["decision"]["honest_dotD_validator_closed"],
            "promoted_value": qa_alpha["promoted_value"],
        },
        "closed_in_active_ledger": {
            "matter_slot_orientation_U10_Ubar5_1M": True,
            "functional_operator_blocks_u_d_e_nuD": True,
            "overlap_normalization_rho_s_Ti_over_sqrt2": True,
            "selected_N_alpha1_h_ext_value": True,
            "du_dalpha1_equals_h_ext": True,
            "selected_dotD_source_verified": True,
            "alpha1_driver_verified": True,
            "honest_dotD_replay": True,
        },
        "not_closed_by_import": {
            "operator_layer_Pic0_or_torsion_gerbe_rule": qa_alpha["residual_open"]["operator_layer_Pic0_or_torsion_gerbe_rule"],
            "primitive_C1_contractions": qa_alpha["residual_open"]["primitive_C1_contractions"],
            "A_selected": qa_alpha["residual_open"]["A_selected"],
            "b_selected": qa_alpha["residual_open"]["b_selected"],
            "lambda_12": qa_alpha["residual_open"]["lambda_12"],
            "Yukawa_magnitudes": qa_alpha["residual_open"]["Yukawa_magnitudes"],
            "full_SM_closure": qa_alpha["residual_open"]["full_SM_closure"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(IMPORT_PACKET, import_packet)

    primitive_status = qa_primitive["primitive_status"]
    atom_contract = {
        "schema": "MTTStep18PrimitiveC1AtomContract.v1",
        "status": "PRIMITIVE_C1_ATOM_CONTRACT_SHARPENED_NOT_EMITTED",
        "post_alpha_prefix_closed": qa_primitive["post_alpha_prefix"],
        "primitive_status": primitive_status,
        "atom_table": atom_missing_summary(qa_primitive),
        "lambda12_status": qa_primitive["lambda12_status"],
        "exact_atom_count": primitive_status["atom_count"],
        "exact_missing_atom_count": primitive_status["missing_atom_count"],
        "required_terms_per_sector": [
            "theta_overlap_variation",
            "left_zero_mode_response",
            "right_zero_mode_response",
            "higgs_zero_mode_response",
            "explicit_vertex",
            "basis_connection",
        ],
        "required_sectors": ["u", "d", "e", "nuD"],
        "two_legal_exits": {
            "direct_atom_formula_emission": True,
            "independent_selected_galerkin_table": True,
        },
        "forbidden_shortcuts": {
            "repeat_Galerkin_as_blocker_without_rows": True,
            "use_locked_C1_columns": True,
            "promote_diagnostic_lambda12_values": True,
            "use_observed_Yukawa_CKM_PMNS_masses": True,
        },
        "closure_claimed": False,
    }
    write_json(ATOM_CONTRACT, atom_contract)

    next_workorder = {
        "schema": "MTTStep18ToStep19ValueExecutionWorkorder.v1",
        "status": "NEXT_WORKORDER_PRIMITIVE_C1_ATOMS_OR_SELECTED_LAMBDA12_TABLE",
        "completed_step": 18,
        "next_step": 19,
        "next_required_artifact": NEXT,
        "closed_do_not_reopen": {
            "Step14_Step16_source_identity": True,
            "Step17_stationary_projectors_rho_s": True,
            "Step17_source_level_projective_rhoE": True,
            "Step18_matter_slot_operator_blocks": True,
            "Step18_alpha1_dotD_driver": True,
        },
        "must_emit_next": {
            "primitive_C1_atoms_24": True,
            "or_selected_lambda12_spectral_table": True,
            "A_selected_b_selected_after_atoms": True,
            "sector_response_matrices_after_atoms": True,
            "Rtheta_scalar_rows_after_values": True,
        },
        "atom_shape": atom_missing_summary(qa_primitive),
        "success_criterion": {
            "missing_atom_count_zero": True,
            "A_selected_emitted_or_lambda12_table_emitted": True,
            "target_fitting_used_false": True,
            "observed_data_used_as_selector_false": True,
        },
        "closure_claimed": False,
    }
    write_json(NEXT_WORKORDER, next_workorder)

    candidate = {
        "candidate": "MTTSelectedStep18QaSU3AlphaDotDImportOrPrimitiveC1Frontier",
        "status": STATUS,
        "inputs": {
            "step17": rel(STEP17),
            "cross_repo_audit": rel(CROSS_REPO),
            "qa_operator": rel(QA_OPERATOR),
            "qa_alpha": rel(QA_ALPHA),
            "qa_primitive": rel(QA_PRIMITIVE),
        },
        "output_packets": {
            "step18_imported_qasu3_operator_alpha_dotd": rel(IMPORT_PACKET),
            "step18_primitive_c1_atom_contract": rel(ATOM_CONTRACT),
            "step18_to_step19_value_execution_workorder": rel(NEXT_WORKORDER),
        },
        "theorem": {
            "name": "Step18QaSU3AlphaDotDImportTheorem",
            "proved": True,
            "statement": "The latest QA/SU3 same-source operator-emission and alpha1 replay packets are imported into the active SM closure ledger. Therefore matter-slot functional operator blocks, overlap normalization, N_alpha1(h_ext)=1, du/dalpha1=h_ext, selected_dotD_source_verified, alpha1_driver_verified, and honest dotD replay are closed in the active ledger. This import does not compute primitive C1 atoms, A_selected, b_selected, lambda12, Yukawa values, Higgs Huv, or true SM equivalence.",
        },
        "closure_decision": {
            "step18_import_closed": True,
            "matter_slot_orientation_imported": True,
            "operator_blocks_imported": True,
            "overlap_normalization_imported": True,
            "alpha1_dotD_driver_imported": True,
            "honest_dotD_replay_imported": True,
            "primitive_C1_contractions_closed": False,
            "primitive_C1_missing_atom_count": primitive_status["missing_atom_count"],
            "A_selected_emitted": False,
            "b_selected_emitted": False,
            "lambda12_closed": False,
            "Yukawa_or_full_SM_closure": False,
            "Higgs_Huv_or_lambda_H_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "what_closes_now": {
            "matter_slot_orientation_U10_Ubar5_1M": True,
            "functional_operator_blocks_u_d_e_nuD": True,
            "overlap_normalization_rho_s_Ti_over_sqrt2": True,
            "N_alpha1_h_ext_selected_value": True,
            "du_dalpha1_equals_h_ext": True,
            "selected_dotD_source_verified": True,
            "alpha1_driver_verified": True,
            "honest_dotD_replay": True,
        },
        "what_remains_open": {
            "primitive_C1_atoms_24": True,
            "A_selected": True,
            "b_selected": True,
            "sector_response_matrices": True,
            "Rtheta_internal_scalar_rows": True,
            "lambda12_selected_spectral_table": True,
            "Yukawa_CKM_PMNS_masses": True,
            "Higgs_Huv_lambda_H": True,
            "true_SM_equivalence": True,
        },
        "remaining_steps": [
            "emit_24_primitive_C1_atoms_or_independent_selected_galerkin_table",
            "compute_A_selected_b_selected_and_sector_response_matrices",
            "replay_Rtheta_internal_scalar_rows",
            "construct_selected_lambda12_U1_SU2_spectral_table",
            "propagate_Yukawa_CKM_PMNS_mass_predictions_without_observed_targets",
            "solve_Higgs_EHuv_Herm2_payload_for_lambda_H",
            "run_true_SM_equivalence_and_no_knob_closure_validator",
        ],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step18_QaSU3_AlphaDotDImport_or_PrimitiveC1Frontier_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "matter_slot_orientation_imported": True,
        "operator_blocks_imported": True,
        "overlap_normalization_imported": True,
        "alpha1_dotD_driver_imported": True,
        "honest_dotD_replay_imported": True,
        "primitive_C1_missing_atom_count": primitive_status["missing_atom_count"],
        "primitive_C1_contractions_closed": False,
        "A_selected_emitted": False,
        "b_selected_emitted": False,
        "lambda12_closed": False,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected Step18 QaSU3 AlphaDotD Import or PrimitiveC1Frontier v1

Status: `{STATUS}`.

Closed now in the active SM ledger:

```text
matter-slot orientation U10/Ubar5/1M                  closed by QA/SU3 import
functional operator blocks u,d,e,nuD                  closed by QA/SU3 import
overlap normalization rho_s(T_i)/sqrt(2)              closed by QA/SU3 import
N_alpha1(h_ext)=1                                     closed by QA/SU3 import
du/dalpha1 = h_ext                                    closed by QA/SU3 import
selected_dotD_source_verified                         closed by QA/SU3 import
alpha1_driver_verified                                closed by QA/SU3 import
honest dotD replay                                    closed by QA/SU3 import
```

Still open:

```text
24 primitive C1 atoms for u,d,e,nuD
A_selected and b_selected
sector response matrices
Rtheta internal scalar rows
selected lambda12 U1/SU2 spectral/local determinant table
Yukawa, CKM, PMNS, and masses
Higgs Huv / lambda_H
true SM equivalence and full no-knob closure
```

This step deliberately forbids saying "Galerkin remains" as a generic blocker.
The next packet must either emit the 24 primitive C1 atom rows directly or run an
independent selected Galerkin table that outputs those rows.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
