"""Audit the Qa/SU3 monad-to-operator-packet transfer gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_monad_to_operator_packet_transfer_gate_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Monad_to_Operator_Packet_Transfer_Gate_v1.md"
SCRIPT = REPO / "scripts" / "build_selected_qa_su3_monad_to_operator_packet_transfer_gate.py"


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


def route(cert: dict, route_id: str) -> dict:
    for item in cert["route_decision"]:
        if item["id"] == route_id:
            return item
    raise AssertionError(route_id)


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    computed = run_script()
    note = NOTE.read_text(encoding="utf-8")
    result = cert["result"]
    packet = cert["packet_transfer"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "QA_SU3_MONAD_TO_OPERATOR_PACKET_TRANSFER_PARTIAL_SOURCE_FOUND_OPERATOR_OPEN",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["result"] == cert["result"]
            and computed["erratum_and_mu_dependencies"] == cert["erratum_and_mu_dependencies"],
            computed["result"],
        ),
        check(
            "source slot partially filled",
            packet["selected_branch_and_source_certificate"]["status"] == "PARTIAL_PASS"
            and packet["selected_color_bundle_sheaf_or_twist"]["status"] == "CANDIDATE_PASS_NOT_SELECTED_FOR_THRESHOLD"
            and result["selected_source_slot_partially_filled"] is True,
            packet["selected_branch_and_source_certificate"],
        ),
        check(
            "operator slots remain open",
            packet["laplace_type_principal_symbol"]["status"] == "OPEN"
            and packet["endomorphism_E_or_heat_zero_order_block"]["status"] == "OPEN"
            and packet["spectrum_heat_torsion_finite_part"]["status"] == "OPEN",
            packet,
        ),
        check(
            "visible route not overpromoted",
            route(cert, "visible_E8_to_E6_benchmark_route")["status"]
            == "SUPPORTED_AS_SOURCE_CONTEXT_NOT_QA_SU3_CLOSURE"
            and route(cert, "direct_Qa_SU3_threshold_source_route")["status"]
            == "OPEN_REQUIRES_REPRESENTATION_MAP",
            cert["route_decision"],
        ),
        check(
            "A01 route blocked honestly",
            route(cert, "A01_left_invariant_operator_route")["status"]
            == "BLOCKED_BY_ERRATUM_AND_MU_SELECTION"
            and cert["erratum_and_mu_dependencies"]["printed_A01_as_determinant_source_accepted"] is False,
            cert["erratum_and_mu_dependencies"],
        ),
        check(
            "no closure claimed",
            result["endomorphism_E_computed"] is False
            and result["determinant_computable_now"] is False
            and result["qa_su3_closed"] is False
            and result["target_fitting_used"] is False,
            result,
        ),
        check(
            "guardrails recorded",
            "mu chosen from Qa/SU3 residual" in cert["do_not_use"]
            and "Chern classes c1,c2,c3 as substitute for endomorphism_E or determinant finite part" in cert["do_not_use"],
            cert["do_not_use"],
        ),
        check(
            "note records next source-certified operator gate",
            "Selected_Qa_SU3_Source_Certified_A01_Erratum_or_Monad_DE_Operator_v1" in note
            and "Qa/SU3 closed: no" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 monad-to-operator-packet transfer gate audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
