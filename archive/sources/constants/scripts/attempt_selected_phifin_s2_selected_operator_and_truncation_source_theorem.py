"""Attempt the selected S2 operator/truncation source theorem."""

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
GR = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-protospinor-gr-response-proof")

VALUE_REPLAY_CERT = (
    CERTS / "selected_phifin_s2_value_emission_with_gap_error_honest_replay_certificate.json"
)
VALUE_REPLAY_PACKET = (
    DATA / "selected_phifin_s2_value_emission_with_gap_error_honest_replay.candidate.json"
)
SCAFFOLD_IMPORT = GR / "candidate_data" / "routec_smooth_bn_galerkin_lift_import.packet.json"
SOURCE_MANIFEST = SM / "candidate_data" / "selected_source_paper_integration_manifest.candidate.json"
SMOOTH_BN = SM / "candidate_data" / "selected_routec_smooth_bn_galerkin_lift.candidate.json"
DE_ACTION = SM / "candidate_data" / "selected_routec_de_action_on_smooth_bn.candidate.json"
DOTD = SM / "candidate_data" / "selected_routec_sector_projectors_dotd_on_smooth_bn.candidate.json"

OUTPUT_PACKET = (
    DATA / "selected_phifin_s2_selected_operator_and_truncation_source_theorem_attempt.candidate.json"
)
OUTPUT_CERT = (
    CERTS / "selected_phifin_s2_selected_operator_and_truncation_source_theorem_attempt_certificate.json"
)
OUTPUT_NOTE = (
    CORPUS / "Selected_PhiFin_S2_Selected_Operator_and_Truncation_Source_Theorem_Attempt_v1.md"
)


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def manifest_insertions_by_id(manifest: dict[str, Any]) -> dict[str, Any]:
    return {item["id"]: item for item in manifest["insertions"]}


def build_packet() -> dict[str, Any]:
    replay_cert = load_json(VALUE_REPLAY_CERT)
    replay_packet = load_json(VALUE_REPLAY_PACKET)
    scaffold = load_json(SCAFFOLD_IMPORT)
    manifest = load_json(SOURCE_MANIFEST)
    smooth_bn = load_json(SMOOTH_BN)
    de_action = load_json(DE_ACTION)
    dotd = load_json(DOTD)
    insertions = manifest_insertions_by_id(manifest)

    model_gap = replay_packet["gap_error_replay"]["model_active_gap_gamma_N"]
    model_epsilon = replay_packet["gap_error_replay"]["model_active_residual_epsilon_N"]
    honest = replay_packet["honest_replay"]

    theorem_attempt = {
        "name": "SelectedPhiFinS2SelectedOperatorAndTruncationSourceTheorem",
        "target_statement": (
            "The emitted 27-mode B_N D_E/Riesz/Green/dotD payload is the selected "
            "full Iwasawa/Strominger Phi_fin trace, with a selected truncation "
            "bound epsilon_N strictly below the selected spectral gap gamma_N; "
            "therefore the S2 source flags and honest replay are theorem-derived."
        ),
        "proved": False,
        "refutation_reason": (
            "Current artifacts prove a model-active finite scaffold and diagnostic "
            "validator consistency, but they explicitly leave the full selected "
            "Iwasawa/Strominger operator, truncation error, and theorem-derived "
            "source/alpha1 flags open."
        ),
    }

    current_evidence = {
        "same_basis_27_mode_payload": replay_cert["what_closes_now"][
            "same_basis_27_mode_value_payload_located"
        ],
        "model_active_gap_positive": model_gap > 0,
        "model_active_epsilon_below_gap": model_epsilon < model_gap,
        "D_E_honest_replay_fails_only_source_flags": honest["D_E_fails_only_by_source_flags"],
        "dotD_honest_replay_fails_only_source_driver_flags": honest[
            "dotD_fails_only_by_source_driver_flags"
        ],
        "D_E_diagnostic_lift_passes": honest["D_E_diagnostic_lift_passes"],
        "dotD_diagnostic_lift_passes": honest["dotD_diagnostic_lift_passes"],
        "target_fitting_excluded": replay_cert["what_closes_now"]["target_fitting_excluded"],
    }

    blockers = {
        "I3_smooth_BN_convergence_and_truncation": {
            "paper_slot_status": insertions["I3_smooth_bn_galerkin_lift_theorem"]["status"],
            "safe_wording": insertions["I3_smooth_bn_galerkin_lift_theorem"]["safe_wording"],
            "missing_obligations": insertions["I3_smooth_bn_galerkin_lift_theorem"][
                "proof_obligations"
            ],
            "current_artifact_says_open": scaffold["still_open_checks"][
                "full_iwasawa_truncation_error_open"
            ],
        },
        "I4_selected_D_E_action_and_source_flags": {
            "paper_slot_status": insertions["I4_selected_DE_action_and_source_flags"]["status"],
            "safe_wording": insertions["I4_selected_DE_action_and_source_flags"]["safe_wording"],
            "missing_obligations": insertions["I4_selected_DE_action_and_source_flags"][
                "proof_obligations"
            ],
            "honest_D_E_promotes": de_action["validation"]["honest"]["exit_code"] == 0,
        },
        "I5_dotD_alpha1_source_and_C1_response": {
            "paper_slot_status": insertions["I5_dotD_alpha1_and_C1_response"]["status"],
            "safe_wording": insertions["I5_dotD_alpha1_and_C1_response"]["safe_wording"],
            "missing_obligations": insertions["I5_dotD_alpha1_and_C1_response"][
                "proof_obligations"
            ],
            "honest_dotD_promotes": dotd["validation"]["honest"]["exit_code"] == 0,
        },
    }

    required_payload = {
        "selected_smooth_operator_formula": "OPEN",
        "proof_27_mode_BN_is_N1_truncation_of_selected_operator": "OPEN",
        "operator_difference_bound_full_minus_model_active": "OPEN",
        "selected_gamma_N": "OPEN",
        "selected_epsilon_N": "OPEN",
        "proof_epsilon_N_below_gamma_margin": "OPEN",
        "theorem_derived_selected_source_flags": "OPEN",
        "honest_replay_passes_without_lifted_flags": "OPEN",
    }

    return {
        "packet": "Selected_PhiFin_S2_Selected_Operator_and_Truncation_Source_Theorem_Attempt_v1",
        "status": "SELECTED_PHIFIN_S2_SELECTED_OPERATOR_TRUNCATION_THEOREM_ATTEMPT_BLOCKED",
        "inputs": {
            "local_value_replay_certificate": str(VALUE_REPLAY_CERT.relative_to(ROOT)),
            "local_value_replay_packet": str(VALUE_REPLAY_PACKET.relative_to(ROOT)),
            "GR_smooth_BN_scaffold_import": str(SCAFFOLD_IMPORT),
            "SM_source_paper_integration_manifest": str(SOURCE_MANIFEST),
            "SM_smooth_BN_candidate": str(SMOOTH_BN),
            "SM_DE_action_candidate": str(DE_ACTION),
            "SM_dotD_candidate": str(DOTD),
        },
        "theorem_attempt": theorem_attempt,
        "current_evidence": current_evidence,
        "blockers": blockers,
        "selected_truncation_status": {
            "model_active_gamma_N": model_gap,
            "model_active_epsilon_N": model_epsilon,
            "model_active_gap_condition_passes": model_epsilon < model_gap,
            "selected_gamma_N": None,
            "selected_epsilon_N": None,
            "selected_gap_condition_passes": False,
            "why_model_gap_cannot_be_relabelled_selected": (
                "The model-active diagonal stiffness is a scaffold operator. The "
                "selected full Iwasawa/Strominger D_E and the norm bound between "
                "the full operator and this finite model have not been emitted."
            ),
        },
        "minimal_payload_to_close": required_payload,
        "verdict": {
            "selected_operator_truncation_theorem_proved": False,
            "selected_S2_value_emission_may_be_promoted": False,
            "negative_result_proved": True,
            "reason": (
                "Existing artifacts are sufficient for a rigorous model-active "
                "finite replay, but not for selected full-operator provenance. "
                "Promotion would require proving the I3/I4/I5 paper-theorem slots."
            ),
            "next_required_artifact": "Selected_PhiFin_S2_Full_Operator_Error_Bound_or_Source_Theorem_v1",
        },
        "guardrails": {
            "does_not_relabel_model_active_as_selected": True,
            "does_not_promote_lifted_flags": True,
            "does_not_claim_selected_truncation_error": True,
            "does_not_claim_honest_replay_passes": True,
            "does_not_claim_A_selected_or_b_selected": True,
            "does_not_use_observed_or_benchmark_inputs": True,
        },
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "SelectedPhiFinS2SelectedOperatorAndTruncationSourceTheoremAttempt",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "what_closes_now": {
            "theorem_attempt_executed": True,
            "model_active_gap_noted_as_insufficient_for_selected_gap": True,
            "I3_I4_I5_source_obligations_identified": True,
            "promotion_from_current_corpus_refuted": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_full_iwasawa_strominger_operator_formula": True,
            "selected_27_mode_truncation_theorem": True,
            "full_minus_model_operator_norm_bound": True,
            "selected_gap_error_certificate": True,
            "theorem_derived_selected_source_flags": True,
            "honest_replay_without_lifted_flags": True,
            "A_selected": True,
            "b_selected": True,
        },
        "verdict": packet["verdict"],
        "guardrails": packet["guardrails"],
    }


