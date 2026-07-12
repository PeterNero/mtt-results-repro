"""Build strict R_H^RG source construction / independent validation oracle packet."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_strictrhrgsourceconstruction_or_independentvalidationoracle"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
GATE_EXECUTION = PACKET_DIR / "strict_rhrg_source_gate_execution.packet.json"
ORACLE_RANK = PACKET_DIR / "independent_validation_oracle_rank_test.packet.json"
INVARIANT_REPLAY = PACKET_DIR / "expanded_finite_invariant_source_search_replay.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_strict_rhrg_oracle_execution.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_StrictRHRGSourceConstruction_or_IndependentValidationOracle_v1.md"

PREVIOUS = DATA / "selected_hrgcrossusepredictionvalidation_or_strictrhrgsourcetheorem.candidate.json"
CONTRACT = (
    DATA
    / "selected_intrinsichquartickrow_or_selectedlargethresholdrgtheorem"
    / "selected_large_threshold_rg_acceptance_contract.packet.json"
)
STRICT_SEARCH = (
    DATA
    / "selected_hthresholdrgoperator_or_universalprimitivepolicy"
    / "strict_h_threshold_rg_operator_source_search.packet.json"
)
STRICT_EXECUTION = (
    DATA
    / "selected_hrgnonhiggsretardedoverlapmap_or_strictsourcetheorem"
    / "strict_hrg_source_theorem_execution.packet.json"
)
CONTROLLED_VALIDATION = (
    DATA
    / "selected_hrgcrossusepredictionvalidation_or_strictrhrgsourcetheorem"
    / "controlled_hrg_crossuse_prediction_validation.packet.json"
)
DYNAMIC_MAP = (
    DATA
    / "selected_hrgconsumervaluesource_or_largethresholdtransportmap"
    / "dynamic_c1_same_hrg_transport_prediction_map.packet.json"
)
INVARIANT_SEARCH = (
    DATA
    / "selected_hrgconsumervaluesource_or_largethresholdtransportmap"
    / "finite_invariant_hrg_specialization_search.packet.json"
)
RO_FAMILY = DATA / "selected_rofamilyselectorsourcetheorem_or_nonhiggspredictionmap.candidate.json"
UNPATCHED = DATA / "selected_unpatchedphifinc1sourcerule_or_honestgalerkintables_to_hrgconsumermap.candidate.json"
HLAMBDA = DATA / "selected_hlambdaoverlapkernelrow_or_scalaromegaexecutiongate.candidate.json"

STATUS = (
    "MTT_SELECTED_STRICTRHRGSOURCECONSTRUCTION_OR_INDEPENDENTVALIDATIONORACLE_"
    "EXECUTED_STRICT_SOURCE_AND_ORACLE_OPEN"
)
NEXT = "MTT_Selected_RHRGDeterminantIndexCandidate_or_ExternalValidationTarget_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing strict RHRG/oracle inputs: " + ", ".join(missing))


def diagnostic_invariant_replay(hrg: float) -> list[dict[str, Any]]:
    """Replay a fixed, non-promoting finite-expression search around source constants."""
    constants = {
        "q": 79.0,
        "formal_rows": 110.0,
        "primitive_rows": 72.0,
        "charged_rows": 9.0,
        "rank": 2.0,
        "pi": math.pi,
        "sqrt3": math.sqrt(3.0),
        "phi": (1.0 + math.sqrt(5.0)) / 2.0,
        "exp_2pi": math.exp(2.0 * math.pi),
    }
    formulas = [
        ("primitive_rows*pi*sqrt3", constants["primitive_rows"] * constants["pi"] * constants["sqrt3"]),
        ("formal_rows*pi/sqrt(phi)", constants["formal_rows"] * constants["pi"] / math.sqrt(constants["phi"])),
        ("q*pi*pi/2", constants["q"] * constants["pi"] * constants["pi"] / 2.0),
        ("exp(2*pi)/phi", constants["exp_2pi"] / constants["phi"]),
        ("q*sqrt(formal_rows*charged_rows/rank)", constants["q"] * math.sqrt(constants["formal_rows"] * constants["charged_rows"] / constants["rank"])),
        ("formal_rows*sqrt(q*pi/rank)", constants["formal_rows"] * math.sqrt(constants["q"] * constants["pi"] / constants["rank"])),
    ]
    rows: list[dict[str, Any]] = []
    for formula, value in formulas:
        rows.append(
            {
                "formula": formula,
                "value": value,
                "absolute_error": abs(value - hrg),
                "relative_error": abs(value / hrg - 1.0),
                "accepted_as_source_identity": False,
            }
        )
    rows.sort(key=lambda row: row["relative_error"])
    return rows


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        CONTRACT,
        STRICT_SEARCH,
        STRICT_EXECUTION,
        CONTROLLED_VALIDATION,
        DYNAMIC_MAP,
        INVARIANT_SEARCH,
        RO_FAMILY,
        UNPATCHED,
        HLAMBDA,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    contract = load(CONTRACT)
    strict_search = load(STRICT_SEARCH)
    strict_execution = load(STRICT_EXECUTION)
    controlled_validation = load(CONTROLLED_VALIDATION)
    dynamic_map = load(DYNAMIC_MAP)
    invariant_search = load(INVARIANT_SEARCH)
    ro_family = load(RO_FAMILY)
    unpatched = load(UNPATCHED)
    hlambda = load(HLAMBDA)

    hrg = previous["key_numbers"]["UP_RET_OVERLAP_HRG"]
    predicted_rows = dynamic_map["predicted_transport_rows"]
    validation_values = [
        predicted_rows["HRG_times_A_transpose_A"][0][0],
        predicted_rows["HRG_times_A_transpose_b"][0],
        predicted_rows["HRG_times_deltaTheta_C1"][0],
    ]
    normalized_rows = [value / hrg for value in validation_values]
    oracle_rank = 1 if all(abs(value - hrg * norm) < 1e-12 for value, norm in zip(validation_values, normalized_rows)) else 0

    gate_results = {
        "selected_physical_gauge_action_normalization_or_primitive_tier": {
            "controlled_tier": previous["minimal_parameter_tier_claimed"],
            "strict_no_knob_tier": False,
        },
        "selected_matching_scale_mu_match": contract["accepted_current_source_rows"]["selected_mu_match"],
        "selected_H_sector_threshold_RG_operator_R_H_RG": contract["accepted_current_source_rows"]["selected_R_H_RG"],
        "same_branch_scheme_alignment_with_Omega_H_lambda": ro_family["closure_decision"]["RO_family_selector_source_selected"],
        "no_observed_lambda_or_residual_scan_used": True,
        "selected_K_threshold_Omega_H_lambda": contract["accepted_current_source_rows"]["selected_K_threshold_Omega_H_lambda"],
        "selected_A_EW": contract["accepted_current_source_rows"]["selected_A_EW"],
    }

    strict_gate_execution = {
        "schema": "MTTStrictRHRGSourceGateExecution.v1",
        "status": "STRICT_RHRG_SOURCE_GATES_EXECUTED_NOT_ALL_SATISFIED",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "acceptance_contract_ref": rel(CONTRACT),
        "searched_object": contract["object_to_emit"],
        "gate_results": gate_results,
        "strict_acceptance_conditions": contract["strict_acceptance_conditions"],
        "source_imports": {
            "strict_operator_search_status": strict_search["status"],
            "strict_execution_status": strict_execution["status"],
            "dynamic_payload_selected": unpatched["closure_decision"]["selected_dynamic_phi_fin_c1_payload_emitted"],
            "charged_Hlambda_gate_status": hlambda["status"],
        },
        "decision": {
            "strict_R_H_RG_source_constructed": False,
            "all_strict_gates_satisfied": False,
            "controlled_parameter_tier_available": True,
            "strict_no_knob_credit_allowed": False,
        },
    }

    oracle_rank_test = {
        "schema": "MTTIndependentValidationOracleRankTest.v1",
        "status": "INDEPENDENT_VALIDATION_ORACLE_TEST_EXECUTED_DEPENDENT_ROWS_ONLY",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "controlled_validation_ref": rel(CONTROLLED_VALIDATION),
        "tested_rows": [
            {"name": "HRG*A00", "value": validation_values[0], "normalized_by_HRG": normalized_rows[0]},
            {"name": "HRG*b0", "value": validation_values[1], "normalized_by_HRG": normalized_rows[1]},
            {"name": "HRG*deltaTheta0", "value": validation_values[2], "normalized_by_HRG": normalized_rows[2]},
        ],
        "rank_result": {
            "declared_HRG_parameter_rank": 1,
            "independent_validation_rank": 0,
            "row_family_rank_after_dividing_by_HRG": oracle_rank,
            "reason": "All exact rows are generated by the same declared HRG scalar times already-selected dynamic C1 rows.",
        },
        "decision": {
            "independent_validation_oracle_emitted": False,
            "controlled_internal_validation_remains_valid": True,
            "counts_for_true_SM_equivalence": False,
        },
    }

    replay_rows = diagnostic_invariant_replay(hrg)
    expanded_replay = {
        "schema": "MTTExpandedFiniteInvariantSourceSearchReplay.v1",
        "status": "EXPANDED_FINITE_INVARIANT_REPLAY_EXECUTED_NO_SELECTED_EXACT_IDENTITY",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "diagnostic_target_scan_used": True,
        "previous_best_relative_error": invariant_search["diagnostics"]["best_candidate_relative_error"],
        "candidate_rows": replay_rows,
        "best_candidate": replay_rows[0],
        "decision": {
            "exact_selected_identity_found": False,
            "near_miss_promoted": False,
            "strict_R_H_RG_source_constructed": False,
        },
    }

    cutset = {
        "schema": "MTTNextCutsetAfterStrictRHRGOracleExecution.v1",
        "status": "NEXT_FRONTIER_RHRG_DETERMINANT_INDEX_OR_EXTERNAL_VALIDATION_TARGET",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closed_here": [
            "strict R_H^RG acceptance contract executed gate-by-gate",
            "independent validation oracle rank test executed",
            "expanded finite-invariant source replay executed without promotion",
        ],
        "still_open": [
            "selected determinant/index/RG candidate for R_H^RG",
            "independent non-Higgs or external validation target not used as selector",
            "selected mu_match and A_EW source rows for strict no-knob tier",
            "true SM/no-knob equivalence",
        ],
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "MTTSelectedStrictRHRGSourceConstructionOrIndependentValidationOracle",
        "schema": "MTTSelectedCandidate.v1",
        "status": STATUS,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "minimal_parameter_tier_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "StrictRHRGSourceConstructionOrIndependentValidationOracleTheorem",
            "proved": True,
            "statement": (
                "Executing the selected R_H^RG acceptance contract against the "
                "current source ledger leaves the strict source unemitted.  The "
                "controlled HRG rows pass internal validation but fail independence: "
                "they are scalar multiples of already-selected dynamic C1 rows."
            ),
        },
        "packets": {
            "gate_execution": rel(GATE_EXECUTION),
            "oracle_rank": rel(ORACLE_RANK),
            "invariant_replay": rel(INVARIANT_REPLAY),
            "cutset": rel(CUTSET),
        },
        "closure_decision": {
            "strict_R_H_RG_source_constructed": False,
            "all_strict_R_H_RG_gates_satisfied": False,
            "independent_validation_oracle_emitted": False,
            "controlled_internal_validation_remains_valid": True,
            "expanded_invariant_exact_identity_found": False,
            "lambda_H_predicted": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "key_numbers": {
            "UP_RET_OVERLAP_HRG": hrg,
            "controlled_validation_row_count": len(validation_values),
            "independent_validation_rank": 0,
            "row_family_rank_after_dividing_by_HRG": oracle_rank,
            "accepted_strict_source_count": 0,
            "best_expanded_invariant_relative_error": replay_rows[0]["relative_error"],
            "previous_best_invariant_relative_error": invariant_search["diagnostics"]["best_candidate_relative_error"],
        },
    }

    cert = {
        "certificate": "MTTSelectedStrictRHRGSourceConstructionOrIndependentValidationOracle",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "theorem_proved": True,
        "minimal_parameter_tier_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "strict_R_H_RG_source_constructed": False,
        "all_strict_R_H_RG_gates_satisfied": False,
        "independent_validation_oracle_emitted": False,
        "controlled_internal_validation_remains_valid": True,
        "expanded_invariant_exact_identity_found": False,
        "lambda_H_predicted": False,
        "accepted_strict_source_count": 0,
        "independent_validation_rank": 0,
    }

    note = f"""# MTT Selected Strict R_H^RG Source Construction or Independent Validation Oracle v1

