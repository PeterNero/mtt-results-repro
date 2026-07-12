"""Build the GR-surface / internal-quantum separation theorem packet."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

LOCKED = DATA / "locked_proof_state.candidate.json"
OUTPUT_DATA = DATA / "gr_surface_internal_quantum_separation_theorem.candidate.json"
OUTPUT_CERT = CERTS / "gr_surface_internal_quantum_separation_theorem_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Qa_SU3_GR_Surface_Internal_Quantum_Separation_Theorem_v1.md"


def build() -> tuple[dict[str, object], dict[str, object], str]:
    locked = json.loads(LOCKED.read_text(encoding="utf-8"))
    finite = locked["locked_state"]["finite_hessian"]

    source_amendment = {
        "name": "GRSurfaceInternalQuantumSeparation",
        "authorial_intended_setup": [
            "the only real smooth elastic continuum layer is the GR/protospinor/TT surface sector",
            "nil, lens, circle, monad, twist, and Qa/SU3 color/operator data are quantized internal coherent packets",
            "Planck/minimal-scale internal packet effects are represented by finite/projective/coherent data, not by an additional smooth Qa/SU3 continuum complement",
            "the shared circle remains as the coherence/phase carrier linking the finite internal packet to the smooth GR surface, not as a second smooth determinant domain",
        ],
        "corpus_alignment_evidence": [
            "the protospinor/GR response program separates external TT/Lichnerowicz execution from internal finite gap/operator packets",
            "the Qa/SU3 locked proof already isolates the missing gate as either complement quotient/cancellation or a smooth spectrum source",
            "the finite trace branch source-selects the reduced coherent-sector Hessian with H_sel determinant 2008",
            "the MTT corpus language emphasizes lens/circle/nil and projective/coherent packets more than independent spatial dimensions for the internal sector",
        ],
        "not_assumed_from_old_corpus_without_amendment": [
            "a full same-source smooth Qa/SU3 zeta determinant",
            "a measured coupling or SM threshold match",
            "a numeric GR surface determinant correction to Qa/SU3",
        ],
    }

    hypotheses = [
        "the selected MTT branch adopts the source rule that GR/protospinor/TT carries the smooth elastic continuum degrees of freedom",
        "nil/lens/circle/internal gauge data enter Qa/SU3 through the selected finite coherent packet after projector/quotient",
        "the smooth GR surface determinant is universal/background or belongs to the GR response sector, and is not counted as a Qa/SU3 internal threshold determinant",
        "local gauge, FP/BRST, and quotient determinants are counted once only, with no smooth-complement double count",
        "the finite packet is the locked H_sel/G_ret/Pi_tw/tau branch from the audited Qa/SU3 proof state",
    ]

    conclusions = {
        "Qa_SU3_internal_determinant_domain": "selected finite coherent packet H_sel",
        "smooth_complement_policy": "routed_to_GR_protospinor_surface_sector_not_a_Qa_SU3_internal_determinant",
        "internal_reduced_logdet": finite["finite_rank_logdet"],
        "internal_reduced_determinant": finite["determinant"],
        "full_smooth_Qa_SU3_threshold_claimed": False,
        "measured_coupling_or_full_SM_closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedQaSU3GRSurfaceInternalQuantumSeparationTheorem",
        "status": "QA_SU3_GR_SURFACE_INTERNAL_QUANTUM_SEPARATION_SOURCE_AMENDMENT_ACCEPTED_REDUCED_DETERMINANT_PROMOTED",
        "inputs": {
            "locked_proof_state": str(LOCKED.relative_to(ROOT)),
            "authorial_source_amendment": True,
            "target_fitting_used": False,
        },
        "source_amendment": source_amendment,
        "theorem": {
            "name": "SelectedQaSU3GRSurfaceInternalQuantumSeparation",
            "hypotheses": hypotheses,
            "proof_idea": [
                "the locked proof reduces the open gate to either complement quotient/cancellation or a smooth spectrum source",
                "the source amendment supplies the quotient/cancellation policy by assigning all real smooth elastic modes to the GR/protospinor surface sector",
                "the internal Qa/SU3 sector therefore has no remaining smooth determinant complement beyond the selected finite coherent packet",
                "the locked finite determinant log(2008) is promoted only as the internal reduced Qa/SU3 determinant",
            ],
            "conclusions": conclusions,
        },
        "locked_finite_data": {
            "H_sel": finite["H_sel"],
            "G_ret": finite["G_ret"],
            "Pi_tw": finite["Pi_tw"],
            "tau": finite["tau"],
            "spectrum": finite["spectrum"],
            "determinant": finite["determinant"],
            "finite_rank_logdet": finite["finite_rank_logdet"],
        },
        "guardrails": [
            "this is not a nil smooth zeta-spectrum computation",
            "this does not use the GR surface determinant as a Qa/SU3 correction",
            "this does not import q79/S3/visible-sector numeric values as proof inputs",
            "this does not fit observed couplings, masses, or residuals",
            "this does not double-count local FP/BRST or gauge quotient determinants",
            "this does not claim full SM closure or a measured coupling match",
        ],
        "decision": {
            "smoothness_objection_for_internal_reduced_Qa_SU3_determinant": "closed_if_source_amendment_accepted",
            "internal_reduced_Qa_SU3_determinant": "CLOSED_LOG_2008",
            "GR_smooth_surface_response": "ROUTED_TO_GR_PROTOSPINOR_SECTOR",
            "full_Qa_SU3_physical_threshold_closure": "not_claimed_until_coupling_bridge_or_surface_response_matching_is_supplied",
            "full_SM_closure_now": False,
        },
        "closure_claimed": True,
        "closure_scope": "internal_reduced_Qa_SU3_determinant_only",
        "target_fitting_used": False,
    }

    certificate = {
        "certificate": "SelectedQaSU3GRSurfaceInternalQuantumSeparationTheorem",
        "status": candidate["status"],
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "what_closes": {
            "complement_quotient_policy_as_source_amendment": True,
            "smoothness_objection_for_internal_reduced_determinant": True,
            "internal_reduced_Qa_SU3_logdet": "log(2008)",
        },
        "what_remains_open": {
            "measured_coupling_bridge": True,
            "full_SM_closure": True,
            "GR_surface_response_formalization_in_GR_repo": True,
        },
        "closure_scope": candidate["closure_scope"],
        "target_fitting_used": False,
    }
    return candidate, certificate, render_note(candidate)


def render_note(candidate: dict[str, object]) -> str:
    amend = candidate["source_amendment"]
    theorem = candidate["theorem"]
    finite = candidate["locked_finite_data"]
    guardrails = "\n".join(f"- {item}" for item in candidate["guardrails"])
    hypotheses = "\n".join(f"- {item}" for item in theorem["hypotheses"])
    proof_idea = "\n".join(f"- {item}" for item in theorem["proof_idea"])
    intended = "\n".join(f"- {item}" for item in amend["authorial_intended_setup"])
    alignment = "\n".join(f"- {item}" for item in amend["corpus_alignment_evidence"])
    return f"""# Selected Qa/SU3 GR Surface / Internal Quantum Separation Theorem v1

