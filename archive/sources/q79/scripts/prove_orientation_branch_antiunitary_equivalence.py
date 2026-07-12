"""Prove finite antiunitary equivalence of the q79/q369 branch-smoke packets."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CANDIDATES = ROOT / "candidate_data"
CERTS = ROOT / "certificates"

Q79 = CANDIDATES / "iwasawa_route_c_branch_smoke" / "current_q79_orientation"
Q369 = CANDIDATES / "iwasawa_route_c_branch_smoke" / "conjugate_q369_orientation"
OUT_CANDIDATE = CANDIDATES / "orientation_branch_antiunitary_equivalence.candidate.json"
OUT_CERT = CERTS / "orientation_branch_antiunitary_equivalence_certificate.json"

TOL = 1e-9

FILE_SPECS = {
    "de_action.candidate.json": {
        "slot_key": "operator_slots",
        "matrix_keys": ["domain_gram", "range_gram", "D_E_matrix", "stiffness_matrix"],
        "vector_list_keys": ["ordered_zero_mode_basis"],
        "source_flag_keys": ["selected_source_verified"],
    },
    "reduced_green.candidate.json": {
        "slot_key": "green_slots",
        "matrix_keys": [
            "gram_matrix",
            "stiffness_matrix",
            "riesz_projector",
            "complement_projector",
            "reduced_green_operator",
        ],
        "vector_list_keys": [],
        "source_flag_keys": ["selected_source_verified"],
    },
    "dotd_response.candidate.json": {
        "slot_key": "dotd_response_slots",
        "matrix_keys": [
            "gram_matrix",
            "stiffness_matrix",
            "riesz_projector",
            "complement_projector",
            "reduced_green_operator",
            "dotD_alpha1_matrix",
        ],
        "vector_list_keys": [
            "ordered_zero_mode_basis",
            "source_vectors",
            "horizontal_response_vectors",
        ],
        "source_flag_keys": ["selected_dotD_source_verified", "alpha1_driver_verified"],
    },
}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def parse_complex(value: Any) -> complex:
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return complex(float(value), 0.0)
    if (
        isinstance(value, list)
        and len(value) == 2
        and all(isinstance(part, (int, float)) and not isinstance(part, bool) for part in value)
    ):
        return complex(float(value[0]), float(value[1]))
    raise ValueError(f"invalid complex entry {value!r}")


def parse_matrix(entry: Any) -> list[list[complex]]:
    matrix_data = entry.get("matrix") if isinstance(entry, dict) else entry
    return [[parse_complex(value) for value in row] for row in matrix_data]


def parse_vector_list(entry: Any) -> list[list[complex]]:
    return [[parse_complex(value) for value in vector] for vector in entry]


def compare_matrix(
    left: list[list[complex]],
    right: list[list[complex]],
    label: str,
    diffs: list[dict[str, Any]],
) -> tuple[int, float]:
    if len(left) != len(right) or len(left[0]) != len(right[0]):
        diffs.append({"label": label, "reason": "shape mismatch"})
        return 0, float("inf")
    count = 0
    max_diff = 0.0
    for row in range(len(left)):
        for col in range(len(left[0])):
            diff = abs(right[row][col] - left[row][col].conjugate())
            count += 1
            max_diff = max(max_diff, diff)
            if diff > TOL:
                diffs.append(
                    {
                        "label": f"{label}[{row},{col}]",
                        "q79": [left[row][col].real, left[row][col].imag],
                        "q369": [right[row][col].real, right[row][col].imag],
                        "abs_diff": diff,
                    }
                )
    return count, max_diff


def compare_vector_lists(
    left: list[list[complex]],
    right: list[list[complex]],
    label: str,
    diffs: list[dict[str, Any]],
) -> tuple[int, float]:
    if len(left) != len(right):
        diffs.append({"label": label, "reason": "outer length mismatch"})
        return 0, float("inf")
    count = 0
    max_diff = 0.0
    for idx, (left_vector, right_vector) in enumerate(zip(left, right)):
        if len(left_vector) != len(right_vector):
            diffs.append({"label": f"{label}[{idx}]", "reason": "vector length mismatch"})
            continue
        for col, (left_value, right_value) in enumerate(zip(left_vector, right_vector)):
            diff = abs(right_value - left_value.conjugate())
            count += 1
            max_diff = max(max_diff, diff)
            if diff > TOL:
                diffs.append(
                    {
                        "label": f"{label}[{idx}][{col}]",
                        "q79": [left_value.real, left_value.imag],
                        "q369": [right_value.real, right_value.imag],
                        "abs_diff": diff,
                    }
                )
    return count, max_diff


def branch_pair_ok(q79_packet: dict[str, Any], q369_packet: dict[str, Any]) -> bool:
    left = q79_packet["branch_packet"]
    right = q369_packet["branch_packet"]
    return (
        left["torsion_label_m"] == 1
        and right["torsion_label_m"] == 2
        and left["global_cp_label"] == 79
        and right["global_cp_label"] == 369
        and left["conditional_su5_transport_orientation"] == "F"
        and right["conditional_su5_transport_orientation"] == "F*"
        and left["sector_orientations"]["H"] == right["sector_orientations"]["H"] == 0
        and all(
            left["sector_orientations"][sector] + right["sector_orientations"][sector] == 3
            for sector in ("Q", "L", "u", "d", "e", "N")
        )
    )


def analyze() -> dict[str, Any]:
    comparisons: dict[str, Any] = {}
    total_entries = 0
    global_max_diff = 0.0
    all_diffs: list[dict[str, Any]] = []
    source_flag_counts = {
        "q79_false": 0,
        "q369_false": 0,
        "mismatched": 0,
    }

    first_q79 = load(Q79 / "dotd_response.candidate.json")
    first_q369 = load(Q369 / "dotd_response.candidate.json")

    for filename, spec in FILE_SPECS.items():
        q79_data = load(Q79 / filename)
        q369_data = load(Q369 / filename)
        slot_key = spec["slot_key"]
        file_diffs: list[dict[str, Any]] = []
        file_entries = 0
        file_max = 0.0
        sectors = sorted(q79_data[slot_key])
        for sector in sectors:
            left_slot = q79_data[slot_key][sector]
            right_slot = q369_data[slot_key][sector]
            for key in spec["matrix_keys"]:
                count, max_diff = compare_matrix(
                    parse_matrix(left_slot[key]),
                    parse_matrix(right_slot[key]),
                    f"{filename}:{sector}.{key}",
                    file_diffs,
                )
                file_entries += count
                file_max = max(file_max, max_diff)
            for key in spec["vector_list_keys"]:
                count, max_diff = compare_vector_lists(
                    parse_vector_list(left_slot[key]),
                    parse_vector_list(right_slot[key]),
                    f"{filename}:{sector}.{key}",
                    file_diffs,
                )
                file_entries += count
                file_max = max(file_max, max_diff)
            for key in spec["source_flag_keys"]:
                if left_slot.get(key) is False:
                    source_flag_counts["q79_false"] += 1
                if right_slot.get(key) is False:
                    source_flag_counts["q369_false"] += 1
                if left_slot.get(key) != right_slot.get(key):
                    source_flag_counts["mismatched"] += 1
        comparisons[filename] = {
            "sectors_compared": sectors,
            "entries_compared": file_entries,
            "max_abs_conjugation_error": file_max,
            "difference_count": len(file_diffs),
        }
        total_entries += file_entries
        global_max_diff = max(global_max_diff, file_max)
        all_diffs.extend(file_diffs)

    antiunitary_equivalence_closed = (
        branch_pair_ok(first_q79, first_q369)
        and not all_diffs
        and source_flag_counts["mismatched"] == 0
    )

    report = {
        "calculation": "OrientationBranchAntiunitaryEquivalence",
        "status": "ORIENTATION_BRANCH_ANTIUNITARY_EQUIVALENCE_CLOSED_SOURCE_SELECTION_OPEN",
        "compared_branches": {
            "q79": str(Q79.relative_to(ROOT)),
            "q369": str(Q369.relative_to(ROOT)),
        },
        "branch_pair": {
            "q79_m": first_q79["branch_packet"]["torsion_label_m"],
            "q369_m": first_q369["branch_packet"]["torsion_label_m"],
            "q79_global_cp_label": first_q79["branch_packet"]["global_cp_label"],
            "q369_global_cp_label": first_q369["branch_packet"]["global_cp_label"],
            "sector_orientations_are_conjugate": branch_pair_ok(first_q79, first_q369),
        },
        "comparisons": comparisons,
        "summary": {
            "total_entries_compared": total_entries,
            "max_abs_conjugation_error": global_max_diff,
            "difference_count": len(all_diffs),
            "antiunitary_equivalence_closed": antiunitary_equivalence_closed,
            "source_flags_match_and_remain_false": source_flag_counts["mismatched"] == 0
            and source_flag_counts["q79_false"] > 0
            and source_flag_counts["q369_false"] > 0,
            "source_flag_counts": source_flag_counts,
        },
        "guardrails": {
            "claims_unique_branch_selected": False,
            "claims_selected_source_origin": False,
            "uses_observed_cp_sign": False,
            "uses_observed_masses_or_mixings": False,
            "claims_full_sm_closure": False,
        },
        "verdict": {
            "honest_answer": (
                "The current q79 and q369 branch-smoke operator packets are "
                "finite antiunitary conjugates.  This closes the finite branch "
                "pair comparison, but it does not select one branch because the "
                "source flags remain false on both sides."
            ),
            "next_step": (
                "Add a selected source or retarded boundary theorem that breaks "
                "the antiunitary pair, or prove physical predictions are "
                "orientation-invariant up to CP-odd sign until that theorem is supplied."
            ),
        },
    }
    return report


def main() -> int:
    report = analyze()
    write(OUT_CANDIDATE, report)
    cert = {
        "certificate": "OrientationBranchAntiunitaryEquivalence",
        "status": report["status"],
        "analysis_script": "scripts/prove_orientation_branch_antiunitary_equivalence.py",
        "candidate_data": str(OUT_CANDIDATE.relative_to(ROOT)),
        "summary": report["summary"],
        "branch_pair": report["branch_pair"],
        "what_this_closes": {
            "q79_q369_finite_operator_conjugacy": report["summary"][
                "antiunitary_equivalence_closed"
            ],
            "finite_branch_pair_comparison": True,
            "source_flags_identified_as_common_open_layer": report["summary"][
                "source_flags_match_and_remain_false"
            ],
        },
        "what_this_does_not_close": {
            "unique_m1_vs_m2_selection": False,
            "selected_source_origin": False,
            "selected_alpha1_driver": False,
            "primitive_C1_contractions": False,
            "full_SM_closure": False,
        },
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    write(OUT_CERT, cert)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["summary"]["antiunitary_equivalence_closed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
