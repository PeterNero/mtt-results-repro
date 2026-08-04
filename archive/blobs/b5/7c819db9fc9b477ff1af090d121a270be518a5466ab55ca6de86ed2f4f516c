"""Audit the operator-level rho_E/B_N fill cut-set import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "import_operatorlevel_fill_cutset_matter_overlap.py"
PACKET = ROOT / "candidate_data" / "operatorlevel_rhoe_bn_fill_cutset_matter_overlap_import.candidate.json"
CERT = ROOT / "certificates" / "operatorlevel_rhoe_bn_fill_cutset_matter_overlap_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "OperatorLevel_RhoE_BN_Fill_Cutset_MatterOverlap_Import_v1.md"

STATUS = "OPERATORLEVEL_RHOE_BN_FILL_REDUCED_MATTERSLOT_OVERLAP_SOURCE_OPEN"
NEXT = "Selected_U1Y_RouteC_Hybrid_Galerkin_Overlap_Source_Packet_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(label: str, condition: bool, detail: object) -> None:
    print(f"{'PASS' if condition else 'FAIL'}: {label} -- {detail}")
    if not condition:
        raise SystemExit(1)


def main() -> int:
    packet = load(PACKET)
    cert = load(CERT)
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    check("script runs", proc.returncode == 0, proc.stdout)
    script_cert = json.loads(proc.stdout)

    check("status", cert["status"] == STATUS, cert["status"])
    check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])
    check("theorem proved", packet["theorem"]["proved"] is True, packet["theorem"])
    check("all checks pass", all(packet["checks"].values()), packet["checks"])
    structural = packet["structural_partition"]
    check(
        "structural partition matches",
        structural["matches_required_partition"] is True
        and sorted(structural["phase_route_from_10M"]) == ["e", "u"]
        and sorted(structural["shift_route_from_non10_plus_singlet"]) == ["d", "nuD"]
        and structural["nuD_singlet_rule_closed"] is False,
        structural,
    )
    check(
        "selected clauses remain open",
        all(item["closed"] is False for item in packet["theorem_clauses"]),
        packet["theorem_clauses"],
    )
    check(
        "operator cutset remains open",
        packet["visible_operator_cutset"]["selected_D_E_dotD_Riesz_Green"] is True
        and packet["visible_operator_cutset"]["primitive_C1_overlap_tensors"] is True,
        packet["visible_operator_cutset"],
    )
    check("frontier advances", packet["frontier_update"]["current_next"] == NEXT, packet["frontier_update"])
    check("guardrails retained", all(value is True for value in cert["guardrails"].values()), cert["guardrails"])

    note = NOTE.read_text(encoding="utf-8")
    for phrase in ("matter-slot overlap", "conditional route is exact", "without locked target columns"):
        check(f"note records {phrase}", phrase in note, NOTE)

    print("\nOperator-level rho_E/B_N fill cut-set import audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
