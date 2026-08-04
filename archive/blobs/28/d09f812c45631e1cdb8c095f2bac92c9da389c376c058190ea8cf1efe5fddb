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
NODAL = PERIOD_DIRECTORY / "d004_selected_009.nodal_factor.interval.packet.json"
TAIL = PERIOD_DIRECTORY / "d004_selected_009.E32_tail.interval.packet.json"
MAIN = PERIOD_DIRECTORY / "d004_selected_009.E32_main.interval.packet.json"
FULL = PERIOD_DIRECTORY / "d004_selected_009.E32_full.interval.packet.json"
PACKET = PERIOD_DIRECTORY / "selected_alignment_E32_hensel_seed_and_first_full_interval.packet.json"
FRONTIER = PERIOD_DIRECTORY / "U6_frontier_after_A136.packet.json"
SLUG = "selected_q79e32thimblehenselseedandfirstfullinterval"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERTIFICATE = ROOT / "certificates" / f"{SLUG}.certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_q79E32ThimbleHenselSeedAndFirstFullInterval_v1.md"


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
    nodal = load(NODAL)
    tail = load(TAIL)
    main_interval = load(MAIN)
    full = load(FULL)
    if not a135["local_theorem"]["proved_for_all_selected_thimbles"]:
        raise AssertionError("A135 regular-singular theorem is not closed")
    if not nodal["scope"]["analytic_Hensel_factor_germ_closed"]:
        raise AssertionError("nodal Hensel germ is not closed")
    if not tail["scope"]["endpoint_tail_interval_closed"]:
        raise AssertionError("endpoint tail interval is not closed")
    if not main_interval["scope"]["main_homogeneous_Gauss_Manin_segment_interval_closed"]:
        raise AssertionError("main homogeneous interval is not closed")
    if not full["scope"]["single_full_E32_thimble_interval_closed"]:
        raise AssertionError("full single-thimble interval is not closed")
    if not full["A134_radius_ledger"]["fallback_met"]:
        raise AssertionError("first full interval misses the A134 fallback")
    if not full["full_E32_thimble"]["floating_candidate_contained"]:
        raise AssertionError("independent floating center is outside the interval")

    manifest = a134["selected_E32_decomposition"]["primitive_thimble_chain"]
    selected_row = [
        row for row in manifest if int(row["distinguished_index"]) == 4
    ]
    if len(selected_row) != 1:
        raise AssertionError("d004 is not unique in the A134 chain")
    coefficient = int(selected_row[0]["coefficient"])
    radius = float(full["full_E32_thimble"]["interval_radius_upper"])
    center_difference = float(
        full["full_E32_thimble"]["floating_candidate_center_difference"]
    )
    certified_budget_cost = abs(coefficient) * (radius + center_difference)
    initial_budget = float(
        a134["strict_budget_ledger"]["remaining_weighted_thimble_combination_radius_budget"]
    )
    remaining_budget = initial_budget - certified_budget_cost
    if remaining_budget <= 0:
        raise AssertionError("first certified thimble exhausts the weighted budget")
    steps = main_interval["validated_main_transport"]["steps"]
    maximum_correction = max(float(row["transformed_lift_correction"]) for row in steps)
    final_envelope = float(steps[-1]["E32_radius_envelope"])

    packet = {
        "schema": "MTTQ79SelectedE32ThimbleHenselSeedAndFirstFullInterval.v1",
        "artifact": "A136",
        "status": "FIRST_SELECTED_FULL_E32_THIMBLE_INTERVAL_CLOSED_WEIGHTED_EXECUTION_OPEN",
        "authority": [
            {"path": relative(path), "sha256": sha256(path)}
            for path in (A134, A135, NODAL, TAIL, MAIN, FULL, Path(__file__))
        ],
        "selected_first_execution": {
            "distinguished_index": 4,
            "root_id": "selected_009",
            "height_four_chain_coefficient": coefficient,
            "line_chart": "y",
            "endpoint_cutoff_epsilon": 1.0e-5,
        },
        "certified_local_seed": {
            "node_parameter_radius_upper": nodal["certified_node"]["parameter_radius_upper"],
            "double_root_radius_upper": nodal["certified_node"]["double_root_radius_upper"],
            "node_jacobian_absolute_lower": nodal["certified_node"][
                "jacobian_determinant_absolute_lower"
            ],
            "quartic_at_node_absolute_lower": nodal["local_weierstrass_factor"][
                "quartic_at_double_root_absolute_lower"
            ],
            "hensel_jacobian_absolute_lower": nodal["local_weierstrass_factor"][
                "hensel_jacobian_determinant_absolute_lower"
            ],
            "factor_disk_residual_upper": tail["quantitative_Hensel_disk"][
                "factor_residual_infinity_norm_upper"
            ],
            "factor_disk_inverse_norm_upper": tail["quantitative_Hensel_disk"][
                "factor_jacobian_inverse_infinity_norm_upper"
            ],
            "factor_disk_contraction_upper": tail["quantitative_Hensel_disk"][
                "contraction_bound_upper"
            ],
            "route": "local Weierstrass/Hensel factor realizes the A135 log-free branch without a raw fixed-frame pole bound",
        },
        "certified_interval_execution": {
            "endpoint_tail_radius_upper": tail["E32_endpoint_tail"]["interval_radius_upper"],
            "main_augmented_frame_radius_upper": main_interval["E32_main_segment"][
                "interval_radius_upper"
            ],
            "main_certificate_method": main_interval["validated_main_transport"][
                "certificate_method"
            ],
            "main_accepted_steps": main_interval["validated_main_transport"][
                "accepted_step_count"
            ],
            "main_rejected_steps": main_interval["validated_main_transport"][
                "rejected_step_count"
            ],
            "maximum_accepted_lift_correction": maximum_correction,
            "final_E32_radius_envelope": final_envelope,
            "full_interval_center": full["full_E32_thimble"]["interval_center"],
            "full_interval_radius_upper": radius,
            "independent_A131_center_difference": center_difference,
            "independent_A131_center_contained": True,
            "floating_value_used_as_bound": False,
        },
        "weighted_budget_ledger": {
            "A134_initial_remaining_budget": initial_budget,
            "certified_coefficient_l1_cost": abs(coefficient),
            "certified_radius_plus_center_displacement_cost": certified_budget_cost,
            "remaining_budget_after_first_interval": remaining_budget,
            "selected_support_closed": 1,
            "selected_support_total": len(manifest),
            "selected_l1_closed": abs(coefficient),
            "selected_l1_total": sum(abs(int(row["coefficient"])) for row in manifest),
        },
        "scope": {
            "observed_SM_values_used": False,
            "A135_local_theorem_instantiated_numerically": True,
            "first_selected_full_E32_thimble_interval_closed": True,
            "first_interval_meets_uniform_fallback": True,
            "weighted_71_thimble_interval_closed": False,
            "fixed_carrier_exact_separation_closed": False,
            "covariant_alignment_zero_closed": False,
        },
        "remaining": {
            "y_chart_selected_thimbles": 29,
            "z_chart_selected_thimbles": 41,
            "total_selected_thimbles": 70,
            "remaining_l1_weight": 121,
            "next_engine_step": "parameterize the interval system by y/z chart and batch the same Hensel-tail plus augmented-frame certificate",
        },
    }
    dump(PACKET, packet)

    frontier = {
        "schema": "MTTU6FrontierAfterA136.v1",
        "status": "U6_FIRST_FULL_E32_THIMBLE_INTERVAL_CLOSED_WEIGHTED_BATCH_OPEN",
        "closed": [
            "A133 refined beta interval and one-row E32 cutset",
            "A134 rigorous selected E32 handle interval",
            "A135 regular-singular and log-free branch theorem for all 71 selected thimbles",
            "A136 exact interval node and local Hensel seed for d004",
            "A136 rigorous endpoint tail and six-dimensional augmented main transport for d004",
            "A136 first full selected E32 thimble interval inside the A134 fallback",
        ],
        "active_target": packet["remaining"]["next_engine_step"],
        "selected_support_closed": 1,
        "selected_support_total": len(manifest),
        "remaining_weighted_budget": remaining_budget,
        "not_closed": [
            "remaining 70 full E32 thimble intervals",
            "weighted 71-thimble E32 interval",
            "exact frozen-carrier decision",
            "covariant PGL3 F/J continuation",
        ],
    }
    dump(FRONTIER, frontier)

    note = f"""# MTT Selected q79 E32 Thimble Hensel Seed and First Full Interval v1

## What A136 closes

For the selected `d004 / selected_009` thimble, A136 replaces the open A135
value placeholders by an interval-certified local object. Interval Newton
isolates the nodal parameter and double root at radius
`{nodal['certified_node']['parameter_radius_upper']:.3e}`. The nodal sextic
admits a monic quadratic times quartic factor with

```text
|H(r)| > {nodal['local_weierstrass_factor']['quartic_at_double_root_absolute_lower']:.15g},
|det J_Hensel| > {nodal['local_weierstrass_factor']['hensel_jacobian_determinant_absolute_lower']:.15g}.
```

The quantitative Taylor-Hensel disk has residual at most
`{tail['quantitative_Hensel_disk']['factor_residual_infinity_norm_upper']:.3e}`
and contraction bound
`{tail['quantitative_Hensel_disk']['contraction_bound_upper']:.3e}`. It gives a
rigorous desingularized endpoint-tail ball. The ordinary segment is certified
in a six-dimensional homogeneous augmented fundamental frame, which keeps the
`E32` integral error correlated with the five period coordinates.

The reproducible main command used for this packet is:

```text
python scripts/certify_q79_selected_alignment_single_E32_thimble_main_interval.py --distinguished-index 4 --order 48 --maximum-lift-correction 1e-8 --target-main-radius 1e-5 --initial-radius-allowance 1e-6
```

The final result is

```text
E32(d004) in ball(
  {full['full_E32_thimble']['interval_center']['real']}
  + {full['full_E32_thimble']['interval_center']['imaginary']} i,
  {radius:.17g}
).
```

The independent A131 floating center differs by only
`{center_difference:.3e}` and lies inside this ball, but it is never used as
an error bound. The A134 sufficient per-unit fallback is
`{full['A134_radius_ledger']['sufficient_uniform_per_unit_thimble_radius']:.17g}`,
so the first full interval passes with margin
`{full['A134_radius_ledger']['fallback_margin']:.17g}`.

## Exact frontier

This is the first complete numerical instantiation of A135, not the weighted
closure. One of 71 selected thimbles (L1 weight 2 of 123) is closed. The
remaining budget after charging both its radius and its displacement from the
A131 reference center is `{remaining_budget:.17g}`. The next task is to add a
chart parameter to the validated engine and execute the same certificate for
29 remaining y-chart and 41 z-chart thimbles.

No observed Standard Model value is used.
"""
    NOTE.write_text(note, encoding="utf-8")

    candidate = {
        "schema": "MTTSelectedQ79E32ThimbleHenselSeedAndFirstFullInterval.v1",
        "status": packet["status"],
        "artifact": "A136",
        "packet": relative(PACKET),
        "packet_sha256": sha256(PACKET),
        "frontier": relative(FRONTIER),
        "frontier_sha256": sha256(FRONTIER),
        "note": relative(NOTE),
        "note_sha256": sha256(NOTE),
        "closure_claimed": False,
        "first_selected_full_interval_closed": True,
        "weighted_interval_closed": False,
        "observed_SM_values_used": False,
    }
    dump(CANDIDATE, candidate)
    certificate = {
        "schema": "MTTCertificate.v1",
        "certificate": "MTTSelectedQ79E32ThimbleHenselSeedAndFirstFullInterval",
        "candidate_path": relative(CANDIDATE),
        "candidate_sha256": sha256(CANDIDATE),
        "status": candidate["status"],
        "closure_claimed": False,
        "first_selected_full_interval_closed": True,
        "weighted_interval_closed": False,
        "observed_SM_values_used": False,
    }
    dump(CERTIFICATE, certificate)
    print(f"wrote {relative(PACKET)}")
    print(f"wrote {relative(FRONTIER)}")
    print(f"wrote {relative(NOTE)}")
    print(f"wrote {relative(CANDIDATE)}")
    print(f"wrote {relative(CERTIFICATE)}")
    print(
        json.dumps(
            {
                "full_radius": radius,
                "fallback_margin": full["A134_radius_ledger"]["fallback_margin"],
                "center_difference": center_difference,
                "weighted_budget_cost": certified_budget_cost,
                "remaining_weighted_budget": remaining_budget,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
