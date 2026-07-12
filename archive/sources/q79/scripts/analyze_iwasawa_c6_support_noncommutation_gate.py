"""Analyze the C6 support gate for leading CKM noncommutation.

The q79 branch now fixes the pure C6 phase to a single global conjugate pair.
This script computes the next finite gate: how selected C6 support matrices
would enter the leading up/down heavy-link mismatch

    Delta_v = (M_d13 - M_u13, M_d23 - M_u23).

It deliberately does not invent C6 support matrices or amplitudes.  Instead it
checks that no selected C6 support data are present in the current package and
records the exact symbolic criterion that such data must satisfy.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERT_DIR = ROOT / "certificates"
CANDIDATE_DIR = ROOT / "candidate_data"

C6_GLOBAL_CERT = CERT_DIR / "iwasawa_c6_global_phase_block_certificate.json"
CKM_CERT = CERT_DIR / "ckm_leading_noncommutation_criterion_certificate.json"
JARLSKOG_CERT = CERT_DIR / "jarlskog_closure_criterion_certificate.json"
WEIGHT_CERT = CERT_DIR / "selected_channel_weight_extraction_protocol_certificate.json"
FORCED_CERT = CERT_DIR / "forced_channel_weight_blocks_certificate.json"

EXPECTED_SELECTED_C6_SUPPORT_FILES = [
    CERT_DIR / "selected_c6_support_matrices_certificate.json",
    CERT_DIR / "iwasawa_c6_support_matrices_certificate.json",
    CERT_DIR / "selected_c6_support_data_certificate.json",
    CANDIDATE_DIR / "selected_c6_support_matrices.json",
    CANDIDATE_DIR / "iwasawa_c6_support_matrices.selected.json",
]


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def certificate_status(path: Path) -> str:
    if not path.exists():
        return "MISSING"
    return str(load_json(path).get("status", "UNKNOWN"))


def present_selected_support_files() -> list[str]:
    return [rel(path) for path in EXPECTED_SELECTED_C6_SUPPORT_FILES if path.exists()]


def analyze() -> dict[str, Any]:
    c6_global = load_json(C6_GLOBAL_CERT)
    ckm = load_json(CKM_CERT)
    jarlskog = load_json(JARLSKOG_CERT)
    weight = load_json(WEIGHT_CERT)
    forced = load_json(FORCED_CERT)

    c6_calc = c6_global["calculation_results"]
    selected_q = c6_calc["selected_q_label_from_closed_branch"]
    inverse_q = c6_calc["inverse_label"]
    chi_79 = c6_calc["chi_79"]
    chi_369 = c6_calc["chi_369"]
    present_support = present_selected_support_files()
    c6_open_fields = {
        "forced_block_open": forced.get("open", {}),
        "weight_protocol_open": weight.get("open", {}),
        "global_phase_still_open": c6_global.get("still_open", {}),
    }

    return {
        "calculation": "IwasawaC6SupportNoncommutationGate",
        "purpose": (
            "Compute the finite leading gate that selected C6 support matrices "
            "must satisfy before q79 can feed CKM noncommutation."
        ),
        "input_statuses": {
            rel(C6_GLOBAL_CERT): certificate_status(C6_GLOBAL_CERT),
            rel(CKM_CERT): certificate_status(CKM_CERT),
            rel(JARLSKOG_CERT): certificate_status(JARLSKOG_CERT),
            rel(WEIGHT_CERT): certificate_status(WEIGHT_CERT),
            rel(FORCED_CERT): certificate_status(FORCED_CERT),
        },
        "selected_c6_phase_block": {
            "selected_label": selected_q,
            "conjugate_label": inverse_q,
            "chi_79": chi_79,
            "chi_369": chi_369,
            "all_c6_channels_share_one_phase_per_branch": c6_calc[
                "all_surviving_C6_channels_share_one_phase_per_branch"
            ],
            "pure_flat_action_S": c6_calc["pure_flat_action_S"],
            "exp_minus_S": c6_calc["exp_minus_S"],
        },
        "selected_support_data_scan": {
            "expected_selected_c6_support_files": [
                rel(path) for path in EXPECTED_SELECTED_C6_SUPPORT_FILES
            ],
            "present_selected_c6_support_files": present_support,
            "selected_c6_support_data_found": bool(present_support),
            "selected_c6_support_values_computed": False,
            "open_fields_confirming_absence": c6_open_fields,
        },
        "symbolic_decomposition": {
            "leading_setup": ckm["setup"],
            "c6_decomposition": "M_s = T_s + chi_q C_s",
            "T_s": "aggregate of selected character-trivial channel supports in sector s",
            "C_s": "selected C6 amplitude-support matrix in sector s",
            "heavy_link_vector": "v_s = (M_s13, M_s23) = t_s + chi_q c_s",
            "t_s": "(T_s13, T_s23)",
            "c_s": "(C_s13, C_s23)",
            "delta_v": "Delta_v = Delta_t + chi_q Delta_c",
            "delta_t": "t_d - t_u",
            "delta_c": "c_d - c_u",
            "leading_commutator": ckm["commutator_expansion"]["leading_matrix"],
        },
        "finite_gate": {
            "leading_noncommutation_condition": "Delta_v != (0,0)",
            "expanded_condition": "Delta_t + chi_q Delta_c != (0,0)",
            "c6_affects_leading_heavy_link_if": "Delta_c != (0,0)",
            "c6_alone_cannot_close_full_cp": True,
            "full_cp_requires": jarlskog["criterion"]["nonzero_condition"],
            "spectral_requirement": jarlskog["setup"]["spectral_condition"],
        },
        "case_table": [
            {
                "case": "no selected C6 heavy-link support",
                "condition": "Delta_c = (0,0)",
                "leading_noncommutation": "controlled only by Delta_t",
                "q79_drives_leading_gate": False,
            },
            {
                "case": "C6 heavy-link support identical in up and down sectors",
                "condition": "c_d = c_u",
                "leading_noncommutation": "C6 cancels from Delta_v at order epsilon",
                "q79_drives_leading_gate": False,
            },
            {
                "case": "C6 heavy-link support mismatch",
                "condition": "Delta_c != (0,0)",
                "leading_noncommutation": (
                    "passes unless the character-trivial part exactly cancels "
                    "Delta_t = -chi_q Delta_c"
                ),
                "q79_drives_leading_gate": True,
            },
            {
                "case": "full CKM CP closure",
                "condition": "nondegenerate spectra and Im det([H_u,H_d]) != 0",
                "leading_noncommutation": "necessary orientation input, not sufficient",
                "q79_drives_leading_gate": "requires selected non-rephasable support",
            },
        ],
        "what_this_closes": {
            "c6_support_entry_target": True,
            "leading_c6_heavy_link_gate": True,
            "c6_global_phase_overclaim_blocked": True,
            "numeric_support_absence_confirmed": True,
        },
        "still_open": {
            "selected_C6_amplitudes_A_gamma": True,
            "selected_C6_support_matrices": True,
            "Delta_t_from_character_trivial_channels": True,
            "Delta_c_from_C6_support": True,
            "selected_Y_u_Y_d": True,
            "Jarlskog_value": True,
            "Yukawa_magnitudes": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_selected_C6_support_values_computed": False,
            "claims_Delta_v_computed": False,
            "claims_leading_noncommutation_passes": False,
            "claims_jarlskog_nonzero": False,
            "claims_yukawa_magnitudes": False,
            "claims_full_SM_closure": False,
        },
        "verdict": {
            "criterion_closed": True,
            "selected_c6_support_values_open": True,
            "numeric_ckm_noncommutation_open": True,
            "next_packet": (
                "Supply selected C6 amplitude-support matrices C_u and C_d, "
                "plus character-trivial heavy-link vectors t_u and t_d, then "
                "evaluate Delta_t + chi_q Delta_c."
            ),
        },
    }


def main() -> int:
    print(json.dumps(analyze(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
