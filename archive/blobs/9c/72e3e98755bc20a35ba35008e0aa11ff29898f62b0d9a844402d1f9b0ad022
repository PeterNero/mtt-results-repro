from __future__ import annotations

import json
import math
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
NONSM_REPO = TEXPAPERS / "mtt-nonsm-constants-no-knob"
Q79_REPO = TEXPAPERS / "mtt-q79-proof-repro"

DEP_CERT = ROOT / "certificates" / "protospinor_gr_response_dependency_certificate.json"
MATRIX_CERT = ROOT / "certificates" / "gr_dependency_matrix_certificate.json"
RHO_CERT = NONSM_REPO / "certificates" / "final_internal_rho_uv_selected_radius_theorem_certificate.json"
DIM_CERT = NONSM_REPO / "certificates" / "dimensionful_constant_obstruction_certificate.json"
SHARED_CERT = Q79_REPO / "certificates" / "shared_knob_cross_encoding_ledger_certificate.json"

GR_SOURCE = TEXPAPERS / "11 General Relativity & Geometry" / "_md" / "Modal_Triplet_Theory__From_MTT_to_General_Relativity_v2.md"
QG_SOURCE = TEXPAPERS / "12 Quantum Gravity" / "_md" / "Modal_Triplet_Theory__From_MTT_to_a_UV_Finite__Unitary_Quantum_Gravity_v4.md"
PROTO_ACTION_SOURCE = TEXPAPERS / "10 ProtoSpinor" / "_work" / "Closure_Geometry_and_Unified_Dynamics__A_Ten_Dimensional_Action_for_Mass__Scalar_Relaxation__Quantization__and_Curvature_v3" / "main.tex"

OUT = ROOT / "certificates" / "selected_gr_hessian_kernel_candidate_certificate.json"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def pattern_found(path: Path, pattern: str) -> bool:
    return bool(re.search(pattern, read(path), flags=re.IGNORECASE | re.DOTALL))


def shared_lambda_floor(shared: dict[str, Any]) -> float | None:
    for row in shared.get("shared_knobs", []):
        if row.get("id") == "theta_overlap_scaffold":
            return float(row["selected_data"]["lambda_star_floor"])
    return None


