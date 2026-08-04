from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MTT = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")

NO_GO = ROOT / "certificates" / "btt_exact_support_independence_no_go_certificate.json"
ADJOINT = ROOT / "certificates" / "btt_adjoint_shape_map_typing_theorem_certificate.json"
UNIQUENESS = ROOT / "certificates" / "gr_tt_helicity2_z64_uniqueness_theorem_certificate.json"
ATTEMPT = ROOT / "certificates" / "central_circle_tt_adjoint_support_proof_attempt_certificate.json"

CENTRAL = (
    MTT
    / "13 Standard Model & Topology-Only Constraints"
    / "The_Central_Circle__Inertia__Mass__Gravity__and_Time_as_Shared_Coherence_Bookkeeping_in_Modal_Triplet_Theory.md"
)
QG = MTT / "12 Quantum Gravity" / "Modal_Triplet_Theory__From_MTT_to_a_UV_Finite__Unitary_Quantum_Gravity_v4.md"
FINITE = MTT / "5 Dirac Delta" / "Finite_Coherent_Projection_in_Modal_Triplet_Theory_v2.md"
KK = (
    MTT
    / "15 Discrete & Spectral & Operator Geometric Theories"
    / "Modal_Triplet_Theory__From_MTT_to_Kaluza__Klein_Theory.md"
)
STRING = MTT / "19 A project-first reframing" / "A_Projection_First_Reframing_of_String_Theory (1).md"
B1 = MTT / "1 Core & Encodings" / "The_Modal_Triplet_Theory_Program_B1__Gravity_as_Kinematic_Consistency_Encoding.md"
GR = MTT / "11 General Relativity & Geometry" / "Modal_Triplet_Theory__From_MTT_to_General_Relativity_v2.md"

OUT_CERT = ROOT / "certificates" / "external_clues_btt_support_closure_routes_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "External_Clues_BTT_Support_Closure_Routes_v1.md"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def has(text: str, *needles: str) -> bool:
    return all(needle in text for needle in needles)


