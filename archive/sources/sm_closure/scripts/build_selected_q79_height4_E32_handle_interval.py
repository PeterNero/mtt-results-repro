from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
)
PERIOD_DIRECTORY = DIRECTORY / "selected_alignment_thimble_periods"
A133 = PERIOD_DIRECTORY / "selected_alignment_height4_frozen_carrier_refinement_and_interval_cutset.packet.json"
HANDLE_INTERVAL = PERIOD_DIRECTORY / "selected_alignment_E32_handle_combination.interval.packet.json"
PERIODS = PERIOD_DIRECTORY / "selected_alignment_full_integral_basis_period_table.packet.json"
HANDLES = PERIOD_DIRECTORY / "selected_alignment_primitive_handle_periods.packet.json"
PACKET = PERIOD_DIRECTORY / "selected_alignment_height4_E32_handle_interval_and_thimble_cutset.packet.json"
FRONTIER = PERIOD_DIRECTORY / "U6_frontier_after_A134.packet.json"
SLUG = "selected_q79heightfoure32handleintervalandthimblecutset"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERTIFICATE = ROOT / "certificates" / f"{SLUG}.certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_q79HeightFourE32HandleIntervalAndThimbleCutset_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def complex_pair(value: complex) -> dict[str, str]:
    return {
        "real": format(float(value.real), ".17g"),
        "imaginary": format(float(value.imag), ".17g"),
    }


