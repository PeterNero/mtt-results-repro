"""Audit combined K-threshold grammar and conditional scalar closure."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_combinedthresholdkernelkrows_sourcetheorem"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
GRAMMAR = PACKET_DIR / "closed_source_k_threshold_grammar.packet.json"
ATTEMPT = PACKET_DIR / "selected_k_threshold_source_theorem_attempt.packet.json"
CONDITIONAL = PACKET_DIR / "conditional_k_rows_scalar_closure_theorem.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_k_source_theorem_attempt.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_CombinedThresholdKernelKRows_SourceTheorem_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_COMBINEDTHRESHOLDKERNELKROWS_SOURCETHEOREM_"
    "BUILT_CONDITIONAL_CLOSURE_SOURCE_THEOREM_OPEN"
)
NEXT = "MTT_Selected_KThresholdFunctionalFromHYMThresholdAction_or_ControlledEmpiricalKImport_v1"
REQUIRED_COLUMNS = {
    "theta_exponent",
    "qutrit_floor",
    "shared_h_index",
    "phase_column",
    "shift_column",
    "mixed_slot",
    "family_sector",
    "H_sector",
    "log_reduced_heat_trace",
}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector violation")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting violation")
    require(packet.get("closure_claimed") is True, f"{label} should close its local theorem")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    grammar = load(GRAMMAR)
    attempt = load(ATTEMPT)
    conditional = load(CONDITIONAL)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("certificate", cert),
        ("grammar", grammar),
        ("source attempt", attempt),
        ("conditional theorem", conditional),
        ("cutset", cutset),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "candidate theorem should be conditional/local")
    require(cert["theorem_proved"] is True, "certificate theorem should be conditional/local")
    require(data["full_no_knob_closure_claimed"] is False, "full no-knob overclaim")
    require(data["true_SM_equivalence_claimed"] is False, "true SM equivalence overclaim")
    require(cert["full_no_knob_closure_claimed"] is False, "certificate full no-knob overclaim")
    require(cert["true_SM_equivalence_claimed"] is False, "certificate true SM overclaim")

    decision = data["closure_decision"]
    require(decision["closed_source_K_grammar_built"] is True, "K grammar not built")
    require(decision["conditional_K_rows_scalar_closure_proved"] is True, "conditional theorem not proved")
    require(decision["selected_FK_functional_proved"] is False, "F_K overaccepted")
    require(decision["accepted_combined_K_source_row_count"] == 0, "K source rows overaccepted")
    require(decision["accepted_internal_scalar_value_row_count"] == 0, "scalar rows overaccepted")
    require(decision["lambda_H_value_row_emitted"] is False, "lambda_H overemitted")
    require(decision["controlled_empirical_K_import_available"] is True, "empirical K import unavailable")
    require(
        decision["controlled_empirical_K_import_selected_for_no_knob"] is False,
        "empirical K promoted to no-knob",
    )
    require(decision["true_SM_equivalence_closed"] is False, "true SM closure overclaimed")
    require(decision["full_no_knob_closed"] is False, "full no-knob closure overclaimed")

    require(grammar["status"] == "CLOSED_SOURCE_GRAMMAR_AVAILABLE_FUNCTIONAL_NOT_SELECTED", "grammar status mismatch")
    require(grammar["row_count"] == 10, "grammar row count mismatch")
    require(set(grammar["available_grammar_columns"]) == REQUIRED_COLUMNS, "grammar columns mismatch")
    require(grammar["selected_numerical_K_functional_present"] is False, "numerical F_K overaccepted")
    require(grammar["accepted_combined_K_source_row_count"] == 0, "grammar overaccepted K rows")
    for key in [
        "theta_exponent_rows_closed",
        "finite_heat_response_closed",
        "K_product_contract_closed",
        "source_feature_table_closed",
    ]:
        require(grammar["closed_source_inputs"][key] is True, f"closed source input missing: {key}")
    for row in grammar["grammar_rows"]:
        require(set(row["closed_features_available_before_replay"]) == REQUIRED_COLUMNS, f"{row['omega_id']} columns mismatch")
        require(row["internal_selected_K_row_accepted"] is False, f"{row['omega_id']} K row overaccepted")
        require(row["empirical_K_import_available"] is True, f"{row['omega_id']} empirical K import missing")
        require(row["observed_data_used_as_selector"] is False, f"{row['omega_id']} observed selector violation")
        require(row["target_fitting_used"] is False, f"{row['omega_id']} target fitting violation")
        require(
            "grammar contains no selected numerical functional F_K" in row["why_grammar_does_not_select_value"],
            f"{row['omega_id']} missing F_K blocker",
        )

    require(attempt["candidate_theorem"]["proved_now"] is False, "source theorem overproved")
    require(attempt["closed_support_sufficient_for_slots"] is True, "slot support should close")
    require(attempt["closed_support_sufficient_for_values"] is False, "value support overclaimed")
    require(attempt["accepted_combined_K_source_row_count"] == 0, "attempt overaccepted K rows")
    require(attempt["accepted_internal_scalar_value_row_count"] == 0, "attempt overaccepted scalar rows")
    require(attempt["lambda_H_value_row_emitted"] is False, "attempt emitted lambda_H")
    require(
        "empirical K rows are controlled import data, not selected source rows" in attempt["why_not_proved"],
        "attempt missing empirical-import guard",
    )

    require(
        conditional["status"] == "CONDITIONAL_SCALAR_CLOSURE_PROVED_ANTECEDENT_OPEN",
        "conditional status mismatch",
    )
    require(conditional["antecedent"]["selected_K_threshold_row_count_required"] == 10, "antecedent required count")
    require(conditional["antecedent"]["selected_K_threshold_row_count_present"] == 0, "antecedent present count")
    require(conditional["antecedent"]["satisfied"] is False, "antecedent incorrectly satisfied")
    require(conditional["consequent_if_satisfied"]["strict_Omega_rows_executable"] is True, "strict Omega implication")
    require(conditional["consequent_if_satisfied"]["lambda_H_row_executable"] is True, "lambda_H implication")
    require(conditional["consequent_current"]["strict_Omega_rows_executable"] is False, "current Omega overclaim")
    require(conditional["consequent_current"]["lambda_H_row_executable"] is False, "current lambda_H overclaim")
    require(
        conditional["empirical_import_can_satisfy_antecedent_for_no_knob"] is False,
        "empirical import satisfied no-knob antecedent",
    )
    require(conditional["controlled_empirical_K_import_available"] is True, "controlled empirical K unavailable")

    require(cutset["next_required_artifact"] == NEXT, "cutset next mismatch")
    for phrase in [
        "closed source grammar for all ten K_threshold slots emitted",
        "conditional theorem proved: selected ten K rows imply scalar Omega execution",
        "current closed support shown insufficient to select numerical K values",
        "empirical K import retained only as controlled non-no-knob layer",
    ]:
        require(phrase in cutset["closed_here"], f"cutset closed_here missing {phrase}")
    for phrase in [
        "selected functional F_K from same-branch HYM/threshold action",
        "ten selected K_threshold numerical rows",
        "selected H-sector K row/lambda_H execution",
        "matrix-level CKM/offdiagonal mixing extension",
        "full no-knob SM closure",
    ]:
        require(phrase in cutset["still_open"], f"cutset still_open missing {phrase}")
    for phrase in [
        "choose F_K coefficients from empirical K residuals",
        "promote controlled empirical K import to no-knob",
        "use row-id lookup as a source theorem",
        "reopen D_fin or theta exponents as if they were the K-value blocker",
    ]:
        require(phrase in cutset["forbidden_routes"], f"cutset forbidden_routes missing {phrase}")

    for phrase in [
        "selected numerical F_K functional : false",
        "accepted K source rows            : 0",
        "F_K : closed K grammar -> (K_threshold.Omega_i)_i",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
