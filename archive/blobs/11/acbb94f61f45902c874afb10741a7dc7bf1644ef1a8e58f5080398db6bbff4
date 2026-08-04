"""Reduce the Qa/SU3 next gate to a selected spectral fallback source solve."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
Q79_REPO = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")

TERMINAL_LANE = CERTS / "selected_qa_su3_terminal_monad_lane_selector_attempt_certificate.json"
Q79_SPECTRAL_GATE = Q79_REPO / "certificates" / "iwasawa_spectral_operator_gate_certificate.json"
Q79_GALERKIN_PROTOCOL = Q79_REPO / "certificates" / "iwasawa_non_invariant_galerkin_protocol_certificate.json"
Q79_ROUTE_C_SMOKE = Q79_REPO / "certificates" / "iwasawa_route_c_branch_smoke_attempt_certificate.json"

OUTPUT_TEMPLATE = CERTS / "selected_qa_su3_spectral_fallback_source_solve.template.json"
OUTPUT_CERT = CERTS / "selected_qa_su3_spectral_fallback_reduction_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def make_template() -> dict[str, Any]:
    return {
        "schema": "SelectedQaSU3SpectralFallbackSourceSolve.v1",
        "status": "OPEN_SELECTED_QA_SU3_SPECTRAL_FALLBACK_SOURCE_SOLVE_REQUIRED",
        "purpose": (
            "Replace the unselected Route C smoke data by a genuine selected "
            "finite HYM/Strominger or Dolbeault operator source, then rerun the "
            "same D_E, Riesz, Green, dotD, and sector validators."
        ),
        "must_supply": {
            "selected_D_E_source": None,
            "route_c_residual_solve_or_typed_monad_operator": None,
            "selected_source_flags_justified_not_lifted": None,
            "same_branch_rhoE_metric_sector_data": None,
            "D_E_action_certificate": None,
            "Riesz_gap_certificate": None,
            "reduced_Green_certificate": None,
            "dotD_alpha1_certificate": None,
            "primitive_overlap_or_C1_contractions": None,
        },
        "forbidden_shortcuts": [
            "Do not turn lifted smoke flags into selected-source proof.",
            "Do not use observed masses or mixings to select the projector.",
            "Do not reuse the rank-one seed as the full family basis.",
        ],
    }


def all_lifted_validators_pass(route_c: dict[str, Any], branch: str) -> bool:
    validators = route_c["branches"][branch]["validators"]["lifted_selected_flags_smoke"]
    return all(item["pass"] is True for item in validators.values())


def honest_exit_codes(route_c: dict[str, Any], branch: str) -> dict[str, int]:
    validators = route_c["branches"][branch]["validators"]["honest_unselected"]
    return {name: int(item["exit_code"]) for name, item in sorted(validators.items())}


def main() -> None:
    terminal = load(TERMINAL_LANE)
    spectral = load(Q79_SPECTRAL_GATE)
    protocol = load(Q79_GALERKIN_PROTOCOL)
    route_c = load(Q79_ROUTE_C_SMOKE)

    branch = "current_q79_orientation"
    honest = honest_exit_codes(route_c, branch)
    honest_passes = [name for name, code in honest.items() if code == 0]
    honest_fails = [name for name, code in honest.items() if code != 0]

    finite_pipeline_available_conditionally = (
        spectral["verdict"]["closes_spectral_fallback_input_contract"] is True
        and protocol["verdict"]["closes_execution_protocol"] is True
        and all_lifted_validators_pass(route_c, branch)
    )
    honest_source_failure_is_exact = honest_passes == [
        "rhoE_mesh",
        "rhoE_metric",
        "sector_maps",
    ] and honest_fails == [
        "de_action",
        "dotd_response",
        "reduced_green",
        "riesz_gap",
        "route_c_residual",
    ]

    output = {
        "certificate": "SelectedQaSU3SpectralFallbackReduction",
        "status": "QA_SU3_SPECTRAL_FALLBACK_REDUCED_TO_SELECTED_SOURCE_SOLVE",
        "inputs": {
            "terminal_lane_gate": str(TERMINAL_LANE.relative_to(ROOT)),
            "q79_spectral_operator_gate": str(Q79_SPECTRAL_GATE),
            "q79_non_invariant_galerkin_protocol": str(Q79_GALERKIN_PROTOCOL),
            "q79_route_c_branch_smoke": str(Q79_ROUTE_C_SMOKE),
        },
        "template_written": str(OUTPUT_TEMPLATE.relative_to(ROOT)),
        "closed_now": {
            "spectral_fallback_input_contract_closed": spectral["verdict"][
                "closes_spectral_fallback_input_contract"
            ],
            "finite_galerkin_execution_protocol_closed": protocol["verdict"][
                "closes_execution_protocol"
            ],
            "current_q79_branch_finite_pipeline_conditionally_validates": finite_pipeline_available_conditionally,
            "rhoE_metric_sector_algebra_passes_honestly": honest_passes
            == ["rhoE_mesh", "rhoE_metric", "sector_maps"],
            "honest_failures_are_selected_source_failures": honest_source_failure_is_exact,
            "terminal_lane_arithmetic_already_closed": terminal["closed_now"][
                "conditional_uniqueness_inside_terminal_lane"
            ],
        },
        "not_closed": {
            "selected_D_E_source": protocol["values_still_open"]["selected_D_E"],
            "basis_B_N_values": protocol["values_still_open"]["basis_B_N"],
            "operator_matrix_L_N_values": protocol["values_still_open"]["K_N"],
            "eigenpairs_and_Psi_i_values": protocol["values_still_open"]["eigenpairs"],
            "dotD_alpha1_values": protocol["values_still_open"]["dotD_alpha1"],
            "primitive_overlap_or_C1_contractions": True,
            "full_SM_closure": True,
        },
        "honest_current_q79_validator_exit_codes": honest,
        "conditional_smoke_result": {
            "lifted_selected_flags_all_validators_pass": route_c["calculation_results"][
                "lifted_selected_flags_all_validators_pass"
            ][branch],
            "route_c_residual_values_are_smoke_not_solve": route_c["calculation_results"][
                "route_c_residual_values_are_smoke_not_solve"
            ],
            "selected_origin_still_missing": route_c["calculation_results"][
                "selected_origin_still_missing"
            ],
        },
        "next_object": {
            "name": "Selected_Qa_SU3_RouteC_Source_Solve_or_Typed_Operator_v1",
            "accepted_routes": protocol["operator_source_gate"]["accepted_sources"],
            "rejected_routes": protocol["operator_source_gate"]["rejected_sources"],
            "exact_task": (
                "Justify selected_source_verified and selected_dotD_source_verified "
                "from a genuine same-branch source, then rerun the existing finite "
                "validators without lifted smoke flags."
            ),
        },
        "guardrails": {
            "claims_selected_D_E_constructed": False,
            "claims_route_c_residual_solve": False,
            "claims_kernel_dimension_three_as_selected": False,
            "claims_full_SM_closure": False,
            "uses_observed_masses_or_mixings": False,
            "uses_lifted_flags_as_proof": False,
        },
    }

    cert_text = json.dumps(output, indent=2, sort_keys=True)
    template_text = json.dumps(make_template(), indent=2, sort_keys=True)
    if "--write-certificate" in sys.argv:
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
        OUTPUT_TEMPLATE.write_text(template_text + "\n", encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
