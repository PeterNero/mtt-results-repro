"""Reduce the remaining BN27 one-premise geometric rows to value obligations.

The current one-premise BN27 lane has 6/8 final connection-table rows.  This
builder imports the strongest Cech/good-cover and HYM/operator packets and
records what they actually prove: the raw good-cover choice is not a physical
knob, and HYM existence/support packets are available, but neither packet emits
the final Cech cocycles or HYM/End(E) coefficients required by the BN27 table.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_geometric_cechhym_obligation_reduction_after_onepremise"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CECH_PACKET = PACKET_DIR / "cech_goodcover_to_class_representative_reduction.packet.json"
HYM_PACKET = PACKET_DIR / "hym_support_to_ende_value_obligation_reduction.packet.json"
GATE_PACKET = PACKET_DIR / "onepremise_geometric_connection_row_gate.packet.json"
NEXT_PACKET = PACKET_DIR / "next_cechclass_or_hymende_values_contract.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Geometric_CechHYM_Obligation_Reduction_After_OnePremise_v1.md"

ONEPREMISE_CANDIDATE = DATA / "selected_bn27_onepremise_sourceobject_adoption_or_strictcechhym.candidate.json"
ONEPREMISE_GATE = (
    DATA
    / "selected_bn27_onepremise_sourceobject_adoption_or_strictcechhym"
    / "strict_vs_onepremise_connection_row_gate.packet.json"
)
STEP34 = DATA / "selected_step34_flatgerbe_sourcefunctor_or_selectedcoverselector.candidate.json"
STEP35 = DATA / "selected_step35_covergauge_reduction_or_s3classrestrictionselector.candidate.json"
TERMINAL_SWITCH = DATA / "selected_terminalsourceswitch_or_operatorpic0gerbede.candidate.json"
TERMINAL_COCHAIN_GATE = (
    DATA
    / "selected_terminalfinitecochain_connectiontablepromotion_or_fulldevalues"
    / "eight_connection_table_revalidation_after_selector.packet.json"
)
ROUTEC_HYM = DATA / "selected_routec_selected_ah_goodcover_promotion_hym_certificate.candidate.json"
DIAGONAL_HYM = DATA / "selected_chernweilhymde_or_determinanttorsion_fourslotclosingrun.candidate.json"
END0_DE = DATA / "selected_end0_de_payload_from_diagonal_hym.candidate.json"
EXT_HODGE = DATA / "selected_ext_overlap_hym_hodge_projector_table.candidate.json"
TRANSITION_PAYLOAD = (
    DATA
    / "selected_transitionpayload_or_heattorsionresponse_onegateattack"
    / "selected_transition_payload_attack.packet.json"
)
VISIBLE_OPERATOR = (
    DATA
    / "selected_visibleoperatorpayload_or_routechymresidual"
    / "hym_operator_extraction_contract.packet.json"
)

STATUS = (
    "MTT_SELECTED_GEOMETRIC_CECHHYM_OBLIGATION_REDUCTION_AFTER_ONEPREMISE_"
    "REDUCED_TO_CLASS_REPRESENTATIVE_AND_HYMENDE_VALUES"
)
NEXT = "MTT_Selected_CechClassRepresentative_or_HYMEndEConnectionValues_v1"
PREMISE_NAME = "SelectedBN27ThresholdSourceEmissionPrinciple"
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
        raise FileNotFoundError("missing geometric Cech/HYM inputs: " + ", ".join(missing))


def main() -> int:
    require_sources(
        [
            ONEPREMISE_CANDIDATE,
            ONEPREMISE_GATE,
            STEP34,
            STEP35,
            TERMINAL_SWITCH,
            TERMINAL_COCHAIN_GATE,
            ROUTEC_HYM,
            DIAGONAL_HYM,
            END0_DE,
            EXT_HODGE,
            TRANSITION_PAYLOAD,
            VISIBLE_OPERATOR,
        ]
    )

    onepremise = load(ONEPREMISE_CANDIDATE)
    onepremise_gate = load(ONEPREMISE_GATE)
    step34 = load(STEP34)
    step35 = load(STEP35)
    terminal_switch = load(TERMINAL_SWITCH)
    terminal_cochain_gate = load(TERMINAL_COCHAIN_GATE)
    routec_hym = load(ROUTEC_HYM)
    diagonal_hym = load(DIAGONAL_HYM)
    end0_de = load(END0_DE)
    ext_hodge = load(EXT_HODGE)
    transition_payload = load(TRANSITION_PAYLOAD)
    visible_operator = load(VISIBLE_OPERATOR)

    if onepremise_gate["one_premise_final_connection_table_count"] != "6/8":
        raise ValueError("expected one-premise lane at 6/8")
    if onepremise_gate["one_premise_remaining_geometric_rows"] != GEOMETRIC_ROWS:
        raise ValueError("unexpected one-premise geometric rows")
    if onepremise["closure_decision"]["strict_final_connection_tables_accepted"] != 4:
        raise ValueError("strict lane should remain 4/8")

    step34_decision = step34["closure_decision"]
    step35_decision = step35["closure_decision"]
    if not step34_decision["finite_to_smooth_flat_gerbe_source_functor_constructed"]:
        raise ValueError("flat gerbe source functor support missing")
    if not step34_decision["qutrit_central_extension_holonomy_map_constructed"]:
        raise ValueError("qutrit central extension support missing")
    if not step35_decision["good_cover_removed_as_physical_knob"]:
        raise ValueError("good-cover knob reduction missing")
    if not step35_decision["frontier_reduced_to_selected_s3_class_restriction"]:
        raise ValueError("S3 class-restriction reduction missing")
    if step35_decision["selected_s3_differential_cohomology_class_closed"]:
        raise ValueError("S3 differential cohomology class unexpectedly closed")

    if terminal_cochain_gate["status"] != "THREE_OF_EIGHT_FINAL_CONNECTION_TABLES_ACCEPTED_AFTER_SELECTOR":
        raise ValueError("terminal cochain gate status drifted")
    if "cech_transition_cocycles" not in terminal_cochain_gate["remaining_rows"]:
        raise ValueError("terminal cochain gate no longer tracks Cech row")
    if diagonal_hym["closure_decision"]["selected_HYM_or_RouteC_residual_slot_closed"] is not True:
        raise ValueError("diagonal HYM residual slot support missing")
    if end0_de["what_closes_now"]["directionwise_D_E_connection_matrices"] is not True:
        raise ValueError("End0 diagonal D_E support missing")
    if ext_hodge["what_closes_now"]["transition_overlap_trivialization_values_for_eta00"] is not True:
        raise ValueError("Ext/Hodge transition support missing")
    if visible_operator["selected_operator_values_closed"] is not False:
        raise ValueError("visible operator values unexpectedly closed")
    if visible_operator["actual_visible_operator_payload_emitted"] is not False:
        raise ValueError("visible operator payload unexpectedly emitted")

    cech_packet = {
        "schema": "MTTCechGoodCoverToClassRepresentativeReduction.v1",
        "status": "CECH_ROW_REDUCED_TO_SELECTED_CLASS_RESTRICTION_AND_REPRESENTATIVE",
        "closure_claimed": True,
        "row": "cech_transition_cocycles",
        "accepted_as_final_connection_table_row": False,
        "support_imported": {
            "finite_to_smooth_flat_gerbe_source_functor": True,
            "qutrit_central_extension_holonomy_map": True,
            "good_cover_removed_as_physical_knob": True,
            "cover_refinement_invariance_imported": step35_decision["cover_refinement_invariance_imported"],
            "terminal_AH_Cech_equivalence_or_gerbe_route_conditionally_closed": terminal_switch[
                "closure_decision"
            ]["terminal_source_switch_conditionally_closed"],
        },
        "reduced_obligation": {
            "selected_s3_differential_cohomology_class": True,
            "selected_classifying_map_c": True,
            "selected_class_restriction_pullback_table": True,
            "selected_good_cover_or_AH_representative": True,
            "literal_Deligne_Cech_transition_data": [
                "A_ij",
                "B_i",
                "g_ijk",
                "h_ij",
            ],
        },
        "still_open": {
            "selected_s3_differential_cohomology_class_closed": False,
            "selected_classifying_map_c_closed": False,
            "selected_good_cover_closed": False,
            "literal_Deligne_Cech_transition_data_emitted": False,
            "cech_transition_cocycles_final_row_accepted": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    hym_packet = {
        "schema": "MTTHYMSupportToEndEValueObligationReduction.v1",
        "status": "HYM_ROW_REDUCED_TO_SELECTED_ENDE_CONNECTION_VALUES",
        "closure_claimed": True,
        "row": "selected_HYM_or_projective_connection_coefficients",
        "accepted_as_final_connection_table_row": False,
        "support_imported": {
            "routec_hym_bridge_ready_if_selected_stability_and_chamber_supplied": routec_hym[
                "what_closes_now"
            ]["Li_Yau_HYM_bridge_ready_if_selected_stability_and_Gauduchon_chamber_supplied"],
            "diagonal_rank2_HYM_residual_slot_closed": True,
            "directionwise_End0_D_E_connection_matrices": True,
            "Hodge_Lambda_row_table": ext_hodge["what_closes_now"]["Hodge_Lambda_row_table"],
            "transition_overlap_trivialization_values_for_eta00": ext_hodge["what_closes_now"][
                "transition_overlap_trivialization_values_for_eta00"
            ],
            "finite_values_shape_complete": transition_payload["support"]["finite_values_shape_complete"],
            "local_same_source_formula_ready": transition_payload["support"]["local_same_source_formula_ready"],
        },
        "reduced_obligation": {
            "selected_HYM_or_projective_connection_coefficients": True,
            "equivalent_EndE_operator_values_allowed": True,
            "same_source_transition_connection_representative": True,
            "rho_E_metric_D_E_Riesz_Green_dotD_same_source_payload": True,
            "nonlinear_HYM_connection_correction_or_control_bound": True,
        },
        "still_open": {
            "selected_HYM_connection_values_closed": False,
            "selected_operator_values_closed": visible_operator["selected_operator_values_closed"],
            "actual_visible_operator_payload_emitted": visible_operator["actual_visible_operator_payload_emitted"],
            "finite_operator_values_rhoE_DE_Riesz_Green_dotD_closed": False,
            "full_End0_Newton_Galerkin_coefficients_closed": False,
            "selected_HYM_or_projective_connection_coefficients_final_row_accepted": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    gate_packet = {
        "schema": "MTTOnePremiseGeometricConnectionRowGate.v1",
        "status": "ONE_PREMISE_REMAINS_6_OF_8_GEOMETRIC_ROWS_REDUCED_NOT_CLOSED",
        "closure_claimed": True,
        "premise_name": PREMISE_NAME,
        "premise_count": 1,
        "strict_final_connection_table_count": "4/8",
        "one_premise_final_connection_table_count": "6/8",
        "geometric_connection_rows_required": 2,
        "geometric_connection_rows_accepted": 0,
        "geometric_rows": GEOMETRIC_ROWS,
        "cech_row_accepted": False,
        "hym_row_accepted": False,
        "strict_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTNextCechClassOrHYMEndEValuesContract.v1",
        "status": "NEXT_IS_VALUE_EMISSION_FOR_TWO_GEOMETRIC_CONNECTION_ROWS",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "allowed_exits": [
            "emit selected Cech class restriction plus literal representative cocycles",
            "emit selected HYM/projective connection coefficients",
            "emit equivalent selected End(E) operator values accepted by the BN27 connection-row validator",
        ],
        "must_not_count_as_final_rows": [
            "good-cover refinement invariance alone",
            "abstract HYM existence alone",
            "rank-two diagonal HYM residual slot alone",
            "shape-complete smoke or lifted-flag transition payloads",
        ],
        "remaining_exact_rows": GEOMETRIC_ROWS,
        "one_premise_count_before_next": "6/8",
        "one_premise_count_after_success": "8/8",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedGeometricCechHYMObligationReductionAfterOnePremise",
        "status": STATUS,
        "previous_status": onepremise["status"],
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {
            "onepremise_candidate": rel(ONEPREMISE_CANDIDATE),
            "onepremise_gate": rel(ONEPREMISE_GATE),
            "step34": rel(STEP34),
            "step35": rel(STEP35),
            "terminal_switch": rel(TERMINAL_SWITCH),
            "terminal_cochain_gate": rel(TERMINAL_COCHAIN_GATE),
            "routec_hym": rel(ROUTEC_HYM),
            "diagonal_hym": rel(DIAGONAL_HYM),
            "end0_de": rel(END0_DE),
            "ext_hodge": rel(EXT_HODGE),
            "transition_payload": rel(TRANSITION_PAYLOAD),
            "visible_operator": rel(VISIBLE_OPERATOR),
        },
        "output_packets": {
            "cech_goodcover_to_class_representative_reduction": rel(CECH_PACKET),
            "hym_support_to_ende_value_obligation_reduction": rel(HYM_PACKET),
            "onepremise_geometric_connection_row_gate": rel(GATE_PACKET),
            "next_cechclass_or_hymende_values_contract": rel(NEXT_PACKET),
        },
        "closure_decision": {
            "premise_name": PREMISE_NAME,
            "premise_count": 1,
            "strict_final_connection_tables_accepted": 4,
            "one_premise_final_connection_tables_accepted": 6,
            "geometric_connection_rows_required": 2,
            "geometric_connection_rows_accepted": 0,
            "cech_goodcover_knob_removed": True,
            "cech_row_reduced_to_selected_class_representative": True,
            "hym_support_imported": True,
            "hym_row_reduced_to_selected_EndE_values": True,
            "cech_transition_cocycles_final_row_accepted": False,
            "selected_HYM_or_projective_connection_coefficients_final_row_accepted": False,
            "strict_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "GeometricCechHYMObligationReductionTheorem",
            "proved": True,
            "statement": (
                "After adopting the single explicit BN27 threshold-source premise, the proof has exactly two "
                "remaining final connection-table rows.  Existing Cech packets prove that the good-cover choice "
                "is gauge/scaffold data and reduce the row to a selected S3 differential-cohomology class, "
                "classifying map, restriction table, and literal representative cocycles.  Existing HYM packets "
                "prove rank-two and operator-shape support, but reduce the row to selected HYM/projective "
                "connection coefficients or equivalent End(E) values.  Therefore the one-premise lane remains "
                "6/8, and a successful next artifact must emit those two geometric value rows rather than cite "
                "support packets as final rows."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedGeometricCechHYMObligationReductionAfterOnePremise",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "premise_name": PREMISE_NAME,
        "premise_count": 1,
        "strict_final_connection_tables_accepted": 4,
        "one_premise_final_connection_tables_accepted": 6,
        "geometric_connection_rows_required": 2,
        "geometric_connection_rows_accepted": 0,
        "remaining_geometric_connection_rows": GEOMETRIC_ROWS,
        "cech_row_reduced_not_closed": True,
        "hym_row_reduced_not_closed": True,
        "strict_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected Geometric Cech/HYM Obligation Reduction After One Premise v1

## Theorem

`GeometricCechHYMObligationReductionTheorem` is proved.

## Result

The one-counted-premise BN27 lane remains:

- final connection tables: `6/8`
- geometric rows accepted: `0/2`

The two remaining rows are still exactly:

- `cech_transition_cocycles`
- `selected_HYM_or_projective_connection_coefficients`

What improved is the shape of the blocker.  The Cech row is no longer a request
for an arbitrary physical good cover; the good cover is gauge/scaffold data.
The row is now reduced to a selected S3 differential-cohomology class,
classifying map, restriction table, and literal representative cocycles.

The HYM row is no longer abstract existence.  The rank-two HYM residual slot,
diagonal End0 `D_E` support, Hodge/overlap support, and finite value-shape
support are imported.  The row is now reduced to selected HYM/projective
connection coefficients or equivalent selected End(E) values.

This packet does not close strict no-knob SM equivalence.  It prevents the next
pass from re-counting support packets as final value rows.

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
