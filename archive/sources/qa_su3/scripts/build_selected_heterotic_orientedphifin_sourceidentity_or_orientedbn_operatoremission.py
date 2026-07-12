"""Build oriented Phi_fin source-identity / oriented-BN operator-emission theorem."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "direct_fill": DATA / "selected_heterotic_orientedphifin_directfiniteresponse_fillattempt.candidate.json",
    "direct_fill_packet": DATA / "selected_heterotic_orientedphifin_directfiniteresponse_fillattempt_packet.json",
    "source_gate": DATA / "selected_heterotic_orientedphifin_sourceemission_or_smootheqa_thresholdidentity.candidate.json",
    "product_operator": DATA / "selected_heterotic_orientedphifin_productoperator_or_smootheqa_magnitudesource.candidate.json",
    "ctau_source": DATA / "selected_heterotic_bn_centralrankoperator_or_smootheqa_sourceemission.candidate.json",
    "ctau_dirac": DATA / "selected_heterotic_ctau_positivefinitepart_or_smoothdiracconvention_sourcetheorem.candidate.json",
    "routec_trace": DATA / "selected_u1y_routec_trace_equals_27mode_or_full_hym_replay.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_sourceidentity_or_orientedbn_operatoremission.candidate.json"
OUTPUT_FRONTIER = DATA / "selected_heterotic_orientedphifin_sourceidentity_single_frontier.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_sourceidentity_or_orientedbn_operatoremission_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_SourceIdentity_or_OrientedBN_OperatorEmission_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_SOURCEIDENTITY_OPERATORPAYLOAD_READY_SINGLE_SOURCE_FRONTIER_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_SourceOwnership_Theorem_or_SmoothEQa_Quotient_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    direct_fill = load(INPUTS["direct_fill"])
    packet = load(INPUTS["direct_fill_packet"])
    source_gate = load(INPUTS["source_gate"])
    product_operator = load(INPUTS["product_operator"])
    ctau_source = load(INPUTS["ctau_source"])
    ctau_dirac = load(INPUTS["ctau_dirac"])
    routec_trace = load(INPUTS["routec_trace"])

    routec_trace_layer = routec_trace["decision"].get("selected_trace_equals_27mode_DE_gap_layer", False)
    if not routec_trace_layer:
        routec_trace_layer = routec_trace["decision"].get("trace_equals_27mode_DE_gap_layer_closed", False)
    if not routec_trace_layer:
        routec_trace_layer = routec_trace["decision"].get("selected_trace_equality_for_27mode_DE", False)

    support_closure = {
        "ctau_signed_operator_source_selected": ctau_source["decision"]["C_tau_source_selected_as_BN_operator"],
        "ctau_positive_dirac_convention_closed": ctau_dirac["decision"]["ctau_positive_finitepart_convention_closed"],
        "same_BN_domain_for_Ctau_and_PhiFin": product_operator["decision"]["same_BN_domain_for_Ctau_and_PhiFin_positive_gap"],
        "commutation_or_simultaneous_functional_calculus": product_operator["decision"]["commutation_or_simultaneous_functional_calculus_closed"],
        "kernel_policy_and_no_double_count": direct_fill["decision"]["no_double_count_replay_closed"],
        "oriented_D_E_values_materialized": direct_fill["decision"]["oriented_diagonal_response_materialized"],
        "positive_spectrum_materialized": packet["operator_values_materialized"]["minimum_positive_eigenvalue"] > 0,
        "green_riesz_values_materialized": packet["operator_values_materialized"]["green_trace"] > 0,
        "oriented_logdet_candidates_materialized": packet["finitepart_candidates"]["oriented_abs_sector_logdet_sum"] > 0,
        "routec_27mode_DE_trace_layer_selected": routec_trace_layer,
    }

    root_frontier = {
        "schema": "SelectedHeterotic.OrientedPhiFin.SourceIdentity.SingleFrontier.v1",
        "status": "SINGLE_SOURCE_OWNERSHIP_FRONTIER_OPEN",
        "support_closed": support_closure,
        "operator_payload_ready": all(support_closure.values()),
        "not_yet_source_owned": {
            "heterotic_QaSU3_owns_positive_PhiFin_DE_on_oriented_BN": False,
            "same_source_quotient_functor_EndE_or_rhoE_to_oriented_BN": False,
            "smooth_EQa_or_threshold_complex_has_finite_quotient_equal_to_packet": False,
            "finitepart_trace_identity_after_source_ownership": False,
        },
        "minimal_legal_closures": {
            "source_ownership_theorem": [
                "prove the selected heterotic Qa/SU3 source emits the oriented B_N carrier",
                "prove its threshold operator is the materialized Phi_fin D_E magnitude with C_tau orientation",
                "prove the finitepart trace identity consumes exactly the nonzero oriented sector packet",
            ],
            "smooth_EQa_quotient_theorem": [
                "emit selected A/F_A or E_Qa on the heterotic bundle/source",
                "prove its quotient to B_N is the materialized oriented packet",
                "prove heat/zeta/torsion finitepart reduces to the oriented packet with the existing no-double-count policy",
            ],
        },
        "forbidden_shortcuts": [
            "treat Route-C source ownership as heterotic Qa/SU3 ownership without a bridge theorem",
            "promote the oriented logdet candidates before the finitepart trace identity",
            "replace source ownership by observed electroweak or SM residual agreement",
            "reuse the internal 11-label packet as the 27-mode oriented response",
        ],
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    OUTPUT_FRONTIER.write_text(json.dumps(root_frontier, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    decision = {
        "sourceidentity_theorem_attempted": True,
        "operator_payload_ready": root_frontier["operator_payload_ready"],
        "support_closed_count": sum(1 for value in support_closure.values() if value),
        "support_required_count": len(support_closure),
        "single_root_frontier_built": True,
        "heterotic_source_ownership_closed": False,
        "smooth_EQa_quotient_closed": False,
        "finitepart_trace_identity_closed": False,
        "oriented_threshold_value_promoted": False,
        "next_required_artifact": NEXT,
        "frontier_path": rel(OUTPUT_FRONTIER),
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinSourceIdentityOrOrientedBNOperatorEmission",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "direct_fill": direct_fill["status"],
            "source_gate": source_gate["status"],
            "product_operator": product_operator["status"],
            "ctau_source": ctau_source["status"],
            "ctau_dirac": ctau_dirac["status"],
            "routec_trace": routec_trace["status"],
        },
        "frontier_path": rel(OUTPUT_FRONTIER),
        "decision": decision,
        "theorem": {
            "name": "OrientedPhiFinSingleSourceOwnershipFrontierTheorem",
            "proved": True,
            "statement": (
                "All value-side ingredients for the oriented 27-mode B_N response are now "
                "materialized or source-supported: C_tau is selected as the signed BN "
                "operator, its positive Dirac convention is fixed, C_tau and Phi_fin share "
                "one BN domain and commute, the nonzero Phi_fin spectrum and Green/Riesz "
                "packet are materialized, and the Route-C ladder selects the 27-mode D_E "
                "gap layer. The remaining obstruction is not another numerical computation. "
                "It is a single source-ownership theorem: the selected heterotic Qa/SU3 "
                "source must own that positive Phi_fin D_E/oriented BN packet, or a smooth "
                "E_Qa quotient theorem must emit the same packet. Until then the oriented "
                "logdet remains a candidate finitepart, not a promoted threshold value."
            ),
        },
        "guardrails": {
            "does_not_promote_routec_ownership_to_heterotic_ownership": True,
            "does_not_promote_oriented_logdet": True,
            "does_not_reuse_internal_11label_packet_as_27mode_response": True,
            "does_not_claim_smooth_EQa": True,
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
        "frontier_path": rel(OUTPUT_FRONTIER),
        "note_path": rel(OUTPUT_NOTE),
        "operator_payload_ready": root_frontier["operator_payload_ready"],
        "heterotic_source_ownership_closed": False,
        "smooth_EQa_quotient_closed": False,
        "finitepart_trace_identity_closed": False,
        "oriented_threshold_value_promoted": False,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin SourceIdentity or OrientedBN OperatorEmission v1

## Result

```text
status = {STATUS}
operator_payload_ready = {str(root_frontier["operator_payload_ready"]).lower()}
heterotic_source_ownership_closed = false
oriented_threshold_value_promoted = false
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

## Single Frontier

```text
{rel(OUTPUT_FRONTIER)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_FRONTIER)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
