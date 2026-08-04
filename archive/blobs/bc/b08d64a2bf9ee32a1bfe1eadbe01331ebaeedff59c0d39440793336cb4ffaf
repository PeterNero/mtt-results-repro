from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
)
PERIOD_DIRECTORY = DIRECTORY / "selected_alignment_thimble_periods"
A134 = PERIOD_DIRECTORY / "selected_alignment_height4_E32_handle_interval_and_thimble_cutset.packet.json"
A135 = PERIOD_DIRECTORY / "selected_alignment_height4_E32_thimble_regular_singular_reduction.packet.json"
A136 = PERIOD_DIRECTORY / "selected_alignment_E32_hensel_seed_and_first_full_interval.packet.json"
D004_FULL = PERIOD_DIRECTORY / "d004_selected_009.E32_full.interval.packet.json"
D061_NODAL = PERIOD_DIRECTORY / "d061_selected_088.nodal_factor.interval.packet.json"
D061_TAIL = PERIOD_DIRECTORY / "d061_selected_088.E32_tail.interval.packet.json"
D061_MAIN = PERIOD_DIRECTORY / "d061_selected_088.E32_main.interval.packet.json"
D061_FULL = PERIOD_DIRECTORY / "d061_selected_088.E32_full.interval.packet.json"
D047_NODAL = PERIOD_DIRECTORY / "d047_selected_058.nodal_factor.interval.packet.json"
D047_TAIL = PERIOD_DIRECTORY / "d047_selected_058.E32_tail.interval.packet.json"
PACKET = PERIOD_DIRECTORY / "selected_alignment_E32_clearance_ranked_second_full_interval.packet.json"
FRONTIER = PERIOD_DIRECTORY / "U6_frontier_after_A137.packet.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_q79E32ClearanceRankedSecondFullInterval_v1.md"
CANDIDATE = ROOT / "candidate_data" / "selected_q79e32clearancerankedsecondfullinterval.candidate.json"
CERTIFICATE = ROOT / "certificates" / "selected_q79e32clearancerankedsecondfullinterval.certificate.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def main() -> int:
    a134 = load(A134)
    a135 = load(A135)
    a136 = load(A136)
    d004 = load(D004_FULL)
    nodal = load(D061_NODAL)
    tail = load(D061_TAIL)
    main_interval = load(D061_MAIN)
    full = load(D061_FULL)
    hard_nodal = load(D047_NODAL)
    hard_tail = load(D047_TAIL)
    manifest = a134["selected_E32_decomposition"]["primitive_thimble_chain"]
    coefficients = {
        int(row["distinguished_index"]): int(row["coefficient"])
        for row in manifest
    }
    if coefficients[4] != 2 or coefficients[61] != -3 or coefficients[47] != 4:
        raise AssertionError("selected height-four coefficient ledger changed")
    if not a135["local_theorem"]["proved_for_all_selected_thimbles"]:
        raise AssertionError("A135 local theorem is not closed")
    if not a136["scope"]["first_selected_full_E32_thimble_interval_closed"]:
        raise AssertionError("A136 first full interval is not closed")
    for row in (d004, full):
        if not row["scope"]["single_full_E32_thimble_interval_closed"]:
            raise AssertionError("a selected full interval is not closed")
        if not row["A134_radius_ledger"]["fallback_met"]:
            raise AssertionError("a selected full interval misses the A134 fallback")
        if not row["full_E32_thimble"]["floating_candidate_contained"]:
            raise AssertionError("an independent A131 center is outside its ball")
    if not main_interval["scope"]["relative_homotopy_to_distinguished_radial_path_closed"]:
        raise AssertionError("d061 segmented path is not certified in the selected class")
    if float(main_interval["polygonal_homotopy"]["detour_signed_right_offset"]) != 0:
        raise AssertionError("d061 second execution is not the collinear segmented radial path")
    if not tail["scope"]["endpoint_tail_interval_closed"]:
        raise AssertionError("d061 endpoint tail is not closed")

    initial_budget = float(
        a134["strict_budget_ledger"]["remaining_weighted_thimble_combination_radius_budget"]
    )
    selected = []
    total_cost = 0.0
    for index, row in ((4, d004), (61, full)):
        coefficient = coefficients[index]
        radius = float(row["full_E32_thimble"]["interval_radius_upper"])
        displacement = float(
            row["full_E32_thimble"]["floating_candidate_center_difference"]
        )
        cost = abs(coefficient) * (radius + displacement)
        total_cost += cost
        selected.append(
            {
                "distinguished_index": index,
                "root_id": row["selected_thimble"]["root_id"],
                "coefficient": coefficient,
                "coefficient_l1": abs(coefficient),
                "full_interval_center": row["full_E32_thimble"]["interval_center"],
                "full_interval_radius_upper": radius,
                "A131_center_difference": displacement,
                "weighted_radius_plus_displacement_cost": cost,
            }
        )
    remaining_budget = initial_budget - total_cost
    if remaining_budget <= 0:
        raise AssertionError("two certified thimbles exhaust the weighted budget")
    total_l1 = sum(abs(value) for value in coefficients.values())
    maximum_correction = max(
        float(row["transformed_lift_correction"])
        for row in main_interval["validated_main_transport"]["steps"]
    )
    final_radius = float(full["full_E32_thimble"]["interval_radius_upper"])
    fallback = float(
        a134["strict_budget_ledger"]["sufficient_uniform_per_unit_thimble_radius"]
    )

    packet = {
        "schema": "MTTQ79SelectedE32ClearanceRankedSecondFullInterval.v1",
        "artifact": "A137",
        "status": "SECOND_SELECTED_FULL_E32_THIMBLE_INTERVAL_CLOSED_WEIGHTED_BATCH_OPEN",
        "authority": [
            {"path": relative(path), "sha256": sha256(path)}
            for path in (
                A134,
                A135,
                A136,
                D004_FULL,
                D061_NODAL,
                D061_TAIL,
                D061_MAIN,
                D061_FULL,
                D047_NODAL,
                D047_TAIL,
                Path(__file__),
            )
        ],
        "clearance_ranked_execution": {
            "selection_rule": "execute high-L1 y-chart rows in descending certified radial clearance before hard rays",
            "second_index": 61,
            "second_root_id": "selected_088",
            "height_four_coefficient": coefficients[61],
            "line_chart": "y",
            "radial_other_critical_clearance_lower": main_interval[
                "polygonal_homotopy"
            ]["other_critical_ball_clearance_lower"],
            "radial_selected_y_chart_zero_clearance_lower": main_interval[
                "polygonal_homotopy"
            ]["selected_y_chart_zero_clearance_lower"],
            "path_offset": 0.0,
            "relative_homotopy_winding_vector_zero": True,
        },
        "second_local_interval": {
            "node_parameter_radius_upper": nodal["certified_node"][
                "parameter_radius_upper"
            ],
            "double_root_radius_upper": nodal["certified_node"][
                "double_root_radius_upper"
            ],
            "hensel_jacobian_absolute_lower": nodal["local_weierstrass_factor"][
                "hensel_jacobian_determinant_absolute_lower"
            ],
            "tail_radius_upper": tail["E32_endpoint_tail"]["interval_radius_upper"],
            "tail_regular_segments": len(tail["regular_segments"]),
            "main_radius_upper": main_interval["E32_main_segment"][
                "interval_radius_upper"
            ],
            "main_accepted_steps": main_interval["validated_main_transport"][
                "accepted_step_count"
            ],
            "main_rejected_steps": main_interval["validated_main_transport"][
                "rejected_step_count"
            ],
            "maximum_accepted_lift_correction": maximum_correction,
            "full_radius_upper": final_radius,
            "uniform_fallback": fallback,
            "fallback_margin": fallback - final_radius,
            "independent_A131_center_contained": True,
            "floating_value_used_as_bound": False,
        },
        "closed_interval_ledger": selected,
        "hard_ray_diagnostic": {
            "distinguished_index": 47,
            "root_id": "selected_058",
            "coefficient": coefficients[47],
            "node_and_Hensel_factor_closed": hard_nodal["scope"][
                "analytic_Hensel_factor_germ_closed"
            ],
            "endpoint_tail_closed": hard_tail["scope"][
                "endpoint_tail_interval_closed"
            ],
            "endpoint_tail_radius_upper": hard_tail["E32_endpoint_tail"][
                "interval_radius_upper"
            ],
            "full_main_interval_closed": False,
            "diagnosis": "straight and null-homotopic detour pilots expose a stiff interior reduction; retain for checkpointed local-tolerance execution",
        },
        "weighted_budget_ledger": {
            "A134_initial_remaining_budget": initial_budget,
            "certified_radius_plus_displacement_cost": total_cost,
            "remaining_budget_after_two_intervals": remaining_budget,
            "selected_support_closed": 2,
            "selected_support_total": len(manifest),
            "selected_l1_closed": 5,
            "selected_l1_total": total_l1,
            "remaining_support": len(manifest) - 2,
            "remaining_l1_weight": total_l1 - 5,
        },
        "scope": {
            "observed_SM_values_used": False,
            "A135_local_theorem_instantiated_on_two_thimbles": True,
            "second_selected_full_E32_thimble_interval_closed": True,
            "two_intervals_meet_uniform_fallback": True,
            "weighted_71_thimble_interval_closed": False,
            "fixed_carrier_exact_separation_closed": False,
        },
        "remaining": {
            "y_chart_selected_thimbles": 28,
            "z_chart_selected_thimbles": 41,
            "total_selected_thimbles": 69,
            "remaining_l1_weight": total_l1 - 5,
            "next_engine_step": "run the final-radius segmented radial policy down the clearance-ranked y queue, then add the z-chart adapter",
        },
    }
    dump(PACKET, packet)

    frontier = {
        "schema": "MTTU6FrontierAfterA137.v1",
        "status": "U6_TWO_FULL_E32_THIMBLE_INTERVALS_CLOSED_WEIGHTED_BATCH_OPEN",
        "closed": [
            "A136 first full selected E32 thimble interval d004, coefficient L1=2",
            "A137 second full selected E32 thimble interval d061, coefficient L1=3",
            "final-radius segmented transport policy on the selected radial homotopy class",
            "d047 exact node, Hensel factor, and endpoint tail diagnostic",
        ],
        "active_target": packet["remaining"]["next_engine_step"],
        "selected_support_closed": 2,
        "selected_support_total": len(manifest),
        "selected_l1_closed": 5,
        "selected_l1_total": total_l1,
        "remaining_weighted_budget": remaining_budget,
        "not_closed": [
            "remaining 69 full E32 thimble intervals",
            "weighted 71-thimble E32 interval",
            "exact frozen-carrier decision",
            "covariant PGL3 F/J continuation",
        ],
    }
    dump(FRONTIER, frontier)

    note = f"""# MTT Selected q79 E32 Clearance-Ranked Second Full Interval v1

## A137 result

A137 closes the second complete selected E32 thimble interval. The chosen row
is `d061 / selected_088`, whose exact height-four coefficient is `-3`. Its
node and local Weierstrass/Hensel factor are certified, the endpoint tail uses
{len(tail['regular_segments'])} desingularized interval segments, and the main
transport uses a six-dimensional augmented fundamental frame on a segmented
copy of the already-certified radial homotopy class.

```text
tail radius      = {tail['E32_endpoint_tail']['interval_radius_upper']:.16g}
main radius      = {main_interval['E32_main_segment']['interval_radius_upper']:.16g}
full ball radius = {final_radius:.16g}
A134 fallback    = {fallback:.16g}
fallback margin  = {fallback - final_radius:.16g}
```

The independent A131 floating value lies inside the full ball and is not used
as an error bound. Together with A136, 2 of 71 selected thimbles and L1 weight
5 of 123 are now interval-closed. After charging both exact coefficients, the
remaining strict weighted budget is `{remaining_budget:.16g}`.

## Batch lesson

The useful scaling policy is now explicit: enforce the local defect bound at
every Taylor step, but apply the E32 radius budget to the final transported
coordinate. Intermediate fundamental-frame radii need not be monotone. The
`d047` row separately has an exact node/Hensel factor and endpoint tail, but
its main ray remains a hard checkpointed execution target. This diagnostic is
not counted as a third closed thimble.

## Still open

- 69 full E32 thimble intervals, with L1 weight {total_l1 - 5};
- the z-chart interval adapter;
- the exact weighted 71-thimble sum and frozen-carrier separation decision;
- the later covariant PGL3 continuation if the frozen carrier survives.
"""
    NOTE.write_text(note, encoding="utf-8")

    candidate = {
        "schema": "MTTSelectedQ79E32ClearanceRankedSecondFullInterval.v1",
        "artifact": "A137",
        "status": packet["status"],
        "packet": relative(PACKET),
        "packet_sha256": sha256(PACKET),
        "frontier": relative(FRONTIER),
        "frontier_sha256": sha256(FRONTIER),
        "note": relative(NOTE),
        "note_sha256": sha256(NOTE),
        "observed_SM_values_used": False,
        "second_selected_full_interval_closed": True,
        "weighted_interval_closed": False,
        "closure_claimed": False,
    }
    dump(CANDIDATE, candidate)
    certificate = {
        "schema": "MTTCertificate.v1",
        "certificate": "MTTSelectedQ79E32ClearanceRankedSecondFullInterval",
        "status": packet["status"],
        "candidate_path": relative(CANDIDATE),
        "candidate_sha256": sha256(CANDIDATE),
        "observed_SM_values_used": False,
        "second_selected_full_interval_closed": True,
        "weighted_interval_closed": False,
        "closure_claimed": False,
    }
    dump(CERTIFICATE, certificate)
    for path in (PACKET, FRONTIER, NOTE, CANDIDATE, CERTIFICATE):
        print(f"wrote {relative(path)}")
    print(
        json.dumps(
            {
                "second_full_radius": final_radius,
                "fallback_margin": fallback - final_radius,
                "closed_support": 2,
                "closed_l1": 5,
                "remaining_budget": remaining_budget,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
