"""Filter C6 orientation branches by common quark/lepton holonomy origin.

The no-proxy flavor notes state that quark and lepton phases may not be assigned
independently when they come from the same pairwise bundle structure.  Applied
to the qutrit C6 branch reduction, this rejects the mixed Q/L orientation
branches and leaves one global conjugate pair.

This does not choose between the two conjugate conventions; it removes the
independent quark-vs-lepton C6 orientation knob.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]


def run_branch_reduction() -> dict[str, Any]:
    proc = subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "analyze_iwasawa_c6_orientation_branch_reduction.py"),
        ],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stdout)
    return json.loads(proc.stdout)


def analyze() -> dict[str, Any]:
    reduction = run_branch_reduction()
    branches = reduction["branches"]
    common_holonomy_branches = [
        branch for branch in branches if branch["quark_lepton_doublet_orientations_match"]
    ]
    rejected = [
        branch for branch in branches if not branch["quark_lepton_doublet_orientations_match"]
    ]
    label_patterns = [
        [
            branch["channel_c6_labels_left_representative"][channel]
            for channel in ("u:C6", "d:C6", "e:C6", "nuD:C6")
        ]
        for branch in common_holonomy_branches
    ]

    return {
        "calculation": "IwasawaC6CommonHolonomyBranchPair",
        "source_principle": "quark and lepton phases may not be assigned independently when they come from the same pairwise bundle structure",
        "input_branch_count": len(branches),
        "common_holonomy_branch_count": len(common_holonomy_branches),
        "rejected_mixed_quark_lepton_branch_count": len(rejected),
        "common_holonomy_branch_names": [
            branch["name"] for branch in common_holonomy_branches
        ],
        "rejected_mixed_branch_names": [branch["name"] for branch in rejected],
        "common_holonomy_label_patterns": label_patterns,
        "global_conjugate_pair": [
            branch["name"] for branch in common_holonomy_branches
        ],
        "global_conjugate_label_patterns": label_patterns,
        "closed_reduction": {
            "mixed_quark_lepton_C6_orientation_patterns_rejected": True,
            "C6_orientation_reduced_to_global_conjugate_pair": True,
            "independent_quark_vs_lepton_phase_knob_removed": True,
        },
        "still_open": {
            "which_global_conjugate_convention_is_selected": True,
            "left_representative_versus_conjugate_channel_convention": True,
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
