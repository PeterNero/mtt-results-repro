"""Attempt the selected Route-C C1 operator-source/Galerkin rebuild.

The goal is to decide whether current local and adjacent artifacts can emit the
finite selected operator

    A_selected deltaTheta_C1 = b_selected

needed before a DeltaTheta solve or flavor test is honest.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
CERTS = ROOT / "certificates"
SM = TEXPAPERS / "mtt-sm-parity-closure"
Q79 = TEXPAPERS / "mtt-q79-proof-repro"

PREVIOUS = CERTS / "selected_c1_response_operator_emission_audit_import_certificate.json"
FIBER = CERTS / "noninvariant_c1_fiberclass_reduction_certificate.json"
PREFIX = CERTS / "routec_rhoe_bn_operator_prefix_import_certificate.json"

Q79_PHIFIN = Q79 / "certificates" / "q79_selected_phifin_alpha1_payload_certificate.json"
Q79_C1_TEMPLATE = Q79 / "certificates" / "selected_c1_response_data_certificate.template.json"
Q79_C1_ATTEMPT = Q79 / "certificates" / "selected_c1_response_extraction_attempt_certificate.json"
SM_OPERATOR = SM / "certificates" / "selected_routec_selected_c1_response_operator_emission_certificate.json"
SM_OPERATOR_CANDIDATE = SM / "candidate_data" / "selected_routec_selected_c1_response_operator_emission.candidate.json"
SM_PHIFIN = SM / "certificates" / "selected_phifin_alpha1_payload_certificate.json"
SM_SOURCE_ALPHA1 = SM / "certificates" / "selected_source_origin_and_alpha1_driver_certificate.json"
SM_NONINV = SM / "certificates" / "selected_routec_noninvariant_c1_primitive_search_certificate.json"
SM_FIBER = SM / "certificates" / "selected_routec_primitive_source_selection_audit_certificate.json"

OUTPUT = CERTS / "selected_c1_operator_source_rebuild_attempt_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def status(path: Path) -> str | None:
    return load(path).get("status")


def selected_true(value: Any) -> bool:
    return value is True


def main() -> None:
    previous = load(PREVIOUS)
    fiber = load(FIBER)
    prefix = load(PREFIX)
    q79_phifin = load(Q79_PHIFIN)
    q79_template = load(Q79_C1_TEMPLATE)
    q79_attempt = load(Q79_C1_ATTEMPT)
    sm_operator = load(SM_OPERATOR)
    sm_operator_candidate = load(SM_OPERATOR_CANDIDATE)
    sm_phifin = load(SM_PHIFIN)
    sm_source_alpha1 = load(SM_SOURCE_ALPHA1)
    sm_noninv = load(SM_NONINV)
    sm_fiber = load(SM_FIBER)

    q79_gate = q79_phifin.get("closure_gate_table", {})
    q79_selected_flags = q79_gate.get("selected_payload_flags", {})
    q79_alpha_missing = q79_gate.get("alpha1_missing_selected_values", {})
    q79_alpha_support = q79_gate.get("alpha1_support_gates", {})

    q79_template_operator = q79_template.get("operator_data", {})
    q79_response_matrices = q79_template.get("response_matrices", {})
    sm_audit = sm_operator_candidate.get("emission_audit", {})

    required_slots = {
        "selected_source_certificate": {
            "present": bool(sm_source_alpha1),
            "selected": all(
                selected_true(v) for v in q79_selected_flags.values()
            ),
            "best_source": str(Q79_PHIFIN),
            "current_detail": q79_selected_flags,
        },
        "selected_nonidentity_rhoE_or_connection": {
            "present": prefix.get("closed_now", {}).get("nonidentity_projective_rhoE_candidate_built") is True,
            "selected": q79_selected_flags.get("rhoE_selected_by_mtt") is True
            and q79_selected_flags.get("rhoE_nonidentity") is True,
            "best_source": str(PREFIX),
            "current_detail": {
                "prefix_candidate_built": prefix.get("closed_now", {}).get(
                    "nonidentity_projective_rhoE_candidate_built"
                ),
                "q79_rhoE_selected_by_mtt": q79_selected_flags.get("rhoE_selected_by_mtt"),
                "q79_rhoE_nonidentity": q79_selected_flags.get("rhoE_nonidentity"),
            },
        },
        "selected_DE_Riesz_Green_dotD": {
            "present": prefix.get("closed_now", {}).get("D_E_matrix_on_27_mode_BN_emitted") is True
            and prefix.get("closed_now", {}).get("sector_projectors_and_dotD_same_basis_emitted") is True,
            "selected": q79_selected_flags.get("de_action_selected_source") is True
            and q79_selected_flags.get("riesz_gap_selected_source") is True
            and q79_selected_flags.get("reduced_green_selected_source") is True
            and q79_selected_flags.get("dotd_selected_source") is True,
            "best_source": str(PREFIX),
            "current_detail": {
                key: q79_selected_flags.get(key)
                for key in (
                    "de_action_selected_source",
                    "riesz_gap_selected_source",
                    "reduced_green_selected_source",
                    "dotd_selected_source",
                )
            },
        },
        "selected_alpha1_driver": {
            "present": all(selected_true(v) for v in q79_alpha_support.values()),
            "selected": q79_selected_flags.get("dotd_alpha1_driver") is True,
            "best_source": str(Q79_PHIFIN),
            "current_detail": {
                "support": q79_alpha_support,
                "dotd_alpha1_driver_flag": q79_selected_flags.get("dotd_alpha1_driver"),
            },
        },
        "selected_Hess_Xi_finite_blocks": {
            "present": bool(q79_template_operator.get("Hess_Xi_blocks", {}).get("principal_symbol_blocks")),
            "selected": q79_alpha_missing.get("full_lower_order_Hess_Xi_blocks") is False,
            "best_source": str(Q79_C1_TEMPLATE),
            "current_detail": {
                "principal_symbol_blocks_present": bool(
                    q79_template_operator.get("Hess_Xi_blocks", {}).get("principal_symbol_blocks")
                ),
                "full_lower_order_Hess_Xi_blocks_missing": q79_alpha_missing.get(
                    "full_lower_order_Hess_Xi_blocks"
                ),
            },
        },
        "selected_source_vector_b_selected": {
            "present": bool(q79_template.get("selected_driver_row")),
            "selected": q79_alpha_missing.get("evaluated_grad_V_C1_alpha1_source_vector") is False,
            "best_source": str(Q79_C1_TEMPLATE),
            "current_detail": {
                "driver_row_present": bool(q79_template.get("selected_driver_row")),
                "evaluated_source_vector_missing": q79_alpha_missing.get(
                    "evaluated_grad_V_C1_alpha1_source_vector"
                ),
            },
        },
        "selected_zero_mode_bases_and_gram_schmidt": {
            "present": any(
                q79_template.get("zero_modes", {}).get(key) is not None
                for key in ("Q_basis", "u_basis", "d_basis", "L_basis", "e_basis", "N_basis", "H_basis")
            ),
            "selected": q79_alpha_missing.get("sector_zero_mode_bases") is False,
            "best_source": str(Q79_C1_TEMPLATE),
            "current_detail": {
                "sector_zero_mode_bases_missing": q79_alpha_missing.get("sector_zero_mode_bases"),
                "gram_schmidt_rule": q79_template.get("zero_modes", {}).get(
                    "L2_normalization_and_Gram_Schmidt_rule"
                ),
            },
        },
        "selected_primitive_C1_contractions": {
            "present": sm_noninv.get("what_closes", {}).get("finite_noninvariant_C1_candidate_matrices_emitted")
            is True,
            "selected": fiber.get("meaning", {}).get("selected_noninvariant_primitive_source_proved") is True,
            "best_source": str(FIBER),
            "current_detail": {
                "noninvariant_candidates_exist": sm_noninv.get("what_closes", {}).get(
                    "finite_noninvariant_C1_candidate_matrices_emitted"
                ),
                "selected_noninvariant_primitive_source_proved": fiber.get("meaning", {}).get(
                    "selected_noninvariant_primitive_source_proved"
                ),
                "active_shift_forced": fiber.get("closed_now", {}).get(
                    "active_shift_1_1_forced_by_finite_support"
                ),
            },
        },
        "selected_sector_response_matrices": {
            "present": any(value is not None for value in q79_response_matrices.values()),
            "selected": q79_alpha_missing.get("response_matrices_and_tests") is False
            and sm_audit.get("selected_operator_A_selected_emitted") is True,
            "best_source": str(Q79_C1_TEMPLATE),
            "current_detail": {
                "template_response_matrices_null": {
                    key: value is None for key, value in q79_response_matrices.items()
                },
                "response_matrices_and_tests_missing": q79_alpha_missing.get(
                    "response_matrices_and_tests"
                ),
                "A_selected_emitted": sm_audit.get("selected_operator_A_selected_emitted"),
            },
        },
    }

    present_slots = {key: value["present"] for key, value in required_slots.items()}
    selected_slots = {key: value["selected"] for key, value in required_slots.items()}
    all_present = all(present_slots.values())
    all_selected = all(selected_slots.values())

    illegal_or_diagnostic_sources = {
        "diagnostic_noninvariant_C1_candidates": sm_noninv.get("what_closes", {}).get(
            "finite_noninvariant_C1_candidate_matrices_emitted"
        )
        is True
        and fiber.get("meaning", {}).get("selected_noninvariant_primitive_source_proved") is False,
        "model_active_BN_DE_dotD_prefix": prefix.get("closed_now", {}).get(
            "D_E_matrix_on_27_mode_BN_emitted"
        )
        is True
        and required_slots["selected_DE_Riesz_Green_dotD"]["selected"] is False,
        "q79_template_principal_symbol_only": bool(
            q79_template_operator.get("Hess_Xi_blocks", {}).get("principal_symbol_blocks")
        )
        and required_slots["selected_Hess_Xi_finite_blocks"]["selected"] is False,
        "identity_or_unselected_rhoE_payload": required_slots[
            "selected_nonidentity_rhoE_or_connection"
        ]["selected"]
        is False,
    }

    closure_possible = all_present and all_selected
    output = {
        "certificate": "SelectedC1OperatorSourceRebuildAttempt",
        "status": "SELECTED_C1_OPERATOR_REBUILD_ATTEMPT_EXECUTED_SELECTED_BLOCKS_STILL_OPEN",
        "inputs": {
            "previous_emission_audit": str(PREVIOUS.relative_to(ROOT)),
            "fiber_reduction": str(FIBER.relative_to(ROOT)),
            "routec_operator_prefix": str(PREFIX.relative_to(ROOT)),
            "q79_phifin_alpha1_payload": str(Q79_PHIFIN),
            "q79_c1_response_template": str(Q79_C1_TEMPLATE),
            "q79_c1_response_attempt": str(Q79_C1_ATTEMPT),
            "sm_operator_emission": str(SM_OPERATOR),
            "sm_phifin_alpha1": str(SM_PHIFIN),
            "sm_source_alpha1": str(SM_SOURCE_ALPHA1),
            "sm_noninvariant_c1": str(SM_NONINV),
            "sm_fiber_audit": str(SM_FIBER),
        },
        "plan_executed": [
            "enumerated every slot required for A_selected and b_selected",
            "classified each slot by present finite support versus selected-source legality",
            "rejected diagnostic/nonselected candidates as proof sources",
            "built the minimal rebuild payload contract for the next selected solve attempt",
        ],
        "slot_audit": required_slots,
        "slot_summary": {
            "present_slots": present_slots,
            "selected_slots": selected_slots,
            "all_required_slots_present": all_present,
            "all_required_slots_selected": all_selected,
            "closure_possible_from_current_artifacts": closure_possible,
        },
        "illegal_or_diagnostic_sources_rejected": illegal_or_diagnostic_sources,
        "candidate_A_selected": None,
        "candidate_b_selected": None,
        "why_no_A_or_b": (
            "Current artifacts contain support schemas, principal symbols, diagnostic finite matrices, "
            "and model active operators, but they do not contain a complete selected-source set of finite "
            "Hess_Xi blocks, evaluated b_selected, selected dotD, zero-mode bases, primitive contractions, "
            "and sector response matrices."
        ),
        "minimal_rebuild_payload": {
            "file": "certificates/selected_routec_c1_operator_source_rebuild.payload.template.json",
            "required_true_flags": [
                "selected_source_certificate.selected_by_mtt",
                "rhoE_or_connection.selected_nonidentity_payload",
                "DE_Riesz_Green_dotD.selected_source_verified",
                "alpha1.same_branch_driver_verified",
                "Hess_Xi.finite_blocks_emitted",
                "source_vector.b_selected_emitted",
                "zero_modes.selected_bases_emitted",
                "primitive_C1.selected_contractions_emitted",
                "sector_response_matrices.emitted",
            ],
            "validators": [
                "rank(A_selected)",
                "least_squares_or_exact_consistency(A_selected, b_selected)",
                "mass_split_traceless_norm_sq",
                "CKM_PMNS_commutator_norm_sq",
                "CP_odd_invariant",
            ],
        },
        "what_closes_now": {
            "rebuild_search_executed": True,
            "all_candidate_block_sources_classified": True,
            "diagnostic_sources_rejected_as_A_selected": True,
            "minimal_rebuild_payload_specified": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "emit_selected_A_selected": True,
            "emit_selected_b_selected": True,
            "selected_source_certificate": not required_slots["selected_source_certificate"]["selected"],
            "selected_nonidentity_rhoE_or_connection": not required_slots[
                "selected_nonidentity_rhoE_or_connection"
            ]["selected"],
            "selected_DE_Riesz_Green_dotD": not required_slots["selected_DE_Riesz_Green_dotD"][
                "selected"
            ],
            "selected_alpha1_driver": not required_slots["selected_alpha1_driver"]["selected"],
            "selected_Hess_Xi_finite_blocks": not required_slots[
                "selected_Hess_Xi_finite_blocks"
            ]["selected"],
            "selected_source_vector_b_selected": not required_slots[
                "selected_source_vector_b_selected"
            ]["selected"],
            "selected_zero_mode_bases_and_gram_schmidt": not required_slots[
                "selected_zero_mode_bases_and_gram_schmidt"
            ]["selected"],
            "selected_primitive_C1_contractions": not required_slots[
                "selected_primitive_C1_contractions"
            ]["selected"],
            "selected_sector_response_matrices": not required_slots[
                "selected_sector_response_matrices"
            ]["selected"],
            "full_SM_closure": True,
        },
        "next_required_artifact": "Selected_RouteC_C1_Operator_Source_Rebuild_Payload_v1",
        "guardrails": {
            "claims_A_selected_emitted": False,
            "claims_b_selected_emitted": False,
            "claims_deltaTheta_C1_solved": False,
            "claims_flavor_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "honest_answer": (
            "The rebuild attempt was executed and fails honestly: no current artifact can legally emit "
            "A_selected or b_selected. The shortest forward path is now a payload fill, not another "
            "diagnostic search: emit selected finite Hess_Xi blocks, selected b_selected, selected dotD, "
            "zero-mode bases, selected primitive C1 contractions, and sector response matrices in one "
            "source-verified packet."
        ),
        "source_statuses": {
            "previous": previous.get("status"),
            "q79_phifin": q79_phifin.get("status"),
            "q79_attempt": q79_attempt.get("status"),
            "sm_operator": sm_operator.get("status"),
            "sm_phifin": sm_phifin.get("status"),
            "sm_source_alpha1": sm_source_alpha1.get("status"),
            "sm_noninv": sm_noninv.get("status"),
            "sm_fiber": sm_fiber.get("status"),
        },
    }

    if "--write-certificate" in sys.argv:
        OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
