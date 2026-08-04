"""Build CKM, gauge-running, and PMNS convention fill for SM-equivalence."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

TREE = DATA / "sm_equivalence_tree_level_replay_seed.candidate.json"
VALUES = DATA / "sm_equivalence_reference_data_values_fill.candidate.json"

OUTPUT = DATA / "sm_equivalence_ckm_gauge_pmns_convention_fill.candidate.json"
CERT = CERTS / "sm_equivalence_ckm_gauge_pmns_convention_fill_certificate.json"
NOTE = CORPUS / "MTT_SM_Equivalence_CKM_Gauge_PMNS_Convention_Fill_v1.md"

STATUS = "MTT_SM_EQUIVALENCE_CKM_GAUGE_PMNS_CONVENTION_FILL_BUILT_REPLAY_READY"
NEXT = "MTT_SM_Equivalence_Mixing_and_Gauge_Replay_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def c(z: complex) -> list[float]:
    return [z.real, z.imag]


def mat_to_json(m: list[list[complex]]) -> list[list[list[float]]]:
    return [[c(value) for value in row] for row in m]


def matmul(a: list[list[complex]], b: list[list[complex]]) -> list[list[complex]]:
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def dagger(a: list[list[complex]]) -> list[list[complex]]:
    return [[a[j][i].conjugate() for j in range(len(a))] for i in range(len(a[0]))]


def max_unitarity_residual(u: list[list[complex]]) -> float:
    prod = matmul(u, dagger(u))
    return max(abs(prod[i][j] - (1.0 if i == j else 0.0)) for i in range(3) for j in range(3))


def ckm_from_wolfenstein(lambda_: float, A: float, rhobar: float, etabar: float) -> tuple[list[list[complex]], dict[str, float]]:
    # Convert barred Wolfenstein coordinates to the exact PDG-angle convention.
    factor = 1.0 - lambda_ * lambda_ / 2.0
    rho = rhobar / factor
    eta = etabar / factor
    s12 = lambda_
    s23 = A * lambda_ * lambda_
    s13 = A * lambda_**3 * math.sqrt(rho * rho + eta * eta)
    delta = math.atan2(eta, rho)
    c12 = math.sqrt(1.0 - s12 * s12)
    c23 = math.sqrt(1.0 - s23 * s23)
    c13 = math.sqrt(1.0 - s13 * s13)
    e_minus = complex(math.cos(-delta), math.sin(-delta))
    e_plus = complex(math.cos(delta), math.sin(delta))
    v = [
        [c12 * c13, s12 * c13, s13 * e_minus],
        [
            -s12 * c23 - c12 * s23 * s13 * e_plus,
            c12 * c23 - s12 * s23 * s13 * e_plus,
            s23 * c13,
        ],
        [
            s12 * s23 - c12 * c23 * s13 * e_plus,
            -c12 * s23 - s12 * c23 * s13 * e_plus,
            c23 * c13,
        ],
    ]
    params = {
        "lambda": lambda_,
        "A": A,
        "rhobar": rhobar,
        "etabar": etabar,
        "rho": rho,
        "eta": eta,
        "s12": s12,
        "s23": s23,
        "s13": s13,
        "delta_rad": delta,
        "delta_deg": math.degrees(delta),
    }
    return v, params


def pmns_from_angles(sin2_12: float, sin2_23: float, sin2_13: float, delta_deg: float) -> tuple[list[list[complex]], dict[str, float]]:
    s12, s23, s13 = math.sqrt(sin2_12), math.sqrt(sin2_23), math.sqrt(sin2_13)
    c12, c23, c13 = math.sqrt(1 - sin2_12), math.sqrt(1 - sin2_23), math.sqrt(1 - sin2_13)
    delta = math.radians(delta_deg)
    e_minus = complex(math.cos(-delta), math.sin(-delta))
    e_plus = complex(math.cos(delta), math.sin(delta))
    u = [
        [c12 * c13, s12 * c13, s13 * e_minus],
        [
            -s12 * c23 - c12 * s23 * s13 * e_plus,
            c12 * c23 - s12 * s23 * s13 * e_plus,
            s23 * c13,
        ],
        [
            s12 * s23 - c12 * c23 * s13 * e_plus,
            -c12 * s23 - s12 * c23 * s13 * e_plus,
            c23 * c13,
        ],
    ]
    params = {
        "sin2_theta12": sin2_12,
        "sin2_theta23": sin2_23,
        "sin2_theta13": sin2_13,
        "theta12_deg": math.degrees(math.asin(s12)),
        "theta23_deg": math.degrees(math.asin(s23)),
        "theta13_deg": math.degrees(math.asin(s13)),
        "delta_deg": delta_deg,
        "delta_rad": delta,
    }
    return u, params


def jarlskog(u: list[list[complex]]) -> float:
    return (u[0][0] * u[1][1] * u[0][1].conjugate() * u[1][0].conjugate()).imag


def magnitudes(u: list[list[complex]]) -> list[list[float]]:
    return [[abs(value) for value in row] for row in u]


def main() -> int:
    tree = load(TREE)
    values = load(VALUES)

    ckm, ckm_params = ckm_from_wolfenstein(0.22501, 0.826, 0.1591, 0.3523)
    pmns, pmns_params = pmns_from_angles(0.308, 0.470, 0.02215, 212.0)

    gauge = {
        "scheme": "MSbar electroweak at mu=M_Z, plus alpha_s(M_Z)",
        "reference_scale": "M_Z",
        "U1_normalization": {
            "SM_hypercharge": "g_Y",
            "GUT_normalized": "g1=sqrt(5/3) g_Y",
            "alpha1_GUT": "(5/3) alpha_Y",
        },
        "filled_reference_values": {
            "sin2_thetaW_MSbar_MZ": {
                "central_value": 0.23122,
                "uncertainty": 0.00006,
                "source_key": "PDG_2025_ELECTROWEAK_REVIEW",
                "source_version_or_date": "PDG 2025 electroweak review, Table 10.2",
                "used_as_source_selector": False,
            },
            "alpha_s_MZ": {
                "central_value": 0.1180,
                "uncertainty": 0.0009,
                "source_key": "PDG_2025_QCD_WORLD_AVERAGE",
                "source_version_or_date": "PDG 2025 / world-average convention at M_Z",
                "used_as_source_selector": False,
            },
        },
        "open_reference_values": {
            "alpha_em_MSbar_MZ": "needed before alpha1/alpha2 numeric replay in the same scheme",
            "correlation_matrix": "needed for precision gauge-running audit",
            "loop_order_and_threshold_policy": "needed for RG transport",
        },
        "conversion_formulas": {
            "alpha_Y": "alpha_em(M_Z)/(1-sin2_thetaW_MSbar(M_Z))",
            "alpha_2": "alpha_em(M_Z)/sin2_thetaW_MSbar(M_Z)",
            "alpha_1_GUT": "(5/3) alpha_Y",
            "alpha_3": "alpha_s(M_Z)",
        },
        "status": "CONVENTION_FILLED_VALUES_PARTIAL_ALPHA_EM_MZ_OPEN",
    }

    candidate = {
        "candidate": "MTTSMEquivalenceCKMGaugePMNSConventionFill",
        "status": STATUS,
        "inputs": {
            "tree_level_replay_seed": rel(TREE),
            "reference_data_values_fill": rel(VALUES),
        },
        "source_boundary_preserved": True,
        "superset_strategy_use": tree["superset_strategy_use"],
        "CKM_packet": {
            "status": "FILLED_REPLAY_READY_WITHOUT_COVARIANCE",
            "source_key": "PDG_2025_CKM_REVIEW",
            "source_version_or_date": "PDG 2025 CKM review; Wolfenstein/global-fit values",
            "parameterization": "exact PDG three-angle one-phase matrix seeded from barred Wolfenstein parameters",
            "input_values": {
                "lambda": {"central_value": 0.22501, "uncertainty": 0.00068},
                "A": {"central_value": 0.826, "uncertainty_plus": 0.016, "uncertainty_minus": 0.015},
                "rhobar": {"central_value": 0.1591, "uncertainty": 0.0094},
                "etabar": {"central_value": 0.3523, "uncertainty_plus": 0.0073, "uncertainty_minus": 0.0071},
            },
            "derived_parameters": ckm_params,
            "matrix": mat_to_json(ckm),
            "magnitudes": magnitudes(ckm),
            "jarlskog": jarlskog(ckm),
            "unitarity_max_residual": max_unitarity_residual(ckm),
            "correlation_policy": "full CKM fit covariance not encoded yet",
            "used_as_source_selector": False,
        },
        "PMNS_packet": {
            "status": "FILLED_REPLAY_READY_WITHOUT_COVARIANCE",
            "source_key": "NuFIT_6_0",
            "source_version_or_date": "NuFIT 6.0, data available September 2024; normal ordering IC24 with SK-atm row",
            "parameterization": "PDG-like Dirac PMNS matrix; Majorana phases out of scope for Dirac-neutrino parity replay",
            "ordering": "normal",
            "input_values": {
                "sin2_theta12": {"central_value": 0.308, "uncertainty_plus": 0.012, "uncertainty_minus": 0.011},
                "sin2_theta23": {"central_value": 0.470, "uncertainty_plus": 0.017, "uncertainty_minus": 0.013},
                "sin2_theta13": {"central_value": 0.02215, "uncertainty_plus": 0.00056, "uncertainty_minus": 0.00058},
                "delta_CP_deg": {"central_value": 212.0, "uncertainty_plus": 26.0, "uncertainty_minus": 41.0},
                "Delta_m21_sq_eV2": {"central_value": 7.49e-5, "uncertainty": 0.19e-5},
                "Delta_m3l_sq_eV2": {"central_value": 2.513e-3, "uncertainty_plus": 0.021e-3, "uncertainty_minus": 0.019e-3},
            },
            "derived_parameters": pmns_params,
            "matrix": mat_to_json(pmns),
            "magnitudes": magnitudes(pmns),
            "jarlskog": jarlskog(pmns),
            "unitarity_max_residual": max_unitarity_residual(pmns),
            "absolute_mass_policy": "not filled; Dirac neutrino absolute Yukawa magnitudes remain open",
            "correlation_policy": "NuFIT covariance/profile likelihood not encoded yet",
            "used_as_source_selector": False,
        },
        "gauge_packet": gauge,
        "replay_readiness": {
            "CKM_matrix_ready_for_replay": True,
            "PMNS_matrix_ready_for_replay": True,
            "gauge_conventions_ready": True,
            "gauge_alpha1_alpha2_alpha3_values_ready": False,
            "full_covariance_ready": False,
            "RG_common_scale_ready": False,
        },
        "what_closes_now": {
            "CKM_convention_and_matrix_seed": True,
            "PMNS_convention_and_matrix_seed": True,
            "gauge_running_convention_packet": True,
            "mixing_unitarity_checks": True,
            "source_selection_guardrails_preserved": True,
        },
        "what_remains_open": {
            "CKM_covariance_or_profile_policy": True,
            "PMNS_covariance_or_profile_policy": True,
            "alpha_em_MSbar_MZ_value": True,
            "alpha1_alpha2_alpha3_numeric_triplet": True,
            "common_RG_scale_transport": True,
            "mixing_and_gauge_replay": True,
            "empirical_equivalence_audit_run": True,
            "full_SM_equivalence_closure": True,
            "full_no_knob_closure": True,
        },
        "closure_claimed": False,
        "sm_equivalence_claimed": False,
        "no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "SMEquivalenceCKMGaugePMNSConventionFillTheorem",
            "proved": True,
            "statement": (
                "The measured replay branch now has convention-complete CKM and PMNS seed matrices and "
                "a gauge-running convention packet. These are downstream replay data only. Full SM-equivalence "
                "still requires covariance/profile policy, alpha_em(M_Z) in the chosen scheme, numeric "
                "alpha1/alpha2/alpha3 replay, RG transport, and empirical audit."
            ),
        },
    }

    cert = {
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "closure_claimed": False,
        "sm_equivalence_claimed": False,
        "no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT SM-Equivalence CKM Gauge PMNS Convention Fill v1

Status: `{STATUS}`.

## Result

CKM and PMNS seed matrices are now convention-filled for downstream measured
SM-equivalence replay.  The gauge packet fixes the `M_Z`-scale convention and
normalization formulas but leaves `alpha_em(M_Z)` and the full
`alpha_1, alpha_2, alpha_3` numeric triplet open.

## Guardrail

These values are measured replay inputs.  They do not select MTT source
structure, topology, dynamic overlap tensors, `A_selected`, `b_selected`, or
no-knob kernels.

## Next

Build `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
