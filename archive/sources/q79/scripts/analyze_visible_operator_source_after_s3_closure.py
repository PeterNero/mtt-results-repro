"""Reduce the visible operator-source blocker after the selected S3 closure.

The selected S3 class/restriction packet closes the gerbe-side obstruction:
fixed flat class, S3 pullback table, smooth twisted Freed-Witten cancellation,
and block-sector projector retention.  This script checks what that changes in
the visible Green-Schwarz/operator-source route and records the remaining
irreducible cut set without promoting copied curvature rows to a source.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = ROOT / "candidate_data" / "visible_operator_source_after_s3_closure.candidate.json"
CERTIFICATE = ROOT / "certificates" / "visible_operator_source_after_s3_closure_certificate.json"

S3_CLOSURE = ROOT / "certificates" / "visible_twisted_s3_class_restriction_closure_certificate.json"
GS_CURVATURE = (
    ROOT / "certificates" / "time_oriented_m1_visible_green_schwarz_curvature_closure_certificate.json"
)
GS_SOURCE_ATTEMPT = ROOT / "certificates" / "time_oriented_m1_visible_gs_source_attempt_certificate.json"
HYM_ATTEMPT = ROOT / "certificates" / "selected_hym_operator_source_attempt_certificate.json"
BLOCKER_RESOLUTION = ROOT / "certificates" / "visible_operator_source_blocker_resolution_certificate.json"
TWISTED_PACKET_FILL = ROOT / "certificates" / "iwasawa_twisted_source_packet_fill_attempt_certificate.json"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def closed_bool(data: dict[str, Any], *keys: str) -> bool:
    current: Any = data
    for key in keys:
        if not isinstance(current, dict):
            return False
        current = current.get(key)
    return current is True


def analyze() -> dict[str, Any]:
    s3 = load_json(S3_CLOSURE)
    gs_curvature = load_json(GS_CURVATURE)
    gs_source = load_json(GS_SOURCE_ATTEMPT)
    hym = load_json(HYM_ATTEMPT)
    blocker = load_json(BLOCKER_RESOLUTION)
    twisted_fill = load_json(TWISTED_PACKET_FILL)

    s3_closed = s3.get("status") == "VISIBLE_TWISTED_S3_CLASS_RESTRICTION_CLOSED_OPERATOR_SOURCE_OPEN"
    gs_curvature_closed = (
        gs_curvature.get("status") == "TIME_ORIENTED_M1_VISIBLE_GS_CURVATURE_CLOSED_OPERATOR_SOURCE_OPEN"
    )
    visible_source_still_open = (
        gs_source.get("status") == "TIME_ORIENTED_M1_VISIBLE_GS_SOURCE_ATTEMPT_BLOCKED_SELECTED_SOURCE_MISSING"
    )

    retired_by_s3 = {
        "fixed_smooth_flat_S3_class": closed_bool(
            s3, "calculation_results", "fixed_smooth_flat_gerbe_class_closed"
        ),
        "S3_pullback_table": closed_bool(s3, "calculation_results", "S3_pullback_table_supplied"),
        "qutrit_central_cocycle_map": closed_bool(
            s3, "calculation_results", "map_to_qutrit_central_cocycle_verified"
        ),
        "smooth_S3_twisted_Freed_Witten": closed_bool(
            s3, "calculation_results", "smooth_Freed_Witten_cancellation_closed"
        ),
        "block_sector_projector_retention": closed_bool(
            s3, "calculation_results", "block_sector_projector_retention_closed"
        ),
    }

    retired_by_curvature = {
        "required_visible_TrF_row_inserted": closed_bool(
            gs_curvature, "calculation_results", "required_visible_TrF_row_inserted"
        ),
        "zero_visible_green_schwarz_residual": closed_bool(
            gs_curvature, "calculation_results", "visible_green_schwarz_curvature_verified"
        ),
        "symbolic_iwasawa_row_validated": closed_bool(
            gs_curvature, "calculation_results", "symbolic_iwasawa_row_validated"
        ),
    }

    source_attempt = gs_source.get("attempted_source", {})
    remaining_cut_set = {
        "selected_visible_bundle_or_sheaf_model": source_attempt.get(
            "selected_visible_bundle_model"
        )
        is not True,
        "Chern_Weil_row_derived_from_selected_source": source_attempt.get(
            "chern_weil_row_from_source"
        )
        is not True,
        "HYM_or_Route_C_residual_for_visible_source": closed_bool(
            hym, "calculation_results", "selected_hym_operator_source_verified"
        )
        is not True,
        "selected_D_E_dotD_Riesz_Green": closed_bool(
            hym, "calculation_results", "route_c_honest_operator_pipeline_pass"
        )
        is not True,
        "coherent_spectral_zero_mode_projectors": closed_bool(
            gs_curvature, "calculation_results", "projector_retention_verified"
        )
        is not True,
        "primitive_C1_contractions": True,
    }

    all_retired_closed = all(retired_by_s3.values()) and all(retired_by_curvature.values())
    remaining_open = any(remaining_cut_set.values())
    blocker_still_irreducible = (
        blocker.get("status") == "VISIBLE_OPERATOR_SOURCE_BLOCKER_IRREDUCIBLE_NEW_SOURCE_REQUIRED"
        and remaining_open
    )

    return {
        "calculation": "VisibleOperatorSourceAfterS3Closure",
        "status": (
            "VISIBLE_OPERATOR_SOURCE_REDUCED_TO_SELECTED_CW_OPERATOR_SOURCE_OPEN"
            if all_retired_closed and blocker_still_irreducible
            else "VISIBLE_OPERATOR_SOURCE_REDUCTION_NOT_VERIFIED"
        ),
        "generated_by": "scripts/analyze_visible_operator_source_after_s3_closure.py",
        "inputs": {
            "s3_class_restriction_closure_certificate": S3_CLOSURE.name,
            "visible_green_schwarz_curvature_closure_certificate": GS_CURVATURE.name,
            "visible_green_schwarz_source_attempt_certificate": GS_SOURCE_ATTEMPT.name,
            "selected_hym_operator_source_attempt_certificate": HYM_ATTEMPT.name,
            "visible_operator_source_blocker_resolution_certificate": BLOCKER_RESOLUTION.name,
            "twisted_source_packet_fill_attempt_certificate": TWISTED_PACKET_FILL.name,
        },
        "retired_by_selected_s3_closure": retired_by_s3,
        "retired_by_visible_curvature_closure": retired_by_curvature,
        "still_open_cut_set": remaining_cut_set,
        "current_visible_source_attempt": {
            "source_attempt_still_open": visible_source_still_open,
            "required_visible_row_filled": source_attempt.get("required_visible_row_filled"),
            "selected_visible_bundle_model": source_attempt.get("selected_visible_bundle_model"),
            "chern_weil_row_from_source": source_attempt.get("chern_weil_row_from_source"),
            "validator_exit_code": gs_source.get("validator_result", {}).get("exit_code"),
        },
        "operator_source_target": {
            "schema_to_fill": "TimeOrientedM1VisibleGreenSchwarzSource.v1 plus selected D_E/dotD packets",
            "must_consume": [
                "visible_twisted_s3_class_restriction_closure_certificate.json",
                "time_oriented_m1_visible_green_schwarz_curvature_closure_certificate.json",
            ],
            "must_supply_next": [
                "selected visible bundle/sheaf or Route-C source on q79/F,m=1",
                "Chern-Weil derivation of Tr_F_visible^2 from that source",
                "HYM/Strominger or Route-C residual with selected_source_verified true",
                "sector D_E action matrices from the same source",
                "Riesz projector, reduced Green, and dotD_alpha1 response",
                "coherent zero-mode projector retention for those spectral data",
                "primitive C1 contractions",
            ],
        },
        "calculation_results": {
            "selected_s3_support_now_closed": s3_closed and all(retired_by_s3.values()),
            "visible_gs_curvature_now_closed": gs_curvature_closed
            and all(retired_by_curvature.values()),
            "visible_source_attempt_still_rejected": visible_source_still_open,
            "old_s3_gerbe_fw_projector_blockers_retired": all(retired_by_s3.values()),
            "operator_source_cut_set_still_open": remaining_open,
            "blocker_reduced_not_closed": all_retired_closed and blocker_still_irreducible,
        },
        "guardrails": {
            "claims_selected_visible_operator_source_constructed": False,
            "claims_chern_weil_row_derived_from_selected_bundle": False,
            "claims_selected_D_E_dotD_constructed": False,
            "claims_coherent_spectral_projectors_constructed": False,
            "claims_yukawa_matrices_computed": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "The selected S3 closure changes the visible-source problem: "
                "gerbe class, S3 restriction, smooth Freed-Witten cancellation, "
                "and block-sector projector retention are no longer blockers. "
                "The remaining blocker is the selected visible Chern-Weil/operator "
                "source that derives the required Tr_F row and supplies D_E/dotD "
                "spectral data."
            ),
            "next_action": (
                "Construct a selected q79/F,m=1 visible bundle/sheaf or Route-C "
                "source whose Chern-Weil row equals the derived alpha_1 row, then "
                "emit same-source D_E, Riesz/Green, dotD, and primitive C1 data."
            ),
        },
    }


def main() -> int:
    report = analyze()
    write_json(CANDIDATE, report)
    certificate = {
        "certificate": "VisibleOperatorSourceAfterS3Closure",
        "status": report["status"],
        "analysis_script": report["generated_by"],
        "candidate_data": "candidate_data/visible_operator_source_after_s3_closure.candidate.json",
        "inputs": report["inputs"],
        "retired_by_selected_s3_closure": report["retired_by_selected_s3_closure"],
        "retired_by_visible_curvature_closure": report["retired_by_visible_curvature_closure"],
        "still_open_cut_set": report["still_open_cut_set"],
        "operator_source_target": report["operator_source_target"],
        "calculation_results": report["calculation_results"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    write_json(CERTIFICATE, certificate)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["calculation_results"]["blocker_reduced_not_closed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
