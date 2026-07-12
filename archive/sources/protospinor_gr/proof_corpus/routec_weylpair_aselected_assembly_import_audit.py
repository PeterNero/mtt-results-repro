from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "routec_weylpair_aselected_assembly_import_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")
    insertion = Path(cert["paper_insertion_written"]).read_text(encoding="utf-8")

    require(
        cert["status"] == "ROUTEC_WEYLPAIR_CONDITIONAL_A_SOLVE_BUILT_SOURCE_PROVENANCE_OPEN",
        "unexpected status",
    )
    require(cert["theorem"]["proved"] is True, "conditional assembly theorem should be proved")
    require(all(cert["closed_now"].values()), "all closed-now checks should pass")
    require(all(cert["still_open"].values()), "all still-open gates should remain true")
    require(cert["conditional_operator"]["shape"] == [72, 2], "operator shape should be 72x2")
    require(cert["conditional_operator"]["is_A_selected"] is False, "conditional operator must not be selected")
    require(cert["locked_solve"]["rank"] == 2, "rank should be 2")
    require(cert["locked_solve"]["consistent"] is True, "solve should be consistent")
    require(cert["locked_solve"]["relative_residual"] < 1.0e-12, "solve residual too large")
    require(cert["locked_solve"]["deltaTheta_conditional"][0] == 1.0, "first deltaTheta coordinate changed")
    require(abs(cert["locked_solve"]["deltaTheta_conditional"][1] - 1.0) < 1.0e-12, "second deltaTheta coordinate changed")
    require(cert["selected_emission_status"]["A_selected_currently_emitted"] is False, "A_selected must remain open")
    require(cert["selected_emission_status"]["b_selected_currently_emitted"] is False, "b_selected must remain open")
    require(packet["provenance_reduction"]["name"] == "SelectedWeylPairSourceProvenanceLemma", "next lemma mismatch")
    require(cert["verdict"]["selected_source_provenance_proved"] is False, "source provenance must remain open")
    require("does not promote `A_weylpair_conditional` to `A_selected`" in note, "note must preserve A boundary")
    require("This is not yet `A_selected`" in insertion, "insertion must preserve selected boundary")
    require(all(cert["guardrails"].values()), "all guardrails must hold")

    print("AUDIT_PASS: conditional Weyl-pair A solve imported; source provenance remains open")


if __name__ == "__main__":
    main()
