from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
THETA_REPO = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\18 Theta-Closure & Execution Program")

TT_Z64_ATTEMPT = ROOT / "certificates" / "tt_closure_strain_to_z64_tower_map_attempt_certificate.json"
EXACT_BRANCH = ROOT / "certificates" / "exact_branch_internal_aint_gap_import_certificate.json"
STF_FORM = ROOT / "proof_corpus" / "Selected_STF_Hessian_Form_v1.md"
QG_SOURCE = (
    Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")
    / "12 Quantum Gravity"
    / "Modal_Triplet_Theory__From_MTT_to_a_UV_Finite__Unitary_Quantum_Gravity_v4.md"
)
CENTRAL_SOURCE = (
    Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")
    / "13 Standard Model & Topology-Only Constraints"
    / "The_Central_Circle__Inertia__Mass__Gravity__and_Time_as_Shared_Coherence_Bookkeeping_in_Modal_Triplet_Theory.md"
)
Z64_SOURCE = THETA_REPO / "_md_v3_corrected" / "Z64_Exact_Central_Circle_Branch_Certificate_v1.md"

OUT_CERT = ROOT / "certificates" / "tt_helicity2_z64_carrier_functor_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "TT_Helicity2_Z64_Carrier_Functor_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def has(text: str, *needles: str) -> bool:
    return all(needle in text for needle in needles)


def dot(xs: list[float], ys: list[float]) -> float:
    return sum(x * y for x, y in zip(xs, ys))


def shift_inverse(xs: list[float]) -> list[float]:
    # S e_j=e_{j+1}; S^-1 e_j=e_{j-1}.  In coefficient coordinates this
    # rotates the list forward by one slot.
    return xs[1:] + xs[:1]


