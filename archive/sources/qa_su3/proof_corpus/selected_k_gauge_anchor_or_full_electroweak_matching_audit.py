"""Audit the selected K_gauge anchor / electroweak matching frontier theorem."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_k_gauge_anchor_or_full_electroweak_matching.py"
DATA = REPO / "candidate_data" / "selected_k_gauge_anchor_or_full_electroweak_matching.candidate.json"
CERT = REPO / "certificates" / "selected_k_gauge_anchor_or_full_electroweak_matching_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_K_Gauge_Anchor_or_Full_Electroweak_Matching_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(name: str, condition: bool, detail: object) -> None:
    if condition:
        print(f"PASS: {name} -- {detail}")
        return
    print(f"FAIL: {name} -- {detail}")
    raise SystemExit(1)


def main() -> int:
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=REPO, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(proc.stdout)
    check("builder exits cleanly", proc.returncode == 0, proc.returncode)

    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    theorem = data["theorem"]
    checks = data["source_checks"]

    check("status is internal closure only", data["status"] == "INTERNAL_K_GAUGE_ANCHOR_CLOSED_PHYSICAL_ELECTROWEAK_MATCHING_OPEN", data["status"])
    check("internal K closed as unit", decision["internal_K_gauge_anchor_closed"] is True and decision["internal_K_gauge_value"] == "1", decision)
    check("physical closure rejected", decision["physical_K_gauge_anchor_closed"] is False and decision["measured_electroweak_closure"] is False, decision)
    check("kernel vector exact", decision["selected_internal_kernel_vector"] == {"U1": "2/3", "SU2": "1", "Qa_or_SU3": "log(2008)"}, decision["selected_internal_kernel_vector"])
    check("cross repo checks all pass", all(checks.values()), checks)
    check("M-theory physical slot retained", "kappa_11" in theorem["physical_kernel_required"]["K_phys_source"], theorem["physical_kernel_required"])
    check("missing threshold and scheme recorded", "selected threshold vector Delta_a^sel" in theorem["physical_kernel_required"]["still_missing"] and "fixed RG and threshold scheme" in theorem["physical_kernel_required"]["still_missing"], theorem["physical_kernel_required"]["still_missing"])
    check("guardrails reject measured comparison", any("Do not compare" in item for item in data["guardrails"]) and any("observed alpha_EM" in item for item in data["guardrails"]), data["guardrails"])
    check("certificate agrees", cert["closed"]["internal_K_gauge_anchor"] is True and cert["open"]["physical_K_gauge_anchor"] is True, cert)
    check("note records scope", "not yet predicted" in note and "K_gauge,int = 1" in note, NOTE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
