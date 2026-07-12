from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MTT = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")

HELICITY_CERT = ROOT / "certificates" / "tt_helicity2_z64_carrier_functor_certificate.json"
QG_SOURCE = MTT / "12 Quantum Gravity" / "Modal_Triplet_Theory__From_MTT_to_a_UV_Finite__Unitary_Quantum_Gravity_v4.md"
QG_CONSTRUCTIVE = (
    MTT
    / "12 Quantum Gravity"
    / "Constructive_MTT_Quantum_Gravity_I__Borel_Summability_of_the_SPT_Filtered_TT_Sector.md"
)
CENTRAL_SOURCE = (
    MTT
    / "13 Standard Model & Topology-Only Constraints"
    / "The_Central_Circle__Inertia__Mass__Gravity__and_Time_as_Shared_Coherence_Bookkeeping_in_Modal_Triplet_Theory.md"
)
Z64_PROJECTOR = Q79 / "proof_corpus" / "Spectral_Flavor_Projector_Construction_for_Z64_Dyadic_Tower_v1.md"

OUT_CERT = ROOT / "certificates" / "gr_tt_projector_window_helicity2_z64_source_theorem_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "GR_TT_Projector_Window_Helicity2_Z64_Source_Theorem_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def has(text: str, *needles: str) -> bool:
    return all(needle in text for needle in needles)


