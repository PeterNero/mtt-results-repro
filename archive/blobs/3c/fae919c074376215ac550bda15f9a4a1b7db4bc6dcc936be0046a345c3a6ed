"""Attempt to fill the selected matter-slot transversality source packet.

The first fill route is Route C, because it is the current executable spectral
pipeline.  The present Route C branch-smoke package has useful finite algebra,
but its honest validators still fail selected-origin gates.  This script makes
that blocker explicit in a packet consumed by
validate_selected_matter_slot_transversality_source.py.
"""

from __future__ import annotations

import json
import math
import re
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATES = ROOT / "certificates"
OUT_PACKET = CERTIFICATES / "selected_matter_slot_transversality_source.attempt.json"
OUT_CANDIDATE = ROOT / "candidate_data" / "selected_matter_slot_transversality_source_attempt.candidate.json"
OUT_CERT = CERTIFICATES / "selected_matter_slot_transversality_source_attempt_certificate.json"
VALIDATOR = ROOT / "scripts" / "validate_selected_matter_slot_transversality_source.py"
OMEGA = complex(-0.5, math.sqrt(3) / 2.0)
TOL = 1e-10


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def cert(name: str) -> dict[str, Any]:
    return load_json(CERTIFICATES / name)


def get(data: dict[str, Any], *keys: str, default: Any = None) -> Any:
    value: Any = data
    for key in keys:
        if not isinstance(value, dict) or key not in value:
            return default
        value = value[key]
    return value


def encode_scalar(value: complex) -> float | list[float]:
    real = 0.0 if abs(value.real) < TOL else value.real
    imag = 0.0 if abs(value.imag) < TOL else value.imag
    if imag == 0.0:
        return real
    return [real, imag]


def encode(value: Any) -> Any:
    if isinstance(value, complex):
        return encode_scalar(value)
    if isinstance(value, list):
        return [encode(item) for item in value]
    if isinstance(value, dict):
        return {key: encode(item) for key, item in value.items()}
    return value


def identity() -> list[list[complex]]:
    return [[1.0 + 0j if row == col else 0j for col in range(3)] for row in range(3)]


def fourier() -> list[list[complex]]:
    scale = 1.0 / math.sqrt(3)
    return [[OMEGA ** (row * col) * scale for col in range(3)] for row in range(3)]


def parse_report(output: str) -> dict[str, Any]:
    match = re.search(r"matter_slot_source_validation_report=(\{.*\})", output)
    if not match:
        return {}
    return json.loads(match.group(1))


