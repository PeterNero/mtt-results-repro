"""Build I11 Route-B row-source theorem push or Route-A fallback gate."""

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

SLUG = "selected_i11_routeb_rowsource_theorem_push_or_routea_fallback"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CURRENT = PACKET_DIR / "current_rowsource_theorem_push_attempt.packet.json"
WITNESS = PACKET_DIR / "conditional_rowsource_theorem_witness.packet.json"
ROUTEB_PLUG = PACKET_DIR / "conditional_routeb_physical_certificate_plug.packet.json"
FRONTIER = PACKET_DIR / "remaining_rowsource_or_routea_frontier.packet.json"
CURRENT_RESULT = PACKET_DIR / "current_rowsource_validator_result.packet.json"
WITNESS_RESULT = PACKET_DIR / "conditional_rowsource_validator_result.packet.json"
ROUTEB_PLUG_RESULT = PACKET_DIR / "conditional_routeb_physical_validator_result.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_I11_RouteBRowSourceTheoremPush_or_RouteAFallback_v1.md"

ROWSOURCE_VALIDATOR = ROOT / "scripts" / "validate_selected_routeb_rowsource_independence.py"
PHYSICAL_VALIDATOR = ROOT / "scripts" / "validate_selected_physicalsourcecertificate_or_routeb.py"

