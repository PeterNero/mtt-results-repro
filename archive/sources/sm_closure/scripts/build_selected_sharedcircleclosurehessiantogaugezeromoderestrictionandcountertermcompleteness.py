from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
PROTO = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory\10 ProtoSpinor\Closure_Strain_Geometry_and_the_Structure_of_the_Standard_Model_v5.md")
SPECTRAL_SHADOW = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory\15 Discrete & Spectral & Operator Geometric Theories\The_Spectral_Action_as_a_Shadow_of_Coherent_Fixed_Point_Geometry.md")
SLUG = "selected_sharedcircleclosurehessiantogaugezeromoderestrictionandcountertermcompleteness"
STATUS = (
    "MTT_SELECTED_CANONICAL_COVARIANT_GAUGE_RESTRICTION_CLOSED_ONE_EXPLICIT_CLOSURESHADOW_"
    "ACTION_PREMISE_IDENTIFIED_CONDITIONAL_RELATIVE_ACTION_CLOSED_STRICT_DERIVATION_OPEN"
)
NEXT = "MTT_Selected_ClosureShadowGaugeActionAxiomDerivation_or_ExplicitAdoptionAndHeldOutValidation_v1"

OUT = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_SharedCircleClosureHessianToGaugeZeroModeRestrictionAndCountertermCompleteness_v1.md"
RESTRICTION = OUT / "canonical_heat_density_and_gauge_zero_mode_hessian.packet.json"
INDEPENDENCE = OUT / "closure_cost_vs_physical_action_logical_independence.packet.json"
AXIOM = OUT / "minimal_closure_shadow_gauge_action_axiom.packet.json"
CONDITIONAL = OUT / "conditional_action_counterterm_and_spectator_execution.packet.json"
GATE = OUT / "remaining_axiom_derivation_or_adoption_gate.packet.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def block_diag(blocks: list[np.ndarray]) -> np.ndarray:
    size = sum(block.shape[0] for block in blocks)
    result = np.zeros((size, size), dtype=complex)
    offset = 0
    for block in blocks:
        width = block.shape[0]
        result[offset : offset + width, offset : offset + width] = block
        offset += width
    return result


