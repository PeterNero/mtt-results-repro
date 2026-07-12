"""Attempt to fill the selected Qa/SU3 same-source V_alpha/S3 packet.

The expected result is OPEN: current data close the S3 class/restriction side
and the V_alpha target arithmetic, but not the same-source binding, Pic0 rule,
or selected operator execution data.
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

PACKET = CANDIDATES / "selected_qa_su3_same_source_valpha_s3_operator_packet.current_attempt.json"
CANDIDATE = CANDIDATES / "selected_qa_su3_same_source_valpha_s3_operator_packet_attempt.candidate.json"
CERT = CERTS / "selected_qa_su3_same_source_valpha_s3_operator_packet_attempt_certificate.json"

VALPHA = CERTS / "visible_valpha_chern_bianchi_source_packet_candidates_certificate.json"
S3_CLOSURE = CERTS / "visible_twisted_s3_class_restriction_closure_certificate.json"
S3_PACKET = CERTS / "visible_twisted_s3_class_restriction_packet.selected.json"
AFTER_S3 = CERTS / "visible_operator_source_after_s3_closure_certificate.json"
GS_CURVATURE = CERTS / "time_oriented_m1_visible_green_schwarz_curvature_closure_certificate.json"
GS_SOURCE_ATTEMPT = CERTS / "time_oriented_m1_visible_gs_source_attempt_certificate.json"
GS_SOURCE_PACKET = CERTS / "time_oriented_m1_visible_gs_source.attempt.json"
ORDERED_SOURCE = CANDIDATES / "visible_rank2_l2_ordered_source.monad_difference_candidate.json"
PROMOTION_PACKET = CERTS / "selected_hym_operator_source_promotion.attempt.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def run_validator(path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "validate_selected_qa_su3_same_source_valpha_s3_operator_packet.py"),
            str(path),
        ],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    prefix = "selected_qa_su3_same_source_valpha_s3_report="
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


def build_packet() -> dict[str, Any]:
    valpha = load(VALPHA)
    s3 = load(S3_CLOSURE)
    after_s3 = load(AFTER_S3)
    gs_curvature = load(GS_CURVATURE)
    gs_source = load(GS_SOURCE_ATTEMPT)

    primary = valpha["best_current_route"]
    rank2_candidate = valpha["candidate_ranking"][0]
    target = rank2_candidate["topological_target"]

    return {
        "schema": "SelectedQaSU3SameSourceVAlphaS3OperatorPacket.v1",
        "status": "ATTEMPT_BLOCKED_SAME_SOURCE_VALPHA_S3_BINDING_OPEN",
        "source_identity": {
            "source_certificate": None,
            "source_kind": "rank2_valpha_terminal_monad_plus_selected_s3_visible_support",
            "selected_by_mtt": False,
            "same_source_valpha_s3_operator": False,
            "fixture_only": True,
            "no_observed_flavor_inputs": True,
        },
        "source_skeleton": {
            "rank2_valpha_candidate_id": primary["candidate_id"],
            "rank2_valpha_model_selected": valpha["calculation_results"][
                "selected_visible_valpha_source_constructed"
            ],
            "ordered_source_packet": str(ORDERED_SOURCE.relative_to(ROOT)),
            "selected_L": target["l_vector_abc"],
            "selected_L2": target["c1_L_squared_vector_abc"],
            "c2_valpha": target["c2_V_alpha"],
            "terminal_monad_difference_L3_minus_K2_selector_closed": False,
            "nonzero_ext_class_selected": valpha["calculation_results"][
                "selected_nonzero_ext_class_constructed"
            ],
            "non_split_stability_proved": valpha["calculation_results"]["stability_proved"],
            "pic0_resolution": "OPEN",
            "ordered_source_validator_passes": False,
        },
        "same_source_merge": {
            "s3_class_restriction_packet": str(S3_PACKET.relative_to(ROOT)),
            "selected_s3_green_schwarz_visible_support": s3["calculation_results"][
                "selected_S3_class_restriction_packet_constructed"
            ],
            "same_source_link_valpha_to_s3_proved": False,
            "visible_green_schwarz_source_packet": str(GS_SOURCE_PACKET.relative_to(ROOT)),
            "chern_weil_row_derived_from_same_source": gs_source["attempted_source"][
                "chern_weil_row_from_source"
            ],
            "visible_gs_source_validator_passes": gs_source["calculation_results"][
                "visible_green_schwarz_source_verified"
            ],
            "curvature_level_gs_packet_closed": gs_curvature["calculation_results"][
                "visible_green_schwarz_curvature_verified"
            ],
            "block_projector_retention_closed": s3["calculation_results"][
                "block_sector_projector_retention_closed"
            ],
            "coherent_spectral_zero_mode_projectors_closed": not after_s3["still_open_cut_set"][
                "coherent_spectral_zero_mode_projectors"
            ],
        },
        "operator_execution": {
            "selected_source_promotion_packet": str(PROMOTION_PACKET.relative_to(ROOT)),
            "typed_transition_or_rhoE_data_emitted": False,
            "hym_strominger_or_routec_residual_pass": False,
            "sector_D_E_packets_pass": False,
            "riesz_green_packets_pass": False,
            "dotD_packets_pass": False,
            "selected_source_promotion_validator_passes": False,
            "primitive_C1_or_Yukawa_overlap_contractions": False,
        },
        "forbidden_shortcuts": {
            "splices_valpha_and_s3_without_same_source_link": False,
            "promotes_inserted_gs_row_to_chern_weil_derivation": False,
            "uses_routec_smoke_as_selected_operator_data": False,
            "uses_lifted_flags_as_proof": False,
            "uses_observed_masses_or_mixings": False,
            "uses_benchmark_flavor_entries": False,
        },
    }


def main() -> int:
    packet = build_packet()
    write(PACKET, packet)
    validation = run_validator(PACKET)
    parsed = validation["parsed_report"] or {}
    open_items = parsed.get("open_items", [])
    subvalidators = parsed.get("subvalidators", {})

    report = {
        "calculation": "SelectedQaSU3SameSourceVAlphaS3OperatorPacketAttempt",
        "status": "SELECTED_QA_SU3_SAME_SOURCE_VALPHA_S3_OPERATOR_PACKET_ATTEMPT_OPEN",
        "attempt_packet": str(PACKET.relative_to(ROOT)),
        "validator": "scripts/validate_selected_qa_su3_same_source_valpha_s3_operator_packet.py",
        "validator_result": {
            "exit_code": validation["exit_code"],
            "parsed_report": parsed,
        },
        "current_best_inputs": {
            "valpha_candidate_hierarchy": str(VALPHA.relative_to(ROOT)),
            "s3_class_restriction_closure": str(S3_CLOSURE.relative_to(ROOT)),
            "visible_operator_after_s3": str(AFTER_S3.relative_to(ROOT)),
            "gs_curvature_closure": str(GS_CURVATURE.relative_to(ROOT)),
            "gs_source_attempt": str(GS_SOURCE_ATTEMPT.relative_to(ROOT)),
            "ordered_source_packet": str(ORDERED_SOURCE.relative_to(ROOT)),
            "selected_source_promotion_packet": str(PROMOTION_PACKET.relative_to(ROOT)),
        },
        "open_item_count": len(open_items),
        "first_open_items": open_items[:24],
        "subvalidator_exit_codes": {
            key: value.get("exit_code") for key, value in subvalidators.items()
        },
        "what_this_closes": {
            "valpha_s3_packet_validator_created": True,
            "current_best_attempt_executed": True,
            "closed_s3_support_consumed": subvalidators.get("s3_class_restriction", {}).get("exit_code") == 0,
            "open_fields_are_machine_reported": validation["exit_code"] == 2,
        },
        "what_this_does_not_close": {
            "same_source_valpha_s3_binding": False,
            "selected_visible_valpha_source": False,
            "Pic0_selection_or_quotient": False,
            "selected_D_E_dotD_Riesz_Green": False,
            "primitive_C1_contractions": False,
            "full_SM_closure": False,
        },
        "guardrails": {
            "claims_same_source_binding": False,
            "claims_selected_visible_valpha_source": False,
            "claims_chern_weil_derivation_from_same_source": False,
            "claims_selected_operator_execution": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "The current best packet is structurally aligned and consumes the "
                "closed S3 class/restriction data, but it is correctly refused "
                "because V_alpha selection, Pic0, same-source link, and operator "
                "execution are still open."
            ),
            "hard_next_step": (
                "Prove a same-source or physical-quotient map from the selected "
                "S3/Green-Schwarz support to the rank-two V_alpha terminal-monad "
                "source, then refill the packet."
            ),
        },
    }
    write(CANDIDATE, report)
    cert = {
        "certificate": "SelectedQaSU3SameSourceVAlphaS3OperatorPacketAttempt",
        "status": report["status"],
        "analysis_script": "scripts/attempt_selected_qa_su3_same_source_valpha_s3_operator_packet.py",
        "candidate_data": str(CANDIDATE.relative_to(ROOT)),
        "attempt_packet": str(PACKET.relative_to(ROOT)),
        "validator_result": report["validator_result"],
        "subvalidator_exit_codes": report["subvalidator_exit_codes"],
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
