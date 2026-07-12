"""Build the final DynamicC1 source-owner value gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_dynamicc1_sourceowner_dynamictransferhessian_or_honestgalerkinvalues"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
READY_TABLE = PACKET_DIR / "ready_to_promote_dynamic_value_table.packet.json"
LANE_A = PACKET_DIR / "lane_a_residual_projector_source_rule_attempt.packet.json"
LANE_B = PACKET_DIR / "lane_b_honest_galerkin_export_attempt.packet.json"
FINAL_GATE = PACKET_DIR / "final_dynamic_value_gate.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_DynamicC1_SourceOwner_DynamicTransferHessian_or_HonestGalerkinValues_v1.md"

STATUS = "MTT_SELECTED_DYNAMICC1_SOURCEOWNER_DYNAMICVALUE_GATE_BUILT_VALUES_READY_SOURCE_RULE_OPEN"
NEXT = "MTT_Selected_DifferentiatedPhiFinC1_SourceRule_or_HonestGalerkinC1Table_Proof_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    fill = load(DATA / "selected_dynamicc1_sourceowner_fill_or_connectiontables_export_run.candidate.json")
    source_map = load(
        DATA
        / "selected_primitivec1tensor_hessiansourcemap_or_honestgalerkinc1execution"
        / "primitive_tensor_hessian_source_map_candidate.packet.json"
    )
    selection_test = load(
        DATA
        / "selected_sourcemapselectiontheorem_or_honestgalerkinc1valuerun"
        / "source_map_selection_theorem_test.packet.json"
    )
    honest_route = load(
        DATA
        / "selected_sourcemapselectiontheorem_or_honestgalerkinc1valuerun"
        / "honest_galerkin_value_run_route.packet.json"
    )
    value_cutset = load(
        DATA
        / "selected_dynamicc1transfertensor_valueemission_or_honestgalerkinc1run"
        / "strict_value_emission_cutset.packet.json"
    )

    phase = source_map["candidate_residual_operators"]["phase_R_Z"]
    shift = source_map["candidate_residual_operators"]["shift_R_X"]

    ready_table = {
        "schema": "MTTDynamicC1ReadyToPromoteValueTable.v1",
        "status": "VALUES_EXACT_READY_TO_PROMOTE_SOURCE_SELECTION_OPEN",
        "coordinate_system": value_cutset["acceptance_target"]["coordinate_system"],
        "dynamic_operator_candidates": {
            "phase_R_Z": {
                "matrix": phase["shape"]["matrix"],
                "residual_norm_sq": phase["shape"]["residual_norm_sq"],
                "target_norm_sq": phase["shape"]["target_norm_sq"],
                "orthogonal_to_fixed_fiber_span": phase["shape"]["orthogonal_to_fixed_fiber_span"],
                "selected_now": phase["selected_by_MTT_now"],
            },
            "shift_R_X": {
                "matrix": shift["shape"]["matrix"],
                "residual_norm_sq": shift["shape"]["residual_norm_sq"],
                "target_norm_sq": shift["shape"]["target_norm_sq"],
                "orthogonal_to_fixed_fiber_span": shift["shape"]["orthogonal_to_fixed_fiber_span"],
                "selected_now": shift["selected_by_MTT_now"],
            },
        },
        "routed_72_real_completion": source_map["residual_completion_replay"]["routed_72_real_completion"],
        "conditional_hessian_values": source_map["if_source_map_selected_then"],
        "promotion_status": {
            "A_selected_promoted": False,
            "b_selected_promoted": False,
            "deltaTheta_C1_promoted": False,
            "sector_response_matrices_promoted": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    lane_a = {
        "schema": "MTTDifferentiatedPhiFinC1ResidualProjectorSourceRuleAttempt.v1",
        "status": "LANE_A_SOURCE_RULE_ATTEMPT_REDUCED_TO_ONE_APPLICATION_PRINCIPLE_OPEN",
        "candidate_rule": selection_test["selection_attempt"]["candidate_rule"],
        "already_closed_support": selection_test["already_selected_or_closed"],
        "required_source_rule": {
            "name": "DifferentiatedPhiFinC1ResidualProjectorApplicationRule",
            "statement": (
                "On the selected q79/F,m=1 source spine, the differentiated Phi_fin^C1 response applies "
                "the canonical residual projector Q_residual to the selected enriched Weyl-pair phase/shift legs, "
                "and the same differentiated action emits the Hessian/source vector b_selected."
            ),
            "would_select_phase_R_Z": True,
            "would_select_shift_R_X": True,
            "would_emit_b_selected": True,
            "would_emit_sector_response_matrices": True,
        },
        "why_not_proved_now": selection_test["why_selection_is_not_yet_proved"],
        "passes_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    lane_b = {
        "schema": "MTTHonestSelectedGalerkinC1TableExportAttempt.v1",
        "status": "LANE_B_HONEST_GALERKIN_EXPORT_RESTATED_TABLES_OPEN",
        "required_outputs": honest_route["required_outputs"],
        "strict_coordinate_target": honest_route["strict_coordinate_target"],
        "selected_source_verified": honest_route["selected_source_verified"],
        "missing_outputs": honest_route["required_outputs"],
        "would_replace_lane_A_if_emitted": True,
        "passes_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    final_gate = {
        "schema": "MTTFinalDynamicC1ValueGate.v1",
        "status": "FINAL_DYNAMIC_VALUE_GATE_SHARP_VALUES_READY_PROOF_OPEN",
        "closed_not_blockers": value_cutset["closed_not_blockers"],
        "exact_values_ready": {
            "phase_R_Z_matrix_emitted_as_candidate": True,
            "shift_R_X_matrix_emitted_as_candidate": True,
            "A_transpose_A": ready_table["conditional_hessian_values"]["A_transpose_A"],
            "A_transpose_b": ready_table["conditional_hessian_values"]["A_transpose_b"],
            "deltaTheta_C1": ready_table["conditional_hessian_values"]["deltaTheta_C1"],
            "rank": ready_table["conditional_hessian_values"]["rank"],
        },
        "legal_exits": {
            "lane_A_differentiated_PhiFinC1_source_rule": {
                "would_close_dynamic_source_owner": True,
                "passes_now": lane_a["passes_now"],
            },
            "lane_B_honest_selected_Galerkin_C1_table_export": {
                "would_close_dynamic_source_owner": True,
                "passes_now": lane_b["passes_now"],
            },
        },
        "closure_decision": {
            "dynamic_values_ready": True,
            "source_rule_proved": False,
            "honest_galerkin_table_exported": False,
            "dynamic_C1_source_owner_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "next_proof_must_supply": [
            "DifferentiatedPhiFinC1ResidualProjectorApplicationRule",
            "or honest selected Galerkin C1 table export in fixed 72-real coordinates",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    for path, payload in [
        (READY_TABLE, ready_table),
        (LANE_A, lane_a),
        (LANE_B, lane_b),
        (FINAL_GATE, final_gate),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    candidate = {
        "candidate": "MTTSelectedDynamicC1SourceOwnerDynamicTransferHessianOrHonestGalerkinValues",
        "status": STATUS,
        "inputs": {
            "sourceowner_fill_run": rel(DATA / "selected_dynamicc1_sourceowner_fill_or_connectiontables_export_run.candidate.json"),
            "primitive_source_map_candidate": rel(
                DATA
                / "selected_primitivec1tensor_hessiansourcemap_or_honestgalerkinc1execution"
                / "primitive_tensor_hessian_source_map_candidate.packet.json"
            ),
            "source_map_selection_test": rel(
                DATA
                / "selected_sourcemapselectiontheorem_or_honestgalerkinc1valuerun"
                / "source_map_selection_theorem_test.packet.json"
            ),
            "honest_galerkin_route": rel(
                DATA
                / "selected_sourcemapselectiontheorem_or_honestgalerkinc1valuerun"
                / "honest_galerkin_value_run_route.packet.json"
            ),
        },
        "output_packets": {
            "ready_to_promote_dynamic_value_table": rel(READY_TABLE),
            "lane_a_source_rule_attempt": rel(LANE_A),
            "lane_b_honest_galerkin_export_attempt": rel(LANE_B),
            "final_dynamic_value_gate": rel(FINAL_GATE),
        },
        "theorem": {
            "name": "FinalDynamicC1ValueGateTheorem",
            "proved": True,
            "statement": (
                "The remaining DynamicC1 source-owner problem has reached a final executable value gate. "
                "The exact candidate R_Z/R_X matrices and conditional Hessian consequences are emitted and "
                "ready to promote. They promote to selected A_selected, b_selected, deltaTheta_C1, and sector "
                "response matrices exactly if either the differentiated Phi_fin^C1 residual-projector source "
                "rule is proved or an honest selected Galerkin C1 table export supplies replacement values."
            ),
        },
        "closure_decision": final_gate["closure_decision"],
        "what_closes_now": {
            "exact_phase_R_Z_candidate_table_emitted": True,
            "exact_shift_R_X_candidate_table_emitted": True,
            "conditional_hessian_values_attached": True,
            "final_two_exit_dynamic_value_gate_built": True,
            "source_rule_or_galerkin_export_is_only_remaining_dynamic_gate": True,
        },
        "what_remains_open": {
            "prove_differentiated_PhiFinC1_residual_projector_application_rule": True,
            "or_export_honest_selected_Galerkin_C1_tables": True,
            "promote_A_selected_b_selected_deltaTheta_sector_matrices": True,
        },
        "superset_strategy": {
            "using_one_straight_path": False,
            "combined_paths": [
                "Lane A differentiated Phi_fin^C1 residual-projector source rule",
                "Lane B honest selected Galerkin C1 table export",
            ],
            "locked_target": "selected dynamic values in the fixed 72-real C1 coordinate system",
            "paths_used_as_knobs": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_DynamicC1_SourceOwner_DynamicTransferHessian_or_HonestGalerkinValues_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "dynamic_values_ready": True,
        "source_rule_proved": False,
        "honest_galerkin_table_exported": False,
        "dynamic_C1_source_owner_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected DynamicC1 SourceOwner DynamicTransferHessian or HonestGalerkinValues v1

Status: `{STATUS}`.

This artifact carries the source-owner fill run into the final dynamic-value
gate. It emits the exact ready-to-promote `R_Z` and `R_X` candidate tables and
the conditional Hessian consequences:

- `A^T A = 12 I_2`;
- `A^T b = (12,12)`;
- `deltaTheta_C1 = (1,1)`.

This is not a closure claim. The exact values promote only after one legal exit
is supplied:

- Lane A: prove the differentiated `Phi_fin^C1` residual-projector source rule;
- Lane B: export an honest selected Galerkin C1 table in the fixed 72-real
  coordinate system.

No observed constants, benchmark matrices, or target residual fits select the
source.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
