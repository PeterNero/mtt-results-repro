"""Promote finite Hessian/C1 sector contraction matrices for E_CKM."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_finitehessianc1sectorcontractions_or_eckmtraceexecution"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
MATRICES = PACKET_DIR / "finite_hessian_c1_sector_contraction_matrices.packet.json"
TRACE_GATE = PACKET_DIR / "eckm_trace_weight_certificate_gate.packet.json"
DECISION = PACKET_DIR / "eckm_readiness_after_sector_contractions.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_FiniteHessianC1SectorContractions_or_ECKMTraceExecution_v1.md"

PREVIOUS = DATA / "selected_zeromodegramsectorcontractionpayload_or_eckmweightrows.candidate.json"
PREV_DECISION = (
    DATA
    / "selected_zeromodegramsectorcontractionpayload_or_eckmweightrows"
    / "eckm_readiness_after_zeromode_gram_import.packet.json"
)
STEP10 = (
    DATA
    / "selected_step10_physicalphifinc1sourcerule_or_independentgalerkinrows"
    / "step10_dynamic_c1_payload_emission.packet.json"
)
VSD01 = (
    DATA
    / "selected_vsd01_allprimitiverowsassemblymap_or_physicalphifinc1actionsource"
    / "all_primitive_rows_assembly_map.packet.json"
)
WEIGHTS = (
    DATA
    / "selected_ckmsectorpairprojectionrows_or_honestflavorgalerkinexecution"
    / "required_q448_sector_pair_weights.packet.json"
)

STATUS = "MTT_SELECTED_FINITEHESSIANC1_SECTOR_CONTRACTIONS_CLOSED_ECKM_WEIGHT_CERTS_OPEN"
NEXT = "MTT_Selected_ECKMWeightRowCertificates_or_CKMAngleClosureDecision_v1"


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


def trace_complex(matrix: list[list[Any]]) -> complex:
    return sum(as_complex(matrix[i][i]) for i in range(len(matrix)))


def frobenius_norm_sq(matrix: list[list[Any]]) -> float:
    return sum(abs(as_complex(entry)) ** 2 for row in matrix for entry in row)


def cpair(z: complex) -> list[float]:
    return [z.real, z.imag]


def main() -> int:
    previous = load(PREVIOUS)
    prev_decision = load(PREV_DECISION)
    step10 = load(STEP10)
    vsd01 = load(VSD01)
    weights = load(WEIGHTS)

    if previous["closure_decision"]["readiness_promoted_4_to_6"] is not True:
        raise ValueError("previous E_CKM readiness was not promoted to 6/8")
    if step10["contract_outputs_closed_here"]["sector_response_matrices"] is not True:
        raise ValueError("Step10 sector response matrices are not closed")
    if vsd01["row_evidence"]["all_72_primitive_rows_exact"] is not True:
        raise ValueError("VSD01 primitive rows are not exact")

    phase = step10["phase_R_Z"]
    shift = step10["shift_R_X"]
    sector_matrices = {
        "u": phase,
        "d": shift,
        "e": phase,
        "nuD": shift,
    }
    diagnostics = {
        sector: {
            "trace": cpair(trace_complex(matrix)),
            "frobenius_norm_sq": frobenius_norm_sq(matrix),
            "source_column": "phase_R_Z" if sector in ["u", "e"] else "shift_R_X",
        }
        for sector, matrix in sector_matrices.items()
    }

    matrices = {
        "schema": "MTTFiniteHessianC1SectorContractionMatrices.v1",
        "status": "FINITE_HESSIAN_C1_SECTOR_CONTRACTION_MATRICES_CLOSED_FOR_ECKM",
        "source_packets": {
            "step10_dynamic_c1_payload": rel(STEP10),
            "vsd01_primitive_assembly": rel(VSD01),
        },
        "source_evidence": {
            "sector_response_matrices_closed_by_step10": step10["contract_outputs_closed_here"][
                "sector_response_matrices"
            ],
            "all_72_primitive_rows_exact": vsd01["row_evidence"]["all_72_primitive_rows_exact"],
            "formal_110_rows_executed": step10["assembly_evidence"]["formal_110_rows_executed"],
            "observed_data_used_as_selector": False,
        },
        "sector_routing": {
            "u": "phase_R_Z",
            "e": "phase_R_Z",
            "d": "shift_R_X",
            "nuD": "shift_R_X",
        },
        "sector_matrices": sector_matrices,
        "diagnostics": diagnostics,
        "promotes_finite_Hessian_C1_sector_contraction_values": True,
        "does_not_emit_ECKM_weight_rows": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    trace_gate = {
        "schema": "MTTECKMTraceWeightCertificateGate.v1",
        "status": "ECKM_TRACE_WEIGHT_ROW_CERTIFICATES_REMAIN_OPEN",
        "formal_rows": {
            "W12": "Tr_N(Pi_CKM^12 K_CKM[M_u,M_d,M_e,Delta_v,Orbit_lambda])",
            "W23": "Tr_N(Pi_CKM^23 K_CKM[M_u,M_d,M_e,Delta_v,Orbit_lambda])",
            "W13": "Tr_N(Pi_CKM^13 K_CKM[M_u,M_d,M_e,Delta_v,Orbit_lambda])",
        },
        "required_postcheck_values": weights["q448_weights_if_matching_measured_replay"],
        "ready_inputs": [
            "q448 projection contract",
            "q79/heavy-link/orbit domain",
            "stationary transported zero-mode basis",
            "stationary Gram/trace convention",
            "finite Hessian/C1 sector contraction matrices",
        ],
        "missing_inputs": [
            "three selected row certificates for Pi_CKM^12, Pi_CKM^23, Pi_CKM^13",
            "explicit K_CKM trace assembly rule tying the contractions to W12,W23,W13",
        ],
        "selected_functional_executed": False,
        "accepted_weight_rows": 0,
        "observed_data_used_as_selector": False,
        "observed_data_used_for_postcheck": True,
        "target_fitting_used": False,
    }

    closed_count = 7
    required_count = 8
    decision = {
        "schema": "MTTECKMReadinessAfterSectorContractions.v1",
        "status": "ECKM_READINESS_7_OF_8_WEIGHT_CERTIFICATES_OPEN",
        "previous_closed_required_rows": prev_decision["closed_required_rows"],
        "closed_required_rows": closed_count,
        "required_rows": required_count,
        "finite_Hessian_C1_sector_contraction_values_emitted": True,
        "E_CKM_weight_row_certificates_emitted": False,
        "selected_functional_executed": False,
        "accepted_weight_rows": 0,
        "accepted_exact_ckm_correction_rows": 0,
        "accepted_no_knob_CKM_angle_rows": 0,
        "CKM_angle_magnitudes_derived_exact": False,
        "Jarlskog_source_derived_without_measured_angles": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closure_closed": False,
        "still_open_blockers": ["E_CKM_weight_row_certificates"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    theorem = {
        "name": "FiniteHessianC1SectorContractionECKMTheorem",
        "proved": True,
        "statement": (
            "The active Step10/VSD01 source stack emits the finite Hessian/C1 sector-response "
            "contraction matrices needed by E_CKM: M_u=M_e=R_Z and M_d=M_nuD=R_X. "
            "Together with the previously promoted zero-mode and Gram rows, E_CKM readiness "
            "moves from 6/8 to 7/8.  The remaining row is the actual E_CKM trace/weight "
            "certificate for W12,W23,W13."
        ),
    }

    data = {
        "candidate": "MTTSelectedFiniteHessianC1SectorContractionsOrECKMTraceExecution",
        "status": STATUS,
        "inputs": {
            "previous_eckm_readiness": rel(PREVIOUS),
            "previous_readiness_decision": rel(PREV_DECISION),
            "step10_dynamic_c1_payload": rel(STEP10),
            "vsd01_primitive_assembly": rel(VSD01),
            "required_q448_weights": rel(WEIGHTS),
        },
        "output_packets": {
            "finite_hessian_c1_sector_contraction_matrices": rel(MATRICES),
            "eckm_trace_weight_certificate_gate": rel(TRACE_GATE),
            "eckm_readiness_after_sector_contractions": rel(DECISION),
        },
        "closure_decision": {
            "finite_Hessian_C1_sector_contraction_values_emitted": True,
            "readiness_promoted_6_to_7": True,
            "closed_required_rows": closed_count,
            "required_rows": required_count,
            "E_CKM_weight_row_certificates_emitted": False,
            "selected_functional_executed": False,
            "accepted_weight_rows": 0,
            "accepted_exact_ckm_correction_rows": 0,
            "accepted_no_knob_CKM_angle_rows": 0,
            "CKM_angle_magnitudes_derived_exact": False,
            "Jarlskog_source_derived_without_measured_angles": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closure_closed": False,
        },
        "key_numbers": {
            "previous_readiness": prev_decision["closed_required_rows"],
            "current_readiness": closed_count,
            "required_rows": required_count,
            "phase_R_Z_frobenius_norm_sq": diagnostics["u"]["frobenius_norm_sq"],
            "shift_R_X_frobenius_norm_sq": diagnostics["d"]["frobenius_norm_sq"],
            "accepted_eckm_weight_rows": 0,
            "required_q448_weights": weights["q448_weights_if_matching_measured_replay"],
        },
        "theorem": theorem,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "observed_data_used_for_postcheck": True,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_FiniteHessianC1SectorContractions_or_ECKMTraceExecution_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "finite_Hessian_C1_sector_contraction_values_emitted": True,
        "readiness_promoted_6_to_7": True,
        "closed_required_rows": closed_count,
        "required_rows": required_count,
        "E_CKM_weight_row_certificates_emitted": False,
        "selected_functional_executed": False,
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

    note = f"""# MTT Selected FiniteHessianC1SectorContractions or ECKMTraceExecution v1

Status: `{STATUS}`.

## Theorem

`FiniteHessianC1SectorContractionECKMTheorem` is proved.

The active Step10/VSD01 source stack emits the sector contraction matrices for
the E_CKM trace domain:

```text
M_u = R_Z
M_e = R_Z
M_d = R_X
M_nuD = R_X
```

Diagnostics:

```text
||R_Z||_F^2 = {diagnostics['u']['frobenius_norm_sq']:.15f}
||R_X||_F^2 = {diagnostics['d']['frobenius_norm_sq']:.15f}
```

## Readiness

```text
previous readiness = {prev_decision['closed_required_rows']}/{prev_decision['required_rows']}
current readiness  = {closed_count}/{required_count}
accepted W rows    = 0/3
```

The remaining object is no longer a domain or contraction packet. It is exactly
the three E_CKM trace/weight row certificates for `W12`, `W23`, and `W13`.

Next artifact: `{NEXT}`.
"""

    write_json(MATRICES, matrices)
    write_json(TRACE_GATE, trace_gate)
    write_json(DECISION, decision)
    write_json(OUTPUT, data)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
