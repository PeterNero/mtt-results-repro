"""Lift the time-oriented m=1 finite gerbe table to deck/Cech data.

The previous certificate made the selected q79/F, m=1 torsion label concrete
as a finite B-field table on F_3^2.  This script performs the next honest
bridge: pull that finite cocycle back along the active Iwasawa deck quotient

    pi(g1)=(1,0), pi(g2)=(0,1), pi(g3)=...=pi(g6)=(0,0).

The result is a finite deck-level Cech 2-cocycle compatible with the qutrit
clock/shift projective carrier.  It is not a smooth geometric Deligne
representative, and it does not verify Freed-Witten, projector retention, or
selected D_E/dotD data.
"""

from __future__ import annotations

import cmath
import json
from itertools import product
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATES = ROOT / "certificates"
CANDIDATE_DATA = ROOT / "candidate_data"
CANDIDATE = CANDIDATE_DATA / "time_oriented_m1_deck_cech_lift.candidate.json"
CERTIFICATE = CERTIFICATES / "time_oriented_m1_deck_cech_lift_certificate.json"
PROJECTIVE_CARRIER = CANDIDATE_DATA / "iwasawa_projective_magnetic_carrier.meshN1.json"
FINITE_TABLE_CERT = CERTIFICATES / "time_oriented_m1_gerbe_period_table_certificate.json"
FINITE_TABLE_CANDIDATE = CANDIDATE_DATA / "time_oriented_m1_gerbe_period_table.candidate.json"
MOD = 3


Element = tuple[int, int]
Matrix = list[list[complex]]


DECK_QUOTIENT_MAP: dict[str, Element] = {
    "g1": (1, 0),
    "g2": (0, 1),
    "g3": (0, 0),
    "g4": (0, 0),
    "g5": (0, 0),
    "g6": (0, 0),
}
DECK_GENERATORS = tuple(DECK_QUOTIENT_MAP)


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def get(data: dict[str, Any], *keys: str, default: Any = None) -> Any:
    value: Any = data
    for key in keys:
        if not isinstance(value, dict) or key not in value:
            return default
        value = value[key]
    return value


def add(left: Element, right: Element) -> Element:
    return ((left[0] + right[0]) % MOD, (left[1] + right[1]) % MOD)


def period_mod3(left: Element, right: Element) -> int:
    """Return n for B_1(left,right)=n/3 mod Z."""
    _a, b = left
    c, _d = right
    return (-c * b) % MOD


def delta_mod3(g: Element, h: Element, k: Element) -> int:
    return (
        period_mod3(h, k)
        - period_mod3(add(g, h), k)
        + period_mod3(g, add(h, k))
        - period_mod3(g, h)
    ) % MOD


def commutator_mod3(left: Element, right: Element) -> int:
    return (period_mod3(left, right) - period_mod3(right, left)) % MOD


def holonomy_label(value_mod3: int) -> str:
    return {0: "1", 1: "zeta_3", 2: "zeta_3^2"}[value_mod3 % MOD]


def label(element: Element) -> str:
    return f"{element[0]}{element[1]}"


def parse_complex(value: Any) -> complex:
    if isinstance(value, list):
        if len(value) != 2:
            raise ValueError(f"Cannot parse complex entry: {value!r}")
        return complex(float(value[0]), float(value[1]))
    return complex(float(value), 0.0)


def parse_matrix(raw: list[list[Any]]) -> Matrix:
    return [[parse_complex(entry) for entry in row] for row in raw]


def matmul(left: Matrix, right: Matrix) -> Matrix:
    size = len(left)
    return [
        [
            sum(left[row][idx] * right[idx][col] for idx in range(size))
            for col in range(size)
        ]
        for row in range(size)
    ]


def matrix_diff_norm(left: Matrix, right: Matrix) -> float:
    return max(
        abs(left[row][col] - right[row][col])
        for row in range(len(left))
        for col in range(len(left[row]))
    )


