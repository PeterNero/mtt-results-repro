"""Audit Step 18 QA/SU3 alpha1-dotD import and primitive C1 frontier."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step18_qasu3_alphadotd_import_or_primitivec1frontier"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
IMPORT_PACKET = PACKET_DIR / "step18_imported_qasu3_operator_alpha_dotd.packet.json"
ATOM_CONTRACT = PACKET_DIR / "step18_primitive_c1_atom_contract.packet.json"
NEXT_WORKORDER = PACKET_DIR / "step18_to_step19_value_execution_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step18_QaSU3_AlphaDotDImport_or_PrimitiveC1Frontier_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP18_QASU3_ALPHADOTD_IMPORT_CLOSED_PRIMITIVE_C1_LAMBDA12_FRONTIER"
NEXT = "MTT_Selected_Step19_PrimitiveC1AtomEmission_or_SelectedLambda12SpectralTable_v1"
SECTORS = {"u", "d", "e", "nuD"}
TERMS = {
    "theta_overlap_variation",
    "left_zero_mode_response",
    "right_zero_mode_response",
    "higgs_zero_mode_response",
    "explicit_vertex",
    "basis_connection",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    import_packet = load(IMPORT_PACKET)
    atom_contract = load(ATOM_CONTRACT)
    next_workorder = load(NEXT_WORKORDER)
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

    closed = import_packet["closed_in_active_ledger"]
    for key in [
        "matter_slot_orientation_U10_Ubar5_1M",
        "functional_operator_blocks_u_d_e_nuD",
        "overlap_normalization_rho_s_Ti_over_sqrt2",
        "selected_N_alpha1_h_ext_value",
        "du_dalpha1_equals_h_ext",
        "selected_dotD_source_verified",
        "alpha1_driver_verified",
        "honest_dotD_replay",
    ]:
        require(closed[key] is True, f"import did not close {key}")

    alpha = import_packet["alpha_dotd_imported"]
    require(alpha["N_alpha1_h_ext_promoted_to_selected_value"] is True, "N_alpha1 not promoted")
    require(alpha["du_dalpha1_equals_h_ext_emitted"] is True, "du/dalpha1 not emitted")
    require(alpha["selected_dotD_source_verified"] is True, "dotD source not verified")
    require(alpha["alpha1_driver_verified"] is True, "alpha1 driver not verified")
    require(alpha["honest_dotD_validator_closed"] is True, "honest dotD not closed")
    require(alpha["promoted_value"]["N_alpha1_h_ext"] == 1.0, "wrong N_alpha1 value")

    operator = import_packet["operator_layer_imported"]
    require(operator["same_branch_functional_operator_emission_closed"] is True, "operator emission not closed")
    require(operator["selected_1M_Dirac_operator_block_emitted"] is True, "1M block missing")
    require(operator["selected_U10_Ubar5_operator_blocks_emitted"] is True, "U10/Ubar5 blocks missing")
    require(operator["selected_overlap_normalization_emitted"] is True, "overlap normalization missing")
    require(set(operator["sector_blocks"]) == SECTORS, "sector blocks mismatch")
    for sector, block in operator["sector_blocks"].items():
        require(block["dimension"] == 3, f"dimension mismatch for {sector}")
        require(block["normalized_operator"] == "rho_s(T_i)/sqrt(2)", f"normalization mismatch for {sector}")
        require(block["projector_selected_by_same_source"] is True, f"projector source mismatch for {sector}")
        require(block["same_source_action"] is True, f"same-source action mismatch for {sector}")

    not_closed = import_packet["not_closed_by_import"]
    for key in [
        "operator_layer_Pic0_or_torsion_gerbe_rule",
        "primitive_C1_contractions",
        "A_selected",
        "b_selected",
        "lambda_12",
        "Yukawa_magnitudes",
        "full_SM_closure",
    ]:
        require(not_closed[key] is True, f"overclosed import boundary: {key}")

    atom_status = atom_contract["primitive_status"]
    require(atom_status["atom_count"] == 24, "atom count mismatch")
    require(atom_status["missing_atom_count"] == 24, "missing atom count mismatch")
    require(atom_status["all_primitive_atoms_emitted"] is False, "primitive atoms overclosed")
    require(atom_status["A_selected_emitted"] is False, "A overclosed")
    require(atom_status["b_selected_emitted"] is False, "b overclosed")
    require(set(atom_contract["atom_table"]) == SECTORS, "atom sectors mismatch")
    for sector, rows in atom_contract["atom_table"].items():
        require(set(rows["required_terms"]) == TERMS, f"required terms mismatch for {sector}")
        require(rows["missing_term_count"] == 6, f"missing term count mismatch for {sector}")
        require(rows["all_terms_emitted"] is False, f"sector overclosed: {sector}")

    lambda12 = atom_contract["lambda12_status"]
    require(lambda12["lambda_12_closed"] is False, "lambda12 overclosed")
    require(lambda12["lambda_12_computable_from_this_gate"] is False, "lambda12 computability overclaimed")

    decision = data["closure_decision"]
    require(decision["step18_import_closed"] is True, "Step 18 not closed")
    require(decision["alpha1_dotD_driver_imported"] is True, "alpha/dotD not imported")
    require(decision["primitive_C1_contractions_closed"] is False, "primitive C1 overclosed")
    require(decision["primitive_C1_missing_atom_count"] == 24, "candidate missing atom count mismatch")
    require(decision["A_selected_emitted"] is False, "candidate A overclosed")
    require(decision["b_selected_emitted"] is False, "candidate b overclosed")
    require(decision["lambda12_closed"] is False, "candidate lambda12 overclosed")
    require(decision["Yukawa_or_full_SM_closure"] is False, "candidate full SM overclosed")
    require(decision["Higgs_Huv_or_lambda_H_closed"] is False, "candidate Higgs overclosed")

    require(next_workorder["next_step"] == 19, "next step mismatch")
    require(next_workorder["closed_do_not_reopen"]["Step18_alpha1_dotD_driver"] is True, "anti-reopen alpha missing")
    require(next_workorder["must_emit_next"]["primitive_C1_atoms_24"] is True, "primitive next target missing")
    require(next_workorder["success_criterion"]["target_fitting_used_false"] is True, "target guard missing")

    for phrase in [
        "selected_dotD_source_verified                         closed by QA/SU3 import",
        "24 primitive C1 atoms for u,d,e,nuD",
        "must either emit the 24 primitive C1 atom rows directly",
        NEXT,
    ]:
        require(phrase in note, f"note missing phrase: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
