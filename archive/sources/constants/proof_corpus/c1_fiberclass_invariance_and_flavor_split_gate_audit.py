"""Audit C1_FiberClass_Invariance_and_Flavor_Split_Gate_v1."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "c1_fiberclass_invariance_and_flavor_split_gate_certificate.json"
SCRIPT = REPO / "scripts" / "import_c1_fiberclass_invariance_and_flavor_split_gate.py"
NOTE = REPO / "proof_corpus" / "C1_FiberClass_Invariance_and_Flavor_Split_Gate_v1.md"


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
    not_closed = cert["not_closed"]
    guards = cert["guardrails"]

    ok = True
    ok &= check(
        "certificate status",
        cert["status"] == "C1_FIBERCLASS_INVARIANCE_IMPORTED_FLAVOR_SPLIT_OPEN",
        cert["status"],
    )
    ok &= check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])
    ok &= check(
        "fiber-class invariance closes current observable ambiguity",
        closed["active_shift_1_1_forced_by_finite_support"] is True
        and closed["fixed_fiber_shifts_one_gauge_class"] is True
        and closed["observable_invariance_under_fixed_fiber_class_for_current_C1_spectrum"] is True
        and closed["absolute_fiber_origin_not_needed_for_current_spectral_invariants"] is True
        and closed["canonical_shift0_computation_gauge_allowed"] is True,
        closed,
    )
    ok &= check(
        "flavor splitting remains open",
        not_closed["selected_noninvariant_C1_primitive_or_vertex_source"] is True
        and not_closed["higher_order_or_full_strominger_response_support"] is True
        and not_closed["nondegenerate_yukawa_hierarchy"] is True
        and not_closed["CKM_PMNS_CP_from_selected_matrices"] is True,
        not_closed,
    )
    ok &= check(
        "guardrails prevent hierarchy overclaim",
        guards["claims_fiber_origin_physically_selected"] is False
        and guards["claims_nonzero_flavor_hierarchy"] is False
        and guards["claims_CKM_PMNS_CP_closure"] is False
        and guards["claims_full_SM_closure"] is False,
        guards,
    )
    ok &= check(
        "note records degeneracy and next gate",
        "Selected_Higher_Order_or_Full_Response_Flavor_Splitting_v1" in note
        and "degenerate" in note,
        NOTE,
    )

    print("\nC1 fiber-class invariance and flavor-split gate audit")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
