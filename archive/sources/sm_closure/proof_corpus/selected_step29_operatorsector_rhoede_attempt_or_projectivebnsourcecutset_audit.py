"""Audit Step 29 operator-sector rhoE/D_E attempt / projective B_N source cutset."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step29_operatorsector_rhoede_attempt_or_projectivebnsourcecutset"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SMOKE = PACKET_DIR / "step29_operator_sector_smoke_inventory.packet.json"
PROJECTIVE = PACKET_DIR / "step29_projective_rhoe_bn_source_gap.packet.json"
NEXT_CONTRACT = PACKET_DIR / "step29_next_projective_bn_lift_contract.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step29_OperatorSectorRhoEDEAttempt_or_ProjectiveBNSourceCutset_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP29_OPERATORSECTOR_RHOEDE_ATTEMPT_BUILT_IDENTITYSMOKE_RETIRED_PROJECTIVEBN_SOURCE_OPEN"
NEXT = "MTT_Selected_Step30_ProjectiveRhoE_SmoothBNLift_or_SelectedOperatorSectorValues_v1"
SECTORS = {"Q", "u", "d", "L", "e", "N", "H"}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    smoke = load(SMOKE)
    projective = load(PROJECTIVE)
    contract = load(NEXT_CONTRACT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaimed")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaimed")

    require(smoke["route_c_residual_zero"] is True, "smoke residuals not zero")
    require(smoke["route_c_selected_source_verified"] is False, "smoke source oververified")
    require(smoke["root_claims_selected_source"] is False, "root overclaims selected source")
    require(smoke["identity_rhoE_mesh_selected"] is False, "identity mesh overselected")
    require(smoke["identity_rhoE_metric_selected"] is False, "identity metric overselected")
    require(smoke["identity_rhoE_candidate_kind"] == "identity_rhoE_smoke_unselected", "wrong rhoE kind")
    for key in ["sector_maps", "D_E", "Riesz", "Green", "dotD"]:
        require(smoke["sector_slots_present"][key] is True, f"sector slots missing: {key}")
    for key in [
        "all_D_E_selected_source_false",
        "all_Riesz_selected_source_false",
        "all_Green_selected_source_false",
        "all_dotD_selected_source_false",
        "all_dotD_alpha1_driver_false",
    ]:
        require(smoke["source_flags"][key] is True, f"source flag not false: {key}")
    require(smoke["retirement_decision"]["identity_rhoE_route_retired_for_selected_operator_values"] is True, "identity route not retired")
    require(smoke["retirement_decision"]["rerunning_same_smoke_cannot_close_step28"] is True, "loop guard missing")

    gates = projective["nonidentity_candidate"]["numeric_gates"]
    require(projective["nonidentity_candidate"]["kind"] == "selected_deck_compatible_Heisenberg_Weyl_projective_packet", "wrong projective kind")
    require(projective["nonidentity_candidate"]["selected_by_mtt"] is False, "projective candidate overselected")
    require(gates["passes_numeric_packet_gate"] is True, "numeric projective gate failed")
    require(gates["uses_only_selected_active_generators_g1_g2"] is True, "wrong generators")
    require(gates["nonidentity_norm"] > 0, "nonidentity norm missing")
    require(projective["ordinary_route_reduction"]["ordinary_rhoE_route_retired"] is True, "ordinary route not retired")
    require(projective["ordinary_route_reduction"]["projective_twisted_rhoE_candidate_locked"] is True, "projective candidate not locked")
    require(projective["ordinary_route_reduction"]["selected_projective_rhoE_source_closed"] is False, "projective source overclosed")
    for key in [
        "Gram_matrix_entries",
        "gap_error_certificate",
        "generalized_eigenpairs",
        "metric_volume_quadrature",
        "selected_D_E_action_on_basis",
        "smooth_scalar_basis_functions_phi_m",
        "stiffness_matrix_entries",
    ]:
        require(projective["smooth_BN_missing_fields"][key] is True, f"missing field not registered: {key}")
    for key, value in projective["BN_scaffold_gate"].items():
        require(value is False, f"BN scaffold gate overclosed: {key}")

    require(contract["next_required_artifact"] == NEXT, "contract next mismatch")
    require(contract["closure_claimed"] is False, "contract overclaimed")
    for phrase in [
        "smooth quotient-valid B_N Galerkin basis phi_m carrying the non-identity projective rho_E packet",
        "selected D_E action on that smooth basis, not the identity smoke D_E",
        "selected_source_verified flags derived by theorem for route residual, D_E, Riesz/Green, dotD, and zero-mode sectors",
    ]:
        require(phrase in contract["must_emit_next"], f"must emit missing: {phrase}")
    for phrase in [
        "identity rho_E smoke as selected rho_E",
        "formal lifted selected_source_verified flags",
        "observed SM masses, mixings, CP phases, or benchmark matrices as selectors",
    ]:
        require(phrase in contract["must_not_use"], f"must-not-use missing: {phrase}")

    decision = data["closure_decision"]
    for key in [
        "operator_sector_smoke_inventory_filled",
        "identity_rhoE_smoke_retired_as_selected_route",
        "nonidentity_projective_rhoE_candidate_imported",
        "ordinary_nonidentity_rhoE_route_retired",
        "projective_smooth_BN_lift_contract_emitted",
    ]:
        require(decision[key] is True, f"decision close missing: {key}")
    for key in [
        "selected_operator_level_projective_rhoE_transition_closed",
        "selected_sector_basis_D_E_Riesz_Green_dotD_matrices_closed",
        "selected_smooth_BN_Galerkin_basis_closed",
        "selected_source_verified_operator_flags_closed",
        "fullS2_operator_payload_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed: {key}")
    require(decision["accepted_internal_scalar_row_count"] == 0, "scalar rows overaccepted")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["identity_smoke_route_retired"] is True, "certificate did not retire identity smoke")
    require(cert["operator_sector_values_closed"] is False, "certificate overclosed operator values")

    for phrase in [
        "identity rho_E mesh/metric                          unselected smoke",
        "non-identity projective rho_E candidate             numerically locked",
        "smooth projective B_N lift                           open",
        NEXT,
    ]:
        require(phrase in note, f"note missing phrase: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
