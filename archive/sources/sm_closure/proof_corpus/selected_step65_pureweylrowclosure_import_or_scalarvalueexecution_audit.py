"""Audit Step65 pure-Weyl row closure import / scalar-value execution frontier."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step65_pureweylrowclosure_import_or_scalarvalueexecution"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
IMPORT_PACKET = PACKET_DIR / "step65_pure_weyl_row_closure_import.packet.json"
SCALAR_GATE = PACKET_DIR / "step65_scalar_value_execution_after_pure_rows.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step65_PureWeylRowClosureImport_or_ScalarValueExecution_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP65_PURE_WEYL_ROWS_IMPORTED_SCALAR_VALUE_EXECUTION_OPEN"
NEXT = "MTT_Selected_ScalarValueExecutionAfterPureWeylRows_or_LambdaHThresholdRows_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)
    data = load(DATA)
    imported = load(IMPORT_PACKET)
    scalar = load(SCALAR_GATE)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem mismatch")

    for item in [data, imported, scalar, cert]:
        require(item.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(item.get("target_fitting_used") is False, "target fitting violation")

    require(imported["identity_subtraction_used"] is False, "identity subtraction used")
    require(imported["identity_subtraction_promoted"] is False, "identity subtraction promoted")
    require(
        imported["identity_free_unscaled_pure_weyl_rows_closed"] is True,
        "identity-free pure rows not closed",
    )
    counts = imported["identity_free_row_counts"]
    require(counts["R_Z"] == 18, "R_Z count mismatch")
    require(counts["R_X"] == 18, "R_X count mismatch")
    require(counts["zero_route"] == 36, "zero route count mismatch")
    require(counts["total"] == 72, "total row count mismatch")
    exactness = imported["identity_free_exactness"]
    for key in ["R_Z_rows_exact", "R_X_rows_exact", "all_72_exact", "all_72_match_formal_packet"]:
        require(exactness[key] is True, f"exactness missing: {key}")
    require(exactness["max_abs_error_against_formal_packet"] < 1e-12, "formal packet residual too high")
    for key in [
        "A_selected_promoted",
        "PhysicalPhiFinC1ActionSource_promoted",
        "VSD01_source_assembly_subgate_closed",
        "b_selected_promoted",
        "deltaTheta_C1_promoted",
    ]:
        require(imported["source_promotion"][key] is True, f"source promotion missing: {key}")

    require(imported["lambda_orbit_scaled_pure_weyl_rows_closed"] is True, "lambda rows not closed")
    require(imported["lambda_orbit"] == ["1+omega", "1+omega2"], "lambda orbit mismatch")
    require(imported["individual_lambda_selected"] is False, "individual lambda overselected")
    require(imported["orbit_scaled_row_count"] == 72, "scaled row count mismatch")

    require(scalar["lambda_orbit_scaled_pure_rows_available"] is True, "lambda orbit rows not imported")
    require(scalar["second_order_orbit_matrix_packet_closed"] is True, "second-order matrix not imported")
    require(scalar["codomain_scalar_row_count"] == 10, "scalar codomain mismatch")
    require(scalar["execution_inputs_available_now"] is False, "scalar execution inputs overclaimed")
    require(scalar["selected_functional_executed"] is False, "scalar functional overexecuted")
    require(scalar["accepted_scalar_row_count_now"] == 0, "scalar rows overaccepted")
    require(scalar["lambda_H_row_emitted"] is False, "lambda_H overemitted")

    decision = data["closure_decision"]
    require(decision["pure_Weyl_rows_emitted_identity_free"] is True, "decision pure rows missing")
    require(decision["lambda_orbit_scaled_pure_Weyl_rows_closed"] is True, "decision lambda rows missing")
    for key in [
        "identity_subtraction_promoted",
        "individual_lambda_value_selected",
        "lambda_H_row_emitted",
        "scalar_value_execution_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed: {key}")
        require(cert[key] is False, f"certificate overclosed: {key}")
    require(decision["accepted_scalar_row_count_now"] == 0, "decision scalar rows overaccepted")
    require(cert["accepted_scalar_row_count_now"] == 0, "certificate scalar rows overaccepted")

    for phrase in [
        "identity subtraction used                  : false",
        "identity-free pure R_Z rows                : 18",
        "identity-free pure R_X rows                : 18",
        "lambda orbit scaled pure rows closed       : true",
        "accepted scalar rows                       : 0",
        NEXT,
    ]:
        require(phrase in note, f"note missing: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
