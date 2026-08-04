"""Audit final finite-replay Yukawa residual exactness."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_finalyukawareplayresidualexactness_or_strictsmnoknobclosure"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
TAIL_ROWS = PACKET_DIR / "selected_finite_tail_source_rows.packet.json"
REPLAY = PACKET_DIR / "final_finite_replay_exactness_execution.packet.json"
DECISION = PACKET_DIR / "strict_sm_noknob_closure_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_FinalYukawaReplayResidualExactness_or_StrictSMNoKnobClosure_v1.md"

STATUS = "MTT_SELECTED_FINALYUKAWAREPLAYRESIDUALEXACTNESS_BUILT_FINITE_REPLAY_YUKAWA_CLOSED_TRUE_SM_OPEN"
NEXT = "MTT_Selected_TrueSMNoKnobClosure_GlobalLedger_or_RemainingNonYukawaRows_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(CANDIDATE)
    tail_rows = load(TAIL_ROWS)
    replay = load(REPLAY)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "cert status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(cert["next_required_artifact"] == NEXT, "cert next")
    require(data["closure_claimed"] is False, "candidate global overclosed")
    require(data["observed_data_used_as_selector"] is False, "candidate observed selector")
    require(data["target_fitting_used"] is False, "candidate target fitting")

    require(tail_rows["status"] == "TWO_FINITE_TAIL_SOURCE_ROWS_EMITTED", "tail status")
    require(tail_rows["observed_data_used_as_selector"] is False, "tail observed selector")
    require(tail_rows["target_fitting_used"] is False, "tail target fitting")
    inputs = tail_rows["selected_inputs"]
    require(inputs["q64"] == 15, "q64")
    require(inputs["q7"] == 2, "q7")
    require(inputs["q_residue_mod_448"] == 79, "q residue")
    require(inputs["q_mod"] == 448, "q mod")
    require(inputs["carrier_rank"] == 3, "carrier rank")
    require(inputs["projector_rank"] == 2, "projector rank")
    require(inputs["z7_order"] == 7, "z7")
    rows = tail_rows["rows"]
    require(len(rows) == 2, "tail row count")
    endpoint = rows[0]
    require(endpoint["id"] == "endpoint_conjugate_tail", "endpoint id")
    require(endpoint["sector_vector"] == [27.0, 6.0, -26.0], "endpoint vector")
    require(
        endpoint["coefficient_formula"] == "epsilon_theta * s_beta^2 * (q64+1)/(q64*q_mod)",
        "endpoint formula",
    )
    require(abs(endpoint["coefficient"] - 9.826390233522832e-11) < 1.0e-22, "endpoint coefficient")
    require(endpoint["accepted_as_source_row"] is True, "endpoint accepted")
    z7 = rows[1]
    require(z7["id"] == "z7_mixed_tail", "z7 id")
    require(z7["sector_vector"] == [0.0, 1.0, -4.2], "z7 vector")
    require(z7["coefficient_formula"] == "epsilon_theta * s_beta^3 / (q64*z7_order-q7)", "z7 formula")
    require(abs(z7["coefficient"] - 1.883666766188459e-12) < 1.0e-24, "z7 coefficient")
    require(z7["accepted_as_source_row"] is True, "z7 accepted")

    require(replay["status"] == "FINAL_FINITE_REPLAY_RESIDUAL_BELOW_SELECTED_HYM_REPLAY_FLOOR", "replay status")
    require(replay["observed_data_used_as_selector"] is False, "replay observed selector")
    require(replay["target_fitting_used"] is False, "replay target fitting")
    require(replay["family_shape_Q"] == [-2.0, 3.0, -1.0], "family shape")
    require(replay["imported_H_scalar_replay_floor"] == 8.208178923714022e-13, "floor")
    final = replay["after_z7_mixed_tail"]
    require(abs(final["max_abs_log_residual"] - 8.715792346058762e-14) < 1.0e-24, "final residual")
    require(final["max_abs_log_residual"] < replay["imported_H_scalar_replay_floor"], "residual above floor")
    require(replay["final_residual_floor_ratio"] < 0.11, "floor ratio")
    require(replay["finite_replay_exactness_closed"] is True, "finite exactness not closed")
    require(replay["analytic_zero_residual"] is False, "analytic zero overclosed")

    require(
        decision["status"] == "FINITE_REPLAY_YUKAWA_MAGNITUDE_CLOSED_ANALYTIC_ZERO_AND_GLOBAL_SM_OPEN",
        "decision status",
    )
    require(len(decision["closed_now"]) == 4, "closed count")
    require(len(decision["not_closed"]) == 3, "not closed count")
    counts = decision["source_row_counts"]
    require(counts["accepted_strict_phase_antisymmetry_scalar_source_rows"] == 1, "phase scalar count")
    require(counts["accepted_finite_tail_source_rows"] == 2, "tail count")
    require(counts["accepted_finite_replay_yukawa_magnitude_rows"] == 9, "finite replay rows")
    require(counts["accepted_analytic_zero_yukawa_rows"] == 0, "analytic rows overaccepted")
    require(counts["accepted_global_true_sm_no_knob_rows"] == 0, "global rows overaccepted")
    acceptance = decision["acceptance"]
    require(acceptance["finite_tail_source_rows_emitted"] is True, "tail emitted")
    require(acceptance["finite_replay_yukawa_exactness_closed"] is True, "finite replay")
    require(acceptance["fitted_yukawa_magnitudes_retired_for_source_selection"] is True, "fitted retired")
    require(acceptance["analytic_zero_residual_closed"] is False, "analytic zero")
    require(acceptance["strict_no_knob_yukawa_closure_at_finite_replay_standard"] is True, "finite no-knob")
    require(acceptance["global_true_SM_no_knob_closure"] is False, "global closure")
    require(acceptance["true_SM_equivalence_closed"] is False, "true SM closure")
    require(decision["next_exact_target"] == NEXT, "decision next")

    require(data["theorem"]["name"] == "FinalFiniteReplayYukawaResidualExactnessTheorem", "theorem name")
    require(data["theorem"]["proved"] is True, "theorem proved")
    require(data["closure_decision"] == acceptance, "closure copy")
    require(cert["finite_tail_source_rows_emitted"] is True, "cert tail")
    require(cert["accepted_finite_tail_source_rows"] == 2, "cert tail count")
    require(cert["finite_replay_yukawa_exactness_closed"] is True, "cert finite replay")
    require(cert["accepted_finite_replay_yukawa_magnitude_rows"] == 9, "cert finite rows")
    require(cert["analytic_zero_residual_closed"] is False, "cert analytic zero")
    require(cert["global_true_SM_no_knob_closure"] is False, "cert global")
    require(cert["true_SM_equivalence_closed"] is False, "cert true SM")
    require(cert["observed_data_used_as_selector"] is False, "cert observed selector")
    require(cert["target_fitting_used"] is False, "cert target fitting")

    for phrase in [
        "`[27,6,-26]`",
        "`[0,1,-21/5]`",
        "finite-replay Yukawa magnitude exactness is accepted",
        "not analytic zero residual",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
