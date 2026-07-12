"""Compute finite mod-3 compatibility between V_alpha and selected S3 data.

This is deliberately only a finite quotient check.  It may show that the
selected S3 pullback cocycle is compatible with the mod-3 reduction of the
V_alpha Appell-Humbert block, but it cannot by itself select the integral
terminal-monad source, Pic0 representative, or operator data.
"""

from __future__ import annotations

import itertools
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CANDIDATES = ROOT / "candidate_data"
CERTS = ROOT / "certificates"

S3_PACKET = CERTS / "visible_twisted_s3_class_restriction_packet.selected.json"
VALPHA_PACKET = CANDIDATES / "visible_rank2_l2_ordered_source.monad_difference_candidate.json"
OUT_CANDIDATE = CANDIDATES / "valpha_s3_mod3_cocycle_compatibility.candidate.json"
OUT_CERT = CERTS / "valpha_s3_mod3_cocycle_compatibility_certificate.json"

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


def det2(a: list[list[int]]) -> int:
    return (a[0][0] * a[1][1] - a[0][1] * a[1][0]) % MOD


def sub(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [[(a[i][j] - b[i][j]) % MOD for j in range(len(a[0]))] for i in range(len(a))]


def infer_bilinear_matrix(entries: list[dict[str, Any]]) -> list[list[int]]:
    matches: list[list[list[int]]] = []
    for values in itertools.product(range(MOD), repeat=4):
        matrix = [[values[0], values[1]], [values[2], values[3]]]
        ok = True
        for entry in entries:
            left = entry["left"]
            right = entry["right"]
            expected = entry["numerator_mod_3"] % MOD
            predicted = (
                left[0] * (matrix[0][0] * right[0] + matrix[0][1] * right[1])
                + left[1] * (matrix[1][0] * right[0] + matrix[1][1] * right[1])
            ) % MOD
            if predicted != expected:
                ok = False
                break
        if ok:
            matches.append(matrix)
    if len(matches) != 1:
        raise ValueError(f"expected unique bilinear matrix, got {len(matches)}")
    return matches[0]


def gl2_equivalences(source: list[list[int]], target: list[list[int]]) -> list[list[list[int]]]:
    transforms: list[list[list[int]]] = []
    for values in itertools.product(range(MOD), repeat=4):
        p = [[values[0], values[1]], [values[2], values[3]]]
        if det2(p) == 0:
            continue
        transported = matmul(matmul(transpose(p), source), p)
        if transported == target:
            transforms.append(p)
    return transforms


def main() -> int:
    s3 = load(S3_PACKET)
    valpha = load(VALPHA_PACKET)
    entries = s3["explicit_S3_pullback_table"]["entries"]
    b_matrix = infer_bilinear_matrix(entries)
    s3_commutator = sub(b_matrix, transpose(b_matrix))

    target = valpha["target"]
    target_matrix = target["c1_deck_matrix_order_g1_to_g6"]
    valpha_block_12 = [
        [target_matrix[0][0] % MOD, target_matrix[0][1] % MOD],
        [target_matrix[1][0] % MOD, target_matrix[1][1] % MOD],
    ]
    valpha_block_34 = [
        [target_matrix[2][2] % MOD, target_matrix[2][3] % MOD],
        [target_matrix[3][2] % MOD, target_matrix[3][3] % MOD],
    ]

    transforms_12 = gl2_equivalences(s3_commutator, valpha_block_12)
    transforms_34 = gl2_equivalences(s3_commutator, valpha_block_34)
    direct_same_as_12 = s3_commutator == valpha_block_12
    direct_same_as_34 = s3_commutator == valpha_block_34

    report = {
        "calculation": "VAlphaS3Mod3CocycleCompatibility",
        "status": "VALPHA_S3_MOD3_COCYCLE_COMPATIBLE_SELECTION_OPEN",
        "inputs": {
            "selected_s3_packet": str(S3_PACKET.relative_to(ROOT)),
            "valpha_ordered_source_candidate": str(VALPHA_PACKET.relative_to(ROOT)),
        },
        "s3_finite_pullback": {
            "entry_count": len(entries),
            "active_quotient": s3["explicit_S3_pullback_table"]["active_quotient"],
            "bilinear_matrix_B_left_right_mod3": b_matrix,
            "commutator_matrix_B_minus_BT_mod3": s3_commutator,
            "commutator_determinant_mod3": det2(s3_commutator),
        },
        "valpha_mod3_blocks": {
            "selected_L": target["L"],
            "selected_L2": target["L2"],
            "block_g1g2_mod3": valpha_block_12,
            "block_g3g4_mod3": valpha_block_34,
            "blocks_equal_mod3": valpha_block_12 == valpha_block_34,
        },
        "compatibility": {
            "s3_commutator_gl2_equivalent_to_valpha_g1g2": bool(transforms_12),
            "s3_commutator_gl2_equivalent_to_valpha_g3g4": bool(transforms_34),
            "gl2_transform_count_g1g2": len(transforms_12),
            "gl2_transform_count_g3g4": len(transforms_34),
            "example_transform_to_g1g2": transforms_12[0] if transforms_12 else None,
            "direct_matrix_equality_g1g2": direct_same_as_12,
            "direct_matrix_equality_g3g4": direct_same_as_34,
        },
        "what_this_closes": {
            "selected_s3_pullback_table_is_bilinear": True,
            "selected_s3_commutator_is_nondegenerate_mod3": det2(s3_commutator) != 0,
            "finite_active_qutrit_quotient_compatible_with_valpha_blocks": bool(
                transforms_12 and transforms_34
            ),
        },
        "what_this_does_not_close": {
            "integral_ordered_L3_K2_source_selection": False,
            "base_factor_order_selection": False,
            "Pic0_selection_or_quotient": False,
            "same_source_valpha_s3_binding": False,
            "selected_D_E_dotD_Riesz_Green": False,
            "primitive_C1_contractions": False,
            "full_SM_closure": False,
        },
        "guardrails": {
            "claims_selected_valpha_source": False,
            "claims_same_source_binding": False,
            "claims_pic0_resolved": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "The selected S3 finite pullback cocycle is compatible with the "
                "mod-3 reduction of each V_alpha symplectic block up to GL(2,F3). "
                "This is a real finite quotient compatibility lemma, not a source "
                "selection theorem."
            ),
            "why_not_enough": (
                "The active S3 quotient is two-dimensional over F3 and cannot "
                "distinguish the two integral V_alpha blocks, select the ordered "
                "base factors, resolve Pic0, or emit smooth D_E/dotD data."
            ),
            "next_action": (
                "Lift this finite compatibility through typed Cech/Appell-Humbert "
                "transition data and prove the physical quotient from selected S3 "
                "support to the integral V_alpha source."
            ),
        },
    }
    write(OUT_CANDIDATE, report)
    cert = {
        "certificate": "VAlphaS3Mod3CocycleCompatibility",
        "status": report["status"],
        "analysis_script": "scripts/compute_valpha_s3_mod3_cocycle_compatibility.py",
        "candidate_data": str(OUT_CANDIDATE.relative_to(ROOT)),
        "s3_finite_pullback": report["s3_finite_pullback"],
        "valpha_mod3_blocks": report["valpha_mod3_blocks"],
        "compatibility": report["compatibility"],
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
