from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MTT = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")

WINDOW_SOURCE = ROOT / "certificates" / "central_character_window_premise_source_and_proof_certificate.json"
UNIQUENESS = ROOT / "certificates" / "gr_tt_helicity2_z64_uniqueness_theorem_certificate.json"
FUNCTOR = ROOT / "certificates" / "tt_helicity2_z64_carrier_functor_certificate.json"

QG_SOURCE = MTT / "12 Quantum Gravity" / "Modal_Triplet_Theory__From_MTT_to_a_UV_Finite__Unitary_Quantum_Gravity_v4.md"
GR_SOURCE = MTT / "11 General Relativity & Geometry" / "Modal_Triplet_Theory__From_MTT_to_General_Relativity_v2.md"
CENTRAL = (
    MTT
    / "13 Standard Model & Topology-Only Constraints"
    / "The_Central_Circle__Inertia__Mass__Gravity__and_Time_as_Shared_Coherence_Bookkeeping_in_Modal_Triplet_Theory.md"
)

OUT_CERT = ROOT / "certificates" / "selected_tt_metric_shape_map_image_theorem_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "Selected_TT_Metric_Shape_Map_Image_Theorem_v1.md"
OUT_TEMPLATE = ROOT / "candidate_data" / "selected_tt_metric_shape_map_image.template.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def has(text: str, *needles: str) -> bool:
    return all(needle in text for needle in needles)


