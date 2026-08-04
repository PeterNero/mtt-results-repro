"""Audit the finite two-block S3 lift of the full V_alpha mod-3 form."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "valpha_s3_two_block_mod3_lift_certificate.json"
CANDIDATE = REPO / "candidate_data" / "valpha_s3_two_block_mod3_lift.candidate.json"
NOTE = REPO / "proof_corpus" / "VAlpha_S3_Two_Block_Mod3_Lift_v1.md"
SCRIPT = REPO / "scripts" / "compute_valpha_s3_two_block_mod3_lift.py"


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

    construction = cert["construction"]
    source = cert["source"]
    target = cert["target"]
    minimality = cert["minimality"]
    guardrails = cert["guardrails"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "VALPHA_S3_TWO_BLOCK_MOD3_LIFT_CONSTRUCTED_SELECTION_OPEN",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["construction"] == construction
            and computed["minimality"] == minimality,
            computed["status"],
        ),
        check(
            "two-block rank matches V_alpha",
            source["two_block_source_rank"] == 4
            and target["full_valpha_active_rank"] == 4,
            {"source": source["two_block_source_rank"], "target": target["full_valpha_active_rank"]},
        ),
        check(
            "explicit lift equals target",
            construction["lifted_equals_full_valpha"] is True
            and construction["lifted_form"]
            == target["full_valpha_active_matrix_g1_to_g4"],
            construction["lifted_form"],
        ),
        check(
            "one-block obstruction imported",
            minimality["one_block_status"]
            == "VALPHA_S3_FULL_MOD3_PULLBACK_OBSTRUCTED_RANK_MISMATCH"
            and minimality["one_block_max_pullback_rank"] == 2
            and minimality["finite_active_blocks_required_by_rank"] == 2,
            minimality,
        ),
        check(
            "blockwise transform multiplicity",
            construction["blockwise_transform_count_lower_bound"] == 576,
            construction["blockwise_transform_count_lower_bound"],
        ),
        check(
            "guardrails",
            guardrails["claims_two_blocks_are_selected"] is False
            and guardrails["claims_integral_source_selected"] is False
            and guardrails["claims_same_source_binding"] is False,
            guardrails,
        ),
        check(
            "note records exact finite repair",
            "two independent S3-active blocks" in note
            and "does not select" in note
            and "exactly recovers the full V_alpha mod-3 form" in note,
            NOTE,
        ),
        check(
            "candidate matches certificate",
            candidate["status"] == cert["status"]
            and candidate["construction"] == cert["construction"],
            candidate["status"],
        ),
    ]

    print("\nV_alpha/S3 two-block mod-3 lift audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
