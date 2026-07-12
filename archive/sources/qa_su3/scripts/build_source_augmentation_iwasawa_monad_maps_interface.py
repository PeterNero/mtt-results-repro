"""Build the source-augmentation packet interface for Iwasawa monad maps."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PREVIOUS = CERTS / "iwasawa_automorphy_cocycle_data_or_nogo_certificate.json"
TEMPLATE = CERTS / "source_augmentation_iwasawa_monad_maps.template.json"
VALIDATOR = ROOT / "scripts" / "validate_source_augmentation_iwasawa_monad_maps.py"
OUTPUT_DATA = DATA / "source_augmentation_iwasawa_monad_maps_interface.candidate.json"
OUTPUT_CERT = CERTS / "source_augmentation_iwasawa_monad_maps_interface_certificate.json"
OUTPUT_NOTE = CORPUS / "Selected_Qa_SU3_Source_Augmentation_Packet_for_Iwasawa_Monad_Maps_v1.md"


def run_validator() -> dict[str, object]:
    proc = subprocess.run([sys.executable, str(VALIDATOR), str(TEMPLATE)], cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return {"exit_code": proc.returncode, "output": proc.stdout.strip()}


def build() -> tuple[dict[str, object], dict[str, object], str]:
    previous = json.loads(PREVIOUS.read_text(encoding="utf-8"))
    template = json.loads(TEMPLATE.read_text(encoding="utf-8"))
    validator = run_validator()
    acceptance_requirements = {
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
    }
    interface_result = {
        "interface_built": True,
        "validator_built": True,
        "open_template_refuses_to_compute": validator["exit_code"] == 2,
        "augmentation_packet_available": False,
        "explicit_f_g_constructed": False,
        "operator_exit_available": False,
        "qa_su3_closed": False,
        "target_fitting_used": False,
    }
    candidate = {
        "candidate": "SelectedQaSU3SourceAugmentationIwasawaMonadMapsInterface",
        "status": "QA_SU3_SOURCE_AUGMENTATION_IWASAWA_MONAD_MAPS_INTERFACE_BUILT_VALUES_OPEN",
        "input_status": {"automorphy_cocycle_nogo": previous["status"]},
        "template_path": str(TEMPLATE.relative_to(ROOT)),
        "validator_path": str(VALIDATOR.relative_to(ROOT)),
        "template_status": template["status"],
        "template_validator_result": validator,
        "acceptance_requirements": acceptance_requirements,
        "interface_result": interface_result,
        "next_required_artifact": {
            "name": "Selected_Qa_SU3_Source_Augmentation_Packet_Fill_Attempt_v1",
            "must_attempt": [
                "fill the source certificate fields from corpus or an amended source",
                "run the validator",
                "if complete, transfer to typed monad D_E/rho_E packet",
            ],
        },
        "target_fitting_used": False,
    }
    certificate = {
        "certificate": candidate["candidate"],
        "status": candidate["status"],
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "template_path": candidate["template_path"],
        "validator_path": candidate["validator_path"],
        "template_status": candidate["template_status"],
        "template_validator_result": validator,
        "acceptance_requirements": acceptance_requirements,
        "interface_result": interface_result,
        "next_required_artifact": candidate["next_required_artifact"],
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    return candidate, certificate, render_note(candidate)


def render_note(candidate: dict[str, object]) -> str:
    return f"""# Selected Qa/SU3 Source Augmentation Packet for Iwasawa Monad Maps v1

## Purpose

This artifact defines the exact packet needed to turn the Iwasawa `SU(3)` monad from a topological source into checked typed maps and an operator exit.

## New Files

```text
certificates/source_augmentation_iwasawa_monad_maps.template.json
scripts/validate_source_augmentation_iwasawa_monad_maps.py
```

The validator returns:

```text
0 = complete packet passes implemented checks
1 = complete-looking packet fails a structural check
2 = packet is open or incomplete
```

For the current open template:

```text
validator exit code: {candidate["template_validator_result"]["exit_code"]}
validator output: {candidate["template_validator_result"]["output"]}
```

## Acceptance Requirements

A closing packet must supply:

```text
Gamma generator action on complex Iwasawa coordinates,
lattice generators,
left/right quotient convention,
charge-to-factor map q -> a_q(gamma,z),
cocycle and multiplicative charge-law checks,
c1 realization for the nonzero charges,
positive dimensions and bases for F1..F5, G1..G5, and P,
product constants m_i,
numeric f,g coefficients satisfying sum_i m_i f_i g_i = 0,
local-freeness and stability/HYM checks for the exact maps,
and one finite operator exit: Cech_Dolbeault, rho_E, or D_E.
```

## Verdict

```text
interface built: yes
validator built: yes
open template refuses to compute: yes
augmentation packet available: no
explicit f,g constructed: no
operator exit available: no
Qa/SU3 closed: no
target fitting used: no
```

Next artifact:

```text
{candidate["next_required_artifact"]["name"]}
```
"""


def main() -> None:
    candidate, certificate, note = build()
    data_text = json.dumps(candidate, indent=2, sort_keys=True)
    cert_text = json.dumps(certificate, indent=2, sort_keys=True)
    if "--write" in sys.argv:
        OUTPUT_DATA.write_text(data_text + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
