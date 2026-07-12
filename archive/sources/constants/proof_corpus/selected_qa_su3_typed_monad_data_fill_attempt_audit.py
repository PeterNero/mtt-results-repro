"""Audit the selected Qa/SU3 typed monad data fill attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_typed_monad_data_fill_attempt_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Typed_Monad_Data_Fill_Attempt_v1.md"
SCRIPT = REPO / "scripts" / "attempt_fill_selected_qa_su3_typed_monad_data.py"


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
    scan_terms = cert["source_scan"]["terms"]
    partial = cert["partial_packet"]
    unfilled = cert["unfilled_slots"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "QA_SU3_TYPED_MONAD_DATA_FILL_ATTEMPT_BLOCKED_TYPED_MAPS_MISSING",
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
            "source topological monad data found",
            scan_terms["printed_monad_sequence"] is True
            and scan_terms["printed_ell_data"] is True
            and scan_terms["printed_kappa_data"] is True
            and gates["topological_monad_data"] == "PASS_SOURCE_PRINTED",
            scan_terms,
        ),
        check(
            "source names generic maps only",
            scan_terms["generic_maps_statement"] is True
            and scan_terms["constant_matrices_statement"] is True
            and gates["typed_f_g_maps"] == "FAIL_SOURCE_PRINTED_GENERIC_ONLY",
            gates,
        ),
        check(
            "typed matrices remain open",
            unfilled["f_map_matrix"] is None
            and unfilled["g_map_matrix"] is None
            and unfilled["g_f_zero"] is None
            and partial["typed_monad"]["f_map"]["matrix"] is None
            and partial["typed_monad"]["g_map"]["matrix"] is None,
            partial["typed_monad"],
        ),
        check(
            "operator exits remain open",
            gates["de_operator_packet"].startswith("FAIL")
            and gates["rhoE_packet"].startswith("FAIL")
            and unfilled["de_operator_packet"]["available"] is False
            and unfilled["rhoE_packet"]["available"] is False,
            unfilled,
        ),
        check(
            "validator refuses open template",
            cert["template_validator_result"]["exit_code"] == 2
            and "OPEN:" in cert["template_validator_result"]["output"],
            cert["template_validator_result"],
        ),
        check(
            "no closure or target fitting claimed",
            fill["topological_monad_data_filled"] is True
            and fill["typed_maps_filled"] is False
            and fill["determinant_computable_now"] is False
            and fill["qa_su3_closed"] is False
            and fill["target_fitting_used"] is False,
            fill,
        ),
        check(
            "note records next construction or augmentation gate",
            "Selected_Qa_SU3_Monad_Map_Construction_or_Source_Augmentation_v1" in note
            and "typed maps filled: no" in note
            and "Qa/SU3 closed: no" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 typed monad data fill attempt audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
