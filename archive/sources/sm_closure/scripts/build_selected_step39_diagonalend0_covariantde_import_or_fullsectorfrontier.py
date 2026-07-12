"""Build Step 39 diagonal End0 covariant D_E import and full-sector frontier."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step39_diagonalend0_covariantde_import_or_fullsectorfrontier"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
IMPORT = PACKET_DIR / "step39_diagonal_end0_covariant_de_import.packet.json"
FRONTIER = PACKET_DIR / "step39_full_sector_operator_frontier.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step39_DiagonalEnd0CovariantDEImport_or_FullSectorFrontier_v1.md"

STEP38 = DATA / "selected_step38_finiteheisenberg_rhoe_promotion_or_deoperatorfrontier.candidate.json"
END0_DE = DATA / "selected_end0_de_payload_from_diagonal_hym.candidate.json"
GAUGE_TRACE = DATA / "selected_gauge_transported_bn_phifin_trace.candidate.json"
TRANSPORT_VALIDATOR = DATA / "selected_transport_conjugation_validator_replay.candidate.json"
PROJECTOR_PROMOTION = DATA / "selected_finite_projector_source_promotion.candidate.json"

STATUS = "MTT_SELECTED_STEP39_DIAGONAL_END0_COVARIANT_DE_IMPORTED_FULL_SECTOR_VALUES_OPEN"
NEXT = "MTT_Selected_FullSectorDE_DotD_ZeroModeC1_From_DiagonalEnd0Transport_v1"


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

    inputs = [STEP38, END0_DE, GAUGE_TRACE, TRANSPORT_VALIDATOR, PROJECTOR_PROMOTION]
    missing = [rel(path) for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step 39 inputs: " + ", ".join(missing))

    step38 = load(STEP38)
    end0 = load(END0_DE)
    gauge_trace = load(GAUGE_TRACE)
    transport = load(TRANSPORT_VALIDATOR)
    projector = load(PROJECTOR_PROMOTION)

    end0_boundary = end0["operator_payload_boundary"]
    end0_import_checks = {
        "step38_projective_rhoe_closed": step38["closure_decision"][
            "operator_level_projective_rhoE_transition_matrices_closed"
        ]
        is True,
        "diagonal_end0_de_formula_extracted": end0_boundary["diagonal_End0_D_E_formula_extracted"] is True,
        "end0_adjoint_basis_typed": end0["selected_End0_basis"]["basis"] == ["T1", "T2", "T3"],
        "ad_T3_matrix_correct": end0["adjoint_connection_packet"]["ad_T3_matrix_on_basis_T1_T2_T3"]
        == [[0, -1, 0], [1, 0, 0], [0, 0, 0]],
        "central_shared_circle_preserved": end0["what_closes_now"]["central_shared_circle_zero_direction_preserved"]
        is True,
        "gauge_transport_phi_fin_trace_closed": gauge_trace["what_closes_now"]["gauge_transported_PhiFin_trace"]
        is True,
        "stationary_riesz_green_transport_verified": transport["what_closes_now"][
            "selected_riesz_green_source_verified"
        ]
        is True,
        "finite_stationary_projector_source_promoted": projector["what_closes_now"][
            "selected_projector_source_verified"
        ]
        is True,
        "dotd_excluded_by_transport_derivative_guard": transport["what_remains_open"][
            "selected_dotD_alpha1_with_transport_derivative"
        ]
        is True,
        "no_target_fitting": step38["target_fitting_used"] is False
        and end0["target_fitting_used"] is False
        and transport["target_fitting_used"] is False,
    }
    diagonal_end0_de_closes = all(end0_import_checks.values())

    import_packet = {
        "schema": "MTTStep39DiagonalEnd0CovariantDEImport.v1",
        "status": "DIAGONAL_END0_COVARIANT_DE_AND_STATIONARY_TRANSPORT_IMPORTED",
        "inputs": {
            "step38_rhoe": rel(STEP38),
            "diagonal_end0_de": rel(END0_DE),
            "gauge_transported_phi_fin_trace": rel(GAUGE_TRACE),
            "transport_conjugation_validator": rel(TRANSPORT_VALIDATOR),
            "finite_projector_source_promotion": rel(PROJECTOR_PROMOTION),
        },
        "proof_checks": end0_import_checks,
        "selected_diagonal_end0_operator": {
            "carrier": end0["selected_End0_basis"]["carrier"],
            "basis": end0["selected_End0_basis"]["basis"],
            "rank": end0["selected_End0_basis"]["rank"],
            "connection_formula": end0["adjoint_connection_packet"]["induced_End0_connection"],
            "D_E_formula": "D_E = d + du ad(T3)",
            "ad_T3_matrix": end0["adjoint_connection_packet"]["ad_T3_matrix_on_basis_T1_T2_T3"],
            "active_directions": list(end0["D_E_direction_payload"].keys()),
        },
        "stationary_transport_payload": {
            "gauge_transport_trace_closed": gauge_trace["what_closes_now"]["gauge_transported_PhiFin_trace"],
            "selected_functional_zero_mode_bases": gauge_trace["what_closes_now"][
                "selected_functional_zero_mode_bases"
            ],
            "selected_projector_source_verified": projector["what_closes_now"][
                "selected_projector_source_verified"
            ],
            "selected_riesz_green_source_verified": transport["what_closes_now"][
                "selected_riesz_green_source_verified"
            ],
            "dotD_excluded_reason": "dotD_alpha1 requires differentiating the transport U and is not closed by stationary conjugation.",
        },
        "closure_result": {
            "selected_diagonal_End0_covariant_D_E_closed": diagonal_end0_de_closes,
            "selected_stationary_projector_Riesz_Green_transport_closed": diagonal_end0_de_closes,
            "selected_full_sector_covariant_D_E_matrices_closed": False,
            "rank2_to_rank3_sector_transfer_values_closed": False,
            "offdiagonal_End0_control_closed": False,
            "same_branch_dotD_alpha1_values_closed": False,
            "coherent_spectral_zero_mode_projectors_closed": False,
            "primitive_C1_contractions_from_operator_values_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "target_fitting_used": False,
        "observed_data_used_as_selector": False,
    }
    write_json(IMPORT, import_packet)

    frontier = {
        "schema": "MTTStep39FullSectorOperatorFrontier.v1",
        "status": "DIAGONAL_END0_LANE_CLOSED_FULL_SECTOR_OPERATOR_VALUES_OPEN",
        "closed_now": {
            "selected_S3_class_and_qutrit_rhoE": True,
            "finite_trace_DE_gap_Riesz_Green_layer": True,
            "operator_level_projective_rhoE_transition_matrices": True,
            "diagonal_End0_covariant_D_E_lane": diagonal_end0_de_closes,
            "stationary_projector_Riesz_Green_transport_lane": diagonal_end0_de_closes,
        },
        "still_missing_for_full_sector_values": {
            "rank2_to_rank3_sector_transfer_values": True,
            "offdiagonal_End0_vanish_or_control_bound": True,
            "selected_finite_derivative_basis_for_validator": True,
            "full_sector_covariant_D_E_matrices_Q_u_d_L_e_N_H": True,
            "same_branch_dotD_alpha1_with_transport_derivative": True,
            "coherent_spectral_zero_mode_projectors": True,
            "primitive_C1_overlap_contractions": True,
            "internal_R_theta_scalar_rows": True,
        },
        "next_required_payload": {
            "target": NEXT,
            "minimum_fields": [
                "sector-transfer map from diagonal End0 lane to Q,u,d,L,e,N,H operator bases",
                "offdiagonal End0 control or exact vanish theorem",
                "finite derivative basis accepted by the validators",
                "dotD_alpha1 including derivative of U=exp(-u ad(T3))",
                "coherent zero-mode projectors in the transported sector bases",
                "primitive C1 contractions from the transported D_E/Green/dotD packet",
            ],
        },
        "accepted_internal_scalar_row_count": 0,
        "target_fitting_used": False,
        "observed_data_used_as_selector": False,
    }
    write_json(FRONTIER, frontier)

    candidate = {
        "candidate": "MTTSelectedStep39DiagonalEnd0CovariantDEImportOrFullSectorFrontier",
        "status": STATUS,
        "inputs": import_packet["inputs"],
        "output_packets": {
            "diagonal_end0_covariant_de_import": rel(IMPORT),
            "full_sector_operator_frontier": rel(FRONTIER),
        },
        "theorem": {
            "name": "Step39DiagonalEnd0CovariantDEImportTheorem",
            "proved": diagonal_end0_de_closes,
            "statement": (
                "Given the Step38 selected projective rho_E gauge class, the selected diagonal "
                "rank-two HYM replay induces the diagonal End0 covariant operator "
                "D_E=d+du ad(T3), with central shared-circle directions preserved. The existing "
                "gauge-transport Phi_fin trace and transport-conjugation validator import the "
                "stationary projector/Riesz/Green lane. This does not close full sector D_E, "
                "dotD, coherent zero-mode projectors, primitive C1, or internal R_theta rows."
            ),
        },
        "closure_decision": {
            "selected_s3_class_restriction_layer_closed": True,
            "finite_trace_DE_gap_layer_closed": True,
            "operator_level_projective_rhoE_transition_matrices_closed": True,
            "selected_diagonal_End0_covariant_D_E_closed": diagonal_end0_de_closes,
            "selected_stationary_projector_Riesz_Green_transport_closed": diagonal_end0_de_closes,
            "selected_full_sector_covariant_D_E_matrices_closed": False,
            "rank2_to_rank3_sector_transfer_values_closed": False,
            "offdiagonal_End0_control_closed": False,
            "same_branch_dotD_alpha1_values_closed": False,
            "coherent_spectral_zero_mode_projectors_closed": False,
            "primitive_C1_contractions_from_operator_values_closed": False,
            "accepted_internal_scalar_row_count": 0,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": diagonal_end0_de_closes,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "target_fitting_used": False,
        "observed_data_used_as_selector": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step39_DiagonalEnd0CovariantDEImport_or_FullSectorFrontier_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "selected_diagonal_End0_covariant_D_E_closed": diagonal_end0_de_closes,
        "selected_stationary_projector_Riesz_Green_transport_closed": diagonal_end0_de_closes,
        "selected_full_sector_covariant_D_E_matrices_closed": False,
        "same_branch_dotD_alpha1_values_closed": False,
        "coherent_spectral_zero_mode_projectors_closed": False,
        "primitive_C1_contractions_from_operator_values_closed": False,
        "accepted_internal_scalar_row_count": 0,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "observed_data_used_as_selector": False,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected Step39 DiagonalEnd0CovariantDEImport or FullSectorFrontier v1

Status: `{STATUS}`.

Step39 imports the selected diagonal End0 covariant `D_E` lane:

```text
D_E = d + du ad(T3)
```

It also imports the stationary gauge-transport/Riesz-Green replay for the same
diagonal lane. This is a genuine forward closure after Step38, but it is not the
full sector operator-value packet.

Closed now:

- selected diagonal End0 covariant `D_E`
- central shared-circle zero direction for this lane
- stationary transported projector/Riesz/Green lane

Still open:

- rank2-to-rank3 sector transfer values
- offdiagonal End0 control
- full sector `D_E` matrices for Q,u,d,L,e,N,H
- `dotD_alpha1` including transport derivative
- coherent zero-mode projectors
- primitive C1 contractions
- internal `R_theta` scalar rows

Next artifact: `{NEXT}`.
""",
        encoding="utf-8",
    )

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
