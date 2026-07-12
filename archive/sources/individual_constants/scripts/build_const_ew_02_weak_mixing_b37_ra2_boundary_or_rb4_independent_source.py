"""Build CONST-EW-02 B37 RA-2 boundary or RB-4 independent source."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_ew_02_weak_mixing_b37_ra2_boundary_or_rb4_independent_source"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
RA2 = BASE / "route_a_ra2_boundary_source_reduction.packet.json"
RB4 = BASE / "route_b_rb4_independent_source_payload_contract.packet.json"
BOUNDARY = BASE / "weak_mixing_b37_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_EW_02_WeakMixing_B37_RA2_Boundary_or_RB4_IndependentSource_v1.md"

STATUS = "MTT_CONST_EW_02_B37_RA2_BOUNDARY_OR_RB4_INDEPENDENT_SOURCE_BUILT"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    b36_path = DATA / "const_ew_02_weak_mixing_b36_ra1_equality_or_rb3_hessian.candidate.json"
    b36_boundary_path = DATA / "const_ew_02_weak_mixing_b36_ra1_equality_or_rb3_hessian" / "weak_mixing_b36_boundary.packet.json"

    defect_path = SM / "candidate_data" / "selected_c1defectfunctionalsource_or_independentquadraturedatafill.candidate.json"
    defect_source_path = SM / "candidate_data" / "selected_c1defectfunctionalsource_or_independentquadraturedatafill" / "c1_defect_functional_uniqueness_source.packet.json"
    phifin_gap_path = SM / "candidate_data" / "selected_c1defectfunctionalsource_or_independentquadraturedatafill" / "phifinc1_physical_application_source_gap.packet.json"
    trace_boundary_path = SM / "candidate_data" / "selected_c1tracemeasurepromotion_or_actionboundaryproof.candidate.json"
    finite_boundary_path = SM / "candidate_data" / "selected_c1tracemeasurepromotion_or_actionboundaryproof" / "finite_trace_boundary_cancellation_certificate.packet.json"
    physical_promotion_path = SM / "candidate_data" / "selected_c1tracemeasurepromotion_or_actionboundaryproof" / "physical_action_boundary_promotion_attempt.packet.json"
    rb4_schema_path = SM / "candidate_data" / "selected_routeb_independentquadraturepayload_schema_or_executionworkorder.candidate.json"
    rb4_payload_schema_path = SM / "candidate_data" / "selected_routeb_independentquadraturepayload_schema_or_executionworkorder" / "routeb_independent_quadrature_payload_schema.packet.json"

    b36 = load(b36_path)
    b36_boundary = load(b36_boundary_path)
    defect = load(defect_path)
    defect_source = load(defect_source_path)
    phifin_gap = load(phifin_gap_path)
    trace_boundary = load(trace_boundary_path)
    finite_boundary = load(finite_boundary_path)
    physical_promotion = load(physical_promotion_path)
    rb4_schema = load(rb4_schema_path)
    rb4_payload_schema = load(rb4_payload_schema_path)

    ra2 = {
        "schema": "MTTConstEW02B37RouteARA2BoundarySourceReduction.v1",
        "status": "RA2_FORMAL_BOUNDARY_AND_DEFECT_FUNCTIONAL_SUPPORT_CLOSED_PHYSICAL_PROMOTION_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B37-ROUTEA-RA2-BOUNDARY-SOURCE-CANCELLATION",
        "inputs": {
            "defect_functional_candidate": rel(defect_path),
            "defect_functional_source": rel(defect_source_path),
            "phifin_physical_application_gap": rel(phifin_gap_path),
            "trace_boundary_candidate": rel(trace_boundary_path),
            "finite_trace_boundary_cancellation": rel(finite_boundary_path),
            "physical_promotion_attempt": rel(physical_promotion_path),
        },
        "formal_support_closed": {
            "unique_formal_C1_defect_functional_sourced": defect["what_closes_now"]["unique_formal_C1_defect_functional_sourced"],
            "euler_projection_scale_independence_verified": defect["what_closes_now"]["euler_projection_scale_independence_verified"],
            "algebraic_finite_trace_boundary_cancellation": trace_boundary["what_closes_now"]["algebraic_finite_trace_boundary_cancellation"],
            "finite_trace_boundary_statement": finite_boundary["algebraic_boundary_statement"],
        },
        "physical_promotion_still_open": {
            "physical_PhiFinC1_action_identity": trace_boundary["what_remains_open"]["physical_PhiFinC1_action_identity"],
            "same_source_b_selected_emission": trace_boundary["what_remains_open"]["same_source_b_selected_emission"],
            "absence_of_extra_physical_boundary_or_source_term": trace_boundary["what_remains_open"]["absence_of_extra_physical_boundary_or_source_term"],
            "physical_measure_equals_trace_frobenius_pairing": trace_boundary["what_remains_open"]["physical_measure_equals_trace_frobenius_pairing"],
            "bind_differentiated_PhiFinC1_to_variational_problem": defect["what_remains_open"]["bind_differentiated_PhiFinC1_to_variational_problem"],
        },
        "source_gap_reason": phifin_gap["remaining_physical_application_rule"],
        "route_A_promoted_now": physical_promotion["route_A_promoted_now"],
        "free_axiom_patch_used": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    rb4 = {
        "schema": "MTTConstEW02B37RouteBRB4IndependentSourcePayloadContract.v1",
        "status": "RB4_STRICT_INDEPENDENT_SOURCE_PAYLOAD_CONTRACT_IMPORTED_VALUES_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B37-ROUTEB-RB4-INDEPENDENT-QUADRATURE-SOURCE",
        "inputs": {
            "routeb_schema_candidate": rel(rb4_schema_path),
            "routeb_payload_schema": rel(rb4_payload_schema_path),
        },
        "strict_payload_contract": {
            "basis_rows_are_prerequisites": rb4_payload_schema["basis_rows_are_prerequisites"],
            "required_stage_counts": rb4_payload_schema["required_stage_counts"],
            "required_row_fields": rb4_payload_schema["required_row_fields"],
            "accepted_provenance": rb4_payload_schema["accepted_provenance"],
            "forbidden_provenance": rb4_payload_schema["forbidden_provenance"],
            "validator": rb4_payload_schema["validator"],
        },
        "what_closes_now": rb4_schema["what_closes_now"],
        "what_remains_open": rb4_schema["what_remains_open"],
        "validator_rejects_unfilled_template": rb4_schema["validator_rejects_unfilled_template"],
        "locked_target_values_used_as_source": rb4_schema["locked_target_values_used_as_source"],
        "route_B_independent_quadrature_promoted_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    boundary = {
        "schema": "MTTConstEW02B37Boundary.v1",
        "status": "B37_FORMAL_RA2_SUPPORT_AND_RB4_CONTRACT_BUILT_PHYSICAL_SOURCE_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B37-BOUNDARY",
        "previous_B36": {
            "candidate": b36["candidate"],
            "status": b36["status"],
            "still_open": b36_boundary["still_open"],
        },
        "closed_or_sharpened_now": {
            "RA2_formal_C1_defect_functional_source": True,
            "RA2_finite_trace_algebraic_boundary_cancellation": True,
            "RA2_physical_boundary_source_cancellation_promoted": False,
            "RB4_strict_independent_payload_schema_imported": True,
            "RB4_values_or_source_ids_filled": False,
            "superset_paths_constrained_to_same_locked_C1_target": True,
        },
        "still_open": {
            "physical_PhiFinC1_action_identity": True,
            "same_source_b_selected_emission": True,
            "absence_of_extra_physical_boundary_or_source_term": True,
            "independent_quadrature_exactness_certificate": True,
            "selected_kernel_source_ids": True,
            "110_independent_payload_values": True,
            "selected_source_promotion": True,
            "physical_weak_angle_closure": True,
            "strict_full_no_knob_closure": True,
        },
        "superset_strategy": {
            "straight_way_or_combined": "combined superset paths constrained to one locked C1 source-promotion target",
            "route_A": "formal defect functional plus finite trace boundary cancellation",
            "route_B": "independent quadrature payload schema for 72 primitive, 2 Hessian/source, and 36 sector rows",
            "why_not_knobs": "Both routes must emit source-owned objects before promotion; neither route may tune to observed weak angle or replay residual rows as a source.",
        },
        "anti_cycle_delta_from_B36": {
            "B36": "filled support Hessian/source normal equations and identified RA2/RB4",
            "B37": "imports formal RA2 boundary/source support and strict RB4 payload contract, while preserving the physical/source-open fields",
            "not_repeated": [
                "not another A^T A/A^T b replay",
                "not treating formal finite trace cancellation as physical action identity",
                "not treating the RB4 schema as filled independent values",
            ],
        },
        "allowed_claim": "B37 closes formal RA2 support and imports the strict RB4 independent payload contract.",
        "forbidden_claim": "physical RA2 cancellation, same-source b_selected emission, filled independent quadrature values, physical weak-angle closure, or no-knob closure",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstEW02B37NextWork.v1",
        "status": "NEXT_WORKORDER_PHYSICAL_ACTION_IDENTITY_OR_FILLED_INDEPENDENT_PAYLOAD",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B38-ACTION-IDENTITY-OR-RB4-PAYLOAD-FILL",
        "primary": {
            "label": "CONST-EW-02 / WEAK-MIXING / B38-ROUTEA-PHYSICAL-PHIFINC1-ACTION-IDENTITY",
            "task": "Emit the same-source physical Phi_fin^C1 action identity, same-source b_selected, and no-extra-boundary/source proof binding the formal C1DefectLeakageFunctional to the selected physical variation.",
        },
        "parallel": {
            "label": "CONST-EW-02 / WEAK-MIXING / B38-ROUTEB-FILLED-INDEPENDENT-QUADRATURE-PAYLOAD",
            "task": "Fill the 110 strict payload rows with selected kernel source ids, quadrature rule ids, independent source emission flags, and exactness/error certificates.",
        },
    }

    candidate = {
        "candidate": "MTTConstEW02WeakMixingB37RA2BoundaryOrRB4IndependentSource",
        "status": STATUS,
        "active_label": "CONST-EW-02 / WEAK-MIXING / B37-RA2-BOUNDARY-OR-RB4-INDEPENDENT-SOURCE",
        "output_packets": {
            "route_a_ra2_boundary_source_reduction": rel(RA2),
            "route_b_rb4_independent_source_payload_contract": rel(RB4),
            "weak_mixing_b37_boundary": rel(BOUNDARY),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTEW02B37RA2BoundaryOrRB4IndependentSourceTheorem",
            "proved": True,
            "statement": (
                "For the weak-mixing C1 source frontier, Route A now has the formal C1DefectLeakageFunctional source and algebraic finite-trace boundary cancellation, but physical promotion still requires same-source Phi_fin^C1 action identity, b_selected emission, and proof that no extra physical boundary/source term survives. Route B now has the strict independent quadrature payload schema for 110 non-basis rows, but the independent values, source ids, quadrature rule ids, and exactness certificates remain open."
            ),
        },
        "RA2_formal_boundary_source_support_closed": True,
        "RA2_physical_boundary_source_cancellation_promoted": False,
        "RB4_strict_independent_payload_contract_imported": True,
        "RB4_independent_values_filled": False,
        "source_promotion_closed_now": False,
        "physical_weak_angle_closure": False,
        "strict_full_no_knob_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_EW_02_WeakMixing_B37_RA2_Boundary_or_RB4_IndependentSource_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "RA2_formal_boundary_source_support_closed": True,
        "RA2_physical_boundary_source_cancellation_promoted": False,
        "RB4_strict_independent_payload_contract_imported": True,
        "RB4_independent_values_filled": False,
        "source_promotion_closed_now": False,
        "physical_weak_angle_closure": False,
        "strict_full_no_knob_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_primary": next_work["primary"]["label"],
        "next_parallel": next_work["parallel"]["label"],
    }

    note = f"""# MTT CONST EW 02 Weak Mixing B37 RA2 Boundary or RB4 Independent Source v1

Status: `{STATUS}`

Label: `CONST-EW-02 / WEAK-MIXING / B37-RA2-BOUNDARY-OR-RB4-INDEPENDENT-SOURCE`

## Result

```text
RA-2 formal C1 defect functional source          True
RA-2 finite trace algebraic boundary cancellation True
RA-2 physical boundary/source promotion          False
RB-4 strict independent payload schema imported  True
RB-4 independent values/source ids filled        False
```

## Superset Use

This is a combined superset step constrained to one locked C1 target. Route A
uses the variational/finite-trace encoding; Route B uses the independent
quadrature/source-payload encoding. They are not free knobs: both must emit
source-owned objects before promotion.

## Next

`CONST-EW-02 / WEAK-MIXING / B38-ACTION-IDENTITY-OR-RB4-PAYLOAD-FILL`
"""

    for path, payload in [
        (RA2, ra2),
        (RB4, rb4),
        (BOUNDARY, boundary),
        (NEXT_WORK, next_work),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        write_json(path, payload)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
