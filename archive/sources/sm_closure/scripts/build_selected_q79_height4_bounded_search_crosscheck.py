from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np

import build_selected_q79_height4_survivor_queue_and_E32_priority as a208_builder


ROOT = a208_builder.ROOT
PERIOD_DIRECTORY = a208_builder.PERIOD_DIRECTORY
A208 = a208_builder.PACKET
SCIPY_MILP = PERIOD_DIRECTORY / "selected_alignment_height4_bounded_milp.exploratory.json"
HIGHS_WARM = PERIOD_DIRECTORY / (
    "selected_alignment_height4_bounded_highs_warmstart.exploratory.json"
)
EXTENDED_KANNAN = PERIOD_DIRECTORY / "selected_alignment_extended_kannan_grid.exploratory.json"
OUTPUT = PERIOD_DIRECTORY / "selected_alignment_height4_bounded_search_crosscheck.packet.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def main() -> int:
    a208 = load(A208)
    scipy = load(SCIPY_MILP)
    highs = load(HIGHS_WARM)
    extended = load(EXTENDED_KANNAN)
    incumbent = highs["incumbent"]
    effective = [int(value) for value in incumbent["effective_coordinates_Z90"]]
    canonical = effective + [0, 0]
    corrected_id = a208_builder.vector_id(canonical)
    a208_rows = {
        row["candidate_id"]: row for row in a208["height_four_candidates"]
    }
    if corrected_id not in a208_rows:
        raise AssertionError("HiGHS warm incumbent does not map to an A208 row")
    matched = a208_rows[corrected_id]
    if effective != [int(value) for value in matched["effective_coordinates_Z90"]]:
        raise AssertionError("HiGHS incumbent/A208 coordinate mismatch")
    if corrected_id != highs["warm_start"]["candidate_id"]:
        raise AssertionError("HiGHS warm-start crosswalk changed")
    if abs(
        float(highs["solver"]["objective"])
        - float(highs["warm_start"]["component_infinity_residual"])
    ) > 1.0e-12:
        raise AssertionError("HiGHS did not return the injected warm objective")
    if incumbent["improves_warm_start"]:
        raise AssertionError("HiGHS result unexpectedly claims an improvement")
    extension = extended["height_four_screen"]
    if extension["new_nonseparated_rows_relative_to_A208"] != 0:
        raise AssertionError("extended Kannan grid has an unpromoted new row")

    packet = {
        "schema": "MTTQ79SelectedAlignmentHeightFourBoundedSearchCrosscheck.v1",
        "status": "TWO_BOUNDED_SEARCHES_AND_EXTENDED_KANNAN_CROSSCHECKED_NO_OPTIMALITY_PROMOTION",
        "authority": {
            "A208_queue": relative(A208),
            "A208_queue_sha256": sha256(A208),
            "scipy_cold_MILP": relative(SCIPY_MILP),
            "scipy_cold_MILP_sha256": sha256(SCIPY_MILP),
            "highs_warm_started_MILP": relative(HIGHS_WARM),
            "highs_warm_started_MILP_sha256": sha256(HIGHS_WARM),
            "extended_Kannan_grid": relative(EXTENDED_KANNAN),
            "extended_Kannan_grid_sha256": sha256(EXTENDED_KANNAN),
            "builder_source": relative(Path(__file__)),
            "builder_source_sha256": sha256(Path(__file__)),
        },
        "canonical_id_crosswalk": {
            "exploratory_Z90_only_id": incumbent["candidate_id"],
            "canonical_Z92_id_with_two_Leray_zeros": corrected_id,
            "canonical_A208_objective_rank": int(matched["A132_objective_rank"]),
            "same_effective_coordinates": True,
            "explanation": (
                "The exploratory HiGHS script hashed 90 effective coordinates; "
                "A208 hashes the canonical 92-vector (m,0,0). The solver vector "
                "itself is unchanged."
            ),
        },
        "search_results": {
            "cold_scipy_MILP": {
                "time_limit_seconds": scipy["solver"]["time_limit_seconds"],
                "mip_gap": scipy["solver"]["mip_gap"],
                "incumbent_complex_residual": scipy["incumbent"][
                    "residual_maximum_complex_absolute_value"
                ],
                "useful_improvement": False,
            },
            "warm_started_highs": {
                "time_limit_seconds": highs["solver"]["time_limit_seconds"],
                "returned_A208_rank": int(matched["A132_objective_rank"]),
                "component_infinity_objective": highs["solver"]["objective"],
                "mip_dual_bound": highs["solver"]["mip_dual_bound"],
                "mip_gap": highs["solver"]["mip_gap"],
                "improved_A208_incumbent": False,
            },
            "extended_Kannan": {
                "embedding_count": extended["search"]["embedding_count"],
                "unique_candidate_count": extended["search"][
                    "unique_candidate_count"
                ],
                "new_height_four_nonseparated_rows": extension[
                    "new_nonseparated_rows_relative_to_A208"
                ],
                "best_new_height_four_residual": extension["best_rows"][0][
                    "residual_maximum_absolute_value"
                ]
                if extension["best_rows"]
                else extended["best_candidate_by_maximum_height"]["4"][
                    "residual_maximum_absolute_value"
                ],
            },
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "same_selected_carrier": True,
            "A208_queue_unbeaten_by_these_searches": True,
            "bounded_floating_optimum_proved": False,
            "exhaustive_height_four_Z90_search_proved": False,
            "interval_membership_or_nonmembership_proved": False,
            "covariant_PGL3_zero_or_no_go_proved": False,
        },
        "next_required_artifact": (
            "retain A208 as the finite-grid candidate queue, finish the A211 "
            "interval refinements, and treat exhaustive bounded CVP as a separate proof obligation"
        ),
    }
    OUTPUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {relative(OUTPUT)}")
    print(
        json.dumps(
            {
                "canonical_A208_id": corrected_id,
                "A208_rank": matched["A132_objective_rank"],
                "highs_improved": False,
                "extended_Kannan_new_rows": extension[
                    "new_nonseparated_rows_relative_to_A208"
                ],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
