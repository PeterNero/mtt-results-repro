"""Audit oriented Phi_fin source-ownership theorem / smooth E_Qa quotient frontier."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
BUILDER = ROOT / "scripts" / "build_selected_orientedphifin_sourceownership_theorem_or_smootheqa_quotient.py"

SLUG = "selected_orientedphifin_sourceownership_theorem_or_smootheqa_quotient"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_OrientedPhiFin_SourceOwnership_Theorem_or_SmoothEQa_Quotient_v1.md"

OWNERSHIP_ATTEMPT = PACKET_DIR / "sourceownership_theorem_attempt.packet.json"
TRANSPORT_REDUCTION = PACKET_DIR / "sourceidentity_transport_reduction.packet.json"
BRANCH_NOGO = PACKET_DIR / "sourcebranchidentity_current_source_nogo.packet.json"
BN27_TRANSPORT = PACKET_DIR / "bn27_sourceownership_transport_frontier.packet.json"
NEXT_CONTRACT = PACKET_DIR / "bn27_transport_or_connectionwitness_values_contract.packet.json"

STATUS = (
    "MTT_SELECTED_ORIENTEDPHIFIN_SOURCEOWNERSHIP_THEOREM_OR_SMOOTHEQA_QUOTIENT_"
    "BUILT_BRANCHCERT_CLOSED_BN27_TRANSPORT_OPEN"
)
NEXT = "MTT_Selected_OrientedPhiFin_BN27SourceOwnershipTransport_or_ConnectionWitnessValues_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    ownership = load(OWNERSHIP_ATTEMPT)
    transport = load(TRANSPORT_REDUCTION)
    branch = load(BRANCH_NOGO)
    bn27 = load(BN27_TRANSPORT)
    next_contract = load(NEXT_CONTRACT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(next_contract["next_required_artifact"] == NEXT, "next contract mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem flag missing")

    for payload in [candidate, cert, ownership, transport, branch, bn27, next_contract]:
        require(payload["closure_claimed"] is True, "closure boundary missing")
        require(payload["observed_data_used_as_selector"] is False, "observed selector used")
        require(payload["target_fitting_used"] is False, "target fitting used")

    decision = candidate["closure_decision"]
    require(decision["previous_frontier_honored"] is True, "previous frontier not honored")
    require(decision["sourceownership_attempted"] is True, "source ownership not attempted")
    require(decision["transport_reduced_to_sourcebranchidentity"] is True, "transport reduction missing")
    require(decision["source_branch_identity_support_count"] == 3, "source branch support count mismatch")
    require(decision["source_branch_identity_required_clause_count"] == 3, "source branch required count mismatch")
    require(decision["source_branch_identity_emitted_count"] == 0, "source branch clauses overemitted")
    require(decision["branch_certificate_closed"] is True, "branch certificate not closed")
    require(decision["projective_rhoE_lift_retired_as_threshold_proof"] is True, "projective lift not retired")
    for key in [
        "source_ownership_closed",
        "smooth_EQa_quotient_closed",
        "source_branch_identity_closed",
        "BN27_source_ownership_transport_closed",
        "selected_connection_witness_values_closed",
        "direct_BN27_source_declaration_closed",
        "oriented_logdet_promoted",
        "full_no_knob_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"overclosed: {key}")
    require(decision["strict_P_EW_source_rows"] == 0, "strict P_EW overaccepted")
    require(decision["strict_direct_K_threshold_Omega_H_lambda_rows"] == 0, "direct K overaccepted")

    require(ownership["status"] == "SOURCEOWNERSHIP_ATTEMPT_CURRENT_SOURCE_NOGO", "ownership status mismatch")
    require(ownership["operator_payload_ready_retained"] is True, "operator payload readiness lost")
    require(ownership["source_ownership_closed"] is False, "ownership overclosed")
    require(ownership["smooth_EQa_quotient_closed"] is False, "smooth quotient overclosed")
    require(ownership["finitepart_trace_identity_closed"] is False, "finitepart identity overclosed")
    require(ownership["oriented_logdet_promoted"] is False, "oriented logdet overpromoted")

    require(transport["status"] == "TRANSPORT_REDUCED_TO_SOURCEBRANCHIDENTITY", "transport status mismatch")
    require(transport["primary_route"] == "source_identity_transport", "primary route mismatch")
    require(transport["support_prefilter_passes"] is True, "support prefilter missing")
    require(transport["single_remaining_leaf"] == "source_branch_identity", "remaining leaf mismatch")
    require(transport["source_branch_identity_closed"] is False, "source branch overclosed")
    require(transport["transport_closed"] is False, "transport overclosed")
    for sublemma in transport["conditional_sublemmas"].values():
        require(sublemma["conditional_closure_ready"] is True, "conditional sublemma not ready")
        require(sublemma["conditional_on_source_branch_identity"] is True, "conditional dependency lost")
        require(sublemma["unconditional_closed"] is False, "conditional sublemma overclosed")

    require(branch["status"] == "SOURCEBRANCHIDENTITY_SUPPORT_PRESENT_ZERO_EMITTED", "branch status mismatch")
    require(branch["support_count"] == branch["required_clause_count"] == 3, "branch counts mismatch")
    require(branch["emitted_count"] == 0, "branch emitted count mismatch")
    require(branch["source_branch_identity_closed"] is False, "branch identity overclosed")
    require(branch["transport_reduced_leaf_resolved"] is False, "transport leaf overresolved")
    for clause in branch["clauses"].values():
        require(clause["support_present"] is True, "branch support missing")
        require(clause["emitted_by_current_source"] is False, "branch clause overemitted")

    require(bn27["status"] == "BRANCH_CERT_CLOSED_BN27_SOURCEOWNERSHIP_TRANSPORT_OPEN", "bn27 status mismatch")
    require(bn27["branch_certificate_closed"] is True, "bn27 branch cert not closed")
    require(bn27["BN27_source_ownership_transport_closed"] is False, "bn27 transport overclosed")
    require(bn27["selected_connection_witness_values_closed"] is False, "connection values overclosed")
    require(bn27["direct_BN27_source_declaration_closed"] is False, "direct BN27 overclosed")
    require(bn27["projective_rhoE_lift_reopened"] is False, "projective lift reopened")
    require(all(value is False for value in bn27["BN27_source_ownership_fields"].values()), "bn27 ownership fields overfilled")
    require(bn27["projective_lift_no_go"]["missing_positive_oriented_row_count"] == 10, "projective missing rows mismatch")
    require(bn27["projective_lift_no_go"]["missing_multiplier_to_full_abs_sector"] == 5760000, "projective multiplier mismatch")
    require(bn27["projective_lift_no_go"]["operator_lift_passes"] is False, "projective operator lift overpassed")
    require(bn27["support_now_locked"]["oriented_abs_sector_logdet_exact"] == "log(92160000)", "oriented logdet support mismatch")
    for value in bn27["unselected_substitutes_rejected"].values():
        require(value is False, "unselected substitute promoted")

    require(
        next_contract["status"] == "NEXT_IS_BN27_SOURCEOWNERSHIP_TRANSPORT_OR_CONNECTIONWITNESS_VALUES",
        "next contract status mismatch",
    )
    require(any("S_QaSU3^BN27" in item for item in next_contract["must_emit_one_of"]), "BN27 source theorem target missing")
    require(any("connection witness" in item for item in next_contract["must_emit_one_of"]), "connection witness target missing")
    require("branch certificate alone as BN27 source ownership" in next_contract["must_not_use"], "branch cert guard missing")
    require("projective 11-label rho_E shadow as full BN27 threshold proof" in next_contract["must_not_use"], "projective shadow guard missing")

    require("branch certificate closed            : true" in note, "note missing branch certificate")
    require(NEXT in note, "note missing next artifact")

    print("Oriented Phi_fin source-ownership / smooth E_Qa quotient audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
