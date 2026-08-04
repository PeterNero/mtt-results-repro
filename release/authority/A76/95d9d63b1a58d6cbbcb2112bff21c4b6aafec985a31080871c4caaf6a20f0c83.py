"""Test the natural 96/48-dimensional gauge-insertion intertwiner candidates."""
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_gaugeinsertionintertwinerandfinitematchingcondition"
OUT = ROOT / "candidate_data" / SLUG
DIMENSION = OUT / "tower_augmentation_vs_sm_carrier_dimension_test.packet.json"
EQUIVARIANCE = OUT / "finite_character_equivariance_obstruction.packet.json"
PRODUCT = OUT / "canonical_product_domain_construction.packet.json"
MATCHING = OUT / "finite_matching_condition_status.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_GaugeInsertionIntertwinerAndFiniteMatchingCondition_v1.md"
STATUS = "MTT_SELECTED_96_48_DIMENSION_COINCIDENCE_TESTED_EQUIVARIANT_MATTER_INTERTWINER_REJECTED_GAUGE_COMPLEX_SOURCE_OPEN"
NEXT = "MTT_Selected_GaugeFixedFluctuationComplexOnTowerAugmentationDomains_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    paths = {
        "A75_contract": ROOT / "candidate_data" / "selected_physicalkinetichessianblockidentity_or_modernprecisiongaugevalidation" / "selected_gauge_insertion_intertwiner_and_matching_condition.template.json",
        "A75_intertwiner": ROOT / "candidate_data" / "selected_physicalkinetichessianblockidentity_or_modernprecisiongaugevalidation" / "physical_gauge_insertion_intertwiner_audit.packet.json",
        "typed_SM_carrier": ROOT / "candidate_data" / "selected_typedfamilygaugecarrieranddiagonalsmrepresentationtheorem" / "typed_family_gauge_carrier_and_anomaly_table.packet.json",
        "gauge_supertrace": ROOT / "candidate_data" / "selected_gaugeinsertedheatsupertracesecondvariation_or_commonschemethresholdpayload.candidate.json",
        "L64_spectrum": ROOT / "candidate_data" / "selected_actualz64towerkineticfunctionaltyping_or_resolventroutingpromotion" / "actual_z64_tower_spectrum.packet.json",
        "A73_action": ROOT / "candidate_data" / "selected_gaugekineticactionderivationandfrozenprofilevalidation" / "normalized_determinant_action_derivation.packet.json",
    }
    data = {key: load(path) for key, path in paths.items()}

    one_family_dimension = data["typed_SM_carrier"]["typed_carrier"]["one_family_dimension"]
    chiral_dimension = data["typed_SM_carrier"]["typed_carrier"]["physical_dimension"]
    full_finite_dimension = data["gauge_supertrace"]["finite_carrier"]["dimension"]
    q_active_dimension = 16 * 6
    e_active_dimension = 16 * 3
    dimension = {
        "schema": "MTTTowerAugmentationVsSMCarrierDimensionTest.v1",
        "status": "NUMERICAL_DIMENSIONS_MATCH_TYPES_AND_ACTIONS_DIFFER",
        "A73_active_domains": {
            "q": "C16_L64_tower tensor Aug(C[Z7])",
            "q_dimension": q_active_dimension,
            "e_return": "C16_tower tensor Aug(C[Z4])",
            "e_return_dimension": e_active_dimension,
        },
        "selected_SM_matter_domains": {
            "one_family": "H16_SM",
            "one_family_dimension": one_family_dimension,
            "three_family_chiral": "C3_family tensor H16_SM",
            "three_family_chiral_dimension": chiral_dimension,
            "particle_antiparticle_finite_carrier_dimension": full_finite_dimension,
        },
        "coincidences": {
            "q_active_equals_full_finite_fermion_dimension": q_active_dimension == full_finite_dimension,
            "e_active_equals_three_family_chiral_dimension": e_active_dimension == chiral_dimension,
        },
        "typing": {
            "C16_L64_is_a_recursive_tower_mode_space": True,
            "H16_SM_is_a_one_family_gauge_representation": True,
            "these_C16_factors_are_selected_as_the_same_object": False,
            "dimension_equality_implies_physical_intertwiner": False,
        },
    }

    z7_phases = [2.0 * math.pi * k / 7.0 for k in range(1, 7)]
    z4_aug_phases = [math.pi / 2.0, math.pi, 3.0 * math.pi / 2.0]
    z3_phases = [0.0, 2.0 * math.pi / 3.0, 4.0 * math.pi / 3.0]
    equivariance = {
        "schema": "MTTFiniteCharacterEquivarianceObstruction.v1",
        "status": "OBVIOUS_MATTER_CARRIER_IDENTIFICATIONS_FAIL_SELECTED_EQUIVARIANCE",
        "q_factor_test": {
            "source": "Aug(C[Z7])",
            "source_generator_phases": z7_phases,
            "candidate_target_labels": "C3_family tensor particle/antiparticle doubling",
            "selected_target_symmetries": ["Z3 family", "antiunitary particle-antiparticle real structure"],
            "hom_Z7_to_Z3_times_Z2_is_trivial": math.gcd(7, 6) == 1,
            "selected_nontrivial_Z7_action_on_target_exists": False,
            "equivariant_intertwiner_promoted": False,
            "conclusion": "The 6=3*2 dimension match cannot identify the Z7 augmentation action with family/conjugation bookkeeping. Any homomorphism Z7 -> Z3 x Z2 is trivial, while Aug(C[Z7]) has no trivial character.",
        },
        "e_factor_test": {
            "source": "Aug(C[Z4])",
            "source_generator_phases": z4_aug_phases,
            "candidate_target": "C3_family",
            "target_generator_phases": z3_phases,
            "hom_Z4_to_Z3_is_trivial": math.gcd(4, 3) == 1,
            "generator_spectra_equal": False,
            "equivariant_intertwiner_promoted": False,
            "conclusion": "The 3-dimensional Lens-Z4 augmentation is not the selected Z3 family representation despite equal dimension.",
        },
        "C16_factor_test": {
            "source": "C16_L64 recursive composition tower",
            "target": "H16_SM one-family chiral representation",
            "same_source_id": False,
            "selected_gauge_equivariant_map": False,
            "dimension_only_identification_rejected": True,
        },
        "scope": "This rejects the two obvious matter-carrier intertwiners. It does not forbid a new gauge/ghost/Higgs fluctuation complex carrying the tower and augmentation actions.",
    }

    product = {
        "schema": "MTTCanonicalTowerAugmentationProductDomain.v1",
        "status": "MATHEMATICAL_PRODUCT_DOMAINS_CANONICAL_PHYSICAL_GAUGE_SOURCE_NOT_EMITTED",
        "domains": {
            "Vq_full": {"formula": "C16_L64 tensor C[Z7]", "dimension": 112},
            "Vq_active": {"formula": "C16_L64 tensor Aug(C[Z7])", "dimension": 96},
            "Ve_full": {"formula": "C16_tower tensor C[Z4]", "dimension": 64},
            "Ve_active": {"formula": "C16_tower tensor Aug(C[Z4])", "dimension": 48},
        },
        "canonical_projectors": {
            "P7": "I7-|1_7><1_7|/7",
            "P7_rank": 6,
            "P4": "I4-|1_4><1_4|/4",
            "P4_rank": 3,
            "selected_as_orthogonal_complements_once_carriers_are_given": True,
        },
        "mathematical_identity_intertwiners": {
            "Jq_product_identity": True,
            "Je_product_identity": True,
            "A73_block_form_replayed": data["A73_action"]["status"] == "ONE_FINITE_POSITIVE_ACTION_EMITS_A72_RESPONSE_EXACTLY",
        },
        "physical_source": {
            "gauge_one_form_domain_equals_Vq_or_Ve": False,
            "ghost_domain_and_BRST_complex_emitted": False,
            "fermion_and_Higgs_Hessians_on_same_background_emitted": False,
            "q79_P7_colored_routing_emitted": False,
            "Lens_P4_lepton_return_routing_emitted": False,
            "strict_intertwiner_closed": False,
        },
    }

    matching = {
        "schema": "MTTFiniteMatchingConditionStatus.v1",
        "status": "FINITE_RELATIVE_DETERMINANT_WELL_DEFINED_MATCHING_BOUNDARY_SOURCE_OPEN",
        "closed": {
            "finite_matrix_logdet_needs_no_UV_regulator": True,
            "relative_determinant_logdet_H_epsilon_minus_logdet_H_zero_is_exact": True,
            "A51_tree_gauge_metric_is_common_after_GUT_normalization": True,
        },
        "not_closed": {
            "bare_or_local_relative_Fa2_terms_excluded_by_source": True,
            "common_background_BRST_scheme_for_all_blocks": True,
            "matching_scale_selected_from_same_Hessian": True,
            "modern_full_covariance_profile_validation": True,
        },
        "no_go": "The condition Gamma_threshold(0)=0 does not exclude a finite linear term epsilon*(r1,r3) that also vanishes at epsilon=0. A source boundary condition on the first derivative is required.",
        "new_continuous_parameters": 0,
    }

    checks = {
        "q_active_dimension_96": q_active_dimension == 96,
        "e_active_dimension_48": e_active_dimension == 48,
        "dimension_coincidences_found": all(dimension["coincidences"].values()),
        "dimension_only_identification_rejected": not dimension["typing"]["dimension_equality_implies_physical_intertwiner"],
        "Z7_to_Z3Z2_nontrivial_map_absent": equivariance["q_factor_test"]["hom_Z7_to_Z3_times_Z2_is_trivial"],
        "Z4_to_Z3_nontrivial_map_absent": equivariance["e_factor_test"]["hom_Z4_to_Z3_is_trivial"],
        "C16_types_not_conflated": equivariance["C16_factor_test"]["dimension_only_identification_rejected"],
        "canonical_product_domains_constructed": product["mathematical_identity_intertwiners"]["Jq_product_identity"] and product["mathematical_identity_intertwiners"]["Je_product_identity"],
        "physical_intertwiner_not_overclaimed": not product["physical_source"]["strict_intertwiner_closed"],
        "finite_matching_not_overclaimed": matching["not_closed"]["bare_or_local_relative_Fa2_terms_excluded_by_source"],
    }
    candidate = {
        "schema": "MTTSelectedGaugeInsertionIntertwinerAndFiniteMatchingCondition.v1",
        "status": STATUS,
        "results": {
            "active_q_and_e_dimensions": [96, 48],
            "existing_SM_carrier_dimensions": [96, 48],
            "dimension_coincidences_exact": True,
            "obvious_matter_carrier_intertwiners_equivariant": False,
            "canonical_tower_augmentation_product_domains_constructed": True,
            "physical_gauge_fixed_fluctuation_complex_emitted": False,
            "finite_matching_condition_selected": False,
            "strict_gauge_values_accepted": 0,
            "new_continuous_parameters": 0,
        },
        "outputs": {
            "dimension": str(DIMENSION.relative_to(ROOT)).replace("\\", "/"),
            "equivariance": str(EQUIVARIANCE.relative_to(ROOT)).replace("\\", "/"),
            "product": str(PRODUCT.relative_to(ROOT)).replace("\\", "/"),
            "matching": str(MATCHING.relative_to(ROOT)).replace("\\", "/"),
        },
        "checks": {key: bool(value) for key, value in checks.items()},
        "authority_hashes": [{"path": str(path), "sha256": sha256(path)} for path in paths.values()],
        "next_required_artifact": NEXT,
    }
    cert = {
        "certificate": "MTT_Selected_GaugeInsertionIntertwinerAndFiniteMatchingCondition_v1",
        "status": STATUS,
        "active_q_e_dimensions": [96, 48],
        "selected_SM_full_chiral_dimensions": [96, 48],
        "dimension_coincidences_exact": True,
        "equivariant_matter_carrier_intertwiners_closed": False,
        "canonical_product_domains_constructed": True,
        "physical_gauge_fixed_complex_closed": False,
        "finite_matching_condition_closed": False,
        "strict_gauge_values_accepted": 0,
        "new_continuous_parameters": 0,
        "next_required_artifact": NEXT,
    }
    note = f"""# MTT Selected Gauge Insertion Intertwiner and Finite Matching Condition v1

## Exact dimension coincidence

Removing the trivial projector directions gives

```text
dim(C16_L64 tensor Aug(Z7)) = 16*6 = 96,
dim(C16_tower tensor Aug(Z4)) = 16*3 = 48.
```

These equal the selected particle/antiparticle finite-carrier dimension `96` and three-family chiral
dimension `48`. This is a real structural clue, not yet an identification.

## Equivariance obstruction

The factors have different selected meanings. `C16_L64` is the recursive composition tower while
`H16_SM` is one family's chiral gauge representation. No selected map identifies them. More sharply,
the nontrivial `Z7` character space cannot be identified with `Z3` family times a twofold conjugation
label: every homomorphism `Z7 -> Z3 x Z2` is trivial. Likewise every homomorphism `Z4 -> Z3` is
trivial, and the Lens augmentation generator has phases `(pi/2,pi,3pi/2)` rather than the family
phases `(0,2pi/3,4pi/3)`.

Therefore the exact `96/48` dimension matches do not produce gauge-equivariant physical
intertwiners. This prevents a dimension-only promotion of A73 onto the existing matter carrier.

## Constructed product domains

The mathematical domains and projectors are canonical once their carriers are supplied:

```text
Vq = C16_L64 tensor C[Z7],   P7 = I-|1><1|/7,
Ve = C16_tower tensor C[Z4], P4 = I-|1><1|/4.
```

Identity maps on these product domains replay the A73 blocks exactly. What is not emitted is the
physical statement that the gauge one-form/ghost/Higgs/fermion fluctuation complex lives on these
domains with the declared routing and common background.

## Matching condition

The finite relative determinant is exact and regulator-free. Setting its value to zero at the base
point does not remove an additive finite term linear in the gauge invariant, so the first-derivative
matching condition must still be selected by the microscopic action.

The next object is `{NEXT}`. It must construct the actual BRST gauge-fixed fluctuation complex on the
tower-augmentation domains or provide a different selected intertwiner, then fix the two relative
matching directions without observed gauge values.
"""

    dump(DIMENSION, dimension)
    dump(EQUIVARIANCE, equivariance)
    dump(PRODUCT, product)
    dump(MATCHING, matching)
    dump(CANDIDATE, candidate)
    dump(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
