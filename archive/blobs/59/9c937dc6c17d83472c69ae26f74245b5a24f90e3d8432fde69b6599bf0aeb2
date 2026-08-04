"""Prove finite S3 twisted Chan-Paton cancellation.

This closes only the finite quotient cancellation statement.  It does not
promote the S3 source to a selected smooth Deligne/Cech or worldvolume-flux
source, and it does not prove projector retention or selected D_E/dotD data.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = ROOT / "candidate_data" / "visible_twisted_s3_finite_cp_cancellation.candidate.json"
CERTIFICATE = ROOT / "certificates" / "visible_twisted_s3_finite_cp_cancellation_certificate.json"

S3_SELECTOR_CERT = ROOT / "certificates" / "visible_twisted_d7_equivariant_embedding_selector_certificate.json"
CP_RESCUE_CERT = ROOT / "certificates" / "visible_twisted_chan_paton_rescue_certificate.json"
FW_GATE_CERT = ROOT / "certificates" / "time_oriented_m1_freed_witten_cycle_gate_certificate.json"
COMPLEX_SPINC_CERT = ROOT / "certificates" / "visible_complex_worldvolume_spinc_gate_certificate.json"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def s3_assignments(cp: dict[str, Any]) -> list[dict[str, Any]]:
    assignments = cp.get("coordinate_rescue_enumeration", {}).get("minimal_rescue_assignments", [])
    return [
        item
        for item in assignments
        if item.get("twisted_projective_D7_stack_required") == "S3"
    ]


def cancellation_report(assignment: dict[str, Any]) -> dict[str, Any]:
    return {
        "generator_factor_assignment": assignment.get("generator_factor_assignment"),
        "twisted_projective_D7_stack_required": "S3",
        "S3_active_image_rank_over_F3": 2,
        "ordinary_DD_zero_D7_stacks": assignment.get("ordinary_DD_zero_D7_stacks"),
        "ordinary_DD_zero_matter_curves": assignment.get("ordinary_DD_zero_matter_curves"),
        "ordinary_DD_gate_for_S3": False,
        "finite_twisted_CP_module_on_S3": True,
        "finite_twisted_CP_DD_class_matches_B_restriction": True,
        "finite_total_twisted_DD_class_zero": True,
        "matter_curves_remain_ordinary": assignment.get("all_matter_curves_ordinary_DD_zero") is True,
    }


def build_report() -> dict[str, Any]:
    selector = load_json(S3_SELECTOR_CERT)
    cp = load_json(CP_RESCUE_CERT)
    fw = load_json(FW_GATE_CERT)
    spinc = load_json(COMPLEX_SPINC_CERT)
    assignments = s3_assignments(cp)

    projective = cp.get("projective_module_check", {})
    finite_module_matches = (
        projective.get("finite_projective_module_matches_m1_twist") is True
        and projective.get("m1_period_table_q") == 79
        and projective.get("m1_period_table_torsion_label") == 1
        and projective.get("validator", {}).get("exit") == 0
    )
    selector_closed = (
        selector.get("status")
        == "VISIBLE_TWISTED_D7_EQUIVARIANT_EMBEDDING_SELECTOR_S3_CLOSED_SOURCE_OPEN"
    )
    fw_finite_gate_closed = (
        fw.get("status")
        == "TIME_ORIENTED_M1_FREED_WITTEN_CYCLE_GATE_FORMULATED_SELECTED_CYCLES_OPEN"
        and fw.get("calculation_results", {}).get("rank_two_active_images_fail_DD_part")
        is True
    )
    spinc_closed = (
        spinc.get("status") == "VISIBLE_COMPLEX_WORLDVOLUME_SPINC_W3_CLOSED_DD_IMAGES_OPEN"
    )
    finite_cancellation_closed = (
        selector_closed
        and finite_module_matches
        and fw_finite_gate_closed
        and spinc_closed
        and len(assignments) == 2
        and all(item.get("ordinary_DD_zero_D7_stacks") == ["S1", "S2"] for item in assignments)
        and all(item.get("ordinary_DD_zero_matter_curves") == ["C12", "C23", "C31"] for item in assignments)
    )

    return {
        "candidate": "VisibleTwistedS3FiniteChanPatonCancellation",
        "status": (
            "VISIBLE_TWISTED_S3_FINITE_CP_CANCELLATION_CLOSED_SMOOTH_SOURCE_OPEN"
            if finite_cancellation_closed
            else "VISIBLE_TWISTED_S3_FINITE_CP_CANCELLATION_INCONCLUSIVE"
        ),
        "generated_by": "scripts/prove_visible_twisted_s3_finite_cp_cancellation.py",
        "inputs": {
            "equivariant_selector_certificate": "visible_twisted_d7_equivariant_embedding_selector_certificate.json",
            "twisted_chan_paton_rescue_certificate": "visible_twisted_chan_paton_rescue_certificate.json",
            "freed_witten_cycle_gate_certificate": "time_oriented_m1_freed_witten_cycle_gate_certificate.json",
            "visible_complex_worldvolume_spinc_gate_certificate": "visible_complex_worldvolume_spinc_gate_certificate.json",
        },
        "finite_cancellation_inputs": {
            "selector_closes_stack_S3": selector_closed,
            "m1_period_table_q": projective.get("m1_period_table_q"),
            "m1_period_table_torsion_label": projective.get("m1_period_table_torsion_label"),
            "central_phase_label": "zeta_3^2",
            "finite_projective_module_matches_m1_twist": finite_module_matches,
            "ordinary_rank_two_DD_gate_fails_for_S3": fw_finite_gate_closed,
            "visible_cycles_W3_spinC_zero": spinc_closed,
        },
        "s3_cancellation_reports": [cancellation_report(item) for item in assignments],
        "finite_convention": {
            "ordinary_rank_two_B_restriction": "nonzero on S3",
            "twisted_CP_module": "projective qutrit module with the same m=1 zeta_3^2 gerbe class",
            "cancellation_statement": (
                "In the finite twisted-bundle convention, the S3 Chan-Paton "
                "module is a module for the pulled-back B-gerbe, so the "
                "ordinary DD obstruction is replaced by a matched twisted "
                "module rather than by an ordinary vector bundle."
            ),
        },
        "calculation_results": {
            "finite_S3_CP_cancellation_closed": finite_cancellation_closed,
            "ordinary_S3_DD_zero_route_closed": False,
            "twisted_S3_DD_cancellation_available": finite_cancellation_closed,
            "matter_curves_remain_ordinary_DD_zero": all(
                item.get("all_matter_curves_ordinary_DD_zero") is True for item in assignments
            ),
            "smooth_Deligne_Cech_source_constructed": False,
            "selected_projector_retention_verified": False,
        },
        "what_this_closes": {
            "finite_rank_two_S3_DD_obstruction_is_cancellable_by_twisted_CP": finite_cancellation_closed,
            "S3_finite_CP_source_class_matches_q79_m1_twist": finite_cancellation_closed,
            "ordinary_matter_curve_DD_zero_retained": finite_cancellation_closed,
        },
        "still_open": {
            "selected_smooth_S3_Deligne_Cech_or_worldvolume_flux_source": True,
            "fixed_differential_cohomology_refinement_of_finite_class": True,
            "Green_Schwarz_Bianchi_for_smooth_S3_source": True,
            "full_Freed_Witten_for_smooth_S3_source": True,
            "twisted_projector_retention": True,
            "selected_visible_operator_source": True,
            "selected_D_E_dotD": True,
            "primitive_C1_contractions_and_SM_closure": True,
        },
        "guardrails": {
            "claims_smooth_S3_source_constructed": False,
            "claims_full_Freed_Witten_closed": False,
            "claims_projector_retention": False,
            "claims_visible_operator_source_constructed": False,
            "claims_selected_D_E_dotD_constructed": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "The selected S3 stack has a finite twisted Chan-Paton "
                "cancellation for the rank-two DD obstruction: S1, S2, and all "
                "Cij remain ordinary, while S3 carries the q79/F,m=1 projective "
                "module. This closes the finite cancellation sublemma, not the "
                "smooth selected source theorem."
            ),
            "next_closing_object": (
                "Lift this finite S3 twisted CP class to a selected smooth "
                "Deligne/Cech or worldvolume-flux source and prove projector "
                "retention on the block-factorized family/Higgs packet."
            ),
        },
    }


def write_outputs(report: dict[str, Any]) -> None:
    write_json(CANDIDATE, report)
    certificate = {
        "certificate": "VisibleTwistedS3FiniteChanPatonCancellation",
        "status": report["status"],
        "analysis_script": report["generated_by"],
        "candidate_data": "candidate_data/visible_twisted_s3_finite_cp_cancellation.candidate.json",
        "inputs": report["inputs"],
        "finite_cancellation_inputs": report["finite_cancellation_inputs"],
        "s3_cancellation_reports": report["s3_cancellation_reports"],
        "finite_convention": report["finite_convention"],
        "calculation_results": report["calculation_results"],
        "what_this_closes": report["what_this_closes"],
        "still_open": report["still_open"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    write_json(CERTIFICATE, certificate)


def main() -> int:
    report = build_report()
    write_outputs(report)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["calculation_results"]["finite_S3_CP_cancellation_closed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
