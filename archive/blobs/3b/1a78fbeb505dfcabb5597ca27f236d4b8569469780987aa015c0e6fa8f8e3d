from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

from flint import acb, acb_mat, ctx

import certify_q79_height4_d087_full_residue_main_interval as n3_engine
import certify_q79_selected_side_base_lift_interval as serializer
import certify_q79_selected_side_beta_defect_transport as validated


ROOT = Path(__file__).resolve().parents[1]
VALIDATED = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
)
A123 = (
    ROOT
    / "candidate_data"
    / "selected_q79projectivelinechartcovarianceandellzerocontinuation"
    / "projective_line_chart_covariance_theorem.packet.json"
)
A404 = VALIDATED / "n3.junction_operator_sweep.a404.json"
OUTPUT = VALIDATED / "pt" / "a410.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourA404ProjectivePeriodTransitions_A410_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def authority(path: Path) -> dict[str, str]:
    return {"path": relative(path), "sha256": sha256(path)}


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def encoded_ball(value: acb) -> dict:
    bounds = serializer.complex_interval(value)
    persisted = validated.interval_from_bounds(bounds)
    center = validated.midpoint(persisted)
    return {
        "interval_bounds": bounds,
        "interval_center": {
            "real": format(center.real, ".17g"),
            "imaginary": format(center.imag, ".17g"),
        },
        "interval_radius_upper": validated.radius_upper(persisted),
    }


def encoded_matrix(matrix: acb_mat) -> list[list[dict]]:
    return [
        [encoded_ball(matrix[row, column]) for column in range(matrix.ncols())]
        for row in range(matrix.nrows())
    ]


def transition(line: list[acb]) -> tuple[acb_mat, acb_mat, dict]:
    ell_0, ell_1, ell_2 = line
    ell_1_lower = validated.lower(abs(ell_1))
    ell_2_lower = validated.lower(abs(ell_2))
    if ell_1_lower <= 0.0 or ell_2_lower <= 0.0:
        raise ArithmeticError("A410 chart overlap ell_1*ell_2 != 0 is not certified")
    alpha = -ell_0 / ell_1
    beta = -ell_2 / ell_1
    common = -(ell_1**2) / (ell_2**2)
    z_from_y = acb_mat(5, 5)
    for power in range(5):
        for index in range(power + 1):
            z_from_y[power, index] = (
                common
                * acb(math.comb(power, index))
                * alpha ** (power - index)
                * beta**index
            )
    determinant = z_from_y.det()
    determinant_lower = validated.lower(abs(determinant))
    if determinant_lower <= 0.0 or not determinant.contains(acb(-1)):
        raise ArithmeticError("A410 period transition lost the exact determinant -1")
    y_from_z = z_from_y.inv()
    product_left = z_from_y * y_from_z
    product_right = y_from_z * z_from_y
    for row in range(5):
        for column in range(5):
            expected = acb(1 if row == column else 0)
            if not product_left[row, column].contains(expected) or not product_right[row, column].contains(expected):
                raise ArithmeticError("A410 inverse product misses the identity")
    diagnostics = {
        "ell_1_absolute_lower": ell_1_lower,
        "ell_2_absolute_lower": ell_2_lower,
        "z_from_y_determinant": encoded_ball(determinant),
        "z_from_y_determinant_absolute_lower": determinant_lower,
        "exact_symbolic_determinant_minus_one_contained": True,
        "both_interval_inverse_products_contain_identity": True,
    }
    return z_from_y, y_from_z, diagnostics


