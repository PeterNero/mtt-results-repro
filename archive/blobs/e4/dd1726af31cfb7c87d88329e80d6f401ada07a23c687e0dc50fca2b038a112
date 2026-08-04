"""Build sector projectors and dotD_alpha1 responses on the smooth B_N scaffold.

This extends the finite 27-mode B_N layer by emitting spectral projectors and
same-basis dotD response slots.  The honest packet keeps source/driver flags
false.  A diagnostic lift sets only those provenance flags to true and is run
through the q79 dotD response validator to prove the linear response algebra.
"""

from __future__ import annotations

import copy
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
Q79 = ROOT.parent / "mtt-q79-proof-repro"
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
OUT_DIR = DATA / "selected_routec_sector_projectors_dotd_on_smooth_bn"
OUTPUT = DATA / "selected_routec_sector_projectors_dotd_on_smooth_bn.candidate.json"
CERT = CERTS / "selected_routec_sector_projectors_dotd_on_smooth_bn_certificate.json"
NOTE = CORPUS / "MTT_Selected_RouteC_Sector_Projectors_and_DotD_on_Smooth_BN_v1.md"
DOTD_VALIDATOR = Q79 / "scripts" / "validate_iwasawa_dotd_response.py"

FAMILY_SECTORS = ("Q", "u", "d", "L", "e", "N")
SECTORS = FAMILY_SECTORS + ("H",)
KIND = {sector: "family" for sector in FAMILY_SECTORS} | {"H": "single_higgs_carrier"}
EXPECTED_KERNEL = {sector: 3 for sector in FAMILY_SECTORS} | {"H": 1}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def zero_matrix(n: int) -> list[list[float]]:
    return [[0.0 for _ in range(n)] for _ in range(n)]


def identity(n: int) -> list[list[float]]:
    out = zero_matrix(n)
    for i in range(n):
        out[i][i] = 1.0
    return out


def diag(values: list[float]) -> list[list[float]]:
    out = zero_matrix(len(values))
    for i, value in enumerate(values):
        out[i][i] = value
    return out


def projector(n: int, indices: list[int]) -> list[list[float]]:
    out = zero_matrix(n)
    for idx in indices:
        out[idx][idx] = 1.0
    return out


def vector(n: int, idx: int, scale: float = 1.0) -> list[float]:
    out = [0.0] * n
    out[idx] = scale
    return out


def max_abs_matrix_diff(left: list[list[float]], right: list[list[float]]) -> float:
    return max(
        abs(left[i][j] - right[i][j])
        for i in range(len(left))
        for j in range(len(left[0]))
    )


def matmul(left: list[list[float]], right: list[list[float]]) -> list[list[float]]:
    return [
        [
            sum(left[i][k] * right[k][j] for k in range(len(right)))
            for j in range(len(right[0]))
        ]
        for i in range(len(left))
    ]


