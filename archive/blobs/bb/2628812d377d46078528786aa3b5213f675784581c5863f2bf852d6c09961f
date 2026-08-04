"""Add the missing source payload for the canonical PhiFin S2 trace formula."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

S0_PREFIX = DATA / "selected_phifin_s0_source_prefix.candidate.json"
FINITE_TRACE = DATA / "selected_phifin_finite_trace_existence.candidate.json"
S1_PARTIAL = DATA / "selected_phifin_s1s2_value_emission.partial_filled.json"
FORMULA = DATA / "selected_trace_equals_emitted_27_mode_de_attempt.candidate.json"
MORPHISM = DATA / "selected_phifin_s2_finite_trace_morphism_scaffold.candidate.json"

OUTPUT_PACKET = DATA / "selected_canonical_trace_formula_source.candidate.json"
OUTPUT_TEMPLATE = DATA / "selected_canonical_trace_formula_source.payload.template.json"
OUTPUT_CERT = CERTS / "selected_canonical_trace_formula_source_certificate.json"
OUTPUT_NOTE = CORPUS / "SelectedCanonicalTraceFormulaSource_v1.md"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    s0 = load_json(S0_PREFIX)
    finite_trace = load_json(FINITE_TRACE)
    s1 = load_json(S1_PARTIAL)
    formula = load_json(FORMULA)
    morphism = load_json(MORPHISM)

    slots = {
        "T0_selected_smooth_source": {
            "status": "CLOSED",
            "evidence": {
                "s0_closed": s0["s0_closed"],
                "branch": s0["selected_branch"],
                "source_is_not_fixture": s0["what_closes_now"]["selected_source_not_hypothetical_or_fixture"],
            },
            "what_it_supplies": "The smooth selected source exists in the fixed q79/F,m=1 S3/GS branch.",
        },
        "T1_functorial_trace_domain": {
            "status": "CLOSED",
            "evidence": {
                "finite_trace_exists": finite_trace["theorem"]["proved"],
                "same_BN_basis_identity": morphism["morphism_faces"]["F3_same_BN_basis_and_finite_algebra"]["closed"],
            },
            "what_it_supplies": "The equality can be stated on B_N = F3xF3_gerbe_twisted_fourier_N1_rank3.",
        },
        "T2_projective_flat_rhoE_trace": {
            "status": "PARTIAL_CLOSED_SOURCE_LEVEL_OPERATOR_VALUES_OPEN",
            "evidence": {
                "nonidentity_trace": s1["S1_transition_or_connection_trace"]["nonidentity_or_equivalent_connection_trace"],
                "preserves_branch": s1["S1_transition_or_connection_trace"]["preserves_s3_gs_and_q79_f_m1"],
                "full_selected_payload_emitted": s1["partial_fill_guardrail"]["full_selected_payload_emitted"],
            },
            "what_it_supplies": (
                "The active F3xF3 projective Heisenberg/Weyl carrier is present, "
                "but not yet a full selected connection with selected D_E values."
            ),
        },
        "T3_canonical_fourier_metric_formula": {
            "status": "FORMULA_CLOSED_SOURCE_SELECTION_OPEN",
            "evidence": {
                "formula_proved_for_emitted_matrices": formula["formula_theorem"]["proved"],
                "formula_statement": formula["formula_theorem"]["statement"],
            },
            "what_it_supplies": (
                "The finite formula is known exactly; what remains is proving "
                "that the selected trace chooses this canonical metric normalization."
            ),
        },
        "T4_H_rank_two_zero_cluster_shift": {
            "status": "FORMULA_CLOSED_SOURCE_SELECTION_OPEN",
            "evidence": {
                "H_shift_indices": formula["sector_formula_checks"]["H"]["higgs_shift_indices"],
                "H_formula_matches": formula["sector_formula_checks"]["H"]["matches_canonical_formula"],
            },
            "what_it_supplies": (
                "The H correction is exactly rank two on zero-cluster indices 13,14; "
                "the selected source origin of that projector remains open."
            ),
        },
        "T5_same_source_binding": {
            "status": "OPEN",
            "evidence": {
                "selected_trace_equality_proved": formula["selected_trace_attempt"]["proved"],
                "selected_source_flags_all_false": all(
                    not item["selected_source_verified"]
                    for item in formula["sector_formula_checks"].values()
                ),
            },
            "what_it_supplies": (
                "This is the missing final binding: T0-T4 must be derived from "
                "one selected source, not assembled from model-active finite data."
            ),
        },
    }

    missing_payload = {
        "name": "SelectedCanonicalTraceFormulaSourcePayload",
        "must_supply": {
            "canonical_active_metric_normalization_source": (
                "A theorem that the S0 selected Strominger/HYM minimizer induces "
                "the active F3xF3 metric whose Fourier Laplacian has eigenvalues "
                "((2*pi)/3)^2(m^2+n^2) on B_N."
            ),
            "projective_flat_connection_to_DE_source": (
                "A theorem that the selected projective rho_E/connection trace is "
                "flat on active deck directions for the D_E quadratic form, so no "
                "extra off-diagonal or sector-dependent family terms appear."
            ),
            "H_rank_two_shift_source": (
                "A theorem that the Higgs sector adds exactly the rank-two unit "
                "projector on zero-cluster indices 13 and 14 from the same selected source."
            ),
            "same_source_no_substitution_certificate": (
                "A certificate that the emitted canonical formula is computed from "
                "the selected source and not copied from model-active scaffold data."
            ),
        },
    }

    closure_if_payload_supplied = {
        "selected_trace_equality": True,
        "selected_eta_N": formula["conditional_consequence"]["eta_N_if_gate_closes"],
        "eta_threshold": formula["conditional_consequence"]["threshold"],
        "gap_layer_closes": formula["conditional_consequence"]["passes_threshold"],
        "D_E_source_flags_may_be_theorem_derived": True,
        "dotD_C1_still_separate": True,
    }

    return {
        "packet": "SelectedCanonicalTraceFormulaSource_v1",
        "status": "MISSING_SOURCE_PAYLOAD_ADDED_TRACE_EQUALITY_STILL_OPEN",
        "inputs": {
            "S0_prefix": str(S0_PREFIX.relative_to(ROOT)),
            "finite_trace": str(FINITE_TRACE.relative_to(ROOT)),
            "S1_partial": str(S1_PARTIAL.relative_to(ROOT)),
            "formula_attempt": str(FORMULA.relative_to(ROOT)),
            "morphism_scaffold": str(MORPHISM.relative_to(ROOT)),
        },
        "slots": slots,
        "missing_payload": missing_payload,
        "closure_if_payload_supplied": closure_if_payload_supplied,
        "source_lemma": {
            "name": "SelectedCanonicalTraceFormulaSourceLemma",
            "proved": False,
            "statement": (
                "The S0 selected smooth source induces the canonical active "
                "F3xF3 Fourier metric and projective-flat connection on B_N, "
                "and the same source induces the H-sector rank-two zero-cluster "
                "projector. Therefore Phi_fin(D_E(selected source)) equals the "
                "emitted 27-mode D_E formula sector-by-sector."
            ),
            "why_not_proved_yet": (
                "The emitted formula and supporting source scaffold are present, "
                "but the canonical metric/connection and H-projector source "
                "selection theorem is not in the current corpus."
            ),
        },
        "guardrails": {
            "does_not_set_selected_source_flags": True,
            "does_not_claim_source_lemma_proved": True,
            "does_not_promote_eta_now": True,
            "does_not_use_observed_or_benchmark_inputs": True,
            "keeps_dotD_C1_separate": True,
        },
        "verdict": {
            "what_closes_now": (
                "The missing source payload is added as an executable gate with "
                "all required subclaims and current evidence classified."
            ),
            "what_remains": (
                "Prove the source lemma selecting the canonical metric/connection "
                "and H rank-two projector from the same S0 selected source."
            ),
            "next_required_artifact": "Prove_SelectedCanonicalTraceFormulaSourceLemma_v1",
        },
    }


def build_template(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "template": "SelectedCanonicalTraceFormulaSourcePayload",
        "status": "OPEN_FILL_REQUIRED",
        "required_fields": packet["missing_payload"]["must_supply"],
        "acceptance_tests": [
            "all required fields cite theorem-derived selected source evidence",
            "canonical Fourier metric normalization is derived before D_E values are promoted",
            "H rank-two zero-cluster projector is derived from the same source",
            "no selected_source_verified flag is copied from model-active data",
            "no observed masses, mixings, gauge constants, or benchmark matrices are used",
        ],
        "closure_consequence": packet["closure_if_payload_supplied"],
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "SelectedCanonicalTraceFormulaSource",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "template_path": str(OUTPUT_TEMPLATE.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "what_closes_now": {
            "missing_source_payload_added": True,
            "required_subclaims_classified": True,
            "closure_consequence_recorded": True,
        },
        "what_remains_open": {
            "SelectedCanonicalTraceFormulaSourceLemma": True,
            "canonical_metric_connection_source": True,
            "H_rank_two_shift_source": True,
            "selected_trace_equality": True,
        },
        "source_lemma": packet["source_lemma"],
        "closure_if_payload_supplied": packet["closure_if_payload_supplied"],
        "guardrails": packet["guardrails"],
        "verdict": packet["verdict"],
    }


def render_note(cert: dict[str, Any], packet: dict[str, Any]) -> str:
    return f"""# SelectedCanonicalTraceFormulaSource v1

## Result

Status: `{cert["status"]}`

This adds the missing source payload gate. It does not prove the source lemma
yet and does not promote selected source flags.

## Missing Payload

```json
{json.dumps(packet["missing_payload"]["must_supply"], indent=2, sort_keys=True)}
```

## Current Slot Status

```json
{json.dumps(packet["slots"], indent=2, sort_keys=True)}
```

## Source Lemma To Prove

```text
{packet["source_lemma"]["statement"]}
```

## If This Lemma Closes

```json
{json.dumps(packet["closure_if_payload_supplied"], indent=2, sort_keys=True)}
```
"""


def main() -> int:
    packet = build_packet()
    template = build_template(packet)
    cert = build_certificate(packet)
    if "--write" in sys.argv:
        OUTPUT_PACKET.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_TEMPLATE.write_text(json.dumps(template, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(render_note(cert, packet), encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
