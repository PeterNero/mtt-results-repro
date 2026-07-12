"""Audit the q79/q369 finite orientation observable-parity ledger."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "orientation_observable_parity_certificate.json"
CANDIDATE = REPO / "candidate_data" / "orientation_observable_parity.candidate.json"
NOTE = REPO / "proof_corpus" / "Orientation_Observable_Parity_v1.md"
SCRIPT = REPO / "scripts" / "derive_orientation_observable_parity.py"


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
    candidate = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    computed = run_script()
    note = NOTE.read_text(encoding="utf-8")

    finite = cert["finite_operator_parity"]
    even = finite["cp_even_norm_invariants"]
    odd = finite["complex_conjugation_invariants"]
    guardrails = cert["guardrails"]
    yukawa = cert["conditional_yukawa_extension"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "ORIENTATION_OBSERVABLE_PARITY_CLOSED_YUKAWA_VALUES_OPEN",
            cert["status"],
        ),
        check(
            "script recomputes certificate",
            computed["finite_operator_parity"] == cert["finite_operator_parity"]
            and computed["conditional_yukawa_extension"] == cert["conditional_yukawa_extension"],
            computed["finite_operator_parity"],
        ),
        check(
            "cp-even finite norms invariant",
            even["checks"] == 133
            and even["failures"] == 0
            and even["max_abs_error"] == 0.0,
            even,
        ),
        check(
            "complex conjugation parity",
            odd["checks"] == 329
            and odd["failures"] == 0
            and odd["max_abs_error"] < 1e-12
            and odd["nonzero_imaginary_sign_flips"] == 21,
            odd,
        ),
        check(
            "file coverage",
            finite["files"]["de_action.candidate.json"]["cp_even_norm_checks"] == 35
            and finite["files"]["reduced_green.candidate.json"]["cp_even_norm_checks"] == 35
            and finite["files"]["dotd_response.candidate.json"]["cp_even_norm_checks"] == 63,
            finite["files"],
        ),
        check(
            "conditional Yukawa rule is guarded",
            yukawa["current_selected_yukawa_matrices_absent"] is True
            and yukawa["not_a_mass_or_ckm_magnitude_calculation"] is True
            and yukawa["if_selected_yukawa_pair_is_antiunitary_conjugate"][
                "singular_values_equal"
            ]
            is True
            and yukawa["if_selected_yukawa_pair_is_antiunitary_conjugate"][
                "jarlskog_and_other_cp_odd_signs_reverse"
            ]
            is True,
            yukawa,
        ),
        check(
            "no overclaim",
            guardrails["claims_observed_cp_sign_selects_branch"] is False
            and guardrails["uses_observed_masses_or_mixings"] is False
            and guardrails["claims_selected_yukawas_computed"] is False
            and guardrails["claims_full_sm_closure"] is False,
            guardrails,
        ),
        check(
            "note records parity without values",
            "CP-even norm checks" in note
            and "nonzero imaginary sign flips" in note
            and "does not compute selected Yukawa matrices" in note
            and "selected source or retarded boundary theorem" in note,
            NOTE,
        ),
        check(
            "candidate matches certificate",
            candidate["finite_operator_parity"] == cert["finite_operator_parity"]
            and candidate["verdict"] == cert["verdict"],
            candidate["status"],
        ),
    ]

    print("\nOrientation observable parity audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
