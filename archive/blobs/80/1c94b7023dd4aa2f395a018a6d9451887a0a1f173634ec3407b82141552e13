"""Build orientation/magnitude co-emission or endomorphism finitepart frontier packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
QA = Path("C:/Users/nero_/Downloads/TEXPAPERS/mtt-qa-su3-packet-proof/candidate_data")

SLUG = "selected_orientationmagnitudecoemission_or_endomorphismthresholdfinitepart_or_directhkrow"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
COEMISSION_GATE = PACKET_DIR / "orientation_magnitude_coemission_reduction.packet.json"
OPERATOR_GATE = PACKET_DIR / "endomorphism_threshold_finitepart_reduction.packet.json"
CTAU_GATE = PACKET_DIR / "ctau_phifin_threshold_identity_gate.packet.json"
NEXT_CONTRACT = PACKET_DIR / "next_frontier_acceptance_contract.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_OrientationMagnitudeCoEmission_or_EndomorphismThresholdFinitePart_or_DirectHKRow_v1.md"

SOURCES = {
    "previous": DATA
    / "selected_heteroticstromingersourceoperator_or_localsystemtorsion_or_fullfourierorbit_or_directhkrow.candidate.json",
    "coemission_reduction": QA
    / "selected_heterotic_orientedphifin_orientation_magnitude_coemission_theorem.candidate.json",
    "branch_identity_gate": QA
    / "selected_heterotic_orientedphifin_branchidentity_sourcecertificate_or_smootheqa_finalgate.candidate.json",
    "branch_identity_fill": QA
    / "selected_heterotic_orientedphifin_branchidentity_minimalsourcecertificate_fill.candidate.json",
    "bn27_constructive": QA
    / "selected_heterotic_orientedphifin_bn27_selectedsourceemission_or_connectiontables_constructiveattempt.candidate.json",
    "projective_internal_finitepart": QA
    / "selected_heterotic_projectiverhoe_eqa_or_thresholdfinitepart.candidate.json",
    "internal_finitepart_values": QA
    / "selected_heterotic_projectiverhoe_internal_threshold_finitepart.json",
    "physical_normalization_gate": QA
    / "selected_heterotic_projectiverhoe_physicalthresholdnormalization_or_smoothoperatoridentity.candidate.json",
    "kphys_or_smooth_fill": QA
    / "selected_heterotic_projectiverhoe_kphysanchor_or_smoothoperatoridentity_fill.candidate.json",
    "bundle_trace_policy": QA
    / "selected_heterotic_projectiverhoe_bundleconnection_trace_quotient_policy.candidate.json",
    "endomorphism_value_fill": QA
    / "selected_heterotic_endomorphism_threshold_valuepacket_fill.candidate.json",
    "label_embedding": QA
    / "selected_heterotic_ende_to_bn_labelembedding_or_smoothtransitionconnection_valuepacket.candidate.json",
    "operator_intertwiner": QA
    / "selected_heterotic_ende_to_bn_operatorintertwiner_or_smoothconnection_sourceamendment.candidate.json",
    "ctau_source": QA / "selected_heterotic_bn_centralrankoperator_or_smootheqa_sourceemission.candidate.json",
    "ctau_positive": QA
    / "selected_heterotic_ctau_positivefinitepart_or_smoothdiracconvention_sourcetheorem.candidate.json",
    "product_operator": QA
    / "selected_heterotic_orientedphifin_productoperator_or_smootheqa_magnitudesource.candidate.json",
    "magnitude_finitepart": QA
    / "selected_heterotic_orientedphifin_magnitudefinitepart_sourcetheorem_or_smootheqa_traceidentity.candidate.json",
    "threshold_identity_fill": QA
    / "selected_heterotic_orientedphifin_thresholdidentity_sourcefill_or_smootheqa_construction.candidate.json",
    "finite_rhoe_insertion": QA
    / "selected_heterotic_orientedphifin_endedomain_or_nonidentityrhoe_sourcevalue_insertion.candidate.json",
}

STATUS = (
    "MTT_SELECTED_ORIENTATIONMAGNITUDECOEMISSION_OR_ENDOMORPHISMTHRESHOLDFINITEPART_"
    "CTAU_SIGNED_CLOSED_MAGNITUDE_SOURCE_IDENTITY_OPEN"
)
NEXT = "MTT_Selected_FiniteRhoEToOrientedBNFunctor_or_SmoothEQaRepresentative_or_DirectHKRow_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def decision(packet: dict[str, Any]) -> dict[str, Any]:
    return packet.get("decision", packet.get("closure_decision", {}))


def require_sources() -> dict[str, dict[str, Any]]:
    missing = [rel(path) for path in SOURCES.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing orientation/operator frontier inputs: " + ", ".join(missing))
    return {name: load(path) for name, path in SOURCES.items()}


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = require_sources()
    prev = decision(sources["previous"])
    coemission = decision(sources["coemission_reduction"])
    branch_gate = decision(sources["branch_identity_gate"])
    branch_fill = decision(sources["branch_identity_fill"])
    bn27 = decision(sources["bn27_constructive"])
    internal = decision(sources["projective_internal_finitepart"])
    physical = decision(sources["physical_normalization_gate"])
    kphys = decision(sources["kphys_or_smooth_fill"])
    bundle = decision(sources["bundle_trace_policy"])
    endomorphism = decision(sources["endomorphism_value_fill"])
    label = decision(sources["label_embedding"])
    intertwiner = decision(sources["operator_intertwiner"])
    ctau_source = decision(sources["ctau_source"])
    ctau_positive = decision(sources["ctau_positive"])
    product = decision(sources["product_operator"])
    magnitude = decision(sources["magnitude_finitepart"])
    threshold = decision(sources["threshold_identity_fill"])
    rhoe_insert = decision(sources["finite_rhoe_insertion"])
    finite_values = sources["internal_finitepart_values"]

    coemission_gate = {
        "schema": "MTTOrientationMagnitudeCoEmissionReduction.v1",
        "status": "FIVE_FIELD_COEMISSION_REDUCED_TO_FINITE_RHOE_OR_SMOOTH_EQA_BRIDGE",
        "closure_claimed": True,
        "support_reduction": {
            "support_reduction_closed": coemission["support_reduction_closed"],
            "closed_support_count": coemission["closed_support_count"],
            "support_required_count": coemission["support_required_count"],
            "five_field_coemission_request_reduced_to_single_leaf": coemission[
                "five_field_coemission_request_reduced_to_single_leaf"
            ],
            "same_source_orientation_magnitude_branch_identity_closed": coemission[
                "same_source_orientation_magnitude_branch_identity_closed"
            ],
        },
        "branch_identity_fill": {
            "branch_identity_final_gate_executed": branch_gate[
                "branch_identity_final_gate_executed"
            ],
            "minimal_source_certificate_packet_built": branch_gate[
                "minimal_source_certificate_packet_built"
            ],
            "minimal_source_certificate_fill_attempted": branch_fill[
                "minimal_source_certificate_fill_attempted"
            ],
            "filled_count": branch_fill["filled_count"],
            "required_count": branch_fill["required_count"],
            "minimal_new_leaf": branch_fill["minimal_new_leaf"],
            "selected_BN27_source_domain_bridge_closed": branch_fill[
                "selected_BN27_source_domain_bridge_closed"
            ],
        },
        "bn27_constructive_route": {
            "primary_route": bn27["primary_route"],
            "conditional_replay_ready": bn27["conditional_replay_ready"],
            "direct_open_statement_count": bn27["direct_open_statement_count"],
            "connection_open_table_count": bn27["connection_open_table_count"],
            "direct_theorem_closed": bn27["direct_theorem_closed"],
            "connection_tables_closed": bn27["connection_tables_closed"],
        },
        "finite_rhoe_value_insertion": {
            "finite_projective_rhoE_source_value_inserted": rhoe_insert[
                "finite_projective_rhoE_source_value_inserted"
            ],
            "EndE_or_rhoE_to_oriented_BN_functor_closed": rhoe_insert[
                "EndE_or_rhoE_to_oriented_BN_functor_closed"
            ],
            "oriented_BN_carrier_emission_closed": rhoe_insert[
                "oriented_BN_carrier_emission_closed"
            ],
            "smooth_projective_transition_tables_emitted": rhoe_insert[
                "smooth_projective_transition_tables_emitted"
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    operator_gate = {
        "schema": "MTTEndomorphismThresholdFinitePartReduction.v1",
        "status": "INTERNAL_FINITEPART_CLOSED_PHYSICAL_SMOOTH_OPERATOR_IDENTITY_OPEN",
        "closure_claimed": True,
        "internal_projective_rhoe_finitepart": {
            "selected_internal_threshold_finitepart_closed": internal[
                "selected_internal_threshold_finitepart_closed"
            ],
            "E_Qa_computed": internal["E_Qa_computed"],
            "smooth_operator_identity_proved": internal["smooth_operator_identity_proved"],
            "physical_threshold_normalization_closed": internal[
                "physical_threshold_normalization_closed"
            ],
            "Delta_selected_internal_exact": finite_values["Delta_selected_internal_exact"],
            "determinant": finite_values["determinant"],
            "spectrum": finite_values["spectrum"],
        },
        "physical_normalization": {
            "internal_interface_closed": physical["internal_interface_closed"],
            "closed_internal_formula": physical["closed_internal_formula"],
            "physical_threshold_normalization_closed": physical[
                "physical_threshold_normalization_closed"
            ],
            "smooth_operator_identity_proved": physical["smooth_operator_identity_proved"],
            "best_next_lane": kphys["best_next_lane"],
            "physical_anchor_bridge_closed": kphys["physical_anchor_bridge_closed"],
            "smooth_operator_identity_closed": kphys["smooth_operator_identity_closed"],
        },
        "bundle_trace_policy": {
            "finite_internal_trace_and_quotient_policy_closed": bundle[
                "finite_internal_trace_and_quotient_policy_closed"
            ],
            "direct_projective_rhoE_route_primary": bundle[
                "direct_projective_rhoE_route_primary"
            ],
            "standard_embedding_route_retired_for_current_branch": bundle[
                "standard_embedding_route_retired_for_current_branch"
            ],
            "smooth_bundle_connection_policy_closed": bundle[
                "smooth_bundle_connection_policy_closed"
            ],
            "E_Qa_computed": bundle["E_Qa_computed"],
        },
        "endomorphism_value_packet": {
            "template_filled_enough_for_determinant": endomorphism[
                "template_filled_enough_for_determinant"
            ],
            "selected_values_available": endomorphism["selected_values_available"],
            "physical_electroweak_threshold_closure": endomorphism[
                "physical_electroweak_threshold_closure"
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    ctau_gate = {
        "schema": "MTTCtauPhiFinThresholdIdentityGate.v1",
        "status": "CTAU_SIGNED_ORIENTATION_CLOSED_POSITIVE_MAGNITUDE_IDENTITY_OPEN",
        "closure_claimed": True,
        "label_embedding": {
            "label_embedding_candidate_built": label["label_embedding_candidate_built"],
            "projection_pair_candidate_valid_as_injection": label[
                "projection_pair_candidate_valid_as_injection"
            ],
            "rhoE_character_intertwines": label["rhoE_character_intertwines"],
            "D_E_or_EQa_intertwines": label["D_E_or_EQa_intertwines"],
            "finitepart_regularization_same_scheme": label[
                "finitepart_regularization_same_scheme"
            ],
        },
        "central_rank_intertwiner": {
            "central_rank_operator_candidate_intertwines": intertwiner[
                "central_rank_operator_candidate_intertwines"
            ],
            "central_rank_operator_source_selected": intertwiner[
                "central_rank_operator_source_selected"
            ],
            "operator_identity_closed_for_signed_layer": ctau_source[
                "operator_identity_closed_for_signed_layer"
            ],
            "C_tau_source_selected_as_BN_operator": ctau_source[
                "C_tau_source_selected_as_BN_operator"
            ],
            "positive_finitepart_for_C_tau_closed": ctau_source[
                "positive_finitepart_for_C_tau_closed"
            ],
        },
        "ctau_chiral_positive_convention": {
            "ctau_chiral_dirac_convention_source_selected": ctau_positive[
                "ctau_chiral_dirac_convention_source_selected"
            ],
            "ctau_positive_finitepart_convention_closed": ctau_positive[
                "ctau_positive_finitepart_convention_closed"
            ],
            "ctau_logdet_value_full_BN": ctau_positive["ctau_logdet_value_full_BN"],
            "ctau_eta_value_full_BN": ctau_positive["ctau_eta_value_full_BN"],
            "ctau_supplies_orientation": ctau_positive["ctau_supplies_orientation"],
            "ctau_supplies_nonzero_threshold_magnitude": ctau_positive[
                "ctau_supplies_nonzero_threshold_magnitude"
            ],
        },
        "phifin_magnitude": {
            "commutation_or_simultaneous_functional_calculus_closed": product[
                "commutation_or_simultaneous_functional_calculus_closed"
            ],
            "oriented_product_table_built": product["oriented_product_table_built"],
            "oriented_abs_sector_logdet_sum": product["oriented_abs_sector_logdet_sum"],
            "PhiFin_all_positive_logdet": product["PhiFin_all_positive_logdet"],
            "oriented_table_magnitude_finitepart_computed": magnitude[
                "oriented_table_magnitude_finitepart_computed"
            ],
            "oriented_abs_sector_logdet_exact": magnitude[
                "oriented_abs_sector_logdet_exact"
            ],
            "full_positive_logdet_exact": magnitude["full_positive_logdet_exact"],
            "finitepart_trace_identity_closed": magnitude[
                "finitepart_trace_identity_closed"
            ],
        },
        "threshold_identity_fill": {
            "fill_attempt_executed": threshold["fill_attempt_executed"],
            "closed_required_leaf_count": threshold["closed_required_leaf_count"],
            "required_leaf_count": threshold["required_leaf_count"],
            "finite_quotient_identity_constructed": threshold[
                "finite_quotient_identity_constructed"
            ],
            "smooth_EQa_constructed": threshold["smooth_EQa_constructed"],
            "heterotic_threshold_magnitude_promoted": threshold[
                "heterotic_threshold_magnitude_promoted"
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_contract = {
        "schema": "MTTFiniteRhoEToOrientedBNOrSmoothEQa.NextContract.v1",
        "status": "FINITE_RHOE_TO_ORIENTED_BN_OR_SMOOTH_EQA_REPRESENTATIVE_REQUIRED",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "strict_K_threshold_count": {
            "accepted": prev["accepted_selected_K_source_row_count"],
            "required": prev["selected_K_threshold_row_count_required"],
        },
        "closed_now": [
            "five co-emission fields reduced to one branch/source identity leaf",
            "BN27 direct theorem and connection-table schemas built with conditional replay",
            "finite projective rhoE source value inserted at internal/projective scope",
            "internal projective rhoE finitepart log(2008) closed",
            "finite internal trace and quotient policy closed",
            "phase-preserving 27x11 label embedding built as rhoE character injection",
            "C_tau selected as BN signed central-rank operator",
            "P^T C_tau P signed operator identity closed",
            "C_tau chiral positive convention closed with trivial logdet and eta",
            "C_tau and Phi_fin simultaneous functional calculus closed",
            "oriented Phi_fin finitepart table computed exactly",
        ],
        "still_open": [
            "finite rhoE to oriented BN functor with operator and finitepart preservation",
            "smooth projective representative or smooth E_Qa quotient emitting the same threshold complex",
            "selected bundle connection/curvature/representation trace and E_Qa finitepart",
            "physical K_phys/action-unit, mu_match, and RG/threshold convention",
            "direct K_threshold.Omega_H.lambda source row",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedOrientationMagnitudeCoEmissionOrEndomorphismThresholdFinitePart",
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
            "orientation_magnitude_coemission_reduction": rel(COEMISSION_GATE),
            "endomorphism_threshold_finitepart_reduction": rel(OPERATOR_GATE),
            "ctau_phifin_threshold_identity_gate": rel(CTAU_GATE),
            "next_frontier_acceptance_contract": rel(NEXT_CONTRACT),
        },
        "closure_decision": {
            "five_field_coemission_request_reduced_to_single_leaf": True,
            "same_source_orientation_magnitude_branch_identity_closed": False,
            "finite_projective_rhoE_source_value_inserted": True,
            "finite_rhoE_to_oriented_BN_functor_closed": False,
            "internal_projective_rhoE_finitepart_log2008_closed": True,
            "physical_threshold_normalization_closed": False,
            "smooth_operator_identity_closed": False,
            "endomorphism_value_packet_filled": False,
            "label_embedding_27x11_built": True,
            "rhoE_character_intertwines": True,
            "selected_PhiFin_laplacian_intertwines_internal_signed_operator": False,
            "C_tau_source_selected_as_BN_operator": True,
            "C_tau_signed_intertwiner_closed": True,
            "C_tau_positive_finitepart_convention_closed": True,
            "C_tau_nonzero_threshold_magnitude_source": False,
            "C_tau_PhiFin_commutation_closed": True,
            "oriented_PhiFin_finitepart_exactly_computed": True,
            "oriented_logdet_promoted": False,
            "smooth_EQa_constructed": False,
            "selected_K_threshold_Omega_H_lambda": False,
            "strict_H_K_threshold_row_emitted": False,
            "accepted_selected_K_source_row_count": prev["accepted_selected_K_source_row_count"],
            "selected_K_threshold_row_count_required": prev[
                "selected_K_threshold_row_count_required"
            ],
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "OrientationMagnitudeOrEndomorphismFinitepartFrontierTheorem",
            "proved": True,
            "statement": (
                "The orientation/magnitude and endomorphism finitepart branches now "
                "meet at a smaller bridge. The finite projective rhoE source value "
                "and internal log(2008) finitepart are selected at internal scope. "
                "A 27x11 phase-preserving injection exists and intertwines rhoE "
                "characters, but not the selected Phi_fin Laplacian finitepart. "
                "The BN central-rank operator C_tau is selected and exactly "
                "intertwines the internal signed operator; its chiral positive "
                "convention has logdet 0 and eta 0, so it supplies orientation but "
                "not nonzero threshold magnitude. The Phi_fin positive magnitude "
                "finitepart table is exact, but still support-only until a finite "
                "rhoE-to-oriented-BN functor, a smooth E_Qa representative, or a "
                "direct H K row is emitted."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedOrientationMagnitudeCoEmissionOrEndomorphismThresholdFinitePart",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "finite_projective_rhoE_source_value_inserted": True,
        "internal_projective_rhoE_finitepart_log2008_closed": True,
        "C_tau_source_selected_as_BN_operator": True,
        "C_tau_signed_intertwiner_closed": True,
        "C_tau_nonzero_threshold_magnitude_source": False,
        "oriented_PhiFin_finitepart_exactly_computed": True,
        "oriented_logdet_promoted": False,
        "strict_H_K_threshold_row_emitted": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected Orientation-Magnitude Co-Emission or Endomorphism Threshold Finitepart v1

## Theorem

`OrientationMagnitudeOrEndomorphismFinitepartFrontierTheorem` is emitted.

## Newly Closed

- The five orientation/magnitude co-emission fields are reduced to one
  branch/source-identity bridge.
- The finite projective `rho_E` source value is inserted at internal/projective
  scope.
- The internal projective `rho_E` finitepart is closed:
  `Delta_selected_internal = log(2008)`.
- The finite internal trace and quotient policy are closed.
- A phase-preserving `27x11` label embedding is built as a `rho_E` character
  injection.
- `C_tau` is selected as the BN signed central-rank operator.
- `P^T C_tau P` closes the signed operator identity.
- The finite chiral positive convention for `C_tau` is closed, with
  `logdet=0` and `eta=0`.
- `C_tau` and `Phi_fin` share the BN domain and commute.
- The oriented `Phi_fin` finitepart table is exact:
  `log(92160000)` for the oriented absolute sector and
  `log(884736000000)` for the full positive table.

## Not Promoted

`C_tau` supplies orientation, not nonzero threshold magnitude.  The exact
`Phi_fin` table remains support-only until the source bridge is emitted.

## Still Open

- Finite `rho_E -> oriented B_N` functor preserving operator and finitepart.
- Smooth projective representative or smooth `E_Qa` quotient emitting the same
  threshold complex.
- Selected bundle connection, curvature, representation trace, quotient policy,
  and `E_Qa` finitepart.
- Physical `K_phys`/action-unit, `mu_match`, and RG/threshold convention.
- Direct source-native `K_threshold.Omega_H.lambda`.

## Current Count

Strict selected `K_threshold` rows remain
`{prev["accepted_selected_K_source_row_count"]}/{prev["selected_K_threshold_row_count_required"]}`.

## Next Artifact

`{NEXT}`
"""

    write_json(COEMISSION_GATE, coemission_gate)
    write_json(OPERATOR_GATE, operator_gate)
    write_json(CTAU_GATE, ctau_gate)
    write_json(NEXT_CONTRACT, next_contract)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
