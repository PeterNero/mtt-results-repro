"""Build the typed monad D_E / rho_E data interface for Qa/SU3."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"

PREVIOUS = DATA / "source_certified_a01_erratum_or_monad_de_operator.candidate.json"
TEMPLATE = CERTS / "typed_monad_de_or_rhoe_data.template.json"
VALIDATOR = ROOT / "scripts" / "validate_typed_monad_packet.py"
OUTPUT_DATA = DATA / "typed_monad_de_or_rhoe_data_interface.candidate.json"
OUTPUT_CERT = CERTS / "typed_monad_de_or_rhoe_data_interface_certificate.json"


def run_validator() -> dict[str, object]:
    proc = subprocess.run([sys.executable, str(VALIDATOR), str(TEMPLATE)], cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return {"exit_code": proc.returncode, "output": proc.stdout.strip()}


def main() -> None:
    previous = json.loads(PREVIOUS.read_text(encoding="utf-8"))
    template = json.loads(TEMPLATE.read_text(encoding="utf-8"))
    validator_result = run_validator()
    acceptance_interface = {
        "typed_monad_required": [
            "line-bundle typed f map K1 -> direct_sum_i L_i",
            "line-bundle typed g map direct_sum_i L_i -> K2",
            "machine-checkable g*f=0",
            "locally-free/stability/HYM source certificate",
            "c1=0, c2=0, integral c3=6 retained from source data",
        ],
        "cochain_or_dolbeault_required": [
            "Cech C0,C1,C2 dimensions with d0,d1 and d1*d0=0",
            "or Dolbeault operator matrix / connection one-form packet",
            "selected bundle origin rather than diagnostic fixture",
        ],
        "representation_required": [
            "one of E, End(E), ad_SU3, associated_local_system",
            "trace normalization",
            "gauge quotient scheme",
            "zero-mode policy",
        ],
        "operator_exit_required": [
            "D_E packet with principal symbol, connection data, endomorphism_E, and heat/spectrum/torsion finite-part object",
            "or rho_E packet with generator data, metric compatibility, selected bundle origin, and validator pass",
        ],
    }
    candidate = {
        "candidate": "SelectedQaSU3TypedMonadDEOrRhoEDataInterface",
        "status": "TYPED_MONAD_DE_OR_RHOE_DATA_INTERFACE_BUILT_VALUES_OPEN",
        "input_statuses": {"previous_gate": previous["status"]},
        "template_path": str(TEMPLATE.relative_to(ROOT)),
        "validator_path": str(VALIDATOR.relative_to(ROOT)),
        "template_status": template["status"],
        "template_validator_result": validator_result,
        "acceptance_interface": acceptance_interface,
        "interface_result": {
            "interface_built": True,
            "validator_built": True,
            "open_template_refuses_to_compute": validator_result["exit_code"] == 2,
            "typed_monad_packet_available": False,
            "de_operator_packet_available": False,
            "rhoe_packet_available": False,
            "operator_packet_fillable_now": False,
            "determinant_computable_now": False,
            "qa_su3_closed": False,
            "target_fitting_used": False,
        },
        "do_not_use": template["forbidden_inputs"],
        "next_required_artifact": "Selected_Qa_SU3_Typed_Monad_Data_Fill_Attempt_v1",
        "target_fitting_used": False,
    }
    certificate = {
        "certificate": "SelectedQaSU3TypedMonadDEOrRhoEDataInterface",
        "status": "QA_SU3_TYPED_MONAD_DE_OR_RHOE_DATA_INTERFACE_BUILT_VALUES_OPEN",
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "template_path": str(TEMPLATE.relative_to(ROOT)),
        "validator_path": str(VALIDATOR.relative_to(ROOT)),
        "what_closes": {
            "typed_monad_packet_interface_built": True,
            "validator_built": True,
            "open_template_refuses_to_compute": validator_result["exit_code"] == 2,
            "acceptance_requirements_explicit": True,
        },
        "what_remains_open": {
            "typed_f_g_maps": True,
            "selected_representation_trace": True,
            "D_E_or_rhoE_packet": True,
            "endomorphism_E": True,
            "finite_part_data": True,
            "qa_su3_packet_closed": False,
        },
        "next_required_artifact": candidate["next_required_artifact"],
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    data_text = json.dumps(candidate, indent=2, sort_keys=True)
    cert_text = json.dumps(certificate, indent=2, sort_keys=True)
    if "--write" in sys.argv:
        OUTPUT_DATA.write_text(data_text + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
