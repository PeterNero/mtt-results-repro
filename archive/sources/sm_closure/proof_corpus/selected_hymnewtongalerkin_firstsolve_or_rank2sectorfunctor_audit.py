"""Audit selected HYM Newton/Galerkin first solve or rank2-sector functor."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_hymnewtongalerkin_firstsolve_or_rank2sectorfunctor"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
FIRST_SOLVE = PACKET_DIR / "selected_hym_first_solve_payload.packet.json"
END0_GREEN = PACKET_DIR / "full_diagonal_end0_green_payload.packet.json"
TRANSFER = PACKET_DIR / "rank2_to_sector_transfer_boundary.packet.json"
CUTSET = PACKET_DIR / "physical_dotd_or_sector_routing_cutset.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HYMNewtonGalerkin_FirstSolve_or_Rank2SectorFunctor_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_HYMNEWTONGALERKIN_FIRSTSOLVE_OR_RANK2SECTORFUNCTOR_BUILT_DIAGONAL_SOLVE_SECTOR_TRANSFER_OPEN"
NEXT = "MTT_Selected_Physical_dotD_alpha1_or_End0_to_Sector_Routing_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    first = load(FIRST_SOLVE)
    green = load(END0_GREEN)
    transfer = load(TRANSFER)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, "next artifact mismatch")

    require(first["solver"]["converged"] is True, "diagonal HYM solver did not converge")
    require(first["solution_summary"]["final_residual_l2"] < 1e-12, "diagonal HYM residual too large")
    require(first["A_HYM_payload"]["emitted"] is True, "A_HYM payload missing")
    require(first["A_HYM_payload"]["rank2_connection"] == "A_diag = d u * T3 in the selected diagonal End0 lane", "A_HYM formula mismatch")
    require(first["quadrature_truncation_payload"]["emitted_for_diagonal_replay"] is True, "diagonal residual certificate missing")
    require(first["quadrature_truncation_payload"]["accepted_for_full_sector_validator"] is False, "diagonal residual overaccepted")
    require(first["coercivity_status"]["full_gauge_fixed_jacobian_lower_bound_proved"] is False, "full coercivity overproved")

    boundary = green["operator_payload_boundary"]
    require(boundary["diagonal_End0_D_E_formula_extracted"] is True, "End0 D_E not extracted")
    require(boundary["protected_T3_Riesz_projector_extracted"] is True, "T3 Riesz missing")
    require(boundary["protected_T3_reduced_Green_extracted"] is True, "T3 Green missing")
    require(boundary["T1_T2_coupled_covariant_Riesz_Green_extracted"] is True, "T1/T2 Green missing")
    require(boundary["row_model_offdiagonal_T1T2_source_controlled"] is True, "offdiagonal row control missing")
    require(boundary["physical_dotD_alpha1_payload_extracted"] is False, "physical dotD overextracted")
    require(boundary["rank2_to_rank3_sector_transfer_values_extracted"] is False, "sector transfer overextracted")
    require(boundary["validator_ready_sector_payload"] is False, "sector payload overaccepted")
    require(green["T1_T2_covariant_Green"]["green_operator_norm_bound"] < 0.026, "Green bound too large")
    require(green["offdiagonal_row_model_control"]["trace_pairings"]["T1_trace_pairing"] == 0.0, "T1 source not controlled")
    require(green["offdiagonal_row_model_control"]["trace_pairings"]["T2_trace_pairing"] == 0.0, "T2 source not controlled")

    progress = transfer["straight_path_progress"]
    require(progress["diagonal_HYM_solve_closed"] is True, "transfer missing diagonal solve")
    require(progress["A_HYM_formula_emitted"] is True, "transfer missing A_HYM")
    require(progress["End0_D_E_formula_emitted"] is True, "transfer missing End0 D_E")
    require(progress["full_diagonal_End0_Green_closed"] is True, "transfer missing End0 Green")
    require(progress["offdiagonal_row_model_control_closed"] is True, "transfer missing offdiagonal control")
    functor = transfer["rank2_to_sector_functor"]
    require(functor["abstract_End0_functor_available"] is True, "abstract End0 functor missing")
    require(functor["BN_qutrit_identification_rejected_as_selected_End0_basis"] is True, "BN guardrail missing")
    require(functor["sector_routing_values_emitted"] is False, "sector routing overemitted")
    require(functor["physical_dotD_alpha1_emitted"] is False, "physical dotD overemitted")
    require(functor["closed"] is False, "rank2-to-sector transfer overclosed")
    acceptance = transfer["acceptance_kernel_progress"]
    require(acceptance["emit_selected_A_HYM_or_SH_coefficient_vector"] is True, "acceptance did not register A_HYM")
    require(acceptance["construct_rank2_to_sector_transfer_functor_or_prove_unnecessary"] is False, "sector functor overclosed")
    require(acceptance["derive_sector_ready_rhoE_metric_DE_Riesz_Green_dotD_C1"] is False, "sector-ready payload overderived")
    require(acceptance["replay_validators_without_lifted_flags"] is False, "validators overreplayed")

    require(cutset["recommended_next_artifact"] == NEXT, "cutset next artifact mismatch")
    require(cutset["bookkeeping_remaining"] is False, "bookkeeping incorrectly remains")
    require(cutset["source_or_value_emission_required"] is True, "source/value emission not required")
    for required in [
        "emit selected End0-to-sector routing values from rank-2 V_alpha/End0 into the qutrit/family-sector scaffold",
        "emit physical dotD_alpha1 as a same-branch derivative of selected D_E, not a diagnostic lift",
        "derive sector-ready rho_E, metric, D_E, Riesz/Green, dotD, and C1/overlap payloads",
    ]:
        require(required in cutset["remaining_minimal_payloads"], f"cutset missing: {required}")

    require(data["closure_decision"]["selected_diagonal_HYM_first_solve_closed"] is True, "candidate missing first solve closure")
    require(data["closure_decision"]["rank2_End0_payload_closed"] is True, "candidate missing End0 payload closure")
    require(data["closure_decision"]["rank2_to_sector_transfer_closed"] is False, "candidate transfer overclosed")
    require(data["closure_decision"]["physical_dotD_alpha1_closed"] is False, "candidate physical dotD overclosed")
    require(data["closure_decision"]["actual_QaSU3_operator_packet_promoted"] is False, "candidate Qa/SU3 overpromoted")
    require(cert["selected_diagonal_HYM_first_solve_closed"] is True, "certificate missing first solve")
    require(cert["rank2_to_sector_transfer_closed"] is False, "certificate transfer overclosed")
    require("source progress, not true-equivalence closure" in note, "note missing guardrail")

    for packet in [first, green, transfer, cutset, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
