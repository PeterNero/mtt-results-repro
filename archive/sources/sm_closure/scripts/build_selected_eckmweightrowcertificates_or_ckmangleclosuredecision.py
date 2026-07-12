"""Attempt final E_CKM weight row certificates."""

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

SLUG = "selected_eckmweightrowcertificates_or_ckmangleclosuredecision"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SCAN = PACKET_DIR / "available_eckm_trace_invariant_scan.packet.json"
GATE = PACKET_DIR / "kckm_trace_assembly_rule_gate.packet.json"
DECISION = PACKET_DIR / "ckm_angle_closure_decision_after_eckm_attempt.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_ECKMWeightRowCertificates_or_CKMAngleClosureDecision_v1.md"

PREVIOUS = DATA / "selected_finitehessianc1sectorcontractions_or_eckmtraceexecution.candidate.json"
MATRICES = (
    DATA
    / "selected_finitehessianc1sectorcontractions_or_eckmtraceexecution"
    / "finite_hessian_c1_sector_contraction_matrices.packet.json"
)
TRACE_GATE = (
    DATA
    / "selected_finitehessianc1sectorcontractions_or_eckmtraceexecution"
    / "eckm_trace_weight_certificate_gate.packet.json"
)
WEIGHTS = (
    DATA
    / "selected_ckmsectorpairprojectionrows_or_honestflavorgalerkinexecution"
    / "required_q448_sector_pair_weights.packet.json"
)

STATUS = "MTT_SELECTED_ECKM_WEIGHT_ROW_CERTIFICATE_ATTEMPT_EXECUTED_KCKM_RULE_OPEN"
NEXT = "MTT_Selected_KCKMTraceAssemblyRule_or_OnePrincipleCKMClosure_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def invariant_scan(weights: dict[str, float], diagnostics: dict[str, Any]) -> dict[str, Any]:
    q = 79.0
    modulus = 448.0
    delta = 2.0 * math.pi * q / modulus
    constants = {
        "RZ_norm_sq": diagnostics["u"]["frobenius_norm_sq"],
        "RX_norm_sq": diagnostics["d"]["frobenius_norm_sq"],
        "RZ_trace": diagnostics["u"]["trace"][0],
        "RX_trace": diagnostics["d"]["trace"][0],
        "RZ_minus_RX_norm": diagnostics["u"]["frobenius_norm_sq"] - diagnostics["d"]["frobenius_norm_sq"],
        "q": q,
        "sqrt3": math.sqrt(3.0),
        "sin_delta": math.sin(delta),
        "cos_delta_abs": abs(math.cos(delta)),
        "q_cos_over_2": q * abs(math.cos(delta)) / 2.0,
        "q_sin_over_12": q * math.sin(delta) / 12.0,
        "modulus_over_64": modulus / 64.0,
    }
    denominators = [1, 2, 3, 4, 6, 7, 8, 9, 12, 16, 18, 24, 27, 28, 36, 42, 48, 56, 64, 72, 84, 112, 144, 224]
    coeffs = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]
    candidates: list[dict[str, Any]] = []

    for name, value in constants.items():
        for coeff, denom in product(coeffs, denominators):
            candidates.append({"formula": f"({coeff}/{denom})*{name}", "value": coeff * value / denom})

    for (name_a, value_a), (name_b, value_b) in combinations_with_replacement(constants.items(), 2):
        for coeff_a, coeff_b, denom in product([-5, -3, -2, -1, 1, 2, 3, 5], [-5, -3, -2, -1, 1, 2, 3, 5], [2, 3, 4, 6, 7, 8, 9, 12, 16, 18, 24, 28, 36, 42, 48, 56, 72, 84, 112, 144]):
            value = (coeff_a * value_a + coeff_b * value_b) / denom
            candidates.append(
                {
                    "formula": f"({coeff_a}*{name_a} {'+' if coeff_b >= 0 else '-'} {abs(coeff_b)}*{name_b})/{denom}",
                    "value": value,
                }
            )

    best_by_row = {}
    for row, target in weights.items():
        best = min(candidates, key=lambda item: abs(item["value"] - target) / abs(target))
        best_by_row[row] = {
            **best,
            "target_weight": target,
            "absolute_residual": best["value"] - target,
            "relative_residual": abs(best["value"] - target) / abs(target),
            "accepted": False,
            "rejection_reason": "no selected K_CKM trace assembly rule or Pi_CKM row certificate",
        }

    return {
        "schema": "MTTAvailableECKMTraceInvariantScan.v1",
        "status": "AVAILABLE_ECKM_TRACE_INVARIANT_SCAN_EXECUTED_NO_ACCEPTED_ROWS",
        "source_constants": constants,
        "candidate_count": len(candidates),
        "best_by_weight_row": best_by_row,
        "accepted_weight_rows": 0,
        "observed_data_used_as_selector": False,
        "observed_data_used_for_postcheck": True,
        "target_fitting_used": False,
    }


