"""Audit the selected gauge-transported B_N Phi_fin trace theorem."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_gauge_transported_bn_phifin_trace.py"
CANDIDATE = ROOT / "candidate_data" / "selected_gauge_transported_bn_phifin_trace.candidate.json"
CERT = ROOT / "certificates" / "selected_gauge_transported_bn_phifin_trace_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_GaugeTransported_BN_PhiFin_Trace_v1.md"

STATUS = "MTT_SELECTED_GAUGE_TRANSPORTED_BN_PHIFIN_TRACE_PROVED_FINITE_REPLAY_OPEN"
NEXT = "MTT_Selected_TransportClosed_BN_Basis_or_ValidatorReplay_v1"


def check(name: str, condition: bool, detail: object) -> bool:
    print(("PASS" if condition else "FAIL") + f": {name} -- {detail}")
    return condition


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if proc.returncode != 0:
        print(proc.stdout)
        return 1

    data = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    theorem = data["theorem"]
    trace = data["transported_trace"]
    boundary = data["finite_replay_boundary"]
    decision = data["promotion_decision"]

    tests = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, data["status"]),
        check("certificate path", cert["candidate_path"].endswith(CANDIDATE.name), cert),
        check(
            "theorem proved",
            theorem["proved"] is True
            and "D(U psi)=U d psi" in theorem["proof_steps"][2]
            and cert["gauge_transported_trace_proved"] is True,
            theorem,
        ),
        check(
            "transport formulas emitted",
            trace["transport_operator"]["formula"] == "exp(-u ad(T3))"
            and trace["functional_identities"]["D_selected_U_equals_U_d"] is True
            and trace["functional_identities"]["P_selected_equals_U_P_model_U_inverse"] is True
            and trace["functional_identities"]["G_selected_equals_U_G_model_U_inverse_on_complement"] is True,
            trace["transport_operator"],
        ),
        check(
            "sector slots complete",
            len(trace["sector_slots"]) == 7
            and all(trace["sector_slots"][sector]["source_trace_selected_functionally"] is True for sector in trace["sector_slots"])
            and trace["sector_slots"]["H"]["transport_needed"] is False
            and trace["sector_slots"]["Q"]["transport_needed"] is True,
            trace["sector_slots"],
        ),
        check(
            "functional promotion closed",
            decision["functional_selected_trace_proved"] is True
            and decision["rho_candidate_promoted_to_functional_selected_rho_s"] is True
            and cert["functional_rho_s_promoted"] is True,
            decision,
        ),
        check(
            "finite replay still open",
            boundary["finite_27_mode_validator_replay_closed"] is False
            and boundary["direct_truncated_relative_residual_from_T1T2_probe"] > 0.01
            and cert["finite_validator_replay_closed"] is False,
            boundary,
        ),
        check(
            "dotD and alpha1 still open",
            decision["selected_dotD_source_verified"] is False
            and decision["alpha1_driver_verified"] is False
            and data["what_remains_open"]["selected_dotD_alpha1_with_transport_derivative"] is True,
            decision,
        ),
        check(
            "no closure or target fitting",
            data["closure_claimed"] is False
            and data["target_fitting_used"] is False
            and cert["closure_claimed"] is False
            and cert["target_fitting_used"] is False,
            cert,
        ),
        check(
            "note records theorem and boundary",
            "K_s^sel = U K_s^model" in note
            and "functional promotion of `rho_candidate` to selected `rho_s`" in note
            and "not yet finite validator replay" in note
            and f"Next artifact: `{NEXT}`" in note,
            NOTE,
        ),
    ]

    print("\nMTT selected gauge-transported B_N Phi_fin trace audit")
    return 0 if all(tests) else 1


if __name__ == "__main__":
    sys.exit(main())