def main() -> int:
    a133 = load(A133)
    handle_interval = load(HANDLE_INTERVAL)
    periods = load(PERIODS)
    handles = load(HANDLES)

    target = a133["minimal_strict_interval_target"]
    if target["form"] != "E32" or int(target["row_index"]) != 5:
        raise AssertionError("A133 selected interval row changed")
    if not handle_interval["scope"]["selected_handle_combination_interval_closed"]:
        raise AssertionError("selected handle interval is not closed")

    matrix = np.asarray(
        [
            [complex_value(value) for value in row]
            for row in periods["period_matrix_rows"]
        ],
        dtype=np.complex128,
    )
    if matrix.shape != (8, 92) or periods["form_names"][5] != "E32":
        raise AssertionError("A131 period table changed")
    ell = np.asarray(
        a133["height_four_seed"]["effective_coordinates_Z90"] + [0, 0],
        dtype=np.int64,
    )
    if ell.shape != (92,):
        raise AssertionError("A133 effective carrier shape changed")

    handle_coordinates = np.asarray(
        a133["height_four_seed"]["primitive_handle_coordinates"],
        dtype=np.int64,
    )
    handle_matrix = np.asarray(
        [
            [complex_value(value) for value in row]
            for row in handles["primitive_handle_period_matrix"]
        ],
        dtype=np.complex128,
    )
    if handle_matrix.shape != (8, 8):
        raise AssertionError("primitive handle period table changed")

    full_center = complex(matrix[5] @ ell)
    floating_handle_center = complex(handle_matrix[5] @ handle_coordinates)
    floating_thimble_center = full_center - floating_handle_center
    interval_row = handle_interval["E32_handle_combination"]["interval"]
    interval_handle_center = complex_value(interval_row["center"])
    interval_handle_radius = float(interval_row["uniform_radius_upper"])
    handle_center_shift = abs(interval_handle_center - floating_handle_center)
    recorded_shift = float(
        handle_interval["E32_handle_combination"]["A131_center_difference"]
    )
    if abs(handle_center_shift - recorded_shift) > 1.0e-14:
        raise AssertionError("handle center-shift replay changed")

    total_budget = float(target["strict_required_period_combination_radius_upper"])
    handle_budget_cost = interval_handle_radius + handle_center_shift
    thimble_budget = total_budget - handle_budget_cost
    if thimble_budget <= 0:
        raise AssertionError("validated handle interval exhausts A133 budget")
    thimble_l1 = int(a133["height_four_seed"]["primitive_thimble_l1_norm"])
    support = int(a133["height_four_seed"]["primitive_thimble_support"])
    if thimble_l1 != 123 or support != 71:
        raise AssertionError("A133 selected thimble chain changed")

    authority_paths = [A133, HANDLE_INTERVAL, PERIODS, HANDLES, Path(__file__)]
    packet = {
        "schema": "MTTQ79HeightFourE32HandleIntervalAndThimbleCutset.v1",
        "status": "SELECTED_E32_HANDLE_INTERVAL_CLOSED_ONE_WEIGHTED_THIMBLE_INTERVAL_OPEN",
        "authority": [
            {"path": relative(path), "sha256": sha256(path)}
            for path in authority_paths
        ],
        "selected_E32_decomposition": {
            "identity": "sum_I m_I Pi_E32,I = T_E32(m_thimble) + H_E32(m_handle)",
            "A131_full_combination_center": complex_pair(full_center),
            "A131_floating_thimble_combination_center": complex_pair(
                floating_thimble_center
            ),
            "A131_floating_handle_combination_center": complex_pair(
                floating_handle_center
            ),
            "validated_handle_interval_center": complex_pair(
                interval_handle_center
            ),
            "validated_handle_interval_radius": interval_handle_radius,
            "validated_to_A131_handle_center_shift": handle_center_shift,
            "primitive_thimble_support": support,
            "primitive_thimble_l1_norm": thimble_l1,
            "primitive_thimble_chain": a133["height_four_seed"][
                "primitive_thimble_chain"
            ],
            "primitive_handle_coordinates": handle_coordinates.tolist(),
        },
        "strict_budget_ledger": {
            "A133_total_selected_period_combination_radius_budget": total_budget,
            "rigorous_handle_interval_radius": interval_handle_radius,
            "handle_center_shift_from_A131_reference": handle_center_shift,
            "total_handle_budget_cost": handle_budget_cost,
            "remaining_weighted_thimble_combination_radius_budget": thimble_budget,
            "sufficient_uniform_per_unit_thimble_radius": thimble_budget
            / thimble_l1,
            "budget_fraction_remaining": thimble_budget / total_budget,
            "certificate_logic": (
                "A rigorous complex ball for the weighted 71-thimble E32 "
                "combination whose center displacement from the A131 thimble "
                "center plus radius is below the displayed remaining budget, "
                "combined with the certified handle ball, proves frozen-carrier "
                "separation in E32."
            ),
        },
        "scope": {
            "observed_SM_values_used": False,
            "selected_handle_combination_interval_closed": True,
            "selected_thimble_combination_interval_closed": False,
            "all_71_thimbles_need_individual_interval_packets": False,
            "one_weighted_thimble_combination_suffices": True,
            "full_E32_combined_period_interval_closed": False,
            "fixed_carrier_exact_separation_proved": False,
            "covariant_alignment_zero_solved": False,
            "small_residual_promoted_to_equality": False,
        },
        "next_required_artifact": "MTT_Selected_q79HeightFourE32ThimbleCombinationIntervalAndCovariantContinuation_v1",
    }
    dump(PACKET, packet)

    frontier = {
        "schema": "MTTU6FrontierAfterA134.v1",
        "status": "U6_E32_HANDLE_INTERVAL_CLOSED_WEIGHTED_THIMBLE_INTERVAL_AND_COVARIANT_ZERO_OPEN",
        "closed": [
            "A131 selected-carrier floating 8x92 period matrix",
            "A132 exact effective Z90 quotient and selected height-four seed",
            "A133 rigorous refined beta interval and one-row E32 cutset",
            "A134 rigorous direct base-cycle and homogeneous A-handle E32 interval",
        ],
        "active_target": (
            "certify the one weighted 71-thimble E32 combination with center "
            "displacement plus radius below "
            f"{thimble_budget:.17g}"
        ),
        "then": "execute covariant F(A,m), J(A,m) continuation after the frozen-carrier decision",
        "not_closed": [
            "rigorous weighted 71-thimble E32 combination interval",
            "exact frozen-carrier separation or membership",
            "covariant PGL3 zero and nonzero Jacobian",
        ],
    }
    dump(FRONTIER, frontier)

    candidate = {
        "schema": "MTTSelectedQ79HeightFourE32HandleIntervalAndThimbleCutset.v1",
        "status": packet["status"],
        "artifact": "A134",
        "packet": relative(PACKET),
        "packet_sha256": sha256(PACKET),
        "frontier": relative(FRONTIER),
        "frontier_sha256": sha256(FRONTIER),
        "closure_claimed": False,
        "observed_SM_values_used": False,
        "what_closes": {
            "selected_E32_handle_combination_interval": True,
            "strict_remaining_thimble_budget": True,
            "single_weighted_thimble_cutset": True,
        },
        "what_remains_open": {
            "selected_E32_weighted_thimble_interval": True,
            "exact_frozen_carrier_decision": True,
            "covariant_PGL3_zero_and_Jacobian": True,
        },
        "next_required_artifact": packet["next_required_artifact"],
    }

    note = f"""# MTT Selected q79 Height-Four E32 Handle Interval and Thimble Cutset v1

## Result

A134 rigorously evaluates the handle part of the A132 height-four carrier in
the sole separating row selected by A133. The exact primitive identity is

```text
-A:a1 + A:a2 + A:b2 = A:(sigma3 + sigma4).
```

The marked base cycles are computed as direct algebraic-cut integrals. The
selected root-label cuts are `(3,4)` for `sigma3` and `(1,4)` for `sigma4`;
their five-period centers agree with the independently synchronized A131
marking to at most `{handle_interval['base_cycle_interval']['A131_marked_center_maximum_difference']:.3e}`.
Validated homogeneous Gauss-Manin transport around the full A handle gives

```text
H_E32 = {interval_handle_center.real:.17g}
          {interval_handle_center.imag:+.17g} i
radius <= {interval_handle_radius:.17g}.
```

Its center differs from the independent A131 handle value by only
`{handle_center_shift:.3e}`. This is a rigorous interval result, not a
two-precision convergence proxy.

## Remaining exact cutset

The A133 total period budget is `{total_budget:.17g}`. Charging both the
rigorous handle radius and its displacement from the A131 reference leaves

```text
{thimble_budget:.17g}
```

for the weighted 71-thimble `E32` combination. The chain has primitive
coefficient L1 norm `{thimble_l1}`. Certifying the weighted sum directly is
sufficient; 71 independent theorem packets are not logically required. A
uniform per-unit bound of `{thimble_budget / thimble_l1:.17g}` would also
suffice, but is only a fallback strategy.

## Scope

A134 closes the handle interval and fixes the numerical target for the last
period component. It does not yet claim the weighted thimble interval,
frozen-carrier separation, or a covariant PGL3 zero. No observed Standard
Model value is used.
"""
    NOTE.write_text(note, encoding="utf-8")
    candidate["note"] = relative(NOTE)
    candidate["note_sha256"] = sha256(NOTE)
    dump(CANDIDATE, candidate)

    certificate = {
        "schema": "MTTCertificate.v1",
        "certificate": "MTTSelectedQ79HeightFourE32HandleIntervalAndThimbleCutset",
        "candidate_path": relative(CANDIDATE),
        "candidate_sha256": sha256(CANDIDATE),
        "status": candidate["status"],
        "closure_claimed": False,
        "observed_SM_values_used": False,
        "next_required_artifact": candidate["next_required_artifact"],
    }
    dump(CERTIFICATE, certificate)
    print(f"wrote {relative(PACKET)}")
    print(f"wrote {relative(FRONTIER)}")
    print(f"wrote {relative(CANDIDATE)}")
    print(f"wrote {relative(CERTIFICATE)}")
    print(f"wrote {relative(NOTE)}")
    print(
        json.dumps(
            {
                "handle_radius": interval_handle_radius,
                "handle_center_shift": handle_center_shift,
                "remaining_thimble_budget": thimble_budget,
                "per_unit_fallback_budget": thimble_budget / thimble_l1,
                "budget_fraction_remaining": thimble_budget / total_budget,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
