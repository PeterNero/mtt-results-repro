"""Audit Visible_Representative_Selection_in_Antiunitary_q79_q369_Orbit_v1."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "visible_representative_selection_orbit_certificate.json"
SCRIPT = REPO / "scripts" / "construct_visible_representative_selection_orbit.py"
NOTE = REPO / "proof_corpus" / "Visible_Representative_Selection_in_Antiunitary_q79_q369_Orbit_v1.md"


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
    still_open = cert["still_open"]
    guards = cert["guardrails"]
    policy = cert["visible_representative_policy"]
    next_obj = cert["next_closing_object"]

    ok = True
    ok &= check(
        "certificate status",
        cert["status"] == "ANTIUNITARY_ORBIT_RETAINED_VISIBLE_REPRESENTATIVE_SELECTION_OPEN",
        cert["status"],
    )
    ok &= check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])
    ok &= check(
        "orbit retained as full object",
        closed["antiunitary_orbit_is_the_correct_current_object"] is True
        and closed["q79_and_q369_both_retained_in_full_orbit"] is True
        and closed["q79_q369_not_independent_knobs"] is True
        and closed["q369_not_retired_from_full_universe_object"] is True,
        closed,
    )
    ok &= check(
        "visible representative remains open",
        closed["visible_representative_selection_identified_as_next_gate"] is True
        and still_open["which_representative_is_visible"] is True
        and still_open["selected_retarded_source_functional_on_orbit"] is True
        and still_open["selected_source_origin_flags"] is True,
        still_open,
    )
    ok &= check(
        "policy forbids wrong branch interpretation",
        "delete q369 as physically wrong" in policy["forbidden"]
        and "count q79 and q369 as separate parameter choices" in policy["forbidden"]
        and "retain the antiunitary partner as the conjugate presentation of the same full object"
        in policy["allowed"],
        policy,
    )
    ok &= check(
        "next object targets source functional",
        next_obj["name"] == "Selected_Visible_Source_Functional_on_Antiunitary_Orbit_v1"
        and len(next_obj["must_prove"]) == 4,
        next_obj,
    )
    ok &= check(
        "guardrails prevent visible-selection overclaim",
        guards["claims_q79_visible_selected"] is False
        and guards["claims_q369_false_or_retired"] is False
        and guards["claims_two_independent_universes"] is False
        and guards["claims_selected_source_origin"] is False
        and guards["claims_full_SM_closure"] is False
        and guards["uses_observed_cp_sign_or_masses"] is False,
        guards,
    )
    ok &= check(
        "note records refined interpretation",
        "{q79, q369}" in note
        and "q369 should not be treated as discarded or physically false" in note
        and "Selected_Visible_Source_Functional_on_Antiunitary_Orbit_v1" in note,
        NOTE,
    )

    print("\nVisible representative selection in antiunitary q79/q369 orbit audit")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
