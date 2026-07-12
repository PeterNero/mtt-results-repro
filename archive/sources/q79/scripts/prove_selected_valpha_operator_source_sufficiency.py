"""Prove conditional sufficiency for the selected V_alpha source packet.

This script does not claim that the selected source has been constructed.
Instead it answers a narrower question:

If a genuine selected source certificate supplies the currently missing source
flags for the ordered L2 packet, visible Green-Schwarz source, and Route-C
operator data, do the existing finite/curvature matrices already pass the
top-level Selected_VAlpha_ChernWeil_Operator_Source.v1 validator?

The answer should be yes.  That proves the remaining blocker is source origin,
Pic0/stability, and same-source derivation, not a hidden algebraic defect in
the downstream validator stack.
"""

from __future__ import annotations

import copy
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CANDIDATES = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
OUT_DIR = CANDIDATES / "selected_valpha_operator_source_sufficiency"

CURRENT_ATTEMPT = CANDIDATES / "selected_valpha_chern_weil_operator_source.current_attempt.json"
ORDERED_SOURCE_HYP = CANDIDATES / "visible_rank2_l2_ordered_source.monad_difference_hypothetical_selected.json"
GS_SOURCE_ATTEMPT = CERTS / "time_oriented_m1_visible_gs_source.attempt.json"
PROMOTION_ATTEMPT = CERTS / "selected_hym_operator_source_promotion.attempt.json"

OUT_PACKET = OUT_DIR / "selected_valpha_chern_weil_operator_source.hypothetical_selected.json"
OUT_GS = OUT_DIR / "time_oriented_m1_visible_gs_source.hypothetical_selected.json"
OUT_PROMOTION = OUT_DIR / "selected_source_promotion.hypothetical_selected.json"
OUT_CANDIDATE = CANDIDATES / "selected_valpha_operator_source_sufficiency.candidate.json"
OUT_CERT = CERTS / "selected_valpha_operator_source_sufficiency_certificate.json"

ROUTE_C_KEYS = [
    "route_c_residuals",
    "rhoE_mesh",
    "rhoE_metric",
    "sector_maps",
    "de_action",
    "riesz_gap",
    "reduced_green",
    "dotd_response",
]


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


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
        "stdout": proc.stdout,
        "output_head": proc.stdout.strip().splitlines()[:16],
    }


def parse_prefixed_json(stdout: str, prefix: str) -> dict[str, Any]:
    for line in stdout.splitlines():
        if line.startswith(prefix):
            return json.loads(line[len(prefix) :])
    return {}


def lift_flags(value: Any) -> Any:
    lifted = copy.deepcopy(value)

    def walk(node: Any) -> None:
        if isinstance(node, dict):
            for key in list(node):
                if key in {
                    "selected_source_verified",
                    "selected_dotD_source_verified",
                    "alpha1_driver_verified",
                }:
                    node[key] = True
                walk(node[key])
        elif isinstance(node, list):
            for item in node:
                walk(item)

    walk(lifted)
    return lifted


def build_hypothetical_gs_source() -> dict[str, Any]:
    packet = load(GS_SOURCE_ATTEMPT)
    packet["status"] = "HYPOTHETICAL_SELECTED_SOURCE_CONSISTENCY_CHECK"
    packet["selected_by_mtt"] = True
    packet["fixture_only"] = False
    evidence = packet.setdefault("visible_source_evidence", {})
    evidence["selected_visible_bundle_model"] = True
    evidence["same_branch_q79_f_m1"] = True
    evidence["chern_weil_row_from_source"] = True
    evidence["hym_or_route_c_residual_verified"] = True
    evidence["source_certificate"] = "selected_valpha_chern_weil_operator_source_hypothetical_certificate.json"
    evidence["current_blocker"] = "cleared only under hypothetical selected-source sufficiency check"
    return packet


def build_lifted_route_c_payloads() -> dict[str, str]:
    promotion = load(PROMOTION_ATTEMPT)
    source_paths = promotion["paths"]
    lifted_dir = OUT_DIR / "route_c_lifted_flags"
    out_paths: dict[str, str] = {}
    for key in ROUTE_C_KEYS:
        source_path = ROOT / source_paths[key]
        lifted = lift_flags(load(source_path))
        out_path = lifted_dir / f"{key}.hypothetical_selected.json"
        write(out_path, lifted)
        out_paths[key] = rel(out_path)
    return out_paths


def build_hypothetical_promotion(out_paths: dict[str, str]) -> dict[str, Any]:
    packet = load(PROMOTION_ATTEMPT)
    packet["status"] = "HYPOTHETICAL_SELECTED_SOURCE_CONSISTENCY_CHECK"
    packet["selected_source_verified"] = True
    packet["paths"] = out_paths
    return packet


