"""Audit Selected_PhiFin_S2_A_sel_N_Form_Bound_Interface_v1."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_phifin_s2_a_sel_n_form_bound_interface_certificate.json"
PACKET = REPO / "candidate_data" / "selected_phifin_s2_a_sel_n_form_bound_interface.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_PhiFin_S2_A_sel_N_Form_Bound_Interface_v1.md"
SCRIPT = REPO / "scripts" / "build_selected_phifin_s2_a_sel_n_form_bound_interface.py"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(name: str, condition: bool, detail: object) -> bool:
    status = "PASS" if condition else "FAIL"
    print(f"{status}: {name} -- {detail}")
    return condition


def main() -> int:
    cert = load(CERT)
    packet = load(PACKET)
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
    model = packet["A_model_N_summary"]
    evaluated = packet["evaluated_existing_payloads"]
    schema = packet["accepted_payload_schema"]
    closure = packet["current_closure"]

    ok = True
    ok &= check(
        "certificate status",
        cert["status"] == "A_SEL_N_FORM_BOUND_INTERFACE_BUILT_VALUES_OPEN",
        cert["status"],
    )
    ok &= check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])
    ok &= check(
        "A_model_N summary",
        model["basis_id"] == "F3xF3_gerbe_twisted_fourier_N1_rank3"
        and model["shape"] == [27, 27]
        and model["dimension"] == 27
        and model["complement_gap"] == 4.386490844928603
        and model["source_status"] == "model_active_not_selected",
        model,
    )
    ok &= check(
        "schema threshold",
        schema["dimension"] == 27
        and schema["acceptance_rule"]["eta_N_threshold"] == 2.1932454224643014
        and "A_sel_N" in schema["one_of"]["explicit_operator"],
        schema["acceptance_rule"],
    )
    ok &= check(
        "small solve rejected",
        evaluated["small_strominger_galerkin_solve_de_action"]["accepted_as_A_sel_N"] is False
        and evaluated["small_strominger_galerkin_solve_de_action"]["basis_id"] is None,
        evaluated["small_strominger_galerkin_solve_de_action"],
    )
    ok &= check(
        "27-mode unpromoted payload rejected",
        evaluated["smooth_BN_27_mode_DE_honest"]["all_slots_27x27"] is True
        and evaluated["smooth_BN_27_mode_DE_honest"][
            "selected_source_verified_all_sectors"
        ]
        is False
        and evaluated["smooth_BN_27_mode_DE_honest"]["accepted_as_A_sel_N"] is False,
        evaluated["smooth_BN_27_mode_DE_honest"],
    )
    ok &= check(
        "closure remains open",
        closure["interface_built"] is True
        and closure["A_model_N_available"] is True
        and closure["A_sel_N_available"] is False
        and closure["eta_N_bound_available"] is False
        and closure["selected_gap_error_closed"] is False,
        closure,
    )
    ok &= check(
        "guardrails",
        cert["guardrails"]["does_not_accept_dimension_mismatch"] is True
        and cert["guardrails"]["does_not_accept_unpromoted_model_active_payload_as_A_sel_N"]
        is True
        and cert["guardrails"]["does_not_claim_eta_N_computed"] is True,
        cert["guardrails"],
    )
    ok &= check(
        "note records interface",
        "27 x 27" in note and "selected-source flags remain false" in note,
        NOTE,
    )

    print("\nSelected PhiFin S2 A_sel,N form-bound interface audit")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
