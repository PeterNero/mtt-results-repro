"""Audit the actual selected SM packet and anomaly artifact."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "actual_selected_sm_packet_anomaly_audit_certificate.json"
DATA = REPO / "candidate_data" / "actual_selected_sm_packet_anomaly_audit.candidate.json"
NOTE = REPO / "proof_corpus" / "MTT_Actual_Selected_SM_Packet_and_Anomaly_Audit_v1.md"
SCRIPT = REPO / "scripts" / "build_actual_selected_sm_packet_anomaly_audit.py"

REQUIRED_COMPONENTS = {
    "gauge_carrier_su3_su2_u1",
    "fermion_representation_packet",
    "three_family_selector",
    "higgs_carrier_and_yukawa_slots",
    "anomaly_cancellation_certificate",
    "qa_su3_color_operator_packet",
}


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    data = json.loads(DATA.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    computed = json.loads(proc.stdout)
    gates = data["gate_results"]
    components = data["packet_components"]
    component_ids = {row["id"] for row in components}
    sources_present = all(body["present"] for body in data["source_presence"].values())
    qa_open = data["qa_su3_what_remains_open"]
    shortcut_text = " ".join(data["unsafe_shortcuts_rejected"]).lower()
    checks = [
        check("status", cert["status"] == "MTT_ACTUAL_SELECTED_SM_PACKET_AUDIT_BUILT_PACKET_STILL_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("sources present", sources_present, data["source_presence"]),
        check("components complete", REQUIRED_COMPONENTS.issubset(component_ids), component_ids),
        check("topology support", gates["topology_only_sm_structure_supported"] is True, gates),
        check("anomaly support", gates["anomaly_structure_supported"] is True, gates),
        check("representation packet still open", gates["actual_selected_representation_packet_supplied"] is False, gates),
        check("anomaly table still open", gates["actual_anomaly_table_computed_on_selected_packet"] is False, gates),
        check("qa su3 packet still open", gates["qa_su3_operator_packet_supplied"] is False, gates),
        check("typed maps still open", gates["typed_monad_or_section_ring_values_supplied"] is False, gates),
        check("qa open fields imported", "selected_D_E_or_rho_E_operator_packet" in qa_open and "selected_typed_monad_maps_or_Cech_Dolbeault_packet" in qa_open, qa_open),
        check("reject q79 import shortcut", "q79" in shortcut_text and "direct" in shortcut_text, data["unsafe_shortcuts_rejected"]),
        check("reject generic anomaly shortcut", "generic topology-only" in shortcut_text and "representation table" in shortcut_text, data["unsafe_shortcuts_rejected"]),
        check("selected packet not closed", gates["selected_sm_packet_closed"] is False and cert["what_remains_open"]["selected_sm_packet_closed"] is False, cert),
        check("closure not claimed", gates["sm_parity_closure_claimed"] is False and cert["closure_claimed"] is False, cert),
        check("no target fitting", gates["target_fitting_used"] is False and cert["target_fitting_used"] is False, cert),
        check("note records missing packet", "actual selected packet is not yet closed" in note and "Qa/SU3 color/operator packet" in note, NOTE),
        check("next artifact selected", data["next_required_artifact"] == "MTT_Qa_SU3_Color_Operator_Packet_Source_Gate_v1", data["next_required_artifact"]),
    ]
    print("\nMTT actual selected SM packet and anomaly audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