def scalar_mul(scalar: complex, matrix: Matrix) -> Matrix:
    return [[scalar * entry for entry in row] for row in matrix]


def identity(size: int) -> Matrix:
    return [[1.0 + 0j if row == col else 0j for col in range(size)] for row in range(size)]


def carrier_phase_exponent(g1: Matrix, g2: Matrix) -> dict[str, Any]:
    """Find e with g1*g2 = zeta_3^e g2*g1."""
    left_then_right = matmul(g1, g2)
    right_then_left = matmul(g2, g1)
    zeta = cmath.exp(2j * cmath.pi / 3)
    candidates = []
    for exponent in range(MOD):
        error = matrix_diff_norm(left_then_right, scalar_mul(zeta**exponent, right_then_left))
        candidates.append({"exponent_mod3": exponent, "max_error": error})
    best = min(candidates, key=lambda item: item["max_error"])
    return {
        "relation": "rho(g1) rho(g2) = zeta_3^e rho(g2) rho(g1)",
        "best_exponent_mod3": best["exponent_mod3"],
        "best_max_error": best["max_error"],
        "all_candidate_errors": candidates,
        "matches_zeta3_to_numeric_tolerance": best["exponent_mod3"] == 1
        and best["max_error"] < 1e-12,
    }


def generator_period_table() -> dict[str, int]:
    return {
        f"{left}|{right}": period_mod3(DECK_QUOTIENT_MAP[left], DECK_QUOTIENT_MAP[right])
        for left in DECK_GENERATORS
        for right in DECK_GENERATORS
    }


def generator_holonomy_table(periods: dict[str, int]) -> dict[str, str]:
    return {key: holonomy_label(value) for key, value in periods.items()}


def generator_delta_table() -> dict[str, int]:
    return {
        f"{g}|{h}|{k}": delta_mod3(
            DECK_QUOTIENT_MAP[g], DECK_QUOTIENT_MAP[h], DECK_QUOTIENT_MAP[k]
        )
        for g in DECK_GENERATORS
        for h in DECK_GENERATORS
        for k in DECK_GENERATORS
    }


def active_quotient_delta_table() -> dict[str, int]:
    elements = [(a, b) for a, b in product(range(MOD), repeat=2)]
    return {
        f"{label(g)}|{label(h)}|{label(k)}": delta_mod3(g, h, k)
        for g in elements
        for h in elements
        for k in elements
    }


def kernel_directions_trivial(periods: dict[str, int]) -> bool:
    kernel_generators = {"g3", "g4", "g5", "g6"}
    for key, value in periods.items():
        left, right = key.split("|")
        if (left in kernel_generators or right in kernel_generators) and value != 0:
            return False
    return True