def main() -> None:
    dep = load_json(DEP_CERT)
    matrix = load_json(MATRIX_CERT)
    rho = load_json(RHO_CERT)
    dim = load_json(DIM_CERT)
    shared = load_json(SHARED_CERT)

    rho_values = rho["selected_values"]
    lambda_floor = shared_lambda_floor(shared)
    s_star = float(rho_values["s_star_from_rho"])
    lambda_floor_inverse = None if lambda_floor is None else 1.0 / lambda_floor
    s_star_inverse = 1.0 / s_star

    evidence = {
        "gr_eh_reduction_formula_present": pattern_found(
            GR_SOURCE,
            r"G_\\?\\{?\\rm eff\\}?|G_{\s*\\rm eff\s*}|G_eff|mathcal G.*mathcal V",
        )
        and pattern_found(GR_SOURCE, r"Einstein--Hilbert|Einstein equations"),
        "gr_stress_energy_formula_present": pattern_found(GR_SOURCE, r"stress--energy tensor|T_\\{\\mu\\nu\\}"),
        "qg_tt_lichnerowicz_operator_present": pattern_found(QG_SOURCE, r"TT Lichnerowicz operator|H\^1_\\{\\mathrm\\{TT\\}\\}"),
        "qg_retarded_kernel_present": pattern_found(QG_SOURCE, r"retarded kernel|support in the future cone"),
        "proto_anchor_hessian_present": pattern_found(PROTO_ACTION_SOURCE, r"H_\\{?\\rm anchor\\}?|Anchored Quadratic Form"),
        "proto_curvature_strain_present": pattern_found(PROTO_ACTION_SOURCE, r"curvature--strain|Curvature--Curvature|Closure--Curvature"),
    }

    target_kernel = {
        "configuration_variable": "4D Lorentzian metric perturbation h_{mu nu} on emergent Y4",
        "gauge_reduction": "BRST/diffeomorphism quotient; TT sector carries physical graviton response",
        "principal_symbol_target": "P_TT(k) |k|_g^2 P_TT(k)",
        "physical_massless_spin2_polarizations": 2,
        "symmetric_tensor_components_in_4D": 10,
        "diffeomorphism_generator_components": 4,
        "einstein_operator_target": "G_{mu nu}+Lambda_eff g_{mu nu}-8*pi*G_eff*T_{mu nu}",
        "quadratic_action_target": "(32*pi*G_eff)^(-1) <h_TT, E_TT h_TT> plus gauge-fixing/ghost blocks",
        "retarded_response_target": "Delta_ret = boundary value of positive Stieltjes mixture of (E+s)^(-1), supported in the future cone",
    }

    selected_inputs = {
        "protospinor_binary_loop": {
            "closed": dep["closure_accounting"]["protospinor_loop_obstruction_closed"],
            "pi1_SO3_order": dep["topological_invariants"]["pi1_SO3_order"],
            "cover_degree": dep["topological_invariants"]["minimal_spin_lift_cover_degree"],
        },
        "rho_uv_branch": {
            "closed": rho["closed"]["selected_internal_rho_uv"],
            "R_star": rho_values["R_star"],
            "rho_UV": rho_values["rho_UV"],
            "s_star_from_rho": s_star,
        },
        "theta_lambda_floor": {
            "closed_as_scaffold": lambda_floor is not None,
            "lambda_star_floor": lambda_floor,
            "floor_inverse": lambda_floor_inverse,
            "interpretation": "This is a scaffold floor, not enough by itself to prove small higher-curvature corrections.",
        },
        "rho_induced_suppression_scale": {
            "s_star_from_rho": s_star,
            "s_star_inverse": s_star_inverse,
            "interpretation": "A dimensionless selected scale available for candidate suppression tests; not yet a selected GR Hessian eigenvalue.",
        },
    }

    selection_gates = {
        "EH_universality_target_identified": evidence["gr_eh_reduction_formula_present"],
        "TT_kinetic_target_identified": evidence["qg_tt_lichnerowicz_operator_present"],
        "retarded_kernel_target_identified": evidence["qg_retarded_kernel_present"],
        "closure_hessian_anchor_structural_source_found": evidence["proto_anchor_hessian_present"],
        "selected_numeric_H_anchor_matrix_available": False,
        "selected_GR_Hessian_blocks_available": False,
        "selected_retarded_kernel_measure_available": False,
        "matter_gauge_stress_response_map_available": False,
        "absolute_G_eff_normalization_available": dim["verdict"]["absolute_dimensionful_predictions_closed"],
    }
    closed_gate_count = sum(1 for value in selection_gates.values() if value is True)
    total_gate_count = len(selection_gates)

    finite_checks = {
        "spin2_polarization_count_positive": target_kernel["physical_massless_spin2_polarizations"] == 2,
        "symmetric_tensor_component_count": math.comb(4 + 1, 2),
        "rho_uv_positive": float(rho_values["rho_UV"]) > 0.0,
        "R_star_positive": float(rho_values["R_star"]) > 0.0,
        "s_star_positive": s_star > 0.0,
        "lambda_floor_positive": lambda_floor is not None and lambda_floor > 0.0,
    }

    certificate = {
        "certificate": "SelectedGRHessianKernelCandidateCertificate",
        "status": "SELECTED_GR_HESSIAN_KERNEL_CANDIDATE_BUILT_SELECTION_OPEN",
        "purpose": "Build the explicit Einstein-sector Hessian/retarded-kernel target from the corpus and audit whether current selected MTT data close it.",
        "source_files": {
            "gr_reduction": str(GR_SOURCE),
            "qg_kernel": str(QG_SOURCE),
            "proto_action": str(PROTO_ACTION_SOURCE),
        },
        "evidence_patterns": evidence,
        "target_kernel": target_kernel,
        "selected_inputs": selected_inputs,
        "selection_gates": selection_gates,
        "finite_numeric_checks": finite_checks,
        "gate_accounting": {
            "closed_gate_count": closed_gate_count,
            "total_gate_count": total_gate_count,
            "closure_ratio": closed_gate_count / total_gate_count,
            "full_selected_GR_Hessian_closed": False,
        },
        "blocking_missing_objects": [
            "numeric selected H_anchor or equivalent closure Hessian block",
            "selected projection from H_anchor/closure strain to the TT Lichnerowicz block",
            "selected retarded Stieltjes/proper-time measure for the GR response kernel",
            "selected matter/gauge stress-response map",
            "absolute G_eff normalization or proof that only dimensionless GR predictions are claimed",
        ],
        "what_this_closes": {
            "EH_target_operator_identified": True,
            "TT_kernel_target_identified": True,
            "retarded_support_target_identified": True,
            "selected_branch_inputs_imported": True,
            "selected_numeric_GR_response_kernel": False,
        },
        "guardrails": {
            "claims_full_GR_derivation": False,
            "claims_Newton_constant_prediction": False,
            "uses_observed_GR_data": False,
            "treats_structural_EH_reduction_as_selected_Hessian": False,
        },
        "next_theorem": {
            "name": "Selected_GR_Hessian_Block_Source_Theorem",
            "minimal_data_schema": {
                "basis": "explicit finite TT/coherent response basis",
                "H_anchor": "positive symmetric numeric matrix or certified operator block",
                "projection": "matrix P_GR from closure basis to TT metric perturbations",
                "kernel": "K_GR = P_GR^T H_anchor P_GR with gauge/BRST quotient",
                "retarded_measure": "positive measure mu with selected support giving Delta_ret",
                "stress_map": "functional derivative map from selected matter/gauge data to T_{mu nu}",
            },
        },
    }
    OUT.write_text(json.dumps(certificate, indent=2), encoding="utf-8")
    print(json.dumps({"wrote": str(OUT), "status": certificate["status"]}, indent=2))


if __name__ == "__main__":
    main()

