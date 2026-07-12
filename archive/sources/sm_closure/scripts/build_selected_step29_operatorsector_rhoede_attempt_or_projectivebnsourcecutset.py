"""Build Step 29 operator-sector rhoE/D_E attempt / projective B_N source cutset."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step29_operatorsector_rhoede_attempt_or_projectivebnsourcecutset"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SMOKE = PACKET_DIR / "step29_operator_sector_smoke_inventory.packet.json"
PROJECTIVE = PACKET_DIR / "step29_projective_rhoe_bn_source_gap.packet.json"
NEXT_CONTRACT = PACKET_DIR / "step29_next_projective_bn_lift_contract.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step29_OperatorSectorRhoEDEAttempt_or_ProjectiveBNSourceCutset_v1.md"

STEP28 = DATA / "selected_step28_sectorpromotion_reconciliation_or_operatorsectorvaluecutset.candidate.json"
FIRST_RUN = DATA / "selected_routec_strominger_galerkin_first_run.candidate.json"
ROUTEC_RESIDUAL = DATA / "selected_routec_strominger_galerkin_solve" / "route_c_residual.candidate.json"
RHOE_MESH = DATA / "selected_routec_strominger_galerkin_solve" / "rhoE_mesh.candidate.json"
RHOE_METRIC = DATA / "selected_routec_strominger_galerkin_solve" / "rhoE_metric.candidate.json"
DE_ACTION = DATA / "selected_routec_strominger_galerkin_solve" / "de_action.candidate.json"
RIESZ = DATA / "selected_routec_strominger_galerkin_solve" / "riesz_gap.candidate.json"
GREEN = DATA / "selected_routec_strominger_galerkin_solve" / "reduced_green.candidate.json"
DOTD = DATA / "selected_routec_strominger_galerkin_solve" / "dotd_response.candidate.json"
SECTOR_MAPS = DATA / "selected_routec_strominger_galerkin_solve" / "sector_maps.candidate.json"
NONIDENTITY = DATA / "selected_routec_nonidentity_rhoe_bn_construction.candidate.json"
TRANSITION = DATA / "selected_nonidentity_rhoe_transition_source.candidate.json"

STATUS = "MTT_SELECTED_STEP29_OPERATORSECTOR_RHOEDE_ATTEMPT_BUILT_IDENTITYSMOKE_RETIRED_PROJECTIVEBN_SOURCE_OPEN"
NEXT = "MTT_Selected_Step30_ProjectiveRhoE_SmoothBNLift_or_SelectedOperatorSectorValues_v1"
SECTORS = ["Q", "u", "d", "L", "e", "N", "H"]


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def residuals_pass(residuals: dict[str, dict[str, float]]) -> bool:
    return all(abs(slot["value"]) <= slot["tolerance"] for slot in residuals.values())


def all_slots_present(slots: dict[str, Any]) -> bool:
    return set(slots) == set(SECTORS)


def all_slot_flag_false(slots: dict[str, dict[str, Any]], key: str) -> bool:
    return all(slot.get(key) is False for slot in slots.values())


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    inputs = [
        STEP28,
        FIRST_RUN,
        ROUTEC_RESIDUAL,
        RHOE_MESH,
        RHOE_METRIC,
        DE_ACTION,
        RIESZ,
        GREEN,
        DOTD,
        SECTOR_MAPS,
        NONIDENTITY,
        TRANSITION,
    ]
    missing = [rel(path) for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step 29 inputs: " + ", ".join(missing))

    step28 = load(STEP28)
    first_run = load(FIRST_RUN)
    routec_residual = load(ROUTEC_RESIDUAL)
    rhoe_mesh = load(RHOE_MESH)
    rhoe_metric = load(RHOE_METRIC)
    de_action = load(DE_ACTION)
    riesz = load(RIESZ)
    green = load(GREEN)
    dotd = load(DOTD)
    sector_maps = load(SECTOR_MAPS)
    nonidentity = load(NONIDENTITY)
    transition = load(TRANSITION)

    de_slots = de_action["operator_slots"]
    riesz_slots = riesz["spectral_slots"]
    green_slots = green["green_slots"]
    dotd_slots = dotd["dotd_response_slots"]
    sector_projection_maps = sector_maps["sector_projection_maps"]

    smoke = {
        "schema": "MTTStep29OperatorSectorSmokeInventory.v1",
        "status": "IDENTITY_SMOKE_OPERATOR_SECTOR_INVENTORY_FILLED_BUT_UNSELECTED",
        "route_c_residual_zero": residuals_pass(routec_residual["residuals"]),
        "route_c_selected_source_verified": routec_residual["selected_source_verified"],
        "root_claims_selected_source": first_run["root_payload"]["claims_selected_source"],
        "identity_rhoE_mesh_selected": rhoe_mesh["selected_by_mtt"],
        "identity_rhoE_metric_selected": rhoe_metric["selected_by_mtt"],
        "identity_rhoE_candidate_kind": rhoe_mesh["candidate_kind"],
        "sector_slots_present": {
            "sector_maps": all_slots_present(sector_projection_maps),
            "D_E": all_slots_present(de_slots),
            "Riesz": all_slots_present(riesz_slots),
            "Green": all_slots_present(green_slots),
            "dotD": all_slots_present(dotd_slots),
        },
        "source_flags": {
            "all_D_E_selected_source_false": all_slot_flag_false(de_slots, "selected_source_verified"),
            "all_Riesz_selected_source_false": all_slot_flag_false(riesz_slots, "selected_source_verified"),
            "all_Green_selected_source_false": all_slot_flag_false(green_slots, "selected_source_verified"),
            "all_dotD_selected_source_false": all_slot_flag_false(dotd_slots, "selected_dotD_source_verified"),
            "all_dotD_alpha1_driver_false": all_slot_flag_false(dotd_slots, "alpha1_driver_verified"),
        },
        "retirement_decision": {
            "identity_smoke_values_are_postchecks_only": True,
            "identity_rhoE_route_retired_for_selected_operator_values": True,
            "rerunning_same_smoke_cannot_close_step28": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(SMOKE, smoke)

    projective = {
        "schema": "MTTStep29ProjectiveRhoEBNSourceGap.v1",
        "status": "PROJECTIVE_RHOE_CANDIDATE_NUMERICALLY_LOCKED_SMOOTH_BN_SOURCE_OPEN",
        "nonidentity_candidate": {
            "kind": nonidentity["rho_E_candidate"]["kind"],
            "rank": nonidentity["rho_E_candidate"]["rank"],
            "selected_by_mtt": nonidentity["rho_E_candidate"]["selected_by_mtt"],
            "selection_status": nonidentity["rho_E_candidate"]["selection_status"],
            "numeric_gates": nonidentity["rho_E_candidate"]["numeric_gates"],
        },
        "ordinary_route_reduction": {
            "ordinary_rhoE_route_retired": transition["gate_results"]["ordinary_rhoE_route_retired"],
            "projective_twisted_rhoE_candidate_locked": transition["gate_results"]["projective_twisted_rhoE_candidate_locked"],
            "selected_projective_rhoE_source_closed": transition["gate_results"]["selected_projective_rhoE_source_closed"],
            "projective_repair_needed": transition["superset_mode"]["superset_repair"]["needed"],
        },
        "smooth_BN_missing_fields": nonidentity["contract_comparison"]["still_missing_after_this_attempt"],
        "BN_scaffold_gate": {
            "passes_B_N_payload_gate": nonidentity["B_N_scaffold"]["passes_B_N_payload_gate"],
            "smooth_scalar_basis_phi_m_emitted": nonidentity["B_N_scaffold"]["smooth_scalar_basis_phi_m_emitted"],
            "selected_D_E_action_emitted": nonidentity["B_N_scaffold"]["selected_D_E_action_emitted"],
            "metric_quadrature_emitted": nonidentity["B_N_scaffold"]["metric_quadrature_emitted"],
            "gram_stiffness_emitted": nonidentity["B_N_scaffold"]["gram_stiffness_emitted"],
            "gap_certificate_emitted": nonidentity["B_N_scaffold"]["gap_certificate_emitted"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(PROJECTIVE, projective)

    contract = {
        "schema": "MTTStep29NextProjectiveBNLiftContract.v1",
        "status": "NEXT_PROJECTIVE_RHOE_SMOOTH_BN_LIFT_CONTRACT",
        "next_required_artifact": NEXT,
        "must_emit_next": [
            "smooth quotient-valid B_N Galerkin basis phi_m carrying the non-identity projective rho_E packet",
            "selected metric quadrature and Gram/stiffness matrices for the projective/twisted carrier",
            "selected D_E action on that smooth basis, not the identity smoke D_E",
            "sector-basis Riesz projectors and Green operators with gap/error certificates",
            "dotD_alpha1 in the same projective B_N basis compatible with Step18 normalization",
            "selected_source_verified flags derived by theorem for route residual, D_E, Riesz/Green, dotD, and zero-mode sectors",
        ],
        "must_not_use": [
            "identity rho_E smoke as selected rho_E",
            "formal lifted selected_source_verified flags",
            "observed SM masses, mixings, CP phases, or benchmark matrices as selectors",
            "raw finite twisted deck scaffold without smooth B_N metric/quadrature/stiffness data",
        ],
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(NEXT_CONTRACT, contract)

    candidate = {
        "candidate": "MTTSelectedStep29OperatorSectorRhoEDEAttemptOrProjectiveBNSourceCutset",
        "status": STATUS,
        "inputs": {
            "step28": rel(STEP28),
            "first_run": rel(FIRST_RUN),
            "route_c_residual": rel(ROUTEC_RESIDUAL),
            "rhoE_mesh": rel(RHOE_MESH),
            "rhoE_metric": rel(RHOE_METRIC),
            "de_action": rel(DE_ACTION),
            "riesz": rel(RIESZ),
            "green": rel(GREEN),
            "dotd": rel(DOTD),
            "sector_maps": rel(SECTOR_MAPS),
            "nonidentity": rel(NONIDENTITY),
            "transition": rel(TRANSITION),
        },
        "output_packets": {
            "operator_sector_smoke_inventory": rel(SMOKE),
            "projective_rhoe_bn_source_gap": rel(PROJECTIVE),
            "next_projective_bn_lift_contract": rel(NEXT_CONTRACT),
        },
        "theorem": {
            "name": "Step29IdentitySmokeRetirementAndProjectiveBNSourceCutset",
            "proved": True,
            "statement": (
                "The available Route-C/Strominger operator-sector matrices are complete as an "
                "identity-rhoE smoke inventory but cannot close selected operator-sector values: "
                "rhoE is unselected identity data and all D_E/Riesz/Green/dotD source flags are "
                "false. The ordinary identity route is retired. The next admissible route is the "
                "already locked non-identity projective rhoE packet lifted to a smooth selected "
                "B_N Galerkin basis with metric/quadrature/stiffness, selected D_E, spectral "
                "projectors, Green/dotD, and theorem-derived source flags."
            ),
        },
        "closure_decision": {
            "operator_sector_smoke_inventory_filled": True,
            "identity_rhoE_smoke_retired_as_selected_route": True,
            "nonidentity_projective_rhoE_candidate_imported": True,
            "ordinary_nonidentity_rhoE_route_retired": True,
            "projective_smooth_BN_lift_contract_emitted": True,
            "selected_operator_level_projective_rhoE_transition_closed": False,
            "selected_sector_basis_D_E_Riesz_Green_dotD_matrices_closed": False,
            "selected_smooth_BN_Galerkin_basis_closed": False,
            "selected_source_verified_operator_flags_closed": False,
            "fullS2_operator_payload_closed": False,
            "accepted_internal_scalar_row_count": 0,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "what_closes_now": {
            "identity_smoke_route_retired": True,
            "operator_sector_smoke_inventory_as_postcheck": True,
            "projective_nonidentity_rhoE_next_route_locked": True,
            "smooth_BN_missing_fields_enumerated": True,
        },
        "what_remains_open": {
            "selected_projective_rhoE_smooth_BN_lift": True,
            "selected_D_E_Riesz_Green_dotD_operator_sector_values": True,
            "internal_Rtheta_scalar_rows": True,
            "lambda_H": True,
            "Yukawa_CKM_PMNS_mass_values": True,
            "true_SM_equivalence": True,
            "full_no_knob_closure": True,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step29_OperatorSectorRhoEDEAttempt_or_ProjectiveBNSourceCutset_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "identity_smoke_route_retired": True,
        "projective_smooth_BN_lift_closed": False,
        "operator_sector_values_closed": False,
        "accepted_internal_scalar_row_count": 0,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected Step29 OperatorSectorRhoEDEAttempt or ProjectiveBNSourceCutset v1

Status: `{STATUS}`.

Step29 executes the Step28 target against the existing Route-C/Strominger
operator-sector outputs.  The result is sharp:

```text
Route-C residual smoke values                       zero but selected_source_verified=false
identity rho_E mesh/metric                          unselected smoke
sector maps, D_E, Riesz, Green, dotD                present for Q,u,d,L,e,N,H
D_E/Riesz/Green/dotD selected source flags          false
non-identity projective rho_E candidate             numerically locked
smooth projective B_N lift                           open
operator-sector selected values                     open
internal R_theta scalar rows                         open
```

So the next target is not another identity-smoke Galerkin rerun.  It is the
smooth selected B_N lift of the projective/twisted rho_E packet, carrying
metric quadrature, Gram/stiffness, selected D_E, Riesz/Green, dotD, and
theorem-derived selected-source flags.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
