"""Audit CONST-HIGGS-01 H7B1L dynamic Phi_fin^C1 to Huv gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_higgs_01_h7b1l_dynamic_phifinc1_huv_response_or_independent_huv_hessian"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
DYNAMIC_C1_IMPORT = BASE / "dynamic_c1_backimport_for_huv.packet.json"
HUV_PROJECTION_GAP = BASE / "huv_projection_gap.packet.json"
LOCAL_CONDITIONAL_BRIDGE = BASE / "local_tier_conditional_huv_bridge.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_HIGGS_01_H7B1L_DynamicC1HuvProjectionGate_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7B1L_DYNAMIC_C1_BACKIMPORT_BUILT_HUV_PROJECTION_OPEN"


def load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def clean(packet: dict[str, object], name: str) -> None:
    require(packet["observed_data_used_as_selector"] is False, f"{name} observed selector")
    require(packet["target_fitting_used"] is False, f"{name} target fitting")
    require(packet["closure_claimed"] is False, f"{name} closure overclaim")


def all_none(packet: dict[str, object], name: str) -> None:
    for key, value in packet.items():
        require(value is None, f"{name} emitted {key}")


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
    dynamic_import = load(DYNAMIC_C1_IMPORT)
    projection_gap = load(HUV_PROJECTION_GAP)
    local_bridge = load(LOCAL_CONDITIONAL_BRIDGE)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, packet in [
        ("candidate", candidate),
        ("dynamic_import", dynamic_import),
        ("projection_gap", projection_gap),
        ("local_bridge", local_bridge),
        ("next_work", next_work),
        ("cert", cert),
    ]:
        clean(packet, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["H7B1K_gate_imported"] is True, "H7B1K import")
    require(candidate["dynamic_C1_backimport_performed"] is True, "dynamic import")
    require(candidate["local_or_patched_dynamic_C1_support_available"] is True, "local support")
    require(candidate["strict_unpatched_dynamic_C1_support_still_open"] is True, "unpatched dynamic open")
    for key in [
        "C1_to_Huv_projection_functor_emitted",
        "honest_Huv_row_export_emitted",
        "strict_dynamic_Huv_gate_passes",
        "H_response_exported",
        "R_H_exported",
        "B_Huv_value_emitted",
        "M_source_value_emitted",
        "selected_offdiagonal_Omega_found",
        "selected_s_beta_value_found",
        "numeric_lambda_H_derived",
        "strict_no_knob_Higgs_closure",
    ]:
        require(candidate[key] is False, f"candidate overclosed {key}")
    require(candidate["new_Higgs_specific_parameters"] == 0, "candidate params")
    require(
        candidate["selected_next_artifact"] == "MTT_CONST_HIGGS_01_H7B1M_C1ToHuvProjectionOrHonestHuvRowExport_v1",
        "candidate next",
    )

    require(dynamic_import["status"] == "DYNAMIC_C1_SOURCE_SUPPORT_IMPORTED_HUV_RESTRICTION_OPEN", "dynamic status")
    strict = dynamic_import["strict_unpatched_dynamic_C1_state"]
    require(strict["same_source_dynamic_identity_can_promote_now"] is False, "strict identity promotion")
    require(strict["selected_A_selected_emitted"] is False, "strict A")
    require(strict["selected_b_selected_emitted"] is False, "strict b")
    require(strict["selected_sector_response_matrices_emitted"] is False, "strict sector matrices")
    require(strict["physical_source_current_attempt_rejected"] is True, "physical source rejected")
    require(strict["SelectedPhiFinC1PhysicalSourceEmissionTheorem_open"] is True, "Route A open")
    require(strict["SelectedIndependentGalerkinRowsExecution_open"] is True, "Route B open")
    require(strict["unpatched_PSM_C1_02_closed"] is False, "unpatched PSM")
    require(strict["minimal_lemma_full_proved"] is False, "minimal lemma")
    local = dynamic_import["local_or_patched_dynamic_C1_support"]
    require(local["local_dynamic_C1_closed"] is True, "local dynamic")
    require(local["local_source_identity_closed"] is True, "local identity")
    require(local["local_110row_source_identity_validates"] is True, "local rows")
    require(local["unpatched_source_identity_closed"] is False, "unpatched identity")
    require(local["patched_dynamic_C1_no_longer_blocks_SM_parity"] is True, "patched dynamic")
    require(local["patched_source_identity_closed"] is True, "patched source")
    require(local["patched_value_interface_closed"] is True, "patched value")
    require(local["unpatched_no_knob_dynamic_C1_closed"] is False, "patched no-knob")
    normal = dynamic_import["normal_form_support"]
    require(normal["RZ_RX_normal_forms_locked"] is True, "normal forms")
    require(normal["conditional_Gram_exact"] is True, "Gram")
    require(normal["conditional_values"]["Gram_A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "A^TA")
    require(normal["conditional_values"]["A_transpose_b"] == [12.0, 12.0], "A^Tb")
    require(normal["conditional_values"]["deltaTheta_C1"] == [1.0, 1.0], "deltaTheta")
    relevance = dynamic_import["higgs_relevance_decision"]
    require(relevance["dynamic_C1_support_relevant"] is True, "relevance")
    require(relevance["dynamic_C1_support_targets_C1_response_coordinate_system"] is True, "coordinate")
    require(relevance["dynamic_C1_support_directly_emits_Huv_response"] is False, "direct Huv")
    require(relevance["usable_as_Huv_only_after_projection_functor"] is True, "projection needed")
    require(dynamic_import["superset_strategy"]["combining_paths"] is True, "superset")

    require(projection_gap["status"] == "HUV_PROJECTION_RESTRICTION_FUNCTOR_NOT_EMITTED", "gap status")
    require(projection_gap["gap_theorem"]["proved"] is True, "gap theorem")
    fields = projection_gap["required_huv_projection_fields"]
    require(fields["no_observed_selector"] is True, "gap observed")
    require(fields["same_q79_F_m1_branch"] is True, "gap branch")
    for key in [
        "selected_C1_to_Huv_restriction_functor",
        "selected_UV_two_Higgs_basis",
        "source_owned_H_response_on_Huv",
        "source_owned_R_H_or_B_Huv",
        "Hermitian_Huv_mass_strain_entries",
        "finite_exactness_or_error_certificate",
        "coefficient_and_normalization_convention",
    ]:
        require(fields[key] is False, f"gap overclosed {key}")
    for key, value in projection_gap["rejected_promotions"].items():
        require(value is True, f"promotion not rejected {key}")
    all_none(projection_gap["strict_outputs"], "strict output")
    require(projection_gap["passes"] is False, "gap passes")

    require(local_bridge["status"] == "LOCAL_TIER_BRIDGE_CONDITIONAL_PROJECTION_MISSING", "local bridge status")
    assumptions = local_bridge["conditional_assumptions"]
    require(assumptions["accept_local_SelectedFiniteC1SourceIdentityPrinciple"] is True, "local principle")
    require(assumptions["local_dynamic_C1_source_identity_available"] is True, "local available")
    require(assumptions["must_add_selected_C1_to_Huv_projection_functor"] is True, "local projection")
    require(local_bridge["promotion_decision"]["promote_local_bridge_to_strict_Huv"] is False, "promote Huv")
    require(local_bridge["promotion_decision"]["promote_local_bridge_to_numeric_lambda_H"] is False, "promote lambda")

    require(next_work["status"] == "NEXT_WORKORDER_H7B1M_C1_TO_HUV_PROJECTION_OR_HONEST_HUV_ROW_EXPORT", "next status")
    require(next_work["primary_next"]["label"].endswith("H7B1M-C1-TO-HUV-PROJECTION-OR-HONEST-HUV-ROW-EXPORT"), "next label")
    require(len(next_work["two_legal_exits"]) == 2, "next exits")
    require(len(next_work["do_not_repeat"]) == 4, "next guardrails")

    require(cert["status"] == STATUS, "cert status")
    require(cert["dynamic_C1_backimport_performed"] is True, "cert dynamic")
    require(cert["local_or_patched_dynamic_C1_support_available"] is True, "cert local")
    require(cert["strict_unpatched_dynamic_C1_support_still_open"] is True, "cert unpatched")
    require(cert["C1_to_Huv_projection_functor_emitted"] is False, "cert projection")
    require(cert["honest_Huv_row_export_emitted"] is False, "cert rows")
    require(cert["strict_dynamic_Huv_gate_passes"] is False, "cert gate")
    require(cert["new_Higgs_specific_parameters"] == 0, "cert params")

    require("dynamic C1 backimport performed                 True" in note, "note dynamic")
    require("C1-to-Huv projection functor emitted             False" in note, "note projection")
    require("H7B1M-C1-TO-HUV-PROJECTION-OR-HONEST-HUV-ROW-EXPORT" in note, "note next")

    print("CONST-HIGGS-01 H7B1L dynamic C1/Huv projection audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
