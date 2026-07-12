"""Build CONST-EM-01 U1/Y factorized operator source gate.

This artifact attacks the next dimensionless C_Y gate: whether the concrete
factorized U1/Y threshold operator can be promoted from constructed support to
selected source emission.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
QA_SU3 = TEXPAPERS / "mtt-qa-su3-packet-proof"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_em_01_alpha1_u1y_factorized_operator_source"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
MATRIX = BASE / "factorized_operator_matrix_replay.packet.json"
SOURCE_DECISION = BASE / "source_emission_decision.packet.json"
LAMBDA_GATE = BASE / "lambda12_gate.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_EM_01_Alpha1_U1YFactorizedOperatorSource_v1.md"

STATUS = "MTT_CONST_EM_01_U1Y_FACTORIZED_OPERATOR_REPLAY_CLOSED_SOURCE_EMISSION_OPEN"


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

    typed_path = DATA / "const_em_01_alpha1_typed_cy_convention.candidate.json"
    qa_attempt_path = QA_SU3 / "candidate_data" / "selected_electroweak_u1y_factorized_threshold_operator_source_attempt.candidate.json"
    qa_matrix_path = QA_SU3 / "candidate_data" / "selected_electroweak_u1y_factorized_threshold_operator_source_attempt.matrix.json"
    qa_pperp_path = QA_SU3 / "candidate_data" / "selected_u1_quotient_projector_pperp_and_trace_policy.candidate.json"
    qa_operator_prefix_path = QA_SU3 / "candidate_data" / "selected_electroweak_u1y_operator_row_source_packet.fill_attempt.json"
    qa_typed_path = QA_SU3 / "candidate_data" / "selected_electroweak_u1y_hypercharge_weights_typed_convention_gate.candidate.json"

    typed = load(typed_path)
    attempt = load(qa_attempt_path)
    matrix_payload = load(qa_matrix_path)
    pperp = load(qa_pperp_path)
    prefix = load(qa_operator_prefix_path)
    qa_typed = load(qa_typed_path)

    matrix_checks = {
        "factorized_matrix_constructed": attempt["decision"]["factorized_operator_matrix_constructed"] is True,
        "quotient_operator_matrix_constructed": attempt["decision"]["quotient_operator_matrix_constructed"] is True,
        "factorization_matches_27mode_spectrum": attempt["decision"]["factorization_matches_27mode_spectrum"] is True,
        "raw_formula_A_base_tensor_I3": matrix_payload["raw_operator"]["formula"] == "A_base tensor I_3",
        "quotient_formula_A_base_tensor_VmodS": matrix_payload["quotient_operator"]["formula"] == "A_base tensor I_(V_3/<s>)",
        "raw_dimension_24": matrix_payload["raw_operator"]["dimension"] == 24,
        "quotient_dimension_16": matrix_payload["quotient_operator"]["dimension"] == 16,
        "quotient_multiplicities_8_8": matrix_payload["factorization_checks"]["quotient_multiplicities"] == [8, 8],
        "quotient_logdet_matches": abs(matrix_payload["quotient_operator"]["logdet"] - 29.201650332199108) < 1e-12,
        "Pperp_closed": pperp["decision"]["explicit_U1_P_perp_projector"] is True,
        "Pperp_trace_policy_closed": pperp["decision"]["U1_operator_trace_uses_P_perp"] is True,
        "operator_prefix_selected_by_mtt": attempt["source_identity"]["operator_prefix_selected_by_mtt"] is True,
        "same_source_as_27mode_gap_layer": attempt["source_identity"]["same_source_as_27mode_DE_gap_layer"] is True,
        "same_source_as_Pperp_trace_policy": attempt["source_identity"]["same_source_as_Pperp_trace_policy"] is True,
    }
    replay_closed = all(matrix_checks.values())

    source_checks = {
        "selected_source_emission_closed": attempt["decision"]["selected_source_emission_closed"] is True,
        "factorized_matrix_emitted_by_prior_source": attempt["source_identity"]["factorized_matrix_emitted_by_prior_source"] is True,
        "hypercharge_index_Dynkin_weights_closed": attempt["decision"]["hypercharge_index_Dynkin_weights_closed"] is True,
        "typed_convention_map_closed_in_attempt": attempt["decision"]["typed_convention_map_closed"] is True,
        "direct_U1Y_row_promoted": qa_typed["decision"]["direct_U1Y_row_promoted"] is True,
        "Qa_stack_p_a_source_closed": qa_typed["decision"]["Qa_stack_p_a_source_closed"] is True,
    }
    source_emission_closed = all(source_checks.values())

    matrix_packet = {
        "schema": "MTTConstEM01U1YFactorizedOperatorMatrixReplay.v1",
        "status": "FACTORIZED_OPERATOR_MATRIX_REPLAY_CLOSED" if replay_closed else "FACTORIZED_OPERATOR_MATRIX_REPLAY_OPEN",
        "active_label": "CONST-EM-01 / ALPHA1-U1Y-ROW / A5-FACTORIZED-OPERATOR-SOURCE",
        "inputs": {
            "qa_attempt": rel(qa_attempt_path),
            "qa_matrix_payload": rel(qa_matrix_path),
            "qa_pperp": rel(qa_pperp_path),
            "qa_operator_prefix": rel(qa_operator_prefix_path),
        },
        "matrix_checks": matrix_checks,
        "closed_replay_payload": {
            "raw_operator": "A_base tensor I_3",
            "quotient_operator": "A_base tensor I_(V_3/<s>)",
            "raw_dimension": matrix_payload["raw_operator"]["dimension"],
            "quotient_dimension": matrix_payload["quotient_operator"]["dimension"],
            "positive_quotient_multiplicities": attempt["constructed_operator_summary"]["positive_quotient_multiplicities"],
            "quotient_logdet": attempt["decision"]["quotient_logdet"],
            "Pperp": pperp["projector_theorem"]["P_perp"],
            "Pperp_trace": pperp["projector_theorem"]["checks"]["normalized_trace"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    source_decision = {
        "schema": "MTTConstEM01U1YFactorizedOperatorSourceEmissionDecision.v1",
        "status": "SOURCE_EMISSION_REMAINS_OPEN",
        "active_label": "CONST-EM-01 / ALPHA1-U1Y-ROW / A5-FACTORIZED-OPERATOR-SOURCE",
        "source_checks": source_checks,
        "decision": {
            "matrix_replay_closed": replay_closed,
            "source_emission_promoted": source_emission_closed,
            "selected_source_emission_closed": attempt["decision"]["selected_source_emission_closed"],
            "factorized_matrix_emitted_by_prior_source": attempt["source_identity"]["factorized_matrix_emitted_by_prior_source"],
            "hypercharge_index_Dynkin_weights_closed": attempt["decision"]["hypercharge_index_Dynkin_weights_closed"],
            "typed_convention_map_closed_in_this_repo": typed["what_closes_now"]["typed_hypercharge_structural_map"],
            "C_Y_value_claimed": False,
            "physical_alpha_value_claimed": False,
        },
        "current_exact_blocker": [
            "source theorem must emit the exact diagonal A_base tensor I_3 operator, not merely its spectrum shape",
            "source theorem must bind the operator to V/<s> with P_perp in the same U1/Y threshold row",
            "source theorem must emit hypercharge/index/Dynkin weights as selected values",
            "regularization/scale statement must identify quotient logdet row with the typed p_a or direct U1/Y row convention",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    lambda_gate = {
        "schema": "MTTConstEM01Lambda12GateAfterU1YReplay.v1",
        "status": "LAMBDA12_REDUCED_TO_SOURCE_EMISSION_NOT_NUMERIC_CLOSURE",
        "active_label": "CONST-EM-01 / ALPHA1-U1Y-ROW / A5-FACTORIZED-OPERATOR-SOURCE",
        "typed_formula": {
            "hypercharge_embedding": "Y = (1/6) Q_a - (1/2) Q_c",
            "threshold_combination": "p_Y = p_a/36 + p_c/4",
            "weak_split": "lambda_12 = p_Y - p_SU2",
        },
        "conditional_values_from_QA": {
            "conditional_p_a_if_source_emitted": qa_typed["route_tests"]["Qa_stack_interpretation_of_quotient_operator"]["conditional_p_a"],
            "conditional_p_Y_if_source_emitted": qa_typed["route_tests"]["Qa_stack_interpretation_of_quotient_operator"]["conditional_p_Y"],
            "conditional_lambda12_if_source_emitted": qa_typed["route_tests"]["Qa_stack_interpretation_of_quotient_operator"]["conditional_lambda_12"],
            "conditional_Delta_G12_if_source_emitted": qa_typed["route_tests"]["Qa_stack_interpretation_of_quotient_operator"]["conditional_Delta_G_12"],
        },
        "promoted_now": {
            "p_a": False,
            "p_Y": False,
            "lambda_12": False,
            "Delta_G12": False,
        },
        "why_not_promoted": "The conditional values depend on the still-open source emission of the factorized U1/Y threshold operator as p_a or direct U1/Y row.",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTNextLabeledWorkorderAfterU1YFactorizedOperatorReplay.v1",
        "status": "NEXT_WORKORDER_SOURCE_EMISSION_THEOREM_OR_PHYSICAL_ANCHOR",
        "primary": {
            "label": "CONST-EM-01 / ALPHA1-U1Y-ROW / A6-SOURCE-EMISSION-THEOREM",
            "task": "Construct a same-source theorem emitting the exact A_base tensor I_3 threshold operator with Pperp binding and hypercharge/index weights, or prove current-source impossibility.",
        },
        "secondary": {
            "label": "CONST-EM-01 / ALPHA1-PHYSICAL-ANCHOR / A5-KPHYS",
            "task": "Search for the independent physical action anchor K_phys in GR/M-theory/dimensional-anchor branches.",
        },
    }

    candidate = {
        "candidate": "MTTConstEM01Alpha1U1YFactorizedOperatorSource",
        "status": STATUS,
        "active_label": "CONST-EM-01 / ALPHA1-U1Y-ROW / A5-FACTORIZED-OPERATOR-SOURCE",
        "output_packets": {
            "factorized_operator_matrix_replay": rel(MATRIX),
            "source_emission_decision": rel(SOURCE_DECISION),
            "lambda12_gate": rel(LAMBDA_GATE),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "what_closes_now": {
            "factorized_operator_matrix_replay": replay_closed,
            "A_base_tensor_I3_constructed": matrix_checks["raw_formula_A_base_tensor_I3"],
            "quotient_operator_on_V_mod_s_constructed": matrix_checks["quotient_formula_A_base_tensor_VmodS"],
            "Pperp_binding_available": matrix_checks["Pperp_closed"] and matrix_checks["Pperp_trace_policy_closed"],
            "quotient_logdet_replayed": matrix_checks["quotient_logdet_matches"],
            "conditional_lambda12_values_recorded": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_source_emission_of_A_base_tensor_I3": True,
            "hypercharge_index_Dynkin_weights_as_source_values": True,
            "p_a_promotion": True,
            "p_Y_promotion": True,
            "lambda_12": True,
            "C_Y_value": True,
            "physical_action_anchor": True,
            "alpha_zero_or_MZ_value": True,
        },
        "theorem": {
            "name": "CONSTEM01U1YFactorizedOperatorReplayAndSourceEmissionNoGo",
            "proved": replay_closed,
            "statement": (
                "The concrete U1/Y factorized threshold operator replay is closed: A_base tensor I_3 has a quotient "
                "operator A_base tensor I_(V_3/<s>) with positive multiplicities 8+8 and quotient logdet "
                "29.201650332199108, with P_perp and trace policy available from the selected U1 quotient theorem. "
                "Current sources still do not emit this exact operator as the selected U1/Y threshold row with "
                "hypercharge/index/Dynkin weights, so p_a, p_Y, lambda_12, C_Y, and physical alpha remain open."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_EM_01_Alpha1_U1YFactorizedOperatorSource_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "matrix_replay_closed": replay_closed,
        "source_emission_promoted": source_emission_closed,
        "quotient_logdet": attempt["decision"]["quotient_logdet"],
        "lambda_12_claimed": False,
        "C_Y_value_claimed": False,
        "physical_alpha_value_claimed": False,
        "next_primary": "CONST-EM-01 / ALPHA1-U1Y-ROW / A6-SOURCE-EMISSION-THEOREM",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    note = f"""# MTT CONST EM 01 Alpha1 U1Y Factorized Operator Source v1

