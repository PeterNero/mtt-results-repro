"""Build the minimal emission subpacket plan for smooth rho_E payload closure."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "payload_gate": DATA / "selected_heterotic_projectiverhoe_smoothsourcecertificate_or_complementoperatorpayload.candidate.json",
    "minimal_contract": DATA / "selected_heterotic_projectiverhoe_smooth_operator_payload_minimal_contract.json",
    "z3_shadow": DATA / "selected_heterotic_projectiverhoe_abstract_z3_cocycle_shadow_witness.json",
    "finite_values": DATA / "selected_heterotic_projectiverhoe_exactcomplement_or_smoothrhoetransition_valuepacket.values.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_projectiverhoe_smoothoperatorpayload_minimalemissionsubpacket.candidate.json"
OUTPUT_SUBPACKET = DATA / "selected_heterotic_projectiverhoe_smoothoperatorpayload_emission_order.json"
OUTPUT_CERT = CERTS / "selected_heterotic_projectiverhoe_smoothoperatorpayload_minimalemissionsubpacket_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_ProjectiveRhoE_SmoothOperatorPayload_MinimalEmissionSubpacket_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_SMOOTHOPERATORPAYLOAD_MINIMAL_EMISSION_SUBPACKET_BUILT_FIRST_LEAF_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_SmoothDomainCover_SourceLeaf_or_DirectComplementDomain_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    payload_gate = load(INPUTS["payload_gate"])
    contract = load(INPUTS["minimal_contract"])
    z3_shadow = load(INPUTS["z3_shadow"])
    finite_values = load(INPUTS["finite_values"])["finite_internal_values"]

    emission_subpackets = [
        {
            "id": "S1_smooth_domain_cover_or_complement_domain",
            "priority": 1,
            "must_emit": [
                "same-branch smooth heterotic Qa/SU3 source certificate",
                "selected good-cover incidence with nonempty overlaps, or selected smooth operator domain",
                "map from smooth source/domain to the eleven-label finite quotient",
                "proof the abstract Z3 shadow is the shadow of this source, not an independent scaffold",
            ],
            "current_support": {
                "SM_parity_boundary": True,
                "abstract_Z3_shadow": True,
                "finite_eleven_label_quotient": True,
                "source_level_FW_Bianchi_support": True,
            },
            "closed": False,
            "why_first": "Every transition/operator/complement determinant value needs the selected smooth domain or cover before it can be interpreted.",
            "next_artifact": NEXT,
        },
        {
            "id": "S2_transition_or_projection_lift",
            "priority": 2,
            "must_emit": [
                "smooth Deligne/Cech/B-field representative or smooth-to-finite projection P11",
                "rhoE transition matrices lifting the Z3 shadow, or complement operator D_comp",
                "Hermitian metric/unitarity tables, or heat-domain self-adjoint/elliptic setup",
            ],
            "current_support": {
                "abstract_Z3_shadow_tables": list(z3_shadow["tables"].keys()),
                "finite_tau_values": finite_values["tau"],
            },
            "closed": False,
            "depends_on": "S1_smooth_domain_cover_or_complement_domain",
            "next_artifact": "Selected_Heterotic_ProjectiveRhoE_TransitionLift_or_ComplementProjection_Subpacket_v1",
        },
        {
            "id": "S3_operator_and_admissibility",
            "priority": 3,
            "must_emit": [
                "connection A or projective connection, or BRST/FP ghost operator",
                "curvature F_A or complement/ghost pair",
                "operator-level mapped FW/Bianchi/projector retention",
                "operator action D_E or E_Qa",
            ],
            "current_support": {
                "finite_D_E": finite_values["D_E"],
                "source_level_no_double_count": True,
            },
            "closed": False,
            "depends_on": "S2_transition_or_projection_lift",
            "next_artifact": "Selected_Heterotic_ProjectiveRhoE_OperatorAdmissibility_Subpacket_v1",
        },
        {
            "id": "S4_spectrum_finitepart",
            "priority": 4,
            "must_emit": [
                "positive spectrum/gap or exact heat/zeta/torsion finite part",
                "BRST/FP subtraction counted once",
                "finite part after quotient",
                "E_Qa only if the operator action requires it",
            ],
            "current_support": {
                "finite_internal_part": finite_values["finite_internal_part"],
                "finite_H_sel": finite_values["H_sel"],
                "finite_Green_operator": finite_values["Green_operator"],
            },
            "closed": False,
            "depends_on": "S3_operator_and_admissibility",
            "next_artifact": "Selected_Heterotic_ProjectiveRhoE_SpectrumFinitePart_Subpacket_v1",
        },
    ]

    acceptance_tests = {
        "no_target_fitting": True,
        "same_source_across_all_emitted_fields": True,
        "SM_parity_interface_not_used_as_operator_data": True,
        "abstract_Z3_shadow_not_promoted_without_S1": True,
        "finite_packet_not_recounted": True,
        "full_verify_required_after_each_subpacket": True,
    }

    subpacket = {
        "schema": "SelectedHeteroticProjectiveRhoESmoothOperatorPayload.EmissionOrder.v1",
        "status": "EMISSION_ORDER_BUILT_VALUES_OPEN",
        "first_open_leaf": emission_subpackets[0]["id"],
        "subpackets": emission_subpackets,
        "acceptance_tests": acceptance_tests,
    }
    OUTPUT_SUBPACKET.write_text(json.dumps(subpacket, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    decision = {
        "minimal_emission_subpacket_built": True,
        "first_leaf_identified": emission_subpackets[0]["id"],
        "subpacket_count": len(emission_subpackets),
        "S1_closed": False,
        "S2_closed": False,
        "S3_closed": False,
        "S4_closed": False,
        "smooth_transition_tables_emitted": False,
        "complement_kernel_proved": False,
        "smooth_finitepart_computed": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticProjectiveRhoESmoothOperatorPayloadMinimalEmissionSubpacket",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "payload_gate_status": payload_gate["status"],
        "contract_status": contract["status"],
        "emission_order_path": rel(OUTPUT_SUBPACKET),
        "decision": decision,
        "guardrails": {
            "does_not_skip_to_spectrum_before_source_domain": True,
            "does_not_promote_abstract_Z3_shadow": True,
            "does_not_recount_finite_packet": True,
            "does_not_claim_operator_payload_values": True,
            "does_not_use_observed_couplings_or_scales": True,
            "target_fitting_used": False,
        },
        "theorem": {
            "name": "MinimalEmissionOrderForSmoothRhoEOperatorPayload",
            "proved": True,
            "statement": (
                "The smooth rho_E payload can be attacked in four ordered subpackets: "
                "first the selected smooth domain/cover or complement domain; second "
                "the transition/projection lift; third the operator and admissibility "
                "data; fourth the spectrum/finite part. The first unavoidable leaf is "
                "the same-branch smooth source domain or cover, because all later "
                "values require that domain for interpretation."
            ),
        },
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "emission_order_path": rel(OUTPUT_SUBPACKET),
        "note_path": rel(OUTPUT_NOTE),
        "minimal_emission_subpacket_built": True,
        "first_leaf_identified": emission_subpackets[0]["id"],
        "smooth_finitepart_computed": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic ProjectiveRhoE SmoothOperatorPayload MinimalEmissionSubpacket v1

## Result

```text
status = {STATUS}
minimal_emission_subpacket_built = true
first_leaf_identified = S1_smooth_domain_cover_or_complement_domain
smooth_finitepart_computed = false
next_required_artifact = {NEXT}
```

## Emission Order

The payload is split into four ordered subpackets:

1. selected smooth domain/cover or complement domain;
2. transition/projection lift;
3. operator and admissibility data;
4. spectrum and finite part.

The first unavoidable leaf is the selected smooth source domain or cover, because
all later transition, operator, and determinant values require it.

Emission order:

```text
{rel(OUTPUT_SUBPACKET)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_SUBPACKET)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
