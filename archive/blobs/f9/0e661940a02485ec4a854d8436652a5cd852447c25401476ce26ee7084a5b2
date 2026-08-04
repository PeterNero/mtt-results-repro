from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MTT = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")

UNIQUENESS = ROOT / "certificates" / "gr_tt_helicity2_z64_uniqueness_theorem_certificate.json"
GR_SOURCE = MTT / "11 General Relativity & Geometry" / "Modal_Triplet_Theory__From_MTT_to_General_Relativity_v2.md"
QG_SOURCE = MTT / "12 Quantum Gravity" / "Modal_Triplet_Theory__From_MTT_to_a_UV_Finite__Unitary_Quantum_Gravity_v4.md"
CENTRAL = (
    MTT
    / "13 Standard Model & Topology-Only Constraints"
    / "The_Central_Circle__Inertia__Mass__Gravity__and_Time_as_Shared_Coherence_Bookkeeping_in_Modal_Triplet_Theory.md"
)
FLAVOR_QG = Q79 / "proof_corpus" / "Flavor_QG_Projector_Compatibility_Lemma_for_Z64_CKM_Closure_v1.md"
TWISTED_Z64 = Q79 / "proof_corpus" / "Twisted_Equivariant_Central_Circle_Z64_CP_Sector_Candidate_v1.md"
WILSON_Z64 = Q79 / "proof_corpus" / "Finite_Wilson_Deck_Carrier_Extraction_Criterion_for_Z64_v1.md"

OUT_CERT = ROOT / "certificates" / "central_character_window_premise_source_and_proof_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "Central_Character_Window_Premise_Source_and_Proof_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def has(text: str, *needles: str) -> bool:
    return all(needle in text for needle in needles)


