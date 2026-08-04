"""Build the Hessian/kernel central-cocycle derivation interface."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

SEARCH = DATA / "central_cocycle_map_source_search_or_derivation.candidate.json"
VALIDATOR = ROOT / "scripts" / "validate_hessian_kernel_central_cocycle_derivation.py"
TEMPLATE = CERTS / "hessian_kernel_central_cocycle_derivation.template.json"
OUTPUT_DATA = DATA / "hessian_kernel_central_cocycle_derivation_interface.candidate.json"
OUTPUT_CERT = CERTS / "hessian_kernel_central_cocycle_derivation_interface_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Qa_SU3_Hessian_Kernel_Central_Cocycle_Derivation_Interface_v1.md"


def run_validator(path: Path) -> dict[str, object]:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(path)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return {"exit_code": proc.returncode, "output": proc.stdout.strip()}


def build_template() -> dict[str, object]:
    return {
        "schema": "SelectedQaSU3HessianKernelCentralCocycleDerivation.v1",
        "status": "OPEN_SELECTED_QA_SU3_HESSIAN_KERNEL_CENTRAL_COCYCLE_DERIVATION_REQUIRED",
        "source_identity": {
            "branch": None,
            "selection_rule": None,
            "source_certificate": None,
        },
        "hessian_block": {
            "H_sel_basis": None,
            "H_sel_matrix": None,
            "gauge_nullspace_policy": None,
            "positive_on_complement": None,
            "sector_restriction": None,
        },
        "retarded_kernel": {
            "G_ret_or_Green_matrix": None,
            "retarded_orientation_rule": None,
            "complement_projector": None,
            "kernel_identity_checked": None,
        },
        "twist_projection": {
            "Pi_tw_matrix_or_rule": None,
            "module_labels": ["F1", "F2", "F3", "F4", "F5", "G1", "G2", "G3", "G4", "G5", "P"],
            "charge_table": {
                "F1": [-3, 0, 1],
                "F2": [-2, 1, -1],
                "F3": [0, -1, 0],
                "F4": [0, 0, -1],
                "F5": [1, 1, 1],
                "G1": [2, 1, -1],
                "G2": [1, 0, 1],
                "G3": [-1, 2, 0],
                "G4": [-1, 1, 1],
                "G5": [-2, 0, -1],
                "P": [-1, 1, 0],
            },
        },
        "tau_extraction": {
            "extraction_formula": None,
            "module_twist_values": None,
            "central_2_cocycle_table": None,
            "period_denominator_or_smooth_unit": None,
            "cocycle_law_checked": None,
            "period_selected_by_H_sel_G_ret": None,
        },
        "admissibility": {
            "Green_Schwarz_Bianchi_checked": None,
            "Freed_Witten_checked": None,
            "projector_retention_checked": None,
            "zero_mode_policy": None,
            "stability_or_HYM_policy": None,
        },
        "response_payload": {
            "projective_rhoE": None,
            "D_E": None,
            "dotD": None,
            "Riesz_projector": None,
            "Green_operator": None,
            "heat_zeta_or_torsion_finite_part": None,
            "trace_normalization": None,
        },
        "guardrails": {
            "no_target_fitting": None,
            "no_q79_direct_import": None,
            "source_selected": None,
        },
    }


def build() -> tuple[dict[str, object], dict[str, object], str, dict[str, object]]:
    search = json.loads(SEARCH.read_text(encoding="utf-8"))
    template = build_template()
    TEMPLATE.write_text(json.dumps(template, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    validator_result = run_validator(TEMPLATE)
    interface_checks = {
        "template_built": True,
        "validator_built": True,
        "open_template_refuses_to_compute": validator_result["exit_code"] == 2,
        "requires_H_sel": True,
        "requires_G_ret": True,
        "requires_Pi_tw_tau_response": True,
        "qa_su3_packet_closed": False,
        "target_fitting_used": False,
    }
    candidate = {
        "candidate": "SelectedQaSU3HessianKernelCentralCocycleDerivationInterface",
        "status": "QA_SU3_HESSIAN_KERNEL_CENTRAL_COCYCLE_DERIVATION_INTERFACE_BUILT_VALUES_OPEN",
        "input_status": search["status"],
        "template_path": str(TEMPLATE.relative_to(ROOT)),
        "validator_path": str(VALIDATOR.relative_to(ROOT)),
        "template_validator_result": validator_result,
        "required_objects": search["derivation_interface"]["objects_to_supply"],
        "acceptance_equations": search["derivation_interface"]["acceptance_equations"],
        "interface_checks": interface_checks,
        "next_required_artifact": "Selected_Qa_SU3_Hessian_Kernel_Central_Cocycle_Fill_Attempt_v1",
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    certificate = {
        "certificate": candidate["candidate"],
        "status": candidate["status"],
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "template_path": candidate["template_path"],
        "validator_path": candidate["validator_path"],
        "template_validator_result": validator_result,
        "what_closes": {
            "strict_derivation_template_built": True,
            "validator_refuses_open_template": validator_result["exit_code"] == 2,
            "H_sel_G_ret_Pi_tau_response_requirements_encoded": True,
        },
        "what_remains_open": {
            "H_sel_values": True,
            "G_ret_values": True,
            "Pi_tw_values": True,
            "tau_extraction": True,
            "admissibility": True,
            "response_payload": True,
            "qa_su3_packet_closed": False,
        },
        "next_required_artifact": candidate["next_required_artifact"],
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    note = f"""# Selected Qa/SU3 Hessian Kernel Central Cocycle Derivation Interface v1

## Purpose

This is the executable interface for the derivation lane. It prevents a
Hessian/kernel argument from passing unless it supplies actual selected data.

## Required Objects

```text
H_sel    selected Hessian block on the Qa/SU3 c-twist/source sector
G_ret    retarded overlap or Green kernel on the admissible complement
Pi_tw    projection from Hessian/kernel data to twisted module labels
tau      central 2-cocycle/action extracted from H_sel and G_ret
response projective rho_E or D_E/dotD/Riesz/Green/heat/zeta/torsion payload
```

## Validator

```text
template: {candidate["template_path"]}
validator: {candidate["validator_path"]}
open-template exit code: {validator_result["exit_code"]}
open-template output: {validator_result["output"]}
```

The validator checks that a filled packet supplies all top-level data, refuses
target fitting and direct q79 import, and verifies the basic twist law:

```text
tau(F_i)+tau(G_i)=0 for i=1..5,
tau(P)=0.
```

It also requires the filled packet to carry the projective cocycle or response
payload from the same selected source.

## Verdict

```text
interface built: yes
validator built: yes
open template refuses to compute: yes
Qa/SU3 closed: no
target fitting used: no
```

Next artifact:

```text
{candidate["next_required_artifact"]}
```
"""
    return candidate, certificate, note, template


def main() -> None:
    candidate, certificate, note, _template = build()
    data_text = json.dumps(candidate, indent=2, sort_keys=True)
    cert_text = json.dumps(certificate, indent=2, sort_keys=True)
    if "--write" in sys.argv:
        OUTPUT_DATA.write_text(data_text + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
