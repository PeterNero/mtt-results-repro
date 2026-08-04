"""Audit the T_scheme null-delta reconciliation and lambda_H last-row frontier."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_tschemenulldelta_reconciliation_or_lambdahlastrow"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
RECON = PACKET_DIR / "charged_tscheme_lrowlocal_reconciliation.packet.json"
KROWS = PACKET_DIR / "accepted_charged_kthreshold_rows_current.packet.json"
HROW = PACKET_DIR / "h_lambda_last_row_frontier.packet.json"
NEXT = PACKET_DIR / "next_cutset_after_charged_kthreshold_reconciliation.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_TSchemeNullDelta_Reconciliation_or_LambdaHLastRow_v1.md"

STATUS = (
    "MTT_SELECTED_TSCHEMENULLDELTA_RECONCILIATION_OR_LAMBDAHLASTROW_"
    "BUILT_CHARGED_K9_CLOSED_HLAMBDA_LASTROW_OPEN"
)
NEXT_ARTIFACT = "MTT_Selected_LambdaHLastRowPayload_or_StrictDirectKClosure_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def guard(packet: dict, label: str) -> None:
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting")
    require(packet.get("closure_claimed") is True, f"{label} closure flag")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(CANDIDATE)
    recon = load(RECON)
    krows = load(KROWS)
    hrow = load(HROW)
    next_cutset = load(NEXT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("reconciliation", recon),
        ("krows", krows),
        ("hrow", hrow),
        ("next", next_cutset),
        ("cert", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "cert status")
    require(data["next_required_artifact"] == NEXT_ARTIFACT, "candidate next")
    require(cert["next_required_artifact"] == NEXT_ARTIFACT, "cert next")
    require(data["theorem"]["proved"] is True, "candidate theorem")
    require(cert["theorem_proved"] is True, "cert theorem")

    closed = recon["inputs_closed"]
    require(closed["finite_projected_pairing_theorem_proved"] is True, "pairing theorem")
    require(closed["accepted_selected_Q_sel_quadrature_value_count"] == 9, "Q count")
    require(closed["accepted_strict_Lrowlocal_row_count"] == 9, "L count")
    require(closed["source_native_null_threshold_delta_theorem_emitted"] is True, "null theorem")
    require(closed["selected_zero_delta_row_count_emitted"] == 9, "zero delta count")
    require(closed["selected_T_scheme_source_row_count"] == 9, "T count")
    require("does not assert" in recon["guardrail"], "guardrail")

    require(krows["status"] == "NINE_CHARGED_KTHRESHOLD_ROWS_ACCEPTED_CURRENT_CHAIN", "krows status")
    require(krows["row_count"] == 9, "krows row count")
    require(krows["accepted_selected_Q_sel_quadrature_value_count"] == 9, "krows Q count")
    require(krows["accepted_strict_Lrowlocal_row_count"] == 9, "krows L count")
    require(krows["accepted_selected_T_scheme_source_row_count"] == 9, "krows T count")
    require(krows["accepted_selected_charged_K_threshold_row_count"] == 9, "krows K count")
    require(krows["accepted_full_ten_row_K_threshold_row_count"] == 0, "ten row overclaim")
    require(krows["old_krows_reconciled"] is True, "old krows not reconciled")
    for row in krows["rows"]:
        require(row["accepted_as_selected_Q_sel_row"] is True, f"{row['omega_id']} Q")
        require(row["accepted_as_strict_L_rowlocal_row"] is True, f"{row['omega_id']} L")
        require(row["accepted_as_selected_T_scheme_source_row"] is True, f"{row['omega_id']} T")
        require(row["accepted_as_selected_charged_K_threshold_row"] is True, f"{row['omega_id']} K")
        require(row["accepted_as_full_ten_row_K_closure"] is False, f"{row['omega_id']} ten overclaim")
        require(row["selected_T_scheme_source_native"] == 1.0, f"{row['omega_id']} T value")
        require(row["selected_K_threshold_source_value"] == row["selected_strict_L_rowlocal_value"], f"{row['omega_id']} K=L")
        require(row["lambda_H_payload_required_for_full_closure"] is True, f"{row['omega_id']} lambda guard")

    require(hrow["status"] == "H_LAMBDA_LAST_K_ROW_OPEN", "hrow status")
    support = hrow["current_H_support"]
    require(support["finite_H_scalar_source_available"] is True, "H scalar")
    require(support["selected_H_radial_source_row_emitted"] is True, "H radial")
    require(support["selected_R_H_RG_source_emitted"] is True, "R_H")
    require(support["lambda_H_postcheck_passed"] is True, "lambda postcheck")
    require(support["conditional_ten_K_if_prefactor_row_selected"] is True, "conditional ten")
    missing = hrow["still_missing"]
    require(missing["selected_lambda_H_payload_emitted"] is False, "lambda overemitted")
    require(missing["selected_K_threshold_Omega_H_lambda_emitted"] is False, "direct K overemitted")
    require(missing["accepted_direct_K_threshold_Omega_H_lambda_rows"] == 0, "direct K rows")
    require(missing["accepted_strict_P_EW_source_rows"] == 0, "P_EW rows")
    require(missing["accepted_strict_derivation_route_count"] == 0, "derivation rows")
    require(len(hrow["next_legal_exits"]) == 3, "exit count")

    require(next_cutset["status"] == "ONLY_H_LAMBDA_DIRECTK_LASTROW_REMAINS_FOR_TEN_K", "next status")
    require(next_cutset["next_required_artifact"] == NEXT_ARTIFACT, "next artifact")
    require(len(next_cutset["closed_here"]) == 4, "closed count")
    require(len(next_cutset["still_open"]) == 5, "open count")

    decision = data["closure_decision"]
    require(decision["charged_T_scheme_null_delta_rows_selected"] is True, "decision T")
    require(decision["accepted_selected_T_scheme_source_row_count"] == 9, "decision T count")
    require(decision["accepted_strict_Lrowlocal_row_count"] == 9, "decision L count")
    require(decision["accepted_selected_charged_K_threshold_row_count"] == 9, "decision K count")
    require(decision["accepted_full_ten_row_K_threshold_row_count"] == 0, "decision ten")
    require(decision["selected_lambda_H_payload_emitted"] is False, "decision lambda")
    require(decision["selected_K_threshold_Omega_H_lambda_emitted"] is False, "decision direct K")
    require(decision["strict_PEW_directK_source_rows_closed"] is False, "decision PEW")
    require(decision["full_no_knob_closed"] is False, "decision no-knob")
    require(decision["true_SM_equivalence_closed"] is False, "decision true SM")

    key = data["key_numbers"]
    require(key["accepted_selected_T_scheme_source_row_count"] == 9, "key T")
    require(key["accepted_strict_Lrowlocal_row_count"] == 9, "key L")
    require(key["accepted_selected_charged_K_threshold_row_count"] == 9, "key K")
    require(key["accepted_full_ten_row_K_threshold_row_count"] == 0, "key ten")
    require(key["accepted_direct_K_threshold_Omega_H_lambda_rows"] == 0, "key direct K")
    require(key["accepted_strict_P_EW_source_rows"] == 0, "key PEW")

    for phrase in [
        "accepted selected T_scheme rows       : 9",
        "accepted strict L_rowlocal rows       : 9",
        "accepted charged K_threshold rows     : 9",
        "accepted full ten-row K_threshold rows: 0",
        "selected `lambda_H` H-sector quartic/threshold payload: `false`",
        NEXT_ARTIFACT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
