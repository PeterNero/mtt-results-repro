"""Reduce the remaining zero-slope V_alpha stability obstruction.

The previous stability filter left two zero-slope branch candidates:

    M1 = (-2, 1, 0),  M2 = (2, -1, 0).

For the extension 0 -> L -> V -> Q -> 0 with Q=L^{-1}, any morphism M -> V
is controlled by the long exact sequence

    0 -> Hom(M,L) -> Hom(M,V) -> Hom(M,Q) --delta_e--> Ext^1(M,L).

This script evaluates the Hom dimensions in the same reduced base-pullback
Cech/Kunneth model already used for the selected L^2 packet.  It then records
the exact remaining Yoneda scalar needed to exclude M1.  The result is still
guarded: it is a selected-source stability proof only after the same
line-bundle cohomology functor and the final scalar are selected/proven.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
CANDIDATES = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"

STABILITY_FILTER = CERTS / "valpha_extension_stability_filter_attempt_certificate.json"
SELECTED_COHOMOLOGY = (
    CANDIDATES
    / "terminal_admissible_section_source"
    / "visible_rank2_l2_cohomology.selected_under_section_principle.json"
)
PULLBACK_CECH = CERTS / "visible_rank2_l2_pullback_cech_attempt_certificate.json"
APPELL_HUMBERT = CERTS / "visible_rank2_l2_appell_humbert_automorphy_certificate.json"

OUT_DIR = CANDIDATES / "valpha_zero_slope_yoneda"
OUT_PARTIAL = OUT_DIR / "zero_slope_yoneda_reduction.partial.json"
OUT_SCALAR_TEMPLATE = OUT_DIR / "remaining_yoneda_scalar.template.json"
OUT_CANDIDATE = CANDIDATES / "valpha_zero_slope_yoneda_reduction.candidate.json"
OUT_CERT = CERTS / "valpha_zero_slope_yoneda_reduction_certificate.json"
OUT_PAPER = CORPUS / "VAlpha_Zero_Slope_Yoneda_Reduction_v1.md"

L = [1, -2, 0]
Q = [-1, 2, 0]
P = [1, 2, 1]
ZERO_SLOPE_CANDIDATES = [[-2, 1, 0], [2, -1, 0]]


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def add(a: list[int], b: list[int]) -> list[int]:
    return [x + y for x, y in zip(a, b, strict=True)]


def sub(a: list[int], b: list[int]) -> list[int]:
    return [x - y for x, y in zip(a, b, strict=True)]


def dot(a: list[int], b: list[int]) -> int:
    return sum(x * y for x, y in zip(a, b, strict=True))


def elliptic_hodge_for_degree(degree: int) -> dict[str, int]:
    if degree > 0:
        return {"h0": degree, "h1": 0}
    if degree < 0:
        return {"h0": 0, "h1": -degree}
    return {"h0": 1, "h1": 1}


def base_kunneth_hodge(vector: list[int]) -> dict[str, Any]:
    first = elliptic_hodge_for_degree(vector[0])
    second = elliptic_hodge_for_degree(vector[1])
    base = {
        "h0": first["h0"] * second["h0"],
        "h1": first["h0"] * second["h1"] + first["h1"] * second["h0"],
        "h2": first["h1"] * second["h1"],
    }
    return {
        "line_class": vector,
        "central_degree": vector[2],
        "reduced_model": "base pullback pi^*O_E1xE2(a,b), central degree zero",
        "factor_hodge": {"E1": first, "E2": second},
        "base_hodge": base,
        "total_h0": base["h0"],
        "total_h1_reduced": base["h1"] + base["h0"],
        "vertical_H1_contribution": base["h0"],
        "warning_if_central_degree_nonzero": vector[2] != 0,
    }


def hom_dim(source: list[int], target: list[int]) -> dict[str, Any]:
    line = sub(target, source)
    hodge = base_kunneth_hodge(line)
    return {
        "source": source,
        "target": target,
        "line_class_target_tensor_source_inverse": line,
        "space": f"H^0({line})",
        "dimension": hodge["total_h0"],
        "hodge": hodge,
    }


def ext1_dim(source: list[int], target: list[int]) -> dict[str, Any]:
    line = sub(target, source)
    hodge = base_kunneth_hodge(line)
    return {
        "source": source,
        "target": target,
        "line_class_target_tensor_source_inverse": line,
        "space": f"H^1({line})",
        "dimension_reduced": hodge["total_h1_reduced"],
        "hodge": hodge,
    }


def candidate_row(m: list[int], selected_ext_nonzero: bool) -> dict[str, Any]:
    hom_to_l = hom_dim(m, L)
    hom_to_q = hom_dim(m, Q)
    ext_to_l = ext1_dim(m, L)
    slope = dot(m, P)

    if hom_to_l["dimension"] == 0 and hom_to_q["dimension"] == 0:
        status = "EXCLUDED_BY_HOM_VANISHING_IN_REDUCED_PULLBACK_MODEL"
        closed_in_model = True
        needed = []
    elif m == Q and hom_to_q["dimension"] == 1 and selected_ext_nonzero:
        status = "EXCLUDED_BY_NON_SPLIT_BOUNDARY_IDENTITY"
        closed_in_model = True
        needed = []
    elif hom_to_l["dimension"] == 0 and hom_to_q["dimension"] == 1:
        status = "REDUCED_TO_SINGLE_YONEDA_SCALAR"
        closed_in_model = False
        needed = [
            "compute the connecting homomorphism scalar delta_e on the unique Hom(M,Q) generator",
            "prove delta_e != 0 for the selected extension class",
        ]
    else:
        status = "NEEDS_FULL_HOM_YONEDA_MATRIX"
        closed_in_model = False
        needed = [
            "compute Hom(M,L), Hom(M,Q), and the full connecting matrix delta_e",
            "prove every lift-producing Hom(M,Q) vector is obstructed modulo Hom(M,L)",
        ]

    return {
        "M": m,
        "slope_at_p": slope,
        "hom_M_to_L": hom_to_l,
        "hom_M_to_Q_L_inverse": hom_to_q,
        "ext1_M_to_L": ext_to_l,
        "long_exact_sequence": "0 -> Hom(M,L) -> Hom(M,V_alpha) -> Hom(M,Q) --delta_e--> Ext^1(M,L)",
        "status": status,
        "closed_in_reduced_pullback_model": closed_in_model,
        "needed_to_close": needed,
    }


def build_paper(cert: dict[str, Any]) -> str:
    rows = cert["zero_slope_reduction"]["candidate_rows"]
    remaining = cert["zero_slope_reduction"]["remaining_single_scalar_candidate"]
    return f"""# VAlpha Zero-Slope Yoneda Reduction v1

