"""Fill the Bismut R+ curvature part of the heterotic tensor payload."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUT = DATA / "selected_heterotic_bismut_weitzenbock_tensor_payload_fill.candidate.json"
OUTPUT_DATA = DATA / "selected_heterotic_rplus_curvature_payload_fill.candidate.json"
OUTPUT_CERT = CERTS / "selected_heterotic_rplus_curvature_payload_fill_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_RPlus_Curvature_Payload_Fill_v1.md"

STATUS = "HETEROTIC_RPLUS_CURVATURE_PAYLOAD_FILLED_BUNDLE_OPERATOR_OPEN"
NEXT = "Selected_Heterotic_BundleCurvature_RepresentationTrace_or_DirectFiniteOperator_Fill_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_gamma_key(key: str) -> tuple[int, int, int]:
    suffix = key.split("_", 1)[1]
    return tuple(int(ch) - 1 for ch in suffix)  # type: ignore[return-value]


def parse_c_key(key: str) -> tuple[int, int, int]:
    # format c^5_13
    upper, lower = key.split("_", 1)
    k = int(upper.split("^", 1)[1]) - 1
    i = int(lower[0]) - 1
    j = int(lower[1]) - 1
    return i, j, k


def matmul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    return [[sum(a[i][m] * b[m][j] for m in range(6)) for j in range(6)] for i in range(6)]


def mat_sub(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    return [[a[i][j] - b[i][j] for j in range(6)] for i in range(6)]


def mat_add_scaled(a: list[list[float]], b: list[list[float]], scale: float) -> list[list[float]]:
    return [[a[i][j] + scale * b[i][j] for j in range(6)] for i in range(6)]


def sparse_matrix(mat: list[list[float]], prefix: str, tol: float = 1e-14) -> dict[str, float]:
    out: dict[str, float] = {}
    for row in range(6):
        for col in range(6):
            value = mat[row][col]
            if abs(value) > tol:
                out[f"{prefix}_{row + 1}{col + 1}"] = value
    return out


def compute_rplus(payload: dict[str, Any]) -> dict[str, Any]:
    tensors = payload["filled_payload"]["geometric_tensors"]
    gamma_raw = tensors["Bismut_connection_coefficients"]
    c_raw = tensors["structure_constants_c_ij_k"]

    gamma = [[[0.0 for _ in range(6)] for _ in range(6)] for _ in range(6)]
    for key, value in gamma_raw.items():
        i, j, k = parse_gamma_key(key)
        gamma[i][k][j] = float(value)

    c = [[[0.0 for _ in range(6)] for _ in range(6)] for _ in range(6)]
    for key, value in c_raw.items():
        i, j, k = parse_c_key(key)
        c[i][j][k] = float(value)

    matrices: dict[str, dict[str, float]] = {}
    components: dict[str, float] = {}
    frob_sq_total = 0.0
    max_abs = 0.0

    for i in range(6):
        for j in range(i + 1, 6):
            comm = mat_sub(matmul(gamma[i], gamma[j]), matmul(gamma[j], gamma[i]))
            rij = comm
            for m in range(6):
                if abs(c[i][j][m]) > 1e-14:
                    rij = mat_add_scaled(rij, gamma[m], -c[i][j][m])
            sparse = sparse_matrix(rij, f"Rplus_{i + 1}{j + 1}")
            if sparse:
                matrices[f"Rplus_{i + 1}{j + 1}"] = sparse
            for key, value in sparse.items():
                components[key] = value
                frob_sq_total += value * value
                max_abs = max(max_abs, abs(value))

    return {
        "formula": "Rplus_ij = [Gamma_i,Gamma_j] - c^m_ij GammaPlus_m",
        "R_plus_curvature_components": dict(sorted(components.items())),
        "R_plus_curvature_matrices": dict(sorted(matrices.items())),
        "R_plus_summary": {
            "nonzero_ij_matrices": len(matrices),
            "nonzero_components": len(components),
            "max_abs_component": max_abs,
            "frobenius_sq_total_over_i_lt_j": frob_sq_total,
        },
    }


def main() -> dict[str, Any]:
    source = load(INPUT)
    rplus = compute_rplus(source)

    filled_payload = source["filled_payload"]
    filled_payload["geometric_tensors"]["R_plus_curvature_components"] = rplus["R_plus_curvature_components"]
    filled_payload["geometric_tensors"]["R_plus_curvature_matrices"] = rplus["R_plus_curvature_matrices"]

    candidate = {
        "candidate": "SelectedHeteroticRPlusCurvaturePayloadFill",
        "status": STATUS,
        "input": rel(INPUT),
        "input_status": source["status"],
        "target_fitting_used": False,
        "closure_claimed": False,
        "decision": {
            "geometric_tensor_payload_filled": True,
            "R_plus_curvature_filled": True,
            "bundle_tensor_payload_filled": False,
            "E_Qa_computed": False,
            "direct_finite_operator_emitted": False,
            "next_required_artifact": NEXT,
            "target_fitting_used": False,
        },
        "known_inputs": source["known_inputs"],
        "rplus_payload": rplus,
        "filled_payload": filled_payload,
        "missing_fields": [
            "connection_A_components",
            "curvature_F_A_components",
            "ad_bundle_representation",
            "trace_normalization",
            "E_Qa_matrix",
            "kernel_and_quotient_policy",
            "gamma_nk_inverse_table",
        ],
        "guardrails": {
            "promotes_R_plus_as_bundle_curvature": False,
            "promotes_geometry_as_E_Qa": False,
            "inserts_arbitrary_connection_A": False,
            "inserts_arbitrary_trace_normalization": False,
            "uses_observed_electroweak_data": False,
            "uses_target_residual_scan": False,
            "target_fitting_used": False,
        },
        "theorem": {
            "name": "SelectedBismutRPlusCurvaturePayloadFillTheorem",
            "proved": True,
            "statement": (
                "The selected invariant Bismut connection determines the full left-invariant "
                "R+ curvature tensor by R^+_ij=[Gamma_i,Gamma_j]-Gamma_[e_i,e_j]. "
                "This fills the geometric curvature block but does not compute the Qa/SU3 "
                "threshold operator because the selected bundle connection, bundle curvature, "
                "representation action, trace normalization, quotient policy, and finite "
                "operator weights remain open."
            ),
        },
    }

    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "R_plus_curvature_filled": True,
        "bundle_tensor_payload_filled": False,
        "E_Qa_computed": False,
        "rplus_summary": rplus["R_plus_summary"],
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic RPlus Curvature Payload Fill v1

## Result

```text
status = {STATUS}
R_plus_curvature_filled = true
bundle_tensor_payload_filled = false
E_Qa_computed = false
next_required_artifact = {NEXT}
```

## Curvature Formula

For the selected invariant frame and Bismut connection,

```text
Rplus_ij = GammaPlus_i GammaPlus_j - GammaPlus_j GammaPlus_i - c^m_ij GammaPlus_m
```

This is the left-invariant curvature identity
`R^+_ij = [nabla^+_i,nabla^+_j] - nabla^+_[e_i,e_j]`.

## Summary

```json
{json.dumps(rplus["R_plus_summary"], indent=2, sort_keys=True)}
```

## Theorem

The selected invariant Bismut connection determines the full left-invariant
`R+` curvature tensor. This fills the geometric curvature block of the
heterotic Bismut/Weitzenbock payload.

It does not compute `E_Qa`. The open objects are still:

```json
{json.dumps(candidate["missing_fields"], indent=2)}
```

No observed electroweak data, target residual, arbitrary bundle connection, or
arbitrary trace normalization is used.
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
