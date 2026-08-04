"""Attempt to fill the orientation-carrying D_E/dotD source packet.

The expected result is OPEN.  The current branch-smoke data contain coherent
finite q79/q369 operator candidates, but the selected-source and alpha1-driver
flags are still false.  This script records that status in an executable packet
instead of promoting the finite candidates as proof data.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CANDIDATES = ROOT / "candidate_data"
CERTS = ROOT / "certificates"

PACKET = CANDIDATES / "selected_qa_su3_orientation_dedotd_source.current_attempt.json"
CANDIDATE = CANDIDATES / "selected_qa_su3_orientation_dedotd_source_attempt.candidate.json"
CERT = CERTS / "selected_qa_su3_orientation_dedotd_source_attempt_certificate.json"

ORIENTATION = CERTS / "iwasawa_orientation_de_dotd_bridge_certificate.json"
DERESPONSE = CERTS / "time_oriented_m1_deresponse_target_certificate.json"
S3_PACKET = CERTS / "visible_twisted_s3_class_restriction_packet.selected.json"
S3_CLOSURE = CERTS / "visible_twisted_s3_class_restriction_closure_certificate.json"
PROMOTION = CERTS / "selected_hym_operator_source_promotion.attempt.json"

Q79_DIR = CANDIDATES / "iwasawa_route_c_branch_smoke" / "current_q79_orientation"
Q369_DIR = CANDIDATES / "iwasawa_route_c_branch_smoke" / "conjugate_q369_orientation"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def run_validator(script: str, path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / script), str(path)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return {
        "exit_code": proc.returncode,
        "output_head": proc.stdout.strip().splitlines()[:16],
    }


def run_packet_validator(path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "validate_selected_qa_su3_orientation_dedotd_source_packet.py"),
            str(path),
        ],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    prefix = "selected_qa_su3_orientation_dedotd_source_report="
    parsed: dict[str, Any] | None = None
    for line in proc.stdout.splitlines():
        if line.startswith(prefix):
            parsed = json.loads(line[len(prefix) :])
            break
    return {
        "exit_code": proc.returncode,
        "stdout": proc.stdout,
        "parsed_report": parsed,
    }


def branch_paths(base: Path) -> dict[str, str]:
    return {
        "de_action": str((base / "de_action.candidate.json").relative_to(ROOT)),
        "reduced_green": str((base / "reduced_green.candidate.json").relative_to(ROOT)),
        "dotd_response": str((base / "dotd_response.candidate.json").relative_to(ROOT)),
        "route_c_residuals": str((base / "route_c_residual.candidate.json").relative_to(ROOT)),
    }


def branch_validator_summary(base: Path) -> dict[str, Any]:
    paths = branch_paths(base)
    return {
        "de_action": run_validator("validate_iwasawa_de_action.py", ROOT / paths["de_action"]),
        "reduced_green": run_validator(
            "validate_iwasawa_reduced_green.py", ROOT / paths["reduced_green"]
        ),
        "dotd_response": run_validator(
            "validate_iwasawa_dotd_response.py", ROOT / paths["dotd_response"]
        ),
    }


def only_source_flags_block(summary: dict[str, Any]) -> bool:
    required = {
        "de_action": "selected_source_verified is not true",
        "reduced_green": "selected_source_verified is not true",
        "dotd_response": "selected_dotD_source_verified is not true",
    }
    for key, needle in required.items():
        output = "\n".join(summary[key]["output_head"])
        if summary[key]["exit_code"] != 1 or needle not in output:
            return False
    return True


def build_packet() -> dict[str, Any]:
    orientation = load(ORIENTATION)
    deresponse = load(DERESPONSE)
    s3_closure = load(S3_CLOSURE)
    promotion = load(PROMOTION)
    q79_dotd = load(Q79_DIR / "dotd_response.candidate.json")

    branch_packet = q79_dotd["branch_packet"]
    paths = branch_paths(Q79_DIR)

    return {
        "schema": "SelectedQaSU3OrientationCarryingDEDotDSource.v1",
        "status": "ATTEMPT_BLOCKED_SELECTED_SOURCE_FLAGS_OPEN",
        "source_origin": {
            "source_certificate": str(PROMOTION.relative_to(ROOT)),
            "source_kind": "selected_route_c_hym_source",
            "candidate_source_kind": promotion["source_kind"],
            "selected_by_mtt": False,
            "visible_bundle_or_twisted_gerbe_source": False,
            "pic0_selected_or_quotiented": False,
            "freed_witten_and_projector_retention": False,
        },
        "branch_selection": {
            "allowed_torsion_labels": [1, 2],
            "selected_torsion_label_m": branch_packet["torsion_label_m"],
            "global_cp_label": branch_packet["global_cp_label"],
            "must_bind_m_to_global_cp_label": {"m=1": 79, "m=2": 369},
            "selection_justified_by_source": False,
            "branch_status": "conditional_fixed_representative_not_unique_source_selection",
            "do_not_use_observed_cp_sign": True,
        },
        "operator_data": {
            "selected_D_E_action": paths["de_action"],
            "selected_reduced_green": paths["reduced_green"],
            "selected_dotD_alpha1": paths["dotd_response"],
            "sector_D_E_Riesz_Green_dotD_packets": paths,
            "same_branch_derivative_verified": False,
        },
        "support_evidence": {
            "orientation_bridge_status": orientation["status"],
            "m1_deresponse_stack_coherent_conditionally": deresponse["calculation_results"][
                "finite_deresponse_stack_coherent"
            ],
            "finite_s3_class_restriction_passes": s3_closure["calculation_results"][
                "selected_S3_class_restriction_packet_constructed"
            ],
            "s3_class_restriction_packet": str(S3_PACKET.relative_to(ROOT)),
            "q79_branch_smoke_paths": paths,
            "q369_branch_smoke_paths": branch_paths(Q369_DIR),
        },
        "guardrails": {
            "uses_observed_cp_sign": False,
            "uses_observed_masses_or_mixings": False,
            "uses_benchmark_flavor_entries": False,
            "uses_lifted_selected_flags_as_proof": False,
            "claims_full_sm_closure": False,
        },
    }


def main() -> int:
    q79_summary = branch_validator_summary(Q79_DIR)
    q369_summary = branch_validator_summary(Q369_DIR)
    packet = build_packet()
    write(PACKET, packet)
    validation = run_packet_validator(PACKET)
    parsed = validation["parsed_report"] or {}

    report = {
        "calculation": "SelectedQaSU3OrientationDEDotDSourcePacketAttempt",
        "status": "SELECTED_QA_SU3_ORIENTATION_DEDOTD_SOURCE_ATTEMPT_OPEN_SOURCE_FLAGS",
        "attempt_packet": str(PACKET.relative_to(ROOT)),
        "validator": "scripts/validate_selected_qa_su3_orientation_dedotd_source_packet.py",
        "validator_result": {
            "exit_code": validation["exit_code"],
            "parsed_report": parsed,
        },
        "branch_validator_summary": {
            "current_q79_orientation": q79_summary,
            "conjugate_q369_orientation": q369_summary,
        },
        "calculation_results": {
            "both_branch_packets_exist": all((Q79_DIR / name).exists() and (Q369_DIR / name).exists() for name in [
                "de_action.candidate.json",
                "reduced_green.candidate.json",
                "dotd_response.candidate.json",
            ]),
            "q79_finite_equations_blocked_only_by_source_flags": only_source_flags_block(q79_summary),
            "q369_finite_equations_blocked_only_by_source_flags": only_source_flags_block(q369_summary),
            "orientation_packet_validator_returns_open": validation["exit_code"] == 2,
            "selected_source_origin_constructed": False,
            "unique_m_label_selected_by_source": False,
        },
        "first_open_items": parsed.get("open_items", [])[:24],
        "subvalidator_exit_codes": {
            key: value.get("exit_code")
            for key, value in parsed.get("subvalidators", {}).items()
        },
        "what_this_closes": {
            "orientation_dedotd_packet_validator_created": True,
            "current_q79_branch_attempt_executed": True,
            "conjugate_q369_branch_checked_in_parallel": True,
            "finite_branch_data_reaches_validator_layer": True,
            "source_flags_identified_as_blocker": True,
        },
        "what_this_does_not_close": {
            "selected_source_origin": False,
            "unique_m1_vs_m2_selection": False,
            "selected_D_E_or_dotD_source_flags": False,
            "primitive_C1_contractions": False,
            "full_SM_closure": False,
        },
        "guardrails": {
            "claims_selected_source_origin": False,
            "claims_unique_m_label_now": False,
            "claims_selected_D_E_or_dotD": False,
            "uses_observed_cp_sign_or_masses": False,
            "uses_benchmark_flavor_entries": False,
            "claims_full_sm_closure": False,
        },
        "verdict": {
            "honest_answer": (
                "The q79 and q369 finite branch-smoke packets reach the D_E, "
                "Green, and dotD validator layers, but both are rejected at the "
                "same source-selection flags.  The blocker is no longer matrix "
                "shape; it is the selected source origin and same-branch alpha1 "
                "driver proof."
            ),
            "hard_next_step": (
                "Supply a genuine selected visible bundle/twisted-gerbe/Route-C "
                "source certificate that turns the source flags on for exactly "
                "one branch, or prove the two branch packets are antiunitarily "
                "equivalent until a retarded boundary condition selects one."
            ),
        },
    }
    write(CANDIDATE, report)
    cert = {
        "certificate": "SelectedQaSU3OrientationDEDotDSourcePacketAttempt",
        "status": report["status"],
        "analysis_script": "scripts/attempt_selected_qa_su3_orientation_dedotd_source_packet.py",
        "candidate_data": str(CANDIDATE.relative_to(ROOT)),
        "attempt_packet": str(PACKET.relative_to(ROOT)),
        "validator_result": report["validator_result"],
        "calculation_results": report["calculation_results"],
        "subvalidator_exit_codes": report["subvalidator_exit_codes"],
        "first_open_items": report["first_open_items"],
        "what_this_closes": report["what_this_closes"],
        "what_this_does_not_close": report["what_this_does_not_close"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    write(CERT, cert)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if validation["exit_code"] == 2 else 1


if __name__ == "__main__":
    raise SystemExit(main())
