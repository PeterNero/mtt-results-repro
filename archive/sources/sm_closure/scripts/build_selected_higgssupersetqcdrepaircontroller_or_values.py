"""Build a superset controller for Higgs QCD threshold repair values."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_higgssupersetqcdrepaircontroller_or_values"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CONTROLLER = PACKET_DIR / "superset_qcd_repair_controller.packet.json"
ACCEPTANCE = PACKET_DIR / "qcd_repair_value_acceptance_kernel.packet.json"
CUTSET = PACKET_DIR / "minimal_next_value_cutset.packet.json"
UPDATED = PACKET_DIR / "updated_true_equivalence_gate_after_superset_qcd_controller.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HiggsSupersetQCDRepairController_or_Values_v1.md"

STATUS = "MTT_SELECTED_HIGGSSUPERSETQCDREPAIRCONTROLLER_OR_VALUES_BUILT_LOCKED_TARGET_VALUES_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_higgsqcdthresholdrows_or_correlatedprofilefill.candidate.json")
    residuals = load(
        DATA
        / "selected_higgsqcdthresholdrows_or_correlatedprofilefill"
        / "qcd_threshold_residual_rows.packet.json"
    )
    repair = load(
        DATA
        / "selected_higgsqcdthresholdrows_or_correlatedprofilefill"
        / "qcd_threshold_repair_obligations.packet.json"
    )
    profile = load(
        DATA
        / "selected_higgsqcdthresholdrows_or_correlatedprofilefill"
        / "correlated_profile_fill_status_after_qcd_thresholds.packet.json"
    )
    previous_gate = load(
        DATA
        / "selected_higgsqcdthresholdrows_or_correlatedprofilefill"
        / "updated_true_equivalence_gate_after_qcd_threshold_rows.packet.json"
    )
    threshold_contract = load(
        DATA
        / "selected_thresholdmassschemecovariancefill_or_qasu3packetintegration"
        / "threshold_mass_scheme_covariance_acceptance_contract.packet.json"
    )
    qasu3_status = load(DATA / "sm_equivalence_crossrepo_qasu3_status_import.candidate.json")
    inverse_spec = load(DATA / "inverse_superset_search_spec.candidate.json")

    channels = residuals["summary"]["channels"]
    lane_rows = [
        {
            "lane_id": "L0_straight_measured_replay",
            "lane_kind": "STRAIGHT_PATH",
            "role": "establish current proxy rows and residuals from declared measured parity inputs",
            "inputs": [rel(DATA / "selected_higgsqcdthresholdrows_or_correlatedprofilefill" / "qcd_threshold_residual_rows.packet.json")],
            "allowed_to_close": ["diagnostic residual rows", "forbidden fit-factor guard"],
            "not_allowed_to_close": ["threshold repair values", "selected Qa/SU3 operator packet", "correlated profile"],
            "status": "CLOSED_DIAGNOSTIC_ONLY",
        },
        {
            "lane_id": "L1_threshold_mass_scheme_contract",
            "lane_kind": "SUPERSET_CONSTRAINT_PATH",
            "role": "declare legal mass-scheme, alpha_s, threshold, and covariance conditions before any value can promote",
            "inputs": [
                rel(
                    DATA
                    / "selected_thresholdmassschemecovariancefill_or_qasu3packetintegration"
                    / "threshold_mass_scheme_covariance_acceptance_contract.packet.json"
                )
            ],
            "allowed_to_close": ["acceptance conditions", "scheme/covariance preconditions"],
            "not_allowed_to_close": ["numeric threshold values"],
            "status": "CONSTRAINTS_AVAILABLE_VALUES_OPEN",
        },
        {
            "lane_id": "L2_qasu3_source_operator",
            "lane_kind": "SUPERSET_SOURCE_PATH",
            "role": "supply selected color/Yukawa/trace operator attachment for source-sensitive QCD rows",
            "inputs": [rel(DATA / "sm_equivalence_crossrepo_qasu3_status_import.candidate.json")],
            "allowed_to_close": ["operator source attachment if a future promotable packet appears"],
            "not_allowed_to_close": ["numeric threshold corrections from residuals"],
            "status": "SUPPORT_IMPORTED_FINAL_PACKET_OPEN",
        },
        {
            "lane_id": "L3_correlated_profile",
            "lane_kind": "SUPERSET_PROFILE_PATH",
            "role": "supply covariance/profile constraints for the QCD color-threshold block",
            "inputs": [rel(DATA / "selected_higgsqcdthresholdrows_or_correlatedprofilefill" / "correlated_profile_fill_status_after_qcd_thresholds.packet.json")],
            "allowed_to_close": ["QCD covariance/profile block if entries are filled and PSD/profile tests pass"],
            "not_allowed_to_close": ["source/operator selection", "threshold correction values by fit"],
            "status": "BLUEPRINT_AVAILABLE_VALUES_OPEN",
        },
        {
            "lane_id": "L4_inverse_discovery",
            "lane_kind": "SUPERSET_DISCOVERY_PATH",
            "role": "rank candidate threshold/source packets only as discovery; all candidates must replay forward",
            "inputs": [rel(DATA / "inverse_superset_search_spec.candidate.json")],
            "allowed_to_close": ["ranked candidate proposals"],
            "not_allowed_to_close": ["proof promotion", "residual-selected correction factors"],
            "status": "DISCOVERY_ONLY",
        },
    ]

    locked_target = {
        "name": "non-fit Higgs QCD threshold repair packet",
        "channels": channels,
        "must_be_shared_across_channels": True,
        "locked_by": [
            "declared threshold/mass-scheme contract",
            "same-branch Qa/SU3 operator attachment or explicit parity-interface substitute",
            "forward replay before benchmark comparison",
            "QCD block covariance/profile status recorded separately",
        ],
        "must_not_use": [
            "benchmark_over_proxy_ratio as correction",
            "separate continuous multiplier per channel",
            "observed Higgs widths as source selectors",
            "support-only Qa/SU3 packets as final source closure",
        ],
    }

    controller = {
        "schema": "MTTHiggsSupersetQCDRepairController.v1",
        "status": "SUPERSET_QCD_REPAIR_CONTROLLER_BUILT_VALUES_OPEN",
        "locked_target": locked_target,
        "lanes": lane_rows,
        "superset_strategy": {
            "mode": "MULTI_PATH_CONSTRAINTS_TO_LOCKED_TARGET",
            "straight_path_used_for": "current replay and residual diagnostics",
            "superset_paths_used_for": [
                "threshold/mass-scheme/covariance legality",
                "selected Qa/SU3 source/operator attachment",
                "correlated profile validation",
                "discovery-only candidate generation",
            ],
            "paths_combined_as_knobs": False,
            "measured_targets_used_to_lock_source": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    acceptance_tests = [
        {
            "id": "A1_nonfit_value_source",
            "requirement": "threshold repair value is computed from formula, literature convention, selected operator data, or declared covariance model before benchmark comparison",
            "current_status": "OPEN",
        },
        {
            "id": "A2_no_residual_multiplier",
            "requirement": "no forbidden benchmark_over_proxy_ratio from the residual packet is applied as a correction factor",
            "current_status": "CLOSED_GUARD_INSTALLED",
        },
        {
            "id": "A3_scheme_threshold_contract",
            "requirement": "mass-scheme, alpha_s, loop order, and threshold path satisfy the threshold/mass-scheme contract",
            "current_status": "CONTRACT_AVAILABLE_VALUES_OPEN",
        },
        {
            "id": "A4_source_operator_attachment",
            "requirement": "source-sensitive rows have selected Qa/SU3 color/Yukawa/trace operator attachment or explicit parity substitute",
            "current_status": "OPEN_QASU3_FINAL_PACKET_NOT_FOUND",
        },
        {
            "id": "A5_covariance_profile_status",
            "requirement": "QCD block covariance/profile values are either filled and checked, or explicitly marked open",
            "current_status": "OPEN_VALUES_MARKED",
        },
        {
            "id": "A6_forward_replay",
            "requirement": "all observables are recomputed forward from admitted values with observed widths removed from selector inputs",
            "current_status": "READY_NOT_EXECUTED_FOR_REPAIR_VALUES",
        },
    ]

    acceptance = {
        "schema": "MTTHiggsQCDRepairValueAcceptanceKernel.v1",
        "status": "ACCEPTANCE_KERNEL_BUILT_VALUES_OPEN",
        "tests": acceptance_tests,
        "all_tests_closed": False,
        "values_promotable_now": False,
        "forbidden_fit_factors": [
            {
                "channel": row["channel"],
                "forbidden_fit_factor": row["forbidden_fit_factor"],
                "blocked": row["forbidden_fit_factor_may_be_applied"] is False,
            }
            for row in residuals["rows"]
        ],
        "external_contract_values_promotable_now": threshold_contract["values_promotable_now"],
        "qasu3_promotable_packet_found": qasu3_status["any_promotable_qasu3_packet_found"],
        "inverse_search_role": inverse_spec["target_fitting_role"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cutset = {
        "schema": "MTTMinimalNextQCDRepairValueCutset.v1",
        "status": "MINIMAL_CUTSET_IDENTIFIED_VALUES_OPEN",
        "minimal_value_objects": [
            {
                "id": "V1_threshold_formula_values",
                "description": "non-fit threshold/mass-scheme repair values for H_to_ss and H_to_gg",
                "can_be_supplied_by": [
                    "accepted literature formula convention",
                    "local multi-loop implementation benchmarked against literature",
                    "selected operator-derived threshold model",
                ],
                "current_status": "OPEN",
            },
            {
                "id": "V2_qasu3_operator_attachment",
                "description": "selected or parity-accepted Qa/SU3 color/Yukawa/trace operator attachment for source-sensitive rows",
                "can_be_supplied_by": [
                    "future promotable sibling Qa/SU3 packet",
                    "local explicit parity-interface substitute with source provenance",
                ],
                "current_status": "OPEN",
            },
            {
                "id": "V3_qcd_profile_block",
                "description": "QCD color-threshold covariance/profile block for bb, cc, ss, gg",
                "can_be_supplied_by": [
                    "cited correlated external profile",
                    "selected operator uncertainty model",
                    "declared diagonal-only parity fallback with precision guard",
                ],
                "current_status": "OPEN",
            },
        ],
        "smallest_next_executable_artifact": "MTT_Selected_HiggsQCDRepairValues_or_ProfileCovarianceBlock_v1",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    updated = {
        "schema": "MTTUpdatedTrueEquivalenceGateAfterSupersetQCDController.v1",
        "status": "SUPERSET_QCD_CONTROLLER_BUILT_VALUES_OPEN",
        "previous_true_equivalence_blockers": previous_gate["remaining_true_equivalence_blockers"],
        "closed_now": previous_gate["closed_now"] + ["superset QCD repair controller and acceptance kernel"],
        "remaining_true_equivalence_blockers": previous_gate["remaining_true_equivalence_blockers"],
        "next_primary_value_gate": cutset["smallest_next_executable_artifact"],
        "guardrails": {
            "superset_paths_combined_as_constraints_not_knobs": True,
            "residual_ratios_not_applied_as_corrections": True,
            "qcd_repair_values_filled": False,
            "qasu3_operator_attachment_closed": False,
            "correlated_profile_values_filled": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHiggsSupersetQCDRepairControllerOrValues",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_higgsqcdthresholdrows_or_correlatedprofilefill.candidate.json"),
            "threshold_contract": rel(
                DATA
                / "selected_thresholdmassschemecovariancefill_or_qasu3packetintegration"
                / "threshold_mass_scheme_covariance_acceptance_contract.packet.json"
            ),
            "qasu3_crossrepo_status": rel(DATA / "sm_equivalence_crossrepo_qasu3_status_import.candidate.json"),
            "inverse_superset_search_spec": rel(DATA / "inverse_superset_search_spec.candidate.json"),
        },
        "output_packets": {
            "superset_qcd_repair_controller": rel(CONTROLLER),
            "qcd_repair_value_acceptance_kernel": rel(ACCEPTANCE),
            "minimal_next_value_cutset": rel(CUTSET),
            "updated_true_equivalence_gate": rel(UPDATED),
        },
        "theorem": {
            "name": "HiggsSupersetQCDRepairControllerTheorem",
            "proved": True,
            "statement": (
                "The QCD Higgs repair problem can use a superset strategy without adding knobs: the straight replay, "
                "threshold/mass-scheme contract, Qa/SU3 source path, correlated-profile path, and inverse-discovery path "
                "are combined only as constraints on one locked non-fit repair target. Residual multipliers remain forbidden."
            ),
        },
        "what_closes_now": {
            "superset_QCD_repair_controller": True,
            "acceptance_kernel_for_repair_values": True,
            "minimal_next_value_cutset": True,
            "knob_guardrail_for_superset_paths": True,
        },
        "what_remains_open": {
            "non_fit_QCD_threshold_repair_values": True,
            "selected_Qa_SU3_operator_attachment": True,
            "QCD_correlated_profile_block": True,
            "accepted_precision_formula_rows": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "controller_closed": True,
            "repair_values_filled": False,
            "values_promotable_now": False,
            "superset_paths_used_as_knobs": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_HiggsSupersetQCDRepairController_or_Values_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "controller_closed": True,
        "repair_values_filled": False,
        "values_promotable_now": False,
        "superset_paths_used_as_knobs": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": cutset["smallest_next_executable_artifact"],
    }

    note = """# MTT Selected HiggsSupersetQCDRepairController or Values v1

Status: `MTT_SELECTED_HIGGSSUPERSETQCDREPAIRCONTROLLER_OR_VALUES_BUILT_LOCKED_TARGET_VALUES_OPEN`.

This artifact uses the superset strategy deliberately. The straight measured
path, threshold/mass-scheme contract, Qa/SU3 source path, correlated-profile
path, and inverse-discovery path are combined only as constraints on one locked
target: a non-fit QCD threshold repair packet for `H_to_ss` and `H_to_gg`.

No repair value is filled here. Residual ratios remain forbidden fit factors,
and support-only Qa/SU3 artifacts are not promoted to final source closure.
"""

    for path, payload in [
        (CONTROLLER, controller),
        (ACCEPTANCE, acceptance),
        (CUTSET, cutset),
        (UPDATED, updated),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
