"""Audit the Qa/SU3 repair-options synthesis."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "repair_options_external_synthesis_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Source_Augmentation_Repair_Options_v1.md"
SCRIPT = REPO / "scripts" / "build_repair_options_external_synthesis.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=REPO, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=True)
    computed = json.loads(proc.stdout)
    evidence = cert["local_evidence_summary"]
    routes = {route["id"]: route for route in cert["routes"]}
    verdict = cert["verdict"]
    checks = [
        check("status", cert["status"] == "QA_SU3_REPAIR_OPTIONS_SYNTHESIZED_GERBE_ROUTE_PRIMARY_VALUES_OPEN", cert["status"]),
        check("script agreement", computed["local_evidence_summary"] == cert["local_evidence_summary"] and computed["recommendation"] == cert["recommendation"] and computed["verdict"] == cert["verdict"], computed["verdict"]),
        check("external anchors recorded", len(cert["external_anchors"]) >= 5 and any(anchor["id"] == "kapustin_b_field_twisted_bundles" for anchor in cert["external_anchors"]) and any(anchor["id"] == "iwasawa_complex_geometry" for anchor in cert["external_anchors"]), cert["external_anchors"]),
        check("ordinary route blocked", evidence["ordinary_c_axis_obstruction"] is True and evidence["c_axis_obstructed_spaces"] == 8 and routes["ordinary_line_bundle_full_nil_theta"]["status"] == "CONDITIONALLY_RETIRED_UNLESS_C_SOURCE_AMENDED", routes["ordinary_line_bundle_full_nil_theta"]),
        check("direct operator unavailable", routes["source_certified_direct_operator_exit"]["status"] == "LIVE_BUT_NO_CURRENT_SOURCE_EXIT" and routes["source_certified_direct_operator_exit"]["can_close_now"] is False, routes["source_certified_direct_operator_exit"]),
        check("gerbe route primary candidate", evidence["gerbe_twist_products_close"] is True and evidence["finite_z3_gerbe_candidate_closed"] is True and routes["projective_gerbe_twisted_module"]["status"] == "PRIMARY_SOLUTION_CANDIDATE_SOURCE_SELECTION_OPEN", routes["projective_gerbe_twisted_module"]),
        check("honest no closure", verdict["solution_found_at_typing_level"] is True and verdict["full_packet_closed"] is False and verdict["target_fitting_used"] is False and cert["closure_claimed"] is False, verdict),
        check("note records next gate", cert["recommendation"]["next_required_artifact"] in note and "full packet closed: no" in note and "target fitting used: no" in note, NOTE),
    ]
    print("\nSelected Qa/SU3 repair-options synthesis audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
