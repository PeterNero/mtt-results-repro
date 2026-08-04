"""Audit the Route-C C1 primitive response on smooth B_N."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "candidate_data" / "selected_routec_c1_primitive_response_on_smooth_bn.candidate.json"
CERT = REPO / "certificates" / "selected_routec_c1_primitive_response_on_smooth_bn_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_RouteC_C1_Primitive_Response_on_Smooth_BN_v1.md"


def check(name: str, condition: bool, detail: object) -> bool:
    print(("PASS" if condition else "FAIL") + f": {name} -- {detail}")
    return condition


def max_entry(matrix: list[list[object]]) -> float:
    def scalar_abs(value: object) -> float:
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            return abs(float(value))
        if isinstance(value, list) and len(value) == 2:
            return (float(value[0]) ** 2 + float(value[1]) ** 2) ** 0.5
        raise TypeError(value)

    return max((scalar_abs(value) for row in matrix for value in row), default=0.0)


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    matrices = data["c1_response_matrices"]
    matrix_norms = {sector: max_entry(item["matrix"]) for sector, item in matrices.items()}

    checks = [
        check(
            "status",
            data["status"] == "MTT_SELECTED_ROUTEC_C1_PRIMITIVE_RESPONSE_ON_SMOOTH_BN_COMPUTED_SELECTED_PRIMITIVE_OPEN",
            data["status"],
        ),
        check("certificate agreement", cert["status"] == data["status"], cert["status"]),
        check(
            "canonical tensor specified",
            data["primitive_tensor"]["name"] == "canonical_mode_conserving_F3xF3_qutrit_trilinear"
            and data["primitive_tensor"]["nonzero_tensor_slots"] > 0
            and data["primitive_tensor"]["selected_by_theorem"] is False,
            data["primitive_tensor"],
        ),
        check(
            "four C1 sectors emitted",
            set(matrices) == {"u", "d", "e", "nuD"},
            set(matrices),
        ),
        check(
            "canonical C1 response zero",
            data["diagnostics"]["all_c1_matrices_zero_for_canonical_tensor"] is True
            and all(value == 0.0 for value in matrix_norms.values()),
            matrix_norms,
        ),
        check(
            "response support recorded",
            all(data["diagnostics"]["response_support"][sector] for sector in ("Q", "u", "d", "L", "e", "N", "H")),
            data["diagnostics"]["response_support"],
        ),
        check(
            "superset repair classification",
            data["superset_mode"]["superset_repair"]["classification"]
            == "CANONICAL_TRANSLATION_INVARIANT_C1_ZERO_SELECTED_PRIMITIVE_NEEDED",
            data["superset_mode"],
        ),
        check(
            "no flavor claim",
            data["closure_claimed"] is False
            and data["target_fitting_used"] is False
            and data["superset_mode"]["diagnostic_backfit_only"]["observed_physical_data_used"] is False,
            data["superset_mode"]["diagnostic_backfit_only"],
        ),
        check(
            "remaining selected primitive open",
            data["what_remains_open"]["selected_noninvariant_C1_primitive_or_vertex"] is True
            and data["what_remains_open"]["nonzero_C1_response_matrices"] is True
            and data["what_remains_open"]["yukawa_CKM_PMNS_magnitudes"] is True,
            data["what_remains_open"],
        ),
        check(
            "note records implication",
            "Nonzero C1 response requires" in note
            and "No Yukawa, CKM, PMNS, or mass claim is made" in note,
            NOTE,
        ),
    ]
    print("\nMTT selected Route-C C1 primitive response on smooth B_N audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
