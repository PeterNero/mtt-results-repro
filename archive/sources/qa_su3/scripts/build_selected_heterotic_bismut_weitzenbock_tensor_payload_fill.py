"""Fill the source-backed part of the Bismut-Weitzenbock tensor payload."""

from __future__ import annotations

import itertools
import json
from collections import defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "contract": DATA / "selected_heterotic_bismut_weitzenbock_formula_or_ouweight_derivation.candidate.json",
    "template": DATA / "selected_heterotic_bismut_weitzenbock_tensor_payload.template.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_bismut_weitzenbock_tensor_payload_fill.candidate.json"
OUTPUT_CERT = CERTS / "selected_heterotic_bismut_weitzenbock_tensor_payload_fill_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_BismutWeitzenbock_TensorPayload_Fill_v1.md"

STATUS = "HETEROTIC_BISMUT_WEITZENBOCK_TENSOR_PAYLOAD_PARTIAL_GEOMETRY_FILLED_BUNDLE_OPERATOR_OPEN"
NEXT = "Selected_Heterotic_BundleCurvature_RepresentationTrace_or_DirectFiniteOperator_Fill_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def key3(i: int, j: int, k: int) -> str:
    return f"{i}{j}{k}"


def key2(i: int, j: int) -> str:
    return f"{i}{j}"


def antisym3(seed: dict[tuple[int, int, int], float]) -> dict[str, float]:
    out: dict[str, float] = {}
    for tup, value in seed.items():
        for perm in itertools.permutations(tup):
            inv = sum(1 for a in range(3) for b in range(a + 1, 3) if perm[a] > perm[b])
            signed = value * ((-1) ** inv)
            if abs(signed) > 1e-14:
                out[key3(*perm)] = signed
    return dict(sorted(out.items()))


