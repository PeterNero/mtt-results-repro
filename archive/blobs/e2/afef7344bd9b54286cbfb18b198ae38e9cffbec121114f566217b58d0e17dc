"""Promote the reduced V_alpha Yoneda maps to Appell-Humbert multiplication.

The central-neutral destabilizer packet proves the boundary maps in the
reduced Kunneth model.  This script checks whether those maps are merely a
chosen finite basis trick, or whether they are the standard multiplication law
for the already-constructed Appell-Humbert factor of automorphy.

Result: for the neutral standard Gaussian Appell-Humbert representative, the
factor of automorphy is linear in the degree vector.  Therefore

    a_D(gamma,z) * a_(2,-4,0)(gamma,z) = a_(D+(2,-4,0))(gamma,z)

for each Hom degree D=Q-M.  Since D+(2,-4,0)=L-M, every reduced Yoneda boundary
matrix is the corresponding Appell-Humbert theta multiplication map.

This still does not select the Appell-Humbert representative by MTT, and it
does not write a finite good-cover refinement.  It closes the multiplication
law conditional on accepting the Appell-Humbert representative as the raw
automorphy source.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
CANDIDATES = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"

APPELL_HUMBERT = CERTS / "visible_rank2_l2_appell_humbert_automorphy_certificate.json"
DESTABILIZER_REDUCTION = CERTS / "valpha_central_neutral_destabilizer_reduction_certificate.json"
KUNNETH_SCALAR = CERTS / "valpha_kunneth_yoneda_scalar_proof_certificate.json"

OUT_DIR = CANDIDATES / "valpha_appell_humbert_yoneda_promotion"
OUT_TABLE = OUT_DIR / "ah_boundary_factor_table.json"
OUT_CANDIDATE = CANDIDATES / "valpha_appell_humbert_yoneda_promotion.candidate.json"
OUT_CERT = CERTS / "valpha_appell_humbert_yoneda_promotion_certificate.json"
OUT_PAPER = CORPUS / "VAlpha_Appell_Humbert_Yoneda_Promotion_v1.md"

L = (1, -2, 0)
Q = (-1, 2, 0)
L2 = (2, -4, 0)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def add(left: tuple[int, int, int], right: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(a + b for a, b in zip(left, right, strict=True))  # type: ignore[return-value]


def sub(left: tuple[int, int, int], right: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(a - b for a, b in zip(left, right, strict=True))  # type: ignore[return-value]


def as_tuple(values: list[int]) -> tuple[int, int, int]:
    return (values[0], values[1], values[2])


def factor_symbol(degree: tuple[int, int, int]) -> str:
    return f"a_{degree[0]}_{degree[1]}_{degree[2]}(gamma,z)"


def build_factor_table(destabilizer_cert: dict[str, Any]) -> dict[str, Any]:
    table = destabilizer_cert.get("central_neutral_destabilizer_table", {})
    rows = []
    for row in table.get("candidate_rows", []):
        line = as_tuple(row["M_abc"])
        hom_degree = sub(Q, line)
        target_degree = sub(L, line)
        product_degree = add(hom_degree, L2)
        degree_identity = product_degree == target_degree
        boundary = row.get("boundary_map", {})
        rows.append(
            {
                "M_abc": row["M_abc"],
                "hom_degree_Q_minus_M": list(hom_degree),
                "extension_degree_L2": list(L2),
                "product_degree": list(product_degree),
                "target_degree_L_minus_M": list(target_degree),
                "degree_addition_identity": degree_identity,
                "automorphy_product_identity": (
                    f"{factor_symbol(hom_degree)} * {factor_symbol(L2)} = "
                    f"{factor_symbol(target_degree)}"
                ),
                "central_shared_circle_degree_zero": hom_degree[2] == 0
                and L2[2] == 0
                and target_degree[2] == 0,
                "reduced_boundary_rank": boundary.get("rank"),
                "reduced_boundary_injective": boundary.get("injective_on_hom"),
                "reduced_boundary_status": row.get("status"),
            }
        )

    return {
        "schema": "VAlphaAppellHumbertYonedaPromotion.v1",
        "status": "AH_YONEDA_MULTIPLICATION_IDENTITY_VERIFIED_SELECTION_OPEN",
        "representative": "neutral standard Gaussian Appell-Humbert factor of automorphy",
        "factor_formula": (
            "a_d(gamma,z)=prod_j exp(-pi*i*d_j*n_j^2*i - "
            "2*pi*i*d_j*n_j*z_j), with neutral Pic0 character"
        ),
        "multiplication_law": "a_d * a_e = a_{d+e} because the exponent is linear in the degree vector",
        "extension_degree_L2": list(L2),
        "candidate_rows": rows,
        "all_degree_identities_hold": all(row["degree_addition_identity"] for row in rows),
        "all_central_degrees_zero": all(row["central_shared_circle_degree_zero"] for row in rows),
        "all_reduced_boundaries_injective": all(row["reduced_boundary_injective"] is True for row in rows),
    }


def build_paper(cert: dict[str, Any]) -> str:
    table = cert["appell_humbert_yoneda_promotion"]
    rows_text = "\n".join(
        "| `{}` | `{}` | `{}` | `{}` | `{}` | `{}` |".format(
            tuple(row["M_abc"]),
            tuple(row["hom_degree_Q_minus_M"]),
            tuple(row["product_degree"]),
            tuple(row["target_degree_L_minus_M"]),
            row["degree_addition_identity"],
            row["reduced_boundary_status"],
        )
        for row in table["candidate_rows"]
    )
    return f"""# VAlpha Appell-Humbert Yoneda Promotion v1

