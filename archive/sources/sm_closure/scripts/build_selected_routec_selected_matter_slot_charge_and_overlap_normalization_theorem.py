"""Attempt selected matter-slot charge and overlap-normalization theorem."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
Q79 = ROOT.parent / "mtt-q79-proof-repro" / "candidate_data"

PREVIOUS = DATA / "selected_routec_selected_c1_routing_normalization_and_overlap_source_packet.candidate.json"
SECTOR_CHARGE = DATA / "selected_routec_weylpair_sector_charge_or_chirality_certificate.candidate.json"
HYBRID = DATA / "selected_routec_hybrid_matter_slot_galerkin_source_packet.candidate.json"
OPERATOR_OVERLAP = DATA / "selected_routec_selected_operator_source_and_overlap_tensor_packet.candidate.json"
SU5_TRANSVERSALITY = Q79 / "su5_matter_slot_transversality.candidate.json"
SU5_SOURCE_ATTEMPT = Q79 / "selected_su5_source_proof_attempt.candidate.json"
SU5_PROJECTION = Q79 / "su5_projection_tensor_derivation_attempt.candidate.json"
VISIBLE_CW_SOURCE = DATA / "selected_visible_chern_weil_operator_source.candidate.json"

OUTPUT = DATA / "selected_routec_selected_matter_slot_charge_and_overlap_normalization_theorem.candidate.json"
CERT = CERTS / "selected_routec_selected_matter_slot_charge_and_overlap_normalization_theorem_certificate.json"
NOTE = CORPUS / "MTT_Selected_RouteC_Selected_MatterSlot_Charge_and_Overlap_Normalization_Theorem_v1.md"

STATUS = "MTT_SELECTED_ROUTEC_MATTERSLOT_CHARGE_OVERLAP_NORMALIZATION_THEOREM_ATTEMPT_REDUCED_TO_SAME_SOURCE_OPERATOR_PACKET"
NEXT = "MTT_Selected_RouteC_SameSource_MatterSlot_Overlap_Operator_Packet_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    previous = load(PREVIOUS)
    sector_charge = load(SECTOR_CHARGE)
    hybrid = load(HYBRID)
    operator_overlap = load(OPERATOR_OVERLAP)
    su5_trans = load(SU5_TRANSVERSALITY)
    su5_source = load(SU5_SOURCE_ATTEMPT)
    su5_projection = load(SU5_PROJECTION)
    visible_cw = load(VISIBLE_CW_SOURCE)

    finite_matter_slot = {
        "under_transversality_closed": su5_trans["calculation_results"]["finite_transversality_theorem_closed"],
        "retarded_q79_orientation_closed": su5_trans["calculation_results"]["retarded_q79_orientation_closed"],
        "selected_packet": su5_trans["calculation_results"]["selected_packet"],
        "selected_mtt_source_present": su5_trans["calculation_results"]["selected_mtt_source_present"],
        "selected_ordered_su5_packet_closed": su5_trans["calculation_results"]["selected_ordered_su5_packet_closed"],
        "projection_tensor_conditionally_derived": su5_projection["calculation_results"]["finite_projection_tensor_derived"],
        "projection_tensor_promoted_to_selected": su5_projection["calculation_results"]["selected_polarization_source_promotes"],
        "verdict": "finite SU(5) transversality proves the desired I/F packet under a source hypothesis, not selected MTT closure",
    }

    matter_slot_charge = {
        "desired_phase_route": previous["attempts"]["c1_routing"]["conditional_route"]["phase_Z_to"],
        "desired_shift_route": previous["attempts"]["c1_routing"]["conditional_route"]["shift_X_to"],
        "structural_su5_match": sector_charge["certificate_result"]["strongest_structural_match"],
        "routeA_matches_required_partition": sector_charge["superset_paths"]["route_A"]["sector_implication"]["matches_required_partition"],
        "routeB_current_selected_block_uniform": sector_charge["superset_paths"]["route_B"]["evidence"]["all_right_orientations_uniform"],
        "singlet_1M_rule_present": hybrid["attempts"]["conditional_su5_fixture_fill"]["has_1M_singlet_neutrino_rule"],
        "selected_charge_table_closed": sector_charge["certificate_result"]["selected_certificate_closed"],
        "verdict": "the charge theorem is localized but not closed; the 1_M Dirac-neutrino shift rule remains an explicit sublemma",
    }

    overlap_normalization = {
        "conditional_deltaTheta": previous["attempts"]["normalization"]["conditional_deltaTheta"],
        "conditional_condition_number": previous["attempts"]["normalization"]["conditional_condition_number"],
        "conditional_residual_norm": previous["attempts"]["normalization"]["conditional_residual_norm"],
        "selected_normalization_emitted": previous["attempts"]["normalization"]["selected_normalization_emitted"],
        "selected_overlap_functor_emitted": previous["attempts"]["overlap_source"]["selected_overlap_tensor_or_functor_emitted"],
        "canonical_overlap_lane_retired_for_nonzero": previous["attempts"]["overlap_source"]["canonical_overlap_lane_retired_for_nonzero"],
        "enriched_weyl_pair_conditionally_sufficient": previous["attempts"]["overlap_source"]["enriched_weyl_pair_conditionally_sufficient"],
        "verdict": "the conditional normalization is exact, but trace/inner-product/Hessian normalization is not selected",
    }

    same_source_obstruction = {
        "su5_source_attempt_status": su5_source["status"],
        "all_su5_source_routes_blocked": su5_source["calculation_results"]["all_current_source_routes_blocked"],
        "first_missing_su5_object": su5_source["verdict"]["first_missing_object"],
        "visible_cw_source_status": visible_cw["status"],
        "visible_selected_operator_source_closed": visible_cw["open_gates"]["selected_visible_operator_source_closed"],
        "critical_overlap_obligation": visible_cw["open_gates"]["critical_obligations"]["primitive_C1_contractions"],
        "critical_de_dotd_obligation": visible_cw["open_gates"]["critical_obligations"]["selected_D_E_dotD_Riesz_Green"],
        "verdict": "both SU(5) and Route-C/visible-source lanes reduce to the same selected same-source operator packet",
    }

    theorem_attempt = {
        "name": "SelectedMatterSlotChargeAndOverlapNormalizationTheorem",
        "fully_proved": False,
        "proved_subresults": [
            "finite SU(5) transversality gives q79 U_10=I_3 and U_bar5=F under selected transversality",
            "conditional C1 routing Z->u/e and X->d/nuD is exact and unique relative to locked columns",
            "source-level qutrit Weyl carrier and active shift (1,1) are already closed",
            "canonical and primitive-only nonzero routes are correctly retired",
        ],
        "open_sublemmas": [
            "selected matter-slot charge table deriving 10_M -> u/e",
            "selected 1_M Dirac-neutrino rule routing nuD with the shift/non-10 side",
            "selected overlap-transfer functor T_selected",
            "selected normalization from trace/inner-product/Hessian kernel",
            "same-source D_E/dotD/Riesz/Green/overlap operator packet",
        ],
        "minimal_reduction": NEXT,
    }

    candidate = {
        "candidate": "MTTSelectedRouteCSelectedMatterSlotChargeAndOverlapNormalizationTheorem",
        "status": STATUS,
        "inputs": {
            "previous_c1_routing_normalization_packet": rel(PREVIOUS),
            "sector_charge_or_chirality_certificate": rel(SECTOR_CHARGE),
            "hybrid_matter_slot_packet": rel(HYBRID),
            "operator_overlap_packet": rel(OPERATOR_OVERLAP),
            "q79_su5_matter_slot_transversality": rel(SU5_TRANSVERSALITY),
            "q79_su5_source_attempt": rel(SU5_SOURCE_ATTEMPT),
            "q79_su5_projection_tensor": rel(SU5_PROJECTION),
            "visible_cw_operator_source": rel(VISIBLE_CW_SOURCE),
        },
        "finite_matter_slot": finite_matter_slot,
        "matter_slot_charge": matter_slot_charge,
        "overlap_normalization": overlap_normalization,
        "same_source_obstruction": same_source_obstruction,
        "theorem_attempt": theorem_attempt,
        "selection_verdict": {
            "finite_algebra_is_not_blocker": True,
            "conditional_routing_and_normalization_are_exact": True,
            "selected_matter_slot_charge_closed": False,
            "selected_overlap_normalization_closed": False,
            "same_source_operator_packet_required": True,
            "full_SM_or_no_knob_closure": False,
        },
        "what_closes_now": {
            "finite_su5_transversality_imported": True,
            "matter_slot_charge_sublemmas_identified": True,
            "overlap_normalization_sublemmas_identified": True,
            "same_source_obstruction_identified": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_10M_to_u_e_charge_rule": True,
            "selected_non10_and_1M_to_d_nuD_shift_rule": True,
            "selected_overlap_transfer_functor": True,
            "selected_trace_innerproduct_hessian_normalization": True,
            "emit_selected_A_selected_and_b_selected": True,
            "full_SM_or_no_knob_closure": True,
        },
        "superset_strategy": {
            "mode": "CONSTRAINED_SUPERSET_WITH_LOCKED_TARGET",
            "using_one_straight_path": False,
            "paths_combined": [
                "finite SU(5) transversality under source hypothesis",
                "source-level qutrit Weyl carrier",
                "Route-C conditional C1 transfer",
                "visible same-source operator packet contract",
            ],
            "locked_target_role": "checks exactness and uniqueness of conditional routing only",
            "observed_data_used": False,
            "target_fitting_used": False,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(
        json.dumps(
            {
                "status": STATUS,
                "candidate_path": rel(OUTPUT),
                "note_path": rel(NOTE),
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
        """# MTT Selected MatterSlot Charge and Overlap Normalization Theorem

