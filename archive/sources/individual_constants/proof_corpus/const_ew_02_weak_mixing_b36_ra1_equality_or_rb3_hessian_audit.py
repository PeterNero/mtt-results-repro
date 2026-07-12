"""Audit CONST-EW-02 B36 RA-1 equality/RB-3 Hessian artifact."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_ew_02_weak_mixing_b36_ra1_equality_or_rb3_hessian"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
RA1 = BASE / "route_a_ra1_physical_action_equality_import.packet.json"
RB3 = BASE / "route_b_rb3_hessian_source_fill_import.packet.json"
BOUNDARY = BASE / "weak_mixing_b36_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_EW_02_WeakMixing_B36_RA1_Equality_or_RB3_Hessian_v1.md"

STATUS = "MTT_CONST_EW_02_B36_RA1_EQUALITY_OR_RB3_HESSIAN_BUILT"


def load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def clean(packet: dict[str, object], name: str) -> None:
    require(packet["observed_data_used_as_selector"] is False, f"{name} observed selector")
    require(packet["target_fitting_used"] is False, f"{name} target fitting")
    require(packet["closure_claimed"] is False, f"{name} closure overclaim")


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
    ra1 = load(RA1)
    rb3 = load(RB3)
    boundary = load(BOUNDARY)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, item in [
        ("candidate", candidate),
        ("ra1", ra1),
        ("rb3", rb3),
        ("boundary", boundary),
    ]:
        clean(item, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["RA1_physical_action_equality_claimed"] is False, "RA1 equality overclaimed")
    require(candidate["RA1_reduced_to_RA2_boundary_source_cancellation"] is True, "RA1 reduction missing")
    require(candidate["RB3_hessian_source_normal_equations_filled"] is True, "RB3 fill missing")
    require(candidate["RB3_selected_hessian_source_emitted"] is False, "RB3 source overemitted")
    require(candidate["RB3_computed_from_independent_galerkin_quadrature"] is False, "RB3 independent overclaimed")
    require(candidate["RB3_positive_definite_support_hessian"] is True, "RB3 Hessian not positive")
    require(candidate["source_promotion_closed_now"] is False, "source promotion overclosed")
    require(candidate["physical_weak_angle_closure"] is False, "weak angle overclosed")

    require(ra1["clause_id"] == "RA-1", "RA1 id")
    require(ra1["physical_action_equality_claimed"] is False, "RA1 packet overclaimed")
    result = ra1["current_RA1_result"]
    require(result["RA1a_physical_action_candidate_identified"] is True, "RA1a missing")
    require(result["RA1b_first_variation_equality_not_proved"] is True, "RA1b should remain open")
    require(result["RA1d_boundary_source_terms_split_to_RA2"] is True, "RA2 split missing")

    support = rb3["hessian_source_support"]
    require(rb3["input_id"] == "RB-3", "RB3 id")
    require(rb3["primitive_row_count"] == 72, "primitive row count")
    require(support["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "A^T A mismatch")
    require(support["A_transpose_b"] == [12.0, 12.0], "A^T b mismatch")
    require(support["deltaTheta_C1_support_solution"] == [1.0, 1.0], "deltaTheta mismatch")
    require(support["determinant"] == 144.0, "det mismatch")
    require(support["positive_definite_support_hessian"] is True, "Hessian positivity")
    require(rb3["selected_hessian_source_emitted"] is False, "selected Hessian overemitted")
    require(rb3["source_owner_verified"] is False, "source owner oververified")
    require(rb3["residual_replay_dependency"] is True, "residual dependency should remain")

    require(boundary["closed_or_sharpened_now"]["ROUTE_B_RB3_hessian_source_normal_equations_filled"] is True, "boundary RB3")
    require(boundary["still_open"]["RA2_selected_boundary_source_cancellation"] is True, "RA2 open")
    require(boundary["still_open"]["RB4_independent_selected_quadrature_source"] is True, "RB4 open")
    require(boundary["still_open"]["selected_hessian_source_emitted"] is True, "selected hessian open")
    require(boundary["still_open"]["physical_weak_angle_closure"] is True, "weak angle open")
    require("not promoting residual-replay support as selected source" in boundary["anti_cycle_delta_from_B35"]["not_repeated"], "anti-cycle guard")

    require(cert["status"] == STATUS, "cert status")
    require(cert["RA1_reduced_to_RA2_boundary_source_cancellation"] is True, "cert RA1")
    require(cert["RB3_hessian_source_normal_equations_filled"] is True, "cert RB3")
    require(cert["RB3_selected_hessian_source_emitted"] is False, "cert source")
    require(next_work["primary"]["label"] == "CONST-EW-02 / WEAK-MIXING / B37-ROUTEA-RA2-BOUNDARY-SOURCE-CANCELLATION", "next primary")
    require(next_work["parallel"]["label"] == "CONST-EW-02 / WEAK-MIXING / B37-ROUTEB-RB4-INDEPENDENT-QUADRATURE-SOURCE", "next parallel")
    require("A^T A" in note, "note Hessian")
    require("B37" in note, "note next")

    print("CONST-EW-02 B36 RA1 equality/RB3 Hessian audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
