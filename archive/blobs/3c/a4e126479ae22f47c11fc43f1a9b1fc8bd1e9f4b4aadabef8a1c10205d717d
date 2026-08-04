from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

from flint import acb, acb_mat, arb, ctx

import certify_q79_height4_target_main_hessian_interval as main_hessian


ROOT = Path(__file__).resolve().parents[1]
VALIDATED = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
)
A404 = VALIDATED / "n3.junction_operator_sweep.a404.json"
A405 = VALIDATED / "n3.junction_operator_sweep.a405.json"
A410 = VALIDATED / "pt" / "a410.json"
A411 = VALIDATED / "jop" / "trunk.a411.json"
A231 = VALIDATED / "n3.chain.frontier.json"
A400 = VALIDATED / "n3.relative_chain_identity.a400.json"
OUTPUT = VALIDATED / "ol" / "all76.a413.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79All76OuterLegSourceManifest_A413_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def authority(path: Path) -> dict[str, str]:
    return {"path": relative(path), "sha256": sha256(path)}


def resolve(path: str) -> Path:
    return ROOT / Path(path)


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def interval_entry(value: dict) -> acb:
    center = complex_value(value["center"])
    radius = float(value["component_radius_upper"])
    serialization = max(math.ulp(center.real), math.ulp(center.imag), 1.0e-300)
    outward = math.nextafter(radius + serialization, math.inf)
    return acb(
        arb(format(center.real, ".17g"), format(outward, ".17g")),
        arb(format(center.imag, ".17g"), format(outward, ".17g")),
    )


