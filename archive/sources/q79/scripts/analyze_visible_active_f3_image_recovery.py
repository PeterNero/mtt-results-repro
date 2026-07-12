"""Analyze whether the CY-corner visible divisors determine active F_3^2 images.

This is an honest next-step calculation after the visible complex-worldvolume
spinC gate.  It tests the most literal factorized-coordinate interpretation:

    X6 = T1 x T2 x T3,
    S1 = T2 x T3, S2 = T1 x T3, S3 = T1 x T2,
    C12 = T3, C23 = T1, C31 = T2.

The m=1 Freed-Witten DD(B) gate says every selected visible worldvolume must
have active F_3^2 image rank at most one.  If the two independent active
qutrit generators are assigned as tangent coordinate directions of the
factorized corner, at least one coordinate divisor always contains both
generators.  Therefore the naive coordinate-divisor interpretation cannot be
the complete selected visible worldvolume packet.
"""

from __future__ import annotations

import json
from itertools import product
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
EXEC_I = ROOT / "proof_corpus" / "Execution_of_Modal_Triplet_Theory_I__Gauge__Axion__and_Threshold_Sectors_v2.md"
EXEC_II = ROOT / "proof_corpus" / "Execution_of_Modal_Triplet_Theory_II__Flavor__CKM_PMNS__and_Higgs_Sector_on_the_CY_Corner_v2.md"
SPINC_CERT = ROOT / "certificates" / "visible_complex_worldvolume_spinc_gate_certificate.json"
FW_GATE_CERT = ROOT / "certificates" / "time_oriented_m1_freed_witten_cycle_gate_certificate.json"
OUT_CANDIDATE = ROOT / "candidate_data" / "visible_active_f3_image_recovery_obstruction.candidate.json"
OUT_CERT = ROOT / "certificates" / "visible_active_f3_image_recovery_obstruction_certificate.json"