Status: `{STATUS}`

Label: `CONST-EM-01 / ALPHA1-U1Y-ROW / A5-FACTORIZED-OPERATOR-SOURCE`

## Result

The factorized U1/Y operator replay is closed:

- raw operator: `A_base tensor I_3`,
- quotient operator: `A_base tensor I_(V_3/<s>)`,
- quotient dimension: `16`,
- positive quotient multiplicities: `8+8`,
- quotient logdet: `29.201650332199108`,
- `P_perp` and U1 trace policy are available.

This does not yet promote the operator as a selected source row.

## Exact Remaining Blocker

Current sources still do not prove that the selected source emits the exact
diagonal `A_base tensor I_3` threshold operator with:

- binding to `V/<s>` and `P_perp`,
- hypercharge/index/Dynkin weights,
- finite-part regularization/scale convention,
- typed `p_a` or direct U1/Y-row status.

Therefore conditional `p_a`, `p_Y`, `lambda_12`, `C_Y`, and physical alpha
values remain unpromoted.

## Next

Next label: `CONST-EM-01 / ALPHA1-U1Y-ROW / A6-SOURCE-EMISSION-THEOREM`
"""

    for path, payload in [
        (MATRIX, matrix_packet),
        (SOURCE_DECISION, source_decision),
        (LAMBDA_GATE, lambda_gate),
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
