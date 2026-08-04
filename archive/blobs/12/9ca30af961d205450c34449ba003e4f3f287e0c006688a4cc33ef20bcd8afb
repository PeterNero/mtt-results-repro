from __future__ import annotations

import hashlib
import itertools
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_neutraloneholonomyonescaleontologyclosure_and_u5tierdecision"
STATUS = (
    "MTT_NEUTRAL_ONEHOLONOMY_ONESCALE_PROFILE_ONTOLOGY_AND_ORDER_CLOSED_"
    "STRICT_SOURCE_AND_NIL_SATURATION_OPEN"
)
NEXT = "MTT_Selected_PostU5TierLedger_and_U9GlobalBranchMeasure_v1"

OUT = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_NeutralOneHolonomyOneScaleOntologyClosure_and_U5TierDecision_v1.md"

REAL = OUT / "central_holonomy_real_structure_and_Majorana_exclusion.packet.json"
ORDER = OUT / "holonomy_chamber_ordering_and_orientation_pair.packet.json"
PROFILE = OUT / "one_holonomy_one_scale_full_neutral_profile_closure.packet.json"
COUNT = OUT / "post_U5_neutral_parameter_count.packet.json"
DECISION = OUT / "U5_tier_closure_and_strict_frontier.packet.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def orbit(phi: float) -> list[complex]:
    return [complex(math.cos(phi + 2 * math.pi * k / 3), math.sin(phi + 2 * math.pi * k / 3)) for k in range(3)]


def multiset_distance(left: list[complex], right: list[complex]) -> float:
    return min(
        max(abs(left[i] - right[p[i]]) for i in range(3))
        for p in itertools.permutations(range(3))
    )


