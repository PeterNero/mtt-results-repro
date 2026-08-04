"""Audit the selected 1_M Dirac source / U10-Ubar5 polarization gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_1m_dirac_source_or_u10ubar5_polarization.py"
CANDIDATE = ROOT / "candidate_data" / "selected_1m_dirac_source_or_u10ubar5_polarization.candidate.json"
CERT = ROOT / "certificates" / "selected_1m_dirac_source_or_u10ubar5_polarization_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_1M_DiracNeutrino_Source_or_U10Ubar5Polarization_v1.md"

STATUS = "MTT_SELECTED_1M_DIRAC_SOURCE_OR_U10UBAR5_POLARIZATION_GATE_BUILT_SOURCE_PROMOTION_OPEN"
NEXT = "MTT_Selected_U10Ubar5_1M_SourcePromotion_SameBranch_Emission_v1"


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
    route_a = data["route_A_SU5_E6_polarization"]
    route_b = data["route_B_HYM_projector_zero_mode"]
    decision = data["selection_decision"]
    contract = data["same_branch_promotion_contract"]
    remains = data["what_remains_open"]
    superset = data["superset_strategy"]

    tests = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, data["status"]),
        check(
            "Route A support closed but not selected",
            route_a["support_closed"] is True
            and route_a["selected_closed"] is False
            and route_a["finite_packet"]["U_10"] == "I_3"
            and route_a["finite_packet"]["U_bar5"] == "F"
            and route_a["source_flags"]["selected_mtt_source_present"] is False,
            route_a,
        ),
        check(
            "Route B support closed but not selected",
            route_b["support_closed"] is True
            and route_b["selected_closed"] is False
            and route_b["projector_payload_summary"]["finite_projector_values_emitted"] is True
            and route_b["projector_payload_summary"]["selected_HYM_projector_values_promoted"] is False,
            route_b,
        ),
        check(
            "same branch contract includes 1M and U packets",
            contract["must_emit"]["selected_ordered_matter_slot_packet"] == [
                "10_M_clock",
                "bar5_M_shift",
                "1_M_Dirac_shift",
            ]
            and contract["must_emit"]["selected_polarization_values"] == {"U_10": "I_3", "U_bar5": "F"}
            and contract["must_emit"]["selected_sector_route"] == {"phase": ["u", "e"], "shift": ["d", "nuD"]},
            contract,
        ),
        check(
            "no promotion overclaim",
            decision["selected_U10_Ubar5_polarization_closed"] is False
            and decision["selected_1M_Dirac_neutrino_source_rule_closed"] is False
            and decision["selected_sector_charge_or_chirality_closed"] is False
            and decision["selected_transfer_normalization_promoted"] is False
            and data["closure_claimed"] is False
            and cert["closure_claimed"] is False,
            decision,
        ),
        check(
            "source obligations recorded",
            remains["selected_U10_clock_source"] is True
            and remains["selected_Ubar5_shift_source"] is True
            and remains["selected_1M_Dirac_neutrino_shift_source"] is True
            and remains["selected_zero_mode_projector_or_SU5_source_identity"] is True,
            remains,
        ),
        check(
            "guardrails",
            data["target_fitting_used"] is False
            and cert["target_fitting_used"] is False
            and superset["observed_data_used"] is False
            and superset["diagnostic_lift_used_as_proof"] is False
            and "observed flavor data" in contract["forbidden_inputs"]
            and "conditional transversality treated as selected source" in contract["forbidden_inputs"],
            {"superset": superset, "forbidden": contract["forbidden_inputs"]},
        ),
        check(
            "next gate recorded",
            data["next_required_artifact"] == NEXT
            and cert["next_required_artifact"] == NEXT
            and f"Next artifact: `{NEXT}`" in note
            and "Selected same-branch source emission" in note,
            NOTE,
        ),
    ]

    print("\nMTT selected 1_M Dirac source / U10-Ubar5 polarization gate audit")
    return 0 if all(tests) else 1


if __name__ == "__main__":
    sys.exit(main())