def main() -> None:
    helicity = load(HELICITY_CERT)
    qg = read(QG_SOURCE)
    qg_constructive = read(QG_CONSTRUCTIVE)
    central = read(CENTRAL_SOURCE)
    z64_projector = read(Z64_PROJECTOR)

    source_tests = {
        "qg_defines_TT_projected_graviton_operator": has(
            qg,
            "projected linearized graviton operator on the TT sector",
            "lambda_",
        )
        or has(qg, "Lichnerowicz operator on TT modes", "A_{\\mathrm{int}}"),
        "qg_defines_SPT_projector_window": has(
            qg,
            "Pi_{\\mathrm{coh}} = \\phi(E)\\,\\psi(A_{\\mathrm{int}})",
            "tau_0",
        ),
        "constructive_qg_defines_physical_TT_sector": has(
            qg_constructive,
            "physical TT sector",
            "TT bundle",
            "symmetric trace-free divergence-free tensors",
        ),
        "central_circle_gravity_bookkeeping_sourced": has(
            central,
            "Gravity, by contrast, operates on the shared circle itself",
            "central circle",
        ),
        "central_circle_unique_shared_channel_sourced": has(
            central,
            "unique shared coherence bookkeeping channel",
            "gravity",
        ),
        "z64_projector_retains_finite_character_carrier": has(
            z64_projector,
            "retained finite Wilson/deck character carrier",
            "K_64 ~= C[Z_64]",
        ),
        "z64_projector_character_spectrum_sourced": has(
            z64_projector,
            "normalized Fourier characters",
            "D_d^* chi_n",
            "chi_{dn}",
        ),
        "z64_projector_selects_dstar_tower": has(
            z64_projector,
            "P_fl selects the tower (2,2,2,2,2)",
            "C(2,2,2,2,2)=5(2^2-1)=15",
        ),
        "source_states_TT_plus_cross_use_central_circle_helicity2_character_fiber": False,
        "source_states_selected_GR_TT_projector_window_equals_dstar_tensor_k2_pair": False,
        "source_states_order32_helicity2_is_allowed_as_GR_TT_subfiber_of_Z64": False,
    }

    partial_closures = {
        "TT_helicity2_carrier_functor_constructed": helicity["verdict"][
            "canonical_helicity2_carrier_functor_constructed"
        ],
        "compression_to_15_I2_closed": helicity["verdict"]["algebraic_compression_to_15_I2_closed"],
        "retarded_kernel_preserves_helicity2_plane": helicity["verdict"][
            "retarded_kernel_preserves_functor_image"
        ],
        "order32_subcharacter_is_mathematically_inside_Z64_carrier": (
            helicity["numerical_checks"]["character_order"] == 32
            and source_tests["z64_projector_retains_finite_character_carrier"]
        ),
        "qg_selects_TT_SPT_projector_window_in_general": source_tests[
            "qg_defines_TT_projected_graviton_operator"
        ]
        and source_tests["qg_defines_SPT_projector_window"],
        "central_circle_is_gravity_shared_channel": source_tests[
            "central_circle_gravity_bookkeeping_sourced"
        ]
        and source_tests["central_circle_unique_shared_channel_sourced"],
    }

    theorem_decision = {
        "source_identity_closed": False,
        "why_not_closed": (
            "Current sources support the GR TT SPT projector/window, the central circle "
            "as the gravity bookkeeping channel, and the retained Z64 finite character "
            "carrier. They do not explicitly identify the selected GR TT projector/window "
            "with |d_*> tensor span{c_2,s_2}."
        ),
        "strongest_now": (
            "A canonical source-compatible candidate: GR TT plus/cross maps to the real "
            "helicity-2 k=2 central-circle character pair over the selected d_* tower, "
            "with compression 15 I_2."
        ),
        "if_missing_source_lemma_is_added": {
            "lemma": "Selected_GR_TT_Projector_Window_Equals_Helicity2_Z64_Functor",
            "consequence": "lambda_GR_TT = 15 in canonical exact-branch internal units",
        },
        "status_if_no_new_source": "HELICITY2_FUNCTOR_READY_SOURCE_IDENTITY_OPEN",
    }

    note = """# GR TT Projector Window Helicity-2 Z64 Source Theorem v1

## Result

The source search does **not** yet close the full identity, but it closes the
surrounding support tightly.

Supported by current sources:

```text
1. QG selects a projected TT graviton operator with SPT projector/window.
2. The central circle is the shared gravity/coherence bookkeeping channel.
3. The Z64 construction retains a finite Wilson/deck character carrier C[Z64].
4. The helicity-2 real character pair k=2 lies inside that carrier.
5. The constructed functor compresses L64 to 15 I_2.
```

Not yet sourced:

```text
selected GR TT A_int projector/window
  =
|d_*> tensor span{c_2,s_2}
```

## Sharp Missing Lemma

The exact missing statement is:

```text
Selected_GR_TT_Projector_Window_Equals_Helicity2_Z64_Functor.
```

If this lemma is supplied, then the already verified algebra promotes to:

```text
lambda_GR,TT = 15
```

in canonical exact-branch internal units.

## Order-32 Point

The helicity-2 pair has character label `k=2`, hence order `32` inside `Z64`.
This is mathematically allowed as a subcharacter of the retained `C[Z64]`
carrier and is exactly the expected spin-2 periodicity. What is not yet sourced
is that GR TT selection chooses this subfiber as its `A_int` projector/window.
"""
    OUT_NOTE.write_text(note, encoding="utf-8")

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "gr_tt_projector_window_helicity2_z64_source_theorem",
        "status": "HELICITY2_FUNCTOR_READY_SOURCE_IDENTITY_OPEN",
        "input_certificates": {
            "tt_helicity2_z64_carrier_functor": str(HELICITY_CERT),
        },
        "source_files": {
            "qg_source": str(QG_SOURCE),
            "constructive_qg_tt_sector": str(QG_CONSTRUCTIVE),
            "central_circle": str(CENTRAL_SOURCE),
            "z64_projector": str(Z64_PROJECTOR),
        },
        "source_tests": source_tests,
        "partial_closures": partial_closures,
        "theorem_decision": theorem_decision,
        "guardrails": {
            "claims_source_identity_closed": False,
            "claims_full_GR_TT_gap_15": False,
            "claims_order32_is_primitive_order64": False,
            "claims_physical_dimensionful_gap": False,
            "claims_Newton_or_Planck_prediction": False,
        },
        "next_gate": {
            "name": "Selected_GR_TT_Projector_Window_Equals_Helicity2_Z64_Functor",
            "minimal_statement": (
                "The selected GR TT SPT internal projector/window is the central-circle "
                "helicity-2 character fiber |d_*> tensor span{c_2,s_2} inside the retained "
                "exact Z64 branch."
            ),
            "proof_obligations": [
                "TT plus/cross response uses central-circle helicity-2 character, not only abstract spin-2 covariance",
                "GR TT A_int projector/window is the same Riesz/retained finite-character window as the exact Z64 branch",
                "BRST/diffeomorphism quotient commutes with the helicity-2 carrier functor",
                "order-32 helicity periodicity is accepted as the physical spin-2 subfiber of the order-64 exact carrier",
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
