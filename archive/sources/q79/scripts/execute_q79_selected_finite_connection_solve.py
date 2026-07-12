"""Execute the q79 selected finite-connection solve attempt.

The preceding witness audit made the next object concrete: replace identity
rho_E smoke by an honest finite connection trace, then test whether the result
can be promoted to selected q79 operator data.  The strongest current finite
values live in the adjacent constants/SM chain, so this script imports them
strictly and records the exact selected-source cut set.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
CANDIDATES = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"

OUT_DIR = CANDIDATES / "q79_selected_finite_connection_solve_execution"
OUT_CANDIDATE = CANDIDATES / "q79_selected_finite_connection_solve_execution.candidate.json"
OUT_CERT = CERTS / "q79_selected_finite_connection_solve_execution_certificate.json"
OUT_PAPER = CORPUS / "Q79_Selected_Finite_Connection_Solve_Execution_v1.md"

OUT_IMPORT_SUMMARY = OUT_DIR / "finite_connection_execution_import_summary.json"
OUT_ATTEMPT = OUT_DIR / "selected_finite_connection_execution_attempt.open.json"
OUT_CUTSET = OUT_DIR / "honest_replay_cutset.json"
OUT_CONTRACT = OUT_DIR / "selected_trace_or_full_hym_source_contract.open.json"

STATUS = "Q79_SELECTED_FINITE_CONNECTION_SOLVE_EXECUTED_PREFIX_VALUES_SOURCE_TRACE_OPEN"
NEXT = "Q79_Selected_Trace_Equals_Emitted_27Mode_Operator_or_Full_HYM_Newton_Replay_v1"

SM = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure")
CONSTANTS = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-nonsm-constants-no-knob")
GR = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-protospinor-gr-response-proof")

PRIOR_WITNESS = CERTS / "q79_typed_monad_cech_or_hym_connection_witness_certificate.json"
Q79_PHIFIN = CERTS / "q79_selected_phifin_alpha1_payload_certificate.json"
Q79_BASIS_TRANSPORT = CERTS / "q79_routec_basis_transport_primitive_source_theorem_certificate.json"

SM_RHOE = SM / "certificates" / "selected_routec_nonidentity_rhoe_bn_construction_certificate.json"
SM_SMOOTH_BN = SM / "certificates" / "selected_routec_smooth_bn_galerkin_lift_certificate.json"
SM_DE = SM / "certificates" / "selected_routec_de_action_on_smooth_bn_certificate.json"
SM_DOTD = SM / "certificates" / "selected_routec_sector_projectors_dotd_on_smooth_bn_certificate.json"
SM_C1 = SM / "certificates" / "selected_routec_c1_primitive_response_on_smooth_bn_certificate.json"

CONSTANTS_PREFIX = CONSTANTS / "certificates" / "routec_rhoe_bn_operator_prefix_import_certificate.json"
CONSTANTS_S0 = CONSTANTS / "certificates" / "selected_phifin_s0_source_prefix_certificate.json"
CONSTANTS_TRACE_SCAFFOLD = (
    CONSTANTS / "certificates" / "selected_phifin_s2_finite_trace_morphism_scaffold_certificate.json"
)
CONSTANTS_TRACE_EQUALS = (
    CONSTANTS / "certificates" / "selected_trace_equals_emitted_27_mode_de_attempt_certificate.json"
)
CONSTANTS_VALUE_REPLAY = (
    CONSTANTS
    / "certificates"
    / "selected_phifin_s2_value_emission_with_gap_error_honest_replay_certificate.json"
)
CONSTANTS_OPERATOR_THEOREM = (
    CONSTANTS
    / "certificates"
    / "selected_phifin_s2_selected_operator_and_truncation_source_theorem_attempt_certificate.json"
)

GR_HYM_CORRECTION = (
    GR / "certificates" / "selected_hym_correction_and_gauge_projector_value_table_certificate.json"
)

INPUTS = {
    "prior_witness_attempt": PRIOR_WITNESS,
    "q79_phifin_alpha1_payload": Q79_PHIFIN,
    "q79_basis_transport_primitive_source": Q79_BASIS_TRANSPORT,
    "sm_nonidentity_rhoe_bn": SM_RHOE,
    "sm_smooth_bn": SM_SMOOTH_BN,
    "sm_de_action": SM_DE,
    "sm_sector_projectors_dotd": SM_DOTD,
    "sm_c1_primitive_response": SM_C1,
    "constants_routec_prefix": CONSTANTS_PREFIX,
    "constants_s0_source_prefix": CONSTANTS_S0,
    "constants_trace_morphism_scaffold": CONSTANTS_TRACE_SCAFFOLD,
    "constants_trace_equals_emitted_27_mode_de": CONSTANTS_TRACE_EQUALS,
    "constants_value_replay": CONSTANTS_VALUE_REPLAY,
    "constants_operator_truncation_theorem": CONSTANTS_OPERATOR_THEOREM,
    "gr_first_hym_correction": GR_HYM_CORRECTION,
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
        "what_closes": data.get("what_closes") or data.get("what_closes_now") or data.get("closed_now"),
        "what_remains_open": data.get("what_remains_open") or data.get("not_closed"),
        "verdict": data.get("verdict"),
        "guardrails": data.get("guardrails"),
    }


def finite_execution_import_summary(
    prefix: dict[str, Any],
    sm_rhoe: dict[str, Any],
    sm_bn: dict[str, Any],
    sm_de: dict[str, Any],
    sm_dotd: dict[str, Any],
    sm_c1: dict[str, Any],
    gr_hym: dict[str, Any],
) -> dict[str, Any]:
    finite = prefix.get("finite_prefix_summary", {})
    rhoe = finite.get("rho_E", {})
    basis = finite.get("B_N", {})
    de = finite.get("D_E", {})
    dotd = finite.get("dotD", {})
    c1 = finite.get("C1", {})
    return {
        "status": "FINITE_PREFIX_VALUES_IMPORTED_SOURCE_PROMOTION_OPEN",
        "nonidentity_rhoE": {
            "import_status": sm_rhoe.get("status"),
            "nonidentity_projective_rhoE_candidate_built": sm_rhoe.get("what_closes", {}).get(
                "nonidentity_projective_rhoE_candidate_built"
            ),
            "identity_smoke_replaced": prefix.get("closed_now", {}).get(
                "identity_smoke_replaced_by_nonidentity_candidate"
            ),
            "rank": rhoe.get("rank"),
            "nonidentity_norm": rhoe.get("nonidentity_norm"),
            "projective_commutator_residual": rhoe.get("projective_commutator_residual"),
            "unitary_residual_max": rhoe.get("unitary_residual_max"),
            "selected_by_mtt": rhoe.get("selected_by_mtt"),
        },
        "smooth_BN": {
            "import_status": sm_bn.get("status"),
            "basis_id": basis.get("basis_id"),
            "dimension": basis.get("dimension"),
            "zero_cluster_dimension": basis.get("zero_cluster_dimension"),
            "complement_gap": basis.get("complement_gap"),
            "projective_equivariance_up_to_central_phase": basis.get(
                "projective_equivariance_up_to_central_phase"
            ),
            "smooth_scalar_basis_functions_phi_m_emitted": sm_bn.get("what_closes", {}).get(
                "smooth_scalar_basis_functions_phi_m_emitted"
            ),
            "gram_stiffness_emitted": (
                sm_bn.get("what_closes", {}).get("Gram_matrix_entries_emitted")
                and sm_bn.get("what_closes", {}).get("stiffness_matrix_entries_emitted_for_model_active_laplacian")
            ),
        },
        "DE": {
            "import_status": sm_de.get("status"),
            "D_E_matrix_on_27_mode_BN_emitted": sm_de.get("what_closes", {}).get(
                "D_E_matrix_on_27_mode_BN_emitted"
            ),
            "family_kernel_dimension": de.get("family_kernel_dimension"),
            "higgs_kernel_dimension": de.get("higgs_kernel_dimension"),
            "honest_validator_fails_only_by_selected_source_flags": de.get(
                "honest_validator_fails_only_by_selected_source_flags"
            ),
        },
        "dotD": {
            "import_status": sm_dotd.get("status"),
            "sector_projectors_on_27_mode_BN_emitted": sm_dotd.get("what_closes", {}).get(
                "sector_projectors_on_27_mode_BN_emitted"
            ),
            "dotD_alpha1_matrix_in_same_basis_emitted": sm_dotd.get("what_closes", {}).get(
                "dotD_alpha1_matrix_in_same_basis_emitted"
            ),
            "diagnostic_lift_validator_passes": dotd.get("diagnostic_lift_validator_passes"),
            "honest_validator_fails_only_by_source_driver_flags": dotd.get(
                "honest_validator_fails_only_by_source_driver_flags"
            ),
            "projector_ranks": dotd.get("projector_ranks"),
        },
        "C1": {
            "import_status": sm_c1.get("status"),
            "primitive_C1_contraction_engine_built": sm_c1.get("what_closes", {}).get(
                "primitive_C1_contraction_engine_built"
            ),
            "canonical_tensor_zero_response_result_proved_finitely": sm_c1.get("what_closes", {}).get(
                "canonical_tensor_zero_response_result_proved_finitely"
            ),
            "all_c1_matrices_zero_for_canonical_tensor": c1.get(
                "all_c1_matrices_zero_for_canonical_tensor"
            ),
            "why_zero": c1.get("why_zero"),
        },
        "first_HYM_correction": {
            "import_status": gr_hym.get("status"),
            "first_tracefree_hym_density_source_computed": gr_hym.get("what_closes_now", {}).get(
                "first_tracefree_hym_density_source_computed"
            ),
            "selected_End0_direction": gr_hym.get("first_tracefree_hym_correction", {}).get(
                "selected_End0_direction"
            ),
            "poisson_residual_l2": gr_hym.get("first_tracefree_hym_correction", {}).get(
                "poisson_residual_l2"
            ),
            "full_selected_A_HYM_coefficients_open": gr_hym.get("what_remains_open", {}).get(
                "full_selected_A_HYM_coefficients"
            ),
        },
    }


def honest_replay_cutset(
    trace_equals: dict[str, Any],
    value_replay: dict[str, Any],
    operator_theorem: dict[str, Any],
) -> dict[str, Any]:
    return {
        "schema": "Q79SelectedFiniteConnectionHonestReplayCutset.v1",
        "status": "HONEST_REPLAY_BLOCKED_BY_SOURCE_TRACE_AND_FULL_OPERATOR_PROVENANCE",
        "trace_equals_status": trace_equals.get("status"),
        "value_replay_status": value_replay.get("status"),
        "operator_truncation_status": operator_theorem.get("status"),
        "open_items": {
            "selected_trace_equality": trace_equals.get("what_remains_open", {}).get(
                "selected_trace_equality"
            ),
            "canonical_metric_connection_source": trace_equals.get("what_remains_open", {}).get(
                "canonical_metric_connection_source"
            ),
            "H_sector_shift_source": trace_equals.get("what_remains_open", {}).get(
                "H_sector_shift_source"
            ),
            "selected_source_flags": trace_equals.get("what_remains_open", {}).get(
                "selected_source_flags"
            ),
            "honest_replay_without_lifted_flags": value_replay.get("what_remains_open", {}).get(
                "honest_replay_without_lifted_flags"
            ),
            "selected_D_E_source_promotion": value_replay.get("what_remains_open", {}).get(
                "selected_D_E_source_promotion"
            ),
            "selected_dotD_source_verified": value_replay.get("what_remains_open", {}).get(
                "selected_dotD_source_verified"
            ),
            "alpha1_driver_verified": value_replay.get("what_remains_open", {}).get(
                "alpha1_driver_verified"
            ),
            "selected_full_iwasawa_strominger_operator_formula": operator_theorem.get(
                "what_remains_open", {}
            ).get("selected_full_iwasawa_strominger_operator_formula"),
            "full_minus_model_operator_norm_bound": operator_theorem.get("what_remains_open", {}).get(
                "full_minus_model_operator_norm_bound"
            ),
            "selected_gap_error_certificate": operator_theorem.get("what_remains_open", {}).get(
                "selected_gap_error_certificate"
            ),
            "theorem_derived_selected_source_flags": operator_theorem.get("what_remains_open", {}).get(
                "theorem_derived_selected_source_flags"
            ),
        },
        "reason": (
            "The finite matrices have value shape and diagnostic replay, but the "
            "current corpus does not prove that they equal the finite trace of the "
            "selected smooth Strominger/HYM source, nor that the model-active "
            "operator is the full selected Iwasawa/Strominger operator with a "
            "certified truncation error."
        ),
    }


def execution_attempt(import_summary: dict[str, Any], cutset: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema": "Q79SelectedFiniteConnectionSolveExecutionAttempt.v1",
        "status": "FINITE_VALUES_EXECUTED_SELECTED_SOURCE_TRACE_OPEN",
        "branch": {
            "q": 79,
            "orientation": "F",
            "torsion_label_m": 1,
            "basis_id": import_summary["smooth_BN"]["basis_id"],
        },
        "finite_values_present": {
            "nonidentity_projective_rhoE": import_summary["nonidentity_rhoE"][
                "nonidentity_projective_rhoE_candidate_built"
            ],
            "smooth_27_mode_BN": import_summary["smooth_BN"][
                "smooth_scalar_basis_functions_phi_m_emitted"
            ],
            "Gram_and_stiffness": import_summary["smooth_BN"]["gram_stiffness_emitted"],
            "D_E_matrix": import_summary["DE"]["D_E_matrix_on_27_mode_BN_emitted"],
            "Riesz_Green_gap": import_summary["smooth_BN"]["complement_gap"] is not None,
            "sector_projectors": import_summary["dotD"]["sector_projectors_on_27_mode_BN_emitted"],
            "dotD_alpha1": import_summary["dotD"]["dotD_alpha1_matrix_in_same_basis_emitted"],
            "C1_contraction_engine": import_summary["C1"]["primitive_C1_contraction_engine_built"],
            "first_tracefree_HYM_correction": import_summary["first_HYM_correction"][
                "first_tracefree_hym_density_source_computed"
            ],
        },
        "selected_promotion": {
            "rhoE_selected_by_mtt": import_summary["nonidentity_rhoE"]["selected_by_mtt"],
            "selected_trace_equality": False,
            "honest_replay_without_lifted_flags": False,
            "full_selected_operator_formula": False,
            "selected_gap_error_certificate": False,
            "selected_finite_connection_solve_closed": False,
        },
        "cutset": cutset["open_items"],
        "closure_claimed": False,
    }


def source_contract() -> dict[str, Any]:
    return {
        "schema": "Q79SelectedTraceOrFullHYMSourceContract.v1",
        "status": "OPEN",
        "accepted_closing_routes": {
            "finite_trace_identification": [
                "prove selected S0 smooth source transports functorially to the 27-mode B_N trace",
                "prove emitted nonidentity rho_E is the selected trace, not only a projective finite candidate",
                "derive the canonical F3xF3 Fourier Laplacian entries from the selected connection",
                "derive the H-sector rank-two zero-cluster shift from the same source",
                "prove selected gap/truncation error and rerun q79 validators without lifted flags",
            ],
            "full_HYM_Newton_replay": [
                "execute full nonlinear exp(S) HYM/Strominger Newton solve",
                "emit selected A_HYM coefficients in a fixed gauge",
                "bound full-minus-model operator norm on B_N",
                "export D_E/Riesz/Green/dotD/alpha1 from the selected full operator",
            ],
            "typed_monad_Cech_payload": [
                "supply typed f_i/g_i sections, transitions, g o f = 0, and exactness",
                "derive the same finite D_E/Riesz/Green/dotD stack from those data",
            ],
        },
        "must_not_use": [
            "selected flags added by diagnostic lift",
            "observed masses, CKM magnitudes, or benchmark Yukawa entries",
            "identity rho_E smoke",
            "canonical model-active operator relabeled as selected without a trace theorem",
        ],
    }


def build_candidate() -> dict[str, Any]:
    prior = load(PRIOR_WITNESS)
    q79_phifin = load(Q79_PHIFIN)
    q79_basis = load(Q79_BASIS_TRANSPORT)
    prefix = load(CONSTANTS_PREFIX)
    sm_rhoe = load(SM_RHOE)
    sm_bn = load(SM_SMOOTH_BN)
    sm_de = load(SM_DE)
    sm_dotd = load(SM_DOTD)
    sm_c1 = load(SM_C1)
    constants_s0 = load(CONSTANTS_S0)
    trace_scaffold = load(CONSTANTS_TRACE_SCAFFOLD)
    trace_equals = load(CONSTANTS_TRACE_EQUALS)
    value_replay = load(CONSTANTS_VALUE_REPLAY)
    operator_theorem = load(CONSTANTS_OPERATOR_THEOREM)
    gr_hym = load(GR_HYM_CORRECTION)

    import_summary = finite_execution_import_summary(prefix, sm_rhoe, sm_bn, sm_de, sm_dotd, sm_c1, gr_hym)
    cutset = honest_replay_cutset(trace_equals, value_replay, operator_theorem)
    attempt = execution_attempt(import_summary, cutset)
    contract = source_contract()

    write_json(OUT_IMPORT_SUMMARY, import_summary)
    write_json(OUT_CUTSET, cutset)
    write_json(OUT_ATTEMPT, attempt)
    write_json(OUT_CONTRACT, contract)

    all_finite_values_present = all(attempt["finite_values_present"].values())
    selected_solve_closed = attempt["selected_promotion"]["selected_finite_connection_solve_closed"]

    data = {
        "certificate": "Q79SelectedFiniteConnectionSolveExecution",
        "status": STATUS,
        "candidate_path": rel(OUT_CANDIDATE),
        "paper": rel(OUT_PAPER),
        "artifact_paths": {
            "finite_connection_execution_import_summary": rel(OUT_IMPORT_SUMMARY),
            "selected_finite_connection_execution_attempt": rel(OUT_ATTEMPT),
            "honest_replay_cutset": rel(OUT_CUTSET),
            "selected_trace_or_full_hym_source_contract": rel(OUT_CONTRACT),
        },
        "input_statuses": {name: status_record(path) for name, path in INPUTS.items()},
        "prior_witness_status": prior.get("status"),
        "q79_phifin_status": q79_phifin.get("status"),
        "q79_basis_transport_status": q79_basis.get("status"),
        "constants_s0_status": constants_s0.get("status"),
        "trace_scaffold_status": trace_scaffold.get("status"),
        "finite_connection_execution_import_summary": import_summary,
        "selected_finite_connection_execution_attempt": attempt,
        "honest_replay_cutset": cutset,
        "selected_trace_or_full_hym_source_contract": contract,
        "what_closes_now": {
            "identity_rhoE_smoke_replaced_by_nonidentity_projective_candidate": import_summary[
                "nonidentity_rhoE"
            ]["identity_smoke_replaced"],
            "smooth_27_mode_BN_imported": import_summary["smooth_BN"]["dimension"] == 27,
            "model_active_DE_Riesz_Green_values_imported": import_summary["DE"][
                "D_E_matrix_on_27_mode_BN_emitted"
            ],
            "sector_projectors_and_dotD_imported": import_summary["dotD"][
                "dotD_alpha1_matrix_in_same_basis_emitted"
            ],
            "canonical_C1_zero_response_no_go_imported": import_summary["C1"][
                "canonical_tensor_zero_response_result_proved_finitely"
            ],
            "first_tracefree_HYM_correction_imported": import_summary["first_HYM_correction"][
                "first_tracefree_hym_density_source_computed"
            ],
            "honest_replay_cutset_identified": True,
            "selected_trace_or_full_hym_contract_created": True,
            "all_finite_value_shapes_present": all_finite_values_present,
        },
        "what_remains_open": {
            "selected_finite_connection_solve_closed": not selected_solve_closed,
            "selected_trace_equality": True,
            "canonical_metric_connection_source": True,
            "H_sector_shift_source": True,
            "theorem_derived_selected_source_flags": True,
            "full_selected_iwasawa_strominger_operator_formula": True,
            "selected_gap_error_certificate": True,
            "honest_replay_without_lifted_flags": True,
            "selected_noninvariant_C1_primitive_or_basis_transport": True,
            "primitive_C1_nonzero_values": True,
            "A_selected_b_selected_full_SM_closure": True,
        },
        "guardrails": {
            "claims_selected_finite_connection_solve_closed": False,
            "claims_selected_source_flags_promoted": False,
            "claims_model_active_operator_is_full_selected_operator": False,
            "claims_identity_rhoE_smoke_is_selected": False,
            "uses_lifted_flags_as_proof": False,
            "uses_observed_masses_or_ckm_inputs": False,
            "claims_primitive_C1_values_computed": False,
            "claims_A_selected_or_b_selected": False,
            "claims_full_sm_closure": False,
        },
        "theorem": {
            "name": "Q79SelectedFiniteConnectionSolveExecutionCutsetTheorem",
            "proved": True,
            "closure_claimed": False,
            "statement": (
                "The selected finite connection solve has been executed as far as "
                "current finite values permit: identity rho_E smoke is replaced by "
                "a nonidentity projective rho_E candidate; a 27-mode smooth B_N "
                "basis, model-active D_E/Riesz/Green, sector projectors, dotD, "
                "canonical C1 contraction engine, and first tracefree HYM correction "
                "are imported.  This does not close selected source replay, because "
                "the corpus still lacks selected trace equality, full selected "
                "Iwasawa/Strominger operator and truncation bounds, and theorem-"
                "derived selected source flags."
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
    summary = data["finite_connection_execution_import_summary"]
    return f"""# Q79 Selected Finite Connection Solve Execution v1

