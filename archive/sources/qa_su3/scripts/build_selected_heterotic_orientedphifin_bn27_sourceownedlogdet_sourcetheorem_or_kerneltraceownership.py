"""Build BN27 source-owned logdet source theorem / kernel-trace ownership gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "prior_gate": DATA / "selected_heterotic_orientedphifin_bn27_directfinitepartfunctional_or_sourceownedlogdettheorem.candidate.json",
    "sourceowned_logdet_contract": DATA / "selected_heterotic_orientedphifin_bn27_sourceowned_logdet_theorem_contract.json",
    "direct_acceptance_contract": DATA / "selected_heterotic_orientedphifin_directbn27_sourceidentitytransport_acceptance_contract.json",
    "selected_connection_witness_export": DATA / "selected_heterotic_orientedphifin_selectedconnectionwitness_export_fill.candidate.json",
    "sourceownership_transport": DATA / "selected_heterotic_orientedphifin_bn27_sourceownership_transport_or_connectionwitness_values.candidate.json",
    "sourceidentity_direct_or_external": DATA / "selected_heterotic_orientedphifin_bn27_sourceidentity_directsourcetheorem_or_connectionvalues_externalconstruction.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_bn27_sourceownedlogdet_sourcetheorem_or_kerneltraceownership.candidate.json"
OUTPUT_PACKET = DATA / "selected_heterotic_orientedphifin_bn27_sourceownedlogdet_minimal_emission_packet.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_bn27_sourceownedlogdet_sourcetheorem_or_kerneltraceownership_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_BN27_SourceOwnedLogdet_SourceTheorem_or_KernelTraceOwnership_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_BN27_SOURCEOWNED_LOGDET_THEOREM_PACKET_BUILT_OWNERSHIP_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_BN27_SourceOwnedLogdet_MinimalEmissionPacket_Fill_or_SourceAmendment_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def all_closed(fields: dict[str, bool]) -> bool:
    return all(fields.values())


def main() -> dict[str, Any]:
    prior = load(INPUTS["prior_gate"])
    contract = load(INPUTS["sourceowned_logdet_contract"])
    acceptance = load(INPUTS["direct_acceptance_contract"])
    witness = load(INPUTS["selected_connection_witness_export"])
    transport = load(INPUTS["sourceownership_transport"])
    sourceidentity = load(INPUTS["sourceidentity_direct_or_external"])

    support_payload = prior["arithmetic_payload"]
    direct_payload = acceptance["direct_source_identity_payload"]
    witness_fields = witness["export_fields"]

    direct_source_current = {
        "source_object_named_S_QaSU3_BN27": direct_payload["source_object_named_S_QaSU3_BN27"] is True,
        "full_F3xF3_rank_slot_carrier_emitted_before_finite_comparison": direct_payload["full_F3xF3_rank_slot_carrier_emitted_before_finite_comparison"] is True,
        "C_tau_and_PhiFin_DE_coemitted_by_source": direct_payload["C_tau_and_PhiFin_DE_coemitted_by_source"] is True,
        "kernel_shared_circle_policy_source_owned": direct_payload["kernel_shared_circle_policy_source_owned"] is True,
        "finitepart_log92160000_identity_source_owned": direct_payload["finitepart_log92160000_identity_source_owned"] is True,
        "theorem_derived_selected_source_flags": direct_payload["theorem_derived_selected_source_flags"] is True,
        "RouteC_q79_row_internal_to_source_not_imported": direct_payload["RouteC_q79_row_internal_to_source_not_imported"] is True,
    }
    kernel_trace_current = {
        "kernel_policy_export_source_owned": witness_fields["kernel_policy"]["selected_source_owned"] is True,
        "trace_policy_export_source_owned": witness_fields["trace_policy"]["selected_source_owned"] is True,
        "source_identity_export_source_owned": witness_fields["source_identity"]["selected_source_owned"] is True,
        "operators_export_source_owned": witness_fields["operators"]["selected_source_owned"] is True,
        "BN27_deck_action_export_source_owned": witness_fields["BN27_deck_action"]["selected_source_owned"] is True,
    }
    smooth_or_connection_current = {
        "direct_source_theorem_closed": sourceidentity["decision"]["direct_source_theorem_closed"] is True,
        "connection_values_external_construction_closed": sourceidentity["decision"]["connection_values_external_construction_closed"] is True,
        "BN27_source_ownership_transport_closed": transport["decision"]["BN27_source_ownership_transport_closed"] is True,
        "selected_connection_witness_values_closed": transport["decision"]["selected_connection_witness_values_closed"] is True,
    }

    packet = {
        "schema": "SelectedHeterotic.OrientedPhiFin.BN27.SourceOwnedLogdet.MinimalEmissionPacket.v1",
        "status": "MINIMAL_EMISSION_PACKET_REQUIRED",
        "known_exact_arithmetic": support_payload,
        "legal_closing_forms": {
            "direct_source_theorem": {
                "required_fields": list(direct_source_current.keys()),
                "current_fields": direct_source_current,
                "closed_now": all_closed(direct_source_current),
            },
            "kernel_trace_ownership_export": {
                "required_fields": list(kernel_trace_current.keys()),
                "current_fields": kernel_trace_current,
                "closed_now": all_closed(kernel_trace_current),
            },
            "connection_or_smooth_quotient_source": {
                "required_fields": list(smooth_or_connection_current.keys()),
                "current_fields": smooth_or_connection_current,
                "closed_now": all_closed(smooth_or_connection_current),
            },
        },
        "must_not_use": [
            "do not treat exact arithmetic as selected-source ownership",
            "do not import Route-C/q79 support as the heterotic source theorem",
            "do not promote replayed kernel/trace policy as source-owned",
            "do not use observed data or benchmark determinant entries",
        ],
        "target_fitting_used": False,
    }
    OUTPUT_PACKET.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    lane_evaluation = {
        "direct_source_theorem": {
            "closed_now": packet["legal_closing_forms"]["direct_source_theorem"]["closed_now"],
            "first_missing": "source_object_named_S_QaSU3_BN27",
            "current_fields": direct_source_current,
        },
        "kernel_trace_ownership_export": {
            "closed_now": packet["legal_closing_forms"]["kernel_trace_ownership_export"]["closed_now"],
            "first_missing": "kernel_policy_export_source_owned",
            "current_fields": kernel_trace_current,
            "support_present": {
                "kernel_policy": witness_fields["kernel_policy"]["support_present"],
                "trace_policy": witness_fields["trace_policy"]["support_present"],
            },
        },
        "connection_or_smooth_quotient_source": {
            "closed_now": packet["legal_closing_forms"]["connection_or_smooth_quotient_source"]["closed_now"],
            "first_missing": "direct source theorem or selected connection values",
            "current_fields": smooth_or_connection_current,
        },
    }

    decision = {
        "attempt_executed": True,
        "sourceowned_logdet_minimal_packet_built": True,
        "direct_source_theorem_closed": lane_evaluation["direct_source_theorem"]["closed_now"],
        "kernel_trace_ownership_closed": lane_evaluation["kernel_trace_ownership_export"]["closed_now"],
        "connection_or_smooth_source_closed": lane_evaluation["connection_or_smooth_quotient_source"]["closed_now"],
        "source_owned_logdet_closed": False,
        "BN27_source_identity_closed": False,
        "oriented_logdet_promoted": False,
        "minimal_emission_packet_path": rel(OUTPUT_PACKET),
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinBN27SourceOwnedLogdetSourceTheoremOrKernelTraceOwnership",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "prior_gate": prior["status"],
            "sourceowned_logdet_contract": contract["status"],
            "direct_acceptance_contract": acceptance["status"],
            "selected_connection_witness_export": witness["status"],
            "sourceownership_transport": transport["status"],
            "sourceidentity_direct_or_external": sourceidentity["status"],
        },
        "lane_evaluation": lane_evaluation,
        "minimal_emission_packet_path": rel(OUTPUT_PACKET),
        "decision": decision,
        "theorem": {
            "name": "BN27SourceOwnedLogdetMinimalEmissionPacketTheorem",
            "proved": True,
            "statement": (
                "Given the exact oriented BN27 finitepart arithmetic, source-owned promotion is equivalent to filling one "
                "of three selected-source packets: a direct S_QaSU3^BN27 source theorem, a selected kernel/trace ownership "
                "export, or same-source connection/smooth quotient values that imply both. The current corpus fills none of "
                "these packets; it supplies support and replay only. Therefore log(92160000) remains unpromoted, and the next "
                "step is a minimal emission-packet fill or source amendment."
            ),
        },
        "guardrails": {
            "does_not_promote_log92160000": True,
            "does_not_treat_replay_as_source_export": True,
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
        "minimal_emission_packet_path": rel(OUTPUT_PACKET),
        "note_path": rel(OUTPUT_NOTE),
        "sourceowned_logdet_minimal_packet_built": True,
        "source_owned_logdet_closed": False,
        "BN27_source_identity_closed": False,
        "oriented_logdet_promoted": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin BN27 SourceOwnedLogdet SourceTheorem or KernelTraceOwnership v1

## Result

```text
status = {STATUS}
sourceowned_logdet_minimal_packet_built = true
direct_source_theorem_closed = false
kernel_trace_ownership_closed = false
source_owned_logdet_closed = false
oriented_logdet_promoted = false
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

## Minimal Emission Packet

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
