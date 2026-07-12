"""Audit finite-projected Yukawa residual-operator attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_yukawafiniteprojectedoperatorresidualsource_or_exactmagnitudeclosure"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SHAPE = PACKET_DIR / "finite_projected_residual_operator_shape.packet.json"
EXECUTION = PACKET_DIR / "antisymmetric_phase_curvature_residual_execution.packet.json"
DECISION = PACKET_DIR / "exact_magnitude_closure_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_YukawaFiniteProjectedOperatorResidualSource_or_ExactMagnitudeClosure_v1.md"

STATUS = "MTT_SELECTED_YUKAWA_FINITEPROJECTEDOPERATORRESIDUALSOURCE_BUILT_PHASESPLIT_SCALAR_SOURCE_OPEN"
NEXT = "MTT_Selected_PhaseAntisymmetryCurvatureScalarSource_or_FinalYukawaMagnitudeClosure_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(CANDIDATE)
    shape = load(SHAPE)
    execution = load(EXECUTION)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "cert status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(cert["next_required_artifact"] == NEXT, "cert next")
    require(data["closure_claimed"] is False, "candidate overclosed")
    require(data["observed_data_used_as_selector"] is True, "candidate observed guard should be true")
    require(data["target_fitting_used"] is True, "candidate fitting guard should be true")

    require(shape["status"] == "FINITE_PROJECTED_RESIDUAL_OPERATOR_SHAPE_CONSTRUCTED", "shape status")
    require(shape["observed_data_used_as_selector"] is False, "shape observed")
    require(shape["target_fitting_used"] is False, "shape fitting")
    require(shape["family_shape_Q"] == [-2.0, 3.0, -1.0], "shape Q")
    require(shape["sector_operator_vector"] == [27.0, 6.0, 26.0], "operator vector")
    require(shape["selected_inputs"]["carrier_dim"] == 27, "carrier dim")
    require(shape["selected_inputs"]["carrier_rank"] == 3, "carrier rank")
    require(shape["selected_inputs"]["carrier_dim_minus_one"] == 26, "carrier dim minus one")
    require(shape["operator_shape_source_constructed"] is True, "shape not constructed")
    require(shape["operator_scalar_source_constructed"] is False, "scalar overconstructed")

    require(execution["status"] == "RESIDUAL_OPERATOR_EXECUTED_NUMERICALLY_SCALAR_SOURCE_OPEN", "execution status")
    require(execution["observed_data_used_as_selector"] is True, "execution observed")
    require(execution["target_fitting_used"] is True, "execution fitting")
    require(execution["operator_shape"] == [27.0, 6.0, 26.0], "execution vector")
    best = execution["best_fit_scalar"]
    require(best["source_accepted"] is False, "best scalar overaccepted")
    require(abs(best["coefficient"] - (-4.401629403164047e-08)) < 1.0e-18, "best coefficient")
    require(best["remaining_max_abs_log_residual"] < 9.0e-9, "best residual")
    phase = execution["phase_antisymmetry_scalar_ansatz"]
    require(phase["source_accepted"] is False, "phase scalar overaccepted")
    require(phase["coefficient_formula"] == "epsilon_theta * s_beta * (c2_u-c2_e)", "phase formula")
    require(abs(phase["c2_u_minus_c2_e"] - (-0.005014603635927539)) < 1.0e-18, "c2 split")
    require(phase["remaining_max_abs_log_residual"] < 1.0e-8, "phase residual")
    require(phase["remaining_worst_multiplicative_yukawa_error"] < 1.00000001, "phase factor")
    require(execution["improvement"]["phase_split_ansatz_error_reduction_factor"] > 400.0, "improvement")

    require(decision["status"] == "RESIDUAL_OPERATOR_SHAPE_BUILT_PHASESPLIT_SCALAR_SOURCE_OPEN", "decision status")
    require(len(decision["closed_now"]) == 3, "closed count")
    require(len(decision["not_closed"]) == 3, "not closed count")
    counts = decision["source_row_counts"]
    require(counts["constructed_residual_operator_shapes"] == 1, "shape count")
    require(counts["accepted_residual_operator_scalar_rows"] == 0, "scalar rows overaccepted")
    require(counts["accepted_exact_yukawa_magnitude_rows"] == 0, "exact rows")
    require(counts["accepted_full_no_knob_yukawa_rows"] == 0, "no-knob rows")
    acceptance = decision["acceptance"]
    require(acceptance["residual_operator_shape_source_constructed"] is True, "accept shape")
    require(acceptance["phase_split_scalar_ansatz_executed"] is True, "accept ansatz")
    require(acceptance["bounded_error_certificate_remains_valid"] is True, "bounded remains")
    require(acceptance["near_exact_after_phase_split_ansatz"] is True, "near exact")
    require(acceptance["phase_split_scalar_source_selected"] is False, "phase scalar selected")
    require(acceptance["strict_exactness_closed"] is False, "strict overclosed")
    require(acceptance["strict_no_knob_yukawa_closure"] is False, "no-knob overclosed")
    require(acceptance["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(decision["next_exact_target"] == NEXT, "decision next")

    require(data["theorem"]["name"] == "YukawaFiniteProjectedResidualOperatorShapeTheorem", "theorem name")
    require(data["theorem"]["proved"] is True, "theorem proved")
    closure = data["closure_decision"]
    require(closure["residual_operator_shape_source_constructed"] is True, "candidate shape")
    require(closure["phase_split_scalar_source_selected"] is False, "candidate scalar")
    require(closure["strict_exactness_closed"] is False, "candidate exactness")
    require(closure["strict_no_knob_yukawa_closure"] is False, "candidate no-knob")

    require(cert["residual_operator_shape_source_constructed"] is True, "cert shape")
    require(cert["phase_split_scalar_ansatz_executed"] is True, "cert ansatz")
    require(cert["phase_split_scalar_source_selected"] is False, "cert scalar")
    require(cert["near_exact_after_phase_split_ansatz"] is True, "cert near exact")
    require(cert["strict_exactness_closed"] is False, "cert exactness")
    require(cert["strict_no_knob_yukawa_closure"] is False, "cert no-knob")
    require(cert["accepted_exact_yukawa_magnitude_rows"] == 0, "cert exact rows")

    for phrase in [
        "`[27,6,26] = [carrier_dim, 2*carrier_rank, carrier_dim-1]`",
        "`epsilon_theta * s_beta * (c2_u-c2_e)`",
        "below `1e-8`",
        "not an independently selected source scalar",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
