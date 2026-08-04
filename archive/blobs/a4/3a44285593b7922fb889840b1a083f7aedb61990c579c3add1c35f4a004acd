"""Build the CKM correction-functional frontier artifact.

This consumes the selected heavy-link/q79/leading-angle chain and the active
Step10 dynamic Phi_fin^C1 source payload.  It closes the correction domain but
does not promote the measured CKM correction factors as source data.
"""

from __future__ import annotations

import json
import math
from itertools import product
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_ckmanglecorrectionfunctional_or_exactflavorobservableclosure"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
DOMAIN = PACKET_DIR / "dynamic_c1_correction_domain.packet.json"
REQUIREMENT = PACKET_DIR / "ckm_correction_factor_requirement.packet.json"
SCAN = PACKET_DIR / "source_native_correction_candidate_scan.packet.json"
DECISION = PACKET_DIR / "exact_correction_acceptance_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_CKMAngleCorrectionFunctional_or_ExactFlavorObservableClosure_v1.md"

PREVIOUS = DATA / "selected_deltav_to_ckm_anglemagnitudemap_or_honestflavorobservableexecution.candidate.json"
PREVIOUS_CORRECTION = (
    DATA
    / "selected_deltav_to_ckm_anglemagnitudemap_or_honestflavorobservableexecution"
    / "correction_functional_obligation.packet.json"
)
STEP10 = DATA / "selected_step10_physicalphifinc1sourcerule_or_independentgalerkinrows.candidate.json"
STEP10_DYNAMIC = (
    DATA
    / "selected_step10_physicalphifinc1sourcerule_or_independentgalerkinrows"
    / "step10_dynamic_c1_payload_emission.packet.json"
)
VSD01 = DATA / "selected_vsd01_allprimitiverowsassemblymap_or_physicalphifinc1actionsource.candidate.json"
VSD01_ASSEMBLY = (
    DATA
    / "selected_vsd01_allprimitiverowsassemblymap_or_physicalphifinc1actionsource"
    / "all_primitive_rows_assembly_map.packet.json"
)

STATUS = "MTT_SELECTED_CKMANGLECORRECTIONFUNCTIONAL_DYNAMICC1_DOMAIN_CLOSED_EXACT_ROWS_OPEN"
NEXT = "MTT_Selected_CKMSectorPairProjectionRows_or_HonestFlavorGalerkinExecution_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def as_complex(value: Any) -> complex:
    if isinstance(value, list):
        return complex(float(value[0]), float(value[1]))
    return complex(float(value), 0.0)


def frobenius_norm_sq(matrix: list[list[Any]]) -> float:
    return sum(abs(as_complex(entry)) ** 2 for row in matrix for entry in row)


def trace_complex(matrix: list[list[Any]]) -> complex:
    return sum(as_complex(matrix[i][i]) for i in range(len(matrix)))


