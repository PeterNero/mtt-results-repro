from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

from flint import acb, arb, ctx

import certify_q79_selected_alignment_E32_handle_combination_interval as handle
import certify_q79_selected_side_beta_defect_transport as validated


ROOT = Path(__file__).resolve().parents[1]
PERIOD_DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
)
A133 = PERIOD_DIRECTORY / "selected_alignment_height4_frozen_carrier_refinement_and_interval_cutset.packet.json"
A134 = PERIOD_DIRECTORY / "selected_alignment_height4_E32_handle_interval_and_thimble_cutset.packet.json"
HANDLE = PERIOD_DIRECTORY / "selected_alignment_E32_handle_combination.interval.packet.json"
ORIENTATION = PERIOD_DIRECTORY / "selected_alignment_thimble_orientation_synchronization.packet.json"
BETA = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2delignebetaperiodandintegralbranchexecution"
    / "pgl3_selected_side_beta.local_lower.order40_step003.interval.packet.json"
)
DEFAULT_OUTPUT = PERIOD_DIRECTORY / "selected_alignment_E32_weighted_71_thimble_and_frozen_carrier_decision.packet.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def serialized_disk(center: dict[str, str], radius: float) -> tuple[acb, float]:
    real = float(center["real"])
    imaginary = float(center["imaginary"])
    serialization = max(2.0 * math.ulp(real), 2.0 * math.ulp(imaginary))
    inflated = radius + serialization
    return (
        acb(
            arb(center["real"], format(inflated, ".17g")),
            arb(center["imaginary"], format(inflated, ".17g")),
        ),
        serialization,
    )


def exact_point(center: dict[str, str]) -> acb:
    return acb(center["real"], center["imaginary"])


def coordinate_zero_exclusion(value: acb) -> dict[str, object]:
    rows = []
    for name, component in (("real", value.real), ("imaginary", value.imag)):
        lower = float(component.lower())
        upper = float(component.upper())
        if lower > 0.0:
            distance = math.nextafter(lower, -math.inf)
            side = "positive"
        elif upper < 0.0:
            distance = math.nextafter(-upper, -math.inf)
            side = "negative"
        else:
            distance = 0.0
            side = "contains_zero"
        rows.append(
            {
                "component": name,
                "lower": lower,
                "upper": upper,
                "side": side,
                "zero_distance_lower": distance,
            }
        )
    winner = max(rows, key=lambda row: float(row["zero_distance_lower"]))
    return {
        "coordinate_bounds": rows,
        "separating_component": winner["component"],
        "absolute_value_lower": winner["zero_distance_lower"],
        "zero_excluded": float(winner["zero_distance_lower"]) > 0.0,
    }


def full_packet_path(index: int, root_id: str) -> Path:
    return PERIOD_DIRECTORY / f"d{index:03d}_{root_id}.E32_full.interval.packet.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Sum all 71 certified q79 E32 thimbles and decide the frozen carrier."
    )
    parser.add_argument("--artifact", default="A207")
    parser.add_argument("--predecessor", required=True)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--dps", type=int, default=100)
    return parser.parse_args()


