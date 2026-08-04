from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
VALIDATED = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
)
SOURCE = VALIDATED / "far_source" / "d057.1em03.json"
A404 = VALIDATED / "n3.junction_operator_sweep.a404.json"
CANONICAL_MAIN = VALIDATED / "d057.n3.main8.refined.json"
DIRECTORY = VALIDATED / "ol"
CHECKPOINT = DIRECTORY / "d057.a409o.ckpt.json"
PACKET = DIRECTORY / "d057.a409o.json"
BUILDER = ROOT / "scripts" / "run_q79_d057_far_cut_outer_leg_to_a404.py"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    packet = load(PACKET)
    source = load(SOURCE)
    manifest = load(A404)
    canonical = load(CANONICAL_MAIN)
    checkpoint = load(CHECKPOINT)
    require(packet["artifact"] == "A409O", "A409O artifact changed")
    require(packet["schema"] == "MTTQ79HeightFourD057OuterLegToA404.v1", "A409O schema changed")
    target = packet["selected_target"]
    require(int(target["distinguished_index"]) == 57, "A409O target changed")
    require(target["root_id"] == "selected_008" and target["line_chart"] == "y", "A409O branch changed")
    require(int(target["signed_chain_coefficient"]) == 4, "A409O coefficient changed")
    require(float(target["endpoint_cutoff_epsilon"]) == 1.0e-3, "A409O cutoff changed")
    require(int(target["orientation_sign"]) == int(canonical["orientation"]["selected_sign"]), "A409O orientation changed")
    require(source["artifact"] == "A380FS", "A409O source changed")

    entry_index = int(packet["A404_entry"]["entry_index_zero_based"])
    entry = manifest["ordered_entry_rows"][entry_index]
    require(int(entry["distinguished_index"]) == 57, "A409O entry target changed")
    require(entry["point"] == packet["A404_entry"]["point"], "A409O entry point changed")
    endpoint = complex_value(entry["point"])
    start = complex_value(source["far_cut_source"]["cutoff_start_binary64"])
    require(math.isclose(abs(endpoint), 0.1, rel_tol=2.0e-15, abs_tol=2.0e-15), "A409O entry radius changed")
    require(abs(start.real * endpoint.imag - start.imag * endpoint.real) <= 2.0e-15 * abs(start) * abs(endpoint), "A409O leg is not radial")

    execution = packet["validated_outer_main_transport"]
    steps = execution["steps"]
    require(int(execution["accepted_step_count"]) == len(steps) and len(steps) > 0, "A409O step count changed")
    require(math.isclose(float(steps[-1]["end_arclength"]), float(execution["path_length"]), rel_tol=2.0e-15, abs_tol=1.0e-15), "A409O path incomplete")
    require(checkpoint["complete"], "A409O checkpoint incomplete")
    configuration = checkpoint["configuration"]
    require(complex_value(configuration["start"]) == start, "A409O checkpoint start changed")
    require(complex_value(configuration["endpoint"]) == endpoint, "A409O checkpoint endpoint changed")
    require(checkpoint["A409O_builder_sha256"] == sha256(BUILDER), "A409O builder stamp changed")
    require(checkpoint["A409O_A380FS_sha256"] == sha256(SOURCE), "A409O source stamp changed")
    require(checkpoint["A409O_A404_sha256"] == sha256(A404), "A409O manifest stamp changed")

    center = np.asarray([complex_value(value) for value in execution["center"]])
    orientation = int(target["orientation_sign"])
    periods = np.asarray([complex_value(value) for value in packet["selected_entry_period_centers"]])
    residues = np.asarray([complex_value(value) for value in packet["selected_outer_main_residue_centers"]])
    require(float(np.max(abs(periods - orientation * center[:5]))) < 2.0e-14, "A409O period centers changed")
    require(float(np.max(abs(residues + orientation * center[5:]))) < 2.0e-14, "A409O residue centers changed")
    radii = np.asarray(packet["residue_coordinate_radius_uppers"], dtype=np.float64)
    require(radii.shape == (8,) and bool(np.all(np.isfinite(radii))) and bool(np.all(radii >= 0.0)), "A409O radii invalid")
    require(math.isclose(float(np.max(radii)), float(execution["uniform_integral_radius_upper"]), rel_tol=2.0e-14), "A409O maximum radius changed")

    for label, authority in packet["authority"].items():
        path = ROOT / authority["path"]
        require(path.is_file(), f"A409O authority missing: {label}")
        require(sha256(path) == authority["sha256"], f"A409O authority stale: {label}")
    scope = packet["strict_scope"]
    for key in (
        "same_selected_d057_far_cut_source_used",
        "same_A404_radial_entry_used",
        "full_correlated_checkpoint_frames_retained",
        "outer_main_leg_to_common_entry_closed",
    ):
        require(scope[key], f"A409O strict gate false: {key}")
    require(not scope["matching_local_Frobenius_tail_attached"], "A409O overclaims its tail")
    require(not scope["A405_entry_operator_applied"], "A409O overclaims A405")
    require(not scope["integer_chain_combination_at_hub_closed"], "A409O overclaims hub closure")
    require(not scope["full_correlation_preserving_path_execution_closed"], "A409O overclaims full transport")
    require(not scope["interval_Newton_existence_and_uniqueness_closed"], "A409O overclaims Newton")
    require(not scope["covariant_zero_proved"], "A409O overclaims a zero")
    require(not scope["full_SM_closure_proved"], "A409O overclaims SM closure")
    require(not scope["observed_SM_values_used"], "observed SM data entered A409O")
    print(f"PASS: A409O replays the d057 cutoff-to-A404 outer leg with {len(steps)} validated steps")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
