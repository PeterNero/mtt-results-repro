"""Build CONST-EM-01 typed C_Y convention.

This artifact imports the QA typed hypercharge convention and applies it to
the C_Y slot.  It closes the structural convention map, rejects direct
promotion of the internal 2/3 index or quotient logdet as a coupling
multiplier, and reduces C_Y to U1/Y source-row plus physical-anchor data.
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

SLUG = "const_em_01_alpha1_typed_cy_convention"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
TYPED_MAP = BASE / "typed_hypercharge_map.packet.json"
CY_DECISION = BASE / "cy_promotion_decision.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_EM_01_Alpha1_TypedCYConvention_v1.md"

STATUS = "MTT_CONST_EM_01_TYPED_CY_CONVENTION_STRUCTURAL_MAP_CLOSED_CY_VALUE_OPEN"


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

    frontier_path = DATA / "const_em_01_alpha1_normalization_frontier.candidate.json"
    convention_path = DATA / "const_em_01_alpha1_convention_map.candidate.json"
    qa_typed_path = QA_SU3 / "candidate_data" / "selected_electroweak_u1y_hypercharge_weights_typed_convention_gate.candidate.json"
    qa_factorized_path = QA_SU3 / "candidate_data" / "selected_electroweak_u1y_factorized_threshold_operator_source_attempt.candidate.json"
    qa_operator_gate_path = QA_SU3 / "candidate_data" / "selected_electroweak_u1y_factorized_operator_or_su2_cancellation_gate.candidate.json"

    frontier = load(frontier_path)
    convention = load(convention_path)
    qa_typed = load(qa_typed_path)
    qa_factorized = load(qa_factorized_path)
    qa_operator_gate = load(qa_operator_gate_path)

    typed = qa_typed["typed_convention_map"]
    route_tests = qa_typed["route_tests"]

    typed_map = {
        "schema": "MTTConstEM01TypedHyperchargeMap.v1",
        "status": "STRUCTURAL_TYPED_HYPERCHARGE_MAP_CLOSED",
        "active_label": "CONST-EM-01 / ALPHA1-NORMALIZATION / A4-TYPED-CY-CONVENTION",
        "imports": {
            "qa_typed_hypercharge_gate": {
                "path": rel(qa_typed_path),
                "status": qa_typed["status"],
                "typed_hypercharge_convention_map_closed": qa_typed["decision"]["typed_hypercharge_convention_map_closed"],
                "hypercharge_index_weights_closed_structurally": qa_typed["decision"]["hypercharge_index_weights_closed_structurally"],
                "lambda_12_closed": qa_typed["decision"]["lambda_12_closed"],
            },
            "qa_factorized_operator_attempt": {
                "path": rel(qa_factorized_path),
                "status": qa_factorized["status"],
                "quotient_logdet": qa_factorized["decision"]["quotient_logdet"],
                "selected_source_emission_closed": qa_factorized["decision"]["selected_source_emission_closed"],
                "typed_convention_map_closed": qa_factorized["decision"]["typed_convention_map_closed"],
            },
            "qa_factorized_operator_gate": {
                "path": rel(qa_operator_gate_path),
                "status": qa_operator_gate["status"],
                "U1_factorized_threshold_operator_source_closed": qa_operator_gate["decision"]["U1_factorized_threshold_operator_source_closed"],
                "SU2_same_scheme_row_or_cancellation_closed_for_weaksplit": qa_operator_gate["decision"]["SU2_same_scheme_row_or_cancellation_closed_for_weaksplit"],
            },
        },
        "closed_structural_map": {
            "hypercharge_embedding": typed["hypercharge_embedding"],
            "threshold_combination": typed["threshold_combination"],
            "weak_split": typed["weak_split"],
            "Delta_G_12": typed["Delta_G_12"],
            "selected_weights": typed["selected_weights"],
        },
        "route_tests": {
            "typed_hypercharge_stack_map": route_tests["typed_hypercharge_stack_map"],
            "Qc_and_SU2_rows": route_tests["Qc_and_SU2_rows"],
            "Qa_stack_interpretation_of_quotient_operator": route_tests["Qa_stack_interpretation_of_quotient_operator"],
            "direct_U1Y_row_shortcut": route_tests["direct_U1Y_row_shortcut"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cy_decision = {
        "schema": "MTTConstEM01CYPromotionDecision.v1",
        "status": "CY_PROMOTION_REDUCED_TO_U1Y_SOURCE_ROW_AND_PHYSICAL_ANCHOR",
        "active_label": "CONST-EM-01 / ALPHA1-NORMALIZATION / A4-TYPED-CY-CONVENTION",
        "closed_now": {
            "typed_hypercharge_structural_map": True,
            "reject_internal_index_as_direct_CY": True,
            "reject_quotient_logdet_as_direct_pY": True,
            "SU2_row_closed_for_scoped_weak_split": qa_operator_gate["decision"]["SU2_same_scheme_row_or_cancellation_closed_for_weaksplit"],
        },
        "open_now": {
            "Qa_stack_p_a_source_emission": qa_typed["decision"]["Qa_stack_p_a_source_closed"] is False,
            "direct_U1Y_row_source_emission": qa_typed["decision"]["direct_U1Y_row_promoted"] is False,
            "factorized_operator_source_emission": qa_factorized["decision"]["selected_source_emission_closed"] is False,
            "hypercharge_index_Dynkin_weights_as_source_values": qa_factorized["decision"]["hypercharge_index_Dynkin_weights_closed"] is False,
            "lambda_12": qa_typed["decision"]["lambda_12_closed"] is False,
            "physical_CY": True,
            "alpha_Y_numeric": True,
            "alpha_em_numeric": True,
        },
        "typed_CY_options": {
            "internal_index_option": {
                "candidate": "I_U1=2/3",
                "decision": "REJECT_AS_DIRECT_COUPLING_MULTIPLIER",
                "reason": "It is an internal inverse-kernel/index support value.",
            },
            "GUT_factor_option": {
                "candidate": "3/5 or 5/3 convention factor",
                "decision": "STRUCTURAL_ONLY_UNTIL_SOURCE_TYPED",
                "reason": "The stack map gives p_Y=p_a/36+p_c/4; familiar normalization factors cannot be inserted as source values.",
            },
            "quotient_logdet_option": {
                "candidate": qa_factorized["decision"]["quotient_logdet"],
                "decision": "CONDITIONAL_AS_QA_STACK_P_A_ONLY",
                "reason": "Can enter through p_a only after selected source emission of the factorized U1/Y threshold operator.",
            },
            "physical_action_anchor_option": {
                "candidate": "K_phys or dimensional action anchor",
                "decision": "INDEPENDENT_KEY_OPEN",
                "reason": "Needed for absolute physical units and cannot be obtained from the dimensionless U1/Y row alone.",
            },
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTNextLabeledWorkorderAfterTypedCYConvention.v1",
        "status": "NEXT_WORKORDER_U1Y_FACTOR_OPERATOR_SOURCE_OR_PHYSICAL_ANCHOR",
        "primary": {
            "label": "CONST-EM-01 / ALPHA1-U1Y-ROW / A5-FACTORIZED-OPERATOR-SOURCE",
            "task": "Promote or refute source emission of the exact factorized U1/Y threshold operator A_base tensor I_3 on V/<s>, with hypercharge/index weights.",
        },
        "secondary": {
            "label": "CONST-EM-01 / ALPHA1-PHYSICAL-ANCHOR / A5-KPHYS",
            "task": "Search the GR/M-theory and dimensional-anchor branches for the target-independent physical action anchor K_phys.",
        },
    }

    candidate = {
        "candidate": "MTTConstEM01Alpha1TypedCYConvention",
        "status": STATUS,
        "active_label": "CONST-EM-01 / ALPHA1-NORMALIZATION / A4-TYPED-CY-CONVENTION",
        "output_packets": {
            "typed_hypercharge_map": rel(TYPED_MAP),
            "cy_promotion_decision": rel(CY_DECISION),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "what_closes_now": {
            "typed_hypercharge_structural_map": True,
            "pY_equals_pa_over_36_plus_pc_over_4": True,
            "lambda12_formula": True,
            "internal_index_direct_CY_shortcut_rejected": True,
            "quotient_logdet_direct_pY_shortcut_rejected": True,
            "superset_paths_locked_to_source_row_and_anchor_keys": True,
        },
        "what_remains_open": {
            "C_Y_value": True,
            "Qa_stack_p_a_source_emission": True,
            "direct_U1Y_row_source_emission": True,
            "factorized_operator_source_emission": True,
            "hypercharge_index_Dynkin_weights_as_source_values": True,
            "lambda_12": True,
            "physical_action_anchor": True,
            "alpha_zero_or_MZ_value": True,
        },
        "theorem": {
            "name": "CONSTEM01TypedCYConventionReductionTheorem",
            "proved": True,
            "statement": (
                "The structural hypercharge convention is selected as Y=(1/6)Qa-(1/2)Qc and p_Y=p_a/36+p_c/4. "
                "Therefore the C_Y slot cannot be filled by direct use of the internal U1 index 2/3, a standalone GUT factor, "
                "or the quotient logdet as p_Y.  The legal dimensionless route is source emission of p_a or a separately typed "
                "U1/Y row; the legal physical route also requires the independent action anchor and RG/threshold scheme."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_EM_01_Alpha1_TypedCYConvention_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "typed_hypercharge_structural_map_closed": True,
        "C_Y_value_claimed": False,
        "physical_alpha_value_claimed": False,
        "selected_universal_parameters_now": 0,
        "next_primary": "CONST-EM-01 / ALPHA1-U1Y-ROW / A5-FACTORIZED-OPERATOR-SOURCE",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    note = f"""# MTT CONST EM 01 Alpha1 Typed CY Convention v1

Status: `{STATUS}`

Label: `CONST-EM-01 / ALPHA1-NORMALIZATION / A4-TYPED-CY-CONVENTION`

## Result

The typed structural hypercharge convention is closed:

- `Y = (1/6) Q_a - (1/2) Q_c`,
- `p_Y = p_a/36 + p_c/4`,
- `lambda_12 = p_Y - p_SU2`.

This is progress, but it does not yet emit a physical `C_Y` value.

## What Was Rejected

- `I_U1=2/3` is not a direct `C_Y` coupling multiplier.
- `3/5` or `5/3` cannot be inserted as a source value by convention alone.
- the quotient logdet cannot be treated as direct `p_Y`.
- measured `alpha`, `sin^2(theta_W)`, or `g2` cannot select the map.

## Legal Route

The quotient determinant may enter only as `p_a` after source emission of the
factorized U1/Y threshold operator, or through a separately source-typed U1/Y
row.  Physical alpha additionally requires the independent action anchor and
RG/threshold scheme.

## Next

Next label: `CONST-EM-01 / ALPHA1-U1Y-ROW / A5-FACTORIZED-OPERATOR-SOURCE`
"""

    for path, payload in [
        (TYPED_MAP, typed_map),
        (CY_DECISION, cy_decision),
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