def compute_geometry(A: float) -> dict[str, Any]:
    half = A / 2.0
    d_coeffs = {
        "de1": {},
        "de2": {},
        "de3": {},
        "de4": {},
        "de5": {"13": A, "24": -A},
        "de6": {"14": A, "23": A},
    }
    # de^k(E_i,E_j)=-e^k([E_i,E_j]); c^k_ij are vector bracket constants.
    D: dict[tuple[int, int, int], float] = defaultdict(float)
    for (k, i, j), value in {
        (5, 1, 3): A,
        (5, 2, 4): -A,
        (6, 1, 4): A,
        (6, 2, 3): A,
    }.items():
        D[(k, i, j)] = value
        D[(k, j, i)] = -value

    def c(i: int, j: int, k: int) -> float:
        return -D[(k, i, j)]

    structure_constants: dict[str, float] = {}
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                value = c(i, j, k)
                if abs(value) > 1e-14:
                    structure_constants[f"c^{k}_{i}{j}"] = value

    def gamma_lc(i: int, j: int, k: int) -> float:
        return 0.5 * (c(i, j, k) - c(j, k, i) + c(k, i, j))

    h_seed = {
        (1, 3, 6): A,
        (1, 4, 5): -A,
        (2, 3, 5): -A,
        (2, 4, 6): -A,
    }
    H = antisym3(h_seed)

    def h(i: int, j: int, k: int) -> float:
        return H.get(key3(i, j, k), 0.0)

    lc: dict[str, float] = {}
    plus: dict[str, float] = {}
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                g_lc = gamma_lc(i, j, k)
                g_plus = g_lc + 0.5 * h(i, j, k)
                if abs(g_lc) > 1e-14:
                    lc[f"GammaLC_{i}{j}{k}"] = g_lc
                if abs(g_plus) > 1e-14:
                    plus[f"GammaPlus_{i}{j}{k}"] = g_plus

    return {
        "orthonormal_coframe": ["e1", "e2", "e3", "e4", "e5", "e6"],
        "complex_coframe": {
            "omega1": "(e1+i e2)/r1",
            "omega2": "(e3+i e4)/r2",
            "omega3": "(e5+i e6)/r3",
        },
        "structure_equations": d_coeffs,
        "structure_constants_c_ij_k": structure_constants,
        "complex_structure_J_action": {
            "J e1": "e2",
            "J e2": "-e1",
            "J e3": "e4",
            "J e4": "-e3",
            "J e5": "e6",
            "J e6": "-e5",
        },
        "Hermitian_form_omega": {"12": 1.0, "34": 1.0, "56": 1.0},
        "dJ_components": h_seed,
        "torsion_H_or_d_c_omega_components": H,
        "Levi_Civita_connection_coefficients": dict(sorted(lc.items())),
        "Bismut_connection_coefficients": dict(sorted(plus.items())),
        "half_A": half,
    }


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    contract = load(INPUTS["contract"])
    template = load(INPUTS["template"])
    known = contract["contract"]["known_inputs"]
    A = known["A_r3_over_r1r2"]
    geom = compute_geometry(A)

    filled_payload = {
        "source_identity": {
            "same_branch_selected_HYM_or_Strominger_source": False,
            "fixed_frame_and_gauge": "partial: selected invariant real frame filled; bundle gauge still open",
            "selected_domain": "partial: invariant compact Iwasawa frame; full BRST/gauge quotient operator domain open",
        },
        "geometric_tensors": {
            "orthonormal_coframe": geom["orthonormal_coframe"],
            "structure_constants_c_ij_k": geom["structure_constants_c_ij_k"],
            "complex_structure_J": geom["complex_structure_J_action"],
            "Hermitian_form_omega": geom["Hermitian_form_omega"],
            "torsion_H_or_d_c_omega_components": geom["torsion_H_or_d_c_omega_components"],
            "Bismut_connection_coefficients": geom["Bismut_connection_coefficients"],
            "R_plus_curvature_components": None,
            "supporting_structure_equations": geom["structure_equations"],
            "complex_coframe": geom["complex_coframe"],
        },
        "bundle_tensors": template["bundle_tensors"],
        "operator_contract": template["operator_contract"],
        "ou_derivation_alternative": template["ou_derivation_alternative"],
    }

    required_flags = {
        "orthonormal_coframe": True,
        "structure_constants": True,
        "complex_structure_J": True,
        "Hermitian_form_omega": True,
        "torsion_H": True,
        "Bismut_connection_coefficients": True,
        "R_plus_curvature_components": False,
        "connection_A_components": False,
        "curvature_F_A_components": False,
        "ad_bundle_representation": False,
        "trace_normalization": False,
        "E_Qa_matrix": False,
        "kernel_and_quotient_policy": False,
        "gamma_nk_inverse_table": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticBismutWeitzenbockTensorPayloadFill",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {"contract": contract["status"]},
        "known_inputs": known,
        "filled_payload": filled_payload,
        "computed_summary": {
            "A": A,
            "nonzero_de_count": 4,
            "nonzero_structure_constant_count": len(geom["structure_constants_c_ij_k"]),
            "nonzero_torsion_component_count_antisymmetric": len(geom["torsion_H_or_d_c_omega_components"]),
            "nonzero_bismut_connection_coefficients": len(geom["Bismut_connection_coefficients"]),
            "all_bismut_coefficients_are_half_A_magnitude": all(
                abs(abs(value) - geom["half_A"]) < 1e-14
                for value in geom["Bismut_connection_coefficients"].values()
            ),
        },
        "required_flags": required_flags,
        "missing_fields": [key for key, value in required_flags.items() if value is False],
        "decision": {
            "geometric_tensor_payload_filled": True,
            "bundle_tensor_payload_filled": False,
            "R_plus_curvature_filled": False,
            "E_Qa_computed": False,
            "OU_weights_computed": False,
            "direct_finite_operator_emitted": False,
            "next_required_artifact": NEXT,
            "target_fitting_used": False,
        },
        "theorem": {
            "name": "BismutWeitzenbockTensorPayloadPartialFillTheorem",
            "proved": True,
            "statement": (
                "The selected Iwasawa structure equations and radii determine the invariant "
                "real coframe, structure constants, complex structure, Hermitian form, real "
                "torsion three-form, and Bismut connection coefficients in the stated frame. "
                "This still does not compute E_Qa: R_plus curvature components, selected "
                "bundle connection/curvature, representation action, trace normalization, "
                "and quotient policy remain open."
            ),
        },
        "guardrails": {
            "uses_observed_electroweak_data": False,
            "uses_target_residual_scan": False,
            "promotes_geometry_as_E_Qa": False,
            "promotes_partial_domain": False,
            "inserts_arbitrary_ou_weights": False,
            "selects_mu_by_convenience": False,
            "target_fitting_used": False,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    cert = {
        "certificate": "SelectedHeteroticBismutWeitzenbockTensorPayloadFill",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "geometric_tensor_payload_filled": True,
        "bundle_tensor_payload_filled": False,
        "E_Qa_computed": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
    }
    return candidate, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    return f"""# Selected Heterotic BismutWeitzenbock TensorPayload Fill v1

## Result

```text
status = {candidate["status"]}
geometric_tensor_payload_filled = true
bundle_tensor_payload_filled = false
E_Qa_computed = false
next_required_artifact = {candidate["decision"]["next_required_artifact"]}
```

## Filled Payload

```json
{json.dumps(candidate["filled_payload"], indent=2, sort_keys=True)}
```

## Computed Summary

```json
{json.dumps(candidate["computed_summary"], indent=2, sort_keys=True)}
```

## Missing Fields

```json
{json.dumps(candidate["missing_fields"], indent=2, sort_keys=True)}
```

## Theorem

{candidate["theorem"]["statement"]}

## Certificate

```json
{json.dumps(cert, indent=2, sort_keys=True)}
```
"""


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    candidate, cert, note = build()
    write_json(OUTPUT_DATA, candidate)
    write_json(OUTPUT_CERT, cert)
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    for path in [OUTPUT_DATA, OUTPUT_CERT, OUTPUT_NOTE]:
        print(f"wrote {rel(path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
