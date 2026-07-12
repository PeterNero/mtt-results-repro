"""Audit selected SM-slot functor six-arrow source emission."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_smslotfunctor_sixarrow_source_emission.py"
CANDIDATE = ROOT / "candidate_data" / "selected_smslotfunctor_sixarrow_source_emission.candidate.json"
CERT = ROOT / "certificates" / "selected_smslotfunctor_sixarrow_source_emission_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_SelectedSMSlotFunctor_SixArrow_SourceEmission_v1.md"

STATUS = "MTT_SELECTED_SMSLOTFUNCTOR_SIXARROW_PARTIAL_SOURCE_EMISSION_BUILT_POLARIZATION_NORMALIZATION_OPEN"
NEXT = "MTT_SelectedSMSlotFunctor_PolarizationAndOverlap_SourceEmission_v1"


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
    ah = data["AH_Cech_binding"]
    emitted = data["emitted_source_arrows"]
    open_arrows = data["open_source_arrows"]
    arrow_status = data["arrow_status"]
    closes = data["what_closes_now"]
    remains = data["what_remains_open"]

    tests = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, data["status"]),
        check(
            "strategy guarded",
            data["superset_strategy"]["using_one_straight_path"] is False
            and data["superset_strategy"]["observed_data_used"] is False
            and data["superset_strategy"]["target_fitting_used"] is False
            and "A1-A3" in data["superset_strategy"]["straight_path"],
            data["superset_strategy"],
        ),
        check(
            "AH/Cech source-layer binding promoted",
            ah["terminal_source_axiom_backed"] is True
            and ah["selected_L"] == [1, -2, 0]
            and ah["selected_L2"] == [2, -4, 0]
            and ah["constructed_AH_support"] is True
            and ah["constructed_Yoneda_support"] is True
            and ah["ordered_source_layer_binding_promoted"] is True
            and ah["operator_layer_pic0_recheck_open"] is True,
            ah,
        ),
        check(
            "first three arrows emitted",
            emitted["A1_terminal_Ext_to_10M_clock"]["selected"] is True
            and emitted["A1_terminal_Ext_to_10M_clock"]["outputs"] == ["u", "e"]
            and emitted["A2_terminal_Ext_to_bar5M_shift"]["selected"] is True
            and emitted["A2_terminal_Ext_to_bar5M_shift"]["outputs"] == ["d"]
            and emitted["A3_terminal_Ext_to_1M_Dirac"]["selected"] is True
            and emitted["A3_terminal_Ext_to_1M_Dirac"]["outputs"] == ["nuD"],
            emitted,
        ),
        check(
            "last three arrows open",
            open_arrows["A4_q79_polarization_outputs"]["status"] == "SUPPORT_ONLY_SOURCE_OUTPUT_OPEN"
            and open_arrows["A4_q79_polarization_outputs"]["candidate_outputs"] == {
                "U_10": "I_3",
                "U_bar5": "F",
            }
            and open_arrows["A5_overlap_transfer_normalization"]["status"] == "OPEN"
            and open_arrows["A6_same_source_consistency"]["status"] == "PARTIAL_OPEN",
            open_arrows,
        ),
        check(
            "arrow counts exact",
            arrow_status["closed_count"] == 3
            and arrow_status["open_count"] == 3
            and arrow_status["all_six_closed"] is False,
            arrow_status,
        ),
        check(
            "closure accounting",
            closes["selected_sectionring_to_10M_clock_arrow"] is True
            and closes["selected_sectionring_to_bar5M_shift_arrow"] is True
            and closes["selected_sectionring_to_1M_Dirac_arrow"] is True
            and closes["selected_1M_Dirac_shift_readout"] is True
            and remains["selected_U10_Ubar5_source_outputs"] is True
            and remains["selected_overlap_transfer_normalization"] is True
            and remains["same_source_consistency_map"] is True,
            {"closes": closes, "remains": remains},
        ),
        check(
            "no overclaim",
            data["theorem"]["proved"] is True
            and data["closure_claimed"] is False
            and data["selected_SMSlotFunctor_first_three_arrows_claimed"] is True
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
            and "The remaining arrows are" in note,
            NOTE,
        ),
    ]

    print("\nMTT selected SM-slot functor six-arrow source-emission audit")
    return 0 if all(tests) else 1


if __name__ == "__main__":
    sys.exit(main())
