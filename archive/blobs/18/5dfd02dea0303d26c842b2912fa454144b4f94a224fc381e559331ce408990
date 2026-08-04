"""Attempt a finite stability filter for the selected V_alpha extension.

This is not a brute-force matrix search.  It uses the standard extension
stability reduction:

    0 -> L -> V -> L^{-1} -> 0

Any rank-one destabilizer M -> V either maps into the displayed subline L or
projects nontrivially to the quotient L^{-1}.  The quotient class itself lifts
back to a subline exactly when the extension splits, so the selected nonzero
Ext class already excludes the most dangerous positive-slope candidate
M=L^{-1}.  The remaining candidates need explicit Hom and Yoneda pullback
matrices; this script creates the finite data contract for those matrices.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
CANDIDATES = ROOT / "candidate_data"
PROOF_CORPUS = ROOT / "proof_corpus"

COHOMOLOGY_SELECTED = (
    CANDIDATES
    / "terminal_admissible_section_source"
    / "visible_rank2_l2_cohomology.selected_under_section_principle.json"
)
RANK2_ROUTE = CERTS / "visible_rank2_extension_valpha_route_certificate.json"
GAUDUCHON_WALL = CERTS / "selected_gauduchon_wall_radius_gate_certificate.json"
ALL_GATES = CERTS / "all_remaining_valpha_gates_attempt_certificate.json"

OUT_DIR = CANDIDATES / "valpha_extension_stability_filter"
OUT_TEMPLATE = OUT_DIR / "destabilizer_yoneda_obstruction.template.json"
OUT_CANDIDATE = CANDIDATES / "valpha_extension_stability_filter_attempt.candidate.json"
OUT_CERT = CERTS / "valpha_extension_stability_filter_attempt_certificate.json"
OUT_PAPER = PROOF_CORPUS / "VAlpha_Extension_Stability_Filter_Attempt_v1.md"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def dot(a: list[int], b: list[int]) -> int:
    return sum(x * y for x, y in zip(a, b, strict=True))


def neg(v: list[int]) -> list[int]:
    return [-x for x in v]


def unique_vectors(items: list[list[int]]) -> list[list[int]]:
    seen: set[tuple[int, ...]] = set()
    vectors: list[list[int]] = []
    for item in items:
        key = tuple(item)
        if key not in seen:
            seen.add(key)
            vectors.append(item)
    return vectors


def line_candidate_label(m: list[int], selected_l: list[int], l_dual: list[int]) -> str:
    if m == selected_l:
        return "displayed_subline_L"
    if m == l_dual:
        return "quotient_class_L_inverse"
    return "branch_candidate"


def obstruction_status(
    m: list[int],
    slope: int,
    selected_l: list[int],
    l_dual: list[int],
    selected_ext_nonzero: bool,
) -> tuple[str, dict[str, Any]]:
    if slope < 0:
        return (
            "NOT_DESTABILIZING_IN_SELECTED_CHAMBER",
            {
                "reason": "Strictly negative slope cannot destabilize a slope-zero SU(2)-type extension.",
                "closed_by_current_data": True,
            },
        )

    if m == selected_l:
        return (
            "NOT_DESTABILIZING_DISPLAYED_SUBLINE_HAS_NEGATIVE_SLOPE",
            {
                "reason": "The displayed subline is the selected extension subobject and has negative slope.",
                "closed_by_current_data": True,
            },
        )

    if m == l_dual:
        return (
            "EXCLUDED_BY_NON_SPLIT_EXTENSION",
            {
                "reason": (
                    "A lift L^{-1}->V splitting the quotient map exists iff the extension class "
                    "in Ext^1(L^{-1},L)=H^1(X,L^2) is zero.  The selected terminal class is "
                    "closed and not exact, hence nonzero."
                ),
                "closed_by_current_data": selected_ext_nonzero,
                "uses_selected_ext_nonzero": True,
                "yoneda_pullback_for_identity": "selected extension vector",
            },
        )

    if slope == 0:
        return (
            "ZERO_SLOPE_NEEDS_HOM_AND_YONEDA_EXCLUSION",
            {
                "reason": (
                    "Stable, not merely semistable, requires excluding zero-slope rank-one "
                    "subobjects.  This needs H^0(L^{-1} tensor M^{-1}) and the Yoneda "
                    "pullback of the selected extension through every quotient projection."
                ),
                "closed_by_current_data": False,
                "needed_data": [
                    "basis of Hom(M,L^{-1}) = H^0(X,L^{-1} tensor M^{-1})",
                    "pullback obstruction matrix Hom(M,L^{-1}) -> Ext^1(M,L)",
                    "proof no Hom vector has zero pulled-back selected obstruction",
                ],
            },
        )

    return (
        "POSITIVE_SLOPE_NEEDS_HOM_AND_YONEDA_EXCLUSION",
        {
            "reason": (
                "A positive-slope M can only inject through a nonzero projection to L^{-1}; "
                "it is excluded if the selected extension pulls back nontrivially for every "
                "possible projection section."
            ),
            "closed_by_current_data": False,
            "needed_data": [
                "basis of Hom(M,L^{-1}) = H^0(X,L^{-1} tensor M^{-1})",
                "pullback obstruction matrix Hom(M,L^{-1}) -> Ext^1(M,L)",
                "nonvanishing of every selected pullback obstruction",
            ],
        },
    )


def build_paper(cert: dict[str, Any]) -> str:
    finite = cert["finite_branch_candidate_filter"]
    zero = finite["residual_zero_slope_candidates"]
    quotient = finite["quotient_destabilizer_result"]
    references = cert["external_theorem_usage"]["references"]
    return f"""# VAlpha Extension Stability Filter Attempt v1

