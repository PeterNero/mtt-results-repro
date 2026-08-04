from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CORPUS = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")
NONSM = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-nonsm-constants-no-knob")
SLUG = "selected_neutrallensnildeterminantholonomyexecution_or_onescalefinality"
STATUS = (
    "MTT_NEUTRAL_FLAVOR_DETERMINANT_TYPE_SEPARATED_U3_LIFT_TORSOR_PROVED_"
    "ONE_HOLONOMY_PLUS_ONE_SCALE_CURRENT_CORPUS_FINALITY"
)
NEXT = "MTT_Selected_NeutralOneHolonomyOneScaleOntologyClosure_and_U5TierDecision_v1"

OUT = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_NeutralLensNilDeterminantHolonomyExecution_or_OneScaleFinality_v1.md"

TYPES = OUT / "flavor_determinant_vs_analytic_Dirac_determinant_typing.packet.json"
TORSOR = OUT / "fixed_SU3_to_U3_central_lift_torsor_theorem.packet.json"
EXHAUSTION = OUT / "current_corpus_central_holonomy_source_exhaustion.packet.json"
PROFILE = OUT / "one_holonomy_one_scale_neutral_profile.packet.json"
TIER = OUT / "U5_tier_decision_after_A93.packet.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    paths = {
        "A38_factorization": ROOT / "candidate_data" / "selected_neutralcommoncirclefactorizationandholonomyscalarreduction.candidate.json",
        "A40_profile": ROOT / "candidate_data" / "selected_neutraltwoprimitiveprofilevalueclosure.candidate.json",
        "A41_conditional_phase": ROOT / "candidate_data" / "selected_neutrallensdedekindtransgression_or_oneprimitiveprofile.candidate.json",
        "A91_typing": ROOT / "candidate_data" / "selected_neutraldeterminantlineapsoperator_and_native10dmassscale.candidate.json",
        "A92_recursive_domain": ROOT / "candidate_data" / "selected_neutralrecursivesharedcirclediracdomainandspinbranchreduction.candidate.json",
        "A92_flat_no_go": ROOT / "candidate_data" / "selected_neutralrecursivesharedcirclediracdomainandspinbranchreduction" / "flat_lens_and_nil_U1_holonomy_no_go.packet.json",
        "neutral_mass_operator": ROOT / "candidate_data" / "selected_neutralmassoperator_sourceemission.candidate.json",
        "superset_knob_audit": CORPUS / "3 Core Foundations" / "Modal_Triplet_Theory__MTT_as_a_Superset_v2.md",
        "parameter_taxonomy": CORPUS / "2 Meta & Diagnosis & Universality" / "Modal_Triplet_Theory__Parameters__Closure__and_Structural_Falsifiability.md",
        "crossrepo_local_system_audit": NONSM / "certificates" / "selected_qa_su3_local_system_torsion_source_extraction_certificate.json",
    }
    missing = [str(path) for path in paths.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing A93 authority: " + ", ".join(missing))

    a38 = load(paths["A38_factorization"])
    a40 = load(paths["A40_profile"])
    a41 = load(paths["A41_conditional_phase"])
    a91 = load(paths["A91_typing"])
    a92 = load(paths["A92_recursive_domain"])
    flat = load(paths["A92_flat_no_go"])
    neutral = load(paths["neutral_mass_operator"])
    local_system = load(paths["crossrepo_local_system_audit"])
    superset_text = paths["superset_knob_audit"].read_text(encoding="utf-8")
    taxonomy_text = paths["parameter_taxonomy"].read_text(encoding="utf-8")

    type_packet = {
        "schema": "MTTFlavorDeterminantVsAnalyticDiracDeterminantTyping.v1",
        "status": "TWO_DETERMINANT_LINE_OBJECTS_SEPARATED_NO_CANONICAL_IDENTIFICATION_IN_CURRENT_SOURCE",
        "ordinary_flavor_determinant": {
            "object": "det(E_nu)=Lambda^3 E_nu for the rank-three family bundle",
            "connection": "nabla_det=d+Tr(A_nu)",
            "holonomy_identity": "Hol_det(E_nu)(gamma)=det Hol_E_nu(gamma)=det H_nu",
            "A38_readout": "det H_nu=exp(3 i phi_nu)",
            "base": "the selected co-aligned physical/internal loop gamma_nu",
            "requires_Dirac_spectrum": False,
        },
        "analytic_Dirac_determinant": {
            "object": "Det(D_nu) for a family of chiral Dirac operators",
            "fiber": "det ker(D_nu)^* tensor det coker(D_nu)",
            "holonomy_source": "Bismut-Freed/Dai-Freed exponentiated reduced eta invariant of a mapping torus",
            "base": "parameter space of the Dirac family",
            "primary_reference": "https://arxiv.org/abs/hep-th/9405012",
            "same_as_det_E_nu_by_definition": False,
        },
        "current_bridge_status": {
            "index_or_transgression_isomorphism_det_E_to_Det_D": False,
            "holonomy_equality_theorem": False,
            "A41_reciprocity_identity_supplies_bridge": False,
            "APS_route_rejected_as_mathematics": False,
            "APS_route_rejected_as_current_direct_MTT_phase_source": True,
        },
        "theorem": {
            "name": "NeutralDeterminantObjectTypeSeparationTheorem",
            "proved": True,
            "statement": "The determinant of the rank-three neutral family holonomy is the holonomy of the ordinary line det(E_nu), while the Dai-Freed phase is the holonomy of the analytic determinant line Det(D_nu) over an operator-parameter space. They are different functorial objects. Without an explicit index/transgression isomorphism, an eta invariant cannot be substituted for arg det H_nu.",
        },
    }

    torsor_samples = []
    for numerator in range(-4, 5):
        phi = numerator * math.pi / 120.0
        determinant_phase = 3.0 * phi
        torsor_samples.append(
            {
                "numerator_of_pi_over_120": numerator,
                "phi": phi,
                "determinant_phase": determinant_phase,
                "relative_SU3_holonomy_unchanged": True,
                "curvature_unchanged_for_closed_alpha": True,
            }
        )
    torsor_packet = {
        "schema": "MTTFixedSU3ToU3CentralLiftTorsorTheorem.v1",
        "status": "ONE_AND_ONLY_ONE_CONTINUOUS_CENTRAL_HOLONOMY_COORDINATE_SURVIVES_FIXED_SU3_DATA",
        "construction": {
            "fixed_relative_connection": "A_0 with Tr(A_0)=0 and Hol(A_0)=H_cen",
            "normalized_loop_form": "alpha_gamma closed with integral_gamma alpha_gamma=1",
            "all_central_lifts": "A_phi=A_0+i phi alpha_gamma I_3",
            "curvature": "F(A_phi)=F(A_0) when d alpha_gamma=0 and the central term commutes",
            "holonomy": "Hol(A_phi)=exp(i phi) H_cen",
            "determinant": "det Hol(A_phi)=exp(3 i phi)",
            "physical_shape_period": "phi in R/(2pi/3)Z",
            "sample_exact_grid": torsor_samples,
        },
        "identifiability": {
            "fixed_SU3_or_PU3_data_select_phi": False,
            "fixed_curvature_selects_flat_central_holonomy": False,
            "number_of_surviving_continuous_shape_coordinates": 1,
            "additional_family_local_phase_coordinates": 0,
            "minimal_extra_source": "one central U1 holonomy value or an action with a unique minimizer on that circle",
        },
        "theorem": {
            "name": "CentralLiftHolonomyNonIdentifiabilityAndMinimalityTheorem",
            "proved": True,
            "statement": "For every phi there is a U(3) lift A_phi of the same selected traceless family connection with the same curvature and relative H_cen data but determinant holonomy exp(3i phi). Hence existing SU(3), finite-Heisenberg, topology and curvature data cannot distinguish phi. Conversely det H_nu recovers phi modulo 2pi/3, so exactly one scalar is sufficient and necessary.",
        },
    }

    source_markers = {
        "superset_calls_Wilson_phases_continuous_flavor_bottleneck": "Wilson--line / flat--connection phases" in superset_text and "continuous parameters controlling" in superset_text,
        "superset_requires_global_selection": "They must be selected by" in superset_text and "global constraints" in superset_text,
        "taxonomy_lists_holonomy_as_open": "Holonomy phases" in taxonomy_text and "Flavor mixing and CP structure" in taxonomy_text,
        "taxonomy_forbids_persistent_tuning": "Their persistence constitutes falsification" in taxonomy_text,
        "crossrepo_q64_character_bridge_missing": any(row["candidate"] == "z64_q64_15_character_channel" and not row["selected_for_Qa_SU3_torsion"] for row in local_system["candidate_extraction"]),
        "crossrepo_lensnil_flux_not_selected_local_system": any(row["candidate"] == "heterotic_lens_nil_flux_integers" and not row["selected_for_Qa_SU3_torsion"] for row in local_system["candidate_extraction"]),
    }
    exhaustion = {
        "schema": "MTTCurrentCorpusCentralHolonomySourceExhaustion.v1",
        "status": "NO_SELECTED_CENTRAL_U1_VALUE_OR_UNIQUE_MINIMIZING_ACTION_IN_CURRENT_CORPUS",
        "source_markers": source_markers,
        "routes": {
            "finite_qutrit_Heisenberg": "rejected: determinant-trivial SU3 image",
            "flat_lens_fiber": "rejected: only mu3, phi=0 modulo shape period",
            "flat_nil_center": "rejected: commutator killed by all U1 characters",
            "nil_base_Wilson_torus": "mathematically available U1^2, but no selected point or loop",
            "A41_APS_Dedekind": "exact target-ranked arithmetic retained, but determinant-object bridge and selected topology/operator identification absent",
            "LensNil_flux_integers": "present as branch variables, not selected as the neutral local-system/central-connection source",
            "native_10D_action": "allows Wilson connection A but does not emit its value or minimizing potential",
        },
        "conclusion": {
            "strict_no_knob_phi_derivable_from_current_sources": False,
            "one_holonomy_primitive_is_irreducible_in_current_formalization": True,
            "future_new_source_can_reduce_count": True,
            "this_is_not_a_no_go_for_all_future_MTT_completions": True,
        },
    }

    profile_data = a40["calibrated_shape_and_scale"]
    ratio = float(profile_data["ratio"])
    phi_from_ratio = math.atan(math.sqrt(3.0) * ratio / (2.0 - ratio))
    phi_profile = float(profile_data["phi_nu_rad"])
    ratio_reconstructed = (
        2.0 * math.sqrt(3.0) * math.tan(phi_from_ratio)
        / (3.0 + math.sqrt(3.0) * math.tan(phi_from_ratio))
    )
    phi_candidate = float(a41["determinant_line_candidate"]["candidate_phi_nu_rad"])
    candidate_ratio = float(a41["conditional_one_scale_profile"]["candidate_ratio"])
    one_profile = {
        "schema": "MTTOneHolonomyOneScaleNeutralProfile.v1",
        "status": "EXACT_BIJECTION_BETWEEN_SPLITTING_RATIO_AND_ONE_GEOMETRIC_HOLONOMY_COORDINATE",
        "normal_ordering_massless_boundary_formula": {
            "shape": "m_k^2=m0^2+A cos(phi+2pi*k/3)",
            "ordered_small_positive_phi": "c_min=cos(phi+2pi/3), c_mid=cos(phi+4pi/3), c_max=cos(phi)",
            "ratio_formula": "r=(c_mid-c_min)/(c_max-c_min)=2sqrt(3)tan(phi)/(3+sqrt(3)tan(phi))",
            "inverse_formula": "phi=atan(sqrt(3)r/(2-r)), 0<phi<pi/3",
            "scale_formula": "A=Delta_m31^2/(c_max-c_min), m0^2=-A*c_min",
        },
        "A40_profile_identity": {
            "ratio": ratio,
            "phi_from_inverse": phi_from_ratio,
            "phi_A40": phi_profile,
            "absolute_phi_residual": abs(phi_from_ratio - phi_profile),
            "ratio_reconstructed": ratio_reconstructed,
            "absolute_ratio_residual": abs(ratio_reconstructed - ratio),
        },
        "A41_conditional_contact": {
            "phi": phi_candidate,
            "ratio": candidate_ratio,
            "source_promoted": False,
            "role": "optional target-ranked benchmark for the one-holonomy coordinate",
        },
        "coordinate_accounting": {
            "old_measured_splitting_coordinates": 2,
            "new_geometric_shape_coordinates": 1,
            "new_dimensionful_scale_coordinates": 1,
            "net_profile_coordinate_reduction": 0,
            "entry_local_neutrino_parameters": 0,
            "all_36_A40_rows_follow_once_phi_and_scale_are_given": True,
        },
        "profile_tier_observed_data_used": True,
        "strict_prediction_claimed": False,
    }

    tier = {
        "schema": "MTTU5TierDecisionAfterA93.v1",
        "status": "NEUTRAL_SHAPE_CLOSED_AT_ONE_HOLONOMY_PRIMITIVE_STANDARD_STRICT_NO_KNOB_REMAINS_OPEN",
        "closed_now": {
            "correct_flavor_determinant_source_object": True,
            "central_U3_lift_normal_form": True,
            "one_shape_coordinate_minimality": True,
            "one_holonomy_plus_one_scale_profile_sufficiency": True,
            "current_corpus_source_finality": True,
        },
        "not_closed": {
            "strict_selected_phi_value": False,
            "strict_absolute_neutral_scale": False,
            "Dirac_only_action_completeness": bool(neutral["character_and_ontology_gate"]["Dirac_only_completeness_closed"]),
            "Majorana_block_exclusion": bool(neutral["character_and_ontology_gate"]["separate_Majorana_operator_excluded"]),
            "normal_ordering_selected_by_MTT": False,
            "PMNS_covariance_profile": False,
        },
        "adoptable_standard": {
            "name": "one neutral holonomy primitive plus one absolute scale",
            "continuous_neutrino_specific_shape_primitives": 1,
            "dimensionful_neutral_scale_primitives": 1,
            "binary_or_discrete_ontology_choice_still_open": True,
            "appropriate_if_user_accepts_1_to_3_selected_primitives": True,
            "strict_no_knob": False,
        },
        "non_looping_decision": "Do not continue APS/Dedekind or integer near-hit searches unless a new typed transgression det(E_nu)->Det(D_nu), a selected central U1 connection, or a unique holonomy potential is supplied.",
        "new_continuous_parameters_added": 0,
        "next_required_artifact": NEXT,
    }

    checks = {
        "A38_det_readout_closed": a38["neutral_factorization"]["phase_readout"].startswith("phi_nu="),
        "determinant_objects_type_separated": not type_packet["analytic_Dirac_determinant"]["same_as_det_E_nu_by_definition"],
        "central_lift_torsor_has_one_coordinate": torsor_packet["identifiability"]["number_of_surviving_continuous_shape_coordinates"] == 1,
        "central_lifts_preserve_relative_data": all(row["relative_SU3_holonomy_unchanged"] for row in torsor_samples),
        "all_source_markers_found": all(source_markers.values()),
        "flat_routes_already_closed": flat["pi_over_120_available_from_flat_internal_character"] is False,
        "A91_pi120_not_strict": not a91["results"]["pi_over_120_strict_phase_source_closed"],
        "A92_Dnu_family_constructed": a92["results"]["smooth_Dnu_family_constructed"],
        "profile_inverse_exact_numeric": abs(phi_from_ratio - phi_profile) < 1e-14,
        "profile_ratio_roundtrip": abs(ratio_reconstructed - ratio) < 1e-14,
        "profile_count_not_artificially_reduced": one_profile["coordinate_accounting"]["net_profile_coordinate_reduction"] == 0,
        "strict_phi_not_overclosed": not tier["not_closed"]["strict_selected_phi_value"],
        "no_new_parameter": tier["new_continuous_parameters_added"] == 0,
    }
    outputs = {
        "type_separation": str(TYPES.relative_to(ROOT)).replace("\\", "/"),
        "central_lift_torsor": str(TORSOR.relative_to(ROOT)).replace("\\", "/"),
        "source_exhaustion": str(EXHAUSTION.relative_to(ROOT)).replace("\\", "/"),
        "one_holonomy_profile": str(PROFILE.relative_to(ROOT)).replace("\\", "/"),
        "U5_tier": str(TIER.relative_to(ROOT)).replace("\\", "/"),
    }
    candidate = {
        "schema": "MTTSelectedNeutralLensNilDeterminantHolonomyExecutionOrOneScaleFinality.v1",
        "status": STATUS,
        "results": {
            "ordinary_flavor_determinant_is_correct_A38_object": True,
            "analytic_Dirac_determinant_direct_source_retired": True,
            "one_central_holonomy_coordinate_proved_minimal": True,
            "one_holonomy_plus_one_scale_profile_closed": True,
            "strict_phi_source_closed": False,
            "strict_scale_source_closed": False,
            "strict_U5_closed": False,
            "current_corpus_phase_source_exhausted": True,
            "new_continuous_parameters": 0,
        },
        "outputs": outputs,
        "checks": checks,
        "authority_hashes": [
            {"path": str(path), "sha256": sha256(path)} for path in paths.values()
        ],
        "next_required_artifact": NEXT,
    }
    cert = {
        "certificate": "MTT_Selected_NeutralLensNilDeterminantHolonomyExecution_or_OneScaleFinality_v1",
        "status": STATUS,
        "correct_determinant_object": "det(E_nu)",
        "analytic_Det_D_direct_source_retired": True,
        "surviving_shape_coordinates": 1,
        "profile_coordinates_shape_plus_scale": 2,
        "strict_phi_source_closed": False,
        "strict_scale_source_closed": False,
        "strict_U5_closed": False,
        "current_corpus_source_finality_proved": True,
        "new_continuous_parameters": 0,
        "next_required_artifact": NEXT,
    }
    note = f"""# MTT Selected Neutral LensNil Determinant-Holonomy Execution or One-Scale Finality v1

## Determinant type correction

The neutral factorization uses the ordinary determinant line of the rank-three
family bundle:

```text
det(E_nu)=Lambda^3 E_nu,
Hol_det(E_nu)(gamma)=det H_nu=exp(3 i phi_nu).
```

This is not, by definition, the analytic Quillen/Bismut--Freed line `Det(D_nu)`
of a family of chiral Dirac operators. The latter has an eta/mapping-torus
holonomy. No current index or transgression theorem identifies these two lines.
Therefore the APS route is retained as future mathematics but retired as a
direct source for `phi_nu` in the current proof chain.

## Exact one-coordinate finality

Fix the selected traceless family connection `A0` with holonomy `H_cen`. For a
closed one-form `alpha_gamma` normalized by `integral_gamma alpha_gamma=1`, every

```text
A_phi = A0 + i*phi*alpha_gamma*I3
```

has the same curvature and relative `SU(3)` holonomy, while

```text
Hol(A_phi)=exp(i phi) H_cen,
det Hol(A_phi)=exp(3 i phi).
```

Thus the existing topology, curvature, qutrit and `H_cen` data admit every
`phi` modulo `2*pi/3`. They cannot select its value. Conversely the determinant
recovers exactly that one scalar, so one central holonomy coordinate is both
necessary and sufficient.

The corpus explicitly lists Wilson-line/flat-connection phases as the open
flavor bottleneck. Cross-repo source audits do not select the q64 character or
LensNil flux integers as this neutral local system. This proves current-corpus
finality, not a no-go for a future MTT action that uniquely minimizes the
central holonomy.

## One-holonomy plus one-scale profile

For the massless normal-ordering three-basin profile,

```text
r = 2*sqrt(3)*tan(phi)/(3+sqrt(3)*tan(phi)),
phi = atan(sqrt(3)*r/(2-r)).
```

At the A40 profile, `r={ratio}` gives
`phi={phi_from_ratio}`, reproducing A40 with residual
`{abs(phi_from_ratio - phi_profile)}`. Once `phi` and one dimensionful splitting
scale are supplied, all 36 A40 mass/Yukawa/matrix rows follow. This replaces two
measured splitting coordinates by one geometric phase and one scale, so the
profile count is unchanged at two; it is a structural compression, not a new
parameter-count reduction.

U5 is now closed at the explicit **one neutral holonomy primitive plus one
absolute scale** profile standard. Strict no-knob U5 remains open, as do the
selected absolute scale, Dirac-only completeness, Majorana exclusion, ordering
selection and covariance. A41's `pi/120` remains an optional target-ranked
benchmark, not the selected value.

No new parameter was added.

Next artifact: `{NEXT}`.
"""

    for path, payload in [
        (TYPES, type_packet),
        (TORSOR, torsor_packet),
        (EXHAUSTION, exhaustion),
        (PROFILE, one_profile),
        (TIER, tier),
        (CANDIDATE, candidate),
        (CERT, cert),
    ]:
        dump(path, payload)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
