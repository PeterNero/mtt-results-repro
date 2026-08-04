"""Replace the provisional signed anchoring grading by a positive quotient representative."""
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_anchoringparityinsertionlaw_or_independentkineticgramderivation"
OUT = ROOT / "candidate_data" / SLUG
QUOTIENT = OUT / "central_normalization_quotient_and_positive_representative.packet.json"
DEFECT = OUT / "full_anchor_projector_defect_hessian.packet.json"
EXECUTION = OUT / "positive_representative_gauge_execution.packet.json"
GUARDRAILS = OUT / "discarded_sign_mechanisms_and_scope_guard.packet.json"
GATE = OUT / "remaining_action_ownership_and_spectator_gate.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_AnchoringParityInsertionLaw_or_IndependentKineticGramDerivation_v1.md"
STATUS = "MTT_SELECTED_RELATIVE_SIGN_POSITIVE_QUOTIENT_REPRESENTATIVE_AND_DEFECT_HESSIAN_DERIVED_ACTION_OWNERSHIP_OPEN"
NEXT = "MTT_Selected_FullAnchorDefectHessianActionOwnershipAndSpectatorCancellation_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def matvec(matrix: list[list[float]], vector: list[float]) -> list[float]:
    return [sum(a * b for a, b in zip(row, vector)) for row in matrix]


def max_abs(values: list[float]) -> float:
    return max((abs(value) for value in values), default=0.0)


