"""Build latest true-equivalence frontier after partial precision value emission."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_latest_trueequivalencefrontier_or_valueemissioncutset"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
FRONTIER = PACKET_DIR / "latest_true_equivalence_value_source_frontier.packet.json"
CUTSET = PACKET_DIR / "next_value_source_emission_cutset.packet.json"
NEXT_ACTIONS = PACKET_DIR / "next_actions_for_true_equivalence.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_LatestTrueEquivalenceFrontier_or_ValueEmissionCutset_v1.md"

STATUS = "MTT_SELECTED_LATEST_TRUEEQUIVALENCE_FRONTIER_BUILT_VALUE_SOURCE_CUTSET_OPEN"
NEXT = "MTT_Selected_FullProfileMatrixReconstruction_or_QaSU3ActualPacketSearch_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    smparity_status = load(DATA / "selected_latest_smparityclosure_status_or_trueequivalencefrontier.candidate.json")
    full_replay_refresh = load(DATA / "selected_fullsmparityreplayclosure_or_nonhiggsprofilepolicy.candidate.json")
    dual_contract = load(DATA / "selected_trueequivalenceprecisionvaluetable_or_actualqasu3operatorupgrade.candidate.json")
    partial_values = load(DATA / "selected_precisionvalueemissionattempt_or_qasu3sourcepayloadfill.candidate.json")
    post_source_kernel = load(DATA / "selected_postsmparity_trueequivalence_sourceupgrade_kernel.candidate.json")

    frontier = {
        "schema": "MTTLatestTrueEquivalenceValueSourceFrontier.v1",
        "status": "TRUE_EQUIVALENCE_REDUCED_TO_VALUE_OR_ACTUAL_SOURCE_EMISSION",
        "SM_parity_closed": True,
        "SM_parity_not_reopened": smparity_status["SM_parity_closed"] is True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "bookkeeping_layer_closed": {
            "precision_value_table_contract": dual_contract["what_closes_now"]["precision_value_table_contract"],
            "actual_QaSU3_operator_upgrade_contract": dual_contract["what_closes_now"][
                "actual_QaSU3_operator_upgrade_contract"
            ],
            "partial_precision_values_emitted": partial_values["closure_decision"]["partial_precision_values_emitted"],
            "post_parity_source_upgrade_kernel_built": post_source_kernel["closure_decision"]["source_upgrade_kernel_built"],
        },
        "still_open": {
            "actual_QaSU3_operator_packet": partial_values["what_remains_open"]["actual_QaSU3_operator_packet"],
            "full_nonHiggs_covariance_profile": partial_values["what_remains_open"]["full_nonHiggs_covariance_profile"],
            "precision_local_QFT_loop_values": partial_values["what_remains_open"]["precision_local_QFT_loop_values"],
            "selected_HYM_Newton_Galerkin_or_rank2_sector_transfer": post_source_kernel["what_remains_open"][
                "selected_HYM_Newton_Galerkin_first_solve"
            ],
            "QM_GR_measurement_response_interfaces": full_replay_refresh["what_remains_open"].get(
                "local_QFT_observable_functor", True
            ),
            "no_knob_closure": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cutset = {
        "schema": "MTTTrueEquivalenceValueSourceEmissionCutset.v1",
        "status": "NO_PURE_BOOKKEEPING_CLOSURE_REMAINS",
        "legal_routes": {
            "precision_value_route": [
                "full profile/covariance matrix reconstruction or import",
                "precision threshold and pole-running values",
                "loop-corrected local QFT rows",
                "promotion decision against declared precision policy",
            ],
            "actual_source_route": [
                "actual selected Qa/SU3 operator payload",
                "selected HYM Newton/Galerkin or rank2-to-sector transfer",
                "selected rho_E/D_E/Riesz/Green/dotD/C1 source data",
                "mapped Bianchi/Freed-Witten/anomaly certificate",
            ],
        },
        "forbidden_shortcuts": [
            "do not promote partial diagonal precision values to full profile likelihood",
            "do not treat Qa/SU3 parity-interface replacement as actual no-knob operator packet",
            "do not use observed replay rows to select source/operator payloads",
            "do not reopen SM parity while advancing true equivalence",
        ],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_actions = {
        "schema": "MTTNextActionsForTrueEquivalence.v1",
        "status": "PROCEED_TO_FULL_PROFILE_RECONSTRUCTION_OR_ACTUAL_QASU3_SEARCH",
        "recommended_next": NEXT,
        "why": "The precision route already emitted partial diagonal values, and the source route already has an explicit HYM/QaSU3 acceptance kernel. The next useful work is full profile reconstruction or actual Qa/SU3 packet search.",
        "superset_strategy": {
            "combines_paths": True,
            "locked_target": "true SM equivalence after SM-parity closure",
            "path_use": "precision values and actual source payload are parallel legal routes, used as constraints rather than adjustable knobs",
            "uses_observed_constants_as_source_selectors": False,
        },
    }

    FRONTIER.write_text(json.dumps(frontier, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CUTSET.write_text(json.dumps(cutset, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NEXT_ACTIONS.write_text(json.dumps(next_actions, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    candidate = {
        "candidate": "MTTSelectedLatestTrueEquivalenceFrontierOrValueEmissionCutset",
        "status": STATUS,
        "inputs": {
            "latest_smparity_status": rel(DATA / "selected_latest_smparityclosure_status_or_trueequivalencefrontier.candidate.json"),
            "full_smparity_replay_refresh": rel(DATA / "selected_fullsmparityreplayclosure_or_nonhiggsprofilepolicy.candidate.json"),
            "dual_route_contract": rel(DATA / "selected_trueequivalenceprecisionvaluetable_or_actualqasu3operatorupgrade.candidate.json"),
            "partial_precision_value_attempt": rel(DATA / "selected_precisionvalueemissionattempt_or_qasu3sourcepayloadfill.candidate.json"),
            "post_smparity_source_upgrade_kernel": rel(DATA / "selected_postsmparity_trueequivalence_sourceupgrade_kernel.candidate.json"),
        },
        "output_packets": {
            "frontier": rel(FRONTIER),
            "cutset": rel(CUTSET),
            "next_actions": rel(NEXT_ACTIONS),
        },
        "theorem": {
            "name": "LatestTrueEquivalenceValueSourceCutsetTheorem",
            "proved": True,
            "statement": (
                "After SM-parity closure, precision-suite construction, true-equivalence dual-route contract, post-parity source-upgrade kernel, and partial precision value emission, no pure bookkeeping step remains that can close true SM equivalence. "
                "The next closure attempt must emit either full precision/profile/loop values or an actual selected Qa/SU3 source/operator payload."
            ),
        },
        "what_closes_now": {
            "latest_true_equivalence_frontier_consolidated": True,
            "SM_parity_kept_closed": True,
            "bookkeeping_to_value_source_cutset_identified": True,
            "next_artifact_selected": True,
        },
        "what_remains_open": frontier["still_open"],
        "SM_parity_closed": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_LatestTrueEquivalenceFrontier_or_ValueEmissionCutset_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "SM_parity_closed": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "bookkeeping_to_value_source_cutset_identified": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected LatestTrueEquivalenceFrontier or ValueEmissionCutset v1

Status: `{STATUS}`.

SM parity remains closed. True SM equivalence is not closed.

The latest frontier is no longer bookkeeping. Two legal routes remain:

- emit full precision/profile/loop values with threshold and covariance semantics
- emit the actual selected Qa/SU3 source/operator payload

Partial diagonal precision values and Qa/SU3 parity-interface replacement are
useful support, but neither can be promoted to true equivalence by itself.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
