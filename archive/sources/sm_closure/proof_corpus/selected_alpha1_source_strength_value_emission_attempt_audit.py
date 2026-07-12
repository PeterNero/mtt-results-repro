"""Audit the selected alpha1 source-strength value emission attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_alpha1_source_strength_value_emission_attempt.py"
CANDIDATE = ROOT / "candidate_data" / "selected_alpha1_source_strength_value_emission_attempt.candidate.json"
CERT = ROOT / "certificates" / "selected_alpha1_source_strength_value_emission_attempt_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Alpha1_SourceStrength_Value_Emission_Attempt_v1.md"

STATUS = "MTT_SELECTED_ALPHA1_SOURCE_STRENGTH_VALUE_EMISSION_ATTEMPT_BUILT_VALUE_OPEN"
NEXT = "MTT_Selected_SameSource_Alpha1_Normalization_Value_or_RetardedKernel_v1"


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
    attempt = data["emission_attempt"]
    routes = attempt["routes"]
    candidate_value = attempt["conditional_value_candidate"]

    tests = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, data["status"]),
        check("certificate path", cert["candidate_path"].endswith(CANDIDATE.name), cert),
        check(
            "unit candidate isolated",
            candidate_value["lambda_alpha1_candidate"] == 1.0
            and candidate_value["status"] == "CONDITIONAL_UNIT_SOURCE_STRENGTH_CANDIDATE_NOT_SELECTED"
            and candidate_value["h_ext_residual_l2"] < 1e-12,
            candidate_value,
        ),
        check(
            "route A rejects convention-only promotion",
            routes["route_A_unit_source_strength_coordinate"]["attempted"] is True
            and routes["route_A_unit_source_strength_coordinate"]["emitted_as_selected"] is False
            and routes["route_A_unit_source_strength_coordinate"]["prior_naive_scale_rejected"] is True,
            routes["route_A_unit_source_strength_coordinate"],
        ),
        check(
            "route B still lacks same-source normalization",
            routes["route_B_same_source_packet_or_transfer_normalization"][
                "selected_transfer_normalization"
            ]
            is False
            and routes["route_B_same_source_packet_or_transfer_normalization"][
                "same_source_packet_closed"
            ]
            is False,
            routes["route_B_same_source_packet_or_transfer_normalization"],
        ),
        check(
            "route C still lacks typed retarded derivative",
            routes["route_C_retarded_overlap_kernel_transfer"][
                "ckm_retarded_kernel_pattern_available"
            ]
            is True
            and routes["route_C_retarded_overlap_kernel_transfer"][
                "selected_BN_tangent_or_retarded_kernel"
            ]
            is False
            and routes["route_C_retarded_overlap_kernel_transfer"][
                "typed_sm_dotd_kernel_emitted"
            ]
            is False,
            routes["route_C_retarded_overlap_kernel_transfer"],
        ),
        check(
            "route D remains diagnostic only",
            routes["route_D_full_flag_validator_probe"][
                "validator_passes_if_flags_are_theorem_derived"
            ]
            is True
            and routes["route_D_full_flag_validator_probe"]["emitted_as_selected"] is False,
            routes["route_D_full_flag_validator_probe"],
        ),
        check(
            "selected value not emitted",
            attempt["selected_value_emitted"] is False
            and cert["selected_value_emitted"] is False
            and attempt["alpha1_driver_verified"] is False
            and attempt["honest_dotd_validator_closed"] is False,
            attempt,
        ),
        check(
            "no target fitting or closure",
            data["target_fitting_used"] is False
            and data["closure_claimed"] is False
            and cert["target_fitting_used"] is False
            and cert["closure_claimed"] is False,
            cert,
        ),
        check(
            "next gate recorded",
            data["next_required_artifact"] == NEXT
            and f"Next artifact: `{NEXT}`" in note
            and "lambda_alpha1 = 1" in note
            and "not yet emitted as a selected MTT value" in note,
            NOTE,
        ),
    ]

    print("\nMTT selected alpha1 source-strength value emission attempt audit")
    return 0 if all(tests) else 1


if __name__ == "__main__":
    sys.exit(main())