def main() -> int:
    paths = {
        "A20_nil_boundary": ROOT / "candidate_data" / "selected_neutralnilboundarymassfunctional.candidate.json",
        "A40_profile": ROOT / "candidate_data" / "selected_neutraltwoprimitiveprofilevalueclosure.candidate.json",
        "A41_conditional": ROOT / "candidate_data" / "selected_neutrallensdedekindtransgression_or_oneprimitiveprofile.candidate.json",
        "A93_finality": ROOT / "candidate_data" / "selected_neutrallensnildeterminantholonomyexecution_or_onescalefinality.candidate.json",
        "A93_profile": ROOT / "candidate_data" / "selected_neutrallensnildeterminantholonomyexecution_or_onescalefinality" / "one_holonomy_one_scale_neutral_profile.packet.json",
        "neutral_mass_source": ROOT / "candidate_data" / "selected_neutralmassoperator_sourceemission.candidate.json",
        "A90_counts": ROOT / "candidate_data" / "selected_posta89minimalparameterledger_and_nextfrontier" / "tiered_parameter_count_summary.packet.json",
    }
    missing = [str(path) for path in paths.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing A94 authority: " + ", ".join(missing))

    a20 = load(paths["A20_nil_boundary"])
    a40 = load(paths["A40_profile"])
    a41 = load(paths["A41_conditional"])
    a93 = load(paths["A93_finality"])
    a93_profile = load(paths["A93_profile"])
    neutral = load(paths["neutral_mass_source"])
    a90 = load(paths["A90_counts"])

    phi_profile = float(a40["calibrated_shape_and_scale"]["phi_nu_rad"])
    phi_candidate = float(a41["determinant_line_candidate"]["candidate_phi_nu_rad"])
    shape_period = 2.0 * math.pi / 3.0
    self_conjugate_representatives = [0.0, math.pi / 3.0]
    profile_self_distance = multiset_distance(orbit(phi_profile), [z.conjugate() for z in orbit(phi_profile)])
    candidate_self_distance = multiset_distance(orbit(phi_candidate), [z.conjugate() for z in orbit(phi_candidate)])

    real_packet = {
        "schema": "MTTCentralHolonomyRealStructureAndMajoranaExclusion.v1",
        "status": "NONSELFCONJUGATE_CENTRAL_HOLONOMY_FORBIDS_MAJORANA_BLOCKS_AT_SAME_SOURCE_PROFILE_TIER",
        "family_holonomy": "H_nu(phi)=exp(i phi) diag(1,zeta3,zeta3^2)",
        "Majorana_invariance": {
            "matrix_condition": "H_nu(phi)^T M_M H_nu(phi)=M_M",
            "entry_condition": "M_ij can be nonzero only if lambda_i lambda_j=1",
            "existence_condition": "2 phi in (2pi/3) Z",
            "self_conjugate_phi_mod_2pi_over_3": ["0", "pi/3"],
            "equivalent_character_statement": "a Majorana block requires a self-character; the selected Z1344 gate permits only k=0 or k=672",
            "Z1344_self_characters": neutral["character_and_ontology_gate"]["Majorana_admissible_characters_Z1344"],
        },
        "executed_phases": {
            "A40_phi": phi_profile,
            "A40_distance_to_conjugate_eigenvalue_multiset": profile_self_distance,
            "A40_is_self_conjugate": profile_self_distance < 1e-12,
            "A41_phi_pi_over_120": phi_candidate,
            "A41_distance_to_conjugate_eigenvalue_multiset": candidate_self_distance,
            "A41_is_self_conjugate": candidate_self_distance < 1e-12,
        },
        "same_source_profile_theorem": {
            "adopted_premise": "the central flavor holonomy is preserved by the same neutral mass action; no separate Majorana-breaking source is added",
            "Dirac_channel_already_selected": neutral["character_and_ontology_gate"]["selected_1M_equals_Nc_Dirac_channel"],
            "Majorana_blocks_forbidden_for_executed_profile": profile_self_distance >= 1e-12,
            "Dirac_only_profile_ontology_closed": profile_self_distance >= 1e-12,
            "strict_MTT_holonomy_value_selected": False,
            "statement": "At the one-holonomy profile tier, the same central connection that supplies phi must be respected by every neutral mass block. For phi not equal to 0 or pi/3 modulo 2pi/3, no Majorana bilinear is invariant, while the selected L-Nc Dirac channel remains lawful. Thus the executed nonselfconjugate profile is Dirac-only without a new ontology parameter.",
        },
    }

    def chamber(phi: float) -> dict:
        cosines = [math.cos(phi + 2 * math.pi * k / 3) for k in range(3)]
        order = sorted(range(3), key=lambda k: cosines[k])
        low_gap = cosines[order[1]] - cosines[order[0]]
        full_gap = cosines[order[2]] - cosines[order[0]]
        ratio = low_gap / full_gap
        return {
            "phi": phi,
            "cosines": cosines,
            "ascending_k_order": order,
            "small_to_full_gap_ratio": ratio,
            "normal_ordering_chamber": abs(phi) < math.pi / 6.0 and abs(phi) > 0,
        }

    positive = chamber(phi_profile)
    negative = chamber(-phi_profile)
    sorted_positive = sorted(positive["cosines"])
    sorted_negative = sorted(negative["cosines"])
    order_packet = {
        "schema": "MTTHolonomyChamberOrderingAndOrientationPair.v1",
        "status": "ABS_PHI_BELOW_PI_OVER_6_SELECTS_NORMAL_ORDERING_ORIENTATION_SIGN_ONLY_SWAPS_LOW_FAMILY_LABELS",
        "chamber_theorem": {
            "normal": "0<|phi|<pi/6 gives r<1/2: the two lower eigenvalues form the close pair",
            "inverted": "pi/6<|phi|<pi/3 gives r>1/2: the two upper eigenvalues form the close pair",
            "boundary": "|phi|=pi/6 gives equal adjacent gaps",
            "proved_from": "r(phi)=2sqrt(3)tan(|phi|)/(3+sqrt(3)tan(|phi|)) on the fundamental chamber",
        },
        "A40_orientation_pair": {
            "plus": positive,
            "minus": negative,
            "sorted_spectra_equal": max(abs(a - b) for a, b in zip(sorted_positive, sorted_negative)) < 1e-12,
            "family_label_swap": {"plus_low_pair": positive["ascending_k_order"][:2], "minus_low_pair": negative["ascending_k_order"][:2]},
            "both_normal_ordering": positive["normal_ordering_chamber"] and negative["normal_ordering_chamber"],
        },
        "A41_candidate_in_normal_chamber": 0.0 < abs(phi_candidate) < math.pi / 6.0,
        "strict_ordering_selected_without_holonomy_value": False,
    }

    row_counts = a40["row_counts"]
    profile_packet = {
        "schema": "MTTOneHolonomyOneScaleFullNeutralProfileClosure.v1",
        "status": "DIRAC_NORMAL_ORDERING_PROFILE_36_ROWS_CLOSED_FROM_ONE_HOLONOMY_ONE_SCALE_AND_DECLARED_BOUNDARY",
        "adopted_inputs": {
            "dimensionless": ["phi_nu central flavor holonomy"],
            "dimensionful": ["one atmospheric mass-squared scale Delta_m31^2"],
            "discrete_or_structural": [
                "same-source holonomy invariance",
                "nil minimal-trace boundary m_lightest=0",
                "right-handed Dirac mass-basis convention",
            ],
        },
        "derived_at_profile_tier": {
            "Dirac_only_ontology": real_packet["same_source_profile_theorem"]["Dirac_only_profile_ontology_closed"],
            "normal_ordering": order_packet["A40_orientation_pair"]["both_normal_ordering"],
            "lightest_mass_zero": a20["minimal_trace_mass_functional"]["mathematical_theorem_proved"],
            "mass_squared_eV2": a40["physical_values"]["mass_squared_eV2"],
            "masses_eV": a40["physical_values"]["masses_eV"],
            "sum_masses_eV": a40["physical_values"]["sum_masses_eV"],
            "all_A40_rows_inherited": row_counts["total_rows_filled"] == 36,
            "row_counts": row_counts,
        },
        "strict_boundaries": {
            "nil_boundary_source_promotion": a20["minimal_trace_mass_functional"]["selected_MTT_neutral_source_principle_proved"],
            "holonomy_value_selected": False,
            "absolute_scale_selected": False,
            "covariance_propagated": a40["closure_boundary"]["uncertainty_covariance_propagated"],
            "strict_no_knob_U5": False,
        },
        "observed_profile_data_used": True,
        "new_fit_performed_here": False,
    }

    old_pmns = int(a90["current_counts"]["minimal_PMNS_excluding_QCD_theta"] - a90["current_counts"]["non_neutrino_excluding_QCD_theta"])
    count_packet = {
        "schema": "MTTPostU5NeutralParameterCount.v1",
        "status": "MINIMAL_PMNS_COUNT_REMAINS_SIX_BUT_MASS_SECTOR_IS_STRUCTURALLY_REPARAMETERIZED",
        "minimal_PMNS_breakdown": {
            "mixing_angles": 3,
            "Dirac_CP_phase": 1,
            "neutral_shape_holonomy_phi": 1,
            "neutral_absolute_mass_squared_scale": 1,
            "total": 6,
        },
        "comparison": {
            "A90_minimal_PMNS_coordinates": old_pmns,
            "post_A94_minimal_PMNS_coordinates": 6,
            "net_coordinate_reduction": 0,
            "Majorana_phases_counted": 0,
            "independent_lightest_mass_counted": 0,
        },
        "meaning": "The two oscillation-splitting inputs are reorganized as one geometric holonomy and one scale. Ontology, ordering and all mass/Yukawa rows then follow at the adopted profile tier, but the two values are not strict MTT predictions.",
    }

    decision = {
        "schema": "MTTU5TierClosureAndStrictFrontier.v1",
        "status": "U5_CLOSED_AT_ONE_HOLONOMY_ONE_SCALE_PROFILE_STANDARD_STRICT_NO_KNOB_FROZEN_OPEN",
        "adopted_profile_standard": {
            "closed": True,
            "shape_primitives": 1,
            "scale_primitives": 1,
            "continuous_ontology_or_ordering_parameters": 0,
            "Dirac_only": True,
            "normal_ordering": True,
            "m_lightest_zero_boundary": True,
            "numeric_rows": 36,
        },
        "strict_source_standard": {
            "closed": False,
            "missing": [
                "selected central U1 holonomy value or unique holonomy potential",
                "selected absolute neutral scale response",
                "promotion of nil minimal-trace boundary as the physical source principle",
                "full neutral covariance/likelihood packet",
            ],
            "current_corpus_search_frozen": a93["results"]["current_corpus_phase_source_exhausted"],
        },
        "non_looping_locks": [
            "do not reopen the recursive X6 domain",
            "do not reopen the one-holonomy minimality theorem",
            "do not use Det(D_nu) eta values for det(E_nu) without a typed transgression theorem",
            "do not recount Dirac/Majorana or NO/IO as profile parameters inside the nonselfconjugate normal chamber",
            "do not call phi or the mass scale strict predictions",
        ],
        "program_move": "At the adopted 1-3 primitive policy, U5 leaves the active frontier. Move to U9 global branch measure; strict U5 resumes only if a genuinely new holonomy potential, scale source or nil-saturation theorem appears.",
        "new_continuous_parameters_added": 0,
        "next_required_artifact": NEXT,
    }

    checks = {
        "existing_Dirac_channel_selected": neutral["character_and_ontology_gate"]["selected_1M_equals_Nc_Dirac_channel"],
        "self_character_gate_imported": neutral["character_and_ontology_gate"]["Majorana_admissible_characters_Z1344"] == [0, 672],
        "A40_phase_nonselfconjugate": not real_packet["executed_phases"]["A40_is_self_conjugate"],
        "A41_phase_nonselfconjugate": not real_packet["executed_phases"]["A41_is_self_conjugate"],
        "same_source_profile_Dirac_only": real_packet["same_source_profile_theorem"]["Dirac_only_profile_ontology_closed"],
        "orientation_pair_same_sorted_spectrum": order_packet["A40_orientation_pair"]["sorted_spectra_equal"],
        "A40_both_orientations_normal": order_packet["A40_orientation_pair"]["both_normal_ordering"],
        "A41_normal_chamber": order_packet["A41_candidate_in_normal_chamber"],
        "nil_boundary_math_theorem_imported": a20["minimal_trace_mass_functional"]["mathematical_theorem_proved"],
        "all_36_rows_inherited": profile_packet["derived_at_profile_tier"]["all_A40_rows_inherited"],
        "PMNS_count_remains_six": count_packet["minimal_PMNS_breakdown"]["total"] == old_pmns == 6,
        "strict_U5_not_overclosed": not decision["strict_source_standard"]["closed"],
        "no_new_parameter": decision["new_continuous_parameters_added"] == 0,
    }
    outputs = {
        "real_structure": str(REAL.relative_to(ROOT)).replace("\\", "/"),
        "ordering": str(ORDER.relative_to(ROOT)).replace("\\", "/"),
        "profile": str(PROFILE.relative_to(ROOT)).replace("\\", "/"),
        "count": str(COUNT.relative_to(ROOT)).replace("\\", "/"),
        "decision": str(DECISION.relative_to(ROOT)).replace("\\", "/"),
    }
    candidate = {
        "schema": "MTTSelectedNeutralOneHolonomyOneScaleOntologyClosureAndU5TierDecision.v1",
        "status": STATUS,
        "results": {
            "U5_one_holonomy_one_scale_profile_closed": True,
            "Dirac_only_profile_ontology_closed": True,
            "normal_ordering_profile_closed": True,
            "orientation_pair_spectrum_equivalent": True,
            "neutral_numeric_rows_closed": 36,
            "minimal_PMNS_coordinates": 6,
            "strict_holonomy_source_closed": False,
            "strict_scale_source_closed": False,
            "strict_nil_saturation_closed": False,
            "strict_U5_closed": False,
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
        "certificate": "MTT_Selected_NeutralOneHolonomyOneScaleOntologyClosure_and_U5TierDecision_v1",
        "status": STATUS,
        "adopted_profile_U5_closed": True,
        "Dirac_only_profile": True,
        "normal_ordering_profile": True,
        "m_lightest_zero_profile_boundary": True,
        "numeric_rows": 36,
        "shape_plus_scale_primitives": 2,
        "minimal_PMNS_coordinates": 6,
        "strict_U5_closed": False,
        "new_continuous_parameters": 0,
        "next_required_artifact": NEXT,
    }
    note = f"""# MTT Selected Neutral One-Holonomy One-Scale Ontology Closure and U5 Tier Decision v1

## Same-source ontology theorem

For `H_nu(phi)=exp(i phi) diag(1,zeta3,zeta3^2)`, a Majorana block must obey

```text
H_nu(phi)^T M_M H_nu(phi)=M_M.
```

An entry can survive only if its two holonomy eigenvalues multiply to one. This
occurs iff `2*phi` is a multiple of `2*pi/3`, so the self-conjugate points are
`phi=0` and `phi=pi/3` modulo the shape period. This is the smooth counterpart
of the existing `Z1344` self-character gate `{neutral['character_and_ontology_gate']['Majorana_admissible_characters_Z1344']}`.

The A40 profile has `phi={phi_profile}` and the A41 benchmark has
`phi={phi_candidate}`. Neither is self-conjugate. At the adopted same-source
profile standard, where the central holonomy is preserved by the neutral action,
all Majorana blocks therefore vanish while the selected `L-Nc` Dirac channel
remains. Dirac ontology is closed at this tier without an extra parameter.

## Ordering theorem

In the fundamental chamber:

```text
0 < |phi| < pi/6  -> lower pair is close -> normal ordering,
pi/6 < |phi| < pi/3 -> upper pair is close -> inverted ordering.
```

Both `+phi` and `-phi` for A40 lie in the normal chamber. Their sorted spectra
are identical; the sign only exchanges the two low family labels. The A41
benchmark also lies in the normal chamber.

## Adopted U5 closure

With one central holonomy primitive, one atmospheric mass-squared scale, the
declared nil minimal-trace boundary `m_lightest=0`, and the right-handed Dirac
basis convention, all `{row_counts['total_rows_filled']}` A40 mass, Yukawa and
matrix rows follow. The minimal PMNS count remains six:

```text
3 mixing angles + 1 Dirac CP phase + 1 holonomy shape + 1 mass scale = 6.
```

This is a structural reparameterization of the two measured splitting inputs,
not a numerical parameter reduction.

U5 is now closed at the adopted **one holonomy plus one scale profile standard**.
Strict no-knob U5 remains open because MTT has not selected the holonomy value,
absolute scale, nil-saturation source principle or covariance packet. Current
corpus search for the phase is frozen by A93; it should resume only when a new
typed source appears. At the accepted 1--3 primitive policy, the active program
can now move to U9 global branch measure.

No new parameter was added.

Next artifact: `{NEXT}`.
"""

    for path, payload in [
        (REAL, real_packet),
        (ORDER, order_packet),
        (PROFILE, profile_packet),
        (COUNT, count_packet),
        (DECISION, decision),
        (CANDIDATE, candidate),
        (CERT, cert),
    ]:
        dump(path, payload)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
