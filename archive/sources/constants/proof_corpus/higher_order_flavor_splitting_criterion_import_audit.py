"""Audit Higher_Order_Flavor_Splitting_Criterion_Import_v1."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "higher_order_flavor_splitting_criterion_import_certificate.json"
SCRIPT = REPO / "scripts" / "import_higher_order_flavor_splitting_criterion.py"
NOTE = REPO / "proof_corpus" / "Higher_Order_Flavor_Splitting_Criterion_Import_v1.md"


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
        cert["status"] == "HIGHER_ORDER_FLAVOR_SPLITTING_CRITERION_IMPORTED_SELECTED_EMISSION_OPEN",
        cert["status"],
    )
    ok &= check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])
    ok &= check(
        "criterion and diagnostic search close",
        closed["current_scalar_permutation_layer_no_go_proved"] is True
        and closed["higher_order_splitting_criterion_proved"] is True
        and closed["full_response_acceptance_tests_locked"] is True
        and closed["diagnostic_splitter_found_without_observed_targets"] is True
        and closed["first_correction_matrix_search_executed"] is True,
        closed,
    )
    ok &= check(
        "selected emission remains open",
        not_closed["selected_correction_matrix_source"] is True
        and not_closed["selected_galerkin_values"] is True
        and not_closed["honest_replay_without_lifted_flags"] is True
        and not_closed["promoted_non_degenerate_yukawa_hierarchy"] is True
        and not_closed["promoted_CKM_PMNS_CP"] is True,
        not_closed,
    )
    ok &= check(
        "guardrails prevent diagnostic promotion",
        guards["claims_selected_flavor_hierarchy"] is False
        and guards["claims_selected_CKM_PMNS_CP"] is False
        and guards["claims_diagnostic_splitter_is_selected"] is False
        and guards["claims_full_SM_closure"] is False,
        guards,
    )
    ok &= check(
        "note records next gate",
        "Selected_Correction_Matrix_Source_or_Galerkin_Value_Emission_v1" in note
        and "diagnostic splitter is not selected MTT data" in note,
        NOTE,
    )

    print("\nHigher-order flavor splitting criterion import audit")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
