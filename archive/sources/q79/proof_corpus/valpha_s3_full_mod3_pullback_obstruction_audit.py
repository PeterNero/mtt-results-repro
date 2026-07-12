"""Audit the full mod-3 pullback obstruction from S3 to V_alpha."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "valpha_s3_full_mod3_pullback_obstruction_certificate.json"
CANDIDATE = REPO / "candidate_data" / "valpha_s3_full_mod3_pullback_obstruction.candidate.json"
NOTE = REPO / "proof_corpus" / "VAlpha_S3_Full_Mod3_Pullback_Obstruction_v1.md"
SCRIPT = REPO / "scripts" / "compute_valpha_s3_full_mod3_pullback_obstruction.py"


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

    forms = cert["forms"]
    brute = cert["bruteforce"]
    closes = cert["what_this_closes"]
    guardrails = cert["guardrails"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "VALPHA_S3_FULL_MOD3_PULLBACK_OBSTRUCTED_RANK_MISMATCH",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["forms"] == forms and computed["bruteforce"] == brute,
            computed["status"],
        ),
        check(
            "rank mismatch",
            forms["s3_commutator_matrix_F3_rank"] == 2
            and forms["full_valpha_active_matrix_F3_rank"] == 4
            and forms["rank_bound_for_single_s3_pullback"] == 2,
            forms,
        ),
        check(
            "bruteforce confirms no map",
            brute["maps_tested"] == 6561
            and brute["matching_maps"] == 0
            and brute["max_pullback_rank_observed"] == 2,
            brute,
        ),
        check(
            "blockwise compatibility retained",
            cert["blockwise_compatibility_retained"][
                "s3_matches_each_valpha_block_up_to_GL2"
            ]
            is True,
            cert["blockwise_compatibility_retained"],
        ),
        check(
            "correct closure",
            closes["single_s3_active_quotient_cannot_be_full_valpha_mod3_source"]
            is True
            and closes["need_extra_integral_or_second_block_data"] is True,
            closes,
        ),
        check(
            "guardrails",
            guardrails["claims_s3_is_full_valpha_source"] is False
            and guardrails["claims_same_source_binding"] is False,
            guardrails,
        ),
        check(
            "note records obstruction",
            "rank mismatch" in note
            and "blockwise compatibility remains true" in note
            and "cannot be the full V_alpha source" in note,
            NOTE,
        ),
        check(
            "candidate matches certificate",
            candidate["status"] == cert["status"]
            and candidate["forms"] == cert["forms"],
            candidate["status"],
        ),
    ]

    print("\nV_alpha/S3 full mod-3 pullback obstruction audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