## Result

This executes the selected finite connection solve target as far as the current
finite data permit.

The good news: identity-rho smoke is no longer the strongest finite object.
A nonidentity projective `rho_E`, a smooth 27-mode `B_N`, model-active
`D_E`, Riesz/Green data, sector projectors, `dotD_alpha1`, a C1 contraction
engine, and a first tracefree HYM correction are all available as finite value
shapes.

The honest result: the selected finite connection solve is still not closed,
because source trace equality and full selected operator provenance remain
open.

## Imported Finite Values

- `rho_E` rank: `{summary["nonidentity_rhoE"]["rank"]}`
- nonidentity norm: `{summary["nonidentity_rhoE"]["nonidentity_norm"]}`
- projective commutator residual: `{summary["nonidentity_rhoE"]["projective_commutator_residual"]}`
- `rho_E` selected by MTT: `{summary["nonidentity_rhoE"]["selected_by_mtt"]}`
- basis: `{summary["smooth_BN"]["basis_id"]}`
- basis dimension: `{summary["smooth_BN"]["dimension"]}`
- zero cluster dimension: `{summary["smooth_BN"]["zero_cluster_dimension"]}`
- complement gap: `{summary["smooth_BN"]["complement_gap"]}`
- family kernel dimension: `{summary["DE"]["family_kernel_dimension"]}`
- Higgs kernel dimension: `{summary["DE"]["higgs_kernel_dimension"]}`
- canonical C1 zero response: `{summary["C1"]["all_c1_matrices_zero_for_canonical_tensor"]}`
- first tracefree HYM direction: `{summary["first_HYM_correction"]["selected_End0_direction"]}`