Status: `MTT_SELECTED_ROUTEC_MATTERSLOT_CHARGE_OVERLAP_NORMALIZATION_THEOREM_ATTEMPT_REDUCED_TO_SAME_SOURCE_OPERATOR_PACKET`

This artifact attempts to prove the theorem that would promote the conditional
C1 Weyl-pair packet to selected data.

## What Closes

The finite SU(5) transversality theorem is strong:

```text
q79 retarded branch:
U_10 = I_3
U_bar5 = F
```

under the selected transversality/source hypothesis.  This matches the desired
matter-slot direction for the conditional C1 route.

The conditional C1 calculation is also exact:

```text
Z -> u/e
X -> d/nuD
deltaTheta = (1,1)
```

## Why This Is Still Not Selected Closure

The selected source does not yet emit:

- the `10_M -> u/e` matter-slot charge rule,
- the `1_M` Dirac-neutrino rule routing `nuD` with the shift side,
- the selected overlap-transfer functor,
- the selected trace/inner-product/Hessian normalization,
- selected `A_selected` and `b_selected`.

Therefore the theorem reduces to one same-source operator packet, not to more
finite algebra.

Next artifact: `MTT_Selected_RouteC_SameSource_MatterSlot_Overlap_Operator_Packet_v1`.
""",
        encoding="utf-8",
    )
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))


if __name__ == "__main__":
    main()
