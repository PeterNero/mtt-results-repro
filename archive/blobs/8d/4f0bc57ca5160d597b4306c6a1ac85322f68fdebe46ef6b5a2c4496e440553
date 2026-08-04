"""Audit post-B_Huv Higgs-specific M_source frontier closure."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_msourcehiggsspecificoperatorblock_or_c5c6bridgefrontier"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
FUNCTIONAL_RECHECK = PACKET_DIR / "same_source_functional_and_bhuv_recheck.packet.json"
HIGGS_BLOCK_GAP = PACKET_DIR / "higgs_specific_operator_block_gap.packet.json"
MSOURCE_KERNEL = PACKET_DIR / "msource_acceptance_kernel_after_bhuv_and_functional.packet.json"
HK_GATE = PACKET_DIR / "hk_threshold_gate_after_higgs_operator_gap.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_higgs_operator_gap.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_MSourceHiggsSpecificOperatorBlock_or_C5C6BridgeFrontier_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_MSOURCEHIGGSSPECIFICOPERATORBLOCK_OR_C5C6BRIDGEFRONTIER_"
    "BHUV_AND_SHARED_FUNCTIONAL_CLOSED_HIGGS_OPERATOR_BLOCK_OPEN"
)
NEXT = "MTT_Selected_HiggsSpecificHermitianMassStrainBlock_or_C5C6ProjectionBridge_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("closure_claimed") is True, f"{label} closure flag")
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    functional = load(FUNCTIONAL_RECHECK)
    gap = load(HIGGS_BLOCK_GAP)
    kernel = load(MSOURCE_KERNEL)
    hk_gate = load(HK_GATE)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("functional recheck", functional),
        ("Higgs block gap", gap),
        ("M_source kernel", kernel),
        ("H K gate", hk_gate),
        ("cutset", cutset),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "certificate status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(cert["next_required_artifact"] == NEXT, "certificate next")
    require(data["theorem"]["proved"] is True, "theorem proved")
    require(cert["theorem_proved"] is True, "cert theorem proved")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaim")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaim")

    decision = data["closure_decision"]
    for key in [
        "B_Huv_two_column_uv_lift_emitted",
        "same_source_functional_alpha1_dotD_side_closed",
        "matter_operator_blocks_emitted",
        "UV_twoHiggs_basis_missing_retired",
    ]:
        require(decision[key] is True, f"decision should close {key}")
    for key in [
        "Higgs_specific_operator_block_emitted",
        "selected_Hermitian_M_source_emitted",
        "H_sector_restriction_R_H_emitted",
        "direct_Herm2_Huv_payload_emitted",
        "direct_Huu_Hud_Hdd_emitted",
        "selected_s_beta_value_found",
        "K_threshold_Omega_H_lambda_emitted",
        "ten_K_antecedent_satisfied",
        "strict_Omega_lambda_scalar_execution_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed {key}")
    require(decision["accepted_selected_K_source_row_count"] == 9, "K selected count")
    require(decision["selected_K_threshold_row_count_required"] == 10, "K required")
    require(decision["accepted_internal_scalar_value_row_count"] == 0, "scalar rows")

    b_side = functional["B_Huv_side"]
    require(b_side["B_Huv_two_column_uv_lift_emitted"] is True, "B side")
    require(b_side["source_orthonormality"] == "B_Huv^* G_Q B_Huv = I_2", "orthonormality")
    require(
        b_side["ordered_E_H_UV_source_ids"]["H_u"]
        == "Q_sel^U:E_H_UV:H_u:phi_(0,0)_e0",
        "H_u id",
    )
    require(
        b_side["ordered_E_H_UV_source_ids"]["H_d_dagger"]
        == "Q_sel^U:E_H_UV:H_d_dagger:phi_(0,0)_e0",
        "H_d id",
    )

    shared = functional["shared_functional_side"]
    for key in [
        "same_source_functional_value_closed",
        "alpha1_driver_verified",
        "selected_dotD_source_verified",
        "honest_dotD_validator_closed",
        "selected_overlap_normalization_emitted",
    ]:
        require(shared[key] is True, f"shared side should close {key}")
    require(shared["emitted_operator_blocks"] == ["d", "e", "nuD", "u"], "matter blocks")

    scope = functional["scope_discriminator"]
    require(scope["contains_H_u"] is False, "H_u overimport")
    require(scope["contains_H_d_dagger"] is False, "H_d overimport")
    require(scope["contains_Huv"] is False, "Huv overimport")
    require(scope["has_uv_higgs_blocks"] is False, "UV Higgs overimport")
    require(scope["all_blocks_are_matter_or_neutrino"] is True, "scope split")
    fdecision = functional["decision"]
    require(fdecision["old_H7B1Q_UV_twoHiggs_basis_missing_retired_by_B_Huv"] is True, "old B gap")
    require(fdecision["same_source_functional_exit_closed_for_non_Higgs_blocks"] is True, "functional exit")
    for key in [
        "Higgs_specific_operator_block_emitted",
        "M_source_value_emitted",
        "direct_Huv_entries_emitted",
    ]:
        require(fdecision[key] is False, f"functional overclosed {key}")

    updated = gap["updated_missing_for_Huv_after_B_Huv"]
    for key in [
        "UV_twoHiggs_basis_emitted",
        "B_Huv_value_emitted",
        "same_source_functional_alpha1_dotD_closed",
    ]:
        require(updated[key] is True, f"updated should close {key}")
    for key in [
        "M_source_value_emitted",
        "Huu_value_emitted",
        "Hud_value_emitted",
        "Hdd_value_emitted",
        "direct_Huv_entries_emitted",
        "Omega_emitted",
        "s_beta_emitted",
        "lambda_H_emitted",
    ]:
        require(updated[key] is False, f"updated overclosed {key}")
    required = gap["minimal_Higgs_specific_payload_now"]
    require(required["domain"] == "the source-orthonormal B_Huv two-column UV Higgs domain", "domain")
    require("Hermitian sesquilinear mass/strain form" in required["required_object"], "required object")
    why = gap["why_shared_functional_does_not_close_Higgs"]
    for key in [
        "operator_blocks_are_matter_or_neutrino",
        "collapsed_H_rank_one_is_not_UV_twoHiggs_block",
        "dotD_or_alpha1_driver_is_not_a_mass_strain_Hessian",
        "no_Higgs_specific_Hermitian_block",
    ]:
        require(why[key] is True, f"why gap {key}")

    strict = kernel["strict_gate_after_backimport"]
    for key in [
        "same_q79_F_m1_branch",
        "no_observed_selector",
        "B_Huv_two_column_lift",
        "same_source_functional_alpha1_dotD_side",
        "H_sector_restriction_identity_available_if_M_H_is_emitted_on_BHuv_domain",
    ]:
        require(strict[key] is True, f"strict should close {key}")
    for key in [
        "dynamic_hessian_or_mass_strain_source_owned",
        "Higgs_specific_operator_block_emitted",
        "finite_exactness_or_error_certificate_for_values",
        "direct_Herm2_Huv_payload_complete",
    ]:
        require(strict[key] is False, f"strict overclosed {key}")
    direct = kernel["direct_2x2_route"]
    require(direct["M_H"] is None, "M_H overemitted")
    require(direct["Huv"] is None, "Huv overemitted")
    full = kernel["full_operator_route"]
    for key in ["M_source", "R_H", "H_response"]:
        require(full[key] is None, f"full route overemitted {key}")
    for phrase in [
        "selected source-owned Hermitian M_H on the B_Huv two-column domain, or full M_source plus R_H",
        "proof M_H is a mass/strain/Hessian object, not a promoted metric, dotD, or replay witness",
        "Huu,Hud,Hdd with Hdu=conj(Hud)",
    ]:
        require(phrase in kernel["must_emit_next"], f"must emit missing {phrase}")
    for phrase in [
        "promoting the C3 metric Gram matrix as M_source",
        "promoting alpha1/dotD matter blocks as Higgs Huv",
        "using collapsed rank-one H sector values as the UV two-Higgs block",
        "backsolving beta, lambda_H, or thresholds from observed data",
    ]:
        require(phrase in kernel["forbidden_shortcuts"], f"shortcut guard missing {phrase}")

    h_row = hk_gate["H_row"]
    require(h_row["B_Huv_two_column_source_orthonormal_lift_emitted"] is True, "H row B")
    require(h_row["same_source_functional_alpha1_dotD_side_closed"] is True, "H row functional")
    require(h_row["Higgs_specific_operator_block_emitted"] is False, "H row overclosed")
    route = hk_gate["direct_route_state"]
    for key in ["B_Huv_two_column_lift_emitted", "shared_functional_alpha1_dotD_closed"]:
        require(route[key] is True, f"route should close {key}")
    for key in [
        "Higgs_specific_operator_block_emitted",
        "M_source_emitted",
        "direct_Herm2_Huv_payload_emitted",
        "K_threshold_Omega_H_lambda_emitted",
    ]:
        require(route[key] is False, f"route overclosed {key}")
    require(hk_gate["accepted_selected_K_source_row_count"] == 9, "HK count")
    require(hk_gate["selected_K_threshold_row_count_required"] == 10, "HK required")
    require(hk_gate["conditional_consequent_current"]["ten_K_antecedent_satisfied"] is False, "ten K")

    for phrase in [
        "B_Huv two-column UV lift is closed and back-imported",
        "late H7B1Q same-source functional/alpha1/dotD side is closed and back-imported",
        "old missing UV-two-Higgs-basis field is retired for the active direct route",
        "matter/neutrino operator blocks are separated from the missing Higgs block",
        "direct route is reduced to a Higgs-specific Hermitian mass/strain block M_H or full M_source+R_H",
        "H K-threshold gate remains 9/10",
    ]:
        require(phrase in cutset["closed_here"], f"cutset closed missing {phrase}")
    for phrase in [
        "selected Hermitian M_H on the B_Huv two-column domain",
        "or full same-source M_source plus H-sector restriction R_H",
        "direct Huu,Hud,Hdd rows",
        "C5 trace-to-H7B1U/projection-measure identity",
        "C6 no-extra-boundary/source theorem",
        "K_threshold.Omega_H.lambda source row",
        "strict Omega/lambda_H scalar execution",
    ]:
        require(phrase in cutset["still_open"], f"cutset open missing {phrase}")

    for key in [
        "B_Huv_two_column_uv_lift_emitted",
        "same_source_functional_alpha1_dotD_side_closed",
        "matter_operator_blocks_emitted",
        "UV_twoHiggs_basis_missing_retired",
    ]:
        require(cert[key] is True, f"cert should close {key}")
    for key in [
        "Higgs_specific_operator_block_emitted",
        "selected_Hermitian_M_source_emitted",
        "H_sector_restriction_R_H_emitted",
        "direct_Herm2_Huv_payload_emitted",
        "direct_Huu_Hud_Hdd_emitted",
        "selected_s_beta_value_found",
        "K_threshold_Omega_H_lambda_emitted",
        "ten_K_antecedent_satisfied",
        "strict_Omega_lambda_scalar_execution_closed",
        "full_no_knob_closure_claimed",
        "true_SM_equivalence_claimed",
    ]:
        require(cert[key] is False, f"cert overclosed {key}")

    for phrase in [
        "back-imported the emitted `B_Huv` two-column UV lift",
        "back-imported H7B1Q same-source functional/alpha1/dotD closure",
        "retired the old active missing field `UV_twoHiggs_basis_emitted=false`",
        "H K-threshold gate remains `9/10`",
        "selected Hermitian `M_H` on the `B_Huv` two-column domain",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
