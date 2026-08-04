"""Audit the retarded-overlap spectral-pairing lemma / Q_sel execution."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_retardedoverlapspectralpairing_or_independentquadraturevalues"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
LEMMA = PACKET_DIR / "finite_projected_retarded_overlap_spectral_pairing_lemma.packet.json"
QSEL = PACKET_DIR / "independent_qsel_quadrature_values.packet.json"
KSTATUS = PACKET_DIR / "krow_status_after_charged_lrowlocal_promotion.packet.json"
NEXT = PACKET_DIR / "next_cutset_after_charged_lrowlocal_promotion.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_RetardedOverlapSpectralPairingLemma_or_IndependentQuadratureValues_v1.md"

STATUS = (
    "MTT_SELECTED_RETARDEDOVERLAPSPECTRALPAIRING_OR_INDEPENDENTQUADRATUREVALUES_"
    "BUILT_CHARGED_LROWLOCAL_CLOSED_TSCHEME_LAMBDA_OPEN"
)
NEXT_ARTIFACT = "MTT_Selected_TSchemeLambdaH_SourceRows_or_KThresholdRowClosure_v1"


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
    lemma = load(LEMMA)
    qsel = load(QSEL)
    kstatus = load(KSTATUS)
    next_cutset = load(NEXT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("lemma", lemma),
        ("qsel", qsel),
        ("kstatus", kstatus),
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

    prereq = lemma["finite_source_prerequisites"]
    require(prereq["finite_projected_HYM_source_principle_closed"] is True, "finite HYM source")
    require(prereq["automatic_finite_cutoff_exactness_for_A_N_closed"] is True, "finite exactness")
    require(prereq["finite_trace_source"] is True, "finite trace")
    require(prereq["same_source_dynamic_matter_overlap_packet_closed"] is True, "same source packet")
    require(prereq["same_source_validator_ok"] is True, "same source validator")
    require(prereq["selected_family_projector_basis_closed"] is True, "projector basis")

    scope = lemma["scope"]
    require(scope["charged_rows"] == 9, "lemma charged scope")
    require(scope["H_lambda_row_included"] is False, "H lambda overincluded")
    require(scope["literal_continuum_HYM_claimed"] is False, "continuum overclaim")
    require(scope["strict_T_scheme_claimed"] is False, "T scheme overclaim")
    require(scope["strict_K_threshold_claimed"] is False, "K overclaim")
    require(scope["full_no_knob_SM_claimed"] is False, "SM overclaim")
    require(len(lemma["proof_steps"]) == 5, "proof step count")

    require(qsel["status"] == "NINE_CHARGED_QSEL_AND_LROWLOCAL_VALUES_EMITTED", "qsel status")
    require(qsel["row_count"] == 9, "qsel row count")
    require(qsel["charged_sectors"] == ["d", "e", "u"], "charged sectors")
    require(qsel["distinct_L_rowlocal_values"] == [0.683917989586, 1.367835979172], "distinct values")
    require(qsel["accepted_selected_Q_sel_quadrature_value_count"] == 9, "Q_sel count")
    require(qsel["accepted_strict_L_rowlocal_row_count"] == 9, "L count")
    require(qsel["accepted_K_threshold_row_count"] == 0, "K count")
    for row in qsel["rows"]:
        require(row["accepted_as_selected_Q_sel_quadrature_value"] is True, f"{row['row_id']} Q_sel")
        require(row["accepted_as_strict_L_rowlocal_row"] is True, f"{row['row_id']} L")
        require(row["accepted_as_K_threshold_row"] is False, f"{row['row_id']} K")
        require(row["equality_residual"] == 0.0, f"{row['row_id']} residual")
        require(row["Q_sel_value"] == row["L_rowlocal_value"], f"{row['row_id']} Q=L")
        require(row["observed_data_used_as_selector"] is False, f"{row['row_id']} observed")
        require(row["target_fitting_used"] is False, f"{row['row_id']} fitting")

    require(kstatus["status"] == "NINE_CHARGED_LROWLOCAL_ROWS_CLOSED_ZERO_K_ROWS", "kstatus")
    require(kstatus["row_count"] == 10, "K status row count")
    require(kstatus["accepted_selected_Q_sel_quadrature_value_count"] == 9, "K Q count")
    require(kstatus["accepted_strict_Lrowlocal_row_count"] == 9, "K L count")
    require(kstatus["accepted_T_scheme_row_count"] == 0, "K T count")
    require(kstatus["accepted_lambda_H_payload_count"] == 0, "K lambda count")
    require(kstatus["accepted_selected_K_source_row_count"] == 0, "K source count")
    for row in kstatus["rows"]:
        if row["sector"] == "H":
            require(row["selected_Q_sel_value_emitted"] is False, "H Q_sel overemitted")
            require(row["selected_L_rowlocal_value_emitted"] is False, "H L overemitted")
            require(row["selected_lambda_H_payload_emitted"] is False, "H lambda overemitted")
        else:
            require(row["selected_Q_sel_value_emitted"] is True, f"{row['omega_id']} Q missing")
            require(row["selected_L_rowlocal_value_emitted"] is True, f"{row['omega_id']} L missing")
            require(row["L_rowlocal_value"] in [0.683917989586, 1.367835979172], f"{row['omega_id']} L value")
            require(row["selected_lambda_H_payload_emitted"] is None, f"{row['omega_id']} lambda marker")
        require(row["selected_T_scheme_row_emitted"] is False, f"{row['omega_id']} T overemitted")
        require(row["selected_K_threshold_row_emitted"] is False, f"{row['omega_id']} K overemitted")
        require(row["accepted_as_no_knob_source_row"] is False, f"{row['omega_id']} no-knob overaccepted")

    require(next_cutset["status"] == "TSCHEME_LAMBDAH_SOURCE_ROWS_ARE_NEXT", "next status")
    require(next_cutset["next_required_artifact"] == NEXT_ARTIFACT, "next artifact")
    require(len(next_cutset["closed_here"]) == 3, "closed_here count")
    require(len(next_cutset["still_open"]) == 5, "still_open count")
    require(len(next_cutset["forbidden_routes"]) == 3, "forbidden count")

    decision = data["closure_decision"]
    require(decision["retarded_overlap_equals_spectral_pairing_theorem_proved"] is True, "decision lemma")
    require(decision["independent_selected_quadrature_values_emitted"] is True, "decision Q")
    require(decision["accepted_selected_Q_sel_quadrature_value_count"] == 9, "decision Q count")
    require(decision["accepted_strict_Lrowlocal_row_count"] == 9, "decision L count")
    require(decision["selected_T_scheme_rows_emitted"] is False, "decision T")
    require(decision["selected_lambda_H_payload_emitted"] is False, "decision lambda")
    require(decision["accepted_selected_K_source_row_count"] == 0, "decision K")
    require(decision["strict_PEW_directK_source_rows_closed"] is False, "decision PEW")
    require(decision["full_no_knob_closed"] is False, "decision no-knob")
    require(decision["true_SM_equivalence_closed"] is False, "decision true SM")

    key = data["key_numbers"]
    require(key["accepted_selected_Q_sel_quadrature_value_count"] == 9, "key Q")
    require(key["accepted_strict_Lrowlocal_row_count"] == 9, "key L")
    require(key["accepted_T_scheme_row_count"] == 0, "key T")
    require(key["accepted_lambda_H_payload_count"] == 0, "key lambda")
    require(key["accepted_selected_K_source_row_count"] == 0, "key K")

    for phrase in [
        "accepted selected Q_sel rows       : 9",
        "accepted strict L_rowlocal rows    : 9",
        "accepted T_scheme rows             : 0",
        "accepted lambda_H payload rows      : 0",
        "accepted K_threshold rows           : 0",
        NEXT_ARTIFACT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
