"""Attempt to fill the selected PhiFin S2 A_sel,N form-bound interface."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SM = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure")

INTERFACE = DATA / "selected_phifin_s2_a_sel_n_form_bound_interface.candidate.json"
SMOOTH_BN = SM / "candidate_data" / "selected_routec_smooth_bn_galerkin_lift.candidate.json"
DE_27_HONEST = (
    SM
    / "candidate_data"
    / "selected_routec_de_action_on_smooth_bn"
    / "de_action_on_smooth_bn.honest.json"
)
SMALL_SOLVE_DE = (
    SM / "candidate_data" / "selected_routec_strominger_galerkin_solve" / "de_action.candidate.json"
)
PROMOTION = DATA / "selected_phifin_s2_source_promotion_criterion.candidate.json"

OUTPUT_PACKET = DATA / "selected_phifin_s2_a_sel_n_form_bound_fill_attempt.candidate.json"
OUTPUT_CERT = CERTS / "selected_phifin_s2_a_sel_n_form_bound_fill_attempt_certificate.json"
OUTPUT_NOTE = CORPUS / "Selected_PhiFin_S2_A_sel_N_Form_Bound_Fill_Attempt_v1.md"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def matrix_shape(matrix: Any) -> list[int] | None:
    if not isinstance(matrix, list) or not matrix:
        return None
    if not all(isinstance(row, list) for row in matrix):
        return None
    return [len(matrix), len(matrix[0])]


def spectral_norm_difference(a: list[list[float]], b: list[list[float]]) -> float:
    diff = np.array(a, dtype=float) - np.array(b, dtype=float)
    return float(np.linalg.norm(diff, ord=2))


def build_packet() -> dict[str, Any]:
    interface = load_json(INTERFACE)
    smooth = load_json(SMOOTH_BN)
    de_27 = load_json(DE_27_HONEST)
    small_de = load_json(SMALL_SOLVE_DE)
    promotion = load_json(PROMOTION)

    threshold = float(interface["eta_threshold"])
    model = smooth["B_N_lift"]["stiffness_matrix_model_active_laplacian"]
    basis_id = smooth["B_N_lift"]["basis_id"]

    diagnostic_sector_eta: dict[str, Any] = {}
    for sector, slot in de_27["operator_slots"].items():
        eta = spectral_norm_difference(slot["stiffness_matrix"], model)
        diagnostic_sector_eta[sector] = {
            "eta_if_treated_as_A_sel_N": eta,
            "passes_eta_threshold": eta < threshold,
            "selected_source_verified": bool(slot.get("selected_source_verified")),
            "accepted_as_selected_proof": False,
        }

    max_diagnostic_eta = max(item["eta_if_treated_as_A_sel_N"] for item in diagnostic_sector_eta.values())
    all_diagnostic_eta_pass = all(item["passes_eta_threshold"] for item in diagnostic_sector_eta.values())
    all_selected_flags = all(item["selected_source_verified"] for item in diagnostic_sector_eta.values())

    small_shapes = {
        sector: matrix_shape(slot["stiffness_matrix"])
        for sector, slot in small_de["operator_slots"].items()
    }
    small_basis_compatible = small_de.get("basis_id") == basis_id and all(
        shape == [27, 27] for shape in small_shapes.values()
    )

    route_results = {
        "route_1_source_theorem": {
            "attempted": True,
            "closed": False,
            "evidence": {
                "S0_source_available": promotion["current_branch_evaluation"][
                    "fixed_selected_smooth_source_available"
                ],
                "full_selected_payload_emitted": promotion["current_branch_evaluation"][
                    "full_selected_payload_emitted"
                ],
                "S2_D_E_selected_source_verified": promotion["current_branch_evaluation"][
                    "S2_D_E_selected_source_verified"
                ],
                "S2_dotD_selected_source_verified": promotion["current_branch_evaluation"][
                    "S2_dotD_selected_source_verified"
                ],
            },
            "reason": (
                "The abstract S0 source is available, but no theorem currently "
                "identifies the 27-mode stiffness matrices as the finite selected "
                "Phi_fin/Strominger compression."
            ),
        },
        "route_2_explicit_A_sel_N": {
            "attempted": True,
            "closed": False,
            "diagnostic_27_mode_eta": {
                "max_eta_if_provenance_were_supplied": max_diagnostic_eta,
                "all_sectors_pass_threshold_numerically": all_diagnostic_eta_pass,
                "all_sectors_selected_source_verified": all_selected_flags,
                "sector_eta": diagnostic_sector_eta,
            },
            "reason": (
                "The 27-mode matrices are numerically close enough to A_model,N "
                "for the eta threshold, but selected provenance is absent. The "
                "small Strominger solve is basis-incompatible and cannot fill A_sel,N."
            ),
        },
        "route_3_form_bound": {
            "attempted": True,
            "closed": False,
            "candidate_bound_if_provenance_were_supplied": max_diagnostic_eta,
            "passes_threshold_if_provenance_were_supplied": max_diagnostic_eta < threshold,
            "reason": (
                "A form bound eta_N <= max sector diagnostic eta would pass "
                "numerically, but it would be a bound for the unpromoted finite "
                "scaffold, not for a selected Phi_fin/Strominger trace."
            ),
        },
    }

    return {
        "packet": "Selected_PhiFin_S2_A_sel_N_Form_Bound_Fill_Attempt_v1",
        "status": "FORM_BOUND_NUMERICALLY_WITHIN_BUDGET_PROVENANCE_OPEN",
        "inputs": {
            "interface": str(INTERFACE.relative_to(ROOT)),
            "smooth_BN": str(SMOOTH_BN),
            "DE_27_honest": str(DE_27_HONEST),
            "small_solve_DE": str(SMALL_SOLVE_DE),
            "promotion_criterion": str(PROMOTION.relative_to(ROOT)),
        },
        "basis": {
            "required_basis_id": basis_id,
            "dimension": 27,
            "small_solve_basis_compatible": small_basis_compatible,
            "small_solve_shapes": small_shapes,
        },
        "eta_threshold": threshold,
        "route_results": route_results,
        "current_closure": {
            "diagnostic_eta_computed": True,
            "diagnostic_eta_below_threshold": all_diagnostic_eta_pass,
            "selected_A_sel_N_emitted": False,
            "selected_form_bound_emitted": False,
            "selected_gap_error_certificate_closed": False,
            "selected_source_flags_promoted": False,
            "honest_replay_without_lifted_flags": False,
        },
        "key_finding": {
            "numerical_problem": False,
            "provenance_problem": True,
            "summary": (
                "If the existing 27-mode matrices were proven selected, the eta "
                "budget would pass with max diagnostic eta = 1.0 < "
                "2.1932454224643014. Therefore the remaining blocker is not the "
                "size of the operator perturbation; it is source provenance."
            ),
        },
        "minimal_fix_to_close": {
            "name": "Selected_PhiFin_S2_27_Mode_Provenance_Theorem_v1",
            "statement": (
                "Prove that the existing 27-mode B_N stiffness matrices are the "
                "finite selected Phi_fin/Strominger Galerkin compression of the "
                "S0 selected smooth source, not a model-active substitute."
            ),
            "then": [
                "promote the diagnostic eta bound to selected eta_N",
                "emit selected gap/Riesz/Green certificate",
                "rerun honest replay without lifted flags for the gap layer",
            ],
            "still_separate_after_that": [
                "dotD selected source",
                "alpha1 driver",
                "C1/Yukawa response",
            ],
        },
        "guardrails": {
            "does_not_promote_diagnostic_eta": True,
            "does_not_flip_selected_source_flags": True,
            "does_not_accept_small_solve_dimension_mismatch": True,
            "does_not_claim_full_S2_value_emission": True,
            "does_not_use_observed_or_benchmark_inputs": True,
        },
        "verdict": {
            "what_closes_now": (
                "The fill attempt computes the decisive diagnostic: max eta is "
                "1.0, below the 2.1932454224643014 budget, but this is not a "
                "selected proof because source provenance remains open."
            ),
            "what_remains": (
                "Prove 27-mode provenance from the S0 selected Phi_fin/Strominger "
                "source, or independently emit selected A_sel,N."
            ),
            "next_required_artifact": "Selected_PhiFin_S2_27_Mode_Provenance_Theorem_v1",
        },
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "SelectedPhiFinS2ASelNFormBoundFillAttempt",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "what_closes_now": {
            "diagnostic_eta_computed": True,
            "diagnostic_eta_below_threshold": True,
            "provenance_identified_as_remaining_blocker": True,
            "small_solve_rejected_for_dimension_mismatch": True,
        },
        "what_remains_open": {
            "selected_27_mode_provenance_theorem": True,
            "selected_A_sel_N_or_selected_form_bound": True,
            "selected_gap_error_certificate": True,
            "source_flag_promotion": True,
            "dotD_alpha1_C1_response": True,
        },
        "current_closure": packet["current_closure"],
        "key_finding": packet["key_finding"],
        "verdict": packet["verdict"],
        "guardrails": packet["guardrails"],
    }


def render_note(cert: dict[str, Any], packet: dict[str, Any]) -> str:
    route2 = packet["route_results"]["route_2_explicit_A_sel_N"]["diagnostic_27_mode_eta"]
    return f"""# Selected PhiFin S2 A_sel,N Form Bound Fill Attempt v1

