"""Build the selected PhiFin S2 A_sel,N form-bound interface."""

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

ETA_ATTEMPT = DATA / "selected_phifin_s2_eta_n_bound_or_source_flag_emission_attempt.candidate.json"
BRIDGE = DATA / "selected_phifin_s2_full_operator_error_bound_or_source_theorem.candidate.json"
SMOOTH_BN = SM / "candidate_data" / "selected_routec_smooth_bn_galerkin_lift.candidate.json"
DE_27_HONEST = (
    SM
    / "candidate_data"
    / "selected_routec_de_action_on_smooth_bn"
    / "de_action_on_smooth_bn.honest.json"
)
SMALL_SOLVE_SPEC = SM / "candidate_data" / "selected_routec_strominger_galerkin_solve_spec.candidate.json"
SMALL_SOLVE_DE = (
    SM / "candidate_data" / "selected_routec_strominger_galerkin_solve" / "de_action.candidate.json"
)

OUTPUT_PACKET = DATA / "selected_phifin_s2_a_sel_n_form_bound_interface.candidate.json"
OUTPUT_CERT = CERTS / "selected_phifin_s2_a_sel_n_form_bound_interface_certificate.json"
OUTPUT_NOTE = CORPUS / "Selected_PhiFin_S2_A_sel_N_Form_Bound_Interface_v1.md"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def matrix_shape(matrix: Any) -> list[int] | None:
    if not isinstance(matrix, list) or not matrix:
        return None
    if not all(isinstance(row, list) for row in matrix):
        return None
    return [len(matrix), len(matrix[0])]


def diagonal_values(matrix: list[list[float]]) -> list[float]:
    return [float(matrix[i][i]) for i in range(min(len(matrix), len(matrix[0])))]


