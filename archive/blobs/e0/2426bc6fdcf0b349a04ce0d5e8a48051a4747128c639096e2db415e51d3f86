"""Audit CONST-HIGGS-01 H7B1D diagonal HYM rank-2 metric candidate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_higgs_01_h7b1d_diagonal_hym_rank2_metric_candidate"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
IMPORT_PACKET = BASE / "diagonal_hym_rank2_import.packet.json"
CONDITIONAL_READOUT = BASE / "conditional_huv_readout.packet.json"
NONPROMOTION = BASE / "strict_nonpromotion_proof.packet.json"
PROMOTION_CONTRACT = BASE / "promotion_contract.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_HIGGS_01_H7B1D_DiagonalHYMRank2MetricCandidate_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7B1D_DIAGONAL_HYM_RANK2_CANDIDATE_CONDITIONAL_NOT_PROMOTED"


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
    import_packet = load(IMPORT_PACKET)
    readout = load(CONDITIONAL_READOUT)
    nonpromotion = load(NONPROMOTION)
    contract = load(PROMOTION_CONTRACT)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, item in [
        ("candidate", candidate),
        ("import", import_packet),
        ("readout", readout),
        ("nonpromotion", nonpromotion),
        ("contract", contract),
    ]:
        clean(item, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["diagonal_HYM_rank2_metric_found"] is True, "rank2 found")
    require(candidate["diagonal_HYM_nonzero_strain_found"] is True, "nonzero strain")
    require(candidate["conditional_Huv_readout_built"] is True, "conditional readout")
    require(candidate["conditional_endpoint_s_beta_if_nonzero_diagonal_reduction"] == 1, "conditional s")
    for key in [
        "selected_Huv_basis_binding_found",
        "selected_finite_Huv_reduction_found",
        "selected_Huu_Hud_Hdd_found",
        "selected_Delta_Omega_found",
        "selected_rank_one_light_projector_P_L_found",
        "selected_s_beta_value_found",
        "selected_EW_boundary_RG_packet_closed",
        "numeric_lambda_H_derived",
        "strict_no_knob_Higgs_closure",
    ]:
        require(candidate[key] is False, f"candidate overclosed {key}")
    require(candidate["new_Higgs_specific_parameters"] == 0, "new params")

    rank2 = import_packet["rank2_diagonal_HYM_metric"]
    require(rank2["found"] is True, "import rank2")
    require(rank2["metric"] == ["exp(u)", "exp(-u)"], "metric form")
    require(rank2["nonzero_rank2_strain"] is True, "strain nonzero")
    require(rank2["continuous_parameters_added"] == 0, "continuous params")
    why_not = import_packet["why_this_is_not_yet_Huv"]
    require(why_not["H7B1C_requires_ordered_basis"] == ["H_u", "H_d^dagger"], "required basis")
    require(why_not["H_sector_currently_rank"] is True, "H rank preserved")
    require(why_not["H_sector_model_basis_indices"] == [12], "H model basis")
    require(why_not["H_sector_transport"] == "identity on Higgs singlet", "H transport")
    require(why_not["H_projector_selected_source_verified"] is False, "H projector source flag")
    require(import_packet["emits_finite_Huv_2x2_block"] is False, "import overemits Huv")

    assumptions = readout["conditional_assumptions_required"]
    require("H_u,H_d^dagger" in assumptions["A1_two_Higgs_basis_binding"], "A1 binding")
    conditional = readout["if_log_strain_S_is_selected_pointwise"]
    require(conditional["Delta_pointwise"] == "u", "Delta pointwise")
    require(conditional["Omega_pointwise"] == 0, "Omega pointwise")
    require(conditional["u_l2_positive"] is True, "u l2")
    require(conditional["pointwise_s_beta_where_nonzero"] == 1, "pointwise s")
    require(conditional["not_a_finite_scalar_packet"] is True, "not finite")
    naive = readout["why_naive_reductions_do_not_close"]
    require(naive["raw_mean_log_strain_Delta_eff"] == 0, "raw mean")
    require(naive["raw_mean_log_strain_fails_non_scalar_test"] is True, "mean fails")
    require(naive["using_measured_lambda_or_tan_beta_to_choose_reduction_forbidden"] is True, "forbidden")
    endpoint = readout["conditional_endpoint_if_future_nonzero_diagonal_reduction_is_selected"]
    require(endpoint["Omega_eff"] == 0, "endpoint Omega")
    require(endpoint["s_beta"] == 1, "endpoint s")
    require(endpoint["currently_promoted"] is False, "endpoint promoted")

    require(nonpromotion["status"] == "STRICT_PROMOTION_TO_HUV_FAILS_CURRENTLY", "nonpromotion status")
    require(len(nonpromotion["proof_steps"]) == 7, "proof step count")
    conclusion = nonpromotion["conclusion"]
    require(conclusion["diagonal_rank2_support_found"] is True, "support found")
    for key in [
        "selected_Huv_basis_binding_found",
        "selected_finite_reduction_found",
        "selected_Huu_Hud_Hdd_found",
        "selected_Delta_Omega_found",
        "selected_s_beta_found",
        "numeric_lambda_H_derived",
        "strict_no_knob_Higgs_closure",
    ]:
        require(conclusion[key] is False, f"nonpromotion overclosed {key}")
    no_regression = nonpromotion["no_regression_from_H7B1C"]
    require(no_regression["minimal_payload_still_valid"] is True, "payload regression")
    require(no_regression["current_source_insufficiency_still_valid"] is True, "insuff regression")

    exits = contract["legal_exits"]
    require(len(exits) == 3, "exit count")
    require("H7B1E-DIAGONAL-HYM-TO-HUV-BINDING-THEOREM" in exits[0]["label"], "exit A")
    require(exits[0]["conditional_readout_if_nonzero_diagonal"] == "Omega=0 and s_beta=1", "exit A readout")
    require("H7B1E-OFFDIAGONAL-EXT-OMEGA-SOURCE" in exits[1]["label"], "exit B")
    require("H7B2-SELECTED-EW-BOUNDARY-RG-PACKET" in exits[2]["label"], "exit C")
    require(contract["superset_use"]["combined_as_numeric_knobs"] is False, "superset knob")

    require("H7B1E-DIAGONAL-HYM-TO-HUV-BINDING-THEOREM" in next_work["primary_next"]["label"], "next primary")
    require("H7B1E-OFFDIAGONAL-EXT-OMEGA-SOURCE" in next_work["alternate_next"]["label"], "next alternate")
    require(cert["status"] == STATUS, "cert status")
    require(cert["diagonal_HYM_rank2_metric_found"] is True, "cert rank2")
    require(cert["selected_Huv_basis_binding_found"] is False, "cert binding")
    require(cert["selected_finite_Huv_reduction_found"] is False, "cert reduction")
    require(cert["numeric_lambda_H_derived"] is False, "cert lambda")
    require(cert["strict_no_knob_Higgs_closure"] is False, "cert closure")
    require("diagonal HYM rank-2 metric found" in note, "note rank2")
    require("Omega = 0" in note, "note conditional Omega")
    require("not claimed here" in note, "note guardrail")

    print("CONST-HIGGS-01 H7B1D diagonal HYM rank-2 metric candidate audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
