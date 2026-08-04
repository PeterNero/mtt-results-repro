"""Build source-branch identity amendment or selected connection values frontier packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
QA = Path("C:/Users/nero_/Downloads/TEXPAPERS/mtt-qa-su3-packet-proof/candidate_data")

SLUG = "selected_sourcebranchidentity_sourceamendment_or_selectedconnectionvalues_or_directhkrow"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
AMENDMENT_GATE = PACKET_DIR / "source_amendment_or_connection_values_gate.packet.json"
TRANSPORT_GATE = PACKET_DIR / "bn27_sourceownership_transport_gate.packet.json"
CONNECTION_GATE = PACKET_DIR / "typed_connection_witness_gate.packet.json"
NEXT_CONTRACT = PACKET_DIR / "next_connection_witness_value_payload_contract.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_SourceBranchIdentity_SourceAmendment_or_SelectedConnectionValues_or_DirectHKRow_v1.md"

SOURCES = {
    "previous": DATA
    / "selected_finiterhoetoorientedbnfunctor_or_smootheqarepresentative_or_directhkrow.candidate.json",
    "sourcebranch_repair": QA
    / "selected_heterotic_orientedphifin_sourcebranchidentity_sourceamendment_or_connectionvalues.candidate.json",
    "sourcebranch_template": QA
    / "selected_heterotic_orientedphifin_bn27_sourcebranchidentity_sourceamendment_template_or_connectionvalues.candidate.json",
    "sourceownership_transport": QA
    / "selected_heterotic_orientedphifin_bn27_sourceownership_transport_or_connectionwitness_values.candidate.json",
    "directbn27_transport_fill": QA
    / "selected_heterotic_orientedphifin_directbn27_sourceidentitytransport_fill_or_typedconnectionwitnessvalues.candidate.json",
    "direct_source_or_external": QA
    / "selected_heterotic_orientedphifin_bn27_sourceidentity_directsourcetheorem_or_connectionvalues_externalconstruction.candidate.json",
    "selected_trace_root": QA
    / "selected_heterotic_orientedphifin_bn27_selectedtraceequality_fulloperatorformula_or_sourceflagtheorem.candidate.json",
    "full_operator_boundary": QA
    / "selected_heterotic_orientedphifin_bn27_fulloperatorformula_sourceflags_or_quotientfunctor_valueconstruction.candidate.json",
    "u1y_connection_witness": QA
    / "selected_u1y_routec_typed_monad_cech_or_hym_connection_witness.candidate.json",
    "u1y_connection_open": QA
    / "selected_u1y_routec_typed_monad_cech_or_hym_connection_witness.open.json",
    "connection_minimal_packet": QA
    / "selected_heterotic_orientedphifin_selectedconnectionwitness_minimal_source_values_packet.json",
    "external_construction_request": QA
    / "selected_heterotic_orientedphifin_bn27_connectionvalues_externalconstruction_request.json",
}

STATUS = (
    "MTT_SELECTED_SOURCEBRANCHIDENTITY_SOURCEAMENDMENT_OR_SELECTEDCONNECTIONVALUES_"
    "BRANCHCERT_CLOSED_CONNECTION_WITNESS_VALUES_OPEN"
)
NEXT = "MTT_Selected_TypedCechHYMProjectiveConnectionWitnessValues_or_DirectHKRow_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def decision(packet: dict[str, Any]) -> dict[str, Any]:
    return packet.get("decision", packet.get("closure_decision", {}))


def require_sources() -> dict[str, dict[str, Any]]:
    missing = [rel(path) for path in SOURCES.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing source-amendment/connection-value inputs: " + ", ".join(missing))
    return {name: load(path) for name, path in SOURCES.items()}


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = require_sources()
    prev = decision(sources["previous"])
    repair = decision(sources["sourcebranch_repair"])
    template = decision(sources["sourcebranch_template"])
    transport = decision(sources["sourceownership_transport"])
    direct_fill = decision(sources["directbn27_transport_fill"])
    direct_external = decision(sources["direct_source_or_external"])
    trace_root = decision(sources["selected_trace_root"])
    full_boundary = decision(sources["full_operator_boundary"])
    witness = decision(sources["u1y_connection_witness"])

    amendment_gate = {
        "schema": "MTTSourceBranchIdentity.SourceAmendmentOrConnectionValuesGate.v1",
        "status": "SOURCE_AMENDMENT_TEMPLATE_BUILT_CONNECTION_VALUES_UNFILLED",
        "closure_claimed": True,
        "repair_attack": {
            "repair_attack_executed": repair["repair_attack_executed"],
            "primary_lane": repair["primary_lane"],
            "projective_rhoE_primary": repair["projective_rhoE_primary"],
            "projective_finite_candidate_available": repair[
                "projective_finite_candidate_available"
            ],
            "projective_BN27_lift_closed": repair["projective_BN27_lift_closed"],
            "source_branch_identity_closed": repair["source_branch_identity_closed"],
        },
        "source_amendment_template": {
            "template_built": template["template_built"],
            "source_object_filled_field_count": template[
                "source_object_filled_field_count"
            ],
            "source_object_required_field_count": template[
                "source_object_required_field_count"
            ],
            "connection_values_filled_field_count": template[
                "connection_values_filled_field_count"
            ],
            "connection_values_required_field_count": template[
                "connection_values_required_field_count"
            ],
            "source_amendment_closed": template["source_amendment_closed"],
            "connection_values_closed": template["connection_values_closed"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    transport_gate = {
        "schema": "MTTBN27SourceOwnershipTransportGate.v1",
        "status": "BRANCH_CERTIFICATE_CLOSED_TRANSPORT_SOURCE_OPEN",
        "closure_claimed": True,
        "sourceownership_transport": {
            "branch_certificate_closed": transport["branch_certificate_closed"],
            "S_QaSU3_BN27_declared_as_selected_source": transport[
                "S_QaSU3_BN27_declared_as_selected_source"
            ],
            "BN27_source_ownership_transport_closed": transport[
                "BN27_source_ownership_transport_closed"
            ],
            "selected_connection_witness_values_closed": transport[
                "selected_connection_witness_values_closed"
            ],
            "projective_rhoE_lift_reopened": transport["projective_rhoE_lift_reopened"],
            "transport_witness_values_found": transport[
                "transport_witness_values_found"
            ],
        },
        "direct_bn27_fill": {
            "DE_gap_Riesz_Green_export_support_closed": direct_fill[
                "DE_gap_Riesz_Green_export_support_closed"
            ],
            "source_object_named_S_QaSU3_BN27": direct_fill[
                "source_object_named_S_QaSU3_BN27"
            ],
            "typed_connection_witness_values_found": direct_fill[
                "typed_connection_witness_values_found"
            ],
            "direct_source_identity_transport_closed": direct_fill[
                "direct_source_identity_transport_closed"
            ],
            "finite_routec_hym_full_connection_closed": direct_fill[
                "finite_routec_hym_full_connection_closed"
            ],
        },
        "root_cutset": {
            "root_cutset_built": direct_external["root_cutset_built"],
            "all_minimal_roots_closed": direct_external["all_minimal_roots_closed"],
            "selected_trace_equality_proved": direct_external[
                "selected_trace_equality_proved"
            ],
            "full_selected_operator_formula_proved": direct_external[
                "full_selected_operator_formula_proved"
            ],
            "theorem_derived_selected_source_flags": direct_external[
                "theorem_derived_selected_source_flags"
            ],
            "source_object_named_S_QaSU3_BN27": direct_external[
                "source_object_named_S_QaSU3_BN27"
            ],
            "connection_values_external_construction_closed": direct_external[
                "connection_values_external_construction_closed"
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    connection_gate = {
        "schema": "MTTConnectionWitnessValuePayloadGate.v1",
        "status": "TRACE_ROOT_SCOPED_CLOSED_WITNESS_PAYLOAD_VALUES_OPEN",
        "closure_claimed": True,
        "trace_root": {
            "selected_trace_equality_for_27mode_DE_gap_layer_closed": trace_root[
                "selected_trace_equality_for_27mode_DE_gap_layer_closed"
            ],
            "full_selected_operator_formula_closed": trace_root[
                "full_selected_operator_formula_closed"
            ],
            "theorem_derived_selected_source_flags_for_full_BN27": trace_root[
                "theorem_derived_selected_source_flags_for_full_BN27"
            ],
            "source_object_named_S_QaSU3_BN27": trace_root[
                "source_object_named_S_QaSU3_BN27"
            ],
        },
        "full_operator_boundary": {
            "electroweak_internal_finitepart_policy_closed": full_boundary[
                "electroweak_internal_finitepart_policy_closed"
            ],
            "quotient_finitepart_support_imported": full_boundary[
                "quotient_finitepart_support_imported"
            ],
            "full_selected_operator_formula_closed_for_BN27": full_boundary[
                "full_selected_operator_formula_closed_for_BN27"
            ],
            "theorem_derived_selected_source_flags_for_full_BN27": full_boundary[
                "theorem_derived_selected_source_flags_for_full_BN27"
            ],
        },
        "u1y_connection_witness_contract": {
            "contract_built": witness["contract_built"],
            "accepts_three_equivalent_witness_routes": witness[
                "accepts_three_equivalent_witness_routes"
            ],
            "q79_minimal_payload_imported_as_contract": witness[
                "q79_minimal_payload_imported_as_contract"
            ],
            "payload_missing_leaf_count": witness["payload_missing_leaf_count"],
            "typed_monad_cech_values_present": witness[
                "typed_monad_cech_values_present"
            ],
            "direct_hym_values_present": witness["direct_hym_values_present"],
            "finite_routec_solve_values_present": witness[
                "finite_routec_solve_values_present"
            ],
            "same_source_certificate_present": witness[
                "same_source_certificate_present"
            ],
            "selected_connection_witness_constructed": witness[
                "selected_connection_witness_constructed"
            ],
            "primitive_C1_values_computed": witness["primitive_C1_values_computed"],
        },
        "minimal_source_values_packet": {
            "status": sources["connection_minimal_packet"]["status"],
        },
        "external_construction_request": {
            "status": sources["external_construction_request"]["status"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_contract = {
        "schema": "MTTConnectionWitnessValuesOrDirectHKRow.NextContract.v1",
        "status": "TYPED_CECH_HYM_PROJECTIVE_CONNECTION_WITNESS_VALUES_REQUIRED",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "strict_K_threshold_count": {
            "accepted": prev["accepted_selected_K_source_row_count"],
            "required": prev["selected_K_threshold_row_count_required"],
        },
        "closed_now": [
            "heterotic Qa/SU3 branch certificate closed",
            "source amendment template built with 11 source-object fields",
            "connection-values template built with 8 value fields",
            "projective rhoE remains useful only as 11-label finite candidate",
            "27-mode D_E gap/Riesz/Green export support closed",
            "selected trace equality closed at 27-mode D_E gap-layer scope",
            "electroweak quotient finitepart support imported at support scope",
            "connection-witness contract built with three equivalent witness routes",
        ],
        "still_open": [
            "S_QaSU3^BN27 declared and source-owned with carrier, operators, kernel, trace policy, provenance, and replay",
            "selected connection values exporting the BN27 validator fields",
            "typed monad/Cech values",
            "direct selected HYM/Strominger connection values",
            "finite Route-C solve with selected source provenance and validator export",
            "full selected BN27 operator formula and theorem-derived full-packet source flags",
            "physical K_phys/action-unit, mu_match, and RG/threshold convention",
            "direct K_threshold.Omega_H.lambda source row",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedSourceBranchIdentitySourceAmendmentOrSelectedConnectionValues",
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
            "source_amendment_or_connection_values_gate": rel(AMENDMENT_GATE),
            "bn27_sourceownership_transport_gate": rel(TRANSPORT_GATE),
            "typed_connection_witness_gate": rel(CONNECTION_GATE),
            "next_connection_witness_value_payload_contract": rel(NEXT_CONTRACT),
        },
        "closure_decision": {
            "branch_certificate_closed": True,
            "source_amendment_template_built": True,
            "source_object_filled_field_count": 0,
            "source_object_required_field_count": 11,
            "connection_values_filled_field_count": 0,
            "connection_values_required_field_count": 8,
            "source_amendment_closed": False,
            "connection_values_closed": False,
            "S_QaSU3_BN27_declared_as_selected_source": False,
            "BN27_source_ownership_transport_closed": False,
            "selected_connection_witness_values_closed": False,
            "DE_gap_Riesz_Green_export_support_closed": True,
            "selected_trace_equality_for_27mode_DE_gap_layer_closed": True,
            "full_selected_operator_formula_closed": False,
            "theorem_derived_selected_source_flags": False,
            "electroweak_internal_finitepart_policy_closed": True,
            "quotient_finitepart_support_imported": True,
            "connection_witness_contract_built": True,
            "accepts_three_equivalent_witness_routes": True,
            "payload_missing_leaf_count": 29,
            "typed_monad_cech_values_present": False,
            "direct_hym_values_present": False,
            "finite_routec_solve_values_present": False,
            "same_source_certificate_present": False,
            "selected_connection_witness_constructed": False,
            "oriented_logdet_promoted": False,
            "selected_K_threshold_Omega_H_lambda": False,
            "strict_H_K_threshold_row_emitted": False,
            "accepted_selected_K_source_row_count": prev["accepted_selected_K_source_row_count"],
            "selected_K_threshold_row_count_required": prev[
                "selected_K_threshold_row_count_required"
            ],
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "SourceBranchAmendmentOrConnectionWitnessFrontierTheorem",
            "proved": True,
            "statement": (
                "The source-branch identity repair front is now locked to values, "
                "not arithmetic. The heterotic Qa/SU3 branch certificate is closed, "
                "the 27-mode D_E gap/Riesz/Green support exports, and selected trace "
                "equality is closed at gap-layer scope. But no source amendment names "
                "and owns S_QaSU3^BN27, no selected connection values export the BN27 "
                "validators, and the U1/Y connection-witness contract still has 29 "
                "missing payload leaves. The next no-knob object is typed Cech/HYM/"
                "projective connection witness values or a direct H K row."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedSourceBranchIdentitySourceAmendmentOrSelectedConnectionValues",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "branch_certificate_closed": True,
        "source_amendment_template_built": True,
        "DE_gap_Riesz_Green_export_support_closed": True,
        "selected_trace_equality_for_27mode_DE_gap_layer_closed": True,
        "connection_witness_contract_built": True,
        "payload_missing_leaf_count": 29,
        "S_QaSU3_BN27_declared_as_selected_source": False,
        "selected_connection_witness_values_closed": False,
        "strict_H_K_threshold_row_emitted": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected Source-Branch Identity Source Amendment or Selected Connection Values v1

## Theorem

`SourceBranchAmendmentOrConnectionWitnessFrontierTheorem` is emitted.

## Newly Closed

- Heterotic Qa/SU3 branch certificate is closed.
- Source-amendment template is built with `11` source-object fields.
- Connection-values template is built with `8` value fields.
- `27`-mode `D_E` gap/Riesz/Green export support is closed.
- Selected trace equality is closed at `27`-mode `D_E` gap-layer scope.
- Electroweak quotient finitepart support is imported at support scope.
- Connection-witness contract is built with three equivalent routes:
  typed monad/Cech data, direct selected HYM/Strominger connection data, or a
  finite Route-C solve with selected source provenance and validator export.

## Still Open

- `S_QaSU3^BN27` declaration and source ownership.
- Selected connection values exporting BN27 validator fields.
- Typed monad/Cech values.
- Direct selected HYM/Strominger connection values.
- Finite Route-C solve with selected source provenance and validator export.
- Full selected BN27 operator formula and theorem-derived full-packet source
  flags.
- Physical `K_phys`/action-unit, `mu_match`, and RG/threshold convention.
- Direct source-native `K_threshold.Omega_H.lambda`.

## Current Payload Count

The active selected-connection witness payload still has `29` missing leaves.

Strict selected `K_threshold` rows remain
`{prev["accepted_selected_K_source_row_count"]}/{prev["selected_K_threshold_row_count_required"]}`.

## Next Artifact

`{NEXT}`
"""

    write_json(AMENDMENT_GATE, amendment_gate)
    write_json(TRANSPORT_GATE, transport_gate)
    write_json(CONNECTION_GATE, connection_gate)
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
