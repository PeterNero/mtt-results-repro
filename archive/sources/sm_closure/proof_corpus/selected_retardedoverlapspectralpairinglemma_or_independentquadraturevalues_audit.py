"""Audit selected retarded-overlap spectral-pairing lemma packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_retardedoverlapspectralpairinglemma_or_independentquadraturevalues"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
LEMMA = PACKET_DIR / "selected_retarded_overlap_spectral_pairing_lemma.packet.json"
CHARGED_ROWS = PACKET_DIR / "charged_strict_lrowlocal_rows_after_pairing_lemma.packet.json"
K_GATE = PACKET_DIR / "kthreshold_gate_after_charged_lrowlocal_closure.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_retarded_overlap_pairing.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_RetardedOverlapSpectralPairingLemma_or_IndependentQuadratureValues_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_RETARDEDOVERLAPSPECTRALPAIRINGLEMMA_OR_INDEPENDENTQUADRATUREVALUES_"
    "CLOSED_CHARGED_LROWS_TSCHEME_LAMBDAH_OPEN"
)
NEXT = "MTT_Selected_TSchemeLambdaHSourceRows_or_KThresholdRowClosure_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def require_close(value: float, expected: float, message: str) -> None:
    require(abs(float(value) - expected) < 1e-12, message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector violation")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting violation")
    require(packet.get("closure_claimed") is True, f"{label} should close its local theorem")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    lemma = load(LEMMA)
    charged = load(CHARGED_ROWS)
    k_gate = load(K_GATE)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("certificate", cert),
        ("lemma", lemma),
        ("charged rows", charged),
        ("K gate", k_gate),
        ("cutset", cutset),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "candidate theorem missing")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaim")
    require(data["full_no_knob_closure_claimed"] is False, "full no-knob overclaim")

    decision = data["closure_decision"]
    require(decision["retarded_overlap_spectral_pairing_lemma_proved"] is True, "pairing lemma not proved")
    require(
        decision["independent_selected_quadrature_values_needed_for_charged_rows"] is False,
        "Q_sel should no longer be required for charged rows",
    )
    require(decision["charged_strict_Lrowlocal_row_count"] == 9, "charged L count mismatch")
    require(decision["selected_T_scheme_rows_emitted"] is False, "T_scheme overemitted")
    require(decision["selected_lambda_H_payload_emitted"] is False, "lambda_H overemitted")
    require(decision["accepted_selected_K_source_row_count"] == 0, "K rows overaccepted")
    require(decision["accepted_internal_scalar_value_row_count"] == 0, "scalar rows overaccepted")
    require(decision["true_SM_equivalence_closed"] is False, "true SM closure overclaimed")
    require(decision["full_no_knob_closed"] is False, "full no-knob closure overclaimed")

    require(
        lemma["status"] == "CHARGED_RETARDED_OVERLAP_EQUALS_SELECTED_H1_SPECTRAL_PAIRING",
        "lemma status mismatch",
    )
    clauses = lemma["proof_clauses"]
    for key in [
        "rowlocal_functional_contract_defined",
        "physical_dotD_alpha1_imported",
        "stationary_sector_transfer_imported",
        "dynamic_first_response_support_imported",
        "same_source_dynamic_packet_validates",
        "operator_values_selected_emitted",
        "overlap_transfer_selected_emitted",
        "primitive_contractions_selected_emitted",
        "normalization_selected_emitted",
        "matter_slot_charge_selected_emitted",
        "selected_H1_is_hermitian_first_response",
        "rank_one_projector_trace_equals_expectation",
        "finite_basis_spectral_theorem_applies",
    ]:
        require(clauses[key] is True, f"lemma clause missing {key}")
    require(lemma["scope"]["charged_sectors_closed"] == ["u", "d", "e"], "charged scope mismatch")
    require(lemma["scope"]["higgs_lambda_sector_closed"] is False, "H/lambda overclosed")
    require(lemma["scope"]["T_scheme_rows_closed"] is False, "T_scheme overclosed")
    require(lemma["scope"]["K_threshold_rows_closed"] is False, "K rows overclosed")
    require(lemma["scope"]["full_no_knob_SM_closed"] is False, "full no-knob overclosed")
    require(lemma["previous_blocker_retired"] is True, "previous blocker not retired")
    require(
        lemma["independent_Q_sel_quadrature_values_required_for_charged_rows"] is False,
        "Q_sel should not remain required for charged rows",
    )

    require(charged["status"] == "NINE_CHARGED_STRICT_LROWLOCAL_ROWS_EMITTED", "charged row status mismatch")
    require(charged["row_count"] == 9, "charged row count mismatch")
    require(charged["charged_sectors"] == ["u", "d", "e"], "charged sectors mismatch")
    require(charged["source_support_row_count_before"] == 9, "source support before mismatch")
    require(charged["strict_Lrowlocal_row_count_before"] == 0, "strict L before mismatch")
    require(charged["strict_Lrowlocal_row_count_after"] == 9, "strict L after mismatch")

    expected_by_gen = {1: 1.367835979172, 2: 0.683917989586, 3: 0.683917989586}
    seen = {(row["sector"], row["generation"]) for row in charged["rows"]}
    require(seen == {(sector, gen) for sector in ["u", "d", "e"] for gen in [1, 2, 3]}, "charged rows missing")
    for row in charged["rows"]:
        require(row["pairing_identity_used"] is True, f"{row['row_id']} did not use identity")
        require(row["accepted_as_selected_spectral_support_row"] is True, f"{row['row_id']} support not accepted")
        require(row["accepted_as_strict_L_rowlocal_row"] is True, f"{row['row_id']} strict L not accepted")
        require(row["selected_T_scheme_row_emitted"] is False, f"{row['row_id']} T_scheme overemitted")
        require(row["accepted_as_K_threshold_row"] is False, f"{row['row_id']} K row overaccepted")
        require(row["observed_data_used_as_selector"] is False, f"{row['row_id']} observed selector")
        require(row["target_fitting_used"] is False, f"{row['row_id']} target fitting")
        require_close(
            row["selected_strict_L_rowlocal_value"],
            expected_by_gen[row["generation"]],
            f"{row['row_id']} L value mismatch",
        )

    require(
        k_gate["status"] == "CHARGED_LROWS_CLOSED_KROWS_BLOCKED_BY_TSCHEME_AND_LAMBDAH",
        "K gate status mismatch",
    )
    require(k_gate["row_count"] == 10, "K gate row count mismatch")
    require(k_gate["strict_charged_Lrowlocal_row_count"] == 9, "K gate L count mismatch")
    require(k_gate["selected_T_scheme_row_count"] == 0, "T_scheme count mismatch")
    require(k_gate["selected_lambda_H_payload_emitted"] is False, "lambda_H overemitted")
    require(k_gate["accepted_selected_K_source_row_count"] == 0, "K rows overaccepted")
    require(k_gate["accepted_internal_scalar_value_row_count"] == 0, "scalar rows overaccepted")
    require(k_gate["previous_accepted_K_source_row_count"] == 0, "previous K count mismatch")
    for row in k_gate["rows"]:
        if row["sector"] == "H":
            require(row["selected_strict_L_rowlocal_available"] is False, "H L row overemitted")
            require(row["selected_strict_L_rowlocal_value"] is None, "H L value overemitted")
            require(row["selected_lambda_H_payload_emitted"] is False, "H lambda overemitted")
            require("selected lambda_H H-sector payload is not emitted" in row["blocking_reasons"], "H blocker missing")
        else:
            require(row["selected_strict_L_rowlocal_available"] is True, f"{row['omega_id']} L row missing")
            require(row["selected_strict_L_rowlocal_value"] is not None, f"{row['omega_id']} L value missing")
            require(row["selected_lambda_H_payload_emitted"] is None, f"{row['omega_id']} lambda marker mismatch")
            require("selected T_scheme row is not instantiated" in row["blocking_reasons"], "T blocker missing")
        require(row["selected_T_scheme_row_emitted"] is False, f"{row['omega_id']} T_scheme overemitted")
        require(row["selected_K_threshold_row_emitted"] is False, f"{row['omega_id']} K overemitted")
        require(row["accepted_as_no_knob_source_row"] is False, f"{row['omega_id']} no-knob overaccepted")
        require(row["observed_data_used_as_selector"] is False, f"{row['omega_id']} observed selector")
        require(row["target_fitting_used"] is False, f"{row['omega_id']} target fitting")

    require(cutset["next_required_artifact"] == NEXT, "cutset next mismatch")
    for phrase in [
        "retarded-overlap spectral-pairing lemma proved for charged sectors u,d,e",
        "nine strict charged L_rowlocal rows emitted from selected projector/H1 pairings",
        "independent Q_sel quadrature route no longer required for charged rows under this lemma",
        "direct empirical K import remains forbidden as no-knob selector",
    ]:
        require(phrase in cutset["closed_here"], f"cutset closed_here missing {phrase}")
    for phrase in [
        "selected T_scheme.* source rows",
        "selected lambda_H H-sector quartic/threshold payload",
        "ten selected K_threshold rows",
    ]:
        require(phrase in cutset["still_open"], f"cutset still_open missing {phrase}")

    for phrase in [
        "retarded-overlap spectral-pairing lemma proved : true",
        "strict charged L_rowlocal rows emitted          : 9",
        "selected T_scheme rows emitted                  : false",
        "selected lambda_H payload emitted               : false",
        "accepted selected K_threshold rows              : 0",
        "- u.gen1: 1.367835979172",
        "- d.gen2: 0.683917989586",
        "- e.gen3: 0.683917989586",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
