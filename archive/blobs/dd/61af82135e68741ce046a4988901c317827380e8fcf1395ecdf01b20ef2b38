"""Reduce C6 q79 orientation choices using the qutrit pairing rule.

Before the block-coupling calculation, the C6 holonomy labels 79 and 369 were
open independently in each SM channel.  The finite qutrit rule imposes

    s_left + s_right = 0 mod 3

for a trivial Higgs line.  This script enumerates all nontrivial sector
orientation assignments satisfying the four SM Yukawa pair constraints, then
maps sector orientations to q79/conjugate C6 labels.

It closes a reduction of the sign space, not a unique MTT-selected branch.
"""

from __future__ import annotations

import json
from itertools import product
from typing import Any


Q_LABEL = 79
Q_INV_LABEL = 369
MODULUS = 448
SECTORS = ("Q", "u", "d", "L", "e", "N")
CHANNEL_PAIRS = {
    "u:C6": ("Q", "u"),
    "d:C6": ("Q", "d"),
    "e:C6": ("L", "e"),
    "nuD:C6": ("L", "N"),
}


def orientation_label(orientation: int) -> int:
    if orientation == 1:
        return Q_LABEL
    if orientation == 2:
        return Q_INV_LABEL
    raise ValueError(f"unsupported orientation {orientation}")


def pair_allowed(left: int, right: int) -> bool:
    return (left + right) % 3 == 0


def branch_channel_labels(assignments: dict[str, int]) -> dict[str, int]:
    """Use the left matter block as the oriented C6 channel representative."""

    return {
        channel: orientation_label(assignments[left])
        for channel, (left, _right) in CHANNEL_PAIRS.items()
    }


def enumerate_branches() -> list[dict[str, Any]]:
    branches = []
    for values in product((1, 2), repeat=len(SECTORS)):
        assignments = dict(zip(SECTORS, values))
        if not all(
            pair_allowed(assignments[left], assignments[right])
            for left, right in CHANNEL_PAIRS.values()
        ):
            continue
        quark_orientation = assignments["Q"]
        lepton_orientation = assignments["L"]
        labels = branch_channel_labels(assignments)
        branches.append(
            {
                "name": (
                    f"Q{quark_orientation}_L{lepton_orientation}_"
                    f"R{3 - quark_orientation}_E{3 - lepton_orientation}"
                ),
                "sector_orientations": assignments,
                "channel_c6_labels_left_representative": labels,
                "conjugate_channel_c6_labels": {
                    channel: (Q_INV_LABEL if label == Q_LABEL else Q_LABEL)
                    for channel, label in labels.items()
                },
                "all_four_pairings_allowed": True,
                "quark_lepton_doublet_orientations_match": quark_orientation
                == lepton_orientation,
            }
        )
    return branches


def analyze() -> dict[str, Any]:
    branches = enumerate_branches()
    independent_before = 2 ** len(CHANNEL_PAIRS)
    branch_names = [branch["name"] for branch in branches]
    electroweak_doublet_coherent = [
        branch for branch in branches if branch["quark_lepton_doublet_orientations_match"]
    ]
    left_representative_label_patterns = sorted(
        {
            tuple(branch["channel_c6_labels_left_representative"][channel] for channel in CHANNEL_PAIRS)
            for branch in branches
        }
    )
    coherent_label_patterns = sorted(
        {
            tuple(branch["channel_c6_labels_left_representative"][channel] for channel in CHANNEL_PAIRS)
            for branch in electroweak_doublet_coherent
        }
    )

    return {
        "calculation": "IwasawaC6OrientationBranchReduction",
        "modulus": MODULUS,
        "q_label": Q_LABEL,
        "q_inverse_label": Q_INV_LABEL,
        "input_open_independent_C6_sign_choices": independent_before,
        "finite_pairing_rule": "s_left+s_right=0 mod 3",
        "branches": branches,
        "branch_count_after_qutrit_pairing_rule": len(branches),
        "branch_names": branch_names,
        "left_representative_label_patterns": [
            list(pattern) for pattern in left_representative_label_patterns
        ],
        "left_representative_label_pattern_count": len(left_representative_label_patterns),
        "electroweak_doublet_coherent_subbranches": electroweak_doublet_coherent,
        "electroweak_doublet_coherent_branch_count": len(electroweak_doublet_coherent),
        "electroweak_doublet_coherent_label_patterns": [
            list(pattern) for pattern in coherent_label_patterns
        ],
        "global_conjugation_pairs": [
            ["Q1_L1_R2_E2", "Q2_L2_R1_E1"],
            ["Q1_L2_R2_E1", "Q2_L1_R1_E2"],
        ],
        "closed_reduction": {
            "independent_channel_signs_removed": True,
            "four_independent_channel_choices_reduced_to_sector_orientation_branches": True,
            "electroweak_doublet_coherence_reduces_to_global_conjugate_pair": True,
        },
        "still_open": {
            "unique_MTT_branch_among_global_conjugates": True,
            "whether_Q_and_L_doublet_orientations_must_match": True,
            "C6_amplitudes_nonzero_status": True,
            "C6_prefactors": True,
            "Yukawa_magnitudes": True,
        },
    }


def main() -> int:
    print(json.dumps(analyze(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
