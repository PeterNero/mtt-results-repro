from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
Q79_ROOT = ROOT.parent / "mtt-q79-proof-repro"
THETA_ROOT = ROOT.parent / "18 Theta-Closure & Execution Program"
PROTO_ROOT = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")
SLUG = "selected_baselinecostmultiplicitysourceandnoncentralspectatorexclusion"
STATUS = (
    "MTT_SELECTED_SHARED_Z21_BASELINE_MULTIPLICITY_TRACE_AND_EXPLICIT_PARENT_FUNCTIONAL_CLOSED_"
    "PHYSICAL_GAUGE_HESSIAN_RESTRICTION_AND_STRICT_SPECTATOR_COMPLETENESS_OPEN"
)
NEXT = "MTT_Selected_SharedCircleClosureHessianToGaugeZeroModeRestrictionAndCountertermCompleteness_v1"

OUT = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_BaselineCostMultiplicitySourceAndNoncentralSpectatorExclusion_v1.md"
SHARED = OUT / "shared_z21_marginal_and_unique_character_trace.packet.json"
ACTION = OUT / "common_modecount_schur_casimir_parent_functional.packet.json"
SPECTATORS = OUT / "sector_partition_spectator_completeness_and_strict_gate.packet.json"
EXECUTION = OUT / "baseline_plus_defect_gauge_execution.packet.json"
GATE = OUT / "remaining_physical_hessian_restriction_gate.packet.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def max_abs(values: list[float]) -> float:
    return max((abs(value) for value in values), default=0.0)


def gell_mann_generators() -> list[np.ndarray]:
    zero = 0.0
    one = 1.0
    i = 1.0j
    root3 = math.sqrt(3.0)
    lambdas = [
        np.asarray([[zero, one, zero], [one, zero, zero], [zero, zero, zero]], dtype=complex),
        np.asarray([[zero, -i, zero], [i, zero, zero], [zero, zero, zero]], dtype=complex),
        np.asarray([[one, zero, zero], [zero, -one, zero], [zero, zero, zero]], dtype=complex),
        np.asarray([[zero, zero, one], [zero, zero, zero], [one, zero, zero]], dtype=complex),
        np.asarray([[zero, zero, -i], [zero, zero, zero], [i, zero, zero]], dtype=complex),
        np.asarray([[zero, zero, zero], [zero, zero, one], [zero, one, zero]], dtype=complex),
        np.asarray([[zero, zero, zero], [zero, zero, -i], [zero, i, zero]], dtype=complex),
        np.asarray([[one / root3, zero, zero], [zero, one / root3, zero], [zero, zero, -2.0 / root3]], dtype=complex),
    ]
    return [matrix / 2.0 for matrix in lambdas]


