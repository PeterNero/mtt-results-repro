"""Build dynamic retarded-overlap row attempt from selected first-response matrices.

This artifact tests the next tempting shortcut after physical dotD and
stationary sector transfer are imported into the K-row frontier: promote the
selected first dynamic matter/overlap matrices directly to the scalar
row-local retarded-overlap derivative rows.

The selected matrices are retained as real same-source support, but the scalar
K_threshold row evaluator is not emitted by them.  The missing object is the
rowwise scalar quadrature/evaluator, plus T_scheme and lambda_H execution.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_dynamicretardedoverlapderivativerows_or_tschemelambdahsourceexecution"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PROMOTION_ATTEMPT = PACKET_DIR / "dynamic_matrix_to_scalar_retarded_row_promotion_attempt.packet.json"
MISSING_EVALUATOR = PACKET_DIR / "rowwise_scalar_evaluator_missing.packet.json"
EMISSION = PACKET_DIR / "dynamic_retarded_row_emission_attempt.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_dynamic_retarded_row_attempt.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_DynamicRetardedOverlapDerivativeRows_or_TSchemeLambdaHSourceExecution_v1.md"

PREVIOUS = DATA / "selected_physicaldotdalpha1sectortransferretardedoverlapkernel_or_empiricalkparityimport.candidate.json"
PREVIOUS_READINESS = (
    DATA
    / "selected_physicaldotdalpha1sectortransferretardedoverlapkernel_or_empiricalkparityimport"
    / "retarded_overlap_kernel_readiness_after_stationary_transfer.packet.json"
)
K_GRAMMAR = DATA / "selected_combinedthresholdkernelkrows_sourcetheorem" / "closed_source_k_threshold_grammar.packet.json"
DYNAMIC_MATTER = DATA / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure.candidate.json"
DYNAMIC_PACKET = (
    DATA
    / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure"
    / "same_source_matter_overlap_operator_packet.packet.json"
)
DYNAMIC_NONSCALAR = (
    DATA
    / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure"
    / "selected_non_scalar_dynamic_overlap_values.packet.json"
)
DYNAMIC_GUARDRAIL = (
    DATA
    / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure"
    / "full_sm_yukawa_guardrail_after_dynamic_overlap.packet.json"
)
ROWLOCAL_FUNCTIONAL = (
    DATA
    / "selected_rowlocalhymoverlapquadraturefunctional_or_thresholdschemesourcetheorem"
    / "selected_overlap_quadrature_functional.packet.json"
)
THRESHOLD_GATE = (
    DATA
    / "selected_rowlocalhymoverlapquadraturefunctional_or_thresholdschemesourcetheorem"
    / "threshold_scheme_source_gate.packet.json"
)
EMPIRICAL_K = (
    DATA
    / "selected_lrowlocaltschemelambdah_sourceexecution_or_controlledempiricalimport"
    / "controlled_empirical_k_import_contract.packet.json"
)

STATUS = (
    "MTT_SELECTED_DYNAMICRETARDEDOVERLAPDERIVATIVEROWS_OR_TSCHEMELAMBDAHSOURCEEXECUTION_"
    "BUILT_MATRIX_SUPPORT_SCALAR_EVALUATOR_OPEN"
)
NEXT = "MTT_Selected_RowwiseScalarRetardedOverlapQuadratureValues_or_TSchemeLambdaHExecution_v1"


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
        raise FileNotFoundError("missing dynamic retarded-row inputs: " + ", ".join(missing))


def row_attempts(grammar_rows: list[dict[str, Any]], matrix_sectors: set[str]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for row in grammar_rows:
        sector = row["sector"]
        matrix_support = sector in matrix_sectors
        is_higgs = sector == "H"
        rows.append(
            {
                "omega_id": row["omega_id"],
                "combined_kernel_row_id": row["combined_kernel_row_id"],
                "sector": sector,
                "generation_or_lambda": row["generation_or_lambda"],
                "selected_dynamic_matrix_support_available": matrix_support,
                "selected_dynamic_matrix_can_supply_scalar_retarded_row": False,
                "selected_rowwise_scalar_quadrature_evaluator_emitted": False,
                "selected_retarded_overlap_derivative_row_emitted": False,
                "selected_T_scheme_row_emitted": False,
                "selected_lambda_H_payload_emitted": False if is_higgs else None,
                "selected_K_threshold_row_emitted": False,
                "accepted_as_no_knob_source_row": False,
                "blocking_reasons": [
                    "selected first-response matrices are same-source support, not scalar row-local K_threshold values",
                    "rowwise scalar quadrature <K_s,g, K_row K_s,g> has not been executed in selected ordered bases",
                    "selected T_scheme row is not instantiated",
                ]
                + (["H/lambda row has no selected dynamic matter matrix support and no lambda_H payload"] if is_higgs else []),
                "observed_data_used_as_selector": False,
                "target_fitting_used": False,
            }
        )
    return rows


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_READINESS,
        K_GRAMMAR,
        DYNAMIC_MATTER,
        DYNAMIC_PACKET,
        DYNAMIC_NONSCALAR,
        DYNAMIC_GUARDRAIL,
        ROWLOCAL_FUNCTIONAL,
        THRESHOLD_GATE,
        EMPIRICAL_K,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_readiness = load(PREVIOUS_READINESS)
    grammar = load(K_GRAMMAR)
    dynamic_matter = load(DYNAMIC_MATTER)
    dynamic_packet = load(DYNAMIC_PACKET)
    dynamic_nonscalar = load(DYNAMIC_NONSCALAR)
    dynamic_guardrail = load(DYNAMIC_GUARDRAIL)
    rowlocal_functional = load(ROWLOCAL_FUNCTIONAL)
    threshold_gate = load(THRESHOLD_GATE)
    empirical_k = load(EMPIRICAL_K)

    matrix_sectors = set(dynamic_nonscalar["sector_first_responses"].keys())
    k_sectors = {row["sector"] for row in grammar["grammar_rows"]}
    charged_k_sectors = {sector for sector in k_sectors if sector != "H"}
    charged_k_sectors_with_matrix_support = sorted(charged_k_sectors.intersection(matrix_sectors))
    rows = row_attempts(grammar["grammar_rows"], matrix_sectors)

    promotion_attempt = {
        "schema": "MTTDynamicMatrixToScalarRetardedRowPromotionAttempt.v1",
        "status": "SELECTED_DYNAMIC_MATRICES_AVAILABLE_NOT_SCALAR_RETARDED_ROWS",
        "selected_dynamic_packet_status": dynamic_matter["status"],
        "operator_packet_status": dynamic_packet["status"],
        "non_scalar_value_status": dynamic_nonscalar["status"],
        "value_role": dynamic_nonscalar["value_role"],
        "matrix_sectors_available": sorted(matrix_sectors),
        "k_sectors_required": sorted(k_sectors),
        "charged_k_sectors_with_matrix_support": charged_k_sectors_with_matrix_support,
        "higgs_lambda_matrix_support_available": "H" in matrix_sectors,
        "first_response_support_closes": {
            "operator_values_selected_emitted": dynamic_matter["what_closes_now"]["operator_values_selected_emitted"],
            "primitive_C1_contractions_selected_emitted_first_response_layer": dynamic_matter["what_closes_now"][
                "primitive_C1_contractions_selected_emitted_first_response_layer"
            ],
            "same_source_dynamic_matter_overlap_packet_validates": dynamic_matter["what_closes_now"][
                "same_source_dynamic_matter_overlap_packet_validates"
            ],
            "dynamic_value_acceptance_tests_pass_conditionally": dynamic_nonscalar["acceptance_tests"][
                "current_layer_flavor_tests_pass_conditionally"
            ],
            "qualitative_non_scalar_tests_pass": dynamic_nonscalar["guardrail"][
                "qualitative_non_scalar_tests_pass"
            ],
        },
        "guardrails": {
            "Yukawa_magnitudes_predicted": dynamic_nonscalar["guardrail"]["Yukawa_magnitudes_predicted"],
            "full_mass_spectrum_predicted": dynamic_nonscalar["guardrail"]["full_mass_spectrum_predicted"],
            "CKM_PMNS_measured_angles_predicted": dynamic_nonscalar["guardrail"][
                "CKM_PMNS_measured_angles_predicted"
            ],
            "full_SM_no_knob_closed": dynamic_guardrail["not_closed_here"]["full_SM_no_knob_closure"] is False,
        },
        "promotion_result": {
            "matrix_support_accepted_as_same_source_support": True,
            "matrix_support_promoted_to_scalar_retarded_rows": False,
            "reason": (
                "The packet emits selected non-scalar first-response matrices.  The K-row obligation is a scalar "
                "row-local quadrature value for each omega slot, plus T_scheme/lambda_H.  No selected evaluator "
                "maps the matrices to those ten scalar rows yet."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(PROMOTION_ATTEMPT, promotion_attempt)

    missing_evaluator = {
        "schema": "MTTRowwiseScalarEvaluatorMissing.v1",
        "status": "ROWWISE_SCALAR_RETARDED_OVERLAP_EVALUATOR_NOT_EMITTED",
        "available_inputs": {
            "physical_dotD_alpha1_available": previous["closure_decision"]["physical_dotD_alpha1_imported"],
            "stationary_sector_transfer_available": previous["closure_decision"]["stationary_sector_transfer_imported"],
            "dynamic_first_response_support_available": previous["closure_decision"][
                "dynamic_first_response_support_imported"
            ],
            "rowlocal_functional_contract_defined": rowlocal_functional["status"]
            == "ROWLOCAL_HYM_GREEN_QUADRATURE_FUNCTIONAL_DEFINED_VALUES_REQUIRE_SELECTED_KERNEL",
        },
        "missing_inputs": {
            "selected_ordered_zero_mode_basis_matrix_elements_executed": True,
            "selected_retarded_overlap_scalar_kernel_evaluated": True,
            "selected_finite_quadrature_Q_sel_executed": True,
            "selected_T_scheme_rows_instantiated": threshold_gate[
                "selected_threshold_response_functional_instantiated"
            ]
            is False,
            "selected_lambda_H_H_sector_payload_emitted": True,
        },
        "minimum_new_computation": [
            "build the selected ordered basis K_s,g for u,d,e,H inside the stationary sector packet",
            "evaluate L_rowlocal(s,g)=abs(<K_s,g, K_row(A_HYM,G,dotD_alpha1) K_s,g>) as scalar rows",
            "instantiate T_scheme(s,g) from the same-branch threshold/mass/profile functional",
            "emit lambda_H from the H-sector quartic/threshold payload",
        ],
        "forbidden_shortcuts": [
            "take matrix traces/eigenvalues from the first-response packet as K rows without the row-local functional",
            "borrow empirical K residuals as derivative rows",
            "fit T_scheme from observed Yukawa/Higgs values",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(MISSING_EVALUATOR, missing_evaluator)

    emission = {
        "schema": "MTTDynamicRetardedRowEmissionAttempt.v1",
        "status": "DYNAMIC_MATRIX_SUPPORT_IMPORTED_ZERO_SCALAR_K_ROWS_EMITTED",
        "previous_physical_transfer_status": previous["status"],
        "previous_row_count": previous_readiness["row_count"],
        "row_count": len(rows),
        "empirical_K_row_count": empirical_k["empirical_K_row_count"],
        "accepted_selected_retarded_derivative_row_count": 0,
        "accepted_T_scheme_row_count": threshold_gate["accepted_T_scheme_source_row_count"],
        "accepted_selected_K_source_row_count": 0,
        "accepted_internal_scalar_value_row_count": 0,
        "lambda_H_value_row_emitted": False,
        "row_attempts": rows,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(EMISSION, emission)

    cutset = {
        "schema": "MTTNextCutsetAfterDynamicRetardedRowAttempt.v1",
        "status": "NEXT_ATTACK_ROWWISE_SCALAR_QUADRATURE_TSCHEME_LAMBDAH",
        "next_required_artifact": NEXT,
        "closed_here": [
            "selected dynamic first-response matrices imported as same-source support",
            "direct promotion of first-response matrices to scalar K rows tested and rejected",
            "H/lambda absence from dynamic matter matrix support recorded",
            "rowwise scalar quadrature/evaluator identified as the missing object",
        ],
        "still_open": [
            "selected rowwise scalar retarded-overlap quadrature values L_rowlocal(s,g)",
            "selected threshold-scheme rows T_scheme.*",
            "selected lambda_H H-sector quartic/threshold payload",
            "ten selected K_threshold rows",
            "strict Omega/lambda_H scalar execution",
            "matrix-level mixing extension",
            "full no-knob SM closure",
        ],
        "forbidden_routes": missing_evaluator["forbidden_shortcuts"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(CUTSET, cutset)

    decision = {
        "dynamic_first_response_matrix_support_imported": True,
        "dynamic_matrix_to_scalar_retarded_rows_tested": True,
        "matrix_support_promoted_to_scalar_retarded_rows": False,
        "rowwise_scalar_retarded_overlap_evaluator_emitted": False,
        "selected_T_scheme_rows_emitted": False,
        "selected_lambda_H_payload_emitted": False,
        "accepted_selected_retarded_derivative_row_count": 0,
        "accepted_selected_K_source_row_count": 0,
        "accepted_internal_scalar_value_row_count": 0,
        "controlled_empirical_K_import_available": True,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
    }
    candidate = {
        "candidate": "MTTSelectedDynamicRetardedOverlapDerivativeRowsOrTSchemeLambdaHSourceExecution",
        "status": STATUS,
        "closure_claimed": True,
        "theorem": {
            "name": "DynamicMatrixSupportIsNotScalarKRowEvaluator",
            "proved": True,
            "statement": (
                "The selected same-source dynamic matter/overlap packet supplies genuine first-response matrix "
                "support, including non-scalar qualitative flavor tests.  It does not by itself emit the scalar "
                "retarded-overlap derivative rows required by the K_threshold contract, because the row-local "
                "quadrature/evaluator, selected T_scheme rows, and lambda_H H-sector payload remain unexecuted."
            ),
        },
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "dynamic_matrix_to_scalar_retarded_row_promotion_attempt": rel(PROMOTION_ATTEMPT),
            "rowwise_scalar_evaluator_missing": rel(MISSING_EVALUATOR),
            "dynamic_retarded_row_emission_attempt": rel(EMISSION),
            "next_cutset_after_dynamic_retarded_row_attempt": rel(CUTSET),
        },
        "closure_decision": decision,
        "previous_status": previous["status"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_DynamicRetardedOverlapDerivativeRows_or_TSchemeLambdaHSourceExecution_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        **decision,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected DynamicRetardedOverlapDerivativeRows or TSchemeLambdaHSourceExecution v1

Status: `{STATUS}`.

This packet tests the most tempting shortcut after physical `dotD_alpha1` and
stationary sector transfer are imported: promote the selected dynamic
first-response matrices directly to scalar retarded-overlap derivative rows.

Result:

```text
selected dynamic matrix support imported : true
matrix -> scalar K-row shortcut tested   : true
matrix support promoted to scalar rows   : false
rowwise scalar evaluator emitted         : false
selected T_scheme rows emitted           : false
selected lambda_H payload emitted        : false
accepted selected K rows                 : 0
```

The selected dynamic matter/overlap packet is real progress. It validates the
same-source first-response matrix layer and qualitative non-scalar flavor
tests. But the K-row contract needs scalar row-local quadrature values
`L_rowlocal(s,g)=abs(<K_s,g, K_row K_s,g>)`, followed by selected
`T_scheme.*` and `lambda_H` execution. Matrix traces/eigenvalues from the
first-response packet are not accepted as those scalar rows.

Next artifact: `{NEXT}`.
""",
        encoding="utf-8",
    )

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