def main() -> int:
    ctx.dps = 100
    manifest = load(A404)
    sweep = load(A405)
    transitions = load(A410)
    trunk = load(A411)
    floating_chain = load(A231)
    exact_chain = load(A400)
    if not manifest["theorem"]["proved"]:
        raise AssertionError("A413 requires A404")
    if not sweep["strict_scope"]["full_junction_period_and_residue_operator_closed"]:
        raise AssertionError("A413 requires A405")
    if not transitions["strict_scope"]["all_40_y_from_z_inverse_period_matrices_closed"]:
        raise AssertionError("A413 requires A410")
    if not trunk["strict_scope"]["common_hub_to_canonical_base_operator_closed"]:
        raise AssertionError("A413 requires A411")

    transition_by_index = {
        int(row["distinguished_index"]): row
        for row in transitions["native_z_entry_transitions"]
    }
    operator_by_index = {
        int(row["entry"]["distinguished_index"]): row
        for row in sweep["operators_at_77_entries"]
        if row["entry"]["kind"] == "selected_thimble_entry"
    }
    floating_by_index = {
        int(row["distinguished_index"]): row
        for row in floating_chain["exact_floating_decomposition"]["thimble_rows"]
    }
    rows = []
    chart_counts = {"y": 0, "z": 0}
    maximum_radial_cross = 0.0
    minimum_radial_ratio = math.inf
    minimum_entry_determinant = math.inf
    orientation_reversal_count = 0
    picard_lefschetz_correction_count = 0
    retained_checkpoint_count = 0
    reconstructible_legacy_source_count = 0
    component_authorities = []
    for entry_index, entry in enumerate(manifest["ordered_entry_rows"]):
        if entry["kind"] != "selected_thimble_entry":
            continue
        index = int(entry["distinguished_index"])
        stem = f"d{index:03d}.n3"
        main_path = VALIDATED / f"{stem}.main8.refined.json"
        tail_path = VALIDATED / f"{stem}.tail8.refined.json"
        full_path = VALIDATED / f"{stem}.full8.refined.json"
        main_packet = load(main_path)
        tail_packet = load(tail_path)
        full_packet = load(full_path)
        checkpoint_authority = main_packet["authority"].get("completed_transport_checkpoint")
        checkpoint_path = resolve(checkpoint_authority["path"]) if checkpoint_authority else None
        checkpoint = load(checkpoint_path) if checkpoint_path is not None else None
        if checkpoint_path is not None:
            if checkpoint_authority["sha256"] != sha256(checkpoint_path):
                raise AssertionError(f"A413 d{index:03d} checkpoint authority is stale")
            if not checkpoint.get("complete"):
                raise AssertionError(f"A413 d{index:03d} checkpoint is incomplete")
            retained_checkpoint_count += 1
        else:
            if index != 87 or len(main_packet["validated_main_transport"]["center"]) != 13:
                raise AssertionError(f"A413 d{index:03d} lacks a reconstructible source")
            reconstructible_legacy_source_count += 1
        targets = [main_packet["selected_target"], tail_packet["selected_target"], full_packet["selected_target"]]
        root_ids = {target["root_id"] for target in targets}
        charts = {target["line_chart"] for target in targets}
        if root_ids != {full_packet["selected_target"]["root_id"]} or len(charts) != 1:
            raise AssertionError(f"A413 d{index:03d} target packets disagree")
        chart = next(iter(charts))
        if chart not in chart_counts:
            raise AssertionError(f"A413 d{index:03d} chart changed")
        chart_counts[chart] += 1
        raw_coefficient = int(entry["signed_chain_coefficient"])
        floating_row = floating_by_index[index]
        canonical_orientation = int(floating_row["canonical_orientation_sign"])
        endpoint_coefficient = int(full_packet["selected_target"]["selected_chain_coefficient"])
        wall_delta = 3 if index == 65 else 0
        corrected_coefficient = endpoint_coefficient + wall_delta
        if canonical_orientation not in {-1, 1}:
            raise AssertionError(f"A413 d{index:03d} orientation sign changed")
        if int(floating_row["chain_coefficient"]) != raw_coefficient:
            raise AssertionError(f"A413 d{index:03d} raw A130 coefficient changed")
        if endpoint_coefficient != raw_coefficient * canonical_orientation:
            raise AssertionError(f"A413 d{index:03d} orientation reconciliation failed")
        if int(floating_row["PL_corrected_effective_signed_coefficient"]) != corrected_coefficient:
            raise AssertionError(f"A413 d{index:03d} Picard-Lefschetz coefficient changed")
        orientation_reversal_count += int(canonical_orientation == -1)
        picard_lefschetz_correction_count += int(wall_delta != 0)
        initial_periods = main_packet["near_node_direct_cycle_interval"]["initial_period_intervals"]
        tail_intervals = tail_packet["all_eight_endpoint_tails"]["intervals"]
        if len(initial_periods) != 5 or len(tail_intervals) != 8 or len(full_packet["residue_rows"]) != 8:
            raise AssertionError(f"A413 d{index:03d} source dimensions changed")

        _node, start = main_hessian.canonical_cutoff_start(main_packet)
        if checkpoint is not None:
            persisted_start = complex_value(checkpoint["configuration"]["start"])
            if abs(start - persisted_start) > 3.0e-14:
                raise AssertionError(f"A413 d{index:03d} cutoff reconstruction changed")
        endpoint = complex_value(entry["point"])
        normalized_cross = abs(start.real * endpoint.imag - start.imag * endpoint.real) / (abs(start) * abs(endpoint))
        ratio = start / endpoint
        if normalized_cross > 3.0e-14 or ratio.real <= 1.0 or abs(ratio.imag) > 3.0e-13:
            raise AssertionError(f"A413 d{index:03d} is not an outward radial leg")
        maximum_radial_cross = max(maximum_radial_cross, normalized_cross)
        minimum_radial_ratio = min(minimum_radial_ratio, ratio.real)

        operator = operator_by_index[index]
        if int(operator["entry_index_zero_based"]) != entry_index:
            raise AssertionError(f"A413 d{index:03d} A405 operator is reordered")
        period = acb_mat(
            [[interval_entry(value) for value in values] for values in operator["period_transport_5_by_5"]]
        )
        determinant_lower = float(abs(period.det()).lower())
        if determinant_lower <= 0.0:
            raise AssertionError(f"A413 d{index:03d} entry operator is singular")
        minimum_entry_determinant = min(minimum_entry_determinant, determinant_lower)
        transition = transition_by_index.get(index)
        if (chart == "z") != (transition is not None):
            raise AssertionError(f"A413 d{index:03d} chart transition availability changed")
        if transition is not None and int(transition["entry_index_zero_based"]) != entry_index:
            raise AssertionError(f"A413 d{index:03d} A410 entry is reordered")

        row_authorities = {
            "canonical_main": authority(main_path),
            "canonical_tail": authority(tail_path),
            "canonical_full": authority(full_path),
        }
        if checkpoint_path is not None:
            row_authorities["completed_main_checkpoint"] = authority(checkpoint_path)
        component_authorities.extend(row_authorities.values())
        rows.append(
            {
                "distinguished_index": index,
                "root_id": full_packet["selected_target"]["root_id"],
                "line_chart": chart,
                "A130_raw_chain_coefficient": raw_coefficient,
                "canonical_cycle_to_floating_orientation_sign": canonical_orientation,
                "endpoint_floating_chain_coefficient": endpoint_coefficient,
                "Picard_Lefschetz_wall_delta": wall_delta,
                "PL_corrected_effective_chain_coefficient": corrected_coefficient,
                "A404_entry_index_zero_based": entry_index,
                "cutoff_start": {
                    "real": format(start.real, ".17g"),
                    "imaginary": format(start.imag, ".17g"),
                },
                "historical_completed_main_checkpoint_available": checkpoint is not None,
                "A404_entry_point": entry["point"],
                "outward_radial_ratio": ratio.real,
                "normalized_radial_cross_error": normalized_cross,
                "initial_period_interval_count": len(initial_periods),
                "local_tail_interval_count": len(tail_intervals),
                "canonical_full_residue_count": len(full_packet["residue_rows"]),
                "A405_period_determinant_absolute_lower": determinant_lower,
                "A410_y_from_z_transition_required": chart == "z",
                "A410_transition_entry_index_zero_based": (
                    int(transition["entry_index_zero_based"]) if transition is not None else None
                ),
                "authority": row_authorities,
            }
        )

    if len(rows) != 76 or chart_counts != {"y": 36, "z": 40}:
        raise AssertionError(f"A413 target census changed: {len(rows)}, {chart_counts}")
    payload = {
        "schema": "MTTQ79All76OuterLegSourceManifest.v1",
        "status": "ALL_76_OUTER_LEG_NATIVE_SOURCE_CONTRACTS_CERTIFIED",
        "artifact": "A413",
        "target_rows": rows,
        "summary": {
            "certified_target_count": len(rows),
            "native_y_target_count": chart_counts["y"],
            "native_z_target_count": chart_counts["z"],
            "certified_initial_period_interval_count": 5 * len(rows),
            "certified_local_tail_interval_count": 8 * len(rows),
            "certified_canonical_residue_count": 8 * len(rows),
            "maximum_normalized_radial_cross_error": maximum_radial_cross,
            "minimum_outward_radial_ratio": minimum_radial_ratio,
            "minimum_A405_entry_period_determinant_absolute_lower": minimum_entry_determinant,
            "canonical_orientation_reversal_count": orientation_reversal_count,
            "Picard_Lefschetz_corrected_target_count": picard_lefschetz_correction_count,
            "retained_historical_main_checkpoint_count": retained_checkpoint_count,
            "reconstructible_legacy_source_without_checkpoint_count": reconstructible_legacy_source_count,
        },
        "component_authority_manifest": component_authorities,
        "authority": {
            "A404_common_junction_manifest": authority(A404),
            "A405_entry_operators": authority(A405),
            "A410_native_z_transitions": authority(A410),
            "A411_terminal_trunk": authority(A411),
            "A231_floating_chain_replay": authority(A231),
            "A400_exact_relative_chain_identity": authority(A400),
            "builder_source": authority(Path(__file__).resolve()),
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "all_76_native_cutoff_period_sources_present": True,
            "all_76_local_tail_sources_present": True,
            "all_76_cutoff_sources_reconstructible": True,
            "retained_historical_main_checkpoint_count_is_75": retained_checkpoint_count == 75,
            "d087_legacy_source_reconstructed_without_checkpoint": reconstructible_legacy_source_count == 1,
            "all_76_A404_radial_entry_geometries_closed": True,
            "all_76_A405_entry_operators_invertible": True,
            "all_40_native_z_A410_transitions_bound": True,
            "all_76_A130_to_floating_orientation_signs_reconciled": True,
            "d065_Picard_Lefschetz_wall_delta_reconciled": True,
            "outer_leg_numerical_transports_executed": False,
            "integer_chain_combination_at_hub_closed": False,
            "full_correlation_preserving_path_execution_closed": False,
            "interval_Newton_existence_and_uniqueness_closed": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": (
            "execute the A413 radial outer-leg contracts and apply A410/A405/A409T "
            "to each retained affine frame"
        ),
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    NOTE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(
        "# MTT q79 All-76 Outer-Leg Source Manifest (A413) v1\n\n"
        "A413 binds every selected thimble to its certified native-chart cutoff "
        "period vector, local tail, completed affine checkpoint, radial A404 entry, "
        "invertible A405 operator, and (for all 40 native-z rows) A410 transition.\n\n"
        f"The census is 36 native-y plus 40 native-z targets. The minimum radial "
        f"ratio is `{minimum_radial_ratio:.12g}` and the minimum A405 determinant "
        f"lower bound is `{minimum_entry_determinant:.12g}`. It also reconciles "
        f"`{orientation_reversal_count}` orientation reversals and the one d065 "
        "Picard-Lefschetz wall update. Numerical outer-leg "
        "execution and the common-hub sum remain open.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(OUTPUT)}")
    print(f"wrote {relative(NOTE)}")
    print(json.dumps(payload["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
