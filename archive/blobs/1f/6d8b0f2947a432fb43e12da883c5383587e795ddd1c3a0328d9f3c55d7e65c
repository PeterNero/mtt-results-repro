from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "routec_basistransport_primitive_source_theorem_import_certificate.json"
STATUS = "ROUTEC_BASISTRANSPORT_PRIMITIVE_SOURCE_THEOREM_SLOT_IMPORTED_SOURCE_PROOF_OPEN"
NEXT_ARTIFACT = "MTT_Selected_RouteC_BasisTransport_Primitive_Source_Proof_or_Counterexample_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["theorem"]["proved"] is True, "theorem-slot import should be proved")
    require(all(cert["input_checks"].values()), "all input checks should pass")
    require(all(cert["finite_support_checks"].values()), "all finite support checks should pass")
    require(all(cert["theorem_slot_checks"].values()), "all theorem-slot checks should pass")
    require(all(cert["open_gate_checks"].values()), "all open gate checks should pass")
    require(all(cert["paper_checks"].values()), "all paper checks should pass")
    require(all(cert["certificate_checks"].values()), "all certificate checks should pass")

    verdict = cert["verdict"]
    require(verdict["theorem_slot_imported"] is True, "theorem slot should be imported")
    require(verdict["finite_support_lemmas_packaged"] is True, "finite lemmas should be packaged")
    require(verdict["paper_proof_slot_imported"] is True, "paper slot should be imported")
    require(verdict["selected_source_emission_proved"] is False, "source emission must remain open")
    require(verdict["A_selected_emitted"] is False, "A_selected must remain open")
    require(verdict["b_selected_emitted"] is False, "b_selected must remain open")
    require(verdict["splitter_equation_solved"] is False, "splitter solve must remain open")
    require(verdict["observed_flavor_data_used"] is False, "observed data must not be used")
    require(verdict["next_required_artifact"] == NEXT_ARTIFACT, "wrong next artifact")

    slot = packet["theorem_slot"]
    require(
        slot["not_proved_now"]["selected_source_emits_basis_transport_or_vertex_primitive"] is True,
        "source-emission gap must be preserved",
    )
    require(
        "active deck shift (1,1)" in slot["formal_statement"],
        "formal statement must name active shift",
    )
    require(
        "This is not yet the source theorem" in note and "No observed masses" in note,
        "note must preserve boundary and guardrail",
    )

    print("AUDIT_PASS: basis-transport theorem slot imported; source proof remains open")


if __name__ == "__main__":
    main()
