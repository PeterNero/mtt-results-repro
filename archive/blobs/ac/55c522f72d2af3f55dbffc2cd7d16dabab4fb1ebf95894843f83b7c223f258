"""Build the selected Route-C operator-source identity subpacket reduction."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

ATTACK = DATA / "selected_routec_sourceemission_minimal_subpacket_attack_plan.candidate.json"
VISIBLE = DATA / "selected_visible_chern_weil_operator_source.candidate.json"
PROJECTIVE = DATA / "projective_gerbe_rhoe_source_promotion.candidate.json"
RANK2_OR_ROUTEC = DATA / "selected_nonsplit_rank2_or_routec_same_source_packet.candidate.json"
SYMMETRY = DATA / "same_source_symmetry_breaking_source.candidate.json"

OUTPUT = DATA / "selected_routec_operatorsourceidentity_subpacket.candidate.json"
CERT = CERTS / "selected_routec_operatorsourceidentity_subpacket_certificate.json"
NOTE = CORPUS / "MTT_Selected_RouteC_OperatorSourceIdentity_Subpacket_v1.md"

STATUS = "MTT_SELECTED_ROUTEC_OPERATOR_SOURCE_IDENTITY_SUBPACKET_REDUCED_TO_RANK2_OR_ROUTEC_FILL_VALUES_OPEN"
NEXT = "MTT_Selected_RouteC_Rank2_L2_Cohomology_or_RouteC_Residual_Fill_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    attack = load(ATTACK)
    visible = load(VISIBLE)
    projective = load(PROJECTIVE)
    rank2_or_routec = load(RANK2_OR_ROUTEC)
    symmetry = load(SYMMETRY)

    rank2_lane = rank2_or_routec["rank2_lane"]
    route_c_lane = rank2_or_routec["route_c_lane"]
    visible_open = visible["open_gates"]
    projective_result = projective["promotion_result"]

    candidate = {
        "candidate": "MTTSelectedRouteCOperatorSourceIdentitySubpacket",
        "status": STATUS,
        "inputs": {
            "sourceemission_attack_plan": rel(ATTACK),
            "visible_cw_operator_source": rel(VISIBLE),
            "projective_gerbe_rhoe_source_promotion": rel(PROJECTIVE),
            "rank2_or_routec_same_source_packet": rel(RANK2_OR_ROUTEC),
            "same_source_symmetry_breaking_source": rel(SYMMETRY),
        },
        "subpacket_contract": {
            "required_by": attack["next_required_artifact"],
            "must_emit": attack["strategy"]["dependency_order"][0]["must_emit"],
            "passes_only_if": [
                "selected q79/F,m=1 visible bundle/sheaf or Route-C source identity is supplied",
                "the visible Chern-Weil row is derived from that same source",
                "projective/twisted rho_E is promoted at operator level or replaced by explicit selected rho_E/operator data",
                "HYM/Strominger or Route-C residual has selected_source_verified true",
                "coherent spectral zero-mode projector retention is verified for that source",
                "no measured flavor, mass, mixing, CP, or benchmark matrix is used as a selector",
            ],
        },
        "source_level_support": {
            "selected_s3_gerbe_source_level": visible["closed_support"]["selected_s3_gerbe_source_level"],
            "visible_green_schwarz_curvature_row_closed": visible["closed_support"]["visible_green_schwarz_curvature_row_closed"],
            "source_level_projective_gerbe_rhoE_promoted": projective_result["source_level_projective_gerbe_rhoE_promoted"],
            "operator_level_projective_rhoE_promoted": projective_result["operator_level_projective_rhoE_promoted"],
            "visible_operator_source_closed": visible_open["selected_visible_operator_source_closed"],
        },
        "lane_evaluation": {
            "rank2_non_split_valpha": {
                "priority": 1,
                "classification": rank2_lane["classification"],
                "source_shape": rank2_lane["source_shape"],
                "target": rank2_lane["target"],
                "closed": rank2_lane["closed"],
                "blocked_by": rank2_lane["blocked_by"],
                "first_fill_template": rank2_lane["first_fill_template"],
                "required_next_packet": rank2_lane["required_next_packet"],
                "selected_operator_identity_closed": False,
                "why_next": "This lane has the strongest existing topological and automorphy support; the first honest calculation is the selected L^2 cochain/Ext packet plus stability/source selection.",
            },
            "route_c_finite_hym_strominger": {
                "priority": 2,
                "classification": route_c_lane["classification"],
                "source_shape": route_c_lane["source_shape"],
                "closed": route_c_lane["closed"],
                "blocked_by": route_c_lane["blocked_by"],
                "first_fill_template": route_c_lane["first_fill_template"],
                "template_required_fields": route_c_lane["template_required_fields"],
                "selected_operator_identity_closed": False,
                "why_kept": "This lane can bypass explicit rank-two stability only if it emits honest selected rho_E, metric, D_E, residual, Riesz/Green, and dotD values from the same branch.",
            },
        },
        "symmetry_breaking_dependency": {
            "status": symmetry["status"],
            "next_required_artifact": symmetry["next_required_artifact"],
            "primary_route": symmetry["superset_mode"]["primary_superset_path"],
            "remaining_open": symmetry["what_remains_open"],
        },
        "operator_identity_verdict": {
            "subpacket_closed": False,
            "source_level_not_operator_level": True,
            "rank2_or_routec_fill_required": True,
            "selected_visible_operator_source_closed": False,
            "operator_level_projective_rhoE_still_open": True,
            "target_fitting_used": False,
            "next_required_artifact": NEXT,
        },
        "what_closes_now": {
            "source_level_support_separated_from_operator_identity": True,
            "two_live_operator_source_fill_lanes_identified": True,
            "rank2_lane_preferred_for_first_fill": True,
            "route_c_residual_lane_preserved_as_parallel_repair": True,
            "promotion_guardrail_for_A_selected_preserved": True,
        },
        "what_remains_open": {
            "selected_visible_bundle_or_sheaf_model": True,
            "selected_l2_cochain_or_selected_routec_residual_values": True,
            "Chern_Weil_row_derived_from_selected_source": True,
            "operator_level_projective_or_explicit_rhoE_data": True,
            "HYM_or_Route_C_residual_for_visible_source": True,
            "coherent_spectral_zero_mode_projectors": True,
            "selected_D_E_dotD_Riesz_Green": True,
            "primitive_C1_contractions": True,
            "full_SM_or_no_knob_closure": True,
        },
        "superset_mode": {
            "classification": "CONSTRAINED_SUPERSET_REDUCTION_WITH_LOCKED_TARGET",
            "locked_target": "one q79/F,m=1 same-source operator identity packet accepted by visible-source, residual, projector, D_E/Riesz/Green/dotD, and C1 validators",
            "straight_path": {
                "classification": "SOURCE_LEVEL_SUPPORT_ONLY",
                "succeeds": False,
                "reason": "The selected S3/GS/projective carrier supplies source support, but not the operator-level visible source or same-branch spectral values.",
            },
            "superset_convergence": {
                "classification": "PRIMARY_RANK2_FILL_LANE",
                "succeeds": False,
                "requires": list(rank2_lane["blocked_by"].keys()),
            },
            "superset_repair": {
                "classification": "PARALLEL_ROUTEC_FILL_LANE",
                "succeeds": False,
                "requires": list(route_c_lane["blocked_by"].keys()),
            },
            "diagnostic_backfit_only": {
                "used": False,
                "reason": "The artifact only imports corpus/repo proof objects and does not use observed constants or locked flavor data to select a source.",
            },
        },
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "SelectedRouteCOperatorSourceIdentitySubpacketReduction",
            "proved": True,
            "statement": "The first source-emission subpacket is not closed by current support data. Selected S3/Green-Schwarz/projective-gerbe evidence promotes source-level support, but operator-source identity still requires either a selected non-split rank-two L^2 cochain/Ext/stability fill or an honest Route-C HYM/Strominger residual fill. No measured or benchmark data are used, and A_selected remains unpromoted.",
        },
    }

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(
        json.dumps(
            {
                "status": STATUS,
                "candidate_path": rel(OUTPUT),
                "note_path": rel(NOTE),
                "operator_identity_closed": candidate["operator_identity_verdict"]["subpacket_closed"],
                "what_closes": candidate["what_closes_now"],
                "what_remains_open": candidate["what_remains_open"],
                "next_required_artifact": NEXT,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    NOTE.write_text(
        """# MTT Selected Route-C OperatorSourceIdentity Subpacket

