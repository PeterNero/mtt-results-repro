"""Audit selected End0 action matrix or matter-slot routing value fill."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_sector_zero_mode_end0_action_matrix_or_matter_slot_routing_value_fill.py"
CANDIDATE = ROOT / "candidate_data" / "selected_sector_zero_mode_end0_action_matrix_or_matter_slot_routing_value_fill.candidate.json"
CERT = ROOT / "certificates" / "selected_sector_zero_mode_end0_action_matrix_or_matter_slot_routing_value_fill_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_SectorZeroMode_End0Action_Matrix_or_MatterSlotRouting_Value_Fill_v1.md"

STATUS = "MTT_SELECTED_SECTOR_END0_ACTION_VALUE_FILL_ATTEMPTED_RHOS_AND_ROUTING_OPEN"
NEXT = "MTT_Selected_SectorZeroMode_SourceAction_or_SelectedMatterSlotRouting_Source_Theorem_v1"


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
    direct = data["direct_End0_action_value_fill"]
    model = direct["model_matrix_tests"]
    routing = data["matter_slot_routing_value_fill"]
    gram = data["conditional_gram_normalization_theorem"]
    gates = data["selected_source_gates"]
    decision = data["decision"]

    checks = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, data["status"]),
        check("certificate path", cert["candidate_path"].endswith(CANDIDATE.name), cert),
        check(
            "model matrices pass",
            direct["candidate_values_exist_as_universal_model"] is True
            and direct["candidate_values_selected_on_actual_zero_modes"] is False
            and direct["model_source_map_validation"]["matter_sector_maps_present"] is True
            and direct["model_source_map_validation"]["H_map_zero"] is True
            and direct["model_source_map_validation"]["all_source_selected_flags_false"] is True
            and direct["model_source_map_validation"]["model_map_passes_representation_tests"] is True
            and direct["constructed_model_source_map"]["Q"]["rho"]["T3"] == model["model_rho_T3"]
            and all(model["lie_brackets_pass"].values())
            and all(model["skew_for_identity_gram"].values())
            and model["negative_casimir_equals_2I"] is True
            and model["H_action_zero"] is True,
            model,
        ),
        check(
            "direct value fill honestly blocked",
            "selected source map rho_s(T_i) on K_s is not emitted" in direct["why_not_selected"]
            and "coherent spectral zero-mode projector retention remains open" in direct["why_not_selected"],
            direct["why_not_selected"],
        ),
        check(
            "routing value fill honestly blocked",
            routing["selected_matter_slot_routing_present"] is False
            and routing["selected_1M_Dirac_neutrino_rule_present"] is False
            and routing["support_sources"]["hybrid_shape_scaffold_present"] is True
            and routing["support_sources"]["hybrid_selected_matter_slot_transport_present"] is False,
            routing,
        ),
        check(
            "conditional gram theorem",
            gram["proved"] is True
            and "selected physical dotD_alpha1" in gram["does_not_emit"]
            and "sector Gram ambiguity after selected rho_s is emitted" in gram["closes_conditionally"],
            gram,
        ),
        check(
            "source gates remain open",
            gates["selected_zero_mode_bases"] is False
            and gates["selected_rho_s_source_map"] is False
            and gates["coherent_spectral_zero_mode_retention"] is False
            and gates["selected_matter_slot_routing"] is False
            and gates["selected_1M_Dirac_neutrino_rule"] is False,
            gates,
        ),
        check(
            "decision honest",
            decision["selected_End0_action_values_filled"] is False
            and decision["selected_matter_slot_routing_filled"] is False
            and decision["conditional_Gram_theorem_added"] is True
            and decision["next_required_artifact"] == NEXT,
            decision,
        ),
        check(
            "no closure or target fitting",
            data["closure_claimed"] is False
            and data["target_fitting_used"] is False
            and cert["closure_claimed"] is False
            and cert["target_fitting_used"] is False,
            cert,
        ),
        check(
            "note records boundary",
            "does not yet emit selected `rho_s(T_i)` matrices" in note
            and "Conditional Lemma Closed" in note
            and f"Next artifact: `{NEXT}`" in note,
            NOTE,
        ),
    ]

    print("\nMTT selected sector End0 action/routing value-fill audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
