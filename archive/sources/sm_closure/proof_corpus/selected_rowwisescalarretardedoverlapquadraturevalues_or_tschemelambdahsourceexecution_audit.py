"""Audit rowwise scalar retarded-overlap spectral support packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_rowwisescalarretardedoverlapquadraturevalues_or_tschemelambdahsourceexecution"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SPECTRAL_EVALUATOR = PACKET_DIR / "charged_spectral_lrowlocal_evaluator_attempt.packet.json"
STRICT_GATE = PACKET_DIR / "strict_lrowlocal_acceptance_gate_after_spectral_evaluator.packet.json"
KROW_STATUS = PACKET_DIR / "krow_status_after_spectral_lrowlocal_attempt.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_rowwise_scalar_quadrature_attempt.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_RowwiseScalarRetardedOverlapQuadratureValues_or_TSchemeLambdaHExecution_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_ROWWISESCALARRETARDEDOVERLAPQUADRATUREVALUES_OR_TSCHEMELAMBDAHSOURCEEXECUTION_"
    "BUILT_SPECTRAL_SUPPORT_STRICT_QUADRATURE_EQUALITY_OPEN"
)
NEXT = "MTT_Selected_RetardedOverlapSpectralPairingLemma_or_IndependentQuadratureValues_v1"


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
    spectral = load(SPECTRAL_EVALUATOR)
    strict_gate = load(STRICT_GATE)
    krow_status = load(KROW_STATUS)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("certificate", cert),
        ("spectral evaluator", spectral),
        ("strict gate", strict_gate),
        ("K row status", krow_status),
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
    require(decision["selected_family_projector_basis_closed"] is True, "family projector basis not closed")
    require(decision["selected_basis_map_closed"] is True, "basis map not closed")
    require(decision["dynamic_first_response_support_available"] is True, "dynamic support missing")
    require(decision["charged_spectral_support_rows_emitted"] == 9, "support row count mismatch")
    require(decision["spectral_support_rows_promoted_to_strict_Lrowlocal"] is False, "support rows overpromoted")
    require(decision["retarded_overlap_equals_spectral_pairing_theorem_proved"] is False, "equality lemma overclaimed")
    require(decision["independent_selected_quadrature_values_emitted"] is False, "quadrature values overemitted")
    require(decision["selected_T_scheme_rows_emitted"] is False, "T_scheme overemitted")
    require(decision["selected_lambda_H_payload_emitted"] is False, "lambda_H overemitted")
    require(decision["accepted_selected_L_rowlocal_row_count"] == 0, "L rows overaccepted")
    require(decision["accepted_selected_K_source_row_count"] == 0, "K rows overaccepted")
    require(decision["accepted_internal_scalar_value_row_count"] == 0, "scalar rows overaccepted")
    require(decision["true_SM_equivalence_closed"] is False, "true SM closure overclaimed")
    require(decision["full_no_knob_closed"] is False, "full no-knob closure overclaimed")

    require(
        spectral["status"] == "SELECTED_SPECTRAL_SUPPORT_ROWS_EMITTED_STRICT_LROWLOCAL_OPEN",
        "spectral evaluator status mismatch",
    )
    selected_inputs = spectral["selected_inputs"]
    require(selected_inputs["all_sector_projector_bases_closed"] is True, "projectors not closed")
    require(selected_inputs["basis_map_to_sector_scaled_magnitude_rows_closed"] is True, "basis map not closed")
    require(
        selected_inputs["rowlocal_functional_status"]
        == "ROWLOCAL_HYM_GREEN_QUADRATURE_FUNCTIONAL_DEFINED_VALUES_REQUIRE_SELECTED_KERNEL",
        "rowlocal functional status mismatch",
    )
    candidate = spectral["spectral_pairing_candidate"]
    require(candidate["formula"] == "L_spectral_support(s,g)=abs(Tr(P_s,g H1_s))", "formula mismatch")
    require(candidate["row_count"] == 9, "spectral support row count mismatch")
    require(candidate["charged_sectors"] == ["d", "e", "u"], "charged sectors mismatch")
    require(candidate["basis_invariant_projector_pairing"] is True, "basis invariant flag missing")
    require(candidate["selected_source_inputs_verified"] is True, "selected inputs not verified")
    require(candidate["accepted_as_selected_spectral_support_rows"] is True, "support not accepted")
    require(candidate["accepted_as_strict_L_rowlocal_rows"] is False, "strict L rows overaccepted")
    require(
        candidate["strict_Lrowlocal_blocker"]
        == "retarded_overlap_equals_spectral_pairing_theorem_or_independent_Q_sel_values_absent",
        "strict blocker mismatch",
    )
    require(len(candidate["distinct_support_values"]) == 2, "distinct support count mismatch")
    require_close(candidate["distinct_support_values"][0], 0.683917989586, "small support value mismatch")
    require_close(candidate["distinct_support_values"][1], 1.367835979172, "large support value mismatch")

    expected_by_gen = {1: 1.367835979172, 2: 0.683917989586, 3: 0.683917989586}
    seen = {(row["sector"], row["generation"]) for row in candidate["rows"]}
    require(seen == {(sector, gen) for sector in ["u", "d", "e"] for gen in [1, 2, 3]}, "support rows missing")
    for row in candidate["rows"]:
        require(row["accepted_as_selected_spectral_support_row"] is True, f"{row['row_id']} support not accepted")
        require(row["accepted_as_strict_L_rowlocal_row"] is False, f"{row['row_id']} strict L overaccepted")
        require(row["accepted_as_K_threshold_row"] is False, f"{row['row_id']} K overaccepted")
        require(row["observed_data_used_as_selector"] is False, f"{row['row_id']} observed selector")
        require(row["target_fitting_used"] is False, f"{row['row_id']} target fitting")
        require_close(
            row["selected_spectral_support_scalar"],
            expected_by_gen[row["generation"]],
            f"{row['row_id']} support value mismatch",
        )

    shortcuts = spectral["candidate_shortcuts_rejected"]
    require([shortcut["accepted_as_strict_L_rowlocal_rows"] for shortcut in shortcuts] == [False, False, False], "shortcut accepted")
    require(shortcuts[0]["candidate"] == "ordered_basis_diagonal_abs_H1", "ordered diagonal shortcut missing")
    require(shortcuts[1]["candidate"] == "correction_dY_diagonal_or_eigenprofile", "correction shortcut missing")
    require(shortcuts[2]["candidate"] == "controlled_empirical_K_import", "empirical shortcut missing")

    require(
        strict_gate["status"] == "SPECTRAL_SUPPORT_AVAILABLE_STRICT_LROWLOCAL_ACCEPTANCE_BLOCKED",
        "strict gate status mismatch",
    )
    available = strict_gate["available_inputs"]
    require(available["selected_family_projectors_closed"] is True, "strict gate projector input missing")
    require(available["selected_basis_map_closed"] is True, "strict gate basis input missing")
    require(available["selected_dynamic_first_response_support_available"] is True, "strict gate dynamic input missing")
    require(available["rowlocal_functional_contract_defined"] is True, "strict gate functional input missing")
    require(available["charged_spectral_support_rows_emitted"] == 9, "strict gate support count mismatch")
    require(available["no_empirical_selector_used"] is True, "empirical selector used")
    requirements = strict_gate["strict_acceptance_requirements"]
    require(requirements["retarded_overlap_equals_spectral_pairing_theorem_proved"] is False, "equality lemma overclaimed")
    require(requirements["independent_selected_finite_quadrature_Q_sel_values_emitted"] is False, "Q_sel overemitted")
    require(requirements["selected_T_scheme_rows_emitted"] is False, "T_scheme overemitted")
    require(requirements["selected_lambda_H_value_row_emitted"] is False, "lambda_H overemitted")
    require(strict_gate["accepted_selected_spectral_support_row_count"] == 9, "accepted support count mismatch")
    require(strict_gate["accepted_strict_Lrowlocal_row_count"] == 0, "strict L row count mismatch")
    require(strict_gate["accepted_selected_K_source_row_count"] == 0, "K row count mismatch")
    require(strict_gate["accepted_internal_scalar_value_row_count"] == 0, "scalar row count mismatch")
    require(strict_gate["can_close_K_rows_now"] is False, "K rows should not close")

    require(krow_status["status"] == "NINE_SPECTRAL_SUPPORT_ROWS_ZERO_STRICT_K_ROWS", "K status mismatch")
    require(krow_status["row_count"] == 10, "K grammar row count mismatch")
    require(krow_status["charged_spectral_support_rows_emitted"] == 9, "K support count mismatch")
    require(krow_status["accepted_selected_L_rowlocal_row_count"] == 0, "K L-row count mismatch")
    require(krow_status["accepted_T_scheme_row_count"] == 0, "K T-scheme count mismatch")
    require(krow_status["accepted_selected_K_source_row_count"] == 0, "selected K count mismatch")
    require(krow_status["accepted_internal_scalar_value_row_count"] == 0, "scalar count mismatch")
    require(krow_status["lambda_H_value_row_emitted"] is False, "lambda_H overemitted")
    require(krow_status["empirical_K_row_count"] == 10, "empirical K count mismatch")
    require(krow_status["previous_dynamic_retarded_row_count"] == 10, "previous row count mismatch")
    for row in krow_status["rows"]:
        if row["sector"] == "H":
            require(row["selected_spectral_support_available"] is False, "H support overemitted")
            require(row["selected_spectral_support_scalar"] is None, "H support scalar overemitted")
            require(row["selected_lambda_H_payload_emitted"] is False, "H lambda overemitted")
        else:
            require(row["selected_spectral_support_available"] is True, f"{row['omega_id']} support missing")
            require(row["selected_spectral_support_scalar"] is not None, f"{row['omega_id']} scalar missing")
            require(row["selected_lambda_H_payload_emitted"] is None, f"{row['omega_id']} lambda marker mismatch")
        require(row["selected_strict_L_rowlocal_value_emitted"] is False, f"{row['omega_id']} L overemitted")
        require(row["selected_T_scheme_row_emitted"] is False, f"{row['omega_id']} T_scheme overemitted")
        require(row["selected_K_threshold_row_emitted"] is False, f"{row['omega_id']} K overemitted")
        require(row["accepted_as_no_knob_source_row"] is False, f"{row['omega_id']} no-knob overaccepted")
        require(row["observed_data_used_as_selector"] is False, f"{row['omega_id']} observed selector")
        require(row["target_fitting_used"] is False, f"{row['omega_id']} target fitting")

    require(cutset["next_required_artifact"] == NEXT, "cutset next mismatch")
    for phrase in [
        "selected family spectral projector basis reused as row evaluator support",
        "nine charged basis-invariant spectral support scalars emitted",
        "ordered-basis diagonal and correction-matrix shortcuts rejected as strict row-local values",
        "strict L_rowlocal/K-row acceptance gate reduced to one equality lemma or direct selected quadrature execution",
    ]:
        require(phrase in cutset["closed_here"], f"cutset closed_here missing {phrase}")
    for phrase in [
        "prove K_row(A_HYM,G,dotD_alpha1) equals the selected H1 spectral projector pairing on the selected row basis",
        "or independently execute selected finite quadrature Q_sel values for L_rowlocal(s,g)",
        "instantiate selected T_scheme.* source rows",
        "emit selected lambda_H H-sector quartic/threshold payload",
        "emit ten selected K_threshold rows",
    ]:
        require(phrase in cutset["still_open"], f"cutset still_open missing {phrase}")

    for phrase in [
        "selected spectral support scalar rows       : 9",
        "strict L_rowlocal rows accepted             : 0",
        "selected T_scheme rows emitted              : false",
        "selected lambda_H payload emitted           : false",
        "accepted selected K rows                    : 0",
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
