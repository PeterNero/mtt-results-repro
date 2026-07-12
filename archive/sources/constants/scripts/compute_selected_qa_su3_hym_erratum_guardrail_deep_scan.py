"""Deep guardrail scan for Qa/SU3 HYM connection erratum options.

This refines the prior erratum scan.  The earlier artifact identified the
unique B3 repair if B1 and B2 are held fixed.  Here we also test whether a
smaller textual repair can keep the printed B3=mu E12 by moving/signing one of
the sqrt(mu) entries.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
ERRATUM_CERT = (
    ROOT
    / "certificates"
    / "selected_qa_su3_hym_connection_erratum_or_convention_resolution_certificate.json"
)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def elementary(row: int, col: int) -> np.ndarray:
    matrix = np.zeros((3, 3), dtype=int)
    matrix[row - 1, col - 1] = 1
    return matrix


def matrix_rows(matrix: np.ndarray) -> list[list[int]]:
    return [[int(value) for value in row] for row in matrix]


def sparse_solutions_for_printed_b3() -> list[dict[str, Any]]:
    """Find signed elementary B1,B2 with B3=E12 and B3+[B1,B2]=0."""

    entries = [(row, col, elementary(row, col)) for row in range(1, 4) for col in range(1, 4)]
    b3 = elementary(1, 2)
    solutions = []
    for row1, col1, e1 in entries:
        for sign1 in (1, -1):
            b1 = sign1 * e1
            for row2, col2, e2 in entries:
                for sign2 in (1, -1):
                    b2 = sign2 * e2
                    residual = b3 + b1 @ b2 - b2 @ b1
                    if np.array_equal(residual, np.zeros((3, 3), dtype=int)):
                        solutions.append(
                            {
                                "B1": f"{'+' if sign1 > 0 else '-'}E{row1}{col1}",
                                "B2": f"{'+' if sign2 > 0 else '-'}E{row2}{col2}",
                            }
                        )
    return solutions


def named_repairs() -> dict[str, Any]:
    printed_b1 = elementary(1, 3)
    printed_b2 = -elementary(3, 1)
    printed_b3 = elementary(1, 2)

    required_b3_fixed_b1_b2 = -(printed_b1 @ printed_b2 - printed_b2 @ printed_b1)

    moved_b2 = -elementary(3, 2)
    residual_moved_b2 = printed_b3 + printed_b1 @ moved_b2 - moved_b2 @ printed_b1

    return {
        "printed": {
            "B1": "+E13",
            "B2": "-E31",
            "B3": "+E12",
        },
        "repair_A_hold_B1_B2_fixed": {
            "description": "replace B3 by the diagonal integrability value",
            "B1": "+E13",
            "B2": "-E31",
            "B3_required": matrix_rows(required_b3_fixed_b1_b2),
            "B3_required_symbolic": "E11-E33",
            "textual_change_count": "replace one displayed entry by two diagonal entries",
            "source_certified": False,
        },
        "repair_B_hold_B1_B3_fixed": {
            "description": "move the -sqrt(mu) omega2 entry from row 3 column 1 to row 3 column 2",
            "B1": "+E13",
            "B2_required": "-E32",
            "B3": "+E12",
            "residual_after_repair": matrix_rows(residual_moved_b2),
            "residual_zero": bool(np.array_equal(residual_moved_b2, np.zeros((3, 3), dtype=int))),
            "textual_change_count": "move one displayed entry by one column",
            "source_certified": False,
        },
        "repair_C_hold_B2_B3_fixed": {
            "description": "single elementary B1 repair with printed B2=-E31 and B3=E12",
            "exists": False,
            "reason": "No signed elementary B1 appears in the exhaustive sparse solution table with B2=-E31.",
            "source_certified": False,
        },
    }


def main() -> int:
    prior = load(ERRATUM_CERT)
    solutions = sparse_solutions_for_printed_b3()
    named = named_repairs()
    b1_fixed_solutions = [solution for solution in solutions if solution["B1"] == "+E13"]
    b2_printed_solutions = [solution for solution in solutions if solution["B2"] == "-E31"]

    output = {
        "certificate": "SelectedQaSU3HYMErratumGuardrailDeepScan",
        "status": "QA_SU3_HYM_ERRATUM_GUARDRAIL_DEEP_SCAN_DONE_NO_PREMATURE_REPAIR_CLOSURE",
        "input_status": prior["status"],
        "sparse_integrability_scan": {
            "equation": "E12 + [B1,B2] = 0 for signed elementary B1,B2",
            "solution_count": len(solutions),
            "solutions": solutions,
            "solutions_with_printed_B1_E13": b1_fixed_solutions,
            "solutions_with_printed_B2_minus_E31": b2_printed_solutions,
        },
        "named_repair_options": named,
        "guardrail_conclusions": [
            "The diagonal B3 repair is not the only algebraic route; it is only unique if printed B1 and printed B2 are held fixed.",
            "A one-entry move repair exists: keep B1=E13 and B3=E12, change B2 from -E31 to -E32.",
            "No simple sign/transpose convention resolved the printed matrix.",
            "No repair option is source-certified yet, so none may be used for final Qa/SU3 closure.",
            "Future closure must first choose an erratum from mathematical/source evidence or retire this displayed HYM matrix.",
        ],
        "safe_way_forward": [
            "write an erratum note in the corpus or proof repo listing both repair candidates",
            "test repaired pipeline A and repaired pipeline B as diagnostics only",
            "compare repaired c3 and Tr F wedge F data against the source claims",
            "accept a repair only if it reproduces holomorphicity, SU3 trace, Chern-Weil claims, and selection behavior without target fitting",
        ],
        "verdict": {
            "diagonal_B3_repair_unique_without_qualification": False,
            "one_entry_B2_move_repair_exists": True,
            "any_repair_source_certified": False,
            "safe_to_close_Qa_SU3_from_repair_now": False,
            "target_fitting_used": False,
            "next_required_artifact": "Selected_Qa_SU3_Repaired_Pipeline_A_B_Diagnostic_Comparison_v1",
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
