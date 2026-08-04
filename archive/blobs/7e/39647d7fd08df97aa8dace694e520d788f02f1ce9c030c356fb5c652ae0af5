"""Audit SM-equivalence mixing and gauge replay."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "sm_equivalence_mixing_and_gauge_replay.candidate.json"
CERT = ROOT / "certificates" / "sm_equivalence_mixing_and_gauge_replay_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_SM_Equivalence_Mixing_and_Gauge_Replay_v1.md"
BUILDER = ROOT / "scripts" / "build_sm_equivalence_mixing_and_gauge_replay.py"

STATUS = "MTT_SM_EQUIVALENCE_MIXING_AND_GAUGE_REPLAY_BUILT_PARTIAL_EMPIRICAL_REPLAY"
NEXT = "MTT_SM_Equivalence_Common_RG_and_Empirical_Audit_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")

    superset = data["superset_strategy_use"]
    require(superset["mode"] == "SUPERSET_TO_LOCKED_SOURCE_THEN_STRAIGHT_MEASURED_REPLAY", "superset mode mismatch")
    require(superset["measured_targets_used_to_lock_source"] is False, "measured targets used as source selectors")
    require(superset["straight_replay_after_boundary"] is True, "straight replay flag missing")

    ckm = data["CKM_replay"]
    require(ckm["status"] == "FULL_COMPLEX_DOWN_YUKAWA_REPLAY_READY_IN_UP_DIAGONAL_CONVENTION", "CKM status mismatch")
    require(ckm["basis_convention"] == "Y_u diagonal; Y_d = V_CKM diag(y_d)", "CKM basis mismatch")
    require(ckm["unitarity_max_residual"] < 1e-12, "CKM unitarity residual too large")
    require(ckm["down_hermitian_reconstruction_residual"] < 1e-18, "CKM down Hermitian residual too large")
    require(abs(ckm["input_jarlskog"]) > 1e-6, "CKM CP invariant missing")
    require(ckm["used_as_source_selector"] is False, "CKM used as source selector")
    require(len(ckm["Y_d_complex"]) == 3 and len(ckm["Y_d_complex"][0]) == 3, "Y_d matrix shape mismatch")

    pmns = data["PMNS_replay"]
    require(pmns["status"] == "OSCILLATION_MASS_SQUARED_REPLAY_READY_ABSOLUTE_MASS_OPEN", "PMNS status mismatch")
    require(pmns["unitarity_max_residual"] < 1e-12, "PMNS unitarity residual too large")
    require(pmns["diagonalization_max_residual_eV2"] < 1e-18, "PMNS diagonalization residual too large")
    require(abs(pmns["Delta_m21_sq_residual_eV2"]) < 1e-18, "Delta m21 residual too large")
    require(abs(pmns["Delta_m3l_sq_residual_eV2"]) < 1e-18, "Delta m3l residual too large")
    require(abs(pmns["input_jarlskog"]) > 1e-3, "PMNS CP invariant missing")
    require(pmns["absolute_neutrino_mass_filled"] is False, "absolute neutrino mass overclaimed")
    require(pmns["Dirac_neutrino_yukawa_magnitudes_filled"] is False, "Dirac neutrino Yukawa overclaimed")
    require(pmns["used_as_source_selector"] is False, "PMNS used as source selector")

    gauge = data["gauge_replay_MZ"]
    require(gauge["status"] == "ALPHA1_ALPHA2_ALPHA3_MZ_REPLAY_READY_WITHOUT_RG_TRANSPORT", "gauge status mismatch")
    inputs = gauge["filled_inputs"]
    alpha_em = inputs["alpha_em_MSbar_MZ"]["central_value"]
    sin2 = inputs["sin2_thetaW_MSbar_MZ"]["central_value"]
    alpha_s = inputs["alpha_s_MZ"]["central_value"]
    triplet = gauge["numeric_triplet"]
    require(abs(triplet["alpha_Y"]["central_value"] - alpha_em / (1.0 - sin2)) < 1e-15, "alpha_Y formula mismatch")
    require(abs(triplet["alpha_1_GUT"]["central_value"] - (5.0 / 3.0) * alpha_em / (1.0 - sin2)) < 1e-15, "alpha_1 formula mismatch")
    require(abs(triplet["alpha_2"]["central_value"] - alpha_em / sin2) < 1e-15, "alpha_2 formula mismatch")
    require(abs(triplet["alpha_3"]["central_value"] - alpha_s) < 1e-15, "alpha_3 formula mismatch")
    for key in ["alpha_1_GUT", "alpha_2", "alpha_3"]:
        require(triplet[key]["central_value"] > 0.0, f"{key} not positive")
    require(abs(triplet["g_1_GUT"]["central_value"] - math.sqrt(4.0 * math.pi * triplet["alpha_1_GUT"]["central_value"])) < 1e-15, "g1 formula mismatch")
    require(abs(triplet["g_2"]["central_value"] - math.sqrt(4.0 * math.pi * triplet["alpha_2"]["central_value"])) < 1e-15, "g2 formula mismatch")
    require(abs(triplet["g_3"]["central_value"] - math.sqrt(4.0 * math.pi * triplet["alpha_3"]["central_value"])) < 1e-15, "g3 formula mismatch")
    require(gauge["used_as_source_selector"] is False, "gauge values used as source selector")

    tests = data["replay_tests"]
    for key in [
        "CKM_complex_Yukawa_matrix_built",
        "CKM_unitarity_replayed",
        "CKM_down_Hermitian_reconstructed",
        "PMNS_mass_squared_matrix_built",
        "PMNS_unitarity_replayed",
        "PMNS_mass_splittings_replayed",
        "gauge_alpha1_alpha2_alpha3_values_ready",
    ]:
        require(tests[key] is True, f"replay test not closed: {key}")
    for key in [
        "common_RG_scale_transport_done",
        "full_covariance_ready",
        "empirical_equivalence_audit_done",
        "full_SM_equivalence_replay_done",
        "full_no_knob_closure_done",
    ]:
        require(tests[key] is False, f"overclaimed replay test: {key}")

    closes = data["what_closes_now"]
    for key in [
        "CKM_complex_Yukawa_replay",
        "PMNS_oscillation_mass_squared_replay",
        "alpha1_alpha2_alpha3_MZ_numeric_triplet",
        "mixing_and_gauge_replay_executable",
        "source_selection_guardrails_preserved",
    ]:
        require(closes[key] is True, f"close flag missing: {key}")

    remains = data["what_remains_open"]
    for key in [
        "CKM_covariance_or_profile_policy",
        "PMNS_covariance_or_profile_policy",
        "absolute_neutrino_mass_and_Dirac_Yukawa_scale",
        "common_RG_scale_transport",
        "loop_order_and_threshold_policy",
        "empirical_equivalence_audit_run",
        "full_SM_equivalence_closure",
        "full_no_knob_closure",
    ]:
        require(remains[key] is True, f"remaining gate missing: {key}")

    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["sm_equivalence_claimed"] is False, "SM equivalence overclaimed")
    require(data["no_knob_closure_claimed"] is False, "no-knob overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used as selector")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(data["source_boundary_preserved"] is True, "source boundary not preserved")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require("straight SM-standard measured replay" in note, "note missing replay standard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
