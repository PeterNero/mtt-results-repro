"""Audit selected qutrit 27x27 second-pass matrix push."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_qutrit27secondpassmatrixpush_or_leftrightprofilefrontier"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SCAN = PACKET_DIR / "crossrepo_matrix_import_scan.packet.json"
LR = PACKET_DIR / "left_right_weyl_commutant_diagnostics.packet.json"
PROFILE = PACKET_DIR / "class_profile_operator_211.packet.json"
H_PACKET = PACKET_DIR / "strict_h_frontier_after_second_matrix_push.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Qutrit27SecondPassMatrixPush_or_LeftRightProfileFrontier_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_QUTRIT27SECONDPASSMATRIXPUSH_OR_LEFTRIGHTPROFILEFRONTIER_"
    "LEFTRIGHT_CLOSED_PROFILE_OPERATOR_BUILT_H_OPEN"
)
NEXT = "MTT_Selected_StrictFiniteHSourceRowConstruction_or_NonHiggsHRGPrediction_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("closure_claimed") is True, f"{label} closure")
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    scan = load(SCAN)
    lr = load(LR)
    profile = load(PROFILE)
    h_packet = load(H_PACKET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("scan", scan),
        ("left_right", lr),
        ("profile", profile),
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

    checks = lr["relation_checks"]
    for key in [
        "LZ_cubed_minus_I_frobenius",
        "LX_cubed_minus_I_frobenius",
        "RZ_cubed_minus_I_frobenius",
        "RX_cubed_minus_I_frobenius",
        "left_weyl_relation_frobenius",
        "right_weyl_relation_omega_bar_frobenius",
        "LZ_RZ_commutator_frobenius",
        "LZ_RX_commutator_frobenius",
        "LX_RZ_commutator_frobenius",
        "LX_RX_commutator_frobenius",
    ]:
        require(checks[key] < 1e-12, f"matrix relation {key}")
    require(checks["right_weyl_relation_omega_frobenius"] > 1.0, "right orientation check")
    require(lr["classwise_left_right_algebra_rank"] == 243, "left-right rank")
    require(lr["expected_classwise_left_right_algebra_rank"] == 243, "expected rank")

    require(profile["matches_selected_charged_rows"] is True, "profile row match")
    require(profile["matrix_representation_closed"] is True, "profile matrix representation")
    require(profile["source_selection_closed"] is False, "profile source overclaim")
    require(profile["pure_27x27_weyl_symmetry_alone_selects_profile"] is False, "pure Weyl overclaim")
    require(profile["eigenvalue_multiset"]["1.367835979172"] == 9, "double class multiplicity")
    require(profile["eigenvalue_multiset"]["0.683917989586"] == 18, "base class multiplicity")
    for key, value in profile["commutators"].items():
        require(value < 1e-12, f"profile commutator {key}")

    require(scan["stronger_matrix_or_H_source_hit_count"] >= 0, "scan count")
    require("did not find a newer selected" in scan["conclusion"], "scan conclusion")

    require(h_packet["left_right_matrix_layer_closed"] is True, "H frontier left-right")
    require(h_packet["charged_profile_matrix_operator_closed"] is True, "H frontier profile")
    require(h_packet["H_lambda_overlap_kernel_row_emitted"] is False, "H overemitted")
    require(h_packet["strict_H_source_row_emitted"] is False, "strict H overemitted")
    require(h_packet["minimal_one_parameter_H_closed"] is True, "minimal H")
    require(h_packet["minimal_H_parameter_count_spent"] == 1, "H parameter count")

    decision = data["closure_decision"]
    require(decision["left_right_weyl_layer_closed"] is True, "decision left-right")
    require(decision["classwise_left_right_algebra_rank"] == 243, "decision rank")
    require(decision["charged_2_1_1_profile_operator_realized_on_27_carrier"] is True, "decision profile")
    require(decision["profile_operator_selected_by_pure_weyl_symmetry"] is False, "decision pure Weyl")
    require(decision["pure_27x27_matrix_emits_H_lambda_row"] is False, "decision H")
    require(decision["strict_no_knob_H_closed"] is False, "decision strict H")

    constants = data["constants_and_parameters"]
    require(constants["carrier_dimension"] == 27, "dimension")
    require(constants["classwise_left_right_algebra_rank"] == 243, "constant rank")
    require(constants["charged_generation_ratio"] == [2.0, 1.0, 1.0], "constant profile")
    require(constants["minimal_H_parameter_count"] == 1, "constant H count")

    for phrase in [
        "Qutrit27LeftRightProfileFrontierTheorem",
        "class-projected left-right algebra rank: `243`",
        "D_211 = base * (2 P_class0 + P_class1 + P_class2)",
        "Strict H remains open",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print("AUDIT_PASS: qutrit 27 second-pass matrix push closes left-right/profile layer; strict H remains open.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
