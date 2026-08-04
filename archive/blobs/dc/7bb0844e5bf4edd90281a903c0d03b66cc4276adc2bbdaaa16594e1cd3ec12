"""Build best-current final source-emission fill attempt and no-go witness."""

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

SLUG = "selected_finalsourceemission_bestcurrentfill_or_nogowitness"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ATTEMPT = PACKET_DIR / "best_current_source_emission_fill_attempt.packet.json"
WITNESS = PACKET_DIR / "final_source_emission_nogo_witness.packet.json"
VALIDATION = PACKET_DIR / "strict_validator_result.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
AUDIT = CORPUS / f"{SLUG}_audit.py"
NOTE = CORPUS / "MTT_Selected_FinalSourceEmission_BestCurrentFill_or_NoGoWitness_v1.md"

VALIDATOR = ROOT / "scripts" / "validate_selected_phifinc1emission_or_independenthessianquadraturesource.py"
PREVIOUS = DATA / "selected_phifinc1emission_or_independenthessianquadraturesource.candidate.json"
BASE_ATTEMPT = (
    DATA
    / "selected_phifinc1emission_or_independenthessianquadraturesource"
    / "current_source_emission_attempt.packet.json"
)
ACTION_IDENTITY = (
    DATA
    / "selected_physicalc1actionidentity_or_samesourcebselectedemission"
    / "physical_action_identity_to_source_emission.packet.json"
)
B_SELECTED = (
    DATA
    / "selected_physicalc1actionidentity_or_samesourcebselectedemission"
    / "same_source_bselected_emission_attempt.packet.json"
)
QUAD_ATTEMPT = (
    DATA
    / "selected_physicalc1variation_sourcepromotion_or_independentquadratureexecution"
    / "independent_quadrature_execution_attempt.packet.json"
)
QUAD_ENGINE = (
    DATA
    / "selected_c1variationprinciplederivation_or_quadratureenginerun"
    / "route_b_quadrature_engine_run_attempt.packet.json"
)

STATUS = "MTT_SELECTED_FINALSOURCEEMISSION_BESTCURRENTFILL_BUILT_NOGO_WITNESS_OPEN"
NEXT = "MTT_Selected_FinalSourceEmissionActualFill_or_NoGoWitness_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def run_validator(path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(path)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return {
        "path": rel(path),
        "exit_code": proc.returncode,
        "ok": proc.returncode == 0,
        "stdout": proc.stdout.strip().splitlines(),
        "stderr": proc.stderr.strip().splitlines(),
    }


