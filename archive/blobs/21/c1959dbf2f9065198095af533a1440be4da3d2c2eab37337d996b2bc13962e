from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MTT = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")
TEXPAPERS = Path(r"C:\Users\nero_\Downloads\TEXPAPERS")

QG = MTT / "12 Quantum Gravity" / "Modal_Triplet_Theory__From_MTT_to_a_UV_Finite__Unitary_Quantum_Gravity_v4.md"
FCP = MTT / "5 Dirac Delta" / "Finite_Coherent_Projection_in_Modal_Triplet_Theory_v2.md"
Z64 = TEXPAPERS / "18 Theta-Closure & Execution Program" / "_md_v3_corrected" / "Z64_Exact_Central_Circle_Branch_Certificate_v1.md"
PARTIAL = ROOT / "certificates" / "btt_packet_partial_fill_weight_brs_certificate.json"

OUT_CERT = ROOT / "certificates" / "btt_adjoint_shape_map_typing_theorem_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "BTT_Adjoint_Shape_Map_Typing_Theorem_v1.md"
OUT_PACKET = ROOT / "candidate_data" / "selected_tt_adjoint_shape_support.template.json"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def has(text: str, *needles: str) -> bool:
    return all(needle in text for needle in needles)


def main() -> None:
    qg = read(QG)
    fcp = read(FCP)
    z64 = read(Z64)
    partial = load(PARTIAL)

    source_tests = {
        "shape_map_B_is_DG_Pi_coh": has(qg, "B \\;=\\; DG(\\Psi_\\ast)\\Pi_{\\mathrm{coh}}")
        or has(qg, "B= \\left.\\frac{\\delta g}{\\delta \\Psi}\\right|"),
        "propagator_is_B_Ainv_Bstar": has(qg, "propagator $\\Delta_{\\mathrm{prop}}=BA^{-1}B^*$")
        or has(qg, "propagator $\\Delta_{\\mathrm{prop}}=BA^{-1}B^{\\!*}$"),
        "kernel_inverse_on_TT": has(qg, "Quadratic kernel on TT", "K=(BA^{-1}B^*)^{-1}"),
        "physical_TT_two_point_function": has(
            qg,
            "physical TT two-point function",
            "projected, gauge-invariant graviton correlator",
        ),
        "pure_gauge_removed": has(qg, "pure-gauge directions are removed by the BV gauge-fixing"),
        "finite_projection_TT_spin2_source": has(
            fcp,
            "weak-field gravitational filtering acts on physical spin-2 data",
        ),
        "exact_z64_branch_retained_by_Pi_coh": has(z64, "P_CP,64 <= Pi_coh", "[L,Pi_coh]=0"),
        "exact_z64_branch_selected_tower": has(z64, "d_*=(2,2,2,2,2)", "C(d_*)=15"),
    }

    corrected_object = {
        "wrongly_typed_gate": "B_TT : span{TT_plus,TT_cross} -> H0 tensor K64 tensor C|d_*>",
        "reason_wrongly_typed": (
            "The source-defined shape map B=DG(Psi*)Pi_coh maps coherent/internal "
            "configurations to metric fluctuations. A map from TT polarizations back "
            "to internal support is the Hilbert adjoint/pullback B^*, not B."
        ),
        "correct_gate": "J_TT := Pi_exact64 B^* P_TT, with B=DG(Psi*)Pi_coh",
        "domain": "physical TT plus/cross test space or quotient",
        "codomain": "retained coherent internal support H0 tensor K64 tensor C|d_*>",
    }

    closed_now = {
        "B_TT_weight2": partial["closed_properties"]["B_TT_central_circle_weight"] == 2,
        "B_TT_BRST_compatible": partial["closed_properties"]["B_TT_BRST_quotient_compatible"] is True,
        "TT_coupling_nonzero_for_adjoint_support": (
            source_tests["propagator_is_B_Ainv_Bstar"]
            and source_tests["kernel_inverse_on_TT"]
            and source_tests["physical_TT_two_point_function"]
        ),
        "exact_Z64_branch_available_and_coherent": (
            source_tests["exact_z64_branch_retained_by_Pi_coh"]
            and source_tests["exact_z64_branch_selected_tower"]
        ),
    }

    still_open = {
        "Pi_exact64_Bstar_PTT_equals_Bstar_PTT": None,
        "same_sampled_central_circle_angle_for_J_TT_and_Z64_shift": None,
        "J_TT_support_exactly_dstar_k2_plane": None,
    }

    packet = {
        "schema": "SelectedTTAdjointShapeSupport.v1",
        "purpose": "Correctly typed replacement for the B_TT image gate.",
        "operator": "J_TT := Pi_exact64 B^* P_TT",
        "source_shape_map": "B := DG(Psi*) Pi_coh",
        "known_closed": closed_now,
        "required_to_close_lambda_GR_TT_15": still_open,
        "if_required_fields_close_then": {
            "support": "|d_*> tensor span{c_2,s_2}",
            "lambda_GR_TT_internal": 15.0,
        },
        "guardrail": "Do not state B maps TT into the internal branch; use B^* or adjoint support.",
    }
    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "btt_adjoint_shape_map_typing_theorem",
        "status": "BTT_IMAGE_GATE_CORRECTED_TO_ADJOINT_SUPPORT_NONZERO_CLOSED_SUPPORT_OPEN",
        "source_files": {
            "qg": str(QG),
            "finite_coherent_projection": str(FCP),
            "z64_exact_branch": str(Z64),
        },
        "source_tests": source_tests,
        "corrected_object": corrected_object,
        "closed_now": closed_now,
        "still_open": still_open,
        "replacement_packet_written": str(OUT_PACKET),
        "conclusion": {
            "old_BTT_image_gate_valid_as_written": False,
            "correct_gate_is_adjoint_support": True,
            "TT_adjoint_coupling_nonzero": closed_now["TT_coupling_nonzero_for_adjoint_support"],
            "unconditional_lambda_GR_TT_15": False,
            "why_not_final": (
                "The corpus sources exact Z64 coherent retention and nonzero TT adjoint coupling, "
                "but does not yet prove that the TT adjoint support is exhausted by Pi_exact64 "
                "or that the sampled angle is the exact Z64 shift angle."
            ),
        },
        "guardrails": {
            "claims_B_maps_TT_to_internal_branch": False,
            "claims_adjoint_support_exactly_dstar_k2": False,
            "claims_unconditional_lambda_GR_TT_15": False,
            "uses_observed_GR_data": False,
        },
        "note_written": str(OUT_NOTE),
    }

    note = """# BTT Adjoint Shape Map Typing Theorem v1

## Correction

The source-defined metric shape map is

```text
B = DG(Psi*) Pi_coh.
```

This maps coherent/internal configurations to metric fluctuations. Therefore the
previous image gate

```text
B_TT : span{TT_plus,TT_cross} -> H0 tensor K64 tensor C|d_*>
```

is not the correctly typed object unless `B_TT` is explicitly interpreted as a
pullback. The correct operator is the adjoint/co-shape support map:

```text
J_TT := Pi_exact64 B^* P_TT.
```

## Closed Now

The TT coupling is nonzero at the adjoint-support level. The QG source defines
the physical graviton propagator as

```text
Delta_prop = B A^{-1} B^*
```

and the TT quadratic kernel as its inverse. On the physical TT quotient, this
requires nontrivial `B^* P_TT` support. Together with the previous packet, the
spin-2 weight and BRST/diffeomorphism compatibility are closed.

The exact `Z64` branch is also available and coherent:

```text
P_CP,64 <= Pi_coh,
[L,Pi_coh]=0,
d_*=(2,2,2,2,2),
C(d_*)=15.
```

## Still Open

The final support identity is not sourced:

```text
Pi_exact64 B^* P_TT = B^* P_TT,
```

nor is the same sampled central-circle angle between `J_TT` and the exact `Z64`
shift sourced. If those two fields close, the already proved uniqueness theorem
forces

```text
support(J_TT)=|d_*> tensor span{c_2,s_2}
lambda_GR,TT=15
```

in normalized internal exact-branch units.
"""
    OUT_NOTE.write_text(note, encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