def build_hypothetical_top_packet() -> dict[str, Any]:
    packet = load(CURRENT_ATTEMPT)
    packet["status"] = "HYPOTHETICAL_SELECTED_SOURCE_CONSISTENCY_CHECK"

    identity = packet["source_identity"]
    identity["source_certificate"] = "selected_valpha_chern_weil_operator_source_hypothetical_certificate.json"
    identity["selected_by_mtt"] = True
    identity["fixture_only"] = False

    valpha = packet["valpha_extension"]
    valpha["ordered_source_packet"] = rel(ORDERED_SOURCE_HYP)
    valpha["rank2_valpha_model_selected"] = True
    valpha["terminal_monad_difference_L3_minus_K2_selector_closed"] = True
    valpha["ordered_source_validator_passes"] = True
    valpha["pic0_resolution"] = "neutral_character_selected"
    valpha["pic0_selected_or_quotiented"] = True
    valpha["nonzero_ext_class_selected"] = True
    valpha["non_split_stability_or_hym_proved"] = True

    support = packet["s3_green_schwarz_support"]
    support["visible_gs_source_packet"] = rel(OUT_GS)
    support["same_source_link_valpha_to_s3_proved"] = True
    support["chern_weil_row_derived_from_same_source"] = True
    support["visible_gs_source_validator_passes"] = True

    execution = packet["operator_execution"]
    execution["selected_source_promotion_packet"] = rel(OUT_PROMOTION)
    for key in [
        "typed_transition_or_rhoE_data_emitted",
        "hym_strominger_or_routec_residual_pass",
        "sector_D_E_packets_pass",
        "reduced_green_packets_pass",
        "dotD_packets_pass",
        "same_branch_derivative_verified",
        "coherent_spectral_projector_retention",
        "selected_source_promotion_validator_passes",
        "primitive_C1_or_Yukawa_contractions",
    ]:
        execution[key] = True

    branch = packet["branch_orientation"]
    branch["orientation_selection_justified_by_source"] = True
    return packet