Status: `MTT_SELECTED_ROUTEC_OPERATOR_SOURCE_IDENTITY_SUBPACKET_REDUCED_TO_RANK2_OR_ROUTEC_FILL_VALUES_OPEN`

This is the first source-emission subpacket. It separates the closed
source-level support from the still-open operator-level identity.

## What Closes

- The selected S3/Green-Schwarz/projective-gerbe support is sufficient as
  source-level support.
- The visible operator source is not closed by that support alone.
- The live fill lanes are exactly the non-split rank-two `V_alpha` lane and the
  Route-C finite HYM/Strominger residual lane.
- The rank-two lane is the preferred first calculation because it already has
  Chern data, ordered Appell-Humbert support, and an H1/Ext validator scaffold.
- The Route-C lane is preserved as parallel repair because it can bypass an
  explicit rank-two stability proof only by emitting honest selected residual
  and operator values from the same branch.

## What Remains Open

- Selected visible bundle/sheaf or selected Route-C source identity.
- Selected L2 cochain/Ext/stability packet, or selected Route-C residual values.
- Same-source Chern-Weil row.
- Operator-level projective/twisted rho_E promotion or explicit rho_E/operator
  replacement.
- HYM/Strominger or Route-C residual with `selected_source_verified = true`.
- Coherent spectral zero-mode projectors.
- Selected `D_E`, Riesz/Green, and `dotD` values.
- Primitive C1 contractions.

Thus the conditional Weyl-pair operator is still not `A_selected`.

Next artifact: `MTT_Selected_RouteC_Rank2_L2_Cohomology_or_RouteC_Residual_Fill_v1`.
""",
        encoding="utf-8",
    )
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))


if __name__ == "__main__":
    main()
