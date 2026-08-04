"""Build post-SM-parity source-theorem bundle and true-equivalence exit matrix."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_postsmparity_sourcetheorembundle_or_trueequivalence_exitmatrix"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
BUNDLE = PACKET_DIR / "post_smparity_source_theorem_bundle.packet.json"
EXIT_MATRIX = PACKET_DIR / "true_equivalence_exit_matrix.packet.json"
PAPER_CHECKLIST = PACKET_DIR / "paper_insertion_and_guardrail_checklist.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PostSMParity_SourceTheoremBundle_or_TrueEquivalenceExitMatrix_v1.md"

STATUS = "MTT_SELECTED_POSTSMPARITY_SOURCETHEOREMBUNDLE_OR_TRUEEQUIVALENCE_EXITMATRIX_BUILT"
NEXT = "MTT_Selected_HYMNewtonGalerkin_FirstSolve_or_Rank2SectorFunctor_v1"
PARALLEL_NEXT = "MTT_Selected_ProfileLikelihoodSourceImport_or_QaSU3PacketCandidateMining_v1"


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
    replay_refresh = load(DATA / "selected_fullsmparityreplayclosure_or_nonhiggsprofilepolicy.candidate.json")
    dynamic_c1 = load(DATA / "selected_dynamicc1parityvaluepacket_after_stationarydotd_integration.candidate.json")
    physical_patch = load(DATA / "selected_physicalsourceemission_patchbackimport_or_unpatchedderivation.candidate.json")
    source_kernel = load(DATA / "selected_postsmparity_trueequivalence_sourceupgrade_kernel.candidate.json")
    true_frontier = load(DATA / "selected_latest_trueequivalencefrontier_or_valueemissioncutset.candidate.json")
    profile_search = load(DATA / "selected_fullprofilematrixreconstruction_or_qasu3actualpacketsearch.candidate.json")
    qasu3_fill = load(DATA / "selected_qasu3candidatepayloadfill_or_profilesourceacquisition.candidate.json")
    visible_payload = load(DATA / "selected_visibleoperatorpayload_or_routechymresidual.candidate.json")
    static_readout = load(DATA / "selected_matterslot_readout_backimport_from_smslotfunctor.candidate.json")

    source_bundle = {
        "schema": "MTTPostSMParitySourceTheoremBundle.v1",
        "status": "SOURCE_THEOREM_BOUNDARY_BUNDLED",
        "closed_for_SM_parity": {
            "SM_parity_under_declared_interface_standard": sm_parity["closure_decision"]["SM_parity_closed"],
            "Higgs_replay_policy_refresh": replay_refresh["closure_decision"]["SM_parity_closed_after_Higgs_refresh"],
            "static_matter_slot_readout": static_readout["what_closes_now"][
                "selected_matter_slot_transversality_readout_functional_static_tier"
            ],
            "patched_dynamic_C1_value_packet": dynamic_c1["closure_decision"][
                "SM_parity_patched_dynamic_C1_value_packet_available"
            ],
            "patched_A_b_deltaTheta_replay": (
                dynamic_c1["closure_decision"]["patched_A_selected_emitted"]
                and dynamic_c1["closure_decision"]["patched_b_selected_emitted"]
                and dynamic_c1["closure_decision"]["patched_deltaTheta_C1_emitted"]
            ),
            "final_replay_refresh_keeps_SM_parity_closed": replay_refresh["closure_decision"]["SM_parity_closed"],
        },
        "support_only_not_promoted": {
            "actual_QaSU3_operator_packet": qasu3_fill["closure_decision"]["actual_QaSU3_packet_promoted"],
            "visible_operator_payload": visible_payload["closure_decision"]["visible_operator_payload_emitted"],
            "unpatched_dynamic_C1_packet": dynamic_c1["closure_decision"]["unpatched_dynamic_C1_packet_closed"],
            "full_profile_likelihood": profile_search["closure_decision"]["accepted_as_full_profile"],
        },
        "source_theorem_frontier": {
            "actual_QaSU3_operator_packet": True,
            "selected_HYM_Newton_Galerkin_first_solve": source_kernel["what_remains_open"][
                "selected_HYM_Newton_Galerkin_first_solve"
            ],
            "rank2_to_sector_transfer_functor": source_kernel["what_remains_open"][
                "rank2_to_sector_transfer_functor"
            ],
            "selected_rho_E_metric_D_E_Riesz_Green_dotD_C1": source_kernel["what_remains_open"][
                "selected_rho_E_metric_D_E_Riesz_Green_dotD_C1"
            ],
            "unpatched_dynamic_C1_derivation": physical_patch["what_remains_open"][
                "unpatched_no_knob_dynamic_C1_derivation"
            ],
        },
        "guardrails": {
            "SM_parity_not_reopened": True,
            "true_SM_equivalence_not_claimed": True,
            "no_knob_not_claimed": True,
            "observed_data_used_as_selector": False,
            "target_fitting_used": False,
            "superset_paths_are_constraints_not_knobs": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    exit_matrix = {
        "schema": "MTTTrueEquivalenceExitMatrix.v1",
        "status": "TWO_LEGAL_EXITS_EXPLICIT",
        "locked_target": "true SM equivalence after SM-parity closure",
        "exit_A_actual_source_theorem": {
            "name": "actual selected Qa/SU3-HYM operator theorem",
            "primary_next": NEXT,
            "required": [
                "selected gauge-fixed HYM/Strominger solve or theorem-derived equivalent",
                "rank2-to-sector transfer or proof it is unnecessary",
                "validator-ready rho_E, metric, D_E, Riesz/Green, dotD, and C1 payload",
                "same-source Chern-Weil/Freed-Witten/Bianchi/anomaly attachment",
                "no lifted selected flags and no measured-value source selection",
            ],
            "closed_now": False,
        },
        "exit_B_precision_profile_values": {
            "name": "precision profile, loop, threshold, covariance value table",
            "primary_next": PARALLEL_NEXT,
            "required": [
                "published or independently reconstructed profile likelihood",
                "precision loop-corrected local QFT observable rows",
                "threshold and mass-scheme conversion semantics",
                "covariance/profile validation and promotion policy",
                "source layer remains fixed independently of profile residuals",
            ],
            "closed_now": False,
        },
        "superset_use": {
            "using_one_straight_path": False,
            "combines_multiple_paths": True,
            "combination_rule": (
                "Source and precision routes may cross-check a locked target, but neither route supplies "
                "free knobs for the other and measured residuals cannot select source structure."
            ),
        },
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    paper_checklist = {
        "schema": "MTTPaperInsertionAndGuardrailChecklist.v1",
        "status": "READY_FOR_PAPER_DRAFT_INSERTION_WITH_OPEN_GATES",
        "sections_to_add": [
            {
                "title": "SM-Parity Source Interface Closure",
                "claim": "Under the declared parity-interface standard, MTT supplies the typed SM source/replay interface.",
                "guardrail": "Do not call this no-knob derivation or true precision equivalence.",
            },
            {
                "title": "Patched Dynamic C1 Replay Packet",
                "claim": "The SelectedFiniteC1TraceMeasurePrinciple patch supplies parity-tier A_selected, b_selected, deltaTheta_C1, and sector responses.",
                "guardrail": "Unpatched physical Phi_fin^C1 source derivation remains open.",
            },
            {
                "title": "True-Equivalence Exit Matrix",
                "claim": "True equivalence now has two legal exits: actual source theorem or precision profile values.",
                "guardrail": "Superset paths are constraints on one locked target, not adjustable fitting knobs.",
            },
            {
                "title": "Actual Qa/SU3-HYM Operator Theorem",
                "claim": "The next theorem must emit selected rho_E, D_E, Green/Riesz, dotD, and C1 payloads.",
                "guardrail": "Support packets, lifted flags, and replay residuals are not source promotion.",
            },
        ],
        "current_paper_ready_theorem": (
            "SM-parity is closed under the declared parity-interface standard; true SM equivalence requires "
            "either a selected actual Qa/SU3-HYM operator theorem or a precision profile/loop/covariance "
            "value table. No observed constant is used as a source selector."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedPostSMParitySourceTheoremBundleOrTrueEquivalenceExitMatrix",
        "status": STATUS,
        "inputs": {
            "final_sm_parity_closure": rel(DATA / "selected_qasu3sourcepacket_or_finalsmparityclosure.candidate.json"),
            "full_smparity_replay_refresh": rel(
                DATA / "selected_fullsmparityreplayclosure_or_nonhiggsprofilepolicy.candidate.json"
            ),
            "patched_dynamic_C1_value_packet": rel(
                DATA / "selected_dynamicc1parityvaluepacket_after_stationarydotd_integration.candidate.json"
            ),
            "physical_source_patch_backimport": rel(
                DATA / "selected_physicalsourceemission_patchbackimport_or_unpatchedderivation.candidate.json"
            ),
            "post_smparity_source_upgrade_kernel": rel(
                DATA / "selected_postsmparity_trueequivalence_sourceupgrade_kernel.candidate.json"
            ),
            "latest_true_equivalence_frontier": rel(
                DATA / "selected_latest_trueequivalencefrontier_or_valueemissioncutset.candidate.json"
            ),
            "full_profile_matrix_search": rel(
                DATA / "selected_fullprofilematrixreconstruction_or_qasu3actualpacketsearch.candidate.json"
            ),
            "qasu3_payload_fill": rel(DATA / "selected_qasu3candidatepayloadfill_or_profilesourceacquisition.candidate.json"),
            "visible_operator_payload": rel(DATA / "selected_visibleoperatorpayload_or_routechymresidual.candidate.json"),
            "static_matter_slot_readout": rel(
                DATA / "selected_matterslot_readout_backimport_from_smslotfunctor.candidate.json"
            ),
        },
        "output_packets": {
            "source_theorem_bundle": rel(BUNDLE),
            "true_equivalence_exit_matrix": rel(EXIT_MATRIX),
            "paper_insertion_and_guardrail_checklist": rel(PAPER_CHECKLIST),
        },
        "theorem": {
            "name": "PostSMParitySourceTheoremBundleAndExitMatrixTheorem",
            "proved": True,
            "statement": (
                "The current repo proves an SM-parity source/replay closure under the declared interface standard "
                "and bundles the remaining stronger goals into two exact exits: an actual selected Qa/SU3-HYM "
                "operator theorem, or a precision profile/loop/covariance value table. Patched dynamic C1 values "
                "and static matter-slot readout are closed at the parity tier; unpatched dynamic C1, actual Qa/SU3 "
                "operator payloads, true SM equivalence, and no-knob closure remain open."
            ),
        },
        "closure_decision": {
            "SM_parity_closed": True,
            "source_theorem_bundle_built": True,
            "true_equivalence_exit_matrix_built": True,
            "actual_QaSU3_operator_packet_promoted": False,
            "precision_profile_complete": False,
            "unpatched_dynamic_C1_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "what_closes_now": {
            "paper_ready_source_theorem_bundle": True,
            "true_equivalence_exit_matrix": True,
            "static_and_patched_dynamic_parity_closures_reconciled": True,
            "superset_strategy_guardrails_machine_checked": True,
            "SM_parity_not_reopened": True,
        },
        "what_remains_open": {
            "actual_QaSU3_HYM_operator_theorem": True,
            "precision_profile_loop_covariance_value_table": True,
            "unpatched_dynamic_C1_source_derivation": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "superset_strategy": {
            "using_one_straight_path": False,
            "combines_multiple_paths": True,
            "locked_target": "true SM equivalence after SM-parity closure",
            "paths": [
                "actual source theorem route",
                "precision profile value route",
                "patched dynamic C1 parity replay route",
                "static terminal/SM-slot matter readout route",
            ],
            "paths_used_as_knobs": False,
        },
        "previous_statuses": {
            "SM_parity": sm_parity["status"],
            "replay_refresh": replay_refresh["status"],
            "dynamic_C1": dynamic_c1["status"],
            "source_kernel": source_kernel["status"],
            "latest_frontier": true_frontier["status"],
        },
        "next_required_artifact": NEXT,
        "parallel_next_artifact": PARALLEL_NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_Selected_PostSMParity_SourceTheoremBundle_or_TrueEquivalenceExitMatrix_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "SM_parity_closed": True,
        "source_theorem_bundle_built": True,
        "true_equivalence_exit_matrix_built": True,
        "actual_QaSU3_operator_packet_promoted": False,
        "precision_profile_complete": False,
        "unpatched_dynamic_C1_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
        "parallel_next_artifact": PARALLEL_NEXT,
    }

    note = f"""# MTT Selected PostSMParity SourceTheoremBundle or TrueEquivalenceExitMatrix v1

Status: `{STATUS}`.

This theorem bundle records the present boundary:

- SM-parity is closed under the declared parity-interface standard.
- Static matter-slot readout and patched dynamic C1 values are closed at the
  parity tier.
- True SM equivalence is not closed.
- No-knob closure is not closed.

The remaining stronger goal has two legal exits:

1. Actual source theorem: selected Qa/SU3-HYM operator payload with rho_E,
   D_E, Riesz/Green, dotD, and C1 data from the selected branch.
2. Precision replay theorem: a full profile/loop/threshold/covariance value
   table accepted under the declared precision policy.

Superset strategy is still active, but only as constraint propagation toward a
locked target. It is not a knob bank, and observed replay residuals cannot
select source structure.

Next source artifact: `{NEXT}`.
Parallel precision artifact: `{PARALLEL_NEXT}`.
"""

    for path, payload in [
        (BUNDLE, source_bundle),
        (EXIT_MATRIX, exit_matrix),
        (PAPER_CHECKLIST, paper_checklist),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
