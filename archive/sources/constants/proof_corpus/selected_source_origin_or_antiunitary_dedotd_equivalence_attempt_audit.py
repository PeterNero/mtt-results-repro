"""Audit Selected_Source_Origin_or_Antiunitary_DEDotD_Equivalence_v1 attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_source_origin_or_antiunitary_dedotd_equivalence_attempt_certificate.json"
SCRIPT = REPO / "scripts" / "attempt_selected_source_origin_or_antiunitary_dedotd_equivalence.py"
NOTE = REPO / "proof_corpus" / "Selected_Source_Origin_or_Antiunitary_DEDotD_Equivalence_Attempt_v1.md"


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
    route_a = cert["route_A_selected_source_origin"]
    route_b = cert["route_B_antiunitary_then_retarded_selection"]
    next_artifact = cert["next_executable_artifact"]
    guards = cert["guardrails"]

    ok = True
    ok &= check(
        "certificate status",
        cert["status"]
        == "SOURCE_ORIGIN_OR_ANTIUNITARY_DEDOTD_EQUIVALENCE_REDUCED_OPERATOR_EQUIVALENCE_OPEN",
        cert["status"],
    )
    ok &= check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])
    ok &= check(
        "C6 conjugate pair closed",
        closed["C6_branch_space_reduced_to_global_conjugate_pair"] is True
        and closed["independent_channel_phase_knobs_removed"] is True
        and closed["q79_q369_labels_are_complex_conjugates_at_C6_phase_level"] is True
        and closed["not_two_unrelated_universes"] is True,
        closed,
    )
    ok &= check(
        "operator equivalence remains open",
        not_closed["operator_level_antiunitary_equivalence"] is True
        and not_closed["retarded_boundary_selector_for_orientation"] is True
        and not_closed["selected_D_E_dotD_source_flags"] is True,
        not_closed,
    )
    ok &= check(
        "route A and B are explicit",
        route_a["status"] == "OPEN"
        and route_b["status"] == "OPEN"
        and "selected visible bundle/twisted-gerbe/Route-C source origin" in route_a["first_missing"]
        and "operator-level antiunitary map between q79 and q369 D_E domains" in route_b["first_missing"],
        {"route_A": route_a, "route_B": route_b},
    )
    ok &= check(
        "next executable artifact specified",
        next_artifact["name"] == "Antiunitary_DEDotD_Equivalence_Test_v1"
        and len(next_artifact["must_compare"]) == 4,
        next_artifact,
    )
    ok &= check(
        "guardrails prevent branch overclaim",
        guards["claims_selected_source_origin"] is False
        and guards["claims_operator_antiunitary_equivalence_proved"] is False
        and guards["claims_retarded_orientation_selected"] is False
        and guards["claims_selected_D_E_dotD"] is False
        and guards["uses_observed_cp_sign_or_masses"] is False,
        guards,
    )
    ok &= check(
        "note records boundary",
        "Antiunitary_DEDotD_Equivalence_Test_v1" in note
        and "does not select q79 over q369" in note,
        NOTE,
    )
    print("\nSelected source origin or antiunitary D_E/dotD equivalence attempt audit")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
