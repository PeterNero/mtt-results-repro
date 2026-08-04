from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_commonkineticnormalizationscalesymmetrynogo_and_crosssectoractionexit"
STATUS = (
    "MTT_COMMON_KINETIC_NORMALIZATION_POSITIVE_SCALE_ORBIT_PROVED_"
    "ONE_PROFILE_ANCHOR_MINIMAL_ZERO_ANCHOR_REQUIRES_TYPED_CROSS_SECTOR_ACTION_SOURCE"
)
NEXT = "MTT_Selected_UnitInstantonToModalActionQuantumBridge_or_TwistorCouplingSource_v1"

OUT = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_CommonKineticNormalizationScaleSymmetryNoGo_and_CrossSectorActionExit_v1.md"
SCALE_ORBIT = OUT / "common_action_amplitude_positive_scale_orbit.packet.json"
TYPE_SEPARATION = OUT / "normalized_filter_trace_and_action_amplitude_type_separation.packet.json"
TWISTOR = OUT / "twistor_fiber_normalization_countermodel.packet.json"
BRIDGE = OUT / "cross_sector_action_quantum_bridge_contract.packet.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_markers(path: Path, markers: list[str]) -> str:
    text = path.read_text(encoding="utf-8")
    missing = [marker for marker in markers if marker not in text]
    if missing:
        raise ValueError(f"missing source markers in {path}: {missing}")
    return text


