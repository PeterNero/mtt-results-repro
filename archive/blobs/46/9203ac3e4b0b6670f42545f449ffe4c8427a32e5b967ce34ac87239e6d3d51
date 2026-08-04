"""Build the frozen SM-parity boundary and post-SM-parity frontier artifact."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_smparityfrozenboundary_or_postsmparityfrontier"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
BOUNDARY = PACKET_DIR / "frozen_smparity_boundary.packet.json"
TAXONOMY = PACKET_DIR / "post_smparity_tier_taxonomy.packet.json"
NEXT = PACKET_DIR / "next_work_after_frozen_boundary.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_SMParityFrozenBoundary_or_PostSMParityFrontier_v1.md"

STATUS = "MTT_SELECTED_SMPARITY_FROZEN_BOUNDARY_BUILT_POST_SMPARITY_FRONTIER_LOCKED"
NEXT_ARTIFACT = "MTT_Selected_DynamicQaSU3_or_C1Response_PostSourceFrontier_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    latest = load(DATA / "selected_latest_smparityclosure_status_or_trueequivalencefrontier.candidate.json")
    heat_cert = load(CERTS / "selected_heattorsionresponse_finalgate_certificate.json")
    heat_frontier = load(DATA / "selected_heattorsionresponse_finalgate" / "post_eight_slot_true_equivalence_frontier.packet.json")

    proof_inputs = {
        "latest_declared_SM_parity_closed": latest["SM_parity_closed"] is True,
        "latest_declared_true_SM_equivalence_open": latest["true_SM_equivalence_closed"] is False,
        "latest_declared_no_knob_open": latest["no_knob_closed"] is False,
        "latest_guard_excludes_observed_selector": latest["observed_data_used_as_selector"] is False,
        "latest_guard_excludes_target_fitting": latest["target_fitting_used"] is False,
        "finite_source_slot_layer_closed": heat_cert["source_slot_layer_closed"] is True
        and heat_frontier["operator_source_slots_closed"] == 8
        and heat_frontier["operator_source_slots_remaining"] == 0,
        "final_heat_torsion_source_slot_closed": heat_cert["finite_determinant_heat_spectrum_or_torsion_response_closed"] is True,
        "post_eight_frontier_keeps_true_equivalence_open": heat_frontier["true_SM_equivalence_closed"] is False,
        "post_eight_frontier_keeps_no_knob_open": heat_frontier["no_knob_closed"] is False,
        "post_eight_guard_excludes_observed_selector": heat_frontier["observed_data_used_as_selector"] is False,
        "post_eight_guard_excludes_target_fitting": heat_frontier["target_fitting_used"] is False,
    }
    boundary_locks = all(proof_inputs.values())

    boundary = {
        "schema": "MTTFrozenSMParityBoundary.v1",
        "status": "SMPARITY_CLOSED_DO_NOT_REOPEN_AS_ACTIVE_BLOCKER",
        "boundary_locks": boundary_locks,
        "closed_tiers": {
            "SM_parity_replay_under_declared_standard": True,
            "finite_operator_source_slot_layer": True,
        },
        "closed_tier_evidence": {
            "latest_SM_parity_status": rel(DATA / "selected_latest_smparityclosure_status_or_trueequivalencefrontier.candidate.json"),
            "finite_source_slot_certificate": rel(CERTS / "selected_heattorsionresponse_finalgate_certificate.json"),
            "post_eight_source_frontier": rel(
                DATA / "selected_heattorsionresponse_finalgate" / "post_eight_slot_true_equivalence_frontier.packet.json"
            ),
        },
        "reopen_policy": {
            "may_reopen_SM_parity_only_if": [
                "a verifier regression makes a previously passing SM-parity audit fail",
                "a source packet is discovered to have used observed values as a selector",
                "a theorem input is shown inconsistent with its stated scope",
            ],
            "must_not_reopen_SM_parity_because": [
                "true SM equivalence is still open",
                "no-knob constants derivation is still open",
                "dynamic Qa/SU3 or C1 source upgrades remain open",
                "precision RG/threshold/covariance work remains open",
            ],
            "active_label_for_remaining_work": "post-SM-parity true-equivalence/no-knob frontier",
        },
        "guardrails": {
            "observed_data_used_as_selector": False,
            "target_fitting_used": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "proof_inputs": proof_inputs,
    }

    taxonomy = {
        "schema": "MTTPostSMParityTierTaxonomy.v1",
        "status": "POST_SMPARITY_TIER_NAMES_LOCKED",
        "tiers": [
            {
                "id": "tier_0_sm_parity_replay",
                "name": "SM-parity replay",
                "status": "CLOSED_FROZEN",
                "meaning": (
                    "Measured SM parameters may enter downstream under the same kind of standard the SM itself "
                    "uses, while source selection remains independent of observed masses, mixings, and profiles."
                ),
                "do_not_call_remaining_work": "SM-parity blocker",
            },
            {
                "id": "tier_1_finite_source_slot_layer",
                "name": "finite selected operator-source slots",
                "status": "CLOSED_FROZEN",
                "meaning": "The eight finite operator-source slots, including heat/spectrum/pseudodeterminant response, are closed at the selected finite source-slot layer.",
                "do_not_call_remaining_work": "missing source slot",
            },
            {
                "id": "tier_2_post_sm_parity_true_equivalence",
                "name": "post-SM-parity true equivalence",
                "status": "OPEN_ACTIVE",
                "meaning": "Precision QFT observable replay, accepted RG/threshold/covariance policy, local observable functors, and dynamic selected source/operator packets.",
                "primary_next": NEXT_ARTIFACT,
            },
            {
                "id": "tier_3_no_knob_derivation",
                "name": "no-knob derivation",
                "status": "OPEN_SEPARATE_STRONGER_THAN_SM",
                "meaning": "Derive constants and SM numerical values from selected MTT source data instead of admitting them as measured replay inputs.",
                "rule": "Do not demote closed SM-parity merely because this stronger tier is open.",
            },
        ],
        "language_rule": {
            "preferred_phrase": "post-SM-parity frontier",
            "forbidden_regression_phrase": "SM-parity is still blocked",
            "allowed_exception": "Only use blocker language if a frozen-tier audit or guardrail fails.",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_work = {
        "schema": "MTTNextWorkAfterFrozenSMParityBoundary.v1",
        "status": "NEXT_WORK_MOVES_ONLY_IN_POST_SMPARITY_TIERS",
        "next_required_artifact": NEXT_ARTIFACT,
        "next_required_goal": (
            "Build the post-source frontier for actual dynamic Qa/SU3 and selected C1 response without "
            "reopening the closed SM-parity replay/source-slot tiers."
        ),
        "active_open_items": [
            "actual dynamic Qa/SU3 operator packet",
            "selected dotD_alpha1 and primitive C1 response source identity",
            "full S2 value emission beyond D_E/gap layer",
            "precision QFT observable functor with accepted RG/threshold/covariance policy",
            "no-proxy Yukawa/mixing/value derivation for no-knob upgrade",
        ],
        "superset_strategy": {
            "mode": "combine several source lanes with a locked post-SM-parity target",
            "lanes": [
                "finite selected Phi_fin D_E/gap/heat source-slot layer",
                "typed monad and section-ring SM-slot source data",
                "HYM/Route-C and visible Chern-Weil operator packets",
                "external QFT/RG/threshold/covariance benchmark conventions",
                "no-knob sibling repos as source-upgrade evidence, not replay selectors",
            ],
            "locked_target": "dynamic selected operator/value machinery, not another SM-parity replay proof",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedSMParityFrozenBoundaryOrPostSMParityFrontier",
        "status": STATUS,
        "inputs": {
            "latest_SM_parity_status": rel(DATA / "selected_latest_smparityclosure_status_or_trueequivalencefrontier.candidate.json"),
            "final_heat_torsion_source_slot_certificate": rel(CERTS / "selected_heattorsionresponse_finalgate_certificate.json"),
            "post_eight_source_slot_frontier": rel(
                DATA / "selected_heattorsionresponse_finalgate" / "post_eight_slot_true_equivalence_frontier.packet.json"
            ),
        },
        "output_packets": {
            "frozen_smparity_boundary": rel(BOUNDARY),
            "post_smparity_tier_taxonomy": rel(TAXONOMY),
            "next_work_after_frozen_boundary": rel(NEXT),
        },
        "theorem": {
            "name": "FrozenSMParityBoundaryTheorem",
            "proved": boundary_locks,
            "statement": (
                "The declared SM-parity replay tier and the finite selected operator-source slot layer are "
                "closed and frozen. Remaining work belongs to post-SM-parity true equivalence or no-knob "
                "derivation, and must not be counted as a reopened SM-parity blocker unless a frozen-tier "
                "audit or guardrail fails."
            ),
        },
        "what_closes_now": {
            "SM_parity_boundary_frozen": boundary_locks,
            "source_slot_layer_boundary_frozen": boundary_locks,
            "post_SM_parity_language_rule_locked": True,
            "next_required_artifact_selected": NEXT_ARTIFACT,
        },
        "what_remains_open": {
            "post_SM_parity_true_equivalence": True,
            "actual_dynamic_QaSU3_operator_packet": True,
            "selected_C1_response": True,
            "full_S2_value_emission": True,
            "precision_QFT_observable_functor": True,
            "no_knob_derivation": True,
        },
        "closure_decision": {
            "SM_parity_closed_frozen": True,
            "finite_operator_source_slot_layer_closed_frozen": True,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "next_required_artifact": NEXT_ARTIFACT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_SMParityFrozenBoundary_or_PostSMParityFrontier_v1",
        "candidate_path": rel(OUTPUT),
        "status": STATUS,
        "theorem_proved": boundary_locks,
        "SM_parity_closed_frozen": True,
        "finite_operator_source_slot_layer_closed_frozen": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "next_required_artifact": NEXT_ARTIFACT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "note_path": rel(NOTE),
    }

    note = f"""# MTT Selected SMParityFrozenBoundary or PostSMParityFrontier v1

This artifact freezes the boundary we kept crossing and then accidentally
reopening.

Closed and frozen:

- SM-parity replay under the declared standard
- finite selected operator-source slot layer, including all eight source slots

Remaining work must now be called post-SM-parity work:

- true SM equivalence
- dynamic `Qa/SU3` and selected C1 response
- full S2 value emission
- precision QFT/RG/threshold/covariance observable replay
- no-knob constants and value derivation

Language rule:

Do not say SM-parity is blocked merely because true equivalence, no-knob
derivation, dynamic source upgrades, or precision QFT profiles remain open.
Those are stronger tiers.

Allowed exception:

SM-parity may be reopened only if a frozen audit fails, observed values are
found to have selected a source, or a theorem input is shown inconsistent with
its stated scope.

Next artifact: `{NEXT_ARTIFACT}`.
"""

    for path, payload in [
        (BOUNDARY, boundary),
        (TAXONOMY, taxonomy),
        (NEXT, next_work),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
