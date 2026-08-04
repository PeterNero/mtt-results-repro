"""Audit Qa/SU3 selected monad value attempt and D_E import gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
BUILDER = ROOT / "scripts" / "build_selected_qasu3_selectedmonaddevalues_or_bn27strictsourcetheorem.py"

SLUG = "selected_qasu3_selectedmonaddevalues_or_bn27strictsourcetheorem"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_QaSU3_SelectedMonadDEValues_or_BN27StrictSourceTheorem_v1.md"
PRIMITIVE_PACKET = PACKET_DIR / "primitive_balanced_monad_value_selection_attempt.packet.json"
DE_PACKET = PACKET_DIR / "finite_de_operator_value_import_and_promotion_gate.packet.json"
ACCEPTANCE_PACKET = PACKET_DIR / "selected_value_acceptance_result.packet.json"
NEXT_PACKET = PACKET_DIR / "next_strict_selector_or_full_operator_values_contract.packet.json"

STATUS = (
    "MTT_SELECTED_QASU3_SELECTEDMONADDEVALUES_OR_BN27STRICTSOURCETHEOREM_"
    "PRIMITIVE_VALUES_SELECTED_DE_VALUES_IMPORTED_STRICT_PROMOTION_OPEN"
)
NEXT = "MTT_Selected_PrimitiveMonadValueSelectorTheorem_or_FullDEOperatorValues_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    primitive = load(PRIMITIVE_PACKET)
    de = load(DE_PACKET)
    acceptance = load(ACCEPTANCE_PACKET)
    next_packet = load(NEXT_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(next_packet["next_required_artifact"] == NEXT, "next packet mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem not marked proved")
    require(cert["theorem_proved"] is True, "certificate theorem flag missing")

    for payload in [candidate, cert, primitive, de, acceptance, next_packet]:
        require(payload["closure_claimed"] is True, "closure boundary missing")
        require(payload["observed_data_used_as_selector"] is False, "observed selector used")
        require(payload["target_fitting_used"] is False, "target fitting used")

    decision = candidate["closure_decision"]
    require(decision["serious_value_selection_attempt_executed"] is True, "serious attempt missing")
    require(decision["primitive_integer_selector_constructed"] is True, "primitive selector missing")
    require(decision["proposed_f_values_count"] == 5, "f value count mismatch")
    require(decision["proposed_g_values_count"] == 5, "g value count mismatch")
    require(decision["proposed_mu_values_count"] == 5, "mu value count mismatch")
    require(decision["candidate_g_after_f_zero_exact"] is True, "gf zero not exact")
    require(decision["primitive_selector_unique_under_declared_constraints"] is True, "selector uniqueness failed")
    require(decision["D_E_gap_layer_selected"] is True, "D_E gap layer not selected")
    require(decision["D_E_finite_value_shapes_imported"] is True, "D_E finite values not imported")
    require(decision["final_same_source_connection_tables_accepted"] == 0, "final tables overaccepted")

    for key in [
        "selector_derived_from_MTT_source",
        "selected_f_g_values_accepted_as_strict_source",
        "selected_mu_values_accepted_as_strict_source",
        "full_DE_operator_values_selected",
        "strict_BN27_source_theorem_derived",
        "direct_H_K_row_emitted",
        "strict_no_knob_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"overclaim in decision: {key}")
        require(cert[key] is False, f"overclaim in certificate: {key}")

    selector = primitive["selection_functional"]
    require(selector["name"] == "PrimitiveBalancedTerminalCancellationSelector", "selector name mismatch")
    require(selector["derived_from_mtt_geometry"] is False, "selector overderived")
    values = primitive["selected_candidate_values"]
    require(values["f_entries"] == {f"a_{i}": 1 for i in range(1, 6)}, "f entries mismatch")
    require(values["g_entries"] == {f"b_{i}": 1 for i in range(1, 6)}, "g entries mismatch")
    require(values["multiplication_constants_mu"] == [1, 1, 1, 1, -4], "mu entries mismatch")
    require(values["gf_terms"] == [1, 1, 1, 1, -4], "gf terms mismatch")
    require(values["gf_sum"] == 0, "gf sum mismatch")
    require(values["gf_zero_exact"] is True, "gf exact flag mismatch")
    require(values["primitive_gcd"] == 1, "primitive gcd mismatch")
    require(values["all_f_g_nonzero"] is True, "nonzero f/g check failed")
    require(values["all_product_charge_typings_pass"] is True, "charge typing failed")
    require(values["all_ctwist_product_typings_pass"] is True, "c-twist typing failed")
    require(primitive["finite_search_certificate"]["solutions"] == [[1, 1, 1, 1, -4]], "search solutions mismatch")
    require(
        primitive["finite_search_certificate"]["unique_solution_under_declared_selector_class"] is True,
        "declared selector uniqueness failed",
    )
    require(primitive["accepted_as_strict_mtt_source_values"] is False, "primitive values overaccepted")

    require(de["status"] == "FINITE_DE_VALUES_IMPORTED_SELECTED_TRACE_OR_FULL_OPERATOR_PROMOTION_OPEN", "D_E status")
    progress = de["value_shape_progress"]
    for key in [
        "D_E_matrix_on_27_mode_BN_emitted",
        "Riesz_and_Green_gap_emitted",
        "dotD_alpha1_matrix_emitted",
        "sector_projectors_emitted",
        "nonidentity_projective_rhoE_candidate_built",
        "first_tracefree_HYM_correction_computed",
    ]:
        require(progress[key] is True, f"D_E value shape missing: {key}")
    gate = de["promotion_gate"]
    for key in [
        "selected_trace_equality",
        "full_selected_operator_formula",
        "selected_gap_error_certificate",
        "rhoE_selected_by_mtt",
        "honest_replay_without_lifted_flags",
        "selected_finite_connection_solve_closed",
    ]:
        require(gate[key] is False, f"D_E promotion overclaimed: {key}")
    require(de["accepted_as_full_same_source_operator_values"] is False, "D_E values overaccepted")

    strict = acceptance["strict_acceptance"]
    require(strict["accepted_monad_value_rows_as_candidate_rule"] == 1, "candidate row count mismatch")
    require(strict["accepted_strict_mtt_source_value_rows"] == 0, "strict rows overaccepted")
    require(strict["accepted_final_same_source_connection_tables"] == 0, "final tables overaccepted")
    require(strict["required_final_same_source_connection_tables"] == 8, "required table count mismatch")
    for key in [
        "selector_derived_from_mtt_geometry",
        "selected_actual_cech_cocycles_supplied",
        "selected_actual_hym_connection_coefficients_supplied",
        "full_same_source_DE_or_rhoE_values_supplied",
        "strict_BN27_source_theorem_derived",
    ]:
        require(strict[key] is False, f"strict acceptance overclaimed: {key}")

    require("Candidate multiplication constants: `[1, 1, 1, 1, -4]`" in note, "note missing mu")
    require("Candidate `g after f = 0`: `true`" in note, "note missing gf exact")
    require("Final same-source connection tables accepted: `0/8`" in note, "note missing acceptance")
    require(NEXT in note, "note missing next artifact")

    print("Qa/SU3 selected monad D_E value attempt audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
