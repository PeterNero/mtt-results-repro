from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "physical_normalization_stress_response_gate_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")
    source = cert["source_tests"]
    stress = cert["stress_response"]
    norm = cert["physical_normalization"]
    assembly = cert["einstein_response_assembly"]
    guards = cert["guardrails"]

    require(cert["status"] == "STRUCTURAL_STRESS_RESPONSE_CLOSED_PHYSICAL_NORMALIZATION_OPEN", "bad status")
    require(source["effective_einstein_hilbert_action_sourced"] is True, "EH action should be sourced")
    require(source["variational_stress_tensor_sourced"] is True, "stress tensor should be sourced")
    require(source["einstein_equation_sourced"] is True, "Einstein equation should be sourced")
    require(source["bianchi_conservation_sourced"] is True, "Bianchi conservation should be sourced")
    require(source["scalar_ym_dirac_examples_sourced"] is True, "matter examples should be sourced")
    require(source["m_theory_planck_slot_sourced"] is True, "M-theory Planck slot should be sourced")
    require(source["theta_volume_to_newton_slot_sourced"] is True, "Theta Newton slot should be sourced")

    require(stress["universal_variational_definition_closed"] is True, "stress form should close")
    require(stress["conservation_law_closed"] is True, "conservation should close")
    require(stress["matter_examples_closed_as_forms"] is True, "matter forms should close")
    require(stress["selected_numeric_matter_parameters_closed"] is False, "numeric matter parameters remain open")
    require(stress["selected_coherence_to_matter_map_closed"] is False, "coherence-to-matter map remains open")

    require(norm["physical_absolute_dimensionful_anchor_closed"] is False, "physical anchor must remain open")
    require(norm["internal_to_SI_unit_map_selected"] is False, "SI unit map must remain open")
    require(norm["dimensionful_modal_gap_value_computed"] is False, "dimensionful modal gap must remain open")
    require(norm["newton_or_planck_prediction_allowed_now"] is False, "Newton/Planck prediction must not be allowed")

    require(assembly["dimensionless_exact_TT_branch_ready"] is True, "TT branch should be ready")
    require(assembly["stress_response_form_ready"] is True, "stress form should be ready")
    require(assembly["physical_absolute_normalization_ready"] is False, "physical normalization should block")
    require(cert["full_physical_gr_closed"] is False, "full physical GR must not be closed")

    require(guards["claims_measured_Newton_constant"] is False, "must not claim measured Newton")
    require(guards["claims_measured_Planck_scale"] is False, "must not claim measured Planck")
    require(guards["uses_observed_Newton_or_Planck_input"] is False, "must not use target input")
    require(guards["adds_new_GR_parameter"] is False, "must not add GR parameter")
    require(guards["treats_G10_as_selected"] is False, "G10 must not be treated as selected")

    require("stress-response slot" in note, "note should state stress closure")
    require("physical normalization is not closed" in note, "note should state normalization blocker")
    print("AUDIT_PASS: structural stress response closed; physical normalization and full GR remain open")


if __name__ == "__main__":
    main()
