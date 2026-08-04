"""Audit CONST-HIGGS-01 H7B1N H-sector dynamic extension / Huv rows gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_higgs_01_h7b1n_hsector_dynamic_extension_or_honest_huv_rows"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
HSECTOR_EXTENSION = BASE / "hsector_dynamic_extension_attempt.packet.json"
HUV_ROWS = BASE / "honest_huv_row_export_attempt.packet.json"
CUTSET = BASE / "nonlinear_hym_huv_payload_cutset.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_HIGGS_01_H7B1N_HSectorDynamicExtensionOrHonestHuvRows_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7B1N_TWO_ROUTE_TEST_BUILT_NONLINEAR_HYM_HUV_PAYLOAD_OPEN"


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
    hsector = load(HSECTOR_EXTENSION)
    huv_rows = load(HUV_ROWS)
    cutset = load(CUTSET)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, packet in [
        ("candidate", candidate),
        ("hsector", hsector),
        ("huv_rows", huv_rows),
        ("cutset", cutset),
        ("next_work", next_work),
        ("cert", cert),
    ]:
        clean(packet, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["H7B1M_gate_imported"] is True, "H7B1M import")
    require(candidate["Hsector_dynamic_extension_found"] is False, "Hsector extension")
    require(candidate["honest_Huv_row_export_found"] is False, "honest rows")
    require(candidate["nonlinear_HYM_seed_support_closed"] is True, "seed support")
    require(candidate["nonlinear_HYM_correction_closed"] is False, "nonlinear correction")
    require(candidate["broad_H7B1N_gate_reduced_to_minimal_cutset"] is True, "cutset reduction")
    for key in [
        "B_Huv_value_emitted",
        "M_source_value_emitted",
        "direct_Huv_entries_emitted",
        "selected_offdiagonal_Omega_found",
        "selected_s_beta_value_found",
        "numeric_lambda_H_derived",
        "strict_no_knob_Higgs_closure",
    ]:
        require(candidate[key] is False, f"candidate overclosed {key}")
    require(candidate["new_Higgs_specific_parameters"] == 0, "candidate params")
    require(
        candidate["selected_next_artifact"] == "MTT_CONST_HIGGS_01_H7B1O_NonlinearHYMCorrectionOrDirectHuvRows_v1",
        "candidate next",
    )

    require(hsector["status"] == "HSECTOR_DYNAMIC_C1_EXTENSION_NOT_EMITTED_CURRENT_CORPUS", "hsector status")
    target = hsector["current_dynamic_c1_target"]
    require(target["sector_set"] == ["d", "e", "nuD", "u"], "target sectors")
    require(target["inferred_real_dimension"] == 72, "target dim")
    require(target["contains_H_sector"] is False, "target H")
    require(target["contains_Hu_sector"] is False, "target Hu")
    require(target["contains_Hd_dagger_sector"] is False, "target Hd")
    require(target["selected_A_selected_emitted"] is False, "target A")
    require(target["selected_b_selected_emitted"] is False, "target b")
    require(target["conditional_Gram_exact"] is True, "target Gram")
    req = hsector["required_extension_payload"]
    require(req["ordered_UV_basis"] == ["H_u", "H_d^dagger"], "required basis")
    for key in [
        "extend_target_with_H_or_Huv_rows",
        "emit_Pi_Huv_or_R_H",
        "emit_H_response_on_Huv",
        "emit_Hermitian_Huv_mass_strain_entries",
        "emit_exactness_or_error_certificate",
        "emit_coefficient_normalization_convention",
    ]:
        require(req[key] is True, f"required extension {key}")
    decision = hsector["attempt_decision"]
    for key in [
        "H_sector_dynamic_extension_found",
        "selected_Pi_Huv_or_R_H_found",
        "H_response_found",
        "route_A_passes",
    ]:
        require(decision[key] is False, f"hsector decision {key}")

    require(huv_rows["status"] == "HONEST_HUV_ROW_EXPORT_NOT_EMITTED_CURRENT_CORPUS", "huv rows status")
    require(huv_rows["B_Huv_side"]["value_emitted"] is False, "B emitted")
    require(huv_rows["B_Huv_side"]["current_attempt_value_emitted"] is False, "B attempt")
    require(huv_rows["B_Huv_side"]["support_closed"]["single_Higgs_quotient_imported"] is True, "B support")
    require(huv_rows["M_source_side"]["value_emitted"] is False, "M emitted")
    require(huv_rows["M_source_side"]["current_attempt_value_emitted"] is False, "M attempt")
    require(huv_rows["M_source_side"]["conditional_valpha_promoted_to_M_source"] is False, "V_alpha promoted")
    require(huv_rows["M_source_side"]["support_closed"]["nonzero_ext_class_selected"] is True, "M support")
    direct = huv_rows["direct_Huv_rows"]
    require(direct["basis_labels_currently_emitted"] is False, "direct basis")
    require(direct["matrix_values_currently_emitted"] is False, "direct matrix")
    require(direct["current_packet_passes"] is False, "direct pass")
    require(direct["Huu"] is None and direct["Hud"] is None and direct["Hdd"] is None, "direct entries")
    diag = huv_rows["conditional_diagonal_HYM_support"]
    require(diag["conditional_endpoint_s_beta"] == 1, "diag s_beta")
    require(diag["currently_promoted"] is False, "diag promoted")
    require(diag["requires_binding_and_reduction"] is True, "diag binding")
    require(diag["raw_mean_log_strain_fails_non_scalar_test"] is True, "diag mean")
    nonlinear = huv_rows["nonlinear_HYM_support"]
    require(nonlinear["row_level_harmonic_seed_closed"] is True, "nonlinear seed")
    require(nonlinear["transition_overlap_table_closed"] is True, "nonlinear transition")
    require(nonlinear["Hodge_Lambda_row_table_closed"] is True, "nonlinear Hodge")
    require(nonlinear["gauge_projector_row_closed"] is True, "nonlinear projector")
    require(nonlinear["nonlinear_HYM_connection_correction_closed"] is False, "nonlinear correction")
    attempt = huv_rows["attempt_decision"]
    require(attempt["B_Huv_emitted"] is False, "attempt B")
    require(attempt["M_source_emitted"] is False, "attempt M")
    require(attempt["direct_Huv_entries_emitted"] is False, "attempt direct")
    require(attempt["route_B_passes"] is False, "attempt pass")

    require(cutset["status"] == "MINIMAL_CUTSET_NONLINEAR_HYM_CORRECTION_OR_DIRECT_HUV_ROWS", "cutset status")
    require(cutset["cutset_theorem"]["proved"] is True, "cutset theorem")
    for key, value in cutset["closed_as_nonstarters"].items():
        require(value is True, f"nonstarter {key}")
    require(len(cutset["minimal_payload_to_close"]["route_A_Hsector_dynamic_extension"]) == 3, "route A payload")
    require(len(cutset["minimal_payload_to_close"]["route_B_nonlinear_HYM_or_direct_rows"]) == 4, "route B payload")
    all_none(cutset["strict_outputs"], "strict output")
    require(cutset["passes"] is False, "cutset pass")

    require(next_work["status"] == "NEXT_WORKORDER_H7B1O_NONLINEAR_HYM_CORRECTION_OR_DIRECT_HUV_ROWS", "next status")
    require(next_work["primary_next"]["label"].endswith("H7B1O-NONLINEAR-HYM-CORRECTION-OR-DIRECT-HUV-ROWS"), "next label")
    require(len(next_work["two_legal_exits"]) == 2, "next exits")
    require(len(next_work["do_not_repeat"]) == 4, "next guardrails")

    require(cert["status"] == STATUS, "cert status")
    require(cert["Hsector_dynamic_extension_found"] is False, "cert extension")
    require(cert["honest_Huv_row_export_found"] is False, "cert rows")
    require(cert["nonlinear_HYM_seed_support_closed"] is True, "cert seed")
    require(cert["nonlinear_HYM_correction_closed"] is False, "cert nonlinear")
    require(cert["broad_H7B1N_gate_reduced_to_minimal_cutset"] is True, "cert cutset")
    require(cert["new_Higgs_specific_parameters"] == 0, "cert params")

    require("broad H7B1N gate reduced to cutset        True" in note, "note cutset")
    require("H7B1O-NONLINEAR-HYM-CORRECTION-OR-DIRECT-HUV-ROWS" in note, "note next")

    print("CONST-HIGGS-01 H7B1N H-sector/Huv row gate audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
