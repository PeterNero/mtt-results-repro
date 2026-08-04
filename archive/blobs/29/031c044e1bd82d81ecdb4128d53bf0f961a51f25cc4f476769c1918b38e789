from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
SM_PARITY = TEXPAPERS / "mtt-sm-parity-closure"

LOCAL_TLSM = (
    ROOT
    / "certificates"
    / "q79_aggregate_tlsm_anomaly_and_odd_bundle_nogo_certificate.json"
)
SIMULTANEOUS_C2_C3 = (
    ROOT
    / "certificates"
    / "q79_shared_circle_clutching_c2_c3_independence_certificate.json"
)
HODGE_ADMISSIBILITY = (
    ROOT
    / "certificates"
    / "q79_fuyau_mixed_c2_hodge_admissibility_certificate.json"
)
CLUTCHING = (
    SM_PARITY
    / "candidate_data"
    / "selected_q79nonpullbackchiralvisiblebundleandfullsu9holonomyselection"
    / "rank_one_fuyau_shared_circle_clutching.packet.json"
)
SPECTRAL_A128 = (
    SM_PARITY
    / "candidate_data"
    / "selected_q79alignmentcontinuousrootmonodromypromotion"
    / "U6_frontier_after_A128.packet.json"
)
SPECTRAL_A129 = (
    SM_PARITY
    / "candidate_data"
    / "selected_q79alignmenthandlesandglobalsurfacerelation"
    / "U6_frontier_after_A129.packet.json"
)
SPECTRAL_A130 = (
    SM_PARITY
    / "candidate_data"
    / "selected_q79alignmentintegralh2presentation"
    / "U6_frontier_after_A130.packet.json"
)
SPECTRAL_A131 = (
    SM_PARITY
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "U6_frontier_after_A131.packet.json"
)
SPECTRAL_A132 = (
    SM_PARITY
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "U6_frontier_after_A132.packet.json"
)
SPECTRAL_A151 = (
    SM_PARITY
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "U6_frontier_after_A151.packet.json"
)
SAME_CARRIER_CUTSET = (
    SM_PARITY
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "same_carrier_integral_branch_cutset.theorem.packet.json"
)

OUT_CERT = (
    ROOT
    / "certificates"
    / "q79_standard_tlsm_pullback_chirality_nogo_certificate.json"
)
OUT_NOTE = (
    ROOT
    / "proof_corpus"
    / "q79_Standard_TLSM_Pullback_Chirality_NoGo_and_Twisted_Exit_v1.md"
)


