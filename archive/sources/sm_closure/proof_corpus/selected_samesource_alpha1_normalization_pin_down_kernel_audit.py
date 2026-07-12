"""Audit the selected same-source alpha1 normalization pin-down kernel."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_samesource_alpha1_normalization_pin_down_kernel.py"
CANDIDATE = ROOT / "candidate_data" / "selected_samesource_alpha1_normalization_pin_down_kernel.candidate.json"
TEMPLATE = ROOT / "candidate_data" / "selected_samesource_alpha1_normalization_packet.template.json"
CERT = ROOT / "certificates" / "selected_samesource_alpha1_normalization_pin_down_kernel_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_SameSource_Alpha1_Normalization_PinDown_Kernel_v1.md"

STATUS = "MTT_SELECTED_SAMESOURCE_ALPHA1_NORMALIZATION_PINDOWN_KERNEL_BUILT_PACKET_VALUES_OPEN"
NEXT = "MTT_Selected_SameSource_Alpha1_Normalization_Packet_Fill_v1"


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
    kernel = data["acceptance_kernel"]
    packet = data["packet_schema"]
    routes = data["route_status"]
    result = data["pin_down_result"]

    tests = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, data["status"]),
        check(
            "paths",
            cert["candidate_path"].endswith(CANDIDATE.name)
            and cert["template_path"].endswith(TEMPLATE.name),
            cert,
        ),
        check(
            "packet schema has five required fields",
            set(packet["required_fields"]) == {
                "source_identity",
                "source_strength_coordinate",
                "normalization_functional",
                "tangent_equality",
                "sector_dotd_equality",
            }
            and "declaring lambda_alpha1=1 by coordinate convention alone"
            in packet["forbidden_inputs"],
            packet,
        ),
        check(
            "acceptance kernel is iff and guarded",
            len(kernel["promotes_value_if_and_only_if"]) == 6
            and kernel["selected_value_when_passed"]["lambda_alpha1"] == 1.0
            and kernel["current_evaluation"]["selected_value_emitted_now"] is False,
            kernel,
        ),
        check(
            "routes remain open but classified",
            routes["route_A_same_source_packet"]["preferred"] is True
            and routes["route_A_same_source_packet"]["same_source_selected_fields"] == 0
            and routes["route_B_typed_BN_retarded_kernel"]["ckm_pattern_available"] is True
            and routes["route_B_typed_BN_retarded_kernel"][
                "selected_BN_tangent_or_retarded_kernel"
            ]
            is False,
            routes,
        ),
        check(
            "pin-down result does not promote",
            result["lambda_alpha1_candidate_pinned_as_unique_current_candidate"] is True
            and result["lambda_alpha1_selected_now"] is False
            and cert["selected_value_emitted"] is False
            and cert["alpha1_driver_verified"] is False,
            result,
        ),
        check(
            "template ready for fill",
            template["status"] == "TEMPLATE_VALUES_TO_FILL"
            and template["normalization_functional"]["N_alpha1_h_ext"] is None
            and template["tangent_equality"]["tolerance"] == 1e-12,
            template,
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
            and "selected alpha1 source-strength coordinate" in note
            and "N_alpha1(h_ext)=1" in note,
            NOTE,
        ),
    ]

    print("\nMTT selected same-source alpha1 normalization pin-down kernel audit")
    return 0 if all(tests) else 1


if __name__ == "__main__":
    sys.exit(main())
