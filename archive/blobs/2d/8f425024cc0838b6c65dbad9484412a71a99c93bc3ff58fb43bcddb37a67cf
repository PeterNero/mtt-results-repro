"""Attempt to fill direct BN27 source-identity transport or typed connection values."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "transport_gate": DATA / "selected_heterotic_orientedphifin_bn27_sourceownership_transport_or_connectionwitness_values.candidate.json",
    "transport_template": DATA / "selected_heterotic_orientedphifin_bn27_sourceownership_transport_witness.template.json",
    "u1y_selected_source_or_typed_de": DATA / "selected_u1y_routec_selected_source_certificate_or_typed_de_construction.candidate.json",
    "u1y_finite_hym_or_typed_cech": DATA / "selected_u1y_routec_finite_hym_connection_solve_or_typed_cech_payload.candidate.json",
    "sourcebranch_repair": DATA / "selected_heterotic_orientedphifin_sourcebranchidentity_sourceamendment_or_connectionvalues.candidate.json",
    "sourcebranch_repair_packet": DATA / "selected_heterotic_orientedphifin_sourcebranchidentity_repair_packet.json",
    "connection_export_fill": DATA / "selected_heterotic_orientedphifin_selectedconnectionwitness_export_fill.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_directbn27_sourceidentitytransport_fill_or_typedconnectionwitnessvalues.candidate.json"
OUTPUT_CONTRACT = DATA / "selected_heterotic_orientedphifin_directbn27_sourceidentitytransport_acceptance_contract.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_directbn27_sourceidentitytransport_fill_or_typedconnectionwitnessvalues_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_DirectBN27_SourceIdentityTransport_Fill_or_TypedConnectionWitnessValues_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_DIRECTBN27_SOURCEIDENTITY_FILL_DE_GAP_IMPORTED_TRANSPORT_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_BN27_SourceIdentity_DirectSourceTheorem_or_ConnectionValuesExternalConstruction_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    transport = load(INPUTS["transport_gate"])
    template = load(INPUTS["transport_template"])
    u1y_source = load(INPUTS["u1y_selected_source_or_typed_de"])
    u1y_finite = load(INPUTS["u1y_finite_hym_or_typed_cech"])
    repair = load(INPUTS["sourcebranch_repair"])
    repair_packet = load(INPUTS["sourcebranch_repair_packet"])
    export = load(INPUTS["connection_export_fill"])

    finite_decision = u1y_finite["decision"]
    u1y_decision = u1y_source["decision"]
    support_import = {
        "finite_BN_basis_closed_for_gap_layer": u1y_finite["what_closes_now"]["finite_BN_basis_closed_for_gap_layer"],
        "DE_action_closed_for_gap_layer": finite_decision["DE_action_closed_for_gap_layer"],
        "Riesz_Green_gap_layer_closed": finite_decision["Riesz_Green_gap_layer_closed"],
        "selected_trace_equality_for_27mode_DE_imported": u1y_finite["what_closes_now"]["selected_trace_equality_for_27mode_DE_imported"],
        "analytic_alpha1_kernel_ready_once_tangent_exists": u1y_finite["what_closes_now"]["analytic_alpha1_kernel_imported_as_ready_once_tangent_exists"],
    }

    contract = {
        "schema": "SelectedHeterotic.OrientedPhiFin.DirectBN27.SourceIdentityTransport.AcceptanceContract.v1",
        "status": "OPEN_SOURCE_IDENTITY_OR_CONNECTION_VALUES_REQUIRED",
        "direct_source_identity_payload": {
            "source_object_named_S_QaSU3_BN27": None,
            "full_F3xF3_rank_slot_carrier_emitted_before_finite_comparison": None,
            "C_tau_and_PhiFin_DE_coemitted_by_source": None,
            "RouteC_q79_row_internal_to_source_not_imported": None,
            "kernel_shared_circle_policy_source_owned": None,
            "finitepart_log92160000_identity_source_owned": None,
            "theorem_derived_selected_source_flags": None,
        },
        "typed_or_connection_payload": {
            "typed_f_sections": None,
            "typed_g_sections": None,
            "cech_transitions_and_cocycles": None,
            "g_after_f_zero_and_exactness_certificate": None,
            "selected_HYM_or_projective_connection_coefficients": None,
            "residual_bounds_or_exact_connection_equations": None,
            "BN27_operator_export_to_DE_Riesz_Green_kernel_trace": None,
            "no_lifted_flags_replay_audit": None,
        },
        "already_importable_support": support_import,
        "forbidden": template["forbidden_shortcuts"] + [
            "treat selected 27-mode D_E trace equality as source identity",
            "treat alpha1 analytic formula as selected tangent values",
        ],
        "target_fitting_used": False,
    }
    OUTPUT_CONTRACT.write_text(json.dumps(contract, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    lane_evaluation = {
        "direct_source_identity_transport": {
            "closed_now": False,
            "new_support_used": "heterotic branch certificate plus U1/Y 27-mode D_E gap/Riesz/Green support",
            "first_missing": "source_object_named_S_QaSU3_BN27",
            "missing_payload": repair_packet["minimal_success_payload"]["source_identity_transport_theorem"],
            "why_not_closed": "The imported D_E gap layer is an operator support theorem, not a theorem that the Route-C/q79 row is internal to the heterotic BN27 source.",
        },
        "typed_connection_witness_values": {
            "closed_now": False,
            "first_missing": "typed f_i/g_i sections and Cech transition data",
            "missing_payload": repair_packet["minimal_success_payload"]["selected_connection_values_alternative"],
            "u1y_current_status": u1y_source["status"],
            "why_not_closed": "The U1/Y stack classifies the same obstruction: finite prefix values exist, but selected connection witness values and theorem-derived source flags remain absent.",
        },
        "finite_routec_hym_solve": {
            "closed_now": False,
            "support_promoted_for_gap_layer": True,
            "remaining_open": u1y_finite["what_remains_open"],
            "why_not_closed": "The finite Route-C/HYM route promotes only the D_E gap/Riesz/Green layer; dotD alpha1, full connection lift, primitive C1, A_selected/b_selected, and selected source normalization remain open.",
        },
    }

    decision = {
        "attempt_executed": True,
        "DE_gap_Riesz_Green_export_support_closed": all(support_import.values()),
        "direct_source_identity_transport_closed": False,
        "typed_connection_witness_values_found": False,
        "finite_routec_hym_full_connection_closed": False,
        "selected_connection_witness_export_closed": False,
        "BN27_source_ownership_transport_closed": False,
        "source_object_named_S_QaSU3_BN27": False,
        "oriented_logdet_promoted": False,
        "acceptance_contract_path": rel(OUTPUT_CONTRACT),
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinDirectBN27SourceIdentityTransportFillOrTypedConnectionWitnessValues",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "transport_gate": transport["status"],
            "u1y_selected_source_or_typed_de": u1y_source["status"],
            "u1y_finite_hym_or_typed_cech": u1y_finite["status"],
            "sourcebranch_repair": repair["status"],
            "connection_export_fill": export["status"],
        },
        "new_support_imported": support_import,
        "lane_evaluation": lane_evaluation,
        "acceptance_contract_path": rel(OUTPUT_CONTRACT),
        "decision": decision,
        "theorem": {
            "name": "DirectBN27SourceIdentityFillAttemptDEGapImportTheorem",
            "proved": True,
            "statement": (
                "The next fill attempt can import the selected 27-mode D_E gap/Riesz/Green support from the U1/Y Route-C "
                "finite-HYM branch, but this does not close BN27 source-identity transport. The direct source route still "
                "needs S_QaSU3^BN27 and a proof that the Route-C/q79 row is internal to that source. The typed/connection "
                "route still needs actual typed Cech/HYM/projective connection values with theorem-derived source flags."
            ),
        },
        "guardrails": {
            "does_not_treat_DE_gap_support_as_source_identity": True,
            "does_not_promote_log92160000": True,
            "does_not_promote_routec_import": True,
            "does_not_use_lifted_selected_flags": True,
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
        "acceptance_contract_path": rel(OUTPUT_CONTRACT),
        "note_path": rel(OUTPUT_NOTE),
        "DE_gap_Riesz_Green_export_support_closed": decision["DE_gap_Riesz_Green_export_support_closed"],
        "direct_source_identity_transport_closed": False,
        "typed_connection_witness_values_found": False,
        "BN27_source_ownership_transport_closed": False,
        "oriented_logdet_promoted": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin DirectBN27 SourceIdentityTransport Fill or TypedConnectionWitnessValues v1

## Result

```text
status = {STATUS}
DE_gap_Riesz_Green_export_support_closed = true
source_object_named_S_QaSU3_BN27 = false
direct_source_identity_transport_closed = false
typed_connection_witness_values_found = false
BN27_source_ownership_transport_closed = false
oriented_logdet_promoted = false
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

## Acceptance Contract

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
