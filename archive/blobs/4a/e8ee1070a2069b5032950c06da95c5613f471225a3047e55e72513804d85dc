"""Analyze pure qutrit/C6 finite support for CKM heavy links.

The block-factorized packet uses a nontrivial qutrit family block and a trivial
Higgs line.  The finite coupling rule already says that nontrivial matter pairs
must be conjugate: 1+2 or 2+1.  This script computes the corresponding finite
invariant bilinear support matrices.

Result: for the conjugate pairs, the finite invariant support is diagonal in
the qutrit family basis.  Therefore the pure finite qutrit/C6 support has zero
heavy-link entries (13,23).  Any nonzero CKM leading heavy link must come from
selected differential response, selected non-invariant basis transport, or an
additional selected support operator beyond the pure finite invariant pairing.
"""

from __future__ import annotations

import json
from typing import Any


MOD = 3
HEAVY_LINK_POSITIONS = ((0, 2), (1, 2))


def add_mod(left: int, right: int) -> int:
    return (left + right) % MOD


def invariant_support(left_twist: int, right_twist: int) -> list[list[int]]:
    """Return a 0/1 support matrix allowed by finite qutrit invariance.

    For a bilinear support matrix M_ij, the diagonal shift constraint makes the
    support depend only on i-j mod 3.  The clock constraint permits M_ij only if
    left_twist*i + right_twist*j = 0 mod 3.
    """

    support = [[0 for _ in range(MOD)] for _ in range(MOD)]
    for row in range(MOD):
        for col in range(MOD):
            if add_mod(left_twist * row, right_twist * col) == 0:
                support[row][col] = 1

    # Apply the common shift-orbit rule: if one entry in an orbit is allowed,
    # the whole orbit must be allowed; otherwise that orbit is forbidden.
    # This leaves exactly diagonal support for conjugate nontrivial pairs and
    # three circulant supports for 0+0.
    orbit_support = [[0 for _ in range(MOD)] for _ in range(MOD)]
    visited: set[tuple[int, int]] = set()
    for row in range(MOD):
        for col in range(MOD):
            if (row, col) in visited:
                continue
            orbit = [((row + shift) % MOD, (col + shift) % MOD) for shift in range(MOD)]
            visited.update(orbit)
            if all(support[i][j] == 1 for i, j in orbit):
                for i, j in orbit:
                    orbit_support[i][j] = 1
    return orbit_support


def fixed_dimension(support: list[list[int]]) -> int:
    # Each common-shift orbit contributes one invariant coefficient.
    seen: set[tuple[int, int]] = set()
    dimension = 0
    for row in range(MOD):
        for col in range(MOD):
            if support[row][col] == 0 or (row, col) in seen:
                continue
            orbit = [((row + shift) % MOD, (col + shift) % MOD) for shift in range(MOD)]
            seen.update(orbit)
            dimension += 1
    return dimension


def heavy_link_vector(support: list[list[int]]) -> list[int]:
    return [support[row][col] for row, col in HEAVY_LINK_POSITIONS]


def support_kind(support: list[list[int]]) -> str:
    if support == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]:
        return "diagonal_identity_support"
    if support == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]:
        return "blocked_zero_support"
    return "circulant_or_mixed_support"


def analyze_pair(left_twist: int, right_twist: int) -> dict[str, Any]:
    support = invariant_support(left_twist, right_twist)
    heavy = heavy_link_vector(support)
    return {
        "orientation": f"{left_twist}+{right_twist}",
        "left_twist": left_twist,
        "right_twist": right_twist,
        "orientation_sum_mod3": add_mod(left_twist, right_twist),
        "support_matrix": support,
        "support_kind": support_kind(support),
        "fixed_dimension": fixed_dimension(support),
        "heavy_link_entries_13_23": heavy,
        "has_heavy_link_support": any(value != 0 for value in heavy),
    }


def analyze() -> dict[str, Any]:
    pairs = {
        f"{left}+{right}": analyze_pair(left, right)
        for left in range(MOD)
        for right in range(MOD)
    }
    conjugate_pairs = {key: pairs[key] for key in ("1+2", "2+1")}
    trivial_pair = pairs["0+0"]
    nontrivial_blocked = {
        key: value
        for key, value in pairs.items()
        if key not in ("0+0", "1+2", "2+1")
    }

    return {
        "calculation": "QutritC6PureHeavyLinkSupport",
        "setup": {
            "family_basis": "qutrit basis e1,e2,e3, identified with rows/columns 1,2,3",
            "heavy_link_entries": "matrix entries (1,3) and (2,3)",
            "trivial_higgs_line": True,
            "nontrivial_sm_pair_rule": "left_twist + right_twist = 0 mod 3",
        },
        "all_pair_supports": pairs,
        "conjugate_pair_supports": conjugate_pairs,
        "trivial_pair_support": trivial_pair,
        "blocked_nontrivial_pair_supports": nontrivial_blocked,
        "pure_c6_consequence": {
            "conjugate_pair_support_is_diagonal": all(
                item["support_kind"] == "diagonal_identity_support"
                for item in conjugate_pairs.values()
            ),
            "conjugate_pair_heavy_links_zero": all(
                item["heavy_link_entries_13_23"] == [0, 0]
                for item in conjugate_pairs.values()
            ),
            "pure_finite_qutrit_C6_delta_c": [0, 0],
            "pure_finite_qutrit_C6_can_close_leading_CKM_gate": False,
        },
        "not_ruled_out": {
            "selected_differential_response": True,
            "selected_noninvariant_basis_transport": True,
            "selected_C6_support_operator_beyond_pure_finite_pairing": True,
            "character_trivial_C1_or_other_channel_heavy_links": True,
        },
        "guardrails": {
            "claims_selected_C6_amplitudes_computed": False,
            "claims_selected_heavy_link_packet_filled": False,
            "claims_Delta_v_computed": False,
            "claims_full_SM_closure": False,
        },
        "verdict": {
            "pure_finite_qutrit_C6_heavy_link_obstructed": True,
            "c6_only_route_retired_for_leading_heavy_links": True,
            "next_source_for_heavy_links": (
                "selected differential response/basis transport, especially "
                "C1 primitive contractions or selected non-invariant Galerkin data"
            ),
        },
    }


def main() -> int:
    print(json.dumps(analyze(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
