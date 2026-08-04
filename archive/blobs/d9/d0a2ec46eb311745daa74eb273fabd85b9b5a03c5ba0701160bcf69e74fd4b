"""Build the alpha1 source-normalization / End0-sector-routing value-fill attempt.

This follows the promotion theorem and tries both legal routes.  The honest
outcome is asymmetric: the naive source-normalization route is blocked by
topological invariance of the Chern row under continuous Ext scaling, while the
sector-routing route is reduced to a concrete missing selected functor/value
packet.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

THEOREM = DATA / "selected_alpha1_tangent_promotion_or_sector_routing_theorem.candidate.json"
PHYSICAL = DATA / "selected_physical_dotd_alpha1_or_end0_sector_routing.candidate.json"
VISIBLE_AH = Path("C:/Users/nero_/Downloads/TEXPAPERS/mtt-q79-proof-repro/candidate_data/visible_rank2_l2_appell_humbert_automorphy.candidate.json")
Q79_SECTOR = Path("C:/Users/nero_/Downloads/TEXPAPERS/mtt-q79-proof-repro/candidate_data/q79_routec_weylpair_sector_charge_or_chirality_certificate.candidate.json")
CONSTANTS_ALPHA1 = Path("C:/Users/nero_/Downloads/TEXPAPERS/mtt-nonsm-constants-no-knob/candidate_data/selected_alpha1_tangent_or_retarded_overlap_kernel_attempt.candidate.json")
BN_DOTD = DATA / "selected_routec_sector_projectors_dotd_on_smooth_bn.candidate.json"
OPERATOR_PACKET = DATA / "selected_routec_selected_operator_source_and_overlap_tensor_packet.candidate.json"
SOURCE_TO_C1 = DATA / "selected_routec_weylpair_source_to_c1_transfer_map.candidate.json"

OUTPUT = DATA / "selected_alpha1_source_normalization_or_end0_sector_routing_value_fill.candidate.json"
CERT = CERTS / "selected_alpha1_source_normalization_or_end0_sector_routing_value_fill_certificate.json"
NOTE = CORPUS / "MTT_Selected_Alpha1_SourceNormalization_or_End0SectorRouting_Value_Fill_v1.md"

STATUS = "MTT_SELECTED_ALPHA1_VALUE_FILL_ATTEMPTED_SOURCE_NORMALIZATION_NOGO_SECTOR_ROUTING_VALUES_OPEN"
NEXT = "MTT_Selected_End0_to_SectorFunctor_Source_and_Value_Packet_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def note_text(candidate: dict[str, Any]) -> str:
    n = candidate["numerical_tangent_reused"]
    return f"""# MTT Selected Alpha1 SourceNormalization or End0 SectorRouting Value Fill v1

Status: `{STATUS}`

## Aim

The previous theorem allowed physical `dotD_alpha1` only through one of two
same-branch routes:

1. source-normalization: identify the discrete `alpha1` Chern/source row with
   the infinitesimal selected Ext-density tangent; or
2. sector routing: emit a selected End0-to-sector functor and normalization.

This artifact tries both routes.

## Reused Closed Tangent

The selected Ext-density tangent remains closed:

```text
L h_ext = q - mean(q),
Lh = Delta h + 2 q h - 2 mean(q h),
residual L2 = {n["residual_l2"]:.3e},
||h_ext||_L2 = {n["h_l2"]:.12g}.
```

Its Frechet replay remains:

```text
dotD_a[h_ext] = (partial_a h_ext) ad(T3).
```

## Route A Result: Source-Normalization No-Go for the Naive Scale Tangent

The visible rank-two Appell-Humbert packet confirms the topological support

```text
c2(V_alpha) = +4 alpha1.
```

However, scaling the already-selected Ext representative changes the metric/HYM
row representative inside the same extension/topological type.  It does not
change the integral Chern class.  Therefore the continuous Ext-density tangent
cannot by itself be the derivative with respect to the discrete `alpha1`
Chern/source row.

So the value

```text
dotD_alpha1 := dotD[h_ext]
```

