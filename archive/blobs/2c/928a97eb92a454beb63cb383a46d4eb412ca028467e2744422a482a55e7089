"""Audit selected SM-slot functor polarization/overlap source emission."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_smslotfunctor_polarization_overlap_source_emission.py"
CANDIDATE = ROOT / "candidate_data" / "selected_smslotfunctor_polarization_overlap_source_emission.candidate.json"
CERT = ROOT / "certificates" / "selected_smslotfunctor_polarization_overlap_source_emission_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_SelectedSMSlotFunctor_PolarizationAndOverlap_SourceEmission_v1.md"

STATUS = "MTT_SELECTED_SMSLOTFUNCTOR_POLARIZATION_EMITTED_OVERLAP_NORMALIZATION_OPEN"
NEXT = "MTT_SelectedSMSlotFunctor_OverlapKernel_SourceEmission_v1"


def check(name: str, condition: bool, detail: object) -> bool:
    print(("PASS" if condition else "FAIL") + f": {name} -- {detail}")
    return condition


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if proc.returncode != 0:
        print(proc.stdout)
        return 1

    data = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    pol = data["polarization_emission"]
    overlap = data["overlap_kernel_gate"]
    consistency = data["same_source_consistency"]
    arrows = data["arrow_status"]
    closes = data["what_closes_now"]
    remains = data["what_remains_open"]

    tests = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, data["status"]),
        check(
            "strategy guarded",
            data["superset_strategy"]["observed_data_used"] is False
            and data["superset_strategy"]["target_fitting_used"] is False
            and "A1-A3" in data["superset_strategy"]["straight_path"]
            and "do not yet emit A5" in data["superset_strategy"]["support_path"],
            data["superset_strategy"],
        ),
        check(
            "polarization emitted",
            pol["status"] == "EMITTED_SOURCE_ARROW"
            and pol["selected"] is True
            and pol["preconditions"]["first_three_slot_arrows_closed"] is True
            and pol["preconditions"]["selected_10M_clock_label"] is True
            and pol["preconditions"]["selected_bar5M_shift_label"] is True
            and pol["preconditions"]["finite_q79_transversality_closed"] is True
            and pol["preconditions"]["retarded_q79_orientation_closed"] is True
            and pol["selected_outputs"]["q"] == 79
            and pol["selected_outputs"]["U_10"] == "I_3"
            and pol["selected_outputs"]["U_bar5"] == "F",
            pol,
        ),
        check(
            "overlap still open but constrained",
            overlap["status"] == "OPEN"
            and overlap["conditional_support"]["transported_projector_source_promoted"] is True
            and overlap["conditional_support"]["conditional_gram_scalar_fixed_after_rho_s"] is True
            and overlap["conditional_support"]["conditional_normalization_exact"] is True
            and overlap["selected_overlap_transfer_normalization"] is False
            and "selected kernel itself" in overlap["why_not_promoted"],
            overlap,
        ),
        check(
            "same-source consistency partial",
            consistency["status"] == "PARTIAL_OPEN_WAITING_FOR_A5"
            and consistency["closed_parts"]["q79_polarization_A4"] is True
            and consistency["closed_parts"]["transported_projector_source"] is True
            and consistency["open_parts"]["selected_overlap_transfer_kernel_A5"] is True
            and consistency["selected_same_source_consistency_map"] is False,
            consistency,
        ),
        check(
            "arrow counts exact",
            arrows["closed_count"] == 4
            and arrows["open_count"] == 2
            and arrows["all_six_closed"] is False
            and "A4_q79_polarization_outputs" in arrows["closed_arrows"],
            arrows,
        ),
        check(
            "closure accounting",
            closes["selected_U10_Ubar5_source_outputs"] is True
            and closes["selected_q79_retarded_orientation"] is True
            and remains["selected_overlap_transfer_normalization"] is True
            and remains["same_source_consistency_map"] is True
            and remains["selected_overlap_kernel_or_trace_hessian_functional"] is True,
            {"closes": closes, "remains": remains},
        ),
        check(
            "no overclaim",
            data["theorem"]["proved"] is True
            and data["closure_claimed"] is False
            and data["selected_SMSlotFunctor_first_four_arrows_claimed"] is True
            and data["selected_SMSlotFunctor_all_six_arrows_claimed"] is False
            and data["observed_data_used"] is False
            and data["target_fitting_used"] is False
            and cert["selected_SMSlotFunctor_all_six_arrows_claimed"] is False,
            cert,
        ),
        check(
            "note and next gate",
            data["next_required_artifact"] == NEXT
            and cert["next_required_artifact"] == NEXT
            and f"Next artifact: `{NEXT}`" in note
            and "A5 remains open" in note,
            NOTE,
        ),
    ]

    print("\nMTT selected SM-slot functor polarization/overlap source-emission audit")
    return 0 if all(tests) else 1


if __name__ == "__main__":
    sys.exit(main())
