"""Build the PhiFin S2 full-operator error-bound/source theorem gate."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PREVIOUS_PACKET = (
    DATA / "selected_phifin_s2_selected_operator_and_truncation_source_theorem_attempt.candidate.json"
)
VALUE_REPLAY_PACKET = (
    DATA / "selected_phifin_s2_value_emission_with_gap_error_honest_replay.candidate.json"
)

OUTPUT_PACKET = (
    DATA / "selected_phifin_s2_full_operator_error_bound_or_source_theorem.candidate.json"
)
OUTPUT_CERT = (
    CERTS / "selected_phifin_s2_full_operator_error_bound_or_source_theorem_certificate.json"
)
OUTPUT_NOTE = (
    CORPUS / "Selected_PhiFin_S2_Full_Operator_Error_Bound_or_Source_Theorem_v1.md"
)


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load_json(PREVIOUS_PACKET)
    replay = load_json(VALUE_REPLAY_PACKET)
    gamma_model = float(previous["selected_truncation_status"]["model_active_gamma_N"])
    epsilon_model = float(previous["selected_truncation_status"]["model_active_epsilon_N"])
    strict_half_gap = gamma_model / 2.0
    conservative_eta_budget = strict_half_gap - epsilon_model

    conditional_bridge = {
        "name": "FiniteSelfAdjointGapStabilityBridge",
        "proved": True,
        "statement": (
            "Let A0 be the verified 27-mode self-adjoint model-active stiffness "
            "operator with zero cluster separated from the complement by "
            "gamma_model > 0. Let A_sel,N be the selected full "
            "Iwasawa/Strominger operator compressed to the same B_N basis, and "
            "let eta_N = ||A_sel,N - A0||_op. If epsilon_N + eta_N < "
            "gamma_model / 2, then the selected zero-cluster Riesz contour is "
            "stable, the selected complement gap is at least "
            "gamma_model - 2(eta_N + epsilon_N), and the reduced Green operator "
            "exists on the selected complement."
        ),
        "method": (
            "Finite-dimensional min-max/Weyl spectral perturbation plus the "
            "Riesz-contour resolvent identity. No observed constants, benchmark "
            "masses, or fitted target data enter the condition."
        ),
    }

    source_route = {
        "name": "SelectedSourcePromotionRoute",
        "proved": False,
        "sufficient_if_supplied": {
            "selected_connection_formula": True,
            "same_B_N_compression_identity": True,
            "selected_DE_source_flags": True,
            "selected_dotD_source_and_alpha1_driver_flags": True,
            "honest_replay_without_lifted_flags": True,
        },
        "why_open": (
            "The previous theorem attempt shows that I3/I4/I5 paper slots remain "
            "source obligations, not derived flags."
        ),
    }

    error_bound_route = {
        "name": "OperatorErrorBoundRoute",
        "proved": False,
        "required_bound": "eta_N + epsilon_N < gamma_model / 2",
        "current_eta_N": None,
        "current_epsilon_N": epsilon_model,
        "gamma_model": gamma_model,
        "strict_eta_budget": conservative_eta_budget,
        "strict_eta_budget_decimal": conservative_eta_budget,
        "if_eta_supplied_below_budget_then": {
            "selected_gap_lower_bound_formula": "gamma_model - 2*(eta_N + epsilon_N)",
            "selected_Riesz_projector_exists": True,
            "selected_reduced_Green_exists": True,
            "selected_gap_error_certificate_emitted": True,
        },
        "why_open": (
            "No corpus artifact emits eta_N = ||A_sel,N - A_model,N||_op or an "
            "equivalent form-bound for the selected full operator."
        ),
    }

    return {
        "packet": "Selected_PhiFin_S2_Full_Operator_Error_Bound_or_Source_Theorem_v1",
        "status": "CONDITIONAL_OPERATOR_BRIDGE_PROVED_NUMERIC_ETA_SOURCE_OPEN",
        "inputs": {
            "previous_selected_operator_attempt": str(PREVIOUS_PACKET.relative_to(ROOT)),
            "value_replay_packet": str(VALUE_REPLAY_PACKET.relative_to(ROOT)),
        },
        "model_gap_data": {
            "gamma_model": gamma_model,
            "epsilon_model": epsilon_model,
            "strict_half_gap_budget": strict_half_gap,
            "strict_eta_budget_after_epsilon": conservative_eta_budget,
            "model_gap_positive": gamma_model > 0,
            "model_epsilon_below_half_gap": epsilon_model < strict_half_gap,
        },
        "conditional_bridge_theorem": conditional_bridge,
        "two_sufficient_closure_routes": {
            "route_A_source_theorem": source_route,
            "route_B_operator_error_bound": error_bound_route,
        },
        "current_closure_evaluation": {
            "conditional_bridge_closed": True,
            "selected_source_route_closed": False,
            "operator_error_bound_route_closed": False,
            "selected_S2_gap_error_closed": False,
            "honest_replay_promoted": False,
            "selected_value_emission_closed": False,
        },
        "minimal_new_payload_to_close": {
            "eta_N_operator_norm_bound": {
                "required": True,
                "threshold": conservative_eta_budget,
                "accepted_if": "0 <= eta_N < strict_eta_budget_after_epsilon",
            },
            "or_selected_source_theorem": {
                "required": True,
                "slots": ["I3", "I4", "I5"],
            },
            "same_basis_identity": "A_sel,N and A_model,N must be compared on B_N = F3xF3_gerbe_twisted_fourier_N1_rank3",
        },
        "verdict": {
            "what_closes_now": (
                "The rigorous perturbation bridge and exact numeric acceptance "
                "budget close. The missing proof is reduced to a single operator "
                "norm/form-bound eta_N or, alternatively, a source theorem for "
                "I3/I4/I5."
            ),
            "selected_full_operator_theorem_proved_unconditionally": False,
            "next_required_artifact": "Selected_PhiFin_S2_Eta_N_Bound_or_Source_Flag_Emission_v1",
        },
        "guardrails": {
            "does_not_claim_eta_N_emitted": True,
            "does_not_claim_selected_gap_error_closed": True,
            "does_not_promote_source_flags": True,
            "does_not_use_observed_or_benchmark_inputs": True,
            "does_not_relabel_model_active_as_selected": True,
        },
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "SelectedPhiFinS2FullOperatorErrorBoundOrSourceTheorem",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "what_closes_now": {
            "finite_self_adjoint_gap_stability_bridge": True,
            "exact_eta_budget_computed": True,
            "single_numeric_operator_bound_gate_identified": True,
            "source_theorem_alternative_identified": True,
        },
        "what_remains_open": {
            "eta_N_operator_norm_or_form_bound": True,
            "selected_source_flags": True,
            "selected_gap_error_certificate": True,
            "honest_replay_without_lifted_flags": True,
            "selected_value_emission": True,
        },
        "verdict": packet["verdict"],
        "guardrails": packet["guardrails"],
    }


def render_note(cert: dict[str, Any], packet: dict[str, Any]) -> str:
    gap = packet["model_gap_data"]
    route_b = packet["two_sufficient_closure_routes"]["route_B_operator_error_bound"]
    return f"""# Selected PhiFin S2 Full Operator Error Bound or Source Theorem v1

