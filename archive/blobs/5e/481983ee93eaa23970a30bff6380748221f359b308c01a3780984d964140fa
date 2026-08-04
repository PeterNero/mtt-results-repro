"""Audit H/lambda empirical audit and strict source-upgrade packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_hlambdaempiricalaudit_or_strictsamebranchgaugeactionsourceupgrade"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
INPUT_LEDGER = PACKET_DIR / "h_lambda_input_provenance_ledger.packet.json"
EMPIRICAL_AUDIT = PACKET_DIR / "h_lambda_empirical_audit.packet.json"
PARAMETER_AUDIT = PACKET_DIR / "h_lambda_parameter_accounting.packet.json"
STRICT_UPGRADE = PACKET_DIR / "strict_samebranch_upgrade_workorder.packet.json"
NEXT_PACKET = PACKET_DIR / "next_strict_prefactor_or_fullsm_audit_contract.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HLambdaEmpiricalAudit_or_StrictSameBranchGaugeActionSourceUpgrade_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_HLAMBDAEMPIRICALAUDIT_OR_STRICTSAMEBRANCHGAUGEACTIONSOURCEUPGRADE_"
    "ONE_PRIMITIVE_AUDIT_CLOSED_STRICT_PREFACTOR_SOURCE_OPEN"
)
NEXT = "MTT_Selected_StrictPhysicalPrefactorSource_or_FullSMMinimalParameterAudit_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("closure_claimed") is True, f"{label} closure")
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    input_ledger = load(INPUT_LEDGER)
    empirical = load(EMPIRICAL_AUDIT)
    parameter = load(PARAMETER_AUDIT)
    strict = load(STRICT_UPGRADE)
    next_packet = load(NEXT_PACKET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("input_ledger", input_ledger),
        ("empirical", empirical),
        ("parameter", parameter),
        ("strict", strict),
        ("next", next_packet),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "cert status")
    require(data["next_required_artifact"] == NEXT, "next artifact")
    require(next_packet["next_required_artifact"] == NEXT, "next packet")
    require(data["theorem"]["proved"] is True, "theorem")
    require(data["minimal_one_primitive_H_lambda_empirical_audit_closed"] is True, "audit closed")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaim")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaim")

    decision = data["closure_decision"]
    require(decision["selected_R_H_RG_source_emitted"] is True, "R_H")
    require(decision["H_radial_parameter_count"] == 0, "H count")
    require(decision["one_physical_prefactor_primitive_count"] == 1, "prefactor count")
    require(decision["minimal_one_primitive_H_lambda_lane_closed"] is True, "minimal closed")
    require(decision["empirical_postcheck_passed"] is True, "postcheck")
    require(decision["lambda_H_used_as_selector"] is False, "lambda selector")
    require(decision["accepted_strict_samebranch_source_rows"] == 0, "strict rows")
    require(decision["strict_no_knob_H_lambda_closed"] is False, "strict overclaim")

    require(input_ledger["inputs"]["finite_H_scalar_source"]["parameter_count"] == 0, "input H count")
    require(input_ledger["inputs"]["P_EW_action_prefactor"]["parameter_count"] == 1, "input primitive count")
    require(input_ledger["forbidden_inputs_absent"]["lambda_H_as_selector"] is True, "lambda absent")

    require(empirical["postcheck"]["passes_roundoff_gate"] is True, "roundoff")
    require(empirical["prediction_classification"]["conditional_prediction_given_non_Higgs_prefactor"] is True, "conditional")
    require(empirical["prediction_classification"]["strict_no_knob_prediction"] is False, "strict prediction overclaim")

    budget = parameter["effective_H_lambda_lane"]
    require(budget["H_specific_free_parameters"] == 0, "budget H")
    require(budget["shared_physical_prefactor_primitives"] == 1, "budget primitive")
    require(budget["total_counted_parameters_for_this_lane"] == 1, "budget total")
    require(parameter["comparison_to_SM_parameter_bookkeeping"]["SM_treats_lambda_H_as_independent_input"] is True, "SM comparison")

    require(strict["accepted_strict_source_row_count"] == 0, "strict accepted")
    require(len(strict["upgrade_routes"]) == 2, "upgrade route count")

    for phrase in [
        "HLambdaEmpiricalAuditOrStrictSameBranchGaugeActionSourceUpgradeTheorem",
        "H radial parameters = 0",
        "physical prefactor primitives = 1",
        "`lambda_H` is not used as selector",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: H/lambda one-primitive empirical audit closed; strict "
        "same-branch prefactor/direct-K upgrade remains open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
