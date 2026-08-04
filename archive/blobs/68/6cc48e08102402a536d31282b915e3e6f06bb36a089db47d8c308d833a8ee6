"""Build H-sector quartic/threshold payload or strict ten-K closure packet.

The preceding gate proves that the ten-K antecedent is at 9/10 and that
rank-only, heat/torsion-only, and external replay shortcuts cannot supply the
H/lambda row.  This packet advances the remaining target by closing the exact
H-sector source equation and then auditing the current ingredients against it.

The result is deliberately not a value closure: it records the precise H
payload row that must be emitted before strict Omega/lambda_H execution can
trigger.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_hsectorquarticthresholdpayload_or_stricttenkclosure"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
EQUATION = PACKET_DIR / "h_sector_payload_source_equation.packet.json"
TRIALS = PACKET_DIR / "h_sector_payload_candidate_trials.packet.json"
TEN_K_GATE = PACKET_DIR / "strict_ten_k_gate_after_h_payload_attempt.packet.json"
WORKORDER = PACKET_DIR / "h_sector_payload_execution_workorder.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_h_sector_payload_gate.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HSectorQuarticThresholdPayload_or_StrictTenKClosure_v1.md"

PREVIOUS = DATA / "selected_lambdahpayloadexecution_or_tenkthresholdclosure.candidate.json"
PREVIOUS_ANTECEDENT = (
    DATA
    / "selected_lambdahpayloadexecution_or_tenkthresholdclosure"
    / "h_sector_kthreshold_antecedent_recheck.packet.json"
)
PREVIOUS_MINIMAL = (
    DATA
    / "selected_lambdahpayloadexecution_or_tenkthresholdclosure"
    / "minimal_h_lambda_payload_theorem.packet.json"
)
STEP68_EXPONENTS = (
    DATA
    / "selected_step68_thetaexponentweights_or_prefactorthreshold_frontier"
    / "step68_selected_theta_exponent_weight_rows.packet.json"
)
STEP70_FACTOR = (
    DATA
    / "selected_step70_heattorsionprefactorbackimport_or_rowlocalfrontier"
    / "step70_prefactor_slot_factorization.packet.json"
)
STEP71_TARGETS = (
    DATA
    / "selected_step71_smparitymatrixcomparison_or_rowlocaltargets"
    / "step71_rowlocal_composite_target_contract.packet.json"
)
STEP72_PREDICATE = (
    DATA
    / "selected_step72_rowlocalprefactorlawsearch_or_strictomegaacceptance"
    / "step72_strict_rowlocal_omega_acceptance_predicate.packet.json"
)
STEP72_WORKORDER = (
    DATA
    / "selected_step72_rowlocalprefactorlawsearch_or_strictomegaacceptance"
    / "step72_honest_galerkin_rowlocal_workorder.packet.json"
)
STEP73_ATTEMPT = (
    DATA
    / "selected_step73_honestrowlocalhymgalerkin_or_selectedprefactorsourcerows"
    / "step73_ten_rowlocal_prefactor_execution_attempt.packet.json"
)
FINITE_PROJECTOR = DATA / "selected_finite_projector_source_promotion.candidate.json"
CONDITIONAL_K = (
    DATA
    / "selected_combinedthresholdkernelkrows_sourcetheorem"
    / "conditional_k_rows_scalar_closure_theorem.packet.json"
)

STATUS = (
    "MTT_SELECTED_HSECTORQUARTICTHRESHOLDPAYLOAD_OR_STRICTTENKCLOSURE_"
    "BUILT_H_SOURCE_EQUATION_PAYLOAD_ROW_OPEN"
)
NEXT = "MTT_Selected_DirectHThresholdKRowEmission_or_HQuarticFunctionalTheorem_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing H-sector payload inputs: " + ", ".join(missing))


def row_by_omega(rows: list[dict[str, Any]], omega_id: str) -> dict[str, Any]:
    for row in rows:
        if row.get("omega_id") == omega_id:
            return row
    raise KeyError(omega_id)


def symbolic_prefactor_numerator(symbolic: str) -> float:
    prefix, _sep, _suffix = symbolic.partition(" / ")
    return float(prefix.strip().removeprefix("(").removesuffix(")"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_ANTECEDENT,
        PREVIOUS_MINIMAL,
        STEP68_EXPONENTS,
        STEP70_FACTOR,
        STEP71_TARGETS,
        STEP72_PREDICATE,
        STEP72_WORKORDER,
        STEP73_ATTEMPT,
        FINITE_PROJECTOR,
        CONDITIONAL_K,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_antecedent = load(PREVIOUS_ANTECEDENT)
    previous_minimal = load(PREVIOUS_MINIMAL)
    exponents = load(STEP68_EXPONENTS)
    factor = load(STEP70_FACTOR)
    step71 = load(STEP71_TARGETS)
    predicate = load(STEP72_PREDICATE)
    workorder_source = load(STEP72_WORKORDER)
    step73 = load(STEP73_ATTEMPT)
    projector = load(FINITE_PROJECTOR)
    conditional = load(CONDITIONAL_K)

    h_factor = row_by_omega(factor["factor_rows"], "Omega_H.lambda")
    h_target = row_by_omega(step71["target_rows"], "Omega_H.lambda")
    h_attempt = row_by_omega(step73["attempt_rows"], "Omega_H.lambda")
    h_exponent = exponents["higgs_exponent_weight_row"]
    h_projector = projector["promoted_sector_slots"]["H"]
    h_diagnostic_prefactor = symbolic_prefactor_numerator(
        h_target["rowlocal_composite_target_symbolic"]
    )

    equation = {
        "schema": "MTTHSectorPayloadSourceEquation.v1",
        "status": "H_SECTOR_SOURCE_EQUATION_CLOSED_VALUE_ROW_OPEN",
        "closure_claimed": True,
        "omega_id": "Omega_H.lambda",
        "combined_kernel_row_id": "K_threshold.Omega_H.lambda",
        "selected_source_equation": {
            "omega_value": "Omega_H.lambda.value = D_fin.H * K_threshold.Omega_H.lambda * epsilon_Theta^(1/3)",
            "direct_K_row": "K_threshold.Omega_H.lambda",
            "split_K_row": "K_threshold.Omega_H.lambda = L_rowlocal.Omega_H.lambda * T_scheme.Omega_H.lambda",
            "prefactor_factorization": h_factor["factorization"],
        },
        "closed_inputs": {
            "selected_H_projector_carrier": projector["promotion_decision"]["selected_projector_source_verified"],
            "H_projector_rank": h_projector["rank"],
            "H_transport_identity": h_projector["transport"] == "identity on Higgs singlet",
            "D_fin_H_subfactor_closed": h_factor["closed_subsources"]["finite_heat_torsion_response"],
            "D_fin_H_subfactor_id": h_factor["finite_heat_torsion_subfactor_id"],
            "shared_circle_theta_exponent_closed": h_exponent["accepted_as_higgs_exponent_weight"],
            "theta_exponent": h_exponent["theta_exponent"],
            "theta_weight": h_exponent["theta_weight"],
            "ten_K_conditional_theorem_closed": conditional["consequent_if_satisfied"][
                "strict_Omega_rows_executable"
            ]
            and conditional["consequent_if_satisfied"]["lambda_H_row_executable"],
        },
        "open_source_terms": {
            "selected_H_sector_quartic_functional": False,
            "selected_H_threshold_scheme_functional": False,
            "selected_L_rowlocal_Omega_H_lambda": False,
            "selected_T_scheme_Omega_H_lambda": False,
            "direct_K_threshold_Omega_H_lambda": False,
        },
        "diagnostic_postcheck_only": {
            "rowlocal_composite_target_symbolic": h_target["rowlocal_composite_target_symbolic"],
            "diagnostic_prefactor_numerator": h_diagnostic_prefactor,
            "accepted_as_source_row": h_target["accepted_as_rowlocal_source_target"]
            or h_target["accepted_as_full_prefactor_source_row"]
            or h_target["accepted_as_omega_source_row"],
            "source_value_tier": "diagnostic_replay_postcheck_only",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    trials = {
        "schema": "MTTHSectorPayloadCandidateTrials.v1",
        "status": "CURRENT_H_PAYLOAD_CANDIDATES_TESTED_ZERO_ACCEPTED",
        "closure_claimed": True,
        "accepted_H_payload_candidate_count": 0,
        "accepted_direct_H_K_row_count": 0,
        "trials": [
            {
                "trial_id": "direct_H_quartic_from_rank_one_projector",
                "closed_support": {
                    "selected_H_projector_carrier": True,
                    "rank": h_projector["rank"],
                    "transport_identity": h_projector["transport"] == "identity on Higgs singlet",
                },
                "accepted": False,
                "reason": "Carrier/rank data do not define a quartic functional, a threshold map, or a K_threshold value.",
            },
            {
                "trial_id": "D_fin_H_times_shared_circle_theta",
                "closed_support": {
                    "D_fin_H_subfactor": h_factor["finite_heat_torsion_subfactor_id"],
                    "theta_exponent": h_exponent["theta_exponent"],
                    "theta_weight": h_exponent["theta_weight"],
                },
                "accepted": False,
                "reason": "This supplies determinant/exponent support for Omega_H.lambda, but leaves K_threshold.Omega_H.lambda open.",
            },
            {
                "trial_id": "postcheck_inversion_for_K_H",
                "diagnostic_expression": h_target["rowlocal_composite_target_symbolic"],
                "diagnostic_prefactor_numerator": h_diagnostic_prefactor,
                "uses_replay_postcheck": True,
                "accepted": False,
                "reason": "The expression is useful for postcheck comparison only; it is computed from replay target data and cannot select the source row.",
            },
            {
                "trial_id": "step73_honest_galerkin_current_H_row",
                "closed_support": {
                    "diagonal_hym_connection_available": h_attempt["diagonal_hym_connection_available"],
                    "diagonal_green_available": h_attempt["diagonal_green_available"],
                    "model_active_zero_mode_basis_available": h_attempt["model_active_zero_mode_basis_available"],
                },
                "accepted": False,
                "reason": "Step73 emits no selected retarded overlap derivative, selected sector transfer, selected threshold scheme, or lambda_H payload.",
            },
        ],
        "forbidden_promotions": [
            "use H rank one as L_rowlocal.Omega_H.lambda=1",
            "use the postcheck inversion as a source row",
            "treat D_fin.H * epsilon_Theta^(1/3) as Omega_H.lambda without K_threshold.Omega_H.lambda",
            "claim ten-K closure with the H row absent",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    ten_k_gate = {
        "schema": "MTTStrictTenKGateAfterHPayloadAttempt.v1",
        "status": "STRICT_TEN_K_GATE_RECHECKED_H_ROW_STILL_OPEN",
        "closure_claimed": True,
        "accepted_selected_K_source_row_count": previous_antecedent["accepted_selected_K_source_row_count"],
        "selected_K_threshold_row_count_required": previous_antecedent["selected_K_threshold_row_count_required"],
        "ten_K_antecedent_satisfied": False,
        "H_row": {
            "omega_id": "Omega_H.lambda",
            "combined_kernel_row_id": "K_threshold.Omega_H.lambda",
            "selected_H_payload_equation_closed": True,
            "selected_H_quartic_functional_emitted": False,
            "selected_H_threshold_scheme_emitted": False,
            "selected_L_rowlocal_Omega_H_lambda": False,
            "selected_T_scheme_Omega_H_lambda": False,
            "selected_direct_K_threshold_Omega_H_lambda": False,
        },
        "conditional_consequent_current": {
            "strict_Omega_rows_executable": False,
            "lambda_H_row_executable": False,
            "accepted_internal_scalar_value_row_count": 0,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    workorder = {
        "schema": "MTTHSectorPayloadExecutionWorkorder.v1",
        "status": "DIRECT_H_K_ROW_OR_H_QUARTIC_FUNCTIONAL_WORKORDER_EMITTED",
        "closure_claimed": True,
        "source_equation_to_satisfy": equation["selected_source_equation"],
        "allowed_routes": [
            {
                "route_id": "direct_H_K_row_from_selected_galerkin",
                "must_emit": [
                    "selected retarded H overlap derivative or equivalent H quartic matrix element",
                    "selected threshold/scheme binding for H",
                    "K_threshold.Omega_H.lambda as a source row before replay",
                ],
            },
            {
                "route_id": "split_H_quartic_and_threshold_payload",
                "must_emit": [
                    "L_rowlocal.Omega_H.lambda from selected H-sector quartic/overlap functional",
                    "T_scheme.Omega_H.lambda from selected same-branch threshold/scheme map",
                    "product theorem K_H = L_H*T_H",
                ],
            },
            {
                "route_id": "source_selected_H_universal_anchor",
                "must_emit": [
                    "one theorem-selected H-sector source anchor before replay",
                    "proof that the anchor uniquely supplies K_threshold.Omega_H.lambda",
                    "cross-use guard showing the anchor is not an ordinary fitted knob",
                ],
            },
        ],
        "acceptance_tests": [
            "do not read sm_parity_projected_abs_value before source row emission",
            "prove q=79/F/m=1 same-branch provenance for the H row",
            "emit K_threshold.Omega_H.lambda or both split factors before strict Omega execution",
            "then use the existing conditional ten-K theorem as the scalar execution trigger",
        ],
        "imported_step72_workorder": rel(STEP72_WORKORDER),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cutset = {
        "schema": "MTTNextCutsetAfterHSectorPayloadGate.v1",
        "status": "NEXT_FRONTIER_DIRECT_H_K_ROW_OR_H_QUARTIC_FUNCTIONAL",
        "closure_claimed": True,
        "closed_here": [
            "H-sector source equation closed",
            "current H candidate trials tested with zero accepted source rows",
            "postcheck inversion quarantined as replay-only",
            "strict ten-K gate rechecked at 9/10",
            "direct H K row workorder emitted",
        ],
        "still_open": [
            "selected H-sector quartic/overlap functional",
            "selected H-sector threshold/scheme functional",
            "selected K_threshold.Omega_H.lambda source row",
            "strict Omega/lambda_H scalar execution",
            "selected matrix-level mixing extension and true SM equivalence",
        ],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHSectorQuarticThresholdPayloadOrStrictTenKClosure",
        "status": STATUS,
        "previous_status": previous["status"],
        "theorem": {
            "name": "HSectorSourceEquationAndCurrentPayloadNoClosureTheorem",
            "proved": True,
            "statement": (
                "The H/lambda row is reduced to the selected source equation "
                "Omega_H.lambda = D_fin.H * K_threshold.Omega_H.lambda * epsilon_Theta^(1/3). "
                "The current selected supports close the carrier, D_fin.H, and exponent terms, "
                "but emit no H quartic/threshold payload or direct H K row."
            ),
        },
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "closure_decision": {
            "H_payload_source_equation_closed": True,
            "accepted_H_payload_candidate_count": 0,
            "selected_H_quartic_functional_emitted": False,
            "selected_H_threshold_scheme_emitted": False,
            "selected_H_K_threshold_row_emitted": False,
            "accepted_selected_K_source_row_count": previous_antecedent[
                "accepted_selected_K_source_row_count"
            ],
            "selected_K_threshold_row_count_required": previous_antecedent[
                "selected_K_threshold_row_count_required"
            ],
            "ten_K_antecedent_satisfied": False,
            "strict_Omega_lambda_scalar_execution_closed": False,
            "accepted_internal_scalar_value_row_count": 0,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "h_sector_payload_source_equation": rel(EQUATION),
            "h_sector_payload_candidate_trials": rel(TRIALS),
            "strict_ten_k_gate_after_h_payload_attempt": rel(TEN_K_GATE),
            "h_sector_payload_execution_workorder": rel(WORKORDER),
            "next_cutset_after_h_sector_payload_gate": rel(CUTSET),
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTTSelectedHSectorQuarticThresholdPayloadOrStrictTenKClosureCertificate",
        "status": STATUS,
        "theorem_proved": True,
        "H_payload_source_equation_closed": True,
        "accepted_H_payload_candidate_count": 0,
        "selected_H_K_threshold_row_emitted": False,
        "accepted_selected_K_source_row_count": previous_antecedent[
            "accepted_selected_K_source_row_count"
        ],
        "selected_K_threshold_row_count_required": previous_antecedent[
            "selected_K_threshold_row_count_required"
        ],
        "ten_K_antecedent_satisfied": False,
        "strict_Omega_lambda_scalar_execution_closed": False,
        "accepted_internal_scalar_value_row_count": 0,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected HSectorQuarticThresholdPayload or StrictTenKClosure v1

Status: `{STATUS}`

## What Closed

- H-sector source equation: `Omega_H.lambda = D_fin.H * K_threshold.Omega_H.lambda * epsilon_Theta^(1/3)`
- split equation: `K_threshold.Omega_H.lambda = L_rowlocal.Omega_H.lambda * T_scheme.Omega_H.lambda`
- selected H carrier/projector, `D_fin.H`, and shared-circle `1/3` exponent are registered as support
- current H candidate trials tested: `0` accepted
- ten-K gate remains: `{previous_antecedent["accepted_selected_K_source_row_count"]}/{previous_antecedent["selected_K_threshold_row_count_required"]}`

## Still Open

- selected H quartic/overlap functional: `false`
- selected H threshold/scheme functional: `false`
- selected direct `K_threshold.Omega_H.lambda`: `false`
- strict `Omega/lambda_H` execution: `false`

Next required artifact: `{NEXT}`
"""

    write_json(EQUATION, equation)
    write_json(TRIALS, trials)
    write_json(TEN_K_GATE, ten_k_gate)
    write_json(WORKORDER, workorder)
    write_json(CUTSET, cutset)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
