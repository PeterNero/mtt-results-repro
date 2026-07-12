"""Audit the selected dotD alpha1 transport-derivative probe."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_dotd_alpha1_transport_derivative_probe.py"
CANDIDATE = ROOT / "candidate_data" / "selected_dotd_alpha1_transport_derivative_probe.candidate.json"
CERT = ROOT / "certificates" / "selected_dotd_alpha1_transport_derivative_probe_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_dotD_alpha1_TransportDerivative_Probe_v1.md"

STATUS = "MTT_SELECTED_DOTD_ALPHA1_TRANSPORT_DERIVATIVE_CLOSED_DRIVER_NORMALIZATION_OPEN"
NEXT = "MTT_Selected_Alpha1_SourceStrength_Normalization_or_Driver_Theorem_v1"


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
    formula = data["transport_derivative_formula"]
    driver = data["driver_audit"]
    boundary = data["validator_boundary"]
    decision = data["promotion_decision"]

    tests = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, data["status"]),
        check("certificate path", cert["candidate_path"].endswith(CANDIDATE.name), cert),
        check(
            "transport derivative theorem proved",
            theorem["proved"] is True
            and "D_sel(delta psi)+dotD_h psi_sel=0" in formula["identity"]
            and cert["transport_derivative_formula_closed"] is True,
            theorem,
        ),
        check(
            "source formula closes",
            decision["selected_dotD_source_formula_closed"] is True
            and decision["selected_dotD_source_verified_by_transport_derivative"] is True
            and cert["selected_dotD_source_verified_by_transport_derivative"] is True,
            decision,
        ),
        check(
            "driver still open",
            driver["alpha1_driver_verified_now"] is False
            and decision["alpha1_driver_verified"] is False
            and cert["alpha1_driver_verified"] is False
            and driver["h_ext_residual_l2"] < 1e-12,
            driver,
        ),
        check(
            "validator boundary exact",
            boundary["mathematical_dotd_matrices_pass_if_flags_are_theorem_derived"] is True
            and boundary["source_only_fails_only_by_alpha1_driver"] is True
            and boundary["promote_full_flags_now"] is False,
            boundary,
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
            "next gate recorded",
            data["next_required_artifact"] == NEXT
            and f"Next artifact: `{NEXT}`" in note
            and "alpha1 driver is still not promoted" in note,
            NOTE,
        ),
    ]

    print("\nMTT selected dotD alpha1 transport-derivative probe audit")
    return 0 if all(tests) else 1


if __name__ == "__main__":
    sys.exit(main())
