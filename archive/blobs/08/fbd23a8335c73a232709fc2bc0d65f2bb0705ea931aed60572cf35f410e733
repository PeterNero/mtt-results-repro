"""Audit H one-parameter execution ledger or strict finite-H source rows packet."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_honeparameterexecutionledger_or_strictfinitehsourcerows"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
EXECUTION_LEDGER = PACKET_DIR / "h_one_parameter_execution_ledger.packet.json"
STRICT_ROWS = PACKET_DIR / "strict_finite_h_source_rows_execution.packet.json"
CLAIM_BOUNDARY = PACKET_DIR / "claim_boundary_after_h_execution.packet.json"
NEXT_PACKET = PACKET_DIR / "next_strict_upgrade_or_nonhiggs_prediction.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HOneParameterExecutionLedger_or_StrictFiniteHSourceRows_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_HONEPARAMETEREXECUTIONLEDGER_OR_STRICTFINITEHSOURCEROWS_"
    "MINIMAL_H_CLOSED_STRICT_SOURCE_OPEN"
)
NEXT = "MTT_Selected_StrictFiniteHSourceRowConstruction_or_NonHiggsHRGPrediction_v1"


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
    ledger = load(EXECUTION_LEDGER)
    strict = load(STRICT_ROWS)
    boundary = load(CLAIM_BOUNDARY)
    next_packet = load(NEXT_PACKET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("ledger", ledger),
        ("strict", strict),
        ("boundary", boundary),
        ("next", next_packet),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "certificate status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(cert["next_required_artifact"] == NEXT, "certificate next")
    require(data["theorem"]["proved"] is True, "theorem")
    require(cert["theorem_proved"] is True, "certificate theorem")
    require(data["minimal_one_parameter_H_closure_claimed"] is True, "minimal H claim")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaim")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaim")

    parameter = ledger["adopted_parameter"]
    require(parameter["id"] == "UP-RET-OVERLAP.HRG", "parameter id")
    require(parameter["parameter_count_spent"] == 1, "parameter count")
    require(parameter["declared_before_this_execution"] is True, "declared before execution")
    require(parameter["retuned_per_observable"] is False, "retuned")
    require(math.isclose(parameter["derived_N_H"], parameter["value"] ** 2, abs_tol=1e-9), "N_H")

    executed = ledger["executed_result"]
    require(executed["minimal_one_parameter_H_closure_closed"] is True, "minimal H closed")
    require(executed["conditional_H_K_rows"] == 10, "conditional H rows")
    require(executed["strict_K_rows_without_parameter"] == 9, "strict K rows")
    require(executed["lambda_H_calibrated"] is True, "lambda calibrated")
    require(executed["lambda_H_predicted"] is False, "lambda predicted")
    require(math.isclose(executed["controlled_N_H"], executed["controlled_r_H"] ** 2, abs_tol=1e-9), "controlled N_H")

    scope = ledger["scope"]
    require(scope["H_threshold_row"] is True, "H scope")
    for key in ["all_SM_parameters", "Yukawa_or_CKM_or_masses", "nonHiggs_HRG_predictions"]:
        require(scope[key] is False, f"scope overclaim {key}")

    counts = strict["accepted_counts"]
    for key in [
        "accepted_strict_source_route_count",
        "accepted_value_row_count",
        "accepted_final_certificate_count",
        "accepted_direct_radial_hessian_value_rows",
        "same_source_connection_values_accepted",
    ]:
        require(counts[key] == 0, f"strict count {key}")
    for key, value in strict["row_slots"].items():
        require(value is False, f"strict row overemitted {key}")
    require(strict["strict_no_knob_source_closed"] is False, "strict source closed")

    claims = boundary["claims"]
    require(claims["minimal_one_parameter_H_closure"] is True, "boundary minimal")
    for key in [
        "strict_no_knob_H_closure",
        "lambda_H_prediction",
        "full_no_knob_SM_closure",
        "true_SM_equivalence",
    ]:
        require(claims[key] is False, f"boundary overclaim {key}")
    budget = boundary["parameter_budget"]
    require(budget["H_parameters_spent"] == 1, "H budget")
    require(budget["global_selected_universal_parameters_spent"] == 1, "global budget")
    require(budget["general_policy_selected_universal_parameter_count"] == 0, "general selected count")

    require(next_packet["next_required_artifact"] == NEXT, "next artifact")
    require("one counted H parameter executed" in next_packet["closed_here"], "closed here")
    require("strict selected finite-H/source rows" in next_packet["still_open"], "strict still open")

    decision = data["closure_decision"]
    require(decision["H_one_parameter_adopted_now"] is True, "decision adopted")
    require(decision["H_parameter_count_spent"] == 1, "decision parameter count")
    require(decision["minimal_one_parameter_H_closure_closed"] is True, "decision minimal")
    require(decision["conditional_H_K_rows_closed"] == 10, "decision H rows")
    require(decision["strict_H_K_rows_without_parameter"] == 9, "decision strict K")
    require(math.isclose(decision["controlled_N_H"], decision["controlled_r_H"] ** 2, abs_tol=1e-9), "decision N_H")
    require(decision["lambda_H_calibrated"] is True, "decision lambda calibrated")
    require(decision["strict_finite_H_source_rows_executed"] is True, "decision strict executed")
    for key in [
        "lambda_H_predicted",
        "strict_finite_H_source_closed",
        "full_no_knob_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"decision overclaim {key}")
    require(decision["strict_value_rows_accepted"] == 0, "decision strict rows")
    require(decision["accepted_nonhiggs_HRG_prediction_targets"] == 0, "decision non-Higgs")
    require(decision["hlambda_controlled_one_parameter_10of10_imported"] is True, "H lambda import")

    for phrase in [
        "HOneParameterExecutionLedgerOrStrictFiniteHSourceRowsTheorem",
        "parameter count spent: `1`",
        "conditional H K rows: `10/10`",
        "strict source rows accepted: `0`",
        "does not predict `lambda_H`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: one-parameter H execution ledger closed; strict finite-H source rows remain zero."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
