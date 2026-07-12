"""Audit CONST-HIGGS-01 H7A intrinsic K4 row execution payload."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_higgs_01_h7a_intrinsic_k4_row_execution_payload"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
SOURCE_SUPPORT = BASE / "same_source_trace_and_h_projector_support_import.packet.json"
QUADRATIC_NOGO = BASE / "quadratic_gap_layer_to_k4_nogo.packet.json"
EXECUTION_SCHEMA = BASE / "intrinsic_k4_execution_payload_schema.packet.json"
CURRENT_ATTEMPT = BASE / "current_intrinsic_k4_execution_attempt.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_HIGGS_01_H7A_IntrinsicK4RowExecutionPayload_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7A_K4_EXECUTION_PAYLOAD_BUILT_NONLINEAR_SOURCE_OPEN"


def load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def clean(packet: dict[str, object], name: str) -> None:
    require(packet["observed_data_used_as_selector"] is False, f"{name} observed selector")
    require(packet["target_fitting_used"] is False, f"{name} target fitting")
    require(packet["closure_claimed"] is False, f"{name} closure overclaim")


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    computed = json.loads(proc.stdout)
    require(computed["status"] == STATUS, "builder status mismatch")

    candidate = load(DATA)
    support = load(SOURCE_SUPPORT)
    nogo = load(QUADRATIC_NOGO)
    schema = load(EXECUTION_SCHEMA)
    attempt = load(CURRENT_ATTEMPT)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, item in [
        ("candidate", candidate),
        ("support", support),
        ("nogo", nogo),
        ("schema", schema),
        ("attempt", attempt),
    ]:
        clean(item, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["same_source_trace_and_H_projector_support_imported"] is True, "support imported")
    require(candidate["quadratic_gap_layer_false_route_closed"] is True, "quadratic false route")
    require(candidate["intrinsic_k4_execution_schema_ready"] is True, "schema ready")
    require(candidate["selected_nonlinear_source_kernel_found"] is False, "nonlinear source overfound")
    require(candidate["same_source_H_sector_fourth_variation_row_emitted"] is False, "K4 emitted")
    require(candidate["coefficient_convention_emitted"] is False, "coefficient convention")
    require(candidate["numeric_lambda_H_derived"] is False, "lambda numeric")
    require(candidate["strict_no_knob_Higgs_closure"] is False, "no-knob")
    require(candidate["new_Higgs_specific_parameters"] == 0, "Higgs params")

    imported = support["imported_same_source_support"]
    require(imported["selected_trace_equality_proved_for_D_E_gap_layer"] is True, "trace equality")
    require(imported["canonical_metric_connection_and_H_projector_same_source"] is True, "same source")
    require(imported["basis_dimension"] == 27, "basis dimension")
    require(imported["zero_cluster_indices"] == [12, 13, 14], "zero cluster")
    require(imported["H_sector_rank_two_shift_source_proved"] is True, "H shift")
    require(imported["Higgs_coordinate_index"] == 12, "H coord")
    require(imported["quartic_row_address"] == [12, 12, 12, 12], "row address")
    scope = support["scope_limit"]
    require(scope["D_E_gap_layer_only"] is True, "gap layer only")
    require(scope["does_not_claim_dotD_C1"] is True, "dotD guard")
    require(scope["does_not_emit_nonlinear_fourth_variation"] is True, "nonlinear guard")

    fact = nogo["formal_derivative_fact"]
    require(fact["fourth_derivative_of_quadratic_template"] == 0, "quadratic fourth derivative")
    require(fact["therefore_quadratic_gap_layer_emits_Higgs_self_coupling"] is False, "quadratic emits coupling")
    proves = nogo["what_this_proves"]
    require(proves["K2_to_K4_promotion_forbidden"] is True, "K2 promotion")
    require(proves["nonlinear_selected_source_kernel_required"] is True, "nonlinear required")

    target = schema["target"]
    require(target["formal_object"] == "K_H^(4)[a_H,a_H,a_H,a_H]", "schema target")
    require(target["quartic_row_address"] == [12, 12, 12, 12], "schema row")
    required_fields = schema["required_payload_fields"]
    for key, value in required_fields.items():
        require(value is False, f"schema field {key} overfilled")
    convention = schema["coefficient_convention_template_not_filled"]
    require(convention["lambda_formula_not_emitted"] is True, "lambda formula")
    require("normalization of a_H relative to |H|" in convention["mapping_requires"], "amplitude normalization")

    matrix = attempt["support_matrix"]
    require(matrix["row_address_owned"] is True, "attempt row address")
    require(matrix["same_source_D_E_trace_support"] is True, "attempt DE support")
    require(matrix["H_projector_source_support"] is True, "attempt H support")
    require(matrix["quadratic_false_route_rejected"] is True, "attempt false route")
    require(matrix["strict_H7_validator_route_A_passes"] is False, "attempt H7 route A")
    for source in attempt["attempted_sources"].values():
        require(source["accepted_for_K4"] is False, "attempt source accepted")
    result = attempt["result"]
    for key, value in result.items():
        require(value is False, f"attempt result {key} overfilled")

    require("H7A2-SELECTED-NONLINEAR-HIGGS-SOURCE-KERNEL" in next_work["strict_route_A_next"]["label"], "next A2")
    require("H7B-UV-BETA-OR-TWO-HIGGS-PROJECTION-THEOREM" in next_work["strict_route_B_parallel"]["label"], "next B")
    require(cert["status"] == STATUS, "cert status")
    require(cert["same_source_trace_and_H_projector_support_imported"] is True, "cert support")
    require(cert["quadratic_gap_layer_false_route_closed"] is True, "cert false route")
    require(cert["selected_nonlinear_source_kernel_found"] is False, "cert nonlinear")
    require(cert["same_source_H_sector_fourth_variation_row_emitted"] is False, "cert row")
    require(cert["numeric_lambda_H_derived"] is False, "cert lambda")
    require(cert["strict_no_knob_Higgs_closure"] is False, "cert no-knob")
    require("H7A-INTRINSIC-K4" in note and "d^4 S_2" in note, "note")

    print("CONST-HIGGS-01 H7A intrinsic K4 execution payload audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