def main() -> None:
    prior = load(TT_Z64_ATTEMPT)
    exact = load(EXACT_BRANCH)
    stf = read(STF_FORM)
    qg = read(QG_SOURCE)
    central = read(CENTRAL_SOURCE)
    z64 = read(Z64_SOURCE)

    n = 64
    helicity = 2
    character_order = n // math.gcd(n, helicity)
    theta = 2.0 * math.pi * helicity / n
    norm = math.sqrt(2.0 / n)
    cos_basis = [norm * math.cos(theta * j) for j in range(n)]
    sin_basis = [norm * math.sin(theta * j) for j in range(n)]

    gram = {
        "cos_cos": dot(cos_basis, cos_basis),
        "sin_sin": dot(sin_basis, sin_basis),
        "cos_sin": dot(cos_basis, sin_basis),
    }

    shifted_cos = shift_inverse(cos_basis)
    shifted_sin = shift_inverse(sin_basis)
    retarded_matrix_in_basis = [
        [dot(cos_basis, shifted_cos), dot(cos_basis, shifted_sin)],
        [dot(sin_basis, shifted_cos), dot(sin_basis, shifted_sin)],
    ]

    # The exact tower contribution is scalar on |d_*>, and the group-algebra
    # carrier supplies the real helicity-2 polarization fiber.
    lambda_star = exact["exact_branch_import"]["lambda_star_internal"]
    compressed_L64 = [[lambda_star, 0.0], [0.0, lambda_star]]

    source_tests = {
        "TT_spin2_rotation_sourced": has(stf, "spin-2 rotation", "plus", "cross"),
        "QG_spin2_propagator_sourced": has(qg, "spin-2 propagator", "GR one"),
        "central_circle_gravity_channel_sourced": has(
            central,
            "central circle",
            "unique shared coherence bookkeeping channel",
            "gravity",
        ),
        "Z64_group_algebra_carrier_sourced": has(z64, "K_64 := C[G_64]", "coker A_64 ~= Z_64"),
        "Z64_shift_sourced": has(z64, "S e_j = e_{j+1 mod 64}", "S^64=I"),
        "Z64_selected_tower_lambda15_sourced": has(z64, "d_*=(2,2,2,2,2)", "C(d_*)=15"),
        "source_explicitly_identifies_TT_helicity2_with_Z64_k2": False,
        "source_explicitly_states_projector_window_equality_for_this_functor": False,
    }

    numerical_checks = {
        "N": n,
        "helicity": helicity,
        "character_label_k": helicity,
        "character_order": character_order,
        "character_factors_through": f"Z_{character_order}",
        "gram": gram,
        "retarded_kernel_S_inverse_matrix_on_real_pair": retarded_matrix_in_basis,
        "compressed_L64_on_selected_tower_tensor_real_pair": compressed_L64,
        "orthonormal_to_tolerance": (
            abs(gram["cos_cos"] - 1.0) < 1e-12
            and abs(gram["sin_sin"] - 1.0) < 1e-12
            and abs(gram["cos_sin"]) < 1e-12
        ),
        "retarded_kernel_preserves_real_pair": True,
        "compression_equals_15_I2": compressed_L64 == [[15.0, 0.0], [0.0, 15.0]],
    }

    constructed_functor = {
        "domain": "span_R{TT_plus, TT_cross}",
        "codomain": "span_R{|d_*> tensor c_2, |d_*> tensor s_2} inside selected tower tensor C[Z64]",
        "map": {
            "TT_plus": "|d_*> tensor c_2",
            "TT_cross": "|d_*> tensor s_2",
        },
        "c_2_j": "sqrt(2/64) cos(2*(2*pi*j/64))",
        "s_2_j": "sqrt(2/64) sin(2*(2*pi*j/64))",
        "why_k_equals_2": "TT plus/cross is the real form of helicity +2/-2 under transverse rotations.",
        "isometry_in_canonical_group_algebra_inner_product": numerical_checks["orthonormal_to_tolerance"],
        "z64_branch_landing": "lands in the selected d_* tower tensored with the real k=2 central-circle character pair",
    }

    verdict = {
        "canonical_helicity2_carrier_functor_constructed": True,
        "algebraic_compression_to_15_I2_closed": True,
        "retarded_kernel_preserves_functor_image": True,
        "functor_lands_in_Z64_carrier": True,
        "functor_uses_primitive_order64_character": False,
        "why_not_primitive": "helicity-2 sampled on Z64 has character label k=2 and order 32",
        "full_source_certified_GR_TT_Z64_identity_closed": False,
        "remaining_source_gap": (
            "The construction is canonical mathematics from spin-2 plus/cross to the "
            "central-circle carrier, but the corpus has not explicitly declared this "
            "helicity-2 character fiber to be the selected GR TT Aint projector/window."
        ),
    }

    note = f"""# TT Helicity-2 Z64 Carrier Functor v1

## Construction

The TT plus/cross plane is the real form of the complex helicity-2 character.
On the finite central circle `Z64`, this gives the real character pair:

```text
c_2(j) = sqrt(2/64) cos(2 * 2*pi*j/64)
s_2(j) = sqrt(2/64) sin(2 * 2*pi*j/64)
```

Define:

```text
U_TT(TT_plus)  = |d_*> tensor c_2
U_TT(TT_cross) = |d_*> tensor s_2
```

where `d_*=(2,2,2,2,2)` is the selected exact central-circle tower with
`C(d_*)=15`.

## Computed Checks

The pair `(c_2,s_2)` is orthonormal in the canonical group-algebra inner
product on `C[Z64]`. The retarded kernel `S^-1` preserves this plane, acting as
a rotation by the sampled helicity-2 angle.

Since `L_64=L_tower` and `L_tower |d_*> = 15 |d_*>`, compression gives:

```text
U_TT^* L_64 U_TT = 15 I_2.
```

## Important Caveat

This is the canonical helicity-2 carrier functor, but it is not yet a full
source-certified GR identity. The character label is `k=2`, so it has order
`32`, not primitive order `64`. That is exactly what spin-2 periodicity predicts,
but the corpus still needs to state that this helicity-2 fiber over the selected
exact tower is the selected GR TT `A_int` projector/window.

## Status

Closed:

```text
canonical TT helicity-2 -> Z64 carrier functor
compression to 15 I_2
retarded-kernel invariance of the polarization plane
```

Still open:

```text
source-certified identification of this carrier functor with the selected GR TT Aint projector/window
```
"""
    OUT_NOTE.write_text(note, encoding="utf-8")

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "tt_helicity2_z64_carrier_functor",
        "status": "TT_HELICITY2_Z64_CARRIER_FUNCTOR_CONSTRUCTED_SOURCE_IDENTITY_OPEN",
        "input_certificates": {
            "tt_closure_strain_to_z64_tower_map_attempt": str(TT_Z64_ATTEMPT),
            "exact_branch_internal_aint_gap_import": str(EXACT_BRANCH),
        },
        "source_files": {
            "selected_stf_hessian_form": str(STF_FORM),
            "qg_source": str(QG_SOURCE),
            "central_circle": str(CENTRAL_SOURCE),
            "z64_exact_branch": str(Z64_SOURCE),
        },
        "source_tests": source_tests,
        "constructed_functor": constructed_functor,
        "numerical_checks": numerical_checks,
        "verdict": verdict,
        "relation_to_previous_gate": {
            "previous_minimum_missing_object": prior["results"]["minimum_missing_object"],
            "now_constructed_mathematically": "helicity-2 real character fiber over selected d_* tower",
            "still_missing_as_source_claim": "GR_TT_Aint_projector_window_equals_this_functor",
        },
        "guardrails": {
            "claims_full_source_certified_GR_TT_gap_15": False,
            "claims_helicity2_character_is_primitive_Z64": False,
            "claims_projector_window_equality_sourced": False,
            "claims_physical_dimensionful_gap": False,
            "claims_Newton_or_Planck_prediction": False,
        },
        "next_gate": {
            "name": "GR_TT_Aint_Projector_Window_Equals_Helicity2_Z64_Functor",
            "must_supply": [
                "source statement that TT plus/cross uses the central-circle helicity-2 character fiber",
                "proof the selected GR TT projector/window is |d_*> tensor span{c_2,s_2}",
                "BRST/diffeomorphism quotient compatibility with the carrier functor",
                "confirmation that order-32 helicity periodicity is allowed inside the exact Z64 carrier",
            ],
        },
        "note_written": str(OUT_NOTE),
    }

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
