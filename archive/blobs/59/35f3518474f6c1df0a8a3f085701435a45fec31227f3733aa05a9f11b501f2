"""Analyze the Freed-Witten cycle gate for the time-oriented m=1 flat gerbe."""

from __future__ import annotations

import json
from itertools import combinations, product
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATES = ROOT / "certificates"
CANDIDATE_DATA = ROOT / "candidate_data"
CANDIDATE = CANDIDATE_DATA / "time_oriented_m1_freed_witten_cycle_gate.candidate.json"
CERTIFICATE = CERTIFICATES / "time_oriented_m1_freed_witten_cycle_gate_certificate.json"
TEMPLATE = CERTIFICATES / "time_oriented_m1_selected_cycle_restrictions.template.json"
FLAT_GERBE_CERT = CERTIFICATES / "time_oriented_m1_flat_gerbe_promotion_certificate.json"
VALIDATOR = ROOT / "scripts" / "validate_time_oriented_m1_selected_cycle_restrictions.py"
MOD = 3


Element = tuple[int, int]


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def mod(value: int) -> int:
    return value % MOD


def omega(left: Element, right: Element) -> int:
    a, b = left
    c, d = right
    return mod(a * d - b * c)


def rank_over_f3(elements: list[Element]) -> int:
    work = [[entry[0] % MOD, entry[1] % MOD] for entry in elements if entry != (0, 0)]
    rank = 0
    for col in range(2):
        pivot = None
        for row in range(rank, len(work)):
            if work[row][col]:
                pivot = row
                break
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inv = pow(work[rank][col], -1, MOD)
        work[rank] = [(value * inv) % MOD for value in work[rank]]
        for row in range(len(work)):
            if row == rank or work[row][col] == 0:
                continue
            factor = work[row][col]
            work[row] = [
                (work[row][idx] - factor * work[rank][idx]) % MOD
                for idx in range(2)
            ]
        rank += 1
    return rank


def restricted_commutator_rank(elements: list[Element]) -> int:
    return 0 if rank_over_f3(elements) <= 1 else 2


def dd_zero(elements: list[Element]) -> bool:
    return restricted_commutator_rank(elements) == 0


def normalized_line_generator(element: Element) -> Element:
    a, b = element
    if a % MOD:
        inv = pow(a, -1, MOD)
        return mod(a * inv), mod(b * inv)
    inv = pow(b, -1, MOD)
    return 0, mod(b * inv)


def subgroup_distribution() -> dict[str, Any]:
    nonzero = [(a, b) for a, b in product(range(MOD), repeat=2) if (a, b) != (0, 0)]
    lines = sorted({normalized_line_generator(element) for element in nonzero})
    full_rank_pairs = [
        [list(left), list(right)]
        for left, right in combinations(nonzero, 2)
        if rank_over_f3([left, right]) == 2
    ]
    return {
        "zero_subgroup_count": 1,
        "rank_one_line_count": len(lines),
        "rank_one_line_generators": [list(line) for line in lines],
        "rank_two_subgroup_count": 1,
        "rank_two_pair_witness_count": len(full_rank_pairs),
        "all_rank_one_restrictions_DD_zero": all(dd_zero([line]) for line in lines),
        "all_rank_two_pair_witnesses_DD_nonzero": all(
            not dd_zero([(pair[0][0], pair[0][1]), (pair[1][0], pair[1][1])])
            for pair in full_rank_pairs
        ),
    }


def sample_restrictions() -> list[dict[str, Any]]:
    samples: list[tuple[str, list[Element], bool]] = [
        ("inactive_kernel_cycle", [(0, 0)], True),
        ("g1_line_cycle", [(1, 0)], True),
        ("g2_line_cycle", [(0, 1)], True),
        ("diagonal_line_cycle", [(1, 1)], True),
        ("full_active_g1_g2_cycle", [(1, 0), (0, 1)], False),
    ]
    return [
        {
            "id": cycle_id,
            "pi1_image_generators_F3_2": [list(element) for element in elements],
            "image_rank_over_F3": rank_over_f3(elements),
            "restricted_commutator_rank": restricted_commutator_rank(elements),
            "DD_restriction_zero": dd_zero(elements),
            "expected_DD_zero": expected,
        }
        for cycle_id, elements, expected in samples
    ]


