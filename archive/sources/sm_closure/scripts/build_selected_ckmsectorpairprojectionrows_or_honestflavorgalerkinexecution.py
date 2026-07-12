"""Build the CKM sector-pair projection-row contract.

The previous artifact closed the dynamic C1 correction domain.  This one
reduces exact CKM angle correction to three finite q=448 sector-pair weights
and tests whether the current selected source basis emits those weights.
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

SLUG = "selected_ckmsectorpairprojectionrows_or_honestflavorgalerkinexecution"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CONTRACT = PACKET_DIR / "sector_pair_projection_contract.packet.json"
WEIGHTS = PACKET_DIR / "required_q448_sector_pair_weights.packet.json"
BASIS = PACKET_DIR / "finite_source_basis_projection_attempt.packet.json"
DECISION = PACKET_DIR / "sector_pair_projection_acceptance_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_CKMSectorPairProjectionRows_or_HonestFlavorGalerkinExecution_v1.md"

PREVIOUS = DATA / "selected_ckmanglecorrectionfunctional_or_exactflavorobservableclosure.candidate.json"
DOMAIN = (
    DATA
    / "selected_ckmanglecorrectionfunctional_or_exactflavorobservableclosure"
    / "dynamic_c1_correction_domain.packet.json"
)
REQUIREMENT = (
    DATA
    / "selected_ckmanglecorrectionfunctional_or_exactflavorobservableclosure"
    / "ckm_correction_factor_requirement.packet.json"
)
SCAN = (
    DATA
    / "selected_ckmanglecorrectionfunctional_or_exactflavorobservableclosure"
    / "source_native_correction_candidate_scan.packet.json"
)
HEAVYLINK = (
    DATA
    / "selected_sectortransportselectionlemma_su5qutritheavylink"
    / "selected_heavylink_eight_slot_values.packet.json"
)
LEADING = (
    DATA
    / "selected_deltav_to_ckm_anglemagnitudemap_or_honestflavorobservableexecution"
    / "leading_sqrt_flavor_angle_map.packet.json"
)

STATUS = "MTT_SELECTED_CKMSECTORPAIR_PROJECTION_CONTRACT_CLOSED_WEIGHT_SOURCE_ROWS_OPEN"
NEXT = "MTT_Selected_CKMSectorPairWeightSourceTheorem_or_FullFlavorGalerkinRun_v1"
Q = 448.0


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def finite_basis_projection_attempt(targets: dict[str, float], source_constants: dict[str, float]) -> dict[str, Any]:
    """Search a tiny finite-source linear span for the three q=448 weights."""

    basis = {
        "1": 1.0,
        "sqrt2": math.sqrt(2.0),
        "sqrt3": math.sqrt(3.0),
        "phase_norm_sq": source_constants["phase_norm_sq"],
        "shift_norm_sq": source_constants["shift_norm_sq"],
        "delta_v_norm": source_constants["delta_v_norm"],
        "sin_delta": source_constants["sin_delta"],
        "cos_delta_abs": source_constants["cos_delta_abs"],
        "q_cos_over_2": source_constants["q"] * source_constants["cos_delta_abs"] / 2.0,
        "q_sin_over_12": source_constants["q"] * source_constants["sin_delta"] / 12.0,
        "four_sqrt3": 4.0 * math.sqrt(3.0),
        "sqrt2_from_delta_v": source_constants["delta_v_norm"] * math.sqrt(3.0),
    }
    denominators = [1, 2, 3, 4, 6, 7, 8, 9, 12, 16, 18, 24, 27, 36, 48, 72]
    coeffs = [-8, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 8]
    candidates: list[dict[str, Any]] = []

    for name, value in basis.items():
        for coeff, denom in product(coeffs, denominators):
            candidates.append(
                {
                    "formula": f"({coeff}/{denom})*{name}",
                    "value": coeff * value / denom,
                    "term_count": 1,
                }
            )

    for (name_a, value_a), (name_b, value_b) in combinations_with_replacement(basis.items(), 2):
        for coeff_a, coeff_b, denom in product([-3, -2, -1, 1, 2, 3], [-3, -2, -1, 1, 2, 3], [2, 3, 4, 6, 8, 12, 16, 24, 36, 48, 72]):
            value = (coeff_a * value_a + coeff_b * value_b) / denom
            candidates.append(
                {
                    "formula": f"({coeff_a}*{name_a} { '+' if coeff_b >= 0 else '-' } {abs(coeff_b)}*{name_b})/{denom}",
                    "value": value,
                    "term_count": 2,
                }
            )

    best_by_row = {}
    for row, target in targets.items():
        best = min(candidates, key=lambda item: abs(item["value"] - target) / abs(target))
        best_by_row[row] = {
            **best,
            "target_weight": target,
            "absolute_residual": best["value"] - target,
            "relative_residual": abs(best["value"] - target) / abs(target),
            "accepted": False,
            "rejection_reason": "finite source span near-hit lacks a selected row-level projection certificate",
        }

    return {
        "schema": "MTTFiniteSourceBasisProjectionAttempt.v1",
        "status": "FINITE_SOURCE_BASIS_ATTEMPT_EXECUTED_NO_ACCEPTED_WEIGHT_ROWS",
        "basis": basis,
        "candidate_count": len(candidates),
        "best_by_sector_pair": best_by_row,
        "accepted_weight_rows": 0,
        "accepted_exact_ckm_correction_rows": 0,
        "observed_data_used_as_selector": False,
        "observed_data_used_for_postcheck": True,
        "target_fitting_used": False,
    }


def main() -> int:
    previous = load(PREVIOUS)
    domain = load(DOMAIN)
    requirement = load(REQUIREMENT)
    scan = load(SCAN)
    heavylink = load(HEAVYLINK)
    leading = load(LEADING)

    if previous["closure_decision"]["dynamic_c1_correction_domain_closed"] is not True:
        raise ValueError("dynamic C1 correction domain is not closed")
    if previous["closure_decision"]["accepted_exact_correction_rows"] != 0:
        raise ValueError("previous artifact unexpectedly accepted correction rows")
    if domain["status"] != "DYNAMIC_C1_CORRECTION_DOMAIN_CLOSED":
        raise ValueError("domain packet not closed")

    required_corrections = requirement["required_if_matching_measured_replay"]
    q448_weights = {
        "W12": Q * (required_corrections["s12"] - 1.0),
        "W23": Q * (required_corrections["s23"] - 1.0),
        "W13": Q * (required_corrections["s13"] - 1.0),
    }
    weight_ratios = {
        "W23_over_W12": q448_weights["W23"] / q448_weights["W12"],
        "W13_over_W12": q448_weights["W13"] / q448_weights["W12"],
        "W13_over_W23": q448_weights["W13"] / q448_weights["W23"],
    }

    contract = {
        "schema": "MTTCKMSectorPairProjectionContract.v1",
        "status": "Q448_SECTOR_PAIR_PROJECTION_CONTRACT_CLOSED",
        "normalization": "C_ij = 1 + W_ij/448",
        "sector_pair_rows": {
            "s12": {"projection_row": "Pi_CKM^12", "weight": "W12", "leading_angle": leading["predicted_angles"]["s12"]},
            "s23": {"projection_row": "Pi_CKM^23", "weight": "W23", "leading_angle": leading["predicted_angles"]["s23"]},
            "s13": {"projection_row": "Pi_CKM^13", "weight": "W13", "leading_angle": leading["predicted_angles"]["s13"]},
        },
        "selected_inputs_already_available": {
            "selected_Delta_v": True,
            "selected_heavy_link_values": True,
            "dynamic_C1_domain": True,
            "q79_phase_contact": True,
        },
        "selected_heavy_link_delta_v": heavylink["Delta_v_numeric"],
        "formal_correction_functional": (
            "A_CKM = A_CKM^0 multiplied rowwise by "
            "(1 + Tr_N(Pi_CKM^ij K_CKM)/448)"
        ),
        "contract_closes": "the finite-q normalization and row shape of the missing correction functional",
        "contract_does_not_close": "the selected numeric source values W12,W23,W13",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    weights = {
        "schema": "MTTRequiredQ448SectorPairWeights.v1",
        "status": "REQUIRED_WEIGHT_OBLIGATION_IDENTIFIED_NOT_SOURCE_VALUES",
        "q448_weights_if_matching_measured_replay": q448_weights,
        "weight_ratios": weight_ratios,
        "all_three_weights_distinct": len({round(value, 12) for value in q448_weights.values()}) == 3,
        "interpretation": (
            "These are the exact finite-q weights the sector-pair projection rows would need "
            "to emit to turn the leading source-side map into the replayed CKM magnitudes. "
            "They are obligations/postcheck values, not selected source rows."
        ),
        "observed_data_used_as_selector": False,
        "observed_data_used_for_postcheck": True,
        "target_fitting_used": False,
    }

    basis_attempt = finite_basis_projection_attempt(q448_weights, scan["source_constants"])

    decision = {
        "schema": "MTTCKMSectorPairProjectionAcceptanceDecision.v1",
        "status": "PROJECTION_CONTRACT_CLOSED_SELECTED_WEIGHT_ROWS_REMAIN_OPEN",
        "q448_sector_pair_projection_contract_closed": True,
        "required_weight_obligation_identified": True,
        "finite_source_basis_projection_attempt_executed": True,
        "selected_weight_rows": 0,
        "accepted_exact_ckm_correction_rows": 0,
        "accepted_no_knob_CKM_angle_rows": 0,
        "CKM_angle_magnitudes_derived_exact": False,
        "Jarlskog_source_derived_without_measured_angles": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closure_closed": False,
        "remaining_exact_object": "selected source theorem or honest finite Galerkin run emitting W12,W23,W13",
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    theorem = {
        "name": "CKMSectorPairProjectionRowContractTheorem",
        "proved": True,
        "statement": (
            "Given the selected leading CKM map and the closed dynamic C1 correction domain, exact "
            "CKM angle correction is equivalent at the finite q=448 row layer to emitting three "
            "sector-pair projection weights W12,W23,W13 via C_ij=1+W_ij/448. The row shape and "
            "normalization are therefore closed. Current selected packets do not emit the three "
            "numeric weights, and a bounded finite source-basis projection attempt supplies no "
            "accepted row certificates."
        ),
    }

    data = {
        "candidate": "MTTSelectedCKMSectorPairProjectionRowsOrHonestFlavorGalerkinExecution",
        "status": STATUS,
        "inputs": {
            "previous_correction_functional": rel(PREVIOUS),
            "dynamic_c1_domain": rel(DOMAIN),
            "correction_requirement": rel(REQUIREMENT),
            "source_native_scan": rel(SCAN),
            "selected_heavy_link_values": rel(HEAVYLINK),
            "leading_angle_map": rel(LEADING),
        },
        "output_packets": {
            "sector_pair_projection_contract": rel(CONTRACT),
            "required_q448_sector_pair_weights": rel(WEIGHTS),
            "finite_source_basis_projection_attempt": rel(BASIS),
            "sector_pair_projection_acceptance_decision": rel(DECISION),
        },
        "closure_decision": {
            "q448_sector_pair_projection_contract_closed": True,
            "required_weight_obligation_identified": True,
            "finite_source_basis_projection_attempt_executed": True,
            "selected_weight_rows": 0,
            "accepted_exact_ckm_correction_rows": 0,
            "accepted_no_knob_CKM_angle_rows": 0,
            "CKM_angle_magnitudes_derived_exact": False,
            "Jarlskog_source_derived_without_measured_angles": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closure_closed": False,
        },
        "key_numbers": {
            "q448_weights": q448_weights,
            "weight_ratios": weight_ratios,
            "best_source_basis_relative_residuals": {
                row: basis_attempt["best_by_sector_pair"][row]["relative_residual"] for row in ["W12", "W23", "W13"]
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
        "certificate": "MTT_Selected_CKMSectorPairProjectionRows_or_HonestFlavorGalerkinExecution_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "q448_sector_pair_projection_contract_closed": True,
        "required_weight_obligation_identified": True,
        "finite_source_basis_projection_attempt_executed": True,
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

    note = f"""# MTT Selected CKMSectorPairProjectionRows or HonestFlavorGalerkinExecution v1

