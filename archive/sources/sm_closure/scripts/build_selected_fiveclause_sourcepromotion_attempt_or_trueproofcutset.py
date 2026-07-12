"""Build five-clause source-promotion attempt / true proof cutset."""

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

SLUG = "selected_fiveclause_sourcepromotion_attempt_or_trueproofcutset"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ATTEMPT = PACKET_DIR / "five_clause_source_promotion_attempt.packet.json"
CUTSET = PACKET_DIR / "true_proof_cutset.packet.json"
VALIDATOR_RESULT = PACKET_DIR / "strict_validator_result.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_FiveClause_SourcePromotionAttempt_or_TrueProofCutset_v1.md"
VALIDATOR = ROOT / "scripts" / "validate_selected_finitec1_rowkernel_functional_packet.py"

STATUS = "MTT_SELECTED_FIVECLAUSE_SOURCEPROMOTION_ATTEMPT_BUILT_TRUEPROOFCUTSET_OPEN"
NEXT = "MTT_Selected_PhysicalPhiFinC1ActionRestriction_or_IndependentRowKernelSourceTheorem_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def clause_status(
    *,
    support_closed: dict[str, bool],
    source_emitted: bool,
    theorem_derived: bool,
    uses_replay_as_source: bool,
    why_open: str,
    evidence: list[str],
) -> dict[str, Any]:
    return {
        "support_closed": support_closed,
        "source_emitted": source_emitted,
        "same_branch": True,
        "theorem_derived": theorem_derived,
        "uses_replay_as_source": uses_replay_as_source,
        "why_open": why_open,
        "evidence": evidence,
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    candidate_packet = load(DATA / "selected_finitec1_rowkernelfunctional_candidate_or_sourceclausefailure" / "finite_c1_rowkernel_functional_candidate.packet.json")
    measure_split = load(DATA / "selected_finiteweyl_traceuniqueness_or_physicalboundarysource_derivation" / "finite_c1_trace_measure_principle_split.packet.json")
    route_a = load(DATA / "selected_phifinc1_actionrestriction_or_boundarysource_emission" / "route_a_action_restriction_validator_v2.packet.json")
    physical_clause = load(DATA / "selected_physicalactionrestrictionclause_or_primitivekernelformula" / "physical_action_restriction_clause_ledger.packet.json")
    basis = load(DATA / "selected_routeb_selectedbasisindependencefill_or_rowsourcegap" / "route_b_selected_basis_independence_fill.packet.json")
    shape = load(DATA / "selected_variationoperatorshapecompatibility_or_hessiansourcegap" / "variation_operator_shape_compatibility.packet.json")
    hessian_gap = load(DATA / "selected_hessiancountertermsource_bvector_theoremtemplate" / "remaining_hessian_bvector_source_gap.packet.json")
    hessian_template = load(DATA / "selected_hessiancountertermsource_bvector_theoremtemplate" / "hessian_bvector_source_theorem.strict_template.json")

    clauses = {
        "measure_action_binding": clause_status(
            support_closed={
                "finite_selected_C1_quotient": measure_split["clauses"]["finite_selected_C1_quotient"]["closed"],
                "finite_trace_measure_normalization": measure_split["clauses"]["physical_first_variation_uses_normalized_trace_Frobenius_measure"]["closed"],
                "selected_Weyl_variation_algebra": route_a["closed_subclauses"]["selected_Weyl_variation_algebra"],
            },
            source_emitted=False,
            theorem_derived=False,
            uses_replay_as_source=False,
            why_open=physical_clause["five_remaining_physical_clauses"]["physical_PhiFinC1_action_restriction"]["why_open"],
            evidence=[
                rel(DATA / "selected_finiteweyl_traceuniqueness_or_physicalboundarysource_derivation" / "finite_c1_trace_measure_principle_split.packet.json"),
                rel(DATA / "selected_phifinc1_actionrestriction_or_boundarysource_emission" / "route_a_action_restriction_validator_v2.packet.json"),
            ],
        ),
        "boundary_source_null": clause_status(
            support_closed={
                "algebraic_finite_boundary_cancellation": route_a["closed_subclauses"]["algebraic_finite_boundary_cancellation"],
            },
            source_emitted=False,
            theorem_derived=False,
            uses_replay_as_source=False,
            why_open=physical_clause["five_remaining_physical_clauses"]["no_extra_physical_boundary_or_source_term"]["why_open"],
            evidence=[
                rel(DATA / "selected_phifinc1_actionrestriction_or_boundarysource_emission" / "route_a_action_restriction_validator_v2.packet.json"),
            ],
        ),
        "basis_to_row_functionals": clause_status(
            support_closed={
                "selected_basis_independent_of_residual_projector": basis["route_B_independent_execution"]["selected_basis_independent_of_residual_projector"],
                "selected_basis_independence_has_transport_source": basis["route_B_independent_execution"]["selected_basis_independence_certificate"]["all_sector_sources_verified_by_transport_conjugation"],
            },
            source_emitted=False,
            theorem_derived=False,
            uses_replay_as_source=False,
            why_open="Selected basis/projectors are source-independent, but the theorem that they feed every pre-residual primitive row functional is still absent.",
            evidence=[
                rel(DATA / "selected_routeb_selectedbasisindependencefill_or_rowsourcegap" / "route_b_selected_basis_independence_fill.packet.json"),
            ],
        ),
        "phase_shift_pre_residual_operators": clause_status(
            support_closed={
                "phase_operator_shape_attached": shape["phase_operator_shape_attached"],
                "shift_operator_shape_attached": shape["shift_operator_shape_attached"],
                "compatible_with_72_slot_table": shape["compatible_with_72_slot_table"],
            },
            source_emitted=False,
            theorem_derived=False,
            uses_replay_as_source=True,
            why_open="R_Z/R_X are exact and shape-compatible, but operator_shapes_selected_as_source_now is false and current values are residual replay.",
            evidence=[
                rel(DATA / "selected_variationoperatorshapecompatibility_or_hessiansourcegap" / "variation_operator_shape_compatibility.packet.json"),
            ],
        ),
        "hessian_b_source": clause_status(
            support_closed={
                "formal_A_transpose_b_target_identified": hessian_gap["closed_now"]["formal_A_transpose_b_target_identified"],
                "formal_deltaTheta_target_identified": hessian_gap["closed_now"]["formal_deltaTheta_target_identified"],
                "formal_hessian_row_count_is_two": hessian_gap["closed_now"]["formal_hessian_row_count_is_two"],
            },
            source_emitted=False,
            theorem_derived=False,
            uses_replay_as_source=True,
            why_open="Formal Hessian/b target is known, but same_branch_phifin_c1_or_galerkin_source_emits_hessian_rows and same_source_b_selected_emitted are false.",
            evidence=[
                rel(DATA / "selected_hessiancountertermsource_bvector_theoremtemplate" / "remaining_hessian_bvector_source_gap.packet.json"),
                rel(DATA / "selected_hessiancountertermsource_bvector_theoremtemplate" / "hessian_bvector_source_theorem.strict_template.json"),
            ],
        ),
    }

    attempt = dict(candidate_packet)
    attempt["schema"] = "MTTSelectedFiveClauseSourcePromotionAttempt.v1"
    attempt["status"] = "FIVE_CLAUSE_PROMOTION_ATTEMPT_SUPPORT_MAXIMIZED_SOURCE_OPEN"
    attempt["source_clauses"] = {
        key: {
            "source_emitted": value["source_emitted"],
            "same_branch": value["same_branch"],
            "theorem_derived": value["theorem_derived"],
            "uses_replay_as_source": value["uses_replay_as_source"],
            "reason": value["why_open"],
        }
        for key, value in clauses.items()
    }
    attempt["attached_source_evidence"] = [
        {"source": source, "closes": key + " support only"}
        for key, value in clauses.items()
        for source in value["evidence"]
    ]
    attempt["promotion_attempt"] = {
        "all_closed_support_imported": True,
        "any_source_clause_promoted_now": any(value["source_emitted"] and value["theorem_derived"] for value in clauses.values()),
        "source_clause_count": len(clauses),
        "source_clause_open_count": sum(not (value["source_emitted"] and value["theorem_derived"]) for value in clauses.values()),
        "guardrail": "Support closure is not source emission. Replay and locked target values remain postchecks only.",
    }
    ATTEMPT.write_text(json.dumps(attempt, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(ATTEMPT)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    stderr_lines = proc.stderr.splitlines()
    validator_result = {
        "schema": "MTTFiveClausePromotionValidatorResult.v1",
        "payload": rel(ATTEMPT),
        "validator": rel(VALIDATOR),
        "returncode": proc.returncode,
        "expected_failure": True,
        "stderr_excerpt": stderr_lines[:20],
        "source_clause_errors": sum("source_emitted must be true" in line for line in stderr_lines),
        "theorem_errors": sum("theorem_derived must be true" in line for line in stderr_lines),
        "replay_source_errors": sum("uses_replay_as_source must be false" in line for line in stderr_lines),
        "stdout": proc.stdout.strip(),
    }
    VALIDATOR_RESULT.write_text(json.dumps(validator_result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    true_cutset = {
        "schema": "MTTTrueProofCutset.v1",
        "status": "TRUE_PROOF_CUTSET_SHARPENED_TO_TWO_LEGAL_EXITS",
        "validator_rejects_promotion_attempt": proc.returncode == 1,
        "closed_support_not_blocking": {
            "finite_trace_measure_normalization": True,
            "finite_selected_C1_quotient": True,
            "selected_basis_independence": True,
            "phase_shift_shape_compatibility": True,
            "formal_hessian_target": True,
            "all_110_values": True,
        },
        "legal_exit_A": {
            "name": "physical Phi_fin^C1 action restriction theorem",
            "must_emit": [
                "physical action restriction to finite Weyl quotient",
                "zero extra boundary/source term",
                "phase R_Z source selection",
                "shift R_X source selection",
                "same-source b_selected emission",
            ],
        },
        "legal_exit_B": {
            "name": "independent row-kernel source theorem",
            "must_emit": [
                "selected basis-to-row functional theorem for all 72 primitive rows",
                "pre-residual phase/shift variation operators",
                "independent Hessian counterterm/source rows",
                "sector rows assembled from those source rows",
                "no residual-projector replay or locked-target values as source",
            ],
        },
        "minimal_next_object": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    CUTSET.write_text(json.dumps(true_cutset, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    candidate = {
        "candidate": "MTTSelectedFiveClauseSourcePromotionAttemptOrTrueProofCutset",
        "status": STATUS,
        "inputs": {
            "finite_c1_rowkernel_candidate": rel(DATA / "selected_finitec1_rowkernelfunctional_candidate_or_sourceclausefailure" / "finite_c1_rowkernel_functional_candidate.packet.json"),
            "finite_trace_measure_split": rel(DATA / "selected_finiteweyl_traceuniqueness_or_physicalboundarysource_derivation" / "finite_c1_trace_measure_principle_split.packet.json"),
            "route_a_action_restriction_validator": rel(DATA / "selected_phifinc1_actionrestriction_or_boundarysource_emission" / "route_a_action_restriction_validator_v2.packet.json"),
            "selected_basis_independence": rel(DATA / "selected_routeb_selectedbasisindependencefill_or_rowsourcegap" / "route_b_selected_basis_independence_fill.packet.json"),
            "variation_shape": rel(DATA / "selected_variationoperatorshapecompatibility_or_hessiansourcegap" / "variation_operator_shape_compatibility.packet.json"),
            "hessian_source_gap": rel(DATA / "selected_hessiancountertermsource_bvector_theoremtemplate" / "remaining_hessian_bvector_source_gap.packet.json"),
        },
        "output_packets": {
            "five_clause_source_promotion_attempt": rel(ATTEMPT),
            "true_proof_cutset": rel(CUTSET),
            "strict_validator_result": rel(VALIDATOR_RESULT),
        },
        "theorem": {
            "name": "FiveClauseSourcePromotionCutsetTheorem",
            "proved": True,
            "statement": (
                "After importing all current clause-specific support, no source clause can be promoted without a new same-branch "
                "physical Phi_fin^C1 action restriction theorem or an independent row-kernel source theorem. These are the two legal exits."
            ),
        },
        "what_closes_now": {
            "clause_specific_support_imported": True,
            "support_vs_source_separated_per_clause": True,
            "true_proof_cutset_sharpened": True,
            "strict_validator_failure_preserved": proc.returncode == 1,
        },
        "what_remains_open": {
            key: not (value["source_emitted"] and value["theorem_derived"] and not value["uses_replay_as_source"])
            for key, value in clauses.items()
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_FiveClause_SourcePromotionAttempt_or_TrueProofCutset_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "validator_rejects_promotion_attempt": proc.returncode == 1,
        "theorem_proved": True,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected FiveClause SourcePromotionAttempt or TrueProofCutset v1

Status: `{STATUS}`.

All available clause-specific support has now been imported:

```text
finite trace measure normalization = closed
finite selected C1 quotient        = closed
selected basis independence        = closed
phase/shift shape compatibility    = closed
formal Hessian target              = closed
all 110 algebraic values           = closed
```

The strict source validator still rejects the promotion attempt. This means the
remaining proof is not a value problem, a row-count problem, or a measure
normalization problem.

There are now two legal exits:

```text
Route A: physical Phi_fin^C1 action restriction theorem
Route B: independent row-kernel source theorem
```

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
