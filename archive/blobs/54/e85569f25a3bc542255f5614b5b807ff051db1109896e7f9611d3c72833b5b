"""Attempt to create the selected visible Green-Schwarz source packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATES = ROOT / "certificates"
CANDIDATE_DATA = ROOT / "candidate_data"
REQUIREMENT_CERT = CERTIFICATES / "time_oriented_m1_visible_green_schwarz_requirement_certificate.json"
HYM_ATTEMPT_CERT = CERTIFICATES / "selected_hym_operator_source_attempt_certificate.json"
TEMPLATE = CERTIFICATES / "time_oriented_m1_visible_gs_source.template.json"
ATTEMPT = CERTIFICATES / "time_oriented_m1_visible_gs_source.attempt.json"
CANDIDATE = CANDIDATE_DATA / "time_oriented_m1_visible_gs_source_attempt.candidate.json"
CERTIFICATE = CERTIFICATES / "time_oriented_m1_visible_gs_source_attempt_certificate.json"
VALIDATOR = ROOT / "scripts" / "validate_time_oriented_m1_visible_gs_source.py"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def run_validator(path: Path) -> tuple[int, str]:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(path)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return proc.returncode, proc.stdout


def template_packet() -> dict[str, Any]:
    return {
        "schema": "TimeOrientedM1VisibleGreenSchwarzSource.v1",
        "status": "OPEN",
        "requirement_certificate": "time_oriented_m1_visible_green_schwarz_requirement_certificate.json",
        "selected_by_mtt": None,
        "same_branch_as_q79_m1": None,
        "fixture_only": None,
        "curvature_rows": {
            "dH": None,
            "Tr_R_plus_squared": None,
            "Tr_F_visible_squared": None,
            "residual": None,
        },
        "visible_source_evidence": {
            "source_kind": None,
            "selected_visible_bundle_model": None,
            "same_branch_q79_f_m1": None,
            "chern_weil_row_from_source": None,
            "hym_or_route_c_residual_verified": None,
            "source_certificate": None,
        },
        "uses_observed_flavor_data": False,
        "uses_benchmark_flavor_entries": False,
    }


def attempt_packet(requirement: dict[str, Any], hym: dict[str, Any]) -> dict[str, Any]:
    rows = {
        "dH": requirement.get("known_rows", {}).get("dH"),
        "Tr_R_plus_squared": requirement.get("known_rows", {}).get("Tr_R_plus_squared"),
        "Tr_F_visible_squared": requirement.get("derived_required_visible_row", {}).get(
            "Tr_F_visible_squared"
        ),
        "residual": requirement.get("derived_required_visible_row", {}).get("residual_if_supplied"),
    }
    selected_visible_bundle_open = hym.get("still_open", {}).get("selected_visible_sm_bundle_model") is True
    selected_hym_source_verified = (
        hym.get("calculation_results", {}).get("selected_hym_operator_source_verified") is True
    )
    return {
        "schema": "TimeOrientedM1VisibleGreenSchwarzSource.v1",
        "status": "ATTEMPT_BLOCKED_SELECTED_VISIBLE_SOURCE_MISSING",
        "requirement_certificate": "time_oriented_m1_visible_green_schwarz_requirement_certificate.json",
        "selected_by_mtt": False,
        "same_branch_as_q79_m1": True,
        "fixture_only": False,
        "curvature_rows": rows,
        "visible_source_evidence": {
            "source_kind": "finite_HYM_Strominger_solve",
            "selected_visible_bundle_model": False,
            "same_branch_q79_f_m1": True,
            "chern_weil_row_from_source": False,
            "hym_or_route_c_residual_verified": selected_hym_source_verified,
            "source_certificate": "selected_hym_operator_source_attempt_certificate.json",
            "current_blocker": (
                "selected visible SM bundle model is still open"
                if selected_visible_bundle_open
                else "selected HYM source not verified"
            ),
        },
        "uses_observed_flavor_data": False,
        "uses_benchmark_flavor_entries": False,
    }


def attempt_report() -> dict[str, Any]:
    requirement = load_json(REQUIREMENT_CERT)
    hym = load_json(HYM_ATTEMPT_CERT)
    write_json(TEMPLATE, template_packet())
    packet = attempt_packet(requirement, hym)
    write_json(ATTEMPT, packet)
    validator_exit, validator_output = run_validator(ATTEMPT)

    required_row = requirement.get("derived_required_visible_row", {}).get("Tr_F_visible_squared")
    row_filled = packet.get("curvature_rows", {}).get("Tr_F_visible_squared") == required_row
    selected_source_missing = validator_exit == 1

    return {
        "candidate": "TimeOrientedM1VisibleGreenSchwarzSourceAttempt",
        "status": "TIME_ORIENTED_M1_VISIBLE_GS_SOURCE_ATTEMPT_BLOCKED_SELECTED_SOURCE_MISSING",
        "generated_by": "scripts/attempt_time_oriented_m1_visible_gs_source.py",
        "template": "certificates/time_oriented_m1_visible_gs_source.template.json",
        "attempt_packet": "certificates/time_oriented_m1_visible_gs_source.attempt.json",
        "validator": "scripts/validate_time_oriented_m1_visible_gs_source.py",
        "inputs": {
            "requirement_certificate": "time_oriented_m1_visible_green_schwarz_requirement_certificate.json",
            "hym_operator_source_attempt_certificate": "selected_hym_operator_source_attempt_certificate.json",
        },
        "attempted_source": {
            "required_visible_row_filled": row_filled,
            "Tr_F_visible_squared": packet.get("curvature_rows", {}).get("Tr_F_visible_squared"),
            "selected_by_mtt": packet.get("selected_by_mtt"),
            "selected_visible_bundle_model": packet.get("visible_source_evidence", {}).get(
                "selected_visible_bundle_model"
            ),
            "chern_weil_row_from_source": packet.get("visible_source_evidence", {}).get(
                "chern_weil_row_from_source"
            ),
            "source_certificate": packet.get("visible_source_evidence", {}).get(
                "source_certificate"
            ),
        },
        "validator_result": {
            "exit_code": validator_exit,
            "output_head": validator_output.splitlines()[:20],
        },
        "calculation_results": {
            "source_packet_schema_and_validator_created": True,
            "required_visible_TrF_row_inserted": row_filled,
            "validator_rejects_current_attempt": selected_source_missing,
            "selected_visible_source_constructed": False,
            "visible_green_schwarz_source_verified": False,
        },
        "what_this_closes": {
            "executable_selected_visible_source_gate": True,
            "attempt_packet_with_exact_required_row": row_filled,
            "proof_that_current_certificates_do_not_yet_create_selected_source": selected_source_missing,
        },
        "still_open": {
            "selected_visible_bundle_model_realizing_required_row": True,
            "HYM_or_Route_C_residual_for_visible_source": True,
            "Chern_Weil_derivation_from_selected_source": True,
            "selected_projector_retention_for_visible_zero_modes": True,
            "selected_D_E_dotD_Riesz_Green_files": True,
            "primitive_C1_contractions": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_attempt_source_selected": False,
            "claims_visible_green_schwarz_verified": False,
            "claims_selected_D_E_dotD_constructed": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "The selected visible Green-Schwarz source object now exists as "
                "an executable packet/validator. The exact required TrF row can "
                "be inserted, but current certificates still cannot prove that "
                "row comes from a selected visible HYM/Route-C source."
            ),
            "next_closing_object": (
                "Supply selected visible bundle/HYM or Route-C residual evidence "
                "whose Chern-Weil row equals the derived alpha_1 coefficient."
            ),
        },
    }


def write_outputs(report: dict[str, Any]) -> None:
    write_json(CANDIDATE, report)
    certificate = {
        "certificate": "TimeOrientedM1VisibleGreenSchwarzSourceAttempt",
        "status": report["status"],
        "analysis_script": "scripts/attempt_time_oriented_m1_visible_gs_source.py",
        "candidate_data": "candidate_data/time_oriented_m1_visible_gs_source_attempt.candidate.json",
        "template": report["template"],
        "attempt_packet": report["attempt_packet"],
        "validator": report["validator"],
        "inputs": report["inputs"],
        "attempted_source": report["attempted_source"],
        "validator_result": report["validator_result"],
        "calculation_results": report["calculation_results"],
        "what_this_closes": report["what_this_closes"],
        "still_open": report["still_open"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    write_json(CERTIFICATE, certificate)


def main() -> int:
    report = attempt_report()
    write_outputs(report)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
