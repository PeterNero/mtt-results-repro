"""Audit strict P_EW denominator-selection theorem / direct-K promotion."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_strictpewdenominatorselectiontheorem_or_directkpromotion"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SOURCE = PACKET_DIR / "source_component_closure.packet.json"
SPINE = PACKET_DIR / "integer_spine_selection_lemma.packet.json"
BOUNDARY = PACKET_DIR / "oriented_boundary_correction_lemma.packet.json"
ROW = PACKET_DIR / "promoted_strict_pew_source_row.packet.json"
DIRECTK = PACKET_DIR / "promoted_direct_kthreshold_omega_h_lambda_row.packet.json"
NEXT = PACKET_DIR / "next_after_strict_pew_directk_promotion.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_StrictPEWDenominatorSelectionTheorem_or_DirectKPromotion_v1.md"

STATUS = (
    "MTT_SELECTED_STRICTPEWDENOMINATORSELECTIONTHEOREM_OR_DIRECTKPROMOTION_"
    "STRICT_PEW_AND_DIRECTK_PROMOTED"
)
NEXT_ARTIFACT = "MTT_Selected_PrecisionEquivalenceRows_or_TrueSMClosureAudit_v1"


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
    source = load(SOURCE)
    spine = load(SPINE)
    boundary = load(BOUNDARY)
    row = load(ROW)
    directk = load(DIRECTK)
    next_packet = load(NEXT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", candidate),
        ("source", source),
        ("spine", spine),
        ("boundary", boundary),
        ("row", row),
        ("directk", directk),
        ("next", next_packet),
        ("cert", cert),
    ]:
        guard(packet, label)

    require(candidate["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "certificate status")
    require(candidate["theorem"]["name"] == "StrictPEWDenominatorSelectionTheorem", "theorem name")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(cert["theorem_proved"] is True, "cert theorem")
    require(candidate["next_required_artifact"] == NEXT_ARTIFACT, "candidate next")
    require(next_packet["next_required_artifact"] == NEXT_ARTIFACT, "next packet")

    closed = source["closed_components"]
    require(closed["q79_character"] == 79, "q79")
    require(closed["qutrit_phase_space_dimension"] == 27, "qutrit")
    require(closed["family_kernel_rank"] == 3, "rank")
    require(closed["selected_finite_CP_quotient"] == 448, "N")
    require(closed["oriented_half_quotient"] == 224, "N/2")
    require(closed["lambda_12_internal_closed"] is True, "lambda12")
    require(closed["qutrit27_matrix_locked"] is True, "qutrit locked")
    require(closed["prior_candidate_exact_postcheck_passed"] is True, "prior postcheck")
    require(len(source["no_target_inputs"]) == 3, "target guard")

    require(spine["status"] == "INTEGER_SPINE_SELECTED", "spine status")
    require(spine["selection_rule"] == "D0 = q79 + dim_qutrit - rank_family", "spine rule")
    require(spine["computed"]["integer_spine"] == 103, "integer spine")
    require(len(spine["why_unique"]) == 4, "spine uniqueness")

    require(boundary["status"] == "ORIENTED_BOUNDARY_CORRECTION_SELECTED", "boundary status")
    require(boundary["selection_rule"] == "delta_D = lambda_12 / ((N/2)*N*pi)", "boundary rule")
    require(boundary["computed"]["N"] == 448, "boundary N")
    require(boundary["computed"]["N_over_2"] == 224, "boundary half")
    require(8.3e-06 < boundary["computed"]["boundary_correction"] < 8.4e-06, "boundary value")
    require(len(boundary["why_unique"]) == 5, "boundary uniqueness")

    require(row["status"] == "STRICT_PEW_SOURCE_ROW_PROMOTED", "row status")
    require(row["denominator_selection_theorem_proved"] is True, "row theorem")
    require(row["accepted_global_strict_P_EW_source_rows"] == 1, "row count")
    require(row["no_observed_selector"] is True, "row selector")
    require(abs(row["absolute_postcheck_residual"]) < 1e-15, "row residual")
    require(abs(row["relative_postcheck_residual"]) < 1e-13, "row rel residual")

    require(
        directk["status"] == "STRICT_DIRECT_K_THRESHOLD_OMEGA_H_LAMBDA_PROMOTED",
        "direct K status",
    )
    require(directk["strict_P_EW_source_row_available"] is True, "P_EW not available")
    require(directk["accepted_strict_P_EW_source_rows"] == 1, "P_EW row count")
    require(directk["last_row_payload_available"] is True, "last row unavailable")
    require(directk["strict_direct_K_threshold_Omega_H_lambda_rows"] == 1, "direct K count")
    require(directk["strict_zero_primitive_K_threshold_row_count"] == 10, "ten K")

    decision = candidate["closure_decision"]
    require(decision["denominator_selection_theorem_proved"] is True, "decision theorem")
    require(decision["accepted_global_strict_P_EW_source_rows"] == 1, "decision P_EW")
    require(decision["accepted_global_direct_K_threshold_Omega_H_lambda_rows"] == 1, "decision direct K")
    require(decision["strict_zero_primitive_K_threshold_row_count"] == 10, "decision ten K")
    require(decision["strict_zero_primitive_ten_K_closed"] is True, "decision ten closed")
    require(decision["previous_locked_strict_P_EW_rows"] == 0, "previous P_EW")
    require(decision["previous_locked_direct_K_rows"] == 0, "previous K")
    require(decision["current_standard_one_primitive_still_valid"] is True, "one primitive validity")
    require(decision["full_no_knob_closed"] is False, "full no-knob overclaim")
    require(decision["true_SM_equivalence_closed"] is False, "true SM overclaim")
    require(decision["true_precision_equivalence_closed"] is False, "precision overclaim")

    require(next_packet["status"] == "STRICT_PEW_DIRECTK_PROMOTED_NEXT_PRECISION_TRUE_SM_AUDIT", "next status")
    require(len(next_packet["closed_now"]) == 4, "closed-now count")
    require(len(next_packet["still_open"]) == 5, "still-open count")

    for phrase in [
        "accepted global strict P_EW source rows = 1",
        "accepted direct K_threshold.Omega_H.lambda rows = 1",
        "strict zero-primitive K_threshold ledger = 10/10",
        "full no-knob SM closure = false",
        "true precision equivalence = false",
        NEXT_ARTIFACT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