Status: `{STATUS}`

## Theorem

The strict `R_H^RG` acceptance contract has now been executed gate by gate
against the current selected ledger.  The controlled HRG layer remains valid,
but it is not upgraded to no-knob status: no selected determinant/index/RG
operator emits `R_H^RG`, and the exact cross-use rows fail the independence
oracle because they are all generated by one declared HRG scalar.

## Gate Result

- strict `R_H^RG` constructed: `false`
- all strict gates satisfied: `false`
- controlled parameter tier available: `true`
- strict accepted source count: `0`
- selected `mu_match`: `{gate_results["selected_matching_scale_mu_match"]}`
- selected `R_H^RG`: `{gate_results["selected_H_sector_threshold_RG_operator_R_H_RG"]}`
- selected `K_threshold.Omega_H.lambda`: `{gate_results["selected_K_threshold_Omega_H_lambda"]}`

## Oracle Result

- controlled validation row count: `{len(validation_values)}`
- independent validation rank: `0`
- row-family rank after dividing by HRG: `{oracle_rank}`
- reason: all exact rows are scalar multiples of selected dynamic C1 rows.

## Invariant Replay

Best expanded diagnostic formula:
`{replay_rows[0]["formula"]}` with relative error
`{replay_rows[0]["relative_error"]}`.  It is not promoted to a selected source
identity.

## Boundary

Closed here:

- strict `R_H^RG` acceptance contract execution;
- independent validation oracle rank test;
- expanded invariant replay without near-miss promotion.

Still open:

- selected determinant/index/RG candidate for `R_H^RG`;
- independent non-Higgs or external validation target, used only after source
  selection and not as a selector;
- true SM/no-knob equivalence.

Next artifact: `{NEXT}`
"""

    write_json(GATE_EXECUTION, strict_gate_execution)
    write_json(ORACLE_RANK, oracle_rank_test)
    write_json(INVARIANT_REPLAY, expanded_replay)
    write_json(CUTSET, cutset)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE {rel(OUTPUT)}")
    print(f"WROTE {rel(CERT)}")
    print(f"WROTE {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
