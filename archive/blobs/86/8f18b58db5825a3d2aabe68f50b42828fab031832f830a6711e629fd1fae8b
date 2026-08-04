"""Build the selected alpha1 tangent promotion / sector-routing theorem slot.

The artifact is insertion-ready for the paper corpus, but it is intentionally
conservative: it packages the selected Ext-density tangent as a proved local
HYM response and states the exact additional theorem needed before that
response may be called physical dotD_alpha1.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
DRAFT_DIR = CORPUS / "paper_appendix_drafts" / "selected_source"

PREVIOUS = DATA / "selected_physical_dotd_alpha1_or_end0_sector_routing.candidate.json"
OFFDIAG = DATA / "selected_offdiagonal_ext_control_or_sector_transfer.candidate.json"
END0 = DATA / "selected_end0_de_payload_from_diagonal_hym.candidate.json"
GREEN = DATA / "selected_t1t2_covariant_green_and_transfer_probe.candidate.json"
MANIFEST = DATA / "selected_source_paper_integration_manifest.candidate.json"

OUTPUT = DATA / "selected_alpha1_tangent_promotion_or_sector_routing_theorem.candidate.json"
CERT = CERTS / "selected_alpha1_tangent_promotion_or_sector_routing_theorem_certificate.json"
NOTE = CORPUS / "MTT_Selected_Alpha1_Tangent_Promotion_or_SectorRouting_Normalization_Theorem_v1.md"

STATUS = "MTT_SELECTED_ALPHA1_TANGENT_PROMOTION_THEOREM_SLOT_BUILT_SOURCE_PROOF_OPEN"
NEXT = "MTT_Selected_Alpha1_SourceNormalization_or_End0SectorRouting_Value_Fill_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def theorem_text() -> str:
    return """# MTT Selected Alpha1 Tangent Promotion or Sector-Routing Normalization Theorem v1

Status: `MTT_SELECTED_ALPHA1_TANGENT_PROMOTION_THEOREM_SLOT_BUILT_SOURCE_PROOF_OPEN`

## Context

Let `eta_00^unit` be the selected normalized Ext representative and set

```text
rho = |eta_00^unit|^2.
```

Let `u` be the zero-mean solution of the selected diagonal HYM row equation

```text
Delta u = q - mean(q),      q = rho exp(-2u).
```

The selected determinant-one metric and induced End0 connection are

```text
H = diag(exp(u), exp(-u)),
A_diag = du T3,
D_E = d + ad(du T3).
```

The selected row-model Ext moment-map source is `E12`; its metric adjoint is
proportional to `E21`, hence `[E12,E21]` is Cartan and has zero `T1/T2`
projection.  Therefore the already-computed Ext-density tangent remains in the
protected `T3` lane.

## Theorem Slot

In the selected q79/F,m=1 S3/Green-Schwarz branch, the continuous
Ext-density-scale tangent

```text
L h_ext = q - mean(q),
Lh = Delta h + 2 q h - 2 mean(q h)
```

is a well-defined zero-mean tangent of the selected HYM row equation.  Its
Frechet response is

```text
dotD_a[h_ext] = (partial_a h_ext) ad(T3).
```

This tangent may be promoted to physical `dotD_alpha1` if and only if MTT
supplies one of the following same-branch normalizations:

1. a selected source-normalization theorem identifying the discrete `alpha1`
   Chern/source row with the infinitesimal Ext-density scaling direction in
   the solved HYM row equation; or
2. a selected End0-to-sector routing functor, with normalization, sending the
   End0 response above to the physical sector `dotD_alpha1` matrices.

Without one of these two normalizations, the computed tangent is support data
only.  It does not promote `alpha1`, does not emit sector values, and cannot be
used as a validator-ready physical response.

## Proof

The selected HYM row equation fixes `q=rho exp(-2u)` and imposes the zero-mean
gauge slice.  Linearizing the source-density scaling `rho -> exp(t) rho` at
`t=0`, while preserving the zero-mean slice, gives

```text
L h = q - mean(q),
Lh = Delta h + 2 q h - 2 mean(q h).
```

The existing Galerkin replay solves this equation with zero mean and residual
below `1e-12`, so the tangent is a verified selected local HYM response in the
row model.

