"""Audit transport-closed Phi_fin finite replay or symbolic conjugation validator."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_transportclosedphifinfinite_replay_or_symbolicconjugationvalidator"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SYMBOLIC_PACKET = PACKET_DIR / "symbolic_transport_conjugation_validator_packet.packet.json"
SYMBOLIC_RESULT = PACKET_DIR / "symbolic_transport_conjugation_validator_result.packet.json"
SYMBOLIC_QUOTIENT = PACKET_DIR / "transport_closed_symbolic_finite_quotient.packet.json"
MORPHISM_PROOF = PACKET_DIR / "premise_free_phi_fin_restriction_morphism.packet.json"
SOURCE_CERT = PACKET_DIR / "premise_free_route_a_source_certificate.packet.json"
SOURCE_VALIDATOR_RESULT = PACKET_DIR / "premise_free_route_a_source_validator_result.packet.json"
RAW_GUARDRAIL = PACKET_DIR / "raw_27mode_basis_guardrail.packet.json"
NEXT_CUTSET = PACKET_DIR / "next_cutset_after_symbolic_conjugation_validator.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_TransportClosedPhiFinFiniteReplay_or_SymbolicConjugationValidator_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_TRANSPORTCLOSEDPHIFINFINITE_REPLAY_OR_SYMBOLICCONJUGATIONVALIDATOR_"
    "BUILT_SYMBOLIC_FINITE_MORPHISM_VALIDATES_UNPATCHED_SOURCE"
)
NEXT = "MTT_Selected_UnpatchedSourcePromotionReplay_or_FullSMClosureGate_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    symbolic_packet = load(SYMBOLIC_PACKET)
    symbolic_result = load(SYMBOLIC_RESULT)
    quotient = load(SYMBOLIC_QUOTIENT)
    morphism = load(MORPHISM_PROOF)
    source_cert = load(SOURCE_CERT)
    source_result = load(SOURCE_VALIDATOR_RESULT)
    guardrail = load(RAW_GUARDRAIL)
    cutset = load(NEXT_CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")

    require(quotient["finite_rank"] == 27, "symbolic quotient must keep finite rank 27")
    require(quotient["symbolic_transport_envelope"] is True, "symbolic envelope missing")
    require(quotient["raw_27_mode_truncation_claimed_closed"] is False, "raw 27 mode overclaimed")
    for key in [
        "U_inverse_U_identity",
        "U_unitary_or_orthogonal",
        "P_selected_conjugation",
        "G_selected_conjugation",
        "trace_cyclicity",
    ]:
        require(quotient["relations"][key] is True, f"missing quotient relation {key}")

    require(symbolic_packet["raw_27_mode_truncation_claimed_closed"] is False, "symbolic packet overclaims raw basis")
    require(symbolic_result["returncode"] == 0, "symbolic validator should pass")
    require(any("PASS" in line for line in symbolic_result["stdout"]), "symbolic PASS missing")
    for key in [
        "D_selected_U_equals_U_d",
        "P_selected_equals_U_P_model_U_inverse",
        "G_selected_equals_U_G_model_U_inverse_on_complement",
        "trace_cyclicity_for_transport_conjugation",
        "rank_preserved_by_conjugation",
        "gap_preserved_by_unitary_conjugation",
        "finite_trace_restriction_map_equals_constructed_row",
    ]:
        require(symbolic_packet["validated_identities"][key] is True, f"identity missing {key}")

    require(morphism["premise_free"] is True, "morphism not premise-free")
    require(morphism["source_row_used_as_premise"] is False, "source row used as premise")
    require(morphism["closure_claimed"] is True, "morphism closure not claimed")

    route_a = source_cert["route_A_physical_source_certificate"]
    require(route_a["source_row_premise_used"] is False, "source certificate uses row premise")
    require(route_a["same_branch"] is True, "Route A not same branch")
    require(route_a["physical_action_restricts_to_selected_finite_Weyl_quotient"] is True, "Route A restriction not closed")
    require(route_a["no_extra_physical_boundary_or_source_term"] is True, "Route A boundary not closed")
    require(len(route_a["attached_same_branch_sources"]) >= 5, "Route A evidence too small")
    require(source_result["returncode"] == 0, "strict physical-source validator should pass")
    require(any("PASS" in line for line in source_result["stdout"]), "source validator PASS missing")

    require(guardrail["raw_27_mode_truncation_claimed_closed"] is False, "guardrail overclaims raw basis")
    require(guardrail["raw_direct_truncated_relative_residual"] > 0.0, "raw residual absent")
    require(guardrail["gauge_frame_residual_l2"] < 1e-12, "gauge residual too large")

    require(data["what_closes_now"]["symbolic_transport_conjugation_validator_passes"] is True, "symbolic close missing")
    require(data["what_closes_now"]["premise_free_route_A_source_certificate_passes"] is True, "source close missing")
    require(data["promotion_decision"]["finite_emission_morphism_restriction_proved"] is True, "finite morphism not promoted")
    require(data["promotion_decision"]["raw_27mode_finite_replay_closed"] is False, "raw replay overpromoted")
    require(data["promotion_decision"]["full_SM_no_knob_closed"] is False, "full SM overclosed")
    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    require("Raw 27-mode closure is still not claimed" in note, "note missing raw guardrail")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
