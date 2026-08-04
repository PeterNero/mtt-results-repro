from __future__ import annotations

import hashlib
import json
import math
import sys
from pathlib import Path

from flint import acb, acb_mat, ctx


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import certify_q79_height4_d087_full_residue_main_interval as n3_engine
import certify_q79_selected_side_beta_defect_transport as validated


VALIDATED = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
)
A404 = VALIDATED / "n3.junction_operator_sweep.a404.json"
PACKET = VALIDATED / "pt" / "a410.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def decoded_matrix(value: list[list[dict]]) -> acb_mat:
    return acb_mat(
        [
            [validated.interval_from_bounds(entry["interval_bounds"]) for entry in row]
            for row in value
        ]
    )


def main() -> int:
    ctx.dps = 100
    packet = load(PACKET)
    manifest = load(A404)
    require(packet["artifact"] == "A410", "A410 artifact changed")
    require(packet["schema"] == "MTTQ79HeightFourA404ProjectivePeriodTransitions.v1", "A410 schema changed")
    require(packet["formula"]["direction_for_common_A405_frame"] == "p_y=T^{-1}p_z", "A410 direction changed")
    rows = packet["native_z_entry_transitions"]
    require(len(rows) == 40, "A410 native-z count changed")
    system = n3_engine.exact_target_system(100)
    minimum_ell_1 = math.inf
    minimum_ell_2 = math.inf
    minimum_determinant = math.inf
    seen = set()
    for row in rows:
        entry_index = int(row["entry_index_zero_based"])
        index = int(row["distinguished_index"])
        require(index not in seen, "A410 duplicated a target")
        seen.add(index)
        entry = manifest["ordered_entry_rows"][entry_index]
        require(int(entry["distinguished_index"]) == index, "A410 entry mapping changed")
        require(entry["point"] == row["entry_point"], "A410 entry point changed")
        canonical_path = ROOT / row["canonical_target_path"]
        canonical = load(canonical_path)
        require(canonical["selected_target"]["line_chart"] == "z", "A410 included a native-y target")
        require(sha256(canonical_path) == row["canonical_target_sha256"], "A410 target authority stale")
        parameter = complex_value(entry["point"])
        _a, _b, line, _line_w = system.ab_line_data(
            acb(format(parameter.real, ".17g"), format(parameter.imag, ".17g"))
        )
        stored_line = [validated.interval_from_bounds(value["interval_bounds"]) for value in row["line_coordinates"]]
        require(all(left.overlaps(right) for left, right in zip(line, stored_line)), "A410 line coordinates changed")
        ell_0, ell_1, ell_2 = line
        ell_1_lower = validated.lower(abs(ell_1))
        ell_2_lower = validated.lower(abs(ell_2))
        require(ell_1_lower > 0.0 and ell_2_lower > 0.0, "A410 overlap hypothesis failed")
        minimum_ell_1 = min(minimum_ell_1, ell_1_lower)
        minimum_ell_2 = min(minimum_ell_2, ell_2_lower)
        alpha = -ell_0 / ell_1
        beta = -ell_2 / ell_1
        common = -(ell_1**2) / (ell_2**2)
        expected = acb_mat(5, 5)
        for power in range(5):
            for column in range(power + 1):
                expected[power, column] = common * acb(math.comb(power, column)) * alpha ** (power - column) * beta**column
        forward = decoded_matrix(row["z_periods_from_y_periods_5_by_5"])
        inverse = decoded_matrix(row["y_periods_from_z_periods_5_by_5"])
        require(all(forward[r, c].overlaps(expected[r, c]) for r in range(5) for c in range(5)), "A410 forward transition changed")
        determinant = forward.det()
        determinant_lower = validated.lower(abs(determinant))
        require(determinant.contains(acb(-1)) and determinant_lower > 0.0, "A410 determinant gate failed")
        minimum_determinant = min(minimum_determinant, determinant_lower)
        for product in (forward * inverse, inverse * forward):
            require(all(product[r, c].contains(acb(1 if r == c else 0)) for r in range(5) for c in range(5)), "A410 inverse identity failed")
    summary = packet["summary"]
    require(int(summary["certified_native_z_entry_count"]) == 40, "A410 summary count changed")
    for key, expected in (
        ("minimum_ell_1_absolute_lower", minimum_ell_1),
        ("minimum_ell_2_absolute_lower", minimum_ell_2),
        ("minimum_transition_determinant_absolute_lower", minimum_determinant),
    ):
        require(math.isclose(float(summary[key]), expected, rel_tol=2.0e-14), f"A410 summary changed: {key}")
    for label, entry in packet["authority"].items():
        path = ROOT / entry["path"]
        require(path.is_file(), f"A410 authority missing: {label}")
        require(sha256(path) == entry["sha256"], f"A410 authority stale: {label}")
    scope = packet["strict_scope"]
    for key in (
        "A123_exact_formula_consumed",
        "all_40_native_z_entry_overlap_hypotheses_closed",
        "all_40_z_from_y_period_matrices_closed",
        "all_40_y_from_z_inverse_period_matrices_closed",
        "all_transition_determinants_exclude_zero",
    ):
        require(scope[key], f"A410 strict gate false: {key}")
    require(not scope["native_z_outer_leg_values_transformed"], "A410 overclaims outer values")
    require(not scope["A405_common_y_operators_applied"], "A410 overclaims A405")
    require(not scope["common_hub_sum_executed"], "A410 overclaims the hub sum")
    require(not scope["full_correlation_preserving_path_execution_closed"], "A410 overclaims full transport")
    require(not scope["interval_Newton_existence_and_uniqueness_closed"], "A410 overclaims Newton")
    require(not scope["covariant_zero_proved"], "A410 overclaims a zero")
    require(not scope["full_SM_closure_proved"], "A410 overclaims SM closure")
    require(not scope["observed_SM_values_used"], "observed SM data entered A410")
    print(f"PASS: A410 independently replays 40 exact native-z entry transitions; minimum determinant lower {minimum_determinant:.6g}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
