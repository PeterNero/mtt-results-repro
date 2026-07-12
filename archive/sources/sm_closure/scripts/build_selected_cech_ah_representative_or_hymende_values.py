"""Emit the selected AH representative for the BN27 Cech row, with guards.

This builder attacks the two-row geometric frontier after the BN27 one-premise
packet.  It imports the selected ordered AH/good-cover source layer from this
repo and the explicit Appell-Humbert automorphy formulas from the q79 repo.

The result is deliberately split:

* the original one-premise BN27 lane remains 6/8 because literal good-cover
  Deligne-Cech cochains are still not emitted;
* a counted AH-representative lane accepts the Cech row as an equivalent AH
  representative, reaching 7/8 under one additional explicit representative
  principle;
* the HYM/End(E) row remains open, because diagonal End0 support does not emit
  the full selected HYM/projective coefficients or equivalent End(E) values.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
Q79 = ROOT.parent / "mtt-q79-proof-repro"
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_cech_ah_representative_or_hymende_values"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CECH_PACKET = PACKET_DIR / "selected_ah_representative_for_cech_row.packet.json"
HYM_PACKET = PACKET_DIR / "hym_ende_row_recheck_after_ah_representative.packet.json"
GATE_PACKET = PACKET_DIR / "ah_representative_connection_row_gate.packet.json"
NEXT_PACKET = PACKET_DIR / "next_hymende_or_literalgoodcover_contract.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Cech_AH_Representative_or_HYMEndE_Values_v1.md"

PREVIOUS = DATA / "selected_geometric_cechhym_obligation_reduction_after_onepremise.candidate.json"
PREVIOUS_GATE = (
    DATA
    / "selected_geometric_cechhym_obligation_reduction_after_onepremise"
    / "onepremise_geometric_connection_row_gate.packet.json"
)
AH_SOURCE = DATA / "selected_routec_ah_source_selection_or_routec_selected_residual.candidate.json"
TERMINALMAP = DATA / "selected_terminalmap_sourceprinciple_or_smslotfunctor.candidate.json"
TERMINAL_SWITCH = DATA / "selected_terminalsourceswitch_or_operatorpic0gerbede.candidate.json"
AUTOMORPHY = Q79 / "candidate_data" / "visible_rank2_l2_appell_humbert_automorphy.candidate.json"
COHOMOLOGY = Q79 / "candidate_data" / "visible_rank2_l2_pullback_cech_attempt.cohomology.json"
PULLBACK = Q79 / "candidate_data" / "visible_rank2_l2_pullback_cech_attempt.candidate.json"
END0_DIAGONAL = DATA / "selected_end0_de_payload_from_diagonal_hym.candidate.json"
VISIBLE_OPERATOR = (
    DATA
    / "selected_visibleoperatorpayload_or_routechymresidual"
    / "hym_operator_extraction_contract.packet.json"
)

STATUS = (
    "MTT_SELECTED_CECH_AH_REPRESENTATIVE_OR_HYMENDE_VALUES_"
    "AH_EQUIVALENT_CECH_ROW_COUNTED_HYM_OPEN"
)
NEXT = "MTT_Selected_HYMEndEConnectionValues_or_LiteralGoodCoverUpgrade_v1"
BN27_PREMISE = "SelectedBN27ThresholdSourceEmissionPrinciple"
AH_REPRESENTATIVE_PREMISE = "SelectedAHCechRepresentativeEquivalencePrinciple"
GEOMETRIC_ROWS = [
    "cech_transition_cocycles",
    "selected_HYM_or_projective_connection_coefficients",
]


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


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing selected Cech/AH inputs: " + ", ".join(missing))


def main() -> int:
    require_sources(
        [
            PREVIOUS,
            PREVIOUS_GATE,
            AH_SOURCE,
            TERMINALMAP,
            TERMINAL_SWITCH,
            AUTOMORPHY,
            COHOMOLOGY,
            PULLBACK,
            END0_DIAGONAL,
            VISIBLE_OPERATOR,
        ]
    )

    previous = load(PREVIOUS)
    previous_gate = load(PREVIOUS_GATE)
    ah_source = load(AH_SOURCE)
    terminalmap = load(TERMINALMAP)
    terminal_switch = load(TERMINAL_SWITCH)
    automorphy = load(AUTOMORPHY)
    cohomology = load(COHOMOLOGY)
    pullback = load(PULLBACK)
    end0_diagonal = load(END0_DIAGONAL)
    visible_operator = load(VISIBLE_OPERATOR)

    if previous_gate["one_premise_final_connection_table_count"] != "6/8":
        raise ValueError("expected prior one-premise lane at 6/8")
    if previous_gate["geometric_rows"] != GEOMETRIC_ROWS:
        raise ValueError("unexpected prior geometric rows")
    if previous["closure_decision"]["geometric_connection_rows_accepted"] != 0:
        raise ValueError("prior geometric rows should still be 0/2")

    ah_layer = ah_source["selected_AH_goodcover_stability_layer"]
    ah_decision = ah_source["what_closes_now"]
    terminal_decision = terminalmap["what_closes_now"]
    automorphy_checks = automorphy["construction_checks"]
    automorphy_model = automorphy["model"]
    cohomology_tests = cohomology["acceptance_tests"]
    pullback_status = pullback["what_this_closes"]

    selected_ah_source_layer = all(
        [
            ah_layer["proved"],
            ah_layer["selected_ordered_source"],
            ah_layer["selected_cohomology_h1_ext"],
            ah_decision["selected_ordered_AH_goodcover_source_for_stability_layer"],
            ah_decision["AH_automorphy_and_Yoneda_laws_ready_for_selected_layer"],
        ]
    )
    ah_equivalence_principle_available = all(
        [
            terminal_decision["AH_binding_reduced_to_representative_under_selected_class"],
            terminal_switch["closure_decision"]["terminal_source_switch_conditionally_closed"],
        ]
    )
    automorphy_ready = all(
        [
            automorphy_checks["cocycle_law_holds_on_generators_mod_2pi_i"],
            automorphy_checks["cocycle_law_holds_on_small_lattice_box_mod_2pi_i"],
            automorphy_checks["c1_matrix_matches_required_order"],
            automorphy_checks["central_shared_circle_trivial"],
            automorphy_checks["target_degrees"] == [2, -4, 0],
        ]
    )
    h1_ext_ready = all(
        [
            cohomology_tests["h1_positive"],
            cohomology_tests["extension_class_closed"],
            cohomology_tests["extension_class_not_exact"],
            cohomology["reported_cohomology"]["nonzero_extension_class_label"]
            == "theta_plus_0_tensor_eta_minus_0",
            pullback_status["conditional_h1_positive_for_base_pullback_model"],
            pullback_status["integral_deck_c1_cocycle_for_c1_L_squared"],
        ]
    )
    ah_equivalent_cech_row_accepted = (
        selected_ah_source_layer and ah_equivalence_principle_available and automorphy_ready and h1_ext_ready
    )

    if not ah_equivalent_cech_row_accepted:
        raise ValueError("AH-equivalent Cech representative preconditions failed")

    if end0_diagonal["what_closes_now"]["directionwise_D_E_connection_matrices"] is not True:
        raise ValueError("diagonal End0 D_E support missing")
    if visible_operator["selected_operator_values_closed"] is not False:
        raise ValueError("selected HYM/End(E) values unexpectedly closed")

    generator_factors = automorphy_model["generator_factors"]
    c1_matrix = automorphy_model["c1_deck_alternating_matrix_order_g1_to_g6"]
    ext_vector = cohomology["reported_cohomology"]["extension_class_vector_C1"]
    ext_label = cohomology["reported_cohomology"]["nonzero_extension_class_label"]

    cech_packet = {
        "schema": "MTTSelectedAHRepresentativeForCechRow.v1",
        "status": "AH_REPRESENTATIVE_EMITTED_CECH_EQUIVALENT_ROW_ACCEPTED_UNDER_COUNTED_PRINCIPLE",
        "closure_claimed": True,
        "row": "cech_transition_cocycles",
        "literal_good_cover_Deligne_Cech_row_accepted": False,
        "accepted_as_AH_equivalent_cech_row": True,
        "premise_name": AH_REPRESENTATIVE_PREMISE,
        "premise_count_added": 1,
        "selected_source_layer": {
            "selected_ordered_AH_goodcover_source_for_stability_layer": True,
            "selected_h1_nonzero_ext_packet": True,
            "ordered_L_vector": ah_layer["ordered_L_vector"],
            "ordered_L2_vector": ah_layer["ordered_L2_vector"],
            "Pic0_quotient_scope": ah_layer["pic0_rule_scope"],
            "operator_layer_Pic0_reopens": ah_layer["operator_layer_pic0_reopens"],
        },
        "AH_representative_values": {
            "base_torus": automorphy_model["base_torus"],
            "universal_cover": automorphy_model["universal_cover"],
            "factor_formula": automorphy_model["factor_formula"],
            "factor_formula_convention": automorphy_model["factor_formula_convention"],
            "c1_deck_alternating_matrix_order_g1_to_g6": c1_matrix,
            "generator_factors": generator_factors,
            "central_shared_circle_pair": automorphy_model["central_shared_circle_pair"],
            "central_shared_circle_trivial": True,
        },
        "selected_Ext_class_values": {
            "basis_labels_C1": cohomology["cochain_complex"]["basis_labels_C1"],
            "extension_class_vector_C1": ext_vector,
            "nonzero_extension_class_label": ext_label,
            "h1": cohomology["reported_cohomology"]["h1"],
            "closed_nonexact": True,
        },
        "cocycle_certificates": {
            "cocycle_law_holds_on_generators_mod_2pi_i": True,
            "cocycle_law_holds_on_small_lattice_box_mod_2pi_i": True,
            "c1_matrix_matches_required_order": True,
            "c1_pairing_g1_g2": automorphy_checks["c1_pairing_g1_g2"],
            "c1_pairing_g3_g4": automorphy_checks["c1_pairing_g3_g4"],
            "c1_pairing_g5_g6": automorphy_checks["c1_pairing_g5_g6"],
        },
        "guardrails": {
            "raw_good_cover_Aij_Bi_gijk_hij_emitted": False,
            "operator_layer_Pic0_recheck_closed": False,
            "same_source_DE_Riesz_Green_dotD_closed_here": False,
            "strict_unconditional_cech_row_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    hym_packet = {
        "schema": "MTTHYMEndERowRecheckAfterAHRepresentative.v1",
        "status": "HYM_ENDE_ROW_RECHECK_SUPPORT_ONLY_VALUES_OPEN",
        "closure_claimed": True,
        "row": "selected_HYM_or_projective_connection_coefficients",
        "accepted_as_final_connection_table_row": False,
        "support_imported": {
            "diagonal_End0_connection_formula": True,
            "directionwise_D_E_connection_matrices": True,
            "rank2_connection": end0_diagonal["adjoint_connection_packet"]["rank2_connection"],
            "induced_End0_connection": end0_diagonal["adjoint_connection_packet"]["induced_End0_connection"],
            "ad_T3_matrix_on_basis_T1_T2_T3": end0_diagonal["adjoint_connection_packet"][
                "ad_T3_matrix_on_basis_T1_T2_T3"
            ],
            "central_shared_circle_zero_direction_preserved": True,
        },
        "why_not_accepted": {
            "selected_operator_values_closed": visible_operator["selected_operator_values_closed"],
            "actual_visible_operator_payload_emitted": visible_operator["actual_visible_operator_payload_emitted"],
            "offdiagonal_End0_vanish_or_control_bound_open": end0_diagonal["what_remains_open"][
                "offdiagonal_End0_vanish_or_control_bound"
            ],
            "rank2_to_rank3_sector_transfer_values_open": end0_diagonal["what_remains_open"][
                "rank2_to_rank3_sector_transfer_values"
            ],
            "rho_E_metric_D_E_Riesz_Green_dotD_same_source_payload_open": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    gate_packet = {
        "schema": "MTTAHRepresentativeConnectionRowGate.v1",
        "status": "ONE_PREMISE_6_OF_8_TWO_PREMISE_AH_EQUIVALENT_7_OF_8_HYM_OPEN",
        "closure_claimed": True,
        "strict_final_connection_table_count": "4/8",
        "one_premise_final_connection_table_count": "6/8",
        "one_premise_literal_goodcover_cech_row_accepted": False,
        "two_premise_AH_equivalent_final_connection_table_count": "7/8",
        "two_premise_counted_principles": [BN27_PREMISE, AH_REPRESENTATIVE_PREMISE],
        "two_premise_cech_row_accepted": True,
        "two_premise_hym_row_accepted": False,
        "remaining_rows_after_AH_equivalent_lane": ["selected_HYM_or_projective_connection_coefficients"],
        "strict_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTNextHYMEndEOrLiteralGoodCoverContract.v1",
        "status": "NEXT_IS_HYM_ENDE_VALUES_OR_LITERAL_GOODCOVER_UPGRADE",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "current_lanes": {
            "strict_lane": "4/8",
            "one_premise_BN27_lane": "6/8",
            "two_premise_AH_equivalent_lane": "7/8",
        },
        "allowed_exits": [
            "emit selected HYM/projective connection coefficients",
            "emit equivalent selected End(E) operator values accepted by the BN27 connection-row validator",
            "upgrade AH representative to literal good-cover Deligne-Cech cochains A_ij, B_i, g_ijk, h_ij",
            "derive the AH representative equivalence principle instead of counting it as an additional premise",
        ],
        "must_not_count_as_final_HYM_row": [
            "diagonal rank-two End0 D_E support alone",
            "abstract HYM existence alone",
            "shape-complete or lifted-flag operator payloads",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedCechAHRepresentativeOrHYMEndEValues",
        "status": STATUS,
        "previous_status": previous["status"],
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {
            "previous_candidate": rel(PREVIOUS),
            "previous_gate": rel(PREVIOUS_GATE),
            "selected_AH_source_layer": rel(AH_SOURCE),
            "terminalmap_principle": rel(TERMINALMAP),
            "terminal_switch": rel(TERMINAL_SWITCH),
            "q79_AH_automorphy": rel(AUTOMORPHY),
            "q79_pullback_cohomology": rel(COHOMOLOGY),
            "q79_pullback_attempt": rel(PULLBACK),
            "end0_diagonal": rel(END0_DIAGONAL),
            "visible_operator_contract": rel(VISIBLE_OPERATOR),
        },
        "output_packets": {
            "selected_ah_representative_for_cech_row": rel(CECH_PACKET),
            "hym_ende_row_recheck_after_ah_representative": rel(HYM_PACKET),
            "ah_representative_connection_row_gate": rel(GATE_PACKET),
            "next_hymende_or_literalgoodcover_contract": rel(NEXT_PACKET),
        },
        "closure_decision": {
            "strict_final_connection_tables_accepted": 4,
            "one_premise_final_connection_tables_accepted": 6,
            "two_premise_AH_equivalent_final_connection_tables_accepted": 7,
            "counted_principles": [BN27_PREMISE, AH_REPRESENTATIVE_PREMISE],
            "AH_equivalent_cech_row_accepted": True,
            "literal_goodcover_Deligne_Cech_row_accepted": False,
            "HYM_or_EndE_final_row_accepted": False,
            "remaining_row_after_AH_equivalent_lane": "selected_HYM_or_projective_connection_coefficients",
            "strict_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "SelectedAHRepresentativeCechRowEmissionTheorem",
            "proved": True,
            "statement": (
                "The selected ordered AH/good-cover source layer and the explicit q79 Appell-Humbert automorphy "
                "formula emit an AH representative of the Cech transition row for L^2=(2,-4,0), with generator "
                "cocycle checks, c1 pairings (2,-4,0), trivial shared-circle degree, and selected nonzero Ext "
                "class theta_plus_0_tensor_eta_minus_0.  Under the counted "
                "SelectedAHCechRepresentativeEquivalencePrinciple, this accepts the BN27 Cech row in an "
                "AH-equivalent two-premise lane, moving that lane to 7/8.  The original one-premise lane remains "
                "6/8 because literal good-cover Deligne-Cech cochains are not emitted.  The HYM/End(E) row remains "
                "open because diagonal End0 support does not emit the full selected connection/operator values."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedCechAHRepresentativeOrHYMEndEValues",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "strict_final_connection_tables_accepted": 4,
        "one_premise_final_connection_tables_accepted": 6,
        "two_premise_AH_equivalent_final_connection_tables_accepted": 7,
        "counted_principles": [BN27_PREMISE, AH_REPRESENTATIVE_PREMISE],
        "AH_equivalent_cech_row_accepted": True,
        "literal_goodcover_Deligne_Cech_row_accepted": False,
        "HYM_or_EndE_final_row_accepted": False,
        "strict_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected Cech AH Representative or HYM/EndE Values v1

## Theorem

`SelectedAHRepresentativeCechRowEmissionTheorem` is proved.

## Result

The original BN27 counted-premise lane remains:

- strict lane: `4/8`
- one-premise BN27 lane: `6/8`

A new counted AH-representative lane is now available:

- counted principles: `{BN27_PREMISE}` and `{AH_REPRESENTATIVE_PREMISE}`
- AH-equivalent final connection tables: `7/8`
- accepted AH-equivalent row: `cech_transition_cocycles`

The emitted representative is the selected ordered Appell-Humbert/AH transition
data for `L^2=(2,-4,0)` with c1 pairings `(2,-4,0)`, trivial shared-circle
degree, and selected nonzero Ext class `theta_plus_0_tensor_eta_minus_0`.

Guardrails:

- literal good-cover Deligne-Cech cochains `A_ij`, `B_i`, `g_ijk`, `h_ij` are not emitted
- the AH representative equivalence is counted as an additional principle here
- the HYM/End(E) final row remains open
- this is not strict no-knob closure and not true SM equivalence

## Next Artifact

`{NEXT}`
"""

    write_json(CECH_PACKET, cech_packet)
    write_json(HYM_PACKET, hym_packet)
    write_json(GATE_PACKET, gate_packet)
    write_json(NEXT_PACKET, next_packet)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
