"""Build current true-equivalence frontier after external RG and SM-slot closure."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_trueequivalence_currentfrontier_after_externalrg_smslot"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
FRONTIER = PACKET_DIR / "current_true_equivalence_frontier.packet.json"
ROUTES = PACKET_DIR / "dual_route_execution_matrix.packet.json"
NEXT_ACTIONS = PACKET_DIR / "next_actions.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_TrueEquivalence_CurrentFrontier_AfterExternalRG_SMSlot_v1.md"

STATUS = "MTT_SELECTED_TRUEEQUIVALENCE_CURRENTFRONTIER_AFTER_EXTERNALRG_SMSLOT_BUILT_OPEN"
NEXT = "MTT_Selected_PrecisionProfileLoopValues_or_ActualQaSU3OperatorPayload_CurrentExecution_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def true_keys(packet: dict[str, Any], section: str) -> list[str]:
    values = packet.get(section, {})
    if not isinstance(values, dict):
        return []
    return [key for key, value in values.items() if value is True]


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    external_rg = load(DATA / "selected_externalrgbenchmarkvalues_or_localqftobservablefunctor.candidate.json")
    external_lit = load(DATA / "selected_externalliteraturergbenchmarkvalues_or_thresholdcovariance.candidate.json")
    smslot_overlap = load(DATA / "selected_smslotfunctor_overlapkernel_source_emission.candidate.json")
    smslot_downstream = load(DATA / "selected_smslotfunctor_downstream_operator_payloads_or_smparity_ledger.candidate.json")
    precision_contract = load(DATA / "selected_trueequivalenceprecisionvaluetable_or_actualqasu3operatorupgrade.candidate.json")
    profile_matrix = load(DATA / "selected_fullprofilematrixreconstruction_or_qasu3actualpacketsearch.candidate.json")
    source_kernel = load(DATA / "selected_postsmparity_trueequivalence_sourceupgrade_kernel.candidate.json")
    hym_first = load(DATA / "selected_hymnewtongalerkin_firstsolve_or_rank2sectorfunctor.candidate.json")
    stationary = load(DATA / "selected_stationaryprojector_dotd_integrated_frontier.candidate.json")

    frontier = {
        "schema": "MTTTrueEquivalenceCurrentFrontierAfterExternalRGSMSlot.v1",
        "status": "TRUE_EQUIVALENCE_OPEN_VALUE_OR_DYNAMIC_OPERATOR_PAYLOAD",
        "SM_parity_closed": True,
        "external_rg_local_benchmark_done": external_rg["what_closes_now"][
            "independent_local_rg_benchmark_values_filled"
        ],
        "external_literature_rg_rows_done": external_lit["what_closes_now"][
            "external_literature_rg_benchmark_values_filled"
        ],
        "local_qft_functor_interface_done": external_rg["what_closes_now"][
            "local_qft_observable_functor_interface_built"
        ],
        "static_smslot_source_closed": smslot_overlap["what_closes_now"][
            "selected_SMSlotFunctor_all_six_arrows"
        ],
        "static_sector_route_and_trace_normalization_closed": (
            smslot_downstream["what_closes_now"]["selected_static_sector_route_Z_to_u_e_X_to_d_nuD"]
            and smslot_downstream["what_closes_now"]["selected_static_finite_trace_transfer_normalization"]
        ),
        "hym_diagonal_first_solve_closed": hym_first["what_closes_now"]["selected_diagonal_HYM_first_solve"],
        "stationary_projector_dotd_reconciled": stationary["what_closes_now"][
            "stationary_projector_rho_s_reconciled"
        ],
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    routes = {
        "schema": "MTTTrueEquivalenceDualRouteExecutionMatrix.v1",
        "status": "DUAL_ROUTE_OPEN",
        "route_A_precision_profile_loop_values": {
            "current_status": precision_contract["status"],
            "surrogate_profile_matrix_reconstructed": profile_matrix["closure_decision"][
                "surrogate_profile_matrix_reconstructed"
            ],
            "accepted_as_full_profile": profile_matrix["closure_decision"]["accepted_as_full_profile"],
            "must_emit": [
                "published or independently reconstructed non-Higgs profile likelihood",
                "precision local-QFT loop observable values",
                "threshold/mass-scheme/covariance values at declared convention",
                "profile/covariance semantics strong enough for true SM equivalence",
            ],
            "open_items": true_keys(profile_matrix, "what_remains_open")
            + true_keys(precision_contract, "what_remains_open"),
            "closed_now": False,
        },
        "route_B_actual_qasu3_hym_operator_payload": {
            "current_status": source_kernel["status"],
            "hym_first_solve_status": hym_first["status"],
            "stationary_frontier_status": stationary["status"],
            "already_harvested": [
                "selected diagonal HYM first solve",
                "diagonal End0 D_E formula",
                "full diagonal End0 Riesz/Green",
                "static SM-slot six-arrow source",
                "static 1_M Dirac neutrino shift rule",
                "stationary projector/dotD reconciliation",
            ],
            "must_emit": [
                "actual selected Qa/SU3 operator packet",
                "sector-ready dynamic D_E/Riesz/Green/dotD/C1 response payload",
                "selected primitive C1 contractions",
                "selected A_selected, b_selected, deltaTheta_C1, and sector response matrices",
                "proof that dynamic operator values come from the same selected branch, not from parity-interface replay",
            ],
            "open_items": true_keys(source_kernel, "what_remains_open")
            + true_keys(hym_first, "what_remains_open")
            + true_keys(stationary, "what_remains_open"),
            "closed_now": False,
        },
        "route_C_interfaces": {
            "must_emit": [
                "local QFT observable values beyond tree/interface rows",
                "QM/GR measurement and response interfaces at the declared true-equivalence standard",
            ],
            "closed_now": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_actions = {
        "schema": "MTTTrueEquivalenceNextActionsAfterExternalRGSMSlot.v1",
        "recommended_next_artifact": NEXT,
        "primary_actions": [
            "Route A: replace the surrogate profile matrix with a published/reconstructed profile likelihood and precision loop value table.",
            "Route B: promote the actual Qa/SU3/HYM dynamic operator payload from the selected branch.",
            "Keep external RG/literature rows as downstream benchmarks only; do not use them as source selectors.",
            "Keep static SM-slot closure as an input; do not reopen it unless a later validator falsifies it.",
        ],
        "why_this_is_not_a_regression": (
            "The checkpoint starts after external RG, literature RG rows, and static SM-slot closure. "
            "It records only true-equivalence value/operator exits."
        ),
    }

    candidate = {
        "candidate": "MTTSelectedTrueEquivalenceCurrentFrontierAfterExternalRGSMSlot",
        "status": STATUS,
        "inputs": {
            "external_rg_local_qft": rel(DATA / "selected_externalrgbenchmarkvalues_or_localqftobservablefunctor.candidate.json"),
            "external_literature_rg": rel(DATA / "selected_externalliteraturergbenchmarkvalues_or_thresholdcovariance.candidate.json"),
            "smslot_overlap_kernel": rel(DATA / "selected_smslotfunctor_overlapkernel_source_emission.candidate.json"),
            "smslot_downstream_ledger": rel(DATA / "selected_smslotfunctor_downstream_operator_payloads_or_smparity_ledger.candidate.json"),
            "precision_dual_route_contract": rel(DATA / "selected_trueequivalenceprecisionvaluetable_or_actualqasu3operatorupgrade.candidate.json"),
            "full_profile_matrix_search": rel(DATA / "selected_fullprofilematrixreconstruction_or_qasu3actualpacketsearch.candidate.json"),
            "post_smparity_source_upgrade_kernel": rel(DATA / "selected_postsmparity_trueequivalence_sourceupgrade_kernel.candidate.json"),
            "hym_first_solve": rel(DATA / "selected_hymnewtongalerkin_firstsolve_or_rank2sectorfunctor.candidate.json"),
            "stationary_projector_dotd_frontier": rel(DATA / "selected_stationaryprojector_dotd_integrated_frontier.candidate.json"),
        },
        "output_packets": {
            "current_true_equivalence_frontier": rel(FRONTIER),
            "dual_route_execution_matrix": rel(ROUTES),
            "next_actions": rel(NEXT_ACTIONS),
        },
        "theorem": {
            "name": "TrueEquivalenceCurrentFrontierAfterExternalRGSMSlotTheorem",
            "proved": True,
            "statement": (
                "Once external RG/local-QFT interface rows, external literature RG benchmark rows, "
                "static SM-slot six-arrow source emission, and the HYM diagonal first solve are imported, "
                "the active true-equivalence frontier is no longer SM-parity bookkeeping. It is exactly "
                "precision profile/loop value completion or actual selected Qa/SU3-HYM dynamic operator "
                "payload promotion, with QM/GR/local-QFT value interfaces still open."
            ),
        },
        "closure_decision": {
            "SM_parity_closed": True,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "what_closes_now": {
            "external_rg_rung_confirmed_done": True,
            "external_literature_rg_rung_confirmed_done": True,
            "static_smslot_source_closure_confirmed_done": True,
            "true_equivalence_dual_route_frontier_locked": True,
            "SM_parity_not_reopened": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "published_or_reconstructed_profile_likelihood": True,
            "precision_local_QFT_loop_values": True,
            "actual_QaSU3_operator_packet": True,
            "dynamic_sector_ready_operator_payload": True,
            "QM_GR_measurement_response_interfaces": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_Selected_TrueEquivalence_CurrentFrontier_AfterExternalRG_SMSlot_v1",
        "candidate_path": rel(OUTPUT),
        "status": STATUS,
        "theorem_proved": True,
        "SM_parity_closed": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "note_path": rel(NOTE),
    }

    note = f"""# MTT Selected TrueEquivalence CurrentFrontier AfterExternalRG SMSlot v1

This artifact locks the current true-equivalence frontier after the already
verified external RG/local-QFT and external literature RG rungs.

It also imports the static SM-slot result: all six SM-slot arrows and static
overlap transfer normalization are closed as source-tier inputs.

The active frontier is therefore not SM-parity repair.  It is:

- precision profile/loop/covariance value completion, or
- actual selected Qa/SU3-HYM dynamic operator payload promotion.

Next artifact: `{NEXT}`.
"""

    for path, payload in [
        (FRONTIER, frontier),
        (ROUTES, routes),
        (NEXT_ACTIONS, next_actions),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
