from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MTT = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")

NO_GO = ROOT / "certificates" / "btt_exact_support_independence_no_go_certificate.json"
ADJOINT = ROOT / "certificates" / "btt_adjoint_shape_map_typing_theorem_certificate.json"
UNIQUENESS = ROOT / "certificates" / "gr_tt_helicity2_z64_uniqueness_theorem_certificate.json"
CENTRAL = (
    MTT
    / "13 Standard Model & Topology-Only Constraints"
    / "The_Central_Circle__Inertia__Mass__Gravity__and_Time_as_Shared_Coherence_Bookkeeping_in_Modal_Triplet_Theory.md"
)

OUT_CERT = ROOT / "certificates" / "final_btt_support_closure_decision_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "Final_BTT_Support_Closure_Decision_v1.md"
OUT_THEOREM_TEMPLATE = ROOT / "candidate_data" / "central_circle_tt_adjoint_support_theorem.template.json"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def has(text: str, *needles: str) -> bool:
    return all(needle in text for needle in needles)


def main() -> None:
    central = read(CENTRAL)
    no_go = load(NO_GO)
    adjoint = load(ADJOINT)
    uniqueness = load(UNIQUENESS)

    source_tests = {
        "central_paper_labels_core_claim_as_interpretive_synthesis": has(
            central,
            "(L3) Structural identifications (interpretive synthesis)",
            "unifying explanatory map rather than as new standalone theorems",
        ),
        "central_paper_says_we_show_means_synthesize": has(
            central,
            '"we show" in this paper should be read as "we make explicit / we synthesize"',
        ),
        "central_unique_shared_channel_claim_present": has(
            central,
            "the central circle is the unique shared coherence channel",
        ),
        "central_gravity_shared_circle_claim_present": has(
            central,
            "Gravity, by contrast, operates on the shared circle itself",
        ),
        "central_gravity_strain_claim_present": has(
            central,
            "gravity measures how much the shared circle coherence",
            "is strained",
        ),
        "independence_no_go_closed": (
            no_go["status"] == "EXACT_SUPPORT_IDENTITY_INDEPENDENT_OF_CURRENT_SOURCED_ASSUMPTIONS"
        ),
        "adjoint_nonzero_closed": adjoint["closed_now"]["TT_coupling_nonzero_for_adjoint_support"] is True,
        "uniqueness_ready": uniqueness["theorem"]["closed"] is True,
    }

    theorem_template = {
        "schema": "CentralCircleTTAdjointSupportTheorem.v1",
        "status": "REQUIRED_FOR_FINAL_GR_TT_Z64_CLOSURE",
        "statement": (
            "For the selected GR/QG exact branch, the physical TT adjoint support "
            "J_TT=B^*P_TT is exhausted by the exact central-circle Z64 projector: "
            "Pi_exact64 B^* P_TT = B^* P_TT, and the circle coordinate is the same "
            "sampled coordinate used by the exact Z64 shift."
        ),
        "minimal_hypotheses_to_source": [
            "the central-circle gravity/shared-channel claim is promoted from interpretive synthesis to a proved theorem",
            "the selected exact Z64 central-circle projector is identified with the GR/QG shared-circle TT support projector",
            "the adjoint metric shape map B^*P_TT is nonzero and physical on the BRST quotient",
            "the sampled central-circle coordinate agrees with the exact Z64 carrier coordinate",
        ],
        "then_existing_results_imply": {
            "support_J_TT": "|d_*> tensor span{c_2,s_2}",
            "lambda_GR_TT_internal_normalized": 15.0,
        },
        "must_not_use": [
            "observed Newton constant",
            "observed Planck scale",
            "graviton phenomenology",
            "fitting lambda_GR_TT to 15",
        ],
    }
    OUT_THEOREM_TEMPLATE.write_text(json.dumps(theorem_template, indent=2), encoding="utf-8")

    decision = {
        "can_close_unconditionally_from_current_corpus": False,
        "can_close_conditionally_with_template_theorem": True,
        "why_not_unconditional": (
            "The only corpus text strong enough to identify gravity with the shared central circle "
            "explicitly labels the identification as interpretive synthesis, not a standalone theorem; "
            "the exact-support no-go shows the identity is independent of the already sourced assumptions."
        ),
        "what_is_now_closed_down": [
            "the old incorrectly typed B_TT image gate is rejected",
            "the correctly typed adjoint support gate is identified",
            "nonzero TT adjoint coupling, weight 2, and BRST compatibility are closed",
            "the exact-support identity is proved independent of current sourced assumptions",
            "the unique missing theorem is specified in validator-ready form",
        ],
        "next_action_for_full_closure": (
            "Write/prove CentralCircleTTAdjointSupportTheorem.v1 in the corpus, or compute DG(Psi*) "
            "directly and verify Pi_exact64 B^* P_TT = B^* P_TT."
        ),
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "final_btt_support_closure_decision",
        "status": "FINAL_BTT_SUPPORT_GATE_CLOSED_AS_SOURCE_OPEN_NOT_DERIVABLE",
        "source_files": {"central_circle": str(CENTRAL)},
        "input_certificates": {
            "btt_exact_support_independence_no_go": str(NO_GO),
            "btt_adjoint_shape_map_typing_theorem": str(ADJOINT),
            "gr_tt_helicity2_z64_uniqueness": str(UNIQUENESS),
        },
        "source_tests": source_tests,
        "decision": decision,
        "required_theorem_template_written": str(OUT_THEOREM_TEMPLATE),
        "guardrails": {
            "claims_unconditional_lambda_GR_TT_15": False,
            "uses_interpretive_synthesis_as_proof": False,
            "claims_exact_support_sourced": False,
            "uses_observed_GR_data": False,
        },
        "note_written": str(OUT_NOTE),
    }

    note = """# Final BTT Support Closure Decision v1

## Decision

The remaining exact-support identity cannot be closed unconditionally from the
current corpus:

```text
Pi_exact64 B^* P_TT = B^* P_TT.
```

The reason is now precise. The central-circle paper contains the needed physical
idea, but it explicitly labels the gravity/shared-circle identification as
interpretive synthesis, not as a standalone theorem. The exact-support no-go
then proves that this identity is independent of the assumptions currently
sourced in the proof repo.

## What Is Closed

The proof state is no longer vague. We have closed:

```text
correct object: J_TT := Pi_exact64 B^* P_TT,
nonzero TT adjoint support,
TT weight 2,
BRST/diffeomorphism quotient compatibility,
exact Z64 branch availability,
uniqueness of the k=2 real character plane,
independence of exact support from current assumptions.
```

## The Unique Missing Theorem

Full closure now requires exactly this theorem:

```text
CentralCircleTTAdjointSupportTheorem:
For the selected GR/QG exact branch, the physical TT adjoint support B^*P_TT
is exhausted by the exact central-circle Z64 projector, and the sampled
central-circle coordinate is the same coordinate used by the exact Z64 shift.
```

Equivalently:

```text
Pi_exact64 B^* P_TT = B^* P_TT.
```

If that theorem is supplied, existing certificates immediately give:

```text
support(J_TT)=|d_*> tensor span{c_2,s_2},
lambda_GR,TT=15
```

in normalized internal exact-branch units.

## What Would Be Overclaiming

It would be overclaiming to use the current central-circle synthesis text as
the proof of exact support. It is excellent physical guidance, but the paper
itself tells us not to treat that synthesis as a new technical theorem.
"""
    OUT_NOTE.write_text(note, encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"WROTE: {OUT_THEOREM_TEMPLATE}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
