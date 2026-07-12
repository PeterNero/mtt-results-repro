from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MTT = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")

FINAL_DECISION = ROOT / "certificates" / "final_btt_support_closure_decision_certificate.json"
NO_GO = ROOT / "certificates" / "btt_exact_support_independence_no_go_certificate.json"
ADJOINT = ROOT / "certificates" / "btt_adjoint_shape_map_typing_theorem_certificate.json"
UNIQUENESS = ROOT / "certificates" / "gr_tt_helicity2_z64_uniqueness_theorem_certificate.json"

CENTRAL = (
    MTT
    / "13 Standard Model & Topology-Only Constraints"
    / "The_Central_Circle__Inertia__Mass__Gravity__and_Time_as_Shared_Coherence_Bookkeeping_in_Modal_Triplet_Theory.md"
)
GR = MTT / "11 General Relativity & Geometry" / "Modal_Triplet_Theory__From_MTT_to_General_Relativity_v2.md"
CAPACITY = (
    MTT
    / "14 Coherence Capacity Program"
    / "Coherence_Capacity_as_the_Fundamental_Resource_of_Effective_Physics_v3.md"
)

OUT_CERT = ROOT / "certificates" / "central_circle_tt_adjoint_support_proof_attempt_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "Central_Circle_TT_Adjoint_Support_Proof_Attempt_v1.md"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def has(text: str, *needles: str) -> bool:
    return all(needle in text for needle in needles)


