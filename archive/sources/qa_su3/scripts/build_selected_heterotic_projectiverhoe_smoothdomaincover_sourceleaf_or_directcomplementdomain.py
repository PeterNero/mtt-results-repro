"""Build the first-leaf smooth domain/cover or direct complement-domain attempt."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "emission_order": DATA / "selected_heterotic_projectiverhoe_smoothoperatorpayload_emission_order.json",
    "payload_contract": DATA / "selected_heterotic_projectiverhoe_smooth_operator_payload_minimal_contract.json",
    "smooth_source_fill": DATA / "selected_heterotic_projectiverhoe_smoothoperator_sourcepacket_fillattempt.candidate.json",
    "smooth_missing_leaves": DATA / "selected_heterotic_projectiverhoe_smoothoperator_sourcepacket_missing_leaves.json",
    "smooth_promotion_template": DATA / "selected_heterotic_projectiverhoe_smooth_promotion.template.json",
    "finite_tables": DATA / "selected_heterotic_sourceamendment_or_projectiverhoe_representative_tables.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_projectiverhoe_smoothdomaincover_sourceleaf_or_directcomplementdomain.candidate.json"
OUTPUT_REQUEST = DATA / "selected_heterotic_projectiverhoe_smoothdomaincover_minimal_source_request.json"
OUTPUT_CERT = CERTS / "selected_heterotic_projectiverhoe_smoothdomaincover_sourceleaf_or_directcomplementdomain_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_ProjectiveRhoE_SmoothDomainCover_SourceLeaf_or_DirectComplementDomain_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_SMOOTHDOMAINCOVER_FIRSTLEAF_CURRENT_SOURCE_NOGO_REQUEST_BUILT"
NEXT = "Selected_Heterotic_ProjectiveRhoE_SmoothDomainCover_SourceAmendment_or_ExternalConstruction_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    emission_order = load(INPUTS["emission_order"])
    payload_contract = load(INPUTS["payload_contract"])
    smooth_fill = load(INPUTS["smooth_source_fill"])
    missing_leaves = load(INPUTS["smooth_missing_leaves"])
    smooth_template = load(INPUTS["smooth_promotion_template"])
    finite_tables = load(INPUTS["finite_tables"])

    first_leaf = emission_order["subpackets"][0]
    finite_representative = finite_tables["projective_representative_tables"]

    domain_attempt = {
        "same_branch_smooth_heterotic_QaSU3_source_certificate": {
            "support_present": smooth_fill["fill_result"]["same_branch_strominger_iwasawa_context"],
            "selected_emitted": False,
            "reason": "same-branch Strominger/Iwasawa context is present, but no selected smooth Qa/SU3 source certificate is emitted",
        },
        "selected_good_cover_incidence": {
            "support_present": False,
            "selected_emitted": False,
            "reason": "current artifacts do not print a selected good-cover index set with overlap/triple-overlap incidence",
        },
        "selected_smooth_operator_domain": {
            "support_present": False,
            "selected_emitted": False,
            "reason": "current artifacts do not define Dom(D_smooth) or a smooth complement operator domain",
        },
        "smooth_to_eleven_label_quotient_map": {
            "support_present": True,
            "selected_emitted": False,
            "reason": "finite eleven-label quotient is closed, but the smooth-to-finite quotient map is not emitted",
        },
        "z3_shadow_as_shadow_of_this_source": {
            "support_present": True,
            "selected_emitted": False,
            "reason": "abstract Z3 shadow is closed, but not tied to a selected smooth cover/domain",
        },
    }

    direct_complement_attempt = {
        "smooth_operator_domain": {
            "support_present": False,
            "selected_emitted": False,
            "reason": "no direct smooth threshold/complement domain is emitted",
        },
        "projection_P11": {
            "support_present": True,
            "selected_emitted": False,
            "reason": "finite label projector is known internally, but no smooth projection P11 is emitted",
        },
        "D_comp_domain": {
            "support_present": False,
            "selected_emitted": False,
            "reason": "no complement domain or boundary condition data exist",
        },
    }

    request = {
        "schema": "SelectedHeteroticProjectiveRhoESmoothDomainCover.MinimalSourceRequest.v1",
        "status": "SOURCE_VALUES_REQUIRED",
        "lane_A_required_first_leaf": {
            "same_branch_smooth_heterotic_QaSU3_source_certificate": None,
            "selected_good_cover_index_set": None,
            "nonempty_overlap_incidence": None,
            "triple_overlap_incidence": None,
            "smooth_to_finite_label_map": None,
            "proof_Z3_shadow_is_induced_by_cover": None,
        },
        "lane_B_required_first_leaf": {
            "selected_smooth_operator_domain": None,
            "boundary_conditions_or_closed_domain": None,
            "smooth_to_finite_projection_P11": None,
            "complement_domain_definition": None,
            "proof_domain_decomposition_after_gauge_quotient": None,
        },
        "must_not_use": [
            "finite eleven-label quotient alone",
            "abstract Z3 shadow alone",
            "generic Iwasawa manifold name without cover/domain data",
            "SM parity interface replacement",
            "observed coupling or threshold values",
        ],
        "acceptable_external_construction_templates": [
            "explicit finite good-cover of compact Iwasawa/Nil quotient with overlap incidence",
            "Deligne/Cech gerbe representative whose triple-overlap class maps to tau",
            "Strominger/HYM smooth operator domain with quotient projection to F_i,G_i,P",
            "FEEC/Galerkin-style commuting projection from smooth complex to eleven-label quotient",
        ],
    }
    OUTPUT_REQUEST.write_text(json.dumps(request, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    current_source_nogo = (
        all(item["selected_emitted"] is False for item in domain_attempt.values())
        and all(item["selected_emitted"] is False for item in direct_complement_attempt.values())
    )

    decision = {
        "first_leaf_attempted": True,
        "first_leaf_id": first_leaf["id"],
        "domain_cover_leaf_closed": False,
        "direct_complement_domain_closed": False,
        "current_source_nogo_for_S1": current_source_nogo,
        "minimal_source_request_built": True,
        "smooth_transition_tables_emitted": False,
        "smooth_finitepart_computed": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticProjectiveRhoESmoothDomainCoverSourceLeafOrDirectComplementDomain",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "first_leaf": first_leaf,
        "domain_cover_attempt": domain_attempt,
        "direct_complement_attempt": direct_complement_attempt,
        "minimal_source_request_path": rel(OUTPUT_REQUEST),
        "finite_representative_scope": finite_representative["scope"],
        "payload_contract_status": payload_contract["status"],
        "smooth_template_status": smooth_template.get("status", "UNKNOWN"),
        "missing_leaf_count_carried": len(missing_leaves) if isinstance(missing_leaves, list) else sum(len(v) if isinstance(v, list) else 1 for v in missing_leaves.values()),
        "decision": decision,
        "guardrails": {
            "does_not_claim_smooth_cover_from_finite_quotient": True,
            "does_not_claim_domain_from_iwasawa_name_only": True,
            "does_not_promote_Z3_shadow_to_cover": True,
            "does_not_use_SM_parity_as_domain": True,
            "does_not_use_observed_data": True,
            "target_fitting_used": False,
        },
        "theorem": {
            "name": "SmoothDomainCoverFirstLeafCurrentSourceNoGo",
            "proved": True,
            "statement": (
                "The current repository does not emit the first smooth rho_E payload "
                "leaf: neither a selected good-cover/domain with smooth-to-finite map "
                "nor a direct smooth complement domain is present. Existing data supply "
                "support context, finite quotient labels, and an abstract Z3 shadow, but "
                "those are not enough to interpret smooth transition, operator, or "
                "determinant values. A source amendment or external construction must "
                "provide the listed first-leaf data before S2-S4 can close."
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
        "minimal_source_request_path": rel(OUTPUT_REQUEST),
        "note_path": rel(OUTPUT_NOTE),
        "current_source_nogo_for_S1": current_source_nogo,
        "domain_cover_leaf_closed": False,
        "direct_complement_domain_closed": False,
        "smooth_finitepart_computed": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic ProjectiveRhoE SmoothDomainCover SourceLeaf or DirectComplementDomain v1

## Result

```text
status = {STATUS}
current_source_nogo_for_S1 = true
domain_cover_leaf_closed = false
direct_complement_domain_closed = false
next_required_artifact = {NEXT}
```

## Meaning

The first smooth payload leaf is not present in the current source. We have
finite quotient labels and an abstract `Z3` shadow, but not the selected smooth
cover/domain that makes later transition, operator, and determinant values
meaningful.

Minimal source request:

```text
{rel(OUTPUT_REQUEST)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_REQUEST)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