def main() -> None:
    no_go = load(NO_GO)
    adjoint = load(ADJOINT)
    uniqueness = load(UNIQUENESS)
    attempt = load(ATTEMPT)

    central = read(CENTRAL)
    qg = read(QG)
    finite = read(FINITE)
    kk = read(KK)
    string = read(STRING)
    b1 = read(B1)
    gr = read(GR)

    internal_clues = {
        "correct_adjoint_support_nonzero": adjoint["closed_now"]["TT_coupling_nonzero_for_adjoint_support"] is True,
        "exact_support_independence_no_go": (
            no_go["logical_result"]["current_assumptions_force_exact_dstar_support"] is False
        ),
        "z64_weight2_uniqueness_ready": uniqueness["theorem"]["closed"] is True,
        "previous_attempt_reduces_to_selection_premise": (
            attempt["decision"]["proved_conditionally"] is True
            and attempt["decision"]["proved_unconditionally"] is False
        ),
        "central_unique_shared_channel": has(
            central,
            "unique shared coherence channel",
            "Gravity, by contrast, operates on the shared coherence channel",
        )
        or has(central, "unique shared coherence channel", "Gravity, by contrast, operates on the shared circle itself"),
        "qg_spin2_tt_projected_operator": has(
            qg,
            "projected linearized graviton operator on the TT sector",
            "spin-2 propagator reduces to the GR one",
        ),
        "finite_zero_mode_gravity_shadow": has(
            finite,
            "observed gravitational sector",
            "diffeomorphism-compatible zero-mode",
        )
        or has(finite, "zero-mode gravity is undamped"),
        "kk_projection_zero_mode_equivalence": has(
            kk,
            "Projection--compactification equivalence",
            "zero-modes",
            "4D action",
        ),
        "string_massless_spin2_universal_coupling": has(
            string,
            "massless spin-two excitation",
            "required coupling to",
            "energy",
        ),
        "b1_universal_geometry_coupling": has(
            b1,
            "universal coupling property of gravity",
            "couple universally",
        ),
        "gr_longs_wavelength_projection_completeness": has(
            gr,
            "Coherent-sector completeness",
            "content is exhausted by",
        ),
    }

    external_clues = {
        "weinberg_soft_graviton": {
            "source": "Steven Weinberg, Phys. Rev. 135 (1964) B1049, DOI 10.1103/PhysRev.135.B1049",
            "url": "https://journals.aps.org/pr/abstract/10.1103/PhysRev.135.B1049",
            "imported_constraint": (
                "A massless spin-2 soft theorem forces universal gravitational coupling "
                "under the usual S-matrix assumptions."
            ),
            "closure_power_for_mtt": "supports universality of TT response; does not select Pi_exact64",
        },
        "deser_self_interaction": {
            "source": "S. Deser, General Relativity and Gravitation 1 (1970) 9-18; arXiv:gr-qc/0411023",
            "url": "https://arxiv.org/abs/gr-qc/0411023",
            "imported_constraint": (
                "Consistent self-interaction of a massless spin-2 gauge field reconstructs "
                "the Einstein-type nonlinear coupling."
            ),
            "closure_power_for_mtt": "supports GR recovery from TT spin-2 consistency; does not select finite support",
        },
        "kk_zero_mode_logic": {
            "source": "Duff, Nilsson, Pope, Phys. Rept. 130 (1986) 1-142; KK compactification literature",
            "url": "https://doi.org/10.1016/0370-1573(86)90163-8",
            "imported_constraint": (
                "Low-energy four-dimensional gravitons arise from universal internal zero-mode "
                "data in compactification reductions."
            ),
            "closure_power_for_mtt": (
                "suggests B^*P_TT should be a universal coherent shadow; needs MTT finite sampling theorem"
            ),
        },
    }

    routes = {
        "R1_universal_spin2_bookkeeping_selector": {
            "idea": (
                "Use massless spin-2 consistency plus MTT universal geometry coupling to show "
                "physical TT adjoint support must lie in the unique shared bookkeeping channel."
            ),
            "internal_support": internal_clues["b1_universal_geometry_coupling"]
            and internal_clues["central_unique_shared_channel"]
            and internal_clues["qg_spin2_tt_projected_operator"],
            "external_support": ["weinberg_soft_graviton", "deser_self_interaction"],
            "what_it_closes": [
                "universal TT coupling is not a tunable choice",
                "gravity response cannot be assigned to a sector-specific gauge channel",
            ],
            "remaining_gate": (
                "prove that the unique shared bookkeeping channel, when restricted to the selected exact "
                "finite carrier, is exactly Pi_exact64 and not a different coherent subchannel"
            ),
            "closes_exact_support_now": False,
        },
        "R2_equivariant_central_character_selector": {
            "idea": (
                "Treat B^*P_TT as an equivariant co-shape map for the same central U(1) angle "
                "that rotates TT plus/cross. Finite sampling on the selected exact Z64 carrier then "
                "forces the k=2/k=62 real character plane by the existing uniqueness theorem."
            ),
            "internal_support": internal_clues["correct_adjoint_support_nonzero"]
            and internal_clues["z64_weight2_uniqueness_ready"],
            "external_support": ["weinberg_soft_graviton"],
            "what_it_closes": [
                "replaces the vague support premise by a precise equivariance premise",
                "uses the already closed Z64 uniqueness theorem without adding a scalar knob",
            ],
            "remaining_gate": (
                "source or prove same-angle equivariance: B^*P_TT must intertwine TT helicity rotations "
                "with the central-circle action used by the exact Z64 shift"
            ),
            "closes_exact_support_now": False,
        },
        "R3_zero_mode_shadow_plus_finite_helicity": {
            "idea": (
                "Use KK/MTT zero-mode logic for the external graviton and keep helicity as a separate "
                "central-circle character. External zero-mode status removes KK momentum; finite helicity "
                "sampling selects k=2 on Z64."
            ),
            "internal_support": internal_clues["finite_zero_mode_gravity_shadow"]
            and internal_clues["kk_projection_zero_mode_equivalence"],
            "external_support": ["kk_zero_mode_logic"],
            "what_it_closes": [
                "prevents confusion between external/KK zero-mode and central-circle helicity k=2",
                "explains why k=2 support need not contradict low-energy zero-mode recovery",
            ],
            "remaining_gate": (
                "prove the selected zero-mode shadow is carried by the exact central-circle fiber "
                "rather than merely by an abstract coherent subspace"
            ),
            "closes_exact_support_now": False,
        },
        "R4_string_closed_bookkeeping_analogy": {
            "idea": (
                "Use the closed-string massless spin-2/global-bookkeeping analogy as a selection heuristic: "
                "gravity is the global consistency mode, not a localized gauge-sector excitation."
            ),
            "internal_support": internal_clues["string_massless_spin2_universal_coupling"],
            "external_support": ["deser_self_interaction"],
            "what_it_closes": [
                "motivates why the final support should be a global shared carrier",
                "helps reject sector-local lens/nil-only closures as proof sources for TT support",
            ],
            "remaining_gate": "analogy is not a theorem; still needs R2 or direct DG(Psi*) computation",
            "closes_exact_support_now": False,
        },
        "R5_direct_matrix_reconstruction": {
            "idea": (
                "Build the finite co-shape matrix from constraints: nonzero TT adjoint support, BRST quotient, "
                "central equivariance, exact d_* branch, and orthonormal TT basis. Then verify "
                "Pi_exact64 B^*P_TT = B^*P_TT by matrix multiplication."
            ),
            "internal_support": internal_clues["correct_adjoint_support_nonzero"]
            and internal_clues["previous_attempt_reduces_to_selection_premise"],
            "external_support": [],
            "what_it_closes": [
                "turns the proof into a reproducible finite certificate",
                "would close the last gate if the equivariant input matrix is sourced rather than fitted",
            ],
            "remaining_gate": "the selected entries of DG(Psi*) or its equivariant normalization are not in the corpus",
            "closes_exact_support_now": False,
        },
    }

    best_route = {
        "name": "R2_equivariant_central_character_selector",
        "why": (
            "It is the narrowest real proof obligation: no new numerical parameter, no appeal to observed "
            "gravity data, and it exactly targets the independence no-go by adding the missing structural "
            "fact instead of a scalar fit."
        ),
        "new_theorem_to_write": "EquivariantCentralCircleTTSupportTheorem.v1",
        "statement": (
            "On the selected exact GR/QG branch, the adjoint TT co-shape map B^*P_TT is equivariant for the "
            "central-circle U(1) action that rotates TT plus/cross with helicity weight 2, and the selected "
            "finite carrier of that action is the exact Z64 d_* branch."
        ),
        "immediate_consequence": (
            "Pi_exact64 B^*P_TT = B^*P_TT and support(J_TT)=|d_*> tensor span{c_2,s_2}; hence "
            "lambda_GR,TT=15 in normalized internal units."
        ),
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "external_clues_btt_support_closure_routes",
        "status": "EXTERNAL_CLUES_REDUCE_GATE_TO_EQUIVARIANT_CENTRAL_SELECTOR",
        "input_certificates": {
            "btt_exact_support_independence_no_go": str(NO_GO),
            "btt_adjoint_shape_map_typing": str(ADJOINT),
            "gr_tt_helicity2_z64_uniqueness": str(UNIQUENESS),
            "central_circle_tt_adjoint_support_proof_attempt": str(ATTEMPT),
        },
        "source_files": {
            "central_circle": str(CENTRAL),
            "qg": str(QG),
            "finite_projection": str(FINITE),
            "kk": str(KK),
            "string_reframing": str(STRING),
            "b1_gravity_kinematic_consistency": str(B1),
            "gr": str(GR),
        },
        "internal_clues": internal_clues,
        "external_clues": external_clues,
        "routes": routes,
        "best_route": best_route,
        "decision": {
            "exact_support_proved_now": False,
            "support_premise_replaced_by_sharper_theorem": True,
            "new_minimal_gate": best_route["new_theorem_to_write"],
            "why_not_closed": (
                "The external literature closes universality and spin-2 consistency, while the MTT corpus "
                "closes helicity-2 Z64 uniqueness. The still missing statement is the equivariance/same-angle "
                "identification of the actual adjoint shape map B^*P_TT with the selected exact central action."
            ),
        },
        "guardrails": {
            "uses_external_sources_as_inspiration_only": True,
            "claims_weinberg_or_deser_selects_Z64": False,
            "claims_KK_zero_mode_equals_k2_character": False,
            "uses_observed_GR_data": False,
            "adds_new_numeric_knob": False,
        },
        "note_written": str(OUT_NOTE),
    }

    note = """# External Clues for BTT Support Closure Routes v1

## Result

External physics does not close the final support identity by itself, but it
does sharpen the target. The best remaining theorem is not a new number. It is
an equivariance theorem for the actual adjoint TT co-shape map:

```text
B^*P_TT must intertwine TT helicity rotations with the same central-circle
U(1) action whose selected finite carrier is the exact Z64 d_* branch.
```

If that is proved, the already closed Z64 uniqueness theorem forces:

```text
Pi_exact64 B^*P_TT = B^*P_TT,
support(J_TT)=|d_*> tensor span{c_2,s_2},
lambda_GR,TT=15.
```

## External Clues Imported

1. Weinberg soft-graviton logic supports universal spin-2 coupling under the
   usual S-matrix assumptions. It helps show that a physical massless spin-2
   response is not sector-local or freely adjustable.

2. Deser-style self-interaction/gauge-invariance logic supports the recovery of
   Einstein-type nonlinear coupling from consistent massless spin-2 dynamics.

3. Kaluza-Klein zero-mode logic explains why the low-energy graviton is a
   universal coherent mode rather than a massive internal excitation.

None of these standard arguments selects `Z64` or `Pi_exact64`. They are
therefore used as constraints and clues, not as proof of the finite MTT branch.

## Route Audit

### R1 Universal Spin-2 Bookkeeping Selector

This route combines massless spin-2 universality with the MTT central-circle
claim that gravity operates on the unique shared coherence channel.

It supports the physical direction strongly, but it still does not identify the
finite support projector.

### R2 Equivariant Central-Character Selector

This is the best route. It asks for a precise theorem:

```text
B^*P_TT is equivariant for the same central-circle angle that rotates TT
plus/cross with helicity weight 2.
```

Then finite sampling on the selected exact `Z64` branch leaves only the
`k=2/k=62` real character plane. This route directly targets the no-go, because
the no-go allowed nonzero TT support outside `Pi_exact64` only by leaving the
central equivariance/same-angle fact unspecified.

### R3 Zero-Mode Shadow plus Finite Helicity

This route separates two notions that can otherwise get tangled:

- external/KK zero-mode means no low-energy massive internal excitation;
- central-circle `k=2` means spin-2 helicity under the shared angular action.

So `k=2` does not contradict zero-mode gravity. But zero-mode recovery alone
still does not prove the exact finite carrier.

### R4 Closed-String Global Bookkeeping Analogy

This route is useful as intuition: closed-string massless spin-2 behavior points
to gravity as a global consistency/bookkeeping mode. But analogy cannot close
the theorem.

### R5 Direct Matrix Reconstruction

This is the brute-force route: construct the finite matrix for `B^*P_TT`, then
multiply by `Pi_exact64`. It would be decisive, but the selected entries of
`DG(Psi*)` are not yet sourced.

## Next Theorem

Write and prove:

```text
EquivariantCentralCircleTTSupportTheorem.v1
```

Statement:

```text
On the selected exact GR/QG branch, the adjoint TT co-shape map B^*P_TT is
equivariant for the central-circle U(1) action that rotates TT plus/cross with
helicity weight 2, and the selected finite carrier of that action is the exact
Z64 d_* branch.
```

This is the cleanest closure path because it adds no fitted scalar, uses no
observed Newton/Planck input, and converts the previous missing support premise
into a checkable representation-theoretic statement.
"""

    OUT_NOTE.write_text(note, encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
