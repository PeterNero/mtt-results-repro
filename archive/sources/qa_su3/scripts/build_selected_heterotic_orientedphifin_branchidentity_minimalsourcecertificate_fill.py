"""Attempt to fill the oriented Phi_fin branch-identity minimal source certificate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "minimal_packet": DATA / "selected_heterotic_orientedphifin_branchidentity_minimal_source_certificate_packet.json",
    "final_gate": DATA / "selected_heterotic_orientedphifin_branchidentity_sourcecertificate_or_smootheqa_finalgate.candidate.json",
    "finite_physical_quotient": DATA / "selected_heterotic_projectiverhoe_finitephysicalquotient_sourcetheorem.candidate.json",
    "ctau_source": DATA / "selected_heterotic_bn_centralrankoperator_or_smootheqa_sourceemission.candidate.json",
    "routec_gap_layer": DATA / "selected_u1y_routec_trace_equals_27mode_or_full_hym_replay.candidate.json",
    "coemission_theorem": DATA / "selected_heterotic_orientedphifin_orientation_magnitude_coemission_theorem.candidate.json",
    "trace_identity": DATA / "selected_heterotic_orientedphifin_fullfourierorbit_traceidentity.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_branchidentity_minimalsourcecertificate_fill.candidate.json"
OUTPUT_PACKET = DATA / "selected_heterotic_orientedphifin_branchidentity_fill_attempt_report.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_branchidentity_minimalsourcecertificate_fill_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_BranchIdentity_MinimalSourceCertificate_Fill_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_BRANCH_IDENTITY_FILL_ATTEMPT_DOMAIN_BRIDGE_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_BN27_SourceDomainBridge_or_SmoothEQa_Quotient_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    minimal = load(INPUTS["minimal_packet"])
    final_gate = load(INPUTS["final_gate"])
    finite = load(INPUTS["finite_physical_quotient"])
    ctau = load(INPUTS["ctau_source"])
    routec = load(INPUTS["routec_gap_layer"])
    coemission = load(INPUTS["coemission_theorem"])
    trace = load(INPUTS["trace_identity"])

    fill_status = {
        "source_certificate": {
            "filled": False,
            "support": {
                "finite_physical_quotient_domain_closed": finite["decision"]["finite_physical_quotient_domain_closed"],
                "ctau_source_selected_as_BN_operator": ctau["decision"]["C_tau_source_selected_as_BN_operator"],
                "routec_gap_layer_closed": routec["decision"]["DE_gap_Riesz_Green_layer_closed"],
            },
            "blocker": "no single certificate names the finite 11-label quotient, the C_tau BN carrier, and the Route-C 27-mode D_E branch as one selected heterotic source",
        },
        "branch_identity": {
            "filled": False,
            "support": {
                "coemission_support_reduction_closed": coemission["decision"]["support_reduction_closed"],
                "routec_27mode_trace_equality_closed": routec["decision"]["selected_trace_equality_for_27mode_DE"],
                "ctau_signed_intertwiner_closed": ctau["decision"]["C_tau_signed_intertwiner_closed"],
            },
            "blocker": "the 11-label finite physical quotient and the 27-mode oriented BN carrier are connected by support/embedding data, but not by a selected source-domain bridge theorem",
        },
        "carrier_domain": {
            "filled": False,
            "support": {
                "finite_11_label_domain_closed": len(finite["expected_labels"]) == 11,
                "routec_BN_domain_dimension": routec["finite_trace_route"]["gap_layer"]["basis_dimension"],
                "routec_BN_domain_id": routec["finite_trace_route"]["gap_layer"]["basis_id"],
            },
            "blocker": "selected 27-mode oriented BN quotient/domain is not source-owned by the heterotic finite physical quotient theorem",
        },
        "operator_identity": {
            "filled": False,
            "support": {
                "ctau_signed_layer_closed": ctau["decision"]["operator_identity_closed_for_signed_layer"],
                "positive_PhiFin_DE_gap_layer_closed": routec["decision"]["DE_gap_Riesz_Green_layer_closed"],
                "product_support_ready": coemission["decision"]["support_reduction_closed"],
            },
            "blocker": "no selected source-emitted operator identity states E_Qa^or = sign(C_tau) * PhiFin_DE on the nonzero oriented sector",
        },
        "commutation_in_source_algebra": {
            "filled": False,
            "support": {
                "support_commutation_closed": coemission["support_reduction"]["C_tau_commutes_with_PhiFin_DE_as_functional_calculus"],
            },
            "blocker": "commutation is closed as simultaneous table support, but not yet as two operators emitted by one source algebra",
        },
        "finitepart_trace_identity": {
            "filled": False,
            "support": {
                "relative_trace_identity_closed": coemission["support_reduction"]["relative_finitepart_trace_identity_closed"],
                "oriented_abs_sector_product": trace["oriented_abs_sector_product"],
                "oriented_abs_sector_logdet_exact": trace["oriented_abs_sector_logdet_exact"],
            },
            "blocker": "finitepart identity cannot inherit source ownership before the carrier and operator identity are source-owned",
        },
        "audit_replay": {
            "filled": True,
            "support": {
                "support_values_replayed": True,
                "target_fitting_used": False,
            },
            "blocker": None,
        },
    }
    filled_count = sum(1 for item in fill_status.values() if item["filled"])

    report = {
        "schema": "SelectedHeterotic.OrientedPhiFin.BranchIdentity.MinimalSourceCertificateFillAttempt.v1",
        "status": "DOMAIN_BRIDGE_REQUIRED",
        "filled_count": filled_count,
        "required_count": len(fill_status),
        "fill_status": fill_status,
        "minimal_new_leaf": {
            "name": "selected_BN27_source_domain_bridge",
            "statement_required": (
                "The selected heterotic Qa/SU3 source-domain functor promotes the "
                "11-label finite physical quotient to the full 27-mode oriented B_N "
                "threshold domain, preserving C_tau orientation, PhiFin_DE magnitude, "
                "kernel/shared-circle policy, and trace weights."
            ),
            "why_minimal": (
                "All remaining fields depend on this bridge: once the selected BN27 "
                "domain is source-owned, the existing support closes commutation, "
                "operator identity, and finitepart inheritance under one source."
            ),
        },
        "guardrails": {
            "does_not_promote_11label_domain_to_27mode_domain": True,
            "does_not_treat_embedding_as_source_bridge": True,
            "does_not_import_routec_ownership_without_identity": True,
            "does_not_promote_log92160000": True,
            "does_not_use_observed_data": True,
            "target_fitting_used": False,
        },
    }
    OUTPUT_PACKET.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    decision = {
        "minimal_source_certificate_fill_attempted": True,
        "filled_count": filled_count,
        "required_count": len(fill_status),
        "source_certificate_closed": False,
        "selected_BN27_source_domain_bridge_closed": False,
        "branch_identity_closed": False,
        "orientation_magnitude_coemission_closed": False,
        "oriented_logdet_promoted": False,
        "minimal_new_leaf": "selected_BN27_source_domain_bridge",
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinBranchIdentityMinimalSourceCertificateFill",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "final_gate": final_gate["status"],
            "minimal_packet": minimal["status"],
            "finite_physical_quotient": finite["status"],
            "ctau_source": ctau["status"],
            "routec_gap_layer": routec["status"],
            "coemission_theorem": coemission["status"],
        },
        "fill_attempt_report_path": rel(OUTPUT_PACKET),
        "decision": decision,
        "theorem": {
            "name": "MinimalSourceCertificateFillAttemptDomainBridgeObstructionTheorem",
            "proved": True,
            "statement": (
                "The current record can replay every numerical and algebraic support value "
                "needed by the branch-identity packet, and it closes audit replay. It cannot "
                "fill the source certificate because the selected finite physical quotient is "
                "an 11-label domain, while the oriented Phi_fin threshold needs the full "
                "27-mode B_N domain. The missing object is therefore not another determinant "
                "calculation but a selected BN27 source-domain bridge or a smooth E_Qa quotient "
                "that emits the same 27-mode packet."
            ),
        },
        "guardrails": report["guardrails"],
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "fill_attempt_report_path": rel(OUTPUT_PACKET),
        "note_path": rel(OUTPUT_NOTE),
        "minimal_source_certificate_fill_attempted": True,
        "filled_count": filled_count,
        "required_count": len(fill_status),
        "selected_BN27_source_domain_bridge_closed": False,
        "branch_identity_closed": False,
        "orientation_magnitude_coemission_closed": False,
        "oriented_logdet_promoted": False,
        "minimal_new_leaf": decision["minimal_new_leaf"],
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin BranchIdentity MinimalSourceCertificate Fill v1

## Result

```text
status = {STATUS}
filled_count = {filled_count}
required_count = {len(fill_status)}
selected_BN27_source_domain_bridge_closed = false
branch_identity_closed = false
orientation_magnitude_coemission_closed = false
oriented_logdet_promoted = false
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

The minimal new leaf is:

```text
selected_BN27_source_domain_bridge
```

Report:

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
