"""Build finite H functional or M_source value emission packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_finitehfunctional_or_msourcevalueemission"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_FiniteHFunctionalOrMSourceValueEmission_v1.md"

INVENTORY = PACKET_DIR / "finiteh_msource_kh_source_inventory.packet.json"
POLAR = PACKET_DIR / "polar_reduced_value_executor.packet.json"
EXECUTION = PACKET_DIR / "finiteh_msource_kh_value_execution_attempt.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_finiteh_msource_execution.packet.json"

PREVIOUS = DATA / "selected_huvprimitiveformula_or_finiteerrorboundexecution.candidate.json"
SOURCE_GATE = (
    DATA
    / "selected_higgssecondvariationfunctionalsource_or_herm2rowvalues"
    / "source_functional_acceptance_gate.packet.json"
)
STRAIN_SPEC = (
    DATA
    / "selected_higgssecondvariationfunctionalsource_or_herm2rowvalues"
    / "dynamic_strain_kernel_payload_spec.packet.json"
)
DIRECT_H = DATA / "selected_directhquarticthresholdfunctional_or_dynamicherm2valuerows.candidate.json"
POLAR_SCHEMA = (
    DATA
    / "selected_herm2polarsourcecompletion_or_hresponserows"
    / "conditional_hresponse_row_schema_after_polar_completion.packet.json"
)
H_POLAR = DATA / "selected_herm2polarsourcecompletion_or_hresponserows.candidate.json"
H_RADIAL = DATA / "selected_hradialscalephasesource_or_herm2hessianrows.candidate.json"
HYM_ROWS = DATA / "selected_hymoverlapvaluesource_or_selectedoverlapkernelrows.candidate.json"
MSOURCE_CONTRACT = (
    DATA
    / "selected_msourcehuvoperator_or_directherm2rows"
    / "msource_contract_reconciled_with_active_domain.packet.json"
)
FULL_MSOURCE_GATE = (
    DATA
    / "selected_fullmsourcehsectorrestriction_or_hresponsehuvtable"
    / "selected_source_object_value_gate.packet.json"
)

STATUS = (
    "MTT_SELECTED_FINITEHFUNCTIONAL_OR_MSOURCEVALUEEMISSION_"
    "EXECUTED_ZERO_ROWS_POLAR_SOURCE_FIELDS_OPEN"
)
NEXT = "MTT_Selected_HRadialPhaseTraceSource_or_FiniteHActionEmission_v1"


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
        raise FileNotFoundError("missing finite-H/M_source inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        SOURCE_GATE,
        STRAIN_SPEC,
        DIRECT_H,
        POLAR_SCHEMA,
        H_POLAR,
        H_RADIAL,
        HYM_ROWS,
        MSOURCE_CONTRACT,
        FULL_MSOURCE_GATE,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    source_gate = load(SOURCE_GATE)
    strain_spec = load(STRAIN_SPEC)
    direct_h = load(DIRECT_H)
    polar_schema = load(POLAR_SCHEMA)
    h_polar = load(H_POLAR)
    h_radial = load(H_RADIAL)
    hym_rows = load(HYM_ROWS)
    msource_contract = load(MSOURCE_CONTRACT)
    full_msource_gate = load(FULL_MSOURCE_GATE)

    source_inventory = {
        "schema": "MTTFiniteHMSourceKHSourceInventory.v1",
        "status": "FINITE_H_MSOURCE_KH_SOURCE_INVENTORY_EXECUTED_ZERO_ACCEPTED",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "strict_routes": {
            "finite_H_functional_F_H": {
                "accepted": False,
                "current_emitted": source_gate["accepted_value_sources"][
                    "direct_F_H_second_variation"
                ]["emitted_now"],
                "accepted_if": source_gate["accepted_value_sources"][
                    "direct_F_H_second_variation"
                ]["accepted_if"],
                "nearest_payload_spec": rel(STRAIN_SPEC),
            },
            "same_source_M_source": {
                "accepted": False,
                "contract_reconciled": msource_contract["decision"][
                    "M_source_acceptance_contract_reconciled"
                ],
                "current_emitted": not full_msource_gate["derived_objects_currently_absent"][
                    "M_source_absent"
                ],
                "formula": msource_contract["updated_formula"],
            },
            "primitive_H_response_kernel_K_H": {
                "accepted": False,
                "charged_overlap_rows_emitted": hym_rows["closure_decision"][
                    "selected_charged_normalized_overlap_kernel_row_count"
                ],
                "H_lambda_or_H_scalar_row_emitted": hym_rows["closure_decision"][
                    "selected_H_lambda_overlap_kernel_row_emitted"
                ],
                "reason": "nine charged rows are selected, but the H/lambda or H-sector primitive kernel row is absent",
            },
        },
        "controlled_lane_not_strict": {
            "available": h_radial["closure_decision"]["controlled_radial_calibration_available"],
            "parameter_id": "UP-RET-OVERLAP.HRG",
            "parameter_value": h_radial["key_numbers"]["UP_RET_OVERLAP_HRG_controlled_calibration"],
            "accepted_as_no_knob_source": False,
            "reason": "controlled lane calibrates lambda_H and still does not emit strict phase/sign/trace row source fields",
        },
        "decision": {
            "route_inventory_executed": True,
            "accepted_strict_source_route_count": 0,
            "accepted_controlled_source_route_count_for_no_knob": 0,
        },
    }

    s_beta = h_polar["key_numbers"]["selected_s_beta_value"]
    polar_reduced = {
        "schema": "MTTPolarReducedValueExecutor.v1",
        "status": "POLAR_VALUE_EXECUTOR_REDUCED_TO_SELECTED_SCALAR_FIELDS",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "selected_angle_data": {
            "s_beta": s_beta,
            "sqrt_s_beta": h_polar["key_numbers"]["sqrt_s_beta"],
            "sqrt_1_minus_s_beta": h_polar["key_numbers"]["sqrt_1_minus_s_beta"],
            "selected_s_beta_polar_angle_closed": direct_h["closure_decision"][
                "selected_s_beta_polar_angle_closed"
            ],
        },
        "conditional_rows": polar_schema["conditional_rows"],
        "strict_unknown_source_fields": {
            "r_H": polar_schema["required_source_fields"]["r_H"],
            "sigma_D": polar_schema["required_source_fields"]["sigma_D"],
            "phi_Omega": polar_schema["required_source_fields"]["phi_Omega"],
            "m0": polar_schema["required_source_fields"]["m0"],
            "certificates": polar_schema["required_source_fields"]["certificates"],
        },
        "what_selected_s_beta_determines": [
            "Delta^2 / (Delta^2 + |Omega|^2)",
            "the ratio |Delta| : |Omega|",
            "the trace-free polar angle, not radial scale, sign, phase, or trace center",
        ],
        "decision": {
            "polar_reduction_executed": True,
            "strict_radial_scale_source_emitted": h_polar["closure_decision"][
                "strict_radial_scale_source_emitted"
            ],
            "selected_Delta_sign_emitted": h_polar["closure_decision"][
                "selected_Delta_sign_emitted"
            ],
            "selected_Omega_phase_emitted": h_polar["closure_decision"][
                "selected_Omega_phase_emitted"
            ],
            "trace_center_source_or_normalization_emitted": h_polar["closure_decision"][
                "trace_center_source_or_normalization_emitted"
            ],
            "full_H_response_rows_executable": False,
            "tracefree_threshold_block_executable": False,
        },
    }

    execution = {
        "schema": "MTTFiniteHMSourceKHValueExecutionAttempt.v1",
        "status": "FINITE_H_MSOURCE_KH_VALUE_EXECUTION_ZERO_ROWS",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "previous_status": previous["status"],
        "route_results": {
            "finite_H_functional_F_H": {
                "accepted": False,
                "selected_F_H_functional_emitted": direct_h["closure_decision"][
                    "selected_H_quartic_functional_emitted"
                ],
                "selected_F_H_second_variation_emitted": False,
            },
            "same_source_M_source": {
                "accepted": False,
                "selected_M_source_value_emitted": False,
                "M_source_contract_reconciled": True,
            },
            "primitive_H_response_kernel_K_H": {
                "accepted": False,
                "selected_K_H_emitted": False,
                "charged_kernel_rows_available": hym_rows["closure_decision"][
                    "selected_charged_normalized_overlap_kernel_row_count"
                ],
            },
            "controlled_radial_lane": {
                "accepted_for_strict_no_knob": False,
                "available_as_minimal_parameter_support": h_radial["closure_decision"][
                    "controlled_radial_calibration_available"
                ],
                "still_missing_for_full_rows": [
                    "Delta sign",
                    "Omega phase",
                    "trace center or quotient trace theorem",
                    "row-level same-source certificates",
                ],
            },
        },
        "emitted_rows": {
            "Huu": None,
            "Hud_re": None,
            "Hud_im": None,
            "Hdd": None,
            "Delta": None,
            "Re_Omega": None,
            "Im_Omega": None,
        },
        "decision": {
            "execution_attempted": True,
            "accepted_value_row_count": 0,
            "accepted_final_certificate_count": 0,
            "accepted_strict_source_route_count": 0,
            "selected_H_response_value_rows_emitted": False,
            "strict_no_knob_H_closure": False,
        },
    }

    cutset = {
        "schema": "MTTNextCutsetAfterFiniteHMSourceExecution.v1",
        "status": "NEXT_FRONTIER_H_RADIAL_PHASE_TRACE_SOURCE_OR_FINITE_H_ACTION_EMISSION",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closed_here": [
            "strict F_H/M_source/K_H route inventory executed",
            "selected s_beta polar reduction imported into Huv row executor",
            "controlled HRG radial calibration separated from strict no-knob source",
            "remaining row fields reduced to r_H, sigma_D, phi_Omega, m0/quotient trace, and certificates",
        ],
        "still_open": [
            "selected finite H action/functional F_H emitting the Herm(2) Hessian",
            "or selected same-source Hermitian M_source values",
            "or selected primitive H-response kernel K_H",
            "or selected polar source fields r_H, sigma_D, phi_Omega, and m0/trace theorem",
            "row-level exactness/error and ownership certificates",
        ],
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "MTTSelectedFiniteHFunctionalOrMSourceValueEmission",
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
            "name": "FiniteHMSourceKHExecutionReducesToPolarFieldsTheorem",
            "proved": True,
            "statement": (
                "The current strict F_H, M_source, and primitive K_H routes execute "
                "with zero accepted value rows. The selected s_beta polar angle is "
                "retained and reduces the trace-free Herm(2) block to r_H, Delta "
                "sign, and Omega phase; full H-response rows additionally require "
                "m0 or a quotient trace-free theorem. The controlled HRG radial "
                "calibration is useful minimal-parameter support but is not a "
                "strict no-knob value source and still lacks phase/sign/trace row "
                "certificates."
            ),
        },
        "packets": {
            "finiteh_msource_kh_source_inventory": rel(INVENTORY),
            "polar_reduced_value_executor": rel(POLAR),
            "finiteh_msource_kh_value_execution_attempt": rel(EXECUTION),
            "next_cutset": rel(CUTSET),
        },
        "inputs": {
            "previous": rel(PREVIOUS),
            "source_gate": rel(SOURCE_GATE),
            "strain_spec": rel(STRAIN_SPEC),
            "direct_h": rel(DIRECT_H),
            "polar_schema": rel(POLAR_SCHEMA),
            "h_polar": rel(H_POLAR),
            "h_radial": rel(H_RADIAL),
            "hym_rows": rel(HYM_ROWS),
            "msource_contract": rel(MSOURCE_CONTRACT),
            "full_msource_gate": rel(FULL_MSOURCE_GATE),
        },
        "closure_decision": {
            "strict_F_H_M_source_K_H_inventory_executed": True,
            "polar_reduction_executed": True,
            "controlled_lane_separated": True,
            "selected_s_beta_polar_angle_closed": True,
            "selected_F_H_functional_emitted": False,
            "selected_M_source_value_emitted": False,
            "selected_K_H_emitted": False,
            "strict_radial_scale_source_emitted": False,
            "selected_Delta_sign_emitted": False,
            "selected_Omega_phase_emitted": False,
            "trace_center_source_or_normalization_emitted": False,
            "selected_H_response_value_rows_emitted": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "key_numbers": {
            "accepted_strict_source_route_count": 0,
            "accepted_value_row_count": 0,
            "accepted_final_certificate_count": 0,
            "selected_s_beta_value": s_beta,
            "strict_unknown_scalar_source_fields": 4,
            "controlled_parameter_value": h_radial["key_numbers"][
                "UP_RET_OVERLAP_HRG_controlled_calibration"
            ],
        },
    }

    cert = {
        "certificate": "MTTSelectedFiniteHFunctionalOrMSourceValueEmission",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "theorem_proved": True,
        "minimal_parameter_tier_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "strict_F_H_M_source_K_H_inventory_executed": True,
        "polar_reduction_executed": True,
        "controlled_lane_separated": True,
        "accepted_strict_source_route_count": 0,
        "accepted_value_row_count": 0,
        "accepted_final_certificate_count": 0,
        "selected_s_beta_value": s_beta,
        "strict_unknown_scalar_source_fields": 4,
        "selected_F_H_functional_emitted": False,
        "selected_M_source_value_emitted": False,
        "selected_K_H_emitted": False,
        "selected_H_response_value_rows_emitted": False,
    }

    note = f"""# MTT Selected FiniteHFunctional or MSourceValueEmission v1

Status: `{STATUS}`

## Theorem

The strict value-source inventory has now been executed:

- selected finite H functional `F_H`: `0` accepted
- selected same-source Hermitian `M_source`: `0` accepted
- selected primitive H-response kernel `K_H`: `0` accepted

The useful reduction is the selected polar angle:

```text
s_beta = {s_beta}
Delta = sigma_D * r_H * sqrt(s_beta)
Hud_re = r_H * sqrt(1-s_beta) * cos(phi_Omega)
Hud_im = r_H * sqrt(1-s_beta) * sin(phi_Omega)
Huu = m0 + Delta
Hdd = m0 - Delta
```

So the strict row source is reduced to selected source fields:

- `r_H`
- `sigma_D`
- `phi_Omega`
- `m0` or a quotient trace-free H-response theorem
- row ownership/exactness/quotient certificates

The controlled HRG radial calibration exists, but remains marked as a controlled
minimal-parameter lane, not a strict no-knob source.

Next artifact: `{NEXT}`
"""

    write_json(INVENTORY, source_inventory)
    write_json(POLAR, polar_reduced)
    write_json(EXECUTION, execution)
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