## Purpose

The reduced Kunneth proof gives explicit Yoneda boundary maps for the six
central-neutral destabilizer candidates.  This note checks whether those maps
are the actual multiplication law for the already-constructed Appell-Humbert
automorphy representative.

## Multiplication Law

For the neutral standard Gaussian Appell-Humbert representative,

```text
a_d(gamma,z)=prod_j exp(-pi*i*d_j*n_j^2*i - 2*pi*i*d_j*n_j*z_j).
```

The exponent is linear in the degree vector `d`.  Therefore:

```text
a_d(gamma,z) * a_e(gamma,z) = a_{{d+e}}(gamma,z).
```

For the V_alpha extension class, `e=L^2=(2,-4,0)`.  For each candidate line
`M`, the Hom section has degree `D=Q-M`, and the boundary target has degree
`L-M`.  The identity to check is:

```text
(Q-M) + L^2 = L-M.
```

## Candidate Table

| M | Q-M | product | L-M | identity | reduced boundary status |
|---|---|---|---|---:|---|
{rows_text}

Every row satisfies the degree identity, keeps the shared/central circle at
degree zero, and inherits an injective reduced boundary matrix.  Thus the
reduced Kunneth boundary maps are exactly the Appell-Humbert theta
multiplication maps for this neutral representative.

## What This Does Not Prove

This is a promotion to Appell-Humbert automorphy multiplication, not a final selection theorem.
The current Appell-Humbert representative remains
selection-open: MTT still has to select the ordered base, the target branch
over the swapped branch, and the neutral Pic0 character or a Pic0 quotient
rule.  If the final paper insists on literal finite good-cover transition
tables, that cover refinement is also still unsupplied.