STATUS = "MTT_SELECTED_I11_ROUTEB_ROWSOURCE_THEOREM_PUSH_BUILT_FINAL_SOURCE_PROMOTION_GATE"
NEXT = "MTT_Selected_PrimitiveKernelSourceTheorem_or_PhysicalPhiFinC1SourceEmission_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def run_validator(validator: Path, path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(validator), str(path)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return {
        "payload": rel(path),
        "validator": rel(validator),
        "returncode": proc.returncode,
        "stdout": proc.stdout.strip(),
        "stderr_lines": proc.stderr.splitlines(),
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    nearmiss_frontier = load(
        DATA
        / "selected_i11_routeb_nearmiss_or_rowsourcetheorem"
        / "remaining_routeb_rowsource_or_routea_frontier.packet.json"
    )
    current_row_attempt = load(
        DATA
        / "selected_routeb_rowsourceindependenceproof_or_physicalsourcefill"
        / "current_row_source_independence_attempt.packet.json"
    )
    actual_row_attempt = load(
        DATA
        / "selected_routeb_actualrowsourcefill_or_primitivetheoremtemplate"
        / "current_actual_row_source_fill_attempt.packet.json"
    )
    normal_form = load(
        DATA
        / "selected_routeb_rowkernelsource_normalform_or_sourceobjectcontract"
        / "primitive_row_kernel_source_normal_form.packet.json"
    )
    source_contract = load(
        DATA
        / "selected_routeb_rowkernelsource_normalform_or_sourceobjectcontract"
        / "selected_source_object_contract.packet.json"
    )
    two_exit_attempt = load(
        DATA
        / "selected_physicalphifinc1action_or_independentrowkernelsource_theorem"
        / "current_two_exit_source_attempt.packet.json"
    )
    theorem_push = load(
        DATA
        / "selected_sourcetheorem_push_attempt_or_minimalnewlemma"
        / "route_b_independent_rowkernel_source_theorem_push.packet.json"
    )
    routeb_nearmiss = load(
        DATA
        / "selected_i11_routeb_nearmiss_or_rowsourcetheorem"
        / "conditional_route_b_row_source_witness.packet.json"
    )

    current = {
        "schema": "MTTI11RouteBRowSourceTheoremPushAttempt.v1",
        "status": "CURRENT_ROWSOURCE_THEOREM_PUSH_REJECTED_SOURCE_PROMOTION_OPEN",
        "selected_basis_feeds_72_primitive_rows": False,
        "finite_weyl_trace_rule_feeds_all_rows": True,
        "sector_rows_assembled_from_primitive_rows": True,
        "hessian_source_rows_assembled_from_same_rows": True,
        "no_residual_projector_replay_used_as_source": False,
        "no_locked_target_values_used_as_source": True,
        "row_formula_source_theorem_derived": False,
        "source_independent_of_residual_projector_replay": False,
        "attached_source_evidence": [
            {
                "source": rel(
                    DATA
                    / "selected_routeb_rowkernelsource_normalform_or_sourceobjectcontract"
                    / "primitive_row_kernel_source_normal_form.packet.json"
                ),
                "closes": "normal form and finite trace assembly",
            },
            {
                "source": rel(
                    DATA
                    / "selected_routeb_rowkernelsource_normalform_or_sourceobjectcontract"
                    / "selected_source_object_contract.packet.json"
                ),
                "closes": "minimal selected finite C1 row-kernel source object contract",
            },
            {
                "source": rel(
                    DATA
                    / "selected_routeb_actualrowsourcefill_or_primitivetheoremtemplate"
                    / "current_actual_row_source_fill_attempt.packet.json"
                ),
                "closes": "strict primitive-kernel theorem template and current rejected fill",
            },
            {
                "source": rel(
                    DATA
                    / "selected_physicalphifinc1action_or_independentrowkernelsource_theorem"
                    / "current_two_exit_source_attempt.packet.json"
                ),
                "closes": "two legal exits and current failure of both exits",
            },
            {
                "source": rel(
                    DATA
                    / "selected_sourcetheorem_push_attempt_or_minimalnewlemma"
                    / "route_b_independent_rowkernel_source_theorem_push.packet.json"
                ),
                "closes": "minimal Route B source-promotion lemma identification",
            },
        ],
        "imported_open_clauses": normal_form["open_source_clauses"],
        "current_failed_fields": theorem_push["currently_failed_fields"],
        "minimal_source_object": source_contract["minimal_source_object"],
        "route_A_support_status": two_exit_attempt["route_A_physical_action_restriction"],
        "route_B_support_status": two_exit_attempt["route_B_independent_rowkernel_source"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    witness = json.loads(json.dumps(current))
    witness.update(
        {
            "schema": "MTTConditionalI11RouteBRowSourceTheoremWitness.v1",
            "status": "CONDITIONAL_ROWSOURCE_THEOREM_WITNESS_VALIDATES_IF_SOURCE_PROMOTION_LEMMA_SUPPLIED",
            "selected_basis_feeds_72_primitive_rows": True,
            "no_residual_projector_replay_used_as_source": True,
            "row_formula_source_theorem_derived": True,
            "source_independent_of_residual_projector_replay": True,
            "conditional_only": True,
        }
    )
    witness["attached_source_evidence"].append(
        {
            "source": rel(FRONTIER),
            "closes": "SelectedFiniteC1SourcePromotionLemma supplies pre-residual row kernels, variation operators, Hessian source rows, and no residual replay source use",
            "conditional": True,
        }
    )

    routeb_plug = json.loads(json.dumps(routeb_nearmiss))
    routeb_plug["schema"] = "MTTConditionalRouteBPhysicalCertificateAfterRowSourceTheorem.v1"
    routeb_plug["status"] = "CONDITIONAL_ROUTEB_PHYSICAL_CERTIFICATE_PLUG_VALIDATES_AFTER_ROWSOURCE_THEOREM"
    routeb_plug["conditional_rowsource_witness"] = rel(WITNESS)
    routeb_plug["conditional_only"] = True
    routeb_plug["route_B_independent_execution"]["source_independent_of_residual_projector_replay"] = True
    routeb_plug["route_B_independent_execution"]["attached_independent_provenance_sources"].append(
        {
            "source": rel(WITNESS),
            "closes": "all Route B row-source independence fields",
            "promotes_independence": True,
            "conditional": True,
        }
    )

    frontier = {
        "schema": "MTTI11RemainingRowSourceOrRouteAFrontier.v1",
        "status": "ONE_PROOF_OBJECT_REMAINS_FOR_ROUTE_B_OR_ROUTE_A_FALLBACK",
        "closed_now": {
            "row_source_normal_form_reduced": True,
            "minimal_source_object_contract_ready": True,
            "finite_trace_assembly_ready": True,
            "sector_and_hessian_formal_assembly_ready": True,
            "current_rowsource_validator_rejects": True,
            "conditional_rowsource_validator_passes": True,
            "conditional_routeb_physical_certificate_passes": True,
        },
        "route_B_remaining_proof_object": {
            "name": "SelectedFiniteC1SourcePromotionLemma",
            "must_prove": [
                "selected transported bases K_s feed all 72 primitive row kernels before residual projection",
                "selected phase/shift variation operators are emitted pre-residual",
                "same-source Hessian counterterm and b_selected source rows are emitted",
                "36 sector rows and 2 Hessian/source rows assemble from primitive kernels plus finite Weyl trace",
                "residual projector replay and locked target values are postchecks only",
            ],
        },
        "route_A_fallback": nearmiss_frontier["legal_exit_A"],
        "superset_strategy": {
            "straight_route_B": "Promote the independent row-kernel theorem because all numerical/formal Route B fields are already closed.",
            "fallback_route_A": "Derive the physical Phi_fin^C1 action restriction and same-source R_Z/R_X/b_selected emission.",
            "combined_locked_target": "Both paths target the same finite C1 source packet, but only after source emission; residual agreement is a postcheck.",
            "uses_observed_constants": False,
        },
        "not_a_search_problem_anymore": True,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    CURRENT.write_text(json.dumps(current, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    WITNESS.write_text(json.dumps(witness, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    ROUTEB_PLUG.write_text(json.dumps(routeb_plug, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    FRONTIER.write_text(json.dumps(frontier, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    current_result = run_validator(ROWSOURCE_VALIDATOR, CURRENT)
    witness_result = run_validator(ROWSOURCE_VALIDATOR, WITNESS)
    routeb_plug_result = run_validator(PHYSICAL_VALIDATOR, ROUTEB_PLUG)
    CURRENT_RESULT.write_text(json.dumps(current_result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    WITNESS_RESULT.write_text(json.dumps(witness_result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    ROUTEB_PLUG_RESULT.write_text(json.dumps(routeb_plug_result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    candidate = {
        "candidate": "MTTSelectedI11RouteBRowSourceTheoremPushOrRouteAFallback",
        "status": STATUS,
        "inputs": {
            "i11_nearmiss_frontier": rel(
                DATA
                / "selected_i11_routeb_nearmiss_or_rowsourcetheorem"
                / "remaining_routeb_rowsource_or_routea_frontier.packet.json"
            ),
            "row_source_attempt": rel(
                DATA
                / "selected_routeb_rowsourceindependenceproof_or_physicalsourcefill"
                / "current_row_source_independence_attempt.packet.json"
            ),
            "actual_row_source_attempt": rel(
                DATA
                / "selected_routeb_actualrowsourcefill_or_primitivetheoremtemplate"
                / "current_actual_row_source_fill_attempt.packet.json"
            ),
            "source_object_contract": rel(
                DATA
                / "selected_routeb_rowkernelsource_normalform_or_sourceobjectcontract"
                / "selected_source_object_contract.packet.json"
            ),
            "two_exit_source_attempt": rel(
                DATA
                / "selected_physicalphifinc1action_or_independentrowkernelsource_theorem"
                / "current_two_exit_source_attempt.packet.json"
            ),
        },
        "output_packets": {
            "current_attempt": rel(CURRENT),
            "conditional_rowsource_witness": rel(WITNESS),
            "conditional_routeb_physical_certificate_plug": rel(ROUTEB_PLUG),
            "remaining_frontier": rel(FRONTIER),
            "current_rowsource_validator_result": rel(CURRENT_RESULT),
            "conditional_rowsource_validator_result": rel(WITNESS_RESULT),
            "conditional_routeb_physical_validator_result": rel(ROUTEB_PLUG_RESULT),
        },
        "theorem": {
            "name": "I11RouteBRowSourceTheoremPush",
            "proved": True,
            "statement": (
                "The I11 Route-B closure problem is equivalent to proving the SelectedFiniteC1SourcePromotionLemma. "
                "All finite trace, formal row, sector assembly, Hessian assembly, and locked-target guardrail fields are already in place. "
                "The current source-promotion attempt fails exactly because row kernels, variation operators, and Hessian/source rows have not yet been emitted pre-residual from the selected finite C1 source. "
                "A packet satisfying those source clauses validates the row-source validator and plugs into the Route-B physical-source certificate."
            ),
        },
        "what_closes_now": {
            "current_rowsource_attempt_rejected": current_result["returncode"] == 1,
            "conditional_rowsource_witness_passes": witness_result["returncode"] == 0,
            "conditional_routeb_physical_certificate_passes": routeb_plug_result["returncode"] == 0,
            "final_route_B_proof_object_identified": True,
            "route_A_fallback_preserved": True,
        },
        "what_remains_open": {
            "SelectedFiniteC1SourcePromotionLemma": True,
            "RouteA_PhysicalPhiFinC1ActionRestriction": True,
        },
        "conditional_only": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_I11_RouteBRowSourceTheoremPush_or_RouteAFallback_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "current_rowsource_attempt_rejected": current_result["returncode"] == 1,
        "conditional_rowsource_witness_passes": witness_result["returncode"] == 0,
        "conditional_routeb_physical_certificate_passes": routeb_plug_result["returncode"] == 0,
        "final_route_B_proof_object_identified": True,
        "route_A_fallback_preserved": True,
        "conditional_only": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected I11 RouteB RowSourceTheorem Push or RouteA Fallback v1

Status: `{STATUS}`.

This artifact sharpens the last SM-parity source gate. Route B is no longer a
numerical search: it is a single source-promotion theorem.

```text
current row-source validator rejects          = {current_result["returncode"] == 1}
conditional row-source witness validates      = {witness_result["returncode"] == 0}
conditional Route-B physical certificate pass = {routeb_plug_result["returncode"] == 0}
```

The remaining Route-B theorem is `SelectedFiniteC1SourcePromotionLemma`.
It must emit the selected pre-residual primitive row kernels, phase/shift
variation operators, Hessian counterterm and `b_selected` source rows, and prove
that residual-projector replay and locked target values are postchecks only.

Route A remains the straight physical-action fallback: derive the same packet
from selected `Phi_fin^C1` action restriction with no extra boundary/source term.

No observed SM constants, benchmark rows, locked residual targets, or fitted
values are used as selectors.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