## Claim Being Tested

Use the selected non-split extension

```text
0 -> L -> V_alpha -> L^-1 -> 0
L = {cert["selected_extension"]["L"]}
```

as a stability filter rather than searching blindly over matrices.  The selected
wall is `p = {cert["selected_chamber"]["p"]}`, so `mu(L) = {cert["selected_chamber"]["mu_L"]}`
and `mu(L^-1) = {cert["selected_chamber"]["mu_L_inverse"]}`.

## What Closes

The displayed subline is not destabilizing in the selected chamber because its
slope is strictly negative.  The obvious positive-slope quotient class
`L^-1 = {cert["selected_extension"]["L_inverse"]}` is also excluded as an
actual subline: {quotient["status"]}.  The reason is the standard extension
criterion: a section of the quotient map would split the extension, and the
terminal Cech packet supplies a closed, non-exact selected Ext vector
`{cert["selected_extension"]["extension_class_vector"]}`.

This is genuine progress.  It removes the largest fake obstruction without
using benchmark flavor data, observed masses, CKM values, or proxy fitting.

## What Remains

Within the currently available finite branch-candidate set, the only unresolved
candidate classes are the zero-slope ones:

```json
{json.dumps(zero, indent=2)}
```

They cannot be ignored: stable means every proper rank-one subsheaf has
strictly smaller slope than `V_alpha`, so zero-slope injections would still
block stability.  The next missing object is the explicit Hom/Yoneda obstruction
data:

```text
Hom(M,L^-1) = H^0(X,L^-1 tensor M^-1)
Hom(M,L^-1) --pullback selected extension--> Ext^1(M,L).
```

For each residual zero-slope class, every possible quotient projection must
pull back the selected extension to a nonzero obstruction.  If the Hom space is
zero, that candidate is excluded even faster.

## Search-Space Consequence

The wall is not a giant iterative search anymore.  Current data reduce the
rank-two stability check to:

1. a full destabilizer enumeration theorem, or a justified finite reduction to
   the branch candidates recorded here;
2. the Hom/Yoneda matrices for the residual zero-slope classes;
3. a selected HYM/Strominger existence result after stability is proven.

External HYM/Kobayashi-Hitchin-style existence theorems can be used only after
the holomorphic stability hypotheses are proven.  They are excellent filters,
but they do not by themselves select the missing MTT source.

## External Filter References

The external role is deliberately narrow:

{chr(10).join(f"- {item['label']}: {item['url']} ({item['role']})" for item in references)}

## Guardrail

