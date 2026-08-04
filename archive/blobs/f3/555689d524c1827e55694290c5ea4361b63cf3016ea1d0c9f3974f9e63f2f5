"""Audit H-sector dynamic C1 extension or direct Huv rows packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_hsectordynamicc1extension_or_directhuvrows"
BASE = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HSectorDynamicC1Extension_or_DirectHuvRows_v1.md"
BUILD = ROOT / "scripts" / f"build_{SLUG}.py"

H7B1N_IMPORT = BASE / "h7b1n_two_route_cutset_import.packet.json"
H7B1Z_RECONCILE = BASE / "h7b1z_binding_cutset_reconciled_with_active_repo.packet.json"
HSECTOR_ATTEMPT = BASE / "hsector_dynamic_extension_attempt.packet.json"
DIRECT_ATTEMPT = BASE / "direct_huv_rows_after_bhuv_import_attempt.packet.json"
CUTSET = BASE / "next_cutset_after_hsector_directhuv_attempt.packet.json"

STATUS = (
    "MTT_SELECTED_HSECTORDYNAMICC1EXTENSION_OR_DIRECTHUVROWS_"
    "BHUV_EHUV_BINDING_IMPORTED_MSOURCE_OR_DIRECTROWS_OPEN"
)
NEXT = "MTT_Selected_MSourceHuvOperator_or_DirectHerm2Rows_v1"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def require_no_selector(packet: dict, label: str) -> None:
    require(packet.get("observed_data_used_as_selector") is False, f"{label}: observed selector")
    require(packet.get("target_fitting_used") is False, f"{label}: target fitting")


def main() -> int:
    proc = subprocess.run([sys.executable, str(BUILD)], cwd=ROOT, text=True, capture_output=True)
    if proc.returncode:
        print(proc.stdout)
        print(proc.stderr)
        return proc.returncode

    candidate = load(CANDIDATE)
    cert = load(CERT)
    h7b1n = load(H7B1N_IMPORT)
    h7b1z = load(H7B1Z_RECONCILE)
    hsector = load(HSECTOR_ATTEMPT)
    direct = load(DIRECT_ATTEMPT)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["next_required_artifact"] == NEXT, "candidate next")
    require(candidate["closure_claimed"] is True, "candidate closure")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["true_SM_equivalence_claimed"] is False, "true SM overclaim")
    require(candidate["full_no_knob_closure_claimed"] is False, "no-knob overclaim")
    require_no_selector(candidate, "candidate")

    decision = candidate["closure_decision"]
    for key in [
        "h7b1n_cutset_imported",
        "h7b1z_hym_solver_existence_retired",
        "active_E_HUV_source_ids_emitted",
        "active_E_HUV_HYM_metric_connection_bound",
        "active_B_Huv_symbolic_lift_emitted",
        "Hsector_dynamic_extension_attempted",
        "direct_Huv_rows_attempted",
    ]:
        require(decision[key] is True, f"decision true {key}")
    for key in [
        "selected_Hsector_dynamic_C1_extension_emitted",
        "selected_Eval_EHuv_C1_emitted",
        "selected_Pi_Huv_or_R_H_emitted",
        "M_source_emitted",
        "direct_Huu_Hud_Hdd_emitted",
        "direct_Herm2_Huv_payload_emitted",
        "selected_F_Huv_rows_emitted",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision false {key}")

    nums = candidate["key_numbers"]
    require(nums["C1_target_row_count"] == 72, "C1 rows")
    require(nums["C1_higgs_slot_rows_found"] == 0, "C1 H rows")
    require(nums["Huv_source_column_count"] == 2, "Huv columns")
    require(nums["B_Huv_column_count"] == 2, "B columns")
    require(nums["accepted_F_Huv_row_count"] == 0, "F rows")
    require(nums["accepted_certificate_count"] == 0, "cert rows")

    require(cert["status"] == STATUS, "cert status")
    require(cert["next_required_artifact"] == NEXT, "cert next")
    require(cert["theorem_proved"] is True, "cert theorem")
    for key in [
        "h7b1n_cutset_imported",
        "h7b1z_hym_solver_existence_retired",
        "active_E_HUV_source_ids_emitted",
        "active_E_HUV_HYM_metric_connection_bound",
        "active_B_Huv_symbolic_lift_emitted",
        "Hsector_dynamic_extension_attempted",
        "direct_Huv_rows_attempted",
    ]:
        require(cert[key] is True, f"cert true {key}")
    for key in [
        "true_SM_equivalence_claimed",
        "full_no_knob_closure_claimed",
        "observed_data_used_as_selector",
        "target_fitting_used",
        "selected_Hsector_dynamic_C1_extension_emitted",
        "selected_Eval_EHuv_C1_emitted",
        "selected_Pi_Huv_or_R_H_emitted",
        "M_source_emitted",
        "direct_Huu_Hud_Hdd_emitted",
        "direct_Herm2_Huv_payload_emitted",
        "selected_F_Huv_rows_emitted",
    ]:
        require(cert[key] is False, f"cert false {key}")

    require(h7b1n["status"] == "H7B1N_TWO_ROUTE_CUTSET_IMPORTED", "h7b1n status")
    require(h7b1n["imported_theorem"]["proved"] is True, "h7b1n theorem")
    require(h7b1n["imported_hsector_attempt"]["route_A_passes"] is False, "h7b1n A")
    require(h7b1n["imported_hsector_attempt"]["H_sector_dynamic_extension_found"] is False, "h7b1n H")
    require(h7b1n["imported_direct_attempt"]["route_B_passes"] is False, "h7b1n B")
    require(h7b1n["imported_direct_attempt"]["M_source_emitted"] is False, "h7b1n M")
    require(h7b1n["active_repo_update_to_H7B1N"]["B_Huv_emitted_in_active_repo"] is True, "active B")
    require(
        h7b1n["active_repo_update_to_H7B1N"]["finite_E_H_UV_source_ids_emitted_in_active_repo"] is True,
        "active ids",
    )
    require(
        h7b1n["active_repo_update_to_H7B1N"]["selected_HYM_metric_or_connection_bound_in_active_repo"] is True,
        "active HYM",
    )
    require(h7b1n["decision"]["B_Huv_missing_clause_superseded"] is True, "B superseded")
    require(h7b1n["decision"]["M_source_or_direct_Huv_rows_still_absent"] is True, "M still open")
    require_no_selector(h7b1n, "h7b1n")

    require(
        h7b1z["status"] == "H7B1Z_RECONCILED_HYM_SOLVER_RETIRED_BINDING_AND_HERM2_VALUES_OPEN",
        "h7b1z status",
    )
    require(h7b1z["imported_h7b1z"]["HYM_solver_existence_retired_as_blocker"] is True, "solver retired")
    require(h7b1z["active_repo_supersessions"]["selected_E_H_UV_section_basis_source_ids_emitted"] is True, "ids")
    require(h7b1z["active_repo_supersessions"]["selected_HYM_metric_or_connection_on_E_H_UV_bound"] is True, "metric")
    require(h7b1z["active_repo_supersessions"]["B_Huv_symbolic_exact_payload_emitted"] is True, "B exact")
    require(h7b1z["still_open_after_reconciliation"]["direct_Herm2_fill_attempt_values_absent"] is True, "Herm2 absent")
    require(h7b1z["decision"]["projection_measure_equality_still_open"] is True, "projection open")
    require(h7b1z["decision"]["direct_Herm2_rows_still_absent"] is True, "direct open")
    require_no_selector(h7b1z, "h7b1z")

    require(hsector["status"] == "HSECTOR_DYNAMIC_C1_EXTENSION_ATTEMPTED_ZERO_ROWS", "hsector status")
    require(hsector["available_C1_source"]["strict_unpatched_dynamic_C1_closed"] is True, "C1 closed")
    require(hsector["available_C1_source"]["current_target_sectors"] == ["d", "e", "nuD", "u"], "sectors")
    require(hsector["available_C1_source"]["current_H_sector_rows"] == 0, "H rows")
    require(hsector["emitted_extension_rows"] == [], "extension rows")
    require(hsector["emitted_Pi_Huv_or_R_H"] is None, "Pi emitted")
    hdec = hsector["decision"]
    require(hdec["Hsector_dynamic_extension_attempted"] is True, "H attempted")
    for key in [
        "selected_Hsector_dynamic_C1_extension_emitted",
        "selected_Eval_EHuv_C1_emitted",
        "selected_Pi_Huv_or_R_H_emitted",
    ]:
        require(hdec[key] is False, f"hsector false {key}")
    require(hdec["selected_Higgs_C1_variation_slot_count"] == 0, "H slot count")
    require_no_selector(hsector, "hsector")

    require(direct["status"] == "DIRECT_HUV_ROWS_ATTEMPTED_BHUV_AVAILABLE_MSOURCE_ROWS_OPEN", "direct status")
    available = direct["available_direct_route_inputs"]
    require(available["ordered_E_H_UV_basis"] == ["H_u", "H_d^dagger"], "basis")
    require(available["B_Huv_symbolic_exact_payload_emitted"] is True, "B emitted")
    require(len(available["B_Huv_columns"]) == 2, "B columns direct")
    require(available["selected_HYM_metric_or_connection_on_E_H_UV"] is True, "HYM direct")
    require(direct["missing_direct_route_inputs"]["or_direct_rows"] == ["Huu", "Hud_re", "Hud_im", "Hdd"], "rows")
    for value in direct["emitted_rows"].values():
        require(value is None, "direct row emitted")
    ddec = direct["decision"]
    require(ddec["direct_Huv_rows_attempted"] is True, "direct attempted")
    require(ddec["B_Huv_available"] is True, "B available")
    for key in [
        "M_source_emitted",
        "direct_Huu_Hud_Hdd_emitted",
        "direct_Herm2_Huv_payload_emitted",
        "selected_F_Huv_rows_emitted",
    ]:
        require(ddec[key] is False, f"direct false {key}")
    require(ddec["accepted_F_Huv_row_count"] == 0, "direct F rows")
    require(ddec["accepted_certificate_count"] == 0, "direct certs")
    require_no_selector(direct, "direct")

    require(cutset["status"] == "NEXT_FRONTIER_MSOURCE_HUV_OPERATOR_OR_DIRECT_HERM2_ROWS", "cutset status")
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    for phrase in [
        "H7B1N two-route cutset imported",
        "H7B1Z HYM-grid existence blocker retired",
        "active C2/C3/B_Huv supersede older missing-basis/metric/B_Huv clauses",
        "direct Huv route rerun with B_Huv available but zero M_source/direct rows",
    ]:
        require(phrase in cutset["closed_here"], f"closed {phrase}")
    for phrase in [
        "selected same-source M_source Hermitian operator on B_Huv",
        "or direct source-owned Huu,Hud,Hdd Herm(2) rows",
        "same-source exactness/residual certificate",
    ]:
        require(phrase in cutset["still_open"], f"open {phrase}")
    require_no_selector(cutset, "cutset")

    for phrase in [
        "symbolic source-orthonormal `B_Huv` lift emitted: `True`",
        "M_source on B_Huv, or direct certified Huu,Hud,Hdd rows.",
        "Current emitted `Huv` rows: `0`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: H7B1N/Z reconciled; B_Huv/E_H^UV binding imported; "
        "M_source or direct Herm(2) Huv rows remain open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
