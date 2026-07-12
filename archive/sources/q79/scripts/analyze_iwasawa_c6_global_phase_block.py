"""Analyze the C6 global holonomy phase block after branch reduction.

The common-holonomy reduction leaves only a global conjugate pair:

    [79, 79, 79, 79] or [369, 369, 369, 369].

This script computes the resulting pure C6 phase block.  It closes the C6
orientation-sign freedom as a shared phase convention, but it does not compute
the C6 amplitudes, matrix supports, or Yukawa magnitudes.  A shared phase can
only affect physical CP observables through selected nonzero support matrices
that interfere with other channel blocks; it is not an entry-wise fitting knob.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PAIR_CERT = ROOT / "certificates" / "iwasawa_c6_common_holonomy_branch_pair_certificate.json"
FORCED_CERT = ROOT / "certificates" / "forced_channel_weight_blocks_certificate.json"
Z64_CERT = ROOT / "certificates" / "z64_exact_branch_certificate.json"
CHANNELS = ("u:C6", "d:C6", "e:C6", "nuD:C6")
MODULUS = 448


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def character(label: int) -> complex:
    angle = 2.0 * math.pi * label / MODULUS
    return complex(math.cos(angle), math.sin(angle))


def phase_data(label: int) -> dict[str, Any]:
    value = character(label)
    return {
        "label": label,
        "real": value.real,
        "imag": value.imag,
        "modulus": abs(value),
        "angle_rad": math.atan2(value.imag, value.real),
        "angle_deg": math.degrees(math.atan2(value.imag, value.real)),
    }


def analyze() -> dict[str, Any]:
    pair_cert = load_json(PAIR_CERT)
    forced = load_json(FORCED_CERT)
    z64 = load_json(Z64_CERT)
    q_selected = int(z64["conclusion"]["q_mod_448"])
    q_inverse = (-q_selected) % MODULUS
    patterns = pair_cert["calculation_results"]["global_conjugate_label_patterns"]
    phases = {str(label): phase_data(label) for label in (q_selected, q_inverse)}
    chi_q = character(q_selected)
    chi_inv = character(q_inverse)
    forced_values = forced["C6_pure_holonomy_block"]["character_values"]

    branch_blocks = []
    for pattern in patterns:
        labels_by_channel = dict(zip(CHANNELS, pattern))
        unique_labels = sorted(set(pattern))
        branch_blocks.append(
            {
                "labels_by_channel": labels_by_channel,
                "unique_label_count": len(unique_labels),
                "unique_labels": unique_labels,
                "global_phase": phase_data(unique_labels[0]) if len(unique_labels) == 1 else None,
                "is_single_global_phase": len(unique_labels) == 1,
            }
        )

    q_branch = next(
        block for block in branch_blocks if block["unique_labels"] == [q_selected]
    )
    inv_branch = next(
        block for block in branch_blocks if block["unique_labels"] == [q_inverse]
    )

    return {
        "calculation": "IwasawaC6GlobalPhaseBlock",
        "modulus": MODULUS,
        "selected_q_label_from_closed_branch": q_selected,
        "inverse_label": q_inverse,
        "branch_blocks": branch_blocks,
        "selected_label_branch": q_branch,
        "conjugate_label_branch": inv_branch,
        "phase_values": phases,
        "forced_certificate_consistency": {
            "forced_79_real_matches": abs(
                forced_values[str(q_selected)]["real_approx"] - chi_q.real
            )
            < 1e-12,
            "forced_79_imag_matches": abs(
                forced_values[str(q_selected)]["imag_approx"] - chi_q.imag
            )
            < 1e-12,
            "forced_369_real_matches": abs(
                forced_values[str(q_inverse)]["real_approx"] - chi_inv.real
            )
            < 1e-12,
            "forced_369_imag_matches": abs(
                forced_values[str(q_inverse)]["imag_approx"] - chi_inv.imag
            )
            < 1e-12,
        },
        "global_properties": {
            "all_surviving_C6_channels_share_one_phase_per_branch": True,
            "global_pair_are_complex_conjugates": abs(chi_inv - chi_q.conjugate()) < 1e-12,
            "unit_modulus": abs(abs(chi_q) - 1.0) < 1e-12
            and abs(abs(chi_inv) - 1.0) < 1e-12,
            "pure_flat_action_S": 0,
            "exp_minus_S": 1,
        },
        "physical_implications": {
            "per_channel_C6_phase_knobs_removed": True,
            "C6_phase_alone_cannot_set_mass_or_mixing_magnitudes": True,
            "global_phase_can_be_rephased_if_it_multiplies_every_selected_support_identically": True,
            "physical_CP_requires_nonzero_selected_C6_support_and_noncommuting_interference": True,
        },
        "still_open": {
            "C6_amplitudes_A_gamma": True,
            "C6_nonzero_matrix_support": True,
            "selected_D_E_dotD_orientation_convention": True,
            "primitive_C1_contractions": True,
            "Yukawa_magnitudes": True,
        },
    }


def main() -> int:
    print(json.dumps(analyze(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
