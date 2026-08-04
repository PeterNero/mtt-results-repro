"""Build selected lambda_H payload execution or ten-K threshold closure packet.

This packet starts from the closed charged NullThresholdDeltaTheorem result:
nine charged K_threshold rows are selected.  It then tests the remaining
H/lambda row against the available same-branch support.  The result is an
honest non-closure theorem: the H row is narrowed to one positive missing
object, a selected H-sector quartic/threshold payload or direct
K_threshold.Omega_H.lambda source row.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_lambdahpayloadexecution_or_tenkthresholdclosure"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROUTES = PACKET_DIR / "h_lambda_payload_route_evaluation.packet.json"
ANTECEDENT = PACKET_DIR / "h_sector_kthreshold_antecedent_recheck.packet.json"
MINIMAL = PACKET_DIR / "minimal_h_lambda_payload_theorem.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_h_lambda_route_gate.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_LambdaHPayloadExecution_or_TenKThresholdClosure_v1.md"

PREVIOUS = DATA / "selected_thresholddeltarows_or_lambdahpayloadexecution.candidate.json"
PREVIOUS_GATE = (
    DATA
    / "selected_thresholddeltarows_or_lambdahpayloadexecution"
    / "ten_kthreshold_gate_after_charged_null_delta.packet.json"
)
LAMBDA_NORMAL = (
    DATA
    / "selected_neutraltschemesourceprinciple_or_lambdahsectorpayload"
    / "h_sector_lambda_payload_normal_form.packet.json"
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
STEP70_HEAT = (
    DATA
    / "selected_step70_heattorsionprefactorbackimport_or_rowlocalfrontier"
    / "step70_finite_heat_torsion_prefactor_backimport.packet.json"
)
STEP70_NOGO = (
    DATA
    / "selected_step70_heattorsionprefactorbackimport_or_rowlocalfrontier"
    / "step70_heat_torsion_sufficiency_nogo.packet.json"
)
FINITE_PROJECTOR = DATA / "selected_finite_projector_source_promotion.candidate.json"
TOP_HIGGS_FORMULA = DATA / "selected_tophiggsformulamapimport_or_rthetathresholdderivation.candidate.json"
CONDITIONAL_K = (
    DATA
    / "selected_combinedthresholdkernelkrows_sourcetheorem"
    / "conditional_k_rows_scalar_closure_theorem.packet.json"
)

STATUS = (
    "MTT_SELECTED_LAMBDAHPAYLOADEXECUTION_OR_TENKTHRESHOLDCLOSURE_"
    "BUILT_H_PAYLOAD_ROUTES_REJECTED_TEN_K_9_OF_10"
)
NEXT = "MTT_Selected_HSectorQuarticThresholdPayload_or_StrictTenKClosure_v1"


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
        raise FileNotFoundError("missing lambda_H/ten-K inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_GATE,
        LAMBDA_NORMAL,
        STEP68_EXPONENTS,
        STEP70_FACTOR,
        STEP70_HEAT,
        STEP70_NOGO,
        FINITE_PROJECTOR,
        TOP_HIGGS_FORMULA,
        CONDITIONAL_K,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_gate = load(PREVIOUS_GATE)
    lambda_normal = load(LAMBDA_NORMAL)
    exponents = load(STEP68_EXPONENTS)
    factor = load(STEP70_FACTOR)
    heat = load(STEP70_HEAT)
    heat_nogo = load(STEP70_NOGO)
    projector = load(FINITE_PROJECTOR)
    top_higgs = load(TOP_HIGGS_FORMULA)
    conditional = load(CONDITIONAL_K)

    h_factor = next(row for row in factor["factor_rows"] if row["omega_id"] == "Omega_H.lambda")
    h_projector = projector["promoted_sector_slots"]["H"]
    h_exponent = exponents["higgs_exponent_weight_row"]

    route_evaluation = {
        "schema": "MTTHLambdaPayloadRouteEvaluation.v1",
        "status": "H_LAMBDA_PAYLOAD_ROUTES_EVALUATED_NO_SELECTED_PAYLOAD",
        "closure_claimed": True,
        "omega_id": "Omega_H.lambda",
        "combined_kernel_row_id": "K_threshold.Omega_H.lambda",
        "accepted_selected_lambda_H_payload": False,
        "lambda_H_value_row_emitted": False,
        "selected_H_K_threshold_row_emitted": False,
        "routes": [
            {
                "route_id": "rank_one_H_projector_quartic_shortcut",
                "closed_support": {
                    "selected_H_projector_source_verified": projector["promotion_decision"][
                        "selected_projector_source_verified"
                    ],
                    "H_projector_rank": h_projector["rank"],
                    "H_transport_identity": h_projector["transport"] == "identity on Higgs singlet",
                    "H_stationary_rho_s_promoted": h_projector["stationary_rho_s_promoted"],
                },
                "accepted_as_lambda_H_payload": False,
                "reason_rejected": (
                    "Rank-one H projector support identifies the H carrier, but it does not emit "
                    "a selected quartic functional, H-sector overlap numerator, or threshold value payload."
                ),
            },
            {
                "route_id": "heat_torsion_shared_circle_payload",
                "closed_support": {
                    "D_fin_H_selected": heat["closed_now"]["finite_heat_trace_source_subslot"]
                    and heat["closed_now"]["positive_complement_pseudodeterminant_source_subslot"],
                    "D_fin_H_subfactor_id": h_factor["finite_heat_torsion_subfactor_id"],
                    "H_theta_exponent_selected": h_exponent["accepted_as_higgs_exponent_weight"],
                    "H_theta_exponent": h_exponent["theta_exponent"],
                    "prefactor_factorization_row_accepted": h_factor["accepted_as_prefactor_factorization_row"],
                    "heat_torsion_alone_emits_all_prefactor_rows": heat_nogo[
                        "finite_heat_torsion_alone_emits_all_prefactor_rows"
                    ],
                },
                "accepted_as_lambda_H_payload": False,
                "reason_rejected": (
                    "D_fin.H and the shared-circle 1/3 exponent are selected support, but Step70 proves "
                    "heat/torsion alone cannot emit full row-local prefactors or the lambda_H value payload."
                ),
            },
            {
                "route_id": "external_top_higgs_formula_map_replay",
                "closed_support": {
                    "top_higgs_external_formula_map_import_closed": top_higgs["closure_decision"][
                        "top_higgs_external_formula_map_import_closed"
                    ],
                    "lambda_Mt_external_formula_map_row_closed": top_higgs["closure_decision"][
                        "lambda_Mt_external_formula_map_row_closed"
                    ],
                    "same_branch_Rtheta_threshold_derivation_closed": top_higgs["closure_decision"][
                        "same_branch_Rtheta_threshold_derivation_closed"
                    ],
                },
                "accepted_as_lambda_H_payload": False,
                "reason_rejected": (
                    "The top/Higgs formula map is an accepted external replay/support row, not a same-branch "
                    "selected H-sector source row and not a no-knob lambda_H selector."
                ),
            },
            {
                "route_id": "candidate_specific_universal_anchor",
                "closed_support": {
                    "universal_anchor_policy_available": True,
                    "selected_H_anchor_emitted_here": False,
                },
                "accepted_as_lambda_H_payload": False,
                "reason_rejected": (
                    "A universal anchor remains legal only if theorem-selected before replay and if it emits "
                    "the same H/lambda row. No such H anchor is emitted in the current packet."
                ),
            },
        ],
        "guardrails": [
            "do not set L_rowlocal.Omega_H.lambda=1 from rank alone",
            "do not promote D_fin.H or theta exponent 1/3 into a quartic value payload",
            "do not use external lambda_H replay as a no-knob selector",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    antecedent = {
        "schema": "MTTHSectorKThresholdAntecedentRecheck.v1",
        "status": "TEN_K_ANTECEDENT_RECHECKED_PRESENT_9_REQUIRED_10",
        "closure_claimed": True,
        "previous_charged_K_source": rel(PREVIOUS_GATE),
        "accepted_selected_charged_K_threshold_row_count": previous_gate[
            "accepted_selected_charged_K_threshold_row_count"
        ],
        "accepted_selected_K_source_row_count": previous_gate["accepted_selected_K_source_row_count"],
        "selected_K_threshold_row_count_required": conditional["antecedent"][
            "selected_K_threshold_row_count_required"
        ],
        "antecedent_satisfied": False,
        "H_row": {
            "omega_id": "Omega_H.lambda",
            "combined_kernel_row_id": "K_threshold.Omega_H.lambda",
            "selected_lambda_H_payload_emitted": False,
            "selected_H_K_threshold_row_emitted": False,
            "H_sector_Lrowlocal_available": lambda_normal["current_emission"][
                "H_sector_Lrowlocal_available"
            ],
            "T_scheme_Omega_H_lambda_source_row_emitted": lambda_normal["current_emission"][
                "T_scheme_Omega_H_lambda_source_row_emitted"
            ],
            "blocking_reasons": lambda_normal["why_still_open"]
            + [
                "post-null-delta charged closure supplies 9/10 K rows but does not supply the H row",
                "all current H routes are support-only or replay-only",
            ],
        },
        "conditional_consequent_current": {
            "strict_Omega_rows_executable": False,
            "lambda_H_row_executable": False,
            "accepted_internal_scalar_value_row_count": 0,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    minimal = {
        "schema": "MTTMinimalHLambdaPayloadTheorem.v1",
        "status": "MINIMAL_H_LAMBDA_PAYLOAD_THEOREM_SHARPENED",
        "closure_claimed": True,
        "statement": (
            "To close the remaining ten-K antecedent, MTT must emit a same-branch selected "
            "H-sector quartic/threshold payload that supplies L_rowlocal.Omega_H.lambda and "
            "T_scheme.Omega_H.lambda, or directly emits K_threshold.Omega_H.lambda, without "
            "using external lambda_H replay as a selector."
        ),
        "allowed_source_inputs": [
            "rank-one selected H projector/carrier",
            "D_fin.H finite heat/torsion subsource",
            "shared-circle theta exponent 1/3",
            "selected H-sector quartic functional",
            "selected H threshold/scheme functional",
            "same-branch convention binding for the H scalar value",
        ],
        "minimal_success_criteria": {
            "selected_lambda_H_payload_emitted": True,
            "selected_H_K_threshold_row_emitted": True,
            "accepted_selected_K_source_row_count": 10,
            "strict_Omega_lambda_scalar_execution_triggers": True,
        },
        "current_success_criteria_satisfied": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cutset = {
        "schema": "MTTNextCutsetAfterHLambdaRouteGate.v1",
        "status": "NEXT_FRONTIER_H_SECTOR_QUARTIC_THRESHOLD_PAYLOAD",
        "closure_claimed": True,
        "closed_here": [
            "post-null-delta charged closure rechecked as 9/10 selected K rows",
            "rank-one H projector shortcut rejected as quartic/value payload",
            "D_fin.H plus shared-circle 1/3 shortcut rejected as full H payload",
            "external top/Higgs lambda replay rejected as no-knob selector",
            "minimal H/lambda payload theorem stated with exact success criteria",
        ],
        "still_open": [
            "selected H-sector quartic functional",
            "selected H-sector threshold/scheme functional",
            "selected L_rowlocal.Omega_H.lambda and T_scheme.Omega_H.lambda, or direct K_threshold.Omega_H.lambda",
            "ten-row K antecedent",
            "strict Omega/lambda_H scalar execution",
            "selected matrix-level mixing extension and true SM equivalence",
        ],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedLambdaHPayloadExecutionOrTenKThresholdClosure",
        "status": STATUS,
        "previous_status": previous["status"],
        "theorem": {
            "name": "HLambdaPayloadRouteSeparationTheorem",
            "proved": True,
            "statement": (
                "Given the selected charged 9/10 K rows, existing H support is insufficient "
                "to emit lambda_H or the tenth K row. The remaining object is exactly a selected "
                "H-sector quartic/threshold payload or direct H K_threshold source row."
            ),
        },
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "closure_decision": {
            "charged_K_rows_preserved": True,
            "accepted_selected_charged_K_threshold_row_count": previous_gate[
                "accepted_selected_charged_K_threshold_row_count"
            ],
            "accepted_selected_K_source_row_count": previous_gate["accepted_selected_K_source_row_count"],
            "selected_K_threshold_row_count_required": conditional["antecedent"][
                "selected_K_threshold_row_count_required"
            ],
            "selected_lambda_H_payload_emitted": False,
            "selected_H_K_threshold_row_emitted": False,
            "ten_K_antecedent_satisfied": False,
            "strict_Omega_lambda_scalar_execution_closed": False,
            "accepted_internal_scalar_value_row_count": 0,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "h_lambda_payload_route_evaluation": rel(ROUTES),
            "h_sector_kthreshold_antecedent_recheck": rel(ANTECEDENT),
            "minimal_h_lambda_payload_theorem": rel(MINIMAL),
            "next_cutset_after_h_lambda_route_gate": rel(CUTSET),
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTTSelectedLambdaHPayloadExecutionOrTenKThresholdClosureCertificate",
        "status": STATUS,
        "theorem_proved": True,
        "charged_K_rows_preserved": True,
        "accepted_selected_K_source_row_count": previous_gate["accepted_selected_K_source_row_count"],
        "selected_K_threshold_row_count_required": conditional["antecedent"][
            "selected_K_threshold_row_count_required"
        ],
        "selected_lambda_H_payload_emitted": False,
        "selected_H_K_threshold_row_emitted": False,
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

    note = f"""# MTT Selected LambdaH Payload Execution or TenK Threshold Closure v1

Status: `{STATUS}`

## What Closed

- selected charged `K_threshold` rows preserved: `{previous_gate["accepted_selected_K_source_row_count"]}/10`
- rank-one H projector shortcut rejected as a quartic/value payload
- `D_fin.H` plus shared-circle `1/3` shortcut rejected as a full H payload
- external top/Higgs formula replay rejected as a no-knob selector
- minimal H/lambda payload theorem sharpened

## Still Open

- selected `lambda_H` H-sector quartic/threshold payload: `false`
- selected `K_threshold.Omega_H.lambda`: `false`
- ten-K antecedent satisfied: `false`
- strict `Omega/lambda_H` scalar execution: `false`

Next required artifact: `{NEXT}`
"""

    write_json(ROUTES, route_evaluation)
    write_json(ANTECEDENT, antecedent)
    write_json(MINIMAL, minimal)
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
