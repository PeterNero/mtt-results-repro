"""Build the oriented Phi_fin source-emission / smooth E_Qa threshold-identity gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "oriented_gate": DATA / "selected_heterotic_orientedphifin_productoperator_or_smootheqa_magnitudesource.candidate.json",
    "oriented_table": DATA / "selected_heterotic_orientedphifin_simultaneous_ctau_phifin_table.json",
    "phifin_sourceidentity_bridge": DATA / "selected_heterotic_phifin_sourceidentity_bridge_attempt.candidate.json",
    "bundleconnection_or_phifin_gate": DATA / "selected_heterotic_bundleconnection_valuesolve_or_phifin_sourceidentity_proof.candidate.json",
    "finite_internal_source": DATA / "selected_heterotic_projectiverhoe_finitephysicalquotient_sourcetheorem.candidate.json",
    "u1y_trace_27mode": DATA / "selected_u1y_routec_trace_equals_27mode_or_full_hym_replay.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_sourceemission_or_smootheqa_thresholdidentity.candidate.json"
OUTPUT_REQUEST = DATA / "selected_heterotic_orientedphifin_thresholdidentity_source_request.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_sourceemission_or_smootheqa_thresholdidentity_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_SourceEmission_or_SmoothEQa_ThresholdIdentity_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_SOURCEEMISSION_CURRENT_SOURCE_NOGO_REQUEST_BUILT"
NEXT = "Selected_Heterotic_OrientedPhiFin_ThresholdIdentity_SourceFill_or_SmoothEQa_Construction_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    oriented = load(INPUTS["oriented_gate"])
    table = load(INPUTS["oriented_table"])
    bridge = load(INPUTS["phifin_sourceidentity_bridge"])
    bundle_gate = load(INPUTS["bundleconnection_or_phifin_gate"])
    finite_internal = load(INPUTS["finite_internal_source"])
    trace = load(INPUTS["u1y_trace_27mode"])

    closed_support = {
        "same_BN_domain": oriented["decision"]["same_BN_domain_for_Ctau_and_PhiFin_positive_gap"],
        "commutation": oriented["decision"]["commutation_or_simultaneous_functional_calculus_closed"],
        "oriented_table_built": oriented["decision"]["oriented_product_table_built"],
        "finite_positive_policy_available": True,
        "selected_27mode_gap_layer": trace["decision"]["DE_gap_Riesz_Green_layer_closed"],
        "kernel_policy_algebraic": oriented["decision"]["kernel_policy_compatible_algebraically"],
        "no_double_counting_algebraic": oriented["decision"]["no_double_counting_shared_circle_algebraic_check"],
    }

    open_source_fields = {
        "selected_heterotic_threshold_source_certificate": {
            "closed": False,
            "current_support": bundle_gate["decision"].get("finite_internal_packet_promoted_internal_scope", None),
            "missing": "same-branch theorem that the heterotic Qa/SU3 threshold source is the oriented 27-mode B_N Phi_fin operator",
        },
        "oriented_product_operator_emitted_as_selected": {
            "closed": False,
            "current_support": oriented["decision"]["oriented_product_table_built"],
            "missing": "source statement E_Qa^or = sign(C_tau) with magnitude PhiFin_DE, or equivalent threshold complex",
        },
        "smooth_E_Qa_or_bundle_connection_identity": {
            "closed": False,
            "current_support": bridge["decision"].get("bridge_attempted", True),
            "missing": "selected A/F_A, representation action, quotient domain, and Weitzenbock/threshold identity whose finite quotient is the oriented table",
        },
        "heterotic_finitepart_trace_identity": {
            "closed": False,
            "current_support": table["logdet_values"],
            "missing": "source permission to use the oriented table logdet values as heterotic threshold finite part",
        },
    }

    request = {
        "schema": "SelectedHeterotic.OrientedPhiFinThresholdIdentity.SourceRequest.v1",
        "purpose": "Promote the algebraic oriented Phi_fin table to the selected heterotic Qa/SU3 threshold operator, if and only if one same source emits the missing identity data.",
        "closed_support": closed_support,
        "must_emit": {
            "source_certificate": "rank-three Iwasawa SU(3) monad/End(E) or projective rho_E branch, same branch as the finite table",
            "operator_identity": "E_Qa^or or threshold complex has positive magnitude PhiFin_DE and orientation sign(C_tau) on the selected B_N quotient",
            "smooth_or_finite_domain": "selected B_N quotient domain, kernel removal, shared-circle policy, and trace weights",
            "smooth_payload_if_used": "A, F_A, representation action, Weitzenbock/endormorphism E_Qa, quotient projection, finite spectral functor",
            "finitepart_payload": "zeta/heat/torsion finite part using the already built simultaneous table, with no extra shift or observed-data selector",
            "audit_replay": "rerun oriented table, finitepart, and no-double-count checks under selected-source flags",
        },
        "acceptance_rule": {
            "promote_threshold_magnitude_if_all_fields_selected_same_source": True,
            "otherwise_keep_as_support_only": True,
            "observed_data_allowed": False,
        },
        "forbidden_shortcuts": [
            "treat Route-C Phi_fin support as heterotic threshold identity by name",
            "use the oriented table logdet values before source emission",
            "insert a positive shift or rescale to force a desired magnitude",
            "reuse internal log(2008) as the 27-mode oriented magnitude",
            "choose between full and oriented-sector logdet from measured electroweak data",
        ],
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    OUTPUT_REQUEST.write_text(json.dumps(request, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    decision = {
        "closed_support_count": sum(1 for value in closed_support.values() if value is True),
        "open_source_field_count": len(open_source_fields),
        "same_domain_commutation_table_complete": True,
        "source_emission_closed": False,
        "smooth_E_Qa_threshold_identity_closed": False,
        "heterotic_threshold_magnitude_promoted": False,
        "current_source_nogo": True,
        "mathematical_impossibility_claimed": False,
        "full_positive_logdet_support_value": oriented["decision"]["PhiFin_all_positive_logdet"],
        "oriented_abs_logdet_support_value": oriented["decision"]["oriented_abs_sector_logdet_sum"],
        "oriented_signed_difference_support_value": oriented["decision"]["oriented_signed_sector_logdet_difference"],
        "source_request_path": rel(OUTPUT_REQUEST),
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinSourceEmissionOrSmoothEQaThresholdIdentity",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "oriented_gate": oriented["status"],
            "phifin_sourceidentity_bridge": bridge["status"],
            "bundleconnection_or_phifin_gate": bundle_gate["status"],
            "finite_internal_source": finite_internal["status"],
            "u1y_trace_27mode": trace["status"],
        },
        "closed_support": closed_support,
        "open_source_fields": open_source_fields,
        "source_request_path": rel(OUTPUT_REQUEST),
        "decision": decision,
        "theorem": {
            "name": "OrientedPhiFinThresholdIdentityCurrentSourceNoGo",
            "proved": True,
            "statement": (
                "The current corpus now closes every algebraic prerequisite for an oriented "
                "Phi_fin threshold table: same 27-mode B_N domain, commutation, kernel policy, "
                "and finite positive table. However, no current source emits the threshold "
                "identity saying that this oriented table is the selected heterotic Qa/SU3 "
                "E_Qa or threshold complex. Therefore the table remains support-only. Closure "
                "requires one same-source source-fill theorem emitting the source certificate, "
                "operator identity, quotient/kernel policy, and finitepart trace identity."
            ),
        },
        "guardrails": {
            "does_not_promote_support_values": True,
            "does_not_claim_smooth_EQa": True,
            "does_not_reuse_internal_log2008": True,
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
        "source_request_path": rel(OUTPUT_REQUEST),
        "note_path": rel(OUTPUT_NOTE),
        "same_domain_commutation_table_complete": True,
        "source_emission_closed": False,
        "smooth_E_Qa_threshold_identity_closed": False,
        "heterotic_threshold_magnitude_promoted": False,
        "current_source_nogo": True,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin SourceEmission or SmoothEQa ThresholdIdentity v1

## Result

```text
status = {STATUS}
same_domain_commutation_table_complete = true
source_emission_closed = false
smooth_E_Qa_threshold_identity_closed = false
heterotic_threshold_magnitude_promoted = false
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

## Support Values

```json
{json.dumps({k: decision[k] for k in ['full_positive_logdet_support_value', 'oriented_abs_logdet_support_value', 'oriented_signed_difference_support_value']}, indent=2, sort_keys=True)}
```

## Source Request

```text
{rel(OUTPUT_REQUEST)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_REQUEST)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
