"""Build the source-augmentation packet interface for Iwasawa monad maps."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
PREVIOUS = CERTS / "selected_qa_su3_superset_source_route_map_certificate.json"
TEMPLATE = CERTS / "selected_qa_su3_source_augmentation_iwasawa_monad_maps.template.json"
VALIDATOR = ROOT / "scripts" / "validate_selected_qa_su3_source_augmentation_iwasawa_monad_maps.py"
OUTPUT_CERT = CERTS / "selected_qa_su3_source_augmentation_iwasawa_monad_maps_interface_certificate.json"


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
    validator = run_validator()

    output = {
        "certificate": "SelectedQaSU3SourceAugmentationIwasawaMonadMapsInterface",
        "status": "QA_SU3_SOURCE_AUGMENTATION_IWASAWA_MONAD_MAPS_INTERFACE_BUILT_VALUES_OPEN",
        "input_status": {"superset_route_map": previous["status"]},
        "template_path": str(TEMPLATE.relative_to(ROOT)),
        "validator_path": str(VALIDATOR.relative_to(ROOT)),
        "template_status": template["status"],
        "template_validator_result": validator,
        "acceptance_requirements": {
            "geometry": [
                "complex coordinate action of each Gamma generator",
                "lattice generators",
                "left/right quotient convention",
            ],
            "automorphy": [
                "charge_to_factor map q -> a_q(gamma,z)",
                "cocycle check",
                "multiplicative charge law",
                "c1 charge realization for the nonzero charges",
                "not flat-character-only",
            ],
            "sections": [
                "positive dimensions for F1..F5,G1..G5,P",
                "basis list for each section space",
                "section equivariance certified",
            ],
            "monad_maps": [
                "numeric f,g coefficient vectors",
                "numeric product constants m_i",
                "sum_i m_i f_i g_i = 0",
                "local-freeness and stability/HYM source checks",
            ],
            "operator_exit": [
                "one of Cech_Dolbeault, rho_E, or D_E",
                "finite part available",
            ],
        },
        "interface_result": {
            "interface_built": True,
            "validator_built": True,
            "open_template_refuses_to_compute": validator["exit_code"] == 2,
            "augmentation_packet_available": False,
            "explicit_f_g_constructed": False,
            "operator_exit_available": False,
            "qa_su3_closed": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": {
            "name": "Selected_Qa_SU3_Source_Augmentation_Packet_Fill_Attempt_v1",
            "must_attempt": [
                "fill the source certificate fields from corpus or an amended source",
                "run the validator",
                "if complete, transfer to typed monad D_E/rho_E packet",
            ],
        },
    }
    text = json.dumps(output, indent=2, sort_keys=True)
    if "--write-certificate" in sys.argv:
        OUTPUT_CERT.write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
