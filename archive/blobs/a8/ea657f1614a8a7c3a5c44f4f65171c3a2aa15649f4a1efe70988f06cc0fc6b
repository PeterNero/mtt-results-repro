from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "routec_source_overlap_packet_chain_import_certificate.json"
STATUS = "ROUTEC_SOURCE_OVERLAP_PACKET_CHAIN_IMPORTED_CURRENT_SCAFFOLD_NOGO"
NEXT_ARTIFACT = "MTT_Selected_RouteC_SourceEmission_MinimalSubpacket_AttackPlan_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["theorem"]["proved"] is True, "chain import theorem should be proved")
    require(all(cert["input_checks"].values()), "input checks should pass")
    require(len(cert["imported_artifacts"]) == 5, "five source artifacts should be imported")
    for artifact in cert["imported_artifacts"]:
        require(all(artifact["checks"].values()), f"checks failed for {artifact['name']}")

    final = cert["final_checks"]
    require(final["validator_rejects_current_packet"] is True, "validator rejection missing")
    require(final["seven_fields_required"] is True, "seven-field contract missing")
    require(final["no_selected_fields_emitted"] is True, "selected fields should not be emitted")
    require(final["support_shapes_present"] is True, "support shapes should be present")
    require(final["conditional_A_not_promoted"] is True, "A_selected must not be promoted")
    require(final["conditional_b_not_promoted"] is True, "b_selected must not be promoted")

    verdict = cert["verdict"]
    require(verdict["conditional_c1_routing_exact"] is True, "conditional route should be exact")
    require(verdict["conditional_normalization_exact"] is True, "conditional normalization should be exact")
    require(verdict["same_source_promotion_contract_built"] is True, "validator contract missing")
    require(verdict["current_same_source_fill_validates"] is False, "current fill must fail")
    require(verdict["selected_A_selected_emitted"] is False, "A_selected must remain open")
    require(verdict["selected_b_selected_emitted"] is False, "b_selected must remain open")
    require(verdict["observed_flavor_data_used"] is False, "observed data must not be used")
    require(verdict["next_required_artifact"] == NEXT_ARTIFACT, "wrong next artifact")

    require(
        "selected theorem-derived same-source fields = 0" in note
        and NEXT_ARTIFACT in note,
        "note must record no-go and next artifact",
    )
    require(len(packet["final_validator_errors"]) >= 7, "validator errors should be recorded")

    print(
        "AUDIT_PASS: source/overlap chain imported through same-source no-go; "
        "source-emission subpacket is next"
    )


if __name__ == "__main__":
    main()