def analyze() -> dict[str, Any]:
    finite_cert = load_json(FINITE_TABLE_CERT)
    finite_candidate = load_json(FINITE_TABLE_CANDIDATE)
    carrier = load_json(PROJECTIVE_CARRIER)

    periods = generator_period_table()
    holonomies = generator_holonomy_table(periods)
    generator_deltas = generator_delta_table()
    active_deltas = active_quotient_delta_table()
    nonzero_generator_deltas = {
        key: value for key, value in generator_deltas.items() if value != 0
    }
    nonzero_active_deltas = {key: value for key, value in active_deltas.items() if value != 0}

    g1 = parse_matrix(get(carrier, "generator_data", "g1", "matrix"))
    g2 = parse_matrix(get(carrier, "generator_data", "g2", "matrix"))
    phase_relation = carrier_phase_exponent(g1, g2)
    identity_checks = {
        gen: matrix_diff_norm(
            parse_matrix(get(carrier, "generator_data", gen, "matrix")),
            identity(3),
        )
        for gen in ("g3", "g4", "g5", "g6")
    }
    inactive_identity_ok = all(error < 1e-12 for error in identity_checks.values())

    finite_table = get(finite_candidate, "finite_period_table", "period_table_mod3", default={})
    finite_input_closed = (
        finite_cert.get("status")
        == "TIME_ORIENTED_M1_FINITE_GERBE_PERIOD_TABLE_CLOSED_OPERATOR_SOURCE_OPEN"
        and get(finite_cert, "calculation_results", "finite_m1_period_table_constructed")
        is True
    )
    pullback_matches_table = all(
        periods[f"{left}|{right}"]
        == finite_table.get(
            f"{label(DECK_QUOTIENT_MAP[left])}|{label(DECK_QUOTIENT_MAP[right])}"
        )
        for left in DECK_GENERATORS
        for right in DECK_GENERATORS
    )
    commutator_g1g2 = commutator_mod3(DECK_QUOTIENT_MAP["g1"], DECK_QUOTIENT_MAP["g2"])
    commutator_g2g1 = commutator_mod3(DECK_QUOTIENT_MAP["g2"], DECK_QUOTIENT_MAP["g1"])

    deck_cech_closed = (
        finite_input_closed
        and pullback_matches_table
        and not nonzero_generator_deltas
        and not nonzero_active_deltas
        and commutator_g1g2 == 1
        and commutator_g2g1 == 2
        and phase_relation["matches_zeta3_to_numeric_tolerance"] is True
        and kernel_directions_trivial(periods)
        and inactive_identity_ok
    )

    status = (
        "TIME_ORIENTED_M1_DECK_CECH_LIFT_CLOSED_GEOMETRIC_OPERATOR_SOURCE_OPEN"
        if deck_cech_closed
        else "TIME_ORIENTED_M1_DECK_CECH_LIFT_NOT_CLOSED"
    )

    return {
        "candidate": "TimeOrientedM1DeckCechLift",
        "status": status,
        "generated_by": "scripts/construct_time_oriented_m1_deck_cech_lift.py",
        "input_finite_table": {
            "certificate": "time_oriented_m1_gerbe_period_table_certificate.json",
            "candidate_data": "time_oriented_m1_gerbe_period_table.candidate.json",
            "finite_input_closed": finite_input_closed,
        },
        "deck_quotient_map": {
            "source": "Iwasawa deck generators g1..g6, reduced mod the active torsion quotient",
            "target": "F_3^2",
            "map": {gen: list(value) for gen, value in DECK_QUOTIENT_MAP.items()},
            "kernel_generators": ["g3", "g4", "g5", "g6", "g1^3", "g2^3"],
            "interpretation": (
                "Only the g1/g2 magnetic deck square carries the selected m=1 "
                "torsion holonomy; g3..g6 are trivial in this finite torsion quotient."
            ),
        },
        "pulled_back_deck_cech_data": {
            "period_formula": "B_deck(g,h)=B_1(pi(g),pi(h)), with B_1((a,b),(c,d))=-c*b/3 mod Z",
            "generator_period_table_mod3": periods,
            "generator_holonomy_table": holonomies,
            "generator_coboundary_checked_triples": len(generator_deltas),
            "generator_nonzero_coboundary_deltas_mod3": nonzero_generator_deltas,
            "active_quotient_coboundary_checked_triples": len(active_deltas),
            "active_quotient_nonzero_coboundary_deltas_mod3": nonzero_active_deltas,
            "pullback_matches_finite_period_table": pullback_matches_table,
            "kernel_directions_have_trivial_periods": kernel_directions_trivial(periods),
            "full_deck_quotient_cocycle_reason": (
                "The deck cochain is the pullback pi^*B_1. Since delta B_1=0 "
                "on F_3^2, delta pi^*B_1=pi^* delta B_1=0 on the full deck quotient."
            ),
        },
        "qutrit_projective_carrier_match": {
            "carrier_path": "candidate_data/iwasawa_projective_magnetic_carrier.meshN1.json",
            "carrier_status": carrier.get("status"),
            "g1g2_commutator_mod3_from_cech_pullback": commutator_g1g2,
            "g2g1_commutator_mod3_from_cech_pullback": commutator_g2g1,
            "rho_g1_rho_g2_numeric_phase_relation": phase_relation,
            "inactive_generator_identity_errors": identity_checks,
            "inactive_generators_identity": inactive_identity_ok,
        },
        "calculation_results": {
            "deck_quotient_map_fixed": True,
            "finite_m1_table_input_closed": finite_input_closed,
            "deck_cech_pullback_constructed": deck_cech_closed,
            "generator_level_delta_zero": not nonzero_generator_deltas,
            "active_quotient_delta_zero": not nonzero_active_deltas,
            "pullback_functoriality_closes_full_deck_quotient_cocycle": deck_cech_closed,
            "qutrit_projective_commutator_matched": (
                phase_relation["matches_zeta3_to_numeric_tolerance"] is True
                and commutator_g1g2 == 1
            ),
            "kernel_directions_trivial": kernel_directions_trivial(periods),
            "ordinary_single_carrier_higgs_shortcut_still_rejected": True,
        },
        "what_this_closes": {
            "deck_generator_to_F3_squared_quotient_map": deck_cech_closed,
            "finite_Cech_two_cocycle_on_active_deck_quotient": deck_cech_closed,
            "deck_pullback_of_time_oriented_m1_period_table": deck_cech_closed,
            "compatibility_with_qutrit_clock_shift_projective_commutator": deck_cech_closed,
            "triviality_of_inactive_deck_generators_in_this_torsion_quotient": deck_cech_closed,
            "full_deck_quotient_cocycle_by_pullback_functoriality": deck_cech_closed,
        },
        "still_open": {
            "smooth_geometric_Deligne_Cech_representative_on_selected_cover": True,
            "identification_of_selected_cycles_or_branes_for_Freed_Witten": True,
            "Freed_Witten_condition_w2_plus_B_verified": True,
            "heterotic_Green_Schwarz_Bianchi_with_curvature_terms": True,
            "twisted_projector_retention_for_visible_SM_sectors": True,
            "selected_visible_bundle_or_sheaf_operator_source": True,
            "selected_D_E_dotD_Riesz_Green_files_from_same_branch": True,
            "selected_C1_primitive_contractions": True,
            "Yukawa_magnitudes_CKM_angles_and_full_SM_closure": True,
        },
        "guardrails": {
            "claims_smooth_geometric_Deligne_Cech_representative": False,
            "claims_Freed_Witten_verified": False,
            "claims_heterotic_Green_Schwarz_embedding": False,
            "claims_projector_retention": False,
            "claims_selected_D_E_dotD_constructed": False,
            "claims_selected_visible_operator_source": False,
            "claims_Yukawa_or_CKM_magnitudes": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "The selected finite q79/F,m=1 period table now has a deck-level "
                "Cech pullback: g1 and g2 map to the active F_3^2 torsion quotient, "
                "g3..g6 lie in the kernel, delta B remains zero by pullback, and "
                "the g1/g2 commutator matches the qutrit clock-shift carrier."
            )
            if deck_cech_closed
            else "The deck/Cech pullback did not close.",
            "next_closing_object": (
                "Promote this finite deck pullback to a smooth selected Deligne/Cech "
                "or B-field representative on the geometric cover, then verify "
                "Freed-Witten and visible-sector projector retention before deriving "
                "selected D_E/dotD/Riesz/Green data."
            ),
        },
    }


def write_outputs(report: dict[str, Any]) -> None:
    CANDIDATE.parent.mkdir(parents=True, exist_ok=True)
    CERTIFICATE.parent.mkdir(parents=True, exist_ok=True)
    CANDIDATE.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    certificate = {
        "certificate": "TimeOrientedM1DeckCechLift",
        "status": report["status"],
        "analysis_script": "scripts/construct_time_oriented_m1_deck_cech_lift.py",
        "candidate_data": "candidate_data/time_oriented_m1_deck_cech_lift.candidate.json",
        "input_finite_table": report["input_finite_table"],
        "deck_quotient_map": report["deck_quotient_map"],
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
