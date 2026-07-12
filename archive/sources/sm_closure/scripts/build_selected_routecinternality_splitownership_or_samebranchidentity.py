"""Promote Route-C internality and split C_tau/PhiFin ownership.

This is the next narrow step after A_N made the finite carrier/kernel/trace
policy source-owned.  It does not assert same-source branch identity; it only
separates the facts that are now owned on their respective branches.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_routecinternality_splitownership_or_samebranchidentity"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
STATEMENT_PACKET = PACKET_DIR / "source_emission_statement_revalidation_after_routec.packet.json"
FIELD_PACKET = PACKET_DIR / "source_object_field_revalidation_after_splitownership.packet.json"
BRANCH_PACKET = PACKET_DIR / "same_branch_identity_remaining_gate.packet.json"
NEXT_PACKET = PACKET_DIR / "next_samebranch_or_cechhym_contract.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_RouteCInternality_SplitOwnership_or_SameBranchIdentity_v1.md"

PREVIOUS = DATA / "selected_sourceemissionstatementpromotion_after_anpolicy.candidate.json"
PREVIOUS_STATEMENTS = (
    DATA
    / "selected_sourceemissionstatementpromotion_after_anpolicy"
    / "source_emission_statement_revalidation.packet.json"
)
PREVIOUS_FIELDS = (
    DATA
    / "selected_sourceemissionstatementpromotion_after_anpolicy"
    / "source_object_field_revalidation_after_an_policy.packet.json"
)
AN_POLICY = DATA / "selected_finitepartkernelpolicy_on_an_or_sourcebranchidentity" / "an_finitepart_kernel_policy.packet.json"
DE_EXPORT = (
    DATA
    / "selected_derieszgreenkerneltraceexport_promotion_or_remainingconnectiontables"
    / "de_gap_export_row_reconciliation.packet.json"
)
CTAU_GATE = (
    DATA
    / "selected_orientationmagnitudecoemission_or_endomorphismthresholdfinitepart_or_directhkrow"
    / "ctau_phifin_threshold_identity_gate.packet.json"
)
EXACT_VALUES = (
    DATA
    / "selected_torsionalweitzenbockendomorphism_or_ouweightssourcederivation"
    / "exact_oriented_finitepart_values.packet.json"
)
BRANCH_NOGO = (
    DATA
    / "selected_orientedphifin_sourceownership_theorem_or_smootheqa_quotient"
    / "sourcebranchidentity_current_source_nogo.packet.json"
)
SOURCE_ID_REDUCTION = (
    DATA
    / "selected_orientedphifin_sourceownership_theorem_or_smootheqa_quotient"
    / "sourceidentity_transport_reduction.packet.json"
)

STATUS = (
    "MTT_SELECTED_ROUTECINTERNALITY_SPLITOWNERSHIP_OR_SAMEBRANCHIDENTITY_"
    "THREE_OF_SIX_SOURCE_STATEMENTS_SEVEN_OF_ELEVEN_FIELDS_PROMOTED_SAMEBRANCH_OPEN"
)
NEXT = "MTT_Selected_CTauPhiFinSameBranchCoEmission_or_CechHYMConnectionValues_v1"

ACCEPTED_STATEMENTS = [
    "full_F3xF3_carrier_emitted_before_finite_comparison",
    "kernel_and_trace_policies_source_owned",
    "RouteC_row_internal_not_external",
]
REMAINING_STATEMENTS = [
    "C_tau_and_PhiFin_DE_coemitted_by_source",
    "S_QaSU3_BN27_is_selected_threshold_source",
    "no_lift_replay_audit_from_emitted_fields",
]
NEW_FIELDS = [
    "RouteC_row_internal_theorem_not_external_import",
    "one_selected_source_owns_RouteC_PhiFin_DE_magnitude",
    "one_selected_source_owns_heterotic_C_tau_orientation",
    "sixteen_nonzero_oriented_positive_rows_retained",
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
        raise FileNotFoundError("missing route-C/split-ownership inputs: " + ", ".join(missing))


def main() -> int:
    require_sources(
        [
            PREVIOUS,
            PREVIOUS_STATEMENTS,
            PREVIOUS_FIELDS,
            AN_POLICY,
            DE_EXPORT,
            CTAU_GATE,
            EXACT_VALUES,
            BRANCH_NOGO,
            SOURCE_ID_REDUCTION,
        ]
    )

    previous = load(PREVIOUS)
    previous_statements = load(PREVIOUS_STATEMENTS)
    previous_fields = load(PREVIOUS_FIELDS)
    an_policy = load(AN_POLICY)
    de_export = load(DE_EXPORT)
    ctau_gate = load(CTAU_GATE)
    exact_values = load(EXACT_VALUES)
    branch_nogo = load(BRANCH_NOGO)
    source_reduction = load(SOURCE_ID_REDUCTION)

    if previous["next_required_artifact"] != "MTT_Selected_CTauPhiFinSameSourceBranchIdentity_or_CechHYMConnectionValues_v1":
        raise ValueError("previous frontier is not the C_tau/PhiFin same-source branch target")
    if previous_statements["emitted_source_statement_count"] != 2:
        raise ValueError("expected previous source statement count 2/6")
    if previous_fields["promoted_source_object_field_count"] != 3:
        raise ValueError("expected previous source field count 3/11")

    routec_internal_closes = all(
        [
            de_export["accepted_row_payload"]["accepted_as_final_connection_table"],
            de_export["proof_inputs_checked"]["same_q79_F_m1_source"],
            de_export["proof_inputs_checked"]["canonical_trace_source_lemma_proved"],
            de_export["proof_inputs_checked"]["sector_by_sector_DE_identity"],
            de_export["proof_inputs_checked"]["selected_trace_equality_for_27mode_DE"],
            an_policy["kernel_policy"]["kernel_trace_policy_source_owned_on_A_N"],
            an_policy["finitepart_functional"]["source_owned_finitepart_functional_closed_on_A_N"],
        ]
    )
    ctau_orientation_closes = all(
        [
            ctau_gate["central_rank_intertwiner"]["C_tau_source_selected_as_BN_operator"],
            ctau_gate["central_rank_intertwiner"]["operator_identity_closed_for_signed_layer"],
            ctau_gate["ctau_chiral_positive_convention"]["ctau_positive_finitepart_convention_closed"],
            ctau_gate["ctau_chiral_positive_convention"]["ctau_supplies_orientation"],
        ]
    )
    phifin_magnitude_closes = all(
        [
            de_export["accepted_row_payload"]["accepted_as_final_connection_table"],
            ctau_gate["phifin_magnitude"]["commutation_or_simultaneous_functional_calculus_closed"],
            ctau_gate["phifin_magnitude"]["oriented_table_magnitude_finitepart_computed"],
            exact_values["finitepart_values"]["oriented_abs_sector_product"] == 92160000,
        ]
    )
    if not routec_internal_closes:
        raise ValueError("Route-C internality prerequisites do not close")
    if not ctau_orientation_closes:
        raise ValueError("C_tau orientation ownership prerequisites do not close")
    if not phifin_magnitude_closes:
        raise ValueError("PhiFin magnitude ownership prerequisites do not close")

    rows: dict[str, dict[str, Any]] = previous_statements["rows"]
    rows = json.loads(json.dumps(rows))
    rows["RouteC_row_internal_not_external"].update(
        {
            "emitted_as_source_owned": True,
            "promotion_source": rel(DE_EXPORT),
            "accepted_reason": (
                "The Route-C finite trace row is now an accepted selected A_N/PhiFin_DE row with "
                "source-owned finite carrier, kernel, trace, and finitepart policy; it is not an "
                "external benchmark or observed-data import."
            ),
        }
    )

    fields: dict[str, dict[str, Any]] = previous_fields["fields"]
    fields = json.loads(json.dumps(fields))
    for field in NEW_FIELDS:
        fields[field]["source_owned"] = True
        fields[field]["promotion_source"] = rel(DE_EXPORT) if "RouteC" in field else rel(CTAU_GATE)
    fields["sixteen_nonzero_oriented_positive_rows_retained"]["promotion_source"] = rel(EXACT_VALUES)

    field_count = sum(1 for field in fields.values() if field["source_owned"])
    remaining_fields = [name for name, field in fields.items() if not field["source_owned"]]

    statement_packet = {
        "schema": "MTTSourceEmissionStatementRevalidationAfterRouteCInternality.v1",
        "status": "THREE_OF_SIX_SOURCE_EMISSION_STATEMENTS_PROMOTED",
        "closure_claimed": True,
        "previous_emitted_source_statement_count": previous_statements["emitted_source_statement_count"],
        "emitted_source_statement_count": len(ACCEPTED_STATEMENTS),
        "required_source_statement_count": previous_statements["required_source_statement_count"],
        "accepted_statements": ACCEPTED_STATEMENTS,
        "remaining_statements": REMAINING_STATEMENTS,
        "rows": rows,
        "direct_source_theorem_closed": False,
        "same_branch_coemission_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    field_packet = {
        "schema": "MTTSourceObjectFieldRevalidationAfterSplitOwnership.v1",
        "status": "SEVEN_OF_ELEVEN_SOURCE_OBJECT_FIELDS_PROMOTED_SPLIT_OWNERSHIP_ONLY",
        "closure_claimed": True,
        "promoted_source_object_field_count": field_count,
        "required_source_object_field_count": previous_fields["required_source_object_field_count"],
        "newly_promoted_source_object_fields": NEW_FIELDS,
        "promoted_source_object_fields": [name for name, field in fields.items() if field["source_owned"]],
        "remaining_source_object_fields": remaining_fields,
        "fields": fields,
        "split_ownership": {
            "RouteC_PhiFin_DE_magnitude_owned_by_A_N_source": True,
            "heterotic_C_tau_orientation_owned_by_C_tau_source": True,
            "same_source_owns_both": False,
            "operators_coemitted_before_finite_comparison": False,
        },
        "oriented_logdet_promoted": False,
        "unconditional_replay_allowed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    remaining_clauses = json.loads(json.dumps(branch_nogo["clauses"]))
    remaining_clauses["routec_row_not_external_import"].update(
        {
            "emitted_by_current_source": True,
            "resolution": "closed at selected A_N/Route-C finite trace source scope; heterotic same-branch ownership still open",
        }
    )
    branch_packet = {
        "schema": "MTTSameBranchIdentityRemainingGateAfterRouteCInternality.v1",
        "status": "ROUTEC_INTERNALITY_CLOSED_SAME_BRANCH_IDENTITY_STILL_OPEN",
        "closure_claimed": True,
        "routec_row_not_external_import_closed": True,
        "source_branch_identity_closed": False,
        "transport_closed": source_reduction["transport_closed"],
        "support_prefilter_passes": source_reduction["support_prefilter_passes"],
        "remaining_sourcebranch_clauses": {
            key: value for key, value in remaining_clauses.items() if not value["emitted_by_current_source"]
        },
        "closed_sourcebranch_clauses": {
            key: value for key, value in remaining_clauses.items() if value["emitted_by_current_source"]
        },
        "why_same_branch_still_open": [
            "C_tau orientation and PhiFin_DE magnitude are owned on split sources, not one selected BN27 threshold source.",
            "The 11-label rho/tau shadow is still not promoted to the full positive BN27 threshold carrier.",
            "No selected S_QaSU3^BN27 source object owns both branches and the no-lift replay.",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTNextSameBranchOrCechHYMContract.v1",
        "status": "NEXT_IS_SAME_BRANCH_COEMISSION_OR_SELECTED_CECH_HYM_VALUES",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "source_emission_statement_count": "3/6",
        "source_object_field_count": f"{field_count}/11",
        "final_connection_table_count": "4/8",
        "remaining_source_emission_statements": REMAINING_STATEMENTS,
        "remaining_source_object_fields": remaining_fields,
        "remaining_minimal_exits": [
            "prove one selected source owns both C_tau orientation and PhiFin_DE magnitude",
            "promote the full BN27 positive carrier rather than the 11-label rho/tau shadow",
            "declare/derive S_QaSU3^BN27 as the selected threshold source, or emit selected Cech/HYM connection values",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedRouteCInternalitySplitOwnershipOrSameBranchIdentity",
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
            "an_policy": rel(AN_POLICY),
            "de_export": rel(DE_EXPORT),
            "ctau_gate": rel(CTAU_GATE),
            "exact_values": rel(EXACT_VALUES),
            "branch_nogo": rel(BRANCH_NOGO),
            "source_id_reduction": rel(SOURCE_ID_REDUCTION),
        },
        "output_packets": {
            "source_emission_statement_revalidation_after_routec": rel(STATEMENT_PACKET),
            "source_object_field_revalidation_after_splitownership": rel(FIELD_PACKET),
            "same_branch_identity_remaining_gate": rel(BRANCH_PACKET),
            "next_samebranch_or_cechhym_contract": rel(NEXT_PACKET),
        },
        "closure_decision": {
            "source_emission_statement_count": len(ACCEPTED_STATEMENTS),
            "required_source_emission_statement_count": previous_statements["required_source_statement_count"],
            "accepted_source_emission_statements": ACCEPTED_STATEMENTS,
            "remaining_source_emission_statements": REMAINING_STATEMENTS,
            "source_object_field_count": field_count,
            "required_source_object_field_count": previous_fields["required_source_object_field_count"],
            "newly_promoted_source_object_fields": NEW_FIELDS,
            "routec_row_internal_not_external_closed": True,
            "split_Ctau_orientation_owned": True,
            "split_PhiFin_DE_magnitude_owned": True,
            "same_source_owns_both_branches": False,
            "direct_source_theorem_closed": False,
            "source_branch_identity_closed": False,
            "oriented_logdet_promoted": False,
            "no_lifted_flags_connection_replay_promoted": False,
            "final_connection_tables_accepted": 4,
            "strict_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "RouteCInternalityAndSplitOwnershipTheorem",
            "proved": True,
            "statement": (
                "After the A_N finitepart/kernel policy closure, the Route-C PhiFin_DE trace row is "
                "internal to the selected finite source rather than external support.  Separately, the "
                "Route-C source owns the PhiFin_DE magnitude data and the heterotic C_tau source owns "
                "the orientation data.  This promotes the source-emission layer to 3/6 and source-object "
                "fields to 7/11.  It does not prove same-source co-emission, S_QaSU3^BN27 source selection, "
                "logdet promotion, no-lift replay, no-knob closure, or true SM equivalence."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedRouteCInternalitySplitOwnershipOrSameBranchIdentity",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "source_emission_statement_count": len(ACCEPTED_STATEMENTS),
        "required_source_emission_statement_count": previous_statements["required_source_statement_count"],
        "accepted_source_emission_statements": ACCEPTED_STATEMENTS,
        "remaining_source_emission_statements": REMAINING_STATEMENTS,
        "source_object_field_count": field_count,
        "required_source_object_field_count": previous_fields["required_source_object_field_count"],
        "newly_promoted_source_object_fields": NEW_FIELDS,
        "routec_row_internal_not_external_closed": True,
        "split_Ctau_orientation_owned": True,
        "split_PhiFin_DE_magnitude_owned": True,
        "same_source_owns_both_branches": False,
        "direct_source_theorem_closed": False,
        "source_branch_identity_closed": False,
        "oriented_logdet_promoted": False,
        "no_lifted_flags_connection_replay_promoted": False,
        "final_connection_tables_accepted": 4,
        "strict_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected Route-C Internality and Split Ownership or Same Branch Identity v1

## Theorem

`RouteCInternalityAndSplitOwnershipTheorem` is proved.

## Result

The source-emission layer moves from `2/6` to `{len(ACCEPTED_STATEMENTS)}/6`.
The source-object layer moves from `3/11` to `{field_count}/11`.

Newly promoted:

- `RouteC_row_internal_not_external`
- `RouteC_row_internal_theorem_not_external_import`
- `one_selected_source_owns_RouteC_PhiFin_DE_magnitude`
- `one_selected_source_owns_heterotic_C_tau_orientation`
- `sixteen_nonzero_oriented_positive_rows_retained`

This is split ownership only.  Same-source co-emission, selected
`S_QaSU3^BN27`, final `log(92160000)`, and no-lift replay remain open.

## Next Artifact

`{NEXT}`
"""

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
