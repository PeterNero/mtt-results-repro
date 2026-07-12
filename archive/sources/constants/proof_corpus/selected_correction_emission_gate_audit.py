"""Audit Selected_Correction_Matrix_Source_or_Galerkin_Value_Emission_v1."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_correction_emission_gate_certificate.json"
SCRIPT = REPO / "scripts" / "import_selected_correction_emission_gate.py"
NOTE = REPO / "proof_corpus" / "Selected_Correction_Matrix_Source_or_Galerkin_Value_Emission_v1.md"


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
        cert["status"]
        == "SELECTED_CORRECTION_EMISSION_GATE_REDUCED_NONIDENTITY_RHOE_AND_BN_CONSTRUCTION_OPEN",
        cert["status"],
    )
    ok &= check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])
    ok &= check(
        "diagnostic finite splitter recorded",
        closed["diagnostic_qutrit_splitter_exists"] is True
        and closed["diagnostic_splitter_not_promoted"] is True
        and closed["diagnostic_splitter_uses_no_observed_targets"] is True
        and closed["mass_mixing_cp_diagnostic_tests_nonzero"] is True,
        closed,
    )
    ok &= check(
        "strict primitive search does not close emission",
        closed["formal_lift_rejected_as_proof"] is True
        and closed["identity_rhoE_rejected_as_selected_payload"] is True
        and closed["strict_primitive_search_found_no_legal_emission"] is True,
        closed,
    )
    ok &= check(
        "selected source gates remain open",
        not_closed["selected_correction_matrix_source"] is True
        and not_closed["selected_galerkin_values"] is True
        and not_closed["honest_replay_without_lifted_flags"] is True
        and not_closed["promoted_non_degenerate_yukawa_hierarchy"] is True
        and not_closed["promoted_CKM_PMNS_CP"] is True,
        not_closed,
    )
    ok &= check(
        "guardrails prevent promotion",
        guards["claims_selected_flavor_hierarchy"] is False
        and guards["claims_selected_CKM_PMNS_CP"] is False
        and guards["claims_selected_correction_emission"] is False
        and guards["claims_full_SM_closure"] is False
        and guards["uses_observed_flavor_data"] is False,
        guards,
    )
    ok &= check(
        "note records next construction",
        "Selected_RouteC_NonIdentity_RhoE_and_QuotientValid_BN_Construction_v1" in note
        and "diagnostic qutrit search" in note,
        NOTE,
    )

    print("\nSelected correction-emission gate audit")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
