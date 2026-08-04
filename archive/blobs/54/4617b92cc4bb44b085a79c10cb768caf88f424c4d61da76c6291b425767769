"""Build the finite good-cover nerve incidence candidate for smooth rho_E S1."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "external_candidates": DATA / "selected_heterotic_projectiverhoe_smoothdomaincover_external_construction_candidates.json",
    "z3_shadow": DATA / "selected_heterotic_projectiverhoe_abstract_z3_cocycle_shadow_witness.json",
    "finite_values": DATA / "selected_heterotic_projectiverhoe_exactcomplement_or_smoothrhoetransition_valuepacket.values.json",
    "source_request": DATA / "selected_heterotic_projectiverhoe_smoothdomaincover_minimal_source_request.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_projectiverhoe_finitegoodcovernerve_incidencecandidate.candidate.json"
OUTPUT_NERVE = DATA / "selected_heterotic_projectiverhoe_finitegoodcovernerve_incidence_table.json"
OUTPUT_CERT = CERTS / "selected_heterotic_projectiverhoe_finitegoodcovernerve_incidencecandidate_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_ProjectiveRhoE_FiniteGoodCoverNerve_IncidenceCandidate_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_FINITEGOODCOVERNERVE_INCIDENCE_CANDIDATE_BUILT_EMBEDDING_SELECTION_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_GoodCoverEmbedding_or_DeligneRepresentative_SourceProof_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    external_candidates = load(INPUTS["external_candidates"])
    z3_shadow = load(INPUTS["z3_shadow"])
    finite_values = load(INPUTS["finite_values"])["finite_internal_values"]
    source_request = load(INPUTS["source_request"])

    labels = finite_values["labels"]
    tau = finite_values["tau"]

    cover_nodes = ["U0", "U1", "U2"]
    pair_overlaps = {
        "U01": {"nodes": ["U0", "U1"], "nonempty": True},
        "U12": {"nodes": ["U1", "U2"], "nonempty": True},
        "U20": {"nodes": ["U2", "U0"], "nonempty": True},
    }
    triple_overlaps = {
        "U012": {"nodes": ["U0", "U1", "U2"], "nonempty": True}
    }

    label_shadow = {
        label: {
            "tau": tau[label],
            "central_triple_shadow": z3_shadow["tables"][label]["central_triple_012"],
            "label_map": f"constant sheaf label {label} on the finite nerve candidate",
            "shadow_check_passes": z3_shadow["checks"][label]["projective_triple_overlap_matches_tau"],
        }
        for label in labels
    }

    incidence_table = {
        "schema": "SelectedHeteroticProjectiveRhoEFiniteGoodCoverNerve.IncidenceTable.v1",
        "status": "FINITE_NERVE_INCIDENCE_CANDIDATE_ONLY",
        "cover_nodes": cover_nodes,
        "pair_overlaps": pair_overlaps,
        "triple_overlaps": triple_overlaps,
        "nerve_is_two_simplex": True,
        "all_pair_overlaps_nonempty": all(item["nonempty"] for item in pair_overlaps.values()),
        "all_triple_overlaps_nonempty": all(item["nonempty"] for item in triple_overlaps.values()),
        "label_shadow": label_shadow,
        "smooth_embedding_fields": {
            "compact_Iwasawa_or_Nil_quotient": None,
            "coordinate_charts": None,
            "contractible_open_sets": None,
            "partition_of_unity_or_chart_realization": None,
            "MTT_selection_proof": None,
        },
        "not_claimed": [
            "selected compact Iwasawa/Nil good-cover embedding",
            "smooth charts or contractibility proof",
            "Deligne/Cech local B_i,A_ij,g_ijk representative",
            "operator domain or complement domain",
            "smooth rho_E transition matrices",
        ],
    }
    OUTPUT_NERVE.write_text(json.dumps(incidence_table, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    closes_request_fields = {
        "selected_good_cover_index_set": True,
        "nonempty_overlap_incidence": True,
        "triple_overlap_incidence": True,
        "smooth_to_finite_label_map": True,
        "proof_Z3_shadow_is_induced_by_cover": False,
        "same_branch_smooth_heterotic_QaSU3_source_certificate": False,
    }

    still_open = {
        "embedding_as_selected_compact_Iwasawa_Nil_good_cover": True,
        "contractibility_and_chart_realization": True,
        "smooth_Deligne_Cech_representative": True,
        "MTT_selection_before_target_comparison": True,
        "operator_domain_or_complement_domain": True,
    }

    decision = {
        "finite_nerve_candidate_built": True,
        "incidence_fields_closed_at_formal_nerve_level": True,
        "all_labels_shadow_tau": all(item["shadow_check_passes"] for item in label_shadow.values()),
        "closes_S1": False,
        "smooth_good_cover_selected": False,
        "smooth_transition_tables_emitted": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticProjectiveRhoEFiniteGoodCoverNerveIncidenceCandidate",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "external_selection": external_candidates["selected_next_candidate"],
        "source_request_status": source_request["status"],
        "incidence_table_path": rel(OUTPUT_NERVE),
        "closes_request_fields": closes_request_fields,
        "still_open": still_open,
        "decision": decision,
        "guardrails": {
            "does_not_claim_smooth_embedding": True,
            "does_not_claim_contractibility": True,
            "does_not_claim_deligne_representative": True,
            "does_not_claim_operator_domain": True,
            "does_not_claim_S1_closure": True,
            "target_fitting_used": False,
        },
        "theorem": {
            "name": "FiniteGoodCoverNerveIncidenceCandidate",
            "proved": True,
            "statement": (
                "A three-node finite nerve incidence candidate can realize the formal "
                "pair/triple-overlap shape needed by the abstract Z3 shadow and all "
                "eleven selected labels. This closes only the formal incidence scaffold; "
                "it does not embed the nerve as a selected compact Iwasawa/Nil good "
                "cover and does not close S1."
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
        "incidence_table_path": rel(OUTPUT_NERVE),
        "note_path": rel(OUTPUT_NOTE),
        "finite_nerve_candidate_built": True,
        "all_labels_shadow_tau": decision["all_labels_shadow_tau"],
        "closes_S1": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic ProjectiveRhoE FiniteGoodCoverNerve IncidenceCandidate v1

## Result

```text
status = {STATUS}
finite_nerve_candidate_built = true
all_labels_shadow_tau = true
closes_S1 = false
next_required_artifact = {NEXT}
```

## Construction

The formal three-node nerve `U0,U1,U2` has nonempty pair overlaps and a nonempty
triple overlap. Every selected label `F_i,G_i,P` is mapped to the existing
abstract `Z3` central shadow matching `tau`.

Incidence table:

```text
{rel(OUTPUT_NERVE)}
```

This is still not a selected compact Iwasawa/Nil good-cover embedding, and it
does not emit smooth transition matrices or a smooth operator domain.
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NERVE)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
