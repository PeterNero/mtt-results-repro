"""Build the heterotic End(E)->B_N functor / rho_E transition value-packet interface."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUT_BRIDGE = DATA / "selected_heterotic_phifin_sourceidentity_bridge_attempt.candidate.json"

OUTPUT_DATA = DATA / "selected_heterotic_ende_to_bn_functor_or_rhoe_transition_valuepacket.candidate.json"
OUTPUT_CERT = CERTS / "selected_heterotic_ende_to_bn_functor_or_rhoe_transition_valuepacket_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_EndE_to_BN_Functor_or_RhoETransitionData_ValuePacket_v1.md"

STATUS = "HETEROTIC_ENDE_TO_BN_FUNCTOR_OR_RHOE_TRANSITION_VALUEPACKET_INTERFACE_BUILT_VALUES_OPEN"
NEXT = "Selected_Heterotic_EndE_to_BN_Functor_or_RhoETransitionData_ValuePacket_Fill_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def required_field(name: str, description: str) -> dict[str, Any]:
    return {
        "name": name,
        "description": description,
        "required": True,
        "value": None,
        "source_emitted": False,
        "same_branch_selected": False,
    }


def main() -> dict[str, Any]:
    bridge = load(INPUT_BRIDGE)

    packet_template = {
        "source_certificate": {
            "selected_branch_id": required_field(
                "selected_branch_id",
                "Identifier proving the rank-three Iwasawa SU(3) monad/End(E) branch is the source of the packet.",
            ),
            "no_imported_routec_substitution": required_field(
                "no_imported_routec_substitution",
                "Certificate that Route-C 27-mode data are used only through the proved functor, not substituted as source.",
            ),
        },
        "EndE_domain": {
            "finite_EndE_basis": required_field(
                "finite_EndE_basis",
                "Selected finite basis/domain for End(E) coefficients or sections.",
            ),
            "quotient_zero_mode_policy": required_field(
                "quotient_zero_mode_policy",
                "Kernel/shared-line/zero-mode quotient policy for the heterotic Qa/SU3 operator domain.",
            ),
            "trace_inner_product": required_field(
                "trace_inner_product",
                "Trace and inner-product convention used by the heterotic finite operator.",
            ),
        },
        "EndE_to_BN_functor": {
            "basis_map_matrix": required_field(
                "basis_map_matrix",
                "Matrix or formula mapping selected End(E) domain data into the 27-mode B_N packet.",
            ),
            "commuting_projection_certificate": required_field(
                "commuting_projection_certificate",
                "Proof that projection, D_E action, and quotient commute through the map.",
            ),
            "gap_transfer_certificate": required_field(
                "gap_transfer_certificate",
                "Proof that the positive gap and Green bound transfer to the heterotic domain.",
            ),
        },
        "rhoE_transition_data": {
            "nonidentity_rho_E": required_field(
                "nonidentity_rho_E",
                "Selected nonidentity transition/projective carrier for the heterotic bundle/sheaf/twist.",
            ),
            "curvature_or_cocycle": required_field(
                "curvature_or_cocycle",
                "Curvature, Cech cocycle, or projective cocycle data proving the carrier is source-selected.",
            ),
            "shared_line_compatibility": required_field(
                "shared_line_compatibility",
                "Compatibility with the shared-circle/shared-line quotient already used in the electroweak row.",
            ),
        },
        "operator_payload": {
            "D_E_or_E_Qa_matrix": required_field(
                "D_E_or_E_Qa_matrix",
                "Selected finite D_E, Weitzenbock E_Qa, or equivalent threshold operator matrix.",
            ),
            "positive_spectrum_or_gap": required_field(
                "positive_spectrum_or_gap",
                "Positive spectrum, gap lower bound, or exact zero-mode policy.",
            ),
            "finite_part_regularization": required_field(
                "finite_part_regularization",
                "Heat/zeta/torsion finite-part rule and determinant scale in heterotic threshold units.",
            ),
        },
    }

    required_count = sum(len(group) for group in packet_template.values())

    candidate = {
        "candidate": "SelectedHeteroticEndEtoBNFunctorOrRhoETransitionValuePacket",
        "status": STATUS,
        "input": rel(INPUT_BRIDGE),
        "input_status": bridge["status"],
        "target_fitting_used": False,
        "closure_claimed": False,
        "imported_support_allowed": {
            "u1y_27mode_gap_layer_closed": bridge["decision"]["u1y_27mode_gap_layer_closed"],
            "u1y_trace_equality_closed": bridge["decision"]["u1y_trace_equality_closed"],
            "transport_projector_replay_closed": bridge["decision"]["transport_projector_replay_closed"],
            "promotion_allowed_without_this_packet": False,
        },
        "packet_template": packet_template,
        "field_counts": {
            "required": required_count,
            "source_emitted": 0,
            "same_branch_selected": 0,
            "filled_values": 0,
        },
        "acceptance": {
            "passes_now": False,
            "must_fill_all_groups": list(packet_template),
            "success_condition": (
                "Either the End(E)->B_N functor group or rho_E transition group must emit "
                "source-selected nonidentity data, and the operator_payload group must emit "
                "the finite operator plus finite-part rule."
            ),
        },
        "decision": {
            "valuepacket_interface_built": True,
            "values_filled": False,
            "same_source_identity_proved": False,
            "direct_finite_operator_emitted": False,
            "E_Qa_computed": False,
            "computed_threshold_value": False,
            "next_required_artifact": NEXT,
            "target_fitting_used": False,
        },
        "guardrails": {
            "allows_routec_substitution_without_functor": False,
            "allows_identity_rhoE": False,
            "allows_topology_only_operator": False,
            "allows_standard_embedding_without_selector": False,
            "uses_observed_electroweak_data": False,
            "uses_target_residual_scan": False,
            "target_fitting_used": False,
        },
        "theorem": {
            "name": "HeteroticEndEtoBNFunctorOrRhoETransitionPacketSufficiencyCriterion",
            "proved": True,
            "statement": (
                "A heterotic Phi_fin source identity can be accepted only after this "
                "packet emits a selected source certificate, selected End(E) domain "
                "or nonidentity rho_E transition data, a commuting map to B_N or "
                "equivalent direct operator payload, and a finite-part convention. "
                "The interface is sufficient as an acceptance criterion but does "
                "not fill any values."
            ),
        },
    }

    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "valuepacket_interface_built": True,
        "values_filled": False,
        "same_source_identity_proved": False,
        "direct_finite_operator_emitted": False,
        "E_Qa_computed": False,
        "required_fields": required_count,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic EndE to BN Functor or RhoETransitionData ValuePacket v1

## Result

```text
status = {STATUS}
valuepacket_interface_built = true
values_filled = false
same_source_identity_proved = false
direct_finite_operator_emitted = false
E_Qa_computed = false
next_required_artifact = {NEXT}
```

## Packet Template

```json
{json.dumps(packet_template, indent=2, sort_keys=True)}
```

## Acceptance

```json
{json.dumps(candidate["acceptance"], indent=2, sort_keys=True)}
```

This is the smallest honest source-identity payload now needed. The selected
27-mode support is valuable, but it cannot become the heterotic Qa/SU3
threshold until this packet is filled by the selected monad/`End(E)` branch.
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
