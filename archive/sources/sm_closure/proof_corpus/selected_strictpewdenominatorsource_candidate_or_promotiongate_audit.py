"""Audit strict P_EW denominator-source candidate / promotion gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_strictpewdenominatorsource_candidate_or_promotiongate"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
DENOM = PACKET_DIR / "finite_quotient_denominator_source_candidate.packet.json"
ROW = PACKET_DIR / "strict_pew_source_row_candidate.packet.json"
GATE = PACKET_DIR / "promotion_gate_and_no_leakage_audit.packet.json"
NEXT = PACKET_DIR / "next_denominator_selection_theorem_contract.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_StrictPEWDenominatorSourceCandidate_or_PromotionGate_v1.md"

STATUS = (
    "MTT_SELECTED_STRICTPEWDENOMINATORSOURCE_CANDIDATE_OR_PROMOTIONGATE_"
    "EXACT_ROW_FORMULA_EMITTED_SELECTION_PROOF_OPEN"
)
NEXT_ARTIFACT = "MTT_Selected_StrictPEWDenominatorSelectionTheorem_or_DirectKPromotion_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def guard(packet: dict[str, Any], label: str) -> None:
    require(packet.get("closure_claimed") is True, f"{label} closure")
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    denom = load(DENOM)
    row = load(ROW)
    gate = load(GATE)
    next_packet = load(NEXT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", candidate),
        ("denom", denom),
        ("row", row),
        ("gate", gate),
        ("next", next_packet),
        ("cert", cert),
    ]:
        guard(packet, label)

    require(candidate["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "certificate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(cert["theorem_proved"] is True, "cert theorem")
    require(candidate["next_required_artifact"] == NEXT_ARTIFACT, "candidate next")
    require(next_packet["next_required_artifact"] == NEXT_ARTIFACT, "next packet")

    decision = candidate["closure_decision"]
    require(decision["strict_P_EW_denominator_candidate_emitted"] is True, "candidate not emitted")
    require(decision["candidate_strict_P_EW_source_rows_emitted"] == 1, "candidate row count")
    require(decision["accepted_global_strict_P_EW_source_rows"] == 0, "global P_EW overaccepted")
    require(decision["accepted_global_direct_K_threshold_Omega_H_lambda_rows"] == 0, "global K overaccepted")
    require(decision["denominator_selection_theorem_proved"] is False, "denominator overproved")
    require(decision["candidate_exact_postcheck_passed"] is True, "postcheck did not pass")
    require(decision["strict_zero_primitive_ten_K_promotable_if_accepted"] is True, "not promotable")
    require(decision["strict_zero_primitive_ten_K_closed_now"] is False, "strict ten-K overclosed")
    require(decision["full_no_knob_closed"] is False, "no-knob overclosed")
    require(decision["true_SM_equivalence_closed"] is False, "true SM overclosed")

    require(
        denom["status"] == "FINITE_QUOTIENT_DENOMINATOR_CANDIDATE_EMITTED_SELECTION_PROOF_OPEN",
        "denom status",
    )
    require(denom["formula"] == "D_EW = (q79 + dim_27 - rank_3) + lambda_12/((448/2)*448*pi)", "formula")
    components = denom["source_components"]
    require(components["q79_selected"] == 79, "q79")
    require(components["qutrit_dim_selected"] == 27, "dim")
    require(components["family_rank_selected"] == 3, "rank")
    require(components["finite_quotient_selected"] == 448, "448")
    require(components["oriented_half_quotient"] == 224, "224")
    require(components["lambda_12_internal_closed"] is True, "lambda12 closed")
    require(components["qutrit27_matrix_locked"] is True, "qutrit locked")
    sel = denom["selection_status"]
    require(sel["all_symbols_source_available"] is True, "symbols unavailable")
    require(sel["denominator_functional_formula_emitted"] is True, "formula not emitted")
    require(sel["denominator_functional_selected_by_prior_theorem"] is False, "prior theorem overclaim")
    require(sel["accepted_for_global_strict_P_EW"] is False, "denom global overaccepted")

    nums = row["numeric_payload"]
    require(row["status"] == "STRICT_PEW_SOURCE_ROW_FORMULA_EXACT_POSTCHECK_PROMOTION_OPEN", "row status")
    require(row["acceptance"]["candidate_strict_P_EW_source_rows_emitted"] == 1, "row candidate count")
    require(row["acceptance"]["accepted_global_strict_P_EW_source_rows"] == 0, "row global count")
    require(row["acceptance"]["accepted_if_denominator_selection_theorem_proved"] == 1, "conditional count")
    require(row["acceptance"]["direct_K_promotable_if_accepted"] is True, "direct K promotable")
    require(abs(nums["absolute_postcheck_residual"]) < 1e-15, "absolute residual")
    require(abs(nums["relative_postcheck_residual"]) < 1e-13, "relative residual")
    leakage = row["leakage_guard"]
    require(leakage["formula_uses_A_EW_target"] is False, "A_EW leakage")
    require(leakage["formula_uses_lambda_H_target"] is False, "lambda leakage")
    require(leakage["formula_uses_observed_weak_angle"] is False, "weak-angle leakage")
    require(leakage["formula_discovered_by_postcheck_search"] is True, "discovery provenance")
    require(leakage["postcheck_not_counted_as_selection_proof"] is True, "postcheck overused")

    require(gate["status"] == "PROMOTION_GATE_OPEN_BUT_NUMERIC_ROW_READY", "gate status")
    require(gate["previous_global_strict_rows"]["accepted_strict_P_EW_source_rows"] == 0, "prev P_EW")
    require(
        gate["previous_global_strict_rows"]["accepted_direct_K_threshold_Omega_H_lambda_rows"] == 0,
        "prev K",
    )
    require(gate["current_candidate"]["candidate_strict_P_EW_source_rows_emitted"] == 1, "gate candidate")
    require(len(gate["not_promoted_because"]) == 3, "not promoted reasons")
    require(len(gate["would_promote"]) == 3, "promotion consequences")

    require(next_packet["status"] == "NEXT_PROVE_DENOMINATOR_SELECTION_OR_REJECT_CANDIDATE", "next status")
    require(len(next_packet["proof_obligations"]) == 4, "proof obligations")
    require(len(next_packet["fallback_if_rejected"]) == 2, "fallbacks")

    for phrase in [
        "candidate strict P_EW source rows emitted = 1",
        "accepted global strict P_EW source rows   = 0",
        "denominator selection theorem proved      = false",
        "strict zero-primitive ten-K closed now    = false",
        NEXT_ARTIFACT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