def build_packet() -> dict[str, Any]:
    eta_attempt = load_json(ETA_ATTEMPT)
    bridge = load_json(BRIDGE)
    smooth = load_json(SMOOTH_BN)
    de_27 = load_json(DE_27_HONEST)
    small_spec = load_json(SMALL_SOLVE_SPEC)
    small_de = load_json(SMALL_SOLVE_DE)

    threshold = bridge["minimal_new_payload_to_close"]["eta_N_operator_norm_bound"]["threshold"]
    model_matrix = smooth["B_N_lift"]["stiffness_matrix_model_active_laplacian"]
    model_shape = matrix_shape(model_matrix)
    model_diag = diagonal_values(model_matrix)
    basis_id = smooth["B_N_lift"]["basis_id"]

    small_slot_shapes = {
        sector: matrix_shape(slot["stiffness_matrix"])
        for sector, slot in small_de["operator_slots"].items()
    }
    de_27_slot_shapes = {
        sector: matrix_shape(slot["stiffness_matrix"])
        for sector, slot in de_27["operator_slots"].items()
    }

    evaluated_payloads = {
        "small_strominger_galerkin_solve_de_action": {
            "path": str(SMALL_SOLVE_DE),
            "basis_id": small_de.get("basis_id"),
            "slot_stiffness_shapes": small_slot_shapes,
            "accepted_as_A_sel_N": False,
            "rejection_reason": (
                "The smoke solve has sector dimensions 2 or 4 and no matching "
                "27-mode B_N basis identity, so it cannot be compared to the "
                "27x27 A_model,N operator."
            ),
        },
        "smooth_BN_27_mode_DE_honest": {
            "path": str(DE_27_HONEST),
            "basis_id": de_27.get("basis_id"),
            "slot_stiffness_shapes": de_27_slot_shapes,
            "all_slots_27x27": all(shape == [27, 27] for shape in de_27_slot_shapes.values()),
            "selected_source_verified_all_sectors": all(
                bool(slot.get("selected_source_verified"))
                for slot in de_27["operator_slots"].values()
            ),
            "accepted_as_A_sel_N": False,
            "rejection_reason": (
                "The matrices are on the correct 27-mode basis but are explicitly "
                "unpromoted/model-active: selected_source_verified remains false "
                "in every sector."
            ),
        },
    }

    accepted_payload_schema = {
        "schema": "SelectedPhiFinS2ASelNFormBoundPayload.v1",
        "basis_id": basis_id,
        "dimension": 27,
        "one_of": {
            "explicit_operator": {
                "A_sel_N": "27x27 real symmetric or Hermitian matrix on B_N",
                "A_model_N": "the emitted model-active 27x27 stiffness matrix",
                "eta_N_computation": "certified operator norm of A_sel_N - A_model_N",
            },
            "form_bound": {
                "quadratic_form_bound": (
                    "for all normalized v in B_N, "
                    "|<v,(A_sel,N-A_model,N)v>| <= eta_N"
                ),
                "proof_source": "selected finite Phi_fin/Strominger trace",
            },
        },
        "required_provenance": {
            "same_selected_S0_source": True,
            "finite_Phi_fin_trace_morphism": True,
            "selected_connection_or_rhoE_values": True,
            "selected_source_flags_theorem_derived": True,
            "no_lifted_flags": True,
            "no_observed_or_benchmark_inputs": True,
        },
        "acceptance_rule": {
            "eta_N_threshold": threshold,
            "pass_if": "0 <= eta_N < eta_N_threshold",
            "then_closes": [
                "selected_gap_error_certificate",
                "selected_Riesz_projector_exists",
                "selected_reduced_Green_exists",
            ],
            "does_not_by_itself_close": [
                "finite_D_E_source_flags",
                "finite_dotD_source_flags",
                "alpha1_driver",
                "C1/Yukawa response",
            ],
        },
    }

    return {
        "packet": "Selected_PhiFin_S2_A_sel_N_Form_Bound_Interface_v1",
        "status": "A_SEL_N_FORM_BOUND_INTERFACE_BUILT_VALUES_OPEN",
        "inputs": {
            "eta_attempt": str(ETA_ATTEMPT.relative_to(ROOT)),
            "bridge": str(BRIDGE.relative_to(ROOT)),
            "smooth_BN": str(SMOOTH_BN),
            "DE_27_honest": str(DE_27_HONEST),
            "small_solve_spec": str(SMALL_SOLVE_SPEC),
            "small_solve_DE": str(SMALL_SOLVE_DE),
        },
        "A_model_N_summary": {
            "basis_id": basis_id,
            "dimension": model_shape[0],
            "shape": model_shape,
            "diagonal_operator": True,
            "zero_cluster_indices": smooth["B_N_lift"]["zero_cluster"]["indices"],
            "zero_cluster_dimension": smooth["B_N_lift"]["zero_cluster"]["dimension"],
            "complement_gap": smooth["B_N_lift"]["complement_gap"],
            "min_diagonal": min(model_diag),
            "max_diagonal": max(model_diag),
            "source_status": "model_active_not_selected",
        },
        "eta_threshold": threshold,
        "evaluated_existing_payloads": evaluated_payloads,
        "accepted_payload_schema": accepted_payload_schema,
        "current_closure": {
            "interface_built": True,
            "A_model_N_available": True,
            "A_sel_N_available": False,
            "eta_N_bound_available": False,
            "eta_N_threshold_passed": False,
            "selected_gap_error_closed": False,
            "selected_source_flags_promoted": False,
        },
        "negative_findings": {
            "small_solve_is_not_same_basis": True,
            "correct_basis_payload_is_unpromoted": True,
            "S0_source_prefix_not_enough": eta_attempt["source_flag_state"][
                "abstract_S0_selected_source_closed"
            ]
            and not eta_attempt["source_flag_state"]["finite_D_E_selected_source_verified"],
        },
        "guardrails": {
            "does_not_accept_dimension_mismatch": True,
            "does_not_accept_unpromoted_model_active_payload_as_A_sel_N": True,
            "does_not_claim_eta_N_computed": True,
            "does_not_promote_source_flags": True,
            "does_not_use_observed_or_benchmark_inputs": True,
        },
        "verdict": {
            "what_closes_now": (
                "The exact A_sel,N/form-bound interface is built. Existing "
                "candidate payloads are classified: the small Strominger solve is "
                "basis-incompatible, and the 27-mode matrices are unpromoted "
                "model-active data."
            ),
            "what_remains": (
                "Fill this interface with a selected 27x27 A_sel,N or a certified "
                "form bound eta_N from the finite Phi_fin/Strominger trace."
            ),
            "next_required_artifact": "Selected_PhiFin_S2_A_sel_N_Form_Bound_Fill_Attempt_v1",
        },
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "SelectedPhiFinS2ASelNFormBoundInterface",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "what_closes_now": {
            "A_sel_N_payload_schema_built": True,
            "A_model_N_summary_emitted": True,
            "eta_threshold_retained": True,
            "basis_incompatible_small_solve_rejected": True,
            "unpromoted_27_mode_payload_rejected": True,
        },
        "what_remains_open": {
            "A_sel_N": True,
            "eta_N_operator_norm_or_form_bound": True,
            "selected_gap_error_certificate": True,
            "source_flag_promotion": True,
            "honest_replay_without_lifted_flags": True,
        },
        "current_closure": packet["current_closure"],
        "verdict": packet["verdict"],
        "guardrails": packet["guardrails"],
    }


def render_note(cert: dict[str, Any], packet: dict[str, Any]) -> str:
    model = packet["A_model_N_summary"]
    schema = packet["accepted_payload_schema"]
    return f"""# Selected PhiFin S2 A_sel,N Form Bound Interface v1

## Result

Status: `{cert["status"]}`

The comparison interface is now explicit. The current model operator is:

```text
basis_id: {model["basis_id"]}
shape: {model["shape"]}
zero cluster indices: {model["zero_cluster_indices"]}
complement gap: {model["complement_gap"]}
eta threshold: {packet["eta_threshold"]}
```

## Accepted Payload

An accepted fill must provide either:

1. a selected `27 x 27` operator `A_sel,N` on the same `B_N` basis, with
   certified `||A_sel,N - A_model,N||_op`; or
2. a selected quadratic form bound proving
   `|<v,(A_sel,N-A_model,N)v>| <= eta_N` for all normalized `v` in `B_N`.

It passes only if:

```text
{schema["acceptance_rule"]["pass_if"]}
eta_N_threshold = {schema["acceptance_rule"]["eta_N_threshold"]}
```

## Existing Payload Classification

The small Strominger Galerkin solve is rejected because its sector dimensions
are 2 or 4, not the required 27-mode basis.

The 27-mode smooth `B_N` matrices are rejected as `A_sel,N` because their
selected-source flags remain false; they are model-active scaffold data, not
selected full-operator data.

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
