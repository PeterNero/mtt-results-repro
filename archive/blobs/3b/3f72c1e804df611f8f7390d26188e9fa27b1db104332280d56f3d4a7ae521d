"""Build the stability/HYM or Route-C residual source proof attempt."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
Q79 = ROOT.parent / "mtt-q79-proof-repro"

PREVIOUS = DATA / "selected_routec_rank2_l2_or_routec_residual_fill.candidate.json"
STABILITY_FILTER = Q79 / "candidate_data" / "valpha_extension_stability_filter_attempt.candidate.json"
ZERO_SLOPE = Q79 / "candidate_data" / "valpha_zero_slope_yoneda_reduction.candidate.json"
KUNNETH = Q79 / "candidate_data" / "valpha_kunneth_yoneda_scalar_proof.candidate.json"
CENTRAL = Q79 / "candidate_data" / "valpha_central_neutral_destabilizer_reduction.candidate.json"
AH = Q79 / "candidate_data" / "valpha_appell_humbert_yoneda_promotion.candidate.json"
BRIDGE = Q79 / "candidate_data" / "q79_valpha_source_origin_finite_emission_bridge.candidate.json"

OUTPUT = DATA / "selected_routec_stability_hym_or_routec_residual_source.candidate.json"
CERT = CERTS / "selected_routec_stability_hym_or_routec_residual_source_certificate.json"
NOTE = CORPUS / "MTT_Selected_RouteC_Stability_HYM_or_RouteC_Residual_Source_v1.md"

STATUS = "MTT_SELECTED_ROUTEC_STABILITY_ATTEMPT_CENTRAL_NEUTRAL_CLOSED_GLOBAL_ENUMERATION_OPEN"
NEXT = "MTT_Selected_RouteC_Global_Destabilizer_Enumeration_or_Selected_Residual_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    previous = load(PREVIOUS)
    stability = load(STABILITY_FILTER)
    zero_slope = load(ZERO_SLOPE)
    kunneth = load(KUNNETH)
    central = load(CENTRAL)
    ah = load(AH)
    bridge = load(BRIDGE)

    central_table = central["central_neutral_destabilizer_table"]
    candidate = {
        "candidate": "MTTSelectedRouteCStabilityHYMOrRouteCResidualSource",
        "status": STATUS,
        "inputs": {
            "rank2_l2_fill_checkpoint": rel(PREVIOUS),
            "q79_stability_filter": rel(STABILITY_FILTER),
            "q79_zero_slope_yoneda_reduction": rel(ZERO_SLOPE),
            "q79_kunneth_yoneda_scalar_proof": rel(KUNNETH),
            "q79_central_neutral_destabilizer_reduction": rel(CENTRAL),
            "q79_appell_humbert_yoneda_promotion": rel(AH),
            "q79_source_origin_finite_emission_bridge": rel(BRIDGE),
        },
        "rank2_stability_attempt": {
            "extension": stability["selected_extension"],
            "selected_chamber": stability["selected_chamber"],
            "closed_by_stability_filter": stability["closed_by_this_attempt"],
            "finite_branch_reduction": {
                "residual_positive_slope_count": stability["finite_branch_candidate_filter"]["residual_positive_slope_count"],
                "residual_zero_slope_count": stability["finite_branch_candidate_filter"]["residual_zero_slope_count"],
                "quotient_L_inverse_excluded": stability["finite_branch_candidate_filter"]["quotient_L_inverse_excluded"],
            },
        },
        "zero_slope_closure": {
            "zero_slope_status": zero_slope["status"],
            "kunneth_status": kunneth["status"],
            "remaining_scalar_nonzero": kunneth["reduced_kunneth_yoneda_scalar"]["target_vector_nonzero"],
            "reduced_kunneth_matrix_rank": kunneth["reduced_kunneth_yoneda_scalar"]["matrix_rank"],
            "closed_by_kunneth_attempt": kunneth["closed_by_this_attempt"],
        },
        "central_neutral_destabilizer_theorem": {
            "status": central["status"],
            "proved_for_lane": True,
            "lane": "central-neutral base-pullback rank-one subsheaves",
            "all_candidate_boundaries_injective": central_table["all_candidate_boundaries_injective"],
            "all_candidates_obstructed": central_table["all_candidates_obstructed"],
            "candidate_count": len(central_table["candidate_rows"]),
            "candidate_list": central_table["inequality_reduction"]["candidate_list"],
            "hom_to_L_destabilizers_empty": central["closed_by_this_attempt"]["central_neutral_hom_to_L_destabilizers_empty"],
            "hom_to_Q_nonnegative_candidates_finite_six": central["closed_by_this_attempt"]["central_neutral_hom_to_Q_nonnegative_candidates_finite_six"],
            "selected_ext_lowest_basis_confirmed": central["closed_by_this_attempt"]["selected_ext_lowest_basis_confirmed"],
            "central_shared_circle_degree_zero": True,
        },
        "appell_humbert_promotion": {
            "status": ah["status"],
            "conditional_on_selected_AH_source": True,
            "all_degree_identities_hold": ah["appell_humbert_yoneda_promotion"]["all_degree_identities_hold"],
            "all_reduced_boundaries_injective": ah["appell_humbert_yoneda_promotion"]["all_reduced_boundaries_injective"],
            "all_central_degrees_zero": ah["appell_humbert_yoneda_promotion"]["all_central_degrees_zero"],
            "still_open": ah["still_open"],
        },
        "route_c_residual_lane": {
            "finite_codomain_schema_closed": bridge["closed_by_this_attempt"]["finite_emission_codomain_schema_closed"],
            "identity_rhoE_smoke_rejected": bridge["closed_by_this_attempt"]["identity_rhoE_smoke_rejected"],
            "shape_gates": bridge["finite_emission_schema"]["shape_gates"],
            "selected_payload_flags": bridge["finite_emission_schema"]["selected_payload_flags"],
            "still_open": {
                "HYM_or_RouteC_selected_values": bridge["still_open"]["HYM_or_RouteC_selected_values"],
                "nonidentity_selected_rhoE_or_connection_values": bridge["still_open"]["nonidentity_selected_rhoE_or_connection_values"],
                "selected_D_E_Riesz_Green_dotD_flags": bridge["still_open"]["selected_D_E_Riesz_Green_dotD_flags"],
                "selected_PhiFin_alpha1_payload": bridge["still_open"]["selected_PhiFin_alpha1_payload"],
            },
        },
        "proof_verdict": {
            "full_stability_proved": False,
            "hym_existence_proved": False,
            "route_c_residual_selected": False,
            "central_neutral_stability_subtheorem_proved": True,
            "why_full_gate_not_closed": [
                "current proof closes central-neutral base-pullback destabilizers only",
                "global rank-one torsion-free subsheaf enumeration is still open",
                "AH/Yoneda promotion is conditional on selected Appell-Humbert source or literal good-cover refinement",
                "selected HYM/Strominger or Route-C residual values are not emitted",
                "operator-layer Pic0 and same-source D_E/Riesz/Green/dotD remain open",
            ],
        },
        "what_closes_now": {
            "central_neutral_base_pullback_destabilizers_obstructed": True,
            "six_nonnegative_slope_hom_to_Q_candidates_exhausted_in_lane": True,
            "all_six_yoneda_boundaries_injective_in_reduced_model": True,
            "remaining_zero_slope_scalar_nonzero_in_reduced_kunneth_model": True,
            "AH_degree_addition_matches_reduced_yoneda_conditionally": True,
            "rank2_stability_problem_reduced_to_global_subsheaf_enumeration_or_selected_residual": True,
        },
        "what_remains_open": {
            "global_rank_one_torsion_free_subsheaf_enumeration": True,
            "prove_all_destabilizers_have_central_neutral_base_pullback_reflexive_hull": True,
            "MTT_selection_of_AH_representative_or_good_cover_refinement": True,
            "selected_HYM_or_Strominger_existence_certificate": True,
            "selected_RouteC_residual_values": True,
            "operator_layer_pic0": True,
            "same_source_D_E_Riesz_Green_dotD": True,
            "primitive_C1_contractions": True,
            "full_SM_or_no_knob_closure": True,
        },
        "superset_mode": {
            "classification": "CONSTRAINED_SUPERSET_STABILITY_PROOF_ATTEMPT",
            "straight_path": {
                "classification": "RANK2_STABILITY_PARTIAL_SUBTHEOREM",
                "succeeds": False,
                "closed": "central-neutral base-pullback destabilizers",
                "open": "global rank-one torsion-free subsheaf enumeration",
            },
            "superset_convergence": {
                "classification": "RANK2_AH_YONEDA_CONVERGENCE",
                "succeeds": False,
                "closed_conditionally": "AH factor multiplication realizes reduced Yoneda boundaries",
                "open": "MTT selection of AH representative or literal good-cover table",
            },
            "superset_repair": {
                "classification": "ROUTEC_RESIDUAL_REPAIR_OPEN",
                "succeeds": False,
                "open": "selected nonidentity rhoE/connection values and residual flags",
            },
            "diagnostic_backfit_only": {
                "used": False,
                "reason": "Only q79 cohomology/stability artifacts and selected-source contracts are imported; no SM measured targets are used.",
            },
        },
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "SelectedRouteCStabilityCentralNeutralSubtheorem",
            "proved": True,
            "statement": "For the selected rank-two V_alpha extension with L=(1,-2,0), selected nonzero Ext class, and target slope chamber p=(1,2,1), all central-neutral base-pullback rank-one destabilizer candidates are obstructed in the reduced Kunneth/Appell-Humbert Yoneda model. The full stability/HYM theorem is not yet proved, because one still needs a global rank-one torsion-free subsheaf enumeration or a selected Route-C residual/HYM source.",
        },
    }

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(
        json.dumps(
            {
                "status": STATUS,
                "candidate_path": rel(OUTPUT),
                "note_path": rel(NOTE),
                "full_stability_proved": False,
                "central_neutral_subtheorem_proved": True,
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
        """# MTT Selected Route-C Stability/HYM or Route-C Residual Source