Because the induced End0 connection is `D_E=d+ad(du T3)`, differentiating the
connection in a scalar `T3` direction gives

```text
delta D_E = ad(dh T3),
dotD_a[h] = (partial_a h) ad(T3).
```

The row-model off-diagonal control proves that the selected Ext source has no
`T1/T2` leakage: `E12` paired with its metric adjoint produces only the Cartan
direction.  Thus the Ext-density tangent is compatible with the protected
diagonal End0 lane and with the pure-gauge covariant Green theorem already
proved for `T1/T2`.

The remaining issue is not analytic existence.  It is typing and source
normalization.  The physical `alpha1` row is discrete Chern/source data for the
selected branch.  A derivative with respect to it is not defined merely by
choosing a nearby continuous scale parameter unless MTT proves that this scale
is the selected infinitesimal representative of the `alpha1` row.  Equivalently,
MTT may bypass the source-normalization route by proving a selected
End0-to-sector routing functor whose normalization maps the above End0 response
to sector matrices.  These are the only two legal promotion routes recorded by
this theorem.

Therefore the local tangent and its Frechet `dotD` replay are closed, but the
physical `dotD_alpha1` and sector response matrices remain open until one of
the two selected normalizations is supplied.

## Forbidden Shortcuts

- Do not treat the continuous Ext-density scale as a free physical knob.
- Do not identify `h_ext` with `alpha1` by notation alone.
- Do not import q79/constants support artifacts as proof of selected sector
  routing.
- Do not use observed masses, mixings, CP phases, thresholds, or benchmark
  matrices to select the normalization.
- Do not set selected validator flags from diagnostic lifted packets.

## Paper Use

This theorem should be inserted under the `dotD_alpha1` / C1 response sections
of the Theta execution and nonabelian-overlap papers.  It can also be cited by
the Strominger/HYM paper as the analytic row-tangent gate.  The safe conclusion
is: the selected row tangent is rigorous support; physical alpha1 promotion
requires the next source-normalization or sector-routing value fill.

Next artifact: `MTT_Selected_Alpha1_SourceNormalization_or_End0SectorRouting_Value_Fill_v1`.
"""


def draft_text(paper_key: str, paper_path: str) -> str:
    return f"""# I5a. Selected Alpha1 Tangent Promotion or Sector-Routing Normalization

Target paper: `{paper_key}`

Target file: `{paper_path}`

## Theorem

Let `eta_00^unit` be the selected normalized Ext representative, let
`rho=|eta_00^unit|^2`, and let `u` solve the selected diagonal HYM row equation

```text
Delta u = q - mean(q),      q = rho exp(-2u),      mean(u)=0.
```

The Ext-density-scale tangent is the zero-mean solution

```text
L h_ext = q - mean(q),
Lh = Delta h + 2 q h - 2 mean(q h).
```

For the induced determinant-one End0 connection

```text
D_E = d + ad(du T3),
```

the corresponding Frechet response is

```text
dotD_a[h_ext] = (partial_a h_ext) ad(T3).
```

This response may be called physical `dotD_alpha1` only after one of two
same-branch normalizations is proved: either MTT identifies the discrete
`alpha1` Chern/source row with this Ext-density tangent, or MTT supplies a
selected End0-to-sector routing functor with normalization sending this End0
response to the physical sector matrices.

## Proof Sketch

Linearizing the selected HYM row equation under `rho -> exp(t)rho` gives the
operator `L` above in the zero-mean slice.  The selected Galerkin replay solves
this equation with residual below `1e-12`, so the local tangent is closed.  Since
`D_E=d+ad(du T3)`, differentiating in a scalar `T3` direction gives
`dotD_a[h]=(partial_a h)ad(T3)`.  The selected row-model Ext source has zero
`T1/T2` projection, so the tangent stays in the protected Cartan lane.

## Safe Wording Before Promotion

The paper may state that MTT has a selected local HYM Ext-density tangent and a
closed Frechet `dotD` replay in the End0 row model.  It must also state that this
does not promote physical `alpha1`, does not emit sector matrices, and does not
close C1/SM response until selected source-normalization or selected
End0-to-sector routing values are theorem-derived.

