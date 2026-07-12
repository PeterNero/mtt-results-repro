"""Audit the selected Phi_fin payload or B_N basis emission contracts."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "candidate_data" / "selected_phifin_payload_or_bn_basis_emission.candidate.json"
CERT = REPO / "certificates" / "selected_phifin_payload_or_bn_basis_emission_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_PhiFin_Payload_or_BN_Basis_Emission_v1.md"


def check(name: str, condition: bool, detail: object) -> tuple[str, bool, object]:
    return name, condition, detail


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    phifin_path = REPO / data["contracts"]["selected_phifin_payload"]
    bn_path = REPO / data["contracts"]["selected_bn_basis"]
    phifin = json.loads(phifin_path.read_text(encoding="utf-8"))
    bn = json.loads(bn_path.read_text(encoding="utf-8"))

    expected_order = [
        "R1_selected_source_certificate",
        "R2_selected_rhoE_metric_connection",
        "R4_selected_basis_data",
        "R3_selected_operator_spectral_data",
        "R5_selected_C1_response",
        "R6_replay_without_lifted_flags",
    ]
    checks = [
        check(
            "status",
            data["status"] == "MTT_SELECTED_PHIFIN_OR_BN_EMISSION_CONTRACTS_LOCKED_VALUES_OPEN",
            data["status"],
        ),
        check("certificate agreement", cert["status"] == data["status"], cert["status"]),
        check(
            "contracts exist",
            phifin_path.exists() and bn_path.exists()
            and phifin["status"] == "OPEN_SELECTED_VALUES_NOT_EMITTED"
            and bn["status"] == "OPEN_SELECTED_BASIS_NOT_EMITTED",
            data["contracts"],
        ),
        check(
            "remaining parts locked",
            set(data["remaining_parts"].keys()) == set(expected_order)
            and data["dependency_order"] == expected_order
            and all(value is False for value in data["closure_vector"].values()),
            data["remaining_parts"],
        ),
        check(
            "Phi_fin fields locked",
            "rho_E transition data" in phifin["required_outputs"]
            and "dotD_alpha1_matrices" in phifin["minimum_selected_payload_fields"]
            and "route_c_residual.selected_source_verified" in phifin["flags_that_must_be_theorem_derived"],
            phifin,
        ),
        check(
            "B_N fields locked",
            bn["closed_support"]["candidate_deck_generators"] is True
            and bn["required_fields"]["scalar_basis_functions_phi_m"] is True
            and bn["required_fields"]["selected_D_E_action_on_basis"] is True,
            bn,
        ),
        check(
            "support not closure",
            data["support_vector"]["formal_lift_algebra_passes"] is True
            and data["what_remains_open"]["R1_selected_source_certificate"] is True
            and data["what_remains_open"]["R6_replay_without_lifted_flags"] is True,
            data["support_vector"],
        ),
        check(
            "no target fitting",
            data["target_fitting_used"] is False
            and cert["target_fitting_used"] is False
            and data["superset_mode"]["diagnostic_backfit_only"]["observed_physical_data_used"] is False,
            data["superset_mode"]["diagnostic_backfit_only"],
        ),
        check(
            "closure not claimed",
            data["closure_claimed"] is False
            and cert["closure_claimed"] is False
            and data["what_remains_open"]["full_SM_or_no_knob_closure"] is True,
            cert,
        ),
        check(
            "next artifact",
            data["next_required_artifact"] == "MTT_Selected_RouteC_R1_Source_Certificate_or_R4_BN_Basis_Fill_v1"
            and cert["primary_next_artifact"] == data["next_required_artifact"],
            cert["primary_next_artifact"],
        ),
        check(
            "note records emission target",
            "selected `Phi_fin`" in note and "selected quotient/deck-valid `B_N`" in note,
            NOTE,
        ),
    ]

    failed = False
    for name, condition, detail in checks:
        status = "PASS" if condition else "FAIL"
        print(f"{status}: {name} -- {detail}")
        if not condition:
            failed = True
    print("\nMTT selected Phi_fin payload or B_N basis emission audit")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
