"""Build BN27 source-owned logdet minimal-emission packet fill/source-amendment gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "prior_gate": DATA / "selected_heterotic_orientedphifin_bn27_sourceownedlogdet_sourcetheorem_or_kerneltraceownership.candidate.json",
    "minimal_emission_packet": DATA / "selected_heterotic_orientedphifin_bn27_sourceownedlogdet_minimal_emission_packet.json",
    "source_owned_certificate": DATA / "selected_heterotic_orientedphifin_bn27_source_owned_certificate.refined.json",
    "direct_source_declaration_fill": DATA / "selected_heterotic_orientedphifin_directbn27_sourcedeclaration_fill_or_bundleA_selector.candidate.json",
    "selected_connection_witness_export": DATA / "selected_heterotic_orientedphifin_selectedconnectionwitness_export_fill.candidate.json",
    "sourceidentity_direct_or_external": DATA / "selected_heterotic_orientedphifin_bn27_sourceidentity_directsourcetheorem_or_connectionvalues_externalconstruction.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_bn27_sourceownedlogdet_minimalemissionpacket_fill_or_sourceamendment.candidate.json"
OUTPUT_TEMPLATE = DATA / "selected_heterotic_orientedphifin_bn27_sourceownedlogdet_source_amendment_template.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_bn27_sourceownedlogdet_minimalemissionpacket_fill_or_sourceamendment_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_BN27_SourceOwnedLogdet_MinimalEmissionPacket_Fill_or_SourceAmendment_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_BN27_SOURCEOWNED_LOGDET_FILL_ATTEMPT_SOURCE_AMENDMENT_REQUIRED"
NEXT = "Selected_Heterotic_OrientedPhiFin_BN27_SourceObject_SQaSU3BN27_Declaration_or_ConnectionValueExport_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def missing_keys(fields: dict[str, bool]) -> list[str]:
    return [key for key, value in fields.items() if value is not True]


def main() -> dict[str, Any]:
    prior = load(INPUTS["prior_gate"])
    packet = load(INPUTS["minimal_emission_packet"])
    source_cert = load(INPUTS["source_owned_certificate"])
    declaration = load(INPUTS["direct_source_declaration_fill"])
    witness = load(INPUTS["selected_connection_witness_export"])
    sourceidentity = load(INPUTS["sourceidentity_direct_or_external"])

    direct_fields = packet["legal_closing_forms"]["direct_source_theorem"]["current_fields"]
    kernel_trace_fields = packet["legal_closing_forms"]["kernel_trace_ownership_export"]["current_fields"]
    connection_fields = packet["legal_closing_forms"]["connection_or_smooth_quotient_source"]["current_fields"]

    implication_theorem = {
        "schema": "SelectedHeterotic.OrientedPhiFin.BN27.SourceOwnedLogdet.ImplicationDAG.v1",
        "proved_conditionally": True,
        "minimal_roots": [
            "source_object_named_S_QaSU3_BN27 or equivalent selected connection export",
            "theorem-derived selected source flags for the full BN27 packet",
            "kernel/shared-circle and trace-policy ownership from that same source",
        ],
        "then_closes": [
            "full F3xF3 rank-slot carrier emission",
            "C_tau and PhiFin_DE co-emission",
            "finitepart log(92160000) identity source-owned",
            "BN27 source identity",
            "oriented logdet promotion",
        ],
        "reason": "The arithmetic is already exact; only provenance and source-owned policies remain.",
    }

    template = {
        "schema": "SelectedHeterotic.OrientedPhiFin.BN27.SourceOwnedLogdet.SourceAmendmentTemplate.v1",
        "status": "SOURCE_AMENDMENT_TEMPLATE_REQUIRED",
        "smallest_direct_source_amendment": {
            "source_object_named_S_QaSU3_BN27": None,
            "full_F3xF3_rank_slot_carrier_emitted_before_finite_comparison": None,
            "C_tau_and_PhiFin_DE_coemitted_by_source": None,
            "kernel_shared_circle_policy_source_owned": None,
            "trace_policy_source_owned": None,
            "finitepart_log92160000_identity_source_owned": None,
            "theorem_derived_selected_source_flags": None,
            "RouteC_q79_row_internal_to_source_not_imported": None,
        },
        "equivalent_connection_export": {
            "selected_connection_or_smooth_quotient_source": None,
            "BN27_deck_action_export_source_owned": None,
            "operators_export_source_owned": None,
            "kernel_policy_export_source_owned": None,
            "trace_policy_export_source_owned": None,
            "source_identity_export_source_owned": None,
        },
        "known_values_to_consume": packet["known_exact_arithmetic"],
        "conditional_implication_theorem": implication_theorem,
        "must_not_use": packet["must_not_use"],
        "target_fitting_used": False,
    }
    OUTPUT_TEMPLATE.write_text(json.dumps(template, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    lane_evaluation = {
        "direct_source_theorem_fill": {
            "closed_now": False,
            "missing": missing_keys(direct_fields),
            "first_missing": "source_object_named_S_QaSU3_BN27",
            "support_inserted": {
                "branch_certificate_closed": source_cert["source_certificate"]["heterotic_QaSU3_branch_certificate_closed"],
                "direct_declaration_values_filled_as_support": declaration["decision"]["support_values_filled"],
                "exact_logdet_arithmetic_ready": packet["known_exact_arithmetic"]["oriented_abs_sector_product"] == 92160000,
            },
        },
        "kernel_trace_ownership_fill": {
            "closed_now": False,
            "missing": missing_keys(kernel_trace_fields),
            "first_missing": "kernel_policy_export_source_owned",
            "support_inserted": {
                "kernel_policy_support_present": witness["export_fields"]["kernel_policy"]["support_present"],
                "trace_policy_support_present": witness["export_fields"]["trace_policy"]["support_present"],
                "audit_replay_export_filled": witness["export_fields"]["audit_replay"]["filled_for_export"],
            },
        },
        "connection_or_smooth_source_fill": {
            "closed_now": False,
            "missing": missing_keys(connection_fields),
            "first_missing": "selected connection values or direct source theorem",
            "support_inserted": {
                "external_construction_request_built": sourceidentity["decision"]["external_construction_request_built"],
                "root_cutset_built": sourceidentity["decision"]["root_cutset_built"],
            },
        },
    }

    decision = {
        "attempt_executed": True,
        "source_amendment_template_built": True,
        "conditional_implication_theorem_closed": True,
        "direct_source_theorem_closed": False,
        "kernel_trace_ownership_closed": False,
        "connection_or_smooth_source_closed": False,
        "source_owned_logdet_closed": False,
        "BN27_source_identity_closed": False,
        "oriented_logdet_promoted": False,
        "source_amendment_template_path": rel(OUTPUT_TEMPLATE),
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinBN27SourceOwnedLogdetMinimalEmissionPacketFillOrSourceAmendment",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "prior_gate": prior["status"],
            "minimal_emission_packet": packet["status"],
            "sourceidentity_direct_or_external": sourceidentity["status"],
            "selected_connection_witness_export": witness["status"],
            "source_owned_certificate": source_cert["status"],
            "direct_source_declaration_fill": declaration["status"],
        },
        "lane_evaluation": lane_evaluation,
        "conditional_implication_theorem": implication_theorem,
        "decision": decision,
        "theorem": {
            "name": "BN27SourceOwnedLogdetFillAttemptSourceAmendmentRequiredTheorem",
            "proved": True,
            "statement": (
                "The minimal emission packet can be filled only conditionally from the current repo. The exact logdet "
                "arithmetic, branch certificate, direct declaration support values, kernel/trace support, and external "
                "construction request are all present, but none is a source-owned BN27 emission. The useful closed result "
                "is the implication DAG: once S_QaSU3^BN27 or an equivalent selected connection export owns the carrier, "
                "operators, kernel, trace policy, and theorem-derived flags, log(92160000) promotes without further "
                "numerical choices. Until that source amendment is supplied, closure remains open."
            ),
        },
        "guardrails": {
            "does_not_promote_log92160000": True,
            "does_not_treat_support_values_as_source_amendment": True,
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
        "source_amendment_template_path": rel(OUTPUT_TEMPLATE),
        "note_path": rel(OUTPUT_NOTE),
        "conditional_implication_theorem_closed": True,
        "source_owned_logdet_closed": False,
        "BN27_source_identity_closed": False,
        "oriented_logdet_promoted": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin BN27 SourceOwnedLogdet MinimalEmissionPacket Fill or SourceAmendment v1

## Result

```text
status = {STATUS}
conditional_implication_theorem_closed = true
direct_source_theorem_closed = false
kernel_trace_ownership_closed = false
source_owned_logdet_closed = false
oriented_logdet_promoted = false
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

## Source Amendment Template

```text
{rel(OUTPUT_TEMPLATE)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_TEMPLATE)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