Status: `MTT_SELECTED_ROUTEC_STABILITY_ATTEMPT_CENTRAL_NEUTRAL_CLOSED_GLOBAL_ENUMERATION_OPEN`

This is the direct attempt to prove the rank-two stability/HYM gate.

## Proven Subtheorem

For the selected rank-two extension

```text
0 -> L -> V_alpha -> L^-1 -> 0
L = (1,-2,0)
p = (1,2,1)
```

with the selected nonzero Ext vector in `H1(L^2)`, all central-neutral
base-pullback rank-one destabilizer candidates are obstructed in the reduced
Kunneth/Appell-Humbert Yoneda model.

Concretely:

- `L` has negative slope in the selected chamber.
- The quotient `L^-1` is excluded by the non-split Ext class.
- The Hom cone reduces central-neutral nonnegative-slope candidates to six
  classes.
- All six candidates have injective Yoneda boundary maps in the reduced model.
- The previously remaining zero-slope scalar is nonzero.
- Appell-Humbert degree addition conditionally realizes the reduced Yoneda
  multiplication, preserving the shared-circle degree zero condition.

## Not Yet Proved

This does not close full stability/HYM. The missing final mathematical step is
one of:

- prove every rank-one torsion-free destabilizing subsheaf has central-neutral
  base-pullback reflexive hull, or
- supply a selected HYM/Strominger or Route-C residual source directly.

Until then, the result is a strong stability subtheorem, not a selected HYM
existence certificate.

Next artifact: `MTT_Selected_RouteC_Global_Destabilizer_Enumeration_or_Selected_Residual_v1`.
""",
        encoding="utf-8",
    )
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))


if __name__ == "__main__":
    main()
