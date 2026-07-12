"""Audit phase-lane Yukawa curvature clue diagnostic."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_phaselanecurvatureclue_or_yukawareductiondiagnostic"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET = ROOT / "candidate_data" / SLUG / "phase_lane_curvature_models.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PhaseLaneCurvatureClue_or_YukawaReductionDiagnostic_v1.md"

STATUS = "MTT_SELECTED_PHASELANECURVATURECLUE_OR_YUKAWAREDUCTIONDIAGNOSTIC_BUILT_FITTED_CLUE_SOURCE_OPEN"
NEXT = "MTT_Selected_PhaseLaneCurvatureSourceRelation_or_SevenParameterYukawaReduction_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(CANDIDATE)
    packet = load(PACKET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "cert status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(cert["next_required_artifact"] == NEXT, "cert next")
    require(data["closure_claimed"] is False, "candidate overclosed")
    require(data["observed_data_used_as_selector"] is True, "candidate fitted-data guard")
    require(data["target_fitting_used"] is True, "candidate fitting guard")

    require(packet["status"] == "PHASE_LANE_CURVATURE_CLUE_BUILT_SOURCE_OPEN", "packet status")
    require(packet["source_split_used"]["phase_packet_I_plus_Z"] == ["u", "e"], "phase split")
    require(packet["source_split_used"]["shift_packet_I_plus_X"] == ["d"], "shift split")

    coeffs = packet["curvature_coefficients"]
    require(abs(coeffs["c2_u"] - coeffs["c2_e"]) < 0.006, "u/e curvature clue missing")
    require(coeffs["best_small_rational_for_c2_d_over_phase_gamma_den_le_40"] == "3/11", "3/11 clue missing")
    require(coeffs["best_small_rational_for_phase_gamma_over_c2_d_den_le_40"] == "128/35", "dual rational clue")

    models = packet["model_tests"]
    require(models["quark_only_second_order_with_e_linear"]["status"] == "REJECTED_AS_STRONG_NUMERICAL_MODEL", "quark-only rejection")
    require(models["quark_only_second_order_with_e_linear"]["worst_multiplicative_yukawa_error"] > 5.0, "quark-only error too small")

    phase = models["phase_lane_shared_curvature_d_exact"]
    require(phase["parameter_count"] == 8, "phase model count")
    require(phase["worst_multiplicative_yukawa_error"] < 1.002, "phase clue too weak")
    require(phase["status"] == "VERY_STRONG_FITTED_CLUE_NOT_SOURCE", "phase status")

    seven = models["phase_lane_shared_curvature_shift_ratio_3_over_11"]
    require(seven["parameter_count"] == 7, "seven model count")
    require(seven["ratio_c2_d_to_phase_gamma"] == 3.0 / 11.0, "seven ratio")
    require(seven["worst_multiplicative_yukawa_error"] < 1.002, "seven clue too weak")
    require(seven["status"] == "VERY_STRONG_FITTED_CLUE_NOT_SOURCE", "seven status")

    decision = packet["decision"]
    require(decision["quark_only_second_order_supported"] is False, "quark-only overaccepted")
    require(decision["phase_lane_second_order_supported_as_fitted_clue"] is True, "phase clue rejected")
    require(decision["seven_parameter_near_reduction_supported_as_fitted_clue"] is True, "seven clue rejected")
    require(decision["accepted_as_selected_source_theorem"] is False, "source theorem overclaimed")
    require(decision["accepted_no_knob_yukawa_rows"] == 0, "no-knob rows overaccepted")
    require(decision["observed_data_used_as_selector"] is True, "decision fitted-data guard")
    require(decision["target_fitting_used"] is True, "decision target-fitting guard")

    closure = data["closure_decision"]
    require(closure["quark_only_second_order_rejected_as_fit"] is True, "closure quark-only")
    require(closure["phase_lane_curvature_clue_retained"] is True, "closure phase clue")
    require(closure["seven_parameter_yukawa_near_reduction_retained"] is True, "closure seven clue")
    require(closure["strict_no_knob_flavor_closure"] is False, "strict flavor overclosed")
    require(closure["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(closure["full_no_knob_closed"] is False, "no-knob overclosed")

    require(cert["theorem_target_proved"] is False, "cert theorem overproved")
    require(cert["accepted_as_selected_source_theorem"] is False, "cert source overproved")
    require(cert["accepted_no_knob_yukawa_rows"] == 0, "cert no-knob rows")

    for phrase in [
        "fitted diagnostic, not a selected-source proof",
        "`c2_d / gamma_phase =",
        "`3/11`",
        "quarks only are second order",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
