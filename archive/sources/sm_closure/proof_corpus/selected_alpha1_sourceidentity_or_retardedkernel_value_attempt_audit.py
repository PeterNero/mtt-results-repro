"""Audit selected alpha1 source-identity or retarded-kernel value attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_alpha1_sourceidentity_or_retardedkernel_value_attempt.py"
CANDIDATE = ROOT / "candidate_data" / "selected_alpha1_sourceidentity_or_retardedkernel_value_attempt.candidate.json"
CERT = ROOT / "certificates" / "selected_alpha1_sourceidentity_or_retardedkernel_value_attempt_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Alpha1_SourceIdentity_or_RetardedKernel_Value_Attempt_v1.md"

STATUS = "MTT_SELECTED_ALPHA1_SOURCEIDENTITY_OR_RETARDEDKERNEL_VALUE_ATTEMPT_REDUCED_TO_SOURCE_CERTIFICATE_OPEN"
NEXT = "MTT_Selected_Visible_RouteC_SourceIdentity_Certificate_or_TypedBNRetardedDerivative_v1"


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
    packet = data["packet_result"]
    lane_a = data["proof_lanes"]["lane_A_same_source_identity"]
    lane_b = data["proof_lanes"]["lane_B_typed_retarded_kernel"]
    verdict = data["comparative_verdict"]

    tests = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, data["status"]),
        check("certificate path", cert["candidate_path"].endswith(CANDIDATE.name), cert),
        check(
            "packet value preserved",
            packet["lambda_alpha1"] == 1.0
            and packet["N_alpha1_h_ext"] == 1.0
            and packet["selected_value_emitted"] is False,
            packet,
        ),
        check(
            "lane A support but no selected identity",
            lane_a["support_closed"]["same_source_support_converges"] is True
            and lane_a["support_closed"]["gauge_transported_functional_trace"] is True
            and lane_a["support_closed"]["stationary_projector_source_replay"] is True
            and lane_a["selected_source_identity_emitted"] is False
            and lane_a["external_prefix"]["cw_theorem_proved"] is False,
            lane_a,
        ),
        check(
            "lane B support but no typed derivative",
            lane_b["support_closed"]["ckm_retarded_kernel_pattern_available"] is True
            and lane_b["support_closed"]["q79_and_q369_reach_de_green_dotd_layer"] is True
            and lane_b["typed_bn_retarded_derivative_emitted"] is False
            and lane_b["blocking_flags"]["selected_BN_tangent_or_retarded_kernel"] is False,
            lane_b,
        ),
        check(
            "minimal common object identified",
            verdict["neither_lane_closes_now"] is True
            and "selected visible/Route-C source certificate" in verdict["minimal_common_missing_object"],
            verdict,
        ),
        check(
            "no target fitting or closure",
            data["target_fitting_used"] is False
            and data["closure_claimed"] is False
            and cert["target_fitting_used"] is False
            and cert["closure_claimed"] is False
            and cert["selected_value_emitted"] is False,
            cert,
        ),
        check(
            "next gate recorded",
            data["next_required_artifact"] == NEXT
            and f"Next artifact: `{NEXT}`" in note
            and "typed B_N retarded alpha1 derivative" in note,
            NOTE,
        ),
    ]

    print("\nMTT selected alpha1 source-identity or retarded-kernel value attempt audit")
    return 0 if all(tests) else 1


if __name__ == "__main__":
    sys.exit(main())
