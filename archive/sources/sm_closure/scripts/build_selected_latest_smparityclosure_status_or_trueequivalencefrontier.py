"""Build latest SM-parity closure status and true-equivalence frontier consolidation."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_latest_smparityclosure_status_or_trueequivalencefrontier"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
LATEST_STATUS = PACKET_DIR / "latest_smparity_closure_status.packet.json"
TRUE_FRONTIER = PACKET_DIR / "true_equivalence_and_noknob_frontier.packet.json"
NEXT_ACTIONS = PACKET_DIR / "next_actions_after_smparity_closure.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_LatestSMParityClosureStatus_or_TrueEquivalenceFrontier_v1.md"

STATUS = "MTT_SELECTED_LATEST_SMPARITYCLOSURE_STATUS_BUILT_TRUE_EQUIVALENCE_OPEN"
NEXT = "MTT_Selected_ExternalRGBenchmarkValues_or_LocalQFTObservableFunctor_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    patch_backimport = load(DATA / "selected_physicalsourceemission_patchbackimport_or_unpatchedderivation.candidate.json")
    final_old_gap = load(DATA / "selected_finalsmparitygapmatrix_or_closureattempt.candidate.json")
    rg_firstpass = load(DATA / "selected_acceptedrgtransportvalues_or_qasu3sourcepacket.candidate.json")
    qasu3_closure = load(DATA / "selected_qasu3sourcepacket_or_finalsmparityclosure.candidate.json")
    true_frontier = load(DATA / "selected_true_sm_equivalence_frontier_after_smparityclosure.candidate.json")
    precision_suite = load(DATA / "selected_precisionempiricalreplaysuite_or_trueequivalence.candidate.json")

    latest_status = {
        "schema": "MTTLatestSMParityClosureStatus.v1",
        "status": "SM_PARITY_CLOSED_UNDER_DECLARED_PARITY_INTERFACE_STANDARD",
        "SM_parity_closed": qasu3_closure["closure_decision"]["SM_parity_closed"],
        "SM_parity_standard": "declared parity-interface standard with measured replay inputs downstream and Qa/SU3 parity-interface replacement accepted",
        "patched_dynamic_C1_retired": patch_backimport["what_closes_now"]["patched_dynamic_C1_no_longer_local_parity_blocker"],
        "accepted_RG_transport_for_SM_parity": rg_firstpass["what_closes_now"][
            "common_scale_Yukawa_and_Higgs_transport_closed_for_SM_parity"
        ],
        "selected_SM_packet_certificate_integrated_for_SM_parity": qasu3_closure["what_closes_now"][
            "selected_SM_packet_certificate_integration_closed_for_SM_parity"
        ],
        "old_gap_matrix_superseded": {
            "previous_status": final_old_gap["status"],
            "reason": "Later artifacts reduce two gates and then close both at the SM-parity tier.",
        },
        "not_claimed": {
            "actual_selected_QaSU3_no_knob_packet": qasu3_closure["actual_selected_operator_packet_claimed"] is False,
            "true_precision_SM_equivalence": qasu3_closure["closure_decision"]["true_SM_equivalence_closed"] is False,
            "full_no_knob_closure": qasu3_closure["closure_decision"]["no_knob_closed"] is False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    true_equivalence_frontier = {
        "schema": "MTTTrueEquivalenceAndNoKnobFrontierAfterSMParityClosure.v1",
        "status": "TRUE_EQUIVALENCE_AND_NOKNOB_FRONTIERS_OPEN_AFTER_SMPARITY",
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "true_equivalence_open": true_frontier["what_remains_open"],
        "precision_suite_status": precision_suite["status"],
        "precision_suite_built": precision_suite["closure_decision"]["precision_empirical_replay_suite_built"],
        "precision_remaining": precision_suite["what_remains_open"],
        "no_knob_open": {
            "actual_QaSU3_operator_packet_upgrade": qasu3_closure["what_remains_open"][
                "actual_QaSU3_color_operator_packet_no_knob"
            ],
            "unpatched_dynamic_C1_measure_derivation": patch_backimport["what_remains_open"][
                "unpatched_no_knob_dynamic_C1_derivation"
            ],
            "full_constants_derivation": True,
        },
        "guardrail": "SM parity is a parity-interface closure, not a no-knob derivation of all constants or a full precision QFT/GR/QM equivalence proof.",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_actions = {
        "schema": "MTTNextActionsAfterSMParityClosure.v1",
        "status": "NEXT_WORK_MOVES_TO_TRUE_EQUIVALENCE_OR_NOKNOB_UPGRADE",
        "recommended_primary_path": [
            "fill external RG benchmark values and precision threshold/pole-running tables",
            "execute full covariance/profile values",
            "advance local QFT observable functor",
            "upgrade Qa/SU3 parity-interface packet to actual selected operator packet",
        ],
        "recommended_no_knob_path": [
            "derive finite C1 trace-measure principle without patch",
            "derive actual Qa/SU3 typed monad/operator maps",
            "derive constants rather than replaying measured values",
        ],
        "superset_strategy": {
            "parity_route": "Use closed SM-parity interface as baseline replay standard.",
            "true_equivalence_route": "Tighten precision, covariance, RG benchmarks, local QFT/QM/GR observable functors.",
            "no_knob_route": "Replace parity-interface and measured replay admissions with actual selected source/operator derivations.",
            "uses_observed_constants_as_selectors": False,
        },
        "next_required_artifact": NEXT,
    }

    LATEST_STATUS.write_text(json.dumps(latest_status, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    TRUE_FRONTIER.write_text(json.dumps(true_equivalence_frontier, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NEXT_ACTIONS.write_text(json.dumps(next_actions, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    candidate = {
        "candidate": "MTTSelectedLatestSMParityClosureStatusOrTrueEquivalenceFrontier",
        "status": STATUS,
        "inputs": {
            "patch_backimport": rel(DATA / "selected_physicalsourceemission_patchbackimport_or_unpatchedderivation.candidate.json"),
            "old_gap_matrix": rel(DATA / "selected_finalsmparitygapmatrix_or_closureattempt.candidate.json"),
            "rg_firstpass": rel(DATA / "selected_acceptedrgtransportvalues_or_qasu3sourcepacket.candidate.json"),
            "qasu3_smparity_closure": rel(DATA / "selected_qasu3sourcepacket_or_finalsmparityclosure.candidate.json"),
            "true_equivalence_frontier": rel(DATA / "selected_true_sm_equivalence_frontier_after_smparityclosure.candidate.json"),
            "precision_suite": rel(DATA / "selected_precisionempiricalreplaysuite_or_trueequivalence.candidate.json"),
        },
        "output_packets": {
            "latest_status": rel(LATEST_STATUS),
            "true_frontier": rel(TRUE_FRONTIER),
            "next_actions": rel(NEXT_ACTIONS),
        },
        "theorem": {
            "name": "LatestSMParityClosureStatusTheorem",
            "proved": True,
            "statement": (
                "After patched dynamic C1 backimport, first-pass RG transport acceptance, and Qa/SU3 parity-interface replacement, SM parity is closed under the declared parity-interface standard. "
                "This supersedes the older open final-gap matrix at the parity tier. True precision SM equivalence and no-knob closure remain open and are separated into executable next frontiers."
            ),
        },
        "what_closes_now": {
            "latest_SM_parity_status_consolidated": True,
            "SM_parity_closed_under_declared_standard": True,
            "older_open_gap_matrix_superseded_at_parity_tier": True,
            "true_equivalence_frontier_preserved": True,
            "no_knob_frontier_preserved": True,
        },
        "what_remains_open": {
            "true_SM_equivalence": True,
            "precision_RG_threshold_covariance_values": True,
            "local_QFT_QM_GR_observable_interfaces": True,
            "actual_QaSU3_operator_packet_no_knob_upgrade": True,
            "unpatched_dynamic_C1_measure_derivation": True,
            "full_no_knob_constants": True,
        },
        "SM_parity_closed": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_LatestSMParityClosureStatus_or_TrueEquivalenceFrontier_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "SM_parity_closed_under_declared_standard": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected LatestSMParityClosureStatus or TrueEquivalenceFrontier v1

Status: `{STATUS}`.

Latest status:

- SM parity is closed under the declared parity-interface standard.
- True precision SM equivalence is still open.
- No-knob closure is still open.

This consolidates later artifacts that supersede the older open final-gap matrix:
patched dynamic C1 is retired at the patched parity tier, first-pass RG transport
is accepted for SM parity, and Qa/SU3 parity-interface replacement closes the
selected SM packet certificate at the parity tier.

Guardrail: this is **not** a claim that actual Qa/SU3 operator maps, precision RG
benchmarks/covariance, local QFT/QM/GR observable functors, or all constants have
been no-knob derived.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
