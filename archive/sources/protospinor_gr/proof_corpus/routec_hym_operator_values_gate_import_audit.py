from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "routec_hym_operator_values_gate_import_certificate.json"
STATUS = "ROUTEC_HYM_OPERATOR_VALUES_GATE_IMPORTED_EXTRACTION_THEOREM_OPEN"
NEXT = "MTT_Selected_HYM_Connection_to_Finite_Operator_Extraction_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["theorem"]["proved"] is True, "operator-values import theorem should be proved")
    require(all(cert["input_checks"].values()), "input checks should pass")
    require(all(cert["honest_checks"].values()), "honest checks should pass")
    require(all(cert["lifted_checks"].values()), "lifted checks should pass")
    require(all(cert["source_flag_checks"].values()), "source flags should all be false")
    require(all(cert["extraction_checks"].values()), "extraction checks should pass")

    verdict = cert["verdict"]
    require(verdict["abstract_HYM_existence_available"] is True, "abstract HYM should be available")
    require(verdict["honest_smoke_partial_support_only"] is True, "smoke should be support only")
    require(verdict["lifted_flags_rejected_as_proof"] is True, "lifted flags must be rejected")
    require(verdict["selected_D_E_Riesz_Green_dotD_closed"] is False, "operator values must remain open")
    require(verdict["selected_A_selected_emitted"] is False, "A_selected must remain open")
    require(verdict["selected_b_selected_emitted"] is False, "b_selected must remain open")
    require(verdict["observed_flavor_data_used"] is False, "observed data must not be used")
    require(verdict["next_required_artifact"] == NEXT, "wrong next artifact")

    require(
        "lifted-flag operator checks pass only as schema sufficiency diagnostics" in note
        and NEXT in note,
        "note must record guardrail and next artifact",
    )
    require(
        packet["needed_extraction_theorem"]["name"]
        == "Selected_HYM_Connection_to_Finite_Operator_Extraction.v1",
        "missing extraction theorem name",
    )

    print("AUDIT_PASS: HYM operator-values gate imported; extraction theorem is next")


if __name__ == "__main__":
    main()
