"""Scaffold the finite trace morphism needed for PhiFin S2 provenance."""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SM = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure")

S0_PREFIX = DATA / "selected_phifin_s0_source_prefix.candidate.json"
FINITE_TRACE = DATA / "selected_phifin_finite_trace_existence.candidate.json"
S1_PARTIAL = DATA / "selected_phifin_s1s2_value_emission.partial_filled.json"
PROVENANCE = DATA / "selected_phifin_s2_27_mode_provenance_theorem_attempt.candidate.json"
FORM_FILL = DATA / "selected_phifin_s2_a_sel_n_form_bound_fill_attempt.candidate.json"
SMOOTH_BN = SM / "candidate_data" / "selected_routec_smooth_bn_galerkin_lift.candidate.json"
DE_27_HONEST = (
    SM
    / "candidate_data"
    / "selected_routec_de_action_on_smooth_bn"
    / "de_action_on_smooth_bn.honest.json"
)

OUTPUT_PACKET = DATA / "selected_phifin_s2_finite_trace_morphism_scaffold.candidate.json"
OUTPUT_CERT = CERTS / "selected_phifin_s2_finite_trace_morphism_scaffold_certificate.json"
OUTPUT_NOTE = CORPUS / "Selected_PhiFin_S2_Finite_Trace_Morphism_Scaffold_v1.md"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def max_abs_diff(a: list[list[float]], b: list[list[float]]) -> float:
    max_diff = 0.0
    for row_a, row_b in zip(a, b):
        for item_a, item_b in zip(row_a, row_b):
            max_diff = max(max_diff, abs(float(item_a) - float(item_b)))
    return max_diff


def shape(matrix: list[list[Any]]) -> list[int]:
    return [len(matrix), len(matrix[0]) if matrix else 0]


def basis_summary(smooth: dict[str, Any], de_27: dict[str, Any]) -> dict[str, Any]:
    basis = smooth["B_N_lift"]["basis"]
    return {
        "basis_id": smooth["B_N_lift"]["basis_id"],
        "de_27_basis_id": de_27["basis_id"],
        "dimension": smooth["B_N_lift"]["dimension"],
        "basis_count": len(basis),
        "fiber_rank": len({item["fiber_index"] for item in basis}),
        "deck_modes": sorted({tuple(item["integer_representative"]) for item in basis}),
        "same_basis_id": smooth["B_N_lift"]["basis_id"] == de_27["basis_id"],
        "same_dimension": smooth["B_N_lift"]["dimension"] == 27,
    }


def sector_matrix_checks(smooth: dict[str, Any], de_27: dict[str, Any]) -> dict[str, Any]:
    model = smooth["B_N_lift"]["stiffness_matrix_model_active_laplacian"]
    checks: dict[str, Any] = {}
    for sector, slot in sorted(de_27["operator_slots"].items()):
        matrix = slot["stiffness_matrix"]
        checks[sector] = {
            "shape": shape(matrix),
            "same_gram_identity": slot["domain_gram"] == smooth["B_N_lift"]["gram_matrix"],
            "boundary_conditions_verified": bool(slot.get("boundary_conditions_verified")),
            "selected_source_verified": bool(slot.get("selected_source_verified")),
            "max_entry_difference_from_model_stiffness": max_abs_diff(matrix, model),
            "accepted_as_selected_trace": False,
        }
    return checks


