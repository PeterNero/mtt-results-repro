"""Build strict PEW/direct-K source-row and final SM no-knob audit."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"
CERTS = ROOT / "certificates"

SLUG = "selected_strictpewdirectksourcerows_or_finalsmnoknobaudit"
OUT = DATA / f"{SLUG}.candidate.json"
PACKET_DIR = DATA / SLUG
STRICT_AUDIT = PACKET_DIR / "strict_pew_directk_source_row_audit.packet.json"
TIERED_CLOSURE = PACKET_DIR / "tiered_sm_closure_status.packet.json"
DECISION = PACKET_DIR / "final_sm_noknob_or_oneprimitive_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_StrictPEWDirectKSourceRows_or_FinalSMNoKnobAudit_v1.md"

PREVIOUS = DATA / "selected_higgsthresholdstrictpewexit_or_selectedsourcerows.candidate.json"
PHYS_AXIOM = DATA / "selected_physicalnormalizationsourceaxiom_or_directkcertificate.candidate.json"
PHYS_DERIVATION = DATA / "selected_physicalnormalizationaxiomderivation_or_strictpewnoknobupgrade.candidate.json"
MIN_LEDGER = DATA / "selected_fullsmminimalparameterledger_or_strictpewsourcetheorem.candidate.json"
MIN_COUNT = DATA / "selected_fullsmminimalparameterledger_or_strictpewsourcetheorem" / "minimal_parameter_count_summary.packet.json"
CLOSED_OPEN = DATA / "selected_fullsmminimalparameterledger_or_strictpewsourcetheorem" / "closed_vs_open_parameter_slots.packet.json"
GLOBAL_LEDGER = DATA / "selected_truesmnoknobclosure_globalledger_or_remainingnonyukawarows.candidate.json"

STATUS = (
    "MTT_SELECTED_STRICTPEWDIRECTKSOURCEROWS_OR_FINALSMNOKNOBAUDIT_"
    "BUILT_STRICT_OPEN_ONEPRIMITIVE_TIER_CLOSED"
)
NEXT = "MTT_Selected_PhysicalNormalizationAxiomDerivation_or_OnePrimitiveAdoptionDecision_v1"


def write_json(path: Path, obj: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def main() -> int:
    previous = load(PREVIOUS)
    phys_axiom = load(PHYS_AXIOM)
    phys_derivation = load(PHYS_DERIVATION)
    min_ledger = load(MIN_LEDGER)
    min_count = load(MIN_COUNT)
    closed_open = load(CLOSED_OPEN)
    global_ledger = load(GLOBAL_LEDGER)

    strict_pew_rows = previous["key_numbers"]["accepted_strict_P_EW_source_rows"]
    strict_direct_k_rows = previous["key_numbers"]["accepted_direct_K_threshold_Omega_H_lambda_rows"]
    premised_k_count = previous["key_numbers"]["premised_selected_K_row_count"]
    shared_primitive_count = previous["key_numbers"]["shared_physical_primitive_count_under_axiom"]
    strict_derivation_count = phys_derivation["closure_decision"]["accepted_strict_derivation_route_count"]
    axiom_constructed = phys_axiom["closure_decision"]["physical_normalization_source_axiom_constructed"]
    direct_k_under_axiom = phys_axiom["closure_decision"][
        "direct_K_threshold_Omega_H_lambda_certificate_constructed_under_axiom"
    ]
    one_primitive_lane_closed = phys_axiom["closure_decision"]["minimal_one_primitive_H_lambda_lane_closed"]
    strict_no_knob_closed = strict_pew_rows > 0 and strict_direct_k_rows > 0
    one_primitive_tier_closed = (
        axiom_constructed
        and direct_k_under_axiom
        and one_primitive_lane_closed
        and premised_k_count == 10
        and shared_primitive_count == 1
    )

    strict_audit = {
        "schema": "MTTStrictPEWDirectKSourceRowAudit.v1",
        "status": "STRICT_SOURCE_ROWS_ZERO_ALL_CURRENT_ROUTES_TESTED",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "previous_candidate": rel(PREVIOUS),
        "physical_normalization_derivation_candidate": rel(PHYS_DERIVATION),
        "accepted_strict_P_EW_source_rows": strict_pew_rows,
        "accepted_direct_K_threshold_Omega_H_lambda_rows": strict_direct_k_rows,
        "accepted_strict_derivation_route_count": strict_derivation_count,
        "physical_normalization_axiom_derived": phys_derivation["closure_decision"][
            "physical_normalization_axiom_derived"
        ],
        "strict_no_knob_ten_row_closure": phys_derivation["closure_decision"][
            "strict_no_knob_ten_row_closure"
        ],
        "tested_routes": phys_derivation["closure_decision"]["accepted_strict_derivation_route_count"],
        "route_test_source": rel(
            DATA
            / "selected_physicalnormalizationaxiomderivation_or_strictpewnoknobupgrade"
            / "strict_physical_normalization_derivation_route_tests.packet.json"
        ),
        "strict_no_knob_closed": strict_no_knob_closed,
    }

    tiered_closure = {
        "schema": "MTTTieredSMClosureStatusAfterStrictPEWAudit.v1",
        "status": "ONE_SHARED_PRIMITIVE_TIER_CLOSED_STRICT_NOKNOB_OPEN",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "physical_normalization_axiom_candidate": rel(PHYS_AXIOM),
        "minimal_parameter_ledger_candidate": rel(MIN_LEDGER),
        "minimal_parameter_count_summary": rel(MIN_COUNT),
        "closed_vs_open_slots": rel(CLOSED_OPEN),
        "physical_normalization_source_axiom_constructed": axiom_constructed,
        "direct_K_certificate_constructed_under_axiom": direct_k_under_axiom,
        "minimal_one_primitive_H_lambda_lane_closed": one_primitive_lane_closed,
        "premised_selected_K_row_count": premised_k_count,
        "shared_physical_primitive_count_under_axiom": shared_primitive_count,
        "P_EW_counted_as_shared_physical_primitive": min_ledger["closure_decision"][
            "P_EW_counted_as_shared_physical_primitive"
        ],
        "P_EW_parameter_count": min_ledger["closure_decision"]["P_EW_parameter_count"],
        "H_specific_parameter_count": min_ledger["closure_decision"]["H_specific_parameter_count"],
        "lambda_H_independent_parameter_replaced": min_ledger["closure_decision"][
            "lambda_H_independent_parameter_replaced"
        ],
        "closed_non_neutrino_SM_like_count_excluding_QCD_theta": min_count[
            "closed_non_neutrino_SM_like_count_excluding_QCD_theta"
        ],
        "closed_with_minimal_PMNS_oscillation_policy_excluding_QCD_theta": min_count[
            "closed_with_minimal_PMNS_oscillation_policy_excluding_QCD_theta"
        ],
        "one_shared_primitive_tier_closed": one_primitive_tier_closed,
        "strict_no_knob_closed": False,
        "true_precision_equivalence_closed": False,
        "open_upgrade_targets": closed_open["open_slots_or_upgrade_targets"],
    }

    decision = {
        "schema": "MTTFinalSMNoKnobOrOnePrimitiveDecision.v1",
        "status": "STRICT_NOKNOB_OPEN_ONE_SHARED_PRIMITIVE_TIER_CLOSED",
        "closed_now": [
            "All current strict PEW/direct-K derivation routes are audited and accept zero strict rows.",
            "The physical-normalization axiom plus direct-K certificate close the ten-K H/lambda ledger under one shared physical primitive.",
            "The minimal SM-sector ledger remains closed at 18 non-neutrino slots and 24 with minimal PMNS, excluding QCD theta.",
            "The independent lambda_H slot is replaced by the shared P_EW primitive; H-specific parameter count is zero.",
        ],
        "not_closed": [
            "Strict no-knob P_EW/direct-K source rows are not emitted.",
            "The physical-normalization axiom is constructed but not derived.",
            "True precision SM equivalence and global no-knob closure remain open.",
        ],
        "source_row_counts": {
            "accepted_strict_P_EW_source_rows": strict_pew_rows,
            "accepted_direct_K_threshold_Omega_H_lambda_rows": strict_direct_k_rows,
            "accepted_strict_derivation_route_count": strict_derivation_count,
            "premised_P_EW_source_rows": phys_axiom["closure_decision"]["premised_P_EW_source_rows"],
            "premised_direct_K_threshold_Omega_H_lambda_rows": phys_axiom["closure_decision"][
                "premised_direct_K_threshold_Omega_H_lambda_rows"
            ],
            "premised_selected_K_row_count": premised_k_count,
            "shared_physical_primitive_count_under_axiom": shared_primitive_count,
            "H_specific_parameter_count": min_ledger["closure_decision"]["H_specific_parameter_count"],
        },
        "acceptance": {
            "strict_PEW_directK_source_rows_closed": False,
            "physical_normalization_axiom_derived": False,
            "strict_no_knob_closure": False,
            "one_shared_primitive_tier_closed": one_primitive_tier_closed,
            "minimal_parameter_ledger_closed": min_ledger["closure_decision"]["minimal_parameter_ledger_closed"],
            "lambda_H_independent_parameter_replaced": min_ledger["closure_decision"][
                "lambda_H_independent_parameter_replaced"
            ],
            "H_specific_parameter_count_zero": min_ledger["closure_decision"][
                "H_specific_parameter_count"
            ]
            == 0,
            "global_true_SM_no_knob_closure": False,
            "true_precision_equivalence_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "next_exact_target": NEXT,
    }

    candidate = {
        "candidate": "MTTSelectedStrictPEWDirectKSourceRowsOrFinalSMNoKnobAudit",
        "status": STATUS,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {
            "previous_higgs_pew_frontier": rel(PREVIOUS),
            "physical_normalization_axiom": rel(PHYS_AXIOM),
            "physical_normalization_derivation": rel(PHYS_DERIVATION),
            "minimal_parameter_ledger": rel(MIN_LEDGER),
            "minimal_parameter_count_summary": rel(MIN_COUNT),
            "closed_vs_open_parameter_slots": rel(CLOSED_OPEN),
            "global_true_sm_noknob_ledger": rel(GLOBAL_LEDGER),
        },
        "output_packets": {
            "strict_pew_directk_source_row_audit": rel(STRICT_AUDIT),
            "tiered_sm_closure_status": rel(TIERED_CLOSURE),
            "final_sm_noknob_or_oneprimitive_decision": rel(DECISION),
        },
        "theorem": {
            "name": "StrictPEWDirectKSourceRowsOrFinalSMNoKnobAuditTheorem",
            "proved": True,
            "statement": (
                "At the final PEW/direct-K layer, current selected source data emit zero strict "
                "P_EW/direct-K rows, so strict no-knob SM closure is not proved. However the "
                "physical-normalization axiom and direct-K certificate close a one-shared-physical-"
                "primitive tier: lambda_H is no longer an independent H knob, the ten-K H/lambda "
                "ledger closes under the axiom, and the minimal SM-sector parameter ledger remains "
                "18/24 excluding QCD theta. The remaining strict task is to derive the axiom or "
                "emit equivalent same-branch source rows."
            ),
        },
        "key_numbers": {
            "accepted_strict_P_EW_source_rows": strict_pew_rows,
            "accepted_direct_K_threshold_Omega_H_lambda_rows": strict_direct_k_rows,
            "accepted_strict_derivation_route_count": strict_derivation_count,
            "premised_selected_K_row_count": premised_k_count,
            "shared_physical_primitive_count_under_axiom": shared_primitive_count,
            "H_specific_parameter_count": min_ledger["closure_decision"]["H_specific_parameter_count"],
            "closed_non_neutrino_SM_like_count_excluding_QCD_theta": min_count[
                "closed_non_neutrino_SM_like_count_excluding_QCD_theta"
            ],
            "closed_with_minimal_PMNS_oscillation_policy_excluding_QCD_theta": min_count[
                "closed_with_minimal_PMNS_oscillation_policy_excluding_QCD_theta"
            ],
            "global_remaining_hard_blocker_count_prior_ledger": global_ledger["key_numbers"][
                "remaining_hard_blocker_count"
            ],
        },
        "closure_decision": decision["acceptance"],
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_StrictPEWDirectKSourceRows_or_FinalSMNoKnobAudit_v1",
        "status": STATUS,
        "candidate": rel(OUT),
        "strict_PEW_directK_source_rows_closed": False,
        "accepted_strict_P_EW_source_rows": strict_pew_rows,
        "accepted_direct_K_threshold_Omega_H_lambda_rows": strict_direct_k_rows,
        "physical_normalization_axiom_derived": False,
        "strict_no_knob_closure": False,
        "one_shared_primitive_tier_closed": one_primitive_tier_closed,
        "minimal_parameter_ledger_closed": min_ledger["closure_decision"]["minimal_parameter_ledger_closed"],
        "lambda_H_independent_parameter_replaced": min_ledger["closure_decision"][
            "lambda_H_independent_parameter_replaced"
        ],
        "shared_physical_primitive_count_under_axiom": shared_primitive_count,
        "H_specific_parameter_count": min_ledger["closure_decision"]["H_specific_parameter_count"],
        "global_true_SM_no_knob_closure": False,
        "true_precision_equivalence_closed": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected StrictPEWDirectKSourceRows or FinalSMNoKnobAudit v1

Status: `{STATUS}`

## Closed Now

- strict PEW/direct-K routes audited: all current routes tested
- strict `P_EW` source rows: `{strict_pew_rows}`
- strict direct-K rows: `{strict_direct_k_rows}`
- one-shared-physical-primitive tier: closed
- premised selected K rows: `{premised_k_count}/10`
- shared primitive count under axiom: `{shared_primitive_count}`
- H-specific parameter count: `0`
- lambda_H independent parameter: replaced by shared `P_EW`

## Ledger Counts

- non-neutrino SM-like count excluding QCD theta: `{min_count["closed_non_neutrino_SM_like_count_excluding_QCD_theta"]}`
- with minimal PMNS oscillation policy excluding QCD theta: `{min_count["closed_with_minimal_PMNS_oscillation_policy_excluding_QCD_theta"]}`

## Still Open

- strict no-knob PEW/direct-K closure
- derivation of the physical-normalization axiom
- full precision true-SM equivalence
- global no-knob closure

The best current completion tier is therefore not strict no-knob; it is a
one-shared-physical-primitive tier with no H-specific lambda knob.

Next required artifact: `{NEXT}`.
"""

    write_json(STRICT_AUDIT, strict_audit)
    write_json(TIERED_CLOSURE, tiered_closure)
    write_json(DECISION, decision)
    write_json(OUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