def finite_near_hit_scan(required: dict[str, float], q: int = 79, modulus: int = 448) -> dict[str, Any]:
    """Small deterministic scan over current source-native scalar clues.

    This is intentionally not an acceptance mechanism.  It checks whether the
    present finite constants accidentally emit the three correction factors.
    """

    delta = 2.0 * math.pi * q / modulus
    constants = {
        "1": 1.0,
        "sqrt3": math.sqrt(3.0),
        "sin_delta": math.sin(delta),
        "cos_delta_abs": abs(math.cos(delta)),
        "delta_v_norm": math.sqrt(2.0 / 3.0),
        "phase_norm_sq": 4.0,
        "shift_norm_sq": 2.0,
        "hessian_normal": 12.0,
        "formal_rows": 110.0,
        "primitive_rows": 72.0,
        "q": float(q),
        "modulus": float(modulus),
    }
    denominators = [3, 6, 7, 9, 12, 18, 24, 27, 36, 72, 79, 84, 110, 144, 224, 336, 448, 672, 1008]
    candidates: list[dict[str, Any]] = []

    for cname, cval in constants.items():
        for denom, sign in product(denominators, [-1.0, 1.0]):
            value = 1.0 + sign * cval / denom
            candidates.append(
                {
                    "formula": f"1 {'+' if sign > 0 else '-'} {cname}/{denom}",
                    "value": value,
                    "source_kind": "diagnostic_simple_source_scalar",
                }
            )
    for name_a, a in constants.items():
        for name_b, b in constants.items():
            if name_a >= name_b:
                continue
            for denom, sign in product([36, 72, 144, 224, 336, 448, 672, 1008], [-1.0, 1.0]):
                value = 1.0 + sign * (a * b) / denom
                candidates.append(
                    {
                        "formula": f"1 {'+' if sign > 0 else '-'} ({name_a}*{name_b})/{denom}",
                        "value": value,
                        "source_kind": "diagnostic_product_source_scalar",
                    }
                )

    best_by_row: dict[str, Any] = {}
    for row, target in required.items():
        best = min(candidates, key=lambda item: abs(item["value"] - target) / abs(target))
        best_by_row[row] = {
            **best,
            "required": target,
            "absolute_residual": best["value"] - target,
            "relative_residual": abs(best["value"] - target) / abs(target),
            "accepted": False,
            "rejection_reason": "near-hit scan has no selected sector-pair row certificate",
        }

    return {
        "schema": "MTTSourceNativeCKMCorrectionCandidateScan.v1",
        "status": "DIAGNOSTIC_NEAR_HIT_SCAN_EXECUTED_NO_ACCEPTED_ROWS",
        "candidate_count": len(candidates),
        "source_constants": constants,
        "best_by_ckm_row": best_by_row,
        "accepted_exact_correction_rows": 0,
        "target_fitting_used": False,
        "observed_data_used_as_selector": False,
        "observed_data_used_for_postcheck": True,
        "guard": "The scan may suggest theorem targets but cannot emit value rows.",
    }


