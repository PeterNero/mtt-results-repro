from __future__ import annotations

import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent

ODD_LIFT = ROOT / "certificates" / "protospinor_odd_weight_lift_selector_dichotomy_certificate.json"
SPIN_PACKET = (
    TEXPAPERS
    / "mtt-sm-parity-closure"
    / "candidate_data"
    / "selected_q79signedsheetspinliftreduction"
    / "q79_signed_sheet_spin_lift_reduction.packet.json"
)
COVER_PACKET = (
    TEXPAPERS
    / "mtt-sm-parity-closure"
    / "candidate_data"
    / "selected_q79nonpullbackchiralvisiblebundleandfullsu9holonomyselection"
    / "q79_genus_two_determinant_zero_spectral_cover.packet.json"
)
TOPOLOGY_PACKET = (
    TEXPAPERS
    / "mtt-sm-parity-closure"
    / "candidate_data"
    / "selected_q79twistedspectralgerbelifthymandbianchiexecution"
    / "spectral_surface_invariants.packet.json"
)

OUT_CERT = ROOT / "certificates" / "q79_signed_sheet_w2_branch_divisor_reduction_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "q79_Signed_Sheet_w2_and_Branch_Divisor_Reduction_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    odd_lift = load(ODD_LIFT)
    spin = load(SPIN_PACKET)
    cover = load(COVER_PACKET)
    topology = load(TOPOLOGY_PACKET)

    transposition = np.array(
        [[int(entry) for entry in row]
         for row in spin["binary_spin_theorem"]["braid_generators"]["q1_rotation"]],
        dtype=int,
    )
    identity = np.eye(3, dtype=int)
    eigenvalues = sorted(int(round(value)) for value in np.linalg.eigvalsh(transposition))
    minus_multiplicity = eigenvalues.count(-1)

    plane_cubic_degree = 3
    dual_curve_degree = plane_cubic_degree * (plane_cubic_degree - 1)
    h_square = int(cover["q79_genus_two_map"]["H_square"])
    a2b = int(topology["divisor"]["A_squared_B"])
    ramification_pairing_with_h = 2 * a2b
    branch_coefficient_from_pairing = ramification_pairing_with_h // h_square

    # If H=m*h in the even K3 lattice, then 2=H^2=m^2*(2r), so
    # 1=m^2*r. There is no integer solution with m>1.
    possible_nontrivial_divisors = [
        m for m in range(2, 20) if 1 % (m * m) == 0
    ]
    h_is_primitive = not possible_nontrivial_divisors
    branch_lattice_divisibility = dual_curve_degree

    z6_to_z2_parity_images = [
        image for image in range(2) if (6 * image) % 2 == 0 and image == 1
    ]
    z6_to_z4_odd_lift_images = [
        image for image in range(4) if (6 * image) % 4 == 0 and image % 2 == 1
    ]

    checks = {
        "odd_lift_cutset_available": (
            odd_lift["status"]
            == "EVEN_TT_AMBIGUITY_PROVED_SHARED_Z2_SPIN_SELECTOR_CUTSET_ISOLATED_NO_ROOT_SELECTED"
        ),
        "signed_transposition_is_involution": np.array_equal(
            transposition @ transposition, identity
        ),
        "signed_transposition_is_oriented": round(np.linalg.det(transposition)) == 1,
        "signed_transposition_has_two_minus_lines": minus_multiplicity == 2,
        "restriction_total_SW_class_is_1_plus_a_squared": minus_multiplicity == 2,
        "spectral_cover_degree_is_three": (
            cover["determinant_zero_cover"]["degree_over_K3"] == 3
        ),
        "elliptic_plane_cubic_dual_degree_is_six": dual_curve_degree == 6,
        "branch_class_is_pullback_6H": dual_curve_degree == 6,
        "ramification_intersection_independently_gives_6H": (
            ramification_pairing_with_h == 12
            and branch_coefficient_from_pairing == 6
        ),
        "H_square_two_forces_primitive_polarization": (
            h_square == 2 and h_is_primitive
        ),
        "K3_unimodularity_then_gives_branch_divisibility_six": (
            branch_lattice_divisibility == 6
        ),
        "Z6_has_sign_character": z6_to_z2_parity_images == [1],
        "Z6_sign_character_has_no_Z4_lift": z6_to_z4_odd_lift_images == [],
        "global_spin_packet_did_not_prejudge_w2": (
            spin["global_spin_contract"]["fields"]["w2_of_signed_sheet_carrier_proved_zero"]
            is False
        ),
    }
    checks = {name: bool(value) for name, value in checks.items()}

    universal_theorem = {
        "sign_class": "a=(sign o monodromy)^*(generator) in H^1(B_open;Z2)",
        "representation": "rho_plus(sigma)=sign(sigma) P_sigma in SO(3)",
        "restriction_to_transposition_C2": "1 direct-sum sign direct-sum sign",
        "restricted_total_SW_class": "(1+a)^2=1+a^2",
        "injectivity_reason": (
            "restriction H^2(BS3;Z2)->H^2(BC2;Z2) is injective because "
            "transfer followed by restriction multiplies by the odd index 3"
        ),
        "result": "w2(E_rho_plus)=a cup a",
        "Bockstein_form": (
            "a cup a is the Bockstein for 0->Z2->Z4->Z2->0; hence w2=0 "
            "if and only if the sign character lifts to a Z4 character"
        ),
        "status": "CLOSED_BY_REPRESENTATION_AND_NATURALITY",
    }

    branch_theorem = {
        "incidence_cover": (
            "the universal degree-three hyperplane divisor of a smooth plane cubic"
        ),
        "branch_curve_in_linear_system": (
            "the dual curve of the smooth plane cubic, of degree d(d-1)=6"
        ),
        "pullback_map": "iota o phi_H:K3->P2 with phi_H^*O(1)=H",
        "branch_class": "[B]=6H",
        "independent_intersection_check": {
            "R": "K_C=(A+B)|_C because K_(K3xE)=0",
            "R_dot_pi_star_H": "(A+B)^2 A=2 A^2 B=12",
            "six_H_dot_H": "6 H^2=12",
        },
        "H_primitive": h_is_primitive,
        "branch_class_lattice_divisibility": branch_lattice_divisibility,
        "status": "BRANCH_CLASS_AND_DIVISIBILITY_CLOSED",
    }

    complement_decision = {
        "standard_complement_lemma": (
            "For a connected reduced irreducible divisor B in a simply connected "
            "surface, under the usual meridian/Gysin hypotheses, H1(X\\B;Z) is "
            "cyclic of order equal to the lattice divisibility of [B]."
        ),
        "q79_consequence_if_irreducible_reduced_packet_is_supplied": "H1(B_open;Z)=Z6",
        "finite_lift_test": {
            "sign_map": "Z6->Z2 sends a meridian to 1",
            "possible_Z4_images_of_meridian_with_odd_reduction": z6_to_z4_odd_lift_images,
            "conclusion": "no Z4 lift, so a^2 and w2 are nonzero",
        },
        "strict_Spin_consequence": (
            "Under that complement hypothesis, the q79 signed-sheet SO3 carrier "
            "has no strict Spin lift on the branch complement. The remaining lawful "
            "route is a separately proved SpinC cancellation or a different smooth HYM carrier."
        ),
        "actual_missing_check": (
            "certify for the selected alignment that the pulled-back dual sextic is "
            "reduced and irreducible, or directly compute the abelianized branch-complement meridian relation"
        ),
        "status": "STRICT_SPIN_NOGO_CONDITIONAL_ON_SELECTED_BRANCH_COMPLEMENT_H1_Z6",
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "q79_signed_sheet_w2_branch_divisor_reduction",
        "date": "2026-07-15",
        "status": "UNIVERSAL_W2_AND_BRANCH_6H_CLOSED_STRICT_SPIN_NOGO_ONE_COMPLEMENT_CHECK_OPEN",
        "inputs": {
            "odd_lift_dichotomy": str(ODD_LIFT),
            "q79_spin_packet": str(SPIN_PACKET),
            "q79_spectral_cover": str(COVER_PACKET),
            "q79_spectral_topology": str(TOPOLOGY_PACKET),
        },
        "checks": checks,
        "finite_data": {
            "signed_transposition": transposition.tolist(),
            "signed_transposition_eigenvalues": eigenvalues,
            "minus_line_multiplicity": minus_multiplicity,
            "plane_cubic_degree": plane_cubic_degree,
            "dual_curve_degree": dual_curve_degree,
            "H_square": h_square,
            "A_squared_B": a2b,
            "ramification_pairing_with_H": ramification_pairing_with_h,
            "branch_coefficient_from_pairing": branch_coefficient_from_pairing,
            "branch_lattice_divisibility": branch_lattice_divisibility,
            "Z6_to_Z4_odd_lift_images": z6_to_z4_odd_lift_images,
        },
        "universal_w2_theorem": universal_theorem,
        "branch_divisor_theorem": branch_theorem,
        "complement_decision": complement_decision,
        "claim_tiers": {
            "w2_equals_sign_square": "CLOSED",
            "strict_Spin_iff_sign_lifts_to_Z4": "CLOSED",
            "q79_branch_class_6H_and_divisibility_6": "CLOSED",
            "selected_q79_branch_complement_H1_is_Z6": "OPEN_ONE_GEOMETRIC_CHECK",
            "strict_q79_Spin_no_go": "CONDITIONAL_ON_PREVIOUS_ROW",
            "q79_SpinC_cancellation": "OPEN",
        },
        "guardrails": {
            "claims_selected_branch_divisor_irreducibility_already_certified": False,
            "claims_strict_q79_Spin_no_go_unconditional": False,
            "claims_SpinC_follows_from_nonzero_w2": False,
            "claims_local_Dic3_extension_splits": False,
            "uses_observed_physics_data": False,
            "adds_fitted_parameter": False,
        },
        "note_written": str(OUT_NOTE),
    }

    note = r"""# q79 Signed-Sheet w2 and Branch-Divisor Reduction v1

Date: 2026-07-15

## Universal obstruction formula

Let

```text
rho_plus(sigma)=sign(sigma) P_sigma in SO(3)
```

and let `a` be the mod-two sign/discriminant class of the q79 sheet monodromy
on the branch complement. Restriction to a transposition subgroup `C2` gives

```text
rho_plus|C2 = 1 direct-sum sign direct-sum sign.
```

Hence its total Stiefel-Whitney class restricts to

```text
(1+a)^2=1+a^2.
```

Restriction from `S3` to this `C2` is injective in mod-two degree two: transfer
back multiplies by the odd index three. Naturality therefore proves

```text
w2(E_rho_plus)=a cup a.
```

For a degree-one mod-two class, `a cup a` is the Bockstein associated to
`0->Z2->Z4->Z2->0`. Consequently,

```text
strict Spin exists on the branch complement
iff the sign character lifts to a Z4 character.
```

This replaces an unspecified list of binary relator signs by one cohomological
test. It is consistent with the local `Dic_3` result: braid generators lift,
while a global relation may still obstruct the lift.

## q79 branch class

The degree-three spectral cover is pulled back from the universal hyperplane
divisor of a smooth plane cubic. Its branch curve in the hyperplane `P2` is the
dual cubic, whose degree is

```text
d(d-1)=3*2=6.
```

Since the genus-two K3 map pulls `O(1)` back to `H`,

```text
[B]=6H.
```

The spectral-surface intersection data independently reproduces this:

```text
R dot pi^*H=(A+B)^2 A=2 A^2 B=12=6 H^2.
```

Because `H^2=2` in the even K3 lattice, `H` cannot be a nontrivial multiple.
The K3 lattice is unimodular, so `[B]=6H` has lattice divisibility six.

## Conditional final Spin decision

For a connected reduced irreducible divisor in a simply connected surface, the
standard meridian/Gysin sequence gives

```text
H1(K3\B;Z)=Z_div([B]).
```

Thus, once reduced irreducibility is certified for the selected pulled-back
dual sextic,

```text
H1(B_open;Z)=Z6.
```

The sign map `Z6->Z2` exists, but it has no lift to `Z4`: an odd image in `Z4`
has order four and cannot be the image of a generator of `Z6`. Therefore

```text
a^2 != 0,
w2 != 0,
strict q79 Spin fails on the branch complement.
```

This last no-go remains conditional on one selected-geometry check: prove that
the pulled-back dual sextic is reduced and irreducible, or compute the same
abelian meridian relation directly. The trial identity-alignment surface is not
a selected source and is not used to promote this condition.

If the no-go closes, it does not invalidate the proto-spinor. It selects the
other already isolated route: construct a genuine SpinC determinant line with
`c1 mod 2=w2`, or replace the singular sheet carrier by a selected smooth HYM
carrier and recompute its obstruction.

Current status:

```text
UNIVERSAL_W2_AND_BRANCH_6H_CLOSED_STRICT_SPIN_NOGO_ONE_COMPLEMENT_CHECK_OPEN
```
"""

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
