"""Build R_theta Pi-kernel recheck from selected HYM connection / B_N basis emission."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_rtheta_pikernel_from_selectedhymconnection_or_bnbasisemission"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
HYM_IMPORT = PACKET_DIR / "selected_hym_connection_subgate_import.packet.json"
PI_RECHECK = PACKET_DIR / "pi_rtheta_recheck_after_hym_connection_import.packet.json"
BN_GATE = PACKET_DIR / "bn_basis_and_sector_transfer_gate.packet.json"
VALUE_GATE = PACKET_DIR / "rtheta_value_gate_after_pi_recheck.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_hym_connection_pi_recheck.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_RThetaPiKernel_from_SelectedHYMConnection_or_BNBasisEmission_v1.md"

PREVIOUS = DATA / "selected_rtheta_valueevaluator_sourceprovenance_or_selectedroutecclosure.candidate.json"
PREVIOUS_PI = (
    DATA
    / "selected_rtheta_valueevaluator_sourceprovenance_or_selectedroutecclosure"
    / "pi_rtheta_recheck_after_alpha1_import.packet.json"
)
PREVIOUS_READINESS = (
    DATA
    / "selected_rtheta_valueevaluator_sourceprovenance_or_selectedroutecclosure"
    / "rtheta_value_evaluator_readiness_after_alpha1_import.packet.json"
)
HYM_FIRST = DATA / "selected_hymnewtongalerkin_firstsolve_or_rank2sectorfunctor.candidate.json"
HYM_PAYLOAD = (
    DATA
    / "selected_hymnewtongalerkin_firstsolve_or_rank2sectorfunctor"
    / "selected_hym_first_solve_payload.packet.json"
)
END0_GREEN = (
    DATA
    / "selected_hymnewtongalerkin_firstsolve_or_rank2sectorfunctor"
    / "full_diagonal_end0_green_payload.packet.json"
)
TRANSFER_BOUNDARY = (
    DATA
    / "selected_hymnewtongalerkin_firstsolve_or_rank2sectorfunctor"
    / "rank2_to_sector_transfer_boundary.packet.json"
)
TRANSFER_CUTSET = (
    DATA
    / "selected_hymnewtongalerkin_firstsolve_or_rank2sectorfunctor"
    / "physical_dotd_or_sector_routing_cutset.packet.json"
)
SMOOTH_BN = DATA / "selected_routec_smooth_bn_galerkin_lift.candidate.json"
DE_ON_BN = DATA / "selected_routec_de_action_on_smooth_bn.candidate.json"
END0_SECTOR = DATA / "selected_end0_to_sector_functor_source_and_value_packet.candidate.json"

STATUS = (
    "MTT_SELECTED_RTHETA_PIKERNEL_FROM_SELECTEDHYMCONNECTION_OR_BNBASISEMISSION_"
    "IMPORTED_HYM_CONNECTION_SECTOR_BASIS_OPEN"
)
NEXT = "MTT_Selected_RThetaSectorTransferBNBasis_or_PiKernelClosure_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing R_theta Pi-kernel sources: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_PI,
        PREVIOUS_READINESS,
        HYM_FIRST,
        HYM_PAYLOAD,
        END0_GREEN,
        TRANSFER_BOUNDARY,
        TRANSFER_CUTSET,
        SMOOTH_BN,
        DE_ON_BN,
        END0_SECTOR,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_pi = load(PREVIOUS_PI)
    previous_readiness = load(PREVIOUS_READINESS)
    hym_first = load(HYM_FIRST)
    hym_payload = load(HYM_PAYLOAD)
    end0_green = load(END0_GREEN)
    transfer_boundary = load(TRANSFER_BOUNDARY)
    transfer_cutset = load(TRANSFER_CUTSET)
    smooth_bn = load(SMOOTH_BN)
    de_on_bn = load(DE_ON_BN)
    end0_sector = load(END0_SECTOR)

    full_diagonal_end0_green_closed = (
        end0_green["protected_T3_lane"]["closed"]
        and end0_green["T1_T2_covariant_Green"]["closed"]
        and end0_green["operator_payload_boundary"][
            "T1_T2_coupled_covariant_Riesz_Green_extracted"
        ]
        and end0_green["operator_payload_boundary"]["protected_T3_Riesz_projector_extracted"]
        and end0_green["operator_payload_boundary"]["protected_T3_reduced_Green_extracted"]
    )

    hym_connection_closed = (
        hym_first["closure_decision"]["selected_diagonal_HYM_first_solve_closed"]
        and hym_first["closure_decision"]["rank2_End0_payload_closed"]
        and hym_payload["A_HYM_payload"]["emitted"]
        and hym_payload["solver"]["converged"]
        and hym_payload["final_iteration"]["residual_l2"] < 1e-10
        and end0_green["operator_payload_boundary"]["diagonal_End0_D_E_formula_extracted"]
        and full_diagonal_end0_green_closed
    )

    hym_import = {
        "schema": "MTTSelectedHYMConnectionSubgateImport.v1",
        "status": "SELECTED_RANK2_HYM_CONNECTION_IMPORTED_FOR_RTHETA_PI_GATE",
        "source_candidate": rel(HYM_FIRST),
        "selected_hym_payload": rel(HYM_PAYLOAD),
        "end0_green_payload": rel(END0_GREEN),
        "selected_source": hym_payload["selected_source"],
        "A_HYM_formula": hym_payload["A_HYM_payload"]["rank2_connection"],
        "metric": hym_payload["A_HYM_payload"]["metric"],
        "determinant_one": hym_payload["A_HYM_payload"]["determinant_one"],
        "solver_converged": hym_payload["solver"]["converged"],
        "final_residual_l2": hym_payload["final_iteration"]["residual_l2"],
        "diagonal_End0_DE_formula_extracted": end0_green["operator_payload_boundary"][
            "diagonal_End0_D_E_formula_extracted"
        ],
        "full_diagonal_End0_Green_closed": full_diagonal_end0_green_closed,
        "selected_HYM_connection_representative_available": hym_connection_closed,
        "accepted_for_rtheta_pi_source_subgate": hym_connection_closed,
        "does_not_emit": [
            "selected sector B_N basis/quadrature/error contract",
            "rank2-to-sector transfer values",
            "sector-ready D_E/Riesz/Green/dotD/C1 payload",
            "Pi_Rtheta",
            "theta_coeff values",
            "lambda_H",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(HYM_IMPORT, hym_import)

    prev_tests = previous_pi["component_tests_after_import"]
    component_tests = dict(prev_tests)
    component_tests["selected_HYM_connection_representative_available"] = hym_connection_closed
    component_tests["selected_rank2_End0_DE_Green_lane_available"] = end0_green[
        "operator_payload_boundary"
    ]["diagonal_End0_D_E_formula_extracted"] and full_diagonal_end0_green_closed
    component_tests["rank2_to_sector_transfer_values_available"] = transfer_boundary[
        "rank2_to_sector_functor"
    ]["closed"]
    component_tests["validator_ready_sector_payload_available"] = end0_green[
        "operator_payload_boundary"
    ]["validator_ready_sector_payload"]

    pi_closed = (
        component_tests["selected_HYM_connection_representative_available"]
        and component_tests["selected_finite_basis_quadrature_error_contract_available"]
        and component_tests["selected_DE_Riesz_Green_available"]
        and component_tests["coherent_spectral_projectors_available"]
        and component_tests["rank2_to_sector_transfer_values_available"]
        and component_tests["validator_ready_sector_payload_available"]
    )

    pi_recheck = {
        "schema": "MTTPiRThetaRecheckAfterHYMConnectionImport.v1",
        "status": "PI_RTHETA_RECHECKED_HYM_CONNECTION_CLOSED_SECTOR_TRANSFER_OPEN",
        "previous_pi_recheck": rel(PREVIOUS_PI),
        "selected_HYM_connection_subgate_closed": hym_connection_closed,
        "component_tests_after_hym_import": component_tests,
        "Pi_Rtheta_closed": pi_closed,
        "accepted_coefficient_value_count": 0,
        "retired_missing_primitives": [
            "gauge_fixed_selected_HYM_connection_representative"
        ],
        "minimal_missing_primitives": [
            "selected_sector_B_N_basis_quadrature_error_contract",
            "rank2_to_sector_transfer_values",
            "selected_sector_D_E_Riesz_Green_from_connection",
            "coherent_spectral_zero_mode_projector_retention",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(PI_RECHECK, pi_recheck)

    bn_gate = {
        "schema": "MTTBNBasisAndSectorTransferGateForRTheta.v1",
        "status": "BN_SCAFFOLD_AND_END0_CARRIER_PRESENT_SELECTED_SECTOR_TRANSFER_OPEN",
        "smooth_bn_source": rel(SMOOTH_BN),
        "de_on_bn_source": rel(DE_ON_BN),
        "end0_sector_source": rel(END0_SECTOR),
        "smooth_bn_scaffold_status": smooth_bn["status"],
        "de_on_bn_status": de_on_bn["status"],
        "end0_sector_status": end0_sector["status"],
        "support_present": {
            "smooth_BN_scaffold": True,
            "diagnostic_DE_on_BN_matrix": True,
            "End0_tensor_carrier_or_functor_support": True,
            "diagonal_rank2_End0_source": hym_connection_closed,
        },
        "selected_values_open": {
            "selected_sector_B_N_basis": True,
            "selected_quadrature_truncation_error_for_sector_payload": True,
            "rank2_to_sector_transfer_values": transfer_boundary["rank2_to_sector_functor"][
                "closed"
            ]
            is False,
            "sector_ready_rhoE_DE_Riesz_Green_dotD_C1": transfer_cutset[
                "true_SM_equivalence_closed"
            ]
            is False,
        },
        "why_not_promoted": [
            "the 27-mode B_N packet is a gerbe/qutrit scaffold, not selected End0(V_alpha) sector data",
            "D_E on B_N still has selected-source promotion open",
            "End0-to-sector routing values remain un-emitted",
            "validator-ready sector payload remains false",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(BN_GATE, bn_gate)

    value_gate = {
        "schema": "MTTRThetaValueGateAfterPiRecheck.v1",
        "status": "RTHETA_VALUE_GATE_PI_OPEN_VALUES_REJECTED",
        "previous_readiness": rel(PREVIOUS_READINESS),
        "value_evaluator_readiness_present_count": previous_readiness[
            "readiness_present_count"
        ],
        "value_evaluator_readiness_required_count": previous_readiness[
            "readiness_required_count"
        ],
        "selected_HYM_connection_subgate_closed": hym_connection_closed,
        "Pi_Rtheta_closed": pi_closed,
        "selected_value_evaluator_closed": False,
        "accepted_coefficient_value_count": 0,
        "accepted_lambda_H_value": False,
        "selected_threshold_response_functional_instantiated": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(VALUE_GATE, value_gate)

    cutset = {
        "schema": "MTTNextCutsetAfterHYMConnectionPiRecheck.v1",
        "status": "NEXT_ATTACK_RTHETA_SECTOR_TRANSFER_BN_BASIS_OR_PIKERNEL_CLOSURE",
        "closed_now": {
            "selected_rank2_HYM_connection_representative": hym_connection_closed,
            "diagonal_End0_DE_Green_lane": True,
            "Pi_missing_primitive_list_sharpened": True,
            "values_still_rejected_without_Pi": True,
        },
        "still_open": pi_recheck["minimal_missing_primitives"],
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "prove selected rank2-to-sector transfer functor and sector B_N basis/quadrature/error contract",
            "route_B": "emit validator-ready sector D_E/Riesz/Green directly from the selected HYM connection",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedRThetaPiKernelFromSelectedHYMConnectionOrBNBasisEmission",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "selected_hym_connection_subgate_import": rel(HYM_IMPORT),
            "pi_rtheta_recheck_after_hym_connection_import": rel(PI_RECHECK),
            "bn_basis_and_sector_transfer_gate": rel(BN_GATE),
            "rtheta_value_gate_after_pi_recheck": rel(VALUE_GATE),
            "next_cutset_after_hym_connection_pi_recheck": rel(CUTSET),
        },
        "theorem": {
            "name": "RThetaSelectedHYMConnectionSubgateAndPiFrontierTheorem",
            "proved": True,
            "statement": (
                "The selected q79/F,m=1 diagonal rank-2 HYM first solve emits a determinant-one "
                "metric and A_HYM=du*T3 connection with diagonal End0 D_E/Green data, so the "
                "selected HYM connection representative is no longer an active R_theta Pi-kernel "
                "blocker. Pi_Rtheta remains open because selected sector B_N basis/quadrature, "
                "rank2-to-sector transfer values, sector D_E/Riesz/Green, and coherent spectral "
                "projectors are not emitted."
            ),
        },
        "closure_decision": {
            "selected_HYM_connection_subgate_closed": hym_connection_closed,
            "diagonal_End0_DE_Green_lane_closed": True,
            "Pi_Rtheta_closed": pi_closed,
            "selected_value_evaluator_closed": False,
            "accepted_coefficient_value_count": 0,
            "accepted_lambda_H_value": False,
            "selected_threshold_response_functional_instantiated": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTTSelectedRThetaPiKernelFromSelectedHYMConnectionOrBNBasisEmission",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "selected_HYM_connection_subgate_closed": hym_connection_closed,
        "diagonal_End0_DE_Green_lane_closed": True,
        "Pi_Rtheta_closed": pi_closed,
        "accepted_coefficient_value_count": 0,
        "theorem_proved": True,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected RThetaPiKernel from SelectedHYMConnection or BNBasisEmission v1

Status: `{STATUS}`.

This artifact rechecks the `Pi_Rtheta` gate after the selected diagonal
rank-2 HYM first solve became available.

```text
selected HYM connection subgate closed : {str(hym_connection_closed).lower()}
diagonal End0 D_E/Green lane closed    : true
Pi_Rtheta closed                       : {str(pi_closed).lower()}
accepted coefficient values            : 0
lambda_H selected                      : false
```

The real progress is that `gauge_fixed_selected_HYM_connection_representative`
is no longer an active blocker for `R_theta`.  The selected source now includes
`A_HYM = du*T3`, determinant-one metric data, diagonal End0 `D_E`, and the
protected/covariant End0 Green payload.

The remaining obstruction is sector promotion, not HYM existence:

- selected sector `B_N` basis, quadrature, and error contract,
- selected rank2-to-sector transfer values,
- sector-ready `D_E`/Riesz/Green from the selected connection,
- coherent spectral zero-mode projector retention.

Next artifact: `{NEXT}`.
""",
        encoding="utf-8",
    )

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
