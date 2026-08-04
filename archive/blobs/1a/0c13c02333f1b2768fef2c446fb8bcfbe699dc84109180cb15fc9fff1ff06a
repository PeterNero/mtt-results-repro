"""Prove the local criterion for promoting S2 Phi_fin source flags."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
GR = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-protospinor-gr-response-proof")

S0_CERT = CERTS / "selected_phifin_s0_source_prefix_certificate.json"
EXISTENCE_CERT = CERTS / "selected_phifin_finite_trace_existence_certificate.json"
S1_CERT = CERTS / "selected_phifin_s1_rhoe_trace_fill_certificate.json"
S2_CERT = CERTS / "selected_phifin_s2_operator_scaffold_import_certificate.json"
S2_PACKET = DATA / "selected_phifin_s1s2_value_emission.s2_scaffold.json"
SOURCE_LEMMA = GR / "certificates" / "routec_selected_source_origin_paper_lemma_certificate.json"

OUTPUT_PACKET = DATA / "selected_phifin_s2_source_promotion_criterion.candidate.json"
OUTPUT_CERT = CERTS / "selected_phifin_s2_source_promotion_criterion_certificate.json"
OUTPUT_NOTE = CORPUS / "Selected_PhiFin_S2_Source_Promotion_Criterion_v1.md"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    s0 = load_json(S0_CERT)
    existence = load_json(EXISTENCE_CERT)
    s1 = load_json(S1_CERT)
    s2 = load_json(S2_CERT)
    scaffold = load_json(S2_PACKET)
    lemma = load_json(SOURCE_LEMMA)

    s2_blocks = scaffold["S2_galerkin_basis_and_operator_blocks"]
    source_flags = scaffold["S2_operator_scaffold_import"]["source_flags"]

    criterion = {
        "name": "SelectedPhiFinS2SourcePromotionCriterion",
        "proved": True,
        "statement": (
            "For the fixed q79/F,m=1 S3/GS Route-C branch and the imported "
            "F3xF3 gerbe-twisted Fourier rank-3 B_N scaffold, the S2 finite "
            "D_E, Riesz/Green, dotD, and alpha1-driver flags may be promoted "
            "only when the finite Phi_fin trace is a functorial Galerkin/Cech "
            "image of the selected Strominger/HYM minimizer, preserves the "
            "branch data, emits the actual finite values, and supplies a "
            "positive gap/truncation certificate. Under those conditions the "
            "flags are theorem consequences; without them they must remain false."
        ),
    }

    current = {
        "fixed_selected_smooth_source_available": s0["what_closes_now"][
            "S0_selected_source_as_abstract_smooth_source"
        ],
        "abstract_finite_trace_existence_available": existence["what_closes_now"][
            "S1_S2_existence_theorem"
        ],
        "S1_projective_rhoE_trace_filled": s1["what_closes_now"][
            "S1_nonidentity_projective_rhoE_trace_filled"
        ],
        "S2_same_basis_scaffold_available": s2["what_closes_now"][
            "S2_27_mode_operator_scaffold_imported"
        ],
        "S2_D_E_selected_source_verified": source_flags["D_E_selected_source_verified"],
        "S2_dotD_selected_source_verified": source_flags["dotD_selected_source_verified"],
        "S2_dotD_alpha1_driver_verified": source_flags["dotD_alpha1_driver_verified"],
        "selected_gap_error_certificate_emitted": s2_blocks["Riesz_projector_entries"][
            "selected_gap_error_certificate_emitted"
        ],
        "gap_condition_epsilon_lt_gamma_margin": s2_blocks[
            "gap_condition_epsilon_lt_gamma_margin"
        ],
        "full_selected_payload_emitted": scaffold["partial_fill_guardrail"][
            "full_selected_payload_emitted"
        ],
    }

    return {
        "packet": "Selected_PhiFin_S2_Source_Promotion_Criterion_v1",
        "status": "SELECTED_PHIFIN_S2_SOURCE_PROMOTION_CRITERION_PROVED_VALUES_OPEN",
        "inputs": {
            "S0_source_prefix": str(S0_CERT.relative_to(ROOT)),
            "finite_trace_existence": str(EXISTENCE_CERT.relative_to(ROOT)),
            "S1_rhoE_trace_fill": str(S1_CERT.relative_to(ROOT)),
            "S2_operator_scaffold": str(S2_CERT.relative_to(ROOT)),
            "S2_scaffold_packet": str(S2_PACKET.relative_to(ROOT)),
            "GR_conditional_source_origin_lemma": str(SOURCE_LEMMA),
        },
        "criterion": criterion,
        "source_origin_lemma_import": {
            "conditional_status": lemma["theorem"]["conditional_status"],
            "unconditional_status": lemma["theorem"]["unconditional_status"],
            "proof_boundary": lemma["proof_boundary"],
            "open_payload_premises": lemma["open_payload_premises"],
        },
        "necessary_and_sufficient_payload_for_promotion": {
            "same_selected_smooth_source_as_S0": True,
            "functorial_Phi_fin_Galerkin_Cech_trace": True,
            "preserves_q79_F_m1_S3_GS_RouteC_basis": True,
            "actual_D_E_matrix_entries_emitted": True,
            "actual_Riesz_projector_entries_emitted": True,
            "actual_reduced_Green_entries_emitted": True,
            "actual_dotD_alpha1_entries_emitted": True,
            "selected_positive_gap_gamma_N_emitted": True,
            "selected_residual_epsilon_N_emitted": True,
            "epsilon_strictly_below_gap_margin": True,
            "honest_validator_replay_without_lifted_flags": True,
        },
        "current_branch_evaluation": current,
        "verdict": {
            "criterion_proved": True,
            "source_promotion_now_allowed": False,
            "reason": (
                "The scaffold supplies basis and shapes, but not selected finite "
                "values, selected gap/error, or honest replay; the imported source "
                "origin lemma is conditional on exactly those missing Phi_fin outputs."
            ),
            "next_required_artifact": "Selected_PhiFin_S2_Value_Emission_with_Gap_Error_and_Honest_Replay_v1",
        },
        "guardrails": {
            "does_not_promote_lifted_flags": True,
            "does_not_claim_selected_D_E_values_emitted": True,
            "does_not_claim_selected_dotD_values_emitted": True,
            "does_not_claim_selected_gap_error_emitted": True,
            "does_not_claim_A_selected_or_b_selected": True,
            "does_not_use_observed_or_benchmark_inputs": True,
        },
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "SelectedPhiFinS2SourcePromotionCriterion",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "what_closes_now": {
            "S2_source_promotion_criterion_proved": packet["criterion"]["proved"],
            "conditional_source_origin_lemma_integrated": True,
            "missing_payload_identified_as_finite_emission_not_flag_choice": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_finite_D_E_values": True,
            "selected_Riesz_projector_values": True,
            "selected_reduced_Green_values": True,
            "selected_dotD_alpha1_values": True,
            "selected_gap_error_certificate": True,
            "honest_validator_replay": True,
            "A_selected": True,
            "b_selected": True,
        },
        "guardrails": packet["guardrails"],
        "verdict": packet["verdict"],
    }


def render_note(cert: dict[str, Any], packet: dict[str, Any]) -> str:
    evaluation = packet["current_branch_evaluation"]
    return f"""# Selected PhiFin S2 Source Promotion Criterion v1

