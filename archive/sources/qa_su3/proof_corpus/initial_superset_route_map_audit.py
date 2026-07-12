"""Audit the initial Qa/SU3 route map."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "initial_superset_route_map_certificate.json"
SCRIPT = REPO / "scripts" / "build_initial_superset_route_map.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=REPO, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=True)
    computed = json.loads(proc.stdout)
    checks = [
        check("status", cert["status"] == "QA_SU3_PACKET_REPO_INITIALIZED_PRIMARY_SOURCE_AUGMENTATION_ROUTE", cert["status"]),
        check("script agreement", computed["route_ranking"] == cert["route_ranking"], computed["route_ranking"]),
        check("packet schema present", "D_E_or_rho_E_data" in cert["selected_packet_schema"], cert["selected_packet_schema"]),
        check("no closure claimed", cert["closure_claimed"] is False and cert["target_fitting_used"] is False, cert),
    ]
    print("\nInitial Qa/SU3 route map audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
