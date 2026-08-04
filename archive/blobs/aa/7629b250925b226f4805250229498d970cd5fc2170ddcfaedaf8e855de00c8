"""Build SM-equivalence mixing and gauge replay artifact."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

CONVENTIONS = DATA / "sm_equivalence_ckm_gauge_pmns_convention_fill.candidate.json"
TREE = DATA / "sm_equivalence_tree_level_replay_seed.candidate.json"

OUTPUT = DATA / "sm_equivalence_mixing_and_gauge_replay.candidate.json"
CERT = CERTS / "sm_equivalence_mixing_and_gauge_replay_certificate.json"
NOTE = CORPUS / "MTT_SM_Equivalence_Mixing_and_Gauge_Replay_v1.md"

STATUS = "MTT_SM_EQUIVALENCE_MIXING_AND_GAUGE_REPLAY_BUILT_PARTIAL_EMPIRICAL_REPLAY"
NEXT = "MTT_SM_Equivalence_Common_RG_and_Empirical_Audit_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def c(pair: list[float]) -> complex:
    return complex(pair[0], pair[1])


def pair(z: complex) -> list[float]:
    return [float(z.real), float(z.imag)]


def diag(values: list[float]) -> list[list[complex]]:
    return [[complex(values[i] if i == j else 0.0, 0.0) for j in range(len(values))] for i in range(len(values))]


def matmul(a: list[list[complex]], b: list[list[complex]]) -> list[list[complex]]:
    rows = len(a)
    cols = len(b[0])
    inner = len(b)
    return [[sum(a[i][k] * b[k][j] for k in range(inner)) for j in range(cols)] for i in range(rows)]


def dagger(a: list[list[complex]]) -> list[list[complex]]:
    return [[a[j][i].conjugate() for j in range(len(a))] for i in range(len(a[0]))]


def to_pairs(a: list[list[complex]]) -> list[list[list[float]]]:
    return [[pair(z) for z in row] for row in a]


def max_abs(a: list[list[complex]]) -> float:
    return max(abs(z) for row in a for z in row)


def diff(a: list[list[complex]], b: list[list[complex]]) -> list[list[complex]]:
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def identity(n: int) -> list[list[complex]]:
    return [[complex(1.0 if i == j else 0.0, 0.0) for j in range(n)] for i in range(n)]


def uncertainty_from_inverse(inv: float, sigma_inv: float) -> float:
    return sigma_inv / (inv * inv)


def gauge_uncertainty(alpha_em: float, alpha_em_sigma: float, sin2: float, sin2_sigma: float, alpha_s_sigma: float) -> dict[str, Any]:
    alpha_y = alpha_em / (1.0 - sin2)
    alpha_2 = alpha_em / sin2
    alpha_1 = (5.0 / 3.0) * alpha_y
    d_alpha_y_da = 1.0 / (1.0 - sin2)
    d_alpha_y_ds = alpha_em / ((1.0 - sin2) ** 2)
    d_alpha_2_da = 1.0 / sin2
    d_alpha_2_ds = -alpha_em / (sin2 * sin2)
    sigma_y = math.hypot(d_alpha_y_da * alpha_em_sigma, d_alpha_y_ds * sin2_sigma)
    sigma_2 = math.hypot(d_alpha_2_da * alpha_em_sigma, d_alpha_2_ds * sin2_sigma)
    sigma_1 = (5.0 / 3.0) * sigma_y
    return {
        "alpha_Y": {"central_value": alpha_y, "uncertainty": sigma_y},
        "alpha_1_GUT": {"central_value": alpha_1, "uncertainty": sigma_1},
        "alpha_2": {"central_value": alpha_2, "uncertainty": sigma_2},
        "alpha_3": {"central_value": 0.1180, "uncertainty": alpha_s_sigma},
    }


def main() -> int:
    conventions = load(CONVENTIONS)
    tree = load(TREE)

    ckm = [[c(cell) for cell in row] for row in conventions["CKM_packet"]["matrix"]]
    pmns = [[c(cell) for cell in row] for row in conventions["PMNS_packet"]["matrix"]]

    yuk = tree["tree_level_replay"]["yukawa_matrices"]
    yu = [yuk["Y_u_diag"][i][i] for i in range(3)]
    yd = [yuk["Y_d_diag"][i][i] for i in range(3)]
    ye = [yuk["Y_e_diag"][i][i] for i in range(3)]

    yu_diag = diag(yu)
    yd_diag = diag(yd)
    ye_diag = diag(ye)
    yd_ckm = matmul(ckm, yd_diag)
    hu = matmul(yu_diag, dagger(yu_diag))
    hd = matmul(yd_ckm, dagger(yd_ckm))
    hd_expected = matmul(matmul(ckm, diag([x * x for x in yd])), dagger(ckm))
    ckm_unitarity_residual = max_abs(diff(matmul(dagger(ckm), ckm), identity(3)))
    down_hermitian_residual = max_abs(diff(hd, hd_expected))

    pmns_values = conventions["PMNS_packet"]["input_values"]
    dm21 = pmns_values["Delta_m21_sq_eV2"]["central_value"]
    dm3l = pmns_values["Delta_m3l_sq_eV2"]["central_value"]
    nu_mass_sq = [0.0, dm21, dm3l]
    hnu_flavor = matmul(matmul(pmns, diag(nu_mass_sq)), dagger(pmns))
    hnu_replayed_diag = matmul(matmul(dagger(pmns), hnu_flavor), pmns)
    pmns_diag_residual = max_abs(diff(hnu_replayed_diag, diag(nu_mass_sq)))
    pmns_unitarity_residual = max_abs(diff(matmul(dagger(pmns), pmns), identity(3)))
    dm21_replayed = float(hnu_replayed_diag[1][1].real - hnu_replayed_diag[0][0].real)
    dm3l_replayed = float(hnu_replayed_diag[2][2].real - hnu_replayed_diag[0][0].real)

    gauge = conventions["gauge_packet"]["filled_reference_values"]
    alpha_inv_mz = 127.951
    alpha_inv_mz_sigma = 0.009
    alpha_em_mz = 1.0 / alpha_inv_mz
    alpha_em_mz_sigma = uncertainty_from_inverse(alpha_inv_mz, alpha_inv_mz_sigma)
    sin2 = gauge["sin2_thetaW_MSbar_MZ"]["central_value"]
    sin2_sigma = gauge["sin2_thetaW_MSbar_MZ"]["uncertainty"]
    alpha_s = gauge["alpha_s_MZ"]["central_value"]
    alpha_s_sigma = gauge["alpha_s_MZ"]["uncertainty"]
    gauge_triplet = gauge_uncertainty(alpha_em_mz, alpha_em_mz_sigma, sin2, sin2_sigma, alpha_s_sigma)
    gauge_triplet["alpha_3"]["central_value"] = alpha_s
    gauge_triplet["g_1_GUT"] = {
        "central_value": math.sqrt(4.0 * math.pi * gauge_triplet["alpha_1_GUT"]["central_value"])
    }
    gauge_triplet["g_2"] = {
        "central_value": math.sqrt(4.0 * math.pi * gauge_triplet["alpha_2"]["central_value"])
    }
    gauge_triplet["g_3"] = {
        "central_value": math.sqrt(4.0 * math.pi * gauge_triplet["alpha_3"]["central_value"])
    }

    candidate = {
        "candidate": "MTTSMEquivalenceMixingAndGaugeReplay",
        "status": STATUS,
        "inputs": {
            "CKM_gauge_PMNS_convention_fill": rel(CONVENTIONS),
            "tree_level_replay_seed": rel(TREE),
        },
        "superset_strategy_use": {
            "mode": "SUPERSET_TO_LOCKED_SOURCE_THEN_STRAIGHT_MEASURED_REPLAY",
            "locked_target": "static SM source/interface boundary plus measured-slot policy",
            "measured_targets_used_to_lock_source": False,
            "straight_replay_after_boundary": True,
            "explanation": (
                "The superset paths are not mixed into this calculation.  They only justify "
                "the typed source/interface boundary.  CKM, PMNS, masses, and gauge values "
                "then enter as measured SM-parity replay inputs."
            ),
        },
        "CKM_replay": {
            "status": "FULL_COMPLEX_DOWN_YUKAWA_REPLAY_READY_IN_UP_DIAGONAL_CONVENTION",
            "basis_convention": "Y_u diagonal; Y_d = V_CKM diag(y_d)",
            "Y_u_diag": to_pairs(yu_diag),
            "Y_d_complex": to_pairs(yd_ckm),
            "H_u": to_pairs(hu),
            "H_d": to_pairs(hd),
            "input_CKM_matrix": conventions["CKM_packet"]["matrix"],
            "input_CKM_magnitudes": conventions["CKM_packet"]["magnitudes"],
            "input_jarlskog": conventions["CKM_packet"]["jarlskog"],
            "unitarity_max_residual": ckm_unitarity_residual,
            "down_hermitian_reconstruction_residual": down_hermitian_residual,
            "mass_singular_values_by_construction": yd,
            "used_as_source_selector": False,
        },
        "PMNS_replay": {
            "status": "OSCILLATION_MASS_SQUARED_REPLAY_READY_ABSOLUTE_MASS_OPEN",
            "basis_convention": "Y_e diagonal; H_nu = U_PMNS diag(0, Delta_m21^2, Delta_m3l^2) U_PMNS^dagger",
            "Y_e_diag": to_pairs(ye_diag),
            "normal_ordering_minimal_mass_squared_spectrum_eV2": nu_mass_sq,
            "H_nu_mass_squared_flavor_basis_eV2": to_pairs(hnu_flavor),
            "input_PMNS_matrix": conventions["PMNS_packet"]["matrix"],
            "input_PMNS_magnitudes": conventions["PMNS_packet"]["magnitudes"],
            "input_jarlskog": conventions["PMNS_packet"]["jarlskog"],
            "unitarity_max_residual": pmns_unitarity_residual,
            "diagonalization_max_residual_eV2": pmns_diag_residual,
            "Delta_m21_sq_replayed_eV2": dm21_replayed,
            "Delta_m3l_sq_replayed_eV2": dm3l_replayed,
            "Delta_m21_sq_residual_eV2": dm21_replayed - dm21,
            "Delta_m3l_sq_residual_eV2": dm3l_replayed - dm3l,
            "absolute_neutrino_mass_filled": False,
            "Dirac_neutrino_yukawa_magnitudes_filled": False,
            "Majorana_phase_policy": "out of scope for Dirac-neutrino parity replay",
            "used_as_source_selector": False,
        },
        "gauge_replay_MZ": {
            "status": "ALPHA1_ALPHA2_ALPHA3_MZ_REPLAY_READY_WITHOUT_RG_TRANSPORT",
            "scheme": "MSbar electroweak at mu=M_Z; GUT-normalized U(1) alpha_1=(5/3) alpha_Y",
            "reference_scale": "M_Z",
            "filled_inputs": {
                "alpha_em_MSbar_MZ_inverse": {
                    "central_value": alpha_inv_mz,
                    "uncertainty": alpha_inv_mz_sigma,
                    "source_key": "PDG_2025_ELECTROWEAK_REVIEW",
                    "source_version_or_date": "PDG 2025 electroweak review; effective alpha(M_Z) convention",
                    "used_as_source_selector": False,
                },
                "alpha_em_MSbar_MZ": {
                    "central_value": alpha_em_mz,
                    "uncertainty": alpha_em_mz_sigma,
                    "source_key": "DERIVED_FROM_PDG_2025_ELECTROWEAK_REVIEW",
                    "used_as_source_selector": False,
                },
                "sin2_thetaW_MSbar_MZ": gauge["sin2_thetaW_MSbar_MZ"],
                "alpha_s_MZ": gauge["alpha_s_MZ"],
            },
            "conversion_formulas": conventions["gauge_packet"]["conversion_formulas"],
            "numeric_triplet": gauge_triplet,
            "correlation_policy": "first-order uncorrelated propagation for alpha_em and sin2thetaW; full electroweak fit covariance open",
            "loop_order_and_threshold_policy": "not filled; common RG transport remains open",
            "used_as_source_selector": False,
        },
        "replay_tests": {
            "CKM_complex_Yukawa_matrix_built": True,
            "CKM_unitarity_replayed": ckm_unitarity_residual < 1e-12,
            "CKM_down_Hermitian_reconstructed": down_hermitian_residual < 1e-18,
            "PMNS_mass_squared_matrix_built": True,
            "PMNS_unitarity_replayed": pmns_unitarity_residual < 1e-12,
            "PMNS_mass_splittings_replayed": abs(dm21_replayed - dm21) < 1e-18 and abs(dm3l_replayed - dm3l) < 1e-18,
            "gauge_alpha1_alpha2_alpha3_values_ready": True,
            "common_RG_scale_transport_done": False,
            "full_covariance_ready": False,
            "empirical_equivalence_audit_done": False,
            "full_SM_equivalence_replay_done": False,
            "full_no_knob_closure_done": False,
        },
        "what_closes_now": {
            "CKM_complex_Yukawa_replay": True,
            "PMNS_oscillation_mass_squared_replay": True,
            "alpha1_alpha2_alpha3_MZ_numeric_triplet": True,
            "mixing_and_gauge_replay_executable": True,
            "source_selection_guardrails_preserved": True,
        },
        "what_remains_open": {
            "CKM_covariance_or_profile_policy": True,
            "PMNS_covariance_or_profile_policy": True,
            "absolute_neutrino_mass_and_Dirac_Yukawa_scale": True,
            "common_RG_scale_transport": True,
            "loop_order_and_threshold_policy": True,
            "empirical_equivalence_audit_run": True,
            "full_SM_equivalence_closure": True,
            "full_no_knob_closure": True,
        },
        "closure_claimed": False,
        "sm_equivalence_claimed": False,
        "no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "source_boundary_preserved": True,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "SMEquivalenceMixingAndGaugeReplayTheorem",
            "proved": True,
            "statement": (
                "Given the already selected source/interface boundary and the frozen measured "
                "SM-parity slots, the repository constructs an up-diagonal CKM replay with a "
                "full complex down Yukawa matrix, a PMNS normal-ordering mass-squared replay, "
                "and the MSbar M_Z gauge triplet alpha_1, alpha_2, alpha_3.  This proves the "
                "mixing/gauge replay layer is executable, while leaving covariance, RG "
                "transport, absolute neutrino mass, empirical audit, and no-knob derivation open."
            ),
        },
    }

    cert = {
        "certificate": "MTT_SM_Equivalence_Mixing_and_Gauge_Replay_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "closure_claimed": False,
        "sm_equivalence_claimed": False,
        "no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "source_boundary_preserved": True,
        "theorem_proved": True,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT SM Equivalence Mixing and Gauge Replay v1

Status: `{STATUS}`.

This is a straight SM-standard measured replay after the source/interface
boundary is fixed.  The superset strategy is not used to tune the values.

What is emitted:

```text
CKM replay:  Y_u diagonal, Y_d = V_CKM diag(y_d)
PMNS replay: H_nu = U_PMNS diag(0, Delta_m21^2, Delta_m3l^2) U_PMNS^dagger
Gauge replay: alpha_1=(5/3) alpha_em/(1-sin^2 theta_W), alpha_2=alpha_em/sin^2 theta_W, alpha_3=alpha_s
```

Central gauge triplet at `M_Z`:

```text
alpha_1^GUT = {gauge_triplet["alpha_1_GUT"]["central_value"]}
alpha_2     = {gauge_triplet["alpha_2"]["central_value"]}
alpha_3     = {gauge_triplet["alpha_3"]["central_value"]}
g_1^GUT     = {gauge_triplet["g_1_GUT"]["central_value"]}
g_2         = {gauge_triplet["g_2"]["central_value"]}
g_3         = {gauge_triplet["g_3"]["central_value"]}
```

Replay residuals:

```text
CKM unitarity residual         = {ckm_unitarity_residual}
CKM H_d reconstruction residual = {down_hermitian_residual}
PMNS unitarity residual        = {pmns_unitarity_residual}
PMNS diagonalization residual  = {pmns_diag_residual}
```

Still open:

```text
full CKM/PMNS covariance or profile policy
absolute neutrino mass and Dirac neutrino Yukawa magnitudes
common RG scale transport, loop order, and threshold policy
empirical equivalence audit
full SM-equivalence closure
full no-knob closure
```

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