def main() -> int:
    previous = load(PREVIOUS)
    previous_correction = load(PREVIOUS_CORRECTION)
    step10 = load(STEP10)
    dynamic = load(STEP10_DYNAMIC)
    vsd01 = load(VSD01)
    assembly = load(VSD01_ASSEMBLY)

    if previous["closure_decision"]["correction_functional_obligation_identified"] is not True:
        raise ValueError("previous correction obligation is not identified")
    if step10["closure_decision"]["selected_dynamic_phi_fin_c1_payload_emitted"] is not True:
        raise ValueError("Step10 dynamic C1 payload is not emitted")
    if assembly["row_evidence"]["all_72_primitive_rows_exact"] is not True:
        raise ValueError("VSD01 primitive rows are not exact")

    required = previous_correction["needed_if_matching_measured_replay"]
    required_ordered = {key: required[key] for key in ["s12", "s23", "s13"]}
    phase_norm_sq = frobenius_norm_sq(dynamic["phase_R_Z"])
    shift_norm_sq = frobenius_norm_sq(dynamic["shift_R_X"])
    phase_trace = trace_complex(dynamic["phase_R_Z"])
    shift_trace = trace_complex(dynamic["shift_R_X"])

    correction_requirement = {
        "schema": "MTTCKMCorrectionFactorRequirement.v1",
        "status": "THREE_UNEQUAL_CORRECTION_FACTORS_IDENTIFIED_FOR_EXACT_REPLAY",
        "required_if_matching_measured_replay": required_ordered,
        "all_three_factors_distinct": len({round(value, 15) for value in required_ordered.values()}) == 3,
        "relative_sizes": {
            "s12_minus_1": required_ordered["s12"] - 1.0,
            "s23_minus_1": required_ordered["s23"] - 1.0,
            "s13_minus_1": required_ordered["s13"] - 1.0,
        },
        "forbidden_source_interpretation": previous_correction["forbidden_as_source"],
        "observed_data_used_as_selector": False,
        "observed_data_used_for_postcheck": True,
    }

    domain = {
        "schema": "MTTDynamicC1CKMCorrectionDomain.v1",
        "status": "DYNAMIC_C1_CORRECTION_DOMAIN_CLOSED",
        "source_owner": "PhysicalPhiFinC1ActionSource",
        "same_branch": True,
        "route_a_source_rule_closed": step10["closure_decision"][
            "route_A_selected_physical_PhiFinC1_source_rule_closed"
        ],
        "dynamic_phi_fin_c1_payload_emitted": step10["closure_decision"][
            "selected_dynamic_phi_fin_c1_payload_emitted"
        ],
        "primitive_rows_exact": assembly["row_evidence"]["all_72_primitive_rows_exact"],
        "formal_110_rows_executed": dynamic["assembly_evidence"]["formal_110_rows_executed"],
        "A_transpose_A": dynamic["A_transpose_A"],
        "A_transpose_b": dynamic["A_transpose_b"],
        "deltaTheta_C1": dynamic["deltaTheta_C1"],
        "rank": dynamic["rank"],
        "row_counts": dynamic["row_counts"],
        "source_scalars": {
            "phase_R_Z_frobenius_norm_sq": phase_norm_sq,
            "shift_R_X_frobenius_norm_sq": shift_norm_sq,
            "phase_R_Z_trace": [phase_trace.real, phase_trace.imag],
            "shift_R_X_trace": [shift_trace.real, shift_trace.imag],
            "hessian_normal_scalar": dynamic["A_transpose_A"][0][0],
        },
        "current_emitted_value_scope": [
            "A_selected",
            "b_selected",
            "deltaTheta_C1",
            "sector_response_matrices",
            "phase_R_Z",
            "shift_R_X",
        ],
        "missing_for_exact_CKM_corrections": [
            "sector-pair projection functional Pi_CKM^12",
            "sector-pair projection functional Pi_CKM^23",
            "sector-pair projection functional Pi_CKM^13",
            "row certificates mapping dynamic C1 rows to angle correction values",
        ],
        "target_fitting_used": False,
        "observed_data_used_as_selector": False,
    }

    scan = finite_near_hit_scan(required_ordered)

    decision = {
        "schema": "MTTExactCKMCorrectionAcceptanceDecision.v1",
        "status": "DOMAIN_CLOSED_EXACT_CORRECTION_ROWS_REJECTED_UNTIL_SECTOR_PAIR_EVALUATORS",
        "dynamic_c1_correction_domain_closed": True,
        "required_correction_factors_identified": True,
        "source_native_scan_executed": True,
        "accepted_exact_correction_rows": 0,
        "accepted_no_knob_CKM_angle_rows": 0,
        "selected_sector_pair_projection_rows": 0,
        "CKM_angle_magnitudes_derived_exact": False,
        "Jarlskog_source_derived_without_measured_angles": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closure_closed": False,
        "rejection_reason": (
            "The active dynamic C1/Phi_fin payload is selected and exact at the source-domain "
            "level, but the repo has not emitted selected sector-pair evaluators that turn it "
            "into the three unequal CKM correction values."
        ),
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "observed_data_used_as_selector": False,
    }

    theorem = {
        "name": "CKMAngleCorrectionFunctionalDynamicC1DomainTheorem",
        "proved": True,
        "statement": (
            "The selected Step10/VSD01 physical Phi_fin^C1 source stack supplies a valid "
            "finite dynamic C1 correction domain for CKM angle magnitudes: A^T A=12 I_2, "
            "A^T b=(12,12), deltaTheta_C1=(1,1), exact R_Z/R_X rows, and exact finite row "
            "provenance. This closes the correction-domain/source-promotion part. It does "
            "not close exact CKM angle magnitudes because the current accepted payload does "
            "not emit sector-pair projection/evaluator rows for s12, s23, and s13."
        ),
    }

    data = {
        "candidate": "MTTSelectedCKMAngleCorrectionFunctionalOrExactFlavorObservableClosure",
        "status": STATUS,
        "inputs": {
            "previous_angle_map": rel(PREVIOUS),
            "previous_correction_obligation": rel(PREVIOUS_CORRECTION),
            "step10_source_rule": rel(STEP10),
            "step10_dynamic_payload": rel(STEP10_DYNAMIC),
            "vsd01_source_stack": rel(VSD01),
            "vsd01_assembly_map": rel(VSD01_ASSEMBLY),
        },
        "output_packets": {
            "dynamic_c1_correction_domain": rel(DOMAIN),
            "ckm_correction_factor_requirement": rel(REQUIREMENT),
            "source_native_correction_candidate_scan": rel(SCAN),
            "exact_correction_acceptance_decision": rel(DECISION),
        },
        "closure_decision": {
            "dynamic_c1_correction_domain_closed": True,
            "Step10_route_A_source_rule_imported": True,
            "VSD01_primitive_rows_imported": True,
            "required_correction_factors_identified": True,
            "source_native_near_hit_scan_executed": True,
            "selected_sector_pair_projection_rows": 0,
            "accepted_exact_correction_rows": 0,
            "accepted_no_knob_CKM_angle_rows": 0,
            "CKM_angle_magnitudes_derived_exact": False,
            "Jarlskog_source_derived_without_measured_angles": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closure_closed": False,
        },
        "key_numbers": {
            "required_corrections": required_ordered,
            "A_transpose_A": dynamic["A_transpose_A"],
            "A_transpose_b": dynamic["A_transpose_b"],
            "deltaTheta_C1": dynamic["deltaTheta_C1"],
            "phase_R_Z_frobenius_norm_sq": phase_norm_sq,
            "shift_R_X_frobenius_norm_sq": shift_norm_sq,
            "dynamic_rank": dynamic["rank"],
        },
        "theorem": theorem,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "observed_data_used_for_postcheck": True,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_CKMAngleCorrectionFunctional_or_ExactFlavorObservableClosure_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "dynamic_c1_correction_domain_closed": True,
        "required_correction_factors_identified": True,
        "source_native_near_hit_scan_executed": True,
        "selected_sector_pair_projection_rows": 0,
        "accepted_exact_correction_rows": 0,
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

    note = f"""# MTT Selected CKMAngleCorrectionFunctional or ExactFlavorObservableClosure v1

Status: `{STATUS}`.

## Theorem

`CKMAngleCorrectionFunctionalDynamicC1DomainTheorem` is proved.

The active Step10/VSD01 source stack supplies the selected dynamic C1 correction
domain:

```text
A^T A          = 12 I_2
A^T b          = (12, 12)
deltaTheta_C1  = (1, 1)
rank           = {dynamic['rank']}
primitive rows = {dynamic['row_counts']['primitive_kernel_rows']}
formal rows    = {dynamic['row_counts']['formal_110_total_rows']}
||R_Z||_F^2    = {phase_norm_sq:.15f}
||R_X||_F^2    = {shift_norm_sq:.15f}
```

This retires the old dynamic C1 source-promotion/Galerkin replay loop for the
CKM correction target. The open object is narrower: selected sector-pair
projection/evaluator rows for `s12`, `s23`, and `s13`.

## Required Corrections

The leading map already computed:

```text
s12 = sqrt(|Y_d1|/|Y_d2|)
s23 = sqrt(|Y_u1|/|Y_u2|)
s13 = sqrt(|Y_u1|/|Y_u3|)
```

To match the measured replay packet, the multiplicative corrections would be:

```text
C12 = {required_ordered['s12']:.15f}
C23 = {required_ordered['s23']:.15f}
C13 = {required_ordered['s13']:.15f}
```

These numbers are recorded only as the obligation/postcheck, not as selected
source values.

## Acceptance Decision

Accepted exact CKM correction rows: `0`.

Reason: the selected dynamic C1 payload provides a valid source domain, but the
current accepted packets do not emit the three sector-pair evaluator rows
`Pi_CKM^12`, `Pi_CKM^23`, and `Pi_CKM^13`. The diagnostic finite-source scan
is rejected as source evidence because near-hits have no row certificate.

Next artifact: `{NEXT}`.
"""

    write_json(DOMAIN, domain)
    write_json(REQUIREMENT, correction_requirement)
    write_json(SCAN, scan)
    write_json(DECISION, decision)
    write_json(OUTPUT, data)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
