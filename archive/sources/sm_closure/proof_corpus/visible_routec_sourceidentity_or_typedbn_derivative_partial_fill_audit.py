"""Audit the partial fill of the visible Route-C source identity gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_visible_routec_sourceidentity_or_typedbn_derivative_partial_fill.py"
CANDIDATE = ROOT / "candidate_data" / "visible_routec_sourceidentity_or_typedbn_derivative.partial_fill.json"
CERT = ROOT / "certificates" / "visible_routec_sourceidentity_or_typedbn_derivative_partial_fill_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Visible_RouteC_SourceIdentity_or_TypedBNRetardedDerivative_PartialFill_v1.md"

STATUS = "MTT_VISIBLE_ROUTEC_SOURCEIDENTITY_PARTIAL_FILL_ALPHA1_DERIVATIVE_OPEN"
NEXT = "MTT_Visible_RouteC_PhiFinAlpha1Derivative_Fill_v1"


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
    lane_a = data["lane_A_visible_routec_source_identity"]
    result = data["partial_fill_result"]
    validation = data["validation"]

    tests = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, data["status"]),
        check(
            "paths",
            cert["candidate_path"].endswith(CANDIDATE.name)
            and cert["note_path"].endswith(NOTE.name),
            cert,
        ),
        check(
            "stationary source identity promoted",
            lane_a["source_identity"]["selected_emitted"] is True
            and lane_a["source_identity"]["same_branch"] is True
            and lane_a["source_identity"]["theorem_derived"] is True
            and lane_a["source_identity"]["provenance"] == "symbolic_transport_conjugation_theorem",
            lane_a["source_identity"],
        ),
        check(
            "visible operator source promoted",
            lane_a["visible_routec_operator_source"]["selected_emitted"] is True
            and lane_a["visible_routec_operator_source"]["same_branch"] is True
            and lane_a["visible_routec_operator_source"]["theorem_derived"] is True,
            lane_a["visible_routec_operator_source"],
        ),
        check(
            "alpha1 blockers preserved",
            result["lane_A_phi_fin_alpha1_payload_closed"] is False
            and result["lane_A_same_branch_alpha1_derivative_closed"] is False
            and result["lane_A_dotd_validator_replay_closed"] is False
            and lane_a["dotd_validator_replay"]["honest_validator_exit_code"] == 1,
            result,
        ),
        check(
            "validator still fails honestly",
            validation["ok"] is False
            and validation["exit_code"] == 1
            and "certificate: neither lane validates" in validation["errors"]
            and cert["validator_ok"] is False,
            validation,
        ),
        check(
            "packet values preserved",
            data["packet_values_preserved"]["lambda_alpha1"] == 1.0
            and data["packet_values_preserved"]["N_alpha1_h_ext"] == 1.0
            and data["packet_values_preserved"]["tangent_residual_l2"] == 0.0,
            data["packet_values_preserved"],
        ),
        check(
            "no target fitting or closure",
            data["target_fitting_used"] is False
            and data["closure_claimed"] is False
            and cert["target_fitting_used"] is False
            and cert["closure_claimed"] is False
            and cert["alpha1_driver_verified"] is False,
            cert,
        ),
        check(
            "next gate recorded",
            data["next_required_artifact"] == NEXT
            and f"Next artifact: `{NEXT}`" in note
            and "`same_branch_alpha1_derivative`" in note,
            NOTE,
        ),
    ]

    print("\nMTT visible Route-C source identity partial fill audit")
    return 0 if all(tests) else 1


if __name__ == "__main__":
    sys.exit(main())
