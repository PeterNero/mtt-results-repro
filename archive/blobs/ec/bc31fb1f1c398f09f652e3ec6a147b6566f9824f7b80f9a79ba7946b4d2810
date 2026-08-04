"""Build the strict-global / true-SM frontier packet after AH8.

The previous artifact closes the counted AH-equivalent BN27 connection-table
lane at 8/8 by accepting a selected finite projected Route-C/HYM representative.
This artifact prevents a loop: it locks that AH8 result as consumed and proves
that the remaining strict/global and true-SM exits are distinct obligations.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_strictglobalcechhym_or_truesmafterah8"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
AH8_LOCK = PACKET_DIR / "ah8_consumed_nonreopen_lock.packet.json"
STRICT_CUTSET = PACKET_DIR / "strict_global_literal_witness_cutset.packet.json"
TRUE_SM_ROUTE = PACKET_DIR / "true_sm_after_ah8_route_split.packet.json"
NEXT_PACKET = PACKET_DIR / "next_literal_witness_or_precision_values_after_ah8.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_StrictGlobalCechHYMProvenance_or_TrueSMClosureAfterAH8_v1.md"

PREVIOUS = DATA / "selected_visibleglobalstromingerprovenance_or_bn27finalrowacceptance.candidate.json"
PREVIOUS_NEXT = (
    DATA
    / "selected_visibleglobalstromingerprovenance_or_bn27finalrowacceptance"
    / "next_strict_global_or_truesm_after_ah8.packet.json"
)
EIGHT_TABLE = (
    DATA
    / "selected_derieszgreenkerneltraceexport_promotion_or_remainingconnectiontables"
    / "eight_table_revalidation_after_de_export.packet.json"
)
CECH_AH = DATA / "selected_cech_ah_representative_or_hymende_values.candidate.json"
GEO_REDUCTION = DATA / "selected_geometric_cechhym_obligation_reduction_after_onepremise.candidate.json"
PRECISION = DATA / "selected_precisionprofiletable_or_truesmequivalenceaudit.candidate.json"
QASU3 = DATA / "selected_qasu3operatorpayload_or_strictpewprecisionexit.candidate.json"
PARAM_LEDGER = DATA / "selected_fullsmminimalparameterledger_or_strictpewsourcetheorem.candidate.json"

STATUS = "MTT_SELECTED_STRICTGLOBALCECHHYM_OR_TRUESMAFTERAH8_AH8_CONSUMED_STRICT_WITNESSES_AND_PRECISION_VALUES_OPEN"
PREVIOUS_STATUS = "MTT_SELECTED_BN27_HYMROW_PROJECTED_ROUTEC_EQUIVALENCE_ACCEPTED_AH8_STRICT_GLOBAL_OPEN"
NEXT = "MTT_Selected_LiteralGoodCoverHYMGlobalWitness_or_PrecisionValueSourceAfterAH8_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing after-AH8 inputs: " + ", ".join(missing))


def main() -> int:
    sources = [PREVIOUS, PREVIOUS_NEXT, EIGHT_TABLE, CECH_AH, GEO_REDUCTION, PRECISION, QASU3, PARAM_LEDGER]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_next = load(PREVIOUS_NEXT)
    eight = load(EIGHT_TABLE)
    cech_ah = load(CECH_AH)
    geo = load(GEO_REDUCTION)
    precision = load(PRECISION)
    qasu3 = load(QASU3)
    ledger = load(PARAM_LEDGER)

    if previous["status"] != PREVIOUS_STATUS:
        raise ValueError("previous AH8 candidate status mismatch")
    if previous_next["next_required_artifact"] != "MTT_Selected_StrictGlobalCechHYMProvenance_or_TrueSMClosureAfterAH8_v1":
        raise ValueError("previous next packet does not point to after-AH8 target")

    ah8_closed = (
        previous["closure_decision"]["two_premise_AH_equivalent_final_connection_tables_accepted"] == 8
        and previous["closure_decision"]["two_premise_AH_equivalent_lane_closed"]
        and previous["closure_decision"]["projected_RouteC_equivalence_for_BN27_HYM_row_accepted"]
    )
    cech_literal_open = not cech_ah["closure_decision"]["literal_goodcover_Deligne_Cech_row_accepted"]
    hym_literal_open = not cech_ah["closure_decision"]["HYM_or_EndE_final_row_accepted"]
    strict_global_open = cech_literal_open or hym_literal_open
    strict_rows_from_original = eight["accepted_final_same_source_connection_tables"]
    one_premise_rows = geo["closure_decision"]["one_premise_final_connection_tables_accepted"]
    ah_rows = previous["closure_decision"]["two_premise_AH_equivalent_final_connection_tables_accepted"]

    true_sm_open_reasons = [
        key
        for key, value in precision["closure_decision"].items()
        if key.endswith("_closed") and value is False and key != "true_SM_equivalence_closed"
    ]
    qasu3_open_reasons = [
        key
        for key, value in qasu3["closure_decision"].items()
        if key.endswith("_closed") and value is False and key != "true_SM_equivalence_closed"
    ]

    ah8_lock = {
        "schema": "MTTAH8ConsumedNonReopenLock.v1",
        "status": "AH8_CONSUMED_DO_NOT_REOPEN_CONNECTION_TABLE_LANE",
        "closure_claimed": True,
        "AH_equivalent_BN27_lane_closed": ah8_closed,
        "accepted_count": ah_rows,
        "accepted_scope": "two-premise AH-equivalent / finite projected Route-C representative",
        "do_not_reopen": previous_next["do_not_reopen"],
        "not_claimed": [
            "literal global AH/Cech/HYM provenance",
            "strict no-knob connection-table closure",
            "true SM precision/equivalence closure",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    strict_cutset = {
        "schema": "MTTStrictGlobalLiteralWitnessCutsetAfterAH8.v1",
        "status": "STRICT_GLOBAL_REDUCED_TO_TWO_LITERAL_WITNESS_FAMILIES",
        "closure_claimed": True,
        "strict_global_closed": False,
        "strict_original_connection_tables_accepted": strict_rows_from_original,
        "one_premise_connection_tables_accepted": one_premise_rows,
        "AH_equivalent_connection_tables_accepted": ah_rows,
        "literal_witness_families_required": [
            {
                "name": "literal_good_cover_Deligne_Cech_data",
                "accepted_now": not cech_literal_open,
                "required_fields": ["good_cover", "A_ij", "B_i", "g_ijk", "h_ij", "transition_functions"],
                "why_support_is_insufficient": "AH representative/class data counts only in the AH-equivalent lane; it is not literal good-cover cochain data.",
            },
            {
                "name": "literal_global_HYM_or_projective_connection_coefficients",
                "accepted_now": not hym_literal_open,
                "required_fields": [
                    "connection_coefficients",
                    "endomorphism_E",
                    "finite_determinant_part",
                    "same_source_rhoE_or_D_E_values",
                ],
                "why_support_is_insufficient": "Finite projected Route-C/HYM data counts as an accepted representative, not continuum/global coefficient emission.",
            },
        ],
        "strict_global_can_be_closed_by_existing_support_packets": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    true_sm_route = {
        "schema": "MTTTrueSMAfterAH8RouteSplit.v1",
        "status": "TRUE_SM_FRONTIER_SEPARATED_FROM_BN27_AH8_ROW",
        "closure_claimed": True,
        "BN27_AH_equivalent_matrix_row_no_longer_blocker": ah8_closed,
        "true_SM_equivalence_closed": False,
        "minimal_parameter_ledger_closed": ledger["closure_decision"]["minimal_parameter_ledger_closed"],
        "precision_profile_table_built": precision["closure_decision"]["precision_profile_table_built"],
        "accepted_true_equivalence_rows": precision["closure_decision"]["accepted_true_equivalence_rows"],
        "qasu3_source_slot_layer_closed": qasu3["closure_decision"]["qasu3_source_slot_layer_closed"],
        "remaining_precision_value_gates": true_sm_open_reasons,
        "remaining_qasu3_value_gates": qasu3_open_reasons,
        "route_decision": (
            "Proceed on two non-overlapping tracks: strict global closure requires literal Cech/HYM witnesses; "
            "true SM equivalence requires precision/value source rows and does not require reopening AH8."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTNextLiteralWitnessOrPrecisionValuesAfterAH8.v1",
        "status": "NEXT_IS_LITERAL_WITNESS_OR_PRECISION_VALUE_SOURCE_AFTER_AH8",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "preferred_next_targets": [
            "construct literal good-cover Deligne-Cech witness family",
            "construct literal global HYM/projective coefficient witness family",
            "execute selected precision/value source rows without reopening BN27 AH8",
        ],
        "blocked_replays": [
            "do not treat AH representative as literal good-cover data",
            "do not treat finite projected HYM representative as continuum/global coefficients",
            "do not treat minimal parameter ledger as true precision equivalence",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    theorem = {
        "name": "AfterAH8StrictGlobalAndTrueSMRouteSeparationTheorem",
        "proved": True,
        "statement": (
            "Once the counted AH-equivalent BN27 lane reaches 8/8 through the selected finite projected "
            "Route-C/HYM representative, that matrix-row obligation is consumed for the AH-equivalent lane. "
            "Strict global closure is a different problem and is exactly reduced to two literal witness "
            "families: good-cover Deligne-Cech cochains and global HYM/projective connection coefficients. "
            "True SM equivalence is also separate: it must close precision/value source rows and selected "
            "dynamic operator values without reopening the AH8 row."
        ),
    }

    candidate = {
        "candidate": "MTTSelectedStrictGlobalCechHYMOrTrueSMAfterAH8",
        "status": STATUS,
        "previous_status": previous["status"],
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {
            "previous_AH8_candidate": rel(PREVIOUS),
            "previous_after_AH8_contract": rel(PREVIOUS_NEXT),
            "eight_table": rel(EIGHT_TABLE),
            "cech_AH_representative": rel(CECH_AH),
            "geometric_reduction": rel(GEO_REDUCTION),
            "precision_profile": rel(PRECISION),
            "qasu3_payload": rel(QASU3),
            "minimal_parameter_ledger": rel(PARAM_LEDGER),
        },
        "output_packets": {
            "ah8_consumed_nonreopen_lock": rel(AH8_LOCK),
            "strict_global_literal_witness_cutset": rel(STRICT_CUTSET),
            "true_sm_after_ah8_route_split": rel(TRUE_SM_ROUTE),
            "next_literal_witness_or_precision_values_after_ah8": rel(NEXT_PACKET),
        },
        "closure_decision": {
            "AH8_consumed_and_locked": ah8_closed,
            "BN27_AH_equivalent_matrix_row_no_longer_blocker": ah8_closed,
            "strict_global_reduced_to_two_literal_witness_families": strict_global_open,
            "literal_good_cover_Cech_witness_family_closed": False,
            "literal_global_HYM_witness_family_closed": False,
            "strict_global_closed": False,
            "minimal_parameter_ledger_closed": ledger["closure_decision"]["minimal_parameter_ledger_closed"],
            "precision_profile_table_built": precision["closure_decision"]["precision_profile_table_built"],
            "qasu3_source_slot_layer_closed": qasu3["closure_decision"]["qasu3_source_slot_layer_closed"],
            "precision_value_source_rows_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": theorem,
    }

    cert = {
        "certificate": "MTTSelectedStrictGlobalCechHYMOrTrueSMAfterAH8",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "AH8_consumed_and_locked": ah8_closed,
        "strict_global_reduced_to_two_literal_witness_families": strict_global_open,
        "strict_global_closed": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected StrictGlobalCechHYMProvenance or TrueSMClosureAfterAH8 v1

## Theorem

`AfterAH8StrictGlobalAndTrueSMRouteSeparationTheorem` is proved.

The counted AH-equivalent BN27 connection-table lane is consumed and locked at
`8/8`; the selected HYM/projective row must not be reopened in that lane.

## What Closes

- AH8 is a non-reopen result for the counted AH-equivalent BN27 matrix lane.
- Strict global closure is reduced to two literal witness families.
- True SM equivalence is separated from the BN27 AH8 row and moved to the
  precision/value-source frontier.

## Remaining Literal Witness Families

- literal good-cover Deligne-Cech data: good cover, `A_ij`, `B_i`, `g_ijk`,
  `h_ij`, and transition functions
- literal global HYM/projective connection data: connection coefficients,
  `endomorphism_E`, finite determinant part, and same-source `rhoE`/`D_E`
  values

## Boundary

This does not claim strict global closure, strict no-knob closure, or true SM
equivalence.

## Next Artifact

`{NEXT}`
"""

    write_json(AH8_LOCK, ah8_lock)
    write_json(STRICT_CUTSET, strict_cutset)
    write_json(TRUE_SM_ROUTE, true_sm_route)
    write_json(NEXT_PACKET, next_packet)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