def run_validator(path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(path)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return {
        "exit_code": proc.returncode,
        "stdout": proc.stdout,
        "report": parse_report(proc.stdout),
    }


def validator_pass(validators: dict[str, Any], name: str) -> bool:
    return get(validators, name, "pass") is True


def route_c_q79_status() -> dict[str, Any]:
    route_c = cert("iwasawa_route_c_branch_smoke_attempt_certificate.json")
    q79 = get(route_c, "branches", "current_q79_orientation", default={})
    honest = get(q79, "validators", "honest_unselected", default={})
    lifted = get(q79, "validators", "lifted_selected_flags_smoke", default={})
    return {
        "branch_packet": q79.get("branch_packet", {}),
        "honest_route_c_residual_pass": validator_pass(honest, "route_c_residual"),
        "honest_rhoE_mesh_pass": validator_pass(honest, "rhoE_mesh"),
        "honest_rhoE_metric_pass": validator_pass(honest, "rhoE_metric"),
        "honest_sector_maps_pass": validator_pass(honest, "sector_maps"),
        "honest_de_action_pass": validator_pass(honest, "de_action"),
        "honest_riesz_gap_pass": validator_pass(honest, "riesz_gap"),
        "honest_reduced_green_pass": validator_pass(honest, "reduced_green"),
        "honest_dotd_response_pass": validator_pass(honest, "dotd_response"),
        "lifted_selected_flags_all_validators_pass": all(
            validator_pass(lifted, name)
            for name in (
                "route_c_residual",
                "rhoE_mesh",
                "rhoE_metric",
                "sector_maps",
                "de_action",
                "riesz_gap",
                "reduced_green",
                "dotd_response",
            )
        ),
        "selected_origin_still_missing": get(
            route_c, "calculation_results", "selected_origin_still_missing"
        )
        is True,
    }


def build_packet(route_status: dict[str, Any]) -> dict[str, Any]:
    source_verified = False
    return encode(
        {
            "schema": "SelectedMatterSlotTransversalitySource.v1",
            "status": "ROUTE_C_SOURCE_ATTEMPT_BLOCKED_SELECTED_ORIGIN_MISSING",
            "purpose": "Attempted Route C fill for the source theorem selecting 10_M clock and bar5_M shift.",
            "source": {
                "source_kind": "route_c_spectral_galerkin",
                "source_certificate": "iwasawa_route_c_branch_smoke_attempt_certificate.json",
                "selected_by_mtt": source_verified,
                "fixture_only": True,
                "uses_observed_flavor_inputs": False,
                "uses_benchmark_flavor_inputs": False,
            },
            "branch": {
                "q": 79,
                "orientation": "F",
                "retarded_q79_branch_selected": True,
                "antiunitary_conjugate_retained": True,
            },
            "route_c_evidence": {
                "selected_origin_verified": not route_status["selected_origin_still_missing"],
                "honest_route_c_residual_pass": route_status["honest_route_c_residual_pass"],
                "honest_de_action_pass": route_status["honest_de_action_pass"],
                "honest_riesz_gap_pass": route_status["honest_riesz_gap_pass"],
                "honest_reduced_green_pass": route_status["honest_reduced_green_pass"],
                "honest_dotd_response_pass": route_status["honest_dotd_response_pass"],
                "honest_rhoE_mesh_pass": route_status["honest_rhoE_mesh_pass"],
                "honest_rhoE_metric_pass": route_status["honest_rhoE_metric_pass"],
                "honest_sector_maps_pass": route_status["honest_sector_maps_pass"],
                "lifted_selected_flags_all_validators_pass": route_status[
                    "lifted_selected_flags_all_validators_pass"
                ],
            },
            "matter_slot_source": {
                "common_family_frame_verified": route_status["honest_sector_maps_pass"],
                "L2_metrics_selected": False,
                "projector_retention_selected": False,
                "zero_mode_basis_selected": False,
                "cross_pairing_metric_10_bar5": identity(),
                "slots": {
                    "10_M": {
                        "dimension": 3,
                        "polarization": "clock",
                        "basis_matrix_U10": identity(),
                        "selected_source_verified": False,
                        "basis_origin": "finite transversality candidate, not selected Route C output",
                    },
                    "bar5_M": {
                        "dimension": 3,
                        "polarization": "shift",
                        "basis_matrix_Ubar5": fourier(),
                        "selected_source_verified": False,
                        "basis_origin": "finite transversality candidate, not selected Route C output",
                    },
                },
            },
            "guardrails": {
                "claims_full_sm_closure": False,
                "uses_common_fourier_gauge_as_physical_mixing": False,
                "uses_observed_flavor_data": False,
                "uses_benchmark_flavor_entries": False,
            },
        }
    )


def analyze() -> dict[str, Any]:
    route_status = route_c_q79_status()
    packet = build_packet(route_status)
    OUT_PACKET.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    validator = run_validator(OUT_PACKET)
    report = {
        "calculation": "SelectedMatterSlotTransversalitySourceRouteCAttempt",
        "generated_by": "scripts/attempt_fill_selected_matter_slot_transversality_source.py",
        "attempt_packet": str(OUT_PACKET.relative_to(ROOT)).replace("\\", "/"),
        "route_c_status": route_status,
        "validator": validator,
        "calculation_results": {
            "route_c_q79_branch_available": bool(route_status["branch_packet"]),
            "route_c_honest_rhoE_metric_sector_pass": route_status["honest_rhoE_mesh_pass"]
            and route_status["honest_rhoE_metric_pass"]
            and route_status["honest_sector_maps_pass"],
            "route_c_honest_selected_origin_pass": route_status["honest_route_c_residual_pass"]
            and route_status["honest_de_action_pass"]
            and route_status["honest_riesz_gap_pass"]
            and route_status["honest_reduced_green_pass"]
            and route_status["honest_dotd_response_pass"],
            "route_c_selected_origin_still_missing": route_status[
                "selected_origin_still_missing"
            ],
            "lifted_selected_flags_algebra_passes": route_status[
                "lifted_selected_flags_all_validators_pass"
            ],
            "attempt_packet_relative_transport_is_F": get(
                validator, "report", "matter_slot_source", "relative_transport_orientation"
            )
            == "F",
            "validator_exit_code": validator["exit_code"],
            "selected_source_verified": get(
                validator, "report", "selected_source_verified"
            )
            is True,
            "promotes_su5_matter_slot_transversality": get(
                validator, "report", "promotes_su5_matter_slot_transversality"
            )
            is True,
        },
        "what_this_closes": {
            "source_packet_interface_instantiated": True,
            "route_c_first_fill_attempt_executed": True,
            "finite_I_F_matrices_not_the_blocker": get(
                validator, "report", "matter_slot_source", "relative_transport_orientation"
            )
            == "F",
            "route_c_selected_origin_blocker_confirmed": validator["exit_code"] == 1,
        },
        "still_open": {
            "route_c_selected_origin": True,
            "selected_D_E_dotD_same_branch": True,
            "selected_projector_retention": True,
            "selected_zero_mode_basis_from_geometry": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_selected_source_verified": False,
            "claims_ordered_su5_packet_selected": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
            "claims_full_SM_closure": False,
        },
        "verdict": {
            "attempted_route_c_fill": True,
            "selected_source_verified": False,
            "current_status": "BLOCKED_ROUTE_C_SELECTED_ORIGIN_MISSING",
            "next_required_input": "replace Route C smoke selected flags with a genuine selected HYM/Strominger or spectral Galerkin residual solve whose honest validators pass",
        },
    }
    OUT_CANDIDATE.parent.mkdir(parents=True, exist_ok=True)
    OUT_CANDIDATE.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    certificate = {
        "certificate": "SelectedMatterSlotTransversalitySourceAttempt",
        "status": "SELECTED_MATTER_SLOT_TRANSVERSALITY_SOURCE_ATTEMPT_BLOCKED_ROUTE_C_SELECTED_ORIGIN_MISSING",
        "candidate_data": str(OUT_CANDIDATE.relative_to(ROOT)).replace("\\", "/"),
        "attempt_packet": str(OUT_PACKET.relative_to(ROOT)).replace("\\", "/"),
        "analysis_script": "scripts/attempt_fill_selected_matter_slot_transversality_source.py",
        "validator_script": "scripts/validate_selected_matter_slot_transversality_source.py",
        "calculation_results": report["calculation_results"],
        "what_this_closes": report["what_this_closes"],
        "still_open": report["still_open"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    OUT_CERT.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return report


def main() -> int:
    print(json.dumps(analyze(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
