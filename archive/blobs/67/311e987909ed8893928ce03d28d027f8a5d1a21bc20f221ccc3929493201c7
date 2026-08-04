"""Audit the U1/SU2 payload template or K_gauge source fill attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "u1_su2_internal_overlap_payload_template_or_k_gauge_source_fill_certificate.json"
DATA = REPO / "candidate_data" / "u1_su2_internal_overlap_payload_template_or_k_gauge_source_fill.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1_SU2_Internal_Overlap_Payload_Template_or_K_Gauge_Source_Fill_v1.md"
SCRIPT = REPO / "scripts" / "build_u1_su2_internal_overlap_payload_template_or_k_gauge_source_fill.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def route(data: dict[str, object], route_id: str) -> dict[str, object]:
    return next(item for item in data["candidate_routes"] if item["id"] == route_id)


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
    decision = data["decision"]
    handles = data["source_extracted_handles"]
    checks = [
        check("status", cert["status"] == "U1_SU2_K_GAUGE_FILL_ATTEMPT_TEMPLATE_BUILT_CURRENT_SOURCE_PARTIAL_ONLY", cert["status"]),
        check("script agreement", computed["what_remains_open"] == cert["what_remains_open"], computed["what_remains_open"]),
        check("templates built", "I_1 = chi_1" in data["payload_template"]["I_1_template"] and "I_2 = chi_2" in data["payload_template"]["I_2_template"], data["payload_template"]),
        check("normalization index handle found", any(item["name"] == "normalization_index" for item in handles["theta_gauge_threshold_variables"]), handles["theta_gauge_threshold_variables"]),
        check("inverse use is discovery only", handles["gauge_couplings_allowed_use"] == "DISCOVERY_ONLY", handles),
        check("SM gauge couplings not source-selected", handles["sm_gauge_coupling_slot_status"] == "MEASURED_PARITY_INPUT_ALLOWED_AFTER_PACKET_SELECTION", handles),
        check("representation packet absent", handles["actual_selected_representation_packet_supplied"] is False, handles),
        check("Qa/SU3 operator packet absent in SM repo", handles["qa_su3_operator_packet_supplied"] is False, handles),
        check("U1 route partial", route(data, "topology_hypercharge_line_bundle_route")["current_status"] == "PARTIAL_STRUCTURAL_NOT_PROMOTED", route(data, "topology_hypercharge_line_bundle_route")),
        check("SU2 route partial", route(data, "weak_su2_carrier_route")["current_status"] == "PARTIAL_STRUCTURAL_NOT_PROMOTED", route(data, "weak_su2_carrier_route")),
        check("K route discovery only", route(data, "inverse_normalization_index_route")["current_status"] == "DISCOVERY_ONLY_NOT_PROMOTED", route(data, "inverse_normalization_index_route")),
        check("no filled payloads", decision["I_1_filled"] is False and decision["I_2_filled"] is False and decision["K_gauge_filled"] is False, decision),
        check("no measured closure", decision["measured_electroweak_closure"] is False, decision),
        check("promotion tests forbid target selector", any("removed from selectors" in item for item in data["promotion_tests"]), data["promotion_tests"]),
        check("note records next object", "Selected_U1_SU2_Source_Response_or_Normalization_Index_Run_v1" in note, NOTE),
    ]
    print("\nSelected U1/SU2 internal overlap payload template or K_gauge source fill audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
