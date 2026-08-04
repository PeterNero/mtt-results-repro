"""Build oriented Phi_fin source-ownership theorem / smooth E_Qa quotient frontier."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
QA = Path("C:/Users/nero_/Downloads/TEXPAPERS/mtt-qa-su3-packet-proof")

SLUG = "selected_orientedphifin_sourceownership_theorem_or_smootheqa_quotient"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_OrientedPhiFin_SourceOwnership_Theorem_or_SmoothEQa_Quotient_v1.md"

OWNERSHIP_ATTEMPT = PACKET_DIR / "sourceownership_theorem_attempt.packet.json"
TRANSPORT_REDUCTION = PACKET_DIR / "sourceidentity_transport_reduction.packet.json"
BRANCH_NOGO = PACKET_DIR / "sourcebranchidentity_current_source_nogo.packet.json"
BN27_TRANSPORT = PACKET_DIR / "bn27_sourceownership_transport_frontier.packet.json"
NEXT_CONTRACT = PACKET_DIR / "bn27_transport_or_connectionwitness_values_contract.packet.json"

PREVIOUS = DATA / "selected_orientedphifin_sourceownedpositiveoperator_or_eqapayload_fill.candidate.json"
PREVIOUS_NEXT = (
    DATA
    / "selected_orientedphifin_sourceownedpositiveoperator_or_eqapayload_fill"
    / "sourceownership_theorem_or_smootheqa_quotient_contract.packet.json"
)

QA_OWNERSHIP = QA / "candidate_data" / "selected_heterotic_orientedphifin_sourceownership_or_smootheqa_quotient.candidate.json"
QA_MINIMAL_TRANSPORT = QA / "candidate_data" / "selected_heterotic_orientedphifin_sourceidentitytransport_or_connectionvalues_minimalpacket.candidate.json"
QA_TRANSPORT_ATTEMPT = QA / "candidate_data" / "selected_heterotic_orientedphifin_sourceidentitytransport_proofattempt.candidate.json"
QA_BRANCH_NOGO = QA / "candidate_data" / "selected_heterotic_orientedphifin_sourcebranchidentity_emission_or_nogo.candidate.json"
QA_BRANCH_REPAIR = QA / "candidate_data" / "selected_heterotic_orientedphifin_sourcebranchidentity_sourceamendment_or_connectionvalues.candidate.json"
QA_PROJECTIVE_LIFT = QA / "candidate_data" / "selected_heterotic_orientedphifin_projectiverhoe_bn27lift_or_directsource_theorem.candidate.json"
QA_SELECTED_BUNDLE_OR_DIRECT = QA / "candidate_data" / "selected_heterotic_orientedphifin_selectedbundleA_or_directbn27_sourceemission.candidate.json"
QA_BN27_CERT = QA / "candidate_data" / "selected_heterotic_orientedphifin_sourceowned_bn27_certificate_or_bundleA_selector.candidate.json"
QA_BN27_TRANSPORT = QA / "candidate_data" / "selected_heterotic_orientedphifin_bn27_sourceownership_transport_or_connectionwitness_values.candidate.json"
QA_TRANSPORT_TEMPLATE = QA / "candidate_data" / "selected_heterotic_orientedphifin_bn27_sourceownership_transport_witness.template.json"

STATUS = (
    "MTT_SELECTED_ORIENTEDPHIFIN_SOURCEOWNERSHIP_THEOREM_OR_SMOOTHEQA_QUOTIENT_"
    "BUILT_BRANCHCERT_CLOSED_BN27_TRANSPORT_OPEN"
)
NEXT = "MTT_Selected_OrientedPhiFin_BN27SourceOwnershipTransport_or_ConnectionWitnessValues_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    previous = load(PREVIOUS)
    previous_next = load(PREVIOUS_NEXT)
    ownership = load(QA_OWNERSHIP)
    minimal_transport = load(QA_MINIMAL_TRANSPORT)
    transport_attempt = load(QA_TRANSPORT_ATTEMPT)
    branch_nogo = load(QA_BRANCH_NOGO)
    branch_repair = load(QA_BRANCH_REPAIR)
    projective_lift = load(QA_PROJECTIVE_LIFT)
    selected_bundle_or_direct = load(QA_SELECTED_BUNDLE_OR_DIRECT)
    bn27_cert = load(QA_BN27_CERT)
    bn27_transport = load(QA_BN27_TRANSPORT)
    transport_template = load(QA_TRANSPORT_TEMPLATE)

    support_clause_count = branch_nogo["decision"]["support_count"]
    required_clause_count = branch_nogo["decision"]["required_clause_count"]
    emitted_clause_count = branch_nogo["decision"]["emitted_count"]

    ownership_attempt_packet = {
        "schema": "MTTOrientedPhiFinSourceOwnershipAttempt.v1",
        "status": "SOURCEOWNERSHIP_ATTEMPT_CURRENT_SOURCE_NOGO",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "source": rel(QA_OWNERSHIP),
        "source_ownership_lane": ownership["lanes"]["source_ownership_theorem"],
        "smooth_EQa_lane": ownership["lanes"]["smooth_EQa_quotient_theorem"],
        "operator_payload_ready_retained": ownership["decision"]["operator_payload_ready_retained"],
        "source_ownership_closed": ownership["decision"]["source_ownership_closed"],
        "smooth_EQa_quotient_closed": ownership["decision"]["smooth_EQa_quotient_closed"],
        "finitepart_trace_identity_closed": ownership["decision"]["finitepart_trace_identity_closed"],
        "oriented_logdet_promoted": ownership["decision"]["oriented_logdet_promoted"],
    }

    transport_reduction_packet = {
        "schema": "MTTSourceIdentityTransportReduction.v1",
        "status": "TRANSPORT_REDUCED_TO_SOURCEBRANCHIDENTITY",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "minimal_packet": rel(QA_MINIMAL_TRANSPORT),
        "proof_attempt": rel(QA_TRANSPORT_ATTEMPT),
        "primary_route": minimal_transport["decision"]["primary_route_selected"],
        "support_prefilter_passes": minimal_transport["decision"]["support_prefilter_passes"],
        "conditional_sublemmas": {
            "operator_coemission_before_finite_comparison": transport_attempt["sublemma_attempts"][
                "operator_coemission_before_finite_comparison"
            ],
            "no_lift_audit_replay_from_emitted_source": transport_attempt["sublemma_attempts"][
                "no_lift_audit_replay_from_emitted_source"
            ],
        },
        "single_remaining_leaf": transport_attempt["decision"]["single_remaining_leaf"],
        "source_branch_identity_closed": transport_attempt["decision"]["source_branch_identity_closed"],
        "transport_closed": transport_attempt["decision"]["source_branch_identity_closed"]
        and transport_attempt["decision"]["operator_coemission_unconditional_closed"]
        and transport_attempt["decision"]["no_lift_replay_unconditional_closed"],
    }

    branch_nogo_packet = {
        "schema": "MTTSourceBranchIdentityCurrentSourceNoGo.v1",
        "status": "SOURCEBRANCHIDENTITY_SUPPORT_PRESENT_ZERO_EMITTED",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "source": rel(QA_BRANCH_NOGO),
        "clauses": branch_nogo["clauses"],
        "support_count": support_clause_count,
        "required_clause_count": required_clause_count,
        "emitted_count": emitted_clause_count,
        "source_branch_identity_closed": branch_nogo["decision"]["source_branch_identity_closed"],
        "transport_reduced_leaf_resolved": branch_nogo["decision"]["transport_reduced_leaf_resolved"],
        "repair_packet_built": branch_nogo["decision"]["repair_packet_built"],
    }

    bn27_transport_packet = {
        "schema": "MTTBN27SourceOwnershipTransportFrontier.v1",
        "status": "BRANCH_CERT_CLOSED_BN27_SOURCEOWNERSHIP_TRANSPORT_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "sources": {
            "branch_repair": rel(QA_BRANCH_REPAIR),
            "projective_lift": rel(QA_PROJECTIVE_LIFT),
            "selected_bundle_or_direct": rel(QA_SELECTED_BUNDLE_OR_DIRECT),
            "bn27_certificate": rel(QA_BN27_CERT),
            "bn27_transport": rel(QA_BN27_TRANSPORT),
            "transport_template": rel(QA_TRANSPORT_TEMPLATE),
        },
        "branch_certificate_closed": bn27_transport["decision"]["branch_certificate_closed"],
        "BN27_source_ownership_transport_closed": bn27_transport["decision"][
            "BN27_source_ownership_transport_closed"
        ],
        "selected_connection_witness_values_closed": bn27_transport["decision"][
            "selected_connection_witness_values_closed"
        ],
        "direct_BN27_source_declaration_closed": bn27_transport["decision"][
            "direct_BN27_source_declaration_closed"
        ],
        "projective_rhoE_lift_reopened": bn27_transport["decision"]["projective_rhoE_lift_reopened"],
        "BN27_source_ownership_fields": bn27_transport["BN27_source_ownership_fields"],
        "support_now_locked": bn27_transport["support_now_locked"],
        "route_ranking": bn27_transport["route_ranking"],
        "projective_lift_no_go": {
            "projective_rhoE_BN27_lift_closed": projective_lift["decision"][
                "projective_rhoE_BN27_lift_closed"
            ],
            "missing_positive_oriented_row_count": projective_lift["lift_tests"]["domain_lift"][
                "missing_positive_oriented_row_count"
            ],
            "missing_multiplier_to_full_abs_sector": projective_lift["lift_tests"]["domain_lift"][
                "missing_multiplier_to_full_abs_sector"
            ],
            "operator_lift_passes": projective_lift["lift_tests"]["operator_lift"]["passes"],
        },
        "unselected_substitutes_rejected": {
            "standard_embedding_promoted": selected_bundle_or_direct["decision"]["standard_embedding_promoted"],
            "finite_projective_rhoE_promoted_to_smooth_A": selected_bundle_or_direct["decision"][
                "finite_projective_rhoE_promoted_to_smooth_A"
            ],
            "direct_BN27_source_emitted": selected_bundle_or_direct["decision"]["direct_BN27_source_emitted"],
            "selected_bundle_A_emitted": selected_bundle_or_direct["decision"]["selected_bundle_A_emitted"],
        },
    }

    next_contract = {
        "schema": "MTTBN27TransportOrConnectionWitnessValuesContract.v1",
        "status": "NEXT_IS_BN27_SOURCEOWNERSHIP_TRANSPORT_OR_CONNECTIONWITNESS_VALUES",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
        "must_emit_one_of": [
            "same-branch source theorem naming S_QaSU3^BN27 as selected source",
            "full F3xF3 rank-slot BN27 carrier emission before finite comparison",
            "selected connection witness values exporting deck/operator/kernel/trace/finitepart to BN27",
            "smooth E_Qa quotient values producing the oriented BN27 packet",
        ],
        "required_closed_payload": transport_template["required_closed_payload"],
        "connection_values_family": transport_template["connection_values_family"],
        "must_not_use": transport_template["forbidden_shortcuts"]
        + [
            "projective 11-label rho_E shadow as full BN27 threshold proof",
            "branch certificate alone as BN27 source ownership",
        ],
    }

    decision = {
        "previous_frontier_honored": previous["next_required_artifact"]
        == "MTT_Selected_OrientedPhiFin_SourceOwnership_Theorem_or_SmoothEQa_Quotient_v1",
        "sourceownership_attempted": True,
        "source_ownership_closed": False,
        "smooth_EQa_quotient_closed": False,
        "transport_reduced_to_sourcebranchidentity": True,
        "source_branch_identity_support_count": support_clause_count,
        "source_branch_identity_required_clause_count": required_clause_count,
        "source_branch_identity_emitted_count": emitted_clause_count,
        "source_branch_identity_closed": False,
        "branch_certificate_closed": bn27_transport["decision"]["branch_certificate_closed"],
        "BN27_source_ownership_transport_closed": False,
        "selected_connection_witness_values_closed": False,
        "direct_BN27_source_declaration_closed": False,
        "projective_rhoE_lift_retired_as_threshold_proof": True,
        "oriented_logdet_promoted": False,
        "strict_P_EW_source_rows": 0,
        "strict_direct_K_threshold_Omega_H_lambda_rows": 0,
        "full_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
    }

    candidate = {
        "candidate": "MTTSelectedOrientedPhiFinSourceOwnershipTheoremOrSmoothEQaQuotient",
        "status": STATUS,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {
            "previous_candidate": rel(PREVIOUS),
            "previous_next_contract": rel(PREVIOUS_NEXT),
            "qasu3_sourceownership_attempt": rel(QA_OWNERSHIP),
            "qasu3_minimal_transport": rel(QA_MINIMAL_TRANSPORT),
            "qasu3_transport_attempt": rel(QA_TRANSPORT_ATTEMPT),
            "qasu3_branch_nogo": rel(QA_BRANCH_NOGO),
            "qasu3_branch_repair": rel(QA_BRANCH_REPAIR),
            "qasu3_projective_lift": rel(QA_PROJECTIVE_LIFT),
            "qasu3_selected_bundle_or_direct": rel(QA_SELECTED_BUNDLE_OR_DIRECT),
            "qasu3_bn27_certificate": rel(QA_BN27_CERT),
            "qasu3_bn27_transport": rel(QA_BN27_TRANSPORT),
            "qasu3_transport_template": rel(QA_TRANSPORT_TEMPLATE),
        },
        "output_packets": {
            "sourceownership_theorem_attempt": rel(OWNERSHIP_ATTEMPT),
            "sourceidentity_transport_reduction": rel(TRANSPORT_REDUCTION),
            "sourcebranchidentity_current_source_nogo": rel(BRANCH_NOGO),
            "bn27_sourceownership_transport_frontier": rel(BN27_TRANSPORT),
            "bn27_transport_or_connectionwitness_values_contract": rel(NEXT_CONTRACT),
        },
        "closure_decision": decision,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "OrientedPhiFinSourceOwnershipOrSmoothEQaQuotientFrontierTheorem",
            "proved": True,
            "statement": (
                "The source-ownership theorem has been attempted and reduced: operator co-emission and "
                "no-lift replay are conditionally ready, but source-branch identity is not emitted.  The "
                "heterotic branch certificate is now closed, improving provenance, but it does not declare "
                "S_QaSU3^BN27 or export the full BN27 carrier/operator/kernel/trace/finitepart payload.  "
                "The next exact object is BN27 source-ownership transport or selected connection-witness values."
            ),
        },
    }

    cert = {
        "certificate": "MTT_Selected_OrientedPhiFin_SourceOwnership_Theorem_or_SmoothEQa_Quotient_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        **decision,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected OrientedPhiFin SourceOwnership Theorem or SmoothEQa Quotient v1

Status: `{STATUS}`.

## Result

The source-ownership theorem has now been attempted and reduced.

```text
source ownership closed             : false
smooth E_Qa quotient closed          : false
transport reduced to one leaf        : true
single remaining leaf                : source_branch_identity
source-branch support clauses        : {support_clause_count}/{required_clause_count}
source-branch emitted clauses        : {emitted_clause_count}/{required_clause_count}
branch certificate closed            : {str(bn27_transport["decision"]["branch_certificate_closed"]).lower()}
BN27 transport closed                : false
```

The important progress is that operator co-emission and no-lift audit replay are
conditionally ready.  The branch certificate is also closed.  What is still not
emitted is the BN27 ownership transport itself: the source has not declared
`S_QaSU3^BN27`, exported the full `F3xF3` rank-slot carrier, or proved the
non-Route-C-import provenance.

## Next

Next artifact: `{NEXT}`.
"""

    write_json(OWNERSHIP_ATTEMPT, ownership_attempt_packet)
    write_json(TRANSPORT_REDUCTION, transport_reduction_packet)
    write_json(BRANCH_NOGO, branch_nogo_packet)
    write_json(BN27_TRANSPORT, bn27_transport_packet)
    write_json(NEXT_CONTRACT, next_contract)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
