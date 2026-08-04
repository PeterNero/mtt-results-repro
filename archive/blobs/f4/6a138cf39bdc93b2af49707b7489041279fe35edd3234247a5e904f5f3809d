"""Build an import-boundary artifact for the SM-parity reproduction repo."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"
SM_REPRO = ROOT.parent / "mtt-sm-parity-repro"

INPUTS = {
    "sm_repro_candidate": SM_REPRO / "outputs" / "selected_qasu3sourcepacket_or_finalsmparityclosure.candidate.json",
    "sm_repro_replacement": SM_REPRO / "outputs" / "qasu3_parity_interface_replacement.packet.json",
    "sm_repro_decision": SM_REPRO / "outputs" / "sm_parity_closure_decision.packet.json",
    "rhoe_skeleton": DATA / "selected_heterotic_projectiverhoe_goodcover_transition_skeleton_or_complement_kernel.candidate.json",
    "rhoe_equations": DATA / "selected_heterotic_projectiverhoe_goodcover_transition_skeleton_or_complement_kernel.equations.json",
}

OUTPUT_DATA = DATA / "smparity_repro_import_boundary_for_rhoe_frontier.candidate.json"
OUTPUT_CERT = CERTS / "smparity_repro_import_boundary_for_rhoe_frontier_certificate.json"
OUTPUT_NOTE = PROOF / "SMParity_Repro_ImportBoundary_for_RhoE_Frontier_v1.md"

STATUS = "SMPARITY_REPRO_IMPORT_BOUNDARY_BUILT_RHOE_NOKNOB_FRONTIER_PRESERVED"
NEXT = "Selected_Heterotic_ProjectiveRhoE_SourceTableSolve_or_ComplementKernelProof_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> dict[str, Any]:
    sm_candidate = load(INPUTS["sm_repro_candidate"])
    replacement = load(INPUTS["sm_repro_replacement"])
    decision = load(INPUTS["sm_repro_decision"])
    rhoe_skeleton = load(INPUTS["rhoe_skeleton"])
    rhoe_equations = load(INPUTS["rhoe_equations"])

    imported_closures = {
        "SM_parity_closed_under_declared_interface_standard": decision["SM_parity_closed"],
        "qasu3_parity_interface_replacement_accepted": replacement["accepted_for_SM_parity_interface"],
        "selected_SM_packet_certificate_integration_closed_for_SM_parity": sm_candidate["what_closes_now"]["selected_SM_packet_certificate_integration_closed_for_SM_parity"],
        "source_boundary_preserved": sm_candidate["source_boundary_preserved"],
        "observed_data_not_selector": decision["observed_data_used_as_selector"] is False,
        "target_fitting_not_used": decision["target_fitting_used"] is False,
    }

    imported_nonclosures = {
        "actual_selected_QaSU3_operator_packet": sm_candidate["actual_selected_operator_packet_claimed"] is False,
        "actual_selected_D_E_or_rho_E_operator_data": "actual selected Qa/SU3 D_E/rho_E operator packet" in decision["no_knob_still_open"],
        "no_knob_closure": decision["no_knob_closed"] is False,
        "true_precision_SM_equivalence": decision["true_SM_equivalence_closed"] is False,
        "accepted_as_actual_selected_no_knob_packet": replacement["accepted_as_actual_selected_no_knob_packet"] is False,
    }

    rhoe_frontier_alignment = {
        "sm_parity_repro_can_support_interface_language": True,
        "sm_parity_repro_can_close_smooth_rhoE_transition_values": False,
        "sm_parity_repro_can_close_complement_kernel": False,
        "sm_parity_repro_can_close_same_branch_smooth_source_certificate": False,
        "reason": (
            "The repro proves a parity-interface replacement at the tier where SM "
            "gauge/representation/operator interface data are admitted. It explicitly "
            "does not claim actual selected Qa/SU3 D_E/rho_E operator data, so it "
            "cannot instantiate the smooth rho_E transition skeleton or complement kernel."
        ),
    }

    allowed_imports = [
        "parity-interface closure status",
        "typed source-interface replacement rule as guardrail context",
        "unsafe-shortcut rejection list",
        "source-boundary and no-target-fitting certificate",
    ]
    forbidden_imports = [
        "smooth heterotic rho_E transition matrices",
        "selected D_E/rho_E operator data",
        "typed monad maps as actual selected operator maps",
        "Freed-Witten/Bianchi/anomaly certificate for the actual packet",
        "no-knob constants or physical threshold normalization",
    ]

    candidate = {
        "candidate": "SMParityReproImportBoundaryForRhoEFrontier",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_hashes": {key: sha256(path) for key, path in INPUTS.items()},
        "imported_closures": imported_closures,
        "imported_nonclosures": imported_nonclosures,
        "allowed_imports": allowed_imports,
        "forbidden_imports": forbidden_imports,
        "rhoe_frontier_alignment": rhoe_frontier_alignment,
        "current_rhoe_next": rhoe_skeleton["decision"]["next_required_artifact"],
        "rhoe_equation_system_status": rhoe_equations["status"],
        "decision": {
            "sm_parity_repro_verified_as_external_readonly_input": True,
            "SM_parity_can_be_marked_closed_for_context": all(imported_closures.values()),
            "rhoe_no_knob_frontier_preserved": all(imported_nonclosures.values()),
            "source_table_solve_still_required": True,
            "complement_kernel_proof_still_required": True,
            "next_required_artifact": NEXT,
            "target_fitting_used": False,
            "closure_claimed": False,
        },
        "guardrails": {
            "does_not_import_parity_replacement_as_actual_operator_packet": True,
            "does_not_import_sm_repro_as_smooth_rhoE_values": True,
            "does_not_import_observed_data": True,
            "does_not_claim_true_precision_equivalence": True,
            "does_not_claim_no_knob_closure": True,
            "target_fitting_used": False,
        },
        "theorem": {
            "name": "SMParityReproImportBoundaryForRhoEFrontier",
            "proved": True,
            "statement": (
                "The read-only mtt-sm-parity-repro result may be imported as a verified "
                "SM-parity interface closure and source-boundary guardrail. Because that "
                "result explicitly leaves actual selected Qa/SU3 D_E/rho_E operator data, "
                "true precision equivalence, and no-knob closure open, it cannot fill the "
                "smooth heterotic rho_E transition-table lane or complement-kernel lane. "
                "The current rho_E frontier is therefore preserved, not bypassed."
            ),
        },
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "SM_parity_closed_for_context": candidate["decision"]["SM_parity_can_be_marked_closed_for_context"],
        "rhoe_no_knob_frontier_preserved": candidate["decision"]["rhoe_no_knob_frontier_preserved"],
        "source_table_solve_still_required": True,
        "complement_kernel_proof_still_required": True,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# SMParity Repro ImportBoundary for RhoE Frontier v1

## Result

```text
status = {STATUS}
SM_parity_closed_for_context = true
rhoe_no_knob_frontier_preserved = true
source_table_solve_still_required = true
complement_kernel_proof_still_required = true
next_required_artifact = {NEXT}
```

## Boundary

The read-only `mtt-sm-parity-repro` result is verified as a parity-interface
closure. It may be imported as context and as a guardrail source-boundary
certificate.

It may not be imported as smooth heterotic `rho_E` transition matrices, selected
`D_E/rho_E` operator data, typed monad maps as actual selected operator maps, an
actual Freed-Witten/Bianchi/anomaly certificate, no-knob constants, or physical
threshold normalization.

The next rhoE proof step is unchanged and sharper:

```text
{NEXT}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
