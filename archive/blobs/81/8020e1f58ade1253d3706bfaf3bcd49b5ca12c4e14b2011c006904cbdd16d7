"""Audit NonInvariant_C1_FiberClass_Reduction_Import_v1."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "noninvariant_c1_fiberclass_reduction_certificate.json"
SCRIPT = REPO / "scripts" / "import_noninvariant_c1_fiberclass_reduction.py"
NOTE = REPO / "proof_corpus" / "NonInvariant_C1_FiberClass_Reduction_Import_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(name: str, condition: bool, detail: object) -> bool:
    status = "PASS" if condition else "FAIL"
    print(f"{status}: {name} -- {detail}")
    return condition


def main() -> int:
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    script_cert = json.loads(proc.stdout)
    closed = cert["closed_now"]
    finite = cert["finite_result"]
    meaning = cert["meaning"]
    not_closed = cert["not_closed"]
    guards = cert["guardrails"]

    ok = True
    ok &= check(
        "certificate status",
        cert["status"] == "NONINVARIANT_C1_FIBERCLASS_REDUCTION_IMPORTED_SELECTED_SOURCE_OPEN",
        cert["status"],
    )
    ok &= check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])
    ok &= check(
        "active and fiber reduction closes",
        closed["active_shift_1_1_forced_by_finite_support"] is True
        and closed["fixed_fiber_shifts_one_qutrit_gauge_class"] is True
        and closed["all_fiber_envelope_retired"] is True,
        closed,
    )
    ok &= check(
        "finite candidate content sane",
        finite["nonzero_unselected_candidates_found"] == 4
        and finite["nonzero_active_shifts"] == [[1, 1]]
        and finite["active_shift_necessary_and_sufficient_for_nonzero"] is True,
        finite,
    )
    ok &= check(
        "source promotion still open",
        meaning["source_has_period_three_projective_class"] is True
        and meaning["operator_level_projective_class_selected"] is False
        and meaning["selected_noninvariant_primitive_source_proved"] is False,
        meaning,
    )
    ok &= check(
        "true gates remain open",
        not_closed["selected_noninvariant_C1_primitive_or_vertex_source"] is True
        and not_closed["observable_invariance_under_fixed_fiber_class"] is True
        and not_closed["yukawa_CKM_PMNS_magnitudes"] is True,
        not_closed,
    )
    ok &= check(
        "guardrails prevent overclaim",
        guards["claims_selected_C1_source"] is False
        and guards["claims_nonzero_selected_C1_response"] is False
        and guards["claims_yukawa_CKM_PMNS_magnitudes"] is False
        and guards["claims_full_SM_closure"] is False,
        guards,
    )
    ok &= check(
        "note records next gate",
        "Selected_C1_Response_Operator_Emission_or_FiberClass_Invariant_Observable_v1" in note
        and "Nonzero one-response C1 matrices occur" in note
        and "only for active shift `(1,1)`" in note,
        NOTE,
    )

    print("\nNon-invariant C1 fiber-class reduction audit")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
