"""Audit the Qa/SU3 twisted gerbe source packet fill attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_twisted_gerbe_source_packet_fill_attempt_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Twisted_Gerbe_Source_Packet_Fill_Attempt_v1.md"
SCRIPT = REPO / "scripts" / "attempt_fill_selected_qa_su3_twisted_gerbe_source_packet.py"


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
    filled = cert["filled_fields"]
    unfilled = cert["unfilled_fields"]
    gates = cert["gate_results"]
    result = cert["fill_result"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "QA_SU3_TWISTED_GERBE_SOURCE_PACKET_FILL_ATTEMPT_PARTIAL_OPERATOR_SECTION_DATA_OPEN",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["filled_fields"] == cert["filled_fields"]
            and computed["unfilled_fields"] == cert["unfilled_fields"]
            and computed["fill_result"] == cert["fill_result"],
            computed["fill_result"],
        ),
        check(
            "selected gerbe source imported",
            filled["selected_s3_flat_deligne_class"] is True
            and filled["selected_s3_pullback_table"] is True
            and filled["map_to_qutrit_central_cocycle"] is True
            and filled["period_denominator"] == 3,
            filled,
        ),
        check(
            "admissibility partially filled",
            filled["smooth_freed_witten"] is True
            and filled["block_sector_projector_retention"] is True
            and gates["block_projector_retention"] == "PASS_BLOCK_SECTOR_ONLY",
            gates,
        ),
        check(
            "section and product data remain open",
            all(item["dimension"] is None and item["basis"] is None for item in unfilled["twisted_section_dimensions_and_bases"].values())
            and all(value is None for value in unfilled["twisted_product_constants"].values())
            and gates["twisted_section_bases"].startswith("OPEN")
            and gates["twisted_product_constants"].startswith("OPEN"),
            unfilled,
        ),
        check(
            "operator source remains open",
            unfilled["green_schwarz_bianchi_verified"] is None
            and unfilled["coherent_spectral_projector_verified"] is None
            and unfilled["operator_exit"]["finite_part_available"] is False
            and gates["operator_exit"].startswith("OPEN"),
            unfilled["operator_exit"],
        ),
        check(
            "validator refuses partial packet",
            cert["validator_result"]["exit_code"] == 2
            and "OPEN:" in cert["validator_result"]["output"],
            cert["validator_result"],
        ),
        check(
            "no closure or target fitting claimed",
            result["selected_gerbe_source_part_filled"] is True
            and result["twisted_section_ring_filled"] is False
            and result["qa_su3_closed"] is False
            and result["target_fitting_used"] is False,
            result,
        ),
        check(
            "note records next construction",
            "Selected_Qa_SU3_Twisted_Section_Basis_or_Operator_Exit_Construction_v1" in note
            and "Qa/SU3 closed: no" in note
            and "target fitting used: no" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 twisted gerbe source packet fill attempt audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
