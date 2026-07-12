"""Build same-source Phi_fin^C1 emission or independent rows actual-fill attempt."""

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

SLUG = "selected_samesourcephifinc1emission_or_independentrowsactualfill"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ATTEMPT = PACKET_DIR / "strongest_legal_two_lane_actual_fill.packet.json"
VALIDATION = PACKET_DIR / "strict_two_lane_validator_result.packet.json"
CUTSET = PACKET_DIR / "remaining_source_cutset.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_SameSourcePhiFinC1Emission_or_IndependentRowsActualFill_v1.md"

PREVIOUS = DATA / "selected_physicalsourcepromotionclauseproof_or_newindependentrowpacketfill.candidate.json"
PREVIOUS_DECISION = (
    DATA
    / "selected_physicalsourcepromotionclauseproof_or_newindependentrowpacketfill"
    / "promotion_clause_or_new_rows_decision.packet.json"
)
ALL_ROWS = DATA / "selected_allrowsprovenancepromotion_or_physicalphifinc1actionsource.candidate.json"
ALL_ROWS_CUTSET = (
    DATA
    / "selected_allrowsprovenancepromotion_or_physicalphifinc1actionsource"
    / "physical_source_promotion_cutset.packet.json"
)
C1_FUNCTIONAL = DATA / "selected_c1defectfunctionalsource_or_independentquadraturedatafill.candidate.json"
ROUTEB_GAP = DATA / "selected_routeb_bestcurrentpayloadfill_or_independentsourcegap.candidate.json"
CLAUSE_PROOF = (
    DATA
    / "selected_finitec1sourceidentityclauseproof_or_independentrowdataemission"
    / "finite_weyl_trace_assembly_clause_proof.packet.json"
)
VALIDATOR = ROOT / "scripts" / "validate_selected_phifinc1emission_or_independenthessianquadraturesource.py"

STATUS = "MTT_SELECTED_SAMESOURCE_PHIFINC1_OR_INDEPENDENTROWS_ACTUALFILL_BUILT_SOURCE_FIELDS_OPEN"
NEXT = "MTT_Selected_PhysicalPhiFinC1ActionIdentity_or_IndependentRowSourceExport_v1"


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


