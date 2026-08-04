"""Audit the q79 Weyl-pair source-provenance reduction."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEP_SCRIPT = ROOT / "scripts" / "analyze_q79_routec_weylpair_aselected_assembly_or_source_proof.py"
SCRIPT = ROOT / "scripts" / "analyze_q79_routec_weylpair_source_provenance_lemma.py"
CERT = ROOT / "certificates" / "q79_routec_weylpair_source_provenance_lemma_certificate.json"
CANDIDATE = ROOT / "candidate_data" / "q79_routec_weylpair_source_provenance_lemma.candidate.json"
TABLE = (
    ROOT
    / "candidate_data"
    / "q79_routec_weylpair_source_provenance_lemma"
    / "source_provenance_reduction_table.json"
)
PAPER = ROOT / "proof_corpus" / "Q79_RouteC_WeylPair_Source_Provenance_Lemma_v1.md"

EXPECTED_STATUS = (
    "Q79_ROUTEC_WEYLPAIR_SOURCE_PROVENANCE_REDUCED_SOURCE_LEVEL_CARRIER_CLOSED_SECTOR_CHARGE_OPEN"
)
EXPECTED_NEXT = "Q79_Selected_RouteC_WeylPair_SectorCharge_or_Chirality_Certificate_v1"

EXPECTED_Q79 = {
    "weylpair_conditional_A_solve": "Q79_ROUTEC_WEYLPAIR_CONDITIONAL_A_SOLVE_BUILT_SOURCE_PROVENANCE_OPEN",
    "e6_to_sm_dictionary": "REPRESENTATION_DICTIONARY_CLOSED_HIGGS_SELECTION_OPEN",
    "qutrit_line_cycle_restrictions": "TIME_ORIENTED_M1_QUTRIT_LINE_CYCLE_RESTRICTIONS_CLOSED_VISIBLE_CYCLE_LIST_OPEN",
    "c6_orientation_branch_reduction": "IWASAWA_C6_ORIENTATION_BRANCH_REDUCED_UNIQUE_BRANCH_OPEN",
    "orientation_de_dotd_bridge": "IWASAWA_ORIENTATION_DE_DOTD_BRIDGE_REDUCED_TO_CONJUGATE_PAIR_OPERATOR_OPEN",
    "su5_qutrit_polarization_attempt": "SELECTED_SU5_QUTRIT_POLARIZATION_PACKET_ATTEMPT_FINITE_PASS_SELECTION_OPEN",
}

EXPECTED_ADJACENT = {
    "sm_weylpair_source_provenance": (
        "MTT_SELECTED_ROUTEC_WEYLPAIR_SOURCE_PROVENANCE_REDUCED_SOURCE_LEVEL_CARRIER_CLOSED_C1_TRANSFER_OPEN"
    ),
    "sm_weylpair_source_to_c1_transfer": (
        "MTT_SELECTED_ROUTEC_WEYLPAIR_SOURCE_TO_C1_TRANSFER_MAP_BUILT_CONDITIONAL_EXACT_SECTOR_ROUTING_OPEN"
    ),
    "sm_weylpair_sector_routing": (
        "MTT_SELECTED_ROUTEC_WEYLPAIR_SECTOR_ROUTING_ATTEMPT_BUILT_NOT_UNIQUELY_SELECTED_BY_CURRENT_DATA"
    ),
    "sm_source_provenance_or_basis": (
        "MTT_SELECTED_ROUTEC_PROVENANCE_AND_BASIS_ATTEMPT_SUPPORT_CLOSED_PRIMITIVES_OPEN"
    ),
    "sm_selected_primitive_emission_search": (
        "MTT_SELECTED_ROUTEC_PRIMITIVE_EMISSION_SEARCH_EXECUTED_NO_LEGAL_EMISSION_FOUND"
    ),
    "gr_source_provenance_or_basis_import": (
        "ROUTEC_PROVENANCE_BASIS_SUPPORT_CLOSED_SELECTED_PRIMITIVES_OPEN"
    ),
    "gr_selected_primitive_emission_search_import": (
        "ROUTEC_SELECTED_PRIMITIVE_EMISSION_SEARCH_IMPORTED_NO_LEGAL_EMISSION_FOUND"
    ),
}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def close_to(value: float, expected: float, tol: float = 1.0e-9) -> bool:
    return math.isclose(float(value), expected, rel_tol=tol, abs_tol=tol)


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
    run(DEP_SCRIPT, failures)
    run(SCRIPT, failures)

    for path in (CERT, CANDIDATE, TABLE, PAPER):
        require(path.exists(), f"missing artifact: {path}", failures)
    if failures:
        print("\n".join(failures))
        return 1

    cert = load(CERT)
    candidate = load(CANDIDATE)
    table = load(TABLE)
    paper = PAPER.read_text(encoding="utf-8")

    require(cert == candidate, "certificate and candidate JSON differ", failures)
    require(table == cert["source_provenance_reduction"], "provenance table mismatch", failures)
    require(cert["status"] == EXPECTED_STATUS, f"unexpected status: {cert['status']}", failures)
    require(cert["next_required_artifact"] == EXPECTED_NEXT, "unexpected next artifact", failures)
    require(cert["closure_claimed"] is False, "closure must stay false", failures)
    require(cert["target_fitting_used"] is False, "target fitting must stay false", failures)

    for name, status in EXPECTED_Q79.items():
        require(
            cert["q79_input_statuses"][name]["status"] == status,
            f"unexpected q79 status for {name}: {cert['q79_input_statuses'][name]['status']}",
            failures,
        )
    for name, status in EXPECTED_ADJACENT.items():
        require(
            cert["adjacent_input_statuses"][name]["status"] == status,
            f"unexpected adjacent status for {name}: {cert['adjacent_input_statuses'][name]['status']}",
            failures,
        )

    support = cert["support_reductions"]
    require(all(support.values()), "support reductions must all pass", failures)

    reduction = cert["source_provenance_reduction"]
    carrier = reduction["source_level_carrier"]
    active = reduction["active_shift"]
    transfer = reduction["source_to_c1_transfer"]
    routing = reduction["sector_routing"]
    q79_evidence = reduction["q79_internal_sector_evidence"]
    primitive = reduction["primitive_emission_search"]

    require(carrier["proved"] is True, "source-level carrier not proved", failures)
    require(carrier["selected_by_mtt_at_s3_level"] is True, "S3 source selection missing", failures)
    require(
        carrier["source_level_projective_class_selected"] is True,
        "source-level projective class not selected",
        failures,
    )
    require(
        carrier["operator_level_projective_rhoE_promoted"] is False,
        "operator rhoE promotion overclaimed",
        failures,
    )
    require(close_to(carrier["g1_equals_phase_Z_residual"], 0.0), "g1/Z residual too large", failures)
    require(close_to(carrier["g1_order3_residual"], 0.0), "g1 order residual too large", failures)
    require(close_to(carrier["g2_equals_shift_X_residual"], 0.0), "g2/X residual too large", failures)
    require(close_to(carrier["g2_order3_residual"], 0.0), "g2 order residual too large", failures)
    require(active["proved"] is True, "active shift provenance not proved", failures)
    require(active["nonzero_active_shifts"] == [[1, 1]], "active shift must be [[1,1]]", failures)

    require(transfer["conditional_exact"] is True, "conditional transfer not exact", failures)
    require(close_to(transfer["phase_residual"], 0.0), "phase transfer residual nonzero", failures)
    require(close_to(transfer["shift_residual"], 0.0), "shift transfer residual nonzero", failures)
    for key in (
        "selected_transfer_map_emitted",
        "selected_sector_routing_emitted",
        "selected_normalization_emitted",
        "promote_to_A_selected_allowed",
    ):
        require(transfer[key] is False, f"transfer overclaim: {key}", failures)

    routes = routing["all_two_two_partitions_tested"]
    exact_rows = routing["exact_rows_relative_to_locked_columns"]
    require(len(routes) == 6, "must enumerate six two-two sector routes", failures)
    require(len(exact_rows) == 1, "locked columns should identify exactly one route", failures)
    if exact_rows:
        require(exact_rows[0]["phase_route"] == ["u", "e"], "wrong exact phase route", failures)
        require(exact_rows[0]["shift_route"] == ["d", "nuD"], "wrong exact shift route", failures)
        require(exact_rows[0]["matches_locked_columns"] is True, "exact route must match", failures)
    require(
        routing["source_data_independently_selects_route"] is False,
        "sector route overselected",
        failures,
    )
    require(routing["target_columns_select_route"] is True, "target-column uniqueness not recorded", failures)
    require(routing["fully_proved"] is False, "sector routing overproved", failures)
    require(routing["proved_by_locked_columns"] is True, "locked-column diagnostic should pass", failures)
    require(routing["proved_by_selected_source"] is False, "selected-source sector route overproved", failures)

    require(q79_evidence["e6_representation_bridge_closed"] is True, "E6 bridge should be closed", failures)
    require(
        q79_evidence["e6_rank_one_seed_sector_assignment_open"] is True,
        "E6 sector assignment must remain open",
        failures,
    )
    require(
        q79_evidence["qutrit_clock_shift_lines_validated"] is True,
        "qutrit line packet should validate",
        failures,
    )
    require(
        q79_evidence["qutrit_complete_visible_cycle_list_open"] is True,
        "complete visible cycle list must remain open",
        failures,
    )
    require(
        q79_evidence["c6_orientation_reduced_not_selected"] is True,
        "C6 orientation should be reduced but not selected",
        failures,
    )
    require(
        q79_evidence["su5_qutrit_finite_packet_validated"] is True,
        "SU5 qutrit finite packet should validate",
        failures,
    )
    require(
        q79_evidence["su5_qutrit_selected_source_available"] is False,
        "SU5 selected source overclaimed",
        failures,
    )
    for key in ("selected_primitives_found", "R1_promotes", "R4_promotes", "R6_ready"):
        require(primitive[key] is False, f"primitive overclaim: {key}", failures)

    decision = cert["decision"]
    for key in (
        "source_level_weyl_carrier_and_active_shift_proved",
        "conditional_source_to_C1_transfer_exact",
        "locked_columns_uniquely_identify_intended_sector_route",
    ):
        require(decision[key] is True, f"decision flag false: {key}", failures)
    for key in (
        "full_selected_weylpair_source_provenance_proved",
        "locked_columns_used_as_selector",
        "selected_sector_route_independently_proved",
        "selected_transfer_map_emitted",
        "selected_primitives_found",
        "conditional_A_promoted_to_A_selected",
        "b_selected_emitted",
        "honest_selected_deltaTheta_C1_solve_run",
        "target_fitting_used",
    ):
        require(decision[key] is False, f"decision overclaim: {key}", failures)

    closed = cert["closed_by_this_attempt"]
    for key in (
        "source_level_weyl_carrier_provenance_closed",
        "active_shift_1_1_provenance_closed",
        "conditional_source_to_C1_transfer_exact",
        "all_two_two_sector_routes_enumerated",
        "locked_columns_identify_intended_route_uniquely",
        "current_proof_blocker_identified",
        "target_fitting_excluded",
    ):
        require(closed[key] is True, f"closed flag false: {key}", failures)

    still_open = cert["still_open"]
    for key in (
        "selected_sector_charge_or_chirality_certificate",
        "source_derivation_of_u_e_phase_route",
        "source_derivation_of_d_nuD_shift_route",
        "selected_transfer_normalization",
        "promote_conditional_A_to_A_selected",
        "Phi_fin_selected_payload",
        "quotient_valid_BN_basis_certificate",
        "full_SM_or_no_knob_closure",
    ):
        require(still_open[key] is True, f"open flag missing: {key}", failures)

    require(all(value is False for value in cert["guardrails"].values()), "guardrail false-map violated", failures)
    require(cert["theorem"]["proved"] is True, "theorem must be proved", failures)
    require(cert["theorem"]["closure_claimed"] is False, "theorem closure must stay false", failures)

    for phrase in (
        "partly proved and partly reduced",
        "The full selected provenance lemma is **not** proved yet",
        "All two-two routes",
        "Q79WeylPairSourceProvenanceReductionTheorem",
        EXPECTED_NEXT,
    ):
        require(phrase in paper, f"paper missing phrase: {phrase}", failures)

    if failures:
        print("Q79 Weyl-pair source provenance audit FAILED")
        print("\n".join(f"- {failure}" for failure in failures))
        return 1

    print("Q79 Weyl-pair source provenance audit PASS")
    print(f"status: {cert['status']}")
    print("source carrier: g1=Z, g2=X, active shift=(1,1)")
    print("conditional transfer residuals: phase=0, shift=0")
    print(f"next: {cert['next_required_artifact']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
