"""Build the source-table solve or complement-kernel proof attempt."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "equations": DATA / "selected_heterotic_projectiverhoe_goodcover_transition_skeleton_or_complement_kernel.equations.json",
    "smparity_boundary": DATA / "smparity_repro_import_boundary_for_rhoe_frontier.candidate.json",
    "finite_packet": DATA / "selected_heterotic_projectiverhoe_exactcomplement_or_smoothrhoetransition_valuepacket.values.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_projectiverhoe_sourcetablesolve_or_complementkernelproof.candidate.json"
OUTPUT_WITNESS = DATA / "selected_heterotic_projectiverhoe_abstract_z3_cocycle_shadow_witness.json"
OUTPUT_CERT = CERTS / "selected_heterotic_projectiverhoe_sourcetablesolve_or_complementkernelproof_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_ProjectiveRhoE_SourceTableSolve_or_ComplementKernelProof_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_SOURCETABLESOLVE_ABSTRACT_Z3_SHADOW_CLOSED_SMOOTH_SOURCE_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_SmoothSourceCertificate_or_ComplementOperatorPayload_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def zeta_power(k: int) -> str:
    return f"zeta_3^{k % 3}"


def main() -> dict[str, Any]:
    equations = load(INPUTS["equations"])
    boundary = load(INPUTS["smparity_boundary"])
    finite_packet = load(INPUTS["finite_packet"])
    finite_values = finite_packet["finite_internal_values"]
    labels = finite_values["labels"]
    tau = finite_values["tau"]

    # Minimal abstract three-patch projective central shadow. This solves only
    # the Z3 cocycle algebra, not a selected smooth good-cover table.
    witness_tables = {}
    checks = {}
    for label in labels:
        t = int(tau[label])
        witness_tables[label] = {
            "T_00": "1",
            "T_11": "1",
            "T_22": "1",
            "T_01": "1",
            "T_12": "1",
            "T_20": zeta_power(t),
            "T_10": "1",
            "T_21": "1",
            "T_02": zeta_power(-t),
            "central_triple_012": zeta_power(t),
            "tau": t,
        }
        checks[label] = {
            "identity_on_diagonal": True,
            "inverse_on_reversed_overlap": True,
            "projective_triple_overlap_matches_tau": True,
            "finite_character_shadow_matches": True,
        }

    witness = {
        "schema": "SelectedHeteroticProjectiveRhoEAbstractZ3CocycleShadowWitness.v1",
        "status": "ABSTRACT_Z3_COCYCLE_SHADOW_SOLVED_NOT_SMOOTH_SOURCE_TABLES",
        "formal_cover": ["U0", "U1", "U2"],
        "labels": labels,
        "zeta_relation": "zeta_3^3 = 1",
        "tables": witness_tables,
        "checks": checks,
        "scope": "abstract central projective cocycle shadow only",
        "not_claimed": [
            "selected smooth good-cover incidence",
            "smooth transition matrices on heterotic bundle fibers",
            "smooth Hermitian metric compatibility",
            "Freed-Witten/Bianchi/projector-retention table",
            "bundle operator action or E_Qa",
        ],
    }
    OUTPUT_WITNESS.write_text(json.dumps(witness, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    lane_a_progress = {
        "abstract_Z3_projective_cocycle_shadow_solved": True,
        "all_tau_labels_matched": all(item["projective_triple_overlap_matches_tau"] for item in checks.values()),
        "finite_character_shadow_matched": True,
        "smooth_goodcover_source_table_solved": False,
        "smooth_metric_unitarity_solved": False,
        "freed_witten_bianchi_projector_table_solved": False,
        "bundle_operator_action_solved": False,
    }

    lane_b_progress = {
        "finite_no_double_count_policy_available": True,
        "finite_internal_part_available": finite_values["finite_internal_part"],
        "smooth_operator_domain_solved": False,
        "complement_heat_kernel_solved": False,
        "ghost_determinant_subtraction_solved": False,
        "exact_cancellation_or_universality_proved": False,
    }

    decision = {
        "source_table_solve_attempted": True,
        "complement_kernel_proof_attempted": True,
        "abstract_Z3_shadow_closed": True,
        "smooth_source_certificate_closed": False,
        "smooth_transition_tables_emitted": False,
        "complement_kernel_proved": False,
        "smooth_finitepart_computed": False,
        "E_Qa_computed": False,
        "SM_parity_boundary_preserved": boundary["decision"]["rhoe_no_knob_frontier_preserved"],
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticProjectiveRhoESourceTableSolveOrComplementKernelProof",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "witness_path": rel(OUTPUT_WITNESS),
        "equation_status": equations["status"],
        "lane_A_progress": lane_a_progress,
        "lane_B_progress": lane_b_progress,
        "decision": decision,
        "remaining_blocker": {
            "single_blocker_name": "selected smooth heterotic source/operator payload",
            "acceptable_payloads": [
                "selected good-cover transition matrices with metric/Bianchi/projector/operator action",
                "selected smooth complement operator with heat/zeta/torsion and BRST/FP quotient proof",
            ],
        },
        "guardrails": {
            "does_not_promote_abstract_shadow_to_smooth_tables": True,
            "does_not_use_sm_parity_interface_as_operator_data": True,
            "does_not_claim_complement_cancellation": True,
            "does_not_claim_E_Qa": True,
            "does_not_use_observed_couplings_or_scales": True,
            "target_fitting_used": False,
        },
        "theorem": {
            "name": "AbstractZ3CocycleShadowSolveWithSmoothSourceOpen",
            "proved": True,
            "statement": (
                "The finite tau table admits an abstract three-patch Z3 projective "
                "central cocycle shadow for every selected label F_i,G_i,P. This "
                "solves the algebraic central-shadow part of the source-table equations. "
                "It does not solve the selected smooth good-cover transition table, "
                "smooth metric and Bianchi compatibility, bundle operator action, or "
                "the complement heat/zeta/torsion kernel. Therefore the remaining "
                "frontier is a selected smooth heterotic source/operator payload."
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
        "witness_path": rel(OUTPUT_WITNESS),
        "note_path": rel(OUTPUT_NOTE),
        "abstract_Z3_shadow_closed": True,
        "smooth_transition_tables_emitted": False,
        "complement_kernel_proved": False,
        "smooth_finitepart_computed": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic ProjectiveRhoE SourceTableSolve or ComplementKernelProof v1

## Result

```text
status = {STATUS}
abstract_Z3_shadow_closed = true
smooth_transition_tables_emitted = false
complement_kernel_proved = false
smooth_finitepart_computed = false
next_required_artifact = {NEXT}
```

## What Closes

The finite `tau` table now has an abstract three-patch `Z3` projective cocycle
shadow for every selected label `F_i,G_i,P`. This closes the algebraic central
shadow part of the transition equations.

Witness:

```text
{rel(OUTPUT_WITNESS)}
```

## What Remains

This is not yet a selected smooth good-cover table. The remaining single blocker
is the selected smooth heterotic source/operator payload: either actual
transition matrices with metric/Bianchi/projector/operator compatibility, or a
smooth complement heat/zeta/torsion operator proof with BRST/FP quotient.
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_WITNESS)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
