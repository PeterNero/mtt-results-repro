"""Audit higher-order full-response matrix / second-order flavor-lift gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_higherorderfullresponsematrices_or_secondorderflavorlift"
DATA = ROOT / "candidate_data"
BASE = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
MATRIX_GATE = BASE / "higher_order_matrix_candidate_gate.packet.json"
SOURCE_GATE = BASE / "coefficient_source_and_orientation_reconciliation.packet.json"
NEXT_CUTSET = BASE / "next_cutset_after_higher_order_matrix_gate.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HigherOrderFullResponseMatrices_or_SecondOrderFlavorLift_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_HIGHERORDERFULLRESPONSEMATRICES_OR_SECONDORDERFLAVORLIFT_BUILT_"
    "ALGEBRAIC_LIFT_CLOSED_SOURCE_EMISSION_OPEN"
)
NEXT = "MTT_Selected_SecondOrderDynamicCoefficientEmission_or_LambdaRepresentativeSelection_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guardrails(payload: dict, label: str) -> None:
    require(payload.get("observed_data_used_as_selector") is False, f"{label}: observed selector used")
    require(payload.get("target_fitting_used") is False, f"{label}: target fitting used")
    require(payload.get("closure_claimed") is False, f"{label}: closure overclaimed")


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(BUILDER)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if proc.returncode != 0:
        print(proc.stdout)
        return proc.returncode

    candidate = load(CANDIDATE)
    matrix_gate = load(MATRIX_GATE)
    source_gate = load(SOURCE_GATE)
    cutset = load(NEXT_CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(candidate["theorem"]["proved"] is True, "candidate theorem not proved")

    closed = candidate["what_closes_now"]
    require(closed["higher_order_algebraic_candidate_matrix_gate_closed"] is True, "matrix gate not closed")
    require(closed["three_family_splitting_candidate_imported"] is True, "three-family split not imported")
    require(closed["nonzero_CP_candidate_imported"] is True, "nonzero CP not imported")
    require(closed["static_orientation_reduction_imported"] is True, "static reduction not imported")
    require(closed["first_response_reentry_prevented"] is True, "first-response guard missing")
    require(closed["target_fitting_excluded"] is True, "target fitting guard missing")

    remaining = candidate["what_remains_open"]
    for key in [
        "selected_second_order_dynamic_coefficient_emission",
        "selected_second_order_physical_matrix_promotion",
        "individual_lambda_representative_selection_or_coexistence",
        "physical_CKM_PMNS_Yukawa_value_closure",
        "accepted_Yukawa_CKM_PMNS_RG_threshold_value_rows",
        "true_SM_equivalence",
        "full_no_knob_closure",
    ]:
        require(remaining[key] is True, f"remaining gate overclosed: {key}")

    decision = candidate["closure_decision"]
    require(decision["algebraic_higher_order_candidate_closed"] is True, "algebraic candidate not closed")
    require(decision["selected_full_response_matrices_emitted"] is False, "selected matrices overemitted")
    require(decision["selected_second_order_physical_matrices_promoted"] is False, "physical matrices overpromoted")
    require(decision["physical_CKM_PMNS_Yukawa_value_closure"] is False, "value closure overclaimed")
    require(decision["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(decision["full_no_knob_closed"] is False, "no-knob overclosed")

    require(matrix_gate["status"] == "ALGEBRAIC_HIGHER_ORDER_MATRIX_CANDIDATE_CLOSED_SELECTED_EMISSION_OPEN", "matrix gate status mismatch")
    require(matrix_gate["candidate_lift"]["candidate_count"] == 4, "candidate lift count mismatch")
    require(matrix_gate["candidate_lift"]["all_branches_split_three_families"] is True, "candidate lift split missing")
    require(matrix_gate["candidate_lift"]["all_branches_emit_nonzero_CP_odd_invariant"] is True, "candidate CP missing")
    require(matrix_gate["candidate_lift"]["hermitian_spectrum_each_sector"] == [1.0, 4.0, 7.0], "spectrum mismatch")
    require(matrix_gate["candidate_lift"]["cp_odd_exact_magnitude"] == "972*sqrt(3)", "CP magnitude mismatch")
    require(matrix_gate["accepted_as_selected_physical_matrices"] is False, "matrix gate overpromoted")

    static = source_gate["closed_static_reductions"]
    for key in [
        "same_orientation_filter_closed",
        "mixed_branches_rejected",
        "static_lambda_orbit_selected",
        "dynamic_first_response_layer_closed",
    ]:
        require(static[key] is True, f"static/source reduction missing: {key}")

    still_open = source_gate["still_open"]
    for key in [
        "individual_lambda_value_selected",
        "selected_second_order_dynamic_coefficient_emission",
        "selected_second_order_physical_matrices_promoted",
        "physical_CKM_PMNS_Yukawa_value_closure",
    ]:
        require(still_open[key] is True, f"source gate overclosed: {key}")

    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    require(len(cutset["success_criteria"]) == 4, "success criteria count mismatch")
    require("selected source emits lambda_Z/lambda_X rows" in cutset["success_criteria"][0], "source-row criterion missing")
    require("no observed masses" in cutset["success_criteria"][3], "observed selector guard missing")

    require(cert["status"] == STATUS, "certificate status mismatch")
    require(cert["algebraic_higher_order_candidate_closed"] is True, "certificate algebraic closure mismatch")
    require(cert["selected_full_response_matrices_emitted"] is False, "certificate selected matrix overclaim")
    require(cert["selected_second_order_physical_matrices_promoted"] is False, "certificate physical promotion overclaim")
    require(cert["true_SM_equivalence_closed"] is False, "certificate true SM overclaim")
    require(cert["full_no_knob_closed"] is False, "certificate no-knob overclaim")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")

    require("This is not selected physical matrix promotion" in note, "note promotion guard missing")
    require(NEXT in note, "note next artifact missing")

    for label, payload in [
        ("candidate", candidate),
        ("matrix gate", matrix_gate),
        ("source gate", source_gate),
        ("cutset", cutset),
        ("certificate", cert),
    ]:
        guardrails(payload, label)

    print(f"PASS {CANDIDATE.name}: {candidate['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
