"""Audit the visible Route-C source identity / typed B_N derivative contract."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_visible_routec_sourceidentity_or_typedbn_derivative_contract.py"
CANDIDATE = ROOT / "candidate_data" / "visible_routec_sourceidentity_or_typedbn_derivative_contract.candidate.json"
TEMPLATE = ROOT / "candidate_data" / "visible_routec_sourceidentity_or_typedbn_derivative.template.json"
VALIDATOR = ROOT / "scripts" / "validate_visible_routec_sourceidentity_or_typedbn_derivative.py"
CERT = ROOT / "certificates" / "visible_routec_sourceidentity_or_typedbn_derivative_contract_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Visible_RouteC_SourceIdentity_or_TypedBNRetardedDerivative_Contract_v1.md"

STATUS = "MTT_VISIBLE_ROUTEC_SOURCEIDENTITY_OR_TYPEDBN_DERIVATIVE_CONTRACT_BUILT_VALUES_OPEN"
NEXT = "MTT_Visible_RouteC_SourceIdentity_or_TypedBNRetardedDerivative_Fill_v1"


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
    template = json.loads(TEMPLATE.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    required = data["required_certificate"]
    validation = data["template_validation"]

    tests = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, data["status"]),
        check(
            "paths",
            cert["candidate_path"].endswith(CANDIDATE.name)
            and cert["template_path"].endswith(TEMPLATE.name)
            and cert["validator_path"].endswith(VALIDATOR.name),
            cert,
        ),
        check(
            "packet values preserved",
            data["packet_values_preserved"]["lambda_alpha1"] == 1.0
            and data["packet_values_preserved"]["N_alpha1_h_ext"] == 1.0
            and cert["lambda_alpha1"] == 1.0,
            data["packet_values_preserved"],
        ),
        check(
            "both lanes are in schema",
            set(required["lane_A_fields"]) == {
                "source_identity",
                "visible_routec_operator_source",
                "phi_fin_payload",
                "same_branch_alpha1_derivative",
                "dotd_validator_replay",
            }
            and set(required["lane_B_fields"]) == {
                "retarded_source_selector",
                "typed_bn_alpha1_derivative",
                "selected_transfer_normalization",
                "sector_dotd_equality",
                "dotd_validator_replay",
            },
            required,
        ),
        check(
            "template open and fails validator now",
            template["status"] == "TEMPLATE_VALUES_TO_FILL"
            and validation["ok"] is False
            and validation["exit_code"] == 1
            and "certificate: neither lane validates" in validation["errors"],
            validation,
        ),
        check(
            "promotion guarded",
            template["promotion_result"]["selected_value_emitted"] is False
            and template["promotion_result"]["alpha1_driver_verified"] is False
            and "If either lane validates" in required["promotion_rule"],
            template["promotion_result"],
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
            and "typed_bn_alpha1_derivative" in note,
            NOTE,
        ),
    ]

    print("\nMTT visible Route-C source identity / typed B_N derivative contract audit")
    return 0 if all(tests) else 1


if __name__ == "__main__":
    sys.exit(main())
