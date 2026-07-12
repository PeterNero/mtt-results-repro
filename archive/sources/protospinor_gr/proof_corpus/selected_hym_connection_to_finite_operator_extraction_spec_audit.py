from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "selected_hym_connection_to_finite_operator_extraction_spec_certificate.json"
STATUS = "SELECTED_HYM_CONNECTION_TO_FINITE_OPERATOR_EXTRACTION_SPEC_BUILT_VALUES_OPEN"
NEXT = "MTT_Selected_HYM_Connection_to_Finite_Operator_Extraction_Run_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    template = json.loads(Path(cert["template_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["theorem"]["proved"] is True, "extraction spec theorem should be proved")
    require(all(cert["checks"].values()), "all spec checks should pass")
    require(len(cert["required_fields"]) == 10, "ten required fields expected")
    require(len(cert["validators"]) == 8, "eight validators expected")
    require(template["closure_claimed"] is False, "spec must not claim closure")
    require(template["acceptance_tests"]["all_required_fields_filled"] is False, "values must remain open")
    require(template["acceptance_tests"]["can_emit_A_selected_after_pass"] is False, "A must not emit before pass")
    require(template["acceptance_tests"]["can_emit_b_selected_after_pass"] is False, "b must not emit before pass")
    require("using lifted selected flags as proof" in template["forbidden_shortcuts"], "lifted flags guardrail missing")
    require(cert["next_required_artifact"] == NEXT, "wrong next artifact")
    require("This spec does not emit values yet" in note and NEXT in note, "note must state boundary")

    print("AUDIT_PASS: HYM connection-to-finite-operator extraction spec built; values are open")


if __name__ == "__main__":
    main()
