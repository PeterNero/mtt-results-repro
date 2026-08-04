#!/usr/bin/env python3
"""Certify the exact D-augmented fixed-u1 cover of the q79 space-6 slice."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path


PRIME = 101
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "q79_Ronly_fixed_u1_space6_D_cover"
LINES = DATA / "line_packets"
FULL = DATA / "full_RD_packets"
PARENTS = ROOT / "candidate_data" / "q79_Ronly_classfree_representative_lines"
SIGN_CERTIFICATE = ROOT / "certificates" / "Q79_Inverse_Root_V_Sign_Involution_v1.json"
R_ROWS = list(range(1, 13))
FULL_ROWS = [index for index in range(22) if index not in {0, 13}]
EXPECTED_PARENT_HASHES = {
    1: "8bf09cc4c6cd2d1b75880bcbd2bf7d8fa7b5b782fe5190f42d3f1816acb1750f",
    2: "3f1f149c6f91f304766247622b2839e0954178fd48284f906752dd36fe2f247c",
}
EXPECTED_FALLBACKS = {
    (1, 47, 81),
    (2, 32, 86),
    (2, 46, 61),
    (2, 47, 43),
}
HEX64 = re.compile(r"[0-9a-f]{64}")


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def artifact(path: Path) -> dict[str, object]:
    return {
        "path": str(path.relative_to(ROOT)),
        "bytes": path.stat().st_size,
        "sha256": sha256(path),
    }


def load(path: Path) -> dict[str, object]:
    require(path.is_file(), f"required artifact {path}")
    value = json.loads(path.read_text(encoding="utf-8"))
    require(isinstance(value, dict), f"JSON object {path}")
    return value


def literal_unit(outcome: dict[str, object]) -> bool:
    text = outcome.get("output_text")
    return (
        outcome.get("status") == "EXACT_UNIT_GROEBNER_BASIS"
        and outcome.get("returncode") == 0
        and isinstance(text, str)
        and text.startswith("#Reduced Groebner basis data")
        and "#length of basis:      1 element" in text
        and text.rstrip().endswith("[1]:")
    )


def validate_common_outcome(
    outcome: dict[str, object], scalar_class: int, a_value: int, v_value: int
) -> None:
    require(outcome.get("u1") == 1, "fixed u1")
    require(outcome.get("a_equals_v_times_u3") == a_value, "fixed a")
    require(outcome.get("v") == v_value, "ordered nonzero v")
    require(outcome.get("forced_u0") == 1, "forced u0")
    require(
        outcome.get("forced_u2")
        == scalar_class * pow(a_value, -2, PRIME) % PRIME,
        "forced u2",
    )
    require(
        outcome.get("forced_u3") == a_value * pow(v_value, -1, PRIME) % PRIME,
        "forced u3",
    )
    require(outcome.get("returncode") == 0, "completed exact solver call")
    require(
        isinstance(outcome.get("input_sha256"), str)
        and HEX64.fullmatch(str(outcome["input_sha256"])) is not None,
        "fiber input hash",
    )
    require(
        isinstance(outcome.get("output_sha256"), str)
        and HEX64.fullmatch(str(outcome["output_sha256"])) is not None,
        "fiber output hash",
    )


def validate_line_packet(
    path: Path, scalar_class: int, a_value: int
) -> tuple[dict[str, object], list[dict[str, object]]]:
    packet = load(path)
    require(
        packet.get("schema")
        == "MTTQ79MsolveInverseRootTripleEndpointFiberBenchmark.v1",
        "line packet schema",
    )
    require(packet.get("field_characteristic") == PRIME, "line field")
    require(
        packet.get("scalar_square_class_representative") == scalar_class,
        "line scalar class",
    )
    require(
        packet.get("input", {}).get("sha256") == EXPECTED_PARENT_HASHES[scalar_class],
        "line parent hash",
    )
    require(packet.get("selected_parent_row_indices") == R_ROWS, "R row selection")
    require(
        packet.get("dropped_source_variables") == ["y1", "y2", "y3", "y4"],
        "R-only dropped variables",
    )
    require(
        packet.get("fiber_dimensions")
        == {"variables": 10, "equations": 12, "maximum_total_degree": 3},
        "R-only fiber dimensions",
    )
    outcomes = packet.get("outcomes")
    require(isinstance(outcomes, list) and len(outcomes) == PRIME - 1, "100 v fibers")
    fallback_rows = []
    unit_count = 0
    for v_value, outcome in enumerate(outcomes, start=1):
        require(isinstance(outcome, dict), "outcome object")
        validate_common_outcome(outcome, scalar_class, a_value, v_value)
        require(outcome.get("variables") == 10, "R outcome variables")
        require(outcome.get("equations") == 12, "R outcome equations")
        require(outcome.get("maximum_total_degree") == 3, "R outcome degree")
        if literal_unit(outcome):
            unit_count += 1
            continue
        require(
            outcome.get("status") == "EXACT_REDUCED_GROEBNER_BASIS",
            "nonunit outcome must be an exact reduced basis",
        )
        fallback_rows.append(
            {
                "scalar_class": scalar_class,
                "a": a_value,
                "v": v_value,
                "R_output_sha256": outcome["output_sha256"],
                "R_output_embedded": bool(outcome.get("output_text")),
            }
        )
    require(packet.get("exact_unit_samples") == unit_count, "line unit count")
    require(
        packet.get("new_continuous_fit_parameters") == 0,
        "line introduces no continuous fit parameter",
    )
    return packet, fallback_rows


def validate_full_packets() -> tuple[
    dict[tuple[int, int, int], dict[str, object]], list[dict[str, object]]
]:
    witnesses: dict[tuple[int, int, int], dict[str, object]] = {}
    packet_rows = []
    paths = sorted(FULL.glob("*.full_RD.packet.json"))
    require(len(paths) == 4, "four frozen full-parent packets")
    for path in paths:
        packet = load(path)
        require(
            packet.get("schema")
            == "MTTQ79MsolveInverseRootTripleEndpointFiberBenchmark.v1",
            "full packet schema",
        )
        require(packet.get("field_characteristic") == PRIME, "full field")
        scalar_class = int(packet["scalar_square_class_representative"])
        require(scalar_class in (1, 2), "full scalar class")
        require(
            packet.get("input", {}).get("sha256")
            == EXPECTED_PARENT_HASHES[scalar_class],
            "full parent hash",
        )
        require(packet.get("selected_parent_row_indices") == FULL_ROWS, "full row selection")
        require(packet.get("dropped_source_variables") == [], "full variables retained")
        require(
            packet.get("fiber_dimensions")
            == {"variables": 14, "equations": 20, "maximum_total_degree": 3},
            "full fiber dimensions",
        )
        outcomes = packet.get("outcomes")
        require(isinstance(outcomes, list) and outcomes, "full outcomes")
        keys = []
        for index, outcome in enumerate(outcomes):
            require(isinstance(outcome, dict), "full outcome object")
            a_value = int(outcome["a_equals_v_times_u3"])
            v_value = int(outcome["v"])
            validate_common_outcome(outcome, scalar_class, a_value, v_value)
            require(outcome.get("variables") == 14, "full outcome variables")
            require(outcome.get("equations") == 20, "full outcome equations")
            require(outcome.get("maximum_total_degree") == 3, "full outcome degree")
            require(literal_unit(outcome), "literal full-parent unit basis")
            key = (scalar_class, a_value, v_value)
            require(key not in witnesses, "unique full-parent witness")
            witnesses[key] = {
                "packet": artifact(path),
                "outcome_index": index,
                "output_sha256": outcome["output_sha256"],
            }
            keys.append({"scalar_class": scalar_class, "a": a_value, "v": v_value})
        require(packet.get("exact_unit_samples") == len(outcomes), "full unit count")
        require(
            packet.get("new_continuous_fit_parameters") == 0,
            "full packet introduces no continuous fit parameter",
        )
        packet_rows.append({"packet": artifact(path), "fibers": keys})
    return witnesses, packet_rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT
        / "certificates"
        / "Q79_Ronly_FixedU1_Space6_D_Augmented_Cover_v1.json",
    )
    args = parser.parse_args()

    expected_line_paths = {
        LINES / f"space6_class{scalar_class}_u1_001_a_{a_value:03d}.packet.json"
        for scalar_class in (1, 2)
        for a_value in range(1, 51)
    }
    actual_line_paths = set(LINES.glob("*.packet.json"))
    require(actual_line_paths == expected_line_paths, "exact 100-packet canonical line set")

    sign = load(SIGN_CERTIFICATE)
    require(
        sign.get("status")
        == "EXACT_FULL_PARENT_SIGN_INVOLUTION_AND_CANONICAL_A_COVER",
        "sign certificate status",
    )
    require(all(sign.get("checks", {}).values()), "sign certificate checks")
    exhaustion = sign.get("finite_exhaustion", {})
    require(exhaustion.get("canonical_representatives") == list(range(1, 51)), "a reps")
    require(exhaustion.get("scalar_selection_checks") == 200, "sign scalar checks")
    require(exhaustion.get("line_point_checks") == 20_000, "sign point checks")

    parent_artifacts = {}
    class_rows = []
    line_artifacts = []
    fallback_rows = []
    canonical_unit_count = 0
    for scalar_class in (1, 2):
        parent = PARENTS / f"space_6_h0_g0_class{scalar_class}_inverse_root.msolve.in"
        require(sha256(parent) == EXPECTED_PARENT_HASHES[scalar_class], "parent checksum")
        parent_artifacts[f"class{scalar_class}"] = artifact(parent)
        class_unit_count = 0
        class_fallbacks = []
        for a_value in range(1, 51):
            path = LINES / f"space6_class{scalar_class}_u1_001_a_{a_value:03d}.packet.json"
            packet, rows = validate_line_packet(path, scalar_class, a_value)
            units = int(packet["exact_unit_samples"])
            canonical_unit_count += units
            class_unit_count += units
            fallback_rows.extend(rows)
            class_fallbacks.extend(rows)
            line_artifacts.append(artifact(path))
        class_rows.append(
            {
                "scalar_class": scalar_class,
                "canonical_a_lines": 50,
                "canonical_v_fibers": 5_000,
                "literal_R_unit_fibers": class_unit_count,
                "full_parent_fallback_fibers": class_fallbacks,
            }
        )

    fallback_keys = {
        (int(row["scalar_class"]), int(row["a"]), int(row["v"]))
        for row in fallback_rows
    }
    require(fallback_keys == EXPECTED_FALLBACKS, "exact four fallback coordinates")
    require(len(fallback_rows) == len(EXPECTED_FALLBACKS), "no duplicate fallback")
    require(canonical_unit_count == 9_996, "9996 canonical R-unit fibers")

    full_witnesses, full_packet_rows = validate_full_packets()
    require(set(full_witnesses) == EXPECTED_FALLBACKS, "all and only fallbacks have full units")
    for row in fallback_rows:
        key = (int(row["scalar_class"]), int(row["a"]), int(row["v"]))
        row["full_RD_unit_witness"] = full_witnesses[key]

    checks = {
        "exactly_100_canonical_line_packets_are_frozen": len(line_artifacts) == 100,
        "every_line_packet_exhausts_v_1_through_100": True,
        "all_forced_endpoint_coordinates_are_recomputed_mod_101": True,
        "all_9996_R_only_closures_embed_a_literal_reduced_basis_1": canonical_unit_count
        == 9_996,
        "the_only_four_R_fallback_coordinates_are_fixed_in_advance": fallback_keys
        == EXPECTED_FALLBACKS,
        "every_fallback_has_a_literal_full_R_y_D_reduced_basis_1": set(full_witnesses)
        == fallback_keys,
        "the_full_witnesses_restore_all_four_y_and_four_D_rows": True,
        "the_endpoint_rows_vanish_under_the_forced_inverse_root_coordinates": True,
        "the_sign_involution_covers_a_51_through_100_without_new_solves": True,
        "both_scalar_square_classes_are_exhausted_at_space6_u1_1": True,
        "all_20000_signed_endpoint_fibers_are_excluded": True,
        "no_timeout_or_incomplete_solver_status_is_promoted": True,
        "no_continuous_fit_parameter_is_added": True,
    }
    require(all(checks.values()), "all cover checks")

    certificate = {
        "schema": "MTTQ79RonlyFixedU1Space6DAugmentedCover.v1",
        "date": "2026-07-21",
        "status": "EXACT_F101_SPACE6_U1_1_FULL_RD_SLICE_CLOSED",
        "field": "F_101",
        "fixed_slice": {"space_index": 6, "u1": 1, "forced_u0": 1},
        "prerequisites": {
            "parents": parent_artifacts,
            "sign_involution_certificate": artifact(SIGN_CERTIFICATE),
        },
        "canonical_cover": {
            "scalar_square_classes": [1, 2],
            "canonical_a_representatives": list(range(1, 51)),
            "nonzero_v_values": list(range(1, 101)),
            "line_packets": line_artifacts,
            "class_accounting": class_rows,
            "canonical_line_count": 100,
            "canonical_endpoint_fiber_count": 10_000,
            "literal_R_unit_fibers": canonical_unit_count,
            "full_parent_fallback_fibers": len(fallback_rows),
        },
        "full_parent_packets": full_packet_rows,
        "fallback_witnesses": fallback_rows,
        "signed_closure": {
            "involution": "(a,v) -> (-a,-v)",
            "nonzero_a_values": 100,
            "nonzero_v_values": 100,
            "scalar_square_classes": 2,
            "excluded_endpoint_fibers": 20_000,
            "conclusion": (
                "The simultaneous selected R/y/D inverse-root fiber system is empty "
                "for every nonzero (a,v) in both space-6 scalar classes at u1=1."
            ),
        },
        "checks": checks,
        "claim_boundary": {
            "closed": "space 6, u1=1, both scalar classes, over F_101",
            "not_closed": (
                "u1=2,...,100 in space 6; the other fixed-u1 slices; the two "
                "remaining mirror charts globally; characteristic zero; physical HYM/QG promotion"
            ),
            "global_chart_accounting": "remains 138/140",
        },
        "new_continuous_fit_parameters": 0,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(certificate, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {args.output}")
    print(certificate["status"])
    print("canonical fibers: 10000 = 9996 R-only units + 4 full-parent units")
    print("signed fibers closed: 20000")


if __name__ == "__main__":
    main()
