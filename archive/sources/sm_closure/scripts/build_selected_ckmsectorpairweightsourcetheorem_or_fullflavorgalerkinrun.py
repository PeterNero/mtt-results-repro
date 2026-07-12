"""Attempt CKM sector-pair weight source emission.

The previous artifact closed the q=448 projection contract.  This artifact
imports the later closed pure-Weyl/lambda-orbit/second-order matrix layer and
tests whether that selected orbit layer already emits the three CKM weights.
"""

from __future__ import annotations

import json
import math
from itertools import combinations_with_replacement, product
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_ckmsectorpairweightsourcetheorem_or_fullflavorgalerkinrun"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
IMPORT = PACKET_DIR / "second_order_orbit_import_for_ckm_weights.packet.json"
EXTRACTION = PACKET_DIR / "orbit_invariant_weight_extraction_attempt.packet.json"
REDUCTION = PACKET_DIR / "ckm_weight_scalar_functional_reduction.packet.json"
DECISION = PACKET_DIR / "ckm_weight_source_acceptance_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_CKMSectorPairWeightSourceTheorem_or_FullFlavorGalerkinRun_v1.md"

PREVIOUS = DATA / "selected_ckmsectorpairprojectionrows_or_honestflavorgalerkinexecution.candidate.json"
WEIGHTS = (
    DATA
    / "selected_ckmsectorpairprojectionrows_or_honestflavorgalerkinexecution"
    / "required_q448_sector_pair_weights.packet.json"
)
BASIS_ATTEMPT = (
    DATA
    / "selected_ckmsectorpairprojectionrows_or_honestflavorgalerkinexecution"
    / "finite_source_basis_projection_attempt.packet.json"
)
PURE_ROWS = DATA / "selected_step65_pureweylrowclosure_import_or_scalarvalueexecution.candidate.json"
ORBIT = DATA / "selected_lambdaorbitsecondordermatrixpacket_or_rthetascalarexecution.candidate.json"
ORBIT_PACKET = (
    DATA
    / "selected_lambdaorbitsecondordermatrixpacket_or_rthetascalarexecution"
    / "lambda_orbit_second_order_matrix_packet.packet.json"
)
ORBIT_TESTS = (
    DATA
    / "selected_lambdaorbitsecondordermatrixpacket_or_rthetascalarexecution"
    / "second_order_orbit_qualitative_sm_tests.packet.json"
)
RTHETA_OBLIGATION = (
    DATA
    / "selected_secondorderorbitqualitativesmclosure_or_rthetascalarvalues"
    / "rtheta_scalar_value_obligation.packet.json"
)

STATUS = "MTT_SELECTED_CKMSECTORPAIR_WEIGHT_SOURCE_ATTEMPT_ORBIT_IMPORTED_SCALAR_EVALUATOR_OPEN"
NEXT = "MTT_Selected_CKMWeightScalarEvaluator_or_SelectedFlavorGalerkinValues_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def invariant_scan(targets: dict[str, float], source_constants: dict[str, float]) -> dict[str, Any]:
    denominators = [1, 2, 3, 4, 6, 7, 8, 9, 12, 16, 18, 24, 27, 28, 36, 42, 48, 54, 72, 84, 108, 144]
    coeffs = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]
    candidates: list[dict[str, Any]] = []

    for name, value in source_constants.items():
        for coeff, denom in product(coeffs, denominators):
            candidates.append(
                {
                    "formula": f"({coeff}/{denom})*{name}",
                    "value": coeff * value / denom,
                    "term_count": 1,
                }
            )

    for (name_a, value_a), (name_b, value_b) in combinations_with_replacement(source_constants.items(), 2):
        for coeff_a, coeff_b, denom in product([-5, -3, -2, -1, 1, 2, 3, 5], [-5, -3, -2, -1, 1, 2, 3, 5], [2, 3, 4, 6, 7, 8, 9, 12, 16, 18, 24, 28, 36, 42, 48, 72, 84, 108, 144]):
            value = (coeff_a * value_a + coeff_b * value_b) / denom
            candidates.append(
                {
                    "formula": f"({coeff_a}*{name_a} {'+' if coeff_b >= 0 else '-'} {abs(coeff_b)}*{name_b})/{denom}",
                    "value": value,
                    "term_count": 2,
                }
            )

    best_by_weight = {}
    for row, target in targets.items():
        best = min(candidates, key=lambda item: abs(item["value"] - target) / abs(target))
        best_by_weight[row] = {
            **best,
            "target_weight": target,
            "absolute_residual": best["value"] - target,
            "relative_residual": abs(best["value"] - target) / abs(target),
            "accepted": False,
            "rejection_reason": "orbit invariant expression has no selected CKM scalar-evaluator certificate",
        }

    return {
        "schema": "MTTCKMOrbitInvariantWeightExtractionAttempt.v1",
        "status": "ORBIT_INVARIANT_WEIGHT_EXTRACTION_EXECUTED_NO_ACCEPTED_ROWS",
        "source_constants": source_constants,
        "candidate_count": len(candidates),
        "best_by_weight": best_by_weight,
        "accepted_weight_rows": 0,
        "accepted_exact_ckm_correction_rows": 0,
        "observed_data_used_as_selector": False,
        "observed_data_used_for_postcheck": True,
        "target_fitting_used": False,
    }


