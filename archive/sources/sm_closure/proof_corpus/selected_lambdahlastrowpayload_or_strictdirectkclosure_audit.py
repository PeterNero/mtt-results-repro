"""Audit lambda_H last-row payload / strict direct-K closure split."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_lambdahlastrowpayload_or_strictdirectkclosure"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
LAMBDA_ROW = PACKET_DIR / "lambda_h_last_row_payload_under_oneprimitive.packet.json"
TEN_K = PACKET_DIR / "ten_kthreshold_ledger_current_standard.packet.json"
STRICT_FRONTIER = PACKET_DIR / "strict_directk_zero_primitive_frontier.packet.json"
NEXT = PACKET_DIR / "next_precision_or_strictupgrade_cutset.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_LambdaHLastRowPayload_or_StrictDirectKClosure_v1.md"

STATUS = (
    "MTT_SELECTED_LAMBDAHLASTROWPAYLOAD_OR_STRICTDIRECTKCLOSURE_"
    "ONEPRIMITIVE_TENK_CLOSED_STRICT_DIRECTK_OPEN"
)
NEXT_ARTIFACT = "MTT_Selected_PrecisionEquivalenceRows_or_StrictPEWDirectKUpgrade_v1"
STRICT_UPGRADE_ARTIFACT = "MTT_Selected_PhysicalNormalizationAxiomDerivation_or_StrictPEWNoKnobUpgrade_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def guard(packet: dict[str, Any], label: str) -> None:
    require(packet.get("closure_claimed") is True, f"{label} closure flag")
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    lambda_row = load(LAMBDA_ROW)
    ten_k = load(TEN_K)
    strict_frontier = load(STRICT_FRONTIER)
    next_packet = load(NEXT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", candidate),
        ("cert", cert),
        ("lambda_row", lambda_row),
        ("ten_k", ten_k),
        ("strict_frontier", strict_frontier),
        ("next", next_packet),
    ]:
        guard(packet, label)

    require(candidate["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "certificate status")
    require(candidate["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem")
    require(candidate["next_required_artifact"] == NEXT_ARTIFACT, "candidate next")
    require(candidate["strict_upgrade_artifact"] == STRICT_UPGRADE_ARTIFACT, "candidate strict upgrade")

    decision = candidate["closure_decision"]
    require(decision["current_closure_standard"] == "one_shared_physical_primitive", "standard")
    require(decision["current_closure_standard_adopted"] is True, "standard adopted")
    require(decision["lambda_H_last_row_payload_accepted_under_current_standard"] is True, "lambda row")
    require(decision["ten_K_threshold_rows_closed_under_current_standard"] is True, "ten K current")
    require(decision["accepted_selected_charged_K_threshold_row_count"] == 9, "charged K count")
    require(decision["accepted_H_lambda_K_threshold_row_count_under_current_standard"] == 1, "H K count")
    require(decision["accepted_full_ten_row_K_threshold_row_count_under_current_standard"] == 10, "ten count")
    require(decision["H_specific_parameter_count"] == 0, "H-specific parameter")
    require(decision["shared_physical_primitive_count"] == 1, "shared primitive")
    require(decision["accepted_strict_P_EW_source_rows"] == 0, "strict P_EW overaccepted")
    require(decision["accepted_strict_direct_K_threshold_Omega_H_lambda_rows"] == 0, "strict direct K")
    require(decision["accepted_full_ten_row_K_threshold_row_count_under_strict_zero_primitive"] == 9, "strict K count")
    require(decision["strict_zero_primitive_directK_closed"] is False, "strict direct-K overclosed")
    require(decision["strict_no_knob_closed"] is False, "strict no-knob overclosed")
    require(decision["true_precision_equivalence_closed"] is False, "precision overclosed")

    require(
        lambda_row["status"] == "LAMBDA_H_LAST_ROW_ACCEPTED_UNDER_ADOPTED_ONE_PRIMITIVE_STANDARD",
        "lambda row status",
    )
    require(lambda_row["accepted_as_tenth_K_row_under_current_standard"] is True, "lambda current")
    require(lambda_row["accepted_as_tenth_K_row_under_one_shared_primitive"] is True, "lambda primitive")
    require(lambda_row["accepted_as_strict_zero_primitive_direct_K_row"] is False, "lambda strict")
    source_chain = lambda_row["source_chain"]
    require(source_chain["finite_H_scalar_source_available"] is True, "finite H")
    require(source_chain["selected_H_radial_source_row_emitted"] is True, "H radial")
    require(source_chain["selected_R_H_RG_source_emitted"] is True, "R_H")
    require(source_chain["physical_normalization_axiom_adopted"] is True, "axiom adopted")
    require(source_chain["direct_K_certificate_under_axiom"] is True, "direct cert")
    require(source_chain["paper_standard_ready"] is True, "paper standard")
    require(lambda_row["parameter_accounting"]["H_specific_parameter_count"] == 0, "lambda H parameter")
    require(lambda_row["parameter_accounting"]["shared_physical_primitive_count"] == 1, "lambda primitive count")
    require(lambda_row["parameter_accounting"]["new_parameter_introduced_by_lambda_row"] == 0, "new lambda knob")

    require(
        ten_k["status"] == "TEN_KTHRESHOLD_ROWS_CLOSED_UNDER_ADOPTED_ONE_PRIMITIVE_STANDARD",
        "ten K status",
    )
    require(ten_k["current_closure_standard_adopted"] is True, "ten K standard")
    require(ten_k["charged_K_threshold_rows"] == 9, "ten K charged")
    require(ten_k["H_lambda_K_threshold_rows_under_oneprimitive"] == 1, "ten K H")
    require(ten_k["accepted_full_ten_row_K_threshold_row_count_under_current_standard"] == 10, "ten K current")
    require(ten_k["accepted_full_ten_row_K_threshold_row_count_under_strict_zero_primitive"] == 9, "ten K strict")
    require(ten_k["strict_direct_K_threshold_Omega_H_lambda_rows"] == 0, "strict direct rows")
    require(ten_k["strict_P_EW_source_rows"] == 0, "strict P rows")
    require(len(ten_k["rows"]) == 10, "row length")
    h_rows = [row for row in ten_k["rows"] if row["row_type"] == "H_lambda"]
    require(len(h_rows) == 1, "H row count")
    require(h_rows[0]["accepted_under_current_standard"] is True, "H current row")
    require(h_rows[0]["accepted_under_one_shared_primitive"] is True, "H primitive row")
    require(h_rows[0]["accepted_as_strict_zero_primitive_direct_K_row"] is False, "H strict row")

    require(strict_frontier["status"] == "STRICT_ZERO_PRIMITIVE_DIRECTK_REMAINS_OPEN", "strict status")
    require(strict_frontier["physical_normalization_axiom_derived"] is False, "axiom derived overclaim")
    require(strict_frontier["scale_symmetry_no_go_active"] is True, "scale no-go")
    require(strict_frontier["accepted_strict_P_EW_source_rows"] == 0, "frontier P_EW")
    require(strict_frontier["accepted_strict_direct_K_threshold_Omega_H_lambda_rows"] == 0, "frontier K")
    require(strict_frontier["accepted_strict_derivation_route_count"] == 0, "frontier route")
    require(len(strict_frontier["legal_strict_exits"]) == 3, "legal strict exits")

    require(
        next_packet["status"] == "TENK_CURRENT_STANDARD_CLOSED_NEXT_PRECISION_OR_STRICT_UPGRADE",
        "next status",
    )
    require(next_packet["next_required_artifact"] == NEXT_ARTIFACT, "next artifact")
    require(next_packet["strict_upgrade_artifact"] == STRICT_UPGRADE_ARTIFACT, "strict artifact")
    require(len(next_packet["closed_now"]) == 4, "closed-now count")
    require(len(next_packet["still_open"]) == 5, "still-open count")

    for phrase in [
        "full K_threshold rows under current standard     : 10/10",
        "H-specific parameter count                       : 0",
        "shared physical primitive count                  : 1",
        "strict ten-row K_threshold ledger          : 9/10",
        "strict no-knob closure                     : false",
        NEXT_ARTIFACT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
