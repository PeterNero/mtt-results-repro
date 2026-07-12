"""Build positive-magnitude source-ownership / smooth-EQa emission attempt."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "magnitude_finitepart": DATA / "selected_heterotic_orientedphifin_magnitudefinitepart_sourcetheorem_or_smootheqa_traceidentity.candidate.json",
    "magnitude_packet": DATA / "selected_heterotic_orientedphifin_magnitudefinitepart_sourcetheorem_or_smootheqa_traceidentity_packet.json",
    "source_ownership_values": DATA / "selected_heterotic_orientedphifin_sourceownership_certificate_fillattempt.values.json",
    "direct_response_packet": DATA / "selected_heterotic_orientedphifin_directfiniteresponse_fillattempt_packet.json",
    "smooth_required": DATA / "selected_heterotic_projectiverhoe_smooth_operator_source_packet_required.json",
    "rplus_payload": DATA / "selected_heterotic_rplus_curvature_payload_fill.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_positivemagnitude_sourceownership_or_smootheqa_emission.candidate.json"
OUTPUT_CONTRACT = DATA / "selected_heterotic_orientedphifin_positivemagnitude_sourceownership_or_smootheqa_emission_contract.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_positivemagnitude_sourceownership_or_smootheqa_emission_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_PositiveMagnitude_SourceOwnership_or_SmoothEQa_Emission_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_POSITIVEMAGNITUDE_SOURCEOWNERSHIP_AND_SMOOTHEQA_EMISSION_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_SourceOwnedPositiveOperator_or_EQaPayload_Fill_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def filled(field: dict[str, Any]) -> bool:
    return field.get("filled") is True


def main() -> dict[str, Any]:
    magnitude = load(INPUTS["magnitude_finitepart"])
    magnitude_packet = load(INPUTS["magnitude_packet"])
    ownership_values = load(INPUTS["source_ownership_values"])
    direct = load(INPUTS["direct_response_packet"])
    smooth_required = load(INPUTS["smooth_required"])
    rplus = load(INPUTS["rplus_payload"])

    ownership_fields = ownership_values["filled_certificate_fields"]
    direct_leaf_status = direct["leaf_status"]
    smooth_minimum = smooth_required["minimum_smooth_operator_payload"]
    rplus_missing = rplus["missing_fields"]

    direct_lane = {
        "lane": "direct_source_owned_positive_operator",
        "same_branch_certificate_closed": filled(ownership_fields["same_branch_QaSU3_heterotic_source_certificate"]),
        "orientation_bound_to_same_threshold_complex": filled(ownership_fields["C_tau_orientation_bound_to_same_threshold_complex"]),
        "oriented_BN_carrier_emitted": filled(ownership_fields["oriented_BN_carrier_emitted_by_that_source"]),
        "EndE_or_rhoE_to_oriented_BN_functor": filled(ownership_fields["quotient_or_functor_EndE_or_rhoE_to_oriented_BN"]),
        "positive_PhiFin_magnitude_owned": filled(ownership_fields["positive_PhiFin_DE_magnitude_owned_by_source"]),
        "finite_threshold_complex_quotients_to_packet": filled(ownership_fields["smooth_EQa_or_finite_threshold_complex_quotients_to_packet"]),
        "finitepart_trace_identity": filled(ownership_fields["finitepart_trace_identity_consumes_nonzero_oriented_sector"]),
        "direct_response_D_E_support_materialized": direct_leaf_status["D_E_or_EQa_matrix_on_oriented_BN"]["support"] is not None,
        "direct_response_positive_spectrum_support_materialized": direct_leaf_status["positive_spectrum_or_heat_zeta_torsion"]["support"] is not None,
        "closed": False,
    }

    smooth_lane = {
        "lane": "smooth_EQa_or_heat_zeta_torsion_emission",
        "R_plus_curvature_filled": rplus["decision"]["R_plus_curvature_filled"],
        "geometric_tensor_payload_filled": rplus["decision"]["geometric_tensor_payload_filled"],
        "bundle_connection_A_filled": "connection_A_components" not in rplus_missing,
        "bundle_curvature_F_A_filled": "curvature_F_A_components" not in rplus_missing,
        "ad_bundle_representation_filled": "ad_bundle_representation" not in rplus_missing,
        "trace_normalization_filled": "trace_normalization" not in rplus_missing,
        "E_Qa_matrix_filled": "E_Qa_matrix" not in rplus_missing,
        "kernel_and_quotient_policy_filled": "kernel_and_quotient_policy" not in rplus_missing,
        "smooth_required_payload": smooth_minimum,
        "closed": False,
    }

    contract = {
        "schema": "SelectedHeterotic.OrientedPhiFin.PositiveMagnitude.SourceOwnedOperatorOrEQaPayload.Contract.v1",
        "status": "OPEN_FILL_REQUIRED",
        "accepted_closing_routes": [
            "emit source-owned positive Phi_fin operator on oriented B_N with quotient/functor and finitepart trace identity",
            "emit smooth E_Qa or heat-zeta-torsion packet whose finite quotient is the oriented 27-mode positive operator",
        ],
        "known_exact_values_to_consume": {
            "oriented_abs_sector_logdet_exact": magnitude["decision"]["oriented_abs_sector_logdet_exact"],
            "full_positive_logdet_exact": magnitude["decision"]["full_positive_logdet_exact"],
            "plus_sector_logdet_exact": magnitude_packet["finitepart_values"]["plus_sector_logdet_exact"],
            "minus_sector_logdet_exact": magnitude_packet["finitepart_values"]["minus_sector_logdet_exact"],
        },
        "direct_source_owned_operator_required_fields": {
            "same_branch_QaSU3_heterotic_source_certificate": "FILLED",
            "oriented_BN_carrier_emitted_by_that_source": None,
            "EndE_or_rhoE_to_oriented_BN_operator_functor_or_quotient": None,
            "positive_PhiFin_DE_magnitude_owned_by_source": None,
            "Riesz_Green_and_positive_spectrum_source_certified": None,
            "finitepart_trace_identity_consumes_log92160000": None,
            "no_double_count_and_shared_circle_policy": "FILLED_SUPPORT",
        },
        "smooth_EQa_required_fields": {
            "R_plus_curvature": "FILLED_GEOMETRY_ONLY",
            "selected_bundle_connection_A": None,
            "bundle_curvature_F_A": None,
            "representation_action_on_uE_one_forms": None,
            "trace_normalization": None,
            "kernel_and_quotient_policy_to_oriented_BN": None,
            "E_Qa_matrix_or_equivalent_zero_order_block": None,
            "positive_spectrum_heat_zeta_or_torsion_finitepart": None,
            "trace_lift_or_complement_quotient_proof": None,
        },
        "forbidden_shortcuts": [
            "promote Route-C 27-mode support to heterotic source ownership without a source theorem",
            "identify log(92160000) with log(2008)",
            "use R_plus geometry as E_Qa without selected bundle A/F_A and representation trace",
            "use observed couplings, matching scales, or residual fits",
        ],
        "target_fitting_used": False,
    }
    OUTPUT_CONTRACT.write_text(json.dumps(contract, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    decision = {
        "positive_magnitude_sourceownership_attempted": True,
        "direct_source_owned_positive_operator_closed": False,
        "smooth_EQa_emission_closed": False,
        "oriented_table_values_ready_to_consume": True,
        "oriented_abs_sector_logdet_exact": magnitude["decision"]["oriented_abs_sector_logdet_exact"],
        "source_owned_positive_PhiFin_magnitude": False,
        "finitepart_trace_identity_closed": False,
        "smooth_E_Qa_trace_identity_closed": False,
        "oriented_logdet_promoted": False,
        "contract_path": rel(OUTPUT_CONTRACT),
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinPositiveMagnitudeSourceOwnershipOrSmoothEQaEmission",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "magnitude_finitepart": magnitude["status"],
            "rplus_payload": rplus["status"],
            "ownership_values": ownership_values["status"],
        },
        "lanes": {
            "direct_source_owned_operator": direct_lane,
            "smooth_EQa_emission": smooth_lane,
        },
        "decision": decision,
        "theorem": {
            "name": "PositiveMagnitudeSourceOwnershipOrSmoothEQaEmissionCurrentSourceAttempt",
            "proved": True,
            "statement": (
                "The oriented Phi_fin positive magnitude now has exact finite table values "
                "ready for consumption, including oriented absolute finitepart log(92160000). "
                "A current-source fill attempt across the two legal lanes does not yet close "
                "threshold ownership: the direct lane still lacks source-emitted oriented B_N, "
                "an End(E)/rho_E operator functor or quotient, positive Phi_fin ownership, and "
                "finitepart trace identity; the smooth lane has R+ geometry but still lacks the "
                "selected bundle connection, bundle curvature, representation trace, quotient "
                "policy, E_Qa, and heat/zeta/torsion finitepart."
            ),
        },
        "guardrails": {
            "does_not_promote_table_values_to_threshold": True,
            "does_not_promote_R_plus_to_E_Qa": True,
            "does_not_identify_log92160000_with_log2008": True,
            "does_not_use_observed_data": True,
            "target_fitting_used": False,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "contract_path": rel(OUTPUT_CONTRACT),
        "note_path": rel(OUTPUT_NOTE),
        "direct_source_owned_positive_operator_closed": False,
        "smooth_EQa_emission_closed": False,
        "oriented_table_values_ready_to_consume": True,
        "oriented_abs_sector_logdet_exact": magnitude["decision"]["oriented_abs_sector_logdet_exact"],
        "source_owned_positive_PhiFin_magnitude": False,
        "finitepart_trace_identity_closed": False,
        "smooth_E_Qa_trace_identity_closed": False,
        "oriented_logdet_promoted": False,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin PositiveMagnitude SourceOwnership or SmoothEQa Emission v1

## Result

```text
status = {STATUS}
oriented_table_values_ready_to_consume = true
oriented_abs_sector_logdet_exact = {magnitude["decision"]["oriented_abs_sector_logdet_exact"]}
direct_source_owned_positive_operator_closed = false
smooth_EQa_emission_closed = false
oriented_logdet_promoted = false
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

## Contract

```text
{rel(OUTPUT_CONTRACT)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CONTRACT)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
