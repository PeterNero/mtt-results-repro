"""Audit CONST-HIGGS-01 H7B1Z E_H^UV fill attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_higgs_01_h7b1z_fill_ehuv_finite_basis_or_herm2_values"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
PARTIAL = BASE / "partial_section_basis_quadrature_fill.packet.json"
DIRECT = BASE / "direct_herm2_fill_attempt.packet.json"
CUTSET = BASE / "remaining_payload_cutset.packet.json"
NO_CYCLE = BASE / "non_circulation_ledger.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_HIGGS_01_H7B1Z_FillEHUvFiniteBasisOrHerm2Values_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7B1Z_HYM_GRID_PARTIAL_FILL_EHUV_BINDING_OPEN"
NEXT_ARTIFACT = "MTT_CONST_HIGGS_01_H7B1ZA_EHUvBindingTraceIdentityOrDirectHuvRows_v1"


def load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def clean(packet: dict[str, object], name: str) -> None:
    require(packet["observed_data_used_as_selector"] is False, f"{name} observed selector")
    require(packet["target_fitting_used"] is False, f"{name} target fitting")
    require(packet["closure_claimed"] is False, f"{name} closure overclaim")


def require_all_true(packet: dict[str, object], name: str) -> None:
    for key, value in packet.items():
        require(value is True, f"{name} expected true: {key}")


def require_all_false(packet: dict[str, object], name: str) -> None:
    for key, value in packet.items():
        require(value is False, f"{name} expected false: {key}")


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    computed = json.loads(proc.stdout)
    require(computed["status"] == STATUS, "builder status mismatch")

    candidate = load(DATA)
    partial = load(PARTIAL)
    direct = load(DIRECT)
    cutset = load(CUTSET)
    no_cycle = load(NO_CYCLE)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, packet in [
        ("candidate", candidate),
        ("partial", partial),
        ("direct", direct),
        ("cutset", cutset),
        ("no_cycle", no_cycle),
        ("next_work", next_work),
        ("cert", cert),
    ]:
        clean(packet, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["name"] == "H7B1ZHYMGridPartialFillAndBindingCutsetTheorem", "theorem name")
    require(candidate["theorem"]["proved"] is True, "theorem proved")
    for key in [
        "H7B1Y_imported",
        "H7B1U_HYM_replay_imported",
        "source_HYM_grid_payload_emitted",
        "computational_uniform_quadrature_emitted",
        "HYM_solver_existence_retired_as_blocker",
    ]:
        require(candidate[key] is True, f"candidate missing {key}")
    for key in [
        "selected_E_H_UV_section_basis_emitted",
        "selected_HYM_metric_or_connection_on_E_H_UV_emitted",
        "trace_to_H7B1U_grid_identity_emitted",
        "Higgs_projection_measure_equality_emitted",
        "same_source_no_extra_boundary_source_proof_emitted",
        "direct_Herm2_Huv_payload_emitted",
        "B_Huv_value_emitted",
        "M_source_value_emitted",
        "direct_Huv_entries_emitted",
        "selected_s_beta_value_found",
        "numeric_lambda_H_derived",
        "strict_no_knob_Higgs_closure",
    ]:
        require(candidate[key] is False, f"candidate overclosed {key}")
    require(candidate["new_Higgs_specific_parameters"] == 0, "candidate params")
    require(candidate["selected_next_artifact"] == NEXT_ARTIFACT, "candidate next")

    require(partial["status"] == "HYM_GRID_AND_COMPUTATIONAL_QUADRATURE_FILLED_EHUV_BINDING_OPEN", "partial status")
    branch = partial["branch_identity_partial_fill"]
    require(branch["same_branch_with_H7B1U_grid"] is True, "same branch grid")
    require("q79/F,m=1" in branch["selected_source_branch"], "selected branch text")
    basis = partial["finite_section_basis_partial_fill"]
    require(basis["coordinate_scaffold"]["basis_labels"] == ["H_u", "H_d^dagger"], "basis labels")
    require(basis["coordinate_scaffold"]["quotient_row"] == [1, 1], "quotient row")
    require(basis["accepted_as_actual_finite_sections"] is False, "basis overaccepted")
    require(basis["basis_source_ids"] is None, "basis ids emitted")
    require(basis["section_coordinates"] is None, "section coordinates emitted")
    hym = partial["selected_HYM_data_partial_fill"]
    require(hym["source_HYM_grid_payload_emitted"] is True, "hym grid")
    require(hym["residual_l2"] < 1e-11, "hym residual")
    require(hym["accepted_as_metric_on_E_H_UV"] is False, "hym metric overaccepted")
    quad = partial["quadrature_and_trace_partial_fill"]
    require(quad["computational_uniform_quadrature_emitted"] is True, "quad emitted")
    require(quad["node_count"] == 24**4, "node count")
    require(quad["uniform_weight_rational"] == "1/331776", "weight rational")
    require(quad["accepted_as_physical_Higgs_projection_measure"] is False, "quad physical overaccepted")
    proj = partial["projection_measure_partial_fill"]
    require(proj["trace_to_H7B1U_grid_identity"] is False, "trace identity")
    require(proj["projection_measure_equality"] is False, "measure equality")
    require(proj["selected_s_beta_promoted"] is False, "s beta")
    decision = partial["acceptance_decision"]
    require(decision["source_HYM_grid_payload_emitted"] is True, "decision grid")
    require(decision["computational_uniform_quadrature_emitted"] is True, "decision quad")
    for key, value in decision.items():
        if key not in {"source_HYM_grid_payload_emitted", "computational_uniform_quadrature_emitted"}:
            require(value is False, f"decision overclosed {key}")

    require(direct["status"] == "DIRECT_HERM2_HUV_FILL_ATTEMPT_VALUES_STILL_ABSENT", "direct status")
    for key, value in direct["attempted_outputs"].items():
        require(value is None, f"direct output emitted {key}")
    require_all_false(direct["decision"], "direct decision")
    require(len(direct["why_no_direct_fill"]) == 3, "direct reasons")

    require(cutset["status"] == "HYM_SOLVER_RETIRED_AS_BLOCKER_EHUV_BINDING_AND_HERM2_VALUES_OPEN", "cutset status")
    require_all_true(cutset["retired_as_blockers"], "retired blockers")
    require_all_true(cutset["still_open"], "still open")
    require("not another HYM solve" in cutset["sharp_statement"], "sharp statement")

    require(no_cycle["status"] == "NO_CIRCULATION_LEDGER_UPDATED_H7B1Z", "no cycle status")
    require_all_true(no_cycle["retired_or_do_not_reopen"], "retired")
    require_all_true(no_cycle["active_not_retired"], "active")
    require_all_false(no_cycle["circulation_test"], "circulation")
    require(len(no_cycle["new_information_added"]) == 4, "new info count")

    require(
        next_work["status"] == "NEXT_WORKORDER_H7B1ZA_EHUV_BINDING_TRACE_IDENTITY_OR_DIRECT_HUV_ROWS",
        "next status",
    )
    require(next_work["primary_next"]["artifact"] == NEXT_ARTIFACT, "next artifact")
    require(next_work["primary_next"]["label"].endswith("H7B1ZA-EHUV-BINDING-TRACE-IDENTITY-OR-DIRECT-HUV-ROWS"), "next label")
    require(len(next_work["legal_exits"]) == 2, "next exits")
    require(next_work["superset_strategy"]["combining_paths"] is True, "superset combining")
    require(next_work["superset_strategy"]["using_one_straight_way"] is False, "superset paths")

    require(cert["status"] == STATUS, "cert status")
    require(cert["source_HYM_grid_payload_emitted"] is True, "cert grid")
    require(cert["computational_uniform_quadrature_emitted"] is True, "cert quad")
    require(cert["HYM_solver_existence_retired_as_blocker"] is True, "cert solver retired")
    for key in [
        "selected_E_H_UV_section_basis_emitted",
        "selected_HYM_metric_or_connection_on_E_H_UV_emitted",
        "trace_to_H7B1U_grid_identity_emitted",
        "direct_Herm2_Huv_payload_emitted",
        "selected_s_beta_value_found",
        "numeric_lambda_H_derived",
        "strict_no_knob_Higgs_closure",
    ]:
        require(cert[key] is False, f"cert overclosed {key}")
    require(cert["new_Higgs_specific_parameters"] == 0, "cert params")

    require("source HYM grid payload emitted              True" in note, "note grid")
    require("selected E_H^UV finite section basis emitted False" in note, "note basis")
    require("direct Herm2 Huv payload emitted             False" in note, "note direct")
    require("H7B1ZA-EHUV-BINDING-TRACE-IDENTITY-OR-DIRECT-HUV-ROWS" in note, "note next")

    print("CONST-HIGGS-01 H7B1Z E_H^UV fill attempt audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
