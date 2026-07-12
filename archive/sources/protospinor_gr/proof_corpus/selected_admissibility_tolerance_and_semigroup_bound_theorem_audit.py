from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "selected_admissibility_tolerance_and_semigroup_bound_theorem_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")
    closed = cert["closed_inputs"]
    classifications = cert["source_classification"]
    rows = cert["finite_resolution_candidates_internal_only"]
    tests = cert["branch_selection_tests"]
    still_open = cert["still_open"]
    guards = cert["guardrails"]

    require(
        cert["status"] == "CQ_EPSILON_REDUCED_TO_FINITE_RESOLUTION_CANDIDATES_UNIQUE_SELECTION_OPEN",
        "unexpected C_Q/epsilon theorem status",
    )
    require(all(closed.values()), "all source inputs must be available")
    require([row["N"] for row in rows] == [64, 79, 448], "unexpected candidate N list")
    require(all(row["C_Q_candidate"] == 1.0 for row in rows), "C_Q candidates should be one")
    require(abs(rows[0]["epsilon_adm_candidate"] - 1 / 64) < 1e-15, "N=64 epsilon changed")
    require(abs(rows[1]["epsilon_adm_candidate"] - 1 / 79) < 1e-15, "N=79 epsilon changed")
    require(abs(rows[2]["epsilon_adm_candidate"] - 1 / 448) < 1e-15, "N=448 epsilon changed")
    require(tests["all_candidates_pass_R1_le_2_internal"] is True, "internal R1 test should pass")
    require(tests["unique_N_for_physical_Omega0_selected"] is False, "unique N should remain open")

    require(
        classifications["C_Q_equals_1"]["classification"]
        == "NORMALIZED_CONTRACTION_CANDIDATE_NOT_PHYSICAL_SOURCE_CERTIFIED",
        "C_Q classification changed",
    )
    require(
        classifications["epsilon_adm_equals_1_over_N"]["classification"]
        == "FINITE_RESOLUTION_CANDIDATE_NOT_UNIQUE_PHYSICAL_SELECTION",
        "epsilon classification changed",
    )

    require(still_open["C_Q_unique_physical_branch_value_sourced"] is False, "C_Q should remain open")
    require(still_open["epsilon_adm_unique_physical_branch_value_sourced"] is False, "epsilon should remain open")
    require(still_open["finite_resolution_N_for_Omega0_selected"] is False, "N should remain open")
    require(still_open["physical_Omega0_closed"] is False, "Omega0 should remain open")

    require(guards["chooses_N_by_target_fit"] is False, "must not target-fit N")
    require(guards["chooses_epsilon_from_Newton_or_Planck"] is False, "must not target-fit epsilon")
    require(guards["treats_internal_candidates_as_physical_prediction"] is False, "must not overclaim candidates")
    require(guards["claims_C_Q_equals_1_physical"] is False, "must not claim physical C_Q")
    require(guards["claims_unique_N_selected"] is False, "must not claim unique N")

    require("N in {64, 79, 448}" in note, "note must list finite candidates")
    require("not physical closure" in note.lower(), "note must reject physical closure")
    print("AUDIT_PASS: C_Q and epsilon_adm reduced to finite candidates; unique physical selection remains open")


if __name__ == "__main__":
    main()
