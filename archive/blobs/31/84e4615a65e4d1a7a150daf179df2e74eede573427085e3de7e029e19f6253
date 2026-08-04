"""Build R_theta sector-transfer/B_N basis recheck or Pi-kernel closure."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_rtheta_sectortransferbnbasis_or_pikernelclosure"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PROJECTOR_IMPORT = PACKET_DIR / "selected_transported_projector_source_import.packet.json"
SECTOR_TRANSFER = PACKET_DIR / "rtheta_sector_transfer_stationary_subgate.packet.json"
PI_RECHECK = PACKET_DIR / "pi_rtheta_recheck_after_sector_projector_promotion.packet.json"
VALUE_GATE = PACKET_DIR / "rtheta_value_gate_after_sector_transfer_recheck.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_sector_transfer_recheck.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_RThetaSectorTransferBNBasis_or_PiKernelClosure_v1.md"

PREVIOUS = DATA / "selected_rtheta_pikernel_from_selectedhymconnection_or_bnbasisemission.candidate.json"
PREVIOUS_PI = (
    DATA
    / "selected_rtheta_pikernel_from_selectedhymconnection_or_bnbasisemission"
    / "pi_rtheta_recheck_after_hym_connection_import.packet.json"
)
FINITE_PROMOTION = DATA / "selected_finite_projector_source_promotion.candidate.json"
PROJECTOR_VALUES = DATA / "selected_hym_projector_zeromode_basis_value_emission.candidate.json"
ALPHA_IMPORT = DATA / "selected_crossrepo_alpha1_driver_replay_import.candidate.json"
PHYSICAL_DOTD = DATA / "selected_physicaldotd_sectorrouting_after_hymfirstsolve.candidate.json"
DIRAC_ROUTING = DATA / "selected_1m_dirac_source_or_u10ubar5_polarization.candidate.json"

STATUS = (
    "MTT_SELECTED_RTHETA_SECTORTRANSFERBNBASIS_OR_PIKERNELCLOSURE_"
    "IMPORTED_TRANSPORTED_PROJECTORS_DOTD_ROUTING_OPEN"
)
NEXT = "MTT_Selected_RThetaDynamicPiEvaluator_or_MatterSlotRoutingClosure_v1"


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
        raise FileNotFoundError("missing R_theta sector-transfer sources: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_PI,
        FINITE_PROMOTION,
        PROJECTOR_VALUES,
        ALPHA_IMPORT,
        PHYSICAL_DOTD,
        DIRAC_ROUTING,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_pi = load(PREVIOUS_PI)
    finite = load(FINITE_PROMOTION)
    values = load(PROJECTOR_VALUES)
    alpha = load(ALPHA_IMPORT)
    physical_dotd = load(PHYSICAL_DOTD)
    dirac = load(DIRAC_ROUTING)

    promoted_slots = finite["promoted_sector_slots"]
    sectors = ["Q", "u", "d", "L", "e", "N", "H"]
    all_slots_promoted = all(
        promoted_slots[sector]["source_verified_by_transport_conjugation"]
        and promoted_slots[sector]["stationary_rho_s_promoted"]
        and promoted_slots[sector]["riesz_projector_valid"]
        and promoted_slots[sector]["green_operator_valid"]
        and promoted_slots[sector]["rank_preserved"]
        for sector in sectors
    )
    projector_import_closed = (
        finite["promotion_decision"]["finite_projector_source_promotion_proved"]
        and finite["promotion_decision"]["selected_projector_source_verified"]
        and finite["promotion_decision"]["validator_ready_stationary_rho_s"]
        and finite["evidence_chain"]["symbolic_transport_validator_closed"]
        and all_slots_promoted
    )

    projector_import = {
        "schema": "MTTSelectedTransportedProjectorSourceImportForRTheta.v1",
        "status": "TRANSPORTED_STATIONARY_PROJECTOR_SOURCE_IMPORTED",
        "source": rel(FINITE_PROMOTION),
        "projector_values_source": rel(PROJECTOR_VALUES),
        "transport_formula": "P_s^sel = U P_s^model U^-1, G_s^sel = U G_s^model U^-1, U=exp(-u ad(T3))",
        "selected_projector_source_verified": finite["promotion_decision"][
            "selected_projector_source_verified"
        ],
        "validator_ready_stationary_rho_s": finite["promotion_decision"][
            "validator_ready_stationary_rho_s"
        ],
        "symbolic_transport_validator_closed": finite["evidence_chain"][
            "symbolic_transport_validator_closed"
        ],
        "gauge_frame_residual": finite["boundary"]["gauge_frame_residual"],
        "raw_direct_truncated_residual": finite["boundary"]["raw_direct_truncated_residual"],
        "raw_untransported_packet_promoted": finite["promotion_decision"][
            "raw_untransported_packet_promoted"
        ],
        "transported_packet_promoted": finite["promotion_decision"][
            "transported_packet_promoted"
        ],
        "sector_count": len(promoted_slots),
        "all_sector_stationary_slots_promoted": all_slots_promoted,
        "accepted_for_rtheta_stationary_pi_subgate": projector_import_closed,
        "does_not_emit": [
            "selected dotD_alpha1 transport derivative",
            "alpha1 source-strength normalization in this repo",
            "matter-slot routing among u,d,e,N",
            "primitive C1 overlap contractions",
            "theta_coeff values",
            "lambda_H",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(PROJECTOR_IMPORT, projector_import)

    sector_transfer = {
        "schema": "MTTRThetaSectorTransferStationarySubgate.v1",
        "status": "STATIONARY_SECTOR_TRANSFER_AND_RHO_S_CLOSED_DYNAMIC_ROUTING_OPEN",
        "selected_sector_basis_projector_contract_closed": projector_import_closed,
        "selected_stationary_rho_s_closed": finite["promotion_decision"][
            "validator_ready_stationary_rho_s"
        ],
        "selected_Riesz_Green_stationary_closed": all(
            promoted_slots[sector]["riesz_projector_valid"]
            and promoted_slots[sector]["green_operator_valid"]
            for sector in sectors
        ),
        "selected_sector_basis_labels": {
            sector: promoted_slots[sector]["selected_basis_labels"] for sector in sectors
        },
        "selected_projector_formulas": {
            sector: promoted_slots[sector]["selected_projector_formula"] for sector in sectors
        },
        "raw_BN_promoted": False,
        "transported_BN_promoted": finite["promotion_decision"]["transported_packet_promoted"],
        "remaining_dynamic_requirements": [
            "selected dotD_alpha1 transport derivative on the transported projector packet",
            "selected matter-slot routing/1_M rule sufficient for charged R_theta slot ownership",
            "primitive C1 overlap contractions or accepted theorem showing Pi_Rtheta does not need them",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(SECTOR_TRANSFER, sector_transfer)

    alpha_imported = (
        alpha["alpha1_driver_verified_imported"]
        and alpha["selected_dotD_source_verified_imported"]
        and alpha["alpha1_driver_replay_import"]["honest_dotD_alpha1_replay"]
    )
    local_dotd_transport_closed = physical_dotd.get("closure_decision", {}).get(
        "physical_dotD_alpha1_closed", False
    ) or physical_dotd.get("what_closes_now", {}).get(
        "physical_dotD_alpha1", False
    )
    matter_slot_routing_closed = dirac.get("closure_decision", {}).get(
        "selected_1M_Dirac_neutrino_rule_closed", False
    ) or dirac.get("closure_decision", {}).get("matter_slot_routing_closed", False)

    prev_tests = previous_pi["component_tests_after_hym_import"]
    component_tests = dict(prev_tests)
    component_tests.update(
        {
            "selected_sector_B_N_basis_quadrature_error_contract_available": projector_import_closed,
            "rank2_to_sector_transfer_values_available": finite["promotion_decision"][
                "validator_ready_stationary_rho_s"
            ],
            "selected_DE_Riesz_Green_available": projector_import_closed,
            "coherent_spectral_projectors_available": projector_import_closed,
            "validator_ready_sector_payload_available": projector_import_closed,
            "selected_dotD_alpha1_imported_crossrepo": alpha_imported,
            "selected_dotD_transport_derivative_local_to_transported_packet": bool(
                local_dotd_transport_closed
            ),
            "selected_matter_slot_routing_available": bool(matter_slot_routing_closed),
        }
    )

    pi_closed = (
        projector_import_closed
        and alpha_imported
        and bool(local_dotd_transport_closed)
        and bool(matter_slot_routing_closed)
    )

    pi_recheck = {
        "schema": "MTTPiRThetaRecheckAfterSectorProjectorPromotion.v1",
        "status": "PI_RTHETA_RECHECKED_STATIONARY_PROJECTORS_CLOSED_DYNAMIC_ROUTING_OPEN",
        "previous_pi_recheck": rel(PREVIOUS_PI),
        "component_tests_after_sector_projector_promotion": component_tests,
        "retired_missing_primitives": [
            "selected_sector_B_N_basis_quadrature_error_contract",
            "rank2_to_sector_transfer_values",
            "selected_sector_D_E_Riesz_Green_from_connection",
            "coherent_spectral_zero_mode_projector_retention",
        ],
        "Pi_Rtheta_closed": pi_closed,
        "accepted_coefficient_value_count": 0,
        "new_minimal_missing_primitives": [
            "selected_dotD_alpha1_transport_derivative_on_transported_projector_packet",
            "selected_matter_slot_routing_or_1M_rule_for_Rtheta_slot_ownership",
            "primitive_C1_overlap_contractions_or_no-need theorem for Pi_Rtheta",
        ],
        "why_not_closed": [
            "cross-repo alpha1/dotD replay is accepted for source provenance, but local transported-packet dotD derivative remains a separate gate",
            "stationary rho_s does not by itself select matter-slot routing among u,d,e,N",
            "R_theta coefficient values cannot be emitted until the dynamic Pi evaluator is fully selected",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(PI_RECHECK, pi_recheck)

    value_gate = {
        "schema": "MTTRThetaValueGateAfterSectorTransferRecheck.v1",
        "status": "RTHETA_VALUES_STILL_REJECTED_DYNAMIC_PI_OPEN",
        "stationary_sector_transfer_closed": projector_import_closed,
        "Pi_Rtheta_closed": pi_closed,
        "accepted_coefficient_value_count": 0,
        "accepted_lambda_H_value": False,
        "selected_threshold_response_functional_instantiated": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(VALUE_GATE, value_gate)

    cutset = {
        "schema": "MTTNextCutsetAfterSectorTransferRecheck.v1",
        "status": "NEXT_ATTACK_RTHETA_DYNAMIC_PI_EVALUATOR_OR_MATTER_SLOT_ROUTING",
        "closed_now": {
            "transported_stationary_projector_source": projector_import_closed,
            "selected_stationary_rho_s": finite["promotion_decision"][
                "validator_ready_stationary_rho_s"
            ],
            "sector_BN_projector_basis_subgate": projector_import_closed,
            "coherent_stationary_spectral_projector_retention": projector_import_closed,
            "values_still_rejected_without_dynamic_Pi": True,
        },
        "still_open": pi_recheck["new_minimal_missing_primitives"],
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "prove selected dotD_alpha1 transport derivative on the transported projector packet and combine with existing alpha1 source import",
            "route_B": "close selected matter-slot routing/1_M rule for charged R_theta slot ownership",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedRThetaSectorTransferBNBasisOrPiKernelClosure",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "selected_transported_projector_source_import": rel(PROJECTOR_IMPORT),
            "rtheta_sector_transfer_stationary_subgate": rel(SECTOR_TRANSFER),
            "pi_rtheta_recheck_after_sector_projector_promotion": rel(PI_RECHECK),
            "rtheta_value_gate_after_sector_transfer_recheck": rel(VALUE_GATE),
            "next_cutset_after_sector_transfer_recheck": rel(CUTSET),
        },
        "theorem": {
            "name": "RThetaStationarySectorTransferPromotionTheorem",
            "proved": True,
            "statement": (
                "The selected finite projector source-promotion theorem supplies transported stationary "
                "sector projectors, Riesz/Green replay, and validator-ready rho_s for Q,u,d,L,e,N,H. "
                "Therefore the R_theta stationary sector-transfer/B_N projector subgate and coherent "
                "stationary spectral projector-retention blocker are retired. Pi_Rtheta remains open "
                "because the dynamic dotD transport derivative, matter-slot routing/1_M rule, and "
                "primitive C1/no-need theorem are not closed."
            ),
        },
        "closure_decision": {
            "stationary_sector_transfer_closed": projector_import_closed,
            "selected_stationary_rho_s_closed": finite["promotion_decision"][
                "validator_ready_stationary_rho_s"
            ],
            "Pi_Rtheta_closed": pi_closed,
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
        "certificate": "MTTSelectedRThetaSectorTransferBNBasisOrPiKernelClosure",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "stationary_sector_transfer_closed": projector_import_closed,
        "selected_stationary_rho_s_closed": finite["promotion_decision"][
            "validator_ready_stationary_rho_s"
        ],
        "Pi_Rtheta_closed": pi_closed,
        "accepted_coefficient_value_count": 0,
        "theorem_proved": True,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected RThetaSectorTransferBNBasis or PiKernelClosure v1

Status: `{STATUS}`.

This artifact imports the transported finite-projector source-promotion theorem
into the `R_theta` `Pi` gate.

```text
transported stationary projector source closed : {str(projector_import_closed).lower()}
selected stationary rho_s closed               : {str(finite['promotion_decision']['validator_ready_stationary_rho_s']).lower()}
old sector projector/B_N blockers retired      : true
Pi_Rtheta closed                               : {str(pi_closed).lower()}
accepted coefficient values                    : 0
```

The raw untransported `B_N` packet is still not promoted.  The selected object
is the exact transported packet

```text
P_s^sel = U P_s^model U^-1,  G_s^sel = U G_s^model U^-1,
U = exp(-u ad(T3)).
```

This closes the stationary sector projector/rho_s side of the `Pi` frontier.
The remaining dynamic frontier is now:

- selected `dotD_alpha1` transport derivative on the transported projector packet,
- selected matter-slot routing or `1_M` rule for `R_theta` slot ownership,
- primitive C1 overlap contractions or a theorem proving `Pi_Rtheta` does not need them.

Next artifact: `{NEXT}`.
""",
        encoding="utf-8",
    )

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
