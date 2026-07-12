"""Audit internal threshold response value rows / external import decision."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_internalthresholdresponsefunctionalvaluerows_or_externalsourceimportdecision"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
INTERNAL_GATE = PACKET_DIR / "internal_threshold_response_value_row_gate.packet.json"
ROW_LEDGER = PACKET_DIR / "ten_row_internal_external_source_decision_ledger.packet.json"
EXTERNAL_DECISION = PACKET_DIR / "controlled_external_source_import_decision.packet.json"
WORKORDER = PACKET_DIR / "source_selected_threshold_functional_execution_workorder.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_internal_external_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_InternalThresholdResponseFunctionalValueRows_or_ExternalSourceImportDecision_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_INTERNALTHRESHOLDRESPONSEFUNCTIONALVALUEROWS_OR_EXTERNALSOURCEIMPORTDECISION_"
    "BUILT_DECISION_BOUNDARY_INTERNAL_ROWS_OPEN"
)
NEXT = "MTT_Selected_LRowlocalTSchemeLambdaH_SourceExecution_or_ControlledEmpiricalImport_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector violation")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting violation")
    require(packet.get("closure_claimed") is True, f"{label} should close its boundary theorem")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    internal_gate = load(INTERNAL_GATE)
    row_ledger = load(ROW_LEDGER)
    external_decision = load(EXTERNAL_DECISION)
    workorder = load(WORKORDER)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("certificate", cert),
        ("internal gate", internal_gate),
        ("row ledger", row_ledger),
        ("external decision", external_decision),
        ("workorder", workorder),
        ("cutset", cutset),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "candidate theorem missing")
    require(cert["theorem_proved"] is True, "certificate theorem missing")

    decision = data["closure_decision"]
    require(decision["ten_row_decision_ledger_built"] is True, "row ledger not built")
    require(decision["controlled_empirical_layer_policy_built"] is True, "external policy not built")
    require(decision["source_selected_execution_workorder_built"] is True, "workorder not built")
    require(decision["internal_threshold_response_value_rows_emitted"] is False, "internal rows overemitted")
    require(decision["accepted_internal_scalar_value_row_count"] == 0, "internal rows overaccepted")
    require(decision["accepted_threshold_scheme_value_row_count"] == 0, "threshold rows overaccepted")
    require(decision["accepted_omega_source_row_count"] == 0, "omega rows overaccepted")
    require(decision["lambda_H_value_row_emitted"] is False, "lambda_H overemitted")
    require(decision["external_source_import_available_at_admitted_replay_tier"] is True, "external lane missing")
    require(decision["external_source_import_selected_for_no_knob"] is False, "external import promoted")
    require(decision["full_no_knob_closed"] is False, "no-knob overclosed")
    require(decision["true_SM_equivalence_closed"] is False, "true SM overclosed")

    require(internal_gate["readiness_fraction"] == "8/9", "readiness fraction mismatch")
    require(
        internal_gate["only_remaining_readiness_blocker"] == "no_knob_value_derivation",
        "wrong readiness blocker",
    )
    require(internal_gate["accepted_internal_scalar_value_row_count"] == 0, "gate overaccepted rows")
    require(internal_gate["selected_threshold_response_functional_instantiated"] is False, "functional overinstantiated")
    for phrase in [
        "selected_L_rowlocal source rows",
        "selected_T_scheme source rows",
        "selected lambda_H payload row",
        "strict Omega acceptance",
    ]:
        require(phrase in internal_gate["blocking_value_sources"], f"internal gate missing {phrase}")

    require(row_ledger["row_count"] == 10, "row ledger count mismatch")
    require(row_ledger["internal_selected_value_row_count"] == 0, "ledger overaccepted rows")
    require(row_ledger["admitted_external_replay_row_count"] == 10, "external replay row count mismatch")
    require(row_ledger["forbidden_target_fit_row_count"] == 10, "forbidden fit row count mismatch")
    for row in row_ledger["row_decisions"]:
        require(row["internal_selected_value_row_accepted"] is False, f"{row['omega_id']} overaccepted")
        require(row["admitted_external_replay_row_available"] is True, f"{row['omega_id']} external row missing")
        require(row["accepted_decision"] == "controlled_external_replay_only", f"{row['omega_id']} bad decision")
        require(
            "L_rowlocal and T_scheme are not selected source rows" in row["why_internal_not_accepted"],
            f"{row['omega_id']} missing source-row reason",
        )
        if row["sector"] == "H":
            require(
                "selected_lambda_H_payload_row" in row["open_internal_source_subfields"],
                "H row missing lambda_H payload blocker",
            )

    require(external_decision["external_import_lane_available"] is True, "external lane not available")
    require(external_decision["accepted_external_threshold_row_count"] == 7, "threshold import count mismatch")
    require(external_decision["accepted_external_mass_scheme_row_count"] == 3, "mass import count mismatch")
    require(external_decision["accepted_diagonal_profile_theorem_closed"] is True, "diagonal profile missing")
    require(external_decision["ten_row_postcheck_targets_available"] is True, "postcheck targets missing")
    require(external_decision["selected_for_no_knob_closure"] is False, "external no-knob promotion")
    require(external_decision["selected_for_true_SM_equivalence"] is False, "external true SM promotion")
    for phrase in [
        "branch/source/operator selection",
        "no-knob value derivation",
        "promotion of fitted row coefficients to source rows",
        "hiding empirical constants inside L_rowlocal or T_scheme",
    ]:
        require(phrase in external_decision["forbidden_use"], f"external guard missing {phrase}")

    require(
        workorder["functional_contract"]["row_formula"]
        == "Omega_i = D_fin[class(i)] * L_rowlocal_i * T_scheme_i * exp(-2*pi*n_i)",
        "workorder row formula mismatch",
    )
    for phrase in [
        "L_rowlocal_i from same-branch HYM/overlap derivative rows",
        "T_scheme_i from same-branch threshold/mass/profile functional rows",
        "lambda_H H-sector payload",
        "strict Omega acceptance after rows are emitted",
    ]:
        require(
            phrase in workorder["functional_contract"]["source_selected_inputs_to_execute"],
            f"workorder missing {phrase}",
        )
    for phrase in [
        "no observed or benchmark SM values enter before row emission",
        "row values have source provenance independent of target residuals",
        "external replay rows remain quarantined as comparison/import data",
    ]:
        require(phrase in workorder["acceptance_tests"], f"acceptance test missing {phrase}")

    require(cutset["next_required_artifact"] == NEXT, "cutset next mismatch")
    for phrase in [
        "ten scalar rows classified by source tier",
        "external import lane admitted only as controlled empirical layer",
        "source-selected L_rowlocal/T_scheme/lambda_H workorder emitted",
    ]:
        require(phrase in cutset["closed_here"], f"cutset closed_here missing {phrase}")
    for phrase in [
        "selected L_rowlocal rows",
        "selected T_scheme rows",
        "selected lambda_H payload row",
        "strict Omega acceptance",
        "matrix-level CKM/offdiagonal mixing extension",
    ]:
        require(phrase in cutset["still_open"], f"cutset still_open missing {phrase}")

    for phrase in [
        "internal selected scalar rows             : 0",
        "admitted replay/postcheck rows            : 10",
        "external import selected for no-knob      : false",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
