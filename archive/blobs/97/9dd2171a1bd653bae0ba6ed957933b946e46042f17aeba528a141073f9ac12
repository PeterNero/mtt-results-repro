"""Check whether one selected S3 active quotient pulls back to full V_alpha.

The previous finite lemma showed blockwise compatibility.  This script tests
the stronger statement needed for source identification: can the single
selected S3 F3^2 commutator pull back along any map F3^4 -> F3^2 to the full
four-generator V_alpha mod-3 alternating form?

It cannot: rank(Q^T J Q) <= 2, while the full V_alpha active form has rank 4.
"""

from __future__ import annotations

import itertools
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CANDIDATES = ROOT / "candidate_data"
CERTS = ROOT / "certificates"

S3_COMPAT = CERTS / "valpha_s3_mod3_cocycle_compatibility_certificate.json"
VALPHA_PACKET = CANDIDATES / "visible_rank2_l2_ordered_source.monad_difference_candidate.json"
OUT_CANDIDATE = CANDIDATES / "valpha_s3_full_mod3_pullback_obstruction.candidate.json"
OUT_CERT = CERTS / "valpha_s3_full_mod3_pullback_obstruction_certificate.json"

MOD = 3


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def matmul(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    rows = len(a)
    cols = len(b[0])
    inner = len(b)
    return [
        [sum(a[i][k] * b[k][j] for k in range(inner)) % MOD for j in range(cols)]
        for i in range(rows)
    ]


def transpose(a: list[list[int]]) -> list[list[int]]:
    return [list(row) for row in zip(*a)]


def rank_mod3(matrix: list[list[int]]) -> int:
    rows = [row[:] for row in matrix]
    if not rows:
        return 0
    m = len(rows)
    n = len(rows[0])
    rank = 0
    pivot_col = 0
    while rank < m and pivot_col < n:
        pivot = None
        for r in range(rank, m):
            if rows[r][pivot_col] % MOD:
                pivot = r
                break
        if pivot is None:
            pivot_col += 1
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inv = 1 if rows[rank][pivot_col] == 1 else 2
        rows[rank] = [(inv * value) % MOD for value in rows[rank]]
        for r in range(m):
            if r != rank and rows[r][pivot_col] % MOD:
                factor = rows[r][pivot_col]
                rows[r] = [
                    (rows[r][c] - factor * rows[rank][c]) % MOD for c in range(n)
                ]
        rank += 1
        pivot_col += 1
    return rank


def pullback(j: list[list[int]], q: list[list[int]]) -> list[list[int]]:
    # q is 2 x 4 and maps F3^4 -> F3^2.  Pullback form is Q^T J Q.
    return matmul(matmul(transpose(q), j), q)


def main() -> int:
    compat = load(S3_COMPAT)
    valpha = load(VALPHA_PACKET)
    s3_commutator = compat["s3_finite_pullback"]["commutator_matrix_B_minus_BT_mod3"]
    full = [
        [value % MOD for value in row[:4]]
        for row in valpha["target"]["c1_deck_matrix_order_g1_to_g6"][:4]
    ]

    matching_maps: list[list[list[int]]] = []
    max_pullback_rank = 0
    rank_histogram: dict[str, int] = {}
    for values in itertools.product(range(MOD), repeat=8):
        q = [list(values[:4]), list(values[4:])]
        q_rank = rank_mod3(q)
        pb = pullback(s3_commutator, q)
        pb_rank = rank_mod3(pb)
        max_pullback_rank = max(max_pullback_rank, pb_rank)
        rank_histogram[str(pb_rank)] = rank_histogram.get(str(pb_rank), 0) + 1
        if pb == full:
            matching_maps.append(q)

    blockwise = compat["compatibility"]
    report = {
        "calculation": "VAlphaS3FullMod3PullbackObstruction",
        "status": "VALPHA_S3_FULL_MOD3_PULLBACK_OBSTRUCTED_RANK_MISMATCH",
        "inputs": {
            "blockwise_compatibility": str(S3_COMPAT.relative_to(ROOT)),
            "valpha_ordered_source_candidate": str(VALPHA_PACKET.relative_to(ROOT)),
        },
        "forms": {
            "s3_commutator_matrix_F3_rank": rank_mod3(s3_commutator),
            "s3_commutator_matrix": s3_commutator,
            "full_valpha_active_matrix_F3_rank": rank_mod3(full),
            "full_valpha_active_matrix_g1_to_g4": full,
            "rank_bound_for_single_s3_pullback": 2,
        },
        "bruteforce": {
            "maps_tested": MOD**8,
            "matching_maps": len(matching_maps),
            "max_pullback_rank_observed": max_pullback_rank,
            "pullback_rank_histogram": rank_histogram,
        },
        "blockwise_compatibility_retained": {
            "s3_matches_each_valpha_block_up_to_GL2": blockwise[
                "s3_commutator_gl2_equivalent_to_valpha_g1g2"
            ]
            and blockwise["s3_commutator_gl2_equivalent_to_valpha_g3g4"],
            "gl2_transform_count_per_block": blockwise["gl2_transform_count_g1g2"],
        },
        "what_this_closes": {
            "single_s3_active_quotient_cannot_be_full_valpha_mod3_source": True,
            "blockwise_compatibility_does_not_promote_to_full_pullback": True,
            "need_extra_integral_or_second_block_data": True,
        },
        "what_this_does_not_close": {
            "same_source_valpha_s3_binding": False,
            "integral_ordered_L3_K2_source_selection": False,
            "Pic0_selection_or_quotient": False,
            "selected_D_E_dotD_Riesz_Green": False,
            "full_SM_closure": False,
        },
        "guardrails": {
            "claims_s3_is_full_valpha_source": False,
            "claims_same_source_binding": False,
            "claims_selected_valpha_source": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "The selected S3 quotient is compatible with each V_alpha block "
                "separately, but a single F3^2 S3 commutator cannot pull back to "
                "the full four-generator V_alpha mod-3 form. The obstruction is "
                "rank: the S3 pullback has rank at most 2, while V_alpha has rank 4."
            ),
            "next_action": (
                "The same-source theorem must add extra integral/two-block data "
                "or a physical quotient that explains how the second V_alpha block "
                "is supplied beyond the single active S3 qutrit quotient."
            ),
        },
    }

    write(OUT_CANDIDATE, report)
    cert = {
        "certificate": "VAlphaS3FullMod3PullbackObstruction",
        "status": report["status"],
        "analysis_script": "scripts/compute_valpha_s3_full_mod3_pullback_obstruction.py",
        "candidate_data": str(OUT_CANDIDATE.relative_to(ROOT)),
        "forms": report["forms"],
        "bruteforce": report["bruteforce"],
        "blockwise_compatibility_retained": report["blockwise_compatibility_retained"],
        "what_this_closes": report["what_this_closes"],
        "what_this_does_not_close": report["what_this_does_not_close"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    write(OUT_CERT, cert)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
