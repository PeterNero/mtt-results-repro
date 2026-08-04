"""Audit the Iwasawa monad-map source-augmentation packet interface."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_source_augmentation_iwasawa_monad_maps_interface_certificate.json"
TEMPLATE = REPO / "certificates" / "selected_qa_su3_source_augmentation_iwasawa_monad_maps.template.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Source_Augmentation_Packet_for_Iwasawa_Monad_Maps_v1.md"
SCRIPT = REPO / "scripts" / "build_selected_qa_su3_source_augmentation_iwasawa_monad_maps_interface.py"
VALIDATOR = REPO / "scripts" / "validate_selected_qa_su3_source_augmentation_iwasawa_monad_maps.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def run_script() -> dict:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    return json.loads(proc.stdout)


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    template = json.loads(TEMPLATE.read_text(encoding="utf-8"))
    computed = run_script()
    note = NOTE.read_text(encoding="utf-8")
    validator_proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(TEMPLATE)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    result = cert["interface_result"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "QA_SU3_SOURCE_AUGMENTATION_IWASAWA_MONAD_MAPS_INTERFACE_BUILT_VALUES_OPEN",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["interface_result"] == cert["interface_result"]
            and computed["acceptance_requirements"] == cert["acceptance_requirements"],
            computed["interface_result"],
        ),
        check(
            "template remains open with no residual fitting",
            template["status"] == "OPEN_SELECTED_QA_SU3_SOURCE_AUGMENTATION_IWASAWA_MONAD_MAPS_REQUIRED"
            and template["selected_branch"]["target_residual_used"] is False
            and "observed Qa/SU3 residual" in template["forbidden_inputs"],
            template["selected_branch"],
        ),
        check(
            "validator refuses open template",
            validator_proc.returncode == 2 and "OPEN:" in validator_proc.stdout,
            validator_proc.stdout,
        ),
        check(
            "acceptance requirements include all hard gates",
            "charge_to_factor map q -> a_q(gamma,z)" in cert["acceptance_requirements"]["automorphy"]
            and "sum_i m_i f_i g_i = 0" in cert["acceptance_requirements"]["monad_maps"]
            and "one of Cech_Dolbeault, rho_E, or D_E" in cert["acceptance_requirements"]["operator_exit"],
            cert["acceptance_requirements"],
        ),
        check(
            "no closure claimed",
            result["interface_built"] is True
            and result["validator_built"] is True
            and result["open_template_refuses_to_compute"] is True
            and result["augmentation_packet_available"] is False
            and result["qa_su3_closed"] is False
            and result["target_fitting_used"] is False,
            result,
        ),
        check(
            "note records fill attempt next",
            "Selected_Qa_SU3_Source_Augmentation_Packet_Fill_Attempt_v1" in note
            and "open template refuses to compute: yes" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 source augmentation Iwasawa monad-map interface audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
