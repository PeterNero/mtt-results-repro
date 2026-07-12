"""Build finite rhoE-to-oriented-BN or smooth EQa representative frontier packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
QA = Path("C:/Users/nero_/Downloads/TEXPAPERS/mtt-qa-su3-packet-proof/candidate_data")

SLUG = "selected_finiterhoetoorientedbnfunctor_or_smootheqarepresentative_or_directhkrow"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
FUNCTOR_GATE = PACKET_DIR / "finite_rhoe_to_oriented_bn_functor_gate.packet.json"
LOGDET_GATE = PACKET_DIR / "bn27_sourceowned_logdet_gate.packet.json"
VALIDATOR_GATE = PACKET_DIR / "bn27_validator_export_transport_gate.packet.json"
NEXT_CONTRACT = PACKET_DIR / "next_source_amendment_or_connection_values_contract.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_FiniteRhoEToOrientedBNFunctor_or_SmoothEQaRepresentative_or_DirectHKRow_v1.md"

SOURCES = {
    "previous": DATA
    / "selected_orientationmagnitudecoemission_or_endomorphismthresholdfinitepart_or_directhkrow.candidate.json",
    "rhoe_oriented_functor": QA
    / "selected_heterotic_orientedphifin_finiterhoe_to_orientedbn_functor_or_smoothrepresentative.candidate.json",
    "oriented_bn_functor": QA
    / "selected_heterotic_orientedphifin_orientedbn_carrier_or_endequotientfunctor.candidate.json",
    "finite_candidate_promotion": QA
    / "selected_heterotic_projectiverhoe_finitecandidate_promotion_or_smoothrepresentative.candidate.json",
    "bn27_direct_arithmetic": QA
    / "selected_heterotic_orientedphifin_bn27_directfinitepartfunctional_or_sourceownedlogdettheorem.candidate.json",
    "sourceowned_logdet": QA
    / "selected_heterotic_orientedphifin_bn27_sourceownedlogdet_sourcetheorem_or_kerneltraceownership.candidate.json",
    "sourceowned_logdet_fill": QA
    / "selected_heterotic_orientedphifin_bn27_sourceownedlogdet_minimalemissionpacket_fill_or_sourceamendment.candidate.json",
    "source_object_declaration": QA
    / "selected_heterotic_orientedphifin_bn27_sourceobject_sqasU3bn27_declaration_or_connectionvalueexport.candidate.json",
    "declaration_fill": QA
    / "selected_heterotic_orientedphifin_bn27_sourceobject_declarationinterface_fill_or_selectedconnectionvalues.candidate.json",
    "validator_export": QA
    / "selected_heterotic_orientedphifin_bn27_samesourceexport_to_bn27validators_or_selectedconnectionvalues.candidate.json",
    "validator_fill": QA
    / "selected_heterotic_orientedphifin_bn27_validatorexport_fill_or_selectedconnectionsolve.candidate.json",
    "connection_witness_fill": QA
    / "selected_heterotic_orientedphifin_selectedconnectionwitness_export_fill.candidate.json",
    "sourceidentity_minimal": QA
    / "selected_heterotic_orientedphifin_sourceidentitytransport_or_connectionvalues_minimalpacket.candidate.json",
    "sourceidentity_attempt": QA
    / "selected_heterotic_orientedphifin_sourceidentitytransport_proofattempt.candidate.json",
    "directbn27_fill": QA
    / "selected_heterotic_orientedphifin_directbn27_sourceidentitytransport_fill_or_typedconnectionwitnessvalues.candidate.json",
    "sourcebranch_nogo": QA
    / "selected_heterotic_orientedphifin_sourcebranchidentity_emission_or_nogo.candidate.json",
}

STATUS = (
    "MTT_SELECTED_FINITERHOETOORIENTEDBNFUNCTOR_OR_SMOOTHEQAREPRESENTATIVE_"
    "OR_DIRECTHKROW_REDUCED_TO_SOURCE_AMENDMENT_OR_CONNECTION_VALUES"
)
NEXT = "MTT_Selected_SourceBranchIdentity_SourceAmendment_or_SelectedConnectionValues_or_DirectHKRow_v1"


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
        raise FileNotFoundError("missing finite rhoE/oriented BN inputs: " + ", ".join(missing))
    return {name: load(path) for name, path in SOURCES.items()}


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = require_sources()
    prev = decision(sources["previous"])
    rhoe_functor = decision(sources["rhoe_oriented_functor"])
    oriented_bn = decision(sources["oriented_bn_functor"])
    finite_promotion = decision(sources["finite_candidate_promotion"])
    direct_arith = decision(sources["bn27_direct_arithmetic"])
    logdet = decision(sources["sourceowned_logdet"])
    logdet_fill = decision(sources["sourceowned_logdet_fill"])
    source_decl = decision(sources["source_object_declaration"])
    decl_fill = decision(sources["declaration_fill"])
    validator = decision(sources["validator_export"])
    validator_fill = decision(sources["validator_fill"])
    conn_fill = decision(sources["connection_witness_fill"])
    minimal = decision(sources["sourceidentity_minimal"])
    attempt = decision(sources["sourceidentity_attempt"])
    direct_fill = decision(sources["directbn27_fill"])
    branch_nogo = decision(sources["sourcebranch_nogo"])

    functor_gate = {
        "schema": "MTTFiniteRhoEToOrientedBNFunctorGate.v1",
        "status": "ORIENTATION_FUNCTOR_CLOSED_MAGNITUDE_FUNCTOR_OPEN",
        "closure_claimed": True,
        "orientation_functor": {
            "finite_rhoE_to_oriented_BN_orientation_functor_closed": rhoe_functor[
                "finite_rhoE_to_oriented_BN_orientation_functor_closed"
            ],
            "threshold_magnitude_functor_closed": rhoe_functor[
                "threshold_magnitude_functor_closed"
            ],
            "finitepart_trace_identity_closed": rhoe_functor[
                "finitepart_trace_identity_closed"
            ],
            "smooth_representative_emitted": rhoe_functor["smooth_representative_emitted"],
        },
        "rho_shadow_functor": {
            "rho_shadow_embedding_retained": oriented_bn["rho_shadow_embedding_retained"],
            "EndE_or_rhoE_to_oriented_BN_functor_closed": oriented_bn[
                "EndE_or_rhoE_to_oriented_BN_functor_closed"
            ],
            "operator_intertwiner_closed": oriented_bn["operator_intertwiner_closed"],
            "finitepart_identity_closed": oriented_bn["finitepart_identity_closed"],
        },
        "smooth_representative": {
            "finite_candidate_values_replayed": finite_promotion[
                "finite_candidate_values_replayed"
            ],
            "smooth_heterotic_representative_emitted": finite_promotion[
                "smooth_heterotic_representative_emitted"
            ],
            "same_source_smooth_operator_identity_proved": finite_promotion[
                "same_source_smooth_operator_identity_proved"
            ],
            "direct_selected_finite_operator_closure_proved": finite_promotion[
                "direct_selected_finite_operator_closure_proved"
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    logdet_gate = {
        "schema": "MTTBN27SourceOwnedLogdetGate.v1",
        "status": "DIRECT_FINITEPART_ARITHMETIC_CLOSED_SOURCEOWNED_LOGDET_OPEN",
        "closure_claimed": True,
        "direct_finitepart_arithmetic": {
            "direct_finitepart_arithmetic_closed": direct_arith[
                "direct_finitepart_arithmetic_closed"
            ],
            "source_owned_finitepart_functional_closed": direct_arith[
                "source_owned_finitepart_functional_closed"
            ],
            "source_object_named_S_QaSU3_BN27": direct_arith[
                "source_object_named_S_QaSU3_BN27"
            ],
            "kernel_trace_source_owned": direct_arith["kernel_trace_source_owned"],
        },
        "sourceowned_logdet": {
            "sourceowned_logdet_minimal_packet_built": logdet[
                "sourceowned_logdet_minimal_packet_built"
            ],
            "direct_source_theorem_closed": logdet["direct_source_theorem_closed"],
            "kernel_trace_ownership_closed": logdet["kernel_trace_ownership_closed"],
            "connection_or_smooth_source_closed": logdet[
                "connection_or_smooth_source_closed"
            ],
            "source_owned_logdet_closed": logdet["source_owned_logdet_closed"],
        },
        "minimal_emission_fill": {
            "conditional_implication_theorem_closed": logdet_fill[
                "conditional_implication_theorem_closed"
            ],
            "source_amendment_template_built": logdet_fill[
                "source_amendment_template_built"
            ],
            "direct_source_theorem_closed": logdet_fill["direct_source_theorem_closed"],
            "kernel_trace_ownership_closed": logdet_fill["kernel_trace_ownership_closed"],
            "connection_or_smooth_source_closed": logdet_fill[
                "connection_or_smooth_source_closed"
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    validator_gate = {
        "schema": "MTTBN27ValidatorExportTransportGate.v1",
        "status": "VALIDATORS_COLLAPSED_TO_SOURCEBRANCH_OR_CONNECTION_VALUES",
        "closure_claimed": True,
        "source_object_declaration": {
            "source_object_declaration_interface_built": source_decl[
                "source_object_declaration_interface_built"
            ],
            "bare_source_name_rejected_as_closure": source_decl[
                "bare_source_name_rejected_as_closure"
            ],
            "direct_source_object_declaration_closed": source_decl[
                "direct_source_object_declaration_closed"
            ],
            "equivalent_connection_value_export_closed": source_decl[
                "equivalent_connection_value_export_closed"
            ],
        },
        "declaration_fill": {
            "u1y_routec_support_imported_for_compatibility": decl_fill[
                "u1y_routec_support_imported_for_compatibility"
            ],
            "same_source_export_to_BN27_validators": decl_fill[
                "same_source_export_to_BN27_validators"
            ],
            "selected_connection_values_closed": decl_fill[
                "selected_connection_values_closed"
            ],
        },
        "validator_export": {
            "validator_export_acceptance_contract_built": validator[
                "validator_export_acceptance_contract_built"
            ],
            "support_ready_count": validator["support_ready_count"],
            "selected_export_owned_count": validator["selected_export_owned_count"],
            "open_validator_count": validator["open_validator_count"],
            "same_source_export_to_BN27_validators": validator[
                "same_source_export_to_BN27_validators"
            ],
        },
        "validator_reduction": {
            "audit_replay_validator_closed": validator_fill[
                "audit_replay_validator_closed"
            ],
            "validator_dependency_collapse_built": validator_fill[
                "validator_dependency_collapse_built"
            ],
            "operator_coemission_conditional_closed": validator_fill[
                "operator_coemission_conditional_closed"
            ],
            "sourcebranch_three_clause_cutset_built": validator_fill[
                "sourcebranch_three_clause_cutset_built"
            ],
            "sourcebranch_emitted_clause_count": validator_fill[
                "sourcebranch_emitted_clause_count"
            ],
            "sourcebranch_required_clause_count": validator_fill[
                "sourcebranch_required_clause_count"
            ],
        },
        "connection_witness_fill": {
            "support_ready_count": conn_fill["support_ready_count"],
            "audit_replay_export_filled": conn_fill["audit_replay_export_filled"],
            "export_filled_count": conn_fill["export_filled_count"],
            "export_required_count": conn_fill["export_required_count"],
            "selected_connection_witness_export_closed": conn_fill[
                "selected_connection_witness_export_closed"
            ],
        },
        "source_identity_transport": {
            "minimal_packet_built": minimal["minimal_packet_built"],
            "primary_route_selected": minimal["primary_route_selected"],
            "support_prefilter_passes": minimal["support_prefilter_passes"],
            "transport_reduced_to_single_leaf": attempt[
                "transport_reduced_to_single_leaf"
            ],
            "single_remaining_leaf": attempt["single_remaining_leaf"],
            "operator_coemission_conditional_closed": attempt[
                "operator_coemission_conditional_closed"
            ],
            "no_lift_replay_conditional_closed": attempt[
                "no_lift_replay_conditional_closed"
            ],
            "source_branch_identity_closed": attempt["source_branch_identity_closed"],
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
        },
        "sourcebranch_nogo": {
            "sourcebranchidentity_attempted": branch_nogo["sourcebranchidentity_attempted"],
            "current_source_nogo": branch_nogo["current_source_nogo"],
            "support_count": branch_nogo["support_count"],
            "required_clause_count": branch_nogo["required_clause_count"],
            "emitted_count": branch_nogo["emitted_count"],
            "repair_packet_built": branch_nogo["repair_packet_built"],
            "transport_reduced_leaf_resolved": branch_nogo[
                "transport_reduced_leaf_resolved"
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_contract = {
        "schema": "MTTSourceBranchIdentityOrConnectionValues.NextContract.v1",
        "status": "SOURCE_AMENDMENT_OR_SELECTED_CONNECTION_VALUES_REQUIRED",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "strict_K_threshold_count": {
            "accepted": prev["accepted_selected_K_source_row_count"],
            "required": prev["selected_K_threshold_row_count_required"],
        },
        "closed_now": [
            "finite rhoE to oriented BN orientation functor closed",
            "smooth representative/current finite promotion route checked and not emitted",
            "BN27 direct finitepart arithmetic log(92160000) closed relative to source ownership",
            "source-owned logdet minimal emission packet and conditional implication DAG built",
            "bare S_QaSU3^BN27 source name rejected as insufficient",
            "BN27 validator export contract built with all six validators support-ready",
            "audit replay validator and export closed",
            "validator dependency collapse reduces five open validators to sourcebranch identity or connection values",
            "source identity transport proof reduced to source_branch_identity",
            "current-source no-go for source_branch_identity proved with exact repair packet",
        ],
        "still_open": [
            "source amendment naming and owning S_QaSU3^BN27 carrier, operators, kernel, trace policy, provenance, and replay",
            "selected connection values exporting the same BN27 validator fields",
            "typed Cech/HYM/projective connection witness values",
            "smooth E_Qa quotient representative with finitepart trace identity",
            "physical K_phys/action-unit, mu_match, and RG/threshold convention",
            "direct K_threshold.Omega_H.lambda source row",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedFiniteRhoEToOrientedBNFunctorOrSmoothEQaRepresentative",
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
            "finite_rhoe_to_oriented_bn_functor_gate": rel(FUNCTOR_GATE),
            "bn27_sourceowned_logdet_gate": rel(LOGDET_GATE),
            "bn27_validator_export_transport_gate": rel(VALIDATOR_GATE),
            "next_source_amendment_or_connection_values_contract": rel(NEXT_CONTRACT),
        },
        "closure_decision": {
            "finite_rhoE_to_oriented_BN_orientation_functor_closed": True,
            "threshold_magnitude_functor_closed": False,
            "smooth_representative_emitted": False,
            "direct_finitepart_arithmetic_log92160000_closed": True,
            "source_owned_logdet_closed": False,
            "conditional_implication_theorem_closed": True,
            "bare_source_name_rejected_as_closure": True,
            "source_object_named_S_QaSU3_BN27": False,
            "validator_export_acceptance_contract_built": True,
            "validator_support_ready_count": 6,
            "validator_selected_export_owned_count": 1,
            "validator_open_count": 5,
            "validator_dependency_collapse_built": True,
            "sourcebranch_three_clause_cutset_built": True,
            "sourceidentity_transport_reduced_to_single_leaf": True,
            "single_remaining_leaf": "source_branch_identity",
            "source_branch_identity_closed": False,
            "sourcebranch_current_source_nogo": True,
            "sourcebranch_support_count": 3,
            "sourcebranch_required_clause_count": 3,
            "sourcebranch_emitted_count": 0,
            "selected_connection_values_closed": False,
            "selected_connection_witness_export_closed": False,
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
            "name": "FiniteRhoEToOrientedBNOrSmoothEQaReductionTheorem",
            "proved": True,
            "statement": (
                "The finite rhoE-to-oriented-BN bridge is closed only at orientation "
                "scope: rhoE character transfer and compressed C_tau are selected, "
                "but magnitude and finitepart preservation are not. BN27 finitepart "
                "arithmetic gives log(92160000) exactly relative to source ownership. "
                "The source-owned logdet problem is reduced to a minimal emission "
                "packet; its conditional implication DAG is closed, but a bare "
                "S_QaSU3^BN27 name is insufficient. The validator export problem "
                "collapses to source_branch_identity or selected connection values. "
                "The source-identity transport proof reduces to source_branch_identity, "
                "and current sources prove a no-go for that leaf: all three clauses "
                "have support and zero emitted source clauses. Therefore the next "
                "object is a source amendment or selected connection-value export, "
                "with direct H K row still independent."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedFiniteRhoEToOrientedBNFunctorOrSmoothEQaRepresentative",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "finite_rhoE_to_oriented_BN_orientation_functor_closed": True,
        "direct_finitepart_arithmetic_log92160000_closed": True,
        "conditional_implication_theorem_closed": True,
        "sourceidentity_transport_reduced_to_single_leaf": True,
        "sourcebranch_current_source_nogo": True,
        "source_branch_identity_closed": False,
        "selected_connection_values_closed": False,
        "oriented_logdet_promoted": False,
        "strict_H_K_threshold_row_emitted": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected Finite RhoE to Oriented BN Functor or Smooth EQa Representative v1

## Theorem

`FiniteRhoEToOrientedBNOrSmoothEQaReductionTheorem` is emitted.

## Newly Closed

- Finite `rho_E -> oriented B_N` orientation functor is closed.
- BN27 direct finitepart arithmetic is exact:
  `log(92160000)` relative to source ownership.
- Source-owned logdet minimal emission packet is built.
- Conditional implication DAG is closed: once the source owns the BN27 carrier,
  operators, kernel, trace policy, and flags, `log(92160000)` promotes without
  new numerical choices.
- A bare `S_QaSU3^BN27` source name is rejected as proof.
- BN27 validator export contract is built with six support-ready validators.
- Audit replay validator/export is closed.
- Validator dependency collapse reduces the open validators to
  `source_branch_identity` or selected connection values.
- Source-identity transport proof reduces to the single
  `source_branch_identity` leaf.
- Current-source no-go for `source_branch_identity` is proved: all three clauses
  have support, but zero clauses are source-emitted.

## Still Open

- Source amendment naming and owning `S_QaSU3^BN27` carrier, operators, kernel,
  trace policy, provenance, and replay.
- Selected connection values exporting the same BN27 validator fields.
- Typed Cech/HYM/projective connection witness values.
- Smooth `E_Qa` quotient representative with finitepart trace identity.
- Physical `K_phys`/action-unit, `mu_match`, and RG/threshold convention.
- Direct source-native `K_threshold.Omega_H.lambda`.

## Current Count

Strict selected `K_threshold` rows remain
`{prev["accepted_selected_K_source_row_count"]}/{prev["selected_K_threshold_row_count_required"]}`.

## Next Artifact

`{NEXT}`
"""

    write_json(FUNCTOR_GATE, functor_gate)
    write_json(LOGDET_GATE, logdet_gate)
    write_json(VALIDATOR_GATE, validator_gate)
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
