"""Audit the selected Qa/SU3 central-character homomorphism theorem."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_central_character_homomorphism_theorem_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Central_Character_Homomorphism_Theorem_v1.md"
SCRIPT = REPO / "scripts" / "compute_selected_qa_su3_central_character_homomorphism_theorem.py"


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
    verdict = cert["verdict"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "QA_SU3_CENTRAL_CHARACTER_HOMOMORPHISM_RANK_ONE_NO_GO",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["ordinary_u1_local_system_test"] == cert["ordinary_u1_local_system_test"]
            and computed["su3_scalar_center_test"] == cert["su3_scalar_center_test"],
            computed["verdict"],
        ),
        check(
            "q64 phase has order 64",
            cert["selected_candidate"]["exact_order"] == 64,
            cert["selected_candidate"],
        ),
        check(
            "ordinary U1 character blocked",
            cert["ordinary_u1_local_system_test"]["passes"] is False
            and "rho(z)=1" in cert["ordinary_u1_local_system_test"]["reason"],
            cert["ordinary_u1_local_system_test"],
        ),
        check(
            "SU3 scalar center blocked",
            cert["su3_scalar_center_test"]["passes"] is False
            and cert["su3_commutator_test"]["passes"] is False,
            {
                "scalar": cert["su3_scalar_center_test"],
                "commutator": cert["su3_commutator_test"],
            },
        ),
        check(
            "negative theorem scoped",
            verdict["rank_one_u1_local_system_bridge_closed_negative"] is True
            and verdict["q64_projective_route_remains_open"] is True
            and verdict["qa_su3_closed"] is False,
            verdict,
        ),
        check(
            "clock shift route not overclaimed",
            cert["nonabelian_clock_shift_route"]["status"] == "OPEN_NOT_QA_SU3_CLOSED"
            and cert["nonabelian_clock_shift_route"]["minimal_finite_dimension_for_exact_phase"] == 64,
            cert["nonabelian_clock_shift_route"],
        ),
        check(
            "forbidden shortcuts recorded",
            "q64=15 as a rank-one U1 character on the Heisenberg center" in cert["do_not_use"]
            and "clock-shift U64 representation as SU3 closure without an operator bridge" in cert["do_not_use"],
            cert["do_not_use"],
        ),
        check(
            "note records negative result",
            "rank-one U1 local-system bridge: closed negative" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 central-character homomorphism theorem audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