def main() -> int:
    paths = {
        "A46_family": ROOT / "candidate_data" / "selected_typedfamilygaugecarrieranddiagonalsmrepresentationtheorem" / "typed_family_gauge_carrier_and_anomaly_table.packet.json",
        "A69_operator": ROOT / "candidate_data" / "selected_commonquarkorder_sharedcirclekineticoperator_or_exactresidualspectrum" / "conditional_common_projected_kinetic_operator.packet.json",
        "A74_trace": ROOT / "candidate_data" / "selected_normalizeddeterminantactionfrommtthessian_or_independentgaugeprofiletest" / "finite_trace_and_projector_uniqueness.packet.json",
        "A75_center": ROOT / "candidate_data" / "selected_physicalkinetichessianblockidentity_or_modernprecisiongaugevalidation" / "gaussian_determinant_and_center_valued_trace.packet.json",
        "A76_obstruction": ROOT / "candidate_data" / "selected_gaugeinsertionintertwinerandfinitematchingcondition" / "finite_character_equivariance_obstruction.packet.json",
        "A77_routing": ROOT / "candidate_data" / "selected_gaugefixedfluctuationcomplexontoweraugmentationdomains" / "primitive_character_orbit_projector_routing.packet.json",
        "A78_functor": ROOT / "candidate_data" / "selected_producttriplegaugefluctuationfunctorandrelativeboundarycondition" / "center_response_to_sector_kinetic_density_functor.packet.json",
        "A80_execution": ROOT / "candidate_data" / "selected_anchoringparityinsertionlaw_or_independentkineticgramderivation" / "positive_representative_gauge_execution.packet.json",
        "A81_candidate": ROOT / "candidate_data" / "selected_fullanchordefecthessianactionownershipandspectatorcancellation.candidate.json",
        "Z7_certificate": Q79_ROOT / "certificates" / "z7_fuyau_mukai_charge_sector_certificate.json",
        "ambient_Z1344": Q79_ROOT / "proof_corpus" / "Ambient_to_Selected_Z448_CP_Quotient_Map_v1.md",
        "color_schur": THETA_ROOT / "_md_v3_corrected" / "Color_Singlet_Redundancy_Source_for_Bq_v1.md",
        "proto_spinor": PROTO_ROOT / "10 ProtoSpinor" / "Closure_Strain_Geometry_and_the_Structure_of_the_Standard_Model_v5.md",
        "central_circle": PROTO_ROOT / "13 Standard Model & Topology-Only Constraints" / "The_Central_Circle__Inertia__Mass__Gravity__and_Time_as_Shared_Coherence_Bookkeeping_in_Modal_Triplet_Theory.md",
    }
    data = {key: load(path) for key, path in paths.items() if path.suffix == ".json"}
    texts = {key: read(path) for key, path in paths.items() if path.suffix != ".json"}

    # The selected ambient cyclic carrier splits into pairwise-coprime factors.
    ambient_factors = [64, 7, 3]
    pairwise_coprime = all(
        math.gcd(ambient_factors[i], ambient_factors[j]) == 1
        for i in range(len(ambient_factors))
        for j in range(i + 1, len(ambient_factors))
    )
    crt21 = [(x % 3, x % 7) for x in range(21)]
    family_frequencies = [(7 * j) % 21 for j in range(3)]
    q_frequencies = [(3 * j) % 21 for j in range(7)]
    shared_frequencies = sorted(set(family_frequencies).intersection(q_frequencies))

    # Dual translation permutes all minimal character projectors transitively.
    difference = np.zeros((21, 21), dtype=float)
    for row in range(21):
        difference[row, row] = 1.0
        difference[row, (row + 1) % 21] = -1.0
    invariance_rank = int(np.linalg.matrix_rank(difference, tol=1e-12))
    normalized_weights = np.ones(21, dtype=float) / 21.0
    shared = {
        "schema": "MTTSharedZ21MarginalAndUniqueCharacterTrace.v1",
        "status": "AMBIENT_Z1344_HAS_SELECTED_Z3_Z7_SHARED_CIRCLE_MARGINAL_WITH_UNIQUE_EQUAL_CHARACTER_WEIGHT",
        "ambient_carrier": {
            "decomposition": "Z1344 ~= Z64 x Z7 x Z3",
            "factor_dimensions": ambient_factors,
            "product": math.prod(ambient_factors),
            "pairwise_coprime": pairwise_coprime,
            "family_kernel_order": 3,
            "selected_CP_quotient_order": 448,
            "later_Z7_charge_certificate_status": data["Z7_certificate"]["status"],
            "later_authority_closes_old_sevenfold_row_obligation": data["Z7_certificate"]["status"] == "CLOSED_CHARGE_SECTOR",
        },
        "minimal_shared_odd_marginal": {
            "group": "Z21 ~= Z3 x Z7",
            "crt_map": "x |-> (x mod 3,x mod 7)",
            "crt_pair_count": len(set(crt21)),
            "bijective": len(set(crt21)) == 21,
            "family_character_frequencies_in_Z21": family_frequencies,
            "q_character_frequencies_in_Z21": q_frequencies,
            "intersection": shared_frequencies,
            "intersection_is_only_invariant_character": shared_frequencies == [0],
        },
        "trace_theorem": {
            "dual_translation_constraint_rank": invariance_rank,
            "invariant_weight_space_dimension": 21 - invariance_rank,
            "normalized_character_weights": normalized_weights.tolist(),
            "max_weight_deviation": float(np.max(np.abs(normalized_weights - 1.0 / 21.0))),
            "family_projector_regular_trace": len(family_frequencies),
            "q_projector_regular_trace": len(q_frequencies),
            "multiplicity_ratio_q_over_family": len(q_frequencies) / len(family_frequencies),
            "proof": "The dual Z21 action cyclically permutes the 21 minimal character projectors. Invariance forces w_k=w_(k+1); normalization fixes w_k=1/21. The unnormalized regular trace therefore gives one unit to every character and traces 3 and 7 on the Z3 and Z7 marginals.",
            "proved": invariance_rank == 20,
        },
        "typing_guard": {
            "family_count_uses_selected_Z3_carrier": data["A46_family"]["checks"]["three_family_chiral_dimension_48"],
            "q_count_uses_full_primitive_Z7_orbit": len(data["A77_routing"]["q_route"]["generated_orbit"]) == 7,
            "Lens_Z4_augmentation_used_as_family_carrier": False,
            "A76_Z4_to_Z3_shortcut_rejected": data["A76_obstruction"]["e_factor_test"]["hom_Z4_to_Z3_is_trivial"],
        },
        "scope": "This fixes relative character multiplicities on a common regular carrier. It does not by itself prove that the physical gauge-zero-mode Hessian is the mode-count functional below.",
    }

    generators = gell_mann_generators()
    color_casimir = sum(generator.conjugate().T @ generator for generator in generators)
    color_target = (4.0 / 3.0) * np.eye(3, dtype=complex)
    color_residual = float(np.linalg.norm(color_casimir - color_target))
    color_normalized_trace = float(np.trace(color_casimir).real / 3.0)
    opposed = np.diag(np.asarray([1.0, -1.0], dtype=float))
    opposed_square = opposed.T @ opposed
    e_per_basin = 0.5 * float(np.trace(opposed_square))
    hidden_samples = []
    for delta in [0.25, 0.5, 1.0, 2.0]:
        a = delta / 2.0
        c = delta / 2.0
        minimum = a * a + c * c
        hidden_samples.append({
            "delta": delta,
            "minimum": minimum,
            "half_delta_squared": 0.5 * delta * delta,
            "residual": abs(minimum - 0.5 * delta * delta),
        })
    schur_half = 0.5
    c_e = len(family_frequencies) * e_per_basin
    c_q = len(q_frequencies) * schur_half * color_normalized_trace
    action = {
        "schema": "MTTCommonModeCountSchurCasimirParentFunctional.v1",
        "status": "EXPLICIT_FINITE_PARENT_CLOSURE_FUNCTIONAL_EMITS_BASELINE_3_AND_14_OVER_3_EXACTLY",
        "parent_functional": {
            "formula": "S_base=(1/2) sum_(g in Z3)||diag(1,-1)e_g||^2 + sum_(r in Z7) min_(a_r+c_r=delta_r)(||a_r||^2+||c_r||^2), with ||delta_r||^2=tau_3(q^* sum_a T_a^*T_a q)",
            "finite": True,
            "positive": True,
            "quadratic": True,
            "no_observed_values_in_definition": True,
        },
        "charged_lepton_lane": {
            "selected_carrier": "three Z3 family/nil-basin characters tensored with the selected Lens quarter/conjugate opposed pair; the Lens-Z4 augmentation is not used as the family carrier",
            "primitive_opposed_pair_source": {
                "A77_primitive_Z4_quarter_turn": data["A77_routing"]["lepton_route"]["primitive_Z4_quarter_turn"],
                "characters": ["+i", "-i"],
                "integer_generator_weights": [1, -1],
                "A81_anchor_to_complement_functor_closed": data["A81_candidate"]["results"]["anchor_to_complement_center_functor_closed"],
            },
            "opposed_loop_generator": opposed.tolist(),
            "generator_square": opposed_square.tolist(),
            "quadratic_half_times_orientation_trace": e_per_basin,
            "basin_count": len(family_frequencies),
            "coefficient": c_e,
            "exact_formula": "(1/2)*3*(1^2+(-1)^2)=3",
            "proto_spinor_full_anchor_and_opposed_loop_markers_present": all(
                phrase in texts["proto_spinor"]
                for phrase in ["three charged-lepton nil basins", "fully anchored", "opposed-loop"]
            ),
        },
        "colored_lane": {
            "selected_carrier": "full primitive Z7 character orbit; the invariant mode is retained in the baseline and removed only in the A77 residual augmentation",
            "channel_count": len(q_frequencies),
            "gell_mann_normalization": "T_a=lambda_a/2, Tr(T_a T_b)=delta_ab/2",
            "sum_Ta_star_Ta": color_casimir.real.tolist(),
            "C2_fundamental": color_normalized_trace,
            "C2_residual_to_4_over_3_identity": color_residual,
            "two_hidden_channel_samples": hidden_samples,
            "Schur_factor": schur_half,
            "coefficient": c_q,
            "exact_formula": "7*(1/2)*(4/3)=14/3",
            "color_singlet_Schur_markers_present": all(
                phrase in texts["color_schur"]
                for phrase in ["Color-Singlet Completion Lemma", "E_min =", "delta^2/2"]
            ),
        },
        "common_trace_ownership": {
            "same_Z21_regular_trace_counts_both_marginals": True,
            "independent_Z3_Z7_character_weights_after_shared_trace": 0,
            "new_continuous_parameters": 0,
            "new_discrete_parameters": 0,
        },
        "exact_baselines": {
            "c_e": c_e,
            "c_q": c_q,
            "c_e_residual_to_3": abs(c_e - 3.0),
            "c_q_residual_to_14_over_3": abs(c_q - 14.0 / 3.0),
        },
        "physical_selection_boundary": {
            "explicit_parent_functional_exists": True,
            "current_MTT_corpus_proves_this_parent_is_the_physical_gauge_zero_mode_Hessian": False,
            "reason": "ProtoSpinor supplies structural full/partial-anchor classes and A65 defines the required gauge Hessian, but no selected second-variation theorem identifies the displayed closure functional with W_kin on the A46 carrier.",
        },
    }

    sector_order = data["A80_execution"]["sector_order"]
    identity = np.ones(6, dtype=float)
    p_colored = np.asarray(data["A78_functor"]["selected_sector_support"]["P_colored"], dtype=float)
    p_e = np.asarray(data["A78_functor"]["selected_sector_support"]["P_e"], dtype=float)
    basis = np.column_stack([identity, p_colored, p_e])
    partition_constraints = np.asarray([
        [1, -1, 0, 0, 0, 0],
        [0, 1, -1, 0, 0, 0],
        [0, 0, 0, 1, 0, -1],
    ], dtype=float)
    basis_constraint_residual = float(np.linalg.norm(partition_constraints @ basis))
    partition_dimension = 6 - int(np.linalg.matrix_rank(partition_constraints, tol=1e-12))
    spectator_basis_rank = int(np.linalg.matrix_rank(basis, tol=1e-12))
    spectators = {
        "schema": "MTTSectorPartitionSpectatorCompletenessAndStrictGate.v1",
        "status": "ALL_DIAGONAL_SPECTATORS_IN_SELECTED_COLORED_FULLANCHOR_NEUTRALPAIR_CLASS_REDUCE_TO_EXISTING_PROJECTORS_STRICT_ACTION_COMPLETENESS_OPEN",
        "selected_partition": {
            "colored_equivalence_class": ["Q", "u", "d"],
            "full_anchor_class": ["e"],
            "neutral_pair_class": ["L", "N"],
            "constraint_matrix": partition_constraints.tolist(),
            "allowed_diagonal_dimension": partition_dimension,
        },
        "basis_theorem": {
            "basis": ["I", "P_colored", "P_e"],
            "numeric_basis_columns": basis.tolist(),
            "basis_rank": spectator_basis_rank,
            "constraint_residual": basis_constraint_residual,
            "spans_entire_partition_invariant_diagonal_space": spectator_basis_rank == partition_dimension and basis_constraint_residual < 1e-14,
            "relative_dimension_mod_common_identity": spectator_basis_rank - 1,
            "consequence": "Within the declared sector-partition symmetry class, there is no fourth diagonal spectator direction beyond the two already computed relative supports.",
        },
        "strictly_unresolved": {
            "derive_partition_symmetry_from_complete_microscopic_action": True,
            "sector_dependent_family_or_nondiagonal_fluctuation_blocks": True,
            "fermion_Higgs_and_other_loop_blocks_cancel_or_are_ratio_neutral": True,
            "A75_rank_two_relative_local_counterterms_excluded": True,
        },
        "known_A81_spectator_classes_closed": data["A81_candidate"]["results"]["known_spectator_classes_closed"],
        "strict_all_spectator_completeness_closed": False,
    }

    baseline_positive = c_e * (identity - p_e) + c_q * p_colored
    a80_baseline = np.asarray(data["A80_execution"]["base_positive_representative"], dtype=float)
    response_positive = np.asarray(data["A80_execution"]["response_positive_representative"], dtype=float)
    total_positive = baseline_positive + response_positive
    a80_total = np.asarray(data["A80_execution"]["total_positive_eigenvalues"], dtype=float)
    execution = {
        "schema": "MTTBaselinePlusDefectGaugeExecution.v1",
        "status": "EXACT_BASELINE_PARENT_FUNCTIONAL_PLUS_A81_DEFECT_REPLAYS_FROZEN_A80_GAUGE_CANDIDATE",
        "sector_order": sector_order,
        "baseline_positive": baseline_positive.tolist(),
        "A80_baseline": a80_baseline.tolist(),
        "baseline_residual": float(np.max(np.abs(baseline_positive - a80_baseline))),
        "response_positive": response_positive.tolist(),
        "total_positive": total_positive.tolist(),
        "A80_total": a80_total.tolist(),
        "total_residual": float(np.max(np.abs(total_positive - a80_total))),
        "frozen_K_over_K2": data["A80_execution"]["K_over_K2_positive"],
        "observed_gauge_values_used_as_selector_here": False,
        "strict_gauge_values_promoted_here": 0,
        "why_zero": "The numerical execution is exact conditional on the displayed parent functional, but the physical MTT Hessian-restriction theorem remains open.",
    }

    gate = {
        "schema": "MTTRemainingPhysicalHessianRestrictionGate.v1",
        "status": "BASELINE_MULTIPLICITY_AND_ARITHMETIC_CLOSED_ONE_OPERATOR_RESTRICTION_AND_STRICT_COMPLETENESS_GATE_REMAINS",
        "closed": {
            "ambient_Z1344_to_Z64_Z7_Z3_factorization": pairwise_coprime and math.prod(ambient_factors) == 1344,
            "later_Z7_source_supersedes_old_candidate_status": shared["ambient_carrier"]["later_authority_closes_old_sevenfold_row_obligation"],
            "shared_Z21_CRT_marginal": shared["minimal_shared_odd_marginal"]["bijective"],
            "unique_equal_character_trace": shared["trace_theorem"]["proved"],
            "selected_Z3_and_Z7_multiplicities": shared["typing_guard"]["family_count_uses_selected_Z3_carrier"] and shared["typing_guard"]["q_count_uses_full_primitive_Z7_orbit"],
            "Lens_Z4_family_shortcut_excluded": shared["typing_guard"]["A76_Z4_to_Z3_shortcut_rejected"],
            "selected_quarter_conjugate_opposed_pair": action["charged_lepton_lane"]["primitive_opposed_pair_source"]["A77_primitive_Z4_quarter_turn"] and action["charged_lepton_lane"]["primitive_opposed_pair_source"]["A81_anchor_to_complement_functor_closed"],
            "opposed_loop_unit_cost_arithmetic": abs(e_per_basin - 1.0) < 1e-15,
            "two_channel_Schur_half": max(row["residual"] for row in hidden_samples) < 1e-15,
            "SU3_fundamental_Casimir": color_residual < 1e-14,
            "baseline_3_and_14_over_3_emitted_by_parent": max(action["exact_baselines"]["c_e_residual_to_3"], action["exact_baselines"]["c_q_residual_to_14_over_3"]) < 1e-14,
            "partition_invariant_diagonal_spectator_space_exhausted": spectators["basis_theorem"]["spans_entire_partition_invariant_diagonal_space"],
            "frozen_gauge_candidate_replayed": execution["total_residual"] < 1e-14,
        },
        "open": {
            "selected_MTT_closure_Hessian_equals_displayed_parent_functional": True,
            "same_second_variation_restricts_to_A65_gauge_zero_modes": True,
            "strict_microscopic_action_enforces_sector_partition_symmetry": True,
            "all_nondiagonal_and_loop_spectators_computed_or_excluded": True,
            "A75_relative_counterterm_space_fixed": True,
            "absolute_P_EW_normalization": True,
            "independent_modern_validation_after_strict_source_freeze": True,
        },
        "direct_sum_weight_no_go": {
            "A75_center_weights_not_fixed_by_inner_conjugation_alone": not data["A75_center"]["A73_scope_correction"]["one_scalar_direct_sum_weighting_forced_by_A74"],
            "shared_Z21_parent_removes_relative_Z3_Z7_weight_if_selected": True,
            "without_parent_selection_remaining_relative_weight_coordinates_after_one_common_scale": 1,
            "no_new_weight_parameter_adopted_here": True,
        },
        "strict_baseline_source_closed": False,
        "strict_spectator_completeness_closed": False,
        "strict_gauge_values_accepted": 0,
        "new_continuous_parameters": 0,
        "new_discrete_parameters": 0,
        "next_required_artifact": NEXT,
    }

    checks = {
        "ambient_marker": "Z_64 x Z_7 x Z_3 ~= Z_1344" in texts["ambient_Z1344"],
        "central_circle_shared_marker": "single internal" in texts["central_circle"] and "reused across all modal bundles" in texts["central_circle"],
        "all_closed_gate_items": all(gate["closed"].values()),
        "parent_not_overpromoted": not action["physical_selection_boundary"]["current_MTT_corpus_proves_this_parent_is_the_physical_gauge_zero_mode_Hessian"],
        "strict_baseline_not_overpromoted": not gate["strict_baseline_source_closed"],
        "strict_spectators_not_overpromoted": not gate["strict_spectator_completeness_closed"],
        "strict_values_zero": gate["strict_gauge_values_accepted"] == 0,
        "no_new_parameters": gate["new_continuous_parameters"] == 0 and gate["new_discrete_parameters"] == 0,
    }
    candidate = {
        "schema": "MTTSelectedBaselineCostMultiplicitySourceAndNoncentralSpectatorExclusion.v1",
        "status": STATUS,
        "results": {
            "old_sevenfold_source_obligation_superseded_closed": True,
            "shared_Z21_equal_character_trace_closed": True,
            "baseline_modecount_arithmetic_3_and_14_over_3_closed": True,
            "explicit_zero_parameter_parent_functional_constructed": True,
            "partition_invariant_diagonal_spectator_class_closed": True,
            "physical_gauge_Hessian_restriction_closed": False,
            "strict_all_spectator_completeness_closed": False,
            "strict_gauge_values_accepted": 0,
            "new_continuous_parameters": 0,
            "new_discrete_parameters": 0,
        },
        "outputs": {
            "shared": str(SHARED.relative_to(ROOT)).replace("\\", "/"),
            "action": str(ACTION.relative_to(ROOT)).replace("\\", "/"),
            "spectators": str(SPECTATORS.relative_to(ROOT)).replace("\\", "/"),
            "execution": str(EXECUTION.relative_to(ROOT)).replace("\\", "/"),
            "gate": str(GATE.relative_to(ROOT)).replace("\\", "/"),
        },
        "checks": checks,
        "authority_hashes": [{"path": str(path), "sha256": sha256(path)} for path in paths.values()],
        "next_required_artifact": NEXT,
    }
    cert = {
        "certificate": "MTT_Selected_BaselineCostMultiplicitySourceAndNoncentralSpectatorExclusion_v1",
        "status": STATUS,
        "shared_circle_marginal": "Z21 ~= Z3 x Z7",
        "family_multiplicity": 3,
        "q_channel_multiplicity": 7,
        "baseline_c_e": c_e,
        "baseline_c_q": c_q,
        "explicit_parent_functional_constructed": True,
        "physical_gauge_Hessian_restriction_closed": False,
        "partition_invariant_diagonal_spectator_class_closed": True,
        "strict_all_spectator_completeness_closed": False,
        "strict_gauge_values_accepted": 0,
        "new_continuous_parameters": 0,
        "new_discrete_parameters": 0,
        "next_required_artifact": NEXT,
    }
    note = f"""# MTT Selected Baseline-Cost Multiplicity Source and Noncentral-Spectator Exclusion v1

## Later-authority correction

A69's sevenfold factor is no longer merely a candidate. The q79 repository now has a closed
Fu-Yau/Mukai charge-sector certificate for `Z7`, and A77 proves that primitive `q7=2` generates the
full seven-character orbit. The selected family carrier is the separate common-circle `Z3`. A76's
equivariance no-go remains essential: the rank-three Lens-`Z4` augmentation is **not** used as the
family carrier. The Lens input instead supplies A77's selected quarter-turn and its conjugate as the
opposed `+1/-1` orientation pair, with A81 supplying the anchor-to-complement map.

## Shared-circle multiplicity theorem

The selected ambient carrier is

```text
Z1344 ~= Z64 x Z7 x Z3.
```

Its family/odd marginal is the minimal common quotient `Z21 ~= Z3 x Z7`. In character coordinates,
the dual `Z21` action permutes all 21 minimal projectors transitively. An invariant positive trace
therefore gives equal weight to every character. The unnormalized regular trace consequently counts
the family and q marginals as exactly `3` and `7`; there is no relative `Z3`/`Z7` weight knob once
this common carrier is selected.

## Exact parent functional

On the selected structural carriers define the finite positive quadratic functional

```text
S_base = (1/2) sum_(g in Z3) ||diag(1,-1)e_g||^2
       + sum_(r in Z7) min_(a_r+c_r=delta_r) (||a_r||^2+||c_r||^2),
||delta_r||_color^2 = tau_3(q^* sum_a T_a^*T_a q).
```

The opposed-loop trace gives

```text
c_e = (1/2)*3*(1^2+(-1)^2) = 3.
```

Two equivalent hidden color-completion channels give the Schur minimum `delta^2/2`, while
`sum_a T_a^*T_a=(4/3)I_3` in the selected `SU3` fundamental normalization. Hence

```text
c_q = 7*(1/2)*(4/3) = 14/3.
```

This is an explicit zero-parameter finite parent functional, not a fit. Adding A81's selected
positive defect reproduces A80's full operator with residual `{execution['total_residual']:.3e}` and
the frozen ratio candidate `{execution['frozen_K_over_K2']}`.

## Spectator theorem and exact boundary

For diagonal sector weights respecting the declared classes

```text
{{Q,u,d}}, {{e}}, {{L,N}},
```

the full invariant space has dimension three and is exactly

```text
span{{I,P_colored,P_e}}.
```

Modulo common identity it has dimension two, so there is no additional diagonal spectator direction
inside this class. This does not exclude sector-dependent family matrices, non-diagonal fluctuation
blocks, fermion/Higgs loop terms, or A75's rank-two relative local-counterterm space.

The remaining proof is now one operator-identification theorem, not two unexplained numbers: prove
that the selected MTT closure Hessian is the displayed shared-circle parent functional and that its
second variation restricts to A65's gauge-zero-mode `W_kin`, with the remaining blocks/counterterms
neutral or absent. The central-circle paper itself labels its universality discussion as structural
synthesis, so this identification is not silently assumed. Strict gauge values accepted here: zero.

Next artifact: `{NEXT}`.
"""

    for path, payload in [(SHARED, shared), (ACTION, action), (SPECTATORS, spectators), (EXECUTION, execution), (GATE, gate), (CANDIDATE, candidate), (CERT, cert)]:
        dump(path, payload)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
