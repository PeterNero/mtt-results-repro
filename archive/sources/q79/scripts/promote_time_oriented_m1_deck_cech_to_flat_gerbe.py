"""Promote the m=1 deck/Cech cocycle to a conditional flat gerbe model.

This script uses the deck/Cech lift as a group cocycle on the candidate Iwasawa
deck scaffold.  On a compact nilmanifold whose universal cover is contractible,
group cocycles give flat Cech/Deligne representatives on the quotient.  The
promotion is conditional because the standard deck scaffold is still not marked
MTT-selected in the current proof package.

The result closes a topological/geometric bridge, not the selected visible
operator source.  In particular it does not verify Freed-Witten on selected
cycles, Green-Schwarz curvature terms, or selected D_E/dotD data.
"""

from __future__ import annotations

import json
from math import gcd
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATES = ROOT / "certificates"
CANDIDATE_DATA = ROOT / "candidate_data"
CANDIDATE = CANDIDATE_DATA / "time_oriented_m1_flat_gerbe_promotion.candidate.json"
CERTIFICATE = CERTIFICATES / "time_oriented_m1_flat_gerbe_promotion_certificate.json"
DECK_LIFT_CERT = CERTIFICATES / "time_oriented_m1_deck_cech_lift_certificate.json"
DECK_LIFT_CANDIDATE = CANDIDATE_DATA / "time_oriented_m1_deck_cech_lift.candidate.json"
STANDARD_DECK_CERT = CERTIFICATES / "iwasawa_standard_lattice_deck_scaffold_certificate.json"
SECTOR_MAP_CERT = CERTIFICATES / "iwasawa_block_factorized_sector_maps_certificate.json"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def get(data: dict[str, Any], *keys: str, default: Any = None) -> Any:
    value: Any = data
    for key in keys:
        if not isinstance(value, dict) or key not in value:
            return default
        value = value[key]
    return value


def torsion_order_from_periods(periods: dict[str, int]) -> int:
    nonzero = [value % 3 for value in periods.values() if value % 3]
    return 3 if nonzero else 1


