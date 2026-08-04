"""Audit the Qa/SU3 twisted section-basis or operator-exit construction gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_twisted_section_basis_or_operator_exit_construction_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Twisted_Section_Basis_or_Operator_Exit_Construction_v1.md"
SCRIPT = REPO / "scripts" / "build_selected_qa_su3_twisted_section_basis_or_operator_exit_construction.py"


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
    closed = cert["closed_now"]
    not_closed = cert["not_closed"]
    gate = cert["gate_result"]
    live = cert["live_routes"]

    checks = [
        check(
            "certificate status",
            cert["status"]
            == "QA_SU3_TWISTED_SECTION_BASIS_OR_OPERATOR_EXIT_CONSTRUCTION_REDUCED_TO_ROUTE_C_SOURCE_PACKET",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["closed_now"] == cert["closed_now"]
            and computed["not_closed"] == cert["not_closed"]
            and computed["gate_result"] == cert["gate_result"],
            computed["gate_result"],
        ),
        check(
            "gerbe and curvature source closed only at source level",
            closed["selected_period_3_gerbe_source"] is True
            and closed["smooth_s3_freed_witten_and_block_sector_source"] is True
            and closed["visible_green_schwarz_curvature_level_source"] is True,
            closed,
        ),
        check(
            "section-basis and operator exits remain open",
            not_closed["ordinary_ab_factor_model"] is True
            and not_closed["twisted_section_bases"] is True
            and not_closed["twisted_product_constants"] is True
            and not_closed["selected_visible_operator_source"] is True
            and not_closed["selected_D_E_dotD_Riesz_Green"] is True,
            not_closed,
        ),
        check(
            "retired shortcuts are all retired",
            all(cert["retired_routes"].values()),
            cert["retired_routes"],
        ),
        check(
            "Route C is primary and executable as a contract",
            live["finite_selected_connection_solve_route_c"]["status"] == "PRIMARY_NEXT_CONSTRUCTION"
            and live["finite_selected_connection_solve_route_c"]["contract_available"] is True,
            live["finite_selected_connection_solve_route_c"],
        ),
        check(
            "no false full closure",
            gate["qa_su3_fully_closed"] is False
            and gate["operator_exit_available_now"] is False
            and gate["section_basis_exit_available_now"] is False
            and gate["target_fitting_used"] is False
            and gate["next_gate_is_sharp"] is True,
            gate,
        ),
        check(
            "note records the correct next artifact",
            "Selected_Qa_SU3_Finite_Selected_Connection_Solve_Packet_v1" in note
            and "Qa/SU3 fully closed: no" in note
            and "target fitting used: no" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 twisted section-basis or operator-exit construction audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
