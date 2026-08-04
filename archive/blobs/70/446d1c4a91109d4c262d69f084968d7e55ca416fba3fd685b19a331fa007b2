"""Analyze the finite twisted Chan-Paton rescue for visible coordinate divisors.

The previous obstruction showed that the literal coordinate D7 stack cannot
pass the *ordinary* m=1 DD(B)|Y=0 gate for all S1,S2,S3.  This script asks a
more refined question:

Can the coordinate model be rescued, at finite quotient level, by letting the
rank-two pullback divisor carry the already validated qutrit projective
Chan-Paton module?

The answer is conditional and precise.  If the two active generators are placed
in distinct coordinate factors, then all three matter curves Cij have
rank <= 1 active image, and exactly one D7 divisor has rank-two active image.
The existing qutrit projective carrier supplies a full-F_3^2 projective module
with the same zeta_3^2 central twist as the time-oriented m=1 period table.
Thus the finite algebraic rescue reduces to choosing which one D7 stack carries
the twisted projective module.  Selection, geometry, HYM/source promotion,
projector retention, and D_E/dotD remain open.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OBSTRUCTION_CERT = ROOT / "certificates" / "visible_active_f3_image_recovery_obstruction_certificate.json"
PROJECTIVE_CARRIER_CERT = ROOT / "certificates" / "iwasawa_projective_magnetic_carrier_certificate.json"
PROJECTIVE_CARRIER = ROOT / "candidate_data" / "iwasawa_projective_magnetic_carrier.meshN1.json"
PROJECTIVE_VALIDATOR = ROOT / "scripts" / "validate_iwasawa_projective_rhoE_mesh.py"
M1_PERIOD_CERT = ROOT / "certificates" / "time_oriented_m1_gerbe_period_table_certificate.json"
OUT_CANDIDATE = ROOT / "candidate_data" / "visible_twisted_chan_paton_rescue.candidate.json"
OUT_CERT = ROOT / "certificates" / "visible_twisted_chan_paton_rescue_certificate.json"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def run_projective_validator() -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(PROJECTIVE_VALIDATOR), str(PROJECTIVE_CARRIER)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return {
        "exit": proc.returncode,
        "output_head": proc.stdout.splitlines()[:8],
    }


def split_assignment_report(assignment: dict[str, Any]) -> dict[str, Any]:
    worldvolumes = assignment["worldvolumes"]
    d7_divisors = [item for item in worldvolumes if item["id"].startswith("S")]
    curves = [item for item in worldvolumes if item["id"].startswith("C")]
    twisted_d7 = [item for item in d7_divisors if item["image_rank_over_F3"] == 2]
    ordinary_d7 = [item for item in d7_divisors if item["image_rank_over_F3"] <= 1]
    ordinary_curves = [item for item in curves if item["image_rank_over_F3"] <= 1]
    return {
        "generator_factor_assignment": assignment["generator_factor_assignment"],
        "twisted_projective_D7_stack_required": twisted_d7[0]["id"] if len(twisted_d7) == 1 else None,
        "ordinary_DD_zero_D7_stacks": [item["id"] for item in ordinary_d7],
        "ordinary_DD_zero_matter_curves": [item["id"] for item in ordinary_curves],
        "all_matter_curves_ordinary_DD_zero": len(ordinary_curves) == len(curves),
        "exactly_one_twisted_D7": len(twisted_d7) == 1,
        "rank_two_curve_count": sum(1 for item in curves if item["image_rank_over_F3"] == 2),
    }


def build_certificate() -> dict[str, Any]:
    obstruction = load_json(OBSTRUCTION_CERT)
    carrier_cert = load_json(PROJECTIVE_CARRIER_CERT)
    period_cert = load_json(M1_PERIOD_CERT)
    validator = run_projective_validator()

    assignments = obstruction.get("enumeration", {}).get("all_assignments", [])
    split_assignments = [
        item
        for item in assignments
        if item.get("generator_factor_assignment", {}).get("e1")
        != item.get("generator_factor_assignment", {}).get("e2")
    ]
    rescue_reports = [split_assignment_report(item) for item in split_assignments]
    minimal_rescue_reports = [
        item
        for item in rescue_reports
        if item["exactly_one_twisted_D7"]
        and item["all_matter_curves_ordinary_DD_zero"]
        and item["rank_two_curve_count"] == 0
    ]
    twisted_stack_choices = sorted(
        {item["twisted_projective_D7_stack_required"] for item in minimal_rescue_reports}
    )

    carrier_histogram = (
        carrier_cert.get("mesh_N1_diagnostic", {}).get("central_phase_histogram", {})
    )
    finite_projective_module_matches_m1 = (
        carrier_cert.get("mesh_N1_diagnostic", {}).get("projective_gerbe_gluing_passes")
        is True
        and carrier_cert.get("mesh_N1_diagnostic", {}).get("strict_vector_bundle_gluing_passes")
        is False
        and carrier_histogram.get("omega^2", 0) > 0
        and period_cert.get("selected_branch", {}).get("torsion_label_m") == 1
        and period_cert.get("selected_branch", {}).get("q") == 79
        and period_cert.get("calculation_results", {}).get("commutator_matrix_matches_qutrit_F_orientation")
        is True
        and validator["exit"] == 0
    )

    finite_rescue_family_closed = (
        obstruction.get("status")
        == "VISIBLE_ACTIVE_F3_IMAGE_RECOVERY_NAIVE_COORDINATE_ROUTE_BLOCKED"
        and len(minimal_rescue_reports) == 6
        and twisted_stack_choices == ["S1", "S2", "S3"]
        and finite_projective_module_matches_m1
    )

    status = (
        "VISIBLE_TWISTED_CP_MINIMAL_COORDINATE_RESCUE_REDUCED_SELECTION_OPEN"
        if finite_rescue_family_closed
        else "VISIBLE_TWISTED_CP_RESCUE_INCONCLUSIVE"
    )

    return {
        "certificate": "VisibleTwistedChanPatonRescue",
        "status": status,
        "generated_by": "scripts/analyze_visible_twisted_chan_paton_rescue.py",
        "depends_on": [
            str(OBSTRUCTION_CERT.relative_to(ROOT)),
            str(PROJECTIVE_CARRIER_CERT.relative_to(ROOT)),
            str(M1_PERIOD_CERT.relative_to(ROOT)),
        ],
        "projective_module_check": {
            "validator": validator,
            "carrier_projective_gluing_passes": carrier_cert.get("mesh_N1_diagnostic", {}).get(
                "projective_gerbe_gluing_passes"
            ),
            "carrier_strict_vector_bundle_gluing_passes": carrier_cert.get(
                "mesh_N1_diagnostic", {}
            ).get("strict_vector_bundle_gluing_passes"),
            "carrier_central_phase_histogram": carrier_histogram,
            "m1_period_table_q": period_cert.get("selected_branch", {}).get("q"),
            "m1_period_table_torsion_label": period_cert.get("selected_branch", {}).get(
                "torsion_label_m"
            ),
            "m1_commutator_matches_qutrit_F": period_cert.get("calculation_results", {}).get(
                "commutator_matrix_matches_qutrit_F_orientation"
            ),
            "finite_projective_module_matches_m1_twist": finite_projective_module_matches_m1,
        },
        "coordinate_rescue_enumeration": {
            "split_active_direction_assignments": len(split_assignments),
            "minimal_rescue_assignment_count": len(minimal_rescue_reports),
            "minimal_rescue_assignments": minimal_rescue_reports,
            "twisted_D7_stack_choices": twisted_stack_choices,
            "interpretation": "one D7 divisor carries the projective qutrit Chan-Paton module; the other two D7 divisors and all three matter curves remain ordinary/isotropic",
        },
        "finite_extended_rule": {
            "rank_0_or_1_image": "ordinary DD(B)|Y=0 gate",
            "rank_2_D7_image": "conditional projective Chan-Paton module with matching m=1 zeta3 twist",
            "rank_2_matter_curve_image": "not accepted in the minimal rescue family",
        },
        "what_this_closes": {
            "finite_algebraic_twisted_CP_rescue_family_exists": finite_rescue_family_closed,
            "coordinate_model_not_forced_to_noncoordinate_if_twisted_CP_allowed": finite_rescue_family_closed,
            "minimal_coordinate_rescue_reduced_to_one_twisted_D7_choice": finite_rescue_family_closed,
        },
        "still_open": {
            "selected_choice_of_twisted_D7_stack_S1_or_S2_or_S3": True,
            "geometric_Deligne_Cech_or_B_field_representative_on_that_stack": True,
            "physical_worldvolume_flux_or_twisted_Chan_Paton_source_certificate": True,
            "HYM_or_Route_C_selected_visible_operator_source": True,
            "projector_retention_D_E_dotD_Riesz_Green": True,
            "primitive_C1_contractions_and_SM_closure": True,
        },
        "guardrails": {
            "claims_complete_Freed_Witten_closed": False,
            "claims_twisted_CP_selected_by_MTT": False,
            "claims_visible_operator_source_constructed": False,
            "claims_projector_retention": False,
            "claims_selected_D_E_dotD_constructed": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": "The ordinary zero-DD coordinate D7 route is blocked, but a finite twisted Chan-Paton rescue is algebraically available: for the six split active-direction assignments, all matter curves remain DD-zero and exactly one D7 stack sees the full F3^2 plane. The existing qutrit projective carrier supplies the matching zeta3 twist for that full-plane stack.",
            "next_closing_object": "Select which D7 stack carries the twisted projective module and promote it to a geometric Deligne/Cech or worldvolume-flux/Chan-Paton source with HYM/operator-source, projector-retention, and D_E/dotD evidence.",
        },
    }


def main() -> int:
    data = build_certificate()
    write_json(OUT_CANDIDATE, data)
    write_json(OUT_CERT, data)
    print(json.dumps(data, indent=2, sort_keys=True))
    return 0 if data["status"] != "VISIBLE_TWISTED_CP_RESCUE_INCONCLUSIVE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