is not legally filled by source-normalization alone.  A future source theorem
would need an additional MTT rule that interprets `alpha1` as a selected
source-strength coordinate in the fixed class, not merely as the topological
Chern label.

## Route B Result: Sector-Routing Values Still Missing

The End0 side supplies a real selected row response in the `T3` lane, while the
Route-C/B_N side supplies conditional sector matrices and a conditional Weyl
transfer.  But the current selected artifacts do not emit a functor

```text
R_sector : End0(V_alpha) -> {{Q,u,d,L,e,N,H}}
```

nor its normalization.  Existing B_N matrices remain diagnostic or conditional:
their honest validator still fails only because `selected_dotD_source_verified`
and `alpha1_driver_verified` are not theorem-derived.

Thus no sector `dotD_alpha1` values are promoted here.

## What This Closes

- The naive `alpha1 = Ext-density scale` promotion is rejected.
- The selected Ext-density tangent remains a valid support tangent.
- The remaining value-fill problem is reduced to one object: a selected
  End0-to-sector functor/source packet with values and normalization.

## What Remains Open

- selected End0-to-sector functor values,
- selected transfer normalization,
- physical sector `dotD_alpha1` matrices,
- C1 response and SM/no-knob closure.

Next artifact: `{NEXT}`.
"""


def main() -> None:
    theorem = load(THEOREM)
    physical = load(PHYSICAL)
    visible_ah = load(VISIBLE_AH)
    q79_sector = load(Q79_SECTOR)
    constants_alpha1 = load(CONSTANTS_ALPHA1)
    bn_dotd = load(BN_DOTD)
    operator_packet = load(OPERATOR_PACKET)
    source_to_c1 = load(SOURCE_TO_C1)

    tangent = theorem["selected_tangent_numerics"]
    route_a_nogo = {
        "name": "NaiveExtScaleToAlpha1SourceNormalizationNoGo",
        "closed": True,
        "topological_support_present": visible_ah["construction_checks"]["c2_extension_target_is_plus_4_alpha1"] is True,
        "central_shared_circle_retained": visible_ah["construction_checks"]["central_shared_circle_trivial"] is True,
        "reason": (
            "The selected Ext-density scale is a continuous representative/metric-source tangent inside a fixed "
            "rank-two extension class. The alpha1 row supported by c2(V_alpha)=4 alpha1 is discrete integral "
            "Chern/source data. Continuous scaling of the Ext representative does not vary the Chern class."
        ),
        "forbidden_identification": "dotD_alpha1 := dotD[h_ext] by notation or normalization choice alone",
        "what_would_be_needed_to_reopen": (
            "A same-branch MTT source theorem interpreting alpha1 as a selected source-strength coordinate in the "
            "fixed topological class, with a Chern-Weil/retarded-kernel normalization independent of observed data."
        ),
    }

    route_b_reduction = {
        "name": "SelectedEnd0ToSectorRoutingValueReduction",
        "closed": False,
        "End0_row_response_available": theorem["theorem_slot"]["proved_unconditionally_now"]["dotD_frechet_replay_closed"] is True,
        "sector_projector_dotd_matrices_exist_conditionally": bn_dotd["what_closes_now"]["dotD_alpha1_matrix_in_same_basis_emitted"] is True,
        "honest_bn_validator_fails_only_by_source_flags": bn_dotd["validation"]["honest_validator_fails_only_by_source_driver_flags"] is True,
        "conditional_weyl_transfer_exact": source_to_c1["conditional_transfer_map"]["conditional_exact"] is True,
        "selected_sector_routing_closed": operator_packet["selected_overlap_transport"]["selected_sector_routing_emitted"] is True,
        "selected_transfer_normalization_closed": operator_packet["selected_overlap_transport"]["selected_transfer_normalization_emitted"] is True,
        "q79_sector_charge_closed": q79_sector["sector_charge_reduction"]["decision"]["selected_sector_charge_or_chirality_table_proved"] is True,
        "constants_repo_transfer_normalization_closed": constants_alpha1["transfer_checks"]["K5_selected_transfer_normalization"] is True,
        "values_promoted": False,
        "why_not_closed": (
            "The row End0 tangent and conditional B_N/Weyl transfer have compatible shapes, but no selected "
            "R_sector functor or normalization is emitted. The current B_N dotD matrices are rejected as honest "
            "physical values because selected_dotD_source_verified and alpha1_driver_verified remain false."
        ),
        "must_emit_next": [
            "domain basis map from selected End0(V_alpha) T1,T2,T3 to sector carrier basis",
            "sector projectors Q,u,d,L,e,N,H in that selected End0 image",
            "normalization mapping dotD[h_ext] to each sector dotD_alpha1 matrix",
            "proof that Z/X or SU5/E6 routing is selected independently of locked target columns",
            "honest validator replay with selected_dotD_source_verified and alpha1_driver_verified true by theorem",
        ],
    }

    candidate = {
        "candidate": "MTTSelectedAlpha1SourceNormalizationOrEnd0SectorRoutingValueFill",
        "status": STATUS,
        "inputs": {
            "promotion_theorem": rel(THEOREM),
            "physical_dotd_alpha1_or_end0_sector_routing": rel(PHYSICAL),
            "visible_rank2_l2_appell_humbert_automorphy": rel(VISIBLE_AH),
            "q79_sector_charge_or_chirality": rel(Q79_SECTOR),
            "constants_alpha1_tangent_attempt": rel(CONSTANTS_ALPHA1),
            "sector_projectors_dotd_on_smooth_bn": rel(BN_DOTD),
            "selected_operator_source_overlap_packet": rel(OPERATOR_PACKET),
            "source_to_c1_transfer_map": rel(SOURCE_TO_C1),
        },
        "numerical_tangent_reused": {
            "residual_l2": tangent["residual_l2"],
            "h_l2": tangent["h_l2"],
            "h_mean_abs": tangent["h_mean_abs"],
            "dotD_direction_summaries": tangent["dotD_direction_summaries"],
        },
        "route_A_source_normalization": route_a_nogo,
        "route_B_end0_to_sector_routing": route_b_reduction,
        "decision": {
            "source_normalization_route_retired_for_naive_scale_tangent": True,
            "sector_routing_route_remains_primary": True,
            "physical_dotD_alpha1_payload_extracted": False,
            "selected_End0_to_sector_routing_values_extracted": False,
            "closure_claimed": False,
            "target_fitting_used": False,
            "best_next_object": NEXT,
        },
        "superset_strategy": {
            "mode": "DUAL_PATH_VALUE_FILL_ATTEMPT",
            "straight_path": "test whether the selected Ext-density tangent can be normalized directly as alpha1",
            "support_path": "test whether existing Route-C/q79/constant sector packets already emit selected routing values",
            "result": "straight naive scale path no-go; support path reduced to selected End0-to-sector functor values",
            "not_used": "observed masses, mixings, CP phases, thresholds, benchmark matrices, or lifted flags",
        },
        "what_closes_now": {
            "naive_Ext_scale_to_alpha1_source_normalization_rejected": True,
            "selected_Ext_density_tangent_retained_as_support": True,
            "sector_routing_value_fill_requirements_enumerated": True,
            "q79_constants_support_not_promoted": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_End0_to_sector_functor_values": True,
            "selected_transfer_normalization": True,
            "selected_sector_charge_or_chirality_table": True,
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
                "certificate": "MTT_Selected_Alpha1_SourceNormalization_or_End0SectorRouting_Value_Fill_v1",
                "status": STATUS,
                "candidate_path": rel(OUTPUT),
                "note_path": rel(NOTE),
                "naive_Ext_scale_to_alpha1_source_normalization_rejected": True,
                "sector_routing_route_remains_primary": True,
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
    NOTE.write_text(note_text(candidate), encoding="utf-8")

    print(json.dumps({"status": STATUS, "candidate": rel(OUTPUT), "note": rel(NOTE)}, indent=2))


if __name__ == "__main__":
    main()
