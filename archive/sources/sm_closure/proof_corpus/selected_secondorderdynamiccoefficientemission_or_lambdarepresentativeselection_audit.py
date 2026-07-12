"""Audit second-order dynamic coefficient emission / lambda representative gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_secondorderdynamiccoefficientemission_or_lambdarepresentativeselection"
DATA = ROOT / "candidate_data"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
REQUIRED_ROWS = PACKET_DIR / "second_order_coefficient_required_rows.packet.json"
EMISSION_ATTEMPT = PACKET_DIR / "second_order_dynamic_emission_attempt.packet.json"
REPRESENTATIVE_DECISION = PACKET_DIR / "lambda_representative_selection_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_second_order_dynamic_coefficient_attempt.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_SecondOrderDynamicCoefficientEmission_or_LambdaRepresentativeSelection_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_secondorderdynamiccoefficientemission_or_lambdarepresentativeselection.py"

STATUS = "MTT_SELECTED_SECONDORDER_DYNAMIC_COEFFICIENT_EMISSION_BUILT_REQUIRED_ROWS_IDENTIFIED_EMISSION_OPEN"
NEXT = "MTT_Selected_PureWeylCoefficientRows_or_PrimitiveC1FormulaExecution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guardrails(payload: dict, label: str) -> None:
    require(payload["observed_data_used_as_selector"] is False, f"{label}: observed selector used")
    require(payload["target_fitting_used"] is False, f"{label}: target fitting used")
    require(payload["closure_claimed"] is False, f"{label}: closure overclaimed")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    required = load(REQUIRED_ROWS)
    emission = load(EMISSION_ATTEMPT)
    representative = load(REPRESENTATIVE_DECISION)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(candidate["theorem"]["proved"] is True, "candidate theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem not proved")

    for label, payload in [
        ("candidate", candidate),
        ("required", required),
        ("emission", emission),
        ("representative", representative),
        ("cutset", cutset),
        ("certificate", cert),
    ]:
        guardrails(payload, label)

    require(required["status"] == "PURE_WEYL_COEFFICIENT_ROWS_IDENTIFIED", "required status mismatch")
    require(required["static_lambda_orbit"] == ["1+omega", "1+omega2"], "lambda orbit mismatch")
    require(required["second_order_rows_required"]["phase_coefficient_row"] == "lambda_static * Z on u,e", "phase row mismatch")
    require(required["second_order_rows_required"]["shift_coefficient_row"] == "lambda_static * X on d,nuD", "shift row mismatch")
    require(
        required["dynamic_payload_rows_required"]
        == ["zero_mode_bases", "finite_Hessian_C1_source", "primitive_C1_contractions"],
        "required payload rows mismatch",
    )
    for row_id, row in required["dynamic_payload_row_status"].items():
        require(row["support_candidate_present"] is True, f"support missing for {row_id}")
        require(
            row["accepted_as_dynamic_phifin_c1_payload_row"] is False,
            f"payload row unexpectedly accepted: {row_id}",
        )

    require(
        emission["status"] == "EMISSION_BLOCKED_SELECTED_DYNAMIC_PAYLOAD_ROWS_ABSENT",
        "emission status mismatch",
    )
    require(emission["accepted_dynamic_payload_row_count"] == 0, "accepted payload row count mismatch")
    require(emission["support_candidate_present_count"] == 9, "support count mismatch")
    require(emission["all_support_shapes_present"] is True, "support shapes missing")
    require(emission["higher_response_execution_inputs_available"] is False, "higher inputs unexpectedly available")
    require(emission["primitive_row_formula_executed"] is False, "primitive row formula overexecuted")
    require(emission["same_source_dynamic_payload_closed"] is False, "dynamic payload overclosed")
    require(emission["selected_functional_executed"] is False, "selected functional overexecuted")
    require(emission["all_required_rows_accepted"] is False, "required rows overaccepted")
    require(emission["second_order_coefficient_rows_emitted"] is False, "second-order rows overemitted")

    require(
        representative["status"] == "STATIC_ORBIT_RETAINED_NO_DYNAMIC_REPRESENTATIVE_SELECTED",
        "representative status mismatch",
    )
    require(representative["surviving_lambdas"] == ["1+omega", "1+omega2"], "surviving lambda mismatch")
    require(len(representative["candidate_physical_signatures"]) == 2, "signature count mismatch")
    require(representative["individual_lambda_selected"] is False, "individual lambda overselected")
    require(representative["coexistence_or_equivalence_proved"] is False, "coexistence overclaimed")
    require(
        representative["selected_second_order_physical_matrix_promoted"] is False,
        "second-order physical matrix overpromoted",
    )

    closed = candidate["what_closes_now"]
    require(closed["pure_Z_X_coefficient_rows_identified"] is True, "pure row identification missing")
    require(closed["second_order_dynamic_emission_attempted"] is True, "emission attempt missing")
    require(closed["blocking_dynamic_payload_rows_named"] is True, "payload blockers missing")
    require(
        closed["lambda_representative_selection_kept_open_without_overclaim"] is True,
        "lambda guard missing",
    )

    remaining = candidate["what_remains_open"]
    for key in [
        "selected_zero_mode_basis_values",
        "selected_finite_Hessian_C1_source_blocks",
        "primitive_C1_contractions",
        "pure_Weyl_coefficient_rows_lambda_Z_lambda_X",
        "individual_lambda_representative_selection_or_coexistence",
        "selected_second_order_physical_matrix_promotion",
        "accepted_Yukawa_CKM_PMNS_RG_threshold_value_rows",
        "true_SM_equivalence",
        "full_no_knob_closure",
    ]:
        require(remaining[key] is True, f"remaining gate overclosed: {key}")

    decision = candidate["closure_decision"]
    require(decision["second_order_coefficient_rows_emitted"] is False, "coefficient rows overemitted")
    require(decision["individual_lambda_value_selected"] is False, "lambda overselected")
    require(decision["selected_second_order_physical_matrices_promoted"] is False, "matrices overpromoted")
    require(decision["accepted_value_layer_closed"] is False, "value layer overclosed")
    require(decision["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(decision["full_no_knob_closed"] is False, "no-knob overclosed")

    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    require("phase correction : lambda_static * Z on u,e" in note, "note missing phase row")
    require("accepted dynamic payload rows      : 0" in note, "note missing payload count")
    require("second-order coefficient rows emitted : false" in note, "note missing emission guard")
    require("full SM closure                    : false" in note, "note missing closure guard")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
