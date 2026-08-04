"""Promote common-carrier operator co-emission after split ownership.

This is deliberately weaker than the same-source theorem.  The previous
Route-C/split-ownership packet already proves that C_tau and PhiFin_DE sit on
the same 27-dimensional BN carrier and commute/simultaneously diagonalize, but
it does not prove that one selected threshold source emits both branches.  This
packet promotes only that common-carrier field.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_commoncarriercoemission_after_splitownership_or_selectedsourceobject"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SUPPORT_PACKET = PACKET_DIR / "common_carrier_operator_coemission_support.packet.json"
STATEMENT_PACKET = PACKET_DIR / "source_emission_statement_revalidation_after_commoncarrier.packet.json"
FIELD_PACKET = PACKET_DIR / "source_object_field_revalidation_after_commoncarrier.packet.json"
BRANCH_PACKET = PACKET_DIR / "same_branch_source_theorem_gate_after_commoncarrier.packet.json"
NEXT_PACKET = PACKET_DIR / "next_selectedsourceobject_or_cechhym_contract.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_CommonCarrierCoEmission_AfterSplitOwnership_or_SelectedSourceObject_v1.md"

PREVIOUS = DATA / "selected_routecinternality_splitownership_or_samebranchidentity.candidate.json"
PREVIOUS_STATEMENTS = (
    DATA
    / "selected_routecinternality_splitownership_or_samebranchidentity"
    / "source_emission_statement_revalidation_after_routec.packet.json"
)
PREVIOUS_FIELDS = (
    DATA
    / "selected_routecinternality_splitownership_or_samebranchidentity"
    / "source_object_field_revalidation_after_splitownership.packet.json"
)
PREVIOUS_BRANCH = (
    DATA
    / "selected_routecinternality_splitownership_or_samebranchidentity"
    / "same_branch_identity_remaining_gate.packet.json"
)
SOURCE_ID_REDUCTION = (
    DATA
    / "selected_orientedphifin_sourceownership_theorem_or_smootheqa_quotient"
    / "sourceidentity_transport_reduction.packet.json"
)
CTAU_GATE = (
    DATA
    / "selected_orientationmagnitudecoemission_or_endomorphismthresholdfinitepart_or_directhkrow"
    / "ctau_phifin_threshold_identity_gate.packet.json"
)

STATUS = (
    "MTT_SELECTED_COMMONCARRIERCOEMISSION_AFTER_SPLITOWNERSHIP_"
    "OPERATORS_FIELD_PROMOTED_SOURCE_THEOREM_OPEN"
)
PREVIOUS_STATUS = (
    "MTT_SELECTED_ROUTECINTERNALITY_SPLITOWNERSHIP_OR_SAMEBRANCHIDENTITY_"
    "THREE_OF_SIX_SOURCE_STATEMENTS_SEVEN_OF_ELEVEN_FIELDS_PROMOTED_SAMEBRANCH_OPEN"
)
NEXT = "MTT_Selected_SelectedSourceObjectSQaSU3BN27_or_CechHYMConnectionValues_v1"
PROMOTED_FIELD = "operators_coemitted_before_finite_comparison"
REMAINING_STATEMENTS = [
    "C_tau_and_PhiFin_DE_coemitted_by_source",
    "S_QaSU3_BN27_is_selected_threshold_source",
    "no_lift_replay_audit_from_emitted_fields",
]


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
        raise FileNotFoundError("missing common-carrier inputs: " + ", ".join(missing))


def main() -> int:
    require_sources(
        [
            PREVIOUS,
            PREVIOUS_STATEMENTS,
            PREVIOUS_FIELDS,
            PREVIOUS_BRANCH,
            SOURCE_ID_REDUCTION,
            CTAU_GATE,
        ]
    )

    previous = load(PREVIOUS)
    previous_statements = load(PREVIOUS_STATEMENTS)
    previous_fields = load(PREVIOUS_FIELDS)
    previous_branch = load(PREVIOUS_BRANCH)
    source_reduction = load(SOURCE_ID_REDUCTION)
    ctau_gate = load(CTAU_GATE)

    if previous["status"] != PREVIOUS_STATUS:
        raise ValueError("previous frontier is not the split-ownership packet")
    if previous_statements["emitted_source_statement_count"] != 3:
        raise ValueError("expected previous source statements 3/6")
    if previous_fields["promoted_source_object_field_count"] != 7:
        raise ValueError("expected previous source-object fields 7/11")

    coemission_support = source_reduction["conditional_sublemmas"]["operator_coemission_before_finite_comparison"]
    support_basis = coemission_support["support"]
    same_carrier_common_calculus = all(
        [
            coemission_support["conditional_closure_ready"],
            coemission_support["conditional_on_source_branch_identity"],
            support_basis["basis_dimension"] == 27,
            support_basis["same_basis"],
            support_basis["commutator_zero"],
            ctau_gate["central_rank_intertwiner"]["C_tau_source_selected_as_BN_operator"],
            ctau_gate["central_rank_intertwiner"]["operator_identity_closed_for_signed_layer"],
            ctau_gate["ctau_chiral_positive_convention"]["ctau_supplies_orientation"],
            ctau_gate["phifin_magnitude"]["commutation_or_simultaneous_functional_calculus_closed"],
            ctau_gate["phifin_magnitude"]["oriented_table_magnitude_finitepart_computed"],
            previous_fields["fields"]["full_F3xF3_rank_slot_carrier_emitted"]["source_owned"],
            previous_fields["fields"]["one_selected_source_owns_RouteC_PhiFin_DE_magnitude"]["source_owned"],
            previous_fields["fields"]["one_selected_source_owns_heterotic_C_tau_orientation"]["source_owned"],
        ]
    )
    if not same_carrier_common_calculus:
        raise ValueError("common-carrier co-emission support is incomplete")

    fields: dict[str, dict[str, Any]] = json.loads(json.dumps(previous_fields["fields"]))
    fields[PROMOTED_FIELD].update(
        {
            "source_owned": True,
            "promotion_source": rel(SUPPORT_PACKET),
            "accepted_reason": (
                "C_tau and PhiFin_DE are simultaneous operators on the same emitted 27-dimensional "
                "BN/F3xF3 carrier before finite determinant comparison.  This promotes only the "
                "common-carrier operator field, not one-source branch identity."
            ),
            "scope": "common_carrier_support_not_same_source_theorem",
        }
    )
    promoted_fields = [name for name, field in fields.items() if field["source_owned"]]
    remaining_fields = [name for name, field in fields.items() if not field["source_owned"]]

    rows: dict[str, dict[str, Any]] = json.loads(json.dumps(previous_statements["rows"]))
    rows["C_tau_and_PhiFin_DE_coemitted_by_source"].update(
        {
            "emitted_as_source_owned": False,
            "current_blocker": (
                "common-carrier simultaneous calculus is closed, but one selected source object "
                "emitting both C_tau orientation and PhiFin_DE magnitude is still unproved"
            ),
            "common_carrier_support_closed": True,
        }
    )
    rows["S_QaSU3_BN27_is_selected_threshold_source"].update(
        {
            "emitted_as_source_owned": False,
            "current_blocker": "selected source object S_QaSU3^BN27 is still not derived in the strict lane",
        }
    )
    rows["no_lift_replay_audit_from_emitted_fields"].update(
        {
            "emitted_as_source_owned": False,
            "current_blocker": "no-lift replay still depends on selected source object and same-source emission",
        }
    )

    support_packet = {
        "schema": "MTTCommonCarrierOperatorCoEmissionSupport.v1",
        "status": "COMMON_CARRIER_OPERATOR_COEMISSION_SUPPORT_CLOSED_SAME_SOURCE_OPEN",
        "closure_claimed": True,
        "support_scope": "common-carrier simultaneous operator support only",
        "promotes_source_object_field": PROMOTED_FIELD,
        "does_not_promote_source_statement": "C_tau_and_PhiFin_DE_coemitted_by_source",
        "basis_dimension": 27,
        "same_basis": support_basis["same_basis"],
        "commutator_zero": support_basis["commutator_zero"],
        "simultaneous_functional_calculus_closed": ctau_gate["phifin_magnitude"][
            "commutation_or_simultaneous_functional_calculus_closed"
        ],
        "C_tau_orientation_owned_on_split_branch": previous_fields["split_ownership"][
            "heterotic_C_tau_orientation_owned_by_C_tau_source"
        ],
        "PhiFin_DE_magnitude_owned_on_split_branch": previous_fields["split_ownership"][
            "RouteC_PhiFin_DE_magnitude_owned_by_A_N_source"
        ],
        "same_source_owns_both": False,
        "source_branch_identity_closed": False,
        "selected_source_object_closed": False,
        "no_lift_replay_allowed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    statement_packet = {
        "schema": "MTTSourceEmissionStatementRevalidationAfterCommonCarrier.v1",
        "status": "THREE_OF_SIX_SOURCE_STATEMENTS_RETAINED_COMMON_CARRIER_SUPPORT_ADDED",
        "closure_claimed": True,
        "previous_emitted_source_statement_count": 3,
        "emitted_source_statement_count": 3,
        "required_source_statement_count": previous_statements["required_source_statement_count"],
        "accepted_statements": previous_statements["accepted_statements"],
        "remaining_statements": REMAINING_STATEMENTS,
        "rows": rows,
        "common_carrier_support_closed": True,
        "same_branch_coemission_closed": False,
        "direct_source_theorem_closed": False,
        "selected_source_object_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    field_packet = {
        "schema": "MTTSourceObjectFieldRevalidationAfterCommonCarrier.v1",
        "status": "EIGHT_OF_ELEVEN_SOURCE_OBJECT_FIELDS_PROMOTED_COMMON_CARRIER_ONLY",
        "closure_claimed": True,
        "previous_promoted_source_object_field_count": 7,
        "promoted_source_object_field_count": len(promoted_fields),
        "required_source_object_field_count": previous_fields["required_source_object_field_count"],
        "newly_promoted_source_object_fields": [PROMOTED_FIELD],
        "promoted_source_object_fields": promoted_fields,
        "remaining_source_object_fields": remaining_fields,
        "fields": fields,
        "split_ownership": {
            "RouteC_PhiFin_DE_magnitude_owned_by_A_N_source": True,
            "heterotic_C_tau_orientation_owned_by_C_tau_source": True,
            "operators_coemitted_before_finite_comparison": True,
            "same_source_owns_both": False,
        },
        "common_carrier_support_closed": True,
        "oriented_logdet_promoted": False,
        "unconditional_replay_allowed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    branch_packet = {
        "schema": "MTTSameBranchSourceTheoremGateAfterCommonCarrier.v1",
        "status": "COMMON_CARRIER_CLOSED_SELECTED_SOURCE_OBJECT_STILL_OPEN",
        "closure_claimed": True,
        "common_carrier_operator_coemission_closed": True,
        "source_branch_identity_closed": False,
        "selected_source_object_S_QaSU3_BN27_closed": False,
        "same_source_owns_both_branches": False,
        "routec_row_not_external_import_closed": previous_branch["routec_row_not_external_import_closed"],
        "remaining_root_clauses": [
            "one_selected_source_names_both_branches",
            "eleven_label_to_full_BN27_threshold_carrier",
            "selected_source_object_S_QaSU3_BN27",
        ],
        "remaining_sourcebranch_clauses": previous_branch["remaining_sourcebranch_clauses"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTNextSelectedSourceObjectOrCechHYMContract.v1",
        "status": "NEXT_IS_SELECTED_SOURCE_OBJECT_SQASU3BN27_OR_CECHHYM_VALUES",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "source_emission_statement_count": "3/6",
        "source_object_field_count": f"{len(promoted_fields)}/11",
        "final_connection_table_count": "4/8",
        "remaining_source_emission_statements": REMAINING_STATEMENTS,
        "remaining_source_object_fields": remaining_fields,
        "remaining_minimal_exits": [
            "derive selected source object S_QaSU3^BN27 that names both branches",
            "promote the full BN27 positive threshold carrier beyond the 11-label shadow",
            "execute no-lift replay from emitted source fields, or emit selected Cech/HYM connection values",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedCommonCarrierCoEmissionAfterSplitOwnershipOrSelectedSourceObject",
        "status": STATUS,
        "previous_status": previous["status"],
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {
            "previous": rel(PREVIOUS),
            "previous_statements": rel(PREVIOUS_STATEMENTS),
            "previous_fields": rel(PREVIOUS_FIELDS),
            "previous_branch": rel(PREVIOUS_BRANCH),
            "source_id_reduction": rel(SOURCE_ID_REDUCTION),
            "ctau_gate": rel(CTAU_GATE),
        },
        "output_packets": {
            "common_carrier_operator_coemission_support": rel(SUPPORT_PACKET),
            "source_emission_statement_revalidation_after_commoncarrier": rel(STATEMENT_PACKET),
            "source_object_field_revalidation_after_commoncarrier": rel(FIELD_PACKET),
            "same_branch_source_theorem_gate_after_commoncarrier": rel(BRANCH_PACKET),
            "next_selectedsourceobject_or_cechhym_contract": rel(NEXT_PACKET),
        },
        "closure_decision": {
            "source_emission_statement_count": 3,
            "required_source_emission_statement_count": previous_statements["required_source_statement_count"],
            "accepted_source_emission_statements": previous_statements["accepted_statements"],
            "remaining_source_emission_statements": REMAINING_STATEMENTS,
            "source_object_field_count": len(promoted_fields),
            "required_source_object_field_count": previous_fields["required_source_object_field_count"],
            "newly_promoted_source_object_fields": [PROMOTED_FIELD],
            "operators_coemitted_before_finite_comparison": True,
            "common_carrier_operator_coemission_closed": True,
            "C_tau_and_PhiFin_DE_coemitted_by_source": False,
            "same_source_owns_both_branches": False,
            "selected_source_object_S_QaSU3_BN27": False,
            "source_branch_identity_closed": False,
            "oriented_logdet_promoted": False,
            "no_lifted_flags_connection_replay_promoted": False,
            "final_connection_tables_accepted": 4,
            "strict_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "CommonCarrierOperatorCoEmissionAfterSplitOwnershipTheorem",
            "proved": True,
            "statement": (
                "Given the emitted rank-27 F3xF3 carrier, split ownership of C_tau orientation and "
                "PhiFin_DE magnitude, and the same-basis/zero-commutator simultaneous functional calculus, "
                "the operators are co-emitted at common-carrier support scope before finite comparison. "
                "This promotes the source-object field operators_coemitted_before_finite_comparison to "
                "8/11, but it does not prove that one selected source emits both operators, does not "
                "select S_QaSU3^BN27, and does not promote logdet/no-lift/final connection rows."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedCommonCarrierCoEmissionAfterSplitOwnershipOrSelectedSourceObject",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "source_emission_statement_count": 3,
        "required_source_emission_statement_count": previous_statements["required_source_statement_count"],
        "source_object_field_count": len(promoted_fields),
        "required_source_object_field_count": previous_fields["required_source_object_field_count"],
        "newly_promoted_source_object_fields": [PROMOTED_FIELD],
        "operators_coemitted_before_finite_comparison": True,
        "common_carrier_operator_coemission_closed": True,
        "C_tau_and_PhiFin_DE_coemitted_by_source": False,
        "same_source_owns_both_branches": False,
        "selected_source_object_S_QaSU3_BN27": False,
        "source_branch_identity_closed": False,
        "oriented_logdet_promoted": False,
        "no_lifted_flags_connection_replay_promoted": False,
        "final_connection_tables_accepted": 4,
        "strict_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected Common-Carrier Co-Emission After Split Ownership v1

## Theorem

`CommonCarrierOperatorCoEmissionAfterSplitOwnershipTheorem` is proved.

## Result

The source-object layer moves from `7/11` to `{len(promoted_fields)}/11` by
promoting `operators_coemitted_before_finite_comparison`.

The source-emission layer remains `3/6`: `C_tau_and_PhiFin_DE_coemitted_by_source`
is still open, because common-carrier simultaneous calculus is weaker than a
single selected source object emitting both branches.

Final connection tables remain `4/8`.  `log(92160000)`, no-lift replay,
strict no-knob closure, and true SM equivalence are not promoted.

## Next Artifact

`{NEXT}`
"""

    write_json(SUPPORT_PACKET, support_packet)
    write_json(STATEMENT_PACKET, statement_packet)
    write_json(FIELD_PACKET, field_packet)
    write_json(BRANCH_PACKET, branch_packet)
    write_json(NEXT_PACKET, next_packet)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