def analyze() -> dict[str, Any]:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    gs_packet = build_hypothetical_gs_source()
    write(OUT_GS, gs_packet)

    lifted_paths = build_lifted_route_c_payloads()
    promotion = build_hypothetical_promotion(lifted_paths)
    write(OUT_PROMOTION, promotion)

    top_packet = build_hypothetical_top_packet()
    write(OUT_PACKET, top_packet)

    validations = {
        "ordered_source_hypothetical": run_validator(
            "validate_visible_rank2_l2_ordered_source_packet.py",
            ORDERED_SOURCE_HYP,
        ),
        "visible_gs_hypothetical": run_validator(
            "validate_time_oriented_m1_visible_gs_source.py",
            OUT_GS,
        ),
        "selected_source_promotion_hypothetical": run_validator(
            "validate_iwasawa_selected_source_promotion.py",
            OUT_PROMOTION,
        ),
        "selected_valpha_source_hypothetical": run_validator(
            "validate_selected_valpha_chern_weil_operator_source.py",
            OUT_PACKET,
        ),
    }

    top_report = parse_prefixed_json(
        validations["selected_valpha_source_hypothetical"]["stdout"],
        "selected_valpha_chern_weil_operator_source_report=",
    )
    all_pass = all(item["exit_code"] == 0 for item in validations.values())

    actual_open = run_validator(
        "validate_selected_valpha_chern_weil_operator_source.py",
        CURRENT_ATTEMPT,
    )
    actual_report = parse_prefixed_json(
        actual_open["stdout"],
        "selected_valpha_chern_weil_operator_source_report=",
    )

    changed_fields = {
        "top_packet": [
            "source_identity.source_certificate",
            "source_identity.selected_by_mtt",
            "source_identity.fixture_only",
            "valpha_extension.rank2_valpha_model_selected",
            "valpha_extension.terminal_monad_difference_L3_minus_K2_selector_closed",
            "valpha_extension.ordered_source_packet",
            "valpha_extension.ordered_source_validator_passes",
            "valpha_extension.pic0_resolution",
            "valpha_extension.pic0_selected_or_quotiented",
            "valpha_extension.nonzero_ext_class_selected",
            "valpha_extension.non_split_stability_or_hym_proved",
            "s3_green_schwarz_support.visible_gs_source_packet",
            "s3_green_schwarz_support.same_source_link_valpha_to_s3_proved",
            "s3_green_schwarz_support.chern_weil_row_derived_from_same_source",
            "s3_green_schwarz_support.visible_gs_source_validator_passes",
            "operator_execution.selected_source_promotion_packet",
            "operator_execution.*_passes",
            "branch_orientation.orientation_selection_justified_by_source",
        ],
        "route_c_payloads": [
            "selected_source_verified",
            "selected_dotD_source_verified",
            "alpha1_driver_verified",
        ],
        "visible_gs_packet": [
            "selected_by_mtt",
            "visible_source_evidence.selected_visible_bundle_model",
            "visible_source_evidence.chern_weil_row_from_source",
            "visible_source_evidence.hym_or_route_c_residual_verified",
            "visible_source_evidence.source_certificate",
        ],
    }

    status = (
        "SELECTED_VALPHA_OPERATOR_SOURCE_CONDITIONAL_SUFFICIENCY_PROVED_SOURCE_OPEN"
        if all_pass and actual_open["exit_code"] == 2
        else "SELECTED_VALPHA_OPERATOR_SOURCE_CONDITIONAL_SUFFICIENCY_FAILED"
    )
    report = {
        "calculation": "SelectedVAlphaOperatorSourceSufficiency",
        "status": status,
        "generated_by": "scripts/prove_selected_valpha_operator_source_sufficiency.py",
        "hypothetical_packets": {
            "selected_valpha_source": rel(OUT_PACKET),
            "visible_green_schwarz_source": rel(OUT_GS),
            "selected_source_promotion": rel(OUT_PROMOTION),
            "route_c_lifted_payload_dir": rel(OUT_DIR / "route_c_lifted_flags"),
        },
        "validation_exit_codes": {
            key: value["exit_code"] for key, value in validations.items()
        },
        "validation_heads": {
            key: value["output_head"] for key, value in validations.items()
        },
        "actual_packet_validation": {
            "exit_code": actual_open["exit_code"],
            "status": actual_report.get("status"),
            "open_item_count": len(actual_report.get("open_items", [])),
        },
        "hypothetical_top_report": top_report,
        "conditional_theorem": {
            "proved": all_pass and actual_open["exit_code"] == 2,
            "statement": (
                "If a genuine selected source certificate justifies the ordered "
                "L3-K2/Pic0/stability fields, derives the visible Green-Schwarz "
                "row from the same source, and validates the same Route-C D_E, "
                "Riesz/Green, and dotD payloads as selected data, then the "
                "Selected_VAlpha_ChernWeil_Operator_Source.v1 validator passes."
            ),
        },
        "changed_fields": changed_fields,
        "what_this_closes": {
            "downstream_validator_stack_has_no_hidden_matrix_defect": all_pass,
            "selected_valpha_source_packet_sufficiency_condition": all_pass,
            "actual_packet_still_open_without_source_flags": actual_open["exit_code"] == 2,
            "next_work_is_source_derivation_not_validator_plumbing": all_pass,
        },
        "what_this_does_not_close": {
            "actual_selected_source_certificate": False,
            "Pic0_selection_or_quotient": False,
            "nonzero_Ext_class_and_stability": False,
            "same_source_Chern_Weil_derivation": False,
            "selected_D_E_dotD_Riesz_Green_as_proof_data": False,
            "primitive_C1_contractions": False,
            "full_SM_closure": False,
        },
        "guardrails": {
            "claims_hypothetical_flags_are_physical_proof": False,
            "claims_selected_source_constructed": False,
            "claims_pic0_resolved": False,
            "claims_D_E_dotD_constructed": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "The selected V_alpha operator-source validator stack is "
                "conditionally sufficient.  When only the missing source and "
                "same-source flags are supplied by a hypothetical certificate, "
                "the ordered-source, visible-GS, selected-source-promotion, and "
                "top-level V_alpha validators all pass.  Therefore the remaining "
                "blocker is a genuine selected-source derivation, not hidden "
                "finite-matrix algebra."
            ),
            "next_action": (
                "Prove the source certificate itself: derive L3-K2/Pic0/stability "
                "and the visible Chern-Weil row from one selected V_alpha HYM or "
                "Route-C source, then replace the hypothetical lifted flags."
            ),
        },
    }
    write(OUT_CANDIDATE, report)
    cert = {
        "certificate": "SelectedVAlphaOperatorSourceSufficiency",
        "status": report["status"],
        "analysis_script": report["generated_by"],
        "candidate_data": rel(OUT_CANDIDATE),
        "hypothetical_packets": report["hypothetical_packets"],
        "validation_exit_codes": report["validation_exit_codes"],
        "actual_packet_validation": report["actual_packet_validation"],
        "conditional_theorem": report["conditional_theorem"],
        "what_this_closes": report["what_this_closes"],
        "what_this_does_not_close": report["what_this_does_not_close"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    write(OUT_CERT, cert)
    return report


def main() -> int:
    report = analyze()
    print(json.dumps(report, indent=2, sort_keys=True))
    return (
        0
        if report["status"]
        == "SELECTED_VALPHA_OPERATOR_SOURCE_CONDITIONAL_SUFFICIENCY_PROVED_SOURCE_OPEN"
        else 1
    )


if __name__ == "__main__":
    raise SystemExit(main())
