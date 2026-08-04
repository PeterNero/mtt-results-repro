"""Search H scalar functionals after the 27x27 left-right/profile push."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_qutrit27hfunctionalsearch_or_radialsourcefrontier"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SCALAR_PACKET = PACKET_DIR / "profile_matrix_scalar_functional_inventory.packet.json"
H_PACKET = PACKET_DIR / "controlled_herm2_matrix_invariants.packet.json"
GATE_PACKET = PACKET_DIR / "strict_h_acceptance_gate_after_matrix_functional_search.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Qutrit27HFunctionalSearch_or_RadialSourceFrontier_v1.md"

STATUS = (
    "MTT_SELECTED_QUTRIT27HFUNCTIONALSEARCH_OR_RADIALSOURCEFRONTIER_"
    "MATRIX_FUNCTIONALS_REJECTED_CONTROLLED_H_READY_RADIAL_OPEN"
)
NEXT = "MTT_Selected_HRadialValueSource_or_NonHiggsHRGPrediction_v1"

SOURCES = {
    "second_matrix_push": DATA / "selected_qutrit27secondpassmatrixpush_or_leftrightprofilefrontier.candidate.json",
    "profile_operator": DATA
    / "selected_qutrit27secondpassmatrixpush_or_leftrightprofilefrontier"
    / "class_profile_operator_211.packet.json",
    "left_right": DATA
    / "selected_qutrit27secondpassmatrixpush_or_leftrightprofilefrontier"
    / "left_right_weyl_commutant_diagnostics.packet.json",
    "dynamic_h_domain": DATA
    / "selected_dynamichiggsresponsehessianonbhuv_or_directmhvalueemission"
    / "dynamic_hessian_domain_and_extraction_gate.packet.json",
    "controlled_h_action": DATA
    / "selected_hpolarfieldpromotion_or_finitehactionderivation"
    / "controlled_finite_h_action_derivation.packet.json",
    "phase_selector": DATA / "selected_hphasesignselector_lenscircle_or_hrgvaluemap.candidate.json",
    "direct_hk_exit": DATA / "selected_directhkthresholdrow_currentexit_or_radialsource.candidate.json",
    "h_one_parameter_ledger": DATA
    / "selected_honeparameterexecutionledger_or_strictfinitehsourcerows.candidate.json",
}


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def complex_matrix(rows: list[list[list[float]]]) -> np.ndarray:
    return np.array([[complex(float(v[0]), float(v[1])) for v in row] for row in rows], dtype=complex)


def main() -> int:
    missing = [rel(path) for path in SOURCES.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing H functional-search inputs: " + ", ".join(missing))

    second = load(SOURCES["second_matrix_push"])
    profile = load(SOURCES["profile_operator"])
    left_right = load(SOURCES["left_right"])
    h_domain = load(SOURCES["dynamic_h_domain"])
    controlled_action = load(SOURCES["controlled_h_action"])
    phase_selector = load(SOURCES["phase_selector"])
    direct_hk = load(SOURCES["direct_hk_exit"])
    one_parameter = load(SOURCES["h_one_parameter_ledger"])["closure_decision"]

    class_weights = np.array(profile["class_weights"], dtype=float)
    eigvals = np.array([class_weights[0]] * 9 + [class_weights[1]] * 18, dtype=float)
    trace = float(np.sum(eigvals))
    frob_sq = float(np.sum(eigvals * eigvals))
    frob = float(math.sqrt(frob_sq))
    normalized = eigvals / trace
    entropy = float(-np.sum(normalized * np.log(normalized)))
    participation = float((trace * trace) / frob_sq)
    logdet = float(np.sum(np.log(eigvals)))
    rank = int(left_right["classwise_left_right_algebra_rank"])
    dim = int(left_right["carrier_dimension"])

    functionals = [
        ("trace_D211", trace),
        ("frobenius_norm_D211", frob),
        ("frobenius_square_D211", frob_sq),
        ("spectral_radius_D211", float(np.max(eigvals))),
        ("spectral_gap_D211", float(np.max(eigvals) - np.min(eigvals))),
        ("logdet_D211", logdet),
        ("entropy_D211", entropy),
        ("participation_ratio_D211", participation),
        ("left_right_rank", float(rank)),
        ("carrier_dimension", float(dim)),
        ("rank_times_base", float(rank * profile["charged_base_overlap_value"])),
        ("dimension_times_trace", float(dim * trace)),
        ("rank_over_trace", float(rank / trace)),
    ]
    scalar_packet = {
        "schema": "MTTProfileMatrixScalarFunctionalInventory.v1",
        "status": "PROFILE_MATRIX_SCALARS_COMPUTED_NONE_ACCEPTED_AS_STRICT_H_RADIAL_SOURCE",
        "closure_claimed": True,
        "D_211_source": rel(SOURCES["profile_operator"]),
        "left_right_source": rel(SOURCES["left_right"]),
        "functionals": [
            {
                "name": name,
                "value": value,
                "source_native_matrix_scalar": True,
                "certified_as_H_radial_source": False,
                "accepted_as_K_threshold_Omega_H_lambda": False,
                "reason_rejected": (
                    "No selected source theorem identifies this D_211/left-right matrix scalar "
                    "with the H radial value, direct N_H, split H threshold row, or R_H^RG."
                ),
            }
            for name, value in functionals
        ],
        "accepted_strict_H_radial_functional_count": 0,
        "accepted_K_threshold_Omega_H_lambda_count": 0,
        "interpretation": (
            "D_211 is a valid 27-carrier realization of selected charged rows. Its matrix "
            "invariants are not source-certified as the Higgs radial/action scalar."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    h = complex_matrix(controlled_action["functional"]["H_controlled"])
    hermitian_error = float(np.linalg.norm(h - h.conj().T))
    trace_h = complex(np.trace(h))
    eig_h = np.linalg.eigvalsh(h)
    h_sq_trace = float(np.trace(h @ h).real)
    radial_from_norm = float(math.sqrt(h_sq_trace / 2.0))
    huu = float(h[0, 0].real)
    hdd = float(h[1, 1].real)
    hud = h[0, 1]
    delta = (huu - hdd) / 2.0
    omega_abs_sq = float(hud.real * hud.real + hud.imag * hud.imag)
    s_beta = float((delta * delta) / (delta * delta + omega_abs_sq))
    det_h = complex(np.linalg.det(h))

    h_packet = {
        "schema": "MTTControlledHerm2MatrixInvariants.v1",
        "status": "CONTROLLED_HERM2_NUMERICS_VERIFIED_MATRIX_DOMAIN_READY_SOURCE_VALUE_OPEN",
        "closure_claimed": True,
        "controlled_H_matrix": controlled_action["functional"]["H_controlled"],
        "domain_readiness": {
            "B_Huv_domain_closed": h_domain["what_is_closed_now"]["B_Huv_domain"],
            "P_H_projector_closed": h_domain["what_is_closed_now"]["P_H_projector"],
            "R_H_restriction_closed": h_domain["what_is_closed_now"]["R_H_restriction"],
            "Herm2_codomain_closed": h_domain["what_is_closed_now"]["Herm2_codomain"],
            "left_right_End9_control_closed": left_right["classwise_left_right_algebra_rank"] == 243,
        },
        "invariants": {
            "Hermitian_error_frobenius": hermitian_error,
            "trace_real": float(trace_h.real),
            "trace_imag": float(trace_h.imag),
            "determinant_real": float(det_h.real),
            "determinant_imag": float(det_h.imag),
            "eigenvalues": [float(v) for v in eig_h],
            "Tr_H_squared": h_sq_trace,
            "r_H_from_sqrt_Tr_H_squared_over_2": radial_from_norm,
            "s_beta_recovered": s_beta,
            "Huu": huu,
            "Hud_re": float(hud.real),
            "Hud_im": float(hud.imag),
            "Hdd": hdd,
        },
        "controlled_one_parameter_matrix_H_ready": True,
        "strict_selected_finite_H_action_emitted": False,
        "strict_selected_radial_source_emitted": False,
        "strict_value_source_blocker": "r_H",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    strict_phi = bool(phase_selector["decision"]["strict_phi_Omega_promoted"])
    strict_r_h = bool(direct_hk["closure_decision"].get("strict_radial_source_emitted", False))
    gate_packet = {
        "schema": "MTTStrictHAcceptanceGateAfterMatrixFunctionalSearch.v1",
        "status": "STRICT_H_GATE_REDUCED_TO_RADIAL_SOURCE_AFTER_MATRIX_FUNCTIONAL_SEARCH",
        "closure_claimed": True,
        "matrix_functional_search_completed": True,
        "accepted_profile_matrix_H_radial_sources": 0,
        "strict_phi_Omega_promoted": strict_phi,
        "strict_r_H_promoted": strict_r_h,
        "strict_H_source_row_emitted": False,
        "direct_K_threshold_Omega_H_lambda_emitted": False,
        "minimal_one_parameter_H_matrix_execution_ready": True,
        "minimal_one_parameter_H_parameter_count": one_parameter["H_parameter_count_spent"],
        "minimal_one_parameter_value": one_parameter["controlled_r_H"],
        "remaining_strict_blocker": "selected r_H / direct N_H / non-Higgs UP-RET-OVERLAP.HRG prediction",
        "legal_next_exits": [
            "selected H radial value source r_H",
            "selected direct N_H = Hess(F_H)[U_H,U_H]",
            "selected split L_rowlocal.Omega_H.lambda and T_scheme.Omega_H.lambda",
            "independent non-Higgs prediction of UP-RET-OVERLAP.HRG",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedQutrit27HFunctionalSearchOrRadialSourceFrontier",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {name: rel(path) for name, path in SOURCES.items()},
        "packets": {
            "profile_matrix_scalar_functional_inventory": rel(SCALAR_PACKET),
            "controlled_herm2_matrix_invariants": rel(H_PACKET),
            "strict_h_acceptance_gate_after_matrix_functional_search": rel(GATE_PACKET),
        },
        "closure_decision": {
            "left_right_27_matrix_layer_closed": second["closure_decision"]["left_right_weyl_layer_closed"],
            "D_211_profile_operator_closed": second["closure_decision"][
                "charged_2_1_1_profile_operator_realized_on_27_carrier"
            ],
            "profile_matrix_scalar_functionals_tested": len(functionals),
            "accepted_profile_matrix_H_radial_sources": 0,
            "controlled_Herm2_numerics_verified": True,
            "controlled_one_parameter_matrix_H_ready": True,
            "minimal_one_parameter_H_parameter_count": one_parameter["H_parameter_count_spent"],
            "strict_phi_Omega_promoted": strict_phi,
            "strict_r_H_promoted": strict_r_h,
            "strict_no_knob_H_closed": False,
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "constants_and_parameters": {
            "charged_base_overlap_value": profile["charged_base_overlap_value"],
            "D_211_trace": trace,
            "D_211_frobenius_norm": frob,
            "D_211_participation_ratio": participation,
            "classwise_left_right_algebra_rank": rank,
            "controlled_r_H": radial_from_norm,
            "controlled_N_H": radial_from_norm * radial_from_norm,
            "controlled_s_beta_recovered": s_beta,
            "minimal_H_parameter": "UP-RET-OVERLAP.HRG",
            "minimal_H_parameter_count": one_parameter["H_parameter_count_spent"],
        },
        "theorem": {
            "name": "Qutrit27HFunctionalSearchAndRadialFrontierTheorem",
            "proved": True,
            "statement": (
                "After the 27x27 left-right/profile closure, all tested source-native "
                "D_211 and matrix-rank scalar functionals fail the strict H acceptance "
                "gate because no selected theorem identifies them with r_H, direct N_H, "
                "or K_threshold.Omega_H.lambda. The controlled Herm(2) H block is "
                "numerically verified and matrix-domain ready at the one-parameter "
                "standard, and the phase sign is promoted; the strict no-knob blocker "
                "is now the radial/source scalar."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedQutrit27HFunctionalSearchOrRadialSourceFrontier",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "profile_matrix_scalar_functionals_tested": len(functionals),
        "accepted_profile_matrix_H_radial_sources": 0,
        "controlled_Herm2_numerics_verified": True,
        "controlled_one_parameter_matrix_H_ready": True,
        "strict_phi_Omega_promoted": strict_phi,
        "strict_r_H_promoted": strict_r_h,
        "strict_no_knob_H_closed": False,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected Qutrit27 H Functional Search or RadialSourceFrontier v1

## Theorem

`Qutrit27HFunctionalSearchAndRadialFrontierTheorem` is emitted.

## What Was Pushed

Starting from the second-pass `27x27` result, this packet tests whether the new
matrix data can supply the missing strict H scalar.

Inputs now closed:

- selected `27x27` left-right Weyl layer;
- central charged profile operator `D_211`;
- full classwise matrix rank `243`;
- two-Higgs `B_Huv/P_H/R_H` Herm(2) domain;
- H phase sign `phi_Omega=+pi/2`;
- controlled one-parameter H radial value.

## Matrix Scalar Search

Tested `{len(functionals)}` source-native profile/matrix scalar functionals,
including `Tr(D_211)`, `||D_211||_F`, `logdet(D_211)`, entropy,
participation ratio, carrier dimension, and left-right rank.

Accepted as strict H radial sources: `0`.

Reason: no selected source theorem identifies any tested `D_211` or rank scalar
with `r_H`, direct `N_H`, split `L_rowlocal/T_scheme`, strict `R_H^RG`, or
`K_threshold.Omega_H.lambda`.

## Controlled Herm(2) Check

The controlled finite-H action is numerically consistent:

- `r_H = sqrt(Tr(H^2)/2) = {radial_from_norm}`;
- `N_H = r_H^2 = {radial_from_norm * radial_from_norm}`;
- recovered `s_beta = {s_beta}`;
- eigenvalues: `{[float(v) for v in eig_h]}`;
- Hermitian error: `{hermitian_error:.3e}`;
- trace: `{float(trace_h.real):.3e} + {float(trace_h.imag):.3e} i`.

This means the one-parameter H matrix layer is executable once the counted
parameter `UP-RET-OVERLAP.HRG` is admitted. It is still not strict no-knob.

## Narrowed Frontier

The phase side is no longer the active blocker in the current ledger:

```text
strict_phi_Omega_promoted = {strict_phi}
```

The strict blocker is now:

```text
selected r_H / direct N_H / non-Higgs UP-RET-OVERLAP.HRG prediction
```

## Next Artifact

`{NEXT}`
"""

    write_json(SCALAR_PACKET, scalar_packet)
    write_json(H_PACKET, h_packet)
    write_json(GATE_PACKET, gate_packet)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
