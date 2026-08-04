"""Build Higgs precision-row promotion gate and full correlated-profile readiness."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_higgsprecisionrows_or_fullcorrelatedprofile"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROWS = PACKET_DIR / "higgs_precision_row_promotion_gate.packet.json"
PROFILE = PACKET_DIR / "full_correlated_profile_readiness_matrix.packet.json"
BLOCKERS = PACKET_DIR / "minimal_precision_closure_blocker_set.packet.json"
DECISION = PACKET_DIR / "precision_rows_or_full_profile_decision.packet.json"
UPDATED_TRUE = PACKET_DIR / "updated_true_equivalence_gate_after_precision_row_gate.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HiggsPrecisionRows_or_FullCorrelatedProfile_v1.md"

STATUS = "MTT_SELECTED_HIGGSPRECISIONROWS_OR_FULLCORRELATEDPROFILE_BUILT_PROMOTION_GATE_VALUES_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def row_requirements(channel: str, row_kind: str) -> dict[str, Any]:
    if channel in {"H_to_bb", "H_to_cc"}:
        return {
            "precision_route": "multiloop running-mass H->qq formula row with scheme/covariance lock",
            "missing_inputs": [
                "accepted multi-loop quark-mass running and threshold matching",
                "QCD/EW/mixed correction order declared at mH",
                "mass and alpha_s covariance propagated into full profile",
            ],
            "operator_source_requirement": "SM-parity Higgs/Yukawa row accepted; no-knob selected source still open",
        }
    if channel in {"H_to_tau_tau", "H_to_mu_mu"}:
        return {
            "precision_route": "leptonic H->ff formula row with electroweak/radiative correction policy",
            "missing_inputs": [
                "accepted electroweak/radiative correction convention",
                "lepton mass scheme and uncertainty propagation",
                "cross-channel Higgs-mass/electroweak covariance",
            ],
            "operator_source_requirement": "SM-parity Higgs/Yukawa row accepted; no-knob selected source still open",
        }
    if channel in {"H_to_ss"}:
        return {
            "precision_route": "precision strange running-mass H->ss threshold formula row",
            "missing_inputs": [
                "multi-loop m_s(2 GeV)->mH running with threshold matching",
                "MSbar strange-mass and alpha_s covariance",
                "QCD/EW/mixed corrections beyond first-pass formula scaffold",
            ],
            "operator_source_requirement": "Qa/SU3 color/Yukawa operator source required for no-knob precision",
        }
    if channel in {"H_to_gg"}:
        return {
            "precision_route": "mass-dependent H->gg loop row with higher-order QCD threshold policy",
            "missing_inputs": [
                "finite top/bottom/charm loop functions and interference",
                "NNLO/N3LO QCD K-factors and threshold matching",
                "alpha_s and heavy-quark mass covariance",
            ],
            "operator_source_requirement": "Qa/SU3 color trace/operator source required for no-knob precision",
        }
    if channel == "H_to_gamma_gamma":
        return {
            "precision_route": "full loop H->gamma gamma formula row with electroweak/QCD correction policy",
            "missing_inputs": [
                "accepted higher-order electroweak and QCD correction convention",
                "mass/coupling covariance for charged loop species",
                "full profile coupling to EW and Higgs-mass uncertainties",
            ],
            "operator_source_requirement": "electroweak charge/operator source required for no-knob precision",
        }
    if channel in {"H_to_WW_star", "H_to_ZZ_star"}:
        return {
            "precision_route": "off-shell four-fermion H->VV* formula kernel or accepted precision import",
            "missing_inputs": [
                "executable off-shell electroweak formula kernel with uncertainty propagation",
                "or accepted external precision import with source/version/profile semantics",
                "cross-channel electroweak input covariance",
            ],
            "operator_source_requirement": "electroweak gauge/Higgs operator source required for no-knob precision",
        }
    if channel == "H_to_Z_gamma":
        return {
            "precision_route": "loop-induced H->Z gamma formula kernel or accepted precision import",
            "missing_inputs": [
                "executable mixed neutral-current loop kernel with EW corrections",
                "or accepted external precision import with source/version/profile semantics",
                "cross-channel electroweak input covariance",
            ],
            "operator_source_requirement": "mixed electroweak neutral-current operator source required for no-knob precision",
        }
    raise ValueError(f"unknown channel {channel}")


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_higgstenchannelcovarianceprofile_or_branchingreplay.candidate.json")
    total = load(
        DATA
        / "selected_higgstenchannelcovarianceprofile_or_branchingreplay"
        / "ten_channel_total_width_diagonal_profile.packet.json"
    )
    branching = load(
        DATA
        / "selected_higgstenchannelcovarianceprofile_or_branchingreplay"
        / "ten_channel_branching_ratio_replay.packet.json"
    )
    qcd_stress = load(
        DATA
        / "selected_higgsqcdprecisionthresholdrows_or_correlatedprofileupgrade"
        / "higgs_qcd_correlation_stress_profile.packet.json"
    )
    ew_stress = load(
        DATA
        / "selected_higgsewformulakernelexecution_or_precisionimportrows"
        / "ew_three_channel_correlation_stress_profile.packet.json"
    )
    previous_true = load(
        DATA
        / "selected_higgstenchannelcovarianceprofile_or_branchingreplay"
        / "updated_true_equivalence_gate_after_ten_channel_branching.packet.json"
    )

    br_by_channel = {row["channel"]: row for row in branching["rows"]}
    precision_rows = []
    for row in total["rows"]:
        requirements = row_requirements(row["channel"], row["row_kind"])
        precision_rows.append(
            {
                "channel": row["channel"],
                "current_row_kind": row["row_kind"],
                "current_width_GeV": row["width_GeV"],
                "current_branching_ratio": br_by_channel[row["channel"]]["branching_ratio"],
                "precision_route": requirements["precision_route"],
                "missing_inputs": requirements["missing_inputs"],
                "operator_source_requirement": requirements["operator_source_requirement"],
                "accepted_as_precision_formula_or_import_row": False,
                "accepted_in_full_correlated_profile": False,
                "may_be_used_for_scaffold_replay": True,
                "observed_data_used_as_selector": False,
                "target_fitting_used": False,
            }
        )

    row_gate = {
        "schema": "MTTHiggsPrecisionRowPromotionGate.v1",
        "status": "HIGGS_PRECISION_ROW_PROMOTION_GATE_BUILT_ZERO_ROWS_PROMOTED",
        "rows": precision_rows,
        "summary": {
            "row_count": len(precision_rows),
            "accepted_precision_row_count": 0,
            "proxy_row_count": sum(row["current_row_kind"] == "computed_proxy" for row in precision_rows),
            "external_import_identity_row_count": sum(
                row["current_row_kind"] == "external_benchmark_fill" for row in precision_rows
            ),
            "all_rows_have_precision_route": True,
            "all_rows_have_operator_source_requirement": True,
            "scaffold_replay_rows_available": len(precision_rows),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    profile_blocks = [
        {
            "block": "diagonal_sidecar_10x10",
            "channels": total["row_basis"],
            "status": "AVAILABLE_AS_DIAGONAL_FALLBACK",
            "accepted_as_full_correlated_profile": False,
        },
        {
            "block": "QCD_color_threshold",
            "channels": qcd_stress["channels"],
            "status": "STRESS_PROFILE_AVAILABLE_FULL_EMPIRICAL_PROFILE_OPEN",
            "accepted_as_full_correlated_profile": qcd_stress["summary"]["accepted_as_full_correlated_profile"],
        },
        {
            "block": "EW_offshell_loop",
            "channels": ew_stress["channels"],
            "status": "STRESS_PROFILE_AVAILABLE_IMPORT_IDENTITY_FULL_EMPIRICAL_PROFILE_OPEN",
            "accepted_as_full_correlated_profile": ew_stress["summary"]["accepted_as_full_correlated_profile"],
        },
        {
            "block": "cross_block_shared_inputs",
            "channels": total["row_basis"],
            "status": "OPEN_SHARED_MH_ALPHA_S_EW_MASS_SCHEME_CORRELATIONS_NOT_FILLED",
            "accepted_as_full_correlated_profile": False,
        },
    ]
    profile = {
        "schema": "MTTHiggsFullCorrelatedProfileReadinessMatrix.v1",
        "status": "FULL_CORRELATED_PROFILE_READINESS_BUILT_EMPIRICAL_PROFILE_OPEN",
        "blocks": profile_blocks,
        "required_full_profile_object": {
            "observable_vector": "ten Higgs partial widths plus total width and branching ratios derived by fixed maps",
            "covariance_or_profile": "10x10 PSD covariance with cross-channel correlations or equivalent profiled likelihood",
            "scheme": "declared perturbative, threshold, mass, and electroweak input convention",
            "source_guard": "measured benchmark values enter after row/source selection only",
        },
        "summary": {
            "block_count": len(profile_blocks),
            "available_stress_or_diagonal_blocks": 3,
            "full_empirical_profile_filled": False,
            "cross_block_correlations_filled": False,
            "accepted_as_full_correlated_profile": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    blockers = {
        "schema": "MTTHiggsMinimalPrecisionClosureBlockerSet.v1",
        "status": "MINIMAL_PRECISION_BLOCKER_SET_LOCALIZED",
        "blockers": [
            {
                "id": "accepted_precision_row_values",
                "description": "replace every proxy/import-identity row by an accepted precision formula row or accepted precision import",
                "blocking_precision_total_width": True,
                "blocking_precision_branching_ratios": True,
            },
            {
                "id": "full_correlated_profile",
                "description": "supply the ten-channel correlated covariance/profile likelihood, including cross-block shared inputs",
                "blocking_precision_total_width": True,
                "blocking_precision_branching_ratios": True,
            },
            {
                "id": "source_operator_upgrade",
                "description": "supply actual no-knob Qa/SU3 and electroweak operator-source packets for true source closure",
                "blocking_precision_total_width": False,
                "blocking_precision_branching_ratios": False,
                "blocking_true_sm_equivalence_and_no_knob": True,
            },
        ],
        "minimal_for_sm_parity_precision_replay": [
            "accepted_precision_row_values",
            "full_correlated_profile",
        ],
        "minimal_for_no_knob_source_closure": [
            "accepted_precision_row_values",
            "full_correlated_profile",
            "source_operator_upgrade",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    decision = {
        "schema": "MTTHiggsPrecisionRowsOrFullProfileDecision.v1",
        "status": "PRECISION_ROW_GATE_BUILT_VALUES_AND_FULL_PROFILE_OPEN",
        "precision_row_promotion_gate_built": True,
        "full_correlated_profile_readiness_built": True,
        "minimal_blocker_set_localized": True,
        "accepted_precision_row_count": 0,
        "full_correlated_profile_filled": False,
        "precision_total_width_closed": False,
        "precision_branching_ratios_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "next_executable_options": [
            "Route A: fill accepted precision formulas/imports row by row",
            "Route B: fill an externally accepted full correlated Higgs profile convention",
            "Route C: continue no-knob operator-source upgrades in parallel without promoting replay precision",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    updated_true = {
        "schema": "MTTUpdatedTrueEquivalenceGateAfterPrecisionRowGate.v1",
        "status": "PRECISION_ROW_GATE_BUILT_TRUE_EQUIVALENCE_STILL_OPEN",
        "previous_true_equivalence_blockers": previous_true["remaining_true_equivalence_blockers"],
        "closed_now": previous_true["closed_now"] + [
            "Higgs ten-channel precision-row promotion gate",
            "Higgs full correlated-profile readiness matrix",
            "minimal Higgs precision closure blocker set",
        ],
        "remaining_true_equivalence_blockers": previous_true["remaining_true_equivalence_blockers"],
        "next_primary_value_gate": "fill accepted precision Higgs row values or the full correlated Higgs profile",
        "guardrails": {
            "zero_precision_rows_promoted": True,
            "full_profile_not_filled": True,
            "precision_total_width_closed": False,
            "precision_branching_ratios_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHiggsPrecisionRowsOrFullCorrelatedProfile",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_higgstenchannelcovarianceprofile_or_branchingreplay.candidate.json"),
            "ten_channel_total_width_profile": rel(
                DATA
                / "selected_higgstenchannelcovarianceprofile_or_branchingreplay"
                / "ten_channel_total_width_diagonal_profile.packet.json"
            ),
            "ten_channel_branching_replay": rel(
                DATA
                / "selected_higgstenchannelcovarianceprofile_or_branchingreplay"
                / "ten_channel_branching_ratio_replay.packet.json"
            ),
            "qcd_stress_profile": rel(
                DATA
                / "selected_higgsqcdprecisionthresholdrows_or_correlatedprofileupgrade"
                / "higgs_qcd_correlation_stress_profile.packet.json"
            ),
            "ew_stress_profile": rel(
                DATA
                / "selected_higgsewformulakernelexecution_or_precisionimportrows"
                / "ew_three_channel_correlation_stress_profile.packet.json"
            ),
        },
        "output_packets": {
            "precision_row_promotion_gate": rel(ROWS),
            "full_correlated_profile_readiness": rel(PROFILE),
            "minimal_precision_closure_blocker_set": rel(BLOCKERS),
            "precision_rows_or_full_profile_decision": rel(DECISION),
            "updated_true_equivalence_gate": rel(UPDATED_TRUE),
        },
        "theorem": {
            "name": "HiggsPrecisionRowsOrFullCorrelatedProfileGateTheorem",
            "proved": True,
            "statement": (
                "Given the ten-channel Higgs branching replay, the repo can determine an exact promotion gate "
                "for every Higgs partial-width row and a readiness matrix for the full correlated profile. "
                "The gate promotes zero rows to precision and localizes the remaining closure to accepted "
                "precision row values plus the full correlated profile, with no benchmark values used as selectors."
            ),
        },
        "what_closes_now": {
            "ten_channel_precision_row_promotion_gate": True,
            "full_correlated_profile_readiness_matrix": True,
            "minimal_precision_blocker_set": True,
            "zero_promotion_guardrail": True,
        },
        "what_remains_open": {
            "accepted_precision_Higgs_row_values": True,
            "full_ten_channel_correlated_profile": True,
            "precision_total_width": True,
            "precision_branching_ratios": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "precision_row_promotion_gate_built": True,
            "full_correlated_profile_readiness_built": True,
            "accepted_precision_row_count": 0,
            "full_correlated_profile_filled": False,
            "precision_total_width_closed": False,
            "precision_branching_ratios_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_HiggsPrecisionRows_or_FullCorrelatedProfile_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "precision_row_promotion_gate_built": True,
        "full_correlated_profile_readiness_built": True,
        "accepted_precision_row_count": 0,
        "full_correlated_profile_filled": False,
        "precision_total_width_closed": False,
        "precision_branching_ratios_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_HiggsPrecisionValueFill_or_ProfileConventionImport_v1",
    }

    note = f"""# MTT Selected HiggsPrecisionRows or FullCorrelatedProfile v1

Status: `{STATUS}`.

This artifact builds the promotion gate for all ten Higgs partial-width rows and
the readiness matrix for the full correlated Higgs profile. It promotes zero
rows to precision. That is the point: the repo now knows exactly what must be
filled before the total width or branching-ratio replay can be promoted.

The near-term fork is now explicit: either fill accepted precision formula or
import values row by row, or import/build a full correlated Higgs profile
convention. No benchmark value is used as a source selector.
"""

    for path, payload in [
        (ROWS, row_gate),
        (PROFILE, profile),
        (BLOCKERS, blockers),
        (DECISION, decision),
        (UPDATED_TRUE, updated_true),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