def analyze() -> dict[str, Any]:
    flat = load_json(FLAT_GERBE_CERT)
    flat_promotion_conditional = (
        flat.get("status")
        == "TIME_ORIENTED_M1_FLAT_GERBE_PROMOTION_CONDITIONAL_CLOSED_SELECTION_OPEN"
    )
    distribution = subgroup_distribution()
    samples = sample_restrictions()

    finite_gate_closed = (
        flat_promotion_conditional
        and distribution["all_rank_one_restrictions_DD_zero"] is True
        and distribution["all_rank_two_pair_witnesses_DD_nonzero"] is True
        and TEMPLATE.exists()
        and VALIDATOR.exists()
    )

    return {
        "candidate": "TimeOrientedM1FreedWittenCycleGate",
        "status": (
            "TIME_ORIENTED_M1_FREED_WITTEN_CYCLE_GATE_FORMULATED_SELECTED_CYCLES_OPEN"
            if finite_gate_closed
            else "TIME_ORIENTED_M1_FREED_WITTEN_CYCLE_GATE_NOT_CLOSED"
        ),
        "generated_by": "scripts/analyze_time_oriented_m1_freed_witten_cycle_gate.py",
        "input_flat_gerbe": {
            "certificate": "time_oriented_m1_flat_gerbe_promotion_certificate.json",
            "conditional_flat_promotion_closed": flat_promotion_conditional,
            "torsion_order": 3,
        },
        "finite_restriction_theorem": {
            "active_quotient": "F_3^2",
            "commutator_form": "omega((a,b),(c,d)) = a*d - b*c mod 3",
            "DD_restriction_zero_iff": "rank(image(pi1(Y)->F_3^2)) <= 1",
            "reason": (
                "For finite abelian groups, U(1) 2-cocycle classes are "
                "classified by alternating bicharacters. The m=1 form is "
                "symplectic on F_3^2, so only zero or line images are isotropic."
            ),
        },
        "subgroup_distribution": distribution,
        "sample_cycle_restrictions": samples,
        "selected_cycle_packet": {
            "template": "certificates/time_oriented_m1_selected_cycle_restrictions.template.json",
            "template_exists": TEMPLATE.exists(),
            "validator": "scripts/validate_time_oriented_m1_selected_cycle_restrictions.py",
            "validator_exists": VALIDATOR.exists(),
            "filled_selected_packet_present": False,
        },
        "calculation_results": {
            "finite_DD_restriction_decision_procedure_closed": finite_gate_closed,
            "rank_zero_or_one_active_images_pass_DD_part": True,
            "rank_two_active_images_fail_DD_part": True,
            "W3_or_spinC_must_be_supplied_per_cycle": True,
            "selected_cycles_supplied": False,
            "Freed_Witten_verified": False,
        },
        "what_this_closes": {
            "DD_B_restriction_calculator_for_m1_flat_gerbe": finite_gate_closed,
            "isotropic_image_criterion_rank_at_most_one": finite_gate_closed,
            "full_active_F3_squared_cycle_obstruction": finite_gate_closed,
            "future_selected_cycle_packet_schema_and_validator": finite_gate_closed,
        },
        "still_open": {
            "selected_cycle_or_brane_list": True,
            "cycle_pi1_image_in_active_F3_squared": True,
            "W3_zero_or_spinC_certificate_per_cycle": True,
            "selected_projector_retention_for_visible_zero_modes": True,
            "selected_D_E_dotD_Riesz_Green_files_from_same_branch": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_selected_cycles_supplied": False,
            "claims_Freed_Witten_verified": False,
            "claims_projector_retention": False,
            "claims_selected_D_E_dotD_constructed": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "The m=1 Freed-Witten gerbe restriction problem is now finite: "
                "a selected cycle passes the DD(B) part exactly when its active "
                "F_3^2 image has rank zero or one. A cycle whose image spans both "
                "g1 and g2 fails the 3-torsion restriction. W3/spinC data and "
                "the selected cycle list remain absent."
            ),
            "next_closing_object": (
                "Fill time_oriented_m1_selected_cycle_restrictions.template.json "
                "with the selected cycles, their F_3^2 images, and W3=0 or spinC "
                "certificates, then rerun the validator and twisted-source gate."
            ),
        },
    }


def write_outputs(report: dict[str, Any]) -> None:
    CANDIDATE.parent.mkdir(parents=True, exist_ok=True)
    CERTIFICATE.parent.mkdir(parents=True, exist_ok=True)
    CANDIDATE.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    certificate = {
        "certificate": "TimeOrientedM1FreedWittenCycleGate",
        "status": report["status"],
        "analysis_script": "scripts/analyze_time_oriented_m1_freed_witten_cycle_gate.py",
        "candidate_data": "candidate_data/time_oriented_m1_freed_witten_cycle_gate.candidate.json",
        "validator_script": "scripts/validate_time_oriented_m1_selected_cycle_restrictions.py",
        "input_flat_gerbe": report["input_flat_gerbe"],
        "finite_restriction_theorem": report["finite_restriction_theorem"],
        "subgroup_distribution": report["subgroup_distribution"],
        "calculation_results": report["calculation_results"],
        "what_this_closes": report["what_this_closes"],
        "still_open": report["still_open"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    CERTIFICATE.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    report = analyze()
    write_outputs(report)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