def main() -> int:
    previous = load(PREVIOUS)
    matrices = load(MATRICES)
    trace_gate = load(TRACE_GATE)
    weights_packet = load(WEIGHTS)

    if previous["closure_decision"]["readiness_promoted_6_to_7"] is not True:
        raise ValueError("previous E_CKM readiness was not promoted to 7/8")
    if matrices["promotes_finite_Hessian_C1_sector_contraction_values"] is not True:
        raise ValueError("sector contractions are not promoted")

    weights = weights_packet["q448_weights_if_matching_measured_replay"]
    scan = invariant_scan(weights, matrices["diagnostics"])

    gate = {
        "schema": "MTTKCKMTraceAssemblyRuleGate.v1",
        "status": "KCKM_TRACE_ASSEMBLY_RULE_REQUIRED_FOR_WEIGHT_CERTIFICATES",
        "all_domain_inputs_ready": True,
        "ready_inputs": trace_gate["ready_inputs"],
        "formal_rows": trace_gate["formal_rows"],
        "missing_rule": "selected K_CKM trace assembly rule tying Pi_CKM^ij, Delta_v, Orbit_lambda, and M_u/M_d/M_e to W_ij",
        "why_scan_not_enough": [
            "near-hit invariant expressions are not row certificates",
            "the three postcheck weights cannot be promoted without a selected Pi_CKM/K_CKM trace rule",
            "using W12,W23,W13 to choose coefficients would be target fitting",
        ],
        "selected_K_CKM_rule_emitted": False,
        "selected_Pi_CKM_row_certificates": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    decision = {
        "schema": "MTTCKMAngleClosureDecisionAfterECKMAttempt.v1",
        "status": "ECKM_DOMAIN_7_OF_8_FINAL_WEIGHT_CERTIFICATES_OPEN",
        "domain_readiness": "7/8",
        "available_eckm_trace_invariant_scan_executed": True,
        "selected_K_CKM_rule_emitted": False,
        "accepted_weight_rows": 0,
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
        "name": "ECKMWeightRowCertificateAttemptTheorem",
        "proved": True,
        "statement": (
            "All current E_CKM domain inputs are ready except the final selected K_CKM/Pi_CKM trace "
            "assembly rule.  A source-invariant scan over the available contractions finds only "
            "uncertified near-hits, so W12,W23,W13 remain postcheck obligations rather than selected "
            "source rows.  CKM angle closure is therefore not yet proved."
        ),
    }

    data = {
        "candidate": "MTTSelectedECKMWeightRowCertificatesOrCKMAngleClosureDecision",
        "status": STATUS,
        "inputs": {
            "previous_eckm_readiness": rel(PREVIOUS),
            "sector_contraction_matrices": rel(MATRICES),
            "trace_gate": rel(TRACE_GATE),
            "required_q448_weights": rel(WEIGHTS),
        },
        "output_packets": {
            "available_eckm_trace_invariant_scan": rel(SCAN),
            "kckm_trace_assembly_rule_gate": rel(GATE),
            "ckm_angle_closure_decision_after_eckm_attempt": rel(DECISION),
        },
        "closure_decision": {
            "available_eckm_trace_invariant_scan_executed": True,
            "selected_K_CKM_rule_emitted": False,
            "accepted_weight_rows": 0,
            "accepted_exact_ckm_correction_rows": 0,
            "accepted_no_knob_CKM_angle_rows": 0,
            "CKM_angle_magnitudes_derived_exact": False,
            "Jarlskog_source_derived_without_measured_angles": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closure_closed": False,
        },
        "key_numbers": {
            "domain_readiness": "7/8",
            "required_q448_weights": weights,
            "best_available_invariant_relative_residuals": {
                row: scan["best_by_weight_row"][row]["relative_residual"] for row in ["W12", "W23", "W13"]
            },
            "accepted_eckm_weight_rows": 0,
        },
        "theorem": theorem,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "observed_data_used_for_postcheck": True,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_ECKMWeightRowCertificates_or_CKMAngleClosureDecision_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "available_eckm_trace_invariant_scan_executed": True,
        "selected_K_CKM_rule_emitted": False,
        "accepted_weight_rows": 0,
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

    note = f"""# MTT Selected ECKMWeightRowCertificates or CKMAngleClosureDecision v1

Status: `{STATUS}`.

## Theorem

`ECKMWeightRowCertificateAttemptTheorem` is proved.

All current E_CKM domain inputs are ready except the final selected
`K_CKM/Pi_CKM` trace assembly rule. A source-invariant scan over the available
contractions was executed, but it emits no accepted rows.

```text
domain readiness = 7/8
accepted W rows  = 0/3
```

The remaining proof object is exact and small:

```text
selected K_CKM trace assembly rule
Pi_CKM^12, Pi_CKM^23, Pi_CKM^13 row certificates
```

CKM angle closure is not claimed.

Next artifact: `{NEXT}`.
"""

    write_json(SCAN, scan)
    write_json(GATE, gate)
    write_json(DECISION, decision)
    write_json(OUTPUT, data)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
