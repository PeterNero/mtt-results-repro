"""Audit Step 20 conditional atom payload and source-theorem frontier."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step20_conditionalatompayload_or_sourcetheorem"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
CONDITIONAL_PAYLOAD = PACKET_DIR / "step20_conditional_phase_shift_payload.packet.json"
VALIDATION_PACKET = PACKET_DIR / "step20_conditional_normal_form_validation.packet.json"
SOURCE_FRONTIER = PACKET_DIR / "step20_source_theorem_frontier.packet.json"
NEXT_WORKORDER = PACKET_DIR / "step20_to_step21_source_theorem_or_atom_decomposition.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step20_ConditionalAtomPayload_or_SourceTheorem_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP20_CONDITIONAL_ATOM_PAYLOAD_BUILT_SOURCE_THEOREM_OPEN"
NEXT = "MTT_Selected_Step21_SourceTheorem_or_PrimitiveAtomDecomposition_v1"
SECTORS = {"u", "d", "e", "nuD"}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def approx(value: float, expected: float, tol: float = 1e-9) -> bool:
    return abs(value - expected) <= tol


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    payload = load(CONDITIONAL_PAYLOAD)
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

    require(payload["selected_source_selector_closed"] is True, "source selector not closed")
    require(set(payload["aggregate_columns"]["phase_packet"]) == SECTORS, "phase sector mismatch")
    require(set(payload["aggregate_columns"]["shift_packet"]) == SECTORS, "shift sector mismatch")
    require(set(payload["aggregate_columns"]["b_conditional"]) == SECTORS, "b sector mismatch")

    not_selected = payload["conditional_not_selected"]
    for key in [
        "selected_dynamic_transfer_identity_proved",
        "selected_PhiFinC1_identity_promoted",
        "selected_primitive_overlap_contractions_promoted",
        "selected_A_selected_promoted",
        "selected_b_selected_promoted",
    ]:
        require(not_selected[key] is False, f"conditional payload overpromoted: {key}")

    computed = validation["computed"]
    require(computed["A_conditional_shape"] == [72, 2], "A shape mismatch")
    require(approx(computed["A_transpose_A"][0][0], 12.0), "G00 mismatch")
    require(approx(computed["A_transpose_A"][1][1], 12.0), "G11 mismatch")
    require(approx(computed["A_transpose_A"][0][1], 0.0), "G01 mismatch")
    require(approx(computed["A_transpose_A"][1][0], 0.0), "G10 mismatch")
    require(all(approx(x, 12.0) for x in computed["A_transpose_b"]), "A^T b mismatch")
    require(all(approx(x, 1.0) for x in computed["deltaTheta_conditional"]), "deltaTheta mismatch")
    require(approx(computed["b_norm_sq"], 24.0), "b norm mismatch")
    require(approx(computed["phase_shift_reconstruction_residual_norm_sq"], 0.0), "b reconstruction residual mismatch")

    checks = validation["checks"]
    for key in [
        "gram_is_12I2",
        "A_transpose_b_is_12_12",
        "deltaTheta_is_1_1",
        "b_equals_phase_plus_shift",
        "matches_existing_dynamic_transfer_packet",
    ]:
        require(checks[key] is True, f"validation check failed: {key}")
    require(validation["selected_value_status"] == "NOT_PROMOTED_SOURCE_THEOREM_OPEN", "selected status mismatch")

    support = frontier["closed_support"]
    for key in [
        "Step19_sourcevalue_gate",
        "primitive_vertex_source_selector",
        "conditional_phase_shift_payload",
        "conditional_normal_form_validation",
        "transport_only_no_go",
        "stationary_trace_insufficient_for_C1",
    ]:
        require(support[key] is True, f"frontier support missing: {key}")

    not_closed = frontier["not_closed"]
    for key in [
        "selected_source_theorem_for_conditional_payload",
        "six_term_primitive_atom_decomposition",
        "selected_A_selected",
        "selected_b_selected",
        "selected_deltaTheta_C1",
        "Yukawa_or_true_SM_closure",
    ]:
        require(not_closed[key] is True, f"frontier overclosed: {key}")

    decision = data["closure_decision"]
    require(decision["step20_conditional_payload_built"] is True, "Step20 not built")
    require(decision["source_selector_closed"] is True, "source selector not carried")
    require(decision["conditional_normal_form_validated"] is True, "normal form not validated")
    require(decision["selected_source_theorem_for_conditional_payload"] is False, "source theorem overclosed")
    require(decision["six_term_primitive_atom_decomposition_emitted"] is False, "atom decomposition overclosed")
    require(decision["selected_A_selected_promoted"] is False, "A overclosed")
    require(decision["selected_b_selected_promoted"] is False, "b overclosed")
    require(decision["selected_deltaTheta_C1_promoted"] is False, "deltaTheta overclosed")

    require(next_workorder["next_step"] == 21, "next step mismatch")
    require(next_workorder["closed_do_not_reopen"]["conditional_phase_shift_payload"] is True, "payload anti-reopen missing")
    require(next_workorder["must_emit_next"]["aggregate_source_theorem"][0] == "prove Phi_C1_selected(Z)=phase_packet", "aggregate source theorem missing")

    for phrase in [
        "aggregate conditional phase/shift columns                emitted",
        "conditional normal form A^T A = 12 I_2                   validated",
        "Not selected yet:",
        NEXT,
    ]:
        require(phrase in note, f"note missing phrase: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
