"""Build Strominger-trace C1 first-variation / quadrature execution plan gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
DRAFT_DIR = CORPUS / "paper_appendix_drafts" / "selected_source"

PREVIOUS_SLUG = "selected_i10_payloadcertificate_or_independentquadraturevaluesfill"
PREVIOUS = DATA / f"{PREVIOUS_SLUG}.candidate.json"
CUTSET = DATA / PREVIOUS_SLUG / "minimal_next_cutset.packet.json"
ROUTE_A_ATTEMPT = DATA / PREVIOUS_SLUG / "route_a_i10_payload_certificate_fill_attempt.packet.json"
ROUTE_B_ATTEMPT = DATA / PREVIOUS_SLUG / "route_b_independent_quadrature_values_fill_attempt.packet.json"

SLUG = "selected_stromingertracec1firstvariation_or_quadratureexecutionplan"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
FIRST_VARIATION = PACKET_DIR / "route_a_first_variation_certificate_plan.packet.json"
QUADRATURE_PLAN = PACKET_DIR / "route_b_quadrature_execution_manifest.packet.json"
ROW_SCHEDULE = PACKET_DIR / "quadrature_row_schedule.packet.json"
PAPER_DRAFT = DRAFT_DIR / "theta_execution_flavor__i11_strominger_trace_c1_first_variation.md"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_StromingerTraceC1FirstVariation_or_QuadratureExecutionPlan_v1.md"

STATUS = "MTT_SELECTED_STROMINGERTRACE_C1_FIRSTVARIATION_OR_QUADRATURE_EXECUTION_PLAN_BUILT_OPEN"
NEXT = "MTT_Selected_C1FirstVariationCertificateFill_or_QuadratureRowsFirstRun_v1"

SECTORS = ["u", "e", "d", "nuD"]
RESPONSES = ["phase", "shift"]


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def primitive_row_ids() -> list[str]:
    return [f"{sector}:{response}:r{row}c{col}" for sector in SECTORS for response in RESPONSES for row in range(3) for col in range(3)]


def sector_matrix_row_ids() -> list[str]:
    return [f"{sector}:M:r{row}c{col}" for sector in SECTORS for row in range(3) for col in range(3)]


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    DRAFT_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    cutset = load(CUTSET)
    route_a_attempt = load(ROUTE_A_ATTEMPT)
    route_b_attempt = load(ROUTE_B_ATTEMPT)
    replay = previous["replay_if_route_A_or_B_accepted"]

    first_variation = {
        "schema": "MTTStromingerTraceC1FirstVariationCertificatePlan.v1",
        "status": "CERTIFICATE_PLAN_BUILT_VALUES_OPEN",
        "route": "A",
        "theorem_slot": "I11_strominger_trace_c1_first_variation",
        "purpose": "Make the I10 minimizer proof checkable by replacing informal minimization with first-variation, Hessian/coercivity, boundary, and normalization clauses.",
        "inputs_from_previous_attempt": {
            "missing_payloads": [
                key
                for key, item in route_a_attempt["payload_checks"].items()
                if isinstance(item, dict) and item.get("value") is False
            ],
            "no_observed_data_as_selector": route_a_attempt["payload_checks"]["no_observed_data_as_selector"]["value"],
        },
        "certificate_fields": {
            "selected_trace_map": {
                "required": True,
                "must_provide": [
                    "selected minimizer identifier",
                    "finite Phi_fin trace operator",
                    "C1 response coordinate map",
                    "selected normalization/boundary clause",
                ],
                "verified_now": False,
            },
            "first_variation_identity": {
                "required": True,
                "formula": "d/dt Q(Phi_fin^C1 + t eta)|_{t=0}=0 for all admissible eta in the selected C1 response span",
                "verified_now": False,
            },
            "hessian_or_coercivity": {
                "required": True,
                "formula": "delta^2 Q[eta,eta] >= c ||Q_residual eta||^2 with c>0 on the admissible quotient span",
                "verified_now": False,
            },
            "boundary_cancellation": {
                "required": True,
                "formula": "boundary terms vanish under selected q79/F,m=1 S3/GS routing and finite trace constraints",
                "verified_now": False,
            },
            "normalization_compatibility": {
                "required": True,
                "formula": "finite trace/Frobenius normalization leaves the Euler equation scale-independent",
                "verified_now": False,
            },
        },
        "would_close_if_all_verified": {
            "defect_functional_minimizer_payload_verified": True,
            "selected_minimizer_trace_payload_verified": True,
            "selected_c1_response_payload_verified": True,
            "I10_proved": True,
            "unpatched_dynamic_packet_closed": True,
        },
        "verified_now": False,
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    zero_mode_ids = [
        "Q:k0",
        "Q:k1",
        "Q:k2",
        "u:k0",
        "u:k1",
        "u:k2",
        "d:k0",
        "d:k1",
        "d:k2",
        "L:k0",
        "L:k1",
        "L:k2",
        "e:k0",
        "e:k1",
        "e:k2",
        "nuD:k0",
        "nuD:k1",
        "nuD:k2",
        "H:h0",
    ]
    primitive_ids = primitive_row_ids()
    sector_ids = sector_matrix_row_ids()
    hessian_ids = ["theta_phase", "theta_shift"]
    quadrature_plan = {
        "schema": "MTTQuadratureExecutionManifest.v1",
        "status": "EXECUTION_PLAN_BUILT_VALUES_OPEN",
        "route": "B",
        "purpose": "Produce independent rows sufficient to verify A, b, sector matrices, rank, and deltaTheta without relying on the I10 theorem.",
        "previous_table_counts": route_b_attempt["table_counts"],
        "row_requirements": {
            "zero_mode_basis_rows": {
                "count": len(zero_mode_ids),
                "row_ids": zero_mode_ids,
                "filled_now": False,
            },
            "primitive_contraction_rows": {
                "count": len(primitive_ids),
                "row_ids": primitive_ids,
                "filled_now": False,
            },
            "hessian_source_rows": {
                "count": len(hessian_ids),
                "row_ids": hessian_ids,
                "filled_now": False,
            },
            "sector_matrix_rows": {
                "count": len(sector_ids),
                "row_ids": sector_ids,
                "filled_now": False,
            },
        },
        "acceptance_equations": {
            "A_transpose_A_target": replay["A_transpose_A"],
            "A_transpose_b_target": replay["A_transpose_b"],
            "deltaTheta_C1_target": replay["deltaTheta_C1"],
            "rank_minimum": 2,
            "forbidden_shortcuts": [
                "copying A or b from patched replay without row-level quadrature support",
                "using measured masses, mixings, or CP phase as row targets",
                "declaring rank from the target solve without row-level matrix construction",
            ],
        },
        "accepted_now": False,
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    row_schedule = {
        "schema": "MTTQuadratureRowSchedule.v1",
        "status": "ROW_SCHEDULE_BUILT_NOT_EXECUTED",
        "execution_order": [
            {
                "stage": "basis",
                "rows": zero_mode_ids,
                "why_first": "All primitive and sector rows must reference selected basis ids.",
            },
            {
                "stage": "primitive_contractions",
                "rows": primitive_ids,
                "why_second": "Primitive rows build the raw 72-real response tensor.",
            },
            {
                "stage": "hessian_source",
                "rows": hessian_ids,
                "why_third": "Hessian/source rows normalize the two response columns and b vector.",
            },
            {
                "stage": "sector_matrices",
                "rows": sector_ids,
                "why_fourth": "Sector matrices are the final observable packet after row-level contractions.",
            },
        ],
        "next_executable_stage": "basis",
        "executed_now": False,
    }

    draft = """# Appendix Slot I11: Strominger Trace C1 First Variation

