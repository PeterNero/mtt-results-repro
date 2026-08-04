"""Audit the Strominger/Iwasawa source-to-c-twist map gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "strominger_source_to_ctwist_map_or_nogo_certificate.json"
DATA = REPO / "candidate_data" / "strominger_source_to_ctwist_map_or_nogo.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Strominger_Source_to_CTwist_Map_or_NoGo_v1.md"
SCRIPT = REPO / "scripts" / "build_strominger_source_to_ctwist_map_or_nogo.py"


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
    maps = {item["route_id"]: item for item in data["candidate_maps"]}
    gates = data["gate_results"]
    scans = data["source_scans"]
    checks = [
        check("status", cert["status"] == "QA_SU3_STROMINGER_SOURCE_TO_CTWIST_MAP_GATE_BUILT_MAP_OPEN_NO_GO_NOT_TRIGGERED", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("strominger source present", scans["strominger"]["terms"]["fixed_topological_sector"] and scans["strominger"]["terms"]["Hhat_global"], scans["strominger"]),
        check("iwasawa gerbe present", scans["iwasawa_flux"]["terms"]["integral_periods"] and scans["iwasawa_flux"]["terms"]["B_field_global"], scans["iwasawa_flux"]),
        check("q79 kept guardrail", maps["finite_Z3_torsion_extraction"]["verdict"] == "GUARDRAIL_ONLY", maps["finite_Z3_torsion_extraction"]),
        check("transgression remains live", maps["Hhat_curvature_transgression"]["verdict"] == "LIVE_BUT_VALUES_OPEN", maps["Hhat_curvature_transgression"]),
        check("map not supplied", gates["same_branch_tau_to_c_twist_map_supplied"] is False and cert["what_remains_open"]["explicit_restriction_slant_or_transgression_to_c_twist"] is True, gates),
        check("no no-go", gates["same_branch_tau_to_c_twist_map_proved_zero"] is False and gates["gerbe_route_retired"] is False, gates),
        check("fallback required", gates["A01_DE_parallel_fallback_required"] is True, gates),
        check("closure not claimed", cert["closure_claimed"] is False and cert["what_remains_open"]["qa_su3_packet_closed"] is False, cert),
        check("no target fitting", cert["target_fitting_used"] is False and data["target_fitting_used"] is False, cert),
        check("note records next artifact", cert["next_required_artifact"] in note, NOTE),
    ]
    print("\nSelected Qa/SU3 Strominger source-to-c-twist map/no-go audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