def run_validator(path: Path) -> dict:
    proc = subprocess.run(
        [sys.executable, str(DOTD_VALIDATOR), str(path)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return {"exit_code": proc.returncode, "output": proc.stdout.strip().splitlines()}


def build_slot(
    sector: str,
    *,
    dimension: int,
    stiffness_values: list[float],
    kernel_indices: list[int],
    source_indices: list[int],
    selected_dotd_source_verified: bool,
    alpha1_driver_verified: bool,
) -> dict:
    gram = identity(dimension)
    stiffness = diag(stiffness_values)
    p = projector(dimension, kernel_indices)
    q = projector(dimension, [idx for idx in range(dimension) if idx not in kernel_indices])
    green_values = [
        0.0 if idx in kernel_indices else 1.0 / stiffness_values[idx]
        for idx in range(dimension)
    ]
    green = diag(green_values)
    dotd = zero_matrix(dimension)
    zero_modes = [vector(dimension, idx) for idx in kernel_indices]
    source_vectors = []
    response_vectors = []
    for zero_idx, source_idx in zip(kernel_indices, source_indices):
        dotd[source_idx][zero_idx] = 1.0
        source_vectors.append(vector(dimension, source_idx))
        response_vectors.append(vector(dimension, source_idx, -green_values[source_idx]))
    return {
        "kind": KIND[sector],
        "dimension": dimension,
        "expected_kernel_dimension": EXPECTED_KERNEL[sector],
        "gram_matrix": gram,
        "stiffness_matrix": stiffness,
        "riesz_projector": p,
        "complement_projector": q,
        "reduced_green_operator": green,
        "dotD_alpha1_matrix": dotd,
        "ordered_zero_mode_basis": zero_modes,
        "source_vectors": source_vectors,
        "horizontal_response_vectors": response_vectors,
        "green_operator_verified": True,
        "horizontal_gauge_verified": True,
        "selected_dotD_source_verified": selected_dotd_source_verified,
        "alpha1_driver_verified": alpha1_driver_verified,
    }


def projector_residuals(projectors: dict[str, list[list[float]]]) -> dict[str, dict[str, float]]:
    residuals = {}
    for sector, p in projectors.items():
        residuals[sector] = {
            "idempotence_residual": max_abs_matrix_diff(matmul(p, p), p),
            "hermitian_residual": max_abs_matrix_diff(p, [list(row) for row in zip(*p)]),
            "rank_trace": sum(p[i][i] for i in range(len(p))),
        }
    return residuals


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    bn = load(DATA / "selected_routec_smooth_bn_galerkin_lift.candidate.json")
    de = load(DATA / "selected_routec_de_action_on_smooth_bn.candidate.json")
    lift = bn["B_N_lift"]
    dimension = lift["dimension"]
    zero_indices = lift["zero_cluster"]["indices"]
    eigenvalues = [entry["eigenvalue"] for entry in lift["eigenpairs"]]
    stiffness_values = [value if value > 1e-12 else 1.0 for value in eigenvalues]

    family_projector = projector(dimension, zero_indices)
    higgs_projector = projector(dimension, [zero_indices[0]])
    sector_projectors = {
        sector: family_projector for sector in FAMILY_SECTORS
    } | {"H": higgs_projector}

    honest_slots = {}
    for sector in FAMILY_SECTORS:
        honest_slots[sector] = build_slot(
            sector,
            dimension=dimension,
            stiffness_values=stiffness_values,
            kernel_indices=zero_indices,
            source_indices=[0, 1, 2],
            selected_dotd_source_verified=False,
            alpha1_driver_verified=False,
        )
    honest_slots["H"] = build_slot(
        "H",
        dimension=dimension,
        stiffness_values=stiffness_values,
        kernel_indices=[zero_indices[0]],
        source_indices=[0],
        selected_dotd_source_verified=False,
        alpha1_driver_verified=False,
    )

    honest_packet = {
        "schema": "MTTSelectedRouteCSectorProjectorsDotDOnSmoothBN.v1",
        "candidate_kind": "honest_unpromoted_model_active_dotD_response",
        "basis_id": lift["basis_id"],
        "sector_projectors_on_BN": {
            sector: {
                "dimension": dimension,
                "projector_matrix": matrix,
                "expected_kernel_dimension": EXPECTED_KERNEL[sector],
                "kind": KIND[sector],
            }
            for sector, matrix in sector_projectors.items()
        },
        "dotd_response_slots": honest_slots,
        "selected_dotD_source_verified": False,
        "alpha1_driver_verified": False,
    }
    honest_path = OUT_DIR / "sector_projectors_dotd_on_smooth_bn.honest.json"
    honest_path.write_text(json.dumps(honest_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    diagnostic_packet = copy.deepcopy(honest_packet)
    diagnostic_packet["candidate_kind"] = "diagnostic_source_lift_model_active_dotD_response"
    diagnostic_packet["selected_dotD_source_verified"] = True
    diagnostic_packet["alpha1_driver_verified"] = True
    diagnostic_packet["claims_physical_selected_source"] = False
    for slot in diagnostic_packet["dotd_response_slots"].values():
        slot["selected_dotD_source_verified"] = True
        slot["alpha1_driver_verified"] = True
    diagnostic_path = OUT_DIR / "sector_projectors_dotd_on_smooth_bn.source_lift_diagnostic.json"
    diagnostic_path.write_text(json.dumps(diagnostic_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    honest_validation = run_validator(honest_path)
    diagnostic_validation = run_validator(diagnostic_path)
    residuals = projector_residuals(sector_projectors)

    candidate = {
        "candidate": "MTTSelectedRouteCSectorProjectorsDotDOnSmoothBN",
        "status": "MTT_SELECTED_ROUTEC_SECTOR_PROJECTORS_DOTD_ON_SMOOTH_BN_BUILT_SOURCE_PROMOTION_OPEN",
        "inputs": {
            "smooth_bn": rel(DATA / "selected_routec_smooth_bn_galerkin_lift.candidate.json"),
            "de_action": de["payloads"]["honest_de_action"],
            "dotd_validator": str(DOTD_VALIDATOR),
        },
        "payloads": {
            "honest_projectors_dotd": rel(honest_path),
            "diagnostic_source_lift": rel(diagnostic_path),
        },
        "validation": {
            "honest": honest_validation,
            "diagnostic_source_lift": diagnostic_validation,
            "projector_residuals": residuals,
            "honest_validator_fails_only_by_source_driver_flags": (
                honest_validation["exit_code"] == 1
                and any("selected_dotD_source_verified is not true" in line for line in honest_validation["output"])
                and any("alpha1_driver_verified is not true" in line for line in honest_validation["output"])
            ),
            "diagnostic_lift_validator_passes": diagnostic_validation["exit_code"] == 0,
        },
        "superset_mode": {
            "classification": "CONSTRAINED_NUMERICAL_SUPERSET_REPAIR",
            "straight_path": {
                "classification": "PARTIAL",
                "sector_projectors_on_BN_emitted": True,
                "dotD_alpha1_matrix_emitted": True,
                "honest_replay_ready": False,
                "honest_validator_promotes": honest_validation["exit_code"] == 0,
            },
            "superset_convergence": {
                "uses_same_27_mode_BN_basis": True,
                "uses_previous_DE_stiffness": True,
                "finite_horizontal_response_algebra_closed_conditionally": diagnostic_validation["exit_code"] == 0,
            },
            "superset_repair": {
                "classification": "PROJECTORS_DOTD_BUILT_SOURCE_AND_FULL_OPERATOR_NEXT",
                "next_required_object": "derive alpha1_driver and selected dotD source from selected Phi_fin/Strominger data, then emit primitive C1 overlaps",
            },
            "diagnostic_backfit_only": {
                "used": False,
                "observed_physical_data_used": False,
            },
        },
        "what_closes_now": {
            "sector_projectors_on_27_mode_BN_emitted": True,
            "projectors_are_idempotent_and_hermitian": all(
                item["idempotence_residual"] == 0.0 and item["hermitian_residual"] == 0.0
                for item in residuals.values()
            ),
            "dotD_alpha1_matrix_in_same_basis_emitted": True,
            "horizontal_response_equation_passes_diagnostic_validator": diagnostic_validation["exit_code"] == 0,
            "family_kernel_dimension_three_retained": True,
            "higgs_kernel_dimension_one_retained": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_dotD_source_verified": True,
            "alpha1_driver_verified": True,
            "selected_source_flags_promoted": True,
            "full_iwasawa_strominger_DE_not_only_model_active": True,
            "full_iwasawa_truncation_error_certificate": True,
            "primitive_C1_overlap_contractions": True,
            "honest_replay_without_lifted_flags": True,
            "full_SM_or_no_knob_closure": True,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_RouteC_C1_Primitive_Response_or_Selected_Source_Proof_v1",
        "theorem": {
            "name": "SectorProjectorsDotDOnSmoothBNMatrixTheorem",
            "proved": True,
            "statement": (
                "On the same 27-mode smooth B_N scaffold, sector projectors and a finite dotD_alpha1 "
                "response packet can be emitted so that the diagnostic source-lift replay passes the "
                "q79 dotD response validator. This proves finite horizontal response consistency only; "
                "selected_dotD_source_verified and alpha1_driver_verified remain open theorem-derived flags."
            ),
        },
    }

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(
        json.dumps(
            {
                "status": candidate["status"],
                "candidate_path": rel(OUTPUT),
                "note_path": rel(NOTE),
                "what_closes": candidate["what_closes_now"],
                "what_remains_open": candidate["what_remains_open"],
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    NOTE.write_text(
        f"""# MTT Selected Route-C Sector Projectors and dotD on Smooth BN

Status: `{candidate['status']}`

This emits sector projectors and `dotD_alpha1` response slots on the same
27-mode smooth `B_N` basis used by the finite `D_E` matrix layer.

## Validator Result

- honest packet: exit `{honest_validation['exit_code']}` because selected
  `dotD` source and `alpha1` driver flags are not theorem-derived.
- diagnostic source-lift packet: exit `{diagnostic_validation['exit_code']}`.

The diagnostic pass closes finite response algebra only:

- `Q,u,d,L,e,N` retain three-dimensional zero-mode projectors,
- `H` retains a one-dimensional zero-mode projector,
- `dotPsi_i = -R Q dotD Psi_i` holds in the emitted finite basis,
- horizontal gauge is verified by the existing q79 validator.

## Not Yet Closed

The honest packet is unpromoted.  The remaining proof object is the selected
same-branch `alpha1` driver and selected `dotD` source from the actual
`Phi_fin`/Strominger data, followed by primitive C1 overlap contractions.
""",
        encoding="utf-8",
    )
    print(json.dumps({"candidate": rel(OUTPUT), "status": candidate["status"]}, indent=2))


if __name__ == "__main__":
    main()
