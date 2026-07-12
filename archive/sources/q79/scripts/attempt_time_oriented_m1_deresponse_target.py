"""Test the time-oriented m=1 de_response target.

The previous step fixed the finite gerbe representative:

    q79/F -> m=1.

This script asks a narrower validator question: if a genuine selected source
were supplied on that fixed representative, does the finite q79/F response
stack have the right shape to pass the de_response validators?

It performs two checks:

1. current honest packet: expected to fail because selected-source flags and
   source proof are absent;
2. temporary lifted-source consistency packet: all finite validators must pass
   after the missing selected-source assertions are supplied in a temp copy.

The lifted packet is not written as proof data and is not promoted to selected
physics.  It is a consistency check for the target gate.
"""

from __future__ import annotations

import copy
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
CERTIFICATES = ROOT / "certificates"
BRANCH_DIR = ROOT / "candidate_data" / "iwasawa_route_c_branch_smoke" / "current_q79_orientation"
OUT = ROOT / "candidate_data" / "time_oriented_m1_deresponse_target.candidate.json"
CERT = CERTIFICATES / "time_oriented_m1_deresponse_target_certificate.json"

FILES = {
    "rhoE_mesh": "rhoE_mesh.candidate.json",
    "rhoE_metric": "rhoE_metric.candidate.json",
    "sector_maps": "sector_maps.candidate.json",
    "route_c_residuals": "route_c_residual.candidate.json",
    "de_action": "de_action.candidate.json",
    "riesz_gap": "riesz_gap.candidate.json",
    "reduced_green": "reduced_green.candidate.json",
    "dotd_response": "dotd_response.candidate.json",
}


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def cert(name: str) -> dict[str, Any]:
    return load_json(CERTIFICATES / name)


def get(data: dict[str, Any], *keys: str, default: Any = None) -> Any:
    value: Any = data
    for key in keys:
        if not isinstance(value, dict) or key not in value:
            return default
        value = value[key]
    return value