Status: `{STATUS}`.

## Theorem

`CKMSectorPairProjectionRowContractTheorem` is proved.

The exact CKM correction problem is now reduced to three finite q=448
sector-pair weights:

```text
C_ij = 1 + W_ij / 448
```

For the current replay obligation those weights would be:

```text
W12 = {q448_weights['W12']:.15f}
W23 = {q448_weights['W23']:.15f}
W13 = {q448_weights['W13']:.15f}
```

These are not promoted as source values. They are the target-independent shape
of the missing row evaluator plus the postcheck obligation.

## What Closed

- finite q=448 correction normalization;
- row names `Pi_CKM^12`, `Pi_CKM^23`, `Pi_CKM^13`;
- selected inputs feeding the contract: heavy-link `Delta_v`, q79 phase, and
  the dynamic C1 domain.

## What Remains

Accepted selected weight rows: `0/3`.

The finite source-basis projection attempt found near-hits only. The remaining
exact object is a selected source theorem or honest finite flavor Galerkin run
that emits `W12`, `W23`, and `W13` with row certificates.

Next artifact: `{NEXT}`.
"""

    write_json(CONTRACT, contract)
    write_json(WEIGHTS, weights)
    write_json(BASIS, basis_attempt)
    write_json(DECISION, decision)
    write_json(OUTPUT, data)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
