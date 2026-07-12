"""Audit Step 21 conditional atom decomposition and vertex-source frontier."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step21_conditional_atomdecomposition_or_vertexsource"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
DECOMP_PACKET = PACKET_DIR / "step21_conditional_sixterm_atom_decomposition.packet.json"
VALIDATION_PACKET = PACKET_DIR / "step21_atom_decomposition_validation.packet.json"
SOURCE_FRONTIER = PACKET_DIR / "step21_vertex_source_theorem_frontier.packet.json"
NEXT_WORKORDER = PACKET_DIR / "step21_to_step22_vertex_source_or_selected_values.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step21_ConditionalAtomDecomposition_or_VertexSource_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP21_CONDITIONAL_ATOM_DECOMPOSITION_BUILT_VERTEX_SOURCE_OPEN"
NEXT = "MTT_Selected_Step22_VertexSourceTheorem_or_SelectedASelectedBSelected_v1"
SECTORS = {"u", "d", "e", "nuD"}
DIRECTIONS = {"phase_Z", "shift_X"}
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
    decomp = load(DECOMP_PACKET)
    validation = load(VALIDATION_PACKET)
    frontier = load(SOURCE_FRONTIER)
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

    require(decomp["decomposition_policy"]["name"] == "vertex_only_conditional_representative", "wrong decomposition policy")
    require(set(decomp["direction_order"]) == DIRECTIONS, "direction mismatch")
    require(set(decomp["sector_order"]) == SECTORS, "sector mismatch")
    require(set(decomp["term_order"]) == TERMS, "term mismatch")
    require(set(decomp["conditional_atom_terms"]) == DIRECTIONS, "conditional directions mismatch")
    for direction in DIRECTIONS:
        require(set(decomp["conditional_atom_terms"][direction]) == SECTORS, f"sector mismatch for {direction}")
        for sector in SECTORS:
            terms = decomp["conditional_atom_terms"][direction][sector]
            require(set(terms) == TERMS, f"term set mismatch for {direction}/{sector}")
            require(terms["explicit_vertex"] == decomp["reconstructed_aggregate_columns"][direction][sector], f"explicit vertex mismatch for {direction}/{sector}")
    selected_status = decomp["selected_status"]
    for key in [
        "selected_vertex_source_theorem_proved",
        "selected_sixterm_atom_decomposition_emitted",
        "selected_A_selected_promoted",
        "selected_b_selected_promoted",
    ]:
        require(selected_status[key] is False, f"decomposition overpromoted: {key}")

    require(validation["max_reconstruction_residual"] < 1e-12, "reconstruction residual too large")
    require(validation["checks"]["reconstructs_phase_shift_columns"] is True, "reconstruction check failed")
    require(validation["checks"]["normal_form_still_valid"] is True, "normal form not preserved")
    require(validation["checks"]["selected_values_not_promoted"] is True, "selected values promoted")
    require(validation["template_compatibility"]["formula_slots_match"] is True, "formula slot mismatch")
    require(validation["template_compatibility"]["sector_order_match"] is True, "sector order mismatch")
    require(validation["template_compatibility"]["coordinate_system_match"] is True, "coordinate mismatch")

    support = frontier["closed_support"]
    for key in [
        "Step20_conditional_payload",
        "conditional_sixterm_decomposition",
        "aggregate_reconstruction_validated",
        "source_selector_attached",
    ]:
        require(support[key] is True, f"frontier support missing: {key}")
    not_closed = frontier["not_closed"]
    for key in [
        "selected_vertex_source_theorem",
        "selected_replacement_sixterm_decomposition",
        "selected_A_selected",
        "selected_b_selected",
        "selected_deltaTheta_C1",
        "Yukawa_or_true_SM_closure",
    ]:
        require(not_closed[key] is True, f"frontier overclosed: {key}")

    decision = data["closure_decision"]
    require(decision["step21_conditional_decomposition_built"] is True, "Step21 not built")
    require(decision["conditional_decomposition_reconstructs_aggregate"] is True, "aggregate not reconstructed")
    require(decision["max_reconstruction_residual"] < 1e-12, "candidate residual too large")
    require(decision["selected_vertex_source_theorem_proved"] is False, "vertex theorem overclosed")
    require(decision["selected_replacement_sixterm_decomposition_emitted"] is False, "selected replacement overclosed")
    require(decision["selected_A_selected_promoted"] is False, "A overclosed")
    require(decision["selected_b_selected_promoted"] is False, "b overclosed")

    require(next_workorder["next_step"] == 22, "next step mismatch")
    require(next_workorder["closed_do_not_reopen"]["conditional_sixterm_decomposition"] is True, "anti-reopen missing")
    require(next_workorder["success_criterion"]["selected_vertex_source_or_replacement_decomposition"] is True, "success criterion missing")

    for phrase in [
        "conditional aggregate phase/shift columns decomposed into six-term atom schema",
        "Still not selected:",
        "selected vertex source theorem",
        NEXT,
    ]:
        require(phrase in note, f"note missing phrase: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