## Theorem Slot I11

Let `Phi_fin^C1` be the selected finite C1 trace of the q79/F,m=1
S3/Green-Schwarz Strominger/HYM minimizer, with selected same-branch C1
response span and finite trace/Frobenius normalization.

The required first-variation certificate consists of four checks:

1. The selected finite trace emits a C1 coordinate map on the admissible response span.
2. The first variation of the unique C1 defect functional vanishes on all admissible variations.
3. The Hessian is coercive or convex on the residual quotient span.
4. Boundary terms cancel under the selected routing and normalization conventions.

If these four checks are proved from the selected source packet, I10 follows
without using measured SM masses, mixings, CP phase, benchmark matrices, or
target residuals.
"""
    PAPER_DRAFT.write_text(draft, encoding="utf-8")

    candidate = {
        "candidate": "MTTSelectedStromingerTraceC1FirstVariationOrQuadratureExecutionPlan",
        "status": STATUS,
        "inputs": {
            "previous_gate": rel(PREVIOUS),
            "minimal_cutset": rel(CUTSET),
            "route_a_attempt": rel(ROUTE_A_ATTEMPT),
            "route_b_attempt": rel(ROUTE_B_ATTEMPT),
        },
        "output_packets": {
            "route_a_first_variation_certificate_plan": rel(FIRST_VARIATION),
            "route_b_quadrature_execution_manifest": rel(QUADRATURE_PLAN),
            "quadrature_row_schedule": rel(ROW_SCHEDULE),
            "paper_draft_I11": rel(PAPER_DRAFT),
        },
        "what_closes_now": {
            "I11_first_variation_certificate_schema_built": True,
            "quadrature_execution_row_schedule_built": True,
            "route_A_and_route_B_next_steps_are_executable": True,
            "superset_strategy_locked_to_same_target": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "selected_trace_map_values": True,
            "first_variation_identity_verified": True,
            "hessian_or_coercivity_verified": True,
            "boundary_cancellation_verified": True,
            "quadrature_rows_executed": True,
            "unpatched_SM_parity_dynamic_packet_closure": True,
            "true_SM_equivalence_closure": True,
        },
        "promotion_decision": {
            "route_A_first_variation_certificate_accepted": False,
            "route_B_quadrature_execution_accepted": False,
            "I10_proved": False,
            "unpatched_A_selected_promoted": False,
            "unpatched_b_selected_promoted": False,
            "unpatched_deltaTheta_C1_promoted": False,
            "unpatched_SM_parity_dynamic_packet_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "StromingerTraceC1FirstVariationOrQuadratureExecutionPlanTheorem",
            "proved": True,
            "statement": (
                "The remaining I10 gate is reduced to two executable continuations: a selected first-variation "
                "certificate for the Strominger/HYM finite C1 trace, or an independent quadrature execution "
                "plan with explicit basis, primitive, Hessian, and sector row schedules."
            ),
        },
        "superset_strategy": {
            "straight_route": cutset["recommended_next"]["superset_strategy"]["straight_route"],
            "parallel_route": cutset["recommended_next"]["superset_strategy"]["parallel_route"],
            "locked_target": cutset["recommended_next"]["superset_strategy"]["locked_target"],
        },
        "observed_data_used": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_StromingerTraceC1FirstVariation_or_QuadratureExecutionPlan_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected StromingerTraceC1FirstVariation or QuadratureExecutionPlan v1

Status: `{STATUS}`.

This gate converts the previous cutset into executable next steps.

Route A now requires the I11 first-variation certificate:

```text
selected trace map values        = False
first-variation identity         = False
Hessian/coercivity clause        = False
boundary cancellation            = False
normalization compatibility      = False
```

Route B now has a row schedule:

```text
zero-mode basis rows       = {len(zero_mode_ids)}
primitive contraction rows = {len(primitive_ids)}
hessian source rows        = {len(hessian_ids)}
sector matrix rows         = {len(sector_ids)}
```

Locked replay target:

```text
A^T A      = {replay["A_transpose_A"]}
A^T b      = {replay["A_transpose_b"]}
deltaTheta = {replay["deltaTheta_C1"]}
```

Next artifact: `{NEXT}`.
"""

    FIRST_VARIATION.write_text(json.dumps(first_variation, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    QUADRATURE_PLAN.write_text(json.dumps(quadrature_plan, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    ROW_SCHEDULE.write_text(json.dumps(row_schedule, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
