"""Attempt to fill the same-source monad/GS/operator fusion packet.

This uses the strongest current artifacts, but keeps all selected-source
claims honest.  The expected result is an OPEN packet: it demonstrates exactly
which fields still need a genuine selected visible SM bundle/operator source.
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

PACKET = CANDIDATES / "same_source_monad_gs_operator_fusion.current_attempt.json"
CANDIDATE = CANDIDATES / "same_source_monad_gs_operator_fusion_attempt.candidate.json"
CERT = CERTS / "same_source_monad_gs_operator_fusion_attempt_certificate.json"

ORDERED_PACKET = CANDIDATES / "visible_rank2_l2_ordered_source.monad_difference_candidate.json"
PROMOTION_PACKET = CERTS / "selected_hym_operator_source_promotion.attempt.json"
HYM_ATTEMPT = CERTS / "selected_hym_operator_source_attempt_certificate.json"
GS_SOURCE_ATTEMPT = CERTS / "time_oriented_m1_visible_gs_source_attempt_certificate.json"
GS_CURVATURE = CERTS / "time_oriented_m1_visible_green_schwarz_curvature_closure_certificate.json"
TIME_GERBE = CERTS / "time_oriented_fixed_gerbe_representative_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def dig(data: dict[str, Any], *keys: str, default: Any = None) -> Any:
    current: Any = data
    for key in keys:
        if not isinstance(current, dict):
            return default
        current = current.get(key)
    return default if current is None else current


def run_validator(path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "validate_same_source_monad_gs_operator_fusion_packet.py"),
            str(path),
        ],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    parsed: dict[str, Any] | None = None
    prefix = "same_source_monad_gs_operator_fusion_report="
    for line in proc.stdout.splitlines():
        if line.startswith(prefix):
            parsed = json.loads(line[len(prefix) :])
            break
    return {
        "exit_code": proc.returncode,
        "stdout": proc.stdout,
        "parsed_report": parsed,
    }


def build_attempt_packet() -> dict[str, Any]:
    time_gerbe = load(TIME_GERBE)
    gs_curvature = load(GS_CURVATURE)
    gs_source = load(GS_SOURCE_ATTEMPT)
    hym = load(HYM_ATTEMPT)

    return {
        "schema": "SameSourceMonadGSOperatorFusionPacket.v1",
        "status": "ATTEMPT_BLOCKED_SELECTED_VISIBLE_OPERATOR_SOURCE_MISSING",
        "source_identity": {
            "source_certificate": "certificates/selected_hym_operator_source_attempt_certificate.json",
            "source_kind": "finite_HYM_Strominger_solve",
            "selected_by_mtt": False,
            "fixture_only": True,
            "no_observed_flavor_inputs": True,
            "uses_execution_ii_benchmarks": False,
            "same_source_for_ordered_L_pic0_GS_and_DE": False,
        },
        "ordered_source": {
            "visible_rank2_l2_ordered_source_packet": str(ORDERED_PACKET.relative_to(ROOT)),
            "source_lane_selector": "conditional_terminal_monad_difference_lane_only",
            "selected_L": [1, -2, 0],
            "selected_L2": [2, -4, 0],
            "standard_lattice_or_equivalent_selected": False,
            "base_factor_order_selected": False,
            "base_swap_broken_by_source": True,
            "pic0_resolution": "OPEN",
            "ordered_source_validator_passes": False,
        },
        "green_schwarz_and_gerbe": {
            "time_oriented_m1_representative_used": dig(
                time_gerbe,
                "calculation_results",
                "time_oriented_torsion_label_m1_fixed",
                default=False,
            )
            is True,
            "antiunitary_q369_retained": dig(
                time_gerbe,
                "calculation_results",
                "antiunitary_conjugate_torsion_label_m2_retained",
                default=False,
            )
            is True,
            "visible_green_schwarz_row_derived_from_same_source": dig(
                gs_source,
                "calculation_results",
                "visible_green_schwarz_source_verified",
                default=False,
            )
            is True,
            "freed_witten_or_cycle_restrictions_verified_if_used": False,
            "projector_retention_verified": dig(
                gs_curvature,
                "calculation_results",
                "projector_retention_verified",
                default=False,
            )
            is True,
        },
        "operator_response": {
            "iwasawa_selected_source_promotion_packet": str(PROMOTION_PACKET.relative_to(ROOT)),
            "route_c_residuals_pass": False,
            "de_action_pass": False,
            "riesz_gap_pass": False,
            "reduced_green_pass": False,
            "dotd_response_pass": False,
            "selected_dotD_source_verified": dig(
                hym,
                "operator_source",
                "selected_dotD_constructed",
                default=False,
            )
            is True,
            "primitive_C1_contractions": False,
        },
        "forbidden_shortcuts": {
            "uses_lifted_flags_as_proof": False,
            "uses_observed_masses_or_mixings": False,
            "uses_benchmark_flavor_entries": False,
            "combines_separate_sources_without_same_source_certificate": False,
            "treats_curvature_only_gs_as_operator_source": False,
        },
    }


def main() -> int:
    packet = build_attempt_packet()
    write(PACKET, packet)
    validation = run_validator(PACKET)
    parsed = validation["parsed_report"] or {}
    open_items = parsed.get("open_items", [])

    report = {
        "calculation": "SameSourceMonadGSOperatorFusionAttempt",
        "status": "SAME_SOURCE_MONAD_GS_OPERATOR_FUSION_ATTEMPT_OPEN_SELECTED_SOURCE_MISSING",
        "attempt_packet": str(PACKET.relative_to(ROOT)),
        "validator": "scripts/validate_same_source_monad_gs_operator_fusion_packet.py",
        "validator_result": {
            "exit_code": validation["exit_code"],
            "parsed_report": parsed,
        },
        "current_best_inputs": {
            "ordered_monad_difference_candidate": str(ORDERED_PACKET.relative_to(ROOT)),
            "selected_hym_operator_source_promotion_attempt": str(PROMOTION_PACKET.relative_to(ROOT)),
            "time_oriented_m1_gerbe": str(TIME_GERBE.relative_to(ROOT)),
            "visible_green_schwarz_curvature": str(GS_CURVATURE.relative_to(ROOT)),
            "visible_green_schwarz_source_attempt": str(GS_SOURCE_ATTEMPT.relative_to(ROOT)),
        },
        "open_item_count": len(open_items),
        "first_open_items": open_items[:20],
        "what_this_closes": {
            "fusion_packet_validator_created": True,
            "current_best_patchwork_attempt_executed": True,
            "open_fields_are_machine_reported": validation["exit_code"] == 2,
            "selected_source_gap_confirmed": True,
        },
        "what_this_does_not_close": {
            "same_source_fusion_packet": False,
            "selected_visible_operator_source": False,
            "selected_D_E_dotD": False,
            "Pic0_selection_or_quotient": False,
            "primitive_C1_contractions": False,
            "full_SM_closure": False,
        },
        "guardrails": {
            "claims_selected_source": False,
            "claims_pic0_resolved": False,
            "claims_D_E_dotD_constructed": False,
            "uses_lifted_flags_as_proof": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "The current best fill attempt is correctly refused.  It has the "
                "right shape, but the same selected source is still missing."
            ),
            "next_action": (
                "Construct Selected_Qa_SU3_Visible_SM_Bundle_Operator_Source_v1 "
                "or equivalent typed Cech/finite HYM data, then refill this packet."
            ),
        },
    }
    write(CANDIDATE, report)
    cert = {
        "certificate": "SameSourceMonadGSOperatorFusionAttempt",
        "status": report["status"],
        "analysis_script": "scripts/attempt_same_source_monad_gs_operator_fusion_packet.py",
        "candidate_data": str(CANDIDATE.relative_to(ROOT)),
        "attempt_packet": str(PACKET.relative_to(ROOT)),
        "validator_result": report["validator_result"],
        "open_item_count": report["open_item_count"],
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
