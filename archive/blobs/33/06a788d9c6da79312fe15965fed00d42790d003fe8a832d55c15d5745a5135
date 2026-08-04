"""Build the smooth domain/cover source-amendment or external-construction gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "s1_nogo": DATA / "selected_heterotic_projectiverhoe_smoothdomaincover_sourceleaf_or_directcomplementdomain.candidate.json",
    "source_request": DATA / "selected_heterotic_projectiverhoe_smoothdomaincover_minimal_source_request.json",
    "z3_shadow": DATA / "selected_heterotic_projectiverhoe_abstract_z3_cocycle_shadow_witness.json",
    "finite_values": DATA / "selected_heterotic_projectiverhoe_exactcomplement_or_smoothrhoetransition_valuepacket.values.json",
    "phifin_external_clues": DATA / "selected_u1y_routec_phifin_external_clues.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_projectiverhoe_smoothdomaincover_sourceamendment_or_externalconstruction.candidate.json"
OUTPUT_CANDIDATES = DATA / "selected_heterotic_projectiverhoe_smoothdomaincover_external_construction_candidates.json"
OUTPUT_CERT = CERTS / "selected_heterotic_projectiverhoe_smoothdomaincover_sourceamendment_or_externalconstruction_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_ProjectiveRhoE_SmoothDomainCover_SourceAmendment_or_ExternalConstruction_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_SMOOTHDOMAINCOVER_EXTERNAL_CONSTRUCTION_CANDIDATES_BUILT_SELECTION_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_FiniteGoodCoverNerve_IncidenceCandidate_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    s1_nogo = load(INPUTS["s1_nogo"])
    source_request = load(INPUTS["source_request"])
    z3_shadow = load(INPUTS["z3_shadow"])
    finite_values = load(INPUTS["finite_values"])["finite_internal_values"]
    phifin_clues = load(INPUTS["phifin_external_clues"])

    construction_candidates = [
        {
            "id": "A_finite_good_cover_nerve",
            "template": source_request["acceptable_external_construction_templates"][0],
            "buildable_now": True,
            "what_can_be_built": [
                "finite nerve incidence candidate with nonempty pair and triple overlaps",
                "label map to F_i,G_i,P",
                "compatibility requirement that triple-overlap class shadows tau",
            ],
            "what_still_blocks_selection": [
                "embedding of the nerve as a selected compact Iwasawa/Nil good cover",
                "smooth partition/domain charts and transition maps",
                "proof MTT selects this cover before target comparison",
            ],
            "closes_S1_now": False,
            "next_artifact": "Selected_Heterotic_ProjectiveRhoE_FiniteGoodCoverNerve_IncidenceCandidate_v1",
        },
        {
            "id": "B_deligne_cech_gerbe_representative",
            "template": source_request["acceptable_external_construction_templates"][1],
            "buildable_now": False,
            "what_can_be_built": [
                "abstract Z3 cocycle shadow already exists",
                "finite tau labels already exist",
            ],
            "what_still_blocks_selection": [
                "local B_i, A_ij, g_ijk data",
                "smooth cover incidence",
                "map from smooth Deligne/Cech gerbe class to finite tau",
            ],
            "closes_S1_now": False,
            "next_artifact": "Selected_Heterotic_ProjectiveRhoE_DeligneCechGerbeRepresentative_SourceAmendment_v1",
        },
        {
            "id": "C_strominger_hym_operator_domain",
            "template": source_request["acceptable_external_construction_templates"][2],
            "buildable_now": False,
            "what_can_be_built": [
                "same-branch Strominger/Iwasawa context support",
                "finite internal operator support",
            ],
            "what_still_blocks_selection": [
                "closed smooth operator domain and boundary/quotient policy",
                "smooth-to-finite projection P11",
                "complement domain after gauge quotient",
            ],
            "closes_S1_now": False,
            "next_artifact": "Selected_Heterotic_ProjectiveRhoE_StromingerHYM_DomainPayload_v1",
        },
        {
            "id": "D_feec_galerkin_commuting_projection",
            "template": source_request["acceptable_external_construction_templates"][3],
            "buildable_now": False,
            "what_can_be_built": [
                "external FEEC/Galerkin construction pattern",
                "finite eleven-label codomain",
                "finite gap/Green support",
            ],
            "what_still_blocks_selection": [
                "selected smooth complex",
                "actual finite subcomplex basis",
                "commuting projection proof from smooth cochains to F_i,G_i,P",
            ],
            "closes_S1_now": False,
            "next_artifact": "Selected_Heterotic_ProjectiveRhoE_FEECProjection_SourceAmendment_v1",
        },
    ]

    candidates = {
        "schema": "SelectedHeteroticProjectiveRhoESmoothDomainCover.ExternalConstructionCandidates.v1",
        "status": "CANDIDATES_BUILT_SELECTION_OPEN",
        "source_request_path": rel(INPUTS["source_request"]),
        "finite_labels": finite_values["labels"],
        "z3_shadow_status": z3_shadow["status"],
        "phifin_external_clue_status": phifin_clues["status"],
        "construction_candidates": construction_candidates,
        "selected_next_candidate": "A_finite_good_cover_nerve",
        "selection_reason": (
            "It is the only candidate whose incidence scaffold can be constructed "
            "immediately without pretending to know smooth Deligne fields, operator "
            "domains, or FEEC projection bases."
        ),
    }
    OUTPUT_CANDIDATES.write_text(json.dumps(candidates, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    decision = {
        "external_construction_gate_built": True,
        "candidate_count": len(construction_candidates),
        "selected_next_candidate": "A_finite_good_cover_nerve",
        "any_candidate_closes_S1_now": any(item["closes_S1_now"] for item in construction_candidates),
        "finite_good_cover_nerve_candidate_buildable": True,
        "smooth_domain_or_cover_selected": False,
        "direct_complement_domain_selected": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticProjectiveRhoESmoothDomainCoverSourceAmendmentOrExternalConstruction",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "s1_nogo_status": s1_nogo["status"],
        "construction_candidates_path": rel(OUTPUT_CANDIDATES),
        "decision": decision,
        "guardrails": {
            "does_not_claim_external_template_as_source": True,
            "does_not_claim_good_cover_embedding": True,
            "does_not_claim_deligne_representative": True,
            "does_not_claim_operator_domain": True,
            "does_not_claim_feec_projection": True,
            "target_fitting_used": False,
        },
        "theorem": {
            "name": "SmoothDomainCoverExternalConstructionTriage",
            "proved": True,
            "statement": (
                "The S1 source amendment has four legal external construction "
                "templates. The only immediately executable one is the finite "
                "good-cover nerve incidence candidate. It can build an incidence "
                "scaffold compatible with the finite labels and abstract Z3 shadow, "
                "but it does not select a compact Iwasawa/Nil smooth good cover or "
                "close the first payload leaf."
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
        "construction_candidates_path": rel(OUTPUT_CANDIDATES),
        "note_path": rel(OUTPUT_NOTE),
        "external_construction_gate_built": True,
        "any_candidate_closes_S1_now": decision["any_candidate_closes_S1_now"],
        "selected_next_candidate": "A_finite_good_cover_nerve",
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic ProjectiveRhoE SmoothDomainCover SourceAmendment or ExternalConstruction v1

## Result

```text
status = {STATUS}
external_construction_gate_built = true
any_candidate_closes_S1_now = false
selected_next_candidate = A_finite_good_cover_nerve
next_required_artifact = {NEXT}
```

## Triage

Four legal external-construction templates were compared. Only the finite
good-cover nerve incidence candidate can be built immediately. It will not close
S1 by itself, but it can give the first concrete incidence scaffold that a later
selected compact Iwasawa/Nil cover or Deligne/Cech representative must realize.

Candidate table:

```text
{rel(OUTPUT_CANDIDATES)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_CANDIDATES)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
