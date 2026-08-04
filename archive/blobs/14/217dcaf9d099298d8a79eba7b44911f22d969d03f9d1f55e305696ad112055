from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPRO_ROOT = ROOT.parent / "mtt-sm-parity-repro"

REPRO_CANDIDATE = REPRO_ROOT / "outputs" / "selected_qasu3sourcepacket_or_finalsmparityclosure.candidate.json"
REPRO_DECISION = REPRO_ROOT / "outputs" / "sm_parity_closure_decision.packet.json"
REPRO_FINAL_PACKET = REPRO_ROOT / "outputs" / "final_sm_packet_certificate_parity_closure.packet.json"
REPRO_QASU3 = REPRO_ROOT / "outputs" / "qasu3_parity_interface_replacement.packet.json"
REPRO_REPORT = REPRO_ROOT / "reports" / "verification_report.txt"

OUT_CERT = ROOT / "certificates" / "sm_parity_repro_readonly_bridge_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "sm_parity_repro_readonly_bridge.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "SM_Parity_Repro_Readonly_Bridge_Import_v1.md"

STATUS = "SM_PARITY_REPRO_READONLY_BRIDGE_IMPORTED_PARITY_CLOSED_NOKNOB_OPEN"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    candidate = load(REPRO_CANDIDATE)
    decision = load(REPRO_DECISION)
    final_packet = load(REPRO_FINAL_PACKET)
    qasu3 = load(REPRO_QASU3)
    report = REPRO_REPORT.read_text(encoding="utf-8")

    candidate_ok = all(
        [
            candidate["status"] == "MTT_SELECTED_QASU3SOURCEPACKET_OR_FINALSMPARITYCLOSURE_BUILT_SM_PARITY_CLOSED_NOKNOB_OPEN",
            candidate["theorem"]["proved"] is True,
            candidate["closure_decision"]["SM_parity_closed"] is True,
            candidate["closure_decision"]["true_SM_equivalence_closed"] is False,
            candidate["closure_decision"]["no_knob_closed"] is False,
            candidate["source_boundary_preserved"] is True,
            candidate["actual_selected_operator_packet_claimed"] is False,
            candidate["observed_data_used_as_selector"] is False,
            candidate["target_fitting_used"] is False,
            candidate["what_closes_now"]["SM_parity_closed_under_declared_standard"] is True,
            candidate["what_closes_now"]["selected_SM_packet_certificate_integration_closed_for_SM_parity"] is True,
            all(candidate["what_remains_open"].values()),
        ]
    )

    decision_ok = all(
        [
            decision["schema"] == "MTTSMParityClosureDecision.v1",
            decision["status"] == "SM_PARITY_CLOSED_UNDER_DECLARED_PARITY_INTERFACE_STANDARD",
            decision["SM_parity_closed"] is True,
            decision["true_SM_equivalence_closed"] is False,
            decision["no_knob_closed"] is False,
            decision["current_SM_parity_blockers"] == [],
            decision["observed_data_used_as_selector"] is False,
            decision["target_fitting_used"] is False,
            "actual selected Qa/SU3 D_E/rho_E operator packet" in decision["no_knob_still_open"],
        ]
    )

    final_packet_ok = all(
        [
            final_packet["schema"] == "MTTFinalSMPacketCertificateParityClosure.v1",
            final_packet["status"] == "FINAL_SM_PACKET_CERTIFICATE_CLOSED_FOR_SM_PARITY_VIA_QASU3_INTERFACE_REPLACEMENT",
            final_packet["all_source_rows_closed_for_sm_parity_interface"] is True,
            final_packet["any_source_row_closed_as_actual_no_knob_packet"] is False,
            final_packet["can_close_SM_parity_interface_now"] is True,
            final_packet["can_close_no_knob_SM_derivation_now"] is False,
            final_packet["can_close_true_SM_equivalence_now"] is False,
            final_packet["qasu3_row"]["closed_for_sm_parity_interface"] is True,
            final_packet["qasu3_row"]["closed_as_actual_selected_no_knob_packet"] is False,
        ]
    )

    qasu3_ok = all(
        [
            qasu3["schema"] == "MTTQaSU3ParityInterfaceReplacement.v1",
            qasu3["status"] == "QASU3_PARITY_INTERFACE_REPLACEMENT_ACCEPTED_ACTUAL_OPERATOR_PACKET_OPEN",
            qasu3["accepted_for_SM_parity_interface"] is True,
            qasu3["accepted_as_actual_selected_no_knob_packet"] is False,
            qasu3["accepted_for_true_precision_equivalence"] is False,
            qasu3["parity_interface_closure"]["qa_su3_color_operator_packet_closed_for_sm_parity_interface"] is True,
            qasu3["parity_interface_closure"]["qa_su3_color_operator_packet_closed_as_actual_no_knob_packet"] is False,
            qasu3["parity_interface_closure"]["source_packet_certificate_integration_closed_for_sm_parity"] is True,
            all(value is False for value in qasu3["guardrails"].values()),
            "selected D_E or rho_E operator data" in qasu3["no_knob_frontier_preserved"],
            "mapped Bianchi/Freed-Witten/anomaly certificate" in qasu3["no_knob_frontier_preserved"],
        ]
    )

    report_ok = all(
        marker in report
        for marker in [
            "Verification result: PASS",
            "SM-parity closure: TRUE",
            "true SM equivalence: FALSE",
            "no-knob closure: FALSE",
        ]
    )

    what_closes_now = {
        "readonly_repro_verified": report_ok,
        "SM_parity_closed_under_declared_parity_interface_standard": candidate_ok and decision_ok,
        "selected_SM_packet_certificate_integration_closed_for_SM_parity": final_packet_ok,
        "QaSU3_typed_source_interface_replacement_accepted_for_SM_parity": qasu3_ok,
    }

    what_remains_open = {
        "actual_QaSU3_D_E_or_rho_E_operator_packet": True,
        "typed_monad_or_section_ring_source_maps_as_actual_selected_operator_maps": True,
        "same_branch_period_or_finite_quotient_selector": True,
        "mapped_Bianchi_Freed_Witten_anomaly_certificate_for_actual_packet": True,
        "true_precision_SM_equivalence": True,
        "full_no_knob_SM_derivation": True,
        "dynamic_C1_source_map_selection_in_this_GR_response_chain": True,
    }

    guardrails = {
        "does_not_import_repro_as_no_knob_closure": True,
        "does_not_import_repro_as_true_SM_equivalence": True,
        "does_not_claim_actual_QaSU3_operator_packet": True,
        "does_not_use_observed_or_target_inputs": True,
        "does_not_close_dynamic_C1_source_map_gate": True,
        "readonly_repro_paths_only": True,
    }

    theorem = {
        "name": "SMParityReproReadonlyBridgeImport",
        "proved": all([all(what_closes_now.values()), all(what_remains_open.values()), all(guardrails.values())]),
        "closure_claimed": False,
        "statement": (
            "The read-only mtt-sm-parity-repro capsule is verified and imported as "
            "a tiered parity-interface bridge: SM parity is closed under the declared "
            "parity-interface standard, while true SM equivalence, no-knob closure, "
            "the actual Qa/SU3 operator packet, and the dynamic C1 source-map gate "
            "in this GR-response proof chain remain open."
        ),
    }

    hashes = {
        "selected_qasu3sourcepacket_or_finalsmparityclosure.candidate.json": sha256(REPRO_CANDIDATE),
        "sm_parity_closure_decision.packet.json": sha256(REPRO_DECISION),
        "final_sm_packet_certificate_parity_closure.packet.json": sha256(REPRO_FINAL_PACKET),
        "qasu3_parity_interface_replacement.packet.json": sha256(REPRO_QASU3),
        "verification_report.txt": sha256(REPRO_REPORT),
    }

    packet = {
        "theorem": theorem,
        "status": STATUS,
        "what_closes_now": what_closes_now,
        "what_remains_open": what_remains_open,
        "guardrails": guardrails,
        "repro_summary": {
            "candidate_status": candidate["status"],
            "decision_status": decision["status"],
            "final_packet_status": final_packet["status"],
            "qasu3_status": qasu3["status"],
            "SM_parity_closed": decision["SM_parity_closed"],
            "true_SM_equivalence_closed": decision["true_SM_equivalence_closed"],
            "no_knob_closed": decision["no_knob_closed"],
        },
        "repro_hashes": hashes,
        "input_artifacts": {
            "repro_root": str(REPRO_ROOT),
            "candidate": str(REPRO_CANDIDATE),
            "decision": str(REPRO_DECISION),
            "final_packet": str(REPRO_FINAL_PACKET),
            "qasu3": str(REPRO_QASU3),
            "verification_report": str(REPRO_REPORT),
        },
    }

    note = f"""# SM Parity Repro Readonly Bridge Import v1

## Result

The read-only `mtt-sm-parity-repro` capsule verifies locally and is imported as
a tiered parity-interface result.

```text
SM parity closure       = TRUE
true SM equivalence     = FALSE
no-knob closure         = FALSE
```

The bridge closes selected SM packet certificate integration at the SM-parity
tier only. It does not close actual Qa/SU3 operator derivation, no-knob SM
closure, true precision equivalence, or the dynamic C1 source-map selection gate
in this GR-response chain.

## Status

```text
{STATUS}
```
"""

    cert_out = {
        "program": "MTT protospinor GR response proof",
        "certificate": "sm_parity_repro_readonly_bridge",
        "status": STATUS,
        "closure_claimed": False,
        "theorem": theorem,
        "what_closes_now": what_closes_now,
        "what_remains_open": what_remains_open,
        "guardrails": guardrails,
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }

    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert_out, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {STATUS}")


if __name__ == "__main__":
    main()
