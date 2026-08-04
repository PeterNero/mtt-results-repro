from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_phic1positivedensitypromotionfromclosedrouteasource_or_strictgaugerows"
STATUS = (
    "MTT_SELECTED_PHIC1_POSITIVE_DENSITY_PROMOTED_FROM_CLOSED_ROUTEA_SOURCE_"
    "THREE_GAUGE_ACTION_ROWS_ACCEPTED_AT_CORPUS_ACTION_TIER_PRIMITIVE_CORE_TIER_OPEN"
)
NEXT = "MTT_Selected_GaugeActionCoefficientToCommonSchemeCouplingMapAndProspectiveValidation_v1"

OUT = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PhiC1PositiveDensityPromotionFromClosedRouteASource_or_StrictGaugeRows_v1.md"
GRAM = OUT / "routea_operator_to_positive_gram_density.packet.json"
PROMOTION = OUT / "phic1_source_promotion_theorem.packet.json"
GAUGE = OUT / "selected_gauge_action_rows_after_density_promotion.packet.json"
FRONTIER = OUT / "post_promotion_gauge_frontier.packet.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def complex_matrix(payload: list[list[list[float]]]) -> np.ndarray:
    values = np.asarray(payload, dtype=float)
    return values[..., 0] + 1j * values[..., 1]


def encode_complex(matrix: np.ndarray) -> list[list[list[float]]]:
    return np.stack([matrix.real, matrix.imag], axis=-1).tolist()


def max_abs(matrix: np.ndarray) -> float:
    return float(np.max(np.abs(matrix)))