## Result

The two zero-slope branch candidates from the stability filter are no longer
equally hard.

```json
{json.dumps(rows, indent=2)}
```

In the reduced base-pullback Cech/Kunneth model:

- `M=(2,-1,0)` has `Hom(M,L)=0` and `Hom(M,L^-1)=0`, so it cannot map into
  `V_alpha` at all.
- `M=(-2,1,0)` has `Hom(M,L)=0`, but `Hom(M,L^-1)` is one-dimensional.  Its
  exclusion is exactly one Yoneda boundary scalar.

## Remaining Scalar

The last finite branch-candidate obstruction is:

```json
{json.dumps(remaining, indent=2)}
```

So the next proof object is no longer a broad matrix search.  It is the single
coefficient of the connecting homomorphism

```text
delta_e: H^0(L^-1 tensor M^-1) -> H^1(L tensor M^-1)
```

for `M=(-2,1,0)`, evaluated on the unique Hom generator and the selected Ext
vector `[1,0,0,0,0,0,0,0]`.

## Guardrail

This is a reduced-model Hom/Yoneda calculation.  It does not by itself prove
full stability, because two things remain open:

1. the complete destabilizing rank-one/torsion-free subsheaf enumeration, or a
   theorem reducing it to the finite branch candidates;
2. the final selected Yoneda scalar `delta_e != 0` for `M=(-2,1,0)`.

