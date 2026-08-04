"""Audit Selected_PhiFin_S2_Operator_Scaffold_Import_v1."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_phifin_s2_operator_scaffold_import_certificate.json"
PACKET = REPO / "candidate_data" / "selected_phifin_s1s2_value_emission.s2_scaffold.json"
NOTE = REPO / "proof_corpus" / "Selected_PhiFin_S2_Operator_Scaffold_Import_v1.md"
SCRIPT = REPO / "scripts" / "import_selected_phifin_s2_operator_scaffold.py"


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
    s1 = packet["S1_transition_or_connection_trace"]
    s2 = packet["S2_galerkin_basis_and_operator_blocks"]
    guardrails = packet["partial_fill_guardrail"]

    ok = True
    ok &= check(
        "certificate status",
        cert["status"] == "SELECTED_PHIFIN_S2_OPERATOR_SCAFFOLD_IMPORTED_SELECTED_VALUES_OPEN",
        cert["status"],
    )
    ok &= check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])
    ok &= check(
        "S1 partial rhoE retained",
        s1["selected_connection_or_rhoE_entries"]["status"]
        == "PARTIAL_FILLED_PROJECTIVE_RHOE_TRACE"
        and s1["nonidentity_or_equivalent_connection_trace"] is True,
        s1["selected_connection_or_rhoE_entries"]["status"],
    )
    ok &= check(
        "same S2 basis imported",
        s2["basis_BN_or_Cech_basis_entries"]["basis_id"]
        == "F3xF3_gerbe_twisted_fourier_N1_rank3"
        and s2["basis_BN_or_Cech_basis_entries"]["same_basis_as_S1_rhoE_deck_shadow"] is True,
        s2["basis_BN_or_Cech_basis_entries"],
    )
    ok &= check(
        "D_E and dotD scaffold shapes imported",
        s2["D_E_matrix_entries"]["status"] == "SCAFFOLD_IMPORTED_NOT_SELECTED_VALUES"
        and s2["D_E_matrix_entries"]["shape_checks_pass"] is True
        and s2["D_E_matrix_entries"]["sector_shapes"]["Q"]["matrix_shape"] == [24, 27]
        and s2["D_E_matrix_entries"]["sector_shapes"]["H"]["matrix_shape"] == [26, 27]
        and s2["dotD_alpha1_matrix_entries"]["sector_shapes"]["Q"]["matrix_shape"] == [27, 27],
        {
            "D_E": s2["D_E_matrix_entries"]["sector_shapes"]["Q"],
            "dotD": s2["dotD_alpha1_matrix_entries"]["sector_shapes"]["Q"],
        },
    )
    ok &= check(
        "source flags remain false",
        s2["D_E_matrix_entries"]["selected_source_verified"] is False
        and s2["dotD_alpha1_matrix_entries"]["selected_dotD_source_verified"] is False
        and s2["dotD_alpha1_matrix_entries"]["alpha1_driver_verified"] is False,
        {
            "D_E": s2["D_E_matrix_entries"]["selected_source_verified"],
            "dotD": s2["dotD_alpha1_matrix_entries"]["selected_dotD_source_verified"],
            "alpha1": s2["dotD_alpha1_matrix_entries"]["alpha1_driver_verified"],
        },
    )
    ok &= check(
        "selected validators remain open",
        packet["validator_replay"]["scaffold_shape_validator_passes"] is True
        and packet["validator_replay"]["D_E_validator_passes"] is False
        and packet["validator_replay"]["Riesz_gap_validator_passes"] is False
        and packet["validator_replay"]["reduced_Green_validator_passes"] is False
        and packet["validator_replay"]["dotD_response_validator_passes"] is False,
        packet["validator_replay"],
    )
    ok &= check(
        "guardrails prevent overclaim",
        guardrails["full_selected_payload_emitted"] is False
        and guardrails["selected_source_flags_may_be_set_true"] is False
        and guardrails["S2_scaffold_imported_but_selected_values_open"] is True
        and cert["guardrails"]["claims_selected_D_E_values_emitted"] is False
        and cert["guardrails"]["claims_selected_dotD_values_emitted"] is False,
        guardrails,
    )
    ok &= check(
        "note records scaffold boundary",
        "scaffold import, not selected value emission" in note
        and "honest Route-C replay without lifted flags" in note,
        NOTE,
    )

    print("\nSelected PhiFin S2 operator scaffold import audit")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
