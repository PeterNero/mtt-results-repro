"""Audit the q79 selected Phi_fin alpha1 payload closure gate."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "analyze_q79_selected_phifin_alpha1_payload.py"
CERT = ROOT / "certificates" / "q79_selected_phifin_alpha1_payload_certificate.json"
CANDIDATE = ROOT / "candidate_data" / "q79_selected_phifin_alpha1_payload.candidate.json"
TABLE = ROOT / "candidate_data" / "q79_selected_phifin_alpha1_payload" / "closure_gate_table.json"
PAPER = ROOT / "proof_corpus" / "Q79_Selected_PhiFin_Alpha1_Payload_v1.md"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: object


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def run_script() -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def contains_all(text: str, needles: list[str]) -> bool:
    return all(needle in text for needle in needles)


def main() -> int:
    proc = run_script()
    cert = load(CERT)
    candidate = load(CANDIDATE)
    table = load(TABLE)
    paper = read(PAPER)

    expected_status = (
        "Q79_SELECTED_PHIFIN_ALPHA1_PAYLOAD_CLOSURE_GATE_CLOSED_SELECTED_EMISSION_OPEN"
    )
    closure = cert.get("closure_test", {})
    closure_table = cert.get("closure_gate_table", {})
    shape = closure_table.get("finite_shape_gates", {})
    selected_flags = closure_table.get("selected_payload_flags", {})
    alpha_support = closure_table.get("alpha1_support_gates", {})
    alpha_missing = closure_table.get("alpha1_missing_selected_values", {})
    adjacent = cert.get("adjacent_update_implications", {})
    closed = cert.get("closed_by_this_attempt", {})
    still_open = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})
    statuses = cert.get("adjacent_input_statuses", {})
    repos = cert.get("repo_snapshots", {})

    selected_flags_refuse_promotion = (
        selected_flags.get("route_c_residual_selected_source") is False
        and selected_flags.get("rhoE_selected_by_mtt") is False
        and selected_flags.get("rhoE_nonidentity") is False
        and selected_flags.get("de_action_selected_source") is False
        and selected_flags.get("riesz_gap_selected_source") is False
        and selected_flags.get("reduced_green_selected_source") is False
        and selected_flags.get("dotd_selected_source") is False
        and selected_flags.get("dotd_alpha1_driver") is False
    )

    adjacent_statuses_expected = (
        statuses.get("qa_chi", {}).get("status")
        == "QA_SU3_SELECTED_FINITE_RESPONSE_FUNCTIONAL_CHI_QA_CLOSED_MEASURED_MATCH_OPEN"
        and statuses.get("qa_electroweak_matching", {}).get("status")
        == "QA_SU3_ELECTROWEAK_MATCHING_INTERFACE_BUILT_ABSOLUTE_K_GAUGE_OPEN"
        and statuses.get("qa_u1_su2_same_scheme", {}).get("status")
        == "U1_SU2_SAME_SCHEME_ACCEPTANCE_CONTRACT_BUILT_PAYLOADS_AND_K_GAUGE_OPEN"
        and statuses.get("qa_u1_su2_source_fill", {}).get("status")
        == "U1_SU2_K_GAUGE_FILL_ATTEMPT_TEMPLATE_BUILT_CURRENT_SOURCE_PARTIAL_ONLY"
        and statuses.get("constants_higher_order", {}).get("status")
        == "HIGHER_ORDER_FLAVOR_SPLITTING_CRITERION_IMPORTED_SELECTED_EMISSION_OPEN"
        and statuses.get("constants_selected_correction_gate", {}).get("status")
        == "SELECTED_CORRECTION_EMISSION_GATE_REDUCED_NONIDENTITY_RHOE_AND_BN_CONSTRUCTION_OPEN"
        and statuses.get("constants_c1_response_operator_import", {}).get("status")
        == "SELECTED_C1_RESPONSE_OPERATOR_EMISSION_AUDITED_A_SELECTED_NOT_EMITTED"
        and statuses.get("constants_c1_operator_source_rebuild", {}).get("status")
        == "SELECTED_C1_OPERATOR_REBUILD_ATTEMPT_EXECUTED_SELECTED_BLOCKS_STILL_OPEN"
        and statuses.get("constants_routec_rhoe_bn_prefix", {}).get("status")
        == "ROUTEC_RHOE_BN_OPERATOR_PREFIX_IMPORTED_NONINVARIANT_C1_PRIMITIVE_OPEN"
        and statuses.get("sm_phifin_alpha1", {}).get("status")
        == "MTT_SELECTED_PHIFIN_ALPHA1_PAYLOAD_ATTEMPT_BUILT_SELECTED_SPECTRAL_VALUES_OPEN"
        and statuses.get("sm_correction_emission", {}).get("status")
        == "MTT_SELECTED_ROUTEC_CORRECTION_SOURCE_EMISSION_AUDITED_DIAGNOSTIC_SPLITTER_NOT_SOURCE_EMITTED_VALUES_OPEN"
        and statuses.get("sm_deltatheta_solve_gate", {}).get("status")
        == "MTT_SELECTED_ROUTEC_DELTATHETA_C1_SOLVE_GATE_BUILT_SELECTED_HESSIAN_RESPONSE_OPERATOR_OPEN"
        and statuses.get("sm_c1_response_operator_emission", {}).get("status")
        == "MTT_SELECTED_ROUTEC_C1_RESPONSE_OPERATOR_EMISSION_AUDITED_A_SELECTED_NOT_EMITTED"
        and statuses.get("sm_c1_operator_source_or_galerkin_rebuild", {}).get("status")
        == "MTT_SELECTED_ROUTEC_C1_OPERATOR_SOURCE_GALERKIN_REBUILD_ITERATED_BASIS_TRANSPORT_LANE_SELECTED_AS_NEXT_PROOF_TARGET"
        and statuses.get("sm_noninvariant_c1_primitive_search", {}).get("status")
        == "MTT_SELECTED_ROUTEC_NONINVARIANT_C1_PRIMITIVE_SEARCH_BUILT_UNSELECTED_CANDIDATES_OPEN"
        and statuses.get("gr_remaining_gates", {}).get("status")
        == "CROSS_REPO_REMAINING_GATES_TRIAGED_BEST_NEXT_GATE_SELECTED_MATTER_PAYLOAD"
        and statuses.get("gr_routec_payload_value_import_attempt", {}).get("status")
        == "SELECTED_ROUTEC_PAYLOAD_VALUE_IMPORT_ATTEMPT_BLOCKED_SOURCE_VALUES_OPEN"
        and statuses.get("gr_routec_source_origin_conditional_lemma", {}).get("status")
        == "ROUTEC_SOURCE_ORIGIN_CONDITIONAL_LEMMA_PROVED_PAPER_INSERTION_BUILT_PHI_FIN_OPEN"
    )

    gates = [
        Gate("script exits 0", "PASS" if proc.returncode == 0 else "FAIL", proc.stdout[:1200]),
        Gate("certificate exists", "PASS" if CERT.exists() else "FAIL", CERT),
        Gate("candidate exists", "PASS" if CANDIDATE.exists() else "FAIL", CANDIDATE),
        Gate("gate table exists", "PASS" if TABLE.exists() else "FAIL", TABLE),
        Gate("paper exists", "PASS" if PAPER.exists() else "FAIL", PAPER),
        Gate(
            "status expected",
            "PASS" if cert.get("status") == expected_status else "FAIL",
            cert.get("status"),
        ),
        Gate("candidate mirrors cert", "PASS" if candidate == cert else "FAIL", candidate.get("status")),
        Gate("table mirrors embedded", "PASS" if table == closure_table else "FAIL", table),
        Gate(
            "repos checked",
            "PASS"
            if set(repos) == {"q79", "constants", "gr", "qa_su3", "sm_parity"}
            and all(row.get("present") is True for row in repos.values())
            else "FAIL",
            repos,
        ),
        Gate("finite shape passes", "PASS" if shape and all(shape.values()) else "FAIL", shape),
        Gate(
            "alpha1 support passes",
            "PASS" if alpha_support and all(alpha_support.values()) else "FAIL",
            alpha_support,
        ),
        Gate(
            "selected values still absent",
            "OPEN" if alpha_missing and all(alpha_missing.values()) else "FAIL",
            alpha_missing,
        ),
        Gate(
            "selected flags refuse promotion",
            "OPEN" if selected_flags_refuse_promotion else "FAIL",
            selected_flags,
        ),
        Gate(
            "closure test negative",
            "OPEN"
            if closure.get("finite_shape_pass") is True
            and closure.get("alpha1_support_pass") is True
            and closure.get("selected_payload_flags_all_true") is False
            and closure.get("selected_payload_flags_have_open_false") is True
            and closure.get("alpha1_selected_values_still_missing") is True
            and closure.get("adjacent_selected_q79_payload_values_emitted") is False
            and closure.get("can_close_selected_phifin_alpha1_payload_now") is False
            and closure.get("target_fitting_used") is False
            and closure.get("benchmark_entries_used") is False
            else "FAIL",
            closure,
        ),
        Gate(
            "adjacent statuses expected",
            "PASS" if adjacent_statuses_expected else "FAIL",
            statuses,
        ),
        Gate(
            "adjacent implications sharp",
            "PASS"
            if adjacent.get("qa_chi_closed_but_not_q79_payload") is True
            and adjacent.get("qa_electroweak_interface_open_not_payload_source") is True
            and adjacent.get("qa_u1_su2_same_scheme_payloads_and_k_gauge_open") is True
            and adjacent.get("qa_u1_su2_source_fill_partial_only") is True
            and adjacent.get("higher_order_flavor_splitting_criterion_closed") is True
            and adjacent.get("diagnostic_splitter_not_selected_source_emission") is True
            and adjacent.get("correction_gate_reduced_to_nonidentity_rhoe_bn_prefix") is True
            and adjacent.get("nonidentity_rhoe_bn_prefix_built_but_selected_open") is True
            and adjacent.get("canonical_c1_zero_response_no_go_imported") is True
            and adjacent.get("deltatheta_solve_gate_built_selected_operator_open") is True
            and adjacent.get("c1_response_operator_A_selected_not_emitted") is True
            and adjacent.get("c1_operator_rebuild_attempt_selected_blocks_still_open") is True
            and adjacent.get("noninvariant_c1_candidates_built_but_unselected") is True
            and adjacent.get("basis_transport_lane_selected_as_next_proof_target") is True
            and adjacent.get("sm_phifin_payload_values_still_open") is True
            and adjacent.get("gr_triage_keeps_selected_matter_payload_open") is True
            and adjacent.get("gr_direct_routec_payload_value_import_attempt_blocked") is True
            and adjacent.get("gr_source_origin_conditional_lemma_proved_phi_fin_open") is True
            and adjacent.get("adjacent_repos_emit_selected_q79_payload_values") is False
            else "FAIL",
            adjacent,
        ),
        Gate(
            "closed decision gate",
            "PASS"
            if closed.get("latest_repo_updates_checked") is True
            and closed.get("finite_phifin_alpha1_codomain_confirmed") is True
            and closed.get("alpha1_support_and_rank_contract_confirmed") is True
            and closed.get("diagnostic_vs_selected_emission_separated") is True
            and closed.get("nonidentity_rhoe_bn_prefix_imported_as_unselected_prefix") is True
            and closed.get("canonical_c1_zero_response_no_go_imported") is True
            and closed.get("selected_c1_operator_emission_blocker_identified") is True
            and closed.get("gr_direct_payload_value_import_attempt_checked") is True
            and closed.get("conditional_source_origin_lemma_imported_phi_fin_open") is True
            and closed.get("basis_transport_lane_selected_as_next_target") is True
            and closed.get("straight_payload_promotion_rejected") is True
            and closed.get("next_missing_object_identified") is True
            and closed.get("target_fitting_excluded") is True
            else "FAIL",
            closed,
        ),
        Gate(
            "remaining blockers guarded",
            "OPEN"
            if still_open.get("selected_PhiFin_alpha1_payload_values") is True
            and still_open.get("selected_correction_matrix_source") is True
            and still_open.get("selected_galerkin_values") is True
            and still_open.get("selected_deltaTheta_C1_solution") is True
            and still_open.get("primitive_C1_contractions") is True
            and still_open.get("selected_noninvariant_C1_primitive_or_basis_transport") is True
            and still_open.get("prove_selected_basis_transport_or_vertex_source_theorem") is True
            and still_open.get("emit_selected_A_selected_and_b_selected") is True
            and still_open.get("full_SM_or_no_knob_closure") is True
            else "FAIL",
            still_open,
        ),
        Gate(
            "guardrails",
            "PASS" if guardrails and all(value is False for value in guardrails.values()) else "FAIL",
            guardrails,
        ),
        Gate(
            "theorem is negative closure",
            "PASS"
            if cert.get("theorem", {}).get("proved") is True
            and cert.get("theorem", {}).get("closure_claimed") is False
            and cert.get("closure_claimed") is False
            and cert.get("target_fitting_used") is False
            and cert.get("next_required_artifact")
            == "Q79_Selected_RouteC_BasisTransport_Primitive_Source_Theorem_v1"
            else "FAIL",
            cert.get("theorem"),
        ),
        Gate(
            "paper records closure gate",
            "PASS"
            if contains_all(
                paper,
                [
                    "Q79 Selected PhiFin Alpha1 Payload",
                    "The payload is **not** closed",
                    "diagnostic splitters",
                    "finite prefixes",
                    "GR payload-value import attempt",
                    "basis-transport",
                    "A_selected",
                    "non-invariant basis transport",
                    "source-emitted values",
                    "Closure Test",
                    "Selected Payload Flags",
                    "Q79_Selected_RouteC_BasisTransport_Primitive_Source_Theorem_v1",
                ],
            )
            else "FAIL",
            PAPER,
        ),
    ]

    print("Q79 selected Phi_fin alpha1 payload closure gate audit")
    print("=====================================================")
    width = max(len(gate.label) for gate in gates)
    status_width = max(len(gate.status) for gate in gates)
    failures: list[Gate] = []
    for gate in gates:
        print(f"{gate.label:<{width}}  {gate.status:<{status_width}}")
        if gate.status == "FAIL":
            failures.append(gate)

    if failures:
        print("\nFailures")
        print("--------")
        for failure in failures:
            print(f"- {failure.label}: {failure.detail}")
        return 1

    print("\nResult: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
