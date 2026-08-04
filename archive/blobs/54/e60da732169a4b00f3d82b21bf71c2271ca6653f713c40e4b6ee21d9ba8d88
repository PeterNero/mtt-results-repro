from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "routec_hybrid_matter_slot_galerkin_import_certificate.json"
STATUS = "ROUTEC_HYBRID_MATTERSLOT_GALERKIN_IMPORTED_SOURCE_OVERLAP_OPEN"
NEXT_ARTIFACT = "MTT_Selected_RouteC_Selected_OperatorSource_and_OverlapTensor_Packet_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["theorem"]["proved"] is True, "hybrid import should be proved")
    require(all(cert["input_checks"].values()), "all input checks should pass")
    require(all(cert["honest_checks"].values()), "all honest checks should pass")
    require(all(cert["fixture_checks"].values()), "all fixture checks should pass")
    require(all(cert["c1_checks"].values()), "all C1 checks should pass")
    require(all(cert["verdict_checks"].values()), "all verdict checks should pass")
    require(all(cert["guardrail_checks"].values()), "all guardrail checks should pass")

    verdict = cert["verdict"]
    require(verdict["honest_shape_scaffold_present"] is True, "shape scaffold should be present")
    require(verdict["identity_transport_no_go_recorded"] is True, "identity transport no-go missing")
    require(verdict["conditional_su5_fixture_not_promoted"] is True, "fixture must not be promoted")
    require(verdict["selected_operator_source_present"] is False, "selected source must remain open")
    require(verdict["selected_overlap_tensor_present"] is False, "overlap tensor must remain open")
    require(verdict["conditional_A_promoted_to_A_selected"] is False, "A must not be promoted")
    require(verdict["observed_flavor_data_used"] is False, "observed data must not be used")
    require(verdict["next_required_artifact"] == NEXT_ARTIFACT, "wrong next artifact")

    require(
        packet["attempts"]["honest_routec_galerkin_fill"]["basis_transport"][
            "current_relative_transport"
        ]
        == "I_3",
        "current relative transport should be I_3",
    )
    require(
        "selected operator-source and overlap-tensor packet" in note
        and NEXT_ARTIFACT in note,
        "note must state next packet",
    )

    print("AUDIT_PASS: hybrid matter-slot Galerkin packet imported; selected source/overlap is next")


if __name__ == "__main__":
    main()