def main() -> int:
    previous = load(PREVIOUS)
    base = load(BASE_ATTEMPT)
    action_identity = load(ACTION_IDENTITY)
    b_selected = load(B_SELECTED)
    quad_attempt = load(QUAD_ATTEMPT)
    quad_engine = load(QUAD_ENGINE)

    route_a = dict(base["route_A_phifinc1_source_emission"])
    route_a.update(
        {
            "status": "BEST_CURRENT_ROUTE_A_FILL_ATTEMPT_REPLAY_SUPPORT_ONLY",
            "same_branch": False,
            "physical_phifin_c1_action_emitted": action_identity[
                "current_physical_antecedents"
            ]["physical_action_identity_promoted"],
            "finite_weyl_action_restriction_derived": action_identity["closed_formal_support"][
                "formal_trace_frobenius_pairing"
            ],
            "no_extra_boundary_or_source_term": action_identity["current_physical_antecedents"][
                "no_extra_physical_boundary_or_source_term"
            ],
            "selected_phase_shift_variation_operators_pre_residual": False,
            "selected_hessian_counterterm_source": False,
            "same_source_b_selected_emitted": b_selected["same_source_b_selected_emitted_now"],
            "row_formula_source_theorem_derived": False,
            "attached_same_branch_source_evidence": [
                {
                    "source": rel(ACTION_IDENTITY),
                    "support": "equivalence of physical action identity to source emission",
                    "promotes_source": False,
                },
                {
                    "source": rel(B_SELECTED),
                    "support": "b replay target and why it is not emitted",
                    "promotes_source": False,
                },
            ],
        }
    )

    route_b = dict(base["route_B_independent_hessian_quadrature_source"])
    route_b.update(
        {
            "status": "BEST_CURRENT_ROUTE_B_FILL_ATTEMPT_REPLAY_SUPPORT_ONLY",
            "independent_hessian_quadrature_source_emitted": quad_attempt[
                "independent_execution_now"
            ],
            "selected_b_vector_source": b_selected["b_selected_emitted_by_independent_hessian"],
            "source_independent_of_residual_projector_replay": False,
            "attached_independent_quadrature_evidence": list(
                route_b["attached_independent_quadrature_evidence"]
            )
            + [
                {
                    "source": rel(QUAD_ATTEMPT),
                    "support": "independent quadrature execution attempt records replay, not independent execution",
                    "promotes_source_independence": False,
                },
                {
                    "source": rel(QUAD_ENGINE),
                    "support": "quadrature engine schedule and missing independent rows",
                    "promotes_source_independence": False,
                },
                {
                    "source": rel(B_SELECTED),
                    "support": "independent Hessian b emission is false",
                    "promotes_source_independence": False,
                },
            ],
        }
    )

    attempt = {
        "schema": "MTTFinalSourceEmissionBestCurrentFillAttempt.v1",
        "status": "BEST_CURRENT_FILL_REJECTED_REPLAY_SUPPORT_ONLY",
        "route_A_phifinc1_source_emission": route_a,
        "route_B_independent_hessian_quadrature_source": route_b,
        "support_closed": base["support_closed"],
        "locked_target_values_used_as_source": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(ATTEMPT, attempt)
    validation = run_validator(ATTEMPT)

    witness = {
        "schema": "MTTFinalSourceEmissionNoGoWitness.v1",
        "status": "CURRENT_CORPUS_DOES_NOT_VALIDATE_FINAL_SOURCE_EMISSION",
        "validator_rejects_best_current_fill": validation["exit_code"] == 1,
        "route_A_best_support": {
            "equivalence_statement_available": True,
            "physical_action_identity_promoted": action_identity["current_physical_antecedents"][
                "physical_action_identity_promoted"
            ],
            "same_source_b_selected_emitted": b_selected[
                "same_source_b_selected_emitted_now"
            ],
            "why_not_enough": action_identity["proof_status"],
        },
        "route_B_best_support": {
            "engine_skeleton_ready": quad_engine["engine_spec"]["basis_stage_ready"],
            "independent_execution_now": quad_attempt["independent_execution_now"],
            "independent_hessian_source_vector_missing": quad_attempt[
                "missing_independent_execution"
            ]["independent_hessian_source_vector"],
            "selected_quadrature_engine_or_rule_missing": quad_attempt[
                "missing_independent_execution"
            ]["selected_quadrature_engine_or_rule"],
            "primitive_contraction_integrals_missing": quad_attempt[
                "missing_independent_execution"
            ]["primitive_three_by_three_contraction_integrals"],
        },
        "minimal_non_replay_payload_needed": {
            "route_A": [
                "same-branch physical Phi_fin^C1 action identity",
                "same-branch phase/shift source emission before residual replay",
                "same-source Hessian counterterm and b_selected emission",
            ],
            "route_B": [
                "selected quadrature engine/rule not copied from residual replay",
                "72 primitive contraction integrals with exactness/error certificate",
                "2 independent Hessian/source rows emitting b_selected",
                "36 sector response rows",
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedFinalSourceEmissionBestCurrentFillOrNoGoWitness",
        "status": STATUS,
        "inputs": {
            "previous_gate": rel(PREVIOUS),
            "base_attempt": rel(BASE_ATTEMPT),
            "action_identity": rel(ACTION_IDENTITY),
            "same_source_b_selected": rel(B_SELECTED),
            "independent_quadrature_attempt": rel(QUAD_ATTEMPT),
            "quadrature_engine_attempt": rel(QUAD_ENGINE),
        },
        "output_packets": {
            "best_current_source_emission_fill_attempt": rel(ATTEMPT),
            "strict_validator_result": rel(VALIDATION),
            "final_source_emission_nogo_witness": rel(WITNESS),
        },
        "what_closes_now": {
            "best_current_fill_attempt_constructed": True,
            "replay_support_classified_as_non_source": True,
            "minimal_non_replay_payload_named": True,
            "validator_rejection_preserved": validation["exit_code"] == 1,
        },
        "what_remains_open": {
            "same_branch_phifin_c1_source_emission": True,
            "independent_hessian_quadrature_source": True,
            "source_independent_of_residual_projector_replay": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "theorem": {
            "name": "BestCurrentFillNoGoWitnessTheorem",
            "proved": True,
            "statement": (
                "The strongest current Route A and Route B support packets fail the narrowed final "
                "source-emission validator because they provide equivalence/replay support rather than "
                "same-branch physical Phi_fin^C1 emission or independent Hessian/quadrature provenance."
            ),
        },
        "closure_claimed": False,
        "previous_gate_status": previous["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_FinalSourceEmission_BestCurrentFill_or_NoGoWitness_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "validator_exit_code": validation["exit_code"],
        "validator_rejects_best_current_fill": validation["exit_code"] == 1,
        "same_branch_phifin_source_closed": False,
        "independent_hessian_quadrature_source_closed": False,
        "route_B_promoted_now": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected FinalSourceEmission BestCurrentFill or NoGoWitness v1

Status: `{STATUS}`

This step tries the strongest current fill against the narrowed final validator.
It imports the physical action equivalence, `b_selected` replay packet, and
independent quadrature engine attempt.

The attempt is rejected, correctly. Current artifacts provide replay and
equivalence support, not selected source emission.

Minimal non-replay payload still needed:

1. Route A: same-branch physical `Phi_fin^C1` emission of phase/shift,
   Hessian counterterm, and `b_selected`; or
2. Route B: independent quadrature/Hessian source data for 72 primitive rows,
   2 Hessian/source rows, and 36 sector rows.

Next artifact: `{NEXT}`.
"""

    audit = f'''"""Audit {SLUG}."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "{SLUG}.candidate.json"
ATTEMPT = ROOT / "candidate_data" / "{SLUG}" / "best_current_source_emission_fill_attempt.packet.json"
WITNESS = ROOT / "candidate_data" / "{SLUG}" / "final_source_emission_nogo_witness.packet.json"
CERT = ROOT / "certificates" / "{SLUG}_certificate.json"
VALIDATOR = ROOT / "scripts" / "validate_selected_phifinc1emission_or_independenthessianquadraturesource.py"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_FinalSourceEmission_BestCurrentFill_or_NoGoWitness_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    attempt = load(ATTEMPT)
    witness = load(WITNESS)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(ATTEMPT)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    require(data["status"] == "{STATUS}", "status mismatch")
    require(data["theorem"]["proved"] is True, "no-go theorem not proved")
    require(attempt["route_A_phifinc1_source_emission"]["physical_phifin_c1_action_emitted"] is False, "Route A overclosed")
    require(attempt["route_A_phifinc1_source_emission"]["same_source_b_selected_emitted"] is False, "Route A b overclosed")
    require(attempt["route_B_independent_hessian_quadrature_source"]["independent_hessian_quadrature_source_emitted"] is False, "Route B hessian overclosed")
    require(attempt["route_B_independent_hessian_quadrature_source"]["selected_b_vector_source"] is False, "Route B b overclosed")
    require(proc.returncode == 1, "validator should reject best current fill")
    require(any("neither narrowed Route A nor narrowed Route B validates" in line for line in proc.stderr.splitlines()), "missing validator rejection")
    require(witness["validator_rejects_best_current_fill"] is True, "witness should reject")
    require(witness["route_A_best_support"]["physical_action_identity_promoted"] is False, "Route A witness overclosed")
    require(witness["route_B_best_support"]["independent_execution_now"] is False, "Route B witness overclosed")
    require(witness["route_B_best_support"]["selected_quadrature_engine_or_rule_missing"] is True, "quadrature rule gap missing")
    require(cert["validator_rejects_best_current_fill"] is True, "cert should reject")
    require(cert["same_branch_phifin_source_closed"] is False, "cert Route A overclosed")
    require(cert["independent_hessian_quadrature_source_closed"] is False, "cert Route B overclosed")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require("Current artifacts provide replay and" in note, "note missing guardrail")
    print(f"PASS {{DATA.name}}: {{data['status']}}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
'''

    write_json(VALIDATION, validation)
    write_json(WITNESS, witness)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    AUDIT.write_text(audit, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(AUDIT)}")
    print(f"Validator exit: {validation['exit_code']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
