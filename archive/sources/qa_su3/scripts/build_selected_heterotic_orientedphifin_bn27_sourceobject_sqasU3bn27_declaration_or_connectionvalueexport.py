"""Build BN27 source-object declaration / connection-value export interface."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "prior_gate": DATA / "selected_heterotic_orientedphifin_bn27_sourceownedlogdet_minimalemissionpacket_fill_or_sourceamendment.candidate.json",
    "source_amendment_template": DATA / "selected_heterotic_orientedphifin_bn27_sourceownedlogdet_source_amendment_template.json",
    "connection_request": DATA / "selected_heterotic_orientedphifin_bn27_connectionvalues_externalconstruction_request.json",
    "minimal_root_cutset": DATA / "selected_heterotic_orientedphifin_bn27_sourceidentity_minimal_root_cutset.json",
    "source_owned_certificate": DATA / "selected_heterotic_orientedphifin_bn27_source_owned_certificate.refined.json",
    "u1y_connection_witness_contract": DATA / "selected_u1y_routec_typed_monad_cech_or_hym_connection_witness.candidate.json",
    "u1y_selected_source_certificate": DATA / "selected_u1y_routec_selected_source_certificate_or_typed_de_construction.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_bn27_sourceobject_sqasU3bn27_declaration_or_connectionvalueexport.candidate.json"
OUTPUT_INTERFACE = DATA / "selected_heterotic_orientedphifin_bn27_sourceobject_sqasU3bn27_declaration_interface.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_bn27_sourceobject_sqasU3bn27_declaration_or_connectionvalueexport_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_BN27_SourceObject_SQaSU3BN27_Declaration_or_ConnectionValueExport_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_BN27_SOURCEOBJECT_DECLARATION_INTERFACE_BUILT_VALUES_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_BN27_SourceObject_DeclarationInterface_Fill_or_SelectedConnectionValues_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def null_fields(fields: dict[str, Any]) -> bool:
    return all(value is None for value in fields.values())


def main() -> dict[str, Any]:
    prior = load(INPUTS["prior_gate"])
    template = load(INPUTS["source_amendment_template"])
    connection_request = load(INPUTS["connection_request"])
    cutset = load(INPUTS["minimal_root_cutset"])
    source_cert = load(INPUTS["source_owned_certificate"])
    u1y_witness = load(INPUTS["u1y_connection_witness_contract"])
    u1y_source = load(INPUTS["u1y_selected_source_certificate"])

    direct_fields = template["smallest_direct_source_amendment"]
    connection_fields = template["equivalent_connection_export"]
    roots = cutset["minimal_roots"]

    declaration_interface = {
        "schema": "SelectedHeterotic.OrientedPhiFin.BN27.SourceObjectDeclaration.Interface.v1",
        "status": "INTERFACE_BUILT_VALUES_OPEN",
        "source_object": {
            "symbol": "S_QaSU3^BN27",
            "bare_name_is_not_sufficient": True,
            "definition": "The selected heterotic Qa/SU3 source object emitting the full oriented BN27 threshold packet.",
            "required_exports": {
                "full_F3xF3_rank_slot_carrier": None,
                "C_tau_operator": None,
                "PhiFin_DE_operator": None,
                "operator_coemission_and_commutation": None,
                "kernel_shared_circle_policy": None,
                "trace_policy_and_index_scale": None,
                "finitepart_log92160000_identity": None,
                "not_routec_import_provenance": None,
                "theorem_derived_selected_source_flags": None,
            },
        },
        "equivalent_connection_value_export": {
            "typed_cech_monad": {
                "typed_f_sections": None,
                "typed_g_sections": None,
                "cech_transitions_and_cocycles": None,
                "g_after_f_zero_and_exactness_certificate": None,
                "BN27_operator_export_to_DE_Riesz_Green_kernel_trace": None,
                "no_lifted_flags_replay_audit": None,
            },
            "direct_hym_or_strominger": {
                "selected_HYM_or_projective_connection_coefficients": None,
                "residual_bounds_or_exact_connection_equations": None,
                "canonical_metric_connection_source": None,
                "BN27_operator_export_to_DE_Riesz_Green_kernel_trace": None,
                "no_lifted_flags_replay_audit": None,
            },
            "finite_routec_solve": {
                "selected_trace_equality_to_27mode_operator": roots["selected_trace_equality_to_27mode_operator"]["current_status"],
                "full_selected_iwasawa_strominger_operator_formula": roots["full_selected_iwasawa_strominger_operator_formula"]["current_status"],
                "theorem_derived_selected_source_flags": roots["theorem_derived_selected_source_flags"]["current_status"],
                "same_source_export_to_BN27_validators": None,
            },
        },
        "known_values_to_consume": template["known_values_to_consume"],
        "must_not_use": template["must_not_use"] + [
            "do not close by naming S_QaSU3^BN27 without the required exports",
            "do not treat selected trace equality for the D_E gap layer as full source identity",
        ],
        "target_fitting_used": False,
    }
    OUTPUT_INTERFACE.write_text(json.dumps(declaration_interface, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    route_evaluation = {
        "direct_source_object_declaration": {
            "interface_built": True,
            "closed_now": False,
            "bare_name_rejected": True,
            "all_required_exports_open": null_fields(declaration_interface["source_object"]["required_exports"]),
            "first_missing": "full_F3xF3_rank_slot_carrier",
            "support_available": {
                "heterotic_branch_certificate_closed": source_cert["source_certificate"]["heterotic_QaSU3_branch_certificate_closed"],
                "BN27_source_declared_as_selected_source": source_cert["source_certificate"]["S_QaSU3_BN27_declared_as_selected_source"],
                "exact_logdet_ready": template["known_values_to_consume"]["oriented_abs_sector_product"] == 92160000,
            },
        },
        "equivalent_connection_value_export": {
            "interface_built": True,
            "closed_now": False,
            "first_missing": "typed Cech/HYM/finite Route-C selected connection values",
            "u1y_contract_support": {
                "status": u1y_witness["status"],
                "current_payload_open": u1y_witness["decision"]["selected_connection_witness_constructed"] is False,
            },
            "u1y_source_certificate_support": {
                "status": u1y_source["status"],
                "selected_connection_witness_open": u1y_source["decision"]["selected_connection_witness_values_absent"] is True,
            },
        },
        "finite_routec_solve_export": {
            "interface_built": True,
            "closed_now": False,
            "first_missing": "full selected operator formula and theorem-derived selected source flags",
            "minimal_roots": {
                key: roots[key]["current_status"] for key in roots
            },
        },
    }

    decision = {
        "attempt_executed": True,
        "source_object_declaration_interface_built": True,
        "bare_source_name_rejected_as_closure": True,
        "direct_source_object_declaration_closed": False,
        "equivalent_connection_value_export_closed": False,
        "finite_routec_solve_export_closed": False,
        "source_object_named_S_QaSU3_BN27": False,
        "BN27_source_identity_closed": False,
        "oriented_logdet_promoted": False,
        "declaration_interface_path": rel(OUTPUT_INTERFACE),
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinBN27SourceObjectSQaSU3BN27DeclarationOrConnectionValueExport",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "prior_gate": prior["status"],
            "source_amendment_template": template["status"],
            "connection_request": connection_request["status"],
            "minimal_root_cutset": cutset["status"],
            "source_owned_certificate": source_cert["status"],
            "u1y_connection_witness_contract": u1y_witness["status"],
            "u1y_selected_source_certificate": u1y_source["status"],
        },
        "route_evaluation": route_evaluation,
        "decision": decision,
        "theorem": {
            "name": "BN27SourceObjectDeclarationInterfaceConservativityTheorem",
            "proved": True,
            "statement": (
                "A declaration of S_QaSU3^BN27 is conservative only if it emits the full BN27 carrier, C_tau and PhiFin_DE "
                "operators, kernel/shared-circle policy, trace policy/index scale, finitepart log(92160000) identity, "
                "not-Route-C-import provenance, and theorem-derived selected source flags. A bare source name does not close "
                "the proof. The equivalent constructive route is selected connection values exporting the same fields to the "
                "BN27 validators. Current artifacts provide support and common U1/Y contract shape, but not the selected values."
            ),
        },
        "guardrails": {
            "does_not_promote_log92160000": True,
            "does_not_close_by_bare_source_name": True,
            "does_not_treat_DE_gap_trace_as_full_source_identity": True,
            "does_not_import_routec_as_source_identity": True,
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
        "declaration_interface_path": rel(OUTPUT_INTERFACE),
        "note_path": rel(OUTPUT_NOTE),
        "source_object_declaration_interface_built": True,
        "bare_source_name_rejected_as_closure": True,
        "direct_source_object_declaration_closed": False,
        "equivalent_connection_value_export_closed": False,
        "BN27_source_identity_closed": False,
        "oriented_logdet_promoted": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin BN27 SourceObject SQaSU3BN27 Declaration or ConnectionValueExport v1

## Result

```text
status = {STATUS}
source_object_declaration_interface_built = true
bare_source_name_rejected_as_closure = true
direct_source_object_declaration_closed = false
equivalent_connection_value_export_closed = false
oriented_logdet_promoted = false
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

## Declaration Interface

```text
{rel(OUTPUT_INTERFACE)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_INTERFACE)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
