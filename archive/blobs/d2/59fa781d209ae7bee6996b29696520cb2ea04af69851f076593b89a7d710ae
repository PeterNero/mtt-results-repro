"""Audit the terminal-map source-principle or SM-slot-functor gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_terminalmap_sourceprinciple_or_smslotfunctor.py"
CANDIDATE = ROOT / "candidate_data" / "selected_terminalmap_sourceprinciple_or_smslotfunctor.candidate.json"
CERT = ROOT / "certificates" / "selected_terminalmap_sourceprinciple_or_smslotfunctor_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_TerminalMap_SourcePrinciple_or_SMSlotFunctor_v1.md"

STATUS = "MTT_SELECTED_TERMINALMAP_SOURCEPRINCIPLE_CONDITIONAL_ORDERED_SOURCE_CLOSED_SMSLOTFUNCTOR_OPEN"
NEXT = "MTT_TerminalAdmissibleSection_PrinciplePromotion_or_SelectedSMSlotFunctor_v1"


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

    principle = data["imported_principle_status"]
    terminal = data["conditional_terminal_source_closure"]
    ah = data["AH_Cech_binding_status"]
    sm = data["SM_slot_functor_status"]
    routes = data["two_routes_forward"]
    closes = data["what_closes_now"]
    remains = data["what_remains_open"]

    tests = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, data["status"]),
        check(
            "strategy guarded",
            data["superset_strategy"]["using_one_straight_path"] is False
            and data["superset_strategy"]["observed_data_used"] is False
            and data["superset_strategy"]["target_fitting_used"] is False
            and "no observed masses" in data["superset_strategy"]["locked_target_role"],
            data["superset_strategy"],
        ),
        check(
            "principle imported conditionally",
            principle["principle_name"] == "TerminalAdmissibleSectionSourcePrinciple.v1"
            and principle["corpus_supported"] is True
            and principle["closed_under_explicit_principle"] is True
            and principle["unconditional_in_MTT_spine"] is False
            and "promoted into the main MTT axiomatic spine" in principle["credibility_status"],
            principle,
        ),
        check(
            "terminal source closes under principle",
            terminal["selected_source_label"] == "g3 / L3-K2"
            and terminal["selected_L"] == [1, -2, 0]
            and terminal["selected_L2"] == [2, -4, 0]
            and terminal["selected_c2"] == [4, 0, 0]
            and terminal["terminal_lane_unique_zero_central"] is True
            and terminal["terminal_lane_unique_visible_c2"] is True
            and terminal["ordered_source_validator_passes"] is True
            and terminal["cohomology_validator_passes"] is True
            and terminal["closed_only_if_principle_is_admitted"] is True,
            terminal,
        ),
        check(
            "AH binding scoped correctly",
            ah["AH_goodcover_equivalence_proved"] is True
            and ah["binding_closed_under_principle_at_ordered_layer"] is True
            and ah["raw_good_cover_or_smooth_Dolbeault_transition_data_still_open"] is True
            and ah["operator_layer_Pic0_recheck_still_open"] is True,
            ah,
        ),
        check(
            "SM slot functor still open",
            sm["support_from_dirac_gate"]["finite_q79_polarization_support"] is True
            and sm["support_from_dirac_gate"]["structural_1M_rule_available"] is True
            and sm["still_not_emitted"]["selected_U10_Ubar5_polarization"] is True
            and sm["still_not_emitted"]["selected_1M_Dirac_rule"] is True
            and sm["closed"] is False,
            sm,
        ),
        check(
            "routes forward exact",
            routes["Route_A_promote_principle"]["status"] == "PRIMARY"
            and routes["Route_B_emit_SM_slot_functor"]["status"] == "PARALLEL"
            and routes["Route_C_operator_bypass"]["status"] == "RETAINED",
            routes,
        ),
        check(
            "closure and remainder accounting",
            closes["terminal_source_closed_under_explicit_principle"] is True
            and closes["h1_Ext_packet_promotes_under_principle"] is True
            and remains["promote_principle_to_unconditional_MTT_axiom_or_derive_it"] is True
            and remains["selected_section_ring_to_SM_slot_functor"] is True
            and remains["operator_layer_Pic0_recheck"] is True,
            {"closes": closes, "remains": remains},
        ),
        check(
            "no unconditional overclaim",
            data["closure_claimed"] is False
            and data["unconditional_MTT_closure_claimed"] is False
            and cert["unconditional_MTT_closure_claimed"] is False
            and data["observed_data_used"] is False
            and data["target_fitting_used"] is False,
            cert,
        ),
        check(
            "theorem and next gate recorded",
            data["theorem"]["proved"] is True
            and data["next_required_artifact"] == NEXT
            and cert["next_required_artifact"] == NEXT
            and f"`{NEXT}`" in note,
            NOTE,
        ),
    ]

    print("\nMTT terminal-map source-principle / SM-slot-functor audit")
    return 0 if all(tests) else 1


if __name__ == "__main__":
    sys.exit(main())
