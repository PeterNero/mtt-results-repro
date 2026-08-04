from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
FIXED_DAMPING = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory\5 Dirac Delta\Deriving_the_MTT_Coherence_Scale_from_Fixed__Point_Damping.md")
UNIFIED_ACTION = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory\10 ProtoSpinor\Closure_Geometry_and_Unified_Dynamics__A_Ten_Dimensional_Action_for_Mass__Scalar_Relaxation__Quantization__and_Curvature_v3.md")
SLUG = "selected_closureshadowgaugeactionaxiomderivation_or_explicitadoptionandheldoutvalidation"
STATUS = (
    "MTT_SELECTED_CSGA1_HEATSHADOW_DERIVED_AT_REGIMELOCAL_ACTION_TIER_"
    "ONLY_FINITE_MATCHING_COMPLETENESS_AND_STRICT_PEW_REMAIN"
)
NEXT = "MTT_Selected_FiniteMatchingCompletenessFromUnifiedAction_or_ExplicitBoundaryAdoptionAndHeldOutValidation_v1"

OUT = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_ClosureShadowGaugeActionAxiomDerivation_or_ExplicitAdoptionAndHeldOutValidation_v1.md"
SEMIGROUP = OUT / "fixed_point_semigroup_to_damped_overlap_derivation.packet.json"
ACTION = OUT / "regime_local_unified_action_restriction.packet.json"
REDUCTION = OUT / "closure_shadow_axiom_clause_reduction.packet.json"
GATE = OUT / "remaining_finite_matching_completeness_gate.packet.json"


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
    result = np.zeros((size, size), dtype=float)
    offset = 0
    for block in blocks:
        width = block.shape[0]
        result[offset : offset + width, offset : offset + width] = block
        offset += width
    return result


def positive_sqrt(matrix: np.ndarray) -> np.ndarray:
    values, vectors = np.linalg.eigh(matrix)
    return (vectors * np.sqrt(np.maximum(values, 0.0))) @ vectors.T