def main() -> None:
    window = load(WINDOW_SOURCE)
    uniqueness = load(UNIQUENESS)
    functor = load(FUNCTOR)
    qg = read(QG_SOURCE)
    gr = read(GR_SOURCE)
    central = read(CENTRAL)

    source_tests = {
        "qg_metric_shape_map_defined_as_DG_Pi": has(
            qg,
            "B \\;=\\; DG(\\Psi_\\ast)\\Pi_{\\mathrm{coh}}",
        )
        or has(qg, "metric shape map", "B= \\left.\\frac{\\delta g}{\\delta \\Psi}\\right|"),
        "qg_shape_map_factorized_with_Aint_window": has(
            qg,
            "B \\;=\\; e^{-\\frac{\\tau_0}{2}E}",
            "e^{-\\frac{\\tau_0}{2}A_{\\mathrm{int}}}",
        )
        or has(qg, "B \\;=\\; e^{-\\tfrac{\\tau_0}{2}E}", "e^{-\\tfrac{\\tau_0}{2}A_{\\mathrm{int}}}"),
        "gr_metric_is_observable_pushforward": has(
            gr,
            "observable projection",
            "I\\circ \\Pi",
        )
        or has(gr, "internal pushforward", "projected metric"),
        "central_circle_gravity_operates_on_shared_circle": has(
            central,
            "Gravity, by contrast, operates on the shared circle itself",
        ),
        "central_circle_unique_shared_gravity_channel": has(
            central,
            "unique shared coherence bookkeeping channel",
            "gravity",
        ),
        "uniqueness_for_spin2_z64_window_closed": uniqueness["theorem"]["closed"],
        "helicity2_functor_compresses_to_15": functor["verdict"]["algebraic_compression_to_15_I2_closed"],
        "source_computes_BTT_image_in_exact_branch": False,
        "source_proves_BTT_central_circle_equivariance_weight2": False,
    }

    exact_branch_shape_map_packet = {
        "schema": "SelectedTTMetricShapeMapImage.v1",
        "purpose": "Minimal data needed to promote the exact-branch TT gap to a full selected GR TT theorem.",
        "domain": "span_R{TT_plus, TT_cross}",
        "codomain": "H0 tensor K64 tensor C|d_*>",
        "required_properties": {
            "B_TT_nonzero": None,
            "B_TT_image_in_retained_exact_branch": None,
            "B_TT_central_circle_weight": 2,
            "B_TT_BRST_quotient_compatible": None,
            "same_central_circle_angle_as_Z64_carrier": None,
        },
        "if_valid_then_forced_image": "|d_*> tensor span{c_2,s_2}",
        "if_valid_then_lambda_GR_TT": 15.0,
        "note": "Fill booleans from a source or explicit computation; do not use observed gravity data.",
    }
    OUT_TEMPLATE.write_text(json.dumps(exact_branch_shape_map_packet, indent=2), encoding="utf-8")

    theorem = {
        "name": "Selected_TT_Metric_Shape_Map_Image_Theorem",
        "closed_unconditionally": False,
        "closed_conditionally_on_packet": True,
        "conditional_hypotheses": [
            "B_TT is nonzero on the TT plus/cross quotient",
            "B_TT image lies in the retained exact branch H0 tensor K64 tensor C|d_*>",
            "B_TT is central-circle equivariant of weight 2",
            "B_TT is compatible with the BRST/diffeomorphism quotient",
            "B_TT uses the same central-circle angular coordinate as the exact Z64 carrier",
        ],
        "conditional_conclusion": {
            "B_TT_image": "|d_*> tensor span{c_2,s_2}",
            "lambda_GR_TT": 15.0,
            "reason": "Uniqueness of the spin-2 real character plane in C[Z64] plus exact branch compression.",
        },
    }

    decision = {
        "current_status": "BTT_IMAGE_THEOREM_FORMULATED_CONDITIONAL_PACKET_READY",
        "why_not_fully_closed": (
            "The current corpus defines the metric shape map and the TT SPT window, but "
            "does not compute the internal image of B_TT or prove its central-circle weight."
        ),
        "what_was_closed_now": [
            "the exact data packet required to close the B_TT image theorem",
            "the conditional theorem from that packet to lambda_GR,TT=15",
            "a validator-ready template for source/computation fill-in",
        ],
        "next_computation": (
            "Extract B_TT from DG(Psi*) Pi_coh on the exact branch and verify the "
            "template booleans, especially image_in_retained_exact_branch and weight=2."
        ),
    }

    note = """# Selected TT Metric Shape Map Image Theorem v1

## Result

The final gate has been converted into a validator-ready operator theorem.

Current sources define:

```text
B = DG(Psi*) Pi_coh
```

as the metric shape map, and QG gives the TT SPT `A_int` window. But current
sources do not compute the internal image of the TT restriction `B_TT`.

## Conditional Closure

If the selected exact-branch shape-map packet verifies:

```text
B_TT : span{TT_plus, TT_cross} -> H0 tensor K64 tensor C|d_*>
B_TT has central-circle weight 2
B_TT is BRST/diffeomorphism quotient compatible
```

then the already proved uniqueness theorem forces:

```text
B_TT image = |d_*> tensor span{c_2,s_2}
```

and the exact branch compression gives:

```text
lambda_GR,TT = 15.
```

## What Remains

This artifact does not claim the packet is filled. It creates the precise
packet and theorem needed to close the last shape-map step by source extraction
or direct computation from `DG(Psi*) Pi_coh`.
"""
    OUT_NOTE.write_text(note, encoding="utf-8")

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "selected_tt_metric_shape_map_image_theorem",
        "status": decision["current_status"],
        "input_certificates": {
            "central_character_window_premise": str(WINDOW_SOURCE),
            "helicity2_z64_uniqueness": str(UNIQUENESS),
            "tt_helicity2_z64_carrier_functor": str(FUNCTOR),
        },
        "source_files": {
            "qg": str(QG_SOURCE),
            "gr": str(GR_SOURCE),
            "central_circle": str(CENTRAL),
        },
        "source_tests": source_tests,
        "candidate_packet_written": str(OUT_TEMPLATE),
        "theorem": theorem,
        "decision": decision,
        "guardrails": {
            "claims_BTT_image_computed": False,
            "claims_unconditional_lambda_GR_TT_15": False,
            "claims_physical_dimensionful_gap": False,
            "claims_Newton_or_Planck_prediction": False,
            "uses_observed_GR_data": False,
        },
        "note_written": str(OUT_NOTE),
    }

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"WROTE: {OUT_TEMPLATE}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