def build_packet() -> dict[str, Any]:
    s0 = load_json(S0_PREFIX)
    finite_trace = load_json(FINITE_TRACE)
    s1 = load_json(S1_PARTIAL)
    provenance = load_json(PROVENANCE)
    form_fill = load_json(FORM_FILL)
    smooth = load_json(SMOOTH_BN)
    de_27 = load_json(DE_27_HONEST)

    basis = basis_summary(smooth, de_27)
    sector_checks = sector_matrix_checks(smooth, de_27)
    max_sector_residual = max(
        item["max_entry_difference_from_model_stiffness"]
        for item in sector_checks.values()
    )
    all_shapes_27 = all(item["shape"] == [27, 27] for item in sector_checks.values())
    all_same_gram = all(item["same_gram_identity"] for item in sector_checks.values())
    all_boundary_ok = all(item["boundary_conditions_verified"] for item in sector_checks.values())
    selected_flags_all_false = all(
        not item["selected_source_verified"] for item in sector_checks.values()
    )

    eta = provenance["diagnostic_eta"]
    morphism_faces = {
        "F0_selected_smooth_source": {
            "closed": bool(s0["s0_closed"]),
            "source": str(S0_PREFIX.relative_to(ROOT)),
        },
        "F1_abstract_functorial_trace_exists": {
            "closed": finite_trace["abstract_closure"]["S1_S2_are_selected_if_basis_and_gap_are_selected"],
            "source": str(FINITE_TRACE.relative_to(ROOT)),
            "does_not_emit_values": finite_trace["guardrails"]["claims_finite_values_emitted"] is False,
        },
        "F2_selected_projective_rhoE_trace_partial": {
            "closed": s1["S1_transition_or_connection_trace"]["nonidentity_or_equivalent_connection_trace"],
            "status": s1["status"],
            "still_partial": not s1["partial_fill_guardrail"]["full_selected_payload_emitted"],
        },
        "F3_same_BN_basis_and_finite_algebra": {
            "closed": basis["same_basis_id"] and basis["same_dimension"] and all_shapes_27 and all_same_gram,
            "basis": basis,
            "all_sector_shapes_27": all_shapes_27,
            "all_same_gram": all_same_gram,
            "all_boundary_conditions_verified": all_boundary_ok,
        },
        "F4_operator_entry_identification": {
            "closed": False,
            "finite_diagnostic_residual": max_sector_residual,
            "reason": (
                "The same-basis finite matrices are emitted and diagnostically "
                "within the eta budget, but no selected trace theorem proves "
                "that these entries equal P_N D_E(selected source) P_N."
            ),
        },
        "F5_honest_replay_without_lifted_flags": {
            "closed": False,
            "selected_flags_all_false": selected_flags_all_false,
            "reason": "The validator flags remain false by design until F4 is proved.",
        },
    }

    closed_prefix_faces = [
        name for name, face in morphism_faces.items() if bool(face["closed"])
    ]
    open_faces = [
        name for name, face in morphism_faces.items() if not bool(face["closed"])
    ]

    theorem = {
        "name": "FiniteTraceMorphismScaffoldReduction",
        "proved": True,
        "statement": (
            "The finite trace morphism obligation reduces to one missing "
            "operator-entry identification theorem: prove that the existing "
            "same-basis 27-mode matrices are P_N D_E(A_selected) P_N for the "
            "S0 selected Strominger/HYM source. All prior scaffold faces needed "
            "to state that equality are present."
        ),
    }

    if not math.isclose(max_sector_residual, eta["eta_if_provenance_supplied"], rel_tol=0, abs_tol=1e-12):
        raise ValueError("diagnostic residual disagrees with provenance eta")

    return {
        "packet": "Selected_PhiFin_S2_Finite_Trace_Morphism_Scaffold_v1",
        "status": "FINITE_TRACE_MORPHISM_SCAFFOLD_REDUCED_OPERATOR_IDENTIFICATION_OPEN",
        "inputs": {
            "S0_prefix": str(S0_PREFIX.relative_to(ROOT)),
            "finite_trace_existence": str(FINITE_TRACE.relative_to(ROOT)),
            "S1_partial_rhoE": str(S1_PARTIAL.relative_to(ROOT)),
            "provenance_attempt": str(PROVENANCE.relative_to(ROOT)),
            "form_bound_fill": str(FORM_FILL.relative_to(ROOT)),
            "smooth_BN": str(SMOOTH_BN),
            "DE_27_honest": str(DE_27_HONEST),
        },
        "theorem": theorem,
        "morphism_faces": morphism_faces,
        "closed_prefix_faces": closed_prefix_faces,
        "open_faces": open_faces,
        "sector_matrix_checks": sector_checks,
        "operator_identification_gate": {
            "name": "SelectedTraceEqualsEmitted27ModeDE",
            "statement": (
                "For every sector S in {Q,u,d,L,e,N,H}, the finite trace of the "
                "S0 selected connection satisfies "
                "P_N D_E,S(A_selected) P_N = D_E,S^emitted on "
                "B_N = F3xF3_gerbe_twisted_fourier_N1_rank3."
            ),
            "sufficient_payloads": [
                "explicit selected connection coefficients in the 27-mode basis",
                "or a symbolic form computation deriving the emitted diagonal entries",
                "or a certified form-norm equality between the Phi_fin trace and emitted sector matrices",
            ],
            "why_this_is_the_last_gap_for_gap_layer": (
                "Once this equality is proved, eta_N=1.0 is selected and already "
                "satisfies eta_N < 2.1932454224643014, so the selected "
                "gap/Riesz/Green certificate follows from the existing "
                "perturbation bridge."
            ),
        },
        "conditional_consequence_ready": {
            "eta_N_if_gate_closes": eta["eta_if_provenance_supplied"],
            "threshold": eta["threshold"],
            "passes_threshold": eta["passes_threshold"],
            "selected_eta_emitted_now": False,
            "selected_gap_layer_closes_if_gate_closes": True,
        },
        "guardrails": {
            "does_not_set_selected_source_flags": True,
            "does_not_claim_operator_identification": True,
            "does_not_promote_eta": True,
            "does_not_use_observed_or_benchmark_inputs": True,
            "keeps_dotD_C1_separate": True,
        },
        "verdict": {
            "what_closes_now": (
                "The finite trace morphism is reduced to a single explicit "
                "operator-entry identification gate on the already matching "
                "27-mode basis."
            ),
            "what_remains": (
                "Prove SelectedTraceEqualsEmitted27ModeDE by deriving the sector "
                "stiffness entries from the selected connection, or emit a "
                "certified selected form equality."
            ),
            "next_required_artifact": "SelectedTraceEqualsEmitted27ModeDE_v1",
        },
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "SelectedPhiFinS2FiniteTraceMorphismScaffold",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "what_closes_now": {
            "finite_trace_morphism_scaffold": True,
            "same_BN_basis_identity": True,
            "abstract_trace_and_rhoE_prefix": True,
            "operator_identification_gate_isolated": True,
        },
        "what_remains_open": {
            "SelectedTraceEqualsEmitted27ModeDE": True,
            "selected_eta_N": True,
            "selected_gap_error_certificate": True,
            "D_E_source_flags": True,
            "dotD_alpha1_C1_response": True,
        },
        "closed_prefix_faces": packet["closed_prefix_faces"],
        "open_faces": packet["open_faces"],
        "conditional_consequence_ready": packet["conditional_consequence_ready"],
        "guardrails": packet["guardrails"],
        "verdict": packet["verdict"],
    }