def main() -> None:
    uniqueness = load(UNIQUENESS)
    gr = read(GR_SOURCE)
    qg = read(QG_SOURCE)
    central = read(CENTRAL)
    flavor_qg = read(FLAVOR_QG)
    twisted = read(TWISTED_Z64)
    wilson = read(WILSON_Z64)

    source_tests = {
        "gr_observables_are_internal_pushforward_of_coherent_sector": has(
            gr,
            "joint harmonic projector",
            "observable projection",
            "I\\circ \\Pi",
        )
        or has(gr, "internal pushforward", "coherent sector", "Einstein--Hilbert"),
        "gr_metric_shape_map_or_projected_metric_present": has(
            gr,
            "projected metric",
            "Einstein field equations",
        )
        or has(qg, "Metric shape map", "B="),
        "qg_TT_Aint_projector_window_present": has(
            qg,
            "Lichnerowicz operator on TT modes",
            "A_{\\mathrm{int}}",
            "Pi_{\\mathrm{coh}}",
        ),
        "central_circle_unique_shared_gravity_channel": has(
            central,
            "Gravity, by contrast, operates on the shared circle itself",
            "central circle",
        )
        and has(central, "unique shared coherence bookkeeping channel", "gravity"),
        "finite_Z64_carrier_retained_by_Pi_coh_condition_sourced": has(
            twisted,
            "H_coh,64 = H_0 tensor K_64 tensor C|tau_64>",
            "P_CP,64 <= Pi_coh",
        )
        or has(flavor_qg, "Ran(P_fl) subset Ran(Pi_coh)", "finite Wilson/deck internal sector"),
        "finite_Wilson_deck_carrier_extraction_criterion_sourced": has(
            wilson,
            "exact finite Wilson/deck carrier",
            "K_64 ~= C[Z_64]",
            "primitive-lag support",
        ),
        "source_explicitly_says_GR_TT_shape_map_lands_in_H0_tensor_K64_tensor_dstar": False,
        "source_explicitly_says_GR_TT_projector_window_is_central_character_subfiber": False,
        "source_explicitly_says_same_angle_for_TT_and_Z64_central_circle": False,
    }

    proof_routes = {
        "direct_source_route": {
            "status": "OPEN",
            "missing": "explicit source sentence equating GR TT projector/window with central-character subfiber",
        },
        "metric_shape_map_route": {
            "status": "PRECISE_NEXT_PROOF",
            "sufficient_statement": (
                "The TT component of the metric shape map B_TT has internal image inside "
                "H_0 tensor K_64 tensor C|d_*> and transforms with central-circle weight 2."
            ),
            "then": (
                "By the uniqueness theorem, the image is |d_*> tensor span{c_2,s_2}; "
                "therefore lambda_GR,TT=15."
            ),
            "current_source_has_B_but_not_its_internal_image": True,
        },
        "coherence_universality_route": {
            "status": "CONDITIONAL_NOT_ENOUGH_ALONE",
            "why": (
                "The central circle is sourced as the gravity bookkeeping channel, but that "
                "does not by itself prove that the TT SPT window is a finite character subfiber."
            ),
        },
        "minimal_new_lemma_route": {
            "status": "READY",
            "lemma": "Central_Character_Window_Premise_for_GR_TT",
            "minimal_statement": (
                "The selected GR TT SPT internal projector/window is a central-circle "
                "character subfiber over the exact d_* branch, using the same central-circle "
                "angle as the spin-2 TT response."
            ),
            "consequence": "Full exact-branch internal GR TT gap closes with lambda_GR,TT=15.",
        },
    }

    decision = {
        "can_close_unconditionally_from_current_sources": False,
        "can_close_as_conditional_exact_branch_theorem": True,
        "representation_numeric_part_closed": uniqueness["theorem"]["closed"],
        "remaining_missing_data_type": "metric-shape-map image theorem, not a number",
        "best_next_computation": "compute or source B_TT internal image and central-circle weight",
        "current_status": "CENTRAL_CHARACTER_WINDOW_REDUCED_TO_METRIC_SHAPE_MAP_IMAGE",
    }

    note = """# Central Character Window Premise Source and Proof v1

## Result

The premise is not explicitly present in the current corpus, but the way to
prove it is now sharp.

Current sources give:

```text
1. GR observables are coherent-sector internal pushforwards.
2. QG uses a TT SPT projector/window with internal A_int.
3. Gravity operates on the shared central circle.
4. Z64 has a coherent finite Wilson/deck carrier retained by Pi_coh when selected.
5. The unique spin-2 Z64 character window is k=2/k=62.
```

What is not sourced:

```text
B_TT image lies in H_0 tensor K_64 tensor C|d_*>
and has central-circle weight 2.
```

## Proof Route

It is enough to prove the metric-shape-map image theorem:

```text
B_TT : TT_plus/cross -> H_0 tensor K_64 tensor C|d_*>
```

with spin-2 central-circle weight.

Then the uniqueness theorem forces:

```text
B_TT(TT_plus/cross) = |d_*> tensor span{c_2,s_2}
```

and the already verified compression gives:

```text
lambda_GR,TT = 15.
```

## Boundary

This is not a missing scalar and not a fitting problem. It is a single
operator-image theorem about the TT metric shape map.
"""
    OUT_NOTE.write_text(note, encoding="utf-8")

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "central_character_window_premise_source_and_proof",
        "status": "CENTRAL_CHARACTER_WINDOW_REDUCED_TO_METRIC_SHAPE_MAP_IMAGE",
        "input_certificates": {
            "gr_tt_helicity2_z64_uniqueness_theorem": str(UNIQUENESS),
        },
        "source_files": {
            "gr": str(GR_SOURCE),
            "qg": str(QG_SOURCE),
            "central_circle": str(CENTRAL),
            "flavor_qg_projector_compatibility": str(FLAVOR_QG),
            "twisted_z64_carrier": str(TWISTED_Z64),
            "finite_wilson_deck_carrier": str(WILSON_Z64),
        },
        "source_tests": source_tests,
        "proof_routes": proof_routes,
        "decision": decision,
        "guardrails": {
            "claims_unconditional_source_premise_closed": False,
            "claims_full_GR_TT_gap_15_unconditionally": False,
            "claims_metric_shape_map_image_computed": False,
            "claims_physical_dimensionful_gap": False,
            "claims_Newton_or_Planck_prediction": False,
        },
        "next_gate": {
            "name": "Selected_TT_Metric_Shape_Map_Central_Character_Image",
            "must_prove": [
                "B_TT image is contained in the retained exact central-circle branch H0 tensor K64 tensor C|d_*>",
                "B_TT carries central-circle weight 2 on TT plus/cross",
                "BRST/diffeomorphism quotient does not alter this internal image",
            ],
            "then_forced": [
                "selected GR TT projector/window is |d_*> tensor span{c_2,s_2}",
                "lambda_GR,TT = 15 in canonical exact-branch internal units",
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