## Result

Status: `{cert["status"]}`

This theorem gate closes the abstract perturbation step, but not the selected
full-operator theorem itself.

The current 27-mode model has a positive complement gap. Therefore a selected
full operator compressed to the same `B_N` basis may be promoted if the missing
operator error bound is small enough.

```text
gamma_model = {gap["gamma_model"]}
epsilon_model = {gap["epsilon_model"]}
strict half-gap budget = {gap["strict_half_gap_budget"]}
strict eta budget after epsilon = {gap["strict_eta_budget_after_epsilon"]}
```

## Conditional Theorem

If

```text
eta_N + epsilon_N < gamma_model / 2
```

where `eta_N = ||A_sel,N - A_model,N||_op`, then the selected Riesz contour is
stable, the selected complement gap is bounded below by

```text
gamma_selected >= gamma_model - 2*(eta_N + epsilon_N)
```

and the selected reduced Green operator exists.

## What This Changes

The remaining obstruction is now one of two sharply typed payloads:

1. source theorem route: derive I3/I4/I5 and emit theorem-derived selected
   source flags;
2. operator-bound route: emit an `eta_N` bound satisfying
   `{route_b["required_bound"]}`.

The current strict budget is:

```text
eta_N < {route_b["strict_eta_budget"]}
```

No such `eta_N` has been emitted yet, so selected value emission and honest
replay remain open.

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