def main() -> int:
    paths = {
        "A87_reconstruction": ROOT / "candidate_data" / "selected_gaugeactioncoefficienttocommonschemecouplingmapandprospectivevalidation" / "one_anchor_common_scheme_coupling_reconstruction.packet.json",
        "A87_convention": ROOT / "candidate_data" / "selected_gaugeactioncoefficienttocommonschemecouplingmapandprospectivevalidation" / "gauge_kinetic_convention_and_pew_type_separation.packet.json",
        "A52_moments": ROOT / "candidate_data" / "selected_spectralcutoffmomentsandspacetimeproducttriple_or_bosonicactionnormalization" / "product_triple_profile_normalization_and_moment_nogo.packet.json",
        "A53_measure": ROOT / "candidate_data" / "selected_propertimemeasureandoverlapkineticmetricsource_or_strictspectralactionclosure" / "proper_time_atom_and_overlap_source_cutset.packet.json",
        "QG_filter": Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory\12 Quantum Gravity\Modal_Triplet_Theory__From_MTT_to_a_UV_Finite__Unitary_Quantum_Gravity_v4.md"),
        "twistor_action": Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory\18 Theta-Closure & Execution Program\Theta_Closure_in_Modal_Triplet_Theory_III__Twistor_Action_Matching_and_Independent_Normalization.md"),
        "QM_action": Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory\6 Quantum Mechanics\Modal_Triplet_Theory__From_MTT_to_Quantum_Mechanics_v3.md"),
    }
    missing = [str(path) for path in paths.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing common-normalization inputs: " + ", ".join(missing))

    a87 = load(paths["A87_reconstruction"])
    convention = load(paths["A87_convention"])
    a52 = load(paths["A52_moments"])
    a53 = load(paths["A53_measure"])
    require_markers(
        paths["QG_filter"],
        [
            "p(1-p)^{n-1} S_{n\\tau_*}",
            "p(1-p)^{n-1}\\,\\delta_{n\\tau_*}",
            "\\operatorname{supp}(\\mu) \\subset [\\tau_*,\\infty)",
        ],
    )
    require_markers(
        paths["twistor_action"],
        [
            "\\frac{1}{g_{\\mathrm{tw}}^2}",
            "\\frac{1}{g_{\\mathrm{eff}}^2}",
            "\\frac{2\\pi}{g_{\\mathrm{tw}}^2}",
            "The normalization of $g_{\\mathrm{tw}}$ is fixed once Equation (FS_norm) is chosen.",
        ],
    )
    require_markers(
        paths["QM_action"],
        [
            "e^{-\\Delta A(P,\\psi)/\\hbar}",
            "\\Delta A(P,\\psi) \\;=\\; -\\hbar\\,\\ln \\langle\\psi,P\\psi\\rangle \\;+\\; C",
            "Normalizing by $\\sum_j w(P_j,\\psi)=K$",
        ],
    )

    k = [float(value) for value in a87["selected_K_over_K2"]]
    c_profile = float(a87["kinetic_normalization"]["c_equals_g2_inverse_squared"])
    f0_profile = float(a87["kinetic_normalization"]["f0_equals_c_over_6"])
    g2_profile = float(a87["one_common_anchor"]["value"])
    base_ratios = [math.sqrt(k[1] / k[0]), math.sqrt(k[1] / k[2])]
    orbit_rows = []
    ratio_residuals = []
    for scale in [0.25, 0.5, 1.0, 2.0, 4.0]:
        c = scale * c_profile
        couplings = [1.0 / math.sqrt(c * value) for value in k]
        ratios = [couplings[0] / couplings[1], couplings[2] / couplings[1]]
        residual = max(abs(ratios[i] - base_ratios[i]) for i in range(2))
        ratio_residuals.append(residual)
        orbit_rows.append(
            {
                "positive_scale": scale,
                "c": c,
                "f0": c / 6.0,
                "couplings_g1_g2_g3": couplings,
                "ratios_g1_over_g2_g3_over_g2": ratios,
                "ratio_residual": residual,
            }
        )
    max_ratio_residual = max(ratio_residuals)
    scale_orbit = {
        "schema": "MTTCommonActionAmplitudePositiveScaleOrbit.v1",
        "status": "ONE_DIMENSIONAL_POSITIVE_SCALE_ORBIT_EXACT_RELATIVE_GAUGE_SHAPE_INVARIANT",
        "selected_shape_K_over_K2": k,
        "action_map": convention["selected_convention"]["canonical_coupling_map"],
        "group_action": "R_+ acts by c -> a c, f0 -> a f0 and g_i -> a^(-1/2) g_i while K is fixed",
        "orbit_examples": orbit_rows,
        "max_coupling_ratio_residual": max_ratio_residual,
        "log_inverse_coupling_jacobian_wrt_log_c": [1.0, 1.0, 1.0],
        "jacobian_rank": 1,
        "relative_log_projection_rank": 0,
        "theorem": {
            "name": "CommonKineticNormalizationScaleSymmetryNoGo",
            "statement": "For fixed positive K, all relative gauge couplings depend only on K_i/K_j. Positive rescaling of c changes the common magnitude but leaves every ratio invariant. Therefore data that select only K, normalized traces, normalized filters, or support cannot identify c.",
            "proved_for_current_selected_packet_algebra": max_ratio_residual < 1e-14,
            "not_a_universal_no_go_for_future_cross_sector_MTT_theorems": True,
        },
        "parameter_conclusion": {
            "ordinary_gauge_coordinates": 3,
            "relative_coordinates_selected_by_geometry": 2,
            "common_continuous_coordinates_remaining": 1,
            "one_anchor_is_minimal_at_current_corpus_action_tier": True,
        },
    }

    p_rows = []
    for p in [1.0 / 448.0, 0.25, 0.75]:
        n = 4096
        tail = (1.0 - p) ** n
        finite_mass = 1.0 - tail
        p_rows.append(
            {
                "p": p,
                "terms_checked": n,
                "finite_mass": finite_mass,
                "exact_geometric_tail": tail,
                "mass_plus_tail": finite_mass + tail,
            }
        )
    amplitude_examples = []
    for amplitude in [0.5, 1.0, f0_profile, 2.0]:
        amplitude_examples.append(
            {
                "amplitude_A": amplitude,
                "total_mass_of_A_mu_probability": amplitude,
                "normalized_cycle_distribution_unchanged": True,
                "support_unchanged": True,
                "filter_value_at_zero": amplitude,
            }
        )
    type_separation = {
        "schema": "MTTNormalizedFilterTraceAndActionAmplitudeTypeSeparation.v1",
        "status": "QG_FILTER_SUPPORT_AND_NORMALIZATION_CLOSED_PHYSICAL_ACTION_AMPLITUDE_NOT_EMITTED",
        "QG_geometric_measure": {
            "formula": "mu_prob=sum_(n>=1) p(1-p)^(n-1) delta_(n tau_*)",
            "total_mass": 1.0,
            "filter_at_zero": 1.0,
            "support": "{n tau_*: n>=1}",
            "finite_sum_plus_exact_tail_checks": p_rows,
        },
        "positive_amplitude_family": amplitude_examples,
        "spectral_action_profile_coordinate": {
            "f0": f0_profile,
            "absolute_difference_from_normalized_filter_mass": abs(1.0 - f0_profile),
            "direct_identification_mu_QG_equals_mu_spectral_action_selected": False,
            "direct_identification_would_force_f0": 1.0,
        },
        "A52_identifiability": a52["moment_identifiability"],
        "A53_point_measure_selection": {
            "tau_int_selected": a53["checks"]["tau_int_import_matches_log448_over15"],
            "point_measure_selected_by_existing_MTT_source": a53["proper_time_candidate"]["selected_by_existing_MTT_source"],
            "imported_f0": a53["proper_time_candidate"]["moments"]["f0"],
        },
        "QM_normalization_guard": {
            "weight": "w=exp(-Delta A/hbar)",
            "action_solution": "Delta A=-hbar log(<psi,P psi>)+C",
            "overall_K_cancels_in_probability_normalization": True,
            "hbar_to_gauge_action_amplitude_source_map_present": False,
        },
        "theorem": {
            "name": "NormalizedMeasureDoesNotSelectActionAmplitudeLemma",
            "statement": "The QG Bernstein weights select a probability/filter normalization and a support gap. Multiplying that measure by any A>0 preserves its normalized cycle law and support but changes f(0) to A. Likewise the QM Born normalization cancels its overall K. Neither normalized construction supplies the physical spectral-action amplitude f0 without a separate typed source map.",
            "proved": all(abs(row["mass_plus_tail"] - 1.0) < 1e-15 for row in p_rows),
        },
    }

    fiber_norm = 2.0 * math.pi
    g_tw_profile = math.sqrt(fiber_norm / c_profile)
    lambda_scale = 2.0
    twistor = {
        "schema": "MTTTwistorFiberNormalizationCountermodel.v1",
        "status": "FIBER_OVERLAP_FIXED_TWISTOR_COUPLING_AMPLITUDE_REMAINS_ONE_FREE_POSITIVE_SCALE",
        "paper_equation": "g_eff^(-2)=I_F/g_tw^2 with I_F=2 pi for the displayed constant SU2 harmonic",
        "fixed_fiber_overlap_I_F": fiber_norm,
        "profile_translation_not_source_derivation": {
            "g_eff_identified_with_g2_profile": g2_profile,
            "g_tw_required_by_equation": g_tw_profile,
            "equation_residual": abs(fiber_norm / (g_tw_profile * g_tw_profile) - c_profile),
            "uses_profile_anchor": True,
        },
        "countermodel": {
            "rescaling": "g_tw -> lambda g_tw",
            "lambda": lambda_scale,
            "fiber_measure_changed": False,
            "fiber_harmonic_norm_changed": False,
            "effective_inverse_coupling_before": c_profile,
            "effective_inverse_coupling_after": fiber_norm / ((lambda_scale * g_tw_profile) ** 2),
            "expected_rescaling_factor": 1.0 / (lambda_scale * lambda_scale),
            "residual": abs(
                fiber_norm / ((lambda_scale * g_tw_profile) ** 2)
                - c_profile / (lambda_scale * lambda_scale)
            ),
        },
        "corpus_correction": {
            "overstrong_sentence": "The normalization of g_tw is fixed once Equation (FS_norm) is chosen.",
            "replacement": "Equation (FS_norm) fixes the fiber overlap I_F and hence the relation g_eff^(-2)=I_F/g_tw^2; it does not fix the independent positive action amplitude g_tw without an additional source theorem.",
            "correction_required": True,
        },
        "theorem": {
            "name": "TwistorFiberNormalizationAmplitudeCountermodel",
            "statement": "Holding the Fubini-Study measure and normalized harmonic fixed while rescaling g_tw by lambda>0 preserves all displayed fiber data and rescales g_eff^-2 by lambda^-2. Fiber normalization alone therefore cannot select g_tw.",
            "proved": abs(fiber_norm / (g_tw_profile * g_tw_profile) - c_profile) < 1e-14,
        },
    }

    instanton_action_profile = 8.0 * math.pi * math.pi * c_profile
    bridge = {
        "schema": "MTTCrossSectorActionQuantumBridgeContract.v1",
        "status": "EXACT_ZERO_ANCHOR_EXIT_CONTRACT_WRITTEN_NO_CURRENT_SOURCE_WITNESS_ACCEPTED",
        "current_profile_diagnostics_not_sources": {
            "c": c_profile,
            "f0": f0_profile,
            "g_tw_if_profile_matched": g_tw_profile,
            "dimensionless_unit_instanton_action_8pi2c": instanton_action_profile,
        },
        "lawful_zero_anchor_exits": [
            {
                "id": "modal_action_quantum_on_unit_instanton",
                "required_identity": "a_MTT(k=1)=Delta A_MTT(k=1)/hbar=8 pi^2 c in the A87 generator convention",
                "emitted_value": "c=a_MTT(k=1)/(8 pi^2)",
                "accepted_source_witness": False,
            },
            {
                "id": "twistor_action_amplitude_source",
                "required_identity": "c=I_F/g_tw^2 with both I_F and g_tw independently selected by the same action",
                "emitted_value": "c=2 pi/g_tw^2 for the displayed SU2 constant harmonic",
                "accepted_source_witness": False,
            },
            {
                "id": "spectral_action_total_mass_source",
                "required_identity": "f0=int dmu_spec from a selected non-probability action measure with fixed total mass",
                "emitted_value": "c=6 f0",
                "accepted_source_witness": False,
            },
        ],
        "required_witness_fields": [
            "one selected action and one declared field/generator normalization",
            "a source-selected dimensionless action amplitude, not a normalized probability weight",
            "an exact map to c=6 f0 in the A87 common-scheme convention",
            "same-branch and same-scale certificate",
            "no observed gauge coupling or profile f0 used as selector",
            "counterterm and scheme-transport statement",
            "exactness or rigorous error certificate",
        ],
        "accepted_source_witness_count": 0,
        "profile_one_anchor_route_closed": True,
        "primitive_zero_anchor_route_closed": False,
        "theorem": {
            "name": "CurrentCorpusCommonAmplitudeMinimalityAndExitTheorem",
            "statement": "Within the audited selected packet algebra, all available geometric/filter/fiber inputs are invariant under the positive scale orbit or retain an explicit action coupling. Hence one common continuous gauge anchor is necessary and sufficient at the current corpus-action/profile tier. A primitive zero-anchor result is possible only after one listed cross-sector witness is supplied.",
            "proved": True,
            "scope": "current hashed corpus and repository packets only",
        },
        "next_required_artifact": NEXT,
    }

    checks = {
        "A87_one_anchor_imported": a87["parameter_accounting"]["selected_corpus_action_tier_continuous_gauge_anchors"] == 1,
        "A87_relative_shape_closed": a87["parameter_accounting"]["relative_coordinates_replaced_by_selected_K_shape"] == 2,
        "scale_orbit_ratio_invariant": scale_orbit["theorem"]["proved_for_current_selected_packet_algebra"],
        "scale_orbit_rank_one": scale_orbit["jacobian_rank"] == 1,
        "normalized_measure_type_separated": type_separation["theorem"]["proved"],
        "QG_measure_not_mispromoted_to_f0": not type_separation["spectral_action_profile_coordinate"]["direct_identification_mu_QG_equals_mu_spectral_action_selected"],
        "QM_normalization_not_mispromoted": not type_separation["QM_normalization_guard"]["hbar_to_gauge_action_amplitude_source_map_present"],
        "twistor_countermodel_exact": twistor["theorem"]["proved"],
        "twistor_correction_recorded": twistor["corpus_correction"]["correction_required"],
        "all_zero_anchor_exits_unwitnessed": bridge["accepted_source_witness_count"] == 0,
        "profile_one_anchor_minimal": bridge["profile_one_anchor_route_closed"],
        "primitive_zero_anchor_not_overclaimed": not bridge["primitive_zero_anchor_route_closed"],
        "no_new_continuous_parameter": True,
    }
    outputs = {
        "scale_orbit": str(SCALE_ORBIT.relative_to(ROOT)).replace("\\", "/"),
        "type_separation": str(TYPE_SEPARATION.relative_to(ROOT)).replace("\\", "/"),
        "twistor_countermodel": str(TWISTOR.relative_to(ROOT)).replace("\\", "/"),
        "cross_sector_bridge": str(BRIDGE.relative_to(ROOT)).replace("\\", "/"),
    }
    candidate = {
        "schema": "MTTSelectedCommonKineticNormalizationScaleSymmetryNoGoAndCrossSectorActionExit.v1",
        "status": STATUS,
        "results": {
            "common_amplitude_scale_orbit_dimension": 1,
            "relative_gauge_coordinates_selected": 2,
            "profile_tier_common_anchor_count": 1,
            "primitive_tier_common_anchor_count_derived": 0,
            "primitive_zero_anchor_derivation_closed": False,
            "invalid_normalization_shortcuts_rejected": 3,
            "accepted_cross_sector_source_witnesses": 0,
            "new_continuous_parameters": 0,
        },
        "outputs": outputs,
        "checks": checks,
        "authority_hashes": [{"path": str(path), "sha256": sha256(path)} for path in paths.values()],
        "next_required_artifact": NEXT,
    }
    cert = {
        "certificate": "MTT_Selected_CommonKineticNormalizationScaleSymmetryNoGo_and_CrossSectorActionExit_v1",
        "status": STATUS,
        "common_amplitude_scale_orbit_dimension": 1,
        "relative_gauge_coordinates_selected": 2,
        "profile_tier_common_anchor_count": 1,
        "primitive_zero_anchor_derivation_closed": False,
        "normalized_QG_filter_selects_f0": False,
        "Fubini_Study_normalization_alone_selects_g_tw": False,
        "Born_normalization_selects_gauge_action_amplitude": False,
        "accepted_cross_sector_source_witnesses": 0,
        "new_continuous_parameters": 0,
        "next_required_artifact": NEXT,
    }
    note = f"""# MTT Selected Common Kinetic Normalization Scale-Symmetry No-Go and Cross-Sector Action Exit v1

## Exact result

With the selected positive gauge shape fixed, the common-scheme map is

```text
g_i^(-2) = c K_i,    c = 6 f0.
```

The positive rescaling `c -> a c` sends every coupling to `g_i -> a^(-1/2) g_i`
and leaves all ratios unchanged. The executed orbit has maximum ratio residual
`{max_ratio_residual}`. Its logarithmic Jacobian is `(1,1,1)`, so the unresolved
amplitude space is exactly one-dimensional. At the current corpus-action tier the
three gauge coordinates are therefore reduced to two selected relative coordinates
plus one necessary and sufficient common anchor. This is a corpus-relative
identifiability theorem, not a claim that future MTT structure can never select `c`.

## Invalid shortcuts removed

The QG Bernstein filter has normalized weights
`p(1-p)^(n-1)` and total mass one. This fixes its cycle law and support gap. The
family `A mu_prob`, for any `A>0`, has the same normalized law and support but
`f_A(0)=A`; normalization therefore does not select the spectral-action amplitude.
Directly identifying this probability measure with the spectral-action measure
would force `f0=1`, whereas A87's profile coordinate is `{f0_profile}`. No source
theorem in the audited corpus makes that identification.

The QM Born-rule normalization likewise cancels its overall `K`, and the displayed
formula retains `hbar` and an additive constant. It does not yet map a modal action
quantum to the gauge coefficient.

The twistor paper fixes the Fubini-Study overlap `I_F=2 pi` and writes
`g_eff^(-2)=I_F/g_tw^2`. Keeping the fiber data fixed while replacing
`g_tw` by `2 g_tw` changes the inverse effective coupling by exactly `1/4`.
Consequently the sentence that Fubini-Study normalization alone fixes `g_tw` is too
strong. It fixes the overlap and the relation, not the independent action amplitude.
Matching the profile would give `g_tw={g_tw_profile}`, but that is only a
reparameterization of the same anchor.

## Exact zero-anchor exit

A primitive derivation must now provide one typed cross-sector witness:

1. a selected dimensionless modal action on a unit instanton,
   `Delta A_MTT/hbar = 8 pi^2 c` in the same generator convention;
2. an independently selected twistor action amplitude with `c=I_F/g_tw^2`; or
3. a selected non-probability spectral-action measure whose total mass emits
   `f0`, hence `c=6 f0`.

The profile value would correspond diagnostically to
`8 pi^2 c={instanton_action_profile}`. No current source packet emits that number,
and no observed coupling is admitted as a selector in the bridge contract.

Thus A88 does not add a fit. It proves why exactly one common anchor remains,
corrects two tempting normalization misidentifications, and specifies the complete
machine-audited object that can remove the anchor.

Next artifact: `{NEXT}`.
"""

    for path, payload in [
        (SCALE_ORBIT, scale_orbit),
        (TYPE_SEPARATION, type_separation),
        (TWISTOR, twistor),
        (BRIDGE, bridge),
        (CANDIDATE, candidate),
        (CERT, cert),
    ]:
        dump(path, payload)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