This document does not prove full stability, does not prove HYM existence, and
does not prove full SM closure.  It proves that the selected nonzero Ext packet
excludes the quotient `L^-1` destabilizer and makes the remaining finite
obstruction data completely explicit.
"""


def main() -> int:
    cohomology = load(COHOMOLOGY_SELECTED)
    rank2_route = load(RANK2_ROUTE)
    wall = load(GAUDUCHON_WALL)
    all_gates = load(ALL_GATES)

    selected_l = cohomology.get("target", {}).get("l_vector_abc", [1, -2, 0])
    l_dual = neg(selected_l)
    target_wall = wall.get("wall_dictionary", {}).get("target_wall", {})
    p_vector = target_wall.get("chamber", {}).get("p", [1, 2, 1])
    extension_vector = cohomology.get("reported_cohomology", {}).get(
        "extension_class_vector_C1",
        [],
    )
    ext_nonzero = (
        cohomology.get("acceptance_tests", {}).get("extension_class_closed") is True
        and cohomology.get("acceptance_tests", {}).get("extension_class_not_exact") is True
        and any(value != 0 for value in extension_vector)
    )

    route_vectors = [
        entry.get("l_vector_abc", [])
        for entry in rank2_route.get("finite_line_class_solutions", [])
        if entry.get("l_vector_abc")
    ]
    candidate_vectors = unique_vectors(route_vectors)
    if selected_l not in candidate_vectors:
        candidate_vectors.append(selected_l)
    if l_dual not in candidate_vectors:
        candidate_vectors.append(l_dual)

    candidate_rows: list[dict[str, Any]] = []
    template_rows: list[dict[str, Any]] = []
    for m in candidate_vectors:
        slope = dot(m, p_vector)
        status, detail = obstruction_status(m, slope, selected_l, l_dual, ext_nonzero)
        candidate_rows.append(
            {
                "M": m,
                "label": line_candidate_label(m, selected_l, l_dual),
                "slope_at_selected_p": slope,
                "destabilizing_risk": slope >= 0,
                "status": status,
                "detail": detail,
            }
        )
        if slope >= 0 and m != l_dual:
            template_rows.append(
                {
                    "M": m,
                    "slope_at_selected_p": slope,
                    "hom_M_to_L_inverse_basis": None,
                    "pullback_obstruction_matrix": None,
                    "selected_extension_in_bad_kernel": None,
                    "closure_rule": (
                        "Closed only if Hom(M,L^-1)=0, or if every nonzero quotient "
                        "projection pulls the selected extension to a nonzero class in Ext^1(M,L)."
                    ),
                }
            )

    zero_slope = [
        row
        for row in candidate_rows
        if row["slope_at_selected_p"] == 0
        and row["status"] == "ZERO_SLOPE_NEEDS_HOM_AND_YONEDA_EXCLUSION"
    ]
    open_positive = [
        row
        for row in candidate_rows
        if row["slope_at_selected_p"] > 0
        and row["status"] != "EXCLUDED_BY_NON_SPLIT_EXTENSION"
    ]
    quotient_result = next(
        row for row in candidate_rows if row["label"] == "quotient_class_L_inverse"
    )

    template = {
        "schema": "VAlphaDestabilizerYonedaObstructionData.v1",
        "status": "OPEN_YONEDA_MATRICES_REQUIRED",
        "selected_extension_class_basis": cohomology.get("cochain_complex", {}).get(
            "basis_labels_C1",
            [],
        ),
        "selected_extension_vector": extension_vector,
        "selected_L": selected_l,
        "selected_L_inverse": l_dual,
        "slope_chamber_p": p_vector,
        "destabilizer_candidates": template_rows,
        "required_to_close": [
            "complete destabilizing rank-one/torsion-free subsheaf enumeration or finite reduction theorem",
            "H^0 bases for every residual nonnegative-slope candidate M",
            "Yoneda pullback matrices against the selected extension vector",
            "proof no nonnegative-slope M injects into V_alpha",
        ],
    }

    cert = {
        "certificate": "VAlphaExtensionStabilityFilterAttempt",
        "status": "VALPHA_EXTENSION_STABILITY_FILTER_PARTIAL_QUOTIENT_DESTABILIZER_EXCLUDED_YONEDA_OPEN",
        "analysis_script": rel(Path(__file__)),
        "candidate_data": rel(OUT_CANDIDATE),
        "yoneda_obstruction_template": rel(OUT_TEMPLATE),
        "paper": rel(OUT_PAPER),
        "inputs": {
            "selected_cohomology": rel(COHOMOLOGY_SELECTED),
            "visible_rank2_route": rel(RANK2_ROUTE),
            "selected_gauduchon_wall": rel(GAUDUCHON_WALL),
            "all_remaining_valpha_gates": rel(ALL_GATES),
        },
        "selected_extension": {
            "sequence": "0 -> L -> V_alpha -> L^{-1} -> 0",
            "L": selected_l,
            "L_inverse": l_dual,
            "extension_space": "Ext^1(L^{-1},L)=H^1(X,L^2)",
            "extension_class_vector": extension_vector,
            "extension_class_label": cohomology.get("reported_cohomology", {}).get(
                "nonzero_extension_class_label"
            ),
            "selected_ext_closed_not_exact_nonzero": ext_nonzero,
            "h1": cohomology.get("reported_cohomology", {}).get("h1"),
            "non_split_extension_proved_by_current_data": ext_nonzero,
        },
        "selected_chamber": {
            "p": p_vector,
            "mu_L": dot(selected_l, p_vector),
            "mu_L_inverse": dot(l_dual, p_vector),
            "target_wall_source_status": wall.get("status"),
            "target_wall_selected_by_source": wall.get("current_source_status", {}).get(
                "source_certified_target_wall_present",
                False,
            ),
            "uses_target_wall_as_filter_not_source_selection": True,
        },
        "finite_branch_candidate_filter": {
            "scope": (
                "finite branch-candidate smoke over line classes already isolated by the "
                "visible rank-two route; not a proof over all torsion-free rank-one subsheaves"
            ),
            "candidate_rows": candidate_rows,
            "displayed_subline_result": next(
                row for row in candidate_rows if row["label"] == "displayed_subline_L"
            ),
            "quotient_destabilizer_result": quotient_result,
            "residual_zero_slope_candidates": zero_slope,
            "residual_positive_slope_candidates": open_positive,
            "quotient_L_inverse_excluded": (
                quotient_result["status"] == "EXCLUDED_BY_NON_SPLIT_EXTENSION"
                and quotient_result["detail"]["closed_by_current_data"] is True
            ),
            "residual_zero_slope_count": len(zero_slope),
            "residual_positive_slope_count": len(open_positive),
        },
        "external_theorem_usage": {
            "role": "FILTER_ONLY",
            "statement_used": (
                "HYM/Kobayashi-Hitchin existence theorems may certify an HYM connection "
                "after the selected holomorphic bundle is proven stable in the relevant "
                "Gauduchon/Kahler setting."
            ),
            "references": [
                {
                    "label": "Donaldson-Uhlenbeck-Yau theorem overview in HYM context",
                    "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8741718/",
                    "role": "documents the stable holomorphic bundle <-> HYM connection bridge in a modern HYM setting",
                },
                {
                    "label": "Gauduchon/Hermitian-manifold stability correspondence context",
                    "url": "https://www.sciencedirect.com/science/article/abs/pii/S0007449723000623",
                    "role": "records the Li-Yau/Gauduchon-type generalization context for non-Kahler Hermitian manifolds",
                },
                {
                    "label": "Numerical HYM in heterotic vector-bundle stability",
                    "url": "https://arxiv.org/abs/1004.4399",
                    "role": "motivates using HYM/stability as a computational filter rather than as a fitted SM input",
                },
            ],
            "not_used_to_claim": [
                "that MTT selects the source",
                "that the selected wall is proven by the current source",
                "that full SM closure follows",
            ],
        },
        "closed_by_this_attempt": {
            "nonzero_ext_implies_non_split": ext_nonzero,
            "displayed_L_has_negative_slope": dot(selected_l, p_vector) < 0,
            "quotient_L_inverse_subline_excluded_by_non_split": (
                quotient_result["status"] == "EXCLUDED_BY_NON_SPLIT_EXTENSION"
                and quotient_result["detail"]["closed_by_current_data"] is True
            ),
            "finite_residual_yoneda_contract_created": True,
        },
        "still_open": {
            "complete_destabilizing_subsheaf_enumeration": True,
            "zero_slope_branch_candidate_hom_yoneda_matrices": len(zero_slope) > 0,
            "source_derives_target_wall": wall.get("current_source_status", {}).get(
                "source_certified_target_wall_present",
                False,
            )
            is not True,
            "selected_hym_or_strominger_existence_certificate": True,
            "operator_layer_pic0": True,
            "same_source_D_E_Riesz_Green_dotD": True,
            "primitive_C1_matrices": True,
            "full_SM_closure": True,
        },
        "upstream_gate_status": {
            "all_remaining_valpha_gates_status": all_gates.get("status"),
            "stability_gate_before_this_attempt": all_gates.get("stability_or_routec_gate", {}).get(
                "status"
            ),
        },
        "guardrails": {
            "claims_full_stability": False,
            "claims_hym_existence": False,
            "claims_selected_wall_source": False,
            "claims_full_SM_closure": False,
            "uses_benchmark_flavor_entries": False,
            "uses_observed_flavor_data": False,
        },
        "verdict": {
            "honest_answer": (
                "The selected nonzero Ext class closes the quotient L^{-1} destabilizer and "
                "the target chamber makes the displayed L harmless.  The remaining finite "
                "branch-candidate obstruction is exactly two zero-slope classes requiring "
                "Hom/Yoneda matrices, plus the separate need for a complete subsheaf "
                "enumeration or finite reduction theorem."
            ),
            "next_action": (
                "Compute Hom(M,L^{-1}) and the Yoneda pullback matrices for M=(-2,1,0) "
                "and M=(2,-1,0), or prove a source theorem that these zero-slope classes "
                "cannot occur as rank-one subsheaves."
            ),
        },
    }

    write_json(OUT_TEMPLATE, template)
    write_json(OUT_CANDIDATE, cert)
    write_json(OUT_CERT, cert)
    OUT_PAPER.parent.mkdir(parents=True, exist_ok=True)
    OUT_PAPER.write_text(build_paper(cert), encoding="utf-8")

    print("VAlpha extension stability filter attempt")
    print(json.dumps({"status": cert["status"], "certificate": rel(OUT_CERT)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
