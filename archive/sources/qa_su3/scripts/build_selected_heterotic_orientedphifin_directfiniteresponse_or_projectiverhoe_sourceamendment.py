"""Build oriented Phi_fin direct finite-response / projective-rhoE source-amendment gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "value_insertion": DATA / "selected_heterotic_orientedphifin_ende_basis_or_nonidentityrhoe_valueinsertion.candidate.json",
    "value_insertion_packet": DATA / "selected_heterotic_orientedphifin_ende_basis_or_nonidentityrhoe_valueinsertion_packet.json",
    "direct_operator_attempt": DATA / "selected_heterotic_phifin_direct_operator_emission_attempt.candidate.json",
    "selected_internal_packet_emission": DATA / "selected_heterotic_projectiverhoe_selectedpacketemission_or_operatoridentity.candidate.json",
    "internal_finitepart": DATA / "selected_heterotic_projectiverhoe_eqa_or_thresholdfinitepart.candidate.json",
    "ew_nonidentity_prefix": DATA / "selected_electroweak_qastack_threshold_operator_from_nonidentity_rhoe_quotientbn.candidate.json",
    "oriented_table": DATA / "selected_heterotic_orientedphifin_simultaneous_ctau_phifin_table.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_directfiniteresponse_or_projectiverhoe_sourceamendment.candidate.json"
OUTPUT_CONTRACT = DATA / "selected_heterotic_orientedphifin_directfiniteresponse_source_contract.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_directfiniteresponse_or_projectiverhoe_sourceamendment_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_DirectFiniteResponse_or_ProjectiveRhoE_SourceAmendment_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_DIRECTFINITE_RESPONSE_CONTRACT_BUILT_VALUES_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_DirectFiniteResponse_FillAttempt_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    value_insertion = load(INPUTS["value_insertion"])
    insertion_packet = load(INPUTS["value_insertion_packet"])
    direct_attempt = load(INPUTS["direct_operator_attempt"])
    internal_emission = load(INPUTS["selected_internal_packet_emission"])
    internal_finitepart = load(INPUTS["internal_finitepart"])
    ew_prefix = load(INPUTS["ew_nonidentity_prefix"])
    oriented_table = load(INPUTS["oriented_table"])

    internal_direct_candidate = {
        "id": "selected_internal_11label_projective_packet",
        "source_emitted": internal_emission["decision"]["selected_finite_internal_packet_emitted"],
        "domain_scope": "selected finite internal 11-label Qa/SU3 projective response",
        "has_D_E_Riesz_Green_trace": internal_emission["emission_checks"]["green_inverse_validated"]
        and internal_emission["emission_checks"]["finite_trace_admissibility_closed"],
        "has_internal_finitepart": internal_finitepart["decision"]["selected_internal_threshold_finitepart_closed"],
        "can_close_oriented_27mode_response": False,
        "why_not": "It is selected internal rho_E data, but not an oriented 27-mode B_N Phi_fin threshold complex.",
    }

    routec_direct_candidate = {
        "id": "routec_27mode_nonidentity_BN_prefix",
        "source_emitted": ew_prefix["decision"]["nonidentity_rhoE_BN_prefix_imported"],
        "domain_scope": "Route-C/electroweak 27-mode B_N prefix support",
        "has_D_E_Riesz_Green_dotD": ew_prefix["prefix_payload"]["D_E_matrix_present"]
        and ew_prefix["prefix_payload"]["Riesz_Green_gap_present"]
        and ew_prefix["prefix_payload"]["dotD_alpha1_present"],
        "has_positive_gap": ew_prefix["prefix_payload"]["BN_complement_gap"] > 0,
        "can_close_oriented_heterotic_response": False,
        "why_not": "The prefix can host a threshold operator, but rhoE_selected_by_mtt and heterotic source identity remain false/open.",
    }

    direct_contract = {
        "schema": "SelectedHeterotic.OrientedPhiFin.DirectFiniteResponse.SourceContract.v1",
        "status": "VALUES_REQUIRED",
        "minimum_payload": {
            "same_branch_source_certificate": False,
            "selected_domain_or_quotient_map_to_oriented_BN": False,
            "D_E_or_EQa_matrix_on_oriented_BN": False,
            "orientation_operator_Ctau_binding": True,
            "Riesz_or_Green_operator": False,
            "positive_spectrum_or_heat_zeta_torsion": False,
            "finitepart_trace_identity_for_oriented_logdet": False,
            "no_double_count_replay": insertion_packet["lane_C_direct_same_source_finite_response"]["required_payload"]["no_double_count_replay"],
        },
        "candidate_sources_tested": {
            "internal_direct_candidate": internal_direct_candidate,
            "routec_direct_candidate": routec_direct_candidate,
        },
        "oriented_values_support": oriented_table["logdet_values"],
        "allowed_repairs": [
            "source-amend projective rho_E representative tables and then bind them to oriented B_N",
            "emit a direct heterotic finite response on oriented B_N with D_E/E_Qa, Riesz/Green, finitepart trace identity",
            "prove same-source identity between Route-C 27-mode prefix and heterotic oriented Phi_fin threshold complex",
        ],
        "forbidden_shortcuts": [
            "promote internal log(2008) as oriented 27-mode threshold",
            "promote Route-C nonidentity prefix as heterotic source identity",
            "use oriented logdet table as finitepart without trace theorem",
            "use observed constants or residuals as selector",
        ],
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    OUTPUT_CONTRACT.write_text(json.dumps(direct_contract, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    decision = {
        "direct_contract_built": True,
        "direct_same_source_finite_response_closed": False,
        "projective_rhoE_source_amendment_closed": False,
        "internal_packet_rejected_as_oriented_response": True,
        "routec_prefix_rejected_as_heterotic_identity": True,
        "orientation_binding_support_closed": True,
        "new_oriented_leaf_closed": False,
        "oriented_logdet_promoted": False,
        "next_required_artifact": NEXT,
        "contract_path": rel(OUTPUT_CONTRACT),
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinDirectFiniteResponseOrProjectiveRhoESourceAmendment",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "value_insertion": value_insertion["status"],
            "direct_operator_attempt": direct_attempt["status"],
            "selected_internal_packet_emission": internal_emission["status"],
            "internal_finitepart": internal_finitepart["status"],
            "ew_nonidentity_prefix": ew_prefix["status"],
        },
        "contract_path": rel(OUTPUT_CONTRACT),
        "decision": decision,
        "theorem": {
            "name": "OrientedPhiFinDirectFiniteResponseContractTheorem",
            "proved": True,
            "statement": (
                "The direct finite-response bypass is legal but not yet filled. The selected "
                "internal 11-label projective packet supplies genuine same-branch finite "
                "operator data only at internal rho_E scope. The Route-C 27-mode nonidentity "
                "B_N prefix supplies the right kind of 27-mode support but is not selected as "
                "the heterotic oriented Phi_fin threshold identity. Therefore the next artifact "
                "must fill the direct response contract itself or source-amend projective rho_E "
                "representative tables; no oriented logdet value is promoted."
            ),
        },
        "guardrails": {
            "does_not_promote_internal_log2008": True,
            "does_not_promote_routec_prefix": True,
            "does_not_promote_oriented_logdets": True,
            "does_not_claim_direct_response_closure": True,
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
        "contract_path": rel(OUTPUT_CONTRACT),
        "note_path": rel(OUTPUT_NOTE),
        "direct_contract_built": True,
        "direct_same_source_finite_response_closed": False,
        "projective_rhoE_source_amendment_closed": False,
        "oriented_logdet_promoted": False,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin DirectFiniteResponse or ProjectiveRhoE SourceAmendment v1

## Result

```text
status = {STATUS}
direct_same_source_finite_response_closed = false
projective_rhoE_source_amendment_closed = false
orientation_binding_support_closed = true
oriented_logdet_promoted = false
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

## Direct Response Contract

```text
{rel(OUTPUT_CONTRACT)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CONTRACT)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
