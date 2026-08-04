"""Audit non-identity rho_E / quotient-valid B_N interface import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "import_nonidentity_rhoe_quotientvalid_bn_interface.py"
PACKET = ROOT / "candidate_data" / "nonidentity_rhoe_quotientvalid_bn_interface_import.candidate.json"
CERT = ROOT / "certificates" / "nonidentity_rhoe_quotientvalid_bn_interface_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "NonIdentity_RhoE_QuotientValid_BN_Interface_Import_v1.md"

STATUS = "NONIDENTITY_RHOE_QUOTIENTVALID_BN_INTERFACE_IMPORTED_FILL_OPEN"
NEXT = "Selected_U1Y_RouteC_NonIdentity_RhoE_and_QuotientValid_BN_FillAttempt_v1"


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
    check(
        "upstream template remains open",
        packet["template"]["source_evidence"]["selected_by_mtt"] is None
        and packet["template"]["rho_E"]["nonidentity"] is None
        and packet["template"]["B_N"]["quotient_valid"] is None
        and packet["upstream_certificate"]["closure_claimed"] is False,
        packet["template"],
    )

    scaffold = packet["local_support_scaffold"]
    check(
        "local support scaffold aligned",
        scaffold["closed_now"]["nonidentity_projective_rhoE_candidate_built"] is True
        and scaffold["closed_now"]["smooth_BN_27_mode_scaffold_built"] is True
        and scaffold["closed_now"]["D_E_matrix_on_27_mode_BN_emitted"] is True
        and scaffold["closed_now"]["sector_projectors_and_dotD_same_basis_emitted"] is True,
        scaffold["closed_now"],
    )
    check(
        "support scaffold not selected fill",
        scaffold["finite_prefix_summary"]["rho_E"]["selected_by_mtt"] is False
        and scaffold["not_closed"]["R1_selected_source_certificate"] is True
        and scaffold["not_closed"]["R2_source_promotion_for_rhoE"] is True,
        scaffold,
    )
    check(
        "canonical C1 zero response blocks closure",
        scaffold["closed_now"]["canonical_C1_zero_response_no_go_proved"] is True
        and scaffold["finite_prefix_summary"]["C1"]["all_c1_matrices_zero_for_canonical_tensor"] is True,
        scaffold["finite_prefix_summary"]["C1"],
    )
    check(
        "frontier advances to fill attempt",
        packet["frontier_update"]["current_next"] == NEXT,
        packet["frontier_update"],
    )
    check("guardrails retained", all(value is True for value in cert["guardrails"].values()), cert["guardrails"])

    note = NOTE.read_text(encoding="utf-8")
    for phrase in ("not selected by MTT", "zero one-response", "selected `deltaTheta/C1`"):
        check(f"note records {phrase}", phrase in note, NOTE)

    print("\nNon-identity rho_E / quotient-valid B_N interface import audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