Element = tuple[int, int]
FACTOR_IDS = ("T1", "T2", "T3")
GENERATORS: dict[str, Element] = {"e1": (1, 0), "e2": (0, 1)}
WORLDVOLUMES: dict[str, tuple[str, ...]] = {
    "S1": ("T2", "T3"),
    "S2": ("T1", "T3"),
    "S3": ("T1", "T2"),
    "C12": ("T3",),
    "C23": ("T1",),
    "C31": ("T2",),
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def rank_over_f3(elements: list[Element]) -> int:
    work = [[entry[0] % 3, entry[1] % 3] for entry in elements if entry != (0, 0)]
    rank = 0
    for col in range(2):
        pivot = None
        for row in range(rank, len(work)):
            if work[row][col] % 3:
                pivot = row
                break
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inv = pow(work[rank][col], -1, 3)
        work[rank] = [(value * inv) % 3 for value in work[rank]]
        for row in range(len(work)):
            if row == rank or work[row][col] == 0:
                continue
            factor = work[row][col]
            work[row] = [
                (work[row][idx] - factor * work[rank][idx]) % 3
                for idx in range(2)
            ]
        rank += 1
    return rank


def source_hits() -> dict[str, dict[str, bool]]:
    text_i = read(EXEC_I)
    text_ii = read(EXEC_II)
    return {
        "execution_i": {
            "factorized_corner": "factorized three--modulus corner" in text_i,
            "coordinate_divisors": "S_1,\\; S_2,\\; S_3" in text_i,
            "divisor_volumes": "Vol}(S_1)=t_2 t_3" in text_i
            and "Vol}(S_2)=t_1 t_3" in text_i
            and "Vol}(S_3)=t_1 t_2" in text_i,
            "intersection_number": "\\kappa_{123}=1" in text_i or "\\kappa_{123} = 1" in text_i,
        },
        "execution_ii": {
            "matter_curves": "C_{ij} = S_i \\cap S_j" in text_ii,
            "triple_intersections": "Yukawa couplings arise from triple intersections" in text_ii,
        },
    }


def assignment_report(e1_factor: str, e2_factor: str) -> dict[str, Any]:
    generator_factor = {"e1": e1_factor, "e2": e2_factor}
    worldvolume_reports = []
    for worldvolume, factors in WORLDVOLUMES.items():
        gens = [
            GENERATORS[name]
            for name, factor in generator_factor.items()
            if factor in factors
        ]
        rank = rank_over_f3(gens)
        worldvolume_reports.append(
            {
                "id": worldvolume,
                "coordinate_factors": list(factors),
                "active_generators_seen": [
                    name for name, factor in generator_factor.items() if factor in factors
                ],
                "image_rank_over_F3": rank,
                "DD_B_zero_under_m1_gate": rank <= 1,
            }
        )
    divisors = [item for item in worldvolume_reports if item["id"].startswith("S")]
    curves = [item for item in worldvolume_reports if item["id"].startswith("C")]
    return {
        "generator_factor_assignment": generator_factor,
        "worldvolumes": worldvolume_reports,
        "all_three_coordinate_divisors_DD_zero": all(
            item["DD_B_zero_under_m1_gate"] for item in divisors
        ),
        "all_three_coordinate_curves_DD_zero": all(
            item["DD_B_zero_under_m1_gate"] for item in curves
        ),
        "failing_divisors": [
            item["id"] for item in divisors if not item["DD_B_zero_under_m1_gate"]
        ],
        "failing_curves": [
            item["id"] for item in curves if not item["DD_B_zero_under_m1_gate"]
        ],
    }


def build_certificate() -> dict[str, Any]:
    hits = source_hits()
    spin_cert = load_json(SPINC_CERT)
    fw_cert = load_json(FW_GATE_CERT)
    assignments = [
        assignment_report(e1_factor, e2_factor)
        for e1_factor, e2_factor in product(FACTOR_IDS, repeat=2)
    ]
    divisor_pass_count = sum(
        1 for item in assignments if item["all_three_coordinate_divisors_DD_zero"]
    )
    best_failing_divisor_count = min(len(item["failing_divisors"]) for item in assignments)
    split_assignments_with_curve_pass = [
        item
        for item in assignments
        if item["generator_factor_assignment"]["e1"]
        != item["generator_factor_assignment"]["e2"]
        and item["all_three_coordinate_curves_DD_zero"]
    ]
    corpus_names_factorized_coordinate_stack = all(
        all(section.values()) for section in hits.values()
    )
    m1_gate_rank_rule_present = (
        fw_cert.get("status")
        == "TIME_ORIENTED_M1_FREED_WITTEN_CYCLE_GATE_FORMULATED_SELECTED_CYCLES_OPEN"
    )
    spin_gate_closed = (
        spin_cert.get("status")
        == "VISIBLE_COMPLEX_WORLDVOLUME_SPINC_W3_CLOSED_DD_IMAGES_OPEN"
    )
    naive_route_blocked = (
        corpus_names_factorized_coordinate_stack
        and m1_gate_rank_rule_present
        and spin_gate_closed
        and divisor_pass_count == 0
    )
    status = (
        "VISIBLE_ACTIVE_F3_IMAGE_RECOVERY_NAIVE_COORDINATE_ROUTE_BLOCKED"
        if naive_route_blocked
        else "VISIBLE_ACTIVE_F3_IMAGE_RECOVERY_INCONCLUSIVE"
    )
    return {
        "certificate": "VisibleActiveF3ImageRecoveryObstruction",
        "status": status,
        "generated_by": "scripts/analyze_visible_active_f3_image_recovery.py",
        "depends_on": [
            str(SPINC_CERT.relative_to(ROOT)),
            str(FW_GATE_CERT.relative_to(ROOT)),
        ],
        "source_hits": hits,
        "factorized_coordinate_model": {
            "ambient": "T1 x T2 x T3 factorized CY corner",
            "coordinate_divisors": {
                "S1": ["T2", "T3"],
                "S2": ["T1", "T3"],
                "S3": ["T1", "T2"],
            },
            "matter_curves": {
                "C12": ["T3"],
                "C23": ["T1"],
                "C31": ["T2"],
            },
            "active_quotient": "rank-two symplectic F3^2 with basis e1,e2",
        },
        "enumeration": {
            "coordinate_tangent_assignment_count": len(assignments),
            "all_assignments": assignments,
            "assignments_with_all_divisors_DD_zero": divisor_pass_count,
            "best_failing_divisor_count": best_failing_divisor_count,
            "split_assignments_with_all_curves_DD_zero": len(split_assignments_with_curve_pass),
        },
        "theorem": {
            "statement": "In the literal factorized coordinate-divisor model, no assignment of the two independent active F3^2 generators to coordinate tangent factors makes all three D7 divisors S1,S2,S3 isotropic.",
            "proof": [
                "If e1 and e2 lie in the same coordinate factor Tk, then either of the two divisors not excluding Tk contains both generators and has rank-two active image.",
                "If e1 and e2 lie in two distinct coordinate factors Ti,Tj, then the remaining divisor S_k contains both generators and has rank-two active image.",
                "The m=1 DD(B) gate requires rank at most one for every selected worldvolume; hence the naive coordinate-divisor packet cannot pass.",
            ],
        },
        "guardrails": {
            "claims_actual_visible_active_images_recovered": False,
            "claims_complete_Freed_Witten_closed": False,
            "claims_all_geometric_embeddings_blocked": False,
            "claims_selected_visible_operator_source": False,
            "claims_projector_retention": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "what_this_closes": {
            "naive_coordinate_divisor_active_image_route": naive_route_blocked,
            "reason_active_images_are_still_needed": True,
        },
        "still_open": {
            "actual_selected_active_F3_squared_images_for_S1_S2_S3_Cij": True,
            "possible_noncoordinate_or_isotropic_visible_worldvolume_packet": True,
            "possible_B_field_normal_or_trivial_pullback_placement": True,
            "possible_twisted_Chan_Paton_or_flux_cancellation_schema": True,
            "selected_visible_operator_source": True,
            "projector_retention_D_E_dotD_C1": True,
        },
        "verdict": {
            "honest_answer": "The corpus gives coordinate-looking D7 divisors and matter curves, but it does not give the active F3^2 image map. The most literal coordinate-tangent map is mathematically blocked: at least one D7 divisor always sees the full rank-two active plane, so DD(B)|S is nonzero under the current m=1 gate.",
            "correct_way_forward": "Do not fill the complete visible packet with naive coordinate divisors. Recover or construct a selected active-image map in which every visible worldvolume has isotropic rank <=1 pullback, or extend the proof with an explicit twisted Chan-Paton/flux cancellation certificate.",
        },
    }


def main() -> int:
    data = build_certificate()
    write_json(OUT_CANDIDATE, data)
    write_json(OUT_CERT, data)
    print(json.dumps(data, indent=2, sort_keys=True))
    return 0 if data["status"] != "VISIBLE_ACTIVE_F3_IMAGE_RECOVERY_INCONCLUSIVE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
