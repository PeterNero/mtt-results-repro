"""Audit selected threshold-delta rows or lambda_H payload execution."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_thresholddeltarows_or_lambdahpayloadexecution"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
NULL_THEOREM = PACKET_DIR / "source_native_null_threshold_delta_theorem.packet.json"
T_ROWS = PACKET_DIR / "charged_source_native_tscheme_rows.packet.json"
K_ROWS = PACKET_DIR / "charged_kthreshold_rows_after_null_delta.packet.json"
FULL_GATE = PACKET_DIR / "ten_kthreshold_gate_after_charged_null_delta.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_threshold_delta_rows.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_ThresholdDeltaRows_or_LambdaHPayloadExecution_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_THRESHOLDDELTAROWS_OR_LAMBDAHPAYLOADEXECUTION_"
    "CLOSED_CHARGED_NULL_DELTA_ROWS_H_LAMBDA_OPEN"
)
NEXT = "MTT_Selected_LambdaHPayloadExecution_or_TenKThresholdClosure_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def require_close(value: float, expected: float, message: str) -> None:
    require(abs(float(value) - expected) < 1e-12, message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector violation")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting violation")
    require(packet.get("closure_claimed") is True, f"{label} should close its local theorem/gate")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    null_theorem = load(NULL_THEOREM)
    t_rows = load(T_ROWS)
    k_rows = load(K_ROWS)
    full_gate = load(FULL_GATE)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("certificate", cert),
        ("null theorem", null_theorem),
        ("T rows", t_rows),
        ("K rows", k_rows),
        ("full gate", full_gate),
        ("cutset", cutset),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "candidate theorem missing")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaim")
    require(data["full_no_knob_closure_claimed"] is False, "full no-knob overclaim")

    decision = data["closure_decision"]
    require(decision["source_native_null_threshold_delta_theorem_emitted"] is True, "null theorem not emitted")
    require(decision["selected_zero_delta_row_count_emitted"] == 9, "zero-delta row count mismatch")
    require(decision["selected_T_scheme_source_row_count"] == 9, "T_scheme row count mismatch")
    require(decision["accepted_selected_charged_K_threshold_row_count"] == 9, "charged K count mismatch")
    require(decision["accepted_selected_K_source_row_count"] == 9, "selected K count mismatch")
    require(decision["selected_lambda_H_payload_emitted"] is False, "lambda_H overemitted")
    require(decision["full_ten_row_K_threshold_closure"] is False, "ten-row K overclosed")
    require(decision["accepted_internal_scalar_value_row_count"] == 0, "scalar rows overaccepted")
    require(decision["true_SM_equivalence_closed"] is False, "true SM closure overclaimed")
    require(decision["full_no_knob_closed"] is False, "full no-knob closure overclaimed")

    require(
        null_theorem["status"] == "SOURCE_NATIVE_NULL_THRESHOLD_DELTA_THEOREM_CLOSED_FOR_CHARGED_ROWS",
        "null theorem status mismatch",
    )
    require(null_theorem["closure_claimed"] is True, "null theorem not closed")
    clauses = null_theorem["proof_clauses"]
    for key in [
        "same_branch_scale_scheme_loop_convention_closed",
        "post_pi_formal_convention_source_contract_closed",
        "threshold_functional_contract_emitted",
        "external_import_lane_is_admitted_replay_only",
        "charged_zero_delta_obligations_previously_identified",
        "source_native_identity_not_external_threshold_vanishing",
    ]:
        require(clauses[key] is True, f"null theorem proof clause missing {key}")
    require(clauses["external_rows_used_as_branch_selector"] is False, "external rows promoted")
    require(
        clauses["selected_threshold_response_functional_instantiated"] is False,
        "threshold functional overinstantiated",
    )
    scope = null_theorem["scope"]
    require(scope["charged_source_native_rows_closed"] == ["u", "d", "e"], "charged scope mismatch")
    require(scope["row_count"] == 9, "null theorem row count mismatch")
    require(scope["external_threshold_mass_profile_replay_rows_closed_as_no_knob"] is False, "external rows overclosed")
    require(scope["H_lambda_sector_closed"] is False, "H/lambda overclosed")
    require(scope["full_ten_K_threshold_closure"] is False, "ten K overclosed in scope")
    require(scope["strict_Omega_lambda_scalar_execution_closed"] is False, "strict scalar execution overclosed")
    require("does not assert that physical threshold corrections" in null_theorem["guardrail"], "guardrail missing")

    expected_by_gen = {1: 1.367835979172, 2: 0.683917989586, 3: 0.683917989586}
    expected_slots = {(sector, gen) for sector in ["u", "d", "e"] for gen in [1, 2, 3]}

    require(t_rows["status"] == "NINE_CHARGED_SOURCE_NATIVE_TSCHEME_ROWS_EMITTED", "T packet status")
    require(t_rows["row_count"] == 9, "T row count mismatch")
    require(t_rows["selected_T_scheme_source_row_count"] == 9, "selected T count mismatch")
    require(t_rows["source_native_null_delta_theorem_emitted"] is True, "T packet theorem flag missing")
    require({(row["sector"], row["generation"]) for row in t_rows["rows"]} == expected_slots, "T slots missing")
    for row in t_rows["rows"]:
        require(row["Delta_threshold_source_native"] == 0.0, f"{row['omega_id']} threshold delta")
        require(row["Delta_mass_source_native"] == 0.0, f"{row['omega_id']} mass delta")
        require(row["Delta_profile_source_native"] == 0.0, f"{row['omega_id']} profile delta")
        require(row["zero_delta_sum"] == 0.0, f"{row['omega_id']} zero sum")
        require(row["T_scheme_source_native"] == 1.0, f"{row['omega_id']} T value")
        require(row["source_native_null_delta_theorem_used"] is True, f"{row['omega_id']} theorem flag")
        require(row["selected_as_source_native_T_scheme_row"] is True, f"{row['omega_id']} selected T flag")
        require(row["external_replay_threshold_rows_promoted"] is False, f"{row['omega_id']} external replay promoted")
        require(row["observed_data_used_as_selector"] is False, f"{row['omega_id']} observed selector")
        require(row["target_fitting_used"] is False, f"{row['omega_id']} target fitting")

    require(k_rows["status"] == "NINE_CHARGED_KTHRESHOLD_ROWS_EMITTED_H_ROW_OPEN", "K packet status")
    require(k_rows["row_count"] == 9, "K row count mismatch")
    require(k_rows["accepted_selected_charged_K_threshold_row_count"] == 9, "accepted charged K count")
    require(k_rows["accepted_full_ten_row_K_threshold_row_count"] == 0, "full K rows overaccepted")
    require(k_rows["selected_lambda_H_payload_emitted"] is False, "lambda overemitted in K packet")
    require({(row["sector"], row["generation"]) for row in k_rows["rows"]} == expected_slots, "K slots missing")
    for row in k_rows["rows"]:
        require_close(
            row["selected_K_threshold_source_value"],
            expected_by_gen[row["generation"]],
            f"{row['omega_id']} K value mismatch",
        )
        require_close(
            row["selected_strict_L_rowlocal_value"],
            expected_by_gen[row["generation"]],
            f"{row['omega_id']} L value mismatch",
        )
        require(row["selected_T_scheme_source_native"] == 1.0, f"{row['omega_id']} T source value")
        require(row["formula"] == "K_threshold_i = L_rowlocal_i * T_scheme_i = L_rowlocal_i", "K formula")
        require(row["accepted_as_selected_charged_K_threshold_row"] is True, f"{row['omega_id']} K not accepted")
        require(row["accepted_as_full_ten_row_K_closure"] is False, f"{row['omega_id']} full K overaccepted")
        require(row["lambda_H_payload_required_for_full_closure"] is True, f"{row['omega_id']} lambda blocker lost")
        require(row["observed_data_used_as_selector"] is False, f"{row['omega_id']} observed selector")
        require(row["target_fitting_used"] is False, f"{row['omega_id']} target fitting")

    require(
        full_gate["status"] == "CHARGED_K_ROWS_CLOSED_H_LAMBDA_ROW_STILL_BLOCKS_TEN_ROW_CLOSURE",
        "full gate status mismatch",
    )
    require(full_gate["row_count"] == 10, "full gate row count mismatch")
    require(full_gate["accepted_selected_charged_K_threshold_row_count"] == 9, "full gate charged count")
    require(full_gate["accepted_selected_K_source_row_count"] == 9, "full gate selected K count")
    require(full_gate["selected_K_threshold_row_count_required_for_full_scalar_execution"] == 10, "required K count")
    require(full_gate["full_ten_row_K_threshold_closure"] is False, "full ten K overclosed")
    require(full_gate["selected_lambda_H_payload_emitted"] is False, "lambda payload overemitted")
    require(full_gate["accepted_internal_scalar_value_row_count"] == 0, "scalar rows overaccepted")
    h_row = full_gate["h_lambda_row"]
    require(h_row["omega_id"] == "Omega_H.lambda", "H omega mismatch")
    require(h_row["selected_K_threshold_row_emitted"] is False, "H K overemitted")
    require(h_row["selected_lambda_H_payload_emitted"] is False, "H lambda overemitted")
    require("selected lambda_H H-sector payload is not emitted" in h_row["blocking_reasons"], "H blocker missing")
    current = full_gate["conditional_full_scalar_closure_current"]
    require(current["antecedent_satisfied"] is False, "conditional antecedent overclosed")
    require(current["selected_K_threshold_row_count_present"] == 9, "current K count mismatch")
    require(current["selected_K_threshold_row_count_required"] == 10, "required K count mismatch")
    require(current["strict_Omega_rows_executable"] is False, "Omega execution overclosed")
    require(current["lambda_H_row_executable"] is False, "lambda execution overclosed")

    require(cutset["next_required_artifact"] == NEXT, "cutset next mismatch")
    for phrase in [
        "SourceNativeNullThresholdDeltaTheorem proved for charged rows",
        "nine selected source-native T_scheme rows emitted with value 1",
        "nine charged K_threshold source rows emitted from strict L_rowlocal times source-native identity",
        "external threshold/mass/profile replay rows remain downstream and are not promoted as selectors",
    ]:
        require(phrase in cutset["closed_here"], f"cutset closed missing {phrase}")
    for phrase in [
        "selected lambda_H H-sector quartic/threshold payload",
        "H-sector K_threshold.Omega_H.lambda row",
        "ten-row K_threshold antecedent for strict Omega/lambda_H scalar execution",
        "strict Omega/lambda_H scalar execution",
        "matrix-level mixing extension and true SM equivalence",
    ]:
        require(phrase in cutset["still_open"], f"cutset open missing {phrase}")

    for phrase in [
        "SourceNativeNullThresholdDeltaTheorem",
        "selected charged zero-delta rows: `9`",
        "selected charged source-native `T_scheme` rows: `9`",
        "selected charged `K_threshold` rows: `9`",
        "It does not claim physical threshold corrections vanish.",
        "- u.gen1: 1.367835979172",
        "- d.gen2: 0.683917989586",
        "- e.gen3: 0.683917989586",
        "selected `lambda_H` H-sector quartic/threshold payload: `false`",
        "full ten-row `K_threshold` closure: `false`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