No observed masses, mixings, CP phases, thresholds, benchmark entries, or
diagnostic lifted flags are used as source selectors.
"""


def main() -> None:
    previous = load(PREVIOUS)
    offdiag = load(OFFDIAG)
    end0 = load(END0)
    green = load(GREEN)
    manifest = load(MANIFEST)

    path_a = previous["path_A_straight_selected_Ext_density_scale_tangent"]
    boundary = previous["operator_payload_boundary"]

    theorem = {
        "id": "I5a_alpha1_tangent_promotion_or_sector_routing_normalization",
        "name": "SelectedAlpha1TangentPromotionOrSectorRoutingNormalizationTheorem",
        "status": "THEOREM_SLOT_BUILT_SOURCE_PROOF_OPEN",
        "formal_statement": (
            "The selected Ext-density-scale tangent h_ext solves L h_ext=q-mean(q) in the zero-mean "
            "HYM row slice and has Frechet response dotD_a[h_ext]=(partial_a h_ext)ad(T3). "
            "It is physical dotD_alpha1 iff a selected source-normalization theorem identifies "
            "the discrete alpha1 Chern/source row with this tangent, or a selected End0-to-sector "
            "routing functor with normalization maps it to physical sector dotD_alpha1 matrices."
        ),
        "proved_unconditionally_now": {
            "selected_Ext_density_tangent_closed": path_a["closed"] is True,
            "linearized_equation": path_a["equation"],
            "zero_mean_tangent": path_a["h_mean_abs"] < 1e-14,
            "residual_below_1e_12": path_a["residual_l2"] < 1e-12,
            "nontrivial_tangent": path_a["h_l2"] > 0,
            "dotD_frechet_replay_closed": previous["what_closes_now"]["dotD_Frechet_replay_on_selected_tangent"] is True,
            "offdiagonal_T1T2_leakage_controlled": offdiag["what_closes_now"]["offdiagonal_Ext_source_has_zero_T1_T2_projection_in_selected_row_model"] is True,
            "End0_connection_formula_available": end0["adjoint_connection_packet"]["induced_End0_connection"] == "ad(A_diag) = d u * ad(T3)",
            "T1T2_covariant_green_closed": green["path_A_straight_T1T2_covariant_Green"]["closed"] is True,
        },
        "conditional_promotion_routes": {
            "route_A_source_normalization": {
                "hypothesis": (
                    "A selected same-branch source-normalization theorem identifies the discrete alpha1 "
                    "Chern/source row with the infinitesimal Ext-density scaling direction of the solved HYM row."
                ),
                "then": "h_ext and its Frechet replay may be named physical dotD_alpha1 for the selected row.",
                "proved_now": False,
            },
            "route_B_sector_routing_normalization": {
                "hypothesis": (
                    "A selected End0-to-sector routing functor and normalization are emitted in the same branch, "
                    "mapping the End0 response dotD[h_ext] to the physical Q,u,d,L,e,N,H sector matrices."
                ),
                "then": "physical sector dotD_alpha1 matrices may be used without a continuous alpha1 knob.",
                "proved_now": False,
            },
        },
        "no_promotion_lemma": {
            "statement": (
                "If neither route A nor route B is supplied, the selected Ext-density tangent is support-only "
                "and cannot be used as physical dotD_alpha1 or as validator-ready sector response data."
            ),
            "applies_now": True,
            "reason": previous["path_A_straight_selected_Ext_density_scale_tangent"]["why_not_physical_alpha1"],
        },
        "forbidden_shortcuts": [
            "treating the Ext-density scale as a physical free knob",
            "renaming h_ext as alpha1 without source normalization",
            "importing q79/constants support artifacts as selected sector routing proof",
            "using observed masses, mixings, CP phases, thresholds, or benchmark matrices as selectors",
            "promoting diagnostic lifted flags to theorem-derived selected flags",
        ],
    }

    targets = ["theta_execution_flavor", "theta_nonabelian_overlaps", "strominger_system"]
    DRAFT_DIR.mkdir(parents=True, exist_ok=True)
    draft_paths = {}
    for key in targets:
        draft = DRAFT_DIR / f"{key}__i5a_alpha1_tangent_promotion_or_sector_routing.md"
        draft.write_text(draft_text(key, manifest["papers"][key]), encoding="utf-8")
        draft_paths[key] = rel(draft)

    candidate = {
        "candidate": "MTTSelectedAlpha1TangentPromotionOrSectorRoutingNormalizationTheorem",
        "status": STATUS,
        "inputs": {
            "physical_dotd_alpha1_or_end0_sector_routing_attempt": rel(PREVIOUS),
            "offdiagonal_ext_control": rel(OFFDIAG),
            "selected_end0_de_payload": rel(END0),
            "t1t2_covariant_green": rel(GREEN),
            "paper_integration_manifest": rel(MANIFEST),
        },
        "theorem_slot": theorem,
        "selected_tangent_numerics": {
            "residual_l2": path_a["residual_l2"],
            "h_l2": path_a["h_l2"],
            "h_min": path_a["h_min"],
            "h_max": path_a["h_max"],
            "h_mean_abs": path_a["h_mean_abs"],
            "iterations": path_a["iterations"],
            "dotD_direction_summaries": path_a["dotD_direction_summaries"],
        },
        "operator_payload_boundary": {
            "selected_Ext_density_scale_dotD_tangent_extracted": boundary["selected_Ext_density_scale_dotD_tangent_extracted"],
            "physical_dotD_alpha1_payload_extracted": False,
            "selected_End0_to_sector_routing_values_extracted": False,
            "validator_ready": False,
            "why_not_validator_ready": (
                "The theorem slot closes the promotion criterion, not the selected source-normalization "
                "or sector-routing values needed to promote physical alpha1."
            ),
        },
        "paper_update_record": {
            "id": theorem["id"],
            "section_title": "Selected Alpha1 Tangent Promotion or Sector-Routing Normalization",
            "status": "PAPER_THEOREM_SLOT_DRAFTED_SOURCE_PROOF_OPEN",
            "target_papers": targets,
            "target_paths": {key: manifest["papers"][key] for key in targets},
            "draft_paths": draft_paths,
            "safe_wording": (
                "The selected Ext-density tangent is rigorous local HYM support; it does not promote physical "
                "alpha1 until selected source-normalization or End0-to-sector routing is theorem-derived."
            ),
        },
        "superset_strategy": {
            "locked_target": "selected eta_00 row, diagonal HYM/End0 packet, no measured constants",
            "straight_path": "prove the selected local Ext-density tangent and Frechet End0 response",
            "support_path": "allow either source-normalization or sector-routing normalization as the legal promotion path",
            "not_used": "observed constants, benchmark matrices, lifted flags, and inverse-search targets",
        },
        "what_closes_now": {
            "paper_ready_theorem_slot_added": True,
            "conditional_promotion_criterion_formalized": True,
            "selected_Ext_density_tangent_packaged": True,
            "no_promotion_without_source_or_routing_lemma_recorded": True,
            "appendix_drafts_written": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_source_normalization_identifies_alpha1_tangent": True,
            "selected_End0_to_sector_routing_values": True,
            "physical_dotD_alpha1_same_branch_driver": True,
            "sector_dotD_alpha1_matrices": True,
            "C1_response_and_SM_closure": True,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(
        json.dumps(
            {
                "certificate": "MTT_Selected_Alpha1_Tangent_Promotion_or_SectorRouting_Normalization_Theorem_v1",
                "status": STATUS,
                "candidate_path": rel(OUTPUT),
                "note_path": rel(NOTE),
                "draft_paths": draft_paths,
                "selected_Ext_density_tangent_packaged": True,
                "conditional_promotion_criterion_formalized": True,
                "physical_dotD_alpha1_payload_extracted": False,
                "selected_End0_to_sector_routing_values_extracted": False,
                "closure_claimed": False,
                "target_fitting_used": False,
                "next_required_artifact": NEXT,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    NOTE.write_text(theorem_text(), encoding="utf-8")

    print(json.dumps({"status": STATUS, "candidate": rel(OUTPUT), "note": rel(NOTE), "drafts": draft_paths}, indent=2))


if __name__ == "__main__":
    main()
