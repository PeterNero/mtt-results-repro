"""Audit CONST-HIGGS-01 H5B selected Higgs nonlinear amplitude projection contract."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_higgs_01_h5b_selected_higgs_nonlinear_amplitude_projection"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
ZERO_MODE = BASE / "selected_higgs_zero_mode_coordinate.packet.json"
PROJECTION_CONTRACT = BASE / "nonlinear_amplitude_projection_contract.packet.json"
TEMPLATE_FILL = BASE / "h4_template_field_fill.packet.json"
QUARTIC_BOUNDARY = BASE / "quartic_projection_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_HIGGS_01_H5B_SelectedHiggsNonlinearAmplitudeProjection_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H5B_HIGGS_AMPLITUDE_PROJECTION_CONTRACT_BUILT_SOURCE_ROWS_OPEN"


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
    zero_mode = load(ZERO_MODE)
    projection_contract = load(PROJECTION_CONTRACT)
    template_fill = load(TEMPLATE_FILL)
    quartic_boundary = load(QUARTIC_BOUNDARY)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, item in [
        ("candidate", candidate),
        ("zero_mode", zero_mode),
        ("projection_contract", projection_contract),
        ("template_fill", template_fill),
        ("quartic_boundary", quartic_boundary),
    ]:
        clean(item, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["selected_Higgs_zero_mode_coordinate_closed"] is True, "coordinate closed")
    require(candidate["selected_Higgs_projection_functional_template_closed"] is True, "projection template")
    require(candidate["projection_row_address"] == [12, 12, 12, 12], "row address")
    require(candidate["PhysicalActionOwnsFiniteTraceKernel_closed"] is False, "action overclosed")
    require(candidate["SelectedPhiFinC1PreResidualActionKernelTheorem_closed"] is False, "kernel theorem overclosed")
    require(candidate["actual_nonlinear_Higgs_source_rows_emitted"] is False, "source rows overemitted")
    require(candidate["projection_on_actual_source_kernel_closed"] is False, "actual projection overclosed")
    require(candidate["selected_Higgs_quartic_threshold_kernel_emitted"] is False, "quartic overemitted")
    require(candidate["Higgs_quartic_numeric_value_derived"] is False, "lambda overderived")
    require(candidate["strict_no_knob_Higgs_closure"] is False, "strict overclosed")
    require(candidate["new_Higgs_specific_parameters"] == 0, "Higgs params")

    selection = zero_mode["selection"]
    require(selection["finite_basis_id"] == "F3xF3_gerbe_twisted_fourier_N1_rank3", "basis")
    require(selection["finite_basis_dimension"] == 27, "basis dimension")
    require(selection["sector"] == "H", "sector")
    require(selection["zero_cluster_indices"] == [12, 13, 14], "zero cluster")
    require(selection["rank_two_H_shift_indices"] == [13, 14], "shift")
    require(selection["surviving_zero_mode_indices"] == [12], "surviving")
    require(selection["surviving_zero_mode_dimension"] == 1, "surviving dim")
    require(selection["H_sector_kernel_dimension"] == 1, "kernel dim")
    require(selection["coordinate_symbol"] == "a_H", "symbol")
    require(selection["coordinate_basis_vector"] == "e_H[12]", "basis vector")
    require(zero_mode["proof"]["rank_two_shift_source_proved"] is True, "shift source")
    require(zero_mode["proof"]["zero_mode_dimension_matches_kernel_dimension"] is True, "dimension match")
    require(zero_mode["proof"]["selected_coordinate_closed"] is True, "proof coordinate")

    functional = projection_contract["projection_functional"]
    require(functional["amplitude_coordinate"] == "a_H", "amplitude")
    require(functional["coordinate_index"] == 12, "coordinate index")
    require(functional["coordinate_projector"] == "P_H0 = |e_H[12]><e_H[12]|", "projector")
    require(functional["quartic_row_address"] == [12, 12, 12, 12], "functional row")
    require(functional["projected_formal_object"] == "K_H^(4)[a_H,a_H,a_H,a_H]", "formal object")
    conditional = projection_contract["conditional_acceptance"]
    require(conditional["selected_Higgs_zero_mode_or_amplitude_coordinate_closed"] is True, "conditional coordinate")
    require(conditional["Higgs_projection_certificate_template_closed"] is True, "certificate template")
    require(conditional["actual_nonlinear_source_rows_emitted"] is False, "conditional rows")
    require(conditional["PhysicalActionOwnsFiniteTraceKernel_closed"] is False, "conditional action")
    require(conditional["SelectedPhiFinC1PreResidualActionKernelTheorem_closed"] is False, "conditional kernel")
    require(conditional["projection_on_actual_source_kernel_closed"] is False, "conditional projection")
    require(conditional["lambda_H_coefficient_convention_closed"] is False, "lambda convention")

    require(template_fill["filled_now"]["selected_Higgs_zero_mode_or_amplitude_coordinate"] is True, "template coordinate")
    require(template_fill["acceptance_after_H5B"]["all_required_fields_present"] is False, "all fields")
    require(template_fill["acceptance_after_H5B"]["conditional_witness_counts_as_strict_closure"] is False, "conditional closure")
    require(template_fill["still_open"]["second_or_fourth_variation_rows"] is True, "rows still open")
    require(template_fill["still_open"]["lambda_H_style_coefficient_convention"] is True, "coefficient still open")

    closed = quartic_boundary["what_closes_now"]
    require(closed["selected_Higgs_zero_mode_coordinate"] is True, "boundary coordinate")
    require(closed["selected_Higgs_projection_functional_template"] is True, "boundary template")
    require(closed["quartic_row_address_for_future_source"] is True, "boundary row")
    open_ = quartic_boundary["what_remains_open"]
    require(open_["PhysicalActionOwnsFiniteTraceKernel"] is True, "open action")
    require(open_["SelectedPhiFinC1PreResidualActionKernelTheorem"] is True, "open kernel")
    require(open_["actual_nonlinear_Higgs_source_rows"] is True, "open rows")
    require(open_["projection_on_actual_nonlinear_source_kernel"] is True, "open projection")
    require(open_["lambda_H_numeric_value"] is True, "open lambda")
    require("coordinate projection template -> Higgs quartic value" in quartic_boundary["forbidden_promotions"], "forbidden")

    require(next_work["primary"]["label"] == "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6-SELECTED-PHIFINC1-PRERESIDUAL-ACTION-KERNEL-THEOREM", "primary")
    require(next_work["parallel_after_source"]["label"] == "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6B-PROJECT-ACTUAL-NONLINEAR-SOURCE-ROWS-TO-HIGGS-QUARTIC", "parallel")
    require(next_work["paper_update_section"]["label"] == "CONST-HIGGS-01 / PAPER-INSERT / HIGGS-ZERO-MODE-PROJECTION-CONTRACT", "paper")

    require(cert["status"] == STATUS, "cert status")
    require(cert["selected_Higgs_zero_mode_coordinate_closed"] is True, "cert coordinate")
    require(cert["projection_row_address"] == [12, 12, 12, 12], "cert row")
    require(cert["actual_nonlinear_Higgs_source_rows_emitted"] is False, "cert rows")
    require(cert["Higgs_quartic_numeric_value_derived"] is False, "cert numeric")
    require("H5B-SELECTED-HIGGS" in note and "H6-SELECTED-PHIFINC1" in note, "note")

    print("CONST-HIGGS-01 H5B selected Higgs nonlinear amplitude projection audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
