"""Build the typed monad D_E / rho_E data interface for Qa/SU3."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
TEMPLATE = CERTS / "selected_qa_su3_typed_monad_de_or_rhoe_data.template.json"
PREVIOUS = CERTS / "selected_qa_su3_source_certified_a01_erratum_or_monad_de_operator_certificate.json"
VALIDATOR = ROOT / "scripts" / "validate_selected_qa_su3_typed_monad_packet.py"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def run_validator() -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(TEMPLATE)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return {"exit_code": proc.returncode, "output": proc.stdout.strip()}


def main() -> None:
    previous = load(PREVIOUS)
    template = load(TEMPLATE)
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

    output = {
        "certificate": "SelectedQaSU3TypedMonadDEOrRhoEDataInterface",
        "status": "QA_SU3_TYPED_MONAD_DE_OR_RHOE_DATA_INTERFACE_BUILT_VALUES_OPEN",
        "input_status": {
            "previous_gate": previous["status"],
        },
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
        "next_required_artifact": {
            "name": "Selected_Qa_SU3_Typed_Monad_Data_Fill_Attempt_v1",
            "must_attempt": [
                "fill typed f,g maps from source or derive them from monad construction",
                "run validator on the filled packet",
                "if D_E data is supplied, compute or certify endomorphism_E and finite part",
                "if rho_E data is supplied, run q79 rho_E validator and record metric/source compatibility",
            ],
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
