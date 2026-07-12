"""Construct the finite two-block S3 lift of the full V_alpha mod-3 form.

The one-block obstruction proves that a single selected S3 active quotient
cannot be the full four-generator V_alpha mod-3 source.  This companion
calculation shows the exact finite repair: two independent copies of the
selected S3 commutator, transformed blockwise by the already-audited GL(2,F3)
map, reproduce the full active V_alpha form.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CANDIDATES = ROOT / "candidate_data"
CERTS = ROOT / "certificates"

S3_COMPAT = CERTS / "valpha_s3_mod3_cocycle_compatibility_certificate.json"
ONE_BLOCK_OBSTRUCTION = (
    CERTS / "valpha_s3_full_mod3_pullback_obstruction_certificate.json"
)
VALPHA_PACKET = CANDIDATES / "visible_rank2_l2_ordered_source.monad_difference_candidate.json"
OUT_CANDIDATE = CANDIDATES / "valpha_s3_two_block_mod3_lift.candidate.json"
OUT_CERT = CERTS / "valpha_s3_two_block_mod3_lift_certificate.json"

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


def block_diag(*blocks: list[list[int]]) -> list[list[int]]:
    size = sum(len(block) for block in blocks)
    out = [[0 for _ in range(size)] for _ in range(size)]
    offset = 0
    for block in blocks:
        for i, row in enumerate(block):
            for j, value in enumerate(row):
                out[offset + i][offset + j] = value % MOD
        offset += len(block)
    return out


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


def pullback(form: list[list[int]], q: list[list[int]]) -> list[list[int]]:
    return matmul(matmul(transpose(q), form), q)


def main() -> int:
    compat = load(S3_COMPAT)
    obstruction = load(ONE_BLOCK_OBSTRUCTION)
    valpha = load(VALPHA_PACKET)

    s3_commutator = compat["s3_finite_pullback"]["commutator_matrix_B_minus_BT_mod3"]
    transform = compat["compatibility"]["example_transform_to_g1g2"]
    full_valpha = [
        [value % MOD for value in row[:4]]
        for row in valpha["target"]["c1_deck_matrix_order_g1_to_g6"][:4]
    ]

    two_block_source = block_diag(s3_commutator, s3_commutator)
    block_transform = block_diag(transform, transform)
    lifted = pullback(two_block_source, block_transform)
    blockwise_transform_count = (
        compat["compatibility"]["gl2_transform_count_g1g2"]
        * compat["compatibility"]["gl2_transform_count_g3g4"]
    )

    report = {
        "calculation": "VAlphaS3TwoBlockMod3Lift",
        "status": "VALPHA_S3_TWO_BLOCK_MOD3_LIFT_CONSTRUCTED_SELECTION_OPEN",
        "inputs": {
            "blockwise_compatibility": str(S3_COMPAT.relative_to(ROOT)),
            "one_block_obstruction": str(ONE_BLOCK_OBSTRUCTION.relative_to(ROOT)),
            "valpha_ordered_source_candidate": str(VALPHA_PACKET.relative_to(ROOT)),
        },
        "source": {
            "two_block_source_form": two_block_source,
            "two_block_source_rank": rank_mod3(two_block_source),
            "interpretation": "S3_active_block_1_direct_sum_S3_active_block_2",
        },
        "target": {
            "full_valpha_active_matrix_g1_to_g4": full_valpha,
            "full_valpha_active_rank": rank_mod3(full_valpha),
        },
        "construction": {
            "single_block_transform_from_existing_certificate": transform,
            "block_diagonal_transform": block_transform,
            "lifted_form": lifted,
            "lifted_equals_full_valpha": lifted == full_valpha,
            "blockwise_transform_count_lower_bound": blockwise_transform_count,
        },
        "minimality": {
            "one_block_status": obstruction["status"],
            "one_block_max_pullback_rank": obstruction["bruteforce"][
                "max_pullback_rank_observed"
            ],
            "two_block_rank_matches_target_rank": rank_mod3(two_block_source)
            == rank_mod3(full_valpha),
            "finite_active_blocks_required_by_rank": 2,
        },
        "what_this_closes": {
            "finite_two_block_repair_constructed": lifted == full_valpha,
            "minimal_f3_active_rank_requirement_identified": True,
            "one_s3_block_replaced_by_two_block_requirement": True,
        },
        "what_this_does_not_close": {
            "two_blocks_are_selected_by_MTT": False,
            "integral_ordered_L3_K2_source_selection": False,
            "Pic0_selection_or_quotient": False,
            "same_source_valpha_s3_binding": False,
            "selected_D_E_dotD_Riesz_Green": False,
            "full_SM_closure": False,
        },
        "guardrails": {
            "claims_two_blocks_are_selected": False,
            "claims_integral_source_selected": False,
            "claims_same_source_binding": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "The finite mod-3 repair is exact: two independent selected-S3-type "
                "active blocks, transformed by the existing GL(2,F3) block map, "
                "recover the full four-generator V_alpha form. This is a finite "
                "construction, not a selection theorem."
            ),
            "next_action": (
                "Search the corpus/operator data for the selected geometric origin "
                "of the second active block: integral two-block lift, doubled S3 "
                "support, or a physical quotient theorem."
            ),
        },
    }

    write(OUT_CANDIDATE, report)
    cert = {
        "certificate": "VAlphaS3TwoBlockMod3Lift",
        "status": report["status"],
        "analysis_script": "scripts/compute_valpha_s3_two_block_mod3_lift.py",
        "candidate_data": str(OUT_CANDIDATE.relative_to(ROOT)),
        "source": report["source"],
        "target": report["target"],
        "construction": report["construction"],
        "minimality": report["minimality"],
        "what_this_closes": report["what_this_closes"],
        "what_this_does_not_close": report["what_this_does_not_close"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    write(OUT_CERT, cert)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if lifted == full_valpha else 1


if __name__ == "__main__":
    raise SystemExit(main())