def analyze() -> dict[str, Any]:
    deck_cert = load_json(DECK_LIFT_CERT)
    deck_candidate = load_json(DECK_LIFT_CANDIDATE)
    standard_deck = load_json(STANDARD_DECK_CERT)
    sector_maps = load_json(SECTOR_MAP_CERT)

    periods = get(
        deck_candidate,
        "pulled_back_deck_cech_data",
        "generator_period_table_mod3",
        default={},
    )
    torsion_order = torsion_order_from_periods(periods)
    deck_lift_closed = (
        deck_cert.get("status")
        == "TIME_ORIENTED_M1_DECK_CECH_LIFT_CLOSED_GEOMETRIC_OPERATOR_SOURCE_OPEN"
        and get(deck_cert, "calculation_results", "deck_cech_pullback_constructed") is True
    )
    standard_deck_scaffold_valid = (
        get(standard_deck, "verified_algebra", "generator_count") == 6
        and get(standard_deck, "verified_algebra", "coframe_invariant_under_left_deck_action")
        is True
        and get(standard_deck, "verified_algebra", "compact_quotient_if_candidate_Gamma0_selected")
        is True
    )
    standard_deck_selected = (
        get(standard_deck, "guardrails", "claims_Gamma0_is_MTT_selected") is True
    )
    finite_sector_projectors_valid = (
        get(sector_maps, "calculation_results", "finite_block_factorized_sector_maps_valid")
        is True
        and get(sector_maps, "calculation_results", "family_sector_projectors_full_rank_three")
        is True
        and get(sector_maps, "calculation_results", "higgs_line_rank_one_projector") is True
    )

    flat_promotion_conditional = (
        deck_lift_closed
        and standard_deck_scaffold_valid
        and torsion_order == 3
        and finite_sector_projectors_valid
    )
    selected_geometric_promotion_closed = flat_promotion_conditional and standard_deck_selected

    fw_coprime_primary_split = gcd(2, torsion_order) == 1
    status = (
        "TIME_ORIENTED_M1_FLAT_GERBE_PROMOTION_CONDITIONAL_CLOSED_SELECTION_OPEN"
        if flat_promotion_conditional and not selected_geometric_promotion_closed
        else (
            "TIME_ORIENTED_M1_FLAT_GERBE_PROMOTION_SELECTED_CLOSED_OPERATOR_OPEN"
            if selected_geometric_promotion_closed
            else "TIME_ORIENTED_M1_FLAT_GERBE_PROMOTION_NOT_CLOSED"
        )
    )

    return {
        "candidate": "TimeOrientedM1FlatGerbePromotion",
        "status": status,
        "generated_by": "scripts/promote_time_oriented_m1_deck_cech_to_flat_gerbe.py",
        "inputs": {
            "deck_cech_lift_certificate": "time_oriented_m1_deck_cech_lift_certificate.json",
            "standard_deck_scaffold_certificate": "iwasawa_standard_lattice_deck_scaffold_certificate.json",
            "sector_maps_certificate": "iwasawa_block_factorized_sector_maps_certificate.json",
        },
        "aspherical_nilmanifold_route": {
            "universal_cover": "complex Heisenberg group, diffeomorphic to R^6",
            "candidate_lattice": get(
                standard_deck,
                "candidate_standard_gaussian_lattice",
                "lattice",
            ),
            "contractible_universal_cover": True,
            "quotient_is_K_Gamma_1_if_candidate_lattice_selected": True,
            "standard_deck_scaffold_valid": standard_deck_scaffold_valid,
            "standard_deck_scaffold_selected_by_current_certificates": standard_deck_selected,
            "theorem_used": (
                "For an aspherical quotient, a normalized U(1)-valued group "
                "2-cocycle on the deck group represents a flat Cech/Deligne "
                "gerbe class on the quotient."
            ),
        },
        "flat_gerbe_model": {
            "deck_multiplier": "sigma(g,h)=exp(2*pi*i*B_deck(g,h))",
            "period_denominator": 3,
            "torsion_order": torsion_order,
            "curvature_H_form": "0",
            "deligne_local_data_model": {
                "local_two_forms_B_i": "0",
                "local_one_forms_A_ij": "0",
                "locally_constant_U1_two_cocycle_g_ijk": "induced by sigma on deck-indexed overlaps",
            },
            "dixmier_douady_class": {
                "type": "flat torsion",
                "order": torsion_order,
                "nontrivial_because_qutrit_commutator_rank_two": torsion_order == 3,
            },
            "green_schwarz_curvature_effect": (
                "No de Rham H-flux is added by this flat representative; the "
                "full heterotic Bianchi identity with gauge/gravity curvature "
                "terms is a separate selected-background check."
            ),
        },
        "projective_bundle_and_projector_retention": {
            "qutrit_projective_carrier_matched": get(
                deck_cert,
                "calculation_results",
                "qutrit_projective_commutator_matched",
            )
            is True,
            "finite_block_factorized_sector_projectors_valid": finite_sector_projectors_valid,
            "family_projectors": "Q,u,d,L,e,N are full rank-three identity projectors on the projective family block",
            "higgs_projector": "H is a separate ordinary rank-one line",
            "finite_projector_retention_no_algebraic_obstruction": finite_sector_projectors_valid,
            "selected_projector_retention_verified": False,
        },
        "freed_witten_reduction": {
            "flat_gerbe_torsion_order": torsion_order,
            "W3_is_two_primary": True,
            "three_torsion_cannot_cancel_two_primary_W3": fw_coprime_primary_split,
            "condition_for_each_selected_cycle_Y": [
                "W3(Y)=0",
                "DD(B)|_Y=0 for the 3-torsion flat gerbe class",
            ],
            "selected_cycles_supplied": False,
            "freed_witten_verified": False,
        },
        "calculation_results": {
            "deck_cech_lift_input_closed": deck_lift_closed,
            "conditional_flat_gerbe_representative_exists": flat_promotion_conditional,
            "selected_flat_gerbe_representative_closed": selected_geometric_promotion_closed,
            "curvature_H_zero_for_flat_representative": flat_promotion_conditional,
            "torsion_order_three": torsion_order == 3,
            "projective_qutrit_module_compatible": get(
                deck_cert,
                "calculation_results",
                "qutrit_projective_commutator_matched",
            )
            is True,
            "finite_projector_retention_no_algebraic_obstruction": finite_sector_projectors_valid,
            "freed_witten_primary_decomposition_reduced": fw_coprime_primary_split,
            "freed_witten_verified": False,
            "selected_D_E_dotD_constructed": False,
        },
        "what_this_closes": {
            "conditional_group_cocycle_to_flat_Deligne_Cech_gerbe_promotion": flat_promotion_conditional,
            "flat_curvature_H_zero_statement_for_this_torsion_representative": flat_promotion_conditional,
            "qutrit_projective_bundle_compatibility_with_flat_gerbe": flat_promotion_conditional,
            "finite_block_projector_retention_has_no_algebraic_obstruction": finite_sector_projectors_valid,
            "Freed_Witten_reduced_to_cycle_restriction_and_W3_checks": fw_coprime_primary_split,
        },
        "still_open": {
            "MTT_selection_of_standard_deck_scaffold_or_equivalent_cover": not standard_deck_selected,
            "actual_good_cover_and_geometric_cycle_restriction_tables": True,
            "Freed_Witten_DD_restriction_on_selected_cycles": True,
            "Freed_Witten_W3_or_spinC_check_on_selected_cycles": True,
            "heterotic_Green_Schwarz_Bianchi_with_selected_gauge_gravity_curvatures": True,
            "selected_projector_retention_for_visible_zero_modes": True,
            "selected_D_E_dotD_Riesz_Green_files_from_same_branch": True,
            "selected_C1_primitive_contractions": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_Gamma0_is_MTT_selected": False,
            "claims_unconditional_selected_geometric_representative": False,
            "claims_Freed_Witten_verified": False,
            "claims_Green_Schwarz_Bianchi_verified": False,
            "claims_selected_projector_retention": False,
            "claims_selected_D_E_dotD_constructed": False,
            "claims_Yukawa_or_CKM_magnitudes": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "The finite m=1 deck cocycle has a conditional flat gerbe "
                "promotion on the candidate aspherical Iwasawa deck scaffold. "
                "It supplies a zero-curvature torsion Deligne/Cech model and "
                "a compatible qutrit projective module, but the scaffold and "
                "visible operator source are still not selected by current "
                "certificates."
            )
            if flat_promotion_conditional
            else "The conditional flat gerbe promotion did not close.",
            "next_closing_object": (
                "Supply the selected cover/cycle data and verify the 3-torsion "
                "restriction plus W3=0 Freed-Witten checks, or bypass this route "
                "with a direct selected HYM/Strominger operator-source packet."
            ),
        },
    }


def write_outputs(report: dict[str, Any]) -> None:
    CANDIDATE.parent.mkdir(parents=True, exist_ok=True)
    CERTIFICATE.parent.mkdir(parents=True, exist_ok=True)
    CANDIDATE.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    certificate = {
        "certificate": "TimeOrientedM1FlatGerbePromotion",
        "status": report["status"],
        "analysis_script": "scripts/promote_time_oriented_m1_deck_cech_to_flat_gerbe.py",
        "candidate_data": "candidate_data/time_oriented_m1_flat_gerbe_promotion.candidate.json",
        "inputs": report["inputs"],
        "aspherical_nilmanifold_route": report["aspherical_nilmanifold_route"],
        "flat_gerbe_model": report["flat_gerbe_model"],
        "projective_bundle_and_projector_retention": report[
            "projective_bundle_and_projector_retention"
        ],
        "freed_witten_reduction": report["freed_witten_reduction"],
        "calculation_results": report["calculation_results"],
        "what_this_closes": report["what_this_closes"],
        "still_open": report["still_open"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    CERTIFICATE.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    report = analyze()
    write_outputs(report)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
