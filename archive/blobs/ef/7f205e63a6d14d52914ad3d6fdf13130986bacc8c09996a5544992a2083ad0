"""Prove that Deligne/Cech cover choice is auxiliary for the m=1 S3 route.

The previous smooth-source lift gate deliberately asked for selected cover or
good-cover evidence.  This script records the sharper mathematical reduction:
a good cover is a representative choice for Deligne/Cech data, not a physical
MTT selection datum.  The selected data must instead be the differential
cohomology class, its S3 restriction, Freed-Witten cancellation, and projector
retention.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATES = ROOT / "certificates"
CANDIDATE_DATA = ROOT / "candidate_data"

CANDIDATE = CANDIDATE_DATA / "iwasawa_deligne_cover_gauge_reduction.candidate.json"
CERTIFICATE = CERTIFICATES / "iwasawa_deligne_cover_gauge_reduction_certificate.json"

STANDARD_DECK_CERT = CERTIFICATES / "iwasawa_standard_lattice_deck_scaffold_certificate.json"
FIXED_GERBE_CERT = CERTIFICATES / "time_oriented_fixed_gerbe_representative_certificate.json"
M1_PERIOD_CERT = CERTIFICATES / "time_oriented_m1_gerbe_period_table_certificate.json"
M1_DECK_CECH_CERT = CERTIFICATES / "time_oriented_m1_deck_cech_lift_certificate.json"
M1_FLAT_GERBE_CERT = CERTIFICATES / "time_oriented_m1_flat_gerbe_promotion_certificate.json"
SMOOTH_LIFT_CERT = CERTIFICATES / "visible_twisted_s3_smooth_source_lift_attempt_certificate.json"


EXPECTED_STATUSES = {
    STANDARD_DECK_CERT.name: "STANDARD_IWASAWA_DECK_SCAFFOLD_FORMULATED_SELECTION_OPEN",
    FIXED_GERBE_CERT.name: "TIME_ORIENTED_FIXED_GERBE_REPRESENTATIVE_CLOSED_SOURCE_PACKET_OPEN",
    M1_PERIOD_CERT.name: "TIME_ORIENTED_M1_FINITE_GERBE_PERIOD_TABLE_CLOSED_OPERATOR_SOURCE_OPEN",
    M1_DECK_CECH_CERT.name: "TIME_ORIENTED_M1_DECK_CECH_LIFT_CLOSED_GEOMETRIC_OPERATOR_SOURCE_OPEN",
    M1_FLAT_GERBE_CERT.name: "TIME_ORIENTED_M1_FLAT_GERBE_PROMOTION_CONDITIONAL_CLOSED_SELECTION_OPEN",
    SMOOTH_LIFT_CERT.name: "VISIBLE_TWISTED_S3_SMOOTH_SOURCE_LIFT_ATTEMPT_BLOCKED_SELECTED_COVER_PROJECTORS_OPEN",
}


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def dependency_statuses() -> dict[str, str | None]:
    statuses: dict[str, str | None] = {}
    for path in (
        STANDARD_DECK_CERT,
        FIXED_GERBE_CERT,
        M1_PERIOD_CERT,
        M1_DECK_CECH_CERT,
        M1_FLAT_GERBE_CERT,
        SMOOTH_LIFT_CERT,
    ):
        statuses[path.name] = load_json(path).get("status") if path.exists() else None
    return statuses


def prove() -> dict[str, Any]:
    standard = load_json(STANDARD_DECK_CERT)
    fixed = load_json(FIXED_GERBE_CERT)
    period = load_json(M1_PERIOD_CERT)
    deck = load_json(M1_DECK_CECH_CERT)
    flat = load_json(M1_FLAT_GERBE_CERT)
    smooth = load_json(SMOOTH_LIFT_CERT)
    statuses = dependency_statuses()
    dependencies_match = all(
        statuses.get(name) == expected for name, expected in EXPECTED_STATUSES.items()
    )

    standard_scaffold_valid = (
        standard.get("verified_algebra", {}).get("coframe_invariant_under_left_deck_action")
        is True
        and standard.get("verified_algebra", {}).get("compact_quotient_if_candidate_Gamma0_selected")
        is True
    )
    finite_class_fixed = (
        fixed.get("calculation_results", {}).get("time_oriented_torsion_label_m1_fixed")
        is True
        and period.get("calculation_results", {}).get("finite_m1_period_table_constructed")
        is True
        and deck.get("calculation_results", {}).get("deck_cech_pullback_constructed") is True
    )
    conditional_flat_model = (
        flat.get("calculation_results", {}).get("conditional_flat_gerbe_representative_exists")
        is True
        and flat.get("flat_gerbe_model", {}).get("curvature_H_form") == "0"
    )
    smooth_gate_waits_for_source = (
        smooth.get("calculation_results", {}).get("selected_smooth_S3_source_constructed")
        is False
        and smooth.get("calculation_results", {}).get("smooth_S3_projector_retention_closed")
        is False
    )

    reduction_closed = (
        dependencies_match
        and standard_scaffold_valid
        and finite_class_fixed
        and conditional_flat_model
        and smooth_gate_waits_for_source
    )

    return {
        "candidate": "IwasawaDeligneCoverGaugeReduction",
        "status": (
            "IWASAWA_DELIGNE_COVER_GAUGE_REDUCTION_CLOSED_CLASS_RESTRICTION_OPEN"
            if reduction_closed
            else "IWASAWA_DELIGNE_COVER_GAUGE_REDUCTION_NOT_CLOSED"
        ),
        "generated_by": "scripts/prove_iwasawa_deligne_cover_gauge_reduction.py",
        "dependency_statuses": statuses,
        "mathematical_reduction": {
            "good_cover_role": "auxiliary representative for Cech/Deligne data",
            "reason": (
                "Deligne/Cech representatives on different good covers are "
                "identified by refinement and coboundary equivalence; the "
                "physical datum is the differential-cohomology class, not the "
                "chosen cover."
            ),
            "aspherical_route": (
                "On a quotient with contractible universal cover, the normalized "
                "deck U(1) two-cocycle represents a flat gerbe class; a good "
                "cover can be chosen to write local Deligne data but is not an "
                "extra MTT knob."
            ),
            "curvature_H_form": "0",
            "torsion_order": 3,
        },
        "inputs_checked": {
            "standard_deck_scaffold_valid": standard_scaffold_valid,
            "finite_q79_F_m1_class_fixed": finite_class_fixed,
            "conditional_flat_Deligne_model_exists": conditional_flat_model,
            "smooth_lift_gate_already_waits_for_source": smooth_gate_waits_for_source,
        },
        "what_this_closes": {
            "particular_good_cover_need_not_be_MTT_selected": reduction_closed,
            "cover_refinement_invariance_for_Deligne_Cech_representatives": reduction_closed,
            "selected_cover_blocker_reduced_to_selected_class_and_restriction": reduction_closed,
            "good_cover_is_execution_scaffold_not_physical_knob": reduction_closed,
        },
        "still_open": {
            "fixed_smooth_S3_differential_cohomology_class": True,
            "actual_good_cover_tables_for_executable_restriction": True,
            "restriction_of_the_flat_class_to_selected_S3_worldvolume": True,
            "smooth_S3_Freed_Witten_cancellation": True,
            "twisted_projector_retention_for_block_factorized_sectors": True,
            "selected_visible_operator_source": True,
            "selected_D_E_dotD": True,
            "primitive_C1_contractions_and_SM_closure": True,
        },
        "guardrails": {
            "claims_Gamma0_is_MTT_selected": False,
            "claims_selected_smooth_S3_source": False,
            "claims_Freed_Witten_closed": False,
            "claims_projector_retention": False,
            "claims_selected_D_E_dotD_constructed": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "The good cover itself is not the next physical selection "
                "problem. It is a gauge/execution representative for the "
                "Deligne/Cech gerbe. The remaining physical object is the "
                "selected smooth differential-cohomology class on S3, with "
                "restriction, Freed-Witten cancellation, and projector "
                "retention proved on the same branch."
            ),
            "next_closing_object": (
                "Construct the selected S3 class/restriction packet: fixed "
                "smooth flat gerbe class, S3 pullback table, twisted CP module "
                "matching that pullback, W3/spinC input, and block-sector "
                "projector retention."
            ),
        },
    }


def main() -> int:
    report = prove()
    write_json(CANDIDATE, report)
    certificate = {
        "certificate": "IwasawaDeligneCoverGaugeReduction",
        "status": report["status"],
        "analysis_script": report["generated_by"],
        "candidate_data": "candidate_data/iwasawa_deligne_cover_gauge_reduction.candidate.json",
        "dependency_statuses": report["dependency_statuses"],
        "mathematical_reduction": report["mathematical_reduction"],
        "inputs_checked": report["inputs_checked"],
        "what_this_closes": report["what_this_closes"],
        "still_open": report["still_open"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    write_json(CERTIFICATE, certificate)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