def run_validator(script_name: str, path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(SCRIPTS / script_name), str(path)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    stdout = sanitize_temp_paths(proc.stdout)
    return {
        "script": script_name,
        "path": sanitize_temp_paths(str(path)),
        "exit_code": proc.returncode,
        "pass": proc.returncode == 0,
        "stdout_head": stdout.strip().splitlines()[:30],
    }


def sanitize_temp_paths(value: str) -> str:
    """Stabilize temp-directory names embedded in conditional validator output."""
    value = re.sub(
        r"[A-Za-z]:\\\\Users\\\\[^\\\\]+\\\\AppData\\\\Local\\\\Temp\\\\tmp[^\\\\\"]+",
        "<TEMP>",
        value,
    )
    return re.sub(
        r"[A-Za-z]:\\Users\\[^\\]+\\AppData\\Local\\Temp\\tmp[^\\\"\s]+",
        "<TEMP>",
        value,
    )


def lift_selected_flags(value: Any) -> Any:
    lifted = copy.deepcopy(value)

    def walk(item: Any) -> None:
        if isinstance(item, dict):
            for key in list(item):
                if key in {
                    "selected_source_verified",
                    "selected_dotD_source_verified",
                    "alpha1_driver_verified",
                    "selected_by_mtt",
                }:
                    item[key] = True
                walk(item[key])
        elif isinstance(item, list):
            for child in item:
                walk(child)

    walk(lifted)
    return lifted


def write_lifted_files(temp_dir: Path) -> dict[str, Path]:
    paths: dict[str, Path] = {}
    for key, filename in FILES.items():
        data = load_json(BRANCH_DIR / filename)
        lifted = lift_selected_flags(data)
        if key == "route_c_residuals":
            lifted["status"] = "CONDITIONAL_SELECTED_SOURCE_CONSISTENCY_CHECK"
            lifted["guardrails"] = {
                **lifted.get("guardrails", {}),
                "conditional_lift_only": True,
                "claims_selected_source_in_repo": False,
            }
        path = temp_dir / filename
        path.write_text(json.dumps(lifted, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        paths[key] = path
    return paths


def write_lifted_promotion_packet(temp_dir: Path, paths: dict[str, Path]) -> Path:
    packet = {
        "schema": "IwasawaSelectedSourcePromotionPacket.v1",
        "status": "CONDITIONAL_M1_DERESPONSE_TARGET_CHECK",
        "target_level": "de_response",
        "source_kind": "finite_HYM_Strominger_solve",
        "selected_source_verified": True,
        "no_observed_flavor_inputs": True,
        "uses_execution_ii_benchmarks": False,
        "uses_observed_masses_or_mixings": False,
        "uses_diagnostic_h1_three_as_selected": False,
        "uses_pure_gauge_prototype_as_selected": False,
        "response_gate": {
            "minimum_source_norm": 1e-12,
            "minimum_response_norm": 1e-12,
        },
        "paths": {key: str(path) for key, path in paths.items()},
        "guardrails": {
            "conditional_lift_only": True,
            "not_a_selected_source_certificate": True,
        },
    }
    path = temp_dir / "selected_source_promotion.conditional.json"
    path.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return path


def write_lifted_hym_packet(temp_dir: Path, paths: dict[str, Path], promotion: Path) -> Path:
    packet = {
        "schema": "SelectedHYMOperatorSource.v1",
        "status": "CONDITIONAL_M1_DERESPONSE_TARGET_CHECK",
        "source": {
            "source_kind": "finite_HYM_Strominger_solve",
            "selected_by_mtt": True,
            "fixture_only": False,
            "source_certificate": "conditional_selected_source_assertions_not_repo_proof",
            "uses_observed_flavor_inputs": False,
            "uses_benchmark_flavor_inputs": False,
        },
        "background": {
            "certificate_path": "certificates/z7_fuyau_mukai_charge_sector_certificate.json",
            "fuyau_strominger_charge_sector_closed": True,
            "green_schwarz_bianchi_identity_verified": True,
            "strominger_selection_applies": True,
            "charge_sector_only": False,
            "visible_sm_bundle_model_selected": True,
            "matter_operator_source_constructed": True,
        },
        "branch": {
            "q": 79,
            "orientation": "F",
            "retarded_q79_branch_selected": True,
            "antiunitary_conjugate_retained": True,
            "branch_packet_reference": str(paths["route_c_residuals"]),
        },
        "operator_source": {
            "route_c_residual_packet": str(paths["route_c_residuals"]),
            "selected_source_promotion_packet": str(promotion),
            "same_branch_dotd": True,
            "selected_D_E_constructed": True,
            "selected_dotD_constructed": True,
            "selected_riesz_green_constructed": True,
            "projector_retention_selected": True,
        },
        "guardrails": {
            "conditional_lift_only": True,
            "not_a_selected_source_certificate": True,
        },
    }
    path = temp_dir / "selected_hym_operator_source.conditional.json"
    path.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return path


def analyze() -> dict[str, Any]:
    fixed = cert("time_oriented_fixed_gerbe_representative_certificate.json")
    visible = cert("visible_operator_source_blocker_resolution_certificate.json")
    source_ansatz = cert("visible_rhoE_source_ansatz_search_certificate.json")

    fixed_m1 = (
        get(fixed, "calculation_results", "time_oriented_finite_representative_closed") is True
        and get(fixed, "branch_representatives", "time_oriented_q79", "torsion_label_m") == 1
    )
    current_promotion = run_validator(
        "validate_iwasawa_selected_source_promotion.py",
        CERTIFICATES / "selected_hym_operator_source_promotion.attempt.json",
    )
    current_hym = run_validator(
        "validate_selected_hym_operator_source.py",
        CERTIFICATES / "selected_hym_operator_source.attempt.json",
    )

    with tempfile.TemporaryDirectory() as tmp:
        temp_dir = Path(tmp)
        lifted_paths = write_lifted_files(temp_dir)
        lifted_promotion_path = write_lifted_promotion_packet(temp_dir, lifted_paths)
        lifted_hym_path = write_lifted_hym_packet(temp_dir, lifted_paths, lifted_promotion_path)
        lifted_promotion = run_validator(
            "validate_iwasawa_selected_source_promotion.py",
            lifted_promotion_path,
        )
        lifted_hym = run_validator("validate_selected_hym_operator_source.py", lifted_hym_path)

    conditional_stack_coherent = (
        fixed_m1
        and current_promotion["pass"] is False
        and current_hym["pass"] is False
        and lifted_promotion["pass"] is True
        and lifted_hym["pass"] is True
    )

    status = (
        "TIME_ORIENTED_M1_DERESPONSE_TARGET_COHERENT_SELECTED_SOURCE_OPEN"
        if conditional_stack_coherent
        else "TIME_ORIENTED_M1_DERESPONSE_TARGET_NOT_COHERENT"
    )
    return {
        "candidate": "TimeOrientedM1DeResponseTarget",
        "status": status,
        "generated_by": "scripts/attempt_time_oriented_m1_deresponse_target.py",
        "fixed_representative_input": {
            "q": 79,
            "orientation": "F",
            "torsion_label_m": 1,
            "fixed_by_certificate": "time_oriented_fixed_gerbe_representative_certificate.json",
            "fixed_representative_closed": fixed_m1,
        },
        "current_honest_packets": {
            "selected_source_promotion_attempt": current_promotion,
            "selected_hym_operator_source_attempt": current_hym,
            "expected_to_fail_without_selected_source": True,
        },
        "conditional_lifted_consistency_check": {
            "purpose": "prove finite q79/F m=1 de_response stack is validator-coherent if a genuine selected source supplies the missing assertions",
            "promotion_gate": lifted_promotion,
            "hym_operator_source_gate": lifted_hym,
            "lifted_flags_are_not_written_as_proof_data": True,
        },
        "calculation_results": {
            "m1_representative_fixed": fixed_m1,
            "honest_current_promotion_fails": current_promotion["pass"] is False,
            "honest_current_hym_source_fails": current_hym["pass"] is False,
            "conditional_lifted_promotion_passes": lifted_promotion["pass"] is True,
            "conditional_lifted_hym_gate_passes": lifted_hym["pass"] is True,
            "finite_deresponse_stack_coherent": conditional_stack_coherent,
            "selected_source_still_absent": get(
                visible,
                "calculation_results",
                "blocker_resolved_by_existing_data",
            )
            is False,
            "ordinary_rhoE_routes_retired": get(
                source_ansatz,
                "calculation_results",
                "ordinary_constant_carriers_blocked",
            )
            is True,
        },
        "what_this_closes": {
            "de_response_is_the_right_next_gate_on_m1": conditional_stack_coherent,
            "finite_validator_stack_has_no_additional_algebraic_blocker": conditional_stack_coherent,
            "remaining_blocker_is_source_origin_not_matrix_shape": conditional_stack_coherent,
        },
        "still_open": {
            "actual_selected_visible_SM_bundle_or_twisted_source": True,
            "full_Deligne_Cech_or_B_field_period_table": True,
            "Freed_Witten_and_projector_retention": True,
            "repo_level_selected_D_E_dotD_data": True,
            "selected_C1_primitive_contractions": True,
            "Yukawa_magnitudes_and_CKM_angles": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_selected_source_constructed": False,
            "claims_lifted_flags_are_physical_proof": False,
            "claims_selected_D_E_constructed_in_repo": False,
            "claims_full_twisted_source_promotion": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "On the fixed q79/F, m=1 representative, the finite de_response "
                "stack is coherent: the validators pass in a temporary lifted "
                "selected-source consistency check. The repository still lacks "
                "the genuine selected source that would make those assertions true."
            )
            if conditional_stack_coherent
            else "The m=1 de_response target did not pass the consistency check.",
            "next_closing_object": (
                "Supply the actual selected source origin for the m=1 de_response "
                "packet: selected visible bundle/twisted gerbe data with projector "
                "retention, then write repo-level D_E/dotD/Riesz/Green files with "
                "selected-source flags justified by that source."
            ),
        },
    }


def write_outputs(report: dict[str, Any]) -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    certificate = {
        "certificate": "TimeOrientedM1DeResponseTarget",
        "status": report["status"],
        "candidate_data": str(OUT.relative_to(ROOT)).replace("\\", "/"),
        "analysis_script": "scripts/attempt_time_oriented_m1_deresponse_target.py",
        "fixed_representative_input": report["fixed_representative_input"],
        "calculation_results": report["calculation_results"],
        "what_this_closes": report["what_this_closes"],
        "still_open": report["still_open"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    CERT.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    report = analyze()
    write_outputs(report)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
