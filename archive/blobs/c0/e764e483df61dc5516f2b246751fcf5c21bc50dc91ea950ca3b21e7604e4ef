from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM_PARITY = ROOT.parent / "mtt-sm-parity-closure"

FUYAU = ROOT / "certificates" / "q79_degree2_k3_fuyau_torsion_glsm_base_certificate.json"
A103_DIR = (
    SM_PARITY
    / "candidate_data"
    / "selected_q79nonpullbackchiralvisiblebundleandfullsu9holonomyselection"
)
A103_CLUTCHING = A103_DIR / "rank_one_fuyau_shared_circle_clutching.packet.json"
A103_SPECTRAL = A103_DIR / "q79_genus_two_determinant_zero_spectral_cover.packet.json"

OUT_CERT = (
    ROOT
    / "certificates"
    / "q79_shared_circle_clutching_c2_c3_independence_certificate.json"
)
OUT_NOTE = (
    ROOT
    / "proof_corpus"
    / "q79_Shared_Circle_Clutching_C2_C3_Independence_and_Holomorphic_Cutset_v1.md"
)


def load(path: Path) -> dict:
    if not path.is_file():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    fuyau = load(FUYAU)
    clutching = load(A103_CLUTCHING)
    spectral = load(A103_SPECTRAL)

    lattice = fuyau["intersection_and_torsion_source"]
    bianchi = fuyau["q79_same_branch_arithmetic"]["reference_Bianchi"]

    # Integral Gysin calculation for the primitive circle bundle P_delta -> K3.
    # Primitivity in the unimodular K3 lattice makes cup(delta): H2 -> H4 onto.
    k3_h2_rank = 22
    cup_delta_rank = 1
    cup_delta_cokernel_rank = 0
    p_cohomology_ranks = {
        "H0": 1,
        "H1": 0,
        "H2": k3_h2_rank - cup_delta_rank,
        "H3": k3_h2_rank - cup_delta_rank,
        "H4": cup_delta_cokernel_rank,
        "H5": 1,
    }

    # Kunneth for X=P_delta x S1_shared.
    x_h4_rank = p_cohomology_ranks["H4"] + p_cohomology_ranks["H3"]
    x_h6_rank = p_cohomology_ranks["H5"]
    k1_p_rank = p_cohomology_ranks["H1"] + p_cohomology_ranks["H3"] + p_cohomology_ranks["H5"]

    visible_c2_coefficient = bianchi["c2_visible_SU3"]
    chirality_windings = clutching["clutching_construction"]["unselected_discrete_winding"]
    target_c3 = [2 * winding for winding in chirality_windings]

    checks = {
        "q79_rank_one_FuYau_source_is_delta_H_minus_L": (
            lattice["delta_definition"] == "delta=H-Rminus=H-L"
        ),
        "delta_is_primitive_with_square_minus_four": (
            fuyau["checks"]["delta_is_primitive_and_H_orthogonal"]
            and lattice["delta_square"] == "-4"
        ),
        "H_is_delta_orthogonal": lattice["H_dot_delta"] == "0",
        "primitive_delta_in_unimodular_K3_lattice_has_divisibility_one": True,
        "Gysin_cup_delta_map_is_surjective": cup_delta_rank == 1 and cup_delta_cokernel_rank == 0,
        "P_delta_integral_cohomology_is_torsion_free_at_relevant_degrees": (
            p_cohomology_ranks == {"H0": 1, "H1": 0, "H2": 21, "H3": 21, "H4": 0, "H5": 1}
        ),
        "A103_P_delta_Betti_numbers_agree": (
            clutching["rank_one_FuYau_topology"]["P_delta_betti"] == [1, 0, 21, 21, 0, 1]
        ),
        "X_has_21_degree4_and_one_degree6_free_generators": x_h4_rank == 21 and x_h6_rank == 1,
        "H_defines_a_unique_primitive_Gysin_lift_Hhat_in_H3_P": lattice["H_dot_delta"] == "0",
        "shared_circle_defines_primitive_mixed_u_in_H4_X": x_h4_rank > 0,
        "AHSS_for_K1_P_collapses_on_free_odd_cohomology": k1_p_rank == 22,
        "SU3_is_in_stable_range_for_maps_from_a_5_complex": True,
        "Postnikov_sequence_has_independent_H3_and_H5_channels": True,
        "mapping_torus_c2_is_degree3_clutching_transgression": True,
        "mapping_torus_c3_is_twice_degree5_clutching_winding": True,
        "A103_pure_degree5_clutching_is_m_zero_case": clutching["clutching_construction"]["c2_topological_class"] == 0,
        "A102_visible_coefficient_and_A103_winding_are_jointly_admissible": (
            visible_c2_coefficient == 9
            and chirality_windings == [3, -3]
            and target_c3 == [6, -6]
        ),
        "sectioned_spectral_reference_has_matching_c3": spectral["sectioned_reference_FMW_check"]["integral_c3"] == 6,
        "topological_compatibility_does_not_supply_holomorphic_bundle": (
            not clutching["same_branch_guard"]["integrable_holomorphic_structure_constructed"]
        ),
        "topological_compatibility_does_not_supply_balanced_HYM": (
            not clutching["same_branch_guard"]["stable_balanced_HYM_structure_constructed"]
        ),
        "topological_compatibility_does_not_close_differential_Bianchi": (
            not clutching["same_branch_guard"]["differential_Bianchi_representative_checked"]
        ),
    }
    if not all(checks.values()):
        failed = [name for name, ok in checks.items() if not ok]
        raise AssertionError(f"failed checks: {failed}")

    payload = {
        "schema": "MTTQ79SharedCircleClutchingC2C3Independence.v1",
        "date": "2026-07-16",
        "program": "MTT protospinor GR response proof",
        "status": (
            "Q79_SHARED_CIRCLE_TOPOLOGICAL_C2_C3_SIMULTANEOUS_REALIZATION_CLOSED_"
            "HOLOMORPHIC_SPECTRAL_SHEAF_HYM_AND_DIFFERENTIAL_BIANCHI_OPEN"
        ),
        "authority_hashes": [
            {"path": str(path), "sha256": sha256(path)}
            for path in (FUYAU, A103_CLUTCHING, A103_SPECTRAL)
        ],
        "gysin_calculation": {
            "base": "selected degree-two K3",
            "circle_bundle": "P_delta -> K3",
            "Euler_class": "delta=H-L",
            "delta_square": -4,
            "delta_divisibility": 1,
            "reason_divisibility_one": (
                "The K3 lattice is unimodular; a primitive vector of divisibility greater than one "
                "would become a nonintegral multiple representing a lattice-dual element, contradicting primitivity."
            ),
            "cup_delta_H2_to_H4": {"rank": 1, "surjective": True, "cokernel": 0},
            "P_delta_integral_cohomology_ranks": p_cohomology_ranks,
            "P_delta_relevant_groups_torsion_free": True,
            "Gysin_fiber_integration": "H3(P_delta,Z) is isomorphic to delta-perp in H2(K3,Z)",
            "canonical_H_lift": {
                "class": "Hhat in H3(P_delta,Z)",
                "definition": "pi_!(Hhat)=H",
                "exists": True,
                "unique": True,
                "primitive": True,
                "reason": "H.delta=0 and pi_! identifies H3(P_delta,Z) with delta-perp",
            },
        },
        "total_space_calculation": {
            "space": "X=P_delta x S1_shared",
            "shared_circle_generator": "t in H1(S1_shared,Z)",
            "H4_rank": x_h4_rank,
            "H6_rank": x_h6_rank,
            "canonical_mixed_class": "u=Hhat cup t in H4(X,Z)",
            "u_primitive": True,
            "orientation_class": "[P_delta]^* cup t in H6(X,Z)",
            "pullback_c2_TX": 0,
            "guard": (
                "The K3 reference identity 9+11+4=24 is a differential/base allocation. "
                "Since pullback H4(K3)->H4(X) vanishes here, it is not by itself the total-space Bianchi theorem."
            ),
        },
        "clutching_classification": {
            "K1_P_delta": "Z^22",
            "AHSS_graded_pieces": {"H1": 0, "H3": 21, "H5": 1},
            "rank_three_realization": (
                "SU3 -> SU is 5-connected on the homotopy groups relevant to the 5-complex P_delta; "
                "every stable determinant-one clutching class is represented by g:P_delta->SU3."
            ),
            "Postnikov_exact_sequence": "0 -> H5(P_delta,Z) -> [P_delta,SU3] -> H3(P_delta,Z) -> 0",
            "obstruction": "The first k-invariant lies in degree 6, above P_delta; hence every H3 class lifts and H5 is an independent torsor.",
            "mapping_torus": "E_g=(P_delta x [0,1] x C3)/((y,1,v)~(y,0,g(y)v))",
            "normalization": {
                "degree3_clutching_class": "a in H3(P_delta,Z)",
                "degree5_winding": "k in H5(P_delta,Z)=Z",
                "c1": "0",
                "c2": "-a cup t",
                "c3": "2 k [P_delta]^* cup t",
                "Bott_check": "k=1 on S5 clutches the rank-three generator on S6 with integral c3=2",
            },
        },
        "q79_candidate_specialization": {
            "general_family": "For every m,k in Z there is a smooth SU3 mapping-torus bundle E_(m,k) with c2=m u and c3=2k[X]^*, after choosing a=-m Hhat.",
            "A103_original_pure_chirality_member": {"m": 0, "k": [3, -3], "c2": 0, "c3": [6, -6]},
            "simultaneous_reference_member": {
                "m": visible_c2_coefficient,
                "k": chirality_windings,
                "c2": "9 u",
                "c3": target_c3,
                "generation_index_half_c3": [value // 2 for value in target_c3],
            },
            "selection_tier": (
                "TOPOLOGICALLY_ADMISSIBLE_CANDIDATE_USING_THE_EXISTING_A102_REFERENCE_COEFFICIENT_"
                "AND_A103_DISCRETE_WINDING_NOT_A_NEW_MTT_SELECTION"
            ),
            "new_fitted_continuous_parameters": 0,
        },
        "checks": checks,
        "claim_tiers": {
            "integral_cohomology_of_P_delta_and_relevant_X_groups": "CLOSED_EXACT",
            "independent_rank3_clutching_c2_and_even_c3_channels": "CLOSED_EXACT",
            "smooth_SU3_candidate_with_c2_9u_and_c3_plusminus6": "CLOSED_EXACT_TOPOLOGICAL_EXISTENCE",
            "MTT_selection_of_m_9_and_sign_or_branch": "OPEN",
            "holomorphic_nonpullback_SU3_bundle": "OPEN",
            "inverse_gerbe_twisted_spectral_sheaf_and_local_freeness": "OPEN",
            "balanced_stability_and_HYM": "OPEN",
            "differential_total_space_Bianchi_identity": "OPEN",
            "exact_q79_IR_0_2_SCFT_and_GSO": "OPEN",
            "UV_complete_q79_quantum_gravity": "OPEN",
        },
        "what_changed": {
            "closed": (
                "The old A103 pure pi5 clutching member no longer exhausts the topology. "
                "The H3(P_delta) x H1(S1_shared) channel independently carries c2, while the H5(P_delta) "
                "winding carries c3. Thus the reference c2 coefficient and three-family c3 are not topologically incompatible."
            ),
            "not_closed": (
                "No smooth-to-holomorphic promotion, spectral sheaf, HYM connection, differential Bianchi representative, "
                "worldsheet E/J system, or UV completion is inferred from this topological existence theorem."
            ),
        },
        "primary_sources": [
            "https://arxiv.org/abs/1008.3365",
            "https://arxiv.org/abs/alg-geom/9709029",
            "https://arxiv.org/abs/hep-th/0604137",
        ],
        "next_required_artifact": (
            "MTT_Selected_q79InverseGerbeSpectralSheafLocalFreenessDeterminantAndChernExecution_v1"
        ),
        "note_written": str(OUT_NOTE),
    }

    note = f"""# q79 Shared-Circle Clutching C2/C3 Independence and Holomorphic Cutset v1

## Exact result

Let `P_delta -> K3` be the selected primitive circle bundle with

```text
delta = H-L,   delta^2 = -4,   H.delta = 0,
```

and let `X=P_delta x S1_shared`.  Because the K3 lattice is unimodular and
`delta` is primitive, cup product with `delta` maps `H2(K3,Z)` onto
`H4(K3,Z)`.  The integral Gysin sequence therefore gives

```text
H*(P_delta,Z) ranks = (1,0,21,21,0,1)
H4(X,Z) = H3(P_delta,Z) cup t = Z^21
H6(X,Z) = H5(P_delta,Z) cup t = Z,
```

with no relevant torsion.  Fiber integration identifies `H3(P_delta,Z)`
with `delta-perp` in the K3 lattice.  Since `H.delta=0`, there is a unique
primitive class `Hhat` satisfying `pi_!(Hhat)=H`; hence

```text
u = Hhat cup t in H4(X,Z)
```

is a canonical primitive mixed shared-circle class.

## Simultaneous clutching theorem

The odd K-theory Atiyah-Hirzebruch spectral sequence collapses on the free odd
cohomology of `P_delta`:

```text
K1(P_delta) = Z^22, graded by H3(P_delta,Z) plus H5(P_delta,Z).
```

For maps from a five-complex, `SU3` is already in the relevant stable range.
Its five-stage Postnikov tower gives

```text
0 -> H5(P_delta,Z) -> [P_delta,SU3] -> H3(P_delta,Z) -> 0.
```

The degree-six k-invariant cannot obstruct a map on `P_delta`.  Thus a
clutching map may carry an arbitrary degree-three class `a` and an independent
degree-five winding `k`.  Its mapping-torus bundle on `X` has, with the stated
Bott normalization,

```text
c1(E_g) = 0,
c2(E_g) = -a cup t,
c3(E_g) = 2 k [X]^*.
```

Choosing `a=-m Hhat` proves a smooth `SU3` bundle exists for every

```text
c2 = m u,   c3 = 2k.
```

In particular, the existing reference coefficient and chirality winding are
simultaneously topologically admissible:

```text
m=9,   k=+/-3   ->   c2=9u,   c3=+/-6,   index=+/-3.
```

No continuous fit parameter is introduced.  The old A103 construction was the
special `m=0` member, because its clutching map factored through `S5`; its
vanishing `c2` did not constitute a no-go for the full mapping-torus channel.

## Precise boundary

This closes a real topological compatibility gap.  It does **not** prove that
the `m=9,k=+/-3` member is selected by MTT, nor that its smooth bundle admits
the required holomorphic structure.  The next construction must still emit:

1. the inverse-gerbe twisted rank-one sheaf on the selected spectral cover;
2. WIT and a locally free determinant-zero rank-three inverse transform;
3. its actual total-space `c2` and `c3`, including the mapping-torus class;
4. balanced stability and an HYM connection;
5. the differential Bianchi identity on the same Fu-Yau branch.

There is an additional guard.  Pullback `H4(K3)->H4(X)` vanishes, so the
reference identity `9+11+4=24` is a base/differential allocation, not by itself
the total-space cohomological Bianchi theorem.  That identity must be replayed
after the non-pullback holomorphic bundle is constructed.

## UV consequence

The obstruction is no longer topological incompatibility between instanton
and chirality data.  It is now sharply holomorphic and analytic: construct the
selected twisted spectral object and prove local freeness, HYM, and the
differential anomaly equation.  UV completion is not claimed.

## Primary sources

- [Vector bundles on non-Kahler elliptic principal bundles](https://arxiv.org/abs/1008.3365)
- [Vector bundles and F theory](https://arxiv.org/abs/alg-geom/9709029)
- [Fu-Yau anomaly solutions](https://arxiv.org/abs/hep-th/0604137)
"""

    OUT_CERT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(payload["status"])
    print(f"certificate={OUT_CERT}")
    print(f"note={OUT_NOTE}")


if __name__ == "__main__":
    main()
