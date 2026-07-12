"""Audit selected HYM-overlap value source / selected overlap-kernel rows."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_hymoverlapvaluesource_or_selectedoverlapkernelrows"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
CHARGED = PACKET_DIR / "selected_charged_normalized_overlap_kernel_rows.packet.json"
H_GAP = PACKET_DIR / "h_lambda_overlap_kernel_row_gap.packet.json"
SCALAR = PACKET_DIR / "scalar_execution_gate_after_charged_kernel_rows.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_charged_overlap_kernel_rows.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HYMOverlapValueSourceTheorem_or_SelectedOverlapKernelRows_v1.md"

STATUS = "MTT_SELECTED_HYMOVERLAPVALUESOURCE_OR_SELECTEDOVERLAPKERNELROWS_NINE_CHARGED_ROWS_EMITTED_H_LAMBDA_AND_SCALARS_OPEN"
NEXT = "MTT_Selected_HLambdaOverlapKernelRow_or_ScalarOmegaExecutionGate_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    charged = load(CHARGED)
    h_gap = load(H_GAP)
    scalar = load(SCALAR)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["closure_claimed"] is True, "closure flag missing")
    require(data["full_no_knob_closure_claimed"] is False, "full no-knob overclaimed")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")

    decision = data["closure_decision"]
    require(decision["finite_27x27_qutrit_spectral_package_imported"] is True, "27x27 package not imported")
    require(decision["qutrit_left_action_rank"] == 27, "qutrit rank mismatch")
    require(decision["selected_charged_normalized_overlap_kernel_row_count"] == 9, "charged row count mismatch")
    require(decision["accepted_selected_K_source_row_count"] == 9, "K source count mismatch")
    require(decision["selected_T_scheme_source_row_count"] == 9, "T source count mismatch")
    require(decision["selected_H_lambda_overlap_kernel_row_emitted"] is False, "H row overemitted")
    require(decision["accepted_internal_scalar_value_row_count"] == 0, "scalar rows overaccepted")
    require(decision["full_ten_row_K_threshold_closure"] is False, "ten-row closure overclaimed")

    require(charged["row_count"] == 9, "charged packet row count")
    require(charged["accepted_selected_charged_normalized_overlap_kernel_row_count"] == 9, "accepted charged count")
    require(charged["accepted_full_ten_row_kernel_closure_count"] == 0, "full ten overaccepted")
    require(charged["accepted_strict_scalar_omega_row_count"] == 0, "Omega rows overaccepted")
    expected = {1: 1.367835979172, 2: 0.683917989586, 3: 0.683917989586}
    seen = set()
    for row in charged["rows"]:
        seen.add((row["sector"], row["generation"]))
        require(row["accepted_as_selected_charged_normalized_overlap_kernel_row"] is True, "charged row not accepted")
        require(row["accepted_as_full_ten_row_kernel_closure"] is False, "full closure overaccepted")
        require(row["accepted_as_strict_scalar_omega_row"] is False, "strict scalar overaccepted")
        require(row["selected_T_scheme_source_native"] == 1.0, "T_scheme not one")
        require(row["Delta_threshold_source_native"] == 0.0, "threshold delta not zero")
        require(row["Delta_mass_source_native"] == 0.0, "mass delta not zero")
        require(row["Delta_profile_source_native"] == 0.0, "profile delta not zero")
        require(abs(row["selected_normalized_overlap_kernel_value"] - expected[row["generation"]]) < 1e-12, "L value mismatch")
        require(abs(row["selected_K_threshold_source_value"] - expected[row["generation"]]) < 1e-12, "K value mismatch")
        require(row["observed_data_used_as_selector"] is False, "row observed selector")
        require(row["target_fitting_used"] is False, "row target fitting")
    require(seen == {(sector, gen) for sector in ["u", "d", "e"] for gen in [1, 2, 3]}, "charged row slots mismatch")

    require(h_gap["selected_H_sector_overlap_kernel_row_emitted"] is False, "H overlap row overemitted")
    require(h_gap["selected_lambda_H_payload_emitted"] is False, "lambda payload overemitted")
    require(h_gap["selected_K_threshold_Omega_H_lambda_emitted"] is False, "H K row overemitted")
    require(h_gap["selected_s_beta_value_found"] is True, "s_beta support missing")
    require("selected H radial/threshold scalar still absent" in h_gap["blocking_reasons"], "H radial blocker missing")

    require(scalar["selected_K_threshold_row_count_present_after_this_artifact"] == 9, "scalar gate K count")
    require(scalar["selected_K_threshold_row_count_required"] == 10, "scalar gate required count")
    require(scalar["H_lambda_kernel_row_present"] is False, "scalar gate H row overemitted")
    require(scalar["strict_Omega_rows_executable"] is False, "Omega execution overclosed")
    require(scalar["lambda_H_row_executable"] is False, "lambda execution overclosed")
    require(scalar["accepted_internal_scalar_value_row_count"] == 0, "scalar rows overaccepted")

    require(cutset["next_required_artifact"] == NEXT, "cutset next mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(cert["selected_charged_normalized_overlap_kernel_row_count"] == 9, "cert charged count")
    require(cert["selected_H_lambda_overlap_kernel_row_emitted"] is False, "cert H overemitted")
    require(cert["accepted_internal_scalar_value_row_count"] == 0, "cert scalar overaccepted")

    for phrase in [
        "selected charged normalized overlap-kernel rows: `9`",
        "selected H/lambda overlap-kernel rows: `0`",
        "accepted internal scalar value rows: `0`",
        "Omega_u.gen1: L = K = 1.367835979172",
        "Omega_d.gen2: L = K = 0.683917989586",
        "Omega_e.gen3: L = K = 0.683917989586",
        NEXT,
    ]:
        require(phrase in note, f"note missing phrase: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
