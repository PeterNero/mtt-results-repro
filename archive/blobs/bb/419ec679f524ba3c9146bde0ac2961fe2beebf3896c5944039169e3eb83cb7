"""Audit the Qa/SU3 repair-options external synthesis."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_repair_options_external_synthesis_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Repair_Options_External_Synthesis_v1.md"
SCRIPT = REPO / "scripts" / "build_selected_qa_su3_repair_options_external_synthesis.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def run_script() -> dict:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    return json.loads(proc.stdout)


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    computed = run_script()
    note = NOTE.read_text(encoding="utf-8")
    evidence = cert["local_evidence_summary"]
    routes = {route["id"]: route for route in cert["routes"]}
    verdict = cert["verdict"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "QA_SU3_REPAIR_OPTIONS_SYNTHESIZED_GERBE_ROUTE_PRIMARY_VALUES_OPEN",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["local_evidence_summary"] == cert["local_evidence_summary"]
            and computed["recommendation"] == cert["recommendation"]
            and computed["verdict"] == cert["verdict"],
            computed["verdict"],
        ),
        check(
            "external anchors recorded",
            len(cert["external_anchors"]) >= 5
            and any(anchor["id"] == "kapustin_b_field_twisted_bundles" for anchor in cert["external_anchors"])
            and any(anchor["id"] == "iwasawa_complex_geometry" for anchor in cert["external_anchors"]),
            cert["external_anchors"],
        ),
        check(
            "ordinary route blocked by c-axis obstruction",
            evidence["ordinary_c_axis_obstruction"] is True
            and evidence["c_axis_obstructed_spaces"] == 8
            and routes["ordinary_line_bundle_full_nil_theta"]["status"] == "CONDITIONALLY_RETIRED_UNLESS_C_SOURCE_AMENDED",
            routes["ordinary_line_bundle_full_nil_theta"],
        ),
        check(
            "direct operator exit remains live but unavailable",
            routes["source_certified_direct_operator_exit"]["status"] == "LIVE_BUT_NO_CURRENT_SOURCE_EXIT"
            and routes["source_certified_direct_operator_exit"]["can_close_now"] is False,
            routes["source_certified_direct_operator_exit"],
        ),
        check(
            "gerbe route promoted as primary candidate",
            evidence["gerbe_twist_products_close"] is True
            and evidence["finite_z3_gerbe_candidate_closed"] is True
            and routes["projective_gerbe_twisted_module"]["status"] == "PRIMARY_SOLUTION_CANDIDATE_SOURCE_SELECTION_OPEN",
            routes["projective_gerbe_twisted_module"],
        ),
        check(
            "honest no-closure verdict",
            verdict["solution_found_at_typing_level"] is True
            and verdict["full_packet_closed"] is False
            and verdict["target_fitting_used"] is False,
            verdict,
        ),
        check(
            "note records next gate",
            "Selected_Qa_SU3_Twisted_Section_Ring_and_Gerbe_Source_Gate_v1" in note
            and "full packet closed: no" in note
            and "target fitting used: no" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 repair-options external synthesis audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
