from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from flint import ctx

import certify_q79_height4_d087_full_residue_main_interval as n3_engine
import certify_q79_selected_side_beta_defect_transport as validated


ROOT = Path(__file__).resolve().parents[1]
PERIOD_DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
)
PROBE = PERIOD_DIRECTORY / "covariant_floating_probe"
N3 = PROBE / "cplx" / "n3ud" / "probe.packet.json"
A219 = PROBE / "rank3_complex_PGL3_floating_boundary.packet.json"
BASE_LIFT = PROBE / "validated_transport" / "n3.rank3.base_lift.interval.json"
OUTPUT = PROBE / "validated_transport" / "n3.rank3.anchored_beta.interval.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourRank3AnchoredBetaInterval_A376_v1.md"
ARTIFACT = "A376"


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


def vector(values: list[dict[str, str]]) -> np.ndarray:
    return np.asarray([complex_value(value) for value in values], dtype=np.complex128)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dps", type=int, default=84)
    parser.add_argument("--order", type=int, default=30)
    parser.add_argument("--initial-step", type=float, default=0.012)
    parser.add_argument("--minimum-step", type=float, default=1.0e-10)
    parser.add_argument("--maximum-steps", type=int, default=30000)
    arguments = parser.parse_args()
    ctx.dps = arguments.dps

    base_lift = load(BASE_LIFT)
    if not base_lift["strict_scope"]["rank3_base_Abel_Jacobi_lift_interval_closed"]:
        raise AssertionError("rank-3 beta transport requires the certified n3 base lift")
    system = n3_engine.exact_target_system(arguments.dps)
    waypoints = [
        0 + 0j,
        0.65 + 0j,
        0.65 - 0.1j,
        0.82 - 0.1j,
        0.82 + 0j,
        1 + 0j,
    ]
    old_base_lift = validated.BASE_LIFT
    validated.BASE_LIFT = BASE_LIFT
    try:
        transport = validated.execute_validated_path(
            system,
            waypoints=waypoints,
            path_name="exact n3 selected local lower contour",
            order=arguments.order,
            initial_step=arguments.initial_step,
            minimum_step=arguments.minimum_step,
            maximum_steps=arguments.maximum_steps,
            checkpoint_path=None,
            resume=False,
        )
    finally:
        validated.BASE_LIFT = old_base_lift

    n3 = load(N3)
    candidates = [
        row
        for row in n3["candidate_residuals"]
        if int(row["A132_objective_rank"]) == 3
    ]
    if len(candidates) != 1:
        raise AssertionError("n3 probe no longer contains exactly one rank-3 row")
    candidate = candidates[0]
    floating_beta = vector(candidate["PL_corrected_moving_period"]) + vector(
        candidate["PL_corrected_residual"]
    )
    center = vector(transport["endpoint"]["beta_center"])
    radius = float(transport["endpoint"]["uniform_component_radius_upper"])
    real_differences = abs(floating_beta.real - center.real)
    imaginary_differences = abs(floating_beta.imag - center.imag)
    contained = np.logical_and(real_differences <= radius, imaginary_differences <= radius)
    if not bool(np.all(contained)):
        raise AssertionError(
            "independent n3 floating beta diagnostic left the certified endpoint box"
        )
    rows = []
    for residue_index in range(8):
        rows.append(
            {
                "residue_index_zero_based": residue_index,
                "interval_center": transport["endpoint"]["beta_center"][residue_index],
                "uniform_component_radius_upper": radius,
                "floating_value_diagnostic_only": {
                    "real": format(floating_beta[residue_index].real, ".17g"),
                    "imaginary": format(floating_beta[residue_index].imag, ".17g"),
                },
                "floating_real_center_difference": float(real_differences[residue_index]),
                "floating_imaginary_center_difference": float(
                    imaginary_differences[residue_index]
                ),
                "floating_value_contained": bool(contained[residue_index]),
                "minimum_component_containment_margin": float(
                    radius
                    - max(
                        real_differences[residue_index],
                        imaginary_differences[residue_index],
                    )
                ),
            }
        )

    original_scope = transport.pop("strict_scope")
    transport["schema"] = "MTTQ79HeightFourRank3AnchoredBetaInterval.v1"
    transport["status"] = "N3_RANK3_ANCHORED_BETA_ALL_EIGHT_INTERVAL_CERTIFIED"
    transport["artifact"] = ARTIFACT
    transport["selected_branch"] = {
        "base_lift_artifact": "A375",
        "base_winding_route": base_lift["branch_selection"]["route"],
        "contour": "local lower rectangle in t, positive horizontal detour in w",
        "waypoints": transport["method"]["waypoints"],
        "same_endpoint_convention_as_A219": True,
    }
    transport["all_eight_beta_rows"] = rows
    transport["summary"] = {
        "certified_rows": len(rows),
        "uniform_component_radius_upper": radius,
        "product_box_l2_radius_upper": float(np.sqrt(8.0) * radius),
        "maximum_floating_real_or_imaginary_center_difference": float(
            max(np.max(real_differences), np.max(imaginary_differences))
        ),
        "minimum_floating_containment_margin": min(
            row["minimum_component_containment_margin"] for row in rows
        ),
        "all_floating_diagnostics_contained": bool(np.all(contained)),
        "beta_zero_excluded": bool(transport["endpoint"]["zero_excluded"]),
    }
    transport["authority"] = {
        name: {"path": relative(path), "sha256": sha256(path)}
        for name, path in {
            "A375_rank3_base_lift": BASE_LIFT,
            "n3_ultra_probe": N3,
            "A219_profile_boundary": A219,
            "n3_exact_fibration": n3_engine.FIBRATION,
            "n3_interval_system": Path(n3_engine.__file__).resolve(),
            "validated_beta_transport_engine": Path(validated.__file__).resolve(),
            "builder_source": Path(__file__).resolve(),
        }.items()
    }
    transport["inherited_transport_scope"] = original_scope
    transport["strict_scope"] = {
        "observed_SM_values_used": False,
        "exact_n3_interval_system_used": True,
        "rank3_base_Abel_Jacobi_lift_interval_consumed": True,
        "selected_wall_free_contour_validated": True,
        "inhomogeneous_Gauss_Manin_transport_closed": True,
        "rank3_anchored_beta_interval_closed": True,
        "rank3_handle_combination_interval_closed": False,
        "interval_Jacobian_certificate": False,
        "covariant_zero_proved": False,
        "full_SM_closure_proved": False,
    }
    transport["next_required_artifact"] = (
        "combine the 76-target chain, selected handle, PL wall correction, and "
        "this beta interval; then execute the interval Jacobian/Newton gate"
    )
    dump(OUTPUT, transport)
    NOTE.write_text(
        "# MTT q79 Height-Four Rank-3 Anchored Beta Interval (A376) v1\n\n"
        "A376 starts from the A375 exact n3 Abel-Jacobi lift and validates the "
        "inhomogeneous Gauss-Manin transport on the selected local-lower contour. "
        "In the physical `w` coordinate this is the positive horizontal detour "
        "used to avoid the selected near-wall critical value.\n\n"
        f"All eight beta rows share component radius `{radius:.12g}`. Every "
        "independent floating endpoint diagnostic is contained, with minimum "
        "component margin "
        f"`{transport['summary']['minimum_floating_containment_margin']:.12g}`; "
        "the diagnostics are not used as bounds.\n\n"
        "This closes the moving anchored-beta block. The combined residual, "
        "interval Jacobian, and interval-Newton existence/uniqueness gate remain.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(OUTPUT)}")
    print(f"wrote {relative(NOTE)}")
    print(json.dumps(transport["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
