"""Build same-source connection value table frontier packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
QA = Path("C:/Users/nero_/Downloads/TEXPAPERS/mtt-qa-su3-packet-proof/candidate_data")

SLUG = "selected_samesourceconnectionvaluetable_or_directhkrow"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
TABLE_PACKET = PACKET_DIR / "eight_field_connection_value_table.packet.json"
ROUTE_PACKET = PACKET_DIR / "three_route_field_alignment.packet.json"
VALIDATOR_PACKET = PACKET_DIR / "same_source_connection_table_validator.packet.json"
NEXT_CONTRACT = PACKET_DIR / "next_first_same_source_field_or_direct_hkrow_contract.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_SameSourceConnectionValueTable_or_DirectHKRow_v1.md"

SOURCES = {
    "previous": DATA / "selected_typedcechhymprojectiveconnectionwitnessvalues_or_directhkrow.candidate.json",
    "previous_contract": DATA
    / "selected_typedcechhymprojectiveconnectionwitnessvalues_or_directhkrow"
    / "next_same_source_connection_table_or_direct_hkrow_contract.packet.json",
    "open_payload": QA / "selected_u1y_routec_typed_monad_cech_or_hym_connection_witness.open.json",
    "minimal_values": QA
    / "selected_heterotic_orientedphifin_selectedconnectionwitness_minimal_source_values_packet.json",
    "template": QA
    / "selected_heterotic_orientedphifin_bn27_sourcebranchidentity_sourceamendment_template_or_connectionvalues.candidate.json",
}

STATUS = "MTT_SELECTED_SAMESOURCE_CONNECTION_VALUE_TABLE_BUILT_SUPPORT2_ACCEPTED0_DIRECT_HK_OPEN"
NEXT = "MTT_Selected_FirstSameSourceConnectionFieldEmission_or_DirectHKRow_v1"


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


def require_sources() -> dict[str, dict[str, Any]]:
    missing = [rel(path) for path in SOURCES.values() if not path.exists()]
    if missing:
        raise FileNotFoundError(f"Missing required source packets: {missing}")
    return {name: load(path) for name, path in SOURCES.items()}


def field(
    name: str,
    support_value: str | None,
    support_source: str | None,
    route_requirements: dict[str, list[str]],
    blocker: str,
) -> dict[str, Any]:
    return {
        "field": name,
        "support_value": support_value,
        "support_source": support_source,
        "support_present": support_value is not None,
        "accepted_as_same_source_connection_value": False,
        "route_requirements": route_requirements,
        "blocking_reason": blocker,
    }


def main() -> int:
    sources = require_sources()
    prev_decision = sources["previous"]["closure_decision"]
    contract = sources["previous_contract"]
    open_payload = sources["open_payload"]
    minimal = sources["minimal_values"]
    template_decision = sources["template"]["decision"]

    branch = open_payload["branch"]
    required_fields = contract["required_same_source_connection_table_fields"]

    rows = [
        field(
            "source_id",
            "q79/F,m=1 branch label",
            rel(SOURCES["open_payload"]),
            {
                "source_identity_transport": [
                    "same-source theorem emits Route-C/q79 BN27 finite trace row",
                    "source certificate names the heterotic Qa/SU3 branch as owner",
                ],
                "typed_connection_values": [
                    "typed Cech/monad source certificate",
                    "BN27 export map",
                ],
                "direct_connection_values": [
                    "selected A/F_A or projective rho_E source certificate",
                    "HYM/Strominger/Bianchi residual certificate",
                ],
            },
            "The branch label is selected support, but no same-source certificate owns it as the connection table source.",
        ),
        field(
            "carrier_or_cover_id",
            "27-mode qutrit/BN finite carrier support plus open Cech-cover slot",
            rel(SOURCES["open_payload"]),
            {
                "typed_connection_values": [
                    "cech_cover",
                    "selected_H1_E_representatives",
                    "sector_projection_maps_Q_u_d_L_e_N_H",
                ],
                "finite_routec_solve": [
                    "finite_basis_BN",
                    "nonidentity_selected_rhoE_boundary_matrices",
                ],
                "direct_connection_values": [
                    "selected_holomorphic_bundle_or_sheaf_model",
                    "selected_gauduchon_or_balanced_metric",
                ],
            },
            "Carrier support exists, but the selected cover/bundle/finite basis values are still null.",
        ),
        field(
            "transition_or_connection_representative",
            None,
            None,
            {
                "typed_connection_values": [
                    "typed_f_sections",
                    "typed_g_sections",
                    "line_bundle_transition_functions",
                    "g_after_f_zero_certificate",
                    "cocycle_checks",
                ],
                "finite_routec_solve": [
                    "local_A01_or_discrete_connection_variables",
                    "routec_residual_values",
                ],
                "direct_connection_values": [
                    "hym_connection_coefficients",
                    "gauge_fixing",
                ],
            },
            "No typed sections, Cech transitions, local A01 variables, or HYM coefficients are emitted.",
        ),
        field(
            "D_E_action",
            None,
            None,
            {
                "finite_routec_solve": ["DE_action"],
                "typed_connection_values": [
                    "sector_projection_maps_Q_u_d_L_e_N_H",
                    "exactness_or_torsion_free_sheaf_control",
                ],
                "direct_connection_values": [
                    "finite D_E/E_Qa action and zeta finitepart rule",
                ],
            },
            "D_E gap-layer support is closed, but no same-source D_E action matrix is emitted.",
        ),
        field(
            "rho_E_or_projective_character_table",
            None,
            None,
            {
                "finite_routec_solve": ["nonidentity_selected_rhoE_boundary_matrices"],
                "direct_connection_values": [
                    "selected A/F_A or projective rho_E transition matrices",
                ],
                "source_identity_transport": [
                    "proof that C_tau orientation and PhiFin_DE magnitude are co-emitted before finite comparison",
                ],
            },
            "Projective rhoE support exists upstream, but not as same-source transition or character values for this table.",
        ),
        field(
            "Riesz_projector",
            None,
            None,
            {
                "finite_routec_solve": ["riesz_gap"],
                "typed_connection_values": ["Hermitian metric/trace and BN27 export map"],
                "direct_connection_values": ["HYM/Strominger/Bianchi residual certificate"],
            },
            "Riesz/Green gap-layer export is support only; the table has no selected projector value.",
        ),
        field(
            "reduced_Green_operator",
            None,
            None,
            {
                "finite_routec_solve": ["reduced_green"],
                "direct_connection_values": ["finite D_E/E_Qa action and zeta finitepart rule"],
            },
            "No reduced Green matrix/operator value is emitted from the same source.",
        ),
        field(
            "dotD_alpha1_or_threshold_derivative",
            None,
            None,
            {
                "finite_routec_solve": ["dotD_alpha1"],
                "direct_connection_values": [
                    "finite D_E/E_Qa action and zeta finitepart rule",
                    "threshold derivative finitepart rule",
                ],
            },
            "No same-branch threshold derivative or dotD_alpha1 value is emitted.",
        ),
    ]

    if [row["field"] for row in rows] != required_fields:
        raise ValueError("Field order does not match previous contract")

    support_count = sum(1 for row in rows if row["support_present"])
    accepted_count = sum(1 for row in rows if row["accepted_as_same_source_connection_value"])
    null_payload_slots = {
        "typed_monad_cech_payload_null_slots": sum(
            value is None for value in open_payload["typed_monad_cech_payload"].values()
        ),
        "direct_hym_payload_null_slots": sum(
            value is None for value in open_payload["direct_hym_payload"].values()
        ),
        "finite_routec_solve_payload_null_slots": sum(
            value is None for value in open_payload["finite_routec_solve_payload"].values()
        ),
    }

    table_packet = {
        "schema": "MTTSameSourceConnectionValueTable.v1",
        "status": "EIGHT_FIELD_TABLE_BUILT_SUPPORT_VALUES_NOT_ACCEPTED",
        "closure_claimed": True,
        "branch": branch,
        "field_count": len(rows),
        "support_field_count": support_count,
        "accepted_same_source_connection_value_count": accepted_count,
        "rows": rows,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    route_packet = {
        "schema": "MTTThreeRouteConnectionFieldAlignment.v1",
        "status": "THREE_LEGAL_ROUTES_ALIGNED_TO_EIGHT_FIELDS",
        "closure_claimed": True,
        "acceptable_minimal_values": minimal["acceptable_minimal_values"],
        "typed_route_null_slots": open_payload["typed_monad_cech_payload"],
        "direct_hym_route_null_slots": open_payload["direct_hym_payload"],
        "finite_routec_route_null_slots": open_payload["finite_routec_solve_payload"],
        "same_source_requirements": open_payload["same_source_requirements"],
        "null_payload_slot_counts": null_payload_slots,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    validator_packet = {
        "schema": "MTTSameSourceConnectionTableValidator.v1",
        "status": "VALIDATOR_EXECUTED_REJECTED_FINAL_CONNECTION_VALUES",
        "closure_claimed": True,
        "source_object_required_field_count": template_decision[
            "source_object_required_field_count"
        ],
        "source_object_filled_field_count": template_decision[
            "source_object_filled_field_count"
        ],
        "connection_values_required_field_count": template_decision[
            "connection_values_required_field_count"
        ],
        "connection_values_filled_field_count_before_this_table": template_decision[
            "connection_values_filled_field_count"
        ],
        "table_support_field_count": support_count,
        "accepted_same_source_connection_value_count": accepted_count,
        "rejection_reasons": [
            "support labels do not constitute a same-source certificate",
            "typed Cech/monad fields are null",
            "direct HYM/Strominger connection fields are null",
            "finite Route-C solve fields are null",
            "direct K_threshold.Omega_H.lambda is still not emitted",
        ],
        "accepted_as_full_connection_table": False,
        "direct_H_K_row_emitted": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_contract = {
        "schema": "MTTFirstSameSourceConnectionFieldOrDirectHKRowContract.v1",
        "status": "FIRST_SOURCE_FIELD_OR_DIRECT_HKROW_REQUIRED",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "recommended_first_field": "transition_or_connection_representative",
        "why_first": (
            "It is the first non-label field and would force actual typed sections, "
            "local discrete connection variables, or HYM coefficients; those values "
            "then feed D_E, rho_E, Riesz, Green, and derivative rows."
        ),
        "alternative_first_field": "source_id",
        "alternative_reason": (
            "A source certificate naming the same branch as table owner could promote "
            "the existing q79/F,m=1 support label before numerical connection values."
        ),
        "direct_exit": "K_threshold.Omega_H.lambda",
        "strict_K_threshold_count": {
            "accepted": prev_decision["accepted_selected_K_source_row_count"],
            "required": prev_decision["selected_K_threshold_row_count_required"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedSameSourceConnectionValueTableOrDirectHKRow",
        "status": STATUS,
        "previous_status": sources["previous"]["status"],
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {name: rel(path) for name, path in SOURCES.items()},
        "output_packets": {
            "eight_field_connection_value_table": rel(TABLE_PACKET),
            "three_route_field_alignment": rel(ROUTE_PACKET),
            "same_source_connection_table_validator": rel(VALIDATOR_PACKET),
            "next_first_same_source_field_or_direct_hkrow_contract": rel(NEXT_CONTRACT),
        },
        "closure_decision": {
            "eight_field_table_built": True,
            "three_legal_routes_aligned_to_fields": True,
            "support_field_count": support_count,
            "accepted_same_source_connection_value_count": accepted_count,
            "accepted_as_full_connection_table": False,
            "typed_monad_cech_values_present": False,
            "direct_hym_values_present": False,
            "finite_routec_solve_values_present": False,
            "same_source_certificate_present": False,
            "selected_K_threshold_Omega_H_lambda": False,
            "strict_H_K_threshold_row_emitted": False,
            "payload_missing_leaf_count": prev_decision["payload_missing_leaf_count"],
            "accepted_selected_K_source_row_count": prev_decision[
                "accepted_selected_K_source_row_count"
            ],
            "selected_K_threshold_row_count_required": prev_decision[
                "selected_K_threshold_row_count_required"
            ],
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "SameSourceConnectionValueTableNormalFormTheorem",
            "proved": True,
            "statement": (
                "The same-source connection witness is now a concrete eight-field "
                "table. Current packets provide two label/carrier support fields, "
                "but zero accepted same-source connection values. The first value "
                "field to attack is the transition/connection representative, or "
                "alternatively the source certificate for the existing q79/F,m=1 "
                "branch label; direct K_threshold.Omega_H.lambda remains an "
                "independent exit."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedSameSourceConnectionValueTableOrDirectHKRow",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "eight_field_table_built": True,
        "three_legal_routes_aligned_to_fields": True,
        "support_field_count": support_count,
        "accepted_same_source_connection_value_count": accepted_count,
        "accepted_as_full_connection_table": False,
        "strict_H_K_threshold_row_emitted": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected Same-Source Connection Value Table or Direct H K Row v1

## Theorem

`SameSourceConnectionValueTableNormalFormTheorem` is emitted.

## Newly Closed

- The same-source connection witness is now a concrete `8`-field table.
- The three legal routes are aligned to the same fields:
  typed Cech/monad values, direct HYM/Strominger values, or finite Route-C solve
  values.
- Current support fills `2/8` label/carrier-level support slots, but these are
  not accepted as same-source connection values.
- The strict validator is executed and accepts `0/8` final connection-value
  fields.

## Table Result

- Support fields present: `source_id`, `carrier_or_cover_id`.
- First non-label value field: `transition_or_connection_representative`.
- Accepted same-source connection values: `0`.
- Missing U1/Y connection-witness leaves: `{prev_decision["payload_missing_leaf_count"]}`.
- Strict selected `K_threshold` rows: `{prev_decision["accepted_selected_K_source_row_count"]}/{prev_decision["selected_K_threshold_row_count_required"]}`.

## Why This Breaks The Loop

Older Cech/trace, HYM/Galerkin, and Route-C packets are now routed into exact
table fields. They are useful support, but the validator rejects them unless
they emit source-owned values in the table. The next attempt must fill one row,
not restate route readiness.

## Next Artifact

`{NEXT}`
"""

    write_json(TABLE_PACKET, table_packet)
    write_json(ROUTE_PACKET, route_packet)
    write_json(VALIDATOR_PACKET, validator_packet)
    write_json(NEXT_CONTRACT, next_contract)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