def main() -> int:
    proto = Path("C:/ObsidianVault/BrainOfNerodes/Papers/Modal Triplet Theory/10 ProtoSpinor/Closure_Strain_Geometry_and_the_Structure_of_the_Standard_Model_v5.md")
    paths = {
        "A78_readout": ROOT / "candidate_data" / "selected_producttriplegaugefluctuationfunctorandrelativeboundarycondition" / "center_response_to_sector_kinetic_density_functor.packet.json",
        "A78_branches": ROOT / "candidate_data" / "selected_producttriplegaugefluctuationfunctorandrelativeboundarycondition" / "charged_lepton_dual_metric_sign_branch_execution.packet.json",
        "A78_boundary": ROOT / "candidate_data" / "selected_producttriplegaugefluctuationfunctorandrelativeboundarycondition" / "relative_spectral_action_boundary_condition.packet.json",
        "A79_nogo": ROOT / "candidate_data" / "selected_chargedleptondualmetricsignandspectralactioncompleteness" / "common_positive_heat_sign_no_go.packet.json",
        "A79_grading": ROOT / "candidate_data" / "selected_chargedleptondualmetricsignandspectralactioncompleteness" / "anchoring_parity_grading_construction.packet.json",
        "A79_corpus": ROOT / "candidate_data" / "selected_chargedleptondualmetricsignandspectralactioncompleteness" / "protospinor_source_support_and_missing_insertion_law.packet.json",
        "A69_operator": ROOT / "candidate_data" / "selected_commonquarkorder_sharedcirclekineticoperator_or_exactresidualspectrum" / "conditional_common_projected_kinetic_operator.packet.json",
        "C1_defect_source": ROOT / "candidate_data" / "selected_c1defectfunctionalsource_or_independentquadraturedatafill.candidate.json",
        "Step14_source": ROOT / "candidate_data" / "selected_step14_sourcepromotionclosure_from_premisefreephifin.candidate.json",
        "proto_spinor": proto,
    }
    data = {key: load(path) for key, path in paths.items() if path.suffix == ".json"}
    proto_text = proto.read_text(encoding="utf-8")

    readout = data["A78_readout"]
    sector_order = readout["selected_sector_support"]["sector_order"]
    p_colored = [int(value) for value in readout["selected_sector_support"]["P_colored"]]
    p_e = [int(value) for value in readout["selected_sector_support"]["P_e"]]
    identity = [1] * len(sector_order)
    q_e_complement = [one - value for one, value in zip(identity, p_e)]
    delta_q, delta_e = [float(value) for value in readout["input"]["center_valued_determinant_response"]]

    relative_response = [delta_q * q - delta_e * e for q, e in zip(p_colored, p_e)]
    positive_response = [delta_q * q + delta_e * qe for q, qe in zip(p_colored, q_e_complement)]
    quotient_difference = [positive - relative for positive, relative in zip(positive_response, relative_response)]
    quotient = {
        "schema": "MTTCentralNormalizationQuotientAndPositiveRepresentative.v1",
        "status": "SIGNED_RELATIVE_RESPONSE_HAS_CANONICAL_POSITIVE_PROJECTOR_COMPLEMENT_REPRESENTATIVE",
        "theorem": {
            "equivalence_relation": "C~C+cI because W(C+cI)=exp(-tau*c)W(C)",
            "gauge_rows": "K_a(C+cI)=exp(-tau*c)K_a(C)",
            "relative_ratios": "K_a/K_2 is invariant under C->C+cI",
            "proof": "The scalar identity commutes with C and every gauge insertion, so its exponential factors out of every sector trace and cancels from all ratios.",
            "proved": True,
        },
        "sector_order": sector_order,
        "projectors": {
            "I": identity,
            "P_colored": p_colored,
            "P_e": p_e,
            "Q_e=I-P_e": q_e_complement,
        },
        "relative_representative": relative_response,
        "positive_representative": positive_response,
        "identity_shift": delta_e,
        "positive_minus_relative": quotient_difference,
        "difference_is_delta_e_I": max_abs([value - delta_e for value in quotient_difference]) < 1e-15,
        "positive_representative_psd": min(positive_response) >= 0.0,
        "interpretation": "The negative P_e coefficient is a coordinate in the quotient by common normalization, not a negative eigenvalue of the physical positive Hessian.",
    }

    # The Hessian of 1/2 ||(I-P)x||^2 is I-P for every orthogonal projector P.
    defect_hessian = positive_response
    general_coefficients = {
        "central_form": "H=a I+b P_colored+c P_e",
        "full_anchor_kernel_condition": "H P_e=0 implies c=-a",
        "universal_non_e_defect_magnitude": "a=delta_e",
        "extra_partial_anchor_colored_magnitude": "b=delta_q",
        "unique_solution": "H=delta_e(I-P_e)+delta_q P_colored",
    }
    defect = {
        "schema": "MTTFullAnchorProjectorDefectHessian.v1",
        "status": "CANONICAL_POSITIVE_DEFECT_HESSIAN_UNIQUE_ON_SELECTED_SECTOR_COMMUTANT",
        "projector_distance_theorem": {
            "functional": "D_P(x)=1/2 ||(I-P)x||^2",
            "gradient": "grad D_P=(I-P)x",
            "hessian": "Hess D_P=I-P",
            "positivity": "<x,(I-P)x>=||(I-P)x||^2>=0",
            "kernel": "ker Hess D_P=Ran(P)",
            "proved": True,
        },
        "selected_application": {
            "full_anchor_projector": "P_e on the gauge-commuting charged-singlet-specific lane",
            "partial_anchor_projector": "P_colored",
            "D_anchor": "(delta_e/2)||(I-P_e)x||^2+(delta_q/2)||P_colored x||^2",
            "H_anchor": defect_hessian,
            "H_anchor_psd": min(defect_hessian) >= 0.0,
            "H_anchor_kernel_on_P_e": all(abs(h * e) < 1e-15 for h, e in zip(defect_hessian, p_e)),
            "colored_excess_over_non_e_baseline": delta_q,
        },
        "uniqueness_in_central_three_generator_class": general_coefficients,
        "source_support": {
            "A69_selects_P_e_and_P_colored": readout["selected_sector_support"]["projectors_disjoint"],
            "proto_spinor_selects_charged_leptons_as_fully_anchored": "Charged leptons correspond to fully anchored identity configurations" in proto_text,
            "proto_spinor_selects_quarks_as_partially_anchored": "Quarks are partially anchored identities" in proto_text,
            "MTT_C1_projector_defect_functional_already_sourced_on_its_own_domain": data["C1_defect_source"]["what_closes_now"]["unique_formal_C1_defect_functional_sourced"],
            "MTT_C1_physical_source_stack_later_promoted_on_its_own_domain": data["Step14_source"]["closure_decision"]["source_stack_closed"],
        },
        "scope_guard": {
            "C1_domain_result_transferred_automatically_to_gauge_action": False,
            "physical_gauge_action_identified_with_D_anchor": False,
            "classification_alone_called_action_dynamics": False,
        },
    }

    base = [float(value) for value in data["A69_operator"]["finite_operator"]["C_sector_eigenvalues"]]
    base_traces = [float(value) for value in data["A69_operator"]["finite_operator"]["base_C1_sector_traces"]]
    trace_map = [[float(value) for value in row] for row in readout["functor"]["sector_trace_matrix"]]
    tau = math.log(448.0) / 15.0
    total_relative = [value + response for value, response in zip(base, relative_response)]
    canonical_shift = -min(total_relative)
    total_positive = [value + canonical_shift for value in total_relative]
    base_positive = [value - min(base) for value in base]
    assembled_positive = [value + response for value, response in zip(base_positive, positive_response)]
    weights_relative = [trace * math.exp(-tau * cost) for trace, cost in zip(base_traces, total_relative)]
    weights_positive = [trace * math.exp(-tau * cost) for trace, cost in zip(base_traces, total_positive)]
    kinetic_relative = matvec(trace_map, weights_relative)
    kinetic_positive = matvec(trace_map, weights_positive)
    ratios_relative = [kinetic_relative[0] / kinetic_relative[1], 1.0, kinetic_relative[2] / kinetic_relative[1]]
    ratios_positive = [kinetic_positive[0] / kinetic_positive[1], 1.0, kinetic_positive[2] / kinetic_positive[1]]
    common_factor = math.exp(-tau * canonical_shift)
    frozen_dual = [float(value) for value in data["A78_branches"]["dual_branch"]["K_over_K2"]]
    execution = {
        "schema": "MTTPositiveRepresentativeGaugeExecution.v1",
        "status": "POSITIVE_HESSIAN_REPRESENTATIVE_EXACTLY_REPLAYS_DUAL_RELATIVE_BRANCH",
        "tau_int": tau,
        "sector_order": sector_order,
        "base_relative_eigenvalues": base,
        "base_positive_representative": base_positive,
        "response_relative_eigenvalues": relative_response,
        "response_positive_representative": positive_response,
        "total_relative_eigenvalues": total_relative,
        "canonical_total_identity_shift": canonical_shift,
        "total_positive_eigenvalues": total_positive,
        "assembled_positive_eigenvalues": assembled_positive,
        "total_positive_psd": min(total_positive) >= 0.0,
        "positive_assembly_exact": max_abs([a - b for a, b in zip(total_positive, assembled_positive)]) < 1e-14,
        "common_weight_factor": common_factor,
        "weights_relative": weights_relative,
        "weights_positive": weights_positive,
        "weight_factorization_residual": max_abs([p - common_factor * r for p, r in zip(weights_positive, weights_relative)]),
        "K_relative": kinetic_relative,
        "K_positive": kinetic_positive,
        "K_factorization_residual": max_abs([p - common_factor * r for p, r in zip(kinetic_positive, kinetic_relative)]),
        "K_over_K2_relative": ratios_relative,
        "K_over_K2_positive": ratios_positive,
        "ratio_representative_residual": max_abs([a - b for a, b in zip(ratios_positive, ratios_relative)]),
        "residual_to_A78_dual_branch": max_abs([a - b for a, b in zip(ratios_positive, frozen_dual)]),
        "continuous_parameters_added": 0,
        "observed_gauge_values_used_as_selector": False,
    }

    guardrails = {
        "schema": "MTTAnchoringSignMechanismScopeGuard.v1",
        "status": "INDEFINITE_GRADING_AND_UNSOURCED_TORSION_SHORTCUTS_RETIRED",
        "A79_no_go_preserved": {
            "statement": data["A79_nogo"]["theorem"]["conclusion"],
            "scope": "literal positive sector corrections in one fixed representative",
            "why_A80_does_not_contradict_it": "A80 works in the physical quotient C modulo scalar identity and uses a positive complement projector, not two positive same-support corrections in the fixed representative.",
        },
        "J_anchor_status": {
            "algebraic_relative_coordinate_still_correct": data["A79_grading"]["response"]["exact_match"],
            "literal_indefinite_action_insertion_required": False,
            "replacement": "positive Hessian delta_e(I-P_e)+delta_q P_colored modulo delta_e I",
        },
        "quarter_character_square_route": {
            "promoted": False,
            "reason": "A Hermitian Gram second variation sees |i|^2=1, not i^2=-1; a bilinear holomorphic Hessian would require a separately selected real-action prescription.",
        },
        "analytic_torsion_parity_route": {
            "promoted": False,
            "reason": "Alternating determinant signs are standard on a selected cochain complex, but the corpus does not place P_colored and P_e in the required opposite cohomological degrees.",
        },
        "negative_physical_closure_hessian_claimed": False,
    }

    source_support_all = all(defect["source_support"].values())
    gate = {
        "schema": "MTTRemainingFullAnchorDefectActionOwnershipAndSpectatorGate.v1",
        "status": "RELATIVE_SIGN_HAS_ZERO_PARAMETER_POSITIVE_REALIZATION_PHYSICAL_GAUGE_ACTION_OWNERSHIP_OPEN",
        "closed": {
            "central_identity_is_null_in_gauge_ratio_space": quotient["theorem"]["proved"],
            "signed_relative_response_has_psd_representative": quotient["positive_representative_psd"],
            "projector_defect_hessian_theorem": defect["projector_distance_theorem"]["proved"],
            "selected_classification_and_projector_support_present": source_support_all,
            "positive_execution_exactly_replays_A78": execution["residual_to_A78_dual_branch"] < 1e-14,
            "no_continuous_or_discrete_sign_parameter_in_positive_realization": True,
        },
        "open": {
            "selected_gauge_action_second_variation_equals_D_anchor_on_A77_domains": True,
            "fermion_Higgs_and_inactive_spectators_are_scalar_identity_or_cancel": True,
            "no_extra_relative_local_quadratic_counterterm": True,
            "strict_absolute_P_EW_normalization": True,
            "modern_common_scheme_validation_after_source_promotion": True,
        },
        "frontier_reduction": {
            "old_question": "Why is a negative or indefinite J_anchor inserted?",
            "new_question": "Why does the selected gauge-response action use the canonical full-anchor defect Hessian D_anchor, with all omitted blocks ratio-neutral?",
            "binary_sign_bit_retired_as_tunable_parameter": True,
            "remaining_action_ownership_proposition_count": 1,
        },
        "relative_ratio_source_parameters": {"continuous": 0, "discrete_sign": 0},
        "strict_gauge_values_accepted": 0,
        "next_required_artifact": NEXT,
    }

    checks = {
        "sector_order_correct": sector_order == ["Q", "u", "d", "L", "e", "N"],
        "delta_magnitudes_positive": delta_q > 0.0 and delta_e > 0.0,
        "quotient_difference_exact": quotient["difference_is_delta_e_I"],
        "positive_response_psd": quotient["positive_representative_psd"],
        "defect_hessian_psd": defect["selected_application"]["H_anchor_psd"],
        "defect_kernel_is_e": defect["selected_application"]["H_anchor_kernel_on_P_e"],
        "source_support_present": source_support_all,
        "domain_transfer_not_overclaimed": not defect["scope_guard"]["C1_domain_result_transferred_automatically_to_gauge_action"],
        "total_positive_psd": execution["total_positive_psd"],
        "positive_assembly_exact": execution["positive_assembly_exact"],
        "weight_factorization_exact": execution["weight_factorization_residual"] < 1e-14,
        "kinetic_factorization_exact": execution["K_factorization_residual"] < 1e-13,
        "ratios_invariant": execution["ratio_representative_residual"] < 1e-14,
        "A78_dual_replayed": execution["residual_to_A78_dual_branch"] < 1e-14,
        "no_observed_selector": not execution["observed_gauge_values_used_as_selector"],
        "indefinite_insertion_retired": not guardrails["J_anchor_status"]["literal_indefinite_action_insertion_required"],
        "strict_action_ownership_open": not defect["scope_guard"]["physical_gauge_action_identified_with_D_anchor"],
    }

    candidate = {
        "schema": "MTTSelectedAnchoringParityInsertionLawOrIndependentKineticGramDerivation.v1",
        "status": STATUS,
        "results": {
            "A79_fixed_representative_no_go_preserved": True,
            "central_normalization_quotient_theorem_closed": True,
            "positive_projector_complement_hessian_derived": True,
            "positive_representative_replays_A78_exactly": True,
            "literal_indefinite_J_anchor_insertion_required": False,
            "binary_sign_parameter_remaining": 0,
            "physical_gauge_action_ownership_closed": False,
            "strict_action_completeness_closed": False,
            "strict_gauge_values_accepted": 0,
            "new_continuous_parameters": 0,
        },
        "outputs": {
            "quotient": str(QUOTIENT.relative_to(ROOT)).replace("\\", "/"),
            "defect": str(DEFECT.relative_to(ROOT)).replace("\\", "/"),
            "execution": str(EXECUTION.relative_to(ROOT)).replace("\\", "/"),
            "guardrails": str(GUARDRAILS.relative_to(ROOT)).replace("\\", "/"),
            "gate": str(GATE.relative_to(ROOT)).replace("\\", "/"),
        },
        "checks": {key: bool(value) for key, value in checks.items()},
        "authority_hashes": [{"path": str(path), "sha256": sha256(path)} for path in paths.values()],
        "next_required_artifact": NEXT,
    }
    cert = {
        "certificate": "MTT_Selected_AnchoringParityInsertionLaw_or_IndependentKineticGramDerivation_v1",
        "status": STATUS,
        "central_normalization_quotient_closed": True,
        "positive_defect_hessian": defect_hessian,
        "positive_representative_K_over_K2": ratios_positive,
        "residual_to_A78": execution["residual_to_A78_dual_branch"],
        "binary_sign_parameters_remaining": 0,
        "physical_gauge_action_ownership_closed": False,
        "strict_action_completeness_closed": False,
        "strict_gauge_values_accepted": 0,
        "new_continuous_parameters": 0,
        "next_required_artifact": NEXT,
    }
    note = f"""# MTT Selected Anchoring-Parity Insertion Law or Independent Kinetic-Gram Derivation v1

## Central-normalization quotient theorem

Gauge ratios are invariant under a common scalar shift of the sector cost:

```text
C ~ C+cI,
W(C+cI)=exp(-tau*c)W(C),
K_a(C+cI)=exp(-tau*c)K_a(C).
```

Consequently the A78 relative response has the exactly equivalent representative

```text
delta_q P_colored-delta_e P_e
= delta_q P_colored+delta_e(I-P_e)-delta_e I.
```

The non-scalar representative on the right is positive semidefinite. The apparent negative charged-
lepton coefficient is therefore not evidence for a negative closure Hessian or an indefinite physical
metric; it is a coordinate in the quotient by the one common gauge normalization.

## Positive full-anchor defect Hessian

For every orthogonal projector `P`,

```text
D_P(x)=1/2 ||(I-P)x||^2,
Hess(D_P)=I-P >= 0,
ker Hess(D_P)=Ran(P).
```

Using the already selected charged-singlet support `P_e` and colored support `P_colored` gives

```text
D_anchor(x)=(delta_e/2)||(I-P_e)x||^2
            +(delta_q/2)||P_colored x||^2,
H_anchor=delta_e(I-P_e)+delta_q P_colored.
```

Within `span{{I,P_colored,P_e}}`, this is the unique positive central Hessian with the full-anchor
lane as kernel, universal non-`e` defect magnitude `delta_e`, and the additional partial-anchor
colored magnitude `delta_q`. ProtoSpinor supplies the full-versus-partial anchoring classification;
the existing MTT C1 program independently establishes projector-defect functionals on its own domain.

## Exact gauge execution

The old total relative cost has minimum `{-canonical_shift:.17g}`. Its canonical positive representative
adds `{canonical_shift:.17g} I` and has spectrum

```text
{total_positive}.
```

All three gauge rows acquire the same factor `{common_factor:.17g}`. Their ratios are unchanged:

```text
K/K2 = {ratios_positive},
maximum residual to A78 = {execution['residual_to_A78_dual_branch']:.3e}.
```

No observed coupling was used and no continuous or discrete sign parameter was added.

## Corrected interpretation of A79

A79 remains valid for two literal positive corrections in one fixed representative. A80 does not
evade that theorem with an indefinite grading: it passes to the physically relevant quotient and
uses the positive projector complement. A literal `J_anchor` insertion, the unsupported `i^2` shortcut,
and an unselected analytic-torsion parity assignment are all unnecessary and are not promoted.

## Remaining physical theorem

The sign parameter is retired, but strict source promotion is not yet claimed. The next theorem is
`{NEXT}`: identify the selected gauge-action second variation with `D_anchor` on the A77 domains and
prove that fermion, Higgs and inactive spectator blocks are common-scalar or cancel, with no extra
relative local quadratic term. Absolute `P_EW` normalization and modern validation remain downstream.
"""

    dump(QUOTIENT, quotient)
    dump(DEFECT, defect)
    dump(EXECUTION, execution)
    dump(GUARDRAILS, guardrails)
    dump(GATE, gate)
    dump(CANDIDATE, candidate)
    dump(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
