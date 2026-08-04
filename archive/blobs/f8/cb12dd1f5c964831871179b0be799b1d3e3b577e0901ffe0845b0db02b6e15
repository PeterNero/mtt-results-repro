from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NONSM = ROOT.parent / "mtt-nonsm-constants-no-knob"

OMEGA_GAP = ROOT / "certificates" / "selected_physical_omega_gap_theorem_certificate.json"
SCALE_COEFF = NONSM / "certificates" / "selected_scale_coefficient_extraction_certificate.json"
RHO_UNIT_NO_GO = NONSM / "certificates" / "selected_rho_uv_unit_covariance_no_go_certificate.json"
RHO_RESPONSE_ATTEMPT = NONSM / "certificates" / "selected_rho_uv_response_ratio_computation_attempt_certificate.json"
SUPERSET_RHO = NONSM / "certificates" / "superset_rho_uv_cross_encoding_gate_certificate.json"

OUT_CERT = ROOT / "certificates" / "selected_higher_order_correction_and_disturbance_covariance_theorem_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "Selected_Higher_Order_Correction_and_Disturbance_Covariance_Theorem_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    omega_gap = load(OMEGA_GAP)
    scale_coeff = load(SCALE_COEFF)
    rho_unit_no_go = load(RHO_UNIT_NO_GO)
    rho_response_attempt = load(RHO_RESPONSE_ATTEMPT)
    superset_rho = load(SUPERSET_RHO)

    closed_positive = rho_unit_no_go["already_closed_positive_data"]
    response_computed = rho_response_attempt["computed"]
    scale_extracted = scale_coeff["extracted_coefficients"]

    closed_inputs = {
        "omega_gap_reduced_to_source_data": omega_gap["status"]
        == "OMEGA_GAP_THEOREM_REDUCED_TO_CUV_DELTA_AND_OMEGA0_SOURCE_DATA",
        "scale_minimizer_formula_fixed": scale_coeff["verdict"]["formula_level_coefficient_gap_fixed"],
        "kappa_extracted": scale_coeff["verdict"]["kappa_extracted"],
        "unit_covariance_shortcut_refuted": rho_unit_no_go["verdict"]["unit_covariance_shortcut_valid"] is False,
        "G_11_closed": closed_positive["G_11"] == 1.0,
        "U_support_closed": rho_response_attempt["verdict"]["U_support_closed"],
        "symbolic_rho_formula_computed": rho_response_attempt["verdict"]["symbolic_rho_formula_computed"],
        "retarded_kernel_z64_closed": closed_positive["K_ret_64"] == "S^-1=S^63",
        "internal_lambda_closed": closed_positive["lambda_star"] == 15.0,
        "superset_route_formulated": superset_rho["verdict"]["superset_route_formulated"],
        "threshold_delta_forbidden": superset_rho["verdict"]["threshold_delta_forbidden"],
    }

    primitive_source_objects = {
        "C_UV": {
            "meaning": "selected O(alpha'^2) / curvature UV correction coefficient",
            "current_status": "symbolic support only; no source-certified value",
            "known_row": response_computed["U_raw"],
            "known_formula": response_computed["v1_tilde_alpha_prime_1"],
            "needed_theorem": (
                "evaluate the selected higher-order correction functional on the same "
                "exact branch and inner product"
            ),
        },
        "Q_tau": {
            "meaning": "selected unresolved finite-memory carrier covariance",
            "current_status": "not supplied by current corpus",
            "projected_norm_formula": rho_unit_no_go["remaining_repair_calculation"]["formula"],
            "needed_theorem": (
                "derive Q_tau from the selected carrier geometry and compatible "
                "fluctuation-dissipation pair"
            ),
        },
        "Omega_0": {
            "meaning": "remaining physical inverse-length/action unit",
            "current_status": "not selected",
            "needed_theorem": (
                "connect the source-certified correction/covariance normalization to a "
                "physical unit without observed target constants"
            ),
        },
    }

    repaired_rho_formula = {
        "G_11": closed_positive["G_11"],
        "U_raw": response_computed["U_raw"],
        "U_norm_squared": f"({response_computed['v1_tilde_alpha_prime_1']})^2",
        "D_raw_norm_squared": "d_Q = int_R P K_ret Q_tau K_ret^* P^* dt",
        "rho_UV": "C_UV^2 / delta = ||U||^2 / d_Q",
        "s_star": scale_extracted["s_star_after_kappa_extraction"],
        "omega_gap_phys": "Omega_0 / s_star",
        "Lambda_gap_phys": "sqrt(15) * Omega_0 / s_star",
    }

    guardrails = {
        "sets_D_raw_norm_to_one": False,
        "imports_threshold_delta_as_covariance": False,
        "uses_theta_5TeV_as_prediction": False,
        "uses_observed_Newton_or_Planck": False,
        "claims_C_UV_numeric": False,
        "claims_Q_tau_numeric": False,
        "claims_Omega_0_numeric": False,
        "claims_physical_SM_or_GR_closure": False,
    }

    open_gates = {
        "selected_higher_order_correction_functional_evaluated": False,
        "selected_finite_memory_covariance_Q_tau_derived": False,
        "projected_covariance_integral_d_Q_evaluated": False,
        "same_branch_fluctuation_dissipation_theorem": False,
        "physical_Omega_0_selected": False,
    }

    theorem_ready = all(closed_inputs.values())
    fully_closed = theorem_ready and all(open_gates.values())
    status = (
        "SOURCE_DATA_THEOREM_REDUCED_TO_QTAU_CUV_AND_OMEGA0"
        if theorem_ready and not fully_closed
        else "SOURCE_DATA_THEOREM_CLOSED"
        if fully_closed
        else "SOURCE_DATA_THEOREM_NOT_READY"
    )

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "selected_higher_order_correction_and_disturbance_covariance_theorem",
        "status": status,
        "input_certificates": {
            "selected_physical_omega_gap_theorem": str(OMEGA_GAP),
            "selected_scale_coefficient_extraction": str(SCALE_COEFF),
            "selected_rho_uv_unit_covariance_no_go": str(RHO_UNIT_NO_GO),
            "selected_rho_uv_response_ratio_computation_attempt": str(RHO_RESPONSE_ATTEMPT),
            "superset_rho_uv_cross_encoding_gate": str(SUPERSET_RHO),
        },
        "closed_inputs": closed_inputs,
        "primitive_source_objects": primitive_source_objects,
        "repaired_rho_formula": repaired_rho_formula,
        "open_gates": open_gates,
        "guardrails": guardrails,
        "theorem": {
            "name": "Selected_Higher_Order_Correction_and_Disturbance_Covariance_Theorem.v1",
            "status": "REDUCED_NOT_CLOSED",
            "statement": (
                "The remaining physical omega-gap source-data problem is exactly the "
                "same-branch computation of the selected higher-order correction "
                "coefficient C_UV, the selected finite-memory covariance Q_tau, and "
                "the physical unit Omega_0. Current evidence closes the symbolic UV "
                "row, G_11=1, kappa=1, lambda=15, and K_ret,64=S^-1=S^63, while "
                "refuting the unit-covariance shortcut."
            ),
            "conditional_closure": (
                "If the selected branch supplies C_UV and Q_tau with "
                "d_Q=int_R P K_ret Q_tau K_ret^* P^* dt > 0, then "
                "rho_UV=C_UV^2/d_Q and s_star=(60 rho_UV)^(1/6). If the same "
                "source theorem also supplies Omega_0, then "
                "Lambda_gap_phys=sqrt(15)*Omega_0/s_star and the previous modal "
                "gap bridge yields ell_p, kappa_11, G_eff, and kappa_STF."
            ),
        },
        "next_required_artifacts": [
            "Selected_Finite_Memory_Carrier_Covariance_Computation_v1",
            "Selected_Higher_Order_Correction_Functional_Evaluation_v1",
            "Selected_Physical_Omega0_Source_Theorem_v1",
        ],
        "note_written": str(OUT_NOTE),
    }

    note = f"""# Selected Higher-Order Correction and Disturbance Covariance Theorem v1

## Result

The physical source-data problem has been made exact. It is not closed yet, but
the current corpus no longer leaves a vague normalization gap.

Closed same-branch data:

```text
G_11 = 1
U_raw = {response_computed["U_raw"]}
v1_tilde(alpha_prime=1) = {response_computed["v1_tilde_alpha_prime_1"]}
kappa = 1
lambda_internal = 15
K_ret,64 = S^-1 = S^63
```

The unit-covariance shortcut is refuted. The disturbance denominator must be
computed as the selected finite-memory projection

```text
d_Q = int_R P K_ret Q_tau K_ret^* P^* dt
rho_UV = C_UV^2 / d_Q
s_star = (60 rho_UV)^(1/6)
Lambda_gap_phys = sqrt(15) * Omega_0 / s_star
```

## What Remains

Three primitive source objects remain:

```text
C_UV   selected higher-order correction coefficient
Q_tau  selected unresolved finite-memory carrier covariance
Omega_0 physical inverse-length/action unit
```

This is the correct next gate because it prevents two bad moves: setting
`||D_raw||^2=1` by convention, and importing the unrelated threshold `delta`
as the OU/covariance denominator.

## Conditional Closure

If the branch supplies `C_UV`, derives `Q_tau`, evaluates `d_Q>0`, and supplies
`Omega_0` without observed target constants, then the earlier physical omega-gap
and modal-gap bridge certificates close the path to `ell_p`, `kappa_11`,
`G_eff`, and the TT Einstein-response scale.
"""

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {status}")


if __name__ == "__main__":
    main()
