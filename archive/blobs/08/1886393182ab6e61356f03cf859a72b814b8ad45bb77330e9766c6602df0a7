"""Build the oriented Phi_fin threshold-identity source fill / smooth E_Qa construction attempt."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "source_request": DATA / "selected_heterotic_orientedphifin_thresholdidentity_source_request.json",
    "source_gate": DATA / "selected_heterotic_orientedphifin_sourceemission_or_smootheqa_thresholdidentity.candidate.json",
    "oriented_table": DATA / "selected_heterotic_orientedphifin_simultaneous_ctau_phifin_table.json",
    "selected_packet_emission": DATA / "selected_heterotic_projectiverhoe_selectedpacketemission_or_operatoridentity.candidate.json",
    "internal_finitepart": DATA / "selected_heterotic_projectiverhoe_eqa_or_thresholdfinitepart.candidate.json",
    "smooth_fill": DATA / "selected_heterotic_projectiverhoe_smoothoperator_sourcepacket_fillattempt.candidate.json",
    "smooth_missing": DATA / "selected_heterotic_projectiverhoe_smoothoperator_sourcepacket_missing_leaves.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_thresholdidentity_sourcefill_or_smootheqa_construction.candidate.json"
OUTPUT_FILL = DATA / "selected_heterotic_orientedphifin_thresholdidentity_sourcefill_packet.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_thresholdidentity_sourcefill_or_smootheqa_construction_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_ThresholdIdentity_SourceFill_or_SmoothEQa_Construction_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_THRESHOLDIDENTITY_SOURCEFILL_PARTIAL_FINITE_SELECTED_SMOOTH_EQA_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_MinimalSmoothEQa_LeafFill_or_FiniteQuotientIdentity_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    request = load(INPUTS["source_request"])
    source_gate = load(INPUTS["source_gate"])
    table = load(INPUTS["oriented_table"])
    selected_packet = load(INPUTS["selected_packet_emission"])
    internal_finitepart = load(INPUTS["internal_finitepart"])
    smooth_fill = load(INPUTS["smooth_fill"])
    smooth_missing = load(INPUTS["smooth_missing"])

    fill_packet = {
        "schema": "SelectedHeterotic.OrientedPhiFinThresholdIdentity.SourceFillPacket.v1",
        "source_certificate": {
            "finite_internal_projective_packet_selected": selected_packet["decision"]["selected_finite_internal_packet_emitted"],
            "same_branch_projective_rhoE_support_family": True,
            "selected_before_target_comparison": selected_packet["emission_checks"]["no_target_fitting"],
            "closes_threshold_source_certificate": False,
            "why_not_closed": (
                "The selected finite packet is internal 11-label rho_E/D_E/Green/Riesz/dotD data. "
                "It does not by itself identify the 27-mode oriented Phi_fin table as the selected "
                "heterotic threshold source."
            ),
        },
        "operator_identity": {
            "oriented_table_available": True,
            "same_domain_commutation_closed": source_gate["decision"]["same_domain_commutation_table_complete"],
            "candidate_identity": request["must_emit"]["operator_identity"],
            "closes_operator_identity": False,
            "why_not_closed": "No source emits E_Qa^or or an equivalent threshold complex whose finite quotient is the oriented table.",
        },
        "smooth_or_finite_domain": {
            "finite_BN_table_domain_available": True,
            "kernel_policy_algebraic": source_gate["closed_support"]["kernel_policy_algebraic"],
            "no_double_count_policy_algebraic": source_gate["closed_support"]["no_double_counting_algebraic"],
            "smooth_domain_values_filled": False,
            "closes_domain_leaf": False,
            "why_not_closed": "The finite table domain is available, but selected smooth operator domain/quotient and trace weights are still not emitted.",
        },
        "smooth_payload_if_used": {
            "Rplus_geometry_available": smooth_fill["fill_result"]["Rplus_geometry_available"],
            "selected_connection_A_filled": smooth_fill["fill_result"]["selected_connection_A_filled"],
            "curvature_F_A_filled": smooth_fill["fill_result"]["curvature_F_A_filled"],
            "representation_action_filled": smooth_fill["fill_result"]["representation_action_filled"],
            "E_Qa_matrix_filled": smooth_fill["fill_result"]["E_Qa_matrix_filled"],
            "closes_smooth_EQa": False,
        },
        "finitepart_payload": {
            "oriented_table_logdet_support": table["logdet_values"],
            "internal_log2008_closed_at_internal_scope": internal_finitepart["decision"]["selected_internal_threshold_finitepart_closed"],
            "finitepart_trace_identity_for_oriented_table": False,
            "closes_finitepart_leaf": False,
            "why_not_closed": "The oriented table values are computed, but no source authorizes them as the heterotic threshold finite part.",
        },
        "audit_replay": {
            "oriented_table_replayed": True,
            "finitepart_replay_possible": True,
            "selected_source_flags_all_true": False,
            "closes_audit_replay": False,
        },
        "hard_missing_imported": smooth_missing["hard_missing"],
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    OUTPUT_FILL.write_text(json.dumps(fill_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    required_leaves = {
        "source_certificate": fill_packet["source_certificate"]["closes_threshold_source_certificate"],
        "operator_identity": fill_packet["operator_identity"]["closes_operator_identity"],
        "smooth_or_finite_domain": fill_packet["smooth_or_finite_domain"]["closes_domain_leaf"],
        "smooth_payload_if_used_or_finite_quotient_identity": fill_packet["smooth_payload_if_used"]["closes_smooth_EQa"],
        "finitepart_payload": fill_packet["finitepart_payload"]["closes_finitepart_leaf"],
        "audit_replay": fill_packet["audit_replay"]["closes_audit_replay"],
    }
    closed_count = sum(1 for value in required_leaves.values() if value is True)

    decision = {
        "fill_attempt_executed": True,
        "required_leaf_count": len(required_leaves),
        "closed_required_leaf_count": closed_count,
        "selected_finite_internal_packet_reused": True,
        "oriented_table_reused": True,
        "smooth_EQa_constructed": False,
        "finite_quotient_identity_constructed": False,
        "source_emission_closed": False,
        "heterotic_threshold_magnitude_promoted": False,
        "current_source_nogo": True,
        "mathematical_impossibility_claimed": False,
        "next_required_artifact": NEXT,
        "fill_packet_path": rel(OUTPUT_FILL),
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinThresholdIdentitySourceFillOrSmoothEQaConstruction",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "source_gate": source_gate["status"],
            "selected_packet_emission": selected_packet["status"],
            "internal_finitepart": internal_finitepart["status"],
            "smooth_fill": smooth_fill["status"],
            "smooth_missing": smooth_missing["status"],
        },
        "fill_packet_path": rel(OUTPUT_FILL),
        "required_leaves": required_leaves,
        "decision": decision,
        "theorem": {
            "name": "OrientedPhiFinThresholdIdentitySourceFillCurrentSourceNoGo",
            "proved": True,
            "statement": (
                "The source-fill attempt reuses all available selected finite data and the "
                "oriented 27-mode table, but none of the six required threshold-identity "
                "leaves closes. The selected finite projective rho_E packet is valid at "
                "internal 11-label scope, while the oriented table is valid as algebraic "
                "27-mode support. The missing bridge is still the selected smooth E_Qa or "
                "finite quotient identity that declares the oriented table to be the "
                "heterotic Qa/SU3 threshold complex and finitepart."
            ),
        },
        "guardrails": {
            "does_not_promote_internal_11_label_packet_to_27mode_threshold": True,
            "does_not_promote_oriented_table_values": True,
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
        "fill_packet_path": rel(OUTPUT_FILL),
        "note_path": rel(OUTPUT_NOTE),
        "closed_required_leaf_count": closed_count,
        "source_emission_closed": False,
        "smooth_EQa_constructed": False,
        "finite_quotient_identity_constructed": False,
        "heterotic_threshold_magnitude_promoted": False,
        "current_source_nogo": True,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin ThresholdIdentity SourceFill or SmoothEQa Construction v1

## Result

```text
status = {STATUS}
closed_required_leaf_count = {closed_count}/{len(required_leaves)}
source_emission_closed = false
smooth_EQa_constructed = false
finite_quotient_identity_constructed = false
heterotic_threshold_magnitude_promoted = false
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

## Required Leaves

```json
{json.dumps(required_leaves, indent=2, sort_keys=True)}
```

## Fill Packet

```text
{rel(OUTPUT_FILL)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_FILL)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