def main() -> int:
    ctx.dps = 100
    theorem = load(A123)
    manifest = load(A404)
    if not theorem["theorem"]["proved"] or theorem["normal_function_covariance"]["reduced_period_basis_transition_determinant"] != "-1":
        raise AssertionError("A410 requires the exact A123 determinant theorem")
    if manifest.get("artifact") != "A404" or not manifest["theorem"]["proved"]:
        raise AssertionError("A410 requires A404")
    system = n3_engine.exact_target_system(100)
    rows = []
    target_authorities = []
    minimum_ell_1 = math.inf
    minimum_ell_2 = math.inf
    minimum_determinant = math.inf
    for entry_index, entry in enumerate(manifest["ordered_entry_rows"]):
        if entry.get("kind") != "selected_thimble_entry":
            continue
        index = int(entry["distinguished_index"])
        canonical_path = VALIDATED / f"d{index:03d}.n3.full8.refined.json"
        canonical = load(canonical_path)
        if canonical["selected_target"]["line_chart"] != "z":
            continue
        parameter = complex_value(entry["point"])
        _a, _b, line, _line_w = system.ab_line_data(
            acb(format(parameter.real, ".17g"), format(parameter.imag, ".17g"))
        )
        z_from_y, y_from_z, diagnostics = transition(line)
        minimum_ell_1 = min(minimum_ell_1, diagnostics["ell_1_absolute_lower"])
        minimum_ell_2 = min(minimum_ell_2, diagnostics["ell_2_absolute_lower"])
        minimum_determinant = min(
            minimum_determinant,
            diagnostics["z_from_y_determinant_absolute_lower"],
        )
        rows.append(
            {
                "entry_index_zero_based": entry_index,
                "distinguished_index": index,
                "entry_point": entry["point"],
                "canonical_target_artifact": canonical["artifact"],
                "canonical_target_path": relative(canonical_path),
                "canonical_target_sha256": sha256(canonical_path),
                "line_coordinates": [encoded_ball(value) for value in line],
                "z_periods_from_y_periods_5_by_5": encoded_matrix(z_from_y),
                "y_periods_from_z_periods_5_by_5": encoded_matrix(y_from_z),
                "diagnostics": diagnostics,
            }
        )
        target_authorities.append(authority(canonical_path))
    if len(rows) != 40:
        raise AssertionError(f"A410 expected 40 native-z entries, found {len(rows)}")
    payload = {
        "schema": "MTTQ79HeightFourA404ProjectivePeriodTransitions.v1",
        "status": "ALL_NATIVE_Z_A404_ENTRY_PERIOD_TRANSITIONS_INTERVAL_CERTIFIED",
        "artifact": "A410",
        "formula": {
            "alpha": "-ell_0/ell_1",
            "beta": "-ell_2/ell_1",
            "common": "-ell_1^2/ell_2^2",
            "z_from_y_entry": "T[k,j]=common*binom(k,j)*alpha^(k-j)*beta^j for j<=k",
            "direction_for_common_A405_frame": "p_y=T^{-1}p_z",
            "period_basis_order": ["dt/U", "t dt/U", "t^2 dt/U", "t^3 dt/U", "t^4 dt/U"],
        },
        "native_z_entry_transitions": rows,
        "summary": {
            "certified_native_z_entry_count": len(rows),
            "certified_matrix_count": 2 * len(rows),
            "minimum_ell_1_absolute_lower": minimum_ell_1,
            "minimum_ell_2_absolute_lower": minimum_ell_2,
            "minimum_transition_determinant_absolute_lower": minimum_determinant,
            "all_exact_minus_one_determinants_contained": True,
            "all_inverse_products_contain_identity": True,
        },
        "component_authority_manifest": target_authorities,
        "authority": {
            "A123_projective_chart_covariance": authority(A123),
            "A404_common_junction_manifest": authority(A404),
            "n3_exact_fibration": authority(n3_engine.FIBRATION),
            "exact_interval_system_engine": authority(Path(n3_engine.__file__).resolve()),
            "full_precision_interval_serializer": authority(Path(serializer.__file__).resolve()),
            "builder_source": authority(Path(__file__).resolve()),
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "A123_exact_formula_consumed": True,
            "all_40_native_z_entry_overlap_hypotheses_closed": True,
            "all_40_z_from_y_period_matrices_closed": True,
            "all_40_y_from_z_inverse_period_matrices_closed": True,
            "all_transition_determinants_exclude_zero": True,
            "native_z_outer_leg_values_transformed": False,
            "A405_common_y_operators_applied": False,
            "common_hub_sum_executed": False,
            "full_correlation_preserving_path_execution_closed": False,
            "interval_Newton_existence_and_uniqueness_closed": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": (
            "apply each A410 y-from-z matrix to its native-z outer-leg affine frame "
            "before the A409T/A405 reverse entry operator"
        ),
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    NOTE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(
        "# MTT q79 Height-Four A404 Projective Period Transitions (A410) v1\n\n"
        "A410 instantiates the exact A123 triangular five-period transition at "
        "all 40 native-z A404 entries. Both directions are serialized as interval "
        "matrices; every overlap has `ell_1 ell_2 != 0`, every transition contains "
        "the exact determinant `-1`, and both inverse products contain the identity.\n\n"
        f"The minimum determinant absolute lower bound is `{minimum_determinant:.12g}`. "
        "Outer-leg values and A405 operator application remain separate gates.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(OUTPUT)}")
    print(f"wrote {relative(NOTE)}")
    print(json.dumps(payload["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
