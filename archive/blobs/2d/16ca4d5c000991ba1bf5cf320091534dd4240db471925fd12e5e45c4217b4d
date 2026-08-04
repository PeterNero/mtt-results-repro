"""Audit strict finite-H action source or UP-RET-OVERLAP.HRG cross-use theorem."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_strictfinitehactionsource_or_upretoverlaphrgcrossuse"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
STRICT_SOURCE_PACKET = PACKET_DIR / "strict_finite_h_source_verdict.packet.json"
CROSSUSE_PACKET = PACKET_DIR / "up_ret_overlap_hrg_crossuse_verdict.packet.json"
DECISION_PACKET = PACKET_DIR / "frontier_exit_decision.packet.json"
BLOCKER_PACKET = PACKET_DIR / "blocker_closure_contract.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_StrictFiniteHActionSource_or_UPRetOverlapHRGCrossUse_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_STRICTFINITEHACTIONSOURCE_OR_UPRETOVERLAPHRGCROSSUSE_"
    "DECISION_CLOSED_STRICT_SOURCE_OPEN_ONE_PARAMETER_ALLOWED"
)
NEXT = "MTT_Selected_HOneParameterAdoptionPolicy_or_FiniteHSourceConstruction_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("closure_claimed") is True, f"{label} closure flag")
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    strict = load(STRICT_SOURCE_PACKET)
    crossuse = load(CROSSUSE_PACKET)
    decision_packet = load(DECISION_PACKET)
    blocker = load(BLOCKER_PACKET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("strict", strict),
        ("crossuse", crossuse),
        ("decision", decision_packet),
        ("blocker", blocker),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "certificate status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(cert["next_required_artifact"] == NEXT, "certificate next")
    require(data["theorem"]["proved"] is True, "theorem")
    require(cert["theorem_proved"] is True, "certificate theorem")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaim")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaim")

    routes = strict["strict_source_routes_tested"]
    for key in [
        "selected_F_H_functional_emitted",
        "selected_M_source_value_emitted",
        "selected_K_H_emitted",
        "selected_H_response_value_rows_emitted",
        "strict_N_H_value_emitted",
        "strict_r_H_source_emitted",
        "strict_R_H_RG_source_constructed",
    ]:
        require(routes[key] is False, f"strict route overemitted {key}")

    counts = strict["accepted_counts"]
    for key in [
        "accepted_strict_source_route_count",
        "accepted_value_row_count",
        "accepted_final_certificate_count",
        "accepted_direct_radial_hessian_value_rows",
        "same_source_connection_values_accepted",
    ]:
        require(counts[key] == 0, f"strict accepted count {key}")
    require(strict["strict_no_knob_exit_closed"] is False, "strict no-knob closed")

    primitive = crossuse["primitive"]
    require(primitive["id"] == "UP-RET-OVERLAP.HRG", "primitive id")
    require(primitive["new_parameter_count_if_adopted"] == 1, "parameter count")
    require(math.isclose(primitive["N_H"], primitive["value"] ** 2, abs_tol=1e-9), "N_H")

    support = crossuse["controlled_support"]
    require(support["controlled_one_parameter_radial_layer_closed"] is True, "controlled radial")
    require(support["controlled_conditional_K_row_count"] == 10, "controlled K rows")
    require(support["controlled_crossuse_prediction_validated_internally"] is True, "internal crossuse")
    require(support["same_HRG_parameter_reused_without_retuning"] is True, "same parameter")

    rejection = crossuse["strict_crossuse_rejection"]
    require(rejection["accepted_nonhiggs_prediction_target_count"] == 0, "non-Higgs count")
    require(rejection["RO_value_source_derived"] is False, "RO value source")
    require(rejection["same_HRG_nonHiggs_map_accepted"] is False, "same HRG map")
    require(rejection["UP_RET_OVERLAP_HRG_admitted_as_universal"] is False, "universal admitted")
    require(rejection["lambda_H_predicted"] is False, "lambda predicted")
    require(crossuse["minimal_parameter_exit_allowed"] is True, "minimal allowed")
    require(crossuse["minimal_parameter_exit_is_no_knob"] is False, "minimal no-knob")

    require(decision_packet["status"] == "DECISION_LAYER_CLOSED_TWO_HONEST_EXITS", "decision")
    require(len(decision_packet["honest_exits"]) == 2, "two exits")
    require(decision_packet["honest_exits"][0]["mode"] == "strict_no_knob", "strict exit")
    require(decision_packet["honest_exits"][1]["mode"] == "minimal_parameter", "parameter exit")
    require(
        decision_packet["honest_exits"][0]["counts_as_true_SM_no_knob"] is True,
        "strict counts",
    )
    require(
        decision_packet["honest_exits"][1]["counts_as_true_SM_no_knob"] is False,
        "parameter no-knob",
    )
    for phrase in [
        "controlled HRG calibration counted as lambda_H prediction",
        "controlled 10/10 H K layer counted as no-knob",
        "internal dynamic-C1 cross-use counted as non-Higgs prediction",
        "same-source support labels counted as connection values",
    ]:
        require(phrase in decision_packet["forbidden_replays"], f"forbidden {phrase}")

    require(blocker["status"] == "BLOCKER_DECISION_CLOSED_VALUE_SOURCE_STILL_OPEN", "blocker")
    require("strict selected finite-H value source" in blocker["still_open"], "strict still open")
    require(
        "policy decision to adopt exactly one calibrated H parameter" in blocker["still_open"],
        "policy still open",
    )

    decision = data["closure_decision"]
    require(decision["decision_layer_closed"] is True, "decision closed")
    for key in [
        "strict_finite_H_source_closed",
        "strict_N_H_value_emitted",
        "strict_r_H_source_emitted",
        "strict_R_H_RG_source_constructed",
        "UP_RET_OVERLAP_HRG_universal_admitted",
        "minimal_one_parameter_H_layer_is_no_knob",
        "lambda_H_predicted",
        "strict_H_K_threshold_row_emitted",
        "full_no_knob_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"decision overclosed {key}")
    require(decision["accepted_nonhiggs_HRG_prediction_targets"] == 0, "accepted HRG targets")
    require(decision["strict_F_H_M_source_K_H_rows_accepted"] == 0, "strict rows")
    require(decision["minimal_one_parameter_H_layer_available"] is True, "one parameter available")
    require(
        decision["minimal_one_parameter_H_layer_closes_conditional_H_K"] is True,
        "conditional H K",
    )
    require(decision["lambda_H_calibrated"] is True, "lambda calibrated")
    require(math.isclose(decision["controlled_N_H"], decision["controlled_r_H"] ** 2, abs_tol=1e-9), "decision N_H")

    for phrase in [
        "StrictFiniteHActionSourceOrUPRetOverlapHRGCrossUseTheorem",
        "strict finite-H/source accepted value rows: `0`",
        "accepted non-Higgs `UP-RET-OVERLAP.HRG` targets: `0`",
        "controlled one-parameter H layer available: `true`",
        "does **not** close strict no-knob SM equivalence",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: strict H source/cross-use decision layer closed; "
        "strict no-knob remains open and one-parameter H lane is explicit."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
