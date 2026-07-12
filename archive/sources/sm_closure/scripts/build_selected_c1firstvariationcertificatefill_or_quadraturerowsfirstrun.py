"""Build C1 first-variation certificate fill / quadrature rows first-run gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PREVIOUS_SLUG = "selected_stromingertracec1firstvariation_or_quadratureexecutionplan"
PREVIOUS = DATA / f"{PREVIOUS_SLUG}.candidate.json"
FIRST_PLAN = DATA / PREVIOUS_SLUG / "route_a_first_variation_certificate_plan.packet.json"
QUAD_PLAN = DATA / PREVIOUS_SLUG / "route_b_quadrature_execution_manifest.packet.json"
ROW_SCHEDULE = DATA / PREVIOUS_SLUG / "quadrature_row_schedule.packet.json"
FUNCTIONAL_SOURCE = DATA / "selected_c1defectfunctionalsource_or_independentquadraturedatafill" / "c1_defect_functional_uniqueness_source.packet.json"
ZERO_MODE_THEOREM = DATA / "selected_zero_mode_basis_from_hym_projector_source_theorem.candidate.json"

SLUG = "selected_c1firstvariationcertificatefill_or_quadraturerowsfirstrun"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROUTE_A_FILL = PACKET_DIR / "route_a_first_variation_certificate_partial_fill.packet.json"
ROUTE_B_FIRST_RUN = PACKET_DIR / "route_b_basis_rows_first_run.packet.json"
NEXT_CUTSET = PACKET_DIR / "next_cutset_after_partial_fill.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_C1FirstVariationCertificateFill_or_QuadratureRowsFirstRun_v1.md"

STATUS = "MTT_SELECTED_C1_FIRSTVARIATION_PARTIAL_FILL_OR_QUADRATURE_BASIS_FIRST_RUN_BUILT_OPEN"
NEXT = "MTT_Selected_TraceMapAndBasisValues_or_PrimitiveRowsExecution_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def basis_stub(row_id: str, zero_mode: dict[str, Any]) -> dict[str, Any]:
    sector, basis_id = row_id.split(":")
    lookup_sector = "N" if sector == "nuD" else sector
    slot = zero_mode["finite_acceptance_validator"]["required_slots"].get(lookup_sector)
    required_rank = slot["required_rank"] if slot else 1
    carrier = slot["required_carrier"] if slot else "trivial singlet"
    return {
        "basis_id": row_id,
        "sector": sector,
        "required_rank": required_rank,
        "required_carrier": carrier,
        "selected_basis_value": None,
        "selected_projector_value": None,
        "gram_matrix": None,
        "spectral_gap": None,
        "source_certificate": rel(ZERO_MODE_THEOREM),
        "selected_now": False,
        "why_not_selected": "The HYM projector zero-mode theorem is available as a bridge, but selected sector projectors/bases are not emitted.",
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    first_plan = load(FIRST_PLAN)
    quad_plan = load(QUAD_PLAN)
    row_schedule = load(ROW_SCHEDULE)
    functional = load(FUNCTIONAL_SOURCE)
    zero_mode = load(ZERO_MODE_THEOREM)

    route_a_fill = {
        "schema": "MTTC1FirstVariationCertificatePartialFill.v1",
        "status": "PARTIAL_FILL_FORMAL_HESSIAN_NORMALIZATION_CLOSED_TRACE_AND_VARIATION_OPEN",
        "source_plan": rel(FIRST_PLAN),
        "filled_fields": {
            "selected_trace_map": {
                "verified": False,
                "reason": "The selected minimizer and finite Phi_fin trace values are still not emitted.",
            },
            "first_variation_identity": {
                "verified": False,
                "reason": "The formal Euler equation is available only after Phi_fin^C1 is bound to the selected defect functional; that physical binding is still open.",
            },
            "hessian_or_coercivity": {
                "verified": True,
                "scope": "formal C1 defect functional on the residual quotient span",
                "constant_c": 1.0,
                "source": rel(FUNCTIONAL_SOURCE),
                "reason": "The sourced functional is the squared Frobenius norm of the residual projection, so its Hessian is positive and coercive on the quotient by the fixed-fiber span.",
            },
            "boundary_cancellation": {
                "verified": False,
                "reason": "No selected finite trace operator is emitted, so boundary cancellation for the physical differentiated trace is not yet checkable.",
            },
            "normalization_compatibility": {
                "verified": True,
                "source": rel(FUNCTIONAL_SOURCE),
                "reason": "The functional-source gate already proves positive-scale independence of the Euler projection under the selected trace/Frobenius metric.",
            },
        },
        "functional_source_status": functional["status"],
        "certificate_accepted_now": False,
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    basis_ids = quad_plan["row_requirements"]["zero_mode_basis_rows"]["row_ids"]
    basis_rows = [basis_stub(row_id, zero_mode) for row_id in basis_ids]
    selected_count = sum(1 for row in basis_rows if row["selected_now"])
    route_b_first_run = {
        "schema": "MTTQuadratureBasisRowsFirstRun.v1",
        "status": "BASIS_ROW_STUBS_EMITTED_SELECTED_VALUES_OPEN",
        "source_plan": rel(QUAD_PLAN),
        "basis_rows": basis_rows,
        "row_count": len(basis_rows),
        "selected_row_count": selected_count,
        "all_basis_rows_selected": selected_count == len(basis_rows),
        "zero_mode_bridge_status": zero_mode["status"],
        "zero_mode_current_blockers": zero_mode["current_blockers"],
        "can_advance_to_primitive_rows": False,
        "why_not": [
            "selected sector projectors P_s are not emitted",
            "ordered selected bases K_s are not emitted",
            "selected Gram matrices and spectral gaps are not emitted",
            "primitive rows cannot reference selected basis values yet",
        ],
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    next_cutset = {
        "schema": "MTTC1FirstVariationOrQuadratureNextCutset.v1",
        "status": "NEXT_CUTSET_AFTER_PARTIAL_FILL_SELECTED",
        "closed_now": [
            "formal_hessian_coercivity_on_residual_quotient",
            "finite_trace_frobenius_normalization_scale_independence",
            "basis_row_id_schedule_materialized",
        ],
        "still_blocks_route_A": [
            "selected_trace_map_values",
            "physical_first_variation_identity",
            "boundary_cancellation_for_selected_trace",
        ],
        "still_blocks_route_B": [
            "selected_projector_values",
            "ordered_selected_zero_mode_bases",
            "selected_Gram_matrices",
            "spectral_gap_and_error_bounds",
        ],
        "recommended_next": {
            "artifact": NEXT,
            "reason": "After the formal Hessian/normalization partial fill, both legal routes now depend on selected trace/basis values from the same HYM/Strominger source packet.",
            "superset_strategy": {
                "shared_missing_object": "selected HYM/Strominger finite trace plus sector projector/basis values",
                "straight_route_A": "emit selected trace map values, then prove first variation and boundary cancellation",
                "parallel_route_B": "emit selected basis/projector/Gram/gap rows, then run primitive contraction rows",
            },
        },
    }

    route_a_accepted = all(field["verified"] for field in route_a_fill["filled_fields"].values())
    route_b_accepted = route_b_first_run["all_basis_rows_selected"]
    candidate = {
        "candidate": "MTTSelectedC1FirstVariationCertificateFillOrQuadratureRowsFirstRun",
        "status": STATUS,
        "inputs": {
            "previous_gate": rel(PREVIOUS),
            "first_variation_plan": rel(FIRST_PLAN),
            "quadrature_execution_manifest": rel(QUAD_PLAN),
            "quadrature_row_schedule": rel(ROW_SCHEDULE),
            "functional_source": rel(FUNCTIONAL_SOURCE),
            "zero_mode_basis_theorem": rel(ZERO_MODE_THEOREM),
        },
        "output_packets": {
            "route_a_first_variation_certificate_partial_fill": rel(ROUTE_A_FILL),
            "route_b_basis_rows_first_run": rel(ROUTE_B_FIRST_RUN),
            "next_cutset_after_partial_fill": rel(NEXT_CUTSET),
        },
        "what_closes_now": {
            "formal_hessian_coercivity_on_residual_quotient": True,
            "normalization_scale_independence": True,
            "basis_row_stubs_emitted": True,
            "shared_trace_basis_cutset_identified": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "selected_trace_map_values": True,
            "physical_first_variation_identity": True,
            "boundary_cancellation_for_selected_trace": True,
            "selected_basis_projector_gram_gap_values": True,
            "primitive_quadrature_rows": True,
            "unpatched_SM_parity_dynamic_packet_closure": True,
            "true_SM_equivalence_closure": True,
        },
        "promotion_decision": {
            "route_A_first_variation_certificate_accepted": route_a_accepted,
            "route_B_basis_rows_accepted": route_b_accepted,
            "route_B_can_advance_to_primitive_rows": route_b_first_run["can_advance_to_primitive_rows"],
            "I10_proved": False,
            "unpatched_A_selected_promoted": False,
            "unpatched_b_selected_promoted": False,
            "unpatched_deltaTheta_C1_promoted": False,
            "unpatched_SM_parity_dynamic_packet_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "C1FirstVariationPartialFillAndBasisRowsFirstRunTheorem",
            "proved": True,
            "statement": (
                "The formal defect-functional Hessian/coercivity and normalization clauses are closed at the "
                "functional level, but the physical I11 certificate still needs selected trace values and first "
                "variation/boundary binding. The first quadrature run emits all basis row stubs but cannot accept "
                "them until selected projector, basis, Gram, and gap values are emitted."
            ),
        },
        "observed_data_used": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_C1FirstVariationCertificateFill_or_QuadratureRowsFirstRun_v1",
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

    note = f"""# MTT Selected C1FirstVariationCertificateFill or QuadratureRowsFirstRun v1

Status: `{STATUS}`.

Route A partial fill:

```text
selected trace map                 = False
physical first variation identity  = False
formal Hessian/coercivity          = True
boundary cancellation              = False
normalization compatibility        = True
```

Route B first run:

```text
basis row stubs emitted            = {len(basis_rows)}
selected basis rows                = {selected_count}
advance to primitive rows          = False
```

The shared missing object is now sharper: selected HYM/Strominger finite trace
plus selected sector projector/basis/Gram/gap values.

Next artifact: `{NEXT}`.
"""

    ROUTE_A_FILL.write_text(json.dumps(route_a_fill, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    ROUTE_B_FIRST_RUN.write_text(json.dumps(route_b_first_run, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NEXT_CUTSET.write_text(json.dumps(next_cutset, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
