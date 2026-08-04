"""Validate selected cycle restrictions for the time-oriented m=1 flat gerbe.

The m=1 flat gerbe is represented on the active quotient F_3^2 by the
alternating commutator form

    omega((a,b),(c,d)) = a*d - b*c  mod 3.

For finite abelian groups, the U(1) 2-cocycle class is determined by this
alternating bicharacter.  Therefore its restriction to a selected cycle is
trivial exactly when the cycle's image in F_3^2 is isotropic.  Since F_3^2 is
two-dimensional symplectic, this is equivalent to image rank <= 1.

Exit codes:
  0: selected cycle packet verifies DD(B)|Y=0 and W3(Y)=0 for every cycle
  1: complete packet fails a mathematical/schema check
  2: packet is incomplete/open rather than mathematically failed
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


SCHEMA = "TimeOrientedM1SelectedCycleRestrictions.v1"
EXPECTED_FLAT_GERBE_CERT = "time_oriented_m1_flat_gerbe_promotion_certificate.json"
MOD = 3


class IncompleteData(ValueError):
    """Raised when the selected-cycle packet is still open."""


Element = tuple[int, int]


def mod(value: int) -> int:
    return value % MOD


def parse_element(value: Any) -> Element:
    if not isinstance(value, list) or len(value) != 2:
        raise ValueError(f"cycle image generator must be a two-entry list, got {value!r}")
    return mod(int(value[0])), mod(int(value[1]))


def rank_over_f3(elements: list[Element]) -> int:
    work = [[entry[0] % MOD, entry[1] % MOD] for entry in elements if entry != (0, 0)]
    rank = 0
    for col in range(2):
        pivot = None
        for row in range(rank, len(work)):
            if work[row][col] % MOD:
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


def omega(left: Element, right: Element) -> int:
    a, b = left
    c, d = right
    return mod(a * d - b * c)


def restricted_commutator_rank(elements: list[Element]) -> int:
    span_rank = rank_over_f3(elements)
    if span_rank <= 1:
        return 0
    # Any rank-two subspace of F_3^2 is all of F_3^2.  The symplectic form is
    # nondegenerate on the whole active quotient.
    return 2


def validate_cycle(cycle: dict[str, Any]) -> tuple[list[str], dict[str, Any]]:
    failures: list[str] = []
    cycle_id = cycle.get("id")
    if not isinstance(cycle_id, str) or not cycle_id:
        failures.append("cycle id must be a nonempty string")

    if cycle.get("selected_by_mtt") is not True:
        failures.append(f"{cycle_id}: selected_by_mtt must be true")

    raw_generators = cycle.get("pi1_image_generators_F3_2")
    if not isinstance(raw_generators, list):
        raise IncompleteData(f"{cycle_id}: MISSING pi1_image_generators_F3_2")
    generators = [parse_element(value) for value in raw_generators]
    image_rank = rank_over_f3(generators)
    commutator_rank = restricted_commutator_rank(generators)
    dd_restriction_zero = commutator_rank == 0

    if cycle.get("dd_restriction_zero_claim") is not dd_restriction_zero:
        failures.append(
            f"{cycle_id}: dd_restriction_zero_claim does not match computed value "
            f"{dd_restriction_zero}"
        )
    if not dd_restriction_zero:
        failures.append(f"{cycle_id}: DD(B)|Y is nonzero on the active F_3^2 image")

    w3_zero = cycle.get("W3_zero") is True
    spin_c_verified = cycle.get("spinC_verified") is True
    if not (w3_zero or spin_c_verified):
        failures.append(f"{cycle_id}: W3_zero or spinC_verified must be true")

    return failures, {
        "id": cycle_id,
        "image_rank_over_F3": image_rank,
        "restricted_commutator_rank": commutator_rank,
        "dd_restriction_zero": dd_restriction_zero,
        "W3_zero_or_spinC_verified": w3_zero or spin_c_verified,
    }


def validate_packet(data: dict[str, Any]) -> tuple[list[str], dict[str, Any]]:
    if data.get("status") == "OPEN":
        raise IncompleteData("selected cycle restriction packet is OPEN")
    if data.get("schema") != SCHEMA:
        raise ValueError(f"schema must be {SCHEMA}")
    if data.get("flat_gerbe_certificate") != EXPECTED_FLAT_GERBE_CERT:
        raise ValueError(
            f"flat_gerbe_certificate must be {EXPECTED_FLAT_GERBE_CERT}"
        )
    if data.get("selected_by_mtt") is not True:
        return ["selected_by_mtt must be true"], {}
    if data.get("uses_observed_flavor_data") is not False:
        return ["uses_observed_flavor_data must be false"], {}
    if data.get("uses_benchmark_flavor_entries") is not False:
        return ["uses_benchmark_flavor_entries must be false"], {}

    cycles = data.get("cycles")
    if not isinstance(cycles, list) or not cycles:
        raise IncompleteData("MISSING nonempty cycles list")

    failures: list[str] = []
    cycle_reports = []
    for cycle in cycles:
        if not isinstance(cycle, dict):
            raise ValueError(f"cycle must be an object, got {cycle!r}")
        cycle_failures, report = validate_cycle(cycle)
        failures.extend(cycle_failures)
        cycle_reports.append(report)

    return failures, {
        "schema": data.get("schema"),
        "cycle_count": len(cycles),
        "cycle_reports": cycle_reports,
        "all_dd_restrictions_zero": all(
            report["dd_restriction_zero"] for report in cycle_reports
        ),
        "all_W3_zero_or_spinC_verified": all(
            report["W3_zero_or_spinC_verified"] for report in cycle_reports
        ),
    }


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_time_oriented_m1_selected_cycle_restrictions.py <packet.json>")
        return 1

    packet_path = Path(argv[1]).resolve()
    try:
        data = json.loads(packet_path.read_text(encoding="utf-8"))
        failures, report = validate_packet(data)
    except IncompleteData as exc:
        print(str(exc))
        return 2
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"INVALID selected-cycle restriction packet: {exc}")
        return 1

    print(f"cycle_restriction_report={json.dumps(report, sort_keys=True)}")
    if failures:
        print("selected-cycle restriction FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("selected-cycle restriction PASS")
    print("Freed-Witten DD(B)|Y and W3 gates pass for supplied selected cycles")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
