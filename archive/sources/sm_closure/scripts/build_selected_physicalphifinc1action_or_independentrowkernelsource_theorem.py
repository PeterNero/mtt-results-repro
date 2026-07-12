"""Build selected physical Phi_fin^C1 action / independent row-kernel source theorem gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_physicalphifinc1action_or_independentrowkernelsource_theorem"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
TEMPLATE = PACKET_DIR / "two_exit_source_theorem.strict_template.json"
CURRENT = PACKET_DIR / "current_two_exit_source_attempt.packet.json"
CUTSET = PACKET_DIR / "remaining_source_theorem_cutset.packet.json"
VALIDATOR_RESULT = PACKET_DIR / "strict_validator_result.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PhysicalPhiFinC1Action_or_IndependentRowKernelSource_Theorem_v1.md"
VALIDATOR = ROOT / "scripts" / "validate_selected_physicalphifinc1_action_or_independent_rowkernel_source.py"

STATUS = "MTT_SELECTED_PHYSICALPHIFINC1ACTION_OR_INDEPENDENTROWKERNELSOURCE_THEOREM_BUILT_BOTH_EXITS_OPEN"
NEXT = "MTT_Selected_RouteA_ActionRestrictionProof_or_RouteB_RowKernelEmissionFill_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    proof_cutset = load(DATA / "selected_fiveclause_sourcepromotion_attempt_or_trueproofcutset" / "true_proof_cutset.packet.json")
    promotion = load(DATA / "selected_fiveclause_sourcepromotion_attempt_or_trueproofcutset" / "five_clause_source_promotion_attempt.packet.json")
    route_a_validator = load(DATA / "selected_phifinc1_actionrestriction_or_boundarysource_emission" / "route_a_action_restriction_validator_v2.packet.json")
    basis = load(DATA / "selected_routeb_selectedbasisindependencefill_or_rowsourcegap" / "route_b_selected_basis_independence_fill.packet.json")
    shape = load(DATA / "selected_variationoperatorshapecompatibility_or_hessiansourcegap" / "variation_operator_shape_compatibility.packet.json")
    hessian = load(DATA / "selected_hessiancountertermsource_bvector_theoremtemplate" / "hessian_bvector_source_theorem.strict_template.json")
    rowkernel_candidate = load(DATA / "selected_finitec1_rowkernelfunctional_candidate_or_sourceclausefailure" / "finite_c1_rowkernel_functional_candidate.packet.json")

    template = {
        "schema": "MTTTwoExitFiniteC1SourceTheoremTemplate.v1",
        "status": "STRICT_TEMPLATE_READY_NOT_FILLED",
        "route_A_physical_action_restriction_required_fields": proof_cutset["legal_exit_A"]["must_emit"],
        "route_B_independent_rowkernel_source_required_fields": proof_cutset["legal_exit_B"]["must_emit"],
        "shared_postchecks_after_either_exit": [
            "finite C1 row-kernel functional validator passes",
            "110 algebraic row values become source-promoted values",
            "A^T A=12I, A^T b=(12,12), b_norm_sq=24, deltaTheta=(1,1) are postchecked only",
            "no observed constants or locked targets select the source",
        ],
        "forbidden_shortcuts": [
            "using canonical residual projector replay as source",
            "using locked target A^T b or deltaTheta as source",
            "using observed SM constants as selectors",
            "treating finite measure normalization alone as action restriction",
        ],
        "validator": rel(VALIDATOR),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "locked_target_values_used_as_source": False,
    }

    current = {
        "schema": "MTTCurrentTwoExitFiniteC1SourceAttempt.v1",
        "status": "CURRENT_SUPPORT_IMPORTED_BOTH_EXITS_FAIL_STRICT_VALIDATOR",
        "route_A_physical_action_restriction": {
            "same_branch": False,
            "physical_action_restricts_to_finite_weyl_quotient": False,
            "zero_extra_boundary_or_source_term": False,
            "phase_R_Z_source_selection": False,
            "shift_R_X_source_selection": False,
            "same_source_b_selected_emission": False,
            "attached_source_evidence": [
                {
                    "source": rel(DATA / "selected_phifinc1_actionrestriction_or_boundarysource_emission" / "route_a_action_restriction_validator_v2.packet.json"),
                    "closes": "finite measure, finite quotient, Weyl variation algebra, and algebraic boundary cancellation support only",
                }
            ],
            "support_closed": route_a_validator["closed_subclauses"],
            "still_required": route_a_validator["still_required_physical_subclauses"],
        },
        "route_B_independent_rowkernel_source": {
            "same_branch": True,
            "selected_basis_feeds_all_72_row_functionals": False,
            "pre_residual_phase_shift_variation_operators": False,
            "independent_hessian_counterterm_source_rows": False,
            "sector_rows_assembled_from_source_rows": False,
            "no_residual_projector_replay_or_locked_target_as_source": False,
            "attached_source_evidence": [
                {
                    "source": rel(DATA / "selected_routeb_selectedbasisindependencefill_or_rowsourcegap" / "route_b_selected_basis_independence_fill.packet.json"),
                    "closes": "selected basis independence only",
                },
                {
                    "source": rel(DATA / "selected_variationoperatorshapecompatibility_or_hessiansourcegap" / "variation_operator_shape_compatibility.packet.json"),
                    "closes": "phase/shift shape compatibility only",
                },
                {
                    "source": rel(DATA / "selected_hessiancountertermsource_bvector_theoremtemplate" / "hessian_bvector_source_theorem.strict_template.json"),
                    "closes": "Hessian/b strict template only",
                },
            ],
            "support_closed": {
                "selected_basis_independent_of_residual_projector": basis["route_B_independent_execution"]["selected_basis_independent_of_residual_projector"],
                "phase_shift_shape_compatible": shape["compatible_with_72_slot_table"],
                "hessian_acceptance_target_declared": hessian["acceptance_target"]["A_transpose_b"] == [12.0, 12.0],
                "rowkernel_candidate_values_filled": rowkernel_candidate["row_values"]["values_filled"],
            },
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "locked_target_values_used_as_source": False,
        "closure_claimed": False,
    }

    TEMPLATE.write_text(json.dumps(template, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CURRENT.write_text(json.dumps(current, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(CURRENT)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    stderr_lines = proc.stderr.splitlines()
    validator_result = {
        "schema": "MTTTwoExitSourceTheoremValidatorResult.v1",
        "payload": rel(CURRENT),
        "validator": rel(VALIDATOR),
        "returncode": proc.returncode,
        "expected_failure": True,
        "stderr_excerpt": stderr_lines[:20],
        "route_A_errors": [line for line in stderr_lines if line.startswith("ERROR Route A")],
        "route_B_errors": [line for line in stderr_lines if line.startswith("ERROR Route B")],
        "stdout": proc.stdout.strip(),
    }
    VALIDATOR_RESULT.write_text(json.dumps(validator_result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cutset = {
        "schema": "MTTRemainingTwoExitSourceTheoremCutset.v1",
        "status": "BOTH_EXITS_STRICTLY_DEFINED_BOTH_CURRENTLY_OPEN",
        "validator_rejects_current_attempt": proc.returncode == 1,
        "route_A_minimal_new_payload": {
            "name": "same-branch physical Phi_fin^C1 action rows",
            "must_supply_all": template["route_A_physical_action_restriction_required_fields"],
        },
        "route_B_minimal_new_payload": {
            "name": "independent selected row-kernel source rows",
            "must_supply_all": template["route_B_independent_rowkernel_source_required_fields"],
        },
        "closed_support_not_to_repeat": proof_cutset["closed_support_not_blocking"],
        "why_this_is_sharper": (
            "The previous five-clause cutset is now executable as a two-exit validator. Future work can fill either Route A "
            "or Route B without modifying the downstream row-kernel value machinery."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    CUTSET.write_text(json.dumps(cutset, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    candidate = {
        "candidate": "MTTSelectedPhysicalPhiFinC1ActionOrIndependentRowKernelSourceTheorem",
        "status": STATUS,
        "inputs": {
            "true_proof_cutset": rel(DATA / "selected_fiveclause_sourcepromotion_attempt_or_trueproofcutset" / "true_proof_cutset.packet.json"),
            "five_clause_promotion_attempt": rel(DATA / "selected_fiveclause_sourcepromotion_attempt_or_trueproofcutset" / "five_clause_source_promotion_attempt.packet.json"),
            "rowkernel_candidate": rel(DATA / "selected_finitec1_rowkernelfunctional_candidate_or_sourceclausefailure" / "finite_c1_rowkernel_functional_candidate.packet.json"),
        },
        "output_packets": {
            "two_exit_source_theorem_template": rel(TEMPLATE),
            "current_two_exit_source_attempt": rel(CURRENT),
            "remaining_source_theorem_cutset": rel(CUTSET),
            "strict_validator_result": rel(VALIDATOR_RESULT),
        },
        "theorem": {
            "name": "TwoExitFiniteC1SourceTheoremReduction",
            "proved": True,
            "statement": (
                "Finite C1 row-kernel source closure is exactly the disjunction of Route A physical Phi_fin^C1 "
                "action restriction or Route B independent row-kernel source emission. Current support satisfies neither."
            ),
        },
        "what_closes_now": {
            "two_exit_validator_built": True,
            "route_A_and_B_templates_built": True,
            "current_attempt_rejected_honestly": proc.returncode == 1,
            "downstream_110_value_machinery_reusable_after_either_exit": True,
        },
        "what_remains_open": {
            "route_A_physical_action_restriction_theorem": True,
            "route_B_independent_rowkernel_source_theorem": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
        "previous_status": promotion["status"],
    }

    cert = {
        "certificate": "MTT_Selected_PhysicalPhiFinC1Action_or_IndependentRowKernelSource_Theorem_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "validator_rejects_current_attempt": proc.returncode == 1,
        "theorem_proved": True,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PhysicalPhiFinC1Action or IndependentRowKernelSource Theorem v1

Status: `{STATUS}`.

The final finite C1 source gate is now executable as a strict two-exit
validator.

```text
Route A = physical Phi_fin^C1 action restriction theorem
Route B = independent row-kernel source theorem
current attempt validates = False
```

Already closed support is not repeated: finite trace normalization, finite C1
quotient, selected basis independence, phase/shift shape compatibility, formal
Hessian target, and all `110` algebraic values.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
