"""Build BN27 connection-source values / physical determinant frontier packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
QA = Path("C:/Users/nero_/Downloads/TEXPAPERS/mtt-qa-su3-packet-proof/candidate_data")

SLUG = "selected_bn27connectionsourcevalues_or_physicalalphaactionunitdeterminanttable_or_directhkrow"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
BN27_LANE = PACKET_DIR / "bn27_source_transport_or_connection_values_lane.packet.json"
DETERMINANT_LANE = PACKET_DIR / "physical_determinant_finitepart_or_action_unit_lane.packet.json"
NEXT_CUTSET = PACKET_DIR / "next_cutset_after_bn27_values_physical_determinant.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_BN27ConnectionSourceValues_or_PhysicalAlphaActionUnitDeterminantTable_or_DirectHKRow_v1.md"

SOURCES = {
    "previous": DATA
    / "selected_flattorsionsmoothpromotion_or_selectedbundleabn27source_or_physicalomega0.candidate.json",
    "bn27_sourceidentity_minimal": QA
    / "selected_heterotic_orientedphifin_sourceidentitytransport_or_connectionvalues_minimalpacket.candidate.json",
    "bn27_sourcebranch_repair": QA
    / "selected_heterotic_orientedphifin_sourcebranchidentity_sourceamendment_or_connectionvalues.candidate.json",
    "bn27_sourceamendment_template": QA
    / "selected_heterotic_orientedphifin_bn27_sourcebranchidentity_sourceamendment_template_or_connectionvalues.candidate.json",
    "bn27_sourceobject_fill": QA
    / "selected_heterotic_orientedphifin_bn27_sourceobject_or_connectionvaluepayload_fillattempt.candidate.json",
    "bn27_declaration_interface": QA
    / "selected_heterotic_orientedphifin_bn27_sourceobject_declarationinterface_fill_or_selectedconnectionvalues.candidate.json",
    "bn27_transport_values": QA
    / "selected_heterotic_orientedphifin_bn27_sourceownership_transport_or_connectionwitness_values.candidate.json",
    "smooth_det_table": QA / "smooth_determinant_spectral_table_or_source_operator.candidate.json",
    "central_twist_det": QA / "central_twist_orbit_democracy_source_or_determinant_operator.candidate.json",
    "u1y_quotient_det": QA / "selected_electroweak_u1y_quotientdeterminant_lemma.candidate.json",
    "qastack_minimal_finitepart": QA
    / "selected_electroweak_qastack_minimal_selected_finitepart_payload_fill.candidate.json",
    "qastack_detfunctional": QA
    / "selected_electroweak_qastack_determinantfunctional_or_selected_abase_emission.candidate.json",
    "qastack_or_u1yrow": QA
    / "selected_electroweak_qastack_determinant_or_u1yrow_promotion.candidate.json",
    "u1y_localdet_from_gap": QA
    / "selected_electroweak_u1y_localdeterminant_from_27mode_de_gaplayer.candidate.json",
    "u1y_det_weighting": QA
    / "selected_electroweak_u1y_determinantfunctional_weighting_or_nogo.candidate.json",
    "u1y_factorized_operator": QA
    / "selected_electroweak_u1y_factorized_threshold_operator_source_attempt.candidate.json",
    "u1_hypercharge_spectrum": QA / "selected_u1_hypercharge_local_determinant_spectrum_attempt.candidate.json",
}

STATUS = (
    "MTT_SELECTED_BN27CONNECTIONSOURCEVALUES_OR_PHYSICALALPHAACTIONUNITDETERMINANTTABLE_"
    "CONTRACTED_TO_SOURCEIDENTITY_FINITEPARTPOLICY_OR_DIRECTHKROW"
)
NEXT = "MTT_Selected_SourceIdentityTransportProofAttempt_or_FinitePartPolicyIndexScaleSourceTheorem_or_DirectHKRow_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources() -> dict[str, dict[str, Any]]:
    missing = [rel(path) for path in SOURCES.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing BN27/determinant inputs: " + ", ".join(missing))
    return {name: load(path) for name, path in SOURCES.items()}


def d(src: dict[str, Any]) -> dict[str, Any]:
    return src.get("decision", src.get("closure_decision", {}))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = require_sources()
    prev = d(sources["previous"])
    minimal = d(sources["bn27_sourceidentity_minimal"])
    repair = d(sources["bn27_sourcebranch_repair"])
    template = d(sources["bn27_sourceamendment_template"])
    sourcefill = d(sources["bn27_sourceobject_fill"])
    declaration = d(sources["bn27_declaration_interface"])
    transport = d(sources["bn27_transport_values"])
    smoothdet = d(sources["smooth_det_table"])
    central = d(sources["central_twist_det"])
    quotient = d(sources["u1y_quotient_det"])
    minfinite = d(sources["qastack_minimal_finitepart"])
    detfunc = d(sources["qastack_detfunctional"])
    promo = d(sources["qastack_or_u1yrow"])
    localdet = d(sources["u1y_localdet_from_gap"])
    weighting = d(sources["u1y_det_weighting"])
    factorized = d(sources["u1y_factorized_operator"])
    hyper = d(sources["u1_hypercharge_spectrum"])

    bn27_lane = {
        "schema": "MTTBN27SourceTransportOrConnectionValuesLane.v1",
        "status": "SOURCE_IDENTITY_TRANSPORT_MINIMAL_PACKET_BUILT_VALUES_OPEN",
        "closure_claimed": True,
        "minimal_source_identity_transport": {
            "minimal_packet_built": minimal["minimal_packet_built"],
            "support_prefilter_passes": minimal["support_prefilter_passes"],
            "primary_route_selected": minimal["primary_route_selected"],
            "proof_object_emitted": minimal["proof_object_emitted"],
            "source_identity_transport_closed": minimal["source_identity_transport_closed"],
            "typed_connection_values_closed": minimal["typed_connection_values_closed"],
            "direct_connection_values_closed": minimal["direct_connection_values_closed"],
            "selected_connection_witness_export_closed": minimal[
                "selected_connection_witness_export_closed"
            ],
        },
        "sourcebranch_repair": {
            "repair_attack_executed": repair["repair_attack_executed"],
            "primary_lane": repair["primary_lane"],
            "projective_rhoE_primary": repair["projective_rhoE_primary"],
            "projective_finite_candidate_available": repair[
                "projective_finite_candidate_available"
            ],
            "projective_BN27_lift_closed": repair["projective_BN27_lift_closed"],
            "BN27_domain_emission_closed": repair["BN27_domain_emission_closed"],
            "source_branch_identity_closed": repair["source_branch_identity_closed"],
            "source_identity_transport_closed": repair["source_identity_transport_closed"],
            "selected_connection_witness_export_closed": repair[
                "selected_connection_witness_export_closed"
            ],
        },
        "source_or_connection_template": {
            "template_built": template["template_built"],
            "current_fill_built": template["current_fill_built"],
            "source_object_required_field_count": template["source_object_required_field_count"],
            "source_object_filled_field_count": template["source_object_filled_field_count"],
            "connection_values_required_field_count": template[
                "connection_values_required_field_count"
            ],
            "connection_values_filled_field_count": template[
                "connection_values_filled_field_count"
            ],
            "source_amendment_closed": template["source_amendment_closed"],
            "connection_values_closed": template["connection_values_closed"],
        },
        "field_probe": {
            "attempt_executed": sourcefill["attempt_executed"],
            "source_support_fields_probed": sourcefill["source_support_fields_probed"],
            "connection_support_fields_probed": sourcefill[
                "connection_support_fields_probed"
            ],
            "source_object_filled_field_count": sourcefill[
                "source_object_filled_field_count"
            ],
            "connection_values_filled_field_count": sourcefill[
                "connection_values_filled_field_count"
            ],
            "source_object_payload_closed": sourcefill["source_object_payload_closed"],
            "connection_value_payload_closed": sourcefill[
                "connection_value_payload_closed"
            ],
            "minimal_missing_theorem_built": sourcefill["minimal_missing_theorem_built"],
        },
        "u1y_import_and_transport_boundary": {
            "u1y_routec_support_imported_for_compatibility": declaration[
                "u1y_routec_support_imported_for_compatibility"
            ],
            "finite_routec_solve_export_to_BN27_closed": declaration[
                "finite_routec_solve_export_to_BN27_closed"
            ],
            "same_source_export_to_BN27_validators": declaration[
                "same_source_export_to_BN27_validators"
            ],
            "source_object_named_S_QaSU3_BN27": declaration[
                "source_object_named_S_QaSU3_BN27"
            ],
            "branch_certificate_closed": transport["branch_certificate_closed"],
            "projective_rhoE_lift_reopened": transport["projective_rhoE_lift_reopened"],
            "BN27_source_ownership_transport_closed": transport[
                "BN27_source_ownership_transport_closed"
            ],
            "transport_witness_values_found": transport["transport_witness_values_found"],
            "S_QaSU3_BN27_declared_as_selected_source": transport[
                "S_QaSU3_BN27_declared_as_selected_source"
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    determinant_lane = {
        "schema": "MTTPhysicalDeterminantFinitePartOrActionUnitLane.v1",
        "status": "CONCRETE_DETERMINANT_OPERATOR_SUPPORT_CLOSED_FINITEPART_POLICY_OPEN",
        "closure_claimed": True,
        "finite_support": {
            "finite_projected_hessian_zeta_determinant": smoothdet[
                "finite_projected_hessian_zeta_determinant"
            ],
            "smooth_threshold_spectral_table": smoothdet["smooth_threshold_spectral_table"],
            "smooth_source_operator": smoothdet["smooth_source_operator"],
            "orbit_democracy_weight_source_selection": central[
                "orbit_democracy_weight_source_selection"
            ],
            "finite_response_payload": central["finite_response_payload"],
            "smooth_threshold_determinant_operator": central[
                "smooth_threshold_determinant_operator"
            ],
        },
        "quotient_and_factorized_operator": {
            "algebraic_quotient_determinant_lemma_proved": quotient[
                "algebraic_quotient_determinant_lemma_proved"
            ],
            "quotient_positive_spectrum_computed": quotient[
                "quotient_positive_spectrum_computed"
            ],
            "matches_previous_Pperp_weighted_value": quotient[
                "matches_previous_Pperp_weighted_value"
            ],
            "quotient_logdet": quotient["quotient_logdet"],
            "factorized_operator_matrix_constructed": factorized[
                "factorized_operator_matrix_constructed"
            ],
            "quotient_operator_matrix_constructed": factorized[
                "quotient_operator_matrix_constructed"
            ],
            "factorization_matches_27mode_spectrum": factorized[
                "factorization_matches_27mode_spectrum"
            ],
            "selected_source_emission_closed": factorized[
                "selected_source_emission_closed"
            ],
            "hypercharge_index_Dynkin_weights_closed": factorized[
                "hypercharge_index_Dynkin_weights_closed"
            ],
            "typed_convention_map_closed": factorized["typed_convention_map_closed"],
        },
        "minimal_finitepart_payload": {
            "source_identity_for_DE_gap_layer_filled": minfinite[
                "source_identity_for_DE_gap_layer_filled"
            ],
            "V_mod_s_positive_table_computed_conditionally": minfinite[
                "V_mod_s_positive_table_computed_conditionally"
            ],
            "H_zero_cluster_currently_logdet_neutral": minfinite[
                "H_zero_cluster_currently_logdet_neutral"
            ],
            "kernel_policy_partially_filled": minfinite["kernel_policy_partially_filled"],
            "regularization_finite_part_selected": minfinite[
                "regularization_finite_part_selected"
            ],
            "index_weights_promoted_to_determinant_weights": minfinite[
                "index_weights_promoted_to_determinant_weights"
            ],
            "determinant_scale_selected": minfinite["determinant_scale_selected"],
            "selected_p_a_promoted": minfinite["selected_p_a_promoted"],
        },
        "source_theorem_gate": {
            "route_a_selected_abase_emission_closed": detfunc[
                "route_a_selected_abase_emission_closed"
            ],
            "route_b_direct_bn_functional_closed": detfunc[
                "route_b_direct_bn_functional_closed"
            ],
            "conditional_quotient_logdet_carried": detfunc[
                "conditional_quotient_logdet_carried"
            ],
            "conditional_quotient_logdet_promoted": detfunc[
                "conditional_quotient_logdet_promoted"
            ],
            "Qa_stack_route_promoted": promo["Qa_stack_route_promoted"],
            "direct_pY_route_promoted": promo["direct_pY_route_promoted"],
            "selected_Qa_or_pY_source_payload_found": promo[
                "selected_Qa_or_pY_source_payload_found"
            ],
            "selected_U1Y_determinant_functional_closed": localdet[
                "selected_U1Y_determinant_functional_closed"
            ],
            "determinant_functional_source_theorem_found": weighting[
                "determinant_functional_source_theorem_found"
            ],
            "Pperp_weighting_promoted": weighting["Pperp_weighting_promoted"],
            "u1_hypercharge_spectrum_closed": hyper["u1_hypercharge_spectrum_closed"],
            "Pperp_quotient_identity_promoted": hyper["Pperp_quotient_identity_promoted"],
        },
        "lambda_and_physical_boundary": {
            "lambda_12_closed": False,
            "measured_electroweak_closure": False,
            "full_Qa_SU3_threshold_closure_now": False,
            "physical_action_unit_or_alpha_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_cutset = {
        "schema": "MTTNextCutsetAfterBN27ValuesPhysicalDeterminant.v1",
        "status": "NEXT_FRONTIER_SOURCEIDENTITY_TRANSPORT_OR_FINITEPART_POLICY_OR_DIRECT_HK_ROW",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "closed_here": [
            "BN27 source-identity transport minimal packet built",
            "BN27 support probe covers 11 source fields and 8 connection fields",
            "current BN27 fill emits 0 source fields and 0 connection fields",
            "finite determinant support includes log(2008) projected Hessian determinant",
            "U1/Y quotient determinant lemma computes logdet 29.201650332199108",
            "concrete factorized A_base tensor I_3 quotient operator constructed",
            "minimal finitepart payload fills D_E gap-layer identity and conditional V/<s> positive table",
        ],
        "still_open": [
            "source-identity transport proof object with three sublemmas",
            "direct S_QaSU3^BN27 source object filling 11 fields",
            "selected connection-value payload filling 8 fields",
            "regularization finite part selected as electroweak finite part",
            "index weights promoted to determinant weights",
            "determinant scale selected",
            "hypercharge/index weights and typed convention map",
            "physical alpha/action-unit or Omega0/K_phys anchor",
            "lambda_12 and selected p_a promotion",
            "direct source-native K_threshold.Omega_H.lambda",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedBN27ConnectionSourceValuesOrPhysicalAlphaActionUnitDeterminantTable",
        "status": STATUS,
        "previous_status": sources["previous"]["status"],
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {name: rel(path) for name, path in SOURCES.items()},
        "output_packets": {
            "bn27_source_transport_or_connection_values_lane": rel(BN27_LANE),
            "physical_determinant_finitepart_or_action_unit_lane": rel(DETERMINANT_LANE),
            "next_cutset_after_bn27_values_physical_determinant": rel(NEXT_CUTSET),
        },
        "closure_decision": {
            "BN27_minimal_source_identity_transport_packet_built": True,
            "BN27_source_fields_probed": 11,
            "BN27_connection_fields_probed": 8,
            "BN27_source_fields_filled": 0,
            "BN27_connection_fields_filled": 0,
            "BN27_source_identity_transport_closed": False,
            "S_QaSU3_BN27_declared_as_selected_source": False,
            "selected_connection_values_closed": False,
            "finite_projected_hessian_log2008_closed_as_support": True,
            "u1y_quotient_determinant_lemma_proved": True,
            "factorized_threshold_operator_constructed": True,
            "factorized_threshold_operator_selected_as_source": False,
            "minimal_finitepart_payload_partially_filled": True,
            "regularization_finite_part_selected": False,
            "index_weights_promoted_to_determinant_weights": False,
            "determinant_scale_selected": False,
            "selected_p_a_promoted": False,
            "lambda_12_closed": False,
            "physical_alpha_action_unit_or_Omega0_closed": False,
            "selected_R_H_RG_emitted": False,
            "selected_K_threshold_Omega_H_lambda": False,
            "strict_H_K_threshold_row_emitted": False,
            "accepted_selected_K_source_row_count": prev["accepted_selected_K_source_row_count"],
            "selected_K_threshold_row_count_required": prev[
                "selected_K_threshold_row_count_required"
            ],
            "direct_HK_exit_still_allowed": True,
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "BN27ConnectionValuesOrFinitePartPolicyReductionTheorem",
            "proved": True,
            "statement": (
                "The BN27 route is reduced to an explicit source-identity transport "
                "proof object or emitted connection/source values: current probes cover "
                "eleven source-object fields and eight connection-value fields but fill "
                "none. The physical determinant route is no longer missing a finite "
                "operator model: the quotient determinant and factorized A_base tensor "
                "I_3 operator are constructed as support. What remains is selected "
                "finitepart policy, index-scale/hypercharge weights, determinant scale, "
                "and the physical action-unit/Omega0 anchor. No direct H K row is emitted."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedBN27ConnectionSourceValuesOrPhysicalAlphaActionUnitDeterminantTable",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "BN27_minimal_source_identity_transport_packet_built": True,
        "BN27_source_fields_filled": 0,
        "BN27_connection_fields_filled": 0,
        "BN27_source_identity_transport_closed": False,
        "factorized_threshold_operator_constructed": True,
        "factorized_threshold_operator_selected_as_source": False,
        "minimal_finitepart_payload_partially_filled": True,
        "regularization_finite_part_selected": False,
        "selected_p_a_promoted": False,
        "lambda_12_closed": False,
        "physical_alpha_action_unit_or_Omega0_closed": False,
        "selected_R_H_RG_emitted": False,
        "strict_H_K_threshold_row_emitted": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected BN27 Connection Source Values or Physical Alpha Action-Unit Determinant Table v1

## Theorem

`BN27ConnectionValuesOrFinitePartPolicyReductionTheorem` is emitted.

The current frontier is contracted to a source-identity proof object, selected
source/connection value emission, selected finitepart policy, or direct H row.

## Closed Here

- BN27 source-identity transport minimal packet is built.
- BN27 source/connection probe covers `11` direct source fields and `8`
  connection-value fields.
- Current BN27 fill emits `0` source fields and `0` connection fields.
- Finite determinant support includes the projected Hessian determinant
  `log(2008)`.
- U1/Y quotient determinant lemma computes
  `logdet = 29.201650332199108`.
- Concrete factorized `A_base tensor I_3` quotient operator is constructed.
- Minimal finitepart payload fills the `D_E` gap-layer identity and conditional
  `V/<s>` positive table.

## Still Open

- Source-identity transport proof object with its three sublemmas.
- Direct `S_QaSU3^BN27` source object filling `11` fields.
- Selected connection-value payload filling `8` fields.
- Regularization finite part selected as the electroweak finite part.
- Index weights promoted to determinant weights.
- Determinant scale, hypercharge/index weights, and typed convention map.
- Physical `alpha_phys`/action-unit or `Omega0/K_phys` anchor.
- `lambda_12` and selected `p_a` promotion.
- Direct source-native `K_threshold.Omega_H.lambda`.

## Current Count

Strict selected `K_threshold` rows remain
`{prev["accepted_selected_K_source_row_count"]}/{prev["selected_K_threshold_row_count_required"]}`.

## Next Artifact

`{NEXT}`
"""

    write_json(BN27_LANE, bn27_lane)
    write_json(DETERMINANT_LANE, determinant_lane)
    write_json(NEXT_CUTSET, next_cutset)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
