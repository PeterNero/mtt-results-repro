"""Attempt to fill the selected HYM/Strominger operator-source packet.

The attempt uses exactly the current strongest data:

  * closed Fu-Yau/Strominger charge-sector certificate;
  * current q79/F Route C branch-smoke finite files.

The expected honest outcome is still blocked: the charge sector is selected,
but it does not yet construct the visible matter bundle/operator source.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
BRANCH_ROOT = ROOT / "candidate_data" / "iwasawa_route_c_branch_smoke" / "current_q79_orientation"
PROMOTION_PACKET = ROOT / "certificates" / "selected_hym_operator_source_promotion.attempt.json"
HYM_PACKET = ROOT / "certificates" / "selected_hym_operator_source.attempt.json"
CANDIDATE_PATH = ROOT / "candidate_data" / "selected_hym_operator_source_attempt.candidate.json"
CERTIFICATE_PATH = ROOT / "certificates" / "selected_hym_operator_source_attempt_certificate.json"
VALIDATOR = ROOT / "scripts" / "validate_selected_hym_operator_source.py"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


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
        "pass": proc.returncode == 0,
    }


def parse_report(stdout: str) -> dict[str, Any]:
    prefix = "hym_operator_source_validation_report="
    for line in stdout.splitlines():
        if line.startswith(prefix):
            return json.loads(line[len(prefix) :])
    return {}


def make_promotion_packet() -> dict[str, Any]:
    return {
        "schema": "IwasawaSelectedSourcePromotionPacket.v1",
        "status": "ATTEMPT_BLOCKED_SELECTED_SOURCE",
        "target_level": "de_response",
        "source_kind": "finite_HYM_Strominger_solve",
        "selected_source_verified": False,
        "no_observed_flavor_inputs": True,
        "uses_execution_ii_benchmarks": False,
        "uses_observed_masses_or_mixings": False,
        "uses_diagnostic_h1_three_as_selected": False,
        "uses_pure_gauge_prototype_as_selected": False,
        "paths": {
            "route_c_residuals": rel(BRANCH_ROOT / "route_c_residual.candidate.json"),
            "rhoE_mesh": rel(BRANCH_ROOT / "rhoE_mesh.candidate.json"),
            "rhoE_metric": rel(BRANCH_ROOT / "rhoE_metric.candidate.json"),
            "sector_maps": rel(BRANCH_ROOT / "sector_maps.candidate.json"),
            "de_action": rel(BRANCH_ROOT / "de_action.candidate.json"),
            "riesz_gap": rel(BRANCH_ROOT / "riesz_gap.candidate.json"),
            "reduced_green": rel(BRANCH_ROOT / "reduced_green.candidate.json"),
            "dotd_response": rel(BRANCH_ROOT / "dotd_response.candidate.json"),
        },
        "response_gate": {
            "minimum_source_norm": 1e-12,
            "minimum_response_norm": 1e-12,
        },
    }


def make_hym_packet(z7: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema": "SelectedHYMOperatorSource.v1",
        "status": "CURRENT_FUYAU_ROUTE_C_ATTEMPT_BLOCKED_OPERATOR_SOURCE_MISSING",
        "source": {
            "source_kind": "finite_HYM_Strominger_solve",
            "selected_by_mtt": False,
            "fixture_only": True,
            "source_certificate": "certificates/z7_fuyau_mukai_charge_sector_certificate.json",
            "uses_observed_flavor_inputs": False,
            "uses_benchmark_flavor_inputs": False,
        },
        "background": {
            "certificate_path": "certificates/z7_fuyau_mukai_charge_sector_certificate.json",
            "fuyau_strominger_charge_sector_closed": z7.get("status") == "CLOSED_CHARGE_SECTOR",
            "green_schwarz_bianchi_identity_verified": z7.get("geometry", {}).get(
                "green_schwarz_bianchi_identity_verified"
            )
            is True,
            "strominger_selection_applies": z7.get("selection", {}).get(
                "strominger_selection_applies"
            )
            is True,
            "charge_sector_only": True,
            "visible_sm_bundle_model_selected": False,
            "matter_operator_source_constructed": False,
        },
        "branch": {
            "q": 79,
            "orientation": "F",
            "retarded_q79_branch_selected": True,
            "antiunitary_conjugate_retained": True,
            "branch_packet_reference": rel(BRANCH_ROOT / "route_c_residual.candidate.json"),
        },
        "operator_source": {
            "route_c_residual_packet": rel(BRANCH_ROOT / "route_c_residual.candidate.json"),
            "selected_source_promotion_packet": rel(PROMOTION_PACKET),
            "same_branch_dotd": True,
            "selected_D_E_constructed": False,
            "selected_dotD_constructed": False,
            "selected_riesz_green_constructed": False,
            "projector_retention_selected": False,
        },
        "guardrails": {
            "claims_selected_D_E_constructed": False,
            "claims_ordered_su5_packet_selected": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
    }


def main() -> int:
    z7 = load_json(ROOT / "certificates" / "z7_fuyau_mukai_charge_sector_certificate.json")
    route_c = load_json(ROOT / "certificates" / "iwasawa_route_c_branch_smoke_attempt_certificate.json")
    two_path = load_json(ROOT / "certificates" / "selected_matter_source_two_path_exploration_certificate.json")

    PROMOTION_PACKET.write_text(
        json.dumps(make_promotion_packet(), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    HYM_PACKET.write_text(
        json.dumps(make_hym_packet(z7), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    validation = run_validator(HYM_PACKET)
    report = parse_report(validation["stdout"])

    route_c_honest = (
        route_c.get("branches", {})
        .get("current_q79_orientation", {})
        .get("validators", {})
        .get("honest_unselected", {})
    )
    candidate = {
        "calculation": "SelectedHYMOperatorSourceAttempt",
        "generated_by": "scripts/attempt_selected_hym_operator_source.py",
        "attempt_packet": rel(HYM_PACKET),
        "promotion_packet": rel(PROMOTION_PACKET),
        "calculation_results": {
            "fuyau_strominger_charge_sector_closed": z7.get("status") == "CLOSED_CHARGE_SECTOR",
            "strominger_selection_applies": z7.get("selection", {}).get(
                "strominger_selection_applies"
            )
            is True,
            "route_c_q79_branch_available": bool(
                route_c.get("branches", {}).get("current_q79_orientation", {}).get("branch_packet")
            ),
            "route_c_honest_mesh_metric_sector_pass": all(
                route_c_honest.get(key, {}).get("pass") is True
                for key in ("rhoE_mesh", "rhoE_metric", "sector_maps")
            ),
            "route_c_honest_operator_pipeline_pass": all(
                route_c_honest.get(key, {}).get("pass") is True
                for key in ("route_c_residual", "de_action", "riesz_gap", "reduced_green", "dotd_response")
            ),
            "selected_hym_operator_source_verified": validation["pass"],
            "validator_exit_code": validation["exit_code"],
            "two_path_hybrid_recommended": two_path.get("recommended_strategy")
            == "HYBRID_SELECTED_HYM_ORIGIN_THEN_GALERKIN_ZERO_MODES",
        },
        "validation": {
            "exit_code": validation["exit_code"],
            "report": report,
            "stdout": validation["stdout"],
        },
        "what_this_closes": {
            "path_A_first_fill_attempt_executed": True,
            "closed_charge_sector_not_enough_for_operator_source": True,
            "route_c_honest_operator_blocker_confirmed": True,
            "hym_operator_source_gate_instantiated": True,
        },
        "still_open": {
            "selected_visible_sm_bundle_model": True,
            "selected_route_c_residual_solve": True,
            "selected_D_E_dotD_same_branch": True,
            "selected_Riesz_Green_projector_retention": True,
            "spectral_galerkin_zero_modes": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_selected_D_E_constructed": False,
            "claims_ordered_su5_packet_selected": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "attempted_path_A_fill": True,
            "selected_hym_operator_source_verified": validation["pass"],
            "current_status": "BLOCKED_SELECTED_VISIBLE_OPERATOR_SOURCE_MISSING",
            "next_required_input": (
                "a selected visible SM bundle/operator source whose Route C residual, "
                "D_E, Riesz/Green, and dotD validators pass honestly"
            ),
        },
    }

    CANDIDATE_PATH.write_text(
        json.dumps(candidate, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    certificate = {
        "certificate": "SelectedHYMOperatorSourceAttemptCertificate",
        "status": "SELECTED_HYM_OPERATOR_SOURCE_ATTEMPT_BLOCKED_OPERATOR_SOURCE_MISSING",
        "analysis_script": "scripts/attempt_selected_hym_operator_source.py",
        "candidate_data": rel(CANDIDATE_PATH),
        "attempt_packet": rel(HYM_PACKET),
        "promotion_packet": rel(PROMOTION_PACKET),
        "validator_script": "scripts/validate_selected_hym_operator_source.py",
        "calculation_results": candidate["calculation_results"],
        "what_this_closes": candidate["what_this_closes"],
        "still_open": candidate["still_open"],
        "guardrails": candidate["guardrails"],
        "verdict": candidate["verdict"],
    }
    CERTIFICATE_PATH.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(candidate, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
