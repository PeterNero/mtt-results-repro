"""Promote the rho/tau shadow guard after common-carrier co-emission.

The remaining source-object table still had one ambiguous field: the 11-label
rho/tau shadow embeds, but is not the full BN27 threshold domain.  Earlier
packets repeatedly used this as a blocker; this builder turns it into an
audited guard field so the next frontier cannot loop back to the retired
projective-shadow proof source.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_rhotau_shadowguard_after_commoncarrier_or_selectedsourceobject"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SHADOW_PACKET = PACKET_DIR / "rho_tau_shadow_guard.packet.json"
STATEMENT_PACKET = PACKET_DIR / "source_emission_statement_revalidation_after_shadowguard.packet.json"
FIELD_PACKET = PACKET_DIR / "source_object_field_revalidation_after_shadowguard.packet.json"
BRANCH_PACKET = PACKET_DIR / "selected_source_object_gate_after_shadowguard.packet.json"
NEXT_PACKET = PACKET_DIR / "next_selectedsourceobject_or_nolift_or_cechhym_contract.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_RhoTauShadowGuard_AfterCommonCarrier_or_SelectedSourceObject_v1.md"

PREVIOUS = DATA / "selected_commoncarriercoemission_after_splitownership_or_selectedsourceobject.candidate.json"
PREVIOUS_STATEMENTS = (
    DATA
    / "selected_commoncarriercoemission_after_splitownership_or_selectedsourceobject"
    / "source_emission_statement_revalidation_after_commoncarrier.packet.json"
)
PREVIOUS_FIELDS = (
    DATA
    / "selected_commoncarriercoemission_after_splitownership_or_selectedsourceobject"
    / "source_object_field_revalidation_after_commoncarrier.packet.json"
)
PREVIOUS_BRANCH = (
    DATA
    / "selected_commoncarriercoemission_after_splitownership_or_selectedsourceobject"
    / "same_branch_source_theorem_gate_after_commoncarrier.packet.json"
)
FULL_ORBIT_LANE = (
    DATA
    / "selected_heteroticstromingerewthresholdkernel_or_bn27directcarriersourcetheorem_or_directhkrow"
    / "bn27_direct_carrier_full_orbit_lane.packet.json"
)
TRANSPORT_FRONTIER = (
    DATA
    / "selected_orientedphifin_sourceownership_theorem_or_smootheqa_quotient"
    / "bn27_sourceownership_transport_frontier.packet.json"
)
RHOE_FUNCTOR = (
    DATA
    / "selected_finiterhoetoorientedbnfunctor_or_smootheqarepresentative_or_directhkrow"
    / "finite_rhoe_to_oriented_bn_functor_gate.packet.json"
)
CTAU_GATE = (
    DATA
    / "selected_orientationmagnitudecoemission_or_endomorphismthresholdfinitepart_or_directhkrow"
    / "ctau_phifin_threshold_identity_gate.packet.json"
)

STATUS = (
    "MTT_SELECTED_RHOTAU_SHADOWGUARD_AFTER_COMMONCARRIER_"
    "NINE_OF_ELEVEN_FIELDS_PROMOTED_SELECTEDSOURCEOBJECT_OPEN"
)
PREVIOUS_STATUS = (
    "MTT_SELECTED_COMMONCARRIERCOEMISSION_AFTER_SPLITOWNERSHIP_"
    "OPERATORS_FIELD_PROMOTED_SOURCE_THEOREM_OPEN"
)
NEXT = "MTT_Selected_SelectedSourceObjectSQaSU3BN27_or_NoLiftReplay_or_CechHYMConnectionValues_v1"
PROMOTED_FIELD = "eleven_label_rho_tau_shadow_embeds_but_is_not_threshold_domain"
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
        raise FileNotFoundError("missing rho/tau shadow guard inputs: " + ", ".join(missing))


def main() -> int:
    require_sources(
        [
            PREVIOUS,
            PREVIOUS_STATEMENTS,
            PREVIOUS_FIELDS,
            PREVIOUS_BRANCH,
            FULL_ORBIT_LANE,
            TRANSPORT_FRONTIER,
            RHOE_FUNCTOR,
            CTAU_GATE,
        ]
    )

    previous = load(PREVIOUS)
    previous_statements = load(PREVIOUS_STATEMENTS)
    previous_fields = load(PREVIOUS_FIELDS)
    previous_branch = load(PREVIOUS_BRANCH)
    full_orbit = load(FULL_ORBIT_LANE)
    transport = load(TRANSPORT_FRONTIER)
    rhoe_functor = load(RHOE_FUNCTOR)
    ctau_gate = load(CTAU_GATE)

    if previous["status"] != PREVIOUS_STATUS:
        raise ValueError("previous frontier is not the common-carrier packet")
    if previous_fields["promoted_source_object_field_count"] != 8:
        raise ValueError("expected previous source-object fields 8/11")
    if previous_statements["emitted_source_statement_count"] != 3:
        raise ValueError("expected previous source statements 3/6")

    orbit = full_orbit["orbit_arithmetic"]
    required_product = 9600 * 9600
    shadow_product = orbit["embedded_11_label_shadow_product"]
    missing_multiplier = orbit["missing_multiplier"]
    transport_no_go = transport["projective_lift_no_go"]
    rank3 = transport["route_ranking"]["rank_3_projective_rhoE_BN27_lift"]
    label_embedding = ctau_gate["label_embedding"]
    orientation_functor = rhoe_functor["orientation_functor"]
    rho_shadow = rhoe_functor["rho_shadow_functor"]

    shadow_guard_closed = all(
        [
            label_embedding["label_embedding_candidate_built"],
            label_embedding["projection_pair_candidate_valid_as_injection"],
            label_embedding["rhoE_character_intertwines"],
            not label_embedding["D_E_or_EQa_intertwines"],
            not label_embedding["finitepart_regularization_same_scheme"],
            orientation_functor["finite_rhoE_to_oriented_BN_orientation_functor_closed"],
            not orientation_functor["threshold_magnitude_functor_closed"],
            rho_shadow["rho_shadow_embedding_retained"],
            shadow_product == 16,
            missing_multiplier == 5760000,
            shadow_product * missing_multiplier == required_product,
            orbit["required_full_orbit_product"] == "9600*9600",
            transport_no_go["missing_multiplier_to_full_abs_sector"] == 5760000,
            transport_no_go["missing_positive_oriented_row_count"] == 10,
            not transport_no_go["projective_rhoE_BN27_lift_closed"],
            not transport_no_go["operator_lift_passes"],
            rank3["orientation_shadow_still_valid"],
            rank3["retired_as_threshold_proof_source"],
        ]
    )
    if not shadow_guard_closed:
        raise ValueError("rho/tau shadow guard prerequisites do not close")

    fields: dict[str, dict[str, Any]] = json.loads(json.dumps(previous_fields["fields"]))
    fields[PROMOTED_FIELD].update(
        {
            "source_owned": True,
            "promotion_source": rel(SHADOW_PACKET),
            "accepted_reason": (
                "The 27x11 rho/tau shadow is a valid orientation/character injection, "
                "but its product is 16 and it misses 10 positive oriented rows.  The "
                "selected positive threshold domain requires 9600*9600=92160000, so "
                "the missing multiplier is 5760000.  The shadow is therefore retained "
                "only as an orientation shadow and is rejected as the threshold domain."
            ),
            "scope": "negative_guard_retiring_projective_shadow_as_threshold_source",
        }
    )
    promoted_fields = [name for name, field in fields.items() if field["source_owned"]]
    remaining_fields = [name for name, field in fields.items() if not field["source_owned"]]

    rows: dict[str, dict[str, Any]] = json.loads(json.dumps(previous_statements["rows"]))
    rows["S_QaSU3_BN27_is_selected_threshold_source"].update(
        {
            "emitted_as_source_owned": False,
            "current_blocker": (
                "rho/tau shadow has now been retired as threshold-domain proof; a direct "
                "selected S_QaSU3^BN27 source object or selected Cech/HYM values are still required"
            ),
            "rho_tau_shadow_guard_closed": True,
        }
    )
    rows["C_tau_and_PhiFin_DE_coemitted_by_source"].update(
        {
            "emitted_as_source_owned": False,
            "current_blocker": (
                "common carrier and shadow guard are closed, but one selected source object "
                "emitting both branches is still unproved"
            ),
        }
    )
    rows["no_lift_replay_audit_from_emitted_fields"].update(
        {
            "emitted_as_source_owned": False,
            "current_blocker": "no-lift replay still waits on selected source object or final selected connection values",
        }
    )

    shadow_packet = {
        "schema": "MTTRhoTauShadowGuard.v1",
        "status": "RHO_TAU_SHADOW_EMBEDS_BUT_IS_NOT_THRESHOLD_DOMAIN",
        "closure_claimed": True,
        "promotes_source_object_field": PROMOTED_FIELD,
        "label_embedding_candidate_built": True,
        "projection_pair_candidate_valid_as_injection": True,
        "rhoE_character_intertwines": True,
        "D_E_or_EQa_intertwines": False,
        "finitepart_regularization_same_scheme": False,
        "orientation_functor_closed": True,
        "threshold_magnitude_functor_closed": False,
        "rho_shadow_embedding_retained": True,
        "orientation_shadow_still_valid": True,
        "retired_as_threshold_proof_source": True,
        "shadow_product": shadow_product,
        "required_full_orbit_product": required_product,
        "missing_multiplier": missing_multiplier,
        "missing_positive_oriented_row_count": transport_no_go["missing_positive_oriented_row_count"],
        "projective_rhoE_BN27_lift_closed": False,
        "selected_source_object_closed": False,
        "source_branch_identity_closed": False,
        "oriented_logdet_promoted": False,
        "no_lift_replay_allowed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    statement_packet = {
        "schema": "MTTSourceEmissionStatementRevalidationAfterShadowGuard.v1",
        "status": "THREE_OF_SIX_SOURCE_STATEMENTS_RETAINED_SHADOW_GUARD_CLOSED",
        "closure_claimed": True,
        "previous_emitted_source_statement_count": 3,
        "emitted_source_statement_count": 3,
        "required_source_statement_count": previous_statements["required_source_statement_count"],
        "accepted_statements": previous_statements["accepted_statements"],
        "remaining_statements": REMAINING_STATEMENTS,
        "rows": rows,
        "rho_tau_shadow_guard_closed": True,
        "same_branch_coemission_closed": False,
        "direct_source_theorem_closed": False,
        "selected_source_object_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    field_packet = {
        "schema": "MTTSourceObjectFieldRevalidationAfterShadowGuard.v1",
        "status": "NINE_OF_ELEVEN_SOURCE_OBJECT_FIELDS_PROMOTED_SHADOW_GUARD_ONLY",
        "closure_claimed": True,
        "previous_promoted_source_object_field_count": 8,
        "promoted_source_object_field_count": len(promoted_fields),
        "required_source_object_field_count": previous_fields["required_source_object_field_count"],
        "newly_promoted_source_object_fields": [PROMOTED_FIELD],
        "promoted_source_object_fields": promoted_fields,
        "remaining_source_object_fields": remaining_fields,
        "fields": fields,
        "rho_tau_shadow_guard_closed": True,
        "selected_source_object_S_QaSU3_BN27": False,
        "no_lifted_flags_full_replay_audit": False,
        "oriented_logdet_promoted": False,
        "unconditional_replay_allowed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    branch_packet = {
        "schema": "MTTSelectedSourceObjectGateAfterShadowGuard.v1",
        "status": "SHADOW_PROOF_SOURCE_RETIRED_SELECTED_SOURCE_OBJECT_STILL_OPEN",
        "closure_claimed": True,
        "rho_tau_shadow_guard_closed": True,
        "projective_shadow_retired_as_threshold_proof_source": True,
        "selected_source_object_S_QaSU3_BN27_closed": False,
        "same_source_owns_both_branches": False,
        "source_branch_identity_closed": False,
        "no_lift_replay_closed": False,
        "final_connection_tables_accepted": 4,
        "remaining_root_clauses": [
            "selected_source_object_S_QaSU3_BN27",
            "one_selected_source_names_both_branches",
            "no_lift_replay_from_emitted_fields",
            "selected_Cech_HYM_connection_values",
        ],
        "retired_root_clause": "eleven_label_to_full_BN27_threshold_carrier",
        "previous_remaining_root_clauses": previous_branch["remaining_root_clauses"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTNextSelectedSourceObjectOrNoLiftOrCechHYMContract.v1",
        "status": "NEXT_IS_SELECTED_SOURCE_OBJECT_NOLIFT_OR_CECHHYM_VALUES",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "source_emission_statement_count": "3/6",
        "source_object_field_count": f"{len(promoted_fields)}/11",
        "final_connection_table_count": "4/8",
        "remaining_source_emission_statements": REMAINING_STATEMENTS,
        "remaining_source_object_fields": remaining_fields,
        "remaining_minimal_exits": [
            "derive selected source object S_QaSU3^BN27 that names both branches",
            "execute no-lift replay from emitted source fields after selected source object closure",
            "emit selected Cech/HYM connection values directly",
        ],
        "forbidden_loopback": [
            "do not use the 11-label rho/tau shadow as the full BN27 threshold domain",
            "do not promote log(92160000) from shadow arithmetic alone",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedRhoTauShadowGuardAfterCommonCarrierOrSelectedSourceObject",
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
            "full_orbit_lane": rel(FULL_ORBIT_LANE),
            "transport_frontier": rel(TRANSPORT_FRONTIER),
            "rhoe_functor": rel(RHOE_FUNCTOR),
            "ctau_gate": rel(CTAU_GATE),
        },
        "output_packets": {
            "rho_tau_shadow_guard": rel(SHADOW_PACKET),
            "source_emission_statement_revalidation_after_shadowguard": rel(STATEMENT_PACKET),
            "source_object_field_revalidation_after_shadowguard": rel(FIELD_PACKET),
            "selected_source_object_gate_after_shadowguard": rel(BRANCH_PACKET),
            "next_selectedsourceobject_or_nolift_or_cechhym_contract": rel(NEXT_PACKET),
        },
        "closure_decision": {
            "source_emission_statement_count": 3,
            "required_source_emission_statement_count": previous_statements["required_source_statement_count"],
            "accepted_source_emission_statements": previous_statements["accepted_statements"],
            "remaining_source_emission_statements": REMAINING_STATEMENTS,
            "source_object_field_count": len(promoted_fields),
            "required_source_object_field_count": previous_fields["required_source_object_field_count"],
            "newly_promoted_source_object_fields": [PROMOTED_FIELD],
            "rho_tau_shadow_guard_closed": True,
            "shadow_product": shadow_product,
            "required_full_orbit_product": required_product,
            "missing_multiplier": missing_multiplier,
            "missing_positive_oriented_row_count": transport_no_go["missing_positive_oriented_row_count"],
            "projective_shadow_retired_as_threshold_proof_source": True,
            "selected_source_object_S_QaSU3_BN27": False,
            "C_tau_and_PhiFin_DE_coemitted_by_source": False,
            "same_source_owns_both_branches": False,
            "source_branch_identity_closed": False,
            "oriented_logdet_promoted": False,
            "no_lifted_flags_connection_replay_promoted": False,
            "final_connection_tables_accepted": 4,
            "strict_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "RhoTauShadowGuardAfterCommonCarrierTheorem",
            "proved": True,
            "statement": (
                "The phase-preserving 27x11 rho/tau shadow embeds and preserves the rho_E "
                "orientation characters, but it cannot serve as the selected BN27 threshold "
                "domain: it does not intertwine D_E/E_Qa or finitepart regularization, its "
                "product is 16, it misses 10 positive oriented rows, and the selected positive "
                "orbit requires 9600*9600=92160000, leaving multiplier 5760000.  Therefore "
                "the shadow is retained as orientation support and retired as a threshold proof "
                "source.  This promotes one guard field to 9/11 without selecting S_QaSU3^BN27, "
                "without no-lift replay, and without final connection-row promotion."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedRhoTauShadowGuardAfterCommonCarrierOrSelectedSourceObject",
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
        "rho_tau_shadow_guard_closed": True,
        "shadow_product": shadow_product,
        "required_full_orbit_product": required_product,
        "missing_multiplier": missing_multiplier,
        "missing_positive_oriented_row_count": transport_no_go["missing_positive_oriented_row_count"],
        "projective_shadow_retired_as_threshold_proof_source": True,
        "selected_source_object_S_QaSU3_BN27": False,
        "C_tau_and_PhiFin_DE_coemitted_by_source": False,
        "same_source_owns_both_branches": False,
        "source_branch_identity_closed": False,
        "oriented_logdet_promoted": False,
        "no_lifted_flags_connection_replay_promoted": False,
        "final_connection_tables_accepted": 4,
        "strict_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected Rho/Tau Shadow Guard After Common-Carrier v1

## Theorem

`RhoTauShadowGuardAfterCommonCarrierTheorem` is proved.

## Result

The source-object layer moves from `8/11` to `{len(promoted_fields)}/11` by
promoting `eleven_label_rho_tau_shadow_embeds_but_is_not_threshold_domain`.

The 27x11 shadow remains valid orientation support, but it is now explicitly
retired as a BN27 threshold-domain proof source:

- shadow product: `{shadow_product}`
- required positive product: `9600*9600 = {required_product}`
- missing multiplier: `{missing_multiplier}`
- missing positive oriented rows: `{transport_no_go["missing_positive_oriented_row_count"]}`

Source-emission statements remain `3/6` and final connection tables remain
`4/8`.  Selected `S_QaSU3^BN27`, same-source co-emission, no-lift replay,
strict no-knob closure, and true SM equivalence are not promoted.

## Next Artifact

`{NEXT}`
"""

    write_json(SHADOW_PACKET, shadow_packet)
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
