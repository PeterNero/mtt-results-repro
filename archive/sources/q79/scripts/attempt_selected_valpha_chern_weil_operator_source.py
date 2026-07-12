"""Attempt to fill Selected_VAlpha_ChernWeil_Operator_Source.v1.

The expected current result is OPEN.  This script fills every field that is
closed by the present q79 certificates and leaves the genuine source-selection,
Pic0, stability, Chern-Weil derivation, and operator-execution flags false.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
CANDIDATES = ROOT / "candidate_data"

PACKET = CANDIDATES / "selected_valpha_chern_weil_operator_source.current_attempt.json"
CANDIDATE = CANDIDATES / "selected_valpha_chern_weil_operator_source_attempt.candidate.json"
CERT = CERTS / "selected_valpha_chern_weil_operator_source_attempt_certificate.json"

CRITICAL = CERTS / "valpha_operator_source_critical_path_certificate.json"
CONSTANTS = CERTS / "constants_m1_cw_source_route_import_certificate.json"
S3_CLOSURE = CERTS / "visible_twisted_s3_class_restriction_closure_certificate.json"
S3_PACKET = CERTS / "visible_twisted_s3_class_restriction_packet.selected.json"
GS_CURVATURE = CERTS / "time_oriented_m1_visible_green_schwarz_curvature_closure_certificate.json"
GS_SOURCE_ATTEMPT = CERTS / "time_oriented_m1_visible_gs_source_attempt_certificate.json"
GS_SOURCE_PACKET = CERTS / "time_oriented_m1_visible_gs_source.attempt.json"
ORIENTATION = CERTS / "selected_qa_su3_orientation_dedotd_source_attempt_certificate.json"
ANTIUNITARY = CERTS / "orientation_branch_antiunitary_equivalence_certificate.json"
PARITY = CERTS / "orientation_observable_parity_certificate.json"
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
            str(ROOT / "scripts" / "validate_selected_valpha_chern_weil_operator_source.py"),
            str(path),
        ],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    prefix = "selected_valpha_chern_weil_operator_source_report="
    parsed = None
    for line in proc.stdout.splitlines():
        if line.startswith(prefix):
            parsed = json.loads(line[len(prefix) :])
            break
    return {"exit_code": proc.returncode, "stdout": proc.stdout, "parsed_report": parsed}


def build_packet() -> dict[str, Any]:
    constants = load(CONSTANTS)
    s3 = load(S3_CLOSURE)
    gs_curvature = load(GS_CURVATURE)
    gs_source = load(GS_SOURCE_ATTEMPT)
    orientation = load(ORIENTATION)
    antiunitary = load(ANTIUNITARY)
    parity = load(PARITY)

    target = constants["target_alignment"]["q79_target"]
    h1 = constants["h1_bridge"]

    return {
        "schema": "SelectedVAlphaChernWeilOperatorSource.v1",
        "status": "ATTEMPT_BLOCKED_SELECTED_VALPHA_OPERATOR_SOURCE_OPEN",
        "source_identity": {
            "branch_id": "q79/F,m=1",
            "source_certificate": None,
            "source_kind": "rank2_valpha_chern_weil_operator_source",
            "selected_by_mtt": False,
            "fixture_only": True,
            "no_observed_flavor_inputs": True,
            "no_benchmark_flavor_inputs": True,
        },
        "valpha_extension": {
            "selected_L": target["l_vector_abc"],
            "selected_L2": target["c1_L_squared_vector_abc"],
            "c2_valpha": target["c2_extension_alpha_coeffs"],
            "h1_L2": h1["original_h1"],
            "ordered_source_packet": str(ORDERED_SOURCE.relative_to(ROOT)),
            "rank2_valpha_model_selected": False,
            "terminal_monad_difference_L3_minus_K2_selector_closed": False,
            "ordered_source_validator_passes": False,
            "pic0_resolution": "OPEN",
            "pic0_selected_or_quotiented": False,
            "nonzero_ext_class_selected": False,
            "non_split_stability_or_hym_proved": False,
        },
        "s3_green_schwarz_support": {
            "s3_class_restriction_packet": str(S3_PACKET.relative_to(ROOT)),
            "selected_s3_class_restriction_closed": s3["calculation_results"][
                "selected_S3_class_restriction_packet_constructed"
            ],
            "block_projector_retention_closed": s3["calculation_results"][
                "block_sector_projector_retention_closed"
            ],
            "visible_gs_curvature_closed": gs_curvature["calculation_results"][
                "visible_green_schwarz_curvature_verified"
            ],
            "visible_gs_source_packet": str(GS_SOURCE_PACKET.relative_to(ROOT)),
            "same_source_link_valpha_to_s3_proved": False,
            "chern_weil_row_derived_from_same_source": gs_source["attempted_source"][
                "chern_weil_row_from_source"
            ],
            "visible_gs_source_validator_passes": gs_source["calculation_results"][
                "visible_green_schwarz_source_verified"
            ],
        },
        "operator_execution": {
            "selected_source_promotion_packet": str(PROMOTION_PACKET.relative_to(ROOT)),
            "typed_transition_or_rhoE_data_emitted": False,
            "hym_strominger_or_routec_residual_pass": False,
            "sector_D_E_packets_pass": False,
            "reduced_green_packets_pass": False,
            "dotD_packets_pass": False,
            "same_branch_derivative_verified": False,
            "coherent_spectral_projector_retention": False,
            "selected_source_promotion_validator_passes": False,
            "primitive_C1_or_Yukawa_contractions": False,
        },
        "branch_orientation": {
            "time_oriented_q79_representative": True,
            "m1_label_bound_to_q79": True,
            "antiunitary_conjugate_pair_accounted": antiunitary["what_this_closes"][
                "q79_q369_finite_operator_conjugacy"
            ],
            "cp_even_parity_accounted": parity["finite_operator_parity"][
                "finite_parity_closed"
            ],
            "orientation_selection_justified_by_source": orientation["calculation_results"][
                "unique_m_label_selected_by_source"
            ],
        },
        "forbidden_shortcuts": {
            "uses_observed_masses_or_mixings": False,
            "uses_benchmark_flavor_entries": False,
            "copies_visible_gs_row_without_source_derivation": False,
            "uses_routec_smoke_as_selected_operator_data": False,
            "splices_s3_and_valpha_without_same_source_link": False,
            "treats_pic0_as_notational_without_rule": False,
        },
    }


def main() -> int:
    packet = build_packet()
    write(PACKET, packet)
    validation = run_validator(PACKET)
    parsed = validation["parsed_report"] or {}
    subvalidators = parsed.get("subvalidators", {})
    open_items = parsed.get("open_items", [])
    critical = load(CRITICAL)

    report = {
        "calculation": "SelectedVAlphaChernWeilOperatorSourceAttempt",
        "status": "SELECTED_VALPHA_CHERN_WEIL_OPERATOR_SOURCE_ATTEMPT_OPEN",
        "attempt_packet": str(PACKET.relative_to(ROOT)),
        "validator": "scripts/validate_selected_valpha_chern_weil_operator_source.py",
        "validator_result": {
            "exit_code": validation["exit_code"],
            "parsed_report": parsed,
        },
        "critical_packet_contract": critical["critical_packet_contract"],
        "subvalidator_exit_codes": {
            key: value.get("exit_code") for key, value in subvalidators.items()
        },
        "open_item_count": len(open_items),
        "first_open_items": open_items[:32],
        "closed_inputs_consumed": {
            "constants_q79_target_alignment": True,
            "selected_s3_class_restriction": subvalidators.get("s3_class_restriction", {}).get("exit_code")
            == 0,
            "visible_gs_curvature_closed": packet["s3_green_schwarz_support"][
                "visible_gs_curvature_closed"
            ],
            "antiunitary_branch_pair_accounted": packet["branch_orientation"][
                "antiunitary_conjugate_pair_accounted"
            ],
            "cp_even_parity_accounted": packet["branch_orientation"][
                "cp_even_parity_accounted"
            ],
        },
        "what_this_closes": {
            "selected_valpha_operator_source_validator_created": True,
            "critical_packet_attempt_materialized": True,
            "closed_s3_and_branch_inputs_consumed": True,
            "open_fields_are_machine_reported": validation["exit_code"] == 2,
        },
        "what_this_does_not_close": {
            "selected_visible_valpha_source": False,
            "Pic0_selection_or_quotient": False,
            "nonzero_Ext_class_and_stability": False,
            "same_source_Chern_Weil_derivation": False,
            "selected_D_E_dotD_Riesz_Green": False,
            "primitive_C1_contractions": False,
            "full_SM_closure": False,
        },
        "guardrails": {
            "claims_selected_source_constructed": False,
            "claims_pic0_resolved": False,
            "claims_D_E_dotD_constructed": False,
            "claims_primitive_C1_contractions": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "The Selected_VAlpha_ChernWeil_Operator_Source.v1 slot is now "
                "executable.  The current best fill consumes the closed q79 "
                "target, S3 class/restriction, visible GS curvature, and finite "
                "branch parity data, but the validator correctly keeps it OPEN "
                "until V_alpha selection, Pic0, stability, same-source "
                "Chern-Weil derivation, and operator execution are supplied."
            ),
            "next_action": (
                "Fill this packet from a real selected rank-two V_alpha HYM or "
                "Route-C source; the first flags to flip are source_certificate, "
                "terminal_monad_difference_L3_minus_K2_selector_closed, "
                "pic0_selected_or_quotiented, and chern_weil_row_derived_from_same_source."
            ),
        },
    }
    write(CANDIDATE, report)
    cert = {
        "certificate": "SelectedVAlphaChernWeilOperatorSourceAttempt",
        "status": report["status"],
        "analysis_script": "scripts/attempt_selected_valpha_chern_weil_operator_source.py",
        "candidate_data": str(CANDIDATE.relative_to(ROOT)),
        "attempt_packet": str(PACKET.relative_to(ROOT)),
        "validator_result": report["validator_result"],
        "subvalidator_exit_codes": report["subvalidator_exit_codes"],
        "open_item_count": report["open_item_count"],
        "first_open_items": report["first_open_items"],
        "closed_inputs_consumed": report["closed_inputs_consumed"],
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
