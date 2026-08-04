"""Audit the selected Qa/SU3 orientation D_E/dotD source attempt import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_orientation_dedotd_source_attempt_import_certificate.json"
SCRIPT = REPO / "scripts" / "import_selected_qa_su3_orientation_dedotd_source_attempt.py"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Orientation_DEDotD_Source_Attempt_Import_v1.md"


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
    replay = cert["validator_replay"]
    branch = cert["branch_status"]
    why_open = cert["why_it_does_not_close"]
    guards = cert["guardrails"]
    next_obj = cert["next_closing_object"]

    ok = True
    ok &= check(
        "certificate status",
        cert["status"] == "QA_SU3_ORIENTATION_DEDOTD_SOURCE_ATTEMPT_IMPORTED_SOURCE_ORIGIN_OPEN",
        cert["status"],
    )
    ok &= check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])
    ok &= check(
        "finite validator layer reached",
        closed["orientation_dedotd_validator_available"] is True
        and closed["finite_branch_data_reaches_DE_Green_dotD_layer"] is True
        and closed["finite_DE_and_dotD_validator_schemas_closed"] is True,
        closed,
    )
    ok &= check(
        "both conjugate branches checked",
        branch["current_q79_orientation"]["torsion_label_m"] == 1
        and branch["current_q79_orientation"]["global_cp_label"] == 79
        and branch["conjugate_q369_orientation"]["torsion_label_m"] == 2
        and branch["conjugate_q369_orientation"]["global_cp_label"] == 369
        and branch["unique_branch_selected_now"] is False,
        branch,
    )
    ok &= check(
        "validator replay remains open at source flags",
        replay["exit_code"] == 2
        and replay["status"] == "OPEN"
        and "selected_by_mtt must be true" in replay["first_open_items"]
        and "same_branch_derivative_verified must be true" in replay["first_open_items"],
        replay,
    )
    ok &= check(
        "subvalidators fail before source promotion",
        replay["subvalidator_exit_codes"]["selected_D_E_action"] == 1
        and replay["subvalidator_exit_codes"]["selected_reduced_green"] == 1
        and replay["subvalidator_exit_codes"]["selected_dotD_alpha1"] == 1,
        replay["subvalidator_exit_codes"],
    )
    ok &= check(
        "open reason is source origin",
        why_open["source_origin_open"] is True
        and why_open["selected_source_origin_constructed"] is False
        and why_open["unique_m_label_selected_by_source"] is False
        and why_open["selected_D_E_or_dotD_source_flags"] is True,
        why_open,
    )
    ok &= check(
        "next object names two honest routes",
        next_obj["name"] == "Selected_Source_Origin_or_Antiunitary_DEDotD_Equivalence_v1"
        and len(next_obj["route_A_selected_source_origin"]) == 4
        and len(next_obj["route_B_equivalence_then_retarded_selection"]) == 3,
        next_obj,
    )
    ok &= check(
        "guardrails prevent overclaim",
        guards["claims_selected_source_origin"] is False
        and guards["claims_unique_m_label_now"] is False
        and guards["claims_selected_D_E_or_dotD"] is False
        and guards["uses_observed_cp_sign_or_masses"] is False
        and guards["uses_lifted_selected_flags_as_proof"] is False,
        guards,
    )
    ok &= check(
        "note records boundary",
        "selected source origin: open" in note
        and "Selected_Source_Origin_or_Antiunitary_DEDotD_Equivalence_v1" in note,
        NOTE,
    )

    print("\nSelected Qa/SU3 orientation D_E/dotD source attempt import audit")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
