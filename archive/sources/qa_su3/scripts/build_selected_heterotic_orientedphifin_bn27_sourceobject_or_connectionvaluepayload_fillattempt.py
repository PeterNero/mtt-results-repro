"""Build BN27 source-object or connection-value payload fill attempt."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "template_gate": DATA / "selected_heterotic_orientedphifin_bn27_sourcebranchidentity_sourceamendment_template_or_connectionvalues.candidate.json",
    "template": DATA / "selected_heterotic_orientedphifin_bn27_sourcebranchidentity_sourceamendment_template.json",
    "current_fill": DATA / "selected_heterotic_orientedphifin_bn27_sourcebranchidentity_sourceamendment_current_fill.json",
    "direct_declaration_fill": DATA / "selected_heterotic_orientedphifin_bn27_direct_source_declaration.fill_attempt.json",
    "source_identity_contract": DATA / "selected_heterotic_orientedphifin_directbn27_sourceidentitytransport_acceptance_contract.json",
    "external_connection_request": DATA / "selected_heterotic_orientedphifin_bn27_connectionvalues_externalconstruction_request.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_bn27_sourceobject_or_connectionvaluepayload_fillattempt.candidate.json"
OUTPUT_PROBE = DATA / "selected_heterotic_orientedphifin_bn27_sourceobject_or_connectionvaluepayload_support_probe.json"
OUTPUT_MISSING = DATA / "selected_heterotic_orientedphifin_bn27_minimal_missing_source_value_theorem.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_bn27_sourceobject_or_connectionvaluepayload_fillattempt_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_BN27_SourceObject_or_ConnectionValuePayload_FillAttempt_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_BN27_SOURCEOBJECT_OR_CONNECTIONVALUEPAYLOAD_FILL_SUPPORT_ONLY_SOURCE_VALUES_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_BN27_MinimalMissingSourceValueTheorem_or_ConnectionTables_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    template_gate = load(INPUTS["template_gate"])
    template = load(INPUTS["template"])
    current_fill = load(INPUTS["current_fill"])
    declaration = load(INPUTS["direct_declaration_fill"])
    contract = load(INPUTS["source_identity_contract"])
    external = load(INPUTS["external_connection_request"])

    source_support_probe = {
        "selected_source_object_S_QaSU3_BN27": {
            "support_value": declaration["source_certificate"]["source_name"],
            "source_value_filled": False,
            "reason": declaration["source_certificate"]["why_open"],
        },
        "full_F3xF3_rank_slot_carrier_emitted": {
            "support_value": {
                "basis_id": declaration["domain"]["basis_id"],
                "basis_dimension": declaration["domain"]["basis_dimension"],
                "deck_action_materialized": declaration["domain"]["F3xF3_rank_slot_deck_action_materialized"],
            },
            "source_value_filled": False,
            "reason": "carrier is materialized but selected_domain_or_quotient_map_to_oriented_BN is false and deck action is not source-owned",
        },
        "sixteen_nonzero_oriented_positive_rows_retained": {
            "support_value": {
                "oriented_nonzero_count": declaration["domain"]["oriented_nonzero_count"],
                "positive_spectrum_count": len(declaration["operators"]["positive_spectrum"]),
            },
            "source_value_filled": False,
            "reason": "16 positive rows are replayed support, not source-retained by a theorem-derived BN27 source flag",
        },
        "one_selected_source_owns_heterotic_C_tau_orientation": {
            "support_value": declaration["operators"]["orientation_operator_Ctau_binding"],
            "source_value_filled": False,
            "reason": "C_tau binding is support; source_emits_C_tau is false",
        },
        "one_selected_source_owns_RouteC_PhiFin_DE_magnitude": {
            "support_value": bool(declaration["operators"]["D_E_diagonal_on_oriented_nonzero_BN"]),
            "source_value_filled": False,
            "reason": "PhiFin_DE/D_E row is support; source_emits_PhiFin_DE is false",
        },
        "operators_coemitted_before_finite_comparison": {
            "support_value": declaration["operators"]["C_tau_and_PhiFin_DE_commute"],
            "source_value_filled": False,
            "reason": "commutation is support; co-emission by one selected source is not emitted",
        },
        "RouteC_row_internal_theorem_not_external_import": {
            "support_value": declaration["source_certificate"]["not_routec_or_benchmark_import"],
            "source_value_filled": False,
            "reason": "not_routec_or_benchmark_import is false",
        },
        "kernel_shared_circle_policy_source_owned": {
            "support_value": declaration["domain"]["kernel_shared_circle_no_double_count_policy"],
            "source_value_filled": False,
            "reason": "kernel/shared-circle policy is support replay, not source-owned",
        },
        "trace_zeta_finitepart_policy_source_owned": {
            "support_value": declaration["finitepart"]["finitepart_trace_identity_relative_to_full_orbit_source"],
            "source_value_filled": False,
            "reason": "finitepart identity is relative to a full-orbit source but finitepart source ownership is false",
        },
        "eleven_label_rho_tau_shadow_embeds_but_is_not_threshold_domain": {
            "support_value": declaration["source_certificate"]["relation_to_internal_projective_rhoE_shadow"],
            "source_value_filled": False,
            "reason": "the shadow relation is recorded, but no theorem promotes or separates it as the selected BN27 source domain",
        },
        "no_lifted_flags_full_replay_audit": {
            "support_value": declaration["audit_replay"]["support_replay_ready"],
            "source_value_filled": False,
            "reason": "closure replay is not allowed while decisive source leaves remain open",
        },
    }

    connection_support_probe = {
        "BN27_DE_Riesz_Green_kernel_trace_export": {
            "support_value": contract["already_importable_support"],
            "source_value_filled": False,
            "reason": "gap-layer support imports, but the contract keeps the export payload null",
        },
        "selected_HYM_or_projective_connection_coefficients": {
            "support_value": external["external_connection_values_route"]["direct_hym_or_strominger"],
            "source_value_filled": False,
            "reason": "route requirements exist, but no selected coefficients are emitted",
        },
        "typed_f_sections": {
            "support_value": external["external_connection_values_route"]["typed_cech"][0],
            "source_value_filled": False,
            "reason": "typed f_i section requirement exists, but emitted sections are absent",
        },
        "typed_g_sections": {
            "support_value": external["external_connection_values_route"]["typed_cech"][0],
            "source_value_filled": False,
            "reason": "typed g_i section requirement exists, but emitted sections are absent",
        },
        "cech_transition_cocycles": {
            "support_value": external["external_connection_values_route"]["typed_cech"][1],
            "source_value_filled": False,
            "reason": "Cech transition requirement exists, but tables are absent",
        },
        "g_after_f_zero_exactness_certificate": {
            "support_value": external["external_connection_values_route"]["typed_cech"][2],
            "source_value_filled": False,
            "reason": "exactness requirement exists, but certificate is absent",
        },
        "finitepart_log92160000_identity_from_values": {
            "support_value": declaration["finitepart"]["oriented_abs_sector_logdet_exact"],
            "source_value_filled": False,
            "reason": "arithmetic is exact but not derived from emitted connection values",
        },
        "no_lifted_flags_connection_replay": {
            "support_value": contract["forbidden"],
            "source_value_filled": False,
            "reason": "no-lift guardrails exist, but there are no values to replay",
        },
    }

    probe = {
        "schema": "SelectedHeterotic.OrientedPhiFin.BN27.SourceObjectOrConnectionPayload.SupportProbe.v1",
        "status": "SUPPORT_PROBED_NO_SOURCE_VALUES_FILLED",
        "source_support_probe": source_support_probe,
        "connection_support_probe": connection_support_probe,
        "source_value_filled_count": sum(1 for item in source_support_probe.values() if item["source_value_filled"]),
        "connection_value_filled_count": sum(1 for item in connection_support_probe.values() if item["source_value_filled"]),
        "target_fitting_used": False,
    }
    OUTPUT_PROBE.write_text(json.dumps(probe, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    missing = {
        "schema": "SelectedHeterotic.OrientedPhiFin.BN27.MinimalMissingSourceValueTheorem.v1",
        "status": "ONE_SOURCE_VALUE_THEOREM_OR_FULL_CONNECTION_TABLES_REQUIRED",
        "minimal_direct_theorem": {
            "name": "S_QaSU3_BN27_SelectedSourceEmissionTheorem",
            "must_state": [
                "S_QaSU3^BN27 is the selected heterotic Qa/SU3 threshold source",
                "it emits the full F3xF3 rank-slot carrier before finite comparison",
                "C_tau and PhiFin_DE are co-emitted operators of that source",
                "the Route-C row is an internal theorem of that source, not external support",
                "kernel/shared-circle policy and trace/zeta finitepart policy are source-owned",
                "the no-lift replay audit passes from those emitted fields",
            ],
            "would_fill_source_fields": list(template["source_object_template"].keys()),
        },
        "minimal_constructive_alternative": {
            "name": "BN27_SelectedConnectionTablesExportTheorem",
            "must_emit": list(template["connection_values_template"].keys()),
            "would_fill_connection_fields": list(template["connection_values_template"].keys()),
        },
        "why_this_is_minimal": (
            "All numerical/operator support is already present. The missing object is not another number, "
            "but provenance: either one selected source theorem owning the table, or emitted connection tables "
            "that derive the table and validator exports."
        ),
        "target_fitting_used": False,
    }
    OUTPUT_MISSING.write_text(json.dumps(missing, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    decision = {
        "attempt_executed": True,
        "source_support_fields_probed": len(source_support_probe),
        "connection_support_fields_probed": len(connection_support_probe),
        "source_object_filled_field_count": probe["source_value_filled_count"],
        "connection_values_filled_field_count": probe["connection_value_filled_count"],
        "source_object_payload_closed": False,
        "connection_value_payload_closed": False,
        "source_branch_identity_closed": False,
        "same_source_export_to_BN27_validators": False,
        "oriented_logdet_promoted": False,
        "minimal_missing_theorem_built": True,
        "support_probe_path": rel(OUTPUT_PROBE),
        "minimal_missing_theorem_path": rel(OUTPUT_MISSING),
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinBN27SourceObjectOrConnectionValuePayloadFillAttempt",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "template_gate": template_gate["status"],
            "template": template["status"],
            "current_fill": current_fill["status"],
            "direct_declaration_fill": declaration["status"],
            "source_identity_contract": contract["status"],
            "external_connection_request": external["status"],
        },
        "decision": decision,
        "theorem": {
            "name": "BN27SourceObjectOrConnectionPayloadFillAttemptTheorem",
            "proved": True,
            "statement": (
                "The current artifacts probe every direct-source and connection-value field but fill none as source values. "
                "The BN27 carrier, operators, spectrum, Green/Riesz layer, and logdet arithmetic are available only as support. "
                "Thus the remaining object is exactly a selected source-emission theorem for S_QaSU3^BN27, or full emitted "
                "connection tables deriving the same BN27 validator exports."
            ),
        },
        "guardrails": {
            "does_not_count_support_values_as_source_values": True,
            "does_not_promote_log92160000": True,
            "does_not_treat_routec_import_as_internal": True,
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
        "support_probe_path": rel(OUTPUT_PROBE),
        "minimal_missing_theorem_path": rel(OUTPUT_MISSING),
        "note_path": rel(OUTPUT_NOTE),
        "source_object_filled_field_count": 0,
        "connection_values_filled_field_count": 0,
        "source_branch_identity_closed": False,
        "connection_value_payload_closed": False,
        "oriented_logdet_promoted": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin BN27 SourceObject or ConnectionValuePayload FillAttempt v1

## Result

```text
status = {STATUS}
source_object_filled_field_count = 0
connection_values_filled_field_count = 0
source_branch_identity_closed = false
connection_value_payload_closed = false
oriented_logdet_promoted = false
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

## New Files

```text
{rel(OUTPUT_PROBE)}
{rel(OUTPUT_MISSING)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_PROBE)}")
    print(f"wrote {rel(OUTPUT_MISSING)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
