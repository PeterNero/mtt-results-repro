"""Audit finite mod-3 V_alpha/S3 cocycle compatibility."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "valpha_s3_mod3_cocycle_compatibility_certificate.json"
CANDIDATE = REPO / "candidate_data" / "valpha_s3_mod3_cocycle_compatibility.candidate.json"
NOTE = REPO / "proof_corpus" / "VAlpha_S3_Mod3_Cocycle_Compatibility_Lemma_v1.md"
SCRIPT = REPO / "scripts" / "compute_valpha_s3_mod3_cocycle_compatibility.py"


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

    compat = cert["compatibility"]
    closes = cert["what_this_closes"]
    not_closed = cert["what_this_does_not_close"]
    guardrails = cert["guardrails"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "VALPHA_S3_MOD3_COCYCLE_COMPATIBLE_SELECTION_OPEN",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["compatibility"] == compat
            and computed["s3_finite_pullback"] == cert["s3_finite_pullback"],
            computed["status"],
        ),
        check(
            "S3 table has unique bilinear form",
            cert["s3_finite_pullback"]["entry_count"] == 81
            and cert["s3_finite_pullback"]["bilinear_matrix_B_left_right_mod3"]
            == [[0, 0], [2, 0]],
            cert["s3_finite_pullback"],
        ),
        check(
            "commutator is nondegenerate",
            cert["s3_finite_pullback"]["commutator_matrix_B_minus_BT_mod3"]
            == [[0, 1], [2, 0]]
            and cert["s3_finite_pullback"]["commutator_determinant_mod3"] == 1,
            cert["s3_finite_pullback"],
        ),
        check(
            "V_alpha mod3 blocks match each other",
            cert["valpha_mod3_blocks"]["block_g1g2_mod3"]
            == cert["valpha_mod3_blocks"]["block_g3g4_mod3"]
            == [[0, 2], [1, 0]],
            cert["valpha_mod3_blocks"],
        ),
        check(
            "finite compatibility holds up to GL2",
            compat["s3_commutator_gl2_equivalent_to_valpha_g1g2"] is True
            and compat["s3_commutator_gl2_equivalent_to_valpha_g3g4"] is True
            and compat["gl2_transform_count_g1g2"] == 24,
            compat,
        ),
        check(
            "not overpromoted",
            closes["finite_active_qutrit_quotient_compatible_with_valpha_blocks"] is True
            and not_closed["same_source_valpha_s3_binding"] is False
            and not_closed["Pic0_selection_or_quotient"] is False,
            not_closed,
        ),
        check(
            "guardrails",
            guardrails["claims_selected_valpha_source"] is False
            and guardrails["claims_same_source_binding"] is False
            and guardrails["claims_pic0_resolved"] is False,
            guardrails,
        ),
        check(
            "note records finite-only nature",
            "finite quotient compatibility lemma" in note
            and "does not select the integral source" in note
            and "Pic0" in note,
            NOTE,
        ),
        check(
            "candidate matches certificate",
            candidate["status"] == cert["status"]
            and candidate["compatibility"] == cert["compatibility"],
            candidate["status"],
        ),
    ]

    print("\nV_alpha/S3 mod-3 cocycle compatibility audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
