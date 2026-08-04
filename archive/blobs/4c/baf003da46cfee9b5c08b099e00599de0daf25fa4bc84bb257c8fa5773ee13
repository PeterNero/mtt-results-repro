"""Audit the terminal-monad base-order/AH-binding/SM-slot-map gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_terminalmonad_baseorder_ahbinding_smslotmap.py"
CANDIDATE = ROOT / "candidate_data" / "selected_terminalmonad_baseorder_ahbinding_smslotmap.candidate.json"
CERT = ROOT / "certificates" / "selected_terminalmonad_baseorder_ahbinding_smslotmap_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_TerminalMonad_BaseOrder_AHBinding_SMSlotMap_v1.md"

STATUS = "MTT_SELECTED_TERMINALMONAD_BASEORDER_AHBINDING_SMSLOTMAP_GATE_BUILT_SOURCE_PROMOTION_OPEN"
NEXT = "MTT_Selected_TerminalMap_SourcePrinciple_or_SMSlotFunctor_v1"


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

    base = data["base_order_audit"]
    ah = data["AH_Cech_binding_audit"]
    slot = data["SM_slot_map_audit"]
    cutset = data["three_gate_cutset"]
    closes = data["what_closes_now"]
    remains = data["what_remains_open"]

    tests = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, data["status"]),
        check(
            "strategy guarded",
            data["superset_strategy"]["using_one_straight_path"] is False
            and data["superset_strategy"]["observed_data_used"] is False
            and data["superset_strategy"]["target_fitting_used"] is False
            and "forbidden selectors" in data["superset_strategy"]["locked_target_role"],
            data["superset_strategy"],
        ),
        check(
            "diagnostic base order rejected",
            base["diagnostic_base_order_selected_flag"] is True
            and base["diagnostic_standard_lattice_flag"] is True
            and base["diagnostic_ordered_validator_passes"] is True
            and base["promotable_as_theorem"] is False
            and base["why_not"]["fixture_only"] is True
            and base["why_not"]["selected_by_mtt"] is False,
            base,
        ),
        check(
            "AH binding support not selection",
            ah["automorphy_formula_constructed"] is True
            and ah["c1_matrix_matches_required_order"] is True
            and ah["yoneda_multiplication_identity_verified"] is True
            and ah["AH_source_selected_by_MTT"] is False
            and ah["standard_lattice_selected_by_MTT"] is False
            and ah["target_branch_selected_by_MTT"] is False
            and ah["promotable_as_theorem"] is False,
            ah,
        ),
        check(
            "SM slot support not selection",
            slot["finite_q79_polarization_support"] is True
            and slot["structural_1M_rule_available"] is True
            and slot["selected_U10_Ubar5_polarization_closed"] is False
            and slot["selected_1M_Dirac_rule_closed"] is False
            and slot["slot_contract"]["10_M_clock"] == ["u", "e"]
            and slot["slot_contract"]["1_M_Dirac_shift"] == ["nuD"],
            slot,
        ),
        check(
            "three gate cutset exact",
            cutset["G1_terminal_map_source_principle"]["status"] == "OPEN"
            and cutset["G2_AH_Cech_binding"]["status"] == "OPEN"
            and cutset["G3_SM_slot_functor"]["status"] == "OPEN"
            and "base_factor_order_selected" in cutset["G1_terminal_map_source_principle"]["also_emits"],
            cutset,
        ),
        check(
            "closure accounting",
            closes["diagnostic_base_order_not_promotable"] is True
            and closes["AH_binding_exists_mathematically_not_selected"] is True
            and closes["SM_slot_map_support_exists_not_selected"] is True
            and closes["three_gate_cutset_identified"] is True
            and remains["terminal_map_source_principle"] is True
            and remains["selected_section_ring_to_SM_slot_functor"] is True,
            {"closes": closes, "remains": remains},
        ),
        check(
            "no overclaim",
            data["closure_claimed"] is False
            and cert["closure_claimed"] is False
            and data["observed_data_used"] is False
            and data["target_fitting_used"] is False
            and cert["target_fitting_used"] is False,
            cert,
        ),
        check(
            "theorem and next gate recorded",
            data["theorem"]["proved"] is True
            and data["next_required_artifact"] == NEXT
            and cert["next_required_artifact"] == NEXT
            and f"Next artifact: `{NEXT}`" in note,
            NOTE,
        ),
    ]

    print("\nMTT terminal-monad base-order/AH-binding/SM-slot-map audit")
    return 0 if all(tests) else 1


if __name__ == "__main__":
    sys.exit(main())
