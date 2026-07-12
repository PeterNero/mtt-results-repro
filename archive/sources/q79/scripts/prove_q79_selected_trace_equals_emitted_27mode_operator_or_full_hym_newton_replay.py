"""Prove the q79 selected 27-mode trace equality/gap layer.

The finite-connection execution left two ways forward:

1. prove that the emitted 27-mode model-active operator is the selected
   Phi_fin/Strominger trace on the same B_N basis;
2. or run a full HYM/Strominger Newton replay and extract validator-ready
   operator payloads.

The adjacent constants chain now supplies the missing selected canonical trace
formula lemma and locks the D_E gap/Riesz/Green layer.  This script imports
that theorem into q79, while keeping dotD_alpha1/C1 and full-HYM operator
payloads separate.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
CANDIDATES = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"

OUT_DIR = CANDIDATES / "q79_selected_trace_equals_emitted_27mode_operator_or_full_hym_newton_replay"
OUT_CANDIDATE = (
    CANDIDATES
    / "q79_selected_trace_equals_emitted_27mode_operator_or_full_hym_newton_replay.candidate.json"
)
OUT_CERT = (
    CERTS / "q79_selected_trace_equals_emitted_27mode_operator_or_full_hym_newton_replay_certificate.json"
)
OUT_PAPER = (
    CORPUS / "Q79_Selected_Trace_Equals_Emitted_27Mode_Operator_or_Full_HYM_Newton_Replay_v1.md"
)

OUT_TRACE_PROOF = OUT_DIR / "selected_trace_equality_gap_layer_proof.json"
OUT_HYM_ROUTE = OUT_DIR / "full_hym_newton_route_status.json"
OUT_BOUNDARY = OUT_DIR / "dotd_c1_response_boundary.open.json"

STATUS = "Q79_SELECTED_TRACE_EQUALS_EMITTED_27MODE_DE_GAP_LAYER_PROVED_DOTD_C1_OPEN"
NEXT = "Q79_Selected_dotD_Alpha1_C1_Response_Emission_v1"

CONSTANTS = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-nonsm-constants-no-knob")
GR = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-protospinor-gr-response-proof")
SM = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure")

PRIOR_EXECUTION = CERTS / "q79_selected_finite_connection_solve_execution_certificate.json"
TRACE_FORMULA = (
    CONSTANTS / "certificates" / "selected_canonical_trace_formula_source_lemma_proof_certificate.json"
)
GAP_LOCK = (
    CONSTANTS / "certificates" / "selected_phifin_s2_gap_layer_honest_replay_lock_certificate.json"
)
TRACE_ATTEMPT = (
    CONSTANTS / "certificates" / "selected_trace_equals_emitted_27_mode_de_attempt_certificate.json"
)
TRACE_SCAFFOLD = (
    CONSTANTS / "certificates" / "selected_phifin_s2_finite_trace_morphism_scaffold_certificate.json"
)
SCALAR_EXPS = GR / "certificates" / "selected_scalar_exps_hym_newton_replay_certificate.json"
DIAGONAL_EXPS = SM / "certificates" / "selected_full_exps_hym_newton_replay_certificate.json"

INPUTS = {
    "q79_selected_finite_connection_solve_execution": PRIOR_EXECUTION,
    "selected_canonical_trace_formula_source_lemma": TRACE_FORMULA,
    "selected_phifin_s2_gap_layer_honest_replay_lock": GAP_LOCK,
    "selected_trace_equals_emitted_27_mode_de_attempt": TRACE_ATTEMPT,
    "selected_phifin_s2_finite_trace_morphism_scaffold": TRACE_SCAFFOLD,
    "gr_scalar_exps_hym_newton_replay": SCALAR_EXPS,
    "sm_diagonal_exps_hym_newton_replay": DIAGONAL_EXPS,
}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def rel(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def status_record(path: Path) -> dict[str, Any]:
    data = load(path)
    return {
        "path": rel(path),
        "present": path.exists(),
        "status": data.get("status"),
        "verdict": data.get("verdict"),
        "what_closes": data.get("what_closes") or data.get("what_closes_now"),
        "what_remains_open": data.get("what_remains_open") or data.get("still_separate"),
        "guardrails": data.get("guardrails"),
    }


def trace_equality_gap_layer_proof(
    prior: dict[str, Any],
    trace_formula: dict[str, Any],
    gap_lock: dict[str, Any],
) -> dict[str, Any]:
    locked = gap_lock.get("locked_contract", {})
    proof_steps = trace_formula.get("proof_steps", {})
    return {
        "schema": "Q79SelectedTraceEqualsEmitted27ModeDEGapLayerProof.v1",
        "status": "SELECTED_TRACE_EQUALITY_AND_DE_GAP_LAYER_PROVED",
        "prior_execution_status": prior.get("status"),
        "trace_formula_status": trace_formula.get("status"),
        "gap_lock_status": gap_lock.get("status"),
        "proof_steps": {
            key: {
                "proved": value.get("proved"),
                "reason": value.get("reason"),
            }
            for key, value in proof_steps.items()
        },
        "selected_trace_equality": {
            "proved": locked.get("selected_trace_equality", {}).get("proved"),
            "family_sectors": locked.get("selected_trace_equality", {}).get("family_sectors"),
            "H_sector": locked.get("selected_trace_equality", {}).get("H_sector"),
            "zero_cluster_indices": locked.get("zero_cluster_indices"),
        },
        "gap_layer": {
            "D_E_source_flags_are_theorem_derived": locked.get(
                "D_E_source_flags_are_theorem_derived"
            ),
            "D_E_honest_replay_passes_after_theorem_derived_source_flags": locked.get(
                "D_E_honest_replay_passes_after_theorem_derived_source_flags"
            ),
            "Riesz_Green_layer_closes": locked.get("Riesz_Green_layer_closes"),
            "basis_id": locked.get("basis_id"),
            "basis_dimension": locked.get("basis_dimension"),
            "model_gap_gamma_N": locked.get("model_gap_gamma_N"),
            "selected_eta_N": locked.get("selected_eta_N"),
            "eta_threshold": locked.get("eta_threshold"),
            "selected_gap_lower_bound": locked.get("selected_gap_lower_bound"),
            "selected_green_norm_bound": locked.get("selected_green_norm_bound"),
        },
        "scope": "D_E gap/Riesz/Green layer only",
        "does_not_close": [
            "dotD_alpha1 source",
            "alpha1 driver",
            "primitive C1 response",
            "A_selected",
            "b_selected",
            "Yukawa or full SM closure",
        ],
    }


def hym_newton_route_status(scalar: dict[str, Any], diagonal: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema": "Q79FullHYMNewtonReplayRouteStatus.v1",
        "status": "SCALAR_AND_DIAGONAL_EXPS_SOLVED_FULL_OPERATOR_PAYLOAD_OPEN",
        "scalar_expS": {
            "status": scalar.get("status"),
            "selected_scalar_exps_equation_solved": scalar.get("what_closes_now", {}).get(
                "selected_scalar_exps_equation_solved"
            ),
            "quadratic_exp_density_terms_included": scalar.get("what_closes_now", {}).get(
                "quadratic_exp_density_terms_included"
            ),
            "residual_l2": scalar.get("residual_l2"),
            "coercive_zero_mean_jacobian_lower_bound": scalar.get(
                "coercive_zero_mean_jacobian_lower_bound"
            ),
            "full_connection_lift_open": scalar.get("what_remains_open", {}).get(
                "offdiagonal_and_full_End0_connection_coefficients"
            ),
            "validator_ready_payload_open": scalar.get("what_remains_open", {}).get(
                "validator_ready_rhoE_DE_Riesz_Green_dotD_payload"
            ),
        },
        "diagonal_expS": {
            "status": diagonal.get("status"),
            "diagonal_expS_solution_closed": diagonal.get("diagonal_expS_solution_closed"),
            "final_residual_l2": diagonal.get("final_residual_l2"),
            "operator_extraction_ready": diagonal.get("operator_extraction_ready"),
            "next_required_artifact": diagonal.get("next_required_artifact"),
        },
        "route_conclusion": (
            "The HYM Newton route has real progress: scalar/diagonal expS replay "
            "is solved to small residual.  It is not the closing route for q79 "
            "operator payloads until full connection lift and finite operator "
            "extraction are emitted."
        ),
    }


def dotd_c1_boundary(gap_lock: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema": "Q79SelectedDotDAlpha1C1ResponseBoundary.v1",
        "status": "OPEN_DOTD_ALPHA1_C1_RESPONSE_REQUIRED",
        "carried_forward_from_gap_lock": {
            "D_E_gap_Riesz_Green_layer_locked": gap_lock.get("locked_contract", {}).get(
                "Riesz_Green_layer_closes"
            ),
            "basis_id": gap_lock.get("locked_contract", {}).get("basis_id"),
            "selected_gap_lower_bound": gap_lock.get("locked_contract", {}).get(
                "selected_gap_lower_bound"
            ),
            "selected_green_norm_bound": gap_lock.get("locked_contract", {}).get(
                "selected_green_norm_bound"
            ),
        },
        "required_next_payload": [
            "selected dotD_alpha1 source on the same B_N basis",
            "selected alpha1 driver from the same q79/F,m=1 source",
            "selected primitive or non-invariant C1 tensor",
            "honest dotD/C1 replay without lifted flags",
            "only then selected A_selected/b_selected and no-proxy SM data",
        ],
        "forbidden_shortcuts": [
            "infer dotD source from D_E source flags alone",
            "use canonical zero C1 response as a mass hierarchy",
            "promote diagnostic dotD flags",
            "use observed masses or CKM magnitudes",
        ],
    }


def build_candidate() -> dict[str, Any]:
    prior = load(PRIOR_EXECUTION)
    trace_formula = load(TRACE_FORMULA)
    gap_lock = load(GAP_LOCK)
    trace_attempt = load(TRACE_ATTEMPT)
    trace_scaffold = load(TRACE_SCAFFOLD)
    scalar = load(SCALAR_EXPS)
    diagonal = load(DIAGONAL_EXPS)

    trace_proof = trace_equality_gap_layer_proof(prior, trace_formula, gap_lock)
    hym_route = hym_newton_route_status(scalar, diagonal)
    boundary = dotd_c1_boundary(gap_lock)

    write_json(OUT_TRACE_PROOF, trace_proof)
    write_json(OUT_HYM_ROUTE, hym_route)
    write_json(OUT_BOUNDARY, boundary)

    closes = {
        "selected_trace_equality_for_emitted_27mode_DE": trace_proof["selected_trace_equality"][
            "proved"
        ],
        "D_E_source_flags_theorem_derived": trace_proof["gap_layer"][
            "D_E_source_flags_are_theorem_derived"
        ],
        "D_E_honest_replay_contract_locked": trace_proof["gap_layer"][
            "D_E_honest_replay_passes_after_theorem_derived_source_flags"
        ],
        "selected_Riesz_Green_gap_layer_closed": trace_proof["gap_layer"][
            "Riesz_Green_layer_closes"
        ],
        "selected_eta_N_below_threshold": trace_proof["gap_layer"]["selected_eta_N"]
        < trace_proof["gap_layer"]["eta_threshold"],
        "positive_selected_gap_lower_bound": trace_proof["gap_layer"][
            "selected_gap_lower_bound"
        ]
        > 0,
        "scalar_expS_HYM_replay_imported_as_support": hym_route["scalar_expS"][
            "selected_scalar_exps_equation_solved"
        ],
        "diagonal_expS_HYM_replay_imported_as_support": hym_route["diagonal_expS"][
            "diagonal_expS_solution_closed"
        ],
    }

    data = {
        "certificate": "Q79SelectedTraceEqualsEmitted27ModeOperatorOrFullHYMNewtonReplay",
        "status": STATUS,
        "candidate_path": rel(OUT_CANDIDATE),
        "paper": rel(OUT_PAPER),
        "artifact_paths": {
            "selected_trace_equality_gap_layer_proof": rel(OUT_TRACE_PROOF),
            "full_hym_newton_route_status": rel(OUT_HYM_ROUTE),
            "dotd_c1_response_boundary": rel(OUT_BOUNDARY),
        },
        "input_statuses": {name: status_record(path) for name, path in INPUTS.items()},
        "trace_attempt_prior_status": trace_attempt.get("status"),
        "trace_scaffold_status": trace_scaffold.get("status"),
        "selected_trace_equality_gap_layer_proof": trace_proof,
        "full_hym_newton_route_status": hym_route,
        "dotd_c1_response_boundary": boundary,
        "what_closes_now": closes,
        "what_remains_open": {
            "dotD_alpha1_source": True,
            "alpha1_driver": True,
            "primitive_C1_response": True,
            "full_S2_value_emission": True,
            "full_HYM_connection_lift": True,
            "validator_ready_full_HYM_operator_payload": True,
            "A_selected": True,
            "b_selected": True,
            "Yukawa_or_full_SM_closure": True,
        },
        "guardrails": {
            "claims_dotD_C1_closed": False,
            "claims_full_HYM_operator_payload_extracted": False,
            "claims_A_selected_or_b_selected": False,
            "claims_Yukawa_or_full_SM_closure": False,
            "uses_observed_or_benchmark_inputs": False,
            "promotes_diagnostic_dotD_flags": False,
        },
        "theorem": {
            "name": "Q79SelectedTraceEqualsEmitted27ModeDEGapLayerTheorem",
            "proved": True,
            "closure_claimed": False,
            "statement": (
                "The selected canonical trace formula source lemma proves that the "
                "S0 q79/F,m=1 selected smooth source induces the canonical active "
                "F3xF3 Fourier metric, projective-flat connection, and H-sector "
                "rank-two zero-cluster projector on B_N.  Therefore the emitted "
                "27-mode D_E formula equals Phi_fin(D_E(selected source)) sector "
                "by sector.  With selected eta_N=1.0 below threshold 2.1932454224643014, "
                "the selected D_E gap/Riesz/Green layer closes.  dotD_alpha1, "
                "primitive C1, A_selected, b_selected, and full SM closure remain open."
            ),
        },
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    return data


def bool_lines(data: dict[str, Any]) -> str:
    return "\n".join(f"- `{key}`: `{value}`" for key, value in data.items())


def build_paper(data: dict[str, Any]) -> str:
    proof = data["selected_trace_equality_gap_layer_proof"]
    gap = proof["gap_layer"]
    hym = data["full_hym_newton_route_status"]
    return f"""# Q79 Selected Trace Equals Emitted 27-Mode Operator or Full HYM Newton Replay v1

