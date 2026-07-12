"""Audit q79 typed-monad/Cech or HYM connection witness attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEP = ROOT / "scripts" / "analyze_q79_routec_selected_source_certificate_or_typed_de_construction.py"
SCRIPT = ROOT / "scripts" / "analyze_q79_typed_monad_cech_or_hym_connection_witness.py"
CERT = ROOT / "certificates" / "q79_typed_monad_cech_or_hym_connection_witness_certificate.json"
CANDIDATE = ROOT / "candidate_data" / "q79_typed_monad_cech_or_hym_connection_witness.candidate.json"
OUT_DIR = ROOT / "candidate_data" / "q79_typed_monad_cech_or_hym_connection_witness"
CORPUS_SUMMARY = OUT_DIR / "corpus_witness_search_summary.json"
TYPED_REJECTION = OUT_DIR / "typed_monad_candidate_from_flux_phrase.rejected.json"
SMOKE_NOGO = OUT_DIR / "routec_smoke_promotion_nogo.json"
WITNESS_ATTEMPT = OUT_DIR / "selected_connection_witness_attempt.open.json"
PAYLOAD = OUT_DIR / "minimal_actual_witness_payload.open.json"
PAPER = ROOT / "proof_corpus" / "Q79_Typed_Monad_Cech_or_HYM_Connection_Witness_v1.md"

STATUS = "Q79_TYPED_MONAD_CECH_OR_HYM_CONNECTION_WITNESS_ATTEMPT_OPEN_VALUES_ABSENT"
NEXT = "Q79_Selected_Finite_Connection_Solve_Execution_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def run(script: Path, failures: list[str]) -> None:
    proc = subprocess.run(
        [sys.executable, str(script)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    require(proc.returncode == 0, f"{script.name} failed:\n{proc.stdout}", failures)


def main() -> int:
    failures: list[str] = []
    run(DEP, failures)
    run(SCRIPT, failures)
    for path in (CERT, CANDIDATE, CORPUS_SUMMARY, TYPED_REJECTION, SMOKE_NOGO, WITNESS_ATTEMPT, PAYLOAD, PAPER):
        require(path.exists(), f"missing artifact: {path}", failures)
    if failures:
        print("\n".join(failures))
        return 1

    cert = load(CERT)
    candidate = load(CANDIDATE)
    corpus_summary = load(CORPUS_SUMMARY)
    typed = load(TYPED_REJECTION)
    smoke = load(SMOKE_NOGO)
    witness = load(WITNESS_ATTEMPT)
    payload = load(PAYLOAD)
    paper = PAPER.read_text(encoding="utf-8")

    require(cert == candidate, "certificate and candidate differ", failures)
    require(cert["status"] == STATUS, f"unexpected status: {cert['status']}", failures)
    require(cert["next_required_artifact"] == NEXT, "unexpected next artifact", failures)
    require(cert["closure_claimed"] is False, "closure must stay false", failures)
    require(cert["target_fitting_used"] is False, "target fitting must stay false", failures)
    require(cert["prior_reduction_status"].endswith("OPEN_WITNESS_CONTRACT_CREATED"), "prior reduction not imported", failures)

    require(
        corpus_summary["status"]
        == "CORPUS_SEARCH_FINDS_TOPOLOGICAL_AND_EXISTENCE_DATA_NOT_WITNESS_VALUES",
        "corpus summary status wrong",
        failures,
    )
    require(
        corpus_summary["recovered_support"]["generic_constant_maps_phrase"] is True,
        "generic constant maps phrase should be recovered",
        failures,
    )
    for key in (
        "explicit_f_i_section_representatives",
        "explicit_g_i_section_representatives",
        "transition_functions_for_L_i_K1_K2",
        "Cech_cover_and_cocycles",
        "g_after_f_zero_certificate",
        "monad_exactness_or_sheaf_singularity_control",
        "selected_H1_E_representatives",
        "sector_projection_maps_Q_u_d_L_e_N_H",
        "dotD_alpha1_and_Green_operator_data",
    ):
        require(corpus_summary["not_recovered_witness_values"][key] is True, f"missing flag wrong: {key}", failures)
    require(corpus_summary["selected_D_E_source_found"] is False, "selected D_E source overfound", failures)

    require(typed["schema"] == "Q79TypedMonadFluxPhraseCandidateRejection.v1", "typed schema wrong", failures)
    require(typed["status"] == "REJECTED_AS_WITNESS", "typed route should be rejected", failures)
    require(typed["nonzero_scalar_constant_f_entries_type_valid"] is False, "f scalar typing wrong", failures)
    require(typed["nonzero_scalar_constant_g_entries_type_valid"] is False, "g scalar typing wrong", failures)
    require(typed["requires_global_holomorphic_sections_or_transition_data"] is True, "section requirement missing", failures)
    require(typed["can_verify_g_after_f_zero"] is False, "g after f should not verify", failures)
    require(typed["can_verify_monad_exactness"] is False, "exactness should not verify", failures)
    for key, value in typed["explicit_witness_data_present"].items():
        require(value is False, f"typed witness field unexpectedly present: {key}", failures)
    require(typed["verdict"]["constructs_typed_monad_cech_witness"] is False, "typed witness overconstructed", failures)

    require(smoke["schema"] == "Q79RouteCSmokePromotionNoGo.v1", "smoke schema wrong", failures)
    require(smoke["status"] == "CANNOT_PROMOTE_SMOKE_TO_SELECTED_WITNESS", "smoke no-go status wrong", failures)
    require(smoke["rhoE_mesh_candidate_kind"] == "identity_rhoE_smoke_unselected", "rhoE kind changed", failures)
    require(smoke["residuals_zero"] is True, "route-C residuals should be zero in smoke", failures)
    require(smoke["positive_gates_hold"] is True, "positive gates should hold in smoke", failures)
    require(smoke["selected_source_verified"] is False, "selected source should not verify", failures)
    require(smoke["route_c_residual_values_are_smoke_not_solve"] is True, "smoke flag missing", failures)
    require(smoke["selected_origin_still_missing"] is True, "selected origin should be missing", failures)
    require(smoke["honest_route_c_residual_pass"] is False, "honest route-C residual should fail", failures)
    require(smoke["lifted_flags_route_c_residual_pass"] is True, "lifted smoke should pass diagnostically", failures)
    require(smoke["claims_route_c_residual_solve"] is False, "route-C solve overclaimed", failures)
    require(smoke["claims_selected_D_E_constructed"] is False, "selected D_E overclaimed", failures)
    require(smoke["verdict"]["constructs_selected_connection_witness"] is False, "smoke witness overconstructed", failures)

    require(witness["schema"] == "Q79TypedMonadCechOrHYMConnectionWitnessAttempt.v1", "witness schema wrong", failures)
    require(witness["status"] == "OPEN_WITNESS_VALUES_ABSENT", "witness status wrong", failures)
    require(witness["constructs_actual_selected_witness"] is False, "actual witness overconstructed", failures)
    for route in witness["attempted_routes"].values():
        require(route["attempted"] is True, "route not attempted", failures)
        require(route["constructed"] is False, "route constructed unexpectedly", failures)
    for key, value in witness["candidate_values"].items():
        require(value is None, f"candidate value unexpectedly filled: {key}", failures)

    require(payload["schema"] == "Q79MinimalActualSelectedConnectionWitnessPayload.v1", "payload schema wrong", failures)
    require(payload["status"] == "OPEN", "payload status wrong", failures)
    require(
        set(payload["acceptable_payloads"])
        == {"typed_monad_cech_payload", "direct_hym_payload", "finite_routec_solve_payload"},
        "payload route set wrong",
        failures,
    )
    require("validate_selected_hym_operator_source.py" in payload["validator_chain_after_payload"], "validator chain incomplete", failures)
    for forbidden in ("observed masses", "observed CKM magnitudes", "Execution II benchmark Yukawa entries"):
        require(forbidden in payload["forbidden_inputs"], f"forbidden input missing: {forbidden}", failures)

    for key in (
        "corpus_checked_for_typed_monad_or_hym_witness_values",
        "generic_constant_maps_phrase_rejected_as_witness",
        "identity_rhoE_smoke_rejected_as_selected_witness",
        "direct_HYM_route_classified_as_abstract_existence_only",
        "minimal_actual_witness_payload_created",
    ):
        require(cert["what_closes_now"][key] is True, f"close flag false: {key}", failures)
    for key in (
        "actual_typed_f_i_g_i_sections",
        "actual_cech_transition_and_cocycle_data",
        "actual_g_after_f_zero_and_exactness_certificate",
        "actual_selected_HYM_connection_coefficients",
        "actual_selected_finite_routec_residual_solve",
        "honest_selected_DE_Riesz_Green_dotD_packets",
        "primitive_C1_values",
        "A_selected_b_selected_full_SM_closure",
    ):
        require(cert["what_remains_open"][key] is True, f"remaining flag false: {key}", failures)

    for key, value in cert["guardrails"].items():
        require(value is False, f"guardrail violated: {key}", failures)

    for phrase in (
        "typed monad/Cech or HYM connection witness is not constructed from the current corpus",
        "generic constant maps phrase",
        "not globally typed",
        "identity-rho smoke",
        "cannot be promoted",
        "minimal actual witness payload",
        "selected finite Route-C solve",
        "Q79TypedMonadCechOrHYMConnectionWitnessExhaustionTheorem",
        "not full SM closure",
        NEXT,
    ):
        require(phrase in paper, f"paper missing phrase: {phrase}", failures)

    if failures:
        print("Q79 typed monad/Cech or HYM connection witness audit FAILED")
        print("\n".join(f"- {failure}" for failure in failures))
        return 1

    print("Q79 typed monad/Cech or HYM connection witness audit PASS")
    print(f"status: {cert['status']}")
    print(f"next: {cert['next_required_artifact']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
