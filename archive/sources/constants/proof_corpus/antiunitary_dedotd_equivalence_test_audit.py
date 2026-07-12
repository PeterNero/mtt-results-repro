"""Audit Antiunitary_DEDotD_Equivalence_Test_v1."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "antiunitary_dedotd_equivalence_test_certificate.json"
SCRIPT = REPO / "scripts" / "attempt_antiunitary_dedotd_equivalence_test.py"
NOTE = REPO / "proof_corpus" / "Antiunitary_DEDotD_Equivalence_Test_v1.md"


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
    source_flags = cert["source_flags"]
    not_closed = cert["not_closed"]
    guards = cert["guardrails"]
    next_obj = cert["next_closing_object"]

    ok = True
    ok &= check(
        "certificate status",
        cert["status"] == "ANTIUNITARY_DEDOTD_EQUIVALENCE_TEST_PASSED_SOURCE_SELECTION_OPEN",
        cert["status"],
    )
    ok &= check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])
    ok &= check(
        "all current finite packet equivalence checks close",
        closed["branch_metadata_is_global_conjugate_pair"] is True
        and closed["D_E_action_slots_match_under_antiunitary_conjugation"] is True
        and closed["Green_Riesz_projector_slots_match_under_antiunitary_conjugation"] is True
        and closed["dotD_alpha1_and_horizontal_response_slots_match_under_antiunitary_conjugation"]
        is True
        and closed["operator_level_antiunitary_equivalence_for_current_finite_packets"] is True
        and closed["previous_C6_conjugate_pair_reduction_imported"] is True,
        closed,
    )
    ok &= check(
        "sector checks are exhaustive and true",
        all(
            all(field_checks.values())
            for family in cert["sector_checks"].values()
            for field_checks in family.values()
        ),
        cert["sector_checks"],
    )
    ok &= check(
        "source selection remains honestly open",
        source_flags["still_open_on_both_branches"] is True
        and not_closed["selected_source_origin"] is True
        and not_closed["retarded_or_source_boundary_selector_for_one_representative"] is True
        and not_closed["selected_D_E_dotD_source_flags"] is True,
        {"source_flags": source_flags, "not_closed": not_closed},
    )
    ok &= check(
        "next closing object is selected source or retarded selector",
        next_obj["name"] == "Retarded_Source_Boundary_Selector_or_Selected_Source_Origin_v1"
        and len(next_obj["must_prove"]) == 3,
        next_obj,
    )
    ok &= check(
        "guardrails prevent overclaim",
        guards["claims_q79_selected_over_q369"] is False
        and guards["claims_selected_source_origin"] is False
        and guards["claims_selected_D_E_dotD"] is False
        and guards["claims_primitive_C1_contractions"] is False
        and guards["claims_full_SM_closure"] is False
        and guards["uses_observed_cp_sign_or_masses"] is False
        and guards["uses_benchmark_flavor_entries"] is False,
        guards,
    )
    ok &= check(
        "note records closure and boundary",
        "current finite operator packets are antiunitarily equivalent: yes" in note
        and "does not select q79 over q369" in note
        and "Retarded_Source_Boundary_Selector_or_Selected_Source_Origin_v1" in note,
        NOTE,
    )

    print("\nAntiunitary D_E/dotD equivalence test audit")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
