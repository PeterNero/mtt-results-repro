from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "selected_matter_payload_import_interface_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    template = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")
    slots = cert["required_slots"]
    readiness = cert["readiness"]
    verdict = cert["verdict"]
    guards = cert["guardrails"]

    require(
        cert["status"] == "SELECTED_MATTER_PAYLOAD_IMPORT_INTERFACE_BUILT_VALUES_OPEN",
        "unexpected selected matter payload interface status",
    )
    require(verdict["interface_built"] is True, "interface should be built")
    require(verdict["selected_matter_payload_import_closed"] is False, "payload import must remain open")
    require(verdict["selected_matter_stress_coefficients_closed"] is False, "stress coefficients must remain open")
    require(verdict["full_SM_closure_claim_allowed"] is False, "must not claim full SM")
    require(verdict["full_GR_response_claim_allowed"] is False, "must not claim full GR")
    require(readiness["universal_stress_forms_ready"] is True, "universal stress forms should be ready")
    require(readiness["selected_source_support_shapes_present"] is True, "support shapes should be present")
    require(readiness["selected_payload_values_emitted"] is False, "selected values must remain absent")
    require(readiness["selected_matter_stress_import_ready"] is False, "stress import must not be ready")

    expected_slots = {
        "selected_source_branch",
        "selected_sector_projectors_and_zero_modes",
        "selected_DE_Riesz_Green_dotD",
        "finite_C1_Hessian_deltaTheta",
        "primitive_overlap_contractions",
        "family_kinetic_metrics",
        "neutral_higgs_matching_data",
    }
    require(set(slots) == expected_slots, "required payload slots changed")
    require(all(slot["filled"] is False for slot in slots.values()), "no slot should be filled yet")
    require(set(verdict["blocked_by"]) == expected_slots, "blocked_by must match unfilled slots")
    require(set(template["required_slots"]) == expected_slots, "template slot set changed")
    require(all(slot["values"] is None for slot in template["required_slots"].values()), "template values must be empty")

    require("same-branch selected matter payload" in note, "note must identify the true missing object")
    require("selected matter stress coefficients are open" in note, "note must preserve open status")
    require(all(guards.values()), "all guardrails must hold")

    print("AUDIT_PASS: selected matter payload import interface built; selected values remain open")


if __name__ == "__main__":
    main()
