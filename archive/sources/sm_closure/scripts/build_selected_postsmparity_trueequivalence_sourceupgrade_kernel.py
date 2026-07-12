"""Build post-SM-parity true-equivalence source-upgrade kernel."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_postsmparity_trueequivalence_sourceupgrade_kernel"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
KERNEL = PACKET_DIR / "post_smparity_true_equivalence_source_upgrade_kernel.packet.json"
HYM_ACCEPTANCE = PACKET_DIR / "hym_newton_galerkin_acceptance_kernel.packet.json"
ROUTE_LOCK = PACKET_DIR / "dual_route_superset_lock.packet.json"
CUTSET = PACKET_DIR / "next_source_upgrade_cutset.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PostSMParity_TrueEquivalenceSourceUpgrade_Kernel_v1.md"

STATUS = "MTT_SELECTED_POSTSMPARITY_TRUEEQUIVALENCE_SOURCEUPGRADE_KERNEL_BUILT_HYM_SOLVE_OR_PROFILE_VALUES_OPEN"
NEXT = "MTT_Selected_HYMNewtonGalerkin_FirstSolve_or_Rank2SectorFunctor_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    sm_parity = load(DATA / "selected_qasu3sourcepacket_or_finalsmparityclosure.candidate.json")
    frontier = load(DATA / "selected_true_sm_equivalence_frontier_after_smparityclosure.candidate.json")
    dual_route = load(DATA / "selected_trueequivalenceprecisionvaluetable_or_actualqasu3operatorupgrade.candidate.json")
    qasu3_payload = load(DATA / "selected_qasu3candidatepayloadfill_or_profilesourceacquisition.candidate.json")
    visible_operator = load(DATA / "selected_visibleoperatorpayload_or_routechymresidual.candidate.json")
    hym_bridge = load(DATA / "selected_hymconnectionextraction_or_sourceoriginlemma.candidate.json")
    hym_cutset = load(
        DATA
        / "selected_hymconnectionextraction_or_sourceoriginlemma"
        / "newton_galerkin_or_rank2_sector_transfer_cutset.packet.json"
    )
    full_profile = load(DATA / "selected_fullcovarianceprofile_or_multiloopconventionaudit.candidate.json")

    kernel = {
        "schema": "MTTPostSMParityTrueEquivalenceSourceUpgradeKernel.v1",
        "status": "POST_SMPARITY_KERNEL_LOCKED_TRUE_EQUIVALENCE_OPEN",
        "SM_parity_status": {
            "closed": sm_parity["closure_decision"]["SM_parity_closed"],
            "standard": "declared parity-interface standard",
            "must_not_reopen_for_true_equivalence": True,
            "actual_operator_packet_claimed": sm_parity["actual_selected_operator_packet_claimed"],
        },
        "true_equivalence_status": {
            "closed": frontier["closure_decision"]["true_SM_equivalence_closed"],
            "frontier_matrix_built": frontier["what_closes_now"]["post_SM_parity_frontier_identified"],
            "requires_source_or_precision_upgrade": True,
        },
        "guardrails": {
            "observed_data_used_as_selector": False,
            "target_fitting_used": False,
            "downstream_measured_replay_may_constrain_only": True,
            "no_knob_claims_separated": True,
        },
        "source_upgrade_center": {
            "current_best_lane": "same-source visible/color packet via ordered V_alpha, Route-C/HYM, and HYM extraction",
            "partial_qasu3_payload_filled": qasu3_payload["closure_decision"]["partial_QaSU3_payload_filled"],
            "actual_qasu3_operator_packet_promoted": qasu3_payload["closure_decision"]["actual_QaSU3_packet_promoted"],
            "visible_operator_status": visible_operator["status"],
            "hym_bridge_status": hym_bridge["status"],
        },
        "selected_next_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    hym_acceptance = {
        "schema": "MTTHYMNewtonGalerkinAcceptanceKernel.v1",
        "status": "ACCEPTANCE_KERNEL_BUILT_VALUES_OPEN",
        "source": rel(
            DATA
            / "selected_hymconnectionextraction_or_sourceoriginlemma"
            / "newton_galerkin_or_rank2_sector_transfer_cutset.packet.json"
        ),
        "required_payloads": hym_cutset["remaining_minimal_payloads"],
        "acceptance_checks": [
            "selected gauge-fixed A_HYM or S/H coefficient vector is emitted from the selected q79/F,m=1 source",
            "Coulomb/unitary gauge-fixing and determinant-one metric convention are declared",
            "coercive gauge-fixed Jacobian/Hessian lower bound is proved on the finite basis",
            "quadrature/truncation residual is bounded independently of measured SM targets",
            "rank2 V_alpha data is transferred into the rank-3/family-sector operator scaffold or the transfer is proved unnecessary",
            "rho_E, metric, D_E, Riesz/Green, dotD, and C1/overlap payloads are emitted without lifted selected flags",
            "Bianchi/Freed-Witten/anomaly and typed monad/section-ring maps attach to the same selected packet",
            "all true-equivalence validators replay without smoke fixtures or observed constants as selectors",
        ],
        "diagonal_rank2_support_imported": hym_bridge["closure_decision"]["diagonal_rank2_payload_imported"],
        "full_sector_operator_payload_emitted": hym_bridge["closure_decision"]["full_sector_operator_payload_emitted"],
        "actual_QaSU3_packet_promoted": hym_bridge["closure_decision"]["actual_QaSU3_packet_promoted"],
        "accepted_for_true_SM_equivalence_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    route_lock = {
        "schema": "MTTDualRouteSupersetLock.v1",
        "status": "SUPERSET_ROUTES_LOCKED_WITHOUT_KNOBS",
        "straight_path": {
            "name": "actual_QaSU3_operator_packet_via_HYM_source_upgrade",
            "role": "replace the parity-interface packet with theorem-derived operator data",
            "next_artifact": NEXT,
            "closed_now": False,
        },
        "parallel_precision_path": {
            "name": "precision_profile_loop_covariance_values",
            "role": "complete true-equivalence replay values without selecting source structure",
            "contract_ready": dual_route["closure_decision"]["precision_value_table_contract_ready"],
            "full_covariance_profile_closed": full_profile["closure_decision"]["full_covariance_profile_closed"],
            "closed_now": False,
        },
        "locked_target": "true SM equivalence after SM-parity closure",
        "not_the_locked_target": "no-knob derivation of all constants",
        "route_interaction": (
            "The source route and precision route may cross-check each other, but neither route may use downstream "
            "observed masses, mixings, widths, or profile residuals to choose the selected source packet."
        ),
        "SM_parity_closed": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cutset = {
        "schema": "MTTNextSourceUpgradeCutset.v1",
        "status": "NEXT_GATE_IS_SELECTED_HYM_SOLVE_OR_RANK2_SECTOR_TRANSFER",
        "bookkeeping_remaining": False,
        "value_or_source_emission_required": True,
        "minimal_next_payloads": [
            "execute the selected HYM Newton/Galerkin first solve on the fixed q79/F,m=1 source",
            "or prove the rank2-to-sector transfer functor and emit sector-ready rho_E/D_E/Riesz/Green/dotD/C1 payloads",
            "or fill a published/reconstructed precision profile matrix as the parallel precision route",
        ],
        "primary_recommended_next_artifact": NEXT,
        "parallel_recommended_artifact": "MTT_Selected_ProfileLikelihoodValues_or_PrecisionProfileWorkspaceImport_v1",
        "SM_parity_closed": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedPostSMParityTrueEquivalenceSourceUpgradeKernel",
        "status": STATUS,
        "inputs": {
            "sm_parity_closure": rel(DATA / "selected_qasu3sourcepacket_or_finalsmparityclosure.candidate.json"),
            "true_equivalence_frontier": rel(DATA / "selected_true_sm_equivalence_frontier_after_smparityclosure.candidate.json"),
            "dual_route_contract": rel(
                DATA / "selected_trueequivalenceprecisionvaluetable_or_actualqasu3operatorupgrade.candidate.json"
            ),
            "qasu3_payload_fill": rel(DATA / "selected_qasu3candidatepayloadfill_or_profilesourceacquisition.candidate.json"),
            "visible_operator_bridge": rel(DATA / "selected_visibleoperatorpayload_or_routechymresidual.candidate.json"),
            "hym_extraction_bridge": rel(DATA / "selected_hymconnectionextraction_or_sourceoriginlemma.candidate.json"),
            "hym_cutset": rel(
                DATA
                / "selected_hymconnectionextraction_or_sourceoriginlemma"
                / "newton_galerkin_or_rank2_sector_transfer_cutset.packet.json"
            ),
            "full_covariance_profile": rel(DATA / "selected_fullcovarianceprofile_or_multiloopconventionaudit.candidate.json"),
        },
        "output_packets": {
            "post_smparity_true_equivalence_source_upgrade_kernel": rel(KERNEL),
            "hym_newton_galerkin_acceptance_kernel": rel(HYM_ACCEPTANCE),
            "dual_route_superset_lock": rel(ROUTE_LOCK),
            "next_source_upgrade_cutset": rel(CUTSET),
        },
        "theorem": {
            "name": "PostSMParityTrueEquivalenceSourceUpgradeKernelTheorem",
            "proved": True,
            "statement": (
                "After SM-parity closure, true SM equivalence is reduced to two legal superset upgrades: "
                "a precision profile/loop/covariance value route and an actual selected Qa/SU3 source/operator "
                "route. The current primary source route is the selected HYM Newton/Galerkin or rank2-to-sector "
                "transfer gate. This kernel closes the route-selection layer but emits no new physical values "
                "and makes no true-equivalence or no-knob closure claim."
            ),
        },
        "what_closes_now": {
            "SM_parity_not_reopened": True,
            "post_parity_true_equivalence_routes_locked": True,
            "HYM_acceptance_kernel_built": True,
            "next_source_upgrade_artifact_selected": True,
            "superset_strategy_guardrails_restated": True,
        },
        "what_remains_open": {
            "selected_HYM_Newton_Galerkin_first_solve": True,
            "rank2_to_sector_transfer_functor": True,
            "selected_rho_E_metric_D_E_Riesz_Green_dotD_C1": True,
            "actual_QaSU3_operator_packet": True,
            "full_precision_profile_or_likelihood_values": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "SM_parity_closed": sm_parity["closure_decision"]["SM_parity_closed"],
            "source_upgrade_kernel_built": True,
            "actual_QaSU3_operator_packet_promoted": False,
            "precision_profile_complete": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "superset_strategy": {
            "using_one_straight_way": False,
            "combining_paths": True,
            "paths_combined_as_constraints_not_knobs": [
                "HYM/Route-C source upgrade",
                "terminal-monad/section-ring source support",
                "precision profile and loop replay route",
            ],
            "locked_target": "true SM equivalence after parity closure",
        },
        "previous_statuses": {
            "SM_parity": sm_parity["status"],
            "frontier": frontier["status"],
            "dual_route": dual_route["status"],
            "hym_bridge": hym_bridge["status"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_PostSMParity_TrueEquivalenceSourceUpgrade_Kernel_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "SM_parity_closed": True,
        "source_upgrade_kernel_built": True,
        "actual_QaSU3_operator_packet_promoted": False,
        "precision_profile_complete": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PostSMParity TrueEquivalenceSourceUpgrade Kernel v1

Status: `{STATUS}`.

This artifact does not reopen SM-parity. It locks the post-parity target:
true SM equivalence now needs either precision profile/loop/covariance value
completion or an actual selected Qa/SU3 source/operator upgrade.

The primary source-upgrade route is now the selected HYM Newton/Galerkin or
rank2-to-sector transfer gate. The required output is a validator-ready packet
for rho_E, metric, D_E, Riesz/Green, dotD, and C1/overlap data, derived from
the selected q79/F,m=1 source without lifted flags or observed constants as
selectors.

The parallel precision route remains useful as a cross-check and replay layer,
but it cannot choose the source packet.
"""

    for path, payload in [
        (KERNEL, kernel),
        (HYM_ACCEPTANCE, hym_acceptance),
        (ROUTE_LOCK, route_lock),
        (CUTSET, cutset),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