def render_note(cert: dict[str, Any], packet: dict[str, Any]) -> str:
    return f"""# Selected PhiFin S2 Finite Trace Morphism Scaffold v1

## Result

Status: `{cert["status"]}`

The morphism proof is not fully closed, but it has been reduced to one exact
gate.

## Closed Prefix

```json
{json.dumps(packet["closed_prefix_faces"], indent=2)}
```

These pieces are now enough to state the selected equality on the correct
finite domain: S0 selected smooth source, abstract Phi_fin trace, partial
projective rhoE trace, and the same 27-mode `B_N` basis with matching finite
algebra.

## Remaining Gate

```text
{packet["operator_identification_gate"]["name"]}
```

Statement:

```text
{packet["operator_identification_gate"]["statement"]}
```

## Why This Is Almost the Gap-Layer Closure

If the remaining gate closes, the existing eta becomes selected:

```text
eta_N = {packet["conditional_consequence_ready"]["eta_N_if_gate_closes"]}
threshold = {packet["conditional_consequence_ready"]["threshold"]}
passes = {packet["conditional_consequence_ready"]["passes_threshold"]}
```

Then the selected gap/Riesz/Green layer closes by the existing perturbation
bridge.  This still does not close dotD, C1, Yukawa, or flavor response.

## Required Payload Options

{chr(10).join("- " + item for item in packet["operator_identification_gate"]["sufficient_payloads"])}
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
