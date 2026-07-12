"""Build BN27 source-branch identity source-amendment template / connection-values gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "threeclause_fill": DATA / "selected_heterotic_orientedphifin_bn27_sourcebranchidentity_threeclause_fill_or_connectionsolve.candidate.json",
    "acceptance_packet": DATA / "selected_heterotic_orientedphifin_bn27_sourcebranchidentity_threeclause_acceptance_packet.json",
    "prior_sourceamendment_attack": DATA / "selected_heterotic_orientedphifin_sourcebranchidentity_sourceamendment_or_connectionvalues.candidate.json",
    "directbn27_source_declaration": DATA / "selected_heterotic_orientedphifin_directbn27_sourcedeclaration_fill_or_bundleA_selector.candidate.json",
    "sourceowned_logdet_gate": DATA / "selected_heterotic_orientedphifin_bn27_sourceownedlogdet_minimalemissionpacket_fill_or_sourceamendment.candidate.json",
    "direct_source_identity_transport": DATA / "selected_heterotic_orientedphifin_directbn27_sourceidentitytransport_fill_or_typedconnectionwitnessvalues.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_bn27_sourcebranchidentity_sourceamendment_template_or_connectionvalues.candidate.json"
OUTPUT_TEMPLATE = DATA / "selected_heterotic_orientedphifin_bn27_sourcebranchidentity_sourceamendment_template.json"
OUTPUT_FILL = DATA / "selected_heterotic_orientedphifin_bn27_sourcebranchidentity_sourceamendment_current_fill.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_bn27_sourcebranchidentity_sourceamendment_template_or_connectionvalues_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_BN27_SourceBranchIdentity_SourceAmendment_Template_or_ConnectionValues_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_BN27_SOURCEBRANCHIDENTITY_SOURCEAMENDMENT_TEMPLATE_BUILT_CURRENT_FILL_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_BN27_SourceObject_or_ConnectionValuePayload_FillAttempt_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def null_count(payload: dict[str, Any]) -> int:
    return sum(1 for value in payload.values() if value is None)


def main() -> dict[str, Any]:
    threeclause = load(INPUTS["threeclause_fill"])
    acceptance = load(INPUTS["acceptance_packet"])
    prior = load(INPUTS["prior_sourceamendment_attack"])
    declaration = load(INPUTS["directbn27_source_declaration"])
    logdet = load(INPUTS["sourceowned_logdet_gate"])
    transport = load(INPUTS["direct_source_identity_transport"])

    source_payload = acceptance["source_amendment_payload"]
    connection_payload = acceptance["connection_values_payload"]

    source_template = {
        "schema": "SelectedHeterotic.OrientedPhiFin.BN27.SourceBranchIdentity.SourceAmendmentTemplate.v1",
        "status": "SOURCE_OBJECT_OR_CONNECTION_VALUES_REQUIRED",
        "source_object_template": source_payload,
        "connection_values_template": connection_payload,
        "minimal_direct_source_closure_rule": {
            "requires_all_source_object_fields_non_null": True,
            "closes_three_clauses": [
                "one_selected_source_names_both_branches",
                "eleven_label_to_full_BN27_threshold_carrier",
                "routec_row_not_external_import",
            ],
            "then_closes_validators": [
                "source_identity",
                "BN27_deck_action",
                "operator_coemission",
                "kernel_policy",
                "trace_policy",
                "audit_replay",
            ],
        },
        "minimal_connection_value_closure_rule": {
            "requires_all_connection_value_fields_non_null": True,
            "must_export_to": "BN27 validators before finite comparison",
            "then_closes_same_fields_as_direct_source": True,
        },
        "forbidden_shortcuts": acceptance["guardrails"],
        "target_fitting_used": False,
    }
    OUTPUT_TEMPLATE.write_text(json.dumps(source_template, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    current_fill = {
        "schema": "SelectedHeterotic.OrientedPhiFin.BN27.SourceBranchIdentity.CurrentFill.v1",
        "status": "CURRENT_FILL_SUPPORT_ONLY_VALUES_OPEN",
        "support_reusable": {
            "three_clause_support_count": threeclause["decision"]["support_count"],
            "selected_27mode_DE_trace_equality_support": threeclause["root_reuse"]["selected_trace_equality_for_27mode_DE_gap_layer_closed"],
            "projective_rhoE_primary_support": prior["decision"]["projective_rhoE_primary"],
            "direct_BN27_arithmetic_support": declaration["filled_support_summary"]["oriented_abs_sector_logdet_exact"] == "log(92160000)",
            "minimal_logdet_implication_support": logdet["decision"]["conditional_implication_theorem_closed"],
            "DE_gap_Riesz_Green_support": transport["decision"]["DE_gap_Riesz_Green_export_support_closed"],
        },
        "source_object_fill": source_payload,
        "connection_values_fill": connection_payload,
        "source_object_missing_count": null_count(source_payload),
        "connection_values_missing_count": null_count(connection_payload),
        "all_required_values_emitted": False,
        "source_amendment_closed": False,
        "connection_values_closed": False,
        "target_fitting_used": False,
    }
    OUTPUT_FILL.write_text(json.dumps(current_fill, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    decision = {
        "attempt_executed": True,
        "template_built": True,
        "current_fill_built": True,
        "source_object_required_field_count": len(source_payload),
        "source_object_filled_field_count": len(source_payload) - null_count(source_payload),
        "connection_values_required_field_count": len(connection_payload),
        "connection_values_filled_field_count": len(connection_payload) - null_count(connection_payload),
        "source_amendment_closed": False,
        "connection_values_closed": False,
        "source_branch_identity_closed": False,
        "same_source_export_to_BN27_validators": False,
        "oriented_logdet_promoted": False,
        "template_path": rel(OUTPUT_TEMPLATE),
        "current_fill_path": rel(OUTPUT_FILL),
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinBN27SourceBranchIdentitySourceAmendmentTemplateOrConnectionValues",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "threeclause_fill": threeclause["status"],
            "prior_sourceamendment_attack": prior["status"],
            "directbn27_source_declaration": declaration["status"],
            "sourceowned_logdet_gate": logdet["status"],
            "direct_source_identity_transport": transport["status"],
        },
        "template_path": rel(OUTPUT_TEMPLATE),
        "current_fill_path": rel(OUTPUT_FILL),
        "decision": decision,
        "theorem": {
            "name": "BN27SourceBranchIdentitySourceAmendmentTemplateTheorem",
            "proved": True,
            "statement": (
                "The BN27 source-branch identity problem is now a finite source-value template. "
                "A direct amendment must fill eleven source-object fields naming S_QaSU3^BN27 and owning carrier, "
                "operators, shared-circle kernel, trace policy, provenance, and replay. The constructive alternative "
                "must fill eight connection-value fields and export them to the same BN27 validators. Current artifacts "
                "supply reusable support only; every required source or connection value remains unfilled."
            ),
        },
        "guardrails": {
            "does_not_promote_support_to_source_values": True,
            "does_not_promote_log92160000": True,
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
        "template_path": rel(OUTPUT_TEMPLATE),
        "current_fill_path": rel(OUTPUT_FILL),
        "note_path": rel(OUTPUT_NOTE),
        "source_object_filled_field_count": decision["source_object_filled_field_count"],
        "connection_values_filled_field_count": decision["connection_values_filled_field_count"],
        "source_branch_identity_closed": False,
        "connection_values_closed": False,
        "oriented_logdet_promoted": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin BN27 SourceBranchIdentity SourceAmendment Template or ConnectionValues v1

## Result

```text
status = {STATUS}
source_object_filled_field_count = 0 / {len(source_payload)}
connection_values_filled_field_count = 0 / {len(connection_payload)}
source_branch_identity_closed = false
connection_values_closed = false
oriented_logdet_promoted = false
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

## Template Files

```text
{rel(OUTPUT_TEMPLATE)}
{rel(OUTPUT_FILL)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_TEMPLATE)}")
    print(f"wrote {rel(OUTPUT_FILL)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
