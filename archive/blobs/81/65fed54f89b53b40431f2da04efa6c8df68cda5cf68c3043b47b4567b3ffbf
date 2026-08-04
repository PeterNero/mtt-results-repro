"""Audit the selected Qa/SU3 source-augmentation packet fill attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_source_augmentation_packet_fill_attempt_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Source_Augmentation_Packet_Fill_Attempt_v1.md"
SCRIPT = REPO / "scripts" / "attempt_fill_selected_qa_su3_source_augmentation_iwasawa_monad_maps.py"


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
    fill = cert["fill_result"]
    gates = cert["gate_results"]
    terms = cert["source_scan"]["terms"]
    blockers = cert["hard_blockers"]
    mismatch = cert["local_frame_mismatch"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "QA_SU3_SOURCE_AUGMENTATION_PACKET_FILL_ATTEMPT_BLOCKED_AUTOMORPHY_SECTION_RING_OPEN",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["fill_result"] == cert["fill_result"]
            and computed["gate_results"] == cert["gate_results"]
            and computed["source_scan"] == cert["source_scan"],
            computed["fill_result"],
        ),
        check(
            "source fills partial monad context",
            terms["iwasawa_quotient"] is True
            and terms["printed_monad_sequence"] is True
            and terms["generic_maps"] is True
            and fill["source_certificate_filled"] is True,
            terms,
        ),
        check(
            "automorphy and section ring remain open",
            gates["automorphy_cocycle"] == "FAIL_CURRENT_SOURCE_NO_GO"
            and gates["section_ring"] == "FAIL_INTERFACE_ONLY_VALUES_OPEN"
            and blockers["charge_to_factor_map"] is None
            and blockers["product_constants"] is None,
            blockers,
        ),
        check(
            "local-frame constants not promoted",
            gates["generic_constant_maps"] == "FAIL_LOCAL_FRAME_STATEMENT_NOT_GLOBAL_SECTION_PACKET"
            and "global sections" in " ".join(mismatch["why_not_enough"])
            and blockers["f_coefficients"] is None
            and blockers["g_coefficients"] is None,
            mismatch,
        ),
        check(
            "operator exit remains unavailable",
            gates["operator_exit"] == "FAIL_NOT_AVAILABLE"
            and fill["operator_exit_available"] is False
            and fill["determinant_computable_now"] is False,
            fill,
        ),
        check(
            "validator still refuses open packet",
            cert["template_validator_result"]["exit_code"] == 2
            and "OPEN:" in cert["template_validator_result"]["output"],
            cert["template_validator_result"],
        ),
        check(
            "no closure or target fitting claimed",
            fill["qa_su3_closed"] is False
            and fill["target_fitting_used"] is False
            and fill["explicit_f_g_constructed"] is False,
            fill,
        ),
        check(
            "note records repair options",
            "Selected_Qa_SU3_Source_Augmentation_Repair_Options_v1" in note
            and "Qa/SU3 closed: no" in note
            and "target fitting used: no" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 source-augmentation packet fill attempt audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
