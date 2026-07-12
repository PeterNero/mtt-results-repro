"""Audit dynamic C1 transfer / primitive tensor / Hessian or independent rows gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_dynamicc1transferprimitivetensorhessian_or_independentrows"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
TRANSFER = PACKET_DIR / "dynamic_transfer_primitive_hessian_gate.packet.json"
ROWS = PACKET_DIR / "independent_rows_fallback_gate.packet.json"
DECISION = PACKET_DIR / "dynamic_value_emission_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_DynamicC1TransferPrimitiveTensorHessian_or_IndependentRows_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_dynamicc1transferprimitivetensorhessian_or_independentrows.py"

STATUS = "MTT_SELECTED_DYNAMICC1TRANSFERPRIMITIVETENSORHESSIAN_OR_INDEPENDENTROWS_BUILT_VALUE_EMISSION_GATE_OPEN"
NEXT = "MTT_Selected_SameSourceDynamicTransferIdentity_or_IndependentRowFormulaExecution_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def guardrails(payload: dict, label: str) -> None:
    require(payload["observed_data_used_as_selector"] is False, f"{label}: observed selector used")
    require(payload["target_fitting_used"] is False, f"{label}: target fitting used")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    transfer = load(TRANSFER)
    rows = load(ROWS)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem not proved")
    require("selected value emission" in note, "note misses value-emission gate")

    require(transfer["status"] == "CONDITIONAL_DYNAMIC_VALUES_EXACT_SELECTED_EMISSION_OPEN", "transfer status mismatch")
    require(transfer["retired_static_blockers"]["operator_alpha1_support_closed_for_frontier"] is True, "alpha1 support missing")
    require(transfer["retired_static_blockers"]["source_level_weylpair_provenance_open"] is False, "static provenance not retired")
    require(all(transfer["active_dynamic_cutset"].values()), "active dynamic cutset not all open")
    coord = transfer["conditional_coordinate_packet"]
    require(coord["rank"] == 2, "conditional rank mismatch")
    require(coord["Gram_A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "conditional Gram mismatch")
    require(coord["A_transpose_b_conditional"] == [12.0, 12.0], "conditional A^T b mismatch")
    require(coord["deltaTheta_conditional_from_Gram_solve"] == [1.0, 1.0], "conditional delta mismatch")
    require(transfer["source_map_candidate"]["constructed"] is True, "source map not constructed")
    require(transfer["source_map_candidate"]["selected_by_MTT_now"] is False, "source map overselected")
    require(transfer["hessian_bselected_status"]["promoted"] is False, "hessian/b overpromoted")
    require(transfer["no_linear_algebra_obstruction"] is True, "linear algebra obstruction not cleared")
    require(transfer["selected_value_emission_closed_now"] is False, "value emission overclosed")

    require(rows["status"] == "INDEPENDENT_ROW_FORMULA_FALLBACK_OPEN", "rows status mismatch")
    require(rows["row_count"] == 72, "row count mismatch")
    require(rows["all_rows_named"] is True, "row names mismatch")
    require(rows["route_b_executed_now"] is False, "rows overexecuted")

    require(decision["status"] == "DYNAMIC_VALUE_GATE_BUILT_CLOSURE_NOT_CLAIMED", "decision status mismatch")
    require(decision["static_source_retired"] is True, "static source not retired")
    require(decision["conditional_dynamic_values_exact"] is True, "conditional values not exact")
    require(decision["source_map_candidate_constructed"] is True, "source map not constructed in decision")
    require(decision["same_source_dynamic_transfer_identity_closed"] is False, "identity overclosed")
    require(decision["selected_primitive_tensor_values_emitted"] is False, "primitive tensor overemitted")
    require(decision["selected_Hessian_or_b_source_vector_emitted"] is False, "b overemitted")
    require(decision["independent_rows_executed"] is False, "independent rows overexecuted")
    require(decision["unpatched_dynamic_C1_packet_closed"] is False, "dynamic C1 overclosed")
    require(decision["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(decision["no_knob_closed"] is False, "no-knob overclosed")

    for label, payload in [
        ("candidate", data),
        ("transfer", transfer),
        ("rows", rows),
        ("decision", decision),
        ("certificate", cert),
    ]:
        guardrails(payload, label)

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