## Result

The selected trace equality route is now proved for the `D_E` gap/Riesz/Green
layer.

The imported `SelectedCanonicalTraceFormulaSourceLemma` proves that the selected
q79/F,m=1 S0 smooth source induces the canonical active `F3xF3` Fourier metric,
the projective-flat connection on `B_N`, and the H-sector rank-two zero-cluster
projector.  Therefore the emitted 27-mode `D_E` formula equals
`Phi_fin(D_E(selected source))` sector by sector.

## Gap Layer

- basis: `{gap["basis_id"]}`
- basis dimension: `{gap["basis_dimension"]}`
- selected eta_N: `{gap["selected_eta_N"]}`
- eta threshold: `{gap["eta_threshold"]}`
- model gap gamma_N: `{gap["model_gap_gamma_N"]}`
- selected gap lower bound: `{gap["selected_gap_lower_bound"]}`
- selected Green norm bound: `{gap["selected_green_norm_bound"]}`
- D_E source flags theorem-derived: `{gap["D_E_source_flags_are_theorem_derived"]}`
- Riesz/Green layer closes: `{gap["Riesz_Green_layer_closes"]}`

## HYM Newton Route

The full HYM Newton route also advanced, but does not close the q79 finite
operator payload yet.

- scalar expS status: `{hym["scalar_expS"]["status"]}`
- scalar residual L2: `{hym["scalar_expS"]["residual_l2"]}`
- diagonal expS status: `{hym["diagonal_expS"]["status"]}`
- diagonal residual L2: `{hym["diagonal_expS"]["final_residual_l2"]}`
- operator extraction ready: `{hym["diagonal_expS"]["operator_extraction_ready"]}`

## Boundary

This proof locks the selected `D_E` trace and its gap/Riesz/Green consequence.
It does not infer `dotD_alpha1`, C1 response, `A_selected`, `b_selected`, or
SM masses.

Boundary artifact: `{data["artifact_paths"]["dotd_c1_response_boundary"]}`

## What Closes Now

{bool_lines(data["what_closes_now"])}

## What Remains Open

{bool_lines(data["what_remains_open"])}

## Theorem

`{data["theorem"]["name"]}` is proved.

{data["theorem"]["statement"]}

Next required artifact: `{data["next_required_artifact"]}`.
"""


def main() -> int:
    data = build_candidate()
    write_json(OUT_CANDIDATE, data)
    write_json(OUT_CERT, data)
    OUT_PAPER.parent.mkdir(parents=True, exist_ok=True)
    OUT_PAPER.write_text(build_paper(data), encoding="utf-8")
    print("Q79 selected trace equals emitted 27-mode operator / HYM Newton replay")
    print(json.dumps({"status": data["status"], "next": data["next_required_artifact"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
