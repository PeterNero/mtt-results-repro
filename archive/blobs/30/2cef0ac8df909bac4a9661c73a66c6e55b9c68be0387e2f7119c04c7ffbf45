"""Attempt the Selected PhiFin S2 27-mode provenance theorem."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SM = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure")

S0_PREFIX = DATA / "selected_phifin_s0_source_prefix.candidate.json"
PROMOTION = DATA / "selected_phifin_s2_source_promotion_criterion.candidate.json"
FORM_FILL = DATA / "selected_phifin_s2_a_sel_n_form_bound_fill_attempt.candidate.json"
VALUE_REPLAY = DATA / "selected_phifin_s2_value_emission_with_gap_error_honest_replay.candidate.json"
WAY_FORWARD = SM / "candidate_data" / "routec_selected_source_origin_way_forward.candidate.json"

OUTPUT_PACKET = DATA / "selected_phifin_s2_27_mode_provenance_theorem_attempt.candidate.json"
OUTPUT_CERT = CERTS / "selected_phifin_s2_27_mode_provenance_theorem_attempt_certificate.json"
OUTPUT_NOTE = CORPUS / "Selected_PhiFin_S2_27_Mode_Provenance_Theorem_Attempt_v1.md"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    s0 = load_json(S0_PREFIX)
    promotion = load_json(PROMOTION)
    form_fill = load_json(FORM_FILL)
    replay = load_json(VALUE_REPLAY)
    way_forward = load_json(WAY_FORWARD)

    branch_eval = promotion["current_branch_evaluation"]
    source_origin = promotion["source_origin_lemma_import"]
    diagnostic_eta = form_fill["route_results"]["route_2_explicit_A_sel_N"][
        "diagnostic_27_mode_eta"
    ]["max_eta_if_provenance_were_supplied"]
    eta_threshold = form_fill["eta_threshold"]

    conditional_theorem = {
        "name": "SelectedPhiFinS2_27ModeConditionalProvenanceTheorem",
        "proved": True,
        "statement": (
            "If the S0 selected smooth source admits a functorial finite "
            "Phi_fin/Galerkin-Cech trace on B_N, and if that trace emits the "
            "existing 27-mode D_E stiffness matrices as the selected compression "
            "A_sel,N while preserving the q79/F,m=1 S3/GS Route-C branch, then "
            "the diagnostic eta=1.0 becomes selected eta_N and the selected "
            "gap/Riesz/Green certificate closes because eta_N < 2.1932454224643014."
        ),
    }

    unconditional_attempt = {
        "name": "SelectedPhiFinS2_27ModeUnconditionalProvenanceTheorem",
        "proved": False,
        "reason": (
            "The corpus supplies S0 selected smooth source provenance, a same-basis "
            "27-mode model-active scaffold, and a numerical eta budget. It does "
            "not supply the finite emission morphism proving the 27-mode matrices "
            "are the selected Phi_fin/Strominger compression rather than a "
            "model-active substitute."
        ),
    }

    evidence_table = {
        "S0_abstract_selected_source": s0["s0_closed"],
        "same_27_mode_basis_available": replay["same_basis_value_payload"][
            "basis_id"
        ]
        == "F3xF3_gerbe_twisted_fourier_N1_rank3",
        "actual_27_mode_matrix_entries_emitted": replay["criterion_evaluation"][
            "actual_D_E_matrix_entries_emitted"
        ],
        "diagnostic_eta_below_threshold": diagnostic_eta < eta_threshold,
        "functorial_finite_Phi_fin_trace_proved": False,
        "existing_27_mode_matrices_identified_as_selected_compression": False,
        "S2_D_E_selected_source_verified": branch_eval["S2_D_E_selected_source_verified"],
        "honest_replay_without_lifted_flags": replay["honest_replay"][
            "honest_replay_without_lifted_flags_passes"
        ],
    }

    missing_morphism = {
        "name": "FiniteTraceMorphismIdentifies27ModeScaffold",
        "statement": (
            "The finite Phi_fin/Galerkin-Cech trace of the S0 selected smooth "
            "Strominger/HYM minimizer, restricted to B_N = "
            "F3xF3_gerbe_twisted_fourier_N1_rank3, equals the emitted 27-mode "
            "D_E stiffness matrices sector-by-sector, with the Higgs-sector "
            "rank-one shift accounted for by the same selected source."
        ),
        "must_supply": [
            "selected connection or rho_E finite trace values on B_N",
            "operator equality or certified form equality between Phi_fin trace and 27-mode matrices",
            "branch preservation for q79/F,m=1 S3/GS Route-C",
            "proof that matrices are not fixture/model-active substitutes",
            "honest validator replay without lifted source flags for D_E/Riesz/Green",
        ],
        "why_this_is_enough": (
            "The eta budget is already numerically inside the required threshold. "
            "The missing item is the morphism that turns the diagnostic matrices "
            "into selected matrices."
        ),
    }

    return {
        "packet": "Selected_PhiFin_S2_27_Mode_Provenance_Theorem_Attempt_v1",
        "status": "CONDITIONAL_PROVENANCE_THEOREM_CLOSED_UNCONDITIONAL_MORPHISM_OPEN",
        "inputs": {
            "S0_source_prefix": str(S0_PREFIX.relative_to(ROOT)),
            "promotion_criterion": str(PROMOTION.relative_to(ROOT)),
            "form_bound_fill_attempt": str(FORM_FILL.relative_to(ROOT)),
            "value_replay": str(VALUE_REPLAY.relative_to(ROOT)),
            "routec_source_origin_way_forward": str(WAY_FORWARD),
        },
        "conditional_theorem": conditional_theorem,
        "unconditional_attempt": unconditional_attempt,
        "evidence_table": evidence_table,
        "diagnostic_eta": {
            "eta_if_provenance_supplied": diagnostic_eta,
            "threshold": eta_threshold,
            "passes_threshold": diagnostic_eta < eta_threshold,
            "selected_eta_emitted_now": False,
        },
        "imported_source_origin_status": {
            "conditional_status": source_origin["conditional_status"],
            "unconditional_status": source_origin["unconditional_status"],
            "open_payload_premises": source_origin["open_payload_premises"],
            "recommended_route": way_forward["recommended_next_artifact"]["name"],
            "route_ranking_primary": way_forward["route_ranking"][0],
        },
        "missing_morphism": missing_morphism,
        "current_closure": {
            "conditional_provenance_theorem_closed": True,
            "unconditional_provenance_theorem_closed": False,
            "selected_eta_promoted": False,
            "selected_gap_error_certificate_closed": False,
            "D_E_source_flags_promoted": False,
            "dotD_alpha1_C1_response_closed": False,
        },
        "guardrails": {
            "does_not_promote_conditional_to_unconditional": True,
            "does_not_set_selected_source_flags": True,
            "does_not_treat_model_active_as_selected": True,
            "does_not_claim_selected_eta_emitted": True,
            "does_not_use_observed_or_benchmark_inputs": True,
        },
        "verdict": {
            "what_closes_now": (
                "The conditional provenance theorem closes: if the finite trace "
                "morphism identifies the emitted 27-mode matrices with selected "
                "Phi_fin compression, then eta=1.0 closes the selected "
                "gap/Riesz/Green layer."
            ),
            "what_remains": (
                "Prove the finite trace morphism that identifies the 27-mode "
                "scaffold with the selected Phi_fin/Strominger compression."
            ),
            "next_required_artifact": "Selected_PhiFin_S2_Finite_Trace_Morphism_Identifies_27_Mode_Scaffold_v1",
        },
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "SelectedPhiFinS2_27ModeProvenanceTheoremAttempt",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "what_closes_now": {
            "conditional_provenance_theorem": True,
            "diagnostic_eta_promotable_if_morphism_supplied": True,
            "unconditional_gap_identified": True,
            "finite_trace_morphism_obligation_isolated": True,
        },
        "what_remains_open": {
            "finite_trace_morphism_identifies_27_mode_scaffold": True,
            "selected_eta_N": True,
            "selected_gap_error_certificate": True,
            "D_E_source_flags": True,
            "dotD_alpha1_C1_response": True,
        },
        "current_closure": packet["current_closure"],
        "verdict": packet["verdict"],
        "guardrails": packet["guardrails"],
    }


def render_note(cert: dict[str, Any], packet: dict[str, Any]) -> str:
    return f"""# Selected PhiFin S2 27-Mode Provenance Theorem Attempt v1

## Result

Status: `{cert["status"]}`

The conditional theorem is proved. The unconditional provenance theorem is not
yet proved.

## What Closes

If a finite trace morphism identifies the emitted 27-mode matrices as the
selected `Phi_fin/Strominger` compression, then the existing diagnostic eta
becomes selected:

```text
eta = {packet["diagnostic_eta"]["eta_if_provenance_supplied"]}
threshold = {packet["diagnostic_eta"]["threshold"]}
passes = {packet["diagnostic_eta"]["passes_threshold"]}
```

So the numerical perturbation budget is ready.

## Why It Still Does Not Fully Close

The current corpus does not yet prove:

```text
{packet["missing_morphism"]["name"]}
```

Statement:

```text
{packet["missing_morphism"]["statement"]}
```

## Required Payload

{chr(10).join("- " + item for item in packet["missing_morphism"]["must_supply"])}

## Next Artifact

```text
{packet["verdict"]["next_required_artifact"]}
```
"""


def main() -> int:
    packet = build_packet()
    cert = build_certificate(packet)
    if "--write" in sys.argv:
        OUTPUT_PACKET.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(render_note(cert, packet), encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