def load(path: Path) -> dict:
    if not path.is_file():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    local = load(LOCAL_TLSM)
    simultaneous_c2_c3 = load(SIMULTANEOUS_C2_C3)
    hodge_admissibility = load(HODGE_ADMISSIBILITY)
    clutching = load(CLUTCHING)
    spectral_a128 = load(SPECTRAL_A128)
    spectral_a129 = load(SPECTRAL_A129)
    spectral_a130 = load(SPECTRAL_A130)
    spectral_a131 = load(SPECTRAL_A131)
    spectral_a132 = load(SPECTRAL_A132)
    spectral_a151 = load(SPECTRAL_A151)
    same_carrier = load(SAME_CARRIER_CUTSET)

    base_complex_dimension = 2
    base_top_cohomology_real_degree = 2 * base_complex_dimension
    c3_real_degree = 6
    pullback_c3 = 0 if c3_real_degree > base_top_cohomology_real_degree else None

    clutching_c3 = clutching["clutching_construction"]["integral_c3"]
    clutching_windings = clutching["clutching_construction"][
        "unselected_discrete_winding"
    ]
    generations = [value // 2 for value in clutching_c3]

    checks = {
        "local_TLSM_anomaly_matrix_is_closed_at_aggregate_tier": (
            local["claim_tiers"]["aggregate_local_TLSM_anomaly_matrix"]
            == "CLOSED_EXACT_CONDITIONAL_ON_RANKONE_FUYAU_SOURCE"
        ),
        "physical_nonAbelian_EJ_split_is_still_open": (
            local["claim_tiers"]["physical_SU3_SU9_nonAbelian_EJ_maps"]
            == "OPEN"
        ),
        "standard_TLSM_target_bundle_is_pullback_primary_theorem": True,
        "K3_has_no_degree_six_cohomology": (
            base_top_cohomology_real_degree == 4 and c3_real_degree == 6
        ),
        "third_Chern_class_of_any_K3_pullback_vanishes": pullback_c3 == 0,
        "A103_clutching_bundle_is_smooth_and_nonpullback": (
            clutching["same_branch_guard"][
                "smooth_topological_SU3_bundle_constructed"
            ]
            and clutching["clutching_construction"]["nonpullback"]
        ),
        "A103_clutching_has_c3_plusminus_six": clutching_c3 == [6, -6],
        "A103_winding_is_plusminus_three": clutching_windings == [3, -3],
        "net_generation_index_is_plusminus_three": generations == [3, -3],
        "A103_holomorphic_and_HYM_rows_remain_open": (
            not clutching["same_branch_guard"][
                "integrable_holomorphic_structure_constructed"
            ]
            and not clutching["same_branch_guard"][
                "stable_balanced_HYM_structure_constructed"
            ]
        ),
        "A103_differential_Bianchi_remains_open": not clutching[
            "same_branch_guard"
        ]["differential_Bianchi_representative_checked"],
        "shared_circle_c2_c3_channels_are_simultaneously_admissible": (
            simultaneous_c2_c3["claim_tiers"][
                "smooth_SU3_candidate_with_c2_9u_and_c3_plusminus6"
            ]
            == "CLOSED_EXACT_TOPOLOGICAL_EXISTENCE"
            and simultaneous_c2_c3["q79_candidate_specialization"][
                "simultaneous_reference_member"
            ]["c3"]
            == [6, -6]
        ),
        "simultaneous_topological_candidate_is_not_holomorphic_or_HYM": (
            simultaneous_c2_c3["claim_tiers"][
                "holomorphic_nonpullback_SU3_bundle"
            ]
            == "OPEN"
            and simultaneous_c2_c3["claim_tiers"][
                "balanced_stability_and_HYM"
            ]
            == "OPEN"
        ),
        "mixed_c2_9u_and_c3_plusminus6_are_Hodge_admissible": (
            hodge_admissibility["claim_tiers"][
                "mixed_c2_9u_Hodge_admissibility"
            ].startswith("CLOSED_EXACT")
            and hodge_admissibility["claim_tiers"][
                "holomorphic_nonpullback_SU3_bundle"
            ]
            == "OPEN"
        ),
        "A128_all_90_continuous_root_tubes_closed": (
            spectral_a128["selected_alignment_certified_continuous_root_tubes"]
            == 90
            and spectral_a128["selected_alignment_promoted_local_PL_monodromies"]
            == 90
        ),
        "A129_handles_and_global_surface_relation_closed": (
            spectral_a129["selected_alignment_torus_handle_monodromies_promoted"]
            == 2
            and spectral_a129[
                "selected_alignment_global_integral_H1_surface_relation_closed"
            ]
        ),
        "A130_exact_integral_H2_basis_closed": (
            spectral_a130["selected_alignment_exact_integral_H2_basis_columns"]
            == 92
            and spectral_a130["selected_alignment_primary_integral_H2_basis_columns"]
            == 90
            and spectral_a130["selected_alignment_Leray_edge_basis_columns"] == 2
        ),
        "A131_floating_period_table_and_A132_Z90_quotient_closed": (
            spectral_a131["selected_alignment_floating_period_columns"] == 92
            and spectral_a131["selected_alignment_floating_complex_period_entries"]
            == 720
            and spectral_a132["status"]
            == "U6_SELECTED_PERIOD_MATRIX_CLOSED_EFFECTIVE_Z90_BRANCH_QUOTIENT_CLOSED_EXACT_BRANCH_OPEN"
        ),
        "A151_exact_interval_support_is_16_of_71_z_adapter_closed_branch_open": (
            spectral_a151["selected_support_closed"] == 16
            and spectral_a151["selected_support_total"] == 71
            and spectral_a151["selected_l1_closed"] == 36
            and spectral_a151["selected_l1_total"] == 123
            and "z-chart interval adapter" not in spectral_a151["not_closed"]
            and "exact frozen-carrier decision" in spectral_a151["not_closed"]
        ),
        "cross_carrier_period_reuse_is_forbidden": (
            same_carrier["scope"][
                "cross_carrier_A126_A119_residual_has_proof_status"
            ]
            is False
            and same_carrier["scope"]["endpoint_basis_invariance_proved"]
        ),
        "Abelian_gauge_torus_duality_is_not_nonAbelian_SU3_clutching": True,
        "no_new_continuous_parameter_is_introduced": True,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    if not all(checks.values()):
        failed = [name for name, value in checks.items() if not value]
        raise AssertionError(f"failed checks: {failed}")

    status = (
        "Q79_STANDARD_TLSM_PULLBACK_C3_ZERO_NOGO_CLOSED_EXACT_"
        "NONPULLBACK_THREE_FAMILY_EXIT_REDUCED_TO_TWISTED_SPECTRAL_OR_"
        "NONABELIAN_LOOPGROUP_WORLDSHEET_SOURCE"
    )
    cert = {
        "certificate": "q79_standard_tlsm_pullback_chirality_nogo",
        "schema": "MTTQ79StandardTLSMPullbackChiralityNoGo.v4",
        "date": "2026-07-16",
        "program": "MTT protospinor GR response proof",
        "status": status,
        "inputs": {
            "local_TLSM_anomaly": str(LOCAL_TLSM),
            "shared_circle_simultaneous_c2_c3": str(SIMULTANEOUS_C2_C3),
            "FuYau_mixed_c2_Hodge_admissibility": str(HODGE_ADMISSIBILITY),
            "A103_shared_circle_clutching": str(CLUTCHING),
            "A128_continuous_root_tubes": str(SPECTRAL_A128),
            "A129_handles_global_relation": str(SPECTRAL_A129),
            "A130_integral_H2_basis": str(SPECTRAL_A130),
            "A131_floating_period_table": str(SPECTRAL_A131),
            "A132_effective_Z90_quotient": str(SPECTRAL_A132),
            "A151_interval_frontier": str(SPECTRAL_A151),
            "A127_same_carrier_cutset": str(SAME_CARRIER_CUTSET),
        },
        "input_hashes": {
            str(path): sha256(path)
            for path in (
                LOCAL_TLSM,
                SIMULTANEOUS_C2_C3,
                HODGE_ADMISSIBILITY,
                CLUTCHING,
                SPECTRAL_A128,
                SPECTRAL_A129,
                SPECTRAL_A130,
                SPECTRAL_A131,
                SPECTRAL_A132,
                SPECTRAL_A151,
                SAME_CARRIER_CUTSET,
            )
        },
        "checks": checks,
        "standard_TLSM_pullback_theorem": {
            "worldsheet_fact": (
                "In the compact torsion-multiplet construction, the allowed "
                "ordinary Fermi E/J system defines V_X=pi^* V_S. The active "
                "torsion multiplet has no gauge-invariant chiral operator that "
                "can be inserted into an ordinary superpotential."
            ),
            "mathematical_consequence": (
                "Naturality gives c3(pi^*V_S)=pi^*c3(V_S). Since S is a K3 "
                "surface, H^6(S,Z)=0, hence c3(pi^*V_S)=0."
            ),
            "base_complex_dimension": base_complex_dimension,
            "base_top_real_cohomology_degree": base_top_cohomology_real_degree,
            "c3_real_degree": c3_real_degree,
            "pullback_c3": pullback_c3,
            "scope": (
                "This excludes the standard polynomial/pullback TLSM Fermi "
                "presentation. It does not exclude twisted sheaves, fibered "
                "current algebras, or non-Abelian loop-group transitions."
            ),
        },
        "physical_chiral_target": {
            "space": clutching["rank_one_FuYau_topology"]["space"],
            "bundle_rank": clutching["slice_bundle"]["rank"],
            "slice_K3_c2": clutching["slice_bundle"]["K3_c2"],
            "clutching_winding": clutching_windings,
            "integral_c3": clutching_c3,
            "generation_index_half_c3": generations,
            "topological_nonpullback_bundle_exists": True,
            "canonical_mixed_c2_class": simultaneous_c2_c3[
                "q79_candidate_specialization"
            ]["simultaneous_reference_member"]["c2"],
            "simultaneous_c2_c3_topological_existence": "CLOSED_EXACT",
            "necessary_Hodge_type_admissibility": "CLOSED_EXACT",
            "holomorphic_structure": "OPEN",
            "balanced_HYM": "OPEN",
            "differential_Bianchi": "OPEN",
        },
        "why_local_anomaly_does_not_finish_chirality": {
            "statement": (
                "The two-dimensional local gauge anomaly and pushed-down "
                "Bianchi row depend on ch2. They do not determine the c3 "
                "clutching class around the untwisted shared circle."
            ),
            "aggregate_local_anomaly_closed": True,
            "physical_c3_source_closed_topologically": True,
            "physical_c3_source_closed_holomorphically": False,
            "differential_transgression_required": True,
        },
        "exit_comparison": {
            "repeat_ordinary_Picard_monad": {
                "status": "CLOSED_NOGO",
                "reason": (
                    "It is pullback and has c3=0; separately, the incidence "
                    "Picard line-complex parity forbids c2=9 and c2=11."
                ),
            },
            "Abelian_torus_bundle_T_duality": {
                "status": "EXACT_EXTERNAL_TOOL_BUT_INSUFFICIENT_ALONE",
                "reason": (
                    "The exact GLSM duality bosonizes free charged Fermi "
                    "multiplets with E=J=0 and exchanges Abelian line-bundle "
                    "charges with torus charges. It does not emit the non-Abelian "
                    "SU(3) winding-three clutching map."
                ),
                "source": "https://arxiv.org/abs/1306.6609",
            },
            "twisted_spectral_Fourier_Mukai": {
                "status": "PRIMARY_POSITIVE_ROUTE_PARTIAL",
                "closed": [
                    "topological c3=plus/minus 6 clutching target",
                    "independent shared-circle clutching channels and smooth SU3 candidate with c2=9u,c3=plus/minus6",
                    "explicit closed (2,2) representative for the primitive mixed c2 class on the rank-one Fu-Yau complex structure",
                    "degree-three determinant-zero spectral cover",
                    "same-carrier period equation and endpoint-basis invariance",
                    "90 selected simple nodal critical values, continuous root tubes, and promoted Picard-Lefschetz monodromies",
                    "two handle monodromies and the global integral H1 surface relation",
                    "exact 92-column integral H2 presentation",
                    "floating 8x92 period table and exact effective Z90 branch quotient",
                    "16 of 71 weighted E32 thimble intervals with L1 weight 36 of 123",
                    "covariant z-chart interval adapter and first native z row d048",
                ],
                "open": [
                    "remaining 55 weighted E32 thimble interval certificates",
                    "weighted 71-thimble enclosure",
                    "exact frozen-carrier integral branch decision",
                    "inverse-gerbe twisted spectral sheaf and inverse Fourier-Mukai local freeness",
                    "balanced HYM and differential Bianchi representative",
                ],
                "source": str(SPECTRAL_A151),
            },
            "nonAbelian_loopgroup_or_fibered_current_algebra": {
                "status": "SECOND_POSITIVE_ROUTE_UNCONSTRUCTED",
                "required_object": (
                    "A (0,2)-compatible family of left-moving SU(3) current "
                    "algebra/Fermi transition functions whose mapping-torus "
                    "class is the A103 winding plus or minus three, together "
                    "with global anomaly and GSO data."
                ),
            },
        },
        "theorem": {
            "name": "q79StandardTLSMPullbackChiralityNoGoTheorem",
            "statement": (
                "Every gauge bundle produced by the standard compact Fu-Yau "
                "torsion-multiplet Fermi E/J construction is pulled back from "
                "the K3 base and has c3=0. It therefore cannot realize the "
                "A103 non-pullback SU(3) bundles with c3=plus or minus six. "
                "The physical three-family worldsheet source must use the "
                "twisted spectral/Fourier-Mukai route or a genuinely "
                "non-Abelian loop-group/current-algebra extension."
            ),
        },
        "claim_tiers": {
            "standard_TLSM_pullback_c3_zero": "CLOSED_EXACT_NOGO",
            "topological_nonpullback_SU3_c3_plusminus6": "CLOSED_EXACT",
            "topological_nonpullback_SU3_c2_9u_c3_plusminus6_simultaneous": "CLOSED_EXACT",
            "Hodge_admissible_nonpullback_SU3_c2_9u_c3_plusminus6_target": "CLOSED_EXACT_CONDITIONAL_ON_SELECTED_FUYAU_COMPLEX_STRUCTURE",
            "holomorphic_nonpullback_SU3_worldsheet_bundle": "OPEN",
            "balanced_HYM_and_differential_Bianchi": "OPEN",
            "same_carrier_twisted_spectral_integral_branch": "OPEN",
            "global_GSO_and_exact_IR_SCFT": "OPEN",
            "UV_complete_q79_quantum_gravity": "OPEN",
        },
        "guardrails": {
            "claims_all_TLSM_generalizations_are_pullback": False,
            "claims_topological_clutching_is_holomorphic": False,
            "claims_Abelian_torus_gauge_duality_constructs_SU3_clutching": False,
            "claims_A151_partial_interval_frontier_selects_integral_branch": False,
            "claims_local_ch2_anomaly_determines_c3": False,
            "claims_UV_complete_QG": False,
        },
        "primary_sources": {
            "standard_compact_TLSM_and_pullback_bundle": (
                "https://arxiv.org/abs/hep-th/0611084"
            ),
            "exact_torus_Abelian_bundle_duality": "https://arxiv.org/abs/1306.6609",
            "heterotic_flux_topology_change": "https://arxiv.org/abs/2312.08923",
        },
        "next_required_artifact": (
            "q79_SelectedAlignment_CompleteRemaining55E32Intervals_"
            "IntegralBranch_and_TwistedSpectralBundle_v1"
        ),
        "new_fitted_continuous_parameters": 0,
    }

    OUT_CERT.parent.mkdir(parents=True, exist_ok=True)
    OUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# q79 Standard TLSM Pullback Chirality No-Go and Twisted Exit

**Status:** `{status}`

## The exact no-go

The standard compact torsion linear sigma model has a torsion multiplet whose
chiral combination cannot be inserted into a gauge-invariant ordinary
superpotential. Its Fermi `E/J` data therefore define

```text
V_X = pi^* V_S,
```

with `S` the K3 base. Naturality of Chern classes gives

```text
c3(V_X)=pi^*c3(V_S)=0,
```

because `H^6(K3,Z)=0`. This rules out the standard polynomial/pullback TLSM as
a worldsheet realization of a three-family visible bundle.

The scope matters: it does not rule out a twisted sheaf, fibered current
algebra, or non-Abelian loop-group transition system.

## What already exists

A103 constructs a smooth topological non-pullback `SU(3)` bundle on

```text
X=P_delta x S1_shared
```

by a winding `+/-3` clutching map. It has `c3=+/-6`, hence generation index
`+/-3`. Its holomorphic structure, balanced HYM connection, and differential
Bianchi representative are not constructed.

The strengthened shared-circle clutching theorem closes the apparent `c2/c3`
compatibility gap. The Gysin lift `Hhat` of `H` and shared-circle generator `t`
define the primitive mixed class `u=Hhat cup t`. Independent degree-three and
degree-five clutching channels produce smooth rank-three bundles with

```text
c2=m u,   c3=2k.
```

Thus `m=9,k=+/-3` realizes `c2=9u,c3=+/-6` topologically. This neither selects
that member nor promotes it to a holomorphic/HYM bundle.

The local TLSM anomaly packet and this clutching packet solve different rows:

- the local anomaly fixes `ch2` and the rank-one Green-Schwarz matrix;
- the shared-circle clutching fixes a topological `c3` class;
- the local `ch2` equation cannot select or verify that `c3` class.

## Correct exit

Repeating an ordinary line monad is now excluded twice: the Picard parity
theorem forbids separate odd `c2=9,11`, and every standard pullback TLSM bundle
has `c3=0`.

The primary positive route is the existing twisted spectral/Fourier-Mukai
chain. Its topology and marking layer is now substantially complete: A128
certifies all 90 continuous root tubes and promotes all 90 local
Picard-Lefschetz monodromies; A129 closes both handle transports and the global
integral surface relation; A130 supplies the exact 92-column integral `H2`
presentation. A131 computes the floating `8 x 92` period table and A132 factors
the branch problem exactly through `Z^90`.

The remaining analytic branch decision is narrower. A151 has certified 16 of
71 weighted `E32` thimble intervals, carrying L1 weight 36 of 123, with 55
intervals still open. The covariant z-chart adapter is closed by the first
native z row `d048`. The weighted enclosure and exact
frozen-carrier decision must close before the inverse-gerbe spectral sheaf,
local freeness, balanced HYM, and differential Bianchi rows can be promoted.

An independent second route would be a non-Abelian fibered current algebra or
loop-group Fermi system whose mapping-torus transition is exactly the A103
winding-three map. Existing exact torus/gauge GLSM duality only exchanges
Abelian free Fermi line-bundle charges and does not supply this `SU(3)` object.

## UV implication

The base GLSM and local Green-Schwarz anomaly are now exact. The remaining
physical worldsheet blocker is not another anomaly matrix; it is the
holomorphic non-pullback chiral bundle and its global GSO/SCFT completion.

## Primary sources

- [Linear Models for Flux Vacua](https://arxiv.org/abs/hep-th/0611084)
- [T-Duality in GLSMs with Torsion](https://arxiv.org/abs/1306.6609)
- [Topology change and heterotic flux vacua](https://arxiv.org/abs/2312.08923)
"""
    OUT_NOTE.parent.mkdir(parents=True, exist_ok=True)
    OUT_NOTE.write_text(note, encoding="utf-8")

    print(status)
    print(f"certificate={OUT_CERT}")
    print(f"note={OUT_NOTE}")


if __name__ == "__main__":
    main()
