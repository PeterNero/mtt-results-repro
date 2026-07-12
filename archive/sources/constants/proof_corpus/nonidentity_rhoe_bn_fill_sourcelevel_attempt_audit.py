"""Audit the source-level non-identity rho_E / B_N fill attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "attempt_nonidentity_rhoe_bn_fill_sourcelevel.py"
PACKET = ROOT / "candidate_data" / "nonidentity_rhoe_bn_fill_sourcelevel_attempt.candidate.json"
CERT = ROOT / "certificates" / "nonidentity_rhoe_bn_fill_sourcelevel_attempt_certificate.json"
NOTE = ROOT / "proof_corpus" / "NonIdentity_RhoE_BN_Fill_SourceLevel_Attempt_v1.md"

STATUS = "NONIDENTITY_RHOE_BN_FILL_SOURCELEVEL_RHOE_CLOSED_OPERATOR_BN_OPEN"
NEXT = "Selected_U1Y_RouteC_OperatorLevel_RhoE_BN_SectorCharge_and_C1_Fill_v1"


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

    fill = packet["partial_fill"]
    check(
        "source-level rhoE filled",
        fill["source_evidence"]["selected_by_mtt"] is True
        and fill["source_evidence"]["same_branch_q79_F_m1"] is True
        and fill["rho_E"]["nonidentity"] is True
        and fill["rho_E"]["operator_level_projective_rhoE_promoted"] is False,
        fill,
    )
    check(
        "operator slots remain open",
        fill["B_N"]["quotient_valid"] is None
        and fill["operator_replay"]["D_E"] is None
        and fill["correction_emission"]["A_selected"] is None,
        fill,
    )
    support = packet["support_scaffold_not_promoted"]
    check(
        "local scaffold not promoted",
        support["finite_prefix_summary"]["rho_E"]["selected_by_mtt"] is False
        and support["finite_prefix_summary"]["C1"]["all_c1_matrices_zero_for_canonical_tensor"] is True,
        support["finite_prefix_summary"],
    )
    check("frontier advances", packet["frontier_update"]["current_next"] == NEXT, packet["frontier_update"])
    check("guardrails retained", all(value is True for value in cert["guardrails"].values()), cert["guardrails"])

    note = NOTE.read_text(encoding="utf-8")
    for phrase in ("source level", "not operator-level closure", "quotient-valid `B_N`"):
        check(f"note records {phrase}", phrase in note, NOTE)

    print("\nNon-identity rho_E / B_N source-level fill attempt audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