def main() -> int:
    arguments = parse_args()
    ctx.dps = arguments.dps
    artifact = arguments.artifact.upper()
    predecessor_path = ROOT / arguments.predecessor
    predecessor = load(predecessor_path)
    a133 = load(A133)
    a134 = load(A134)
    handle_packet = load(HANDLE)
    orientation_packet = load(ORIENTATION)
    beta_packet = load(BETA)

    ledger = predecessor["weighted_budget_ledger"]
    if (
        int(ledger["selected_support_closed"]),
        int(ledger["selected_support_total"]),
        int(ledger["selected_l1_closed"]),
        int(ledger["selected_l1_total"]),
        int(ledger["remaining_support"]),
        int(ledger["remaining_l1_weight"]),
    ) != (71, 71, 123, 123, 0, 0):
        raise AssertionError("predecessor is not the complete 71/123 append ledger")
    if predecessor["clearance_ranked_queues"]["y"] or predecessor["clearance_ranked_queues"]["z"]:
        raise AssertionError("ranked queues remain nonempty")
    if predecessor["partial_interval_diagnostics"]:
        raise AssertionError("partial interval diagnostics remain")

    manifest = a134["selected_E32_decomposition"]["primitive_thimble_chain"]
    accepted = predecessor["accepted_full_intervals"]
    coefficient_by_index = {
        int(item["distinguished_index"]): int(item["coefficient"])
        for item in manifest
    }
    accepted_by_index = {
        int(item["distinguished_index"]): item for item in accepted
    }
    if len(manifest) != 71 or len(accepted) != 71 or set(coefficient_by_index) != set(accepted_by_index):
        raise AssertionError("accepted support differs from the A134 manifest")
    if sum(abs(value) for value in coefficient_by_index.values()) != 123:
        raise AssertionError("A134 primitive coefficient norm changed")
    orientation_signs = [int(value) for value in orientation_packet["column_signs"]]
    if len(orientation_signs) != 90 or any(value not in (-1, 1) for value in orientation_signs):
        raise AssertionError("A131 canonical thimble orientation table changed")
    if not orientation_packet["strict_scope"]["all_90_A130_canonical_vanishing_vectors_used"]:
        raise AssertionError("A130 canonical orientation source is incomplete")

    weighted_thimble = acb(0)
    authority_paths = {A133, A134, HANDLE, ORIENTATION, BETA, predecessor_path, Path(__file__)}
    summands = []
    for manifest_row in manifest:
        index = int(manifest_row["distinguished_index"])
        coefficient = int(manifest_row["coefficient"])
        accepted_row = accepted_by_index[index]
        if int(accepted_row["coefficient"]) != coefficient:
            raise AssertionError(f"d{index:03d} coefficient mismatch")
        full_path = full_packet_path(index, accepted_row["root_id"])
        full = load(full_path)
        authority_paths.add(full_path)
        if not full["scope"]["single_full_E32_thimble_interval_closed"]:
            raise AssertionError(f"d{index:03d} full interval gate is open")
        if not full["A134_radius_ledger"]["fallback_met"]:
            raise AssertionError(f"d{index:03d} fallback gate is open")
        interval = validated.interval_from_bounds(full["full_E32_thimble"]["interval"])
        canonical_orientation_sign = orientation_signs[index - 1]
        oriented_coefficient = coefficient * canonical_orientation_sign
        weighted_thimble += acb(oriented_coefficient) * interval
        summands.append(
            {
                "distinguished_index": index,
                "root_id": accepted_row["root_id"],
                "coefficient": coefficient,
                "canonical_orientation_sign": canonical_orientation_sign,
                "oriented_raw_interval_coefficient": oriented_coefficient,
                "full_interval_path": relative(full_path),
                "full_interval_sha256": sha256(full_path),
                "full_interval_radius_upper": validated.radius_upper(interval),
            }
        )

    decomposition = a134["selected_E32_decomposition"]
    a131_thimble = exact_point(decomposition["A131_floating_thimble_combination_center"])
    a131_full = exact_point(decomposition["A131_full_combination_center"])
    thimble_center_difference = abs(handle.midpoint(weighted_thimble) - handle.midpoint(a131_thimble))
    thimble_radius = validated.radius_upper(weighted_thimble)
    direct_thimble_cost = thimble_center_difference + thimble_radius
    if not weighted_thimble.contains(a131_thimble):
        raise AssertionError("weighted thimble ball does not contain the independent A131 center")
    if direct_thimble_cost >= float(a134["strict_budget_ledger"]["remaining_weighted_thimble_combination_radius_budget"]):
        raise AssertionError("direct weighted thimble ball exceeds the A134 budget")
    if direct_thimble_cost > float(ledger["certified_radius_plus_displacement_cost"]):
        raise AssertionError("direct weighted cost exceeds the append triangle ledger")

    handle_row = handle_packet["E32_handle_combination"]
    handle_ball, handle_serialization = serialized_disk(
        handle_row["interval"]["center"],
        float(handle_row["interval"]["uniform_radius_upper"]),
    )
    combined_period = weighted_thimble + handle_ball
    if not combined_period.contains(a131_full):
        raise AssertionError("combined period ball does not contain the A131 full center")
    combined_center_difference = abs(handle.midpoint(combined_period) - handle.midpoint(a131_full))
    combined_radius = validated.radius_upper(combined_period)
    combined_cost = combined_center_difference + combined_radius
    strict_period_budget = float(a133["minimal_strict_interval_target"]["strict_required_period_combination_radius_upper"])
    if combined_cost >= strict_period_budget:
        raise AssertionError("combined period ball does not meet the A133 strict separation budget")

    target = a133["minimal_strict_interval_target"]
    target_index = int(target["row_index"])
    if target["form"] != "E32" or target_index != 5:
        raise AssertionError("A133 separating row changed")
    beta_endpoint = beta_packet["endpoint"]
    beta_center = beta_endpoint["beta_center"][target_index]
    beta_radius = float(beta_endpoint["uniform_component_radius_upper"])
    beta_serialization = float(beta_endpoint["center_serialization_radius_upper"])
    beta_ball, beta_roundtrip = serialized_disk(beta_center, beta_radius + beta_serialization)
    residual = beta_ball - combined_period
    residual_radius = validated.radius_upper(residual)
    separation = coordinate_zero_exclusion(residual)
    residual_modulus_lower = float(separation["absolute_value_lower"])
    zero_excluded = not residual.contains(acb(0)) and bool(separation["zero_excluded"])
    if not zero_excluded:
        raise AssertionError("the final E32 residual interval does not exclude zero")

    output = arguments.output if arguments.output.is_absolute() else ROOT / arguments.output
    payload = {
        "schema": "MTTQ79SelectedE32Weighted71ThimbleAndFrozenCarrierDecision.v1",
        "artifact": artifact,
        "status": "WEIGHTED_71_THIMBLE_E32_INTERVAL_CLOSED_FROZEN_CARRIER_EXACTLY_SEPARATED",
        "authority": [
            {"path": relative(path), "sha256": sha256(path)}
            for path in sorted(authority_paths, key=relative)
        ],
        "selected_manifest": {
            "support": 71,
            "coefficient_l1_norm": 123,
            "canonical_orientation_identity": (
                "the certified interval packets enclose raw holomorphic thimbles; "
                "the A130/A131 integral basis uses sigma_d times each raw thimble"
            ),
            "canonical_orientation_source": relative(ORIENTATION),
            "summands": summands,
        },
        "weighted_thimble_combination": {
            "identity": "T_E32 = sum_d c_d sigma_d Pi_E32,d(raw)",
            "interval": handle.complex_interval(weighted_thimble),
            "interval_center": handle.complex_pair(handle.midpoint(weighted_thimble)),
            "interval_radius_upper": thimble_radius,
            "A131_floating_center": decomposition["A131_floating_thimble_combination_center"],
            "A131_center_difference": thimble_center_difference,
            "A131_center_contained": True,
            "direct_radius_plus_displacement_cost": direct_thimble_cost,
            "append_triangle_cost_upper": ledger["certified_radius_plus_displacement_cost"],
            "A134_remaining_budget": a134["strict_budget_ledger"]["remaining_weighted_thimble_combination_radius_budget"],
        },
        "handle_combination": {
            "interval_center": handle_row["interval"]["center"],
            "source_radius_upper": handle_row["interval"]["uniform_radius_upper"],
            "serialization_inflation": handle_serialization,
            "inflated_interval_radius_upper": validated.radius_upper(handle_ball),
        },
        "full_selected_period_combination": {
            "identity": "P_E32 = T_E32 + H_E32",
            "interval": handle.complex_interval(combined_period),
            "interval_center": handle.complex_pair(handle.midpoint(combined_period)),
            "interval_radius_upper": combined_radius,
            "A131_floating_center": decomposition["A131_full_combination_center"],
            "A131_center_difference": combined_center_difference,
            "A131_center_contained": True,
            "radius_plus_displacement_cost": combined_cost,
            "A133_strict_period_budget": strict_period_budget,
            "strict_budget_met": True,
        },
        "refined_beta_E32": {
            "interval_center": beta_center,
            "source_uniform_component_radius_upper": beta_radius,
            "source_center_serialization_radius_upper": beta_serialization,
            "roundtrip_serialization_inflation": beta_roundtrip,
            "inflated_interval_radius_upper": validated.radius_upper(beta_ball),
        },
        "frozen_carrier_residual": {
            "identity": "R_E32 = beta_E32 - P_E32",
            "interval": handle.complex_interval(residual),
            "interval_center": handle.complex_pair(handle.midpoint(residual)),
            "interval_radius_upper": residual_radius,
            "absolute_value_lower": residual_modulus_lower,
            "absolute_value_lower_method": "distance of a sign-separated rectangular ACB coordinate from zero",
            "separating_component": separation["separating_component"],
            "coordinate_bounds": separation["coordinate_bounds"],
            "zero_excluded": True,
            "decision": (
                "the frozen height-four carrier is rigorously separated from "
                "the selected-alignment equation F(A,m)=0 in the E32 row"
            ),
        },
        "scope": {
            "observed_SM_values_used": False,
            "all_71_single_thimble_intervals_closed": True,
            "selected_thimble_combination_interval_closed": True,
            "full_E32_combined_period_interval_closed": True,
            "weighted_71_thimble_interval_closed": True,
            "fixed_carrier_exact_separation_closed": True,
            "frozen_height_four_carrier_rejected_by_E32_zero_exclusion": True,
            "covariant_alignment_zero_solved_on_this_carrier": False,
            "all_other_carriers_decided": False,
        },
        "next_required_artifact": (
            "remove the rejected frozen height-four carrier from the covariant carrier search "
            "and continue only on the remaining selected carrier branches"
        ),
    }
    dump(output, payload)

    note_path = ROOT / "proof_corpus" / f"MTT_Selected_q79E32Weighted71ThimbleAndFrozenCarrierDecision_{artifact}_v1.md"
    candidate_path = ROOT / "candidate_data" / "selected_q79e32weighted71thimbleandfrozencarrierdecision.candidate.json"
    certificate_path = ROOT / "certificates" / "selected_q79e32weighted71thimbleandfrozencarrierdecision.certificate.json"
    note = f"""# MTT Selected q79 E32 Weighted 71-Thimble and Frozen-Carrier Decision {artifact} v1

## Theorem

For the frozen selected height-four carrier, the exact A134 integer chain of 71
certified E32 thimble balls has coefficient L1 norm 123. The packets enclose
raw holomorphic thimbles, so each integer coefficient is multiplied by the
already frozen A130/A131 canonical orientation sign `sigma_d`. The resulting
weighted interval, added to the independently certified handle interval and
subtracted from the refined selected-side beta interval, excludes zero.

```text
weighted thimble radius = {thimble_radius:.16g}
weighted thimble center displacement = {thimble_center_difference:.16g}
combined period radius + displacement = {combined_cost:.16g}
A133 strict period budget = {strict_period_budget:.16g}
final residual radius = {residual_radius:.16g}
final residual absolute-value lower bound = {residual_modulus_lower:.16g}
separating rectangular coordinate = {separation['separating_component']}
```

Therefore the weighted 71-thimble interval is closed and the frozen height-four
carrier is rigorously separated from `F(A,m)=0` in the E32 row. This rejects
that carrier; it does not assert that another carrier solves the full covariant
alignment system. The lower bound uses the sign-separated rectangular ACB
coordinate directly; it does not rely on Arb's coarser generic complex-modulus
enclosure.
"""
    note_path.write_text(note, encoding="utf-8")
    candidate = {
        "schema": "MTTSelectedQ79E32Weighted71ThimbleAndFrozenCarrierDecision.v1",
        "artifact": artifact,
        "status": payload["status"],
        "packet": relative(output),
        "packet_sha256": sha256(output),
        "note": relative(note_path),
        "note_sha256": sha256(note_path),
        "observed_SM_values_used": False,
        "weighted_71_thimble_interval_closed": True,
        "fixed_carrier_exact_separation_closed": True,
        "closure_claimed": True,
    }
    dump(candidate_path, candidate)
    certificate = {
        "schema": "MTTCertificate.v1",
        "certificate": "MTTSelectedQ79E32Weighted71ThimbleAndFrozenCarrierDecision",
        "artifact": artifact,
        "status": payload["status"],
        "candidate_path": relative(candidate_path),
        "candidate_sha256": sha256(candidate_path),
        "observed_SM_values_used": False,
        "selected_support": 71,
        "selected_coefficient_l1_norm": 123,
        "weighted_71_thimble_interval_closed": True,
        "fixed_carrier_exact_separation_closed": True,
        "residual_zero_excluded": True,
        "closure_claimed": True,
    }
    dump(certificate_path, certificate)
    for path in (output, note_path, candidate_path, certificate_path):
        print(f"wrote {relative(path)}")
    print(
        json.dumps(
            {
                "artifact": artifact,
                "weighted_thimble_radius": thimble_radius,
                "weighted_thimble_center_difference": thimble_center_difference,
                "combined_period_cost": combined_cost,
                "strict_period_budget": strict_period_budget,
                "residual_radius": residual_radius,
                "residual_absolute_value_lower": residual_modulus_lower,
                "zero_excluded": True,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