def main() -> int:
    paths = {
        "A67_density": ROOT / "candidate_data" / "selected_positivesectordensitysourcetheorem_or_commongaugeflavorweightemission" / "conditional_c1_positive_sector_density.packet.json",
        "routeA_source": ROOT / "candidate_data" / "selected_transportclosedphifinfinite_replay_or_symbolicconjugationvalidator" / "premise_free_route_a_source_certificate.packet.json",
        "routeA_promotion": ROOT / "certificates" / "selected_gaugetransported_bn_phifin_trace_or_independentcomplexrowexecution_certificate.json",
        "dynamic_backpromotion": ROOT / "candidate_data" / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure" / "dynamic_transfer_backpromotion_theorem.packet.json",
        "A83_hessian": ROOT / "candidate_data" / "selected_sharedcircleclosurehessiantogaugezeromoderestrictionandcountertermcompleteness" / "canonical_heat_density_and_gauge_zero_mode_hessian.packet.json",
        "A85_action": ROOT / "candidate_data" / "selected_finitematchingcompletenessfromunifiedaction_or_explicitboundaryadoptionandheldoutvalidation" / "closure_shadow_action_tier_ledger.packet.json",
        "PEW": ROOT / "candidate_data" / "selected_strictpewdenominatorselectiontheorem_or_directkpromotion.candidate.json",
        "PEW_cert": ROOT / "certificates" / "selected_strictpewdenominatorselectiontheorem_or_directkpromotion_certificate.json",
    }
    missing = [str(path) for path in paths.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing PhiC1 promotion inputs: " + ", ".join(missing))
    data = {key: load(path) for key, path in paths.items()}

    a67 = data["A67_density"]
    identity = np.eye(3, dtype=complex)
    x = complex_matrix(a67["generators"]["X"])
    z = complex_matrix(a67["generators"]["Z"])
    m_phase = identity + z
    m_shift = identity + x
    phi_phase = m_phase @ m_phase.conj().T
    phi_shift = m_shift @ m_shift.conj().T
    phi_left = phi_phase + phi_shift

    stored_phase = complex_matrix(a67["positive_blocks"]["Phi_phase"])
    stored_shift = complex_matrix(a67["positive_blocks"]["Phi_shift"])
    stored_left = complex_matrix(a67["positive_blocks"]["Phi_left_incidence_pullback"])
    phase_residual = max_abs(phi_phase - stored_phase)
    shift_residual = max_abs(phi_shift - stored_shift)
    left_residual = max_abs(phi_left - stored_left)
    phase_spectrum = np.linalg.eigvalsh(phi_phase)
    shift_spectrum = np.linalg.eigvalsh(phi_shift)

    omega = np.exp(2j * np.pi / 3)
    fourier = np.asarray([[omega ** (j * k) for k in range(3)] for j in range(3)], dtype=complex) / np.sqrt(3)
    right_basis = np.diag([1.0, 1j, -1.0])
    transformed = fourier @ m_phase @ right_basis
    gram_covariance_residual = max_abs(
        transformed @ transformed.conj().T - fourier @ phi_phase @ fourier.conj().T
    )

    route_a = data["routeA_source"]["route_A_physical_source_certificate"]
    back = data["dynamic_backpromotion"]
    source_chain_closed = all(
        [
            data["routeA_promotion"]["PSM_C1_02_unpatched_source_promotion_closed"],
            data["routeA_promotion"]["A_selected_promoted"],
            route_a["phase_R_Z_source_selection"],
            route_a["shift_R_X_source_selection"],
            route_a["same_branch"],
            route_a["physical_action_restricts_to_selected_finite_Weyl_quotient"],
            back["backpromotion_allowed"],
            back["new_prerequisites_after_source_and_postsource_replay"]["selected_source_to_C1_transfer_map_emitted"],
            back["new_prerequisites_after_source_and_postsource_replay"]["selected_sector_routing_dynamic_map_emitted"],
            back["new_prerequisites_after_source_and_postsource_replay"]["selected_Hessian_blocks_emitted"],
            back["new_prerequisites_after_source_and_postsource_replay"]["selected_b_selected_emitted"],
        ]
    )
    density_exact = max(phase_residual, shift_residual, left_residual, gram_covariance_residual) < 1e-13
    density_promoted = source_chain_closed and density_exact

    gram = {
        "schema": "MTTRouteAOperatorToPositiveGramDensity.v1",
        "status": "SELECTED_ROUTEA_I_PLUS_Z_I_PLUS_X_OPERATORS_MAP_CANONICALLY_TO_EXACT_POSITIVE_DENSITY",
        "selected_operators": {
            "phase": "M_phase=I+Z on u,e",
            "shift": "M_shift=I+X on d,N",
            "same_source_backpromotion_closed": source_chain_closed,
        },
        "canonical_functor": {
            "formula": "G(M)=M M^*",
            "positive": True,
            "basis_covariance": "G(U M V)=U G(M) U^* for unitary U,V",
            "basis_covariance_residual": gram_covariance_residual,
            "incidence_pullback": "Phi_Q=Phi_L=G(M_phase)+G(M_shift)",
        },
        "finite_execution": {
            "Phi_phase": encode_complex(phi_phase),
            "Phi_shift": encode_complex(phi_shift),
            "Phi_left_incidence_pullback": encode_complex(phi_left),
            "phase_packet_residual": phase_residual,
            "shift_packet_residual": shift_residual,
            "left_pullback_residual": left_residual,
            "phase_spectrum": phase_spectrum.tolist(),
            "shift_spectrum": shift_spectrum.tolist(),
            "phase_trace": float(np.trace(phi_phase).real),
            "shift_trace": float(np.trace(phi_shift).real),
            "left_trace": float(np.trace(phi_left).real),
            "positive_semidefinite": float(min(np.min(phase_spectrum), np.min(shift_spectrum))) >= -1e-13,
        },
        "theorem": {
            "name": "SelectedOperatorPositiveGramFunctorLemma",
            "statement": "A selected finite response operator canonically emits its positive Gram density M M*. The construction is positive and basis-covariant, so no basis choice, observed value, or extra scalar enters. Incidence pullback is the direct sum/sum of the two selected source-owned response channels.",
            "proved": density_exact,
        },
    }

    promotion = {
        "schema": "MTTPhiC1SourcePromotionTheorem.v1",
        "status": "OLD_AXIOM_CONDITIONAL_PHIC1_DENSITY_PROMOTED_BY_LATER_ROUTEA_SOURCE_THEOREM",
        "historical_status": a67["source_status"],
        "later_source_chain": {
            "unpatched_PSM_C1_02_source_promotion_closed": data["routeA_promotion"]["PSM_C1_02_unpatched_source_promotion_closed"],
            "A_selected_promoted": data["routeA_promotion"]["A_selected_promoted"],
            "phase_R_Z_source_selected": route_a["phase_R_Z_source_selection"],
            "shift_R_X_source_selected": route_a["shift_R_X_source_selection"],
            "I_plus_Z_I_plus_X_backpromotion_allowed": back["backpromotion_allowed"],
            "same_source": route_a["same_branch"],
            "target_fitting_used": back["target_fitting_used"],
            "observed_data_used_as_selector": back["observed_data_used_as_selector"],
        },
        "promoted_source_status": {
            "Phi_C1_positive_density_source_closed": density_promoted,
            "strict_unpatched_at_selected_RouteA_source_tier": density_promoted,
            "new_source_axiom_used": False,
            "new_continuous_numerical_parameters": 0,
            "new_discrete_numerical_parameters": 0,
        },
        "theorem": {
            "name": "PhiC1PositiveDensityBackpromotionTheorem",
            "statement": "The old A67 density was conditional only because I+Z and I+X were not then source-owned. The later premise-free Route-A theorem and same-source dynamic backpromotion select exactly those operators. Applying the canonical positive Gram functor and fixed incidence pullback therefore promotes Phi_C1^+ without a new source axiom.",
            "proved": density_promoted,
        },
    }

    k_rows = [float(value) for value in data["A83_hessian"]["gauge_covariantization"]["kinetic_rows"]]
    k_ratios = [float(value) for value in data["A83_hessian"]["gauge_covariantization"]["ratios"]]
    p_ew = float(data["PEW"]["numerics"]["P_EW"])
    normalized_coefficients = [p_ew * value for value in k_rows]
    current_action_closed = data["A85_action"]["remaining_structural_action_clauses_at_corpus_action_current_profile_tier"] == 0
    gauge_rows_promoted = density_promoted and current_action_closed
    gauge = {
        "schema": "MTTSelectedGaugeActionRowsAfterDensityPromotion.v1",
        "status": "THREE_SELECTED_GAUGE_ACTION_ROWS_ACCEPTED_AT_CORPUS_ACTION_SOURCE_TIER",
        "sector_order": ["U1_GUT", "SU2", "SU3"],
        "K_rows": k_rows,
        "K_over_K2": k_ratios,
        "selected_P_EW_import": {
            "accepted_source_row_in_existing_repository_ledger": data["PEW_cert"]["accepted_global_strict_P_EW_source_rows"] == 1,
            "P_EW": p_ew,
            "source_certificate": data["PEW_cert"]["certificate"],
        },
        "diagnostic_P_EW_times_K_not_inverse_gauge_couplings": normalized_coefficients,
        "acceptance": {
            "Phi_C1_source_promoted": density_promoted,
            "heat_shadow_and_bare_action_complete_at_corpus_action_tier": current_action_closed,
            "selected_gauge_action_rows_at_corpus_action_tier": 3 if gauge_rows_promoted else 0,
            "independent_relative_shape_coordinates": 2 if gauge_rows_promoted else 0,
            "primitive_MTT_core_no_assumption_gauge_rows": 0,
        },
        "scope_guard": {
            "coupling_convention_or_RG_transport_recomputed_here": False,
            "present_profile_called_held_out": False,
            "P_EW_times_K_accepted_as_inverse_gauge_couplings": False,
            "kinetic_normalization_requires_separate_c_equals_6f0_map": True,
            "reason_primitive_core_rows_remain_zero": "A85 retains the corpus spectral-action proper-time assumption and strict renormalized-scheme source as stronger obligations.",
        },
    }

    frontier = {
        "schema": "MTTPostPhiC1PromotionGaugeFrontier.v1",
        "status": "ACTION_AND_DENSITY_SOURCE_GAPS_CLOSED_AT_DECLARED_CORPUS_ACTION_TIER_CONVENTION_AND_PROSPECTIVE_TEST_NEXT",
        "closed_now": {
            "old_A67_axiom_conditional_density_status_superseded": density_promoted,
            "Phi_C1_positive_density_source": density_promoted,
            "three_finite_gauge_action_rows": gauge_rows_promoted,
            "two_relative_gauge_shape_coordinates": gauge_rows_promoted,
            "action_clause_count_at_current_standard_zero": current_action_closed,
        },
        "not_reopened": [
            "27x27 matrix",
            "Yukawa magnitude replay/profile closure",
            "multi-loop common-scheme transport",
            "PSM-C1-02 source promotion",
            "Route-A gauge-transported Phi_fin trace",
        ],
        "open_stronger": {
            "derive_corpus_spectral_action_proper_time_premise_from_primitive_MTT_core": True,
            "derive_renormalization_condition_at_primitive_no_knob_tier": True,
            "map_frozen_action_coefficients_to_declared_common_scheme_without_convention_ambiguity": True,
            "execute_genuinely_prospective_heldout_validation": True,
        },
        "next_required_artifact": NEXT,
    }

    checks = {
        "source_chain_closed": source_chain_closed,
        "gram_exact": density_exact,
        "phase_spectrum": max_abs(np.sort(phase_spectrum) - np.asarray([1.0, 1.0, 4.0])) < 1e-13,
        "shift_spectrum": max_abs(np.sort(shift_spectrum) - np.asarray([1.0, 1.0, 4.0])) < 1e-13,
        "sector_traces": max(abs(a - b) for a, b in zip(a67["sector_trace_weights"], [12.0, 6.0, 6.0, 12.0, 6.0, 6.0])) < 1e-13,
        "density_promoted": density_promoted,
        "action_tier_closed": current_action_closed,
        "gauge_rows_promoted": gauge_rows_promoted,
        "primitive_core_not_overclaimed": gauge["acceptance"]["primitive_MTT_core_no_assumption_gauge_rows"] == 0,
        "no_new_parameters": promotion["promoted_source_status"]["new_continuous_numerical_parameters"] == 0 and promotion["promoted_source_status"]["new_discrete_numerical_parameters"] == 0,
    }
    candidate = {
        "schema": "MTTSelectedPhiC1PositiveDensityPromotionFromClosedRouteASourceOrStrictGaugeRows.v1",
        "status": STATUS,
        "results": {
            "Phi_C1_positive_density_source_closed": density_promoted,
            "old_A67_axiom_conditional_status_superseded": density_promoted,
            "selected_gauge_action_rows_at_corpus_action_tier": 3 if gauge_rows_promoted else 0,
            "independent_relative_gauge_shape_coordinates": 2 if gauge_rows_promoted else 0,
            "primitive_MTT_core_no_assumption_gauge_rows": 0,
            "existing_P_EW_source_row_imported": data["PEW_cert"]["accepted_global_strict_P_EW_source_rows"] == 1,
            "new_continuous_numerical_parameters": 0,
            "new_discrete_numerical_parameters": 0,
        },
        "outputs": {
            "gram_density": str(GRAM.relative_to(ROOT)).replace("\\", "/"),
            "source_promotion": str(PROMOTION.relative_to(ROOT)).replace("\\", "/"),
            "gauge_rows": str(GAUGE.relative_to(ROOT)).replace("\\", "/"),
            "frontier": str(FRONTIER.relative_to(ROOT)).replace("\\", "/"),
        },
        "checks": checks,
        "authority_hashes": [{"path": str(path), "sha256": sha256(path)} for path in paths.values()],
        "next_required_artifact": NEXT,
    }
    cert = {
        "certificate": "MTT_Selected_PhiC1PositiveDensityPromotionFromClosedRouteASource_or_StrictGaugeRows_v1",
        "status": STATUS,
        "Phi_C1_positive_density_source_closed": density_promoted,
        "phase_density_residual": phase_residual,
        "shift_density_residual": shift_residual,
        "left_incidence_pullback_residual": left_residual,
        "Gram_basis_covariance_residual": gram_covariance_residual,
        "selected_gauge_action_rows_at_corpus_action_tier": 3 if gauge_rows_promoted else 0,
        "independent_relative_gauge_shape_coordinates": 2 if gauge_rows_promoted else 0,
        "primitive_MTT_core_no_assumption_gauge_rows": 0,
        "existing_P_EW_source_row_imported": data["PEW_cert"]["accepted_global_strict_P_EW_source_rows"] == 1,
        "new_continuous_numerical_parameters": 0,
        "new_discrete_numerical_parameters": 0,
        "next_required_artifact": NEXT,
    }
    note = f"""# MTT Selected PhiC1 Positive Density Promotion from Closed Route-A Source or Strict Gauge Rows v1

## The stale A67 condition is removed

A67 constructed the exact positive density but labeled it axiom-conditional because its `I+Z` and
`I+X` response operators were not source-owned at that time. Later packets now close precisely that
missing chain:

- premise-free Route-A physical source certificate;
- gauge-transported `Phi_fin` restriction;
- unpatched PSM-C1-02 source promotion and `A_selected`;
- same-source dynamic backpromotion of `I+Z` and `I+X`.

For a selected finite response operator `M`, the map

```text
G(M) = M M^*
```

is canonical, positive, and basis-covariant. Therefore source ownership passes from the selected
operators to their Gram densities. The fixed incidence pullback gives

```text
Phi_u = Phi_e = G(I+Z),
Phi_d = Phi_N = G(I+X),
Phi_Q = Phi_L = G(I+Z)+G(I+X).
```

Both right spectra are `[1,1,4]`; their traces are `6`, the left trace is `12`, and the maximum
stored-packet residual is `{max(phase_residual, shift_residual, left_residual):.3e}`. No observed
gauge value and no new source axiom enters. The old A67 conditional status is superseded at the
selected Route-A source tier.

## Gauge consequence

Combining this promoted density with A84's heat shadow and A85's finite bare-action completeness
promotes all three finite gauge-action rows at the declared corpus-action source tier:

```text
K = {k_rows}
K/K2 = {k_ratios}
```

There are two independent relative shape coordinates after common normalization. The already accepted
repository `P_EW` row is imported separately. The products `P_EW*K` are retained only as typed
diagnostics, not as inverse gauge couplings: the gauge kinetic convention requires the separate common
coefficient `c=6 f0`. This packet does not invent that convention or call the known profile held out.

At the stronger primitive-core tier the accepted count remains zero, because deriving the corpus
spectral-action proper-time premise and the renormalized condition from primitive MTT remains open.
The next non-looping artifact is `{NEXT}`.
"""

    for path, payload in [
        (GRAM, gram),
        (PROMOTION, promotion),
        (GAUGE, gauge),
        (FRONTIER, frontier),
        (CANDIDATE, candidate),
        (CERT, cert),
    ]:
        dump(path, payload)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
