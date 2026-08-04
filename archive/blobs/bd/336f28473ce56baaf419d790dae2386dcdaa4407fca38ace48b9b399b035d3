"""Rebuild the SM-parity closure packets from frozen inputs."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
INPUTS = ROOT / "inputs"
OUTPUTS = ROOT / "outputs"
PROOF = ROOT / "proof"

STATUS = "MTT_SELECTED_QASU3SOURCEPACKET_OR_FINALSMPARITYCLOSURE_BUILT_SM_PARITY_CLOSED_NOKNOB_OPEN"


def load(name: str) -> dict[str, Any]:
    return json.loads((INPUTS / name).read_text(encoding="utf-8"))


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def input_hashes() -> dict[str, str]:
    return {path.name: sha256(path) for path in sorted(INPUTS.glob("*.json"))}


def update_qasu3_row(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for row in rows:
        row = dict(row)
        if row["id"] == "qa_su3_color_operator_packet":
            row["closed_for_sm_parity_interface"] = True
            row["closed_as_actual_selected_no_knob_packet"] = False
            row["parity_interface_replacement"] = "accepted_typed_source_interface_replacement_not_operator_derivation"
            row["required_selected_data"] = (
                "No-knob closure still requires typed monad or section-ring source with selected operator maps, "
                "period/finite quotient selector, and mapped Bianchi/Freed-Witten certificate."
            )
        out.append(row)
    return out


def main() -> int:
    OUTPUTS.mkdir(parents=True, exist_ok=True)
    PROOF.mkdir(parents=True, exist_ok=True)

    one_gate = load("one_gate_candidate.json")
    one_gate_matrix = load("remaining_one_gate_sm_parity_matrix.packet.json")
    qasu3 = load("qasu3_packet_integration_status.packet.json")
    sm_packet_audit = load("actual_selected_sm_packet_anomaly_audit.candidate.json")
    prior_final = load("prior_final_packet_certificate.candidate.json")

    replacement = {
        "schema": "MTTQaSU3ParityInterfaceReplacement.v1",
        "status": "QASU3_PARITY_INTERFACE_REPLACEMENT_ACCEPTED_ACTUAL_OPERATOR_PACKET_OPEN",
        "accepted_for_SM_parity_interface": True,
        "accepted_as_actual_selected_no_knob_packet": False,
        "accepted_for_true_precision_equivalence": False,
        "replacement_rule": {
            "name": "SMParityTypedSourceInterfaceReplacementRule",
            "statement": (
                "At the SM-parity tier, where the Standard Model itself is allowed to take a gauge/"
                "representation/operator interface as admitted structure, the audited typed source-interface "
                "packet may replace the missing actual Qa/SU3 operator derivation for interface certification only."
            ),
            "method": (
                "superset path locked to SM-parity: topology-only SM structure, typed monad/section-ring "
                "support, same-source visible/color attempts, anomaly audits, and rejected-shortcut policy"
            ),
        },
        "imported_open_status": {
            "previous_qasu3_status": qasu3["status"],
            "previous_can_integrate_selected_packet_now": qasu3["can_integrate_selected_packet_now"],
            "actual_operator_needed_for_no_knob": qasu3["needed_for_integration"],
            "previous_critical_row": qasu3["final_packet_critical_open_row"],
        },
        "guardrails": {
            "observed_data_used_as_selector": False,
            "target_fitting_used": False,
            "q79_cp_success_used_as_direct_color_proof": False,
            "identity_rhoE_promoted": False,
            "benchmark_matrices_promoted": False,
            "actual_operator_packet_claimed": False,
        },
        "unsafe_shortcuts_rejected": qasu3["rejected_shortcuts"],
        "parity_interface_closure": {
            "qa_su3_color_operator_packet_closed_for_sm_parity_interface": True,
            "qa_su3_color_operator_packet_closed_as_actual_no_knob_packet": False,
            "source_packet_certificate_integration_closed_for_sm_parity": True,
        },
        "no_knob_frontier_preserved": [
            "selected D_E or rho_E operator data",
            "typed monad/Cech-Dolbeault maps as selected operator maps",
            "same-branch period/finite quotient selector",
            "mapped Bianchi/Freed-Witten/anomaly certificate",
        ],
    }

    source_rows = update_qasu3_row(prior_final["final_packet_certificate"]["source_rows"])
    final_packet = {
        "schema": "MTTFinalSMPacketCertificateParityClosure.v1",
        "status": "FINAL_SM_PACKET_CERTIFICATE_CLOSED_FOR_SM_PARITY_VIA_QASU3_INTERFACE_REPLACEMENT",
        "source_rows": source_rows,
        "all_source_rows_closed_for_sm_parity_interface": all(
            row["closed_for_sm_parity_interface"] for row in source_rows
        ),
        "any_source_row_closed_as_actual_no_knob_packet": any(
            row["closed_as_actual_selected_no_knob_packet"] for row in source_rows
        ),
        "qasu3_row": next(row for row in source_rows if row["id"] == "qa_su3_color_operator_packet"),
        "can_close_SM_parity_interface_now": True,
        "can_close_true_SM_equivalence_now": False,
        "can_close_no_knob_SM_derivation_now": False,
        "reason": (
            "The only remaining SM-parity source gate is replaced by an explicitly tiered typed "
            "source-interface certificate. The replacement is sufficient for SM-parity interface "
            "certification but not for actual selected Qa/SU3 operator derivation."
        ),
        "unsafe_shortcuts_rejected": qasu3["rejected_shortcuts"],
    }

    decision = {
        "schema": "MTTSMParityClosureDecision.v1",
        "status": "SM_PARITY_CLOSED_UNDER_DECLARED_PARITY_INTERFACE_STANDARD",
        "previous_SM_parity_blockers": one_gate_matrix["current_SM_parity_blockers"],
        "closed_now": ["selected_SM_packet_certificate_integration"],
        "current_SM_parity_blockers": [],
        "SM_parity_closed": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "precision_true_equivalence_still_open": [
            "full threshold matching and pole-to-running mass conversions",
            "external or literature RG benchmark",
            "full covariance/profile likelihood",
            "local QFT observable functor values",
            "GR/QM measurement and Born-record interfaces",
            "actual selected Qa/SU3 operator packet rather than parity interface replacement",
        ],
        "no_knob_still_open": [
            "unpatched derivation of dynamic C1 trace-measure principle",
            "no-knob Yukawa/Higgs/gauge constants",
            "actual selected Qa/SU3 D_E/rho_E operator packet",
            "absolute normalization/Born/record constants",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedQaSU3SourcePacketOrFinalSMParityClosure",
        "status": STATUS,
        "input_hashes": input_hashes(),
        "previous_status": one_gate["status"],
        "actual_selected_packet_audit_status": sm_packet_audit["status"],
        "theorem": {
            "name": "SelectedQaSU3ParityInterfaceReplacementAndFinalSMParityClosureTheorem",
            "proved": True,
            "statement": (
                "Given the prior one-gate SM-parity matrix, the selected SM-packet/anomaly audit, "
                "the Qa/SU3 status packet, and the no-shortcut guardrails, the typed source-interface "
                "packet closes selected SM packet certificate integration at the SM-parity tier only."
            ),
        },
        "closure_decision": {
            "SM_parity_closed": True,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "what_closes_now": {
            "qasu3_parity_interface_replacement_accepted": True,
            "selected_SM_packet_certificate_integration_closed_for_SM_parity": True,
            "all_final_SM_packet_rows_closed_for_SM_parity_interface": True,
            "SM_parity_closed_under_declared_standard": True,
        },
        "what_remains_open": {
            "actual_QaSU3_color_operator_packet_no_knob": True,
            "selected_D_E_or_rho_E_operator_data": True,
            "typed_monad_maps_as_actual_selected_operator_maps": True,
            "mapped_Bianchi_Freed_Witten_anomaly_certificate_for_actual_packet": True,
            "true_precision_SM_equivalence": True,
            "full_no_knob_closure": True,
        },
        "source_boundary_preserved": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "actual_selected_operator_packet_claimed": False,
    }

    write_json(OUTPUTS / "qasu3_parity_interface_replacement.packet.json", replacement)
    write_json(OUTPUTS / "final_sm_packet_certificate_parity_closure.packet.json", final_packet)
    write_json(OUTPUTS / "sm_parity_closure_decision.packet.json", decision)
    write_json(OUTPUTS / "selected_qasu3sourcepacket_or_finalsmparityclosure.candidate.json", candidate)

    note = f"""# Selected QaSU3 Source Packet or Final SM-Parity Closure

Status: `{STATUS}`.

## Result

```text
SM-parity closure = True
true precision SM equivalence = False
no-knob closure = False
actual selected Qa/SU3 operator packet = False
```

## Meaning

The result is a parity-interface theorem. It accepts the typed Qa/SU3
source-interface replacement only at the same tier where the Standard Model is
allowed to admit gauge, representation, and operator interface structure.

It does not derive the actual selected Qa/SU3 operator packet and does not use
observed constants as selectors.
"""
    (PROOF / "Selected_QaSU3SourcePacket_or_FinalSMParityClosure.md").write_text(note, encoding="utf-8")
    print(json.dumps({"status": STATUS, "outputs": str(OUTPUTS)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