Summary: this does not by itself prove full stability; it does not prove HYM existence or full SM closure.
"""


def main() -> int:
    stability = load(STABILITY_FILTER)
    selected = load(SELECTED_COHOMOLOGY)
    pullback = load(PULLBACK_CECH)
    appell = load(APPELL_HUMBERT)

    extension_vector = selected.get("reported_cohomology", {}).get(
        "extension_class_vector_C1",
        [],
    )
    selected_ext_nonzero = (
        selected.get("acceptance_tests", {}).get("extension_class_closed") is True
        and selected.get("acceptance_tests", {}).get("extension_class_not_exact") is True
        and any(value != 0 for value in extension_vector)
    )

    rows = [candidate_row(m, selected_ext_nonzero) for m in ZERO_SLOPE_CANDIDATES]
    model_closed = [row for row in rows if row["closed_in_reduced_pullback_model"]]
    scalar_rows = [row for row in rows if row["status"] == "REDUCED_TO_SINGLE_YONEDA_SCALAR"]

    remaining_scalar = {
        "schema": "VAlphaRemainingYonedaScalar.v1",
        "status": "OPEN",
        "M": scalar_rows[0]["M"] if scalar_rows else None,
        "hom_generator_space": "H^0(L^-1 tensor M^-1)=H^0(1,1,0)",
        "hom_dimension": scalar_rows[0]["hom_M_to_Q_L_inverse"]["dimension"] if scalar_rows else None,
        "target_ext_space": "Ext^1(M,L)=H^1(L tensor M^-1)=H^1(3,-3,0)",
        "target_ext_dimension_reduced": scalar_rows[0]["ext1_M_to_L"]["dimension_reduced"]
        if scalar_rows
        else None,
        "selected_ext_vector_in_H1_L2": extension_vector,
        "required_nonzero_scalar": "delta_e(sigma_11) != 0",
        "current_value": None,
        "why_this_is_last_finite_branch_scalar": (
            "The other zero-slope candidate has Hom(M,L)=Hom(M,L^-1)=0 in the "
            "reduced pullback model; the quotient L^-1 was already excluded by "
            "the non-split selected Ext class."
        ),
    }

    partial = {
        "schema": "VAlphaZeroSlopeYonedaReduction.v1",
        "status": "ONE_ZERO_SLOPE_CANDIDATE_MODEL_EXCLUDED_ONE_YONEDA_SCALAR_OPEN",
        "candidate_rows": rows,
        "remaining_single_scalar": remaining_scalar,
    }

    cert = {
        "certificate": "VAlphaZeroSlopeYonedaReduction",
        "status": "VALPHA_ZERO_SLOPE_YONEDA_REDUCED_TO_ONE_SCALAR_OPEN",
        "analysis_script": rel(Path(__file__)),
        "candidate_data": rel(OUT_CANDIDATE),
        "partial_reduction_packet": rel(OUT_PARTIAL),
        "remaining_scalar_template": rel(OUT_SCALAR_TEMPLATE),
        "paper": rel(OUT_PAPER),
        "inputs": {
            "stability_filter": rel(STABILITY_FILTER),
            "selected_cohomology": rel(SELECTED_COHOMOLOGY),
            "pullback_cech": rel(PULLBACK_CECH),
            "appell_humbert": rel(APPELL_HUMBERT),
        },
        "input_statuses": {
            "stability_filter": stability.get("status"),
            "selected_cohomology": selected.get("status"),
            "pullback_cech": pullback.get("status"),
            "appell_humbert": appell.get("status"),
        },
        "method": {
            "exact_sequence": "0 -> Hom(M,L) -> Hom(M,V_alpha) -> Hom(M,Q) --delta_e--> Ext^1(M,L)",
            "Q": Q,
            "L": L,
            "slope_chamber_p": P,
            "cohomology_model": "reduced base-pullback Cech/Kunneth line-bundle cohomology",
            "warning": (
                "This computes the finite branch candidates in the current reduced model. "
                "A full stability theorem still needs a complete subsheaf enumeration or a "
                "source theorem reducing all destabilizers to these candidates."
            ),
        },
        "zero_slope_reduction": {
            "candidate_rows": rows,
            "closed_in_reduced_model_count": len(model_closed),
            "remaining_single_scalar_count": len(scalar_rows),
            "remaining_single_scalar_candidate": remaining_scalar,
            "finite_branch_zero_slope_candidates_all_accounted_for": sorted(
                row["M"] for row in rows
            )
            == sorted(ZERO_SLOPE_CANDIDATES),
        },
        "closed_by_this_attempt": {
            "M_2_minus1_0_has_no_morphism_to_V_in_reduced_model": any(
                row["M"] == [2, -1, 0]
                and row["status"] == "EXCLUDED_BY_HOM_VANISHING_IN_REDUCED_PULLBACK_MODEL"
                for row in rows
            ),
            "M_minus2_1_0_reduced_to_single_yoneda_scalar": any(
                row["M"] == [-2, 1, 0]
                and row["status"] == "REDUCED_TO_SINGLE_YONEDA_SCALAR"
                for row in rows
            ),
            "matrix_search_reduced_to_one_scalar_for_finite_branch_candidates": len(scalar_rows)
            == 1,
        },
        "still_open": {
            "compute_remaining_yoneda_scalar": True,
            "prove_remaining_yoneda_scalar_nonzero": True,
            "complete_destabilizing_subsheaf_enumeration": True,
            "promote_reduced_model_to_selected_full_Hom_functor": True,
            "selected_hym_or_strominger_existence_certificate": True,
            "operator_layer_pic0": True,
            "same_source_D_E_Riesz_Green_dotD": True,
            "primitive_C1_matrices": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_full_stability": False,
            "claims_hym_existence": False,
            "claims_full_subsheaf_enumeration": False,
            "claims_remaining_scalar_nonzero": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "Within the current reduced base-pullback Cech/Kunneth model, one of the two "
                "remaining zero-slope candidates is excluded by Hom vanishing.  The other is "
                "not a broad matrix problem: it is exactly one Yoneda boundary scalar."
            ),
            "next_action": (
                "Compute the multiplication/Yoneda scalar for M=(-2,1,0): "
                "H^0(1,1,0) acting on the selected H^1(2,-4,0) class into H^1(3,-3,0), "
                "then prove it is nonzero in the selected source."
            ),
        },
    }

    write_json(OUT_PARTIAL, partial)
    write_json(OUT_SCALAR_TEMPLATE, remaining_scalar)
    write_json(OUT_CANDIDATE, cert)
    write_json(OUT_CERT, cert)
    OUT_PAPER.parent.mkdir(parents=True, exist_ok=True)
    OUT_PAPER.write_text(build_paper(cert), encoding="utf-8")

    print("VAlpha zero-slope Yoneda reduction")
    print(json.dumps({"status": cert["status"], "certificate": rel(OUT_CERT)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
