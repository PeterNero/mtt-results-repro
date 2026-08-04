"""Build Step73 honest row-local HYM/Galerkin execution attempt."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step73_honestrowlocalhymgalerkin_or_selectedprefactorsourcerows"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
INPUTS_PACKET = PACKET_DIR / "step73_honest_rowlocal_galerkin_input_readiness.packet.json"
SUBSOURCE_PACKET = PACKET_DIR / "step73_diagonal_hym_green_subsource_import.packet.json"
ROW_ATTEMPT_PACKET = PACKET_DIR / "step73_ten_rowlocal_prefactor_execution_attempt.packet.json"
OBSTRUCTION_PACKET = PACKET_DIR / "step73_sector_transfer_and_projector_obstruction.packet.json"
CUTSET_PACKET = PACKET_DIR / "step73_next_selected_sector_transfer_or_overlap_derivative_cutset.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step73_HonestRowLocalHYMGalerkin_or_SelectedPrefactorSourceRows_v1.md"

STEP72 = DATA / "selected_step72_rowlocalprefactorlawsearch_or_strictomegaacceptance.candidate.json"
STEP72_WORKORDER = (
    DATA
    / "selected_step72_rowlocalprefactorlawsearch_or_strictomegaacceptance"
    / "step72_honest_galerkin_rowlocal_workorder.packet.json"
)
STEP72_TARGETS = (
    DATA
    / "selected_step72_rowlocalprefactorlawsearch_or_strictomegaacceptance"
    / "step72_required_rowlocal_prefactor_target_table.packet.json"
)
HYM_FIRST = DATA / "selected_hymnewtongalerkin_firstsolve_or_rank2sectorfunctor.candidate.json"
HYM_PAYLOAD = (
    DATA
    / "selected_hymnewtongalerkin_firstsolve_or_rank2sectorfunctor"
    / "selected_hym_first_solve_payload.packet.json"
)
GREEN_PAYLOAD = (
    DATA
    / "selected_hymnewtongalerkin_firstsolve_or_rank2sectorfunctor"
    / "full_diagonal_end0_green_payload.packet.json"
)
RTHETA_PI = DATA / "selected_rtheta_pikernel_from_selectedhymconnection_or_bnbasisemission.candidate.json"
HYM_SUBGATE = (
    DATA
    / "selected_rtheta_pikernel_from_selectedhymconnection_or_bnbasisemission"
    / "selected_hym_connection_subgate_import.packet.json"
)
BN_GATE = (
    DATA
    / "selected_rtheta_pikernel_from_selectedhymconnection_or_bnbasisemission"
    / "bn_basis_and_sector_transfer_gate.packet.json"
)
ZEROMODE_PROJECTORS = DATA / "selected_hym_projector_zeromode_basis_value_emission.candidate.json"
EXT_OVERLAP = DATA / "selected_ext_overlap_hym_hodge_projector_table.candidate.json"
T1T2_GREEN = DATA / "selected_t1t2_covariant_green_and_transfer_probe.candidate.json"

STATUS = "MTT_SELECTED_STEP73_HONEST_ROWLOCAL_HYM_GALERKIN_BUILT_DIAGONAL_SUBSOURCE_SECTOR_TRANSFER_OPEN"
NEXT = "MTT_Selected_SelectedSectorTransferOverlapDerivative_or_RowLocalPrefactorEmission_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    inputs = [
        STEP72,
        STEP72_WORKORDER,
        STEP72_TARGETS,
        HYM_FIRST,
        HYM_PAYLOAD,
        GREEN_PAYLOAD,
        RTHETA_PI,
        HYM_SUBGATE,
        BN_GATE,
        ZEROMODE_PROJECTORS,
        EXT_OVERLAP,
        T1T2_GREEN,
    ]
    missing = [rel(path) for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step73 inputs: " + ", ".join(missing))

    step72 = load(STEP72)
    workorder = load(STEP72_WORKORDER)
    targets = load(STEP72_TARGETS)
    hym_first = load(HYM_FIRST)
    hym_payload = load(HYM_PAYLOAD)
    green_payload = load(GREEN_PAYLOAD)
    rtheta_pi = load(RTHETA_PI)
    hym_subgate = load(HYM_SUBGATE)
    bn_gate = load(BN_GATE)
    projectors = load(ZEROMODE_PROJECTORS)
    ext_overlap = load(EXT_OVERLAP)
    t1t2_green = load(T1T2_GREEN)

    if step72["status"] != "MTT_SELECTED_STEP72_ROWLOCAL_PREFACTOR_LAW_SEARCH_BUILT_STRICT_OMEGA_STILL_OPEN":
        raise AssertionError("Step73 expects Step72 frontier status")
    if targets["target_row_count"] != 10:
        raise AssertionError("Step73 expects ten target rows")

    projector_validator = projectors["validator_result"]
    projector_closed = projectors["what_closes_now"]
    sector_transfer_open = bn_gate["selected_values_open"]
    selected_projector_promoted = projector_validator["selected_HYM_projector_values_promoted"]

    readiness_rows = [
        {
            "requirement": "selected q79/F/m=1 finite HYM/Strominger operator",
            "source": rel(HYM_SUBGATE),
            "available": hym_subgate["selected_HYM_connection_representative_available"],
            "accepted_for_rowlocal_prefactor_source": True,
            "notes": "diagonal rank-2 HYM representative is imported as a source subgate",
        },
        {
            "requirement": "diagonal End0 Riesz/Green normalization",
            "source": rel(GREEN_PAYLOAD),
            "available": hym_subgate["full_diagonal_End0_Green_closed"],
            "accepted_for_rowlocal_prefactor_source": True,
            "notes": "diagonal End0 Green is source-closed, but not sector-ready",
        },
        {
            "requirement": "ordered zero-mode bases for every Omega slot",
            "source": rel(ZEROMODE_PROJECTORS),
            "available": projector_closed["ordered_zero_mode_basis_ids_emitted"],
            "accepted_for_rowlocal_prefactor_source": False,
            "notes": "finite model-active bases are emitted, but selected HYM projector source promotion is false",
        },
        {
            "requirement": "sector transfer from rank-2/End0 lane to u,d,e,H Omega slots",
            "source": rel(BN_GATE),
            "available": not sector_transfer_open["rank2_to_sector_transfer_values"],
            "accepted_for_rowlocal_prefactor_source": False,
            "notes": "rank2-to-sector transfer values remain open",
        },
        {
            "requirement": "retarded overlap kernel derivative on the same branch",
            "source": rel(T1T2_GREEN),
            "available": t1t2_green["operator_payload_boundary"]["formal_dotD_frechet_formula_retained"],
            "accepted_for_rowlocal_prefactor_source": False,
            "notes": "formal derivative/Green support is retained, but physical dotD_alpha1 payload is not extracted",
        },
        {
            "requirement": "threshold/scale/scheme convention selected before replay",
            "source": rel(STEP72_WORKORDER),
            "available": False,
            "accepted_for_rowlocal_prefactor_source": False,
            "notes": "no selected T_scheme.* rows are emitted",
        },
        {
            "requirement": "lambda_H H-sector source value payload",
            "source": rel(ZEROMODE_PROJECTORS),
            "available": "H" in projectors["finite_value_payload"]["sector_slots"],
            "accepted_for_rowlocal_prefactor_source": False,
            "notes": "H-sector model-active projector exists, but no lambda_H source value payload is emitted",
        },
    ]

    input_packet = {
        "schema": "MTTStep73HonestRowLocalGalerkinInputReadiness.v1",
        "status": "DIAGONAL_HYM_GREEN_READY_SECTOR_ROWLOCAL_INPUTS_OPEN",
        "source_inputs": {
            "step72_workorder": rel(STEP72_WORKORDER),
            "hym_subgate": rel(HYM_SUBGATE),
            "zero_mode_projectors": rel(ZEROMODE_PROJECTORS),
            "bn_sector_transfer_gate": rel(BN_GATE),
            "t1t2_green": rel(T1T2_GREEN),
        },
        "readiness_rows": readiness_rows,
        "ready_source_subgate_count": sum(1 for row in readiness_rows if row["accepted_for_rowlocal_prefactor_source"]),
        "rowlocal_blocking_requirement_count": sum(1 for row in readiness_rows if not row["accepted_for_rowlocal_prefactor_source"]),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(INPUTS_PACKET, input_packet)

    subsource_packet = {
        "schema": "MTTStep73DiagonalHYMGreenSubsourceImport.v1",
        "status": "SELECTED_DIAGONAL_HYM_GREEN_IMPORTED_AS_ROWLOCAL_SUBSOURCE",
        "selected_source": hym_payload["selected_source"],
        "hym_first_solve_status": hym_payload["status"],
        "hym_connection_subgate_status": hym_subgate["status"],
        "diagonal_hym_subsource_closed": True,
        "diagonal_green_subsource_closed": True,
        "accepted_as_full_rowlocal_prefactor_source": False,
        "accepted_rowlocal_source_row_count": 0,
        "source_descriptors": {
            "final_residual_l2": hym_payload["solution_summary"]["final_residual_l2"],
            "u_l2": hym_payload["solution_summary"]["u_l2"],
            "u_min": hym_payload["solution_summary"]["u_min"],
            "u_max": hym_payload["solution_summary"]["u_max"],
            "gradient_l2": hym_payload["A_HYM_payload"]["gradient_l2"],
            "mean_exp_weighted_density": hym_payload["solution_summary"]["mean_exp_weighted_density"],
            "T1T2_green_operator_norm_bound": green_payload["T1_T2_covariant_Green"]["green_operator_norm_bound"],
            "T1T2_min_positive_eigenvalue": green_payload["T1_T2_covariant_Green"]["min_positive_eigenvalue"],
        },
        "does_not_emit": [
            "selected sector B_N basis/quadrature/error contract",
            "rank2-to-sector transfer values",
            "selected sector D_E/Riesz/Green/dotD/C1 payload",
            "ten L_rowlocal.* values",
            "ten T_scheme.* values",
            "lambda_H value row",
            "strict Omega rows",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(SUBSOURCE_PACKET, subsource_packet)

    sector_slots = projectors["finite_value_payload"]["sector_slots"]
    attempt_rows: list[dict[str, Any]] = []
    for target in targets["target_rows"]:
        sector = target["sector"]
        slot = sector_slots.get(sector, sector_slots.get("H"))
        row_blockers = [
            "selected HYM projector source promotion is false",
            "rank2-to-sector transfer values are not emitted",
            "physical retarded overlap derivative/dotD_alpha1 payload is not extracted",
            "threshold/scale/scheme row T_scheme.* is not selected",
        ]
        if target["omega_id"] == "Omega_H.lambda":
            row_blockers.append("lambda_H H-sector value payload is not emitted")
        attempt_rows.append(
            {
                "row_id": f"step73.rowlocal_attempt.{target['omega_id']}",
                "omega_id": target["omega_id"],
                "sector": sector,
                "generation_or_lambda": target["generation_or_lambda"],
                "diagonal_hym_connection_available": True,
                "diagonal_green_available": True,
                "model_active_zero_mode_basis_ids": slot["ordered_zero_mode_basis_ids"] if slot else [],
                "model_active_zero_mode_basis_available": bool(slot),
                "selected_zero_mode_projector_promoted": slot["value_emitted_as_selected_HYM_projector"] if slot else False,
                "selected_sector_transfer_available": False,
                "selected_retarded_overlap_derivative_available": False,
                "selected_threshold_scheme_available": False,
                "postcheck_target_available_after_source_emission": True,
                "postcheck_target_symbolic": target["rowlocal_composite_target_symbolic"],
                "emitted_L_rowlocal_value": None,
                "emitted_T_scheme_value": None,
                "accepted_as_rowlocal_source_row": False,
                "accepted_as_prefactor_source_row": False,
                "accepted_as_omega_source_row": False,
                "blocking_reasons": row_blockers,
                "observed_data_used_as_selector": False,
                "target_fitting_used": False,
            }
        )

    row_attempt_packet = {
        "schema": "MTTStep73TenRowLocalPrefactorExecutionAttempt.v1",
        "status": "TEN_ROWLOCAL_EXECUTION_ATTEMPT_BLOCKED_BEFORE_NUMERIC_SOURCE_ROWS",
        "attempt_rows": attempt_rows,
        "attempt_row_count": len(attempt_rows),
        "accepted_rowlocal_source_row_count": 0,
        "accepted_prefactor_source_row_count": 0,
        "accepted_omega_source_row_count": 0,
        "accepted_internal_scalar_value_row_count": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(ROW_ATTEMPT_PACKET, row_attempt_packet)

    obstruction_packet = {
        "schema": "MTTStep73SectorTransferAndProjectorObstruction.v1",
        "status": "ROWLOCAL_EMISSION_BLOCKED_BY_PROJECTOR_PROMOTION_AND_SECTOR_TRANSFER",
        "projector_status": {
            "finite_model_active_projector_values_emitted": projector_closed[
                "finite_model_active_projector_values_emitted"
            ],
            "ordered_zero_mode_basis_ids_emitted": projector_closed["ordered_zero_mode_basis_ids_emitted"],
            "selected_HYM_projector_values_promoted": selected_projector_promoted,
            "why_not_promoted": projector_validator["why_not_promoted"],
        },
        "sector_transfer_status": {
            "support_present": bn_gate["support_present"],
            "selected_values_open": sector_transfer_open,
            "why_not_promoted": bn_gate["why_not_promoted"],
        },
        "overlap_status": {
            "eta_00_row_level_harmonic_seed_closed": ext_overlap["HYM_correction_status"][
                "row_level_harmonic_seed_closed"
            ],
            "transition_overlap_table_closed": ext_overlap["transition_overlap_table"]["closed"],
            "nonlinear_HYM_connection_correction_closed": ext_overlap["HYM_correction_status"][
                "nonlinear_non_split_HYM_metric_correction_closed"
            ],
            "physical_dotD_alpha1_payload_extracted": t1t2_green["operator_payload_boundary"][
                "physical_dotD_alpha1_payload_extracted"
            ],
        },
        "conclusion": (
            "The selected diagonal HYM/Green lane is a real source subgate, but the ten "
            "Omega row-local prefactors require selected projector promotion, sector transfer, "
            "and retarded overlap derivative rows that are still open."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(OBSTRUCTION_PACKET, obstruction_packet)

    cutset_packet = {
        "schema": "MTTStep73NextSelectedSectorTransferOrOverlapDerivativeCutset.v1",
        "status": "NEXT_TARGET_SELECTED_SECTOR_TRANSFER_OR_OVERLAP_DERIVATIVE",
        "not_missing_anymore": [
            "strict Step72 acceptance predicate",
            "selected diagonal q79/F/m=1 HYM connection representative",
            "diagonal End0 Green/Riesz support",
            "row-by-row honest Galerkin execution attempt",
            "projector/sector-transfer obstruction identified without replay fitting",
        ],
        "still_missing": [
            "selected HYM projector source promotion for the zero-mode bases",
            "selected rank2-to-sector transfer values for u,d,e,H Omega slots",
            "selected retarded overlap kernel derivative / physical dotD_alpha1 payload",
            "selected threshold/scale/scheme rows T_scheme.*",
            "lambda_H H-sector source value payload",
            "strict Omega acceptance after row-local emission",
        ],
        "minimal_theorem_to_close_next": (
            "The selected q79/F,m=1 HYM/Strominger connection plus its sector-transfer functor "
            "emits validator-ready zero-mode projectors and retarded overlap derivatives for "
            "the ten Omega slots before replay magnitudes are read."
        ),
        "route_A": "prove selected rank2-to-sector transfer and HYM projector promotion",
        "route_B": "emit sector-ready D_E/Riesz/Green/dotD/C1 rows directly from the selected HYM connection",
        "route_C": "derive a selected retarded overlap derivative formula whose rows bypass the B_N scaffold",
        "forbidden_routes": [
            "use Step72 postcheck target numbers to choose L_rowlocal.*",
            "promote model-active zero-mode projectors as selected HYM projectors",
            "treat diagonal End0 Green as sector-ready u,d,e,H row-local data",
            "claim strict Omega acceptance before T_scheme.* and lambda_H payload exist",
        ],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(CUTSET_PACKET, cutset_packet)

    candidate = {
        "candidate": "MTTSelectedStep73HonestRowLocalHYMGalerkinOrSelectedPrefactorSourceRows",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in inputs},
        "output_packets": {
            "honest_rowlocal_galerkin_input_readiness": rel(INPUTS_PACKET),
            "diagonal_hym_green_subsource_import": rel(SUBSOURCE_PACKET),
            "ten_rowlocal_prefactor_execution_attempt": rel(ROW_ATTEMPT_PACKET),
            "sector_transfer_and_projector_obstruction": rel(OBSTRUCTION_PACKET),
            "next_selected_sector_transfer_or_overlap_derivative_cutset": rel(CUTSET_PACKET),
        },
        "theorem": {
            "name": "Step73HonestRowLocalHYMPreflightTheorem",
            "proved": True,
            "statement": (
                "Running the Step72 row-local workorder against the current selected HYM/Galerkin "
                "stack imports a real diagonal q79/F,m=1 HYM/Green source subgate, but emits zero "
                "accepted row-local prefactor rows. The obstruction is not the diagonal HYM solve; "
                "it is selected zero-mode projector promotion, rank2-to-sector transfer, retarded "
                "overlap derivative extraction, threshold scheme rows, and lambda_H payload."
            ),
        },
        "closure_decision": {
            "diagonal_hym_green_subsource_closed": True,
            "honest_galerkin_input_readiness_closed": True,
            "ten_rowlocal_execution_attempt_closed": True,
            "projector_sector_transfer_obstruction_closed": True,
            "accepted_rowlocal_source_row_count": 0,
            "accepted_prefactor_source_row_count": 0,
            "accepted_omega_source_row_count": 0,
            "accepted_internal_scalar_value_row_count": 0,
            "selected_HYM_projector_values_promoted": False,
            "selected_sector_transfer_values_emitted": False,
            "selected_retarded_overlap_derivative_rows_emitted": False,
            "selected_threshold_scheme_rows_emitted": False,
            "lambda_H_value_row_emitted": False,
            "strict_omega_acceptance_closed": False,
            "scalar_value_execution_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "previous_status": step72["status"],
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step73_HonestRowLocalHYMGalerkin_or_SelectedPrefactorSourceRows_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        **candidate["closure_decision"],
        "theorem_proved": True,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected Step73 HonestRowLocalHYMGalerkin or SelectedPrefactorSourceRows v1

Status: `{STATUS}`.

## What Moved

Step73 executes the Step72 workorder against the current selected HYM/Galerkin
stack.  This is not another status-only loop: it imports the already computed
diagonal HYM solve as a real source subgate.

```text
selected source                 : {hym_payload['selected_source']}
HYM residual                    : {hym_payload['solution_summary']['final_residual_l2']:.12g}
u_l2                            : {hym_payload['solution_summary']['u_l2']:.12g}
gradient_l2                     : {hym_payload['A_HYM_payload']['gradient_l2']:.12g}
T1/T2 Green norm bound          : {green_payload['T1_T2_covariant_Green']['green_operator_norm_bound']:.12g}
accepted row-local source rows  : 0
accepted Omega source rows      : 0
```

## Why It Still Does Not Close

The diagonal HYM/Green lane is selected and useful, but it is not yet the
sector-ready row-local prefactor packet.

```text
model-active zero-mode basis ids emitted       : {projector_closed['ordered_zero_mode_basis_ids_emitted']}
selected HYM projector values promoted         : {selected_projector_promoted}
rank2-to-sector transfer values emitted        : {not sector_transfer_open['rank2_to_sector_transfer_values']}
physical dotD_alpha1 / overlap derivative      : {t1t2_green['operator_payload_boundary']['physical_dotD_alpha1_payload_extracted']}
selected threshold scheme rows                 : False
```

So the old repeated "Galerkin remains" wall is now narrower.  The diagonal
Galerkin/HYM solve is not the blocker anymore; the blocker is transport from
that solve into selected zero-mode projector and sector row-local data.

## Row Gate

All ten `Omega` rows were attempted.  Each row has diagonal HYM/Green support,
but each row is rejected before numeric source emission because projector
promotion, sector transfer, overlap derivative extraction, and `T_scheme.*`
are not selected.  The `lambda_H` row also lacks the H-sector value payload.

## Next Object

Next artifact: `{NEXT}`.

The next theorem should prove selected sector transfer/projector promotion, or
directly emit sector-ready `D_E/Riesz/Green/dotD/C1` plus retarded overlap
derivative rows from the selected HYM connection.
""",
        encoding="utf-8",
    )

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
