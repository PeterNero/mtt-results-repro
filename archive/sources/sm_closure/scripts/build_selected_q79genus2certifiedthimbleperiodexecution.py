from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79genus2thimbleperiodexecution"
OUTPUT_DIR = ROOT / "candidate_data" / SLUG
BATCH = OUTPUT_DIR / "distinguished_thimble_period_batch.packet.json"
PRIMITIVE = OUTPUT_DIR / "primitive_thimble_period_candidate_table.packet.json"
CLOSED = OUTPUT_DIR / "closed_thimble_period_candidate_table.packet.json"
REPRESENTATIVE = OUTPUT_DIR / "representative_convergence_audit.packet.json"
FULL = OUTPUT_DIR / "full_90_column_convergence_audit.packet.json"
PRESENTATION = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2integralsurfacecyclepresentation"
    / "integral_surface_cycle_presentation.packet.json"
)
ENGINE = ROOT / "scripts" / "q79genus2_period_transport.py"
NOTE = (
    ROOT
    / "proof_corpus"
    / "MTT_Selected_q79GenusTwoCertifiedThimblePeriodExecution_v1.md"
)
SUMMARY = OUTPUT_DIR / "certified_thimble_period_execution.packet.json"
FRONTIER = OUTPUT_DIR / "U6_frontier_after_A118.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERTIFICATE = ROOT / "certificates" / f"{SLUG}_certificate.json"
STATUS = (
    "MTT_U6_Q79_ALL_THIMBLE_PERIODS_FLOATING_CONVERGED_"
    "HANDLE_LERAY_INTERVAL_PROMOTION_OPEN"
)
NEXT = "MTT_Selected_q79GenusTwoHandleAndLerayPeriodExecution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    inputs = (
        BATCH,
        PRIMITIVE,
        CLOSED,
        REPRESENTATIVE,
        FULL,
        PRESENTATION,
        ENGINE,
        NOTE,
    )
    for path in inputs:
        if not path.exists():
            raise FileNotFoundError(path)

    batch = load(BATCH)
    primitive = load(PRIMITIVE)
    closed = load(CLOSED)
    representative = load(REPRESENTATIVE)
    full = load(FULL)
    presentation = load(PRESENTATION)
    engine_hash = sha256(ENGINE)
    if batch["authority"]["period_engine_sha256"] != engine_hash:
        raise AssertionError("stale batch engine authority")
    if full["authority"]["period_engine_sha256"] != engine_hash:
        raise AssertionError("stale full-audit engine authority")
    if representative["authority"]["period_engine_sha256"] != engine_hash:
        raise AssertionError("stale representative engine authority")

    primitive_comparison = full["primitive_table_comparison"]
    closed_comparison = full["closed_thimble_table_comparison"]
    summary = {
        "schema": "MTTQ79CertifiedThimblePeriodExecution.v1",
        "status": STATUS,
        "authority": {
            "period_engine_sha256": engine_hash,
            "integral_cycle_presentation_sha256": sha256(PRESENTATION),
            "batch_sha256": sha256(BATCH),
            "primitive_table_sha256": sha256(PRIMITIVE),
            "closed_table_sha256": sha256(CLOSED),
            "representative_convergence_sha256": sha256(REPRESENTATIVE),
            "full_convergence_sha256": sha256(FULL),
        },
        "execution": {
            "primitive_table_shape": [8, 90],
            "primitive_complex_entries": 720,
            "closed_thimble_table_shape": [8, 86],
            "closed_thimble_complex_entries": 688,
            "assembly": "Pi_thimble=T_8x90*K_90x86",
            "desingularized_local_direct_columns": batch["counts"][
                "desingularized_local_direct_columns"
            ],
            "high_precision_Gauss_Manin_connection_evaluations": batch[
                "counts"
            ]["high_precision_Gauss_Manin_connection_evaluations"],
        },
        "numerical_safety": {
            "minimum_endpoint_tail_clearance": batch["minimums"][
                "endpoint_tail_other_root_normalized_clearance"
            ],
            "minimum_local_direct_clearance": batch["minimums"][
                "local_direct_other_root_normalized_clearance"
            ],
            "maximum_equilibrated_reduction_condition": batch["maximums"][
                "equilibrated_Gauss_Manin_reduction_condition_number"
            ],
            "maximum_high_precision_solution_ball_radius": batch["maximums"][
                "high_precision_solution_ball_radius"
            ],
            "maximum_ODE_function_evaluations": batch["maximums"][
                "ODE_function_evaluations"
            ],
        },
        "full_convergence": {
            "all_90_columns_rerun": full["strict_scope"][
                "all_90_columns_independently_rerun"
            ],
            "primitive": primitive_comparison,
            "closed_thimble": closed_comparison,
            "representative_three_axis_maximum_scale_normalized_difference": representative[
                "maximum_scale_normalized_difference"
            ],
        },
        "surface_column_ledger": {
            "floating_closed_thimble_columns": 86,
            "handle_columns_open": 4,
            "Leray_edge_columns_open": 2,
            "final_integral_period_table_shape": [8, 92],
            "final_integral_period_table_complete": False,
        },
        "A119_supersession": {
            "primitive_90_column_table_remains_valid": True,
            "old_86_column_TK_table_is_diagnostic_only": True,
            "old_86_column_table_promoted_to_final_integral_H2": False,
            "reason": "A119 aligns the endpoint-chord orientations and attaches the handle thimble tails before taking the primitive quotient.",
        },
        "strict_scope": {
            "floating_thimble_execution_closed": True,
            "full_floating_convergence_audit_closed": True,
            "interval_period_enclosure_closed": False,
            "handle_period_execution_closed": False,
            "Leray_edge_period_execution_closed": False,
            "beta_vector_closed": False,
            "integral_branch_selected": False,
            "gerbe_zero_or_no_go_closed": False,
            "full_U6_closed": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": NEXT,
    }
    dump(SUMMARY, summary)

    frontier = {
        "schema": "MTTU6FrontierAfterA118.v1",
        "status": STATUS,
        "global_integral_H1_surface_relation_closed": True,
        "integral_surface_cycle_presentation_closed": True,
        "primitive_thimble_columns_executed": 90,
        "closed_thimble_columns_with_floating_periods": 86,
        "handle_columns_executed": 0,
        "Leray_edge_columns_executed": 0,
        "surface_H2_rank": presentation["surface_h2_decomposition"][
            "known_integral_H2_rank"
        ],
        "final_integral_period_columns_executed": 86,
        "final_integral_period_columns_required": 92,
        "full_90_column_floating_convergence_audited": True,
        "interval_period_columns_certified": 0,
        "beta_C_period_rows_emitted": 0,
        "integral_period_branch_selected": False,
        "gerbe_zero_or_no_go_executed": False,
        "strict_MTT_source_moduli_removed": 0,
        "U6_strong_CP_closed": False,
        "next_required_artifact": NEXT,
    }
    dump(FRONTIER, frontier)

    authority_paths = [*inputs, Path(__file__), SUMMARY, FRONTIER]
    candidate = {
        "schema": "MTTSelectedQ79GenusTwoCertifiedThimblePeriodExecution.v1",
        "status": STATUS,
        "proof_artifact": str(NOTE.relative_to(ROOT)).replace("\\", "/"),
        "authority_hashes": [
            {
                "path": str(path.relative_to(ROOT)).replace("\\", "/"),
                "sha256": sha256(path),
            }
            for path in authority_paths
        ],
        "outputs": {
            "summary": str(SUMMARY.relative_to(ROOT)).replace("\\", "/"),
            "primitive_table": str(PRIMITIVE.relative_to(ROOT)).replace(
                "\\", "/"
            ),
            "closed_thimble_table": str(CLOSED.relative_to(ROOT)).replace(
                "\\", "/"
            ),
            "frontier": str(FRONTIER.relative_to(ROOT)).replace("\\", "/"),
        },
        "supersession": {
            "artifact": "MTT_Selected_q79GenusTwoHandleAndLerayPeriodExecution_v1",
            "primitive_thimble_values_retained": True,
            "old_TK_integral_basis_interpretation_retired": True,
        },
        "checks": {
            "all_90_primitive_columns_executed": batch["counts"][
                "complete_period_packets"
            ]
            == 90,
            "all_86_closed_thimble_columns_assembled": len(
                closed["period_rows"][0]
            )
            == 86,
            "full_90_column_rerun_executed": full["strict_scope"][
                "all_90_columns_independently_rerun"
            ],
            "primitive_scaled_difference_below_2e_8": float(
                primitive_comparison["maximum_scale_normalized_difference"]
            )
            < 2.0e-8,
            "closed_scaled_difference_below_1e_8": float(
                closed_comparison["maximum_scale_normalized_difference"]
            )
            < 1.0e-8,
            "local_direct_clearance_above_one": float(
                batch["minimums"][
                    "local_direct_other_root_normalized_clearance"
                ]
            )
            > 1.0,
            "interval_promotion_not_invented": not summary["strict_scope"][
                "interval_period_enclosure_closed"
            ],
            "handle_and_Leray_values_not_invented": (
                frontier["handle_columns_executed"] == 0
                and frontier["Leray_edge_columns_executed"] == 0
            ),
            "integral_branch_not_invented": not frontier[
                "integral_period_branch_selected"
            ],
            "gerbe_decision_not_invented": not frontier[
                "gerbe_zero_or_no_go_executed"
            ],
        },
        "results": frontier,
        "next_required_artifact": NEXT,
    }
    dump(CANDIDATE, candidate)
    certificate = {
        "certificate": "MTTSelectedQ79GenusTwoCertifiedThimblePeriodExecution",
        "status": STATUS,
        "candidate_path": str(CANDIDATE.relative_to(ROOT)).replace("\\", "/"),
        "candidate_sha256": sha256(CANDIDATE),
        "closure_claimed": False,
        "floating_thimble_period_execution_closed": True,
        "interval_period_enclosure_closed": False,
        "final_8x92_period_table_closed": False,
        "full_U6_closed": False,
        "old_TK_integral_basis_interpretation_superseded_by_A119": True,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    dump(CERTIFICATE, certificate)
    print(json.dumps(candidate, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
