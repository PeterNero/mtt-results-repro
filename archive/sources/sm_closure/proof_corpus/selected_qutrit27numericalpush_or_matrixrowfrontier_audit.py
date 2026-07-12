"""Audit selected qutrit 27x27 numerical push / matrix-row frontier."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_qutrit27numericalpush_or_matrixrowfrontier"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SPECTRAL = PACKET_DIR / "qutrit27_spectral_diagnostics.packet.json"
PROFILE = PACKET_DIR / "charged_row_profile_diagnostics.packet.json"
SEARCH = PACKET_DIR / "matrix_functional_candidate_search.packet.json"
H_PACKET = PACKET_DIR / "h_row_frontier_after_27_push.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Qutrit27NumericalPush_or_MatrixRowFrontier_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_QUTRIT27NUMERICALPUSH_OR_MATRIXROWFRONTIER_"
    "SPECTRAL_DIAGNOSTICS_CLOSED_CHARGED_PROFILE_EXTRACTED_H_OPEN"
)
NEXT = "MTT_Selected_StrictFiniteHSourceRowConstruction_or_NonHiggsHRGPrediction_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("closure_claimed") is True, f"{label} closure flag")
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    spectral = load(SPECTRAL)
    profile = load(PROFILE)
    search = load(SEARCH)
    h_packet = load(H_PACKET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("spectral", spectral),
        ("profile", profile),
        ("search", search),
        ("h_packet", h_packet),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "certificate status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(cert["next_required_artifact"] == NEXT, "certificate next")
    require(data["theorem"]["proved"] is True, "theorem")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaim")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaim")

    require(spectral["carrier_dimension"] == 27, "carrier dimension")
    checks = spectral["relation_checks"]
    for key in [
        "LZ_cubed_minus_I_frobenius",
        "LX_cubed_minus_I_frobenius",
        "LZ_LX_minus_omega_LX_LZ_frobenius",
    ]:
        require(checks[key] < 1e-12, f"relation error {key}")
    require(checks["commutator_norm_LZ_LX_minus_LX_LZ"] > 1.0, "noncommutative norm")
    for family in ["class", "phase", "shift"]:
        ranks = [entry["rank"] for entry in spectral["projector_diagnostics"][family].values()]
        require(ranks == [9, 9, 9], f"{family} projector ranks")

    require(profile["selected_charged_row_count"] == 9, "charged row count")
    require(profile["accepted_full_ten_row_kernel_closure_count"] == 0, "ten row overclaim")
    summary = profile["profile_summary"]
    require(summary["all_sectors_share_same_generation_profile"] is True, "shared profile")
    require(summary["generation_ratio"] == [2.0, 1.0, 1.0], "generation ratio")
    require(summary["linear_weights"] == [0.5, 0.25, 0.25], "linear weights")
    for got, want in zip(summary["quadratic_weights"], [2.0 / 3.0, 1.0 / 6.0, 1.0 / 6.0]):
        require(math.isclose(got, want, rel_tol=0.0, abs_tol=1e-15), "quadratic weights")
    require(profile["source_boundary"]["pure_27x27_weyl_symmetry_alone_selects_2_1_1"] is False, "2:1:1 overselected")

    require(search["tested_candidate_count"] >= 7, "candidate count")
    require(search["accepted_H_lambda_candidate_count"] == 0, "H candidate overaccepted")
    require(search["accepted_new_charged_profile_source_count"] == 0, "charged source overaccepted")
    require(search["decision"]["pure_27x27_matrix_package_emits_new_scalar_rows"] is False, "scalar overemitted")
    require(search["decision"]["H_lambda_requires_extra_source_object"] is True, "H frontier missing")

    require(h_packet["H_lambda_overlap_kernel_row_emitted"] is False, "H row emitted")
    require(h_packet["strict_H_source_row_emitted"] is False, "strict H emitted")
    require(h_packet["minimal_one_parameter_H_closed"] is True, "minimal H missing")
    require(h_packet["minimal_H_parameter_count_spent"] == 1, "H parameter count")
    require(h_packet["h_gap_import"]["selected_K_threshold_Omega_H_lambda_emitted"] is False, "K H overemitted")
    require(h_packet["h_gap_import"]["selected_lambda_H_payload_emitted"] is False, "lambda overemitted")

    decision = data["closure_decision"]
    require(decision["qutrit27_spectral_diagnostics_closed"] is True, "decision spectral")
    require(decision["charged_2_1_1_profile_extracted"] is True, "decision profile")
    require(decision["all_charged_sectors_share_profile"] is True, "decision shared")
    require(decision["pure_27x27_matrix_emits_H_lambda_row"] is False, "decision H overclaim")
    require(decision["accepted_H_lambda_candidate_count"] == 0, "decision H count")
    require(decision["minimal_one_parameter_H_closure_available"] is True, "decision minimal H")
    require(decision["minimal_one_parameter_H_parameter_count"] == 1, "decision H parameter count")
    require(decision["strict_no_knob_H_closed"] is False, "decision strict H")

    constants = data["constants_and_parameters"]
    require(constants["carrier_dimension"] == 27, "constant dimension")
    require(constants["charged_generation_ratio"] == [2.0, 1.0, 1.0], "constant profile")
    require(constants["minimal_H_parameter"] == "UP-RET-OVERLAP.HRG", "constant H parameter")
    require(constants["minimal_H_parameter_count"] == 1, "constant H parameter count")

    for phrase in [
        "Qutrit27NumericalPushAndMatrixRowFrontierTheorem",
        "2 : 1 : 1",
        "Pure source-native 27x27 matrix functionals tested here do not emit a new H row.",
        "parameter count: `1`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print("AUDIT_PASS: qutrit 27x27 numerical push closed; H row remains open at strict level.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
