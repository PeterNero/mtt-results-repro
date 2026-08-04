"""Audit the H-lambda formal operator / direct radial Hessian value packet."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_hlambdarowlocaloverlapandscheme_or_directradialhessianvalue"


def read_json(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    candidate = read_json(f"candidate_data/{SLUG}.candidate.json")
    operator = read_json(f"candidate_data/{SLUG}/h_lambda_formal_rowlocal_operator.packet.json")
    scheme = read_json(f"candidate_data/{SLUG}/h_lambda_scheme_factor_contract.packet.json")
    hessian = read_json(f"candidate_data/{SLUG}/direct_radial_hessian_value_execution_contract.packet.json")
    gate = read_json(f"candidate_data/{SLUG}/h_lambda_operator_execution_gate.packet.json")
    cert = read_json(f"certificates/{SLUG}_certificate.json")

    require(candidate["theorem"]["proved"] is True, "theorem must be proved")
    require(candidate["decision"]["formal_H_lambda_rowlocal_operator_emitted"] is True, "formal operator")
    require(candidate["decision"]["formal_H_lambda_scheme_slot_emitted"] is True, "scheme slot")
    require(candidate["decision"]["direct_radial_hessian_execution_contract_closed"] is True, "hessian contract")
    require(candidate["decision"]["numeric_H_lambda_rowlocal_value_emitted"] is False, "numeric L overpromoted")
    require(candidate["decision"]["numeric_T_scheme_value_emitted"] is False, "numeric T overpromoted")
    require(candidate["decision"]["direct_N_H_value_emitted"] is False, "direct N_H overpromoted")
    require(candidate["decision"]["accepted_H_scalar_value_rows"] == 0, "accepted H rows")
    require(candidate["next_target"] == "MTT_Selected_HLambdaFiniteGalerkinExecution_or_RadialHessianScalarRun_v1", "next target")

    require(operator["operator_id"] == "RO.q79F1.Omega_H.lambda", "operator id")
    require(operator["same_branch"]["q"] == 79, "branch q")
    require(operator["same_branch"]["orientation"] == "F", "branch orientation")
    require(operator["same_branch"]["torsion_m"] == 1, "branch torsion")
    require(operator["carrier"]["carrier_dimension"] == 27, "carrier dimension")
    require(operator["carrier"]["left_X27_rank"] == 27, "X rank")
    require(operator["carrier"]["left_Z27_rank"] == 27, "Z rank")
    require(operator["emission"]["formal_source_operator_emitted"] is True, "operator not emitted")
    require(operator["emission"]["numeric_matrix_entries_emitted"] is False, "numeric entries emitted")
    require(operator["emission"]["selected_rowlocal_scalar_value_emitted"] is False, "scalar value emitted")
    require(operator["emission"]["accepted_as_L_rowlocal_value"] is False, "L value accepted")
    require("delta_{Omega_H.lambda} D_E" in operator["formal_operator"]["symbolic_definition"], "delta insertion")

    require(scheme["emission"]["formal_scheme_slot_emitted"] is True, "scheme slot not emitted")
    require(scheme["emission"]["numeric_scheme_value_emitted"] is False, "scheme value emitted")
    require(scheme["emission"]["accepted_as_T_scheme_value"] is False, "scheme accepted")
    scheme_guard_text = " ".join(scheme["why_charged_T_scheme_does_not_transfer"])
    require("charged" in scheme_guard_text and "T_scheme=1" in scheme_guard_text, "charged shortcut guard")
    require(scheme["closed_equation"].endswith("T_scheme.Omega_H.lambda"), "scheme equation")

    require(hessian["required_scalar"] == "N_H = Hess(F_H)[U_H,U_H]", "required scalar")
    require(hessian["current_emission"]["direct_N_H_value_emitted"] is False, "N_H emitted")
    require(hessian["current_emission"]["accepted_direct_radial_hessian_value_rows"] == 0, "N_H rows")
    require("selected finite H-sector action F_H" in hessian["legal_source_operators"], "F_H legal source missing")
    require("selected same-source Hermitian M_source restricted to B_Huv" in hessian["legal_source_operators"], "M source missing")

    require(gate["counts"]["charged_rows_selected"] == 9, "charged rows")
    require(gate["counts"]["strict_K_rows_selected"] == 9, "strict K rows")
    require(gate["counts"]["strict_K_rows_required"] == 10, "strict K required")
    require(gate["counts"]["H_lambda_numeric_row_selected"] == 0, "H lambda numeric selected")
    require(gate["counts"]["accepted_H_scalar_value_rows"] == 0, "H scalar rows")
    require(gate["guards"]["does_not_use_step72_H_target_as_source"] is True, "Step72 source guard")
    require(gate["guards"]["does_not_use_controlled_r_H_as_strict_source"] is True, "controlled source guard")
    require(gate["guards"]["does_not_transfer_charged_T_scheme_to_H"] is True, "T scheme guard")
    require(
        gate["next_required_artifact"] == "MTT_Selected_HLambdaFiniteGalerkinExecution_or_RadialHessianScalarRun_v1",
        "gate next target",
    )

    require(cert["proved"] is True, "certificate proved")
    require(cert["checks"]["formal_H_lambda_rowlocal_operator_emitted"] is True, "cert operator")
    require(cert["checks"]["formal_H_lambda_scheme_slot_emitted"] is True, "cert scheme")
    require(cert["checks"]["numeric_H_lambda_rowlocal_value_emitted"] is False, "cert numeric L")
    require(cert["checks"]["numeric_T_scheme_value_emitted"] is False, "cert numeric T")
    require(cert["checks"]["direct_N_H_value_emitted"] is False, "cert N_H")
    require(cert["checks"]["accepted_H_scalar_value_rows"] == 0, "cert rows")

    print("selected_hlambdarowlocaloverlapandscheme_or_directradialhessianvalue audit: PASS")


if __name__ == "__main__":
    main()
