from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_connection_witness_contract_certificate.json"
STATUS = "POST_ALPHA_CONNECTION_WITNESS_CONTRACT_IMPORTED_VALUES_OPEN"
NEXT = "Selected_U1Y_RouteC_FiniteHYMConnectionSolve_or_TypedCechPayload_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "must not claim closure")
    require(cert["selected_connection_witness_constructed"] is False, "must not construct witness")
    require(cert["reduced_to"] == NEXT, "wrong reduction target")
    require(all(cert["checks"].values()), "all certificate checks should pass")

    require(packet["theorem"]["proved"] is True, "theorem should be proved")
    require(packet["branch"]["q"] == 79, "wrong q")
    require(packet["branch"]["orientation"] == "F", "wrong orientation")
    require(packet["branch"]["torsion_label_m"] == 1, "wrong torsion label")
    require(packet["branch"]["antiunitary_partner_retained"] is True, "antiunitary partner should be retained")

    routes = packet["witness_routes"]
    require(set(routes) == {"typed_monad_cech", "direct_hym", "finite_routec_solve"}, "wrong witness routes")
    require(packet["payload_counts"]["typed_monad_cech_missing"] == 9, "wrong typed payload count")
    require(packet["payload_counts"]["direct_hym_missing"] == 6, "wrong HYM payload count")
    require(packet["payload_counts"]["finite_routec_solve_missing"] == 10, "wrong finite payload count")
    require(packet["payload_counts"]["same_source_missing"] == 4, "wrong same-source payload count")

    payload = packet["open_payload"]
    require(payload["status"] == "OPEN_VALUES_REQUIRED", "payload should be open")
    for section in ["typed_monad_cech_payload", "direct_hym_payload", "finite_routec_solve_payload"]:
        require(all(value is None for value in payload[section].values()), f"{section} should be empty")
    same_source = payload["same_source_requirements"]
    require(same_source["no_lifted_selected_flags"] is True, "no-lift guardrail missing")
    require(same_source["no_observed_or_benchmark_inputs"] is True, "target guardrail missing")
    require(same_source["source_certificate"] is None, "source certificate should be absent")

    blocked = packet["blocked_current_attempts"]
    require(blocked["typed_monad_cech"]["status"] == "REJECTED_AS_WITNESS", "typed route should be rejected as witness")
    require(blocked["direct_selected_hym_connection"]["status"] == "ABSTRACT_EXISTENCE_ONLY", "HYM route should be abstract only")
    require(blocked["routec_smoke_promotion"]["status"] == "CANNOT_PROMOTE_SMOKE_TO_SELECTED_WITNESS", "smoke route should not promote")
    require(all(entry["constructed"] is False for entry in blocked.values()), "blocked attempts should construct nothing")

    finite = packet["finite_prefix_support"]
    require(finite["dimension"] == 27, "finite prefix should be 27-mode")
    require(finite["DE_emitted"] is True, "DE support should be present")
    require(finite["dotD_alpha1_emitted"] is True, "dotD support should be present")
    require(finite["selected_by_mtt"] is False, "finite prefix must not be selected")

    require(packet["next_required_artifact"] == NEXT, "wrong next artifact")
    require(all(packet["what_closes_now"].values()), "closure flags should pass")
    require(all(packet["what_remains_open"].values()), "open flags should remain")
    require(all(packet["guardrails"].values()), "guardrails should hold")
    require(STATUS in note and NEXT in note and "29 required leaves" in note, "note missing essentials")

    print("AUDIT_PASS: selected connection witness contract imported; payload values remain open")


if __name__ == "__main__":
    main()