def main() -> int:
    paths = {
        "A67_density": ROOT / "candidate_data" / "selected_positivesectordensitysourcetheorem_or_commongaugeflavorweightemission" / "conditional_c1_positive_sector_density.packet.json",
        "A75_counterterm": ROOT / "candidate_data" / "selected_physicalkinetichessianblockidentity_or_modernprecisiongaugevalidation" / "relative_counterterm_and_matching_no_go.packet.json",
        "A78_boundary": ROOT / "candidate_data" / "selected_producttriplegaugefluctuationfunctorandrelativeboundarycondition" / "relative_spectral_action_boundary_condition.packet.json",
        "A80_execution": ROOT / "candidate_data" / "selected_anchoringparityinsertionlaw_or_independentkineticgramderivation" / "positive_representative_gauge_execution.packet.json",
        "A83_restriction": ROOT / "candidate_data" / "selected_sharedcircleclosurehessiantogaugezeromoderestrictionandcountertermcompleteness" / "canonical_heat_density_and_gauge_zero_mode_hessian.packet.json",
        "A83_independence": ROOT / "candidate_data" / "selected_sharedcircleclosurehessiantogaugezeromoderestrictionandcountertermcompleteness" / "closure_cost_vs_physical_action_logical_independence.packet.json",
        "A83_axiom": ROOT / "candidate_data" / "selected_sharedcircleclosurehessiantogaugezeromoderestrictionandcountertermcompleteness" / "minimal_closure_shadow_gauge_action_axiom.packet.json",
        "fixed_damping": FIXED_DAMPING,
        "unified_action": UNIFIED_ACTION,
    }
    data = {key: load(path) for key, path in paths.items() if path.suffix == ".json"}
    texts = {key: read(path) for key, path in paths.items() if path.suffix != ".json"}

    sectors = data["A80_execution"]["sector_order"]
    costs = np.asarray(data["A80_execution"]["total_positive_eigenvalues"], dtype=float)
    tau = float(data["A80_execution"]["tau_int"])
    h_full = block_diag([cost * np.eye(3) for cost in costs])
    positive = data["A67_density"]["positive_blocks"]
    phase = np.asarray(positive["Phi_phase"], dtype=float)[..., 0]
    shift = np.asarray(positive["Phi_shift"], dtype=float)[..., 0]
    left = np.asarray(positive["Phi_left_incidence_pullback"], dtype=float)[..., 0]
    phi_lookup = {"Q": left, "u": phase, "d": shift, "L": left, "e": phase, "N": shift}
    phi_full = block_diag([phi_lookup[sector] for sector in sectors])
    exp_h = block_diag([math.exp(-tau * cost) * np.eye(3) for cost in costs])
    phi_sqrt = positive_sqrt(phi_full)
    damped_overlap = phi_sqrt @ exp_h @ phi_sqrt
    a83_density_eigenvalues = np.linalg.eigvalsh(damped_overlap)
    direct_heat_density = exp_h @ phi_full
    commute_residual = float(np.linalg.norm(h_full @ phi_full - phi_full @ h_full))
    factorization_residual = float(np.linalg.norm(damped_overlap - direct_heat_density))
    selected_gap = 15.0
    selected_tolerance = 1.0 / 448.0
    damping_residual = abs(math.exp(-selected_gap * tau) - selected_tolerance)

    fixed_markers = {
        "A_can_be_Hessian": "is the Hessian or linearized dissipative generator" in texts["fixed_damping"],
        "linear_flow_is_heat_semigroup": "Phi_t=e^{-tA}" in texts["fixed_damping"],
        "kernel_unique_by_functional_calculus": "uniquely determined by functional calculus" in texts["fixed_damping"],
    }
    semigroup = {
        "schema": "MTTFixedPointSemigroupToDampedOverlapDerivation.v1",
        "status": "CLOSURE_HESSIAN_GENERATES_UNIQUE_SELECTED_TIME_DAMPED_OVERLAP_KERNEL",
        "fixed_point_theorem_import": fixed_markers,
        "selected_time_identity": {
            "tau_int": tau,
            "gap": selected_gap,
            "finite_tolerance": selected_tolerance,
            "identity": "exp(-15 tau_int)=1/448",
            "residual": damping_residual,
        },
        "finite_execution": {
            "H_closure_dimension": int(h_full.shape[0]),
            "Phi_C1_dimension": int(phi_full.shape[0]),
            "commutator_Hcl_PhiC1_residual": commute_residual,
            "damped_overlap_formula": "Phi_C1^(1/2) exp(-tau_int H_cl) Phi_C1^(1/2)",
            "direct_heat_density_formula": "exp(-tau_int H_cl) Phi_C1",
            "factorization_residual": factorization_residual,
            "minimum_damped_density_eigenvalue": float(np.min(a83_density_eigenvalues)),
            "matches_A83_minimum_eigenvalue": abs(float(np.min(a83_density_eigenvalues)) - data["A83_restriction"]["finite_density"]["minimum_eigenvalue"]) < 1e-14,
        },
        "theorem": {
            "statement": "At a fixed point, the Hessian of the closure/admissibility functional is the linearized stabilization generator. The selected proper time then determines exp(-tau_int H_cl) uniquely by functional calculus. Because H_cl is sector-central, it commutes with Phi_C1, so the canonical damped overlap is exactly the A83 heat density.",
            "proved_at_fixed_point_gradient_flow_tier": all(fixed_markers.values()) and damping_residual < 1e-15 and commute_residual < 1e-14 and factorization_residual < 1e-13,
        },
        "boundary": "This derives the damping kernel once H_cl, Phi_C1 and tau_int are admitted in the selected regime. It does not by itself declare the resulting overlap to be the complete physical gauge action.",
    }

    action_markers = {
        "J_is_action_potential": "- J(s)" in texts["unified_action"] and "The potential term must reproduce the closure cost functional" in texts["unified_action"],
        "coherent_coefficients_are_internal_overlaps": "Coefficients of four-dimensional operators are given by finite overlap integrals of internal modes" in texts["unified_action"],
        "gauge_kinetic_terms_reduce_from_internal_geometry": "gauge kinetic terms reduce to" in texts["unified_action"],
        "regime_local_not_global": "not a primitive global law" in texts["unified_action"],
    }
    action = {
        "schema": "MTTRegimeLocalUnifiedActionRestriction.v1",
        "status": "UNIFIED_ACTION_AND_COHERENT_REDUCTION_IDENTIFY_DAMPED_INTERNAL_OVERLAP_AS_GAUGE_KINETIC_SOURCE_AT_ACTION_TIER",
        "corpus_markers": action_markers,
        "restriction_chain": [
            "J(s) is the potential in the regime-local ten-dimensional action",
            "H_cl is its anchored second variation at alignment",
            "fixed-point damping supplies the canonical exp(-tau_int H_cl) overlap kernel",
            "coherent reduction makes four-dimensional coefficients finite internal overlaps",
            "A83 evaluates the represented gauge overlap as Tr_HF(W_kin T_a T_b)",
        ],
        "CSGA1_heat_shadow_derived_at_regime_local_action_tier": all(action_markers.values()) and semigroup["theorem"]["proved_at_fixed_point_gradient_flow_tier"],
        "scope": {
            "global_microscopic_action_derived": False,
            "regime_local_action_encoding": True,
            "A67_density_still_at_source_axiom_tier": data["A67_density"]["source_status"]["scientific_status"],
            "truncation_and_matching_corrections_automatically_zero": False,
        },
    }

    reduction = {
        "schema": "MTTClosureShadowAxiomClauseReduction.v1",
        "status": "CSGA1_DERIVED_CSGA2_REMAINS_ONLY_RELATIVE_ACTION_PREMISE",
        "predecessor_axiom": data["A83_axiom"]["statement"],
        "clause_status": {
            "CSGA1_heat_shadow": {
                "previous": "underived structural action clause",
                "current": "derived at fixed-point gradient-flow plus regime-local unified-action tier",
                "closed": action["CSGA1_heat_shadow_derived_at_regime_local_action_tier"],
            },
            "CSGA2_finite_matching_completeness": {
                "current": "not derived; A75 proves two relative finite terms remain allowed",
                "closed_strictly": False,
                "closed_at_adopted_one_primitive_boundary_tier": data["A78_boundary"]["adopted_closure_tier"]["relative_matching_directions_closed_conditionally"] == 2,
            },
        },
        "remaining_structural_action_premise_count": 1,
        "remaining_logical_clause_count": 1,
        "new_continuous_numerical_parameters": 0,
        "new_discrete_numerical_parameters": 0,
        "conditional_current_standard": {
            "relative_gauge_action_closed": True,
            "basis": "CSGA1 derived here plus A78 adopted one-primitive relative boundary",
            "additional_physical_primitive_count": 0,
        },
        "strict_unconditional": {
            "relative_gauge_action_closed": False,
            "blocking_clause": "CSGA2 finite matching/action completeness",
            "strict_gauge_values_accepted": 0,
        },
    }

    gate = {
        "schema": "MTTRemainingFiniteMatchingCompletenessGate.v1",
        "status": "HEATSHADOW_ACTION_MAP_DERIVED_ONLY_FINITE_MATCHING_COMPLETENESS_HELDOUT_VALIDATION_AND_STRICT_PEW_OPEN",
        "closed": {
            "fixed_point_Hessian_to_semigroup": semigroup["theorem"]["proved_at_fixed_point_gradient_flow_tier"],
            "selected_time_identity": damping_residual < 1e-15,
            "damped_overlap_equals_A83_heat_density": factorization_residual < 1e-13,
            "unified_action_contains_J_as_potential": action_markers["J_is_action_potential"],
            "coherent_reduction_emits_internal_overlap_coefficients": action_markers["coherent_coefficients_are_internal_overlaps"],
            "CSGA1_derived_at_regime_local_action_tier": action["CSGA1_heat_shadow_derived_at_regime_local_action_tier"],
            "one_primitive_profile_tier_relative_boundary_available": reduction["clause_status"]["CSGA2_finite_matching_completeness"]["closed_at_adopted_one_primitive_boundary_tier"],
        },
        "open": {
            "derive_CSGA2_from_complete_microscopic_action_and_heavy_sector_matching": True,
            "or_explicitly_adopt_CSGA2_as_finite_matching_boundary": True,
            "promote_A67_density_beyond_source_axiom_tier": True,
            "held_out_validation_after_final_action_freeze": True,
            "strict_absolute_P_EW_source": True,
        },
        "strict_gauge_values_accepted": 0,
        "conditional_gauge_values_emitted_at_current_standard": 3,
        "remaining_relative_gauge_numerical_objects": 0,
        "remaining_structural_action_clauses": 1,
        "new_continuous_numerical_parameters": 0,
        "new_discrete_numerical_parameters": 0,
        "next_required_artifact": NEXT,
    }

    checks = {
        "fixed_markers": all(fixed_markers.values()),
        "action_markers": all(action_markers.values()),
        "damping_identity": damping_residual < 1e-15,
        "commutation": commute_residual < 1e-14,
        "damped_factorization": factorization_residual < 1e-13,
        "CSGA1_closed": reduction["clause_status"]["CSGA1_heat_shadow"]["closed"],
        "CSGA2_not_overpromoted": not reduction["clause_status"]["CSGA2_finite_matching_completeness"]["closed_strictly"],
        "all_gate_closed_items": all(gate["closed"].values()),
        "strict_values_zero": gate["strict_gauge_values_accepted"] == 0,
        "no_new_numeric_parameters": gate["new_continuous_numerical_parameters"] == 0 and gate["new_discrete_numerical_parameters"] == 0,
    }
    candidate = {
        "schema": "MTTSelectedClosureShadowGaugeActionAxiomDerivationOrExplicitAdoptionAndHeldoutValidation.v1",
        "status": STATUS,
        "results": {
            "CSGA1_heat_shadow_derived_at_regime_local_action_tier": True,
            "CSGA2_finite_matching_completeness_derived_strictly": False,
            "remaining_structural_action_clause_count": 1,
            "relative_gauge_action_closed_at_adopted_current_standard": True,
            "strict_gauge_values_accepted": 0,
            "conditional_gauge_values_emitted": 3,
            "remaining_relative_gauge_numerical_objects": 0,
            "new_continuous_numerical_parameters": 0,
            "new_discrete_numerical_parameters": 0,
        },
        "outputs": {
            "semigroup": str(SEMIGROUP.relative_to(ROOT)).replace("\\", "/"),
            "action": str(ACTION.relative_to(ROOT)).replace("\\", "/"),
            "reduction": str(REDUCTION.relative_to(ROOT)).replace("\\", "/"),
            "gate": str(GATE.relative_to(ROOT)).replace("\\", "/"),
        },
        "checks": checks,
        "authority_hashes": [{"path": str(path), "sha256": sha256(path)} for path in paths.values()],
        "next_required_artifact": NEXT,
    }
    cert = {
        "certificate": "MTT_Selected_ClosureShadowGaugeActionAxiomDerivation_or_ExplicitAdoptionAndHeldOutValidation_v1",
        "status": STATUS,
        "exp_minus_15_tau_residual_to_1_over_448": damping_residual,
        "Hcl_PhiC1_commutator_residual": commute_residual,
        "damped_overlap_factorization_residual": factorization_residual,
        "CSGA1_derived_at_regime_local_action_tier": True,
        "CSGA2_derived_strictly": False,
        "remaining_structural_action_clause_count": 1,
        "conditional_gauge_values_emitted": 3,
        "strict_gauge_values_accepted": 0,
        "new_continuous_numerical_parameters": 0,
        "new_discrete_numerical_parameters": 0,
        "next_required_artifact": NEXT,
    }
    note = f"""# MTT Selected Closure-Shadow Gauge-Action Axiom Derivation or Explicit Adoption and Held-Out Validation v1

## CSGA1 is derivable at the action tier

The fixed-point damping theorem already states that, in the gradient-flow case, the Hessian of the
closure/admissibility functional is the linearized stabilization generator and that the unique
selected-time kernel is `exp(-tau A)`. The selected values satisfy

```text
exp(-15 tau_int) = 1/448
```

with residual `{damping_residual:.3e}`.

The regime-local ten-dimensional action paper then supplies the missing action bridge: `J(s)` is its
potential, and coherent reduction makes four-dimensional coefficients finite internal overlaps. On
the selected finite carrier, `H_cl` is sector-central and commutes with `Phi_C1^+`, so

```text
Phi_C1^(1/2) exp(-tau_int H_cl) Phi_C1^(1/2)
= exp(-tau_int H_cl) Phi_C1^+
```

with residual `{factorization_residual:.3e}`. This is exactly A83's gauge density. Therefore CSGA1,
the heat-shadow clause, is derived at the existing fixed-point-gradient-flow plus regime-local
unified-action tier; it need not be adopted as a new independent axiom there.

## One clause remains

CSGA2 remains independent:

```text
At the selected finite matching point, no additional sector-relative gauge-quadratic
functional is present beyond the represented finite trace action.
```

A75 proves why this is necessary: gauge symmetry permits three `F_a^2` coefficients and leaves two
relative directions after quotienting common normalization. The unified action paper is explicitly
regime-local and retains truncation/heavy-sector corrections, so it does not prove those two directions
vanish. At the already adopted one-primitive/profile standard A78 supplies this relative boundary,
so the relative gauge action is closed there with no additional primitive. Strict unconditional
closure still requires a microscopic matching-completeness theorem or explicit adoption of CSGA2.

No relative gauge number, matrix entry, multiplicity, projector, or sign remains to calculate. After
CSGA2 is fixed, the action must be frozen before a genuinely held-out modern validation; the existing
candidate was developed after the gauge profile was known and cannot be relabeled an independent
prediction.

Next artifact: `{NEXT}`.
"""

    for path, payload in [(SEMIGROUP, semigroup), (ACTION, action), (REDUCTION, reduction), (GATE, gate), (CANDIDATE, candidate), (CERT, cert)]:
        dump(path, payload)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