def render_note(cert: dict[str, Any], packet: dict[str, Any]) -> str:
    trunc = packet["selected_truncation_status"]
    return f"""# Selected PhiFin S2 Selected Operator and Truncation Source Theorem Attempt v1

## Result

The selected full-operator/truncation theorem was attempted and is blocked by
explicit source obligations.

Status: `{cert["status"]}`

This is a negative but useful theorem attempt. The current corpus proves a
same-basis 27-mode model-active replay with a positive model gap, but it does
not prove that the model-active operator is the selected full
Iwasawa/Strominger `D_E` trace.

## Current Gap Data

```text
model-active gamma_N: {trunc["model_active_gamma_N"]}
model-active epsilon_N: {trunc["model_active_epsilon_N"]}
model-active epsilon < gamma: {trunc["model_active_gap_condition_passes"]}
selected gamma_N: {trunc["selected_gamma_N"]}
selected epsilon_N: {trunc["selected_epsilon_N"]}
selected gap condition passes: {trunc["selected_gap_condition_passes"]}
```

The model-active gap cannot be relabelled selected because the selected full
operator and the full-minus-model norm bound have not been emitted.

## Blocking Theorem Slots

- `I3_smooth_bn_galerkin_lift_theorem`: prove smooth `B_N` convergence and
  full Iwasawa/Strominger truncation error.
- `I4_selected_DE_action_and_source_flags`: derive `D_E` from the selected
  connection and prove the 27-mode matrix is its N=1 truncation.
- `I5_dotD_alpha1_and_C1_response`: derive same-branch `alpha1`, selected
  `dotD`, horizontal response, and overlap/C1 data.

## Verdict

Selected S2 value emission cannot be promoted from the current corpus alone.
The next real artifact must supply either a full operator error bound or a
source theorem deriving those three theorem slots.

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