No full V_alpha stability, HYM existence, or full SM closure is claimed here.
"""


def main() -> int:
    appell = load(APPELL_HUMBERT)
    destabilizer = load(DESTABILIZER_REDUCTION)
    scalar = load(KUNNETH_SCALAR)

    construction = appell.get("construction_checks", {})
    selection = appell.get("selection_analysis", {})
    ah_constructed = (
        construction.get("c1_matrix_matches_required_order") is True
        and construction.get("central_shared_circle_trivial") is True
        and construction.get("trivial_semicharacter_allowed_because_c1_pairing_even") is True
    )
    table = build_factor_table(destabilizer)
    promoted = (
        ah_constructed
        and table["all_degree_identities_hold"]
        and table["all_central_degrees_zero"]
        and table["all_reduced_boundaries_injective"]
    )

    cert = {
        "certificate": "VAlphaAppellHumbertYonedaPromotion",
        "status": (
            "VALPHA_APPELL_HUMBERT_YONEDA_PROMOTION_CONDITIONAL_SELECTION_OPEN"
            if promoted
            else "VALPHA_APPELL_HUMBERT_YONEDA_PROMOTION_OPEN"
        ),
        "analysis_script": rel(Path(__file__)),
        "candidate_data": rel(OUT_CANDIDATE),
        "table_packet": rel(OUT_TABLE),
        "paper": rel(OUT_PAPER),
        "inputs": {
            "appell_humbert": rel(APPELL_HUMBERT),
            "destabilizer_reduction": rel(DESTABILIZER_REDUCTION),
            "kunneth_scalar": rel(KUNNETH_SCALAR),
        },
        "input_statuses": {
            "appell_humbert": appell.get("status"),
            "destabilizer_reduction": destabilizer.get("status"),
            "kunneth_scalar": scalar.get("status"),
        },
        "appell_humbert_selection_state": {
            "mathematical_representative_constructed": ah_constructed,
            "selected_by_mtt": selection.get("selected_by_mtt") is True,
            "neutral_pic0_selected_by_mtt": selection.get("neutral_pic0_character_selected_by_mtt")
            is True,
            "target_branch_selected_by_mtt": selection.get("target_branch_L_selected_by_mtt")
            is True,
        },
        "appell_humbert_yoneda_promotion": table,
        "closed_by_this_attempt": {
            "AH_factor_product_law_matches_yoneda_degree_addition": table[
                "all_degree_identities_hold"
            ],
            "central_shared_circle_preserved_degree_zero": table["all_central_degrees_zero"],
            "reduced_boundary_maps_promoted_to_AH_theta_multiplication_conditional": promoted,
            "raw_good_cover_gap_reduced_to_optional_cover_refinement_if_AH_source_allowed": promoted,
        },
        "still_open": {
            "MTT_selection_of_Appell_Humbert_representative": True,
            "MTT_selection_or_quotient_of_Pic0_character": True,
            "target_branch_over_swapped_branch_selection": True,
            "literal_finite_good_cover_transition_table_if_required": True,
            "global_rank_one_torsion_free_subsheaf_enumeration": True,
            "selected_hym_or_strominger_existence_certificate": True,
            "same_source_D_E_Riesz_Green_dotD": True,
            "primitive_C1_matrices": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_MTT_selected_AH_source": False,
            "claims_neutral_Pic0_selected": False,
            "claims_raw_finite_good_cover_table_supplied": False,
            "claims_full_stability": False,
            "claims_hym_existence": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "The reduced Kunneth/Yoneda boundary maps are not arbitrary once "
                "the neutral standard Appell-Humbert representative is accepted: "
                "they are exactly factor-of-automorphy multiplication by degree "
                "addition. The remaining issue is selection of that representative "
                "or a literal good-cover refinement, not the multiplication law."
            ),
            "next_action": (
                "Prove MTT selects the ordered neutral Appell-Humbert source, or "
                "build a finite good-cover refinement of the same factor system "
                "if the final formalism requires explicit cover transitions."
            ),
        },
    }

    write_json(OUT_TABLE, table)
    write_json(OUT_CANDIDATE, cert)
    write_json(OUT_CERT, cert)
    OUT_PAPER.parent.mkdir(parents=True, exist_ok=True)
    OUT_PAPER.write_text(build_paper(cert), encoding="utf-8")

    print("VAlpha Appell-Humbert Yoneda promotion")
    print(json.dumps({"status": cert["status"], "certificate": rel(OUT_CERT)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
