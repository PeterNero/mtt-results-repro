from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPECTRAL_ACTION = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory\15 Discrete & Spectral & Operator Geometric Theories\The_Spectral_Action_as_a_Shadow_of_Coherent_Fixed_Point_Geometry.md"
)
QFT_ACTION = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory\7 Quantum Field Theory\Modal_Triplet_Theory__Quantum_Amplitudes_from_Modal_Geometry_v2.md"
)
SLUG = "selected_finitematchingcompletenessfromunifiedaction_or_explicitboundaryadoptionandheldoutvalidation"
STATUS = (
    "MTT_SELECTED_BARE_FINITE_MATCHING_COMPLETENESS_DERIVED_AT_CORPUS_SPECTRAL_ACTION_TIER_"
    "RENORMALIZED_SCHEME_SEPARATED_CURRENT_PROFILE_TIER_CLOSED_STRICT_PRIMITIVE_SOURCE_OPEN"
)
NEXT = "MTT_Selected_PhiC1PositiveDensityPromotionFromClosedRouteASource_or_StrictGaugeRows_v1"

OUT = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_FiniteMatchingCompletenessFromUnifiedAction_or_ExplicitBoundaryAdoptionAndHeldOutValidation_v1.md"
BARE = OUT / "finite_projected_spectral_action_bare_completeness.packet.json"
SCHEME = OUT / "bare_action_vs_renormalized_scheme_separation.packet.json"
LEDGER = OUT / "closure_shadow_action_tier_ledger.packet.json"
FREEZE = OUT / "prospective_heldout_gauge_validation_freeze.packet.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    paths = {
        "A75_counterterm": ROOT / "candidate_data" / "selected_physicalkinetichessianblockidentity_or_modernprecisiongaugevalidation" / "relative_counterterm_and_matching_no_go.packet.json",
        "A78_boundary": ROOT / "candidate_data" / "selected_producttriplegaugefluctuationfunctorandrelativeboundarycondition" / "relative_spectral_action_boundary_condition.packet.json",
        "A83_hessian": ROOT / "candidate_data" / "selected_sharedcircleclosurehessiantogaugezeromoderestrictionandcountertermcompleteness" / "canonical_heat_density_and_gauge_zero_mode_hessian.packet.json",
        "A84_gate": ROOT / "candidate_data" / "selected_closureshadowgaugeactionaxiomderivation_or_explicitadoptionandheldoutvalidation" / "remaining_finite_matching_completeness_gate.packet.json",
        "finite_source": ROOT / "candidate_data" / "selected_finiteprojectedhymsourceprinciple_or_bandlimitexactnessproof.candidate.json",
        "multiloop_scheme": ROOT / "certificates" / "selected_multiloopcommonsourceprecisiontransport_or_officialjointlikelihood_certificate.json",
        "spectral_action_corpus": SPECTRAL_ACTION,
        "qft_action_corpus": QFT_ACTION,
    }
    missing = [str(path) for path in paths.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing finite-matching inputs: " + ", ".join(missing))

    data = {key: load(path) for key, path in paths.items() if path.suffix == ".json"}
    spectral_text = read(SPECTRAL_ACTION)
    qft_text = read(QFT_ACTION)

    spectral_markers = {
        "proper_time_assumption_explicit": "coherent fixed-point action admits a proper-time representation" in spectral_text,
        "spectral_action_shadow_theorem_explicit": "arises as the truncation shadow of the coherent fixed-point action" in spectral_text,
        "proper_time_trace_formula_explicit": "S_{\\mathrm{coh}} = \\int_0^\\infty" in spectral_text,
        "regulated_trace_step_explicit": "Truncation replaces the integral" in spectral_text and "regulated trace" in spectral_text,
    }
    qft_markers = {
        "finite_renormalization_freedom_explicit": "finite renormalization freedom classified by local covariant counterterms" in qft_text,
        "local_counterterm_affine_freedom_explicit": "addition of local covariant counterterms" in qft_text,
        "msbar_is_scheme_choice_explicit": "counterterms selected by" in qft_text and "allowed class" in qft_text,
    }

    relative_map = [[1, -1, 0], [0, -1, 1]]
    common_vector = [1, 1, 1]
    common_image = [sum(row[i] * common_vector[i] for i in range(3)) for row in relative_map]
    relative_rank = 2  # The first and third columns form the 2x2 identity minor.
    finite_source_exact = data["finite_source"]["closure_decision"]["automatic_finite_cutoff_exactness_for_A_N_closed"]
    csga1_closed = data["A84_gate"]["closed"]["CSGA1_derived_at_regime_local_action_tier"]
    bare_completeness = all(spectral_markers.values()) and finite_source_exact and csga1_closed

    bare = {
        "schema": "MTTFiniteProjectedSpectralActionBareCompleteness.v1",
        "status": "BARE_FINITE_SOURCE_ACTION_COMPLETE_AT_CORPUS_SPECTRAL_ACTION_TIER",
        "source_action": {
            "formula": "S_N[A]=P_EW Tr_N f_tau(D_A^2)",
            "selected_quadratic_restriction": "(1/2) Tr_HF(exp(-tau_int H_cl) Phi_C1^+ F^2)",
            "finite_source_algebra": "A_N",
            "finite_trace_exact": finite_source_exact,
        },
        "corpus_markers": spectral_markers,
        "relative_counterterm_space": {
            "coefficient_order": ["c_U1", "c_SU2", "c_SU3"],
            "quotient_map": relative_map,
            "rank": relative_rank,
            "common_normalization_kernel_vector": common_vector,
            "common_vector_image": common_image,
        },
        "theorem": {
            "name": "FiniteProjectedSpectralActionBareCompletenessLemma",
            "statement": "If the selected finite source action is the corpus spectral-action shadow S_N, its quadratic gauge Hessian is the complete bare gauge source. Adding a nonzero relative c_a F_a^2 term defines a different source action S_N+C rather than a further term left undetermined inside S_N. Hence the two A75 relative coordinates vanish at this bare source boundary.",
            "proof_steps": [
                "A84 identifies the selected heat-shadow gauge Hessian.",
                "The corpus spectral-action theorem identifies the coherent action shadow with the regulated proper-time trace.",
                "The selected finite projected algebra makes that trace an exact finite source object.",
                "The A75 quotient has rank two and kills only common normalization.",
                "A nonzero relative vector changes the defined source action, so it is excluded once S_N is selected as the complete bare source.",
            ],
            "proved_at_corpus_spectral_action_tier": bare_completeness,
        },
        "scope_guard": {
            "derived_from_primitive_MTT_core_axioms": False,
            "reason": "The corpus spectral-action result explicitly assumes a proper-time representation of the coherent fixed-point action.",
            "quantum_renormalization_scheme_fixed_by_this_lemma": False,
        },
    }

    scheme = {
        "schema": "MTTBareActionVsRenormalizedSchemeSeparation.v1",
        "status": "BARE_ACTION_COMPLETE_RENORMALIZED_FINITE_SCHEME_FREEDOM_RETAINED",
        "qft_corpus_markers": qft_markers,
        "theorem": {
            "name": "BareSourceAndRenormalizedMatchingSeparationLemma",
            "statement": "Completeness of the finite bare spectral action does not set all finite parts of renormalized time-ordered products. The latter form the local covariant counterterm freedom stated in the MTT QFT corpus and require a scheme or physical renormalization condition.",
            "proved": all(qft_markers.values()),
        },
        "current_profile_tier": {
            "selected_multiloop_common_scheme_fixed": data["multiloop_scheme"]["selected_multiloop_common_scheme_fixed"],
            "multiloop_threshold_mass_scheme_transport_closed": data["multiloop_scheme"]["multiloop_threshold_mass_scheme_transport_closed"],
            "accepted_precision_rows": data["multiloop_scheme"]["accepted_multiloop_precision_transport_rows"],
            "additional_gauge_source_primitive_added_here": 0,
        },
        "strict_no_knob_tier": {
            "renormalization_condition_derived_from_primitive_MTT_core": False,
            "official_joint_likelihood_imported": data["multiloop_scheme"]["official_joint_input_correlation_likelihood_imported"],
        },
    }

    ledger = {
        "schema": "MTTClosureShadowActionTierLedger.v1",
        "status": "CSGA1_AND_BARE_CSGA2_CLOSED_AT_CORPUS_ACTION_TIER_CURRENT_PROFILE_SCHEME_CLOSED",
        "clauses": {
            "CSGA1_heat_shadow": {
                "closed_at_regime_local_action_tier": csga1_closed,
                "source": "A84",
            },
            "CSGA2_bare_finite_source_completeness": {
                "closed_at_corpus_spectral_action_tier": bare_completeness,
                "derived_from_primitive_core_axioms": False,
            },
            "renormalized_common_scheme": {
                "closed_at_current_profile_tier": data["multiloop_scheme"]["selected_multiloop_common_scheme_fixed"],
                "closed_at_strict_primitive_no_knob_tier": False,
            },
        },
        "remaining_structural_action_clauses_at_corpus_action_current_profile_tier": 0,
        "remaining_structural_action_clauses_at_primitive_no_knob_tier": 1,
        "conditional_gauge_values_emitted_at_current_standard": data["A84_gate"]["conditional_gauge_values_emitted_at_current_standard"],
        "strict_gauge_values_accepted": 0,
        "new_continuous_numerical_parameters": 0,
        "new_discrete_numerical_parameters": 0,
        "next_strict_source_target": NEXT,
    }

    freeze = {
        "schema": "MTTProspectiveHeldOutGaugeValidationFreeze.v1",
        "status": "ACTION_SOURCE_HASH_FROZEN_PROSPECTIVE_HELDOUT_VALIDATION_NOT_YET_EXECUTED",
        "freeze": {
            "source_action_formula": bare["source_action"]["formula"],
            "gauge_K_rows": data["A83_hessian"]["gauge_covariantization"]["kinetic_rows"],
            "gauge_K_ratios": data["A83_hessian"]["gauge_covariantization"]["ratios"],
            "authority_hashes": [{"path": str(path), "sha256": sha256(path)} for path in paths.values()],
        },
        "prospective_acceptance": {
            "eligible_data": "A common-scheme gauge observable or coupling combination not used to select H_cl, Phi_C1, tau_int, or the action boundary and fixed after this source freeze.",
            "required_test": "Run the frozen action and declared RG/scheme transport without retuning, then report residual and covariance pull.",
            "failure_rule": "A statistically significant incompatible held-out result falsifies this selected source branch; it may not be repaired by a new sector-relative matching term.",
        },
        "held_out_validation_executed": False,
        "reason": "The present gauge profile was available during construction and is a diagnostic/replay check, not an independent prospective prediction.",
    }

    checks = {
        "spectral_markers": all(spectral_markers.values()),
        "qft_markers": all(qft_markers.values()),
        "finite_source_exact": finite_source_exact,
        "CSGA1_imported": csga1_closed,
        "relative_rank_two": relative_rank == data["A75_counterterm"]["theorem"]["relative_rank"],
        "common_normalization_is_kernel": common_image == [0, 0],
        "bare_CSGA2_closed_at_stated_tier": bare_completeness,
        "primitive_no_knob_not_overclaimed": not bare["scope_guard"]["derived_from_primitive_MTT_core_axioms"],
        "renormalized_scheme_freedom_retained": scheme["theorem"]["proved"],
        "current_profile_scheme_closed": scheme["current_profile_tier"]["selected_multiloop_common_scheme_fixed"],
        "heldout_not_backdated": not freeze["held_out_validation_executed"],
        "no_new_numeric_parameters": ledger["new_continuous_numerical_parameters"] == 0 and ledger["new_discrete_numerical_parameters"] == 0,
    }
    candidate = {
        "schema": "MTTSelectedFiniteMatchingCompletenessFromUnifiedActionOrExplicitBoundaryAdoptionAndHeldoutValidation.v1",
        "status": STATUS,
        "results": {
            "CSGA1_closed_at_regime_local_action_tier": csga1_closed,
            "CSGA2_bare_source_closed_at_corpus_spectral_action_tier": bare_completeness,
            "CSGA2_derived_from_primitive_MTT_core_axioms": False,
            "renormalized_scheme_closed_at_current_profile_tier": scheme["current_profile_tier"]["selected_multiloop_common_scheme_fixed"],
            "renormalized_scheme_closed_at_strict_no_knob_tier": False,
            "remaining_action_clauses_at_current_standard": 0,
            "strict_gauge_values_accepted": 0,
            "conditional_gauge_values_emitted": ledger["conditional_gauge_values_emitted_at_current_standard"],
            "held_out_validation_executed": False,
            "new_continuous_numerical_parameters": 0,
            "new_discrete_numerical_parameters": 0,
        },
        "outputs": {
            "bare_completeness": str(BARE.relative_to(ROOT)).replace("\\", "/"),
            "scheme_separation": str(SCHEME.relative_to(ROOT)).replace("\\", "/"),
            "tier_ledger": str(LEDGER.relative_to(ROOT)).replace("\\", "/"),
            "heldout_freeze": str(FREEZE.relative_to(ROOT)).replace("\\", "/"),
        },
        "checks": checks,
        "authority_hashes": [{"path": str(path), "sha256": sha256(path)} for path in paths.values()],
        "next_required_artifact": NEXT,
    }
    cert = {
        "certificate": "MTT_Selected_FiniteMatchingCompletenessFromUnifiedAction_or_ExplicitBoundaryAdoptionAndHeldOutValidation_v1",
        "status": STATUS,
        "CSGA2_bare_source_closed_at_corpus_spectral_action_tier": bare_completeness,
        "CSGA2_derived_from_primitive_MTT_core_axioms": False,
        "renormalized_scheme_closed_at_current_profile_tier": scheme["current_profile_tier"]["selected_multiloop_common_scheme_fixed"],
        "renormalized_scheme_closed_at_strict_no_knob_tier": False,
        "relative_counterterm_rank": relative_rank,
        "remaining_action_clauses_at_current_standard": 0,
        "strict_gauge_values_accepted": 0,
        "conditional_gauge_values_emitted": ledger["conditional_gauge_values_emitted_at_current_standard"],
        "held_out_validation_executed": False,
        "new_continuous_numerical_parameters": 0,
        "new_discrete_numerical_parameters": 0,
        "next_required_artifact": NEXT,
    }
    note = f"""# MTT Selected Finite Matching Completeness from Unified Action or Explicit Boundary Adoption and Held-Out Validation v1

## Bare finite-source theorem

The remaining A84 action clause splits into a bare source question and a renormalized-scheme question.
They are not the same statement.

The corpus spectral-action paper assumes a proper-time representation for the coherent fixed-point
action and then identifies its coherent truncation shadow with the regulated spectral trace. The
repository independently proves that the selected `A_N` source algebra, projected operations, and
finite trace are exact. Together with A84, this gives the exact bare source action

```text
S_N[A] = P_EW Tr_N f_tau(D_A^2),
S_N^(2)[F] = (1/2) Tr_HF(exp(-tau_int H_cl) Phi_C1^+ F^2).
```

The A75 relative quotient has rank two. Once `S_N` is selected as the complete bare source, adding
nonzero relative coefficients defines a different action `S_N+C`; it is not an undetermined term
inside `S_N`. Thus bare CSGA2 is closed at the corpus spectral-action tier.

This is not promoted to a theorem from primitive MTT core axioms. The corpus result explicitly assumes
the proper-time representation of the coherent fixed-point action.

## Renormalized scheme is separate

The MTT QFT corpus correctly states that renormalized time-ordered products retain finite local
covariant counterterm freedom. Bare spectral-action completeness therefore does not make a
renormalization scheme disappear. The already selected common-scheme multi-loop transport fixes that
freedom at the current profile tier, with no new gauge primitive introduced here. Strict primitive
no-knob selection of the renormalization condition remains stronger and open.

Accordingly, both CSGA clauses and the common scheme are closed at the declared current standard;
strict gauge values remain `0` because source promotion of `Phi_C1` and the absolute normalization are
separate obligations. The next strict target is `{NEXT}`.

## Held-out rule

The action formula, three K rows, ratios, and authority hashes are frozen by the executable packet.
The current gauge profile cannot be backdated into a held-out prediction because it was known during
construction. A future or otherwise genuinely unused common-scheme gauge observable must be evaluated
without retuning; failure may not be repaired by adding a sector-relative matching term.
"""

    for path, payload in [
        (BARE, bare),
        (SCHEME, scheme),
        (LEDGER, ledger),
        (FREEZE, freeze),
        (CANDIDATE, candidate),
        (CERT, cert),
    ]:
        dump(path, payload)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
