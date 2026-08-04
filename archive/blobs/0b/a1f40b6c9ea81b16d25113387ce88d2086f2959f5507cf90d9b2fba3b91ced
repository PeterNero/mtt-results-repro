"""Build the good-cover embedding or Deligne representative source-proof gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "finite_nerve_candidate": DATA / "selected_heterotic_projectiverhoe_finitegoodcovernerve_incidencecandidate.candidate.json",
    "finite_nerve_table": DATA / "selected_heterotic_projectiverhoe_finitegoodcovernerve_incidence_table.json",
    "ctwist_deligne_template": DATA / "ctwist_deligne_cech_template.candidate.json",
    "twisted_source_fill": DATA / "twisted_source_promotion_packet_fill_attempt.candidate.json",
    "smooth_source_request": DATA / "selected_heterotic_projectiverhoe_smoothdomaincover_minimal_source_request.json",
    "finite_representative": DATA / "selected_heterotic_sourceamendment_or_projectiverhoe_representative_tables.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_projectiverhoe_goodcoverembedding_or_deligne_representative_sourceproof.candidate.json"
OUTPUT_REQUEST = DATA / "selected_heterotic_projectiverhoe_chartatlas_delignecech_localfields_request.json"
OUTPUT_CERT = CERTS / "selected_heterotic_projectiverhoe_goodcoverembedding_or_deligne_representative_sourceproof_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_ProjectiveRhoE_GoodCoverEmbedding_or_DeligneRepresentative_SourceProof_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_GOODCOVEREMBEDDING_DELIGNE_SOURCEPROOF_CURRENT_SOURCE_NOGO"
NEXT = "Selected_Heterotic_ProjectiveRhoE_ChartAtlas_DeligneCech_LocalFields_SourceAmendment_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def none_values(mapping: dict[str, Any]) -> bool:
    return all(value is None for value in mapping.values())


def main() -> dict[str, Any]:
    finite_nerve = load(INPUTS["finite_nerve_candidate"])
    nerve_table = load(INPUTS["finite_nerve_table"])
    deligne_template = load(INPUTS["ctwist_deligne_template"])
    twisted_fill = load(INPUTS["twisted_source_fill"])
    smooth_request = load(INPUTS["smooth_source_request"])
    finite_representative = load(INPUTS["finite_representative"])

    required_values = deligne_template["required_source_values"]
    smooth_embedding_fields = nerve_table["smooth_embedding_fields"]
    finite_values = finite_representative["projective_representative_tables"]["fills_finite_candidate_leaves"]

    lane_a_goodcover_embedding = {
        "lane": "A_good_cover_embedding",
        "attempted": True,
        "formal_nerve_incidence_available": finite_nerve["decision"]["finite_nerve_candidate_built"],
        "all_labels_shadow_tau": finite_nerve["decision"]["all_labels_shadow_tau"],
        "selected_compact_iwasawa_nil_embedding_emitted": smooth_embedding_fields["compact_Iwasawa_or_Nil_quotient"] is not None,
        "coordinate_charts_emitted": smooth_embedding_fields["coordinate_charts"] is not None,
        "contractible_open_sets_emitted": smooth_embedding_fields["contractible_open_sets"] is not None,
        "partition_or_chart_realization_emitted": smooth_embedding_fields["partition_of_unity_or_chart_realization"] is not None,
        "mtt_selection_proof_emitted": smooth_embedding_fields["MTT_selection_proof"] is not None,
        "proof_z3_shadow_induced_by_smooth_cover": finite_nerve["closes_request_fields"]["proof_Z3_shadow_is_induced_by_cover"],
        "current_result": "formal incidence scaffold only",
        "closes_s1": False,
    }

    lane_b_deligne_representative = {
        "lane": "B_deligne_cech_representative",
        "attempted": True,
        "deligne_template_available": deligne_template["status"] == "CTWIST_DELIGNE_CECH_TEMPLATE_BUILT_VALUES_OPEN",
        "template_typing_passes_all_products": all(item["passes_template_typing"] for item in deligne_template["product_checks"]),
        "local_B_i_A_ij_g_ijk_emitted": required_values["B_i"] is not None and required_values["A_ij"] is not None and required_values["g_ijk"] is not None,
        "explicit_good_cover_emitted": required_values["explicit_good_cover"] is not None,
        "tau_or_DD_class_emitted": required_values["tau_or_DD_class"] is not None,
        "twisted_section_bases_emitted": required_values["twisted_section_bases"] is not None,
        "multiplication_constants_emitted": required_values["multiplication_constants"] is not None,
        "maps_to_required_c_twists": deligne_template["promotion_tests"]["maps_to_required_c_twists"],
        "current_result": "typed Deligne/Cech shape only",
        "closes_s1": False,
    }

    finite_packet_bridge = {
        "finite_tau_values_available": True,
        "finite_rhoE_character_available": True,
        "finite_D_E_Green_Riesz_available": True,
        "finite_cocycle_law_checked": finite_values["central_cocycle_law_checked"],
        "finite_packet_can_supply_target_shadow": True,
        "finite_packet_can_replace_smooth_local_fields": False,
        "reason": (
            "The finite packet fixes the internal quotient response and the central "
            "shadow, but it does not provide a smooth chart atlas, Deligne local "
            "forms/functions, or a same-source smooth operator domain."
        ),
    }

    request = {
        "schema": "SelectedHeteroticProjectiveRhoE.ChartAtlasDeligneCechLocalFieldsRequest.v1",
        "status": "SOURCE_AMENDMENT_REQUIRED",
        "purpose": (
            "Close S1 by supplying either a selected compact Iwasawa/Nil chart "
            "atlas realizing the three-node nerve, or selected Deligne/Cech local "
            "fields whose triple cocycle maps to the finite tau table."
        ),
        "required_good_cover_embedding_payload": {
            "selected_compact_Iwasawa_or_Nil_quotient": None,
            "lattice_or_nilmanifold_definition": None,
            "coordinate_charts_U0_U1_U2": None,
            "contractibility_proof_for_Ui_and_all_nonempty_overlaps": None,
            "nonempty_pair_and_triple_overlap_realization": None,
            "partition_of_unity_or_smooth_chart_realization": None,
            "smooth_to_finite_label_map_for_Fi_Gi_P": None,
            "proof_Z3_shadow_induced_by_cover_not_assigned_afterward": None,
            "MTT_selection_proof_before_target_comparison": None,
        },
        "required_deligne_cech_payload": {
            "explicit_good_cover": None,
            "B_i_local_two_forms": None,
            "A_ij_overlap_one_forms": None,
            "g_ijk_triple_overlap_U1_functions": None,
            "quadruple_overlap_cocycle_identity_or_vacuous_cover_proof": None,
            "tau_or_DD_class": None,
            "h_ij_for_T_plus_and_T_minus": None,
            "ordinary_ab_line_bundle_factors": None,
            "twisted_section_bases": None,
            "multiplication_constants_Fi_Gi_to_P": None,
            "map_to_finite_tau_table": None,
        },
        "required_operator_admissibility_payload_after_s1": {
            "mapped_Freed_Witten_check": None,
            "mapped_Green_Schwarz_Bianchi_check": None,
            "metric_or_unitarity_compatibility": None,
            "twisted_projector_retention": None,
            "smooth_operator_domain_or_complement_domain": None,
        },
        "finite_target_shadow_allowed_as_check_only": {
            "tau": finite_values["tau_values"],
            "rho_E_central_character": finite_values["rho_E_central_character"],
            "D_E": finite_values["D_E"],
            "Green_operator": finite_values["Green_operator"],
            "Riesz_projector": finite_values["Riesz_projector"],
        },
        "forbidden_shortcuts": [
            "promoting the formal three-node nerve as a smooth cover",
            "promoting Deligne/Cech template variables as local fields",
            "importing q79/S3 Deligne values as Qa/SU3 source values",
            "using observed couplings, masses, or target residuals to choose the cover",
            "assigning the Z3 shadow after the finite tau table instead of deriving it from the smooth source",
        ],
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    OUTPUT_REQUEST.write_text(json.dumps(request, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    decision = {
        "goodcover_embedding_attempted": True,
        "deligne_representative_attempted": True,
        "formal_nerve_incidence_available": lane_a_goodcover_embedding["formal_nerve_incidence_available"],
        "ctwist_deligne_template_available": lane_b_deligne_representative["deligne_template_available"],
        "selected_compact_iwasawa_nil_embedding_emitted": lane_a_goodcover_embedding["selected_compact_iwasawa_nil_embedding_emitted"],
        "contractible_chart_atlas_emitted": lane_a_goodcover_embedding["contractible_open_sets_emitted"],
        "local_B_i_A_ij_g_ijk_emitted": lane_b_deligne_representative["local_B_i_A_ij_g_ijk_emitted"],
        "tau_shadow_induced_by_smooth_cover": lane_a_goodcover_embedding["proof_z3_shadow_induced_by_smooth_cover"],
        "finite_packet_remains_valid_internal_check": True,
        "S1_closed": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticProjectiveRhoEGoodCoverEmbeddingOrDeligneRepresentativeSourceProof",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "lane_a_goodcover_embedding": lane_a_goodcover_embedding,
        "lane_b_deligne_representative": lane_b_deligne_representative,
        "finite_packet_bridge": finite_packet_bridge,
        "source_amendment_request_path": rel(OUTPUT_REQUEST),
        "decision": decision,
        "guardrails": {
            "does_not_promote_formal_nerve_to_smooth_cover": True,
            "does_not_promote_ctwist_template_to_values": True,
            "does_not_import_q79_deligne_values": True,
            "does_not_use_observed_data": True,
            "does_not_claim_s1_closure": True,
            "target_fitting_used": False,
        },
        "theorem": {
            "name": "GoodCoverEmbeddingOrDeligneRepresentativeCurrentSourceNoGo",
            "proved": True,
            "statement": (
                "Given the current source state, the finite three-node nerve and "
                "the Deligne/Cech template jointly determine the required smooth "
                "payload shape, but neither emits the selected compact Iwasawa/Nil "
                "good-cover embedding nor the local B_i,A_ij,g_ijk representative. "
                "Therefore S1 remains open, and the next source amendment must "
                "supply explicit chart-atlas or Deligne/Cech local-field data."
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
        "source_amendment_request_path": rel(OUTPUT_REQUEST),
        "note_path": rel(OUTPUT_NOTE),
        "goodcover_embedding_attempted": True,
        "deligne_representative_attempted": True,
        "formal_nerve_incidence_available": True,
        "ctwist_deligne_template_available": True,
        "smooth_embedding_fields_null": none_values(smooth_embedding_fields),
        "deligne_required_values_null": none_values(required_values),
        "S1_closed": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic ProjectiveRhoE GoodCoverEmbedding or DeligneRepresentative SourceProof v1

## Result

```text
status = {STATUS}
formal_nerve_incidence_available = true
ctwist_deligne_template_available = true
S1_closed = false
next_required_artifact = {NEXT}
```

## Proof gate

The current source has a formal three-node nerve and an abstract `Z3` shadow
matching the finite `tau` table. It also has the Deligne/Cech gerbe equation
template. These two objects specify the shape of the missing smooth source, but
they do not emit a selected compact Iwasawa/Nil chart atlas or local
`B_i,A_ij,g_ijk` fields.

The finite `rho_E/D_E/Green/Riesz` packet therefore remains a valid internal
check, not a substitute for smooth local data.

Source-amendment request:

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
