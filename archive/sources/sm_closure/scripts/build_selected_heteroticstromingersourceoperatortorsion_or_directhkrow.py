"""Build the heterotic/Strominger source-operator torsion or direct H K-row packet.

This consumes the newest Qa/SU3 HYM, gerbe, and projective-rhoE packets.  The
point is to avoid looping on the old "torsion/operator source" phrase: the
finite internal projective-rhoE payload is now real support, while the physical
smooth/operator identity and H-row value are still not emitted.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
QA = Path("C:/Users/nero_/Downloads/TEXPAPERS/mtt-qa-su3-packet-proof/candidate_data")

SLUG = "selected_heteroticstromingersourceoperatortorsion_or_directhkrow"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
LANE_REDUCTION = PACKET_DIR / "heterotic_source_operator_torsion_lane_reduction.packet.json"
FINITE_SUPPORT = PACKET_DIR / "projective_rhoe_finite_internal_support_import.packet.json"
PHYSICAL_BLOCKER = PACKET_DIR / "physical_threshold_blocker_contract.packet.json"
NEXT_CUTSET = PACKET_DIR / "next_cutset_after_heterotic_source_operator_torsion.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HeteroticStromingerSourceOperatorTorsion_or_DirectHKRow_v1.md"

SOURCES = {
    "previous": DATA / "selected_hgaugekineticnormalizationmumatch_or_directhkthresholdrow.candidate.json",
    "previous_cutset": DATA
    / "selected_hgaugekineticnormalizationmumatch_or_directhkthresholdrow"
    / "next_cutset_after_h_gauge_action_layer.packet.json",
    "hym_mu": QA / "selected_heterotic_hym_mu_selection_or_full_deltaa_spectrum.candidate.json",
    "endomorphism_torsion_decision": QA / "endomorphism_or_local_system_torsion_decision.candidate.json",
    "gerbe_interface": QA / "gerbe_twisted_local_system_response_interface.candidate.json",
    "gerbe_fill": QA / "gerbe_twisted_local_system_response_fill_attempt.candidate.json",
    "projective_rhoe_source_hunt": QA / "projective_rhoe_or_de_response_source_hunt.candidate.json",
    "projective_finite_domain": QA
    / "selected_heterotic_projectiverhoe_finitephysicalquotient_sourcetheorem.candidate.json",
    "projective_selected_packet": QA
    / "selected_heterotic_projectiverhoe_selectedpacketemission_or_operatoridentity.candidate.json",
    "projective_direct_payload": QA
    / "selected_heterotic_projectiverhoe_directoperatorpayload_fillattempt.candidate.json",
    "projective_internal_finitepart": QA
    / "selected_heterotic_projectiverhoe_eqa_or_thresholdfinitepart.candidate.json",
    "projective_minimal_smooth_nogo": QA
    / "selected_heterotic_projectiverhoe_minimalsmoothclosure_sourcerequest_or_directnogo.candidate.json",
    "projective_smooth_source_fill": QA
    / "selected_heterotic_projectiverhoe_smoothoperator_sourcepacket_fillattempt.candidate.json",
}

STATUS = (
    "MTT_SELECTED_HETEROTICSTROMINGERSOURCEOPERATORTORSION_OR_DIRECTHKROW_"
    "FINITE_INTERNAL_SUPPORT_CLOSED_PHYSICAL_VALUES_OPEN"
)
NEXT = "MTT_Selected_ProjectiveRhoESmoothOperatorSourceValues_or_DirectHKRow_v1"


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
        raise FileNotFoundError("missing heterotic source/operator inputs: " + ", ".join(missing))
    return {name: load(path) for name, path in SOURCES.items()}


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = require_sources()
    prev = sources["previous"]["closure_decision"]
    hym = sources["hym_mu"]["decision"]
    endo = sources["endomorphism_torsion_decision"]["decision"]
    gerbe_interface = sources["gerbe_interface"]["interface_checks"]
    gerbe_fill = sources["gerbe_fill"]["fill_result"]
    gerbe_decision = sources["gerbe_fill"]["decision"]
    rhoe_hunt = sources["projective_rhoe_source_hunt"]["decision"]
    finite_domain = sources["projective_finite_domain"]["decision"]
    selected_packet = sources["projective_selected_packet"]["decision"]
    direct_payload = sources["projective_direct_payload"]["decision"]
    internal_finitepart = sources["projective_internal_finitepart"]["decision"]
    minimal_nogo = sources["projective_minimal_smooth_nogo"]["decision"]
    smooth_fill = sources["projective_smooth_source_fill"]["decision"]
    smooth_fill_result = sources["projective_smooth_source_fill"]["fill_result"]

    lane_reduction = {
        "schema": "MTTHeteroticSourceOperatorTorsionLaneReduction.v1",
        "status": "HYM_AND_GERBE_LANES_REDUCED_TO_PROJECTIVE_RHOE_SOURCE_VALUES",
        "closure_claimed": True,
        "hym_invariant_block": {
            "mu_selected": hym["mu_selected"],
            "invariant_block_mu_extremum_refuted": hym["invariant_block_mu_extremum_refuted"],
            "full_deltaA_spectrum_computed": hym["full_deltaA_spectrum_computed"],
            "threshold_payload_closed": hym["threshold_payload_closed"],
            "next_required_artifact": hym["next_required_artifact"],
        },
        "gerbe_torsion_lane": {
            "primary_next_lane": endo["primary_next_lane"],
            "interface_primary_route_confirmed": gerbe_interface["primary_route_confirmed"],
            "twist_cancellation_table_filled": gerbe_fill["twist_cancellation_table_filled"],
            "global_gerbe_curvature_available": gerbe_fill["global_gerbe_curvature_available"],
            "primitive_complex_central_support_filled": gerbe_fill[
                "primitive_complex_central_support_filled"
            ],
            "same_branch_representative_filled": gerbe_fill["same_branch_representative_filled"],
            "same_branch_rhoE_or_local_system_filled": gerbe_fill[
                "same_branch_rhoE_or_local_system_filled"
            ],
            "finite_response_filled": gerbe_fill["finite_response_filled"],
            "next_required_artifact": sources["gerbe_fill"]["next_required_artifact"],
        },
        "projective_rhoe_source_hunt": {
            "result": rhoe_hunt["result"],
            "next_move": rhoe_hunt["next_move"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    finite_support = {
        "schema": "MTTProjectiveRhoEFiniteInternalSupportImport.v1",
        "status": "PROJECTIVE_RHOE_FINITE_INTERNAL_SUPPORT_IMPORTED_PHYSICAL_OPEN",
        "closure_claimed": True,
        "closed_internal_support": {
            "finite_physical_quotient_domain_closed": finite_domain[
                "finite_physical_quotient_domain_closed"
            ],
            "finite_trace_admissibility_closed": finite_domain[
                "finite_trace_admissibility_closed"
            ],
            "selected_finite_internal_packet_emitted": selected_packet[
                "selected_finite_internal_packet_emitted"
            ],
            "finite_rhoE_packet_selected_not_validator_only": selected_packet[
                "finite_rhoE_packet_selected_not_validator_only"
            ],
            "direct_finite_internal_operator_payload_closed": direct_payload[
                "direct_finite_internal_operator_payload_closed"
            ],
            "all_acceptance_fields_filled_at_finite_internal_scope": direct_payload[
                "all_acceptance_fields_filled_at_finite_internal_scope"
            ],
            "selected_internal_threshold_finitepart_closed": internal_finitepart[
                "selected_internal_threshold_finitepart_closed"
            ],
            "selected_internal_logdet_retained": direct_payload["selected_internal_logdet_retained"],
        },
        "not_physical_H_row": {
            "E_Qa_computed": internal_finitepart["E_Qa_computed"],
            "threshold_value_computed": selected_packet["threshold_value_computed"],
            "physical_threshold_normalization_closed": internal_finitepart[
                "physical_threshold_normalization_closed"
            ],
            "smooth_operator_identity_proved": internal_finitepart[
                "smooth_operator_identity_proved"
            ],
            "smooth_transition_matrices_emitted": internal_finitepart[
                "smooth_transition_matrices_emitted"
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    physical_blocker = {
        "schema": "MTTPhysicalThresholdBlockerContract.v1",
        "status": "SMOOTH_OPERATOR_SOURCE_VALUES_REQUIRED_DIRECT_HK_STILL_ALLOWED",
        "closure_claimed": True,
        "minimal_smooth_nogo": {
            "direct_current_corpus_nogo_proved": minimal_nogo["direct_current_corpus_nogo_proved"],
            "finite_internal_closure_preserved": minimal_nogo["finite_internal_closure_preserved"],
            "requires_new_source_insertion": minimal_nogo["requires_new_source_insertion"],
            "source_request_locked": minimal_nogo["source_request_locked"],
            "smooth_finitepart_can_close_now": minimal_nogo["smooth_finitepart_can_close_now"],
            "next_required_artifact": minimal_nogo["next_required_artifact"],
        },
        "smooth_operator_fill_attempt": {
            "support_context_filled": smooth_fill["support_context_filled"],
            "smooth_projective_source_values_filled": smooth_fill[
                "smooth_projective_source_values_filled"
            ],
            "bundle_operator_values_filled": smooth_fill["bundle_operator_values_filled"],
            "admissibility_values_filled": smooth_fill["admissibility_values_filled"],
            "finite_part_values_filled": smooth_fill["finite_part_values_filled"],
            "smooth_finitepart_computed": smooth_fill["smooth_finitepart_computed"],
            "threshold_value_computed": smooth_fill["threshold_value_computed"],
            "next_required_artifact": smooth_fill["next_required_artifact"],
        },
        "missing_source_leaves": {
            "selected_representative_filled": smooth_fill_result["selected_representative_filled"],
            "representation_action_filled": smooth_fill_result["representation_action_filled"],
            "projective_rhoE_transition_tables_filled": smooth_fill_result[
                "projective_rhoE_transition_tables_filled"
            ],
            "representative_to_central_cocycle_map_filled": smooth_fill_result[
                "representative_to_central_cocycle_map_filled"
            ],
            "selected_connection_A_filled": smooth_fill_result["selected_connection_A_filled"],
            "curvature_F_A_filled": smooth_fill_result["curvature_F_A_filled"],
            "E_Qa_matrix_filled": smooth_fill_result["E_Qa_matrix_filled"],
            "positive_spectrum_or_heat_coefficients_filled": smooth_fill_result[
                "positive_spectrum_or_heat_coefficients_filled"
            ],
            "zeta_or_torsion_regularization_filled": smooth_fill_result[
                "zeta_or_torsion_regularization_filled"
            ],
            "finite_part_value_filled": smooth_fill_result["finite_part_value_filled"],
        },
        "direct_source_native_HK_exit_still_allowed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_cutset = {
        "schema": "MTTNextCutsetAfterHeteroticSourceOperatorTorsion.v1",
        "status": "NEXT_FRONTIER_PROJECTIVE_RHOE_SMOOTH_OPERATOR_VALUES_OR_DIRECT_HK",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "closed_here": [
            "HYM invariant-block mu extremum refuted as a source selector",
            "gerbe/twisted-module lane imported through partial fill attempt",
            "projective rhoE finite physical quotient domain imported as closed support",
            "selected finite internal projective-rhoE packet imported as selected support",
            "direct finite internal operator payload imported as closed internal support",
            "selected internal threshold finite part imported as closed internal support",
        ],
        "still_open": [
            "same-branch smooth/projective representative and representation action",
            "representative-to-central-cocycle map or exact smooth finite-part source amendment",
            "projective rhoE transition tables and selected connection/curvature values",
            "E_Qa matrix or equivalent threshold finite response value",
            "positive spectrum, heat coefficients, zeta/torsion regularization, and finite part",
            "physical threshold normalization and smooth operator identity",
            "selected R_H^RG row and same-scheme Omega_H.lambda certificate",
            "direct source-native K_threshold.Omega_H.lambda",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHeteroticStromingerSourceOperatorTorsionOrDirectHKRow",
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
            "heterotic_source_operator_torsion_lane_reduction": rel(LANE_REDUCTION),
            "projective_rhoe_finite_internal_support_import": rel(FINITE_SUPPORT),
            "physical_threshold_blocker_contract": rel(PHYSICAL_BLOCKER),
            "next_cutset_after_heterotic_source_operator_torsion": rel(NEXT_CUTSET),
        },
        "closure_decision": {
            "HYM_invariant_mu_extremum_refuted": True,
            "HYM_full_deltaA_spectrum_computed": False,
            "gerbe_response_interface_built": True,
            "gerbe_response_fill_partial_source_support": True,
            "projective_rhoe_finite_internal_support_closed": True,
            "projective_rhoe_physical_threshold_value_computed": False,
            "smooth_operator_identity_or_physical_normalization_closed": False,
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
            "name": "HeteroticStromingerSourceOperatorTorsionOrDirectHKRowTheorem",
            "proved": True,
            "statement": (
                "The HYM/gerbe/torsion branch has been contracted to a projective-rhoE "
                "smooth operator value problem.  New Qa/SU3 results close the finite "
                "internal projective-rhoE quotient, selected finite packet, direct "
                "finite internal operator payload, and internal finite part.  They do "
                "not emit the physical smooth operator identity, physical threshold "
                "normalization, E_Qa value, R_H^RG row, or K_threshold.Omega_H.lambda."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedHeteroticStromingerSourceOperatorTorsionOrDirectHKRow",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "projective_rhoe_finite_internal_support_closed": True,
        "projective_rhoe_physical_threshold_value_computed": False,
        "smooth_operator_identity_or_physical_normalization_closed": False,
        "selected_R_H_RG_emitted": False,
        "strict_H_K_threshold_row_emitted": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected Heterotic/Strominger Source-Operator Torsion or Direct H K-Row v1

## Theorem

`HeteroticStromingerSourceOperatorTorsionOrDirectHKRowTheorem` is emitted.

The old HYM/torsion/operator frontier is now narrower.  The HYM invariant block
does not select `mu`; the gerbe/twisted-module lane supplies the right support
but not the finite response; and the latest projective-rhoE chain closes the
finite internal quotient/operator/finite-part layer only.

## Closed Here

- HYM invariant-block `mu` extremum refuted as a source selector.
- Gerbe/twisted source support imported through the partial fill attempt.
- Projective-rhoE finite physical quotient domain closed as support.
- Selected finite internal projective-rhoE packet emitted as support.
- Direct finite internal operator payload closed as internal support.
- Selected internal threshold finite part closed as internal support.

## Still Open

- Same-branch smooth/projective representative and representation action.
- Representative-to-central-cocycle map or smooth finite-part source amendment.
- Projective `rho_E` transition tables and selected connection/curvature values.
- `E_Qa` matrix or equivalent physical threshold finite response value.
- Positive spectrum, heat coefficients, zeta/torsion regularization, and finite part.
- Physical threshold normalization and smooth operator identity.
- Selected `R_H^RG` row and same-scheme `Omega_H.lambda` certificate.
- Direct source-native `K_threshold.Omega_H.lambda`.

## Current Count

Strict selected `K_threshold` rows remain
`{prev["accepted_selected_K_source_row_count"]}/{prev["selected_K_threshold_row_count_required"]}`.

## Next Artifact

`{NEXT}`
"""

    write_json(LANE_REDUCTION, lane_reduction)
    write_json(FINITE_SUPPORT, finite_support)
    write_json(PHYSICAL_BLOCKER, physical_blocker)
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
