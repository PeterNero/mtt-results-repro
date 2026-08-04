from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "routec_sourceemission_stability_chain_import_certificate.json"
STATUS = "ROUTEC_SOURCEEMISSION_STABILITY_CHAIN_IMPORTED_HYM_EXISTENCE_OPERATOR_VALUES_OPEN"
NEXT_ARTIFACT = "MTT_Selected_RouteC_HYM_OperatorValues_or_DERieszGreenDotD_Source_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["theorem"]["proved"] is True, "stability chain import should be proved")
    require(all(cert["input_checks"].values()), "input checks should pass")
    require(len(cert["imported_artifacts"]) == 8, "eight source artifacts should be imported")
    for artifact in cert["imported_artifacts"]:
        require(all(artifact["checks"].values()), f"checks failed for {artifact['name']}")

    final = cert["final_checks"]
    require(final["rank2_l2_h1_is_8"] is True, "rank-two H1 result missing")
    require(final["rank2_nonzero_ext_closed"] is True, "nonzero Ext closure missing")
    require(final["selected_equal_radius_metric_present"] is True, "selected equal-radius metric missing")
    require(final["equal_radius_stability_closed"] is True, "equal-radius stability closure missing")
    require(final["abstract_hym_existence_bridge_closed"] is True, "HYM bridge missing")
    require(final["operator_values_not_emitted"] is True, "operator values must remain open")

    verdict = cert["verdict"]
    require(verdict["abstract_HYM_existence_bridged"] is True, "abstract HYM bridge should close")
    require(verdict["selected_HYM_operator_values_emitted"] is False, "operator values must remain open")
    require(verdict["selected_A_selected_emitted"] is False, "A_selected must remain open")
    require(verdict["selected_b_selected_emitted"] is False, "b_selected must remain open")
    require(verdict["observed_flavor_data_used"] is False, "observed data must not be used")
    require(verdict["next_required_artifact"] == NEXT_ARTIFACT, "wrong next artifact")

    require(
        "rank-two L2 cohomology validates with h1 = 8" in note
        and "selected HYM connection/operator values" in note
        and NEXT_ARTIFACT in note,
        "note must record closure and next gate",
    )
    require(packet["theorem"]["proved"] is True, "packet theorem should be proved")

    print(
        "AUDIT_PASS: source-emission stability chain imported; selected HYM/operator values are next"
    )


if __name__ == "__main__":
    main()
