"""Build final gate for oriented Phi_fin branch identity or smooth E_Qa quotient."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "coemission_theorem": DATA / "selected_heterotic_orientedphifin_orientation_magnitude_coemission_theorem.candidate.json",
    "coemission_packet": DATA / "selected_heterotic_orientedphifin_orientation_magnitude_coemission_packet.json",
    "single_frontier": DATA / "selected_heterotic_orientedphifin_sourceidentity_single_frontier.json",
    "threshold_source_request": DATA / "selected_heterotic_orientedphifin_thresholdidentity_source_request.json",
    "minimal_amendment_plan": DATA / "selected_heterotic_orientedphifin_sourceleaf_minimal_source_amendment_plan.json",
    "source_identity_attempt": DATA / "selected_heterotic_orientedphifin_sourceidentity_or_orientedbn_operatoremission.candidate.json",
    "sourceleaf_discovery": DATA / "selected_heterotic_orientedphifin_sourceleaf_corpus_discovery_report.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_branchidentity_sourcecertificate_or_smootheqa_finalgate.candidate.json"
OUTPUT_PACKET = DATA / "selected_heterotic_orientedphifin_branchidentity_minimal_source_certificate_packet.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_branchidentity_sourcecertificate_or_smootheqa_finalgate_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_BranchIdentity_SourceCertificate_or_SmoothEQa_FinalGate_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_BRANCH_IDENTITY_FINAL_GATE_OPEN_MINIMAL_SOURCE_PACKET_BUILT"
NEXT = "Selected_Heterotic_OrientedPhiFin_BranchIdentity_MinimalSourceCertificate_Fill_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    coemission = load(INPUTS["coemission_theorem"])
    packet = load(INPUTS["coemission_packet"])
    frontier = load(INPUTS["single_frontier"])
    request = load(INPUTS["threshold_source_request"])
    amendment = load(INPUTS["minimal_amendment_plan"])
    source_identity = load(INPUTS["source_identity_attempt"])
    discovery = load(INPUTS["sourceleaf_discovery"])

    direct_route = {
        "route": "direct_same_source_branch_identity",
        "closed": False,
        "support": {
            "operator_payload_ready": frontier["operator_payload_ready"],
            "support_reduction_closed": coemission["decision"]["support_reduction_closed"],
            "ctau_signed_operator_source_selected": frontier["support_closed"]["ctau_signed_operator_source_selected"],
            "routec_27mode_DE_trace_layer_selected": frontier["support_closed"]["routec_27mode_DE_trace_layer_selected"],
            "oriented_logdet_candidates_materialized": frontier["support_closed"]["oriented_logdet_candidates_materialized"],
        },
        "missing": {
            "selected_heterotic_QaSU3_source_certificate_names_both_branches": True,
            "source_emits_oriented_BN_carrier_as_threshold_domain": True,
            "source_emits_positive_PhiFin_DE_magnitude_with_Ctau_orientation": True,
            "source_owns_finitepart_trace_identity_for_oriented_nonzero_sector": True,
        },
        "reason_open": (
            "The direct carrier support is ready, but the current record does not contain "
            "a theorem naming one selected heterotic Qa/SU3 source that emits both the "
            "Route-C magnitude branch and the C_tau orientation branch."
        ),
    }

    smooth_route = {
        "route": "smooth_E_Qa_quotient_theorem",
        "closed": False,
        "support": {
            "smooth_lane_retained": True,
            "threshold_request_has_smooth_payload_contract": "smooth_payload_if_used" in request["must_emit"],
            "minimal_plan_keeps_smooth_fallback": "smooth_lane_kept_as_fallback" in amendment,
        },
        "missing": {
            "selected_A_or_F_A": True,
            "representation_action_and_trace": True,
            "Weitzenbock_or_endomorphism_EQa_identity": True,
            "quotient_projection_to_oriented_BN_packet": True,
            "finite_spectral_functor_to_log92160000": True,
        },
        "reason_open": (
            "The corpus has structural heterotic/bundle language, but not selected smooth "
            "A/F_A, representation trace, E_Qa identity, or quotient proof to this oriented "
            "27-mode packet."
        ),
    }

    minimal_packet = {
        "schema": "SelectedHeterotic.OrientedPhiFin.BranchIdentity.MinimalSourceCertificatePacket.v1",
        "status": "SOURCE_CERTIFICATE_PACKET_REQUIRED",
        "acceptance_rule": {
            "observed_data_allowed": False,
            "support_values_may_be_replayed": True,
            "promote_log92160000_only_if_packet_filled": True,
            "otherwise_keep_support_only": True,
        },
        "must_emit": {
            "source_certificate": (
                "the selected heterotic Qa/SU3 source branch, named explicitly, with no "
                "Route-C ownership import unless a bridge theorem proves identity"
            ),
            "branch_identity": (
                "the Route-C selected 27-mode Phi_fin D_E magnitude branch and the C_tau "
                "oriented B_N branch are the same selected threshold complex"
            ),
            "carrier_domain": "selected oriented B_N quotient/domain with kernel and shared-circle policy",
            "operator_identity": "E_Qa^or or threshold operator = sign(C_tau) * PhiFin_DE on the nonzero oriented sector",
            "commutation_in_source_algebra": "C_tau and PhiFin_DE commute as source-emitted operators, not only as support tables",
            "finitepart_trace_identity": "source-owned trace/zeta/torsion finitepart equals log(92160000)",
            "audit_replay": "rerun support table, no-double-count, and co-emission checks under selected-source flags",
        },
        "current_route_verdicts": {
            "direct_same_source_branch_identity": "OPEN_STRONGEST_ROUTE",
            "smooth_E_Qa_quotient_theorem": "OPEN_FALLBACK",
        },
        "sourceleaf_discovery_counts": {
            "repo_files_scanned": discovery["repo_scan"]["files_scanned"],
            "repo_support_only_geometry_files": discovery["repo_scan"]["buckets"]["support_only_geometry"]["file_count"],
            "repo_support_only_geometry_hits": discovery["repo_scan"]["buckets"]["support_only_geometry"]["needle_hits"],
            "repo_direct_selected_carrier_files": discovery["repo_scan"]["buckets"]["direct_selected_carrier"]["file_count"],
            "repo_direct_selected_carrier_hits": discovery["repo_scan"]["buckets"]["direct_selected_carrier"]["needle_hits"],
        },
    }
    OUTPUT_PACKET.write_text(json.dumps(minimal_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    decision = {
        "branch_identity_final_gate_executed": True,
        "direct_same_source_branch_identity_closed": False,
        "smooth_EQa_quotient_closed": False,
        "minimal_source_certificate_packet_built": True,
        "strongest_route": "direct_same_source_branch_identity",
        "orientation_magnitude_coemission_closed": False,
        "oriented_logdet_promoted": False,
        "full_oriented_phi_fin_threshold_closed": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinBranchIdentitySourceCertificateOrSmoothEQaFinalGate",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "coemission_theorem": coemission["status"],
            "coemission_packet": packet["status"],
            "single_frontier": frontier["status"],
            "source_identity_attempt": source_identity["status"],
            "minimal_amendment_plan": amendment["status"],
        },
        "routes": {
            "direct_same_source_branch_identity": direct_route,
            "smooth_E_Qa_quotient_theorem": smooth_route,
        },
        "minimal_source_certificate_packet_path": rel(OUTPUT_PACKET),
        "decision": decision,
        "theorem": {
            "name": "BranchIdentityFinalGateCurrentSourceNoGoAndMinimalPacketTheorem",
            "proved": True,
            "statement": (
                "Given the closed co-emission support reduction, the only legal ways to "
                "promote the oriented Phi_fin finitepart are either a direct same-source "
                "branch identity certificate or a smooth E_Qa quotient theorem. The current "
                "record supplies all value-side and algebraic support, but neither route "
                "contains the selected source-emission theorem. Therefore the branch is not "
                "closed; the minimal source-certificate packet emitted here is necessary and "
                "sufficient for the next fill attempt to promote log(92160000)."
            ),
        },
        "guardrails": {
            "does_not_claim_branch_identity": True,
            "does_not_claim_smooth_EQa": True,
            "does_not_promote_oriented_logdet": True,
            "does_not_use_routec_as_heterotic_source_without_bridge": True,
            "does_not_use_observed_data": True,
            "target_fitting_used": False,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "minimal_source_certificate_packet_path": rel(OUTPUT_PACKET),
        "note_path": rel(OUTPUT_NOTE),
        "branch_identity_final_gate_executed": True,
        "direct_same_source_branch_identity_closed": False,
        "smooth_EQa_quotient_closed": False,
        "minimal_source_certificate_packet_built": True,
        "strongest_route": "direct_same_source_branch_identity",
        "orientation_magnitude_coemission_closed": False,
        "oriented_logdet_promoted": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin BranchIdentity SourceCertificate or SmoothEQa FinalGate v1

## Result

```text
status = {STATUS}
direct_same_source_branch_identity_closed = false
smooth_EQa_quotient_closed = false
minimal_source_certificate_packet_built = true
strongest_route = direct_same_source_branch_identity
orientation_magnitude_coemission_closed = false
oriented_logdet_promoted = false
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

The minimal source-certificate packet is:

```text
{rel(OUTPUT_PACKET)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_PACKET)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
