from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "core_b0_factorization_final_gate_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")
    sources = cert["source_tests"]
    false_routes = cert["false_closure_routes"]
    packet = cert["final_packet"]
    decision = cert["decision"]
    guards = cert["guardrails"]

    require(cert["status"] == "FINAL_B0_FACTORISATION_GATE_EXPLICIT_NOT_CLOSED", "unexpected status")
    require(sources["shape_map_core_B0_exists"] is True, "shape-map core B0 should exist")
    require(sources["shape_map_core_B0_formula_sourced"] is True, "shape-map core formula should be sourced")
    require(sources["spectral_filter_B0_positive_commuting_exists"] is True, "filter B0 clue missing")
    require(sources["spectral_filter_B0_is_not_shape_map_core"] is True, "filter/shape distinction missing")
    require(sources["central_circle_shared_gravity_sourced"] is True, "central gravity clue missing")
    require(sources["central_circle_finite_holonomy_sourced"] is True, "central finite holonomy missing")
    require(sources["literal_B0_to_UTT_factorization_absent"] is True, "literal B0 factorization unexpectedly sourced")
    require(sources["literal_same_angle_B0_absent"] is True, "same-angle B0 unexpectedly sourced")

    for name, route in false_routes.items():
        require(route["tempting"] is True, f"{name} should be tempting")
        require(route["valid_for_final_shape_support"] is False, f"{name} must not close final support")
        require("reason" in route and route["reason"], f"{name} needs reason")

    require(packet["name"] == "SelectedCoreB0TTFactorizationPacket.v1", "wrong final packet")
    require(packet["operator_to_compute"] == "B0^*P_TT", "wrong operator")
    require(packet["closing_tests"]["rank_test"] == "rank(U_TT^* B0^*P_TT)=2", "rank test missing")
    require(packet["closing_tests"]["no_leakage_test"] == "(I-Pi_exact64)B0^*P_TT=0", "leakage test missing")
    require("S_64" in packet["closing_tests"]["same_angle_test"], "same-angle test missing")
    require("lambda_GR,TT=15" in packet["if_passes"][-1], "lambda consequence missing")

    require(decision["final_support_closed_now"] is False, "must not close final support")
    require(decision["honest_status"] == "FINAL_GATE_IS_EXPLICIT_CORE_B0_PACKET_NOT_YET_FILLED", "wrong honest status")

    require(guards["claims_final_support_closed"] is False, "must not claim final support")
    require(guards["uses_filter_B0_as_shape_B0"] is False, "must not conflate B0s")
    require(guards["uses_central_circle_interpretation_as_matrix_proof"] is False, "must not overuse central text")
    require(guards["uses_observed_GR_data"] is False, "must not use observed data")
    require(guards["adds_numeric_knob"] is False, "must not add knob")

    require("not honestly closed yet" in note, "note should be honest")
    require("Final Packet" in note, "note should include final packet")
    print("AUDIT_PASS: final B0 factorization gate explicit and not overclaimed")


if __name__ == "__main__":
    main()