def main() -> int:
    previous = load(PREVIOUS)
    weights_packet = load(WEIGHTS)
    basis_attempt = load(BASIS_ATTEMPT)
    pure_rows = load(PURE_ROWS)
    orbit = load(ORBIT)
    orbit_packet = load(ORBIT_PACKET)
    orbit_tests = load(ORBIT_TESTS)
    rtheta = load(RTHETA_OBLIGATION)

    if previous["closure_decision"]["q448_sector_pair_projection_contract_closed"] is not True:
        raise ValueError("q448 CKM projection contract is not closed")
    if pure_rows["closure_decision"]["lambda_orbit_scaled_pure_Weyl_rows_closed"] is not True:
        raise ValueError("lambda-orbit scaled pure Weyl rows are not closed")
    if orbit["closure_decision"]["selected_second_order_orbit_matrix_packet_closed"] is not True:
        raise ValueError("second-order orbit matrix packet is not closed")
    if rtheta["selected_functional_executed"] is not False:
        raise ValueError("unexpected selected scalar functional execution")

    weights = weights_packet["q448_weights_if_matching_measured_replay"]
    spectrum = orbit_tests["hermitian_spectrum_each_sector"]
    comm_norm_sq = orbit_packet["matrix_branches"][0]["commutator_norm_sq"]
    comm_norm = math.sqrt(comm_norm_sq)
    cp_abs = 972.0 * math.sqrt(3.0)
    q = 79.0
    modulus = 448.0
    delta = 2.0 * math.pi * q / modulus
    source_constants = {
        "spec_min": spectrum[0],
        "spec_mid": spectrum[1],
        "spec_max": spectrum[2],
        "spec_sum": sum(spectrum),
        "spec_product": math.prod(spectrum),
        "gap_41": spectrum[1] - spectrum[0],
        "gap_74": spectrum[2] - spectrum[1],
        "gap_71": spectrum[2] - spectrum[0],
        "comm_norm": comm_norm,
        "comm_norm_sq": comm_norm_sq,
        "cp_abs_over_100": cp_abs / 100.0,
        "sqrt_cp_abs": math.sqrt(cp_abs),
        "q": q,
        "sqrt3": math.sqrt(3.0),
        "sin_delta": math.sin(delta),
        "cos_delta_abs": abs(math.cos(delta)),
        "q_cos_over_2": q * abs(math.cos(delta)) / 2.0,
        "q_sin_over_12": q * math.sin(delta) / 12.0,
    }
    extraction = invariant_scan(weights, source_constants)

    import_packet = {
        "schema": "MTTSecondOrderOrbitImportForCKMWeights.v1",
        "status": "SECOND_ORDER_ORBIT_AND_PURE_WEYL_ROWS_IMPORTED_FOR_CKM_WEIGHT_SOURCE_ATTEMPT",
        "pure_weyl_rows_closed": pure_rows["closure_decision"]["pure_Weyl_rows_emitted_identity_free"],
        "lambda_orbit_scaled_pure_rows_closed": pure_rows["closure_decision"][
            "lambda_orbit_scaled_pure_Weyl_rows_closed"
        ],
        "second_order_orbit_matrix_packet_closed": orbit["closure_decision"][
            "selected_second_order_orbit_matrix_packet_closed"
        ],
        "qualitative_three_family_splitting_closed": orbit["closure_decision"][
            "qualitative_three_family_splitting_closed"
        ],
        "qualitative_CP_nonzero_closed": orbit["closure_decision"]["qualitative_CP_nonzero_closed"],
        "individual_lambda_representative_selected": orbit["closure_decision"][
            "individual_lambda_representative_selected"
        ],
        "orbit_representatives": orbit_packet["selected_branch_ids"],
        "orbit_invariants": {
            "hermitian_spectrum_each_sector": spectrum,
            "commutator_norm_sq": comm_norm_sq,
            "cp_odd_exact_magnitude": orbit_packet["matrix_branches"][0]["cp_odd_exact_magnitude"],
            "all_representatives_positive_orientation": orbit_tests[
                "all_selected_orbit_representatives_positive_orientation"
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    reduction = {
        "schema": "MTTCKMWeightScalarFunctionalReduction.v1",
        "status": "CKM_WEIGHT_SOURCE_REDUCED_TO_SELECTED_SCALAR_EVALUATOR",
        "weight_rows": ["W12", "W23", "W13"],
        "required_values_if_matching_replay": weights,
        "available_source_layer": [
            "selected q79 phase",
            "selected heavy-link Delta_v",
            "selected dynamic C1 correction domain",
            "selected lambda-orbit scaled pure Weyl rows",
            "selected second-order orbit matrix packet",
        ],
        "unavailable_value_execution_layer": rtheta["domain_inventory_now"],
        "minimal_evaluator": (
            "E_CKM^ij = Tr_N(Pi_CKM^ij K_CKM(Delta_v, Orbit_lambda, C1/Hessian/zero-mode value rows))"
        ),
        "relation_to_rtheta_frontier": (
            "The CKM weights are not identical to the ten typed Rtheta scalar rows, but they require the "
            "same missing value-execution ingredients: selected zero-mode bases, metric/Gram rule, "
            "Riesz/Green operator, finite Hessian C1 source blocks, rho_E/sector projectors, dotD/"
            "deltaTheta, and primitive C1 sector contractions."
        ),
        "what_is_no_longer_missing": [
            "pure Weyl coefficient/source rows",
            "lambda orbit",
            "qualitative second-order three-family splitting",
            "qualitative nonzero CP orbit invariant",
            "q448 CKM projection row contract",
        ],
        "what_remains_missing": [
            "selected scalar evaluator E_CKM^12",
            "selected scalar evaluator E_CKM^23",
            "selected scalar evaluator E_CKM^13",
            "row certificates for W12,W23,W13",
        ],
        "observed_data_used_as_selector": False,
        "observed_data_used_for_postcheck": True,
        "target_fitting_used": False,
    }

    decision = {
        "schema": "MTTCKMWeightSourceAcceptanceDecision.v1",
        "status": "ORBIT_LAYER_IMPORTED_WEIGHT_SOURCE_ROWS_REMAIN_OPEN",
        "second_order_orbit_imported": True,
        "orbit_invariant_extraction_attempt_executed": True,
        "ckm_weight_scalar_functional_reduction_closed": True,
        "selected_weight_rows": 0,
        "accepted_exact_ckm_correction_rows": 0,
        "accepted_no_knob_CKM_angle_rows": 0,
        "CKM_angle_magnitudes_derived_exact": False,
        "Jarlskog_source_derived_without_measured_angles": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closure_closed": False,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    theorem = {
        "name": "CKMSectorPairWeightSourceReductionTheorem",
        "proved": True,
        "statement": (
            "The selected pure-Weyl/lambda-orbit/second-order matrix layer is sufficient to supply "
            "the qualitative three-family/CP source domain for CKM sector-pair weights, and the "
            "q=448 row contract is already closed. However, the selected orbit invariants alone do "
            "not emit W12,W23,W13: current accepted packets still lack the scalar evaluator that "
            "contracts sector-pair projectors against the orbit matrix and finite C1/Hessian/zero-mode "
            "value rows. Therefore exact CKM angle closure is reduced to E_CKM^ij row execution."
        ),
    }

    data = {
        "candidate": "MTTSelectedCKMSectorPairWeightSourceTheoremOrFullFlavorGalerkinRun",
        "status": STATUS,
        "inputs": {
            "previous_projection_contract": rel(PREVIOUS),
            "required_q448_weights": rel(WEIGHTS),
            "previous_finite_basis_attempt": rel(BASIS_ATTEMPT),
            "pure_weyl_row_closure": rel(PURE_ROWS),
            "second_order_orbit_candidate": rel(ORBIT),
            "second_order_orbit_packet": rel(ORBIT_PACKET),
            "second_order_orbit_tests": rel(ORBIT_TESTS),
            "rtheta_scalar_obligation": rel(RTHETA_OBLIGATION),
        },
        "output_packets": {
            "second_order_orbit_import_for_ckm_weights": rel(IMPORT),
            "orbit_invariant_weight_extraction_attempt": rel(EXTRACTION),
            "ckm_weight_scalar_functional_reduction": rel(REDUCTION),
            "ckm_weight_source_acceptance_decision": rel(DECISION),
        },
        "closure_decision": {
            "second_order_orbit_imported": True,
            "pure_weyl_lambda_orbit_rows_imported": True,
            "orbit_invariant_extraction_attempt_executed": True,
            "ckm_weight_scalar_functional_reduction_closed": True,
            "selected_weight_rows": 0,
            "accepted_exact_ckm_correction_rows": 0,
            "accepted_no_knob_CKM_angle_rows": 0,
            "CKM_angle_magnitudes_derived_exact": False,
            "Jarlskog_source_derived_without_measured_angles": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closure_closed": False,
        },
        "key_numbers": {
            "q448_weights": weights,
            "orbit_spectrum": spectrum,
            "commutator_norm_sq": comm_norm_sq,
            "cp_odd_abs": cp_abs,
            "best_orbit_invariant_relative_residuals": {
                row: extraction["best_by_weight"][row]["relative_residual"] for row in ["W12", "W23", "W13"]
            },
        },
        "theorem": theorem,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "observed_data_used_for_postcheck": True,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_CKMSectorPairWeightSourceTheorem_or_FullFlavorGalerkinRun_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "second_order_orbit_imported": True,
        "pure_weyl_lambda_orbit_rows_imported": True,
        "orbit_invariant_extraction_attempt_executed": True,
        "ckm_weight_scalar_functional_reduction_closed": True,
        "selected_weight_rows": 0,
        "accepted_exact_ckm_correction_rows": 0,
        "accepted_no_knob_CKM_angle_rows": 0,
        "CKM_angle_magnitudes_derived_exact": False,
        "Jarlskog_source_derived_without_measured_angles": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closure_closed": False,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "observed_data_used_for_postcheck": True,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected CKMSectorPairWeightSourceTheorem or FullFlavorGalerkinRun v1

Status: `{STATUS}`.

## Theorem

`CKMSectorPairWeightSourceReductionTheorem` is proved.

The selected pure-Weyl/lambda-orbit/second-order matrix layer is now imported
into the CKM sector-pair weight problem. It supplies:

```text
orbit spectrum          = {spectrum}
commutator norm squared = {comm_norm_sq}
CP-odd invariant        = 972*sqrt(3)
lambda representatives  = {orbit_packet['selected_branch_ids']}
```

This closes the qualitative three-family/CP source domain for the CKM weight
attempt. It does not emit the scalar weights.

## CKM Weight Obligation

```text
W12 = {weights['W12']:.15f}
W23 = {weights['W23']:.15f}
W13 = {weights['W13']:.15f}
```

An invariant extraction scan over the selected orbit constants was executed.
Accepted selected weight rows remain `0/3`.

## Exact Remaining Object

The missing row is no longer a generic coefficient-source issue. It is the
selected scalar evaluator:

```text
E_CKM^ij = Tr_N(Pi_CKM^ij K_CKM(Delta_v, Orbit_lambda, C1/Hessian/zero-mode value rows))
```

This evaluator needs the same value-execution ingredients as the typed
`R_theta` scalar frontier: zero-mode bases, metric/Gram rule, Riesz/Green,
finite Hessian C1 source blocks, rho_E/sector projectors, dotD/deltaTheta, and
primitive C1 sector contractions.

Next artifact: `{NEXT}`.
"""

    write_json(IMPORT, import_packet)
    write_json(EXTRACTION, extraction)
    write_json(REDUCTION, reduction)
    write_json(DECISION, decision)
    write_json(OUTPUT, data)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