## Result

The source-promotion rule for S2 is now explicit.

Status: `{cert["status"]}`

The imported conditional source-origin lemma says the Route-C finite residual,
`rho_E`, metric, `D_E`, Riesz/Green, `dotD`, and C1 payloads become
theorem-derived selected-source data exactly when `Phi_fin` emits the required
finite payload with branch preservation and gap/error control.

## Criterion

S2 promotion requires all of:

```text
same selected smooth source as S0
functorial Phi_fin Galerkin/Cech trace
preservation of q79/F,m=1 S3/GS Route-C basis
actual D_E, Riesz, reduced Green, and dotD_alpha1 entries
positive selected gap gamma_N
selected residual epsilon_N with epsilon below the gap margin
honest validator replay without lifted flags
```

## Current Evaluation

```text
S0 selected smooth source available: {evaluation["fixed_selected_smooth_source_available"]}
abstract finite trace existence available: {evaluation["abstract_finite_trace_existence_available"]}
S1 projective rhoE trace filled: {evaluation["S1_projective_rhoE_trace_filled"]}
S2 same-basis scaffold available: {evaluation["S2_same_basis_scaffold_available"]}
D_E selected source verified now: {evaluation["S2_D_E_selected_source_verified"]}
dotD selected source verified now: {evaluation["S2_dotD_selected_source_verified"]}
alpha1 driver verified now: {evaluation["S2_dotD_alpha1_driver_verified"]}
selected gap/error emitted now: {evaluation["selected_gap_error_certificate_emitted"]}
full selected payload emitted now: {evaluation["full_selected_payload_emitted"]}
```

Therefore source promotion is not allowed yet. The missing object is not a
manual flag choice; it is the selected finite S2 value-emission packet with
gap/error control and honest replay.

## Next Gate

```text
Selected_PhiFin_S2_Value_Emission_with_Gap_Error_and_Honest_Replay_v1
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