## Source Amendment

This artifact formalizes the intended MTT setup:

{intended}

The amendment is consistent with the current proof corpus because:

{alignment}

## Theorem

```text
{theorem["name"]}
```

Hypotheses:

{hypotheses}

Conclusion:

```text
Qa/SU3 internal determinant domain = selected finite coherent packet H_sel
smooth GR/protospinor surface modes = routed to GR response sector
internal reduced determinant = {finite["determinant"]}
internal reduced logdet = {finite["finite_rank_logdet"]}
full SM closure = not claimed
```

Proof idea:

{proof_idea}

## Locked Finite Packet

```text
H_sel = {finite["H_sel"]}
G_ret = {finite["G_ret"]}
Pi_tw = {finite["Pi_tw"]}
spectrum = {finite["spectrum"]}
det(H_sel) = {finite["determinant"]}
finite-rank logdet = {finite["finite_rank_logdet"]}
```

## Guardrails

{guardrails}

## Decision

The smooth-complement obstruction is closed for the internal reduced Qa/SU3
determinant if this source amendment is accepted. The result promoted here is
only:

```text
Selected internal reduced Qa/SU3 determinant = log(2008)
```

The GR/protospinor smooth surface response and the bridge from this internal
determinant to measured couplings remain separate tasks.
"""


def main() -> None:
    candidate, certificate, note = build()
    data_text = json.dumps(candidate, indent=2, sort_keys=True)
    cert_text = json.dumps(certificate, indent=2, sort_keys=True)
    if "--write" in sys.argv:
        OUTPUT_DATA.write_text(data_text + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
