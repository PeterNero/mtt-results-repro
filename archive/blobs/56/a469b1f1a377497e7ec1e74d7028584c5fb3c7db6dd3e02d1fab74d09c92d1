"""Audit first-pass MZ-to-Mt Jacobian execution / threshold response fill."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"

SLUG = "selected_mztomtjacobianexecution_or_selectedthresholdresponsefunctionalfill"
STATUS = (
    "MTT_SELECTED_MZTOMTJACOBIANEXECUTION_OR_SELECTEDTHRESHOLDRESPONSEFUNCTIONALFILL_"
    "BUILT_FIRSTPASS_RG_JACOBIAN_AND_CROSSBLOCK_RESPONSE_SELECTED_RTHETA_OPEN"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    candidate = load(DATA / f"{SLUG}.candidate.json")
    jacobian = load(DATA / SLUG / "firstpass_rg_mz_to_mt_jacobian.packet.json")
    crossblock = load(DATA / SLUG / "firstpass_weak_bct_crossblock_covariance.packet.json")
    rtheta = load(DATA / SLUG / "selected_threshold_response_functional_fill_gate.packet.json")
    cutset = load(DATA / SLUG / "next_cutset_after_mztomt_jacobian_execution.packet.json")
    cert = load(CERTS / f"{SLUG}_certificate.json")

    errors: list[str] = []

    if candidate.get("status") != STATUS:
        errors.append("candidate status mismatch")
    if cert.get("status") != STATUS:
        errors.append("certificate status mismatch")
    if candidate.get("closure_claimed") is not False:
        errors.append("candidate must not claim full closure")
    if candidate.get("observed_data_used_as_selector") is not False:
        errors.append("observed values must not be selectors")
    if candidate.get("target_fitting_used") is not False:
        errors.append("target fitting must remain false")

    if jacobian.get("accepted_as_firstpass_MZ_to_Mt_RG_jacobian") is not True:
        errors.append("first-pass inverse Jacobian must be accepted")
    if jacobian.get("accepted_as_selected_precision_MZ_to_Mt_RG_jacobian") is not False:
        errors.append("precision selected Jacobian must remain open")
    if abs(jacobian.get("determinant_forward", 0.0)) <= 1e-12:
        errors.append("forward Jacobian determinant is too small")
    if jacobian.get("inverse_residual_max_abs", 1.0) >= 1e-8:
        errors.append("inverse residual is too large")
    if jacobian.get("max_baseline_delta_vs_accepted_packet", 1.0) >= 1e-12:
        errors.append("baseline replay does not match accepted first-pass packet")
    if len(jacobian.get("input_coordinate_rows_native_Mt", [])) != 5:
        errors.append("expected five native input rows")
    if len(jacobian.get("output_coordinate_rows_MZ", [])) != 5:
        errors.append("expected five MZ output rows")

    inserted = crossblock.get("inserted_cross_block_entries", [])
    nonzero = [entry for entry in inserted if abs(entry.get("covariance", 0.0)) > 0.0]
    if crossblock.get("accepted_as_firstpass_cross_block_covariance_values") is not True:
        errors.append("first-pass cross-block covariance values must be accepted")
    if crossblock.get("accepted_as_full_covariance_profile_likelihood") is not False:
        errors.append("full covariance/profile must remain open")
    if crossblock.get("inserted_entry_count") != len(inserted):
        errors.append("inserted entry count mismatch")
    if len(nonzero) == 0:
        errors.append("expected at least one nonzero cross-block entry")

    if rtheta.get("Rtheta_coefficient_values_closed") is not False:
        errors.append("Rtheta coefficients must remain open")
    if rtheta.get("selected_threshold_response_functional_instantiated") is not False:
        errors.append("selected threshold response functional must remain uninstantiated")
    if rtheta.get("selected_Rtheta_source_rows_closed") is not False:
        errors.append("selected Rtheta source rows must remain open")

    closed = cutset.get("closed_now", {})
    if closed.get("firstpass_MZ_to_Mt_inverse_RG_jacobian") is not True:
        errors.append("cutset must close first-pass inverse Jacobian")
    if closed.get("firstpass_weak_BCT_crossblock_covariance_values") is not True:
        errors.append("cutset must close first-pass weak/BCT cross-block values")
    still_open = cutset.get("still_open", {})
    for key in [
        "selected_precision_MZ_to_Mt_common_scale_RG_jacobian",
        "Rtheta_coefficient_values",
        "selected_threshold_response_functional",
        "selected_Rtheta_source_rows",
        "true_SM_equivalence",
        "full_no_knob",
    ]:
        if still_open.get(key) is not True:
            errors.append(f"{key} must remain open")

    if errors:
        print("selected_mztomtjacobianexecution_or_selectedthresholdresponsefunctionalfill audit: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("selected_mztomtjacobianexecution_or_selectedthresholdresponsefunctionalfill audit: PASS")
    print(f"status: {STATUS}")
    print(f"determinant_forward: {jacobian['determinant_forward']}")
    print(f"inverse_residual_max_abs: {jacobian['inverse_residual_max_abs']}")
    print(f"inserted_cross_block_entries: {crossblock['inserted_entry_count']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
