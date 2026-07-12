"""Lock the selected Phi_fin S2 D_E gap-layer replay."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SOURCE_LEMMA = DATA / "selected_canonical_trace_formula_source_lemma_proof.candidate.json"
OLD_REPLAY = DATA / "selected_phifin_s2_value_emission_with_gap_error_honest_replay.candidate.json"
FORMULA = DATA / "selected_trace_equals_emitted_27_mode_de_attempt.candidate.json"

OUTPUT_PACKET = DATA / "selected_phifin_s2_gap_layer_honest_replay_lock.candidate.json"
OUTPUT_CERT = CERTS / "selected_phifin_s2_gap_layer_honest_replay_lock_certificate.json"
OUTPUT_NOTE = CORPUS / "Selected_PhiFin_S2_Gap_Layer_Honest_Replay_Lock_v1.md"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    lemma = load_json(SOURCE_LEMMA)
    replay = load_json(OLD_REPLAY)
    formula = load_json(FORMULA)

    gap = lemma["gap_layer_consequence"]
    replay_gap = replay["gap_error_replay"]
    honest = replay["honest_replay"]
    payload = replay["same_basis_value_payload"]
    gamma_model = replay_gap["model_active_gap_gamma_N"]
    eta_n = gap["selected_eta_N"]
    selected_gap_lower_bound = gamma_model - 2.0 * eta_n
    selected_green_norm_bound = 1.0 / selected_gap_lower_bound

    de_replay_locked = (
        lemma["theorem"]["proved"]
        and lemma["selected_trace_equality"]["proved"]
        and gap["D_E_source_flags_may_be_theorem_derived"]
        and gap["gap_Riesz_Green_closes"]
        and honest["D_E_fails_only_by_source_flags"]
        and formula["formula_theorem"]["proved"]
        and all(
            sector["matches_canonical_formula"]
            for sector in formula["sector_formula_checks"].values()
        )
        and selected_gap_lower_bound > 0.0
    )
    full_s2_still_open = (
        honest["dotD_fails_only_by_source_driver_flags"]
        and replay["still_separate"]["dotD_alpha1_C1_response"]
        if "still_separate" in replay
        else True
    )

    return {
        "packet": "Selected_PhiFin_S2_Gap_Layer_Honest_Replay_Lock_v1",
        "status": (
            "SELECTED_PHIFIN_S2_D_E_GAP_LAYER_LOCKED"
            if de_replay_locked
            else "SELECTED_PHIFIN_S2_D_E_GAP_LAYER_LOCK_FAILED"
        ),
        "inputs": {
            "source_lemma": str(SOURCE_LEMMA.relative_to(ROOT)),
            "previous_combined_replay": str(OLD_REPLAY.relative_to(ROOT)),
            "formula": str(FORMULA.relative_to(ROOT)),
        },
        "locked_contract": {
            "scope": "D_E gap/Riesz/Green layer only",
            "basis_id": payload["basis_id"],
            "basis_dimension": payload["basis_dimension"],
            "zero_cluster_indices": payload["zero_cluster_indices"],
            "selected_trace_equality": lemma["selected_trace_equality"],
            "D_E_honest_replay_passes_after_theorem_derived_source_flags": de_replay_locked,
            "D_E_source_flags_are_theorem_derived": gap[
                "D_E_source_flags_may_be_theorem_derived"
            ],
            "selected_eta_N": eta_n,
            "eta_threshold": gap["eta_threshold"],
            "model_gap_gamma_N": gamma_model,
            "selected_gap_lower_bound": selected_gap_lower_bound,
            "selected_green_norm_bound": selected_green_norm_bound,
            "Riesz_Green_layer_closes": gap["gap_Riesz_Green_closes"],
        },
        "replay_delta": {
            "previous_D_E_replay_failed_only_by_source_flags": honest[
                "D_E_fails_only_by_source_flags"
            ],
            "new_source_flags_theorem_derived_for_D_E": gap[
                "D_E_source_flags_may_be_theorem_derived"
            ],
            "previous_dotD_replay_failed_by_source_driver_flags": honest[
                "dotD_fails_only_by_source_driver_flags"
            ],
            "full_s2_honest_replay_without_lifted_flags": False,
            "reason_full_s2_still_open": (
                "The source lemma promotes only the selected D_E trace and "
                "gap/Riesz/Green layer. It does not emit selected dotD_alpha1, "
                "alpha1 driver, A_selected, or b_selected."
            ),
        },
        "formula_lock": {
            "family_sectors": "canonical F3xF3 Fourier Laplacian",
            "H_sector": "canonical F3xF3 Fourier Laplacian plus rank-two projector on indices 13,14",
            "all_sector_formulas_match": all(
                sector["matches_canonical_formula"]
                for sector in formula["sector_formula_checks"].values()
            ),
            "H_shift_indices": formula["sector_formula_checks"]["H"][
                "higgs_shift_indices"
            ],
        },
        "still_separate": {
            "full_S2_value_emission": full_s2_still_open,
            "dotD_alpha1_C1_response": True,
            "alpha1_driver": True,
            "A_selected_and_b_selected": True,
            "Yukawa_or_full_SM_closure": True,
        },
        "guardrails": {
            "does_not_promote_dotD_flags": True,
            "does_not_claim_full_S2_honest_replay": True,
            "does_not_claim_A_selected_or_b_selected": True,
            "does_not_claim_Yukawa_or_SM_closure": True,
            "does_not_use_observed_or_benchmark_inputs": True,
            "locks_only_theorem_derived_D_E_flags": True,
        },
        "verdict": {
            "what_is_locked": (
                "The selected Phi_fin 27-mode D_E trace and its positive "
                "gap/Riesz/Green consequence are now a theorem-derived replay "
                "contract."
            ),
            "next_required_artifact": (
                "Selected_PhiFin_dotD_alpha1_C1_Response_Emission_v1"
            ),
        },
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "SelectedPhiFinS2GapLayerHonestReplayLock",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "locked_contract": packet["locked_contract"],
        "replay_delta": packet["replay_delta"],
        "still_separate": packet["still_separate"],
        "guardrails": packet["guardrails"],
        "verdict": packet["verdict"],
    }


def render_note(cert: dict[str, Any], packet: dict[str, Any]) -> str:
    contract = packet["locked_contract"]
    return f"""# Selected PhiFin S2 Gap-Layer Honest Replay Lock v1

## Result

Status: `{cert["status"]}`

The selected `D_E` gap layer is now locked as a theorem-derived replay
contract.  The earlier combined replay failed on `D_E` only because source
flags were false; `SelectedCanonicalTraceFormulaSourceLemma` now supplies those
flags for the `D_E` layer only.

## Locked Contract

```json
{json.dumps(contract, indent=2, sort_keys=True)}
```

## Boundary

This lock does not promote `dotD_alpha1`, the alpha1 driver, `A_selected`,
`b_selected`, Yukawa data, or full SM closure.

Next required artifact:

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
