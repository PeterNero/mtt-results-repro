"""Build source-owned positive-operator / E_Qa payload fill attempt."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "contract": DATA / "selected_heterotic_orientedphifin_positivemagnitude_sourceownership_or_smootheqa_emission_contract.json",
    "positive_gate": DATA / "selected_heterotic_orientedphifin_positivemagnitude_sourceownership_or_smootheqa_emission.candidate.json",
    "direct_response_packet": DATA / "selected_heterotic_orientedphifin_directfiniteresponse_fillattempt_packet.json",
    "ownership_values": DATA / "selected_heterotic_orientedphifin_sourceownership_certificate_fillattempt.values.json",
    "standard_embedding_gate": DATA / "selected_heterotic_standard_embedding_selector_or_phifin_gate.candidate.json",
    "bundle_policy": DATA / "selected_heterotic_projectiverhoe_bundleconnection_trace_quotient_policy.candidate.json",
    "rplus_payload": DATA / "selected_heterotic_rplus_curvature_payload_fill.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_sourceownedpositiveoperator_or_eqapayload_fill.candidate.json"
OUTPUT_PACKET = DATA / "selected_heterotic_orientedphifin_sourceownedpositiveoperator_or_eqapayload_minimal_source_packet.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_sourceownedpositiveoperator_or_eqapayload_fill_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_SourceOwnedPositiveOperator_or_EQaPayload_Fill_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_SOURCEOWNED_POSITIVE_OPERATOR_OR_EQA_PAYLOAD_FILL_VALUES_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_MinimalNewSourcePacket_Fill_or_ProofClosure_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def field_filled(fields: dict[str, Any], name: str) -> bool:
    return fields[name].get("filled") is True


def main() -> dict[str, Any]:
    contract = load(INPUTS["contract"])
    positive_gate = load(INPUTS["positive_gate"])
    direct = load(INPUTS["direct_response_packet"])
    ownership = load(INPUTS["ownership_values"])
    standard_embedding = load(INPUTS["standard_embedding_gate"])
    bundle_policy = load(INPUTS["bundle_policy"])
    rplus = load(INPUTS["rplus_payload"])

    ownership_fields = ownership["filled_certificate_fields"]
    direct_source_attempt = {
        "same_branch_certificate": field_filled(ownership_fields, "same_branch_QaSU3_heterotic_source_certificate"),
        "orientation_binding": field_filled(ownership_fields, "C_tau_orientation_bound_to_same_threshold_complex"),
        "no_double_count_shared_circle_policy": field_filled(ownership_fields, "kernel_zero_mode_shared_circle_policy_replayed"),
        "oriented_BN_carrier_emitted": field_filled(ownership_fields, "oriented_BN_carrier_emitted_by_that_source"),
        "EndE_or_rhoE_operator_functor_or_quotient": field_filled(ownership_fields, "quotient_or_functor_EndE_or_rhoE_to_oriented_BN"),
        "positive_PhiFin_magnitude_owned": field_filled(ownership_fields, "positive_PhiFin_DE_magnitude_owned_by_source"),
        "finite_threshold_complex_quotient": field_filled(ownership_fields, "smooth_EQa_or_finite_threshold_complex_quotients_to_packet"),
        "finitepart_trace_identity": field_filled(ownership_fields, "finitepart_trace_identity_consumes_nonzero_oriented_sector"),
        "table_D_E_Riesz_Green_positive_spectrum_materialized": (
            bool(direct["operator_values_materialized"]["D_E_diagonal_on_oriented_nonzero_BN"])
            and direct["operator_values_materialized"]["minimum_positive_eigenvalue"] > 0
        ),
        "exact_finitepart_ready": positive_gate["decision"]["oriented_table_values_ready_to_consume"],
        "closed": False,
    }

    smooth_attempt = {
        "standard_embedding_retired_for_current_branch": standard_embedding["decision"]["standard_embedding_retired_as_current_proof_source"],
        "finite_internal_trace_policy_closed": bundle_policy["decision"]["finite_internal_trace_and_quotient_policy_closed"],
        "R_plus_geometry_filled": rplus["decision"]["R_plus_curvature_filled"],
        "selected_bundle_connection_A": False,
        "bundle_curvature_F_A": False,
        "representation_action_on_uE_one_forms": False,
        "trace_normalization": False,
        "kernel_and_quotient_policy_to_oriented_BN": False,
        "E_Qa_matrix_or_equivalent_zero_order_block": False,
        "positive_spectrum_heat_zeta_or_torsion_finitepart": False,
        "trace_lift_or_complement_quotient_proof": False,
        "closed": False,
    }

    minimal_source_packet = {
        "schema": "SelectedHeterotic.OrientedPhiFin.SourceOwnedPositiveOperatorOrEQaPayload.MinimalSourcePacket.v1",
        "status": "OPEN_SOURCE_VALUES_REQUIRED",
        "known_values": contract["known_exact_values_to_consume"],
        "route_A_direct_source_owned_positive_operator": {
            "required_fields": {
                "source_emits_oriented_BN_carrier": None,
                "source_emits_EndE_or_rhoE_to_oriented_BN_operator_functor_or_quotient": None,
                "source_emits_positive_PhiFin_D_E_magnitude_on_oriented_BN": None,
                "source_certifies_Riesz_Green_positive_spectrum": None,
                "source_proves_finitepart_trace_identity_for_log92160000": None,
            },
            "already_available_support": [
                "same_branch_QaSU3_heterotic_source_certificate",
                "C_tau orientation binding",
                "shared-circle/no-double-count policy",
                "exact oriented table values log(92160000), log(9600), log(884736000000)",
            ],
        },
        "route_B_smooth_EQa_payload": {
            "required_fields": {
                "selected_bundle_connection_A": None,
                "bundle_curvature_F_A": None,
                "representation_action_on_uE_one_forms": None,
                "trace_normalization": None,
                "kernel_and_quotient_policy_to_oriented_BN": None,
                "E_Qa_matrix_or_equivalent_zero_order_block": None,
                "positive_spectrum_heat_zeta_or_torsion_finitepart": None,
                "trace_lift_or_complement_quotient_proof": None,
            },
            "already_available_support": [
                "selected invariant Bismut/R_plus geometry",
                "finite internal trace and quotient policy at eleven-label scope",
                "standard embedding explicitly retired for current source branch",
            ],
        },
        "forbidden_shortcuts": contract["forbidden_shortcuts"]
        + [
            "declare the oriented 27-mode table source-owned by naming alone",
            "use the finite internal eleven-label quotient as the oriented 27-mode quotient without an operator functor",
        ],
        "target_fitting_used": False,
    }
    OUTPUT_PACKET.write_text(json.dumps(minimal_source_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    decision = {
        "fill_attempted": True,
        "direct_source_owned_positive_operator_closed": False,
        "smooth_EQa_payload_closed": False,
        "minimal_source_packet_written": True,
        "minimal_source_packet_path": rel(OUTPUT_PACKET),
        "oriented_abs_sector_logdet_exact": contract["known_exact_values_to_consume"]["oriented_abs_sector_logdet_exact"],
        "oriented_logdet_promoted": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinSourceOwnedPositiveOperatorOrEQaPayloadFill",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "positive_gate": positive_gate["status"],
            "standard_embedding_gate": standard_embedding["status"],
            "bundle_policy": bundle_policy["status"],
            "rplus": rplus["status"],
        },
        "attempts": {
            "direct_source_owned_positive_operator": direct_source_attempt,
            "smooth_EQa_payload": smooth_attempt,
        },
        "decision": decision,
        "theorem": {
            "name": "SourceOwnedPositiveOperatorOrEQaPayloadCurrentSourceFillTheorem",
            "proved": True,
            "statement": (
                "The current repository can fill support for the oriented positive magnitude "
                "problem but not the source-owned operator itself. The exact oriented table "
                "values, same-branch source certificate, orientation binding, no-double-count "
                "policy, and R+ geometry are available. Closure still requires one new source "
                "packet: either a direct source-owned positive Phi_fin operator on oriented B_N "
                "with finitepart trace identity, or a smooth E_Qa/heat-zeta-torsion payload "
                "with selected bundle connection, curvature, representation trace, quotient "
                "policy, and trace lift."
            ),
        },
        "guardrails": {
            "does_not_promote_table_values_to_threshold": True,
            "does_not_reopen_standard_embedding": True,
            "does_not_use_R_plus_as_E_Qa": True,
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
        "minimal_source_packet_path": rel(OUTPUT_PACKET),
        "note_path": rel(OUTPUT_NOTE),
        "direct_source_owned_positive_operator_closed": False,
        "smooth_EQa_payload_closed": False,
        "minimal_source_packet_written": True,
        "oriented_abs_sector_logdet_exact": contract["known_exact_values_to_consume"]["oriented_abs_sector_logdet_exact"],
        "oriented_logdet_promoted": False,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin SourceOwnedPositiveOperator or EQaPayload Fill v1

## Result

```text
status = {STATUS}
direct_source_owned_positive_operator_closed = false
smooth_EQa_payload_closed = false
minimal_source_packet_written = true
oriented_abs_sector_logdet_exact = {contract["known_exact_values_to_consume"]["oriented_abs_sector_logdet_exact"]}
oriented_logdet_promoted = false
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

## Minimal Source Packet

```text
{rel(OUTPUT_PACKET)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_PACKET)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