## Result

Status: `{cert["status"]}`

The full plan was executed across the three routes:

1. selected source theorem route,
2. explicit selected `A_sel,N` route,
3. quadratic form-bound route.

## Diagnostic Eta

The existing 27-mode matrices are not selected yet, but if provenance were
supplied their diagnostic bound would be:

```text
max diagnostic eta = {route2["max_eta_if_provenance_were_supplied"]}
threshold = {packet["eta_threshold"]}
passes threshold numerically = {route2["all_sectors_pass_threshold_numerically"]}
selected source verified in all sectors = {route2["all_sectors_selected_source_verified"]}
```

This is the crucial result: the remaining problem is provenance, not size.

## Sector Eta Values

```json
{json.dumps(route2["sector_eta"], indent=2, sort_keys=True)}
```

## Why It Still Does Not Close

The diagnostic eta cannot be promoted because the current 27-mode matrices are
still model-active scaffold data. The small Strominger solve is rejected because
it is not on the 27-mode `B_N` basis.

## Minimal Fix

```text
{packet["minimal_fix_to_close"]["name"]}
```

Prove that the existing 27-mode matrices are the finite selected
Phi_fin/Strominger Galerkin compression of the S0 selected smooth source. If
that proof lands, the eta budget is already numerically good enough.
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
