from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
PERIOD_DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
)
PROBE = PERIOD_DIRECTORY / "covariant_floating_probe"
VALIDATED = PROBE / "validated_transport"
PREFIX = VALIDATED / "n3.certified76.recomposition.json"
A231 = VALIDATED / "n3.chain.frontier.json"
HANDLE = VALIDATED / "n3.rank3.handle_combination.interval.json"
BETA = VALIDATED / "n3.rank3.anchored_beta.interval.json"
D065 = VALIDATED / "d065.n3.full8.refined.json"
N3 = PROBE / "cplx" / "n3ud" / "probe.packet.json"
OUTPUT = VALIDATED / "n3.rank3.full_residual.interval.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourRank3FullResidualInterval_A377_v1.md"
ARTIFACT = "A377"


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


def encoded_complex(value: complex) -> dict[str, str]:
    return {
        "real": format(value.real, ".17g"),
        "imaginary": format(value.imag, ".17g"),
    }


def vector(values: list[dict[str, str]]) -> np.ndarray:
    return np.asarray([complex_value(value) for value in values], dtype=np.complex128)


def main() -> int:
    prefix = load(PREFIX)
    if (
        prefix["artifact"] != "A373"
        or int(prefix["certified_A219_priority_prefix_length"]) != 76
        or not prefix["strict_scope"]["all_76_target_intervals_closed"]
    ):
        raise AssertionError("A377 requires the final 76-target certified prefix")
    a231 = load(A231)
    handle = load(HANDLE)
    beta = load(BETA)
    d065 = load(D065)
    n3 = load(N3)
    if not handle["strict_scope"]["rank3_handle_combination_interval_closed"]:
        raise AssertionError("rank-3 handle interval is open")
    if not beta["strict_scope"]["rank3_anchored_beta_interval_closed"]:
        raise AssertionError("rank-3 beta interval is open")
    decomposition = a231["exact_floating_decomposition"]
    wall_weight = int(decomposition["PL_wall_weight"])
    if (
        int(decomposition["PL_crossing_period_distinguished_index"]) != 65
        or wall_weight != 3
    ):
        raise AssertionError("A231 Picard-Lefschetz wall correction changed")
    if int(d065["selected_target"]["distinguished_index"]) != 65:
        raise AssertionError("d065 full interval identity changed")

    candidate_rows = [
        row
        for row in n3["candidate_residuals"]
        if int(row["A132_objective_rank"]) == 3
    ]
    if len(candidate_rows) != 1:
        raise AssertionError("n3 probe no longer contains exactly one rank-3 row")
    floating_residual = vector(candidate_rows[0]["PL_corrected_residual"])
    beta_radius = float(beta["endpoint"]["uniform_component_radius_upper"])
    rows = []
    for residue_index in range(8):
        chain_row = prefix["residue_rows"][residue_index]
        handle_row = handle["all_eight_handle_rows"][residue_index]
        wall_row = d065["residue_rows"][residue_index]
        beta_center = complex_value(beta["endpoint"]["beta_center"][residue_index])
        chain_center = complex_value(chain_row["certified_prefix_interval_center"])
        chain_radius = float(chain_row["certified_prefix_interval_radius_upper"])
        handle_center = complex_value(handle_row["interval_center"])
        handle_radius = float(handle_row["uniform_component_radius_upper"])
        wall_center = wall_weight * complex_value(wall_row["full_interval_center"])
        wall_radius = abs(wall_weight) * float(wall_row["full_interval_radius_upper"])
        period_center = chain_center + handle_center + wall_center
        period_radius = chain_radius + handle_radius + wall_radius
        residual_center = beta_center - period_center
        residual_radius = beta_radius + period_radius
        floating = floating_residual[residue_index]
        real_difference = abs(floating.real - residual_center.real)
        imaginary_difference = abs(floating.imag - residual_center.imag)
        contained = real_difference <= residual_radius and imaginary_difference <= residual_radius
        if not contained:
            raise AssertionError("floating rank-3 residual left the rigorous residual box")
        zero_contained = (
            abs(residual_center.real) <= residual_radius
            and abs(residual_center.imag) <= residual_radius
        )
        rows.append(
            {
                "residue_index_zero_based": residue_index,
                "beta_interval_center": encoded_complex(beta_center),
                "beta_component_radius_upper": beta_radius,
                "raw_76_thimble_interval_center": encoded_complex(chain_center),
                "raw_76_thimble_component_radius_upper": chain_radius,
                "rank3_handle_interval_center": encoded_complex(handle_center),
                "rank3_handle_component_radius_upper": handle_radius,
                "PL_wall_correction_interval_center": encoded_complex(wall_center),
                "PL_wall_correction_component_radius_upper": wall_radius,
                "PL_corrected_period_interval_center": encoded_complex(period_center),
                "PL_corrected_period_component_radius_upper": period_radius,
                "residual_interval_center": encoded_complex(residual_center),
                "residual_component_radius_upper": residual_radius,
                "zero_contained_in_residual_box": zero_contained,
                "floating_residual_diagnostic_only": encoded_complex(floating),
                "floating_real_center_difference": real_difference,
                "floating_imaginary_center_difference": imaginary_difference,
                "floating_residual_contained": True,
                "floating_containment_margin": residual_radius
                - max(real_difference, imaginary_difference),
            }
        )

    residual_radii = np.asarray(
        [row["residual_component_radius_upper"] for row in rows], dtype=np.float64
    )
    residual_centers = np.asarray(
        [complex_value(row["residual_interval_center"]) for row in rows],
        dtype=np.complex128,
    )
    zero_contained_all_rows = all(row["zero_contained_in_residual_box"] for row in rows)
    payload = {
        "schema": "MTTQ79HeightFourRank3FullResidualInterval.v1",
        "status": "N3_RANK3_FULL_EIGHT_RESIDUAL_ROWS_INTERVAL_RECOMPOSED",
        "artifact": ARTIFACT,
        "identity": (
            "R_n3 = beta_n3 - (sum_76 m_I Pi_I + H_rank3 + 3 Pi_d065)"
        ),
        "PL_wall_correction": {
            "source_distinguished_index": int(
                decomposition["PL_wall_source_distinguished_index"]
            ),
            "crossing_period_distinguished_index": 65,
            "integer_weight": wall_weight,
        },
        "residue_rows": rows,
        "summary": {
            "certified_rows": len(rows),
            "maximum_residual_component_radius_upper": float(np.max(residual_radii)),
            "residual_product_box_l2_radius_upper": float(np.linalg.norm(residual_radii)),
            "residual_interval_center_l2_norm": float(np.linalg.norm(residual_centers)),
            "minimum_floating_containment_margin": min(
                row["floating_containment_margin"] for row in rows
            ),
            "all_floating_residual_diagnostics_contained": True,
            "zero_contained_in_every_residual_component_box": zero_contained_all_rows,
        },
        "authority": {
            name: {"path": relative(path), "sha256": sha256(path)}
            for name, path in {
                "A373_final_76_target_prefix": PREFIX,
                "A231_chain_and_PL_identity": A231,
                "A374_rank3_handle_interval": HANDLE,
                "A376_rank3_anchored_beta_interval": BETA,
                "d065_full_interval": D065,
                "n3_ultra_probe": N3,
                "builder_source": Path(__file__).resolve(),
            }.items()
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "all_76_target_intervals_closed": True,
            "rank3_handle_combination_interval_closed": True,
            "rank3_anchored_beta_interval_closed": True,
            "PL_wall_correction_interval_closed": True,
            "rank3_full_residual_interval_closed": True,
            "zero_in_residual_box_is_not_an_existence_proof": True,
            "interval_Jacobian_certificate": False,
            "interval_Newton_existence_and_uniqueness_closed": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": (
            "enclose the same-source complex 8x8 Jacobian on a wall-free n3 "
            "parameter polydisk and execute an interval Newton or Krawczyk gate"
        ),
    }
    dump(OUTPUT, payload)
    NOTE.write_text(
        "# MTT q79 Height-Four Rank-3 Full Residual Interval (A377) v1\n\n"
        "A377 recomposes the complete rigorous rank-3 residual from the final "
        "76-thimble chain, selected all-row handle contribution, explicit "
        "Picard-Lefschetz correction `3 Pi_d065`, and anchored beta interval.\n\n"
        f"The maximum component radius is `{np.max(residual_radii):.12g}` and "
        f"the product-box L2 radius is `{np.linalg.norm(residual_radii):.12g}`. "
        "Every independent floating residual is contained and was not used as "
        "an error bound.\n\n"
        "Containment of zero in this residual box is not promoted to a zero "
        "theorem. Existence and uniqueness require the separate interval "
        "Jacobian plus interval-Newton/Krawczyk certificate.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(OUTPUT)}")
    print(f"wrote {relative(NOTE)}")
    print(json.dumps(payload["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
