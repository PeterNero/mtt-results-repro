from __future__ import annotations

import hashlib
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import certify_q79_height4_target_main_hessian_interval as main_hessian
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
PACKET = VALIDATED / "ol" / "all76.a413.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def resolve(path: str) -> Path:
    return ROOT / Path(path)


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def main() -> int:
    packet = load(PACKET)
    manifest = load(A404)
    sweep = load(A405)
    transitions = load(A410)
    if packet.get("artifact") != "A413":
        raise AssertionError("A413 artifact changed")
    top = {
        "A404_common_junction_manifest": A404,
        "A405_entry_operators": A405,
        "A410_native_z_transitions": A410,
        "A411_terminal_trunk": A411,
        "A231_floating_chain_replay": A231,
        "A400_exact_relative_chain_identity": A400,
    }
    for label, path in top.items():
        if packet["authority"][label]["sha256"] != sha256(path):
            raise AssertionError(f"A413 authority is stale: {label}")
    entries = {
        int(row["distinguished_index"]): (entry_index, row)
        for entry_index, row in enumerate(manifest["ordered_entry_rows"])
        if row["kind"] == "selected_thimble_entry"
    }
    operators = {
        int(row["entry"]["distinguished_index"]): row
        for row in sweep["operators_at_77_entries"]
        if row["entry"]["kind"] == "selected_thimble_entry"
    }
    z_transitions = {
        int(row["distinguished_index"]): row
        for row in transitions["native_z_entry_transitions"]
    }
    floating_rows = {
        int(row["distinguished_index"]): row
        for row in load(A231)["exact_floating_decomposition"]["thimble_rows"]
    }
    rows = packet["target_rows"]
    if len(rows) != 76:
        raise AssertionError("A413 target count changed")
    charts = {"y": 0, "z": 0}
    maximum_cross = 0.0
    minimum_ratio = math.inf
    seen = set()
    orientation_reversals = 0
    wall_corrections = 0
    retained_checkpoints = 0
    legacy_sources = 0
    for row in rows:
        index = int(row["distinguished_index"])
        if index in seen:
            raise AssertionError("A413 repeats a target")
        seen.add(index)
        entry_index, entry = entries[index]
        if entry_index != int(row["A404_entry_index_zero_based"]):
            raise AssertionError(f"A413 d{index:03d} entry changed")
        raw = int(entry["signed_chain_coefficient"])
        orientation = int(row["canonical_cycle_to_floating_orientation_sign"])
        endpoint_coefficient = int(row["endpoint_floating_chain_coefficient"])
        wall_delta = int(row["Picard_Lefschetz_wall_delta"])
        corrected = int(row["PL_corrected_effective_chain_coefficient"])
        floating = floating_rows[index]
        if int(row["A130_raw_chain_coefficient"]) != raw:
            raise AssertionError(f"A413 d{index:03d} raw coefficient changed")
        if endpoint_coefficient != raw * orientation:
            raise AssertionError(f"A413 d{index:03d} orientation reconciliation changed")
        if wall_delta != (3 if index == 65 else 0) or corrected != endpoint_coefficient + wall_delta:
            raise AssertionError(f"A413 d{index:03d} wall reconciliation changed")
        if int(floating["chain_coefficient"]) != raw or int(floating["PL_corrected_effective_signed_coefficient"]) != corrected:
            raise AssertionError(f"A413 d{index:03d} A231 coefficient changed")
        orientation_reversals += int(orientation == -1)
        wall_corrections += int(wall_delta != 0)
        chart = row["line_chart"]
        charts[chart] += 1
        if (chart == "z") != (index in z_transitions):
            raise AssertionError(f"A413 d{index:03d} transition assignment changed")
        if int(operators[index]["entry_index_zero_based"]) != entry_index:
            raise AssertionError(f"A413 d{index:03d} operator changed")
        for authority in row["authority"].values():
            path = resolve(authority["path"])
            if authority["sha256"] != sha256(path):
                raise AssertionError(f"A413 d{index:03d} component authority is stale")
        main = load(resolve(row["authority"]["canonical_main"]["path"]))
        tail = load(resolve(row["authority"]["canonical_tail"]["path"]))
        full = load(resolve(row["authority"]["canonical_full"]["path"]))
        checkpoint_authority = row["authority"].get("completed_main_checkpoint")
        checkpoint = load(resolve(checkpoint_authority["path"])) if checkpoint_authority else None
        if checkpoint is not None:
            if not checkpoint.get("complete"):
                raise AssertionError(f"A413 d{index:03d} checkpoint is incomplete")
            retained_checkpoints += 1
        else:
            if index != 87 or not row["historical_completed_main_checkpoint_available"] is False:
                raise AssertionError(f"A413 d{index:03d} legacy checkpoint exception changed")
            legacy_sources += 1
        if len(main["near_node_direct_cycle_interval"]["initial_period_intervals"]) != 5:
            raise AssertionError(f"A413 d{index:03d} period source changed")
        if len(tail["all_eight_endpoint_tails"]["intervals"]) != 8 or len(full["residue_rows"]) != 8:
            raise AssertionError(f"A413 d{index:03d} residue source changed")
        _node, reconstructed_start = main_hessian.canonical_cutoff_start(main)
        start = complex_value(row["cutoff_start"])
        if abs(start - reconstructed_start) > 3.0e-14:
            raise AssertionError(f"A413 d{index:03d} cutoff reconstruction changed")
        endpoint = complex_value(row["A404_entry_point"])
        cross = abs(start.real * endpoint.imag - start.imag * endpoint.real) / (abs(start) * abs(endpoint))
        ratio = (start / endpoint).real
        if cross > 3.0e-14 or ratio <= 1.0:
            raise AssertionError(f"A413 d{index:03d} radial geometry changed")
        if not math.isclose(cross, float(row["normalized_radial_cross_error"]), rel_tol=2.0e-13, abs_tol=1.0e-30):
            raise AssertionError(f"A413 d{index:03d} cross diagnostic changed")
        if not math.isclose(ratio, float(row["outward_radial_ratio"]), rel_tol=2.0e-13):
            raise AssertionError(f"A413 d{index:03d} radial ratio changed")
        maximum_cross = max(maximum_cross, cross)
        minimum_ratio = min(minimum_ratio, ratio)
    if charts != {"y": 36, "z": 40} or seen != set(entries):
        raise AssertionError(f"A413 census changed: {charts}")
    summary = packet["summary"]
    if not math.isclose(maximum_cross, float(summary["maximum_normalized_radial_cross_error"]), rel_tol=2.0e-13, abs_tol=1.0e-30):
        raise AssertionError("A413 maximum cross does not replay")
    if not math.isclose(minimum_ratio, float(summary["minimum_outward_radial_ratio"]), rel_tol=2.0e-13):
        raise AssertionError("A413 minimum ratio does not replay")
    if orientation_reversals != int(summary["canonical_orientation_reversal_count"]):
        raise AssertionError("A413 orientation-reversal count does not replay")
    if wall_corrections != int(summary["Picard_Lefschetz_corrected_target_count"]):
        raise AssertionError("A413 wall-correction count does not replay")
    if retained_checkpoints != 75 or retained_checkpoints != int(summary["retained_historical_main_checkpoint_count"]):
        raise AssertionError("A413 retained-checkpoint census does not replay")
    if legacy_sources != 1 or legacy_sources != int(summary["reconstructible_legacy_source_without_checkpoint_count"]):
        raise AssertionError("A413 legacy-source census does not replay")
    scope = packet["strict_scope"]
    if not scope["all_76_native_cutoff_period_sources_present"] or not scope["all_76_A405_entry_operators_invertible"] or not scope["all_76_A130_to_floating_orientation_signs_reconciled"]:
        raise AssertionError("A413 source closure flags are false")
    if scope["outer_leg_numerical_transports_executed"] or scope["covariant_zero_proved"]:
        raise AssertionError("A413 overclaims execution")
    print(
        "PASS: A413 independently binds all 76 outer-leg source contracts "
        f"(36 y, 40 z); minimum radial ratio {minimum_ratio:.6g}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
