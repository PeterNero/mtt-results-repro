"""Audit the complex-rotated c-twist primitive normalization gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "complex_rotated_ctwist_normalization_certificate.json"
DATA = REPO / "candidate_data" / "complex_rotated_ctwist_normalization.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Complex_Rotated_CTwist_Normalization_v1.md"
SCRIPT = REPO / "scripts" / "build_complex_rotated_ctwist_normalization.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    data = json.loads(DATA.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    computed = json.loads(proc.stdout)
    gates = data["gate_results"]
    checks = [
        check("status", cert["status"] == "QA_SU3_COMPLEX_ROTATED_CTWIST_PRIMITIVE_NORMALIZATION_CONDITIONAL_PERIOD_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("four primitive slants", len(data["slant_primitive_checks"]) == 4 and gates["all_slants_primitive_after_complex_polarization"] is True, data["slant_primitive_checks"]),
        check("unit scaled coefficients", gates["all_slants_unit_magnitude_in_scaled_frame"] is True, data["slant_primitive_checks"]),
        check("no raw nil axis requirement", gates["raw_nil_axis_match_required_for_ctwist_typing"] is False, gates),
        check("products cancel", gates["all_monad_products_remain_untwisted"] is True, data["product_cancellation_checks"]),
        check("conditional normalization only", gates["conditional_c_plus_minus_one_normalization"] is True and gates["selected_flux_period_normalization_proved"] is False, gates),
        check("finite quotient still open", gates["same_branch_finite_quotient_selected"] is False and cert["what_remains_open"]["same_branch_finite_quotient"] is True, cert),
        check("closure not claimed", cert["closure_claimed"] is False and cert["what_remains_open"]["qa_su3_packet_closed"] is False, cert),
        check("no target fitting", cert["target_fitting_used"] is False and data["target_fitting_used"] is False, cert),
        check("note records next artifact", cert["next_required_artifact"] in note and "conditional" in note.lower(), NOTE),
    ]
    print("\nSelected Qa/SU3 complex-rotated c-twist normalization audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
