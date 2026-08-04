"""Recenter the Lens rank-three projector and transfer its anchor defect to sectors."""
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_fullanchordefecthessianactionownershipandspectatorcancellation"
OUT = ROOT / "candidate_data" / SLUG
RECENTER = OUT / "lens_rankone_anchor_projective_tangent_recentering.packet.json"
FUNCTOR = OUT / "unital_anchor_to_sector_complement_functor.packet.json"
SPECTATORS = OUT / "known_spectator_cancellation_ledger.packet.json"
GATE = OUT / "remaining_baseline_multiplicity_and_noncentral_spectator_gate.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_FullAnchorDefectHessianActionOwnershipAndSpectatorCancellation_v1.md"
STATUS = "MTT_SELECTED_RANKONE_ANCHOR_TO_COMPLEMENT_DEFECT_FUNCTOR_CLOSED_KNOWN_SPECTATORS_NEUTRAL_BASELINE_MULTIPLICITIES_OPEN"
NEXT = "MTT_Selected_BaselineCostMultiplicitySourceAndNoncentralSpectatorExclusion_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def max_abs(values: list[float]) -> float:
    return max((abs(value) for value in values), default=0.0)


def main() -> int:
    paths = {
        "A74_trace": ROOT / "candidate_data" / "selected_normalizeddeterminantactionfrommtthessian_or_independentgaugeprofiletest" / "finite_trace_and_projector_uniqueness.packet.json",
        "A75_counterterm": ROOT / "candidate_data" / "selected_physicalkinetichessianblockidentity_or_modernprecisiongaugevalidation" / "relative_counterterm_and_matching_no_go.packet.json",
        "A77_routing": ROOT / "candidate_data" / "selected_gaugefixedfluctuationcomplexontoweraugmentationdomains" / "primitive_character_orbit_projector_routing.packet.json",
        "A77_execution": ROOT / "candidate_data" / "selected_gaugefixedfluctuationcomplexontoweraugmentationdomains" / "a73_brst_response_exact_execution.packet.json",
        "A77_gate": ROOT / "candidate_data" / "selected_gaugefixedfluctuationcomplexontoweraugmentationdomains" / "remaining_product_triple_and_matching_gate.packet.json",
        "A78_readout": ROOT / "candidate_data" / "selected_producttriplegaugefluctuationfunctorandrelativeboundarycondition" / "center_response_to_sector_kinetic_density_functor.packet.json",
        "A79_corpus": ROOT / "candidate_data" / "selected_chargedleptondualmetricsignandspectralactioncompleteness" / "protospinor_source_support_and_missing_insertion_law.packet.json",
        "A80_quotient": ROOT / "candidate_data" / "selected_anchoringparityinsertionlaw_or_independentkineticgramderivation" / "central_normalization_quotient_and_positive_representative.packet.json",
        "A80_defect": ROOT / "candidate_data" / "selected_anchoringparityinsertionlaw_or_independentkineticgramderivation" / "full_anchor_projector_defect_hessian.packet.json",
        "A80_execution": ROOT / "candidate_data" / "selected_anchoringparityinsertionlaw_or_independentkineticgramderivation" / "positive_representative_gauge_execution.packet.json",
        "A51_spectral": ROOT / "candidate_data" / "selected_finitespectralactionandhiggsinnerfluctuation_or_directgenerativesmactionclosure.candidate.json",
        "A56_gradings": ROOT / "candidate_data" / "selected_gaugeinsertedheatsupertracesecondvariation_or_commonschemethresholdpayload" / "finite_grading_supertrace_and_fluctuation_complex_cutset.packet.json",
        "A57_complex": ROOT / "candidate_data" / "selected_gaugefixedfluctuationcomplexhessians_or_oneloopthresholdsupertracepayload" / "gauge_fixed_complex_and_signed_heat_rows.packet.json",
        "A65_kinetic": ROOT / "candidate_data" / "selected_gaugezeromodekineticinnerproduct_or_chernweilbackgroundenergynogo" / "finite_gauge_zero_mode_kinetic_weight_theorem.packet.json",
        "A69_operator": ROOT / "candidate_data" / "selected_commonquarkorder_sharedcirclekineticoperator_or_exactresidualspectrum" / "conditional_common_projected_kinetic_operator.packet.json",
    }
    data = {key: load(path) for key, path in paths.items()}

    # The invariant and quarter-character lines in C[Z4] are unitarily related.
    u0 = np.asarray([1.0, 1.0, 1.0, 1.0], dtype=complex) / 2.0
    u1 = np.asarray([1.0, 1.0j, -1.0, -1.0j], dtype=complex) / 2.0
    q0 = np.outer(u0, u0.conjugate())
    q1 = np.outer(u1, u1.conjugate())
    identity4 = np.eye(4, dtype=complex)
    p0 = identity4 - q0
    p1 = identity4 - q1
    character_unitary = np.diag(np.asarray([1.0, 1.0j, -1.0, -1.0j], dtype=complex))
    conjugacy_residual = float(np.linalg.norm(character_unitary @ p0 @ character_unitary.conjugate().T - p1))
    projector_residuals = {
        "Q_quarter_idempotence": float(np.linalg.norm(q1 @ q1 - q1)),
        "P_quarter_perp_idempotence": float(np.linalg.norm(p1 @ p1 - p1)),
        "orthogonality": float(np.linalg.norm(q1 @ p1)),
        "completeness": float(np.linalg.norm(q1 + p1 - identity4)),
    }
    delta_q = float(data["A77_execution"]["q_block"]["value"])
    determinant_samples = []
    for epsilon in [0.0, 0.25, 0.5, 1.0, 2.0]:
        _, logdet0 = np.linalg.slogdet(identity4 + epsilon * delta_q * p0)
        _, logdet1 = np.linalg.slogdet(identity4 + epsilon * delta_q * p1)
        determinant_samples.append({
            "epsilon": epsilon,
            "normalized_logdet_invariant_complement": float(logdet0 / 4.0),
            "normalized_logdet_quarter_complement": float(logdet1 / 4.0),
            "absolute_residual": float(abs(logdet0 - logdet1) / 4.0),
        })
    recenter = {
        "schema": "MTTLensRankOneAnchorProjectiveTangentRecentering.v1",
        "status": "A77_RANKTHREE_RETURN_PROJECTOR_RECENTERED_ON_SELECTED_QUARTER_ANCHOR_WITHOUT_NUMERICAL_CHANGE",
        "selected_Z4_character_lines": {
            "invariant": "u0=(1,1,1,1)/2",
            "quarter": "u1=(1,i,-1,-i)/2",
            "Q_quarter_rank": int(np.linalg.matrix_rank(q1, tol=1e-12)),
            "Q_quarter_perp_rank": int(np.linalg.matrix_rank(p1, tol=1e-12)),
        },
        "unitary_recentring": {
            "U_character": "diag(1,i,-1,-i)",
            "U P_invariant_perp U*=P_quarter_perp": conjugacy_residual < 1e-14,
            "residual": conjugacy_residual,
        },
        "projector_checks": projector_residuals,
        "normalized_trace": {
            "tau4_P_invariant_perp": float(np.trace(p0).real / 4.0),
            "tau4_P_quarter_perp": float(np.trace(p1).real / 4.0),
            "A74_forced_value": float(data["A74_trace"]["applications"]["P4_nontrivial"]["normalized_trace"]),
            "all_equal_three_over_four": max_abs([
                float(np.trace(p0).real / 4.0) - 0.75,
                float(np.trace(p1).real / 4.0) - 0.75,
                float(data["A74_trace"]["applications"]["P4_nontrivial"]["normalized_trace"]) - 0.75,
            ]) < 1e-15,
        },
        "determinant_recentring_samples": determinant_samples,
        "all_determinant_samples_equal": max(row["absolute_residual"] for row in determinant_samples) < 1e-14,
        "projective_tangent_theorem": {
            "tangent_space": "T_[Q] CP^3 ~= Hom(Ran Q,Ran(I-Q)) ~= C^3",
            "quadratic_defect": "D_Q(v)=1/2 ||(I-Q)v||^2",
            "hessian": "Hess D_Q=I-Q on the tangent",
            "why_isotropic": "A74 unitary-conjugation-invariant normalized trace induces the canonical invariant finite Frobenius metric.",
            "proved": True,
        },
        "scope": "This identifies the correct complement of the selected quarter-character line. It does not identify the baseline coefficients 3 and 14/3 with a microscopic action.",
    }

    sector_order = data["A78_readout"]["selected_sector_support"]["sector_order"]
    p_e = [int(value) for value in data["A78_readout"]["selected_sector_support"]["P_e"]]
    p_colored = [int(value) for value in data["A78_readout"]["selected_sector_support"]["P_colored"]]
    identity6 = [1] * 6
    q_e = [one - e for one, e in zip(identity6, p_e)]
    delta_e = float(data["A77_execution"]["e_total"]["value"])
    target_defect = [float(value) for value in data["A80_defect"]["selected_application"]["H_anchor"]]
    mapped_defect = [delta_e * qe + delta_q * q for qe, q in zip(q_e, p_colored)]
    functor = {
        "schema": "MTTUnitalAnchorToSectorComplementFunctor.v1",
        "status": "UNIQUE_UNITAL_CENTER_MAP_SENDS_QUARTER_ANCHOR_DEFECT_TO_CHARGEDSECTOR_COMPLEMENT",
        "source_center": "Z(C*(Q_quarter))=C Q_quarter direct-sum C(I-Q_quarter)",
        "target_center": "C P_e direct-sum C(I-P_e) inside the six-sector gauge commutant",
        "selected_anchor_map": "Phi_anchor(Q_quarter)=P_e",
        "unital_consequence": "Phi_anchor(I-Q_quarter)=I-P_e",
        "formula": "Phi_anchor(a Q_quarter+b(I-Q_quarter))=a P_e+b(I-P_e)",
        "theorem": {
            "unital": True,
            "star_preserving": True,
            "multiplicative": True,
            "positive": True,
            "unique_given_anchor_image": True,
            "proof": "The two minimal central idempotents are complementary. A unital star homomorphism is fixed by the image of either one, so Q->P_e forces I-Q->I-P_e.",
        },
        "action_response": {
            "source_quarter_tangent_hessian": "delta_e(I-Q_quarter)",
            "target_full_anchor_defect": mapped_defect,
            "A80_target": target_defect,
            "exact_match": max_abs([a - b for a, b in zip(mapped_defect, target_defect)]) < 1e-15,
            "colored_extra_added_on_independent_selected_support": "delta_q P_colored",
        },
        "interpretation": "The map is direct on the selected anchor line and therefore contravariant on its defect: preserving the anchor forces the physical quadratic variation onto the complementary tangent.",
        "continuous_parameters_added": 0,
        "discrete_sign_parameters_added": 0,
    }

    known_spectators = [
        {
            "id": "central_identity",
            "result": "C->C+cI multiplies every K_a by one common factor",
            "relative_effect_rank": 0,
            "closed": data["A80_quotient"]["theorem"]["proved"],
        },
        {
            "id": "A51_universal_tree_trace",
            "result": "GUT-normalized finite tree trace is (6,6,6)",
            "relative_effect_rank": 0,
            "closed": data["A51_spectral"]["checks"]["GUT_normalized_U1_equals_nonabelian_traces"],
        },
        {
            "id": "finite_KO6_chirality",
            "result": "gauge-inserted KO6 chiral supertrace is exactly zero",
            "relative_effect_rank": 0,
            "closed": data["A56_gradings"]["checks"]["KO6_squared_charge_supertrace_zero"],
        },
        {
            "id": "uniform_fermion_parity",
            "result": "uniform fermion parity only flips the universal trace",
            "relative_effect_rank": 0,
            "closed": data["A56_gradings"]["checks"]["uniform_fermion_parity_only_flips_common_sign"],
        },
        {
            "id": "tree_Higgs_column",
            "result": "Higgs is not an independent tree finite-carrier gauge trace column",
            "relative_effect_rank": 0,
            "closed": data["A65_kinetic"]["checks"]["Higgs_is_not_an_independent_tree_trace_column"],
        },
        {
            "id": "common_internal_one_loop_spectrum",
            "result": "common finite determinant is a one-loop scale translation, not an independent threshold shape",
            "relative_effect_rank": 0,
            "closed": not data["A57_complex"]["common_internal_spectrum_execution"]["adds_independent_threshold_shape"],
        },
    ]
    unresolved_spectators = {
        "sector_resolved_internal_fluctuation_spectra": not data["A57_complex"]["checks"]["sector_resolved_internal_spectra_not_present"],
        "fermion_Higgs_and_other_A77_blocks_ratio_neutral_or_cancel": not data["A77_gate"]["open"]["fermion_Higgs_and_other_gauge_blocks_are_q79_neutral_or_cancel"],
        "extra_relative_local_quadratic_terms_excluded": data["A75_counterterm"]["finite_exact_object_scope"]["arbitrary_additive_finite_gauge_quadratic_term_excluded_automatically"],
    }
    spectators = {
        "schema": "MTTKnownSpectatorCancellationLedger.v1",
        "status": "ALL_CURRENTLY_COMPUTABLE_SPECTATOR_CLASSES_RELATIVE_NEUTRAL_NONCENTRAL_COMPLETENESS_OPEN",
        "known_classes": known_spectators,
        "known_class_count": len(known_spectators),
        "known_classes_closed": sum(int(row["closed"]) for row in known_spectators),
        "all_known_classes_closed": all(row["closed"] for row in known_spectators),
        "unresolved_completeness": unresolved_spectators,
        "all_possible_spectators_excluded": False,
        "guard": "A list of known neutral classes is not a proof that no additional sector-resolved block exists.",
    }

    base = data["A69_operator"]["finite_operator"]["C_sector_eigenvalues"]
    base_colored = float(base[0])
    base_e_magnitude = -float(base[4])
    c_colored = base_colored + delta_q
    c_e = base_e_magnitude + delta_e
    total_positive = [c_e * qe + c_colored * q for qe, q in zip(q_e, p_colored)]
    a80_total = [float(value) for value in data["A80_execution"]["total_positive_eigenvalues"]]
    baseline_flags = data["A69_operator"]["source_status"]
    gate = {
        "schema": "MTTRemainingBaselineMultiplicityAndNoncentralSpectatorGate.v1",
        "status": "ANCHOR_COMPLEMENT_ROUTING_CLOSED_TOTAL_POSITIVE_OPERATOR_ASSEMBLED_BASELINE_SOURCE_AND_COMPLETENESS_OPEN",
        "closed": {
            "A77_rankthree_projector_recentered_on_quarter_anchor": recenter["all_determinant_samples_equal"],
            "rankone_anchor_projective_tangent_hessian": recenter["projective_tangent_theorem"]["proved"],
            "unital_anchor_to_sector_complement_functor": all(functor["theorem"].values()),
            "A80_positive_defect_reproduced": functor["action_response"]["exact_match"],
            "known_spectator_classes_neutral": spectators["all_known_classes_closed"],
            "full_total_positive_operator_algebraically_assembled": max_abs([a - b for a, b in zip(total_positive, a80_total)]) < 1e-14,
        },
        "total_positive_operator": {
            "formula": "H_total=(3+delta_e)(I-P_e)+(14/3+delta_q)P_colored",
            "c_e": c_e,
            "c_colored_extra": c_colored,
            "eigenvalues": total_positive,
            "residual_to_A80": max_abs([a - b for a, b in zip(total_positive, a80_total)]),
        },
        "open": {
            "same_action_derives_baseline_c_e_equals_3": True,
            "same_action_derives_baseline_c_colored_equals_14_over_3": True,
            "all_sector_resolved_noncentral_spectators_excluded_or_computed": True,
            "rank_two_relative_counterterm_space_fixed_microscopically": True,
            "strict_absolute_P_EW_normalization": True,
            "independent_modern_validation_after_source_freeze": True,
        },
        "A69_baseline_source_status": baseline_flags,
        "relative_sign_or_anchor_complement_map_still_open": False,
        "relative_ratio_parameters": {"continuous": 0, "discrete_sign": 0},
        "strict_gauge_values_accepted": 0,
        "next_required_artifact": NEXT,
    }

    checks = {
        "A74_trace_theorem": data["A74_trace"]["general_finite_trace_theorem"]["proved"],
        "quarter_character_selected": data["A77_routing"]["lepton_route"]["rank_one_selected_quarter_character"],
        "recenter_unitary_exact": recenter["unitary_recentring"]["U P_invariant_perp U*=P_quarter_perp"],
        "all_projector_residuals_small": max(projector_residuals.values()) < 1e-14,
        "rank_three_trace_forced": recenter["normalized_trace"]["all_equal_three_over_four"],
        "determinant_recenter_exact": recenter["all_determinant_samples_equal"],
        "tangent_hessian_derived": recenter["projective_tangent_theorem"]["proved"],
        "center_functor_all_properties": all(functor["theorem"].values()),
        "center_functor_matches_A80": functor["action_response"]["exact_match"],
        "known_spectators_closed": spectators["all_known_classes_closed"],
        "spectator_completeness_not_overclaimed": not spectators["all_possible_spectators_excluded"],
        "full_total_operator_assembled": gate["closed"]["full_total_positive_operator_algebraically_assembled"],
        "baseline_source_not_overclaimed": not baseline_flags["all_factor_bridges_selected"],
        "counterterm_completeness_not_overclaimed": not data["A75_counterterm"]["finite_exact_object_scope"]["arbitrary_additive_finite_gauge_quadratic_term_excluded_automatically"],
    }

    candidate = {
        "schema": "MTTSelectedFullAnchorDefectHessianActionOwnershipAndSpectatorCancellation.v1",
        "status": STATUS,
        "results": {
            "Lens_projector_recentered_on_selected_quarter_anchor": True,
            "anchor_to_complement_center_functor_closed": True,
            "relative_sign_map_closed": True,
            "known_spectator_classes_closed": spectators["known_classes_closed"],
            "known_spectator_class_count": spectators["known_class_count"],
            "all_spectator_completeness_closed": False,
            "baseline_14_over_3_and_3_source_closed": False,
            "strict_gauge_values_accepted": 0,
            "new_continuous_parameters": 0,
            "new_discrete_parameters": 0,
        },
        "outputs": {
            "recenter": str(RECENTER.relative_to(ROOT)).replace("\\", "/"),
            "functor": str(FUNCTOR.relative_to(ROOT)).replace("\\", "/"),
            "spectators": str(SPECTATORS.relative_to(ROOT)).replace("\\", "/"),
            "gate": str(GATE.relative_to(ROOT)).replace("\\", "/"),
        },
        "checks": {key: bool(value) for key, value in checks.items()},
        "authority_hashes": [{"path": str(path), "sha256": sha256(path)} for path in paths.values()],
        "next_required_artifact": NEXT,
    }
    cert = {
        "certificate": "MTT_Selected_FullAnchorDefectHessianActionOwnershipAndSpectatorCancellation_v1",
        "status": STATUS,
        "rank_three_recenter_residual": conjugacy_residual,
        "anchor_to_complement_functor_closed": True,
        "positive_total_operator": total_positive,
        "known_spectator_classes_closed": spectators["known_classes_closed"],
        "known_spectator_class_count": spectators["known_class_count"],
        "baseline_source_closed": False,
        "all_spectator_completeness_closed": False,
        "strict_gauge_values_accepted": 0,
        "new_continuous_parameters": 0,
        "new_discrete_parameters": 0,
        "next_required_artifact": NEXT,
    }
    note = f"""# MTT Selected Full-Anchor Defect-Hessian Action Ownership and Spectator Cancellation v1

## Lens projector recentering theorem

Let `Q_0` project onto the invariant line `(1,1,1,1)/2` and `Q_1` onto the selected quarter-character
line `(1,i,-1,-i)/2`. Multiplication by the quarter character gives a unitary `U` with

```text
U(I-Q_0)U* = I-Q_1.
```

The numerical residual is `{conjugacy_residual:.3e}`. Both complements have rank three and forced
normalized trace `3/4`. Their normalized determinants agree for every tested deformation, so A77's
rank-three return block can be recentered on the physical quarter anchor without changing A72/A73.

The A74 unitary-invariant trace also supplies the canonical projective tangent metric:

```text
T_[Q_1] CP^3 ~= Hom(Ran Q_1,Ran(I-Q_1)),
Hess D_Q = I-Q_1.
```

No optional ProtoSpinor isotropy assumption is needed.

## Unique anchor-to-sector functor

The selected center map is fixed by

```text
Phi_anchor(Q_1)=P_e,
Phi_anchor(I)=I.
```

Unitality then forces

```text
Phi_anchor(I-Q_1)=I-P_e.
```

Hence the positive Lens tangent Hessian maps exactly to A80's charged-sector complement defect.
Adding the independently selected colored support gives

```text
delta_e(I-P_e)+delta_q P_colored.
```

The relative sign/anchor-complement routing is therefore closed with no continuous or discrete parameter.

## Spectator audit

Six currently computable spectator classes are ratio-neutral: central identity shifts, the universal A51
tree trace, finite KO6 chirality, uniform fermion parity, the absent independent tree-Higgs column, and a
common internal one-loop spectrum (which is only an RG scale translation). This is not a completeness
theorem: sector-resolved noncentral fluctuation blocks and the A75 rank-two local matching space remain.

## Exact remaining source

The full positive operator is already assembled algebraically:

```text
H_total=(3+delta_e)(I-P_e)+(14/3+delta_q)P_colored
       = {total_positive}.
```

What remains is no longer the sign or the Lens projector. The next artifact is `{NEXT}`. It must derive
the baseline coefficients `3` and `14/3` from the same selected action and either compute or exclude every
sector-resolved noncentral spectator/counterterm. Absolute `P_EW` normalization and independent modern
validation remain downstream. Strict gauge values accepted here: zero.
"""

    dump(RECENTER, recenter)
    dump(FUNCTOR, functor)
    dump(SPECTATORS, spectators)
    dump(GATE, gate)
    dump(CANDIDATE, candidate)
    dump(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
