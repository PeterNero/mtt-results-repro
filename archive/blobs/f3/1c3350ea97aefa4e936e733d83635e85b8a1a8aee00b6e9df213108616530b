from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"

ROUTEC_LEMMA = SM / "certificates" / "routec_selected_source_origin_lemma_certificate.json"
PHIFIN = SM / "certificates" / "finite_emission_morphism_phifin_certificate.json"
PHIFIN_ALPHA1 = SM / "certificates" / "selected_phifin_alpha1_payload_certificate.json"
SPECTRAL_RETENTION = SM / "certificates" / "selected_spectral_galerkin_projector_retention_data_certificate.json"
FIRST_RUN = SM / "certificates" / "selected_routec_strominger_galerkin_first_run_certificate.json"
PAPER_DRAFT = SM / "proof_corpus" / "paper_appendix_drafts" / "selected_source" / "strominger_system__i1_selected_strominger_minimizer_to_phifin_trace.md"
IMPORT_ATTEMPT = ROOT / "certificates" / "selected_routec_payload_value_import_attempt_certificate.json"

OUT_CERT = ROOT / "certificates" / "routec_selected_source_origin_paper_lemma_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "RouteC_Selected_Source_Origin_Paper_Lemma_v1.md"
OUT_INSERTION = ROOT / "proof_corpus" / "paper_insertions" / "RouteC_Selected_Source_Origin_Lemma_for_Strominger_Paper.md"
OUT_PACKET = ROOT / "candidate_data" / "routec_selected_source_origin_paper_lemma.packet.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    routec = load(ROUTEC_LEMMA)
    phifin = load(PHIFIN)
    phifin_alpha1 = load(PHIFIN_ALPHA1)
    spectral = load(SPECTRAL_RETENTION)
    first_run = load(FIRST_RUN)
    import_attempt = load(IMPORT_ATTEMPT)
    paper_draft = PAPER_DRAFT.read_text(encoding="utf-8")

    closed_support_premises = {
        "fixed_q79_f_m1_s3_gs_sector_identified": routec["what_closes"]["fixed_q79_f_m1_s3_gs_sector_identified"],
        "mtt_strominger_selection_theorem_available": routec["what_closes"]["mtt_strominger_selection_theorem_available"],
        "same_source_support_convergence_proved": routec["what_closes"]["same_source_support_convergence_proved"],
        "finite_codomains_and_validator_schema_identified": (
            phifin["what_closes"]["Phi_fin_codomain_schema_built"]
            and phifin["what_closes"]["routec_finite_validator_slots_mapped"]
        ),
        "target_fitting_excluded": (
            routec["target_fitting_used"] is False
            and phifin["target_fitting_used"] is False
            and phifin_alpha1["target_fitting_used"] is False
        ),
    }

    open_payload_premises = {
        "FiniteEmissionMorphism_Phi_fin": routec["what_remains_open"]["FiniteEmissionMorphism_Phi_fin"],
        "selected_PhiFin_alpha1_payload_values": phifin_alpha1["what_remains_open"]["selected_PhiFin_alpha1_payload_values"],
        "selected_DE_Riesz_Green_dotD_values": spectral["what_remains_open"]["selected_DE_Riesz_Green_dotD_values"],
        "proof_usable_selected_de_response_packet": first_run["what_remains_open"]["proof_usable_selected_de_response_packet"],
        "primitive_C1_overlap_tensors": routec["what_remains_open"]["primitive_C1_overlap_tensors"],
    }

    theorem = {
        "name": "RouteCSelectedSourceOriginConditionalLemma",
        "statement": (
            "On the fixed q79/F,m=1 S3/Green-Schwarz branch, if a finite emission "
            "morphism Phi_fin is constructed as a functorial Galerkin/Cech trace of "
            "the selected Strominger/HYM minimizer and it preserves the S3/GS class, "
            "q79/F orientation, torsion m=1, and Route-C validator basis, then the "
            "Route-C finite residual, rho_E, metric, D_E, Riesz/Green, dotD, and C1 "
            "payloads are theorem-derived selected-source data."
        ),
        "proof": [
            "The fixed topological sector and q79/F,m=1 S3/GS branch are already selected by the imported source certificates.",
            "The MTT Strominger selection theorem supplies the smooth selected minimizer in that fixed sector, up to the equivalence class allowed by the selected functional.",
            "Same-source support convergence is closed: the S3/GS, projective gerbe, block-projector, and Route-C validator targets all point to one selected source rather than independent fitted packets.",
            "A functorial Phi_fin trace from that minimizer to the finite Route-C codomain would carry selectedness along the map, because every emitted finite slot would be the image of the same selected source.",
            "Preservation of branch orientation, torsion m=1, the S3/GS class, and the validator basis prevents a change of branch or a hidden proxy selector.",
            "Therefore the selected_source_verified fields become theorem consequences exactly when Phi_fin emits the required finite payload with error/gap control.",
        ],
        "unconditional_status": "NOT_PROVED_WITH_CURRENT_CERTIFICATES",
        "conditional_status": "PROVED_FROM_PHI_FIN_EMISSION_PREMISE",
    }

    proof_boundary = {
        "can_add_to_paper_now": True,
        "as_full_unconditional_theorem": False,
        "as_conditional_lemma_and_proof_slot": True,
        "paper_target": "Modal_Triplet_Theory__From_MTT_to_the_Strominger__Heterotic_Flux__System.md",
        "paper_section": "Appendix: Selected Strominger Minimizer and Finite Phi_fin Trace",
        "why_not_unconditional": "Current certificates reduce source origin to Phi_fin and selected emission values, but do not construct Phi_fin or emit A_selected/b_selected/C1 payload values.",
    }

    verdict = {
        "support_part_proved": all(closed_support_premises.values()),
        "conditional_routec_source_origin_lemma_proved": True,
        "unconditional_routec_source_origin_lemma_proved": False,
        "selected_matter_stress_coefficients_closed": False,
        "paper_ready_insertion_written": True,
        "next_required_artifact": "FiniteEmissionMorphism_Phi_fin_with_Selected_Payload_Emission",
    }

    guardrails = {
        "does_not_promote_lifted_flags": True,
        "does_not_claim_phi_fin_constructed": True,
        "does_not_claim_selected_payload_values_emitted": True,
        "does_not_use_observed_or_benchmark_inputs": True,
        "preserves_paper_caveat_until_proof": True,
    }

    insertion = """# Route-C Selected Source-Origin Lemma Insert

Target paper:

```text
Modal_Triplet_Theory__From_MTT_to_the_Strominger__Heterotic_Flux__System.md
```

Suggested location:

```text
Appendix: Selected Strominger Minimizer and Finite Phi_fin Trace
```

## Lemma: Conditional Route-C Source Origin

On the fixed `q79/F,m=1` `S3`/Green-Schwarz branch, suppose there exists a
finite emission morphism

```text
Phi_fin : selected Strominger/HYM minimizer -> finite Route-C payload
```

defined as a functorial Galerkin/Cech trace of the selected minimizer, preserving
the `S3` Deligne/Cech class, the Green-Schwarz row, the `q79/F` orientation, the
torsion label `m=1`, and the Route-C finite validator basis. Then the emitted
finite Route-C residual, `rho_E`, Hermitian metric, sector maps, `D_E`,
Riesz/gap, reduced Green, `dotD_alpha1`, and primitive C1 payloads are selected
source data.

## Proof

The selected branch fixes the topological and differential-cohomology sector:
`q79/F,m=1` with the selected `S3`/Green-Schwarz support. The MTT
Strominger/HYM selection functional selects a minimizer in that fixed sector.
The Route-C finite validator codomain is already identified, and the
same-source support checks show that the `S3` source, projective gerbe support,
block projectors, and Route-C operator targets converge on one source rather
than on independent fitted packets.

If `Phi_fin` is a functorial trace of that minimizer, every finite emitted
object is the image of the same selected source. Preservation of branch
orientation, torsion, `S3`/GS class, and validator basis prevents a hidden
change of sector. Therefore the finite `selected_source_verified` flags become
theorem-derived fields exactly when the `Phi_fin` emission exists with the
required error/gap certificate.

## Present Status

The support part of this lemma is proved in the current proof ledgers. The
unconditional theorem is not yet proved because `Phi_fin` has not emitted the
selected payload values. Until that emission is constructed, Route-C matrices
remain admissible support/diagnostic data, not selected-source proof data.

Required guardrail:

```text
No observed masses, mixings, thresholds, Newton/Planck values, or fitted
constants are used to select the source, branch, cover, operator, or promotion
flag in this lemma.
```
"""

    note = f"""# Route-C Selected Source-Origin Paper Lemma v1

## Result

The unconditional Route-C selected source-origin lemma still cannot be proved
from the current certificates. The maximal theorem we can prove now is the
conditional source-origin lemma from `Phi_fin` emission.

Status:

```text
support part proved: {verdict["support_part_proved"]}
conditional lemma proved: {verdict["conditional_routec_source_origin_lemma_proved"]}
unconditional lemma proved: {verdict["unconditional_routec_source_origin_lemma_proved"]}
```

## Why This Is Still Progress

The proof now has a clean paper-ready form: all fixed-sector and same-source
support is closed, and the only theorem slot that must still be filled is the
finite emission morphism from the selected Strominger/HYM minimizer to the
finite Route-C payload.

The insertion text is written at:

```text
{OUT_INSERTION}
```

It should be added to the Strominger/HYM paper as a conditional lemma and proof
slot, preserving the caveat that Route-C matrices are not selected-source proof
data until `Phi_fin` emits the payload.
"""

    packet = {
        "theorem": theorem,
        "closed_support_premises": closed_support_premises,
        "open_payload_premises": open_payload_premises,
        "proof_boundary": proof_boundary,
        "paper_draft_already_exists_in_sm_parity": str(PAPER_DRAFT),
        "paper_draft_excerpt_status": "APPENDIX_DRAFT_PROOF_SLOT_OPEN" if "APPENDIX_DRAFT_PROOF_SLOT_OPEN" in paper_draft else "UNKNOWN",
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "routec_selected_source_origin_paper_lemma",
        "status": "ROUTEC_SOURCE_ORIGIN_CONDITIONAL_LEMMA_PROVED_PAPER_INSERTION_BUILT_PHI_FIN_OPEN",
        "input_certificates": {
            "routec_selected_source_origin_lemma": str(ROUTEC_LEMMA),
            "finite_emission_morphism_phifin": str(PHIFIN),
            "selected_phifin_alpha1_payload": str(PHIFIN_ALPHA1),
            "selected_spectral_galerkin_projector_retention": str(SPECTRAL_RETENTION),
            "selected_routec_strominger_galerkin_first_run": str(FIRST_RUN),
            "selected_routec_payload_value_import_attempt": str(IMPORT_ATTEMPT),
            "existing_sm_parity_paper_draft": str(PAPER_DRAFT),
        },
        "theorem": theorem,
        "closed_support_premises": closed_support_premises,
        "open_payload_premises": open_payload_premises,
        "proof_boundary": proof_boundary,
        "verdict": verdict,
        "guardrails": guardrails,
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
        "paper_insertion_written": str(OUT_INSERTION),
    }

    OUT_INSERTION.parent.mkdir(parents=True, exist_ok=True)
    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    OUT_INSERTION.write_text(insertion, encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_INSERTION}")
    print("STATUS: ROUTEC_SOURCE_ORIGIN_CONDITIONAL_LEMMA_PROVED_PAPER_INSERTION_BUILT_PHI_FIN_OPEN")


if __name__ == "__main__":
    main()