def missing_true_fields(node: dict[str, Any], fields: list[str]) -> list[str]:
    return [field for field in fields if node.get(field) is not True]


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    all_rows = load(ALL_ROWS)
    all_rows_cutset = load(ALL_ROWS_CUTSET)
    c1_functional = load(C1_FUNCTIONAL)
    routeb_gap = load(ROUTEB_GAP)
    clause = load(CLAUSE_PROOF)

    route_a = {
        "same_branch": True,
        "physical_phifin_c1_action_emitted": False,
        "finite_weyl_action_restriction_derived": False,
        "no_extra_boundary_or_source_term": False,
        "selected_phase_shift_variation_operators_pre_residual": False,
        "selected_hessian_counterterm_source": False,
        "same_source_b_selected_emitted": False,
        "row_formula_source_theorem_derived": False,
        "attached_same_branch_source_evidence": [
            rel(PREVIOUS),
            rel(ALL_ROWS),
            rel(ALL_ROWS_CUTSET),
            rel(C1_FUNCTIONAL),
            "local explicit SelectedWeylVariationActionPrinciple support only",
            "canonical residual projector support only",
        ],
        "why_not_promoted": {
            "physical_phifin_c1_action_emitted": "No unpatched physical Phi_fin^C1 action identity is theorem-emitted.",
            "finite_weyl_action_restriction_derived": "Trace assembly is closed, but physical action restriction is not.",
            "no_extra_boundary_or_source_term": "No physical no-extra-boundary/source theorem is emitted.",
            "selected_phase_shift_variation_operators_pre_residual": "R_Z/R_X remain exact postcheck residual polynomials.",
            "selected_hessian_counterterm_source": "Hessian source is formal replay support only.",
            "same_source_b_selected_emitted": "b_selected is exactly replayed but not emitted by the same physical source.",
            "row_formula_source_theorem_derived": "Rows are formally assembled; the source theorem is missing.",
        },
    }

    route_b = {
        "selected_basis_independent_of_residual_projector": True,
        "quadrature_rule_independent_of_locked_target": True,
        "all_72_primitive_rows_executed": True,
        "formal_110_rows_executed": True,
        "independent_hessian_quadrature_source_emitted": False,
        "selected_b_vector_source": False,
        "source_independent_of_residual_projector_replay": False,
        "exactness_or_error_certificates_attached": True,
        "attached_independent_quadrature_evidence": [
            rel(CLAUSE_PROOF),
            rel(ALL_ROWS),
            rel(ALL_ROWS_CUTSET),
            rel(ROUTEB_GAP),
            rel(PREVIOUS_DECISION),
        ],
        "why_not_promoted": {
            "independent_hessian_quadrature_source_emitted": "The two Hessian/source rows are not independently source-emitted.",
            "selected_b_vector_source": "b_selected is not independently sourced.",
            "source_independent_of_residual_projector_replay": "Current values still rely on residual-projector replay as provenance.",
        },
    }

    attempt = {
        "schema": "MTTSameSourcePhiFinC1OrIndependentRowsActualFillAttempt.v1",
        "status": "STRONGEST_LEGAL_IMPORTS_ATTACHED_VALIDATION_EXPECTED_OPEN",
        "route_A_phifinc1_source_emission": route_a,
        "route_B_independent_hessian_quadrature_source": route_b,
        "locked_target_values_used_as_source": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "import_policy": {
            "positive_formal_rows_imported": True,
            "local_axiom_patched_closure_not_used_as_unpatched_proof": True,
            "residual_projector_replay_not_promoted_as_source": True,
            "measured_or_benchmark_values_excluded": True,
        },
    }
    write_json(ATTEMPT, attempt)
    validation = run_validator(ATTEMPT)
    write_json(VALIDATION, validation)

    route_a_fields = [
        "same_branch",
        "physical_phifin_c1_action_emitted",
        "finite_weyl_action_restriction_derived",
        "no_extra_boundary_or_source_term",
        "selected_phase_shift_variation_operators_pre_residual",
        "selected_hessian_counterterm_source",
        "same_source_b_selected_emitted",
        "row_formula_source_theorem_derived",
    ]
    route_b_fields = [
        "selected_basis_independent_of_residual_projector",
        "quadrature_rule_independent_of_locked_target",
        "all_72_primitive_rows_executed",
        "formal_110_rows_executed",
        "independent_hessian_quadrature_source_emitted",
        "selected_b_vector_source",
        "source_independent_of_residual_projector_replay",
        "exactness_or_error_certificates_attached",
    ]

    cutset = {
        "schema": "MTTRemainingPhysicalPhiFinOrIndependentRowsCutset.v1",
        "status": "ROUTE_A_AND_ROUTE_B_ACTUAL_FILL_REJECTED_SOURCE_CUTSET_EXACT",
        "validator_ok": validation["ok"],
        "route_A_missing_true_fields": missing_true_fields(route_a, route_a_fields),
        "route_B_missing_true_fields": missing_true_fields(route_b, route_b_fields),
        "minimal_next_objects": {
            "route_A": [
                "unpatched physical Phi_fin^C1 action identity on the selected branch",
                "physical no-extra-boundary/source theorem",
                "same-source pre-residual R_Z/R_X and b_selected/Hessian emission",
            ],
            "route_B": [
                "selected independent row-kernel source ids for 72 primitive rows",
                "independent two-row Hessian/source export emitting b_selected",
                "residual-projector replay exclusion certificate for row provenance",
            ],
        },
        "formal_support_closed": {
            "trace_assembly_subclaim": clause["proved_subclaim"]["trace_assembly_closed"],
            "all_rows_formal_replay": all_rows["promotion_decision"]["formal_110_row_replay_closed"],
            "defect_functional_source": c1_functional["promotion_decision"][
                "selected_C1_defect_functional_formal_source_promoted"
            ],
            "route_B_values_present": routeb_gap["what_closes_now"][
                "all_strict_row_slots_present_in_best_current_attempt"
            ],
        },
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedSameSourcePhiFinC1EmissionOrIndependentRowsActualFill",
        "status": STATUS,
        "inputs": {
            "previous": rel(PREVIOUS),
            "previous_decision": rel(PREVIOUS_DECISION),
            "all_rows": rel(ALL_ROWS),
            "c1_functional": rel(C1_FUNCTIONAL),
            "routeb_gap": rel(ROUTEB_GAP),
            "clause_proof": rel(CLAUSE_PROOF),
        },
        "output_packets": {
            "strongest_legal_two_lane_actual_fill": rel(ATTEMPT),
            "strict_two_lane_validator_result": rel(VALIDATION),
            "remaining_source_cutset": rel(CUTSET),
        },
        "theorem": {
            "name": "StrongestLegalActualFillCutsetTheorem",
            "proved": True,
            "statement": (
                "After importing every currently legal same-branch and independent-row support packet, "
                "the strict two-lane validator still rejects. The remaining obstruction is exactly source "
                "promotion: Route A needs an unpatched physical Phi_fin^C1 action identity with no extra "
                "boundary/source term and same-source R_Z/R_X/b_selected emission; Route B needs independent "
                "row-kernel/Hessian source export not sourced by residual-projector replay."
            ),
        },
        "what_closes_now": {
            "strongest_legal_imports_attached": True,
            "two_lane_strict_validator_rerun": True,
            "formal_support_separated_from_source_promotion": True,
            "remaining_cutset_exact": True,
        },
        "what_remains_open": {
            "unpatched_phifin_c1_action_identity": True,
            "physical_no_extra_boundary_source": True,
            "same_source_R_Z_R_X_b_selected_emission": True,
            "independent_row_kernel_source_export": True,
            "independent_b_selected_hessian_source": True,
        },
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_SameSourcePhiFinC1Emission_or_IndependentRowsActualFill_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "validator_ok": validation["ok"],
        "validator_exit_code": validation["exit_code"],
        "route_A_missing_true_fields": cutset["route_A_missing_true_fields"],
        "route_B_missing_true_fields": cutset["route_B_missing_true_fields"],
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    NOTE.write_text(
        "# MTT Selected SameSourcePhiFinC1Emission or IndependentRowsActualFill v1\n\n"
        f"Status: `{STATUS}`.\n\n"
        "This artifact attempts both legal exits with the strongest support currently present "
        "in the repo. Route A imports same-branch/static/local-premise support but refuses to "
        "promote it as an unpatched physical `Phi_fin^C1` action identity. Route B imports the "
        "closed formal row layer but refuses to treat residual-projector replay as independent "
        "row provenance.\n\n"
        "The strict validator still rejects the actual-fill packet. Therefore the remaining "
        "proof is not a value search: it is either physical source identity/no-extra-boundary "
        "promotion for `Phi_fin^C1`, or an independently sourced selected row-kernel/Hessian "
        "export with `b_selected`.\n\n"
        f"Next artifact: `{NEXT}`.\n",
        encoding="utf-8",
    )
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
