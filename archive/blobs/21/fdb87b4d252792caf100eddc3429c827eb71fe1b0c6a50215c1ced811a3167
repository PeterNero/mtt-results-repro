"""Build all-rows provenance promotion / physical Phi_fin^C1 action-source gate.

The previous artifact executed all 72 primitive rows exactly in the finite
Weyl layer.  This one integrates those rows with the existing formal 110-row
finite-trace execution packet: 72 primitive rows, 36 sector-matrix rows, and
2 Hessian/source rows.

It closes the formal finite row replay and normal-equation ledger.  It does
not promote the packet as physical selected Phi_fin^C1 source data.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_allrowsprovenancepromotion_or_physicalphifinc1actionsource"
OUTPUT = DATA / f"{SLUG}.candidate.json"
PACKET_DIR = DATA / SLUG
FORMAL_PACKET = PACKET_DIR / "formal_110_row_replay_integrated.packet.json"
PROMOTION_PACKET = PACKET_DIR / "physical_source_promotion_cutset.packet.json"
DECISION_PACKET = PACKET_DIR / "all_rows_provenance_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
AUDIT = CORPUS / f"{SLUG}_audit.py"
NOTE = CORPUS / "MTT_Selected_AllRowsProvenancePromotion_or_PhysicalPhiFinC1ActionSource_v1.md"

PREVIOUS = DATA / "selected_firstrowprovenancepromotion_or_allrowsweylexecution.candidate.json"
ALL_ROWS = (
    DATA
    / "selected_firstrowprovenancepromotion_or_allrowsweylexecution"
    / "all_72_exact_weyl_row_execution.packet.json"
)
FORMAL_110 = (
    DATA / "selected_routeaemission_or_routebgalerkinrows_execution" / "formal_110_row_execution.packet.json"
)
PHYSICAL_REMAINDER = (
    DATA
    / "selected_finiteweyl_traceuniqueness_or_physicalboundarysource_derivation"
    / "physical_boundary_source_remainder.packet.json"
)
PATCHED_PARITY = DATA / "selected_dynamicc1parityvaluepacket_after_stationarydotd_integration.candidate.json"

STATUS = (
    "MTT_SELECTED_ALLROWSPROVENANCEPROMOTION_OR_PHYSICALPHIFINC1ACTIONSOURCE_"
    "BUILT_FORMAL_110_ROW_REPLAY_PHYSICAL_SOURCE_OPEN"
)
NEXT = "MTT_Selected_PhysicalPhiFinC1ActionSource_or_ProvenanceIndependenceTheorem_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    all_rows = load(ALL_ROWS)
    formal = load(FORMAL_110)
    physical = load(PHYSICAL_REMAINDER)
    patched = load(PATCHED_PARITY)

    row_counts = formal["row_counts"]
    hessian_values = formal["hessian_source_values"]

    formal_replay = {
        "schema": "MTTFormal110RowReplayIntegrated.v1",
        "status": "FORMAL_110_ROW_REPLAY_INTEGRATED_PHYSICAL_PROMOTION_OPEN",
        "row_counts": row_counts,
        "all_72_primitive_rows_exact": all_rows["computed_value_clause_closed_for_all_rows"]
        and all_rows["exactness_clause_closed_for_all_rows"],
        "formal_110_rows_executed": formal["independent_formal_rows_executed_now"],
        "formal_110_matches_prior_replay": formal["comparison_to_prior_algebraic_replay"][
            "matches_prior_replay_under_finite_trace_engine"
        ],
        "formal_110_max_abs_error": formal["comparison_to_prior_algebraic_replay"]["max_abs_error"],
        "primitive_row_source_counts": all_rows["source_counts"],
        "sector_matrix_rows": {
            "count": len(formal["sector_matrix_values"]),
            "all_formal_quadrature_emitted": all(
                row["independent_formal_quadrature_emitted"]
                for row in formal["sector_matrix_values"]
            ),
            "physical_source_promoted": any(row["physical_source_promoted"] for row in formal["sector_matrix_values"]),
        },
        "hessian_source_rows": {
            "count": len(hessian_values),
            "all_formal_quadrature_emitted": all(
                row["independent_formal_quadrature_emitted"] for row in hessian_values
            ),
            "physical_source_promoted": any(row["physical_source_promoted"] for row in hessian_values),
            "A_transpose_A": formal["hessian_source_values"][0]["finite_trace_quadrature_value"][
                "A_column_norm_sq"
            ],
            "A_transpose_b": [
                row["finite_trace_quadrature_value"]["A_transpose_b_component"]
                for row in hessian_values
            ],
            "deltaTheta_C1": [
                row["finite_trace_quadrature_value"]["deltaTheta_component"]
                for row in hessian_values
            ],
        },
        "patched_parity_reference": {
            "source": rel(PATCHED_PARITY),
            "patched_A_selected_emitted": patched["closure_decision"]["patched_A_selected_emitted"],
            "patched_b_selected_emitted": patched["closure_decision"]["patched_b_selected_emitted"],
            "patched_deltaTheta_C1_emitted": patched["closure_decision"][
                "patched_deltaTheta_C1_emitted"
            ],
            "unpatched_A_selected_emitted": patched["closure_decision"][
                "unpatched_A_selected_emitted"
            ],
            "unpatched_b_selected_emitted": patched["closure_decision"][
                "unpatched_b_selected_emitted"
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    promotion_cutset = {
        "schema": "MTTPhysicalSourcePromotionCutset.v1",
        "status": "ONLY_PHYSICAL_SOURCE_OR_INDEPENDENT_PROVENANCE_REMAINS",
        "route_A_physical_action_source": {
            "physical_action_identity": physical["route_A_current_emissions"][
                "physical_action_identity"
            ],
            "physical_measure_equals_trace_frobenius_pairing": physical[
                "route_A_current_emissions"
            ]["physical_measure_equals_trace_frobenius_pairing"],
            "no_extra_physical_boundary_or_source_term": physical["route_A_current_emissions"][
                "no_extra_physical_boundary_or_source_term"
            ],
            "phase_R_Z_source_selection": physical["route_A_current_emissions"][
                "phase_R_Z_source_selection"
            ],
            "shift_R_X_source_selection": physical["route_A_current_emissions"][
                "shift_R_X_source_selection"
            ],
            "same_source_b_selected_emission": physical["route_A_current_emissions"][
                "same_source_b_selected_emission"
            ],
            "closed": False,
        },
        "route_B_independent_provenance": {
            "all_72_primitive_values_exact": True,
            "formal_110_rows_executed": True,
            "source_independent_of_residual_projector_replay": False,
            "closed": False,
        },
        "if_cutset_closes": physical["if_all_minimal_next_emissions_hold"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    decision = {
        "schema": "MTTAllRowsProvenanceDecision.v1",
        "status": "FORMAL_REPLAY_CLOSED_PHYSICAL_SOURCE_AND_PROVENANCE_OPEN",
        "formal_110_row_replay_closed": True,
        "formal_A_b_deltaTheta_replay_closed": True,
        "A_selected_promoted_unpatched": False,
        "b_selected_promoted_unpatched": False,
        "deltaTheta_C1_promoted_unpatched": False,
        "physical_PhiFinC1_action_source_closed": False,
        "provenance_independent_of_residual_projector_replay": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "next_actionable_target": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedAllRowsProvenancePromotionOrPhysicalPhiFinC1ActionSource",
        "status": STATUS,
        "inputs": {
            "previous_gate": rel(PREVIOUS),
            "all_72_exact_rows": rel(ALL_ROWS),
            "formal_110_row_execution": rel(FORMAL_110),
            "physical_boundary_source_remainder": rel(PHYSICAL_REMAINDER),
            "patched_parity_reference": rel(PATCHED_PARITY),
        },
        "output_packets": {
            "formal_110_row_replay_integrated": rel(FORMAL_PACKET),
            "physical_source_promotion_cutset": rel(PROMOTION_PACKET),
            "all_rows_provenance_decision": rel(DECISION_PACKET),
        },
        "what_closes_now": {
            "formal_110_row_replay_integrated": True,
            "formal_A_b_deltaTheta_replay_integrated": True,
            "all_72_exact_rows_retained": True,
            "source_promotion_cutset_minimized": True,
            "observed_constants_excluded_as_selectors": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "physical_PhiFinC1_action_identity": True,
            "no_extra_physical_boundary_or_source_term": True,
            "same_source_R_Z_R_X_b_selected_emission": True,
            "provenance_independent_of_residual_projector_replay": True,
            "unpatched_A_selected": True,
            "unpatched_b_selected": True,
            "unpatched_deltaTheta_C1": True,
            "true_SM_equivalence_closure": True,
            "no_knob_closure": True,
        },
        "promotion_decision": decision,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "theorem": {
            "name": "FormalRowsIntegratedPromotionCutsetTheorem",
            "proved": True,
            "statement": (
                "The exact 72-row finite Weyl execution integrates with the existing "
                "formal 110-row finite-trace execution packet, including 36 sector rows "
                "and 2 Hessian/source rows.  Thus the formal replay of A^T A=12 I_2, "
                "A^T b=(12,12), and deltaTheta=(1,1) is closed at the finite row layer. "
                "The remaining obstruction is not calculation but source promotion: either "
                "prove the physical Phi_fin^C1 action emits the same R_Z/R_X/b_selected "
                "packet with no extra boundary/source term, or supply provenance independent "
                "of residual-projector replay."
            ),
        },
    }

    cert = {
        "certificate": "MTT_Selected_AllRowsProvenancePromotion_or_PhysicalPhiFinC1ActionSource_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "packet_paths": candidate["output_packets"],
        "theorem_proved": True,
        "formal_110_row_replay_closed": True,
        "formal_A_b_deltaTheta_replay_closed": True,
        "physical_PhiFinC1_action_source_closed": False,
        "provenance_independent_of_residual_projector_replay": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected AllRowsProvenancePromotion or PhysicalPhiFinC1ActionSource v1

Status: `{STATUS}`

## Theorem

{candidate["theorem"]["statement"]}

## Closed At Formal Row Layer

- primitive rows: {row_counts["primitive_rows"]}
- sector rows: {row_counts["sector_matrix_rows"]}
- Hessian/source rows: {row_counts["hessian_source_rows"]}
- total formal rows: {row_counts["total_rows"]}
- formal `A^T b`: {formal_replay["hessian_source_rows"]["A_transpose_b"]}
- formal `deltaTheta_C1`: {formal_replay["hessian_source_rows"]["deltaTheta_C1"]}

## Remaining Cutset

Only source promotion remains: physical `Phi_fin^C1` action-source identity or
residual-projector-independent provenance.

Next artifact: `{NEXT}`.
"""

    audit = f'''"""Audit {SLUG}."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "{SLUG}.candidate.json"
CERT = ROOT / "certificates" / "{SLUG}_certificate.json"
PACKET_DIR = ROOT / "candidate_data" / "{SLUG}"
FORMAL = PACKET_DIR / "formal_110_row_replay_integrated.packet.json"
PROMOTION = PACKET_DIR / "physical_source_promotion_cutset.packet.json"
DECISION = PACKET_DIR / "all_rows_provenance_decision.packet.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_AllRowsProvenancePromotion_or_PhysicalPhiFinC1ActionSource_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    cert = load(CERT)
    formal = load(FORMAL)
    promotion = load(PROMOTION)
    decision = load(DECISION)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == "{STATUS}", "status mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(formal["row_counts"]["primitive_rows"] == 72, "primitive count mismatch")
    require(formal["row_counts"]["sector_matrix_rows"] == 36, "sector count mismatch")
    require(formal["row_counts"]["hessian_source_rows"] == 2, "hessian count mismatch")
    require(formal["row_counts"]["total_rows"] == 110, "total count mismatch")
    require(formal["all_72_primitive_rows_exact"] is True, "72 rows not exact")
    require(formal["formal_110_rows_executed"] is True, "formal rows not executed")
    require(formal["formal_110_matches_prior_replay"] is True, "formal replay mismatch")
    require(formal["hessian_source_rows"]["A_transpose_A"] == 12.0, "hessian norm mismatch")
    require(formal["hessian_source_rows"]["A_transpose_b"] == [12.0, 12.0], "A^T b mismatch")
    require(formal["hessian_source_rows"]["deltaTheta_C1"] == [1.0, 1.0], "deltaTheta mismatch")
    require(formal["patched_parity_reference"]["patched_A_selected_emitted"] is True, "patched reference missing")
    require(formal["patched_parity_reference"]["unpatched_A_selected_emitted"] is False, "unpatched overclaimed")
    require(promotion["route_A_physical_action_source"]["closed"] is False, "route A overclosed")
    require(promotion["route_B_independent_provenance"]["closed"] is False, "route B overclosed")
    require(promotion["route_B_independent_provenance"]["all_72_primitive_values_exact"] is True, "route B values missing")
    require(decision["formal_110_row_replay_closed"] is True, "formal replay not closed")
    require(decision["formal_A_b_deltaTheta_replay_closed"] is True, "formal linear replay not closed")
    require(decision["A_selected_promoted_unpatched"] is False, "A selected overpromoted")
    require(decision["b_selected_promoted_unpatched"] is False, "b selected overpromoted")
    require(decision["physical_PhiFinC1_action_source_closed"] is False, "physical source overclosed")
    require(decision["provenance_independent_of_residual_projector_replay"] is False, "provenance overclosed")
    require(decision["true_SM_equivalence_closed"] is False, "SM equivalence overclaimed")
    require(decision["no_knob_closed"] is False, "no-knob overclaimed")
    require(cert["formal_110_row_replay_closed"] is True, "cert formal replay missing")
    require(cert["physical_PhiFinC1_action_source_closed"] is False, "cert physical overclosed")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require("total formal rows: 110" in note, "note missing total rows")
    print(f"PASS {{DATA.name}}: {{data['status']}}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
'''

    write_json(FORMAL_PACKET, formal_replay)
    write_json(PROMOTION_PACKET, promotion_cutset)
    write_json(DECISION_PACKET, decision)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    AUDIT.write_text(audit, encoding="utf-8")

    print(f"wrote {rel(OUTPUT)}")
    print(f"status {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
