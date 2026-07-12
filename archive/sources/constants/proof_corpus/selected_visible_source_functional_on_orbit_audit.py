"""Audit Selected_Visible_Source_Functional_on_Antiunitary_Orbit_v1."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_visible_source_functional_on_orbit_classification_certificate.json"
SCRIPT = REPO / "scripts" / "classify_selected_visible_source_functional_on_orbit.py"
NOTE = REPO / "proof_corpus" / "Selected_Visible_Source_Functional_on_Antiunitary_Orbit_v1.md"


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
    candidates = cert["candidates"]
    next_obj = cert["next_closing_object"]
    guards = cert["guardrails"]

    ok = True
    ok &= check(
        "certificate status",
        cert["status"] == "VISIBLE_SOURCE_FUNCTIONAL_CLASSIFIED_CW_OPERATOR_SOURCE_NEXT",
        cert["status"],
    )
    ok &= check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])
    ok &= check(
        "functional classification closes",
        closed["orbit_available_for_functional"] is True
        and closed["finite_operator_packets_equivalent_on_orbit"] is True
        and closed["candidate_functional_classes_ranked"] is True
        and closed["q79_F_m1_visible_representative_is_best_current_clue"] is True
        and closed["S3_Deligne_GS_support_is_best_current_source_support"] is True
        and closed["next_target_reduced_to_same_source_Chern_Weil_operator_functional"] is True,
        closed,
    )
    ok &= check(
        "candidate statuses are honest",
        candidates["F0_conjugation_invariant_orbit_functional"]["status"]
        == "CLOSED_AS_ORBIT_ONLY_NOT_VISIBLE_SELECTOR"
        and candidates["F1_time_oriented_m1_representative_functional"]["status"]
        == "CONDITIONAL_SUPPORT_NOT_SOURCE_THEOREM"
        and candidates["F2_S3_Deligne_Green_Schwarz_source_support_functional"]["status"]
        == "PARTIAL_SOURCE_SUPPORT_OPERATOR_EXIT_OPEN"
        and candidates["F3_same_source_Chern_Weil_operator_functional"]["status"]
        == "NEXT_PROOF_TARGET",
        candidates,
    )
    ok &= check(
        "real closure remains open",
        not_closed["visible_representative_selected_by_theorem"] is True
        and not_closed["same_source_Chern_Weil_operator_row"] is True
        and not_closed["selected_D_E_dotD_Riesz_Green"] is True
        and not_closed["primitive_C1_contractions"] is True,
        not_closed,
    )
    ok &= check(
        "next object is CW operator source",
        next_obj["name"] == "Selected_Qa_SU3_M1_Chern_Weil_Operator_Source_v1"
        and len(next_obj["acceptance"]) == 4,
        next_obj,
    )
    ok &= check(
        "guardrails prevent premature selection",
        guards["claims_visible_q79_selected_now"] is False
        and guards["claims_q369_false_or_removed"] is False
        and guards["claims_selected_D_E_dotD_now"] is False
        and guards["claims_C1_or_Yukawa_closure"] is False
        and guards["claims_full_SM_closure"] is False
        and guards["uses_observed_cp_sign_or_masses"] is False,
        guards,
    )
    ok &= check(
        "note records classification",
        "F3: same-source Chern-Weil/operator functional" in note
        and "Selected_Qa_SU3_M1_Chern_Weil_Operator_Source_v1" in note
        and "does not yet claim q79 is visibly selected" in note,
        NOTE,
    )

    print("\nSelected visible source functional on antiunitary orbit audit")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
