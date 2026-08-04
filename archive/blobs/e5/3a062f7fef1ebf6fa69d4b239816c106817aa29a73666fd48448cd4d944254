"""Audit Step71 SM-parity matrix comparison / row-local target extraction."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step71_smparitymatrixcomparison_or_rowlocaltargets"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
MATRIX_PROJECTION_PACKET = PACKET_DIR / "step71_smparity_matrix_diagonal_projection.packet.json"
ROWLOCAL_TARGET_PACKET = PACKET_DIR / "step71_rowlocal_composite_target_contract.packet.json"
SCOPE_PACKET = PACKET_DIR / "step71_matrix_scope_comparison.packet.json"
GAP_RECONCILIATION_PACKET = PACKET_DIR / "step71_old_smparity_gap_matrix_reconciliation.packet.json"
CUTSET_PACKET = PACKET_DIR / "step71_next_rowlocal_execution_cutset.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step71_SMParityMatrixComparison_or_RowLocalTargets_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP71_SMPARITY_MATRIX_COMPARISON_BUILT_ROWLOCAL_TARGETS_OPEN"
NEXT = "MTT_Selected_RowLocalHYMOverlapThresholdPrefactors_or_StrictOmegaAcceptance_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)
    data = load(DATA)
    projection = load(MATRIX_PROJECTION_PACKET)
    rowlocal = load(ROWLOCAL_TARGET_PACKET)
    scope = load(SCOPE_PACKET)
    gap = load(GAP_RECONCILIATION_PACKET)
    cutset = load(CUTSET_PACKET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "candidate theorem missing")
    require(cert["theorem_proved"] is True, "certificate theorem missing")

    for item in [data, projection, rowlocal, scope, gap, cutset, cert]:
        require(item.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(item.get("target_fitting_used") is False, "target fitting violation")

    require(projection["status"] == "SM_PARITY_REPLAY_MATRIX_PROJECTED_TO_STEP70_SCALAR_SLOTS", "projection status mismatch")
    branch = projection["selected_source_branch"]
    require(
        branch["q"] == 79 and branch["orientation"] == "F" and branch["torsion_m"] == 1,
        "branch mismatch",
    )
    require("source_packet" in branch, "branch provenance missing")
    acceptance = projection["value_row_acceptance"]
    require(acceptance["accepted_for_SM_parity"] is True, "SM-parity acceptance missing")
    require(acceptance["accepted_as_no_knob_MTT_prediction"] is False, "replay matrix overpromoted")
    require(acceptance["accepted_internal_scalar_row_count"] == 0, "internal scalar rows overaccepted")
    require(projection["diagonal_projection_row_count"] == 10, "projection row count mismatch")
    require(projection["matrix_projection_matches_declared_common_scale_magnitudes"] is True, "projection mismatch")
    require(projection["accepted_as_no_knob_source"] is False, "projection source overaccepted")
    require(projection["accepted_internal_scalar_row_count"] == 0, "projection scalar rows overaccepted")

    summaries = projection["matrix_summaries"]
    require(summaries["u"]["offdiag_to_frob_ratio"] < 1e-20, "Y_u should be effectively diagonal")
    require(summaries["e"]["offdiag_to_frob_ratio"] == 0.0, "Y_e should be diagonal")
    require(summaries["d"]["offdiag_to_frob_ratio"] > 0.01, "Y_d CKM offdiag content missing")
    require(summaries["d"]["contains_ckm_or_mixing_replay"] is True, "Y_d mixing flag missing")

    rows = projection["diagonal_projection_rows"]
    require({row["omega_id"] for row in rows} == {
        "Omega_u.gen1",
        "Omega_u.gen2",
        "Omega_u.gen3",
        "Omega_d.gen1",
        "Omega_d.gen2",
        "Omega_d.gen3",
        "Omega_e.gen1",
        "Omega_e.gen2",
        "Omega_e.gen3",
        "Omega_H.lambda",
    }, "projection Omega set mismatch")
    for row in rows:
        require(row["covered_by_step70_diagonal_scalar_contract"] is True, f"row not covered {row['omega_id']}")
        require(row["accepted_as_source_row"] is False, f"projection row overpromoted {row['omega_id']}")
        require(row["accepted_as_omega_source_row"] is False, f"Omega row overpromoted {row['omega_id']}")
        require("D_fin." in row["step70_prefactor_factorization"], f"factorization missing D_fin {row['omega_id']}")

    targets = rowlocal["target_rows"]
    require(rowlocal["target_row_count"] == 10, "target row count mismatch")
    require(rowlocal["closed_source_subslots"]["theta_weight"] is True, "theta subslot missing")
    require(rowlocal["closed_source_subslots"]["finite_heat_torsion_subfactor"] is True, "heat subslot missing")
    require(rowlocal["open_source_subslots"]["selected_rowlocal_overlap_factor"] is True, "rowlocal open flag missing")
    require(rowlocal["open_source_subslots"]["selected_threshold_scheme_factor"] is True, "scheme open flag missing")
    require(rowlocal["accepted_rowlocal_source_row_count"] == 0, "rowlocal source rows overaccepted")
    require(rowlocal["accepted_full_prefactor_source_row_count"] == 0, "prefactor rows overaccepted")
    require(rowlocal["accepted_omega_source_row_count"] == 0, "Omega rows overaccepted")
    for row in targets:
        require("/ D_fin." in row["rowlocal_composite_target_symbolic"], f"symbolic target missing D_fin {row['omega_id']}")
        require(row["accepted_as_rowlocal_source_target"] is False, f"target overaccepted {row['omega_id']}")
        require(row["accepted_as_full_prefactor_source_row"] is False, f"prefactor overaccepted {row['omega_id']}")
        require(row["closed_subsources"]["sm_parity_matrix_projection_for_postcheck"] is True, "postcheck projection missing")
        require(row["closed_subsources"]["selected_rowlocal_overlap_factor"] is False, "rowlocal overclosed")
        require(row["closed_subsources"]["selected_threshold_scheme_factor"] is False, "scheme overclosed")

    comparison = scope["comparison"]
    require(comparison["same_branch"] is True, "same branch comparison missing")
    require(comparison["diagonal_magnitude_projection_aligned"] is True, "diagonal alignment missing")
    require(comparison["step70_covers_diagonal_scalar_slots"] is True, "diagonal coverage missing")
    require(comparison["step70_covers_ckm_offdiagonal_matrix"] is False, "CKM overclaimed")
    require(comparison["step70_covers_pmns_or_neutrino_mixing"] is False, "PMNS overclaimed")
    require(scope["matrix_scope_metrics"]["Y_d_offdiag_to_frob_ratio"] > 0.01, "Y_d metric missing")

    require(gap["old_gap_matrix_status"] == "FINAL_GAP_MATRIX_BUILT_NOT_CLOSED", "old gap status mismatch")
    require(gap["old_primary_open_sm_parity_gate"] == "common_scale_Yukawa_and_Higgs_transport", "old primary gate mismatch")
    current = gap["current_status_after_later_artifacts"]
    require(current["common_scale_Yukawa_Higgs_replay_values_available"] is True, "common-scale values not available")
    require(current["step42_executable_admitted_replay_solution_closed"] is True, "Step42 replay missing")
    require(current["old_full_no_knob_constants_blocker_refined_to_rowlocal_factors"] is True, "no-knob refinement missing")

    for phrase in [
        "selected row-local HYM zero-mode overlap factors L_rowlocal.*",
        "selected threshold/scale/scheme factors T_scheme.*",
        "selected CKM/down-sector offdiagonal physical matrix theorem",
    ]:
        require(phrase in cutset["still_missing_for_scalar_rows"] or phrase in cutset["still_missing_for_full_physical_matrices"], f"cutset missing {phrase}")
    for phrase in [
        "use the SM-parity replay matrix as a source selector for row-local factors",
        "claim Step70 derives CKM/offdiagonal matrix entries",
        "claim diagnostic row-local composite targets are selected HYM overlap values",
    ]:
        require(phrase in cutset["forbidden_routes"], f"forbidden route missing {phrase}")

    decision = data["closure_decision"]
    for key in [
        "smparity_matrix_comparison_closed",
        "diagonal_projection_to_step70_slots_closed",
        "rowlocal_composite_target_contract_built",
        "old_smparity_gap_matrix_reconciled",
        "scope_split_diagonal_scalar_vs_mixing_closed",
    ]:
        require(decision[key] is True, f"decision did not close {key}")
        require(cert[key] is True, f"certificate did not close {key}")
    for key in [
        "selected_rowlocal_overlap_factors_closed",
        "selected_threshold_scheme_factors_closed",
        "selected_ckm_offdiagonal_matrix_derived",
        "lambda_H_value_row_emitted",
        "scalar_value_execution_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed {key}")
        require(cert[key] is False, f"certificate overclosed {key}")
    require(decision["accepted_rowlocal_source_row_count"] == 0, "decision rowlocal rows overaccepted")
    require(decision["accepted_omega_source_row_count"] == 0, "decision Omega rows overaccepted")

    for phrase in [
        "diagonal projection rows: 10",
        "accepted row-local source rows: 0",
        "Y_d offdiag/frob",
        "outside the current scalar-prefactor closure",
        "older final SM-parity gap matrix was a gate/blocker matrix",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