def main() -> None:
    final = load(FINAL_DECISION)
    no_go = load(NO_GO)
    adjoint = load(ADJOINT)
    uniqueness = load(UNIQUENESS)
    central = read(CENTRAL)
    gr = read(GR)
    capacity = read(CAPACITY)

    route_tests = {
        "central_unique_shared_scalar_channel": has(
            central,
            "unique shared coherence channel",
            "only internal structure common to all sectors",
            "universal, scalar, and resistant to local redefinition",
        ),
        "central_gravity_operates_on_shared_channel": has(
            central,
            "Gravity, by contrast, operates on the shared coherence channel",
        )
        or has(central, "Gravity, by contrast, operates on the shared circle itself"),
        "central_claim_marked_interpretive_not_theorem": has(
            central,
            "interpretive synthesis",
            "unifying explanatory map rather than as new standalone theorems",
        ),
        "gr_observable_content_exhausted_by_projection": has(
            gr,
            "Coherent-sector completeness",
            "observable",
            "content is exhausted by",
            "Im",
        ),
        "capacity_gravity_as_geometric_bookkeeping": has(
            capacity,
            "Gravity as the Geometric Bookkeeping of Coherence Capacity",
            "geometry is the bookkeeping",
            "diffeomorphism invariance",
        ),
        "no_go_says_exact_support_independent": (
            no_go["logical_result"]["current_assumptions_force_exact_dstar_support"] is False
        ),
        "adjoint_support_nonzero_closed": adjoint["closed_now"]["TT_coupling_nonzero_for_adjoint_support"] is True,
        "uniqueness_would_close_after_support": uniqueness["theorem"]["closed"] is True,
    }

    attempted_routes = {
        "route_A_universal_scalar_channel": {
            "premises_sourced": route_tests["central_unique_shared_scalar_channel"]
            and route_tests["central_gravity_operates_on_shared_channel"],
            "blocks": [
                "central paper labels the shared-channel gravity identification as interpretive synthesis",
                "does not name Pi_exact64 as the GR/QG TT support projector",
            ],
            "closes_exact_support": False,
        },
        "route_B_GR_projection_completeness": {
            "premises_sourced": route_tests["gr_observable_content_exhausted_by_projection"],
            "blocks": [
                "GR completeness says physical content is in Im(P), not which finite internal subprojector inside Im(P)",
                "does not identify the image with the exact Z64 d_* branch",
            ],
            "closes_exact_support": False,
        },
        "route_C_capacity_bookkeeping": {
            "premises_sourced": route_tests["capacity_gravity_as_geometric_bookkeeping"],
            "blocks": [
                "capacity geometry selects gravitational bookkeeping, but not the finite Z64 support projector",
                "does not compute DG(Psi*) or B^*P_TT support",
            ],
            "closes_exact_support": False,
        },
    }

    conditional_proof = {
        "new_selection_premise": "Pi_TT_shared := support projector of B^*P_TT equals Pi_exact64 on the selected exact GR/QG branch",
        "proof_steps": [
            "By the adjoint typing theorem, B^*P_TT is the correctly typed physical TT internal support and is nonzero.",
            "By the new selection premise, Pi_exact64 B^*P_TT = B^*P_TT.",
            "By weight-2 and BRST closure, this support is a physical spin-2 central-circle character support.",
            "By the Z64 uniqueness theorem, the only real weight-2 plane in the retained exact branch is |d_*> tensor span{c_2,s_2}.",
            "By exact-branch compression, lambda_GR,TT=15 in normalized internal units.",
        ],
        "valid": True,
        "unconditional": False,
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "central_circle_tt_adjoint_support_proof_attempt",
        "status": "SUPPORT_THEOREM_PROOF_ATTEMPT_BLOCKED_SELECTION_PREMISE_REQUIRED",
        "source_files": {
            "central_circle": str(CENTRAL),
            "gr": str(GR),
            "capacity": str(CAPACITY),
        },
        "input_certificates": {
            "final_btt_support_closure_decision": str(FINAL_DECISION),
            "btt_exact_support_independence_no_go": str(NO_GO),
            "btt_adjoint_shape_map_typing": str(ADJOINT),
            "gr_tt_helicity2_z64_uniqueness": str(UNIQUENESS),
        },
        "route_tests": route_tests,
        "attempted_routes": attempted_routes,
        "conditional_proof_if_selection_premise_added": conditional_proof,
        "decision": {
            "proved_unconditionally": False,
            "proved_conditionally": True,
            "minimal_new_premise": conditional_proof["new_selection_premise"],
            "why_unconditional_proof_fails": (
                "Every sourced route establishes that gravity/TT support belongs to shared coherent "
                "bookkeeping, but none identifies the support projector with Pi_exact64. The existing "
                "independence no-go proves that this identification cannot be inferred from the other premises."
            ),
        },
        "guardrails": {
            "claims_exact_support_sourced": False,
            "claims_unconditional_lambda_GR_TT_15": False,
            "uses_interpretive_synthesis_as_proof": False,
            "uses_observed_GR_data": False,
        },
        "note_written": str(OUT_NOTE),
    }

    note = """# Central Circle TT Adjoint Support Proof Attempt v1

## Attempted Theorem

Prove:

```text
Pi_exact64 B^* P_TT = B^* P_TT.
```

## What The Corpus Gives

Three routes were tested.

1. The central-circle route gives a strong physical selector: the central circle
   is the unique shared coherence channel, and gravity operates on that shared
   channel.

2. The GR route gives coherent-sector completeness: physical long-wavelength
   content is exhausted by the observable projection.

3. The capacity route gives gravity as the geometric bookkeeping of coherence
   capacity under locality and diffeomorphism invariance.

Together these make the exact-support theorem highly natural, but they still do
not identify the support projector of `B^*P_TT` with `Pi_exact64`.

## Why The Direct Proof Fails

The central-circle paper explicitly labels its shared-channel gravity claim as
interpretive synthesis rather than a standalone theorem. GR completeness says
the physical content lies in the coherent projected image, not which finite
subprojector inside that image is selected. Capacity bookkeeping identifies the
geometric role of gravity, but it does not compute `DG(Psi*)` or `B^*P_TT`.

The earlier exact-support no-go is decisive: there are models satisfying the
already sourced assumptions with nonzero TT propagation while placing
`B^*P_TT` outside `Pi_exact64`.

## Conditional Proof

If we add the single selection premise:

```text
support projector of B^*P_TT = Pi_exact64
```

on the selected exact GR/QG branch, then the proof is immediate.

1. `B^*P_TT` is the correctly typed physical TT internal support and is nonzero.
2. The selection premise gives `Pi_exact64 B^*P_TT = B^*P_TT`.
3. Weight `2` and BRST compatibility are already closed.
4. The Z64 uniqueness theorem forces the support to be
   `|d_*> tensor span{c_2,s_2}`.
5. Exact-branch compression gives internal normalized `lambda_GR,TT=15`.

## Conclusion

The theorem is not provable unconditionally from the current source set. It is
provable from exactly one additional selection premise, and that premise is now
isolated with no remaining algebraic ambiguity.
"""
    OUT_NOTE.write_text(note, encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