## Honest Replay Cut Set

The finite value shapes are present, but honest replay still fails at:

{bool_lines(data["honest_replay_cutset"]["open_items"])}

This is exactly the distinction we needed: values are available at model-active
finite level, but selected source replay has not been theorem-derived.

## Closing Contract

The next proof must close one of these routes:

- finite trace identification from the selected smooth source to the emitted
  27-mode operator;
- full nonlinear HYM/Strominger Newton replay with selected coefficients and
  truncation bounds;
- explicit typed monad/Cech payload deriving the same finite stack.

Contract: `{data["artifact_paths"]["selected_trace_or_full_hym_source_contract"]}`

## What Closes Now

{bool_lines(data["what_closes_now"])}

## What Remains Open

{bool_lines(data["what_remains_open"])}

## Theorem

`{data["theorem"]["name"]}` is proved as an execution/cutset theorem.

{data["theorem"]["statement"]}

This does not compute selected primitive C1 values, `A_selected`, `b_selected`,
or full SM closure.

Next required artifact: `{data["next_required_artifact"]}`.
"""


def main() -> int:
    data = build_candidate()
    write_json(OUT_CANDIDATE, data)
    write_json(OUT_CERT, data)
    OUT_PAPER.parent.mkdir(parents=True, exist_ok=True)
    OUT_PAPER.write_text(build_paper(data), encoding="utf-8")
    print("Q79 selected finite connection solve execution")
    print(json.dumps({"status": data["status"], "next": data["next_required_artifact"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