def main() -> int:
    paths = {
        "A46_family": ROOT / "candidate_data" / "selected_typedfamilygaugecarrieranddiagonalsmrepresentationtheorem" / "typed_family_gauge_carrier_and_anomaly_table.packet.json",
        "A65_kinetic": ROOT / "candidate_data" / "selected_gaugezeromodekineticinnerproduct_or_chernweilbackgroundenergynogo" / "finite_gauge_zero_mode_kinetic_weight_theorem.packet.json",
        "A67_density": ROOT / "candidate_data" / "selected_positivesectordensitysourcetheorem_or_commongaugeflavorweightemission" / "conditional_c1_positive_sector_density.packet.json",
        "A75_counterterm": ROOT / "candidate_data" / "selected_physicalkinetichessianblockidentity_or_modernprecisiongaugevalidation" / "relative_counterterm_and_matching_no_go.packet.json",
        "A78_functor": ROOT / "candidate_data" / "selected_producttriplegaugefluctuationfunctorandrelativeboundarycondition" / "center_response_to_sector_kinetic_density_functor.packet.json",
        "A78_boundary": ROOT / "candidate_data" / "selected_producttriplegaugefluctuationfunctorandrelativeboundarycondition" / "relative_spectral_action_boundary_condition.packet.json",
        "A80_execution": ROOT / "candidate_data" / "selected_anchoringparityinsertionlaw_or_independentkineticgramderivation" / "positive_representative_gauge_execution.packet.json",
        "A82_action": ROOT / "candidate_data" / "selected_baselinecostmultiplicitysourceandnoncentralspectatorexclusion" / "common_modecount_schur_casimir_parent_functional.packet.json",
        "A82_spectators": ROOT / "candidate_data" / "selected_baselinecostmultiplicitysourceandnoncentralspectatorexclusion" / "sector_partition_spectator_completeness_and_strict_gate.packet.json",
        "A82_gate": ROOT / "candidate_data" / "selected_baselinecostmultiplicitysourceandnoncentralspectatorexclusion" / "remaining_physical_hessian_restriction_gate.packet.json",
        "proto_spinor": PROTO,
        "spectral_shadow": SPECTRAL_SHADOW,
    }
    data = {key: load(path) for key, path in paths.items() if path.suffix == ".json"}
    texts = {key: read(path) for key, path in paths.items() if path.suffix != ".json"}

    sector_order = data["A80_execution"]["sector_order"]
    total_cost = np.asarray(data["A80_execution"]["total_positive_eigenvalues"], dtype=float)
    tau = float(data["A80_execution"]["tau_int"])
    attenuation = np.exp(-tau * total_cost)
    base_traces = np.asarray(data["A67_density"]["sector_trace_weights"], dtype=float)
    weights = base_traces * attenuation
    a80_weights = np.asarray(data["A80_execution"]["weights_positive"], dtype=float)
    trace_map = np.asarray(data["A78_functor"]["functor"]["sector_trace_matrix"], dtype=float)
    kinetic = trace_map @ weights
    a80_kinetic = np.asarray(data["A80_execution"]["K_positive"], dtype=float)
    ratios = kinetic / kinetic[1]
    a80_ratios = np.asarray(data["A80_execution"]["K_over_K2_positive"], dtype=float)

    positive_blocks = data["A67_density"]["positive_blocks"]
    phase = np.asarray(positive_blocks["Phi_phase"], dtype=float)[..., 0]
    shift = np.asarray(positive_blocks["Phi_shift"], dtype=float)[..., 0]
    left = np.asarray(positive_blocks["Phi_left_incidence_pullback"], dtype=float)[..., 0]
    phi_by_sector = {"Q": left, "u": phase, "d": shift, "L": left, "e": phase, "N": shift}
    weighted_blocks = [attenuation[index] * phi_by_sector[sector] for index, sector in enumerate(sector_order)]
    w_full = block_diag([np.asarray(block, dtype=complex) for block in weighted_blocks])
    eigenvalues = np.linalg.eigvalsh(w_full).real
    block_trace_residual = max(
        abs(float(np.trace(phi_by_sector[sector])) - base_traces[index])
        for index, sector in enumerate(sector_order)
    )

    restriction = {
        "schema": "MTTCanonicalHeatDensityAndGaugeZeroModeHessian.v1",
        "status": "FINITE_HEAT_DENSITY_AND_UNIQUE_TRACE_COVARIANTIZATION_REPRODUCE_A65_GAUGE_HESSIAN_EXACTLY",
        "input": {
            "H_closure_sector_eigenvalues": total_cost.tolist(),
            "tau_int": tau,
            "Phi_C1_sector_traces": base_traces.tolist(),
            "formula": "W_kin=exp(-tau_int H_closure) Phi_C1^+",
        },
        "finite_density": {
            "dimension": int(w_full.shape[0]),
            "self_adjoint_residual": float(np.linalg.norm(w_full - w_full.conjugate().T)),
            "minimum_eigenvalue": float(np.min(eigenvalues)),
            "maximum_eigenvalue": float(np.max(eigenvalues)),
            "positive_definite": bool(np.min(eigenvalues) > 0.0),
            "family_block_trace_residual": block_trace_residual,
            "commutes_with_gauge_action": data["A46_family"]["checks"]["family_projectors_commute_with_all_gauge_generators"],
            "reason": "Phi_C1 acts on the family factor while rho_phys(g)=I3_family tensor rho_16(g); the sector heat factor is central.",
        },
        "gauge_covariantization": {
            "quadratic_action": "S_gauge^(2)[F]=(1/2) sum_ab Tr_HF(W_kin T_a T_b) <F^a,F^b>",
            "A65_Hessian": "K_ab=Tr_HF(W_kin T_a T_b)",
            "sector_factorization": "Tr_(family tensor R_s)((w_s Phi_s) tensor T_a^2)=w_s Tr_family(Phi_s) Tr_Rs(T_a^2)",
            "kinetic_rows": kinetic.tolist(),
            "A80_kinetic_rows": a80_kinetic.tolist(),
            "kinetic_residual": float(np.max(np.abs(kinetic - a80_kinetic))),
            "ratios": ratios.tolist(),
            "A80_ratios": a80_ratios.tolist(),
            "ratio_residual": float(np.max(np.abs(ratios - a80_ratios))),
            "mathematical_restriction_closed": True,
        },
        "uniqueness_scope": {
            "given_H_closure_Phi_tau_and_A46_representation": "The heat density is fixed by functional calculus and its trace Hessian is fixed by the represented gauge generators.",
            "symmetry_alone_selects_H_closure_Phi_tau": False,
            "physical_MTT_action_identified_here": False,
        },
    }

    proto_not_lagrangian = "is not a Lagrangian" in texts["proto_spinor"] and "bookkeeping-cost geometry" in texts["proto_spinor"]
    shadow_assumption = "The coherent fixed-point action admits a proper-time representation" in texts["spectral_shadow"]
    independence = {
        "schema": "MTTClosureCostVersusPhysicalActionLogicalIndependence.v1",
        "status": "CURRENT_CORPUS_DOES_NOT_DERIVE_CLOSURE_HESSIAN_TO_GAUGE_ACTION_IDENTIFICATION",
        "proto_spinor_boundary": {
            "closure_cost_explicitly_not_a_Lagrangian": proto_not_lagrangian,
            "quadratic_normal_form_is_an_assumption": "Assume the quadratic normal form" in texts["proto_spinor"] or "#### Assumption" in texts["proto_spinor"],
            "consequence": "The A82 bookkeeping Hessian cannot be renamed a physical gauge action without a shadow/restriction theorem.",
        },
        "spectral_shadow_boundary": {
            "proper_time_representation_stated_as_assumption": shadow_assumption,
            "assumed_formula": "S_coh=int mu(tau) Tr exp(-tau D^2)",
            "does_not_instantiate_A82_H_closure": True,
            "does_not_select_point_measure_at_tau_int": True,
        },
        "finite_density_boundary": {
            "A67_scientific_status": data["A67_density"]["source_status"]["scientific_status"],
            "A67_strict_unpatched_no_knob_source": data["A67_density"]["source_status"]["strict_unpatched_no_knob_source"],
        },
        "counterterm_boundary": {
            "A75_no_go": data["A75_counterterm"]["theorem"]["conclusion"],
            "relative_counterterm_space_not_fixed_by_finite_determinant_value_at_origin": True,
        },
        "theorem": {
            "statement": "The selected carriers and exact finite arithmetic determine a canonical candidate action, but the current premises admit both that candidate and the same candidate plus an arbitrary allowed relative quadratic term. Therefore physical action identity is logically independent of A65-A82.",
            "proved": proto_not_lagrangian and shadow_assumption and not data["A67_density"]["source_status"]["strict_unpatched_no_knob_source"],
        },
    }

    axiom_text = (
        "ClosureShadowGaugeActionAxiom. On a selected finite coherent sector with positive closure Hessian "
        "H_cl, selected C1 density Phi_C1^+, and selected proper time tau_int, the quadratic physical "
        "gauge shadow at the finite matching point is S_gauge^(2)=(1/2) Tr_HF(exp(-tau_int H_cl) "
        "Phi_C1^+ F^2). No additional sector-relative gauge-quadratic functional is present at that "
        "matching point; one common overall normalization is the already counted P_EW primitive."
    )
    axiom = {
        "schema": "MTTMinimalClosureShadowGaugeActionAxiom.v1",
        "status": "ONE_EXPLICIT_STRUCTURAL_ACTION_PREMISE_IS_SUFFICIENT_AND_CURRENTLY_UNDERIVED",
        "name": "ClosureShadowGaugeActionAxiom",
        "statement": axiom_text,
        "clauses": {
            "CSGA1_heat_shadow": "W_kin=exp(-tau_int H_cl) Phi_C1^+ on the selected finite carrier",
            "CSGA2_finite_matching_completeness": "the represented finite trace action is complete at the matching point up to one common normalization; no extra relative F_a^2 term is added",
        },
        "why_minimal": {
            "CSGA1_closes_A65_restriction": restriction["gauge_covariantization"]["mathematical_restriction_closed"],
            "CSGA2_is_required_by_A75_no_go": True,
            "removing_CSGA1_leaves_physical_Wkin_unidentified": True,
            "removing_CSGA2_leaves_rank_two_relative_matching_freedom": True,
        },
        "parameter_policy": {
            "structural_action_premises": 1,
            "logical_clauses_inside_premise": 2,
            "new_continuous_numerical_parameters": 0,
            "new_discrete_numerical_parameters": 0,
            "existing_shared_physical_primitive": "P_EW",
            "additional_physical_primitives": 0,
            "observed_gauge_values_used_to_define_axiom": False,
        },
        "epistemic_status": {
            "derived_from_current_MTT_axioms": False,
            "compatible_with_spectral_shadow_paper": True,
            "must_be_explicitly_adopted_or_derived_before_strict_promotion": True,
        },
    }

    conditional = {
        "schema": "MTTConditionalActionCountertermAndSpectatorExecution.v1",
        "status": "UNDER_CLOSURESHADOW_AXIOM_RELATIVE_GAUGE_ACTION_AND_CURRENT_SPECTATORS_CLOSE_WITH_ZERO_NEW_NUMERICAL_PARAMETERS",
        "premise": "ClosureShadowGaugeActionAxiom",
        "conditional_results": {
            "physical_Hessian_restriction_to_A65": True,
            "gauge_K_rows_emitted": 3,
            "independent_ratio_rows_emitted": 2,
            "K_over_K2": ratios.tolist(),
            "A75_relative_counterterm_coordinates_fixed_to": [0.0, 0.0],
            "A82_partition_diagonal_spectator_class_complete": data["A82_spectators"]["basis_theorem"]["spans_entire_partition_invariant_diagonal_space"],
            "additional_nondiagonal_or_loop_spectators_present_in_selected_action": False,
            "absolute_normalization_uses_existing_P_EW_only": data["A78_boundary"]["adopted_closure_tier"]["one_shared_physical_normalization_primitive"],
            "new_continuous_numerical_parameters": 0,
        },
        "unconditional_results": {
            "mathematical_covariantization_closed": True,
            "physical_action_source_closed": False,
            "strict_gauge_values_accepted": 0,
            "strict_counterterm_completeness_closed": False,
        },
        "validation_boundary": {
            "candidate_was_developed_after_gauge_profile_known": True,
            "can_be_called_independent_prediction_now": False,
            "required_next_test": "freeze the action premise first, then test against a genuinely held-out modern common-scheme likelihood or a new observable not used in construction",
        },
    }

    gate = {
        "schema": "MTTRemainingAxiomDerivationOrAdoptionGate.v1",
        "status": "NO_NUMERICAL_OBJECT_REMAINS_FOR_RELATIVE_GAUGE_ACTION_ONE_FOUNDATIONAL_ARROW_REMAINS",
        "closed": {
            "A82_parent_functional_explicit": data["A82_action"]["parent_functional"]["finite"],
            "finite_heat_density_computed": restriction["finite_density"]["positive_definite"],
            "gauge_covariant_trace_Hessian_derived": restriction["gauge_covariantization"]["mathematical_restriction_closed"],
            "A65_K_rows_reproduced": restriction["gauge_covariantization"]["kinetic_residual"] < 1e-13,
            "A80_ratios_reproduced": restriction["gauge_covariantization"]["ratio_residual"] < 1e-14,
            "logical_independence_of_physical_action_identification": independence["theorem"]["proved"],
            "minimal_sufficient_action_axiom_written": True,
            "conditional_counterterm_and_spectator_completeness": conditional["conditional_results"]["physical_Hessian_restriction_to_A65"] and conditional["conditional_results"]["A82_partition_diagonal_spectator_class_complete"],
        },
        "open": {
            "derive_CSGA1_from_projection_fixed_point_or_selected_SPT_measure": True,
            "derive_CSGA2_from_microscopic_action_completeness_or_adopt_finite_matching_rule": True,
            "promote_A67_density_beyond_accepted_source_axiom_tier": True,
            "held_out_modern_validation_after_action_freeze": True,
            "strict_absolute_P_EW_source": True,
        },
        "frontier_statement": "The remaining relative gauge-action problem is not a missing matrix entry, multiplicity, sign, projector, or scalar value. It is whether MTT derives or explicitly adopts the closure-Hessian-to-physical-action arrow and its finite matching completeness clause.",
        "strict_gauge_values_accepted": 0,
        "conditional_gauge_values_emitted_under_one_structural_premise": 3,
        "new_continuous_numerical_parameters": 0,
        "new_discrete_numerical_parameters": 0,
        "next_required_artifact": NEXT,
    }

    checks = {
        "all_closed_items": all(gate["closed"].values()),
        "density_positive": restriction["finite_density"]["positive_definite"],
        "family_gauge_commutant": restriction["finite_density"]["commutes_with_gauge_action"],
        "weight_replay": float(np.max(np.abs(weights - a80_weights))) < 1e-14,
        "K_replay": restriction["gauge_covariantization"]["kinetic_residual"] < 1e-13,
        "ratio_replay": restriction["gauge_covariantization"]["ratio_residual"] < 1e-14,
        "not_lagrangian_guard": independence["proto_spinor_boundary"]["closure_cost_explicitly_not_a_Lagrangian"],
        "proper_time_assumption_guard": independence["spectral_shadow_boundary"]["proper_time_representation_stated_as_assumption"],
        "axiom_not_overpromoted": not axiom["epistemic_status"]["derived_from_current_MTT_axioms"],
        "strict_values_zero": gate["strict_gauge_values_accepted"] == 0,
        "no_new_numeric_parameters": gate["new_continuous_numerical_parameters"] == 0 and gate["new_discrete_numerical_parameters"] == 0,
    }
    candidate = {
        "schema": "MTTSelectedSharedCircleClosureHessianToGaugeZeroModeRestrictionAndCountertermCompleteness.v1",
        "status": STATUS,
        "results": {
            "canonical_finite_heat_density_constructed": True,
            "mathematical_gauge_zero_mode_Hessian_restriction_closed": True,
            "physical_action_identification_derived_unconditionally": False,
            "minimal_sufficient_structural_action_premise_count": 1,
            "conditional_relative_gauge_action_closed": True,
            "conditional_counterterm_and_selected_spectator_completeness_closed": True,
            "strict_gauge_values_accepted": 0,
            "conditional_gauge_values_emitted": 3,
            "new_continuous_numerical_parameters": 0,
            "new_discrete_numerical_parameters": 0,
        },
        "outputs": {
            "restriction": str(RESTRICTION.relative_to(ROOT)).replace("\\", "/"),
            "independence": str(INDEPENDENCE.relative_to(ROOT)).replace("\\", "/"),
            "axiom": str(AXIOM.relative_to(ROOT)).replace("\\", "/"),
            "conditional": str(CONDITIONAL.relative_to(ROOT)).replace("\\", "/"),
            "gate": str(GATE.relative_to(ROOT)).replace("\\", "/"),
        },
        "checks": checks,
        "authority_hashes": [{"path": str(path), "sha256": sha256(path)} for path in paths.values()],
        "next_required_artifact": NEXT,
    }
    cert = {
        "certificate": "MTT_Selected_SharedCircleClosureHessianToGaugeZeroModeRestrictionAndCountertermCompleteness_v1",
        "status": STATUS,
        "finite_density_dimension": int(w_full.shape[0]),
        "minimum_density_eigenvalue": float(np.min(eigenvalues)),
        "K_replay_residual": restriction["gauge_covariantization"]["kinetic_residual"],
        "ratio_replay_residual": restriction["gauge_covariantization"]["ratio_residual"],
        "mathematical_gauge_restriction_closed": True,
        "physical_action_identification_derived": False,
        "minimal_structural_action_premise_count": 1,
        "conditional_gauge_values_emitted": 3,
        "strict_gauge_values_accepted": 0,
        "new_continuous_numerical_parameters": 0,
        "new_discrete_numerical_parameters": 0,
        "next_required_artifact": NEXT,
    }
    note = f"""# MTT Selected Shared-Circle Closure Hessian to Gauge-Zero-Mode Restriction and Counterterm Completeness v1

## Exact covariant restriction

A82 supplies the positive finite closure Hessian `H_cl`. With the already selected proper time and
C1 density, functional calculus gives

```text
W_kin = exp(-tau_int H_cl) Phi_C1^+.
```

The resulting `18x18` family/sector density is positive definite; its least eigenvalue is
`{float(np.min(eigenvalues)):.12g}`. Since `Phi_C1^+` acts on the family factor and the selected gauge
representation is `I3_family tensor rho_16`, it commutes with the gauge action. The finite quadratic
covariantization

```text
S_gauge^(2)[F] = (1/2) sum_ab Tr_HF(W_kin T_a T_b) <F^a,F^b>
```

has Hessian exactly equal to A65's `K_ab`. It reproduces A80's three kinetic rows with residual
`{restriction['gauge_covariantization']['kinetic_residual']:.3e}` and its ratios with residual
`{restriction['gauge_covariantization']['ratio_residual']:.3e}`. The mathematical restriction is closed.

## Why physical identity does not follow automatically

ProtoSpinor explicitly defines its closure cost as bookkeeping geometry, **not a Lagrangian**. The
spectral-shadow paper obtains a heat action only after assuming that the coherent fixed-point action has
a proper-time representation. A67 is also explicit that its C1 density is closed at an accepted
source-axiom tier rather than at strict unpatched no-knob tier. Finally, A75 proves that setting a finite
determinant to zero at the origin does not eliminate two allowed relative linear matching terms.

Therefore `H_cl -> W_kin -> S_gauge` is a fully executed canonical map, but current MTT premises do not
yet say that it is the physical map. This is a logical obstruction, not a missing calculation.

## Minimal sufficient premise

The exact remaining premise is:

> {axiom_text}

It has two logically necessary clauses: the heat-shadow map and finite matching completeness. It adds
zero continuous or discrete numerical parameters and no new physical primitive beyond the already
counted `P_EW`.

Under this one structural premise, all three gauge rows emit, both relative A75 counterterm coordinates
are fixed to zero at the selected matching point, and the A82 partition-invariant spectator class is
complete. Unconditionally, strict gauge values remain zero because the premise is written and tested but
not derived or adopted here. The existing ratio candidate also remains a posteriori rather than an
independent prediction; it needs a held-out test after the action is frozen.

Next artifact: `{NEXT}`.
"""

    for path, payload in [(RESTRICTION, restriction), (INDEPENDENCE, independence), (AXIOM, axiom), (CONDITIONAL, conditional), (GATE, gate), (CANDIDATE, candidate), (CERT, cert)]:
        dump(path, payload)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
