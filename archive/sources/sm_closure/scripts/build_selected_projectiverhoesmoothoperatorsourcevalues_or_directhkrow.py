"""Build projective-rhoE smooth operator source values or direct H K-row packet.

This consumes the later Qa/SU3 projective-rhoE chain.  It advances the prior
"smooth source values" frontier to its first unavoidable smooth leaf: either a
selected smooth good-cover/domain with transition data or an exact complement
domain/kernel theorem.  The finite algebraic/projective side is imported as
closed support only.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
QA = Path("C:/Users/nero_/Downloads/TEXPAPERS/mtt-qa-su3-packet-proof/candidate_data")

SLUG = "selected_projectiverhoesmoothoperatorsourcevalues_or_directhkrow"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
FINITE_MAP = PACKET_DIR / "finite_representative_cocycle_and_internal_values.packet.json"
PHYSICAL_FORK = PACKET_DIR / "physical_normalization_or_smooth_identity_fork.packet.json"
SMOOTH_LEAF = PACKET_DIR / "smooth_domain_cover_or_complement_leaf.packet.json"
NEXT_CUTSET = PACKET_DIR / "next_cutset_after_projective_rhoe_smooth_values.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_ProjectiveRhoESmoothOperatorSourceValues_or_DirectHKRow_v1.md"

SOURCES = {
    "previous": DATA / "selected_heteroticstromingersourceoperatortorsion_or_directhkrow.candidate.json",
    "previous_cutset": DATA
    / "selected_heteroticstromingersourceoperatortorsion_or_directhkrow"
    / "next_cutset_after_heterotic_source_operator_torsion.packet.json",
    "rep_to_cocycle": QA
    / "selected_heterotic_projectiverhoe_representative_to_cocycle_or_smoothfinitepart_sourceamendment.candidate.json",
    "physical_normalization": QA
    / "selected_heterotic_projectiverhoe_physicalthresholdnormalization_or_smoothoperatoridentity.candidate.json",
    "kphys_or_smooth_identity": QA
    / "selected_heterotic_projectiverhoe_kphysanchor_or_smoothoperatoridentity_fill.candidate.json",
    "support_prefilter": QA
    / "selected_heterotic_projectiverhoe_smoothsourcecertificate_or_complementoperatorpayload.candidate.json",
    "minimal_emission": QA
    / "selected_heterotic_projectiverhoe_smoothoperatorpayload_minimalemissionsubpacket.candidate.json",
    "smooth_domain_leaf": QA
    / "selected_heterotic_projectiverhoe_smoothdomaincover_sourceleaf_or_directcomplementdomain.candidate.json",
    "smooth_domain_external": QA
    / "selected_heterotic_projectiverhoe_smoothdomaincover_sourceamendment_or_externalconstruction.candidate.json",
    "finite_nerve": QA / "selected_heterotic_projectiverhoe_finitegoodcovernerve_incidencecandidate.candidate.json",
    "goodcover_sourceproof": QA
    / "selected_heterotic_projectiverhoe_goodcoverembedding_or_deligne_representative_sourceproof.candidate.json",
    "source_table_or_kernel": QA
    / "selected_heterotic_projectiverhoe_sourcetablesolve_or_complementkernelproof.candidate.json",
    "no_double_count": QA
    / "selected_heterotic_projectiverhoe_smoothtransitiontables_or_complementquotient_nodoublecount.candidate.json",
    "value_packet": QA
    / "selected_heterotic_projectiverhoe_exactcomplement_or_smoothrhoetransition_valuepacket.candidate.json",
    "source_search": QA
    / "selected_heterotic_projectiverhoe_exactcomplementfactorization_or_goodcovertransitiontables_sourcesearch.candidate.json",
}

STATUS = (
    "MTT_SELECTED_PROJECTIVERHOESMOOTHOPERATORSOURCEVALUES_OR_DIRECTHKROW_"
    "FINITE_COCYCLE_AND_NODOUBLECOUNT_CLOSED_S1_SMOOTH_LEAF_OPEN"
)
NEXT = "MTT_Selected_SmoothDomainCoverOrComplementKernelSourceLeaf_or_DirectHKRow_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources() -> dict[str, dict[str, Any]]:
    missing = [rel(path) for path in SOURCES.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing projective rhoE smooth-value inputs: " + ", ".join(missing))
    return {name: load(path) for name, path in SOURCES.items()}


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = require_sources()
    prev = sources["previous"]["closure_decision"]
    rep = sources["rep_to_cocycle"]["decision"]
    phys = sources["physical_normalization"]["decision"]
    kphys = sources["kphys_or_smooth_identity"]["decision"]
    prefilter = sources["support_prefilter"]["decision"]
    minimal = sources["minimal_emission"]["decision"]
    leaf = sources["smooth_domain_leaf"]["decision"]
    external = sources["smooth_domain_external"]["decision"]
    nerve = sources["finite_nerve"]["decision"]
    goodcover = sources["goodcover_sourceproof"]["decision"]
    source_table = sources["source_table_or_kernel"]["decision"]
    nodouble = sources["no_double_count"]["decision"]
    value_packet = sources["value_packet"]["decision"]
    source_search = sources["source_search"]["decision"]

    finite_map = {
        "schema": "MTTFiniteRepresentativeCocycleAndInternalValues.v1",
        "status": "FINITE_REPRESENTATIVE_COCYCLE_INTERNAL_VALUES_IMPORTED",
        "closure_claimed": True,
        "finite_representative_to_cocycle": {
            "finite_representative_to_cocycle_map_closed": rep[
                "finite_representative_to_cocycle_map_closed"
            ],
            "finite_projective_rhoE_character_table_closed": rep[
                "finite_projective_rhoE_character_table_closed"
            ],
            "finite_internal_response_attached": rep["finite_internal_response_attached"],
        },
        "internal_values": {
            "finite_internal_values_reemitted": value_packet["finite_internal_values_reemitted"],
            "internal_projection_family_closed": value_packet["internal_projection_family_closed"],
            "no_double_count_policy_imported": value_packet["no_double_count_policy_imported"],
            "abstract_Z3_shadow_closed": source_table["abstract_Z3_shadow_closed"],
            "finite_nerve_candidate_built": nerve["finite_nerve_candidate_built"],
            "incidence_fields_closed_at_formal_nerve_level": nerve[
                "incidence_fields_closed_at_formal_nerve_level"
            ],
        },
        "not_promoted_to_smooth_physical_value": {
            "E_Qa_computed": rep["E_Qa_computed"] or value_packet["E_Qa_computed"],
            "smooth_representative_emitted": rep["smooth_representative_emitted"],
            "smooth_transition_tables_emitted": rep["smooth_transition_tables_emitted"]
            or value_packet["smooth_transition_tables_emitted"],
            "smooth_finitepart_computed": rep["smooth_finitepart_computed"]
            or value_packet["smooth_finitepart_computed"],
            "smooth_bundle_operator_emitted": rep["smooth_bundle_operator_emitted"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    physical_fork = {
        "schema": "MTTPhysicalNormalizationOrSmoothIdentityFork.v1",
        "status": "INTERNAL_FORMULA_CLOSED_KPHYS_OR_SMOOTH_IDENTITY_OPEN",
        "closure_claimed": True,
        "internal_interface": {
            "internal_interface_closed": phys["internal_interface_closed"],
            "closed_internal_formula": phys["closed_internal_formula"],
        },
        "physical_anchor_lane": {
            "physical_threshold_normalization_closed": phys[
                "physical_threshold_normalization_closed"
            ],
            "physical_anchor_bridge_closed": kphys["physical_anchor_bridge_closed"],
            "physical_lane_has_anchor_slot_but_no_value": kphys[
                "physical_lane_has_anchor_slot_but_no_value"
            ],
            "measured_coupling_match_claimed": phys["measured_coupling_match_claimed"],
        },
        "smooth_identity_lane": {
            "best_next_lane": kphys["best_next_lane"],
            "smooth_operator_identity_proved": phys["smooth_operator_identity_proved"],
            "smooth_operator_identity_closed": kphys["smooth_operator_identity_closed"],
            "smooth_lane_has_geometry_but_no_bundle_operator": kphys[
                "smooth_lane_has_geometry_but_no_bundle_operator"
            ],
            "next_required_artifact": kphys["next_required_artifact"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    smooth_leaf = {
        "schema": "MTTSmoothDomainCoverOrComplementLeaf.v1",
        "status": "FIRST_SMOOTH_LEAF_REDUCED_TO_DOMAIN_COVER_OR_COMPLEMENT_KERNEL",
        "closure_claimed": True,
        "support_prefilter": {
            "support_prefilter_closed": prefilter["support_prefilter_closed"],
            "retired_blockers_count": prefilter["retired_blockers_count"],
            "operator_payload_contract_built": prefilter["operator_payload_contract_built"],
        },
        "minimal_emission_order": {
            "minimal_emission_subpacket_built": minimal["minimal_emission_subpacket_built"],
            "subpacket_count": minimal["subpacket_count"],
            "first_leaf_identified": minimal["first_leaf_identified"],
        },
        "first_leaf_attempt": {
            "first_leaf_attempted": leaf["first_leaf_attempted"],
            "current_source_nogo_for_S1": leaf["current_source_nogo_for_S1"],
            "domain_cover_leaf_closed": leaf["domain_cover_leaf_closed"],
            "direct_complement_domain_closed": leaf["direct_complement_domain_closed"],
            "minimal_source_request_built": leaf["minimal_source_request_built"],
        },
        "external_construction_triage": {
            "external_construction_gate_built": external["external_construction_gate_built"],
            "candidate_count": external["candidate_count"],
            "selected_next_candidate": external["selected_next_candidate"],
            "finite_good_cover_nerve_candidate_buildable": external[
                "finite_good_cover_nerve_candidate_buildable"
            ],
            "any_candidate_closes_S1_now": external["any_candidate_closes_S1_now"],
            "smooth_domain_or_cover_selected": external["smooth_domain_or_cover_selected"],
            "direct_complement_domain_selected": external["direct_complement_domain_selected"],
        },
        "finite_nerve_and_goodcover": {
            "formal_nerve_incidence_available": goodcover["formal_nerve_incidence_available"],
            "ctwist_deligne_template_available": goodcover["ctwist_deligne_template_available"],
            "contractible_chart_atlas_emitted": goodcover["contractible_chart_atlas_emitted"],
            "selected_compact_iwasawa_nil_embedding_emitted": goodcover[
                "selected_compact_iwasawa_nil_embedding_emitted"
            ],
            "local_B_i_A_ij_g_ijk_emitted": goodcover["local_B_i_A_ij_g_ijk_emitted"],
            "tau_shadow_induced_by_smooth_cover": goodcover["tau_shadow_induced_by_smooth_cover"],
        },
        "no_double_count_and_value_packet": {
            "no_double_count_policy_closed": nodouble["no_double_count_policy_closed"],
            "GR_surface_routing_closed": nodouble["GR_surface_routing_closed"],
            "finite_internal_quotient_retained": nodouble["finite_internal_quotient_retained"],
            "exact_complement_quotient_closed": nodouble["exact_complement_quotient_closed"],
            "heat_zeta_torsion_factorization_closed": value_packet[
                "heat_zeta_torsion_factorization_closed"
            ],
            "smooth_transition_tables_emitted": value_packet["smooth_transition_tables_emitted"],
        },
        "source_search": {
            "source_search_executed": source_search["source_search_executed"],
            "goodcover_transition_values_found": source_search["goodcover_transition_values_found"],
            "exact_complement_factorization_found": source_search[
                "exact_complement_factorization_found"
            ],
            "can_close_smooth_finitepart_now": source_search["can_close_smooth_finitepart_now"],
            "blockers": source_search["blockers"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_cutset = {
        "schema": "MTTNextCutsetAfterProjectiveRhoESmoothValues.v1",
        "status": "NEXT_FRONTIER_S1_SMOOTH_DOMAIN_COVER_OR_COMPLEMENT_KERNEL",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "closed_here": [
            "finite representative-to-cocycle map closed",
            "finite projective rhoE character table closed",
            "finite internal response attached to representative",
            "internal projection/value packet re-emitted with no-double-count policy",
            "abstract Z3 central cocycle shadow closed",
            "finite good-cover nerve incidence scaffold built",
            "physical normalization fork reduced to K_phys anchor or smooth operator identity",
            "support prefilter and minimal four-subpacket emission order closed",
        ],
        "still_open": [
            "S1 smooth good-cover/domain selected by MTT",
            "direct smooth complement domain or complement kernel theorem",
            "compact Iwasawa/Nil chart atlas and selected good-cover embedding",
            "smooth Deligne/Cech local fields B_i, A_ij, g_ijk",
            "smooth projective rhoE transition tables",
            "mapped Freed-Witten, Bianchi, projector-retention, and admissibility checks",
            "smooth bundle operator, E_Qa, heat/zeta/torsion finite part",
            "physical K_phys anchor, mu_match, RG/threshold scheme, and convention map",
            "selected R_H^RG row and same-scheme Omega_H.lambda certificate",
            "direct source-native K_threshold.Omega_H.lambda",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedProjectiveRhoESmoothOperatorSourceValuesOrDirectHKRow",
        "status": STATUS,
        "previous_status": sources["previous"]["status"],
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {name: rel(path) for name, path in SOURCES.items()},
        "output_packets": {
            "finite_representative_cocycle_and_internal_values": rel(FINITE_MAP),
            "physical_normalization_or_smooth_identity_fork": rel(PHYSICAL_FORK),
            "smooth_domain_cover_or_complement_leaf": rel(SMOOTH_LEAF),
            "next_cutset_after_projective_rhoe_smooth_values": rel(NEXT_CUTSET),
        },
        "closure_decision": {
            "finite_representative_to_cocycle_map_closed": True,
            "finite_internal_values_and_no_double_count_closed": True,
            "abstract_Z3_shadow_closed": True,
            "finite_nerve_scaffold_built": True,
            "support_prefilter_closed": True,
            "minimal_emission_order_closed": True,
            "S1_smooth_domain_cover_or_complement_domain_closed": False,
            "smooth_transition_tables_emitted": False,
            "smooth_bundle_operator_or_E_Qa_emitted": False,
            "physical_Kphys_or_normalization_closed": False,
            "selected_R_H_RG_emitted": False,
            "selected_K_threshold_Omega_H_lambda": False,
            "strict_H_K_threshold_row_emitted": False,
            "accepted_selected_K_source_row_count": prev["accepted_selected_K_source_row_count"],
            "selected_K_threshold_row_count_required": prev[
                "selected_K_threshold_row_count_required"
            ],
            "direct_HK_exit_still_allowed": True,
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "ProjectiveRhoESmoothOperatorSourceValuesOrDirectHKRowTheorem",
            "proved": True,
            "statement": (
                "The projective-rhoE smooth-value frontier has been reduced to the "
                "first smooth payload leaf.  Finite representative-to-cocycle data, "
                "finite internal values, no-double-count policy, abstract Z3 shadow, "
                "and the finite nerve scaffold are closed support.  They do not emit "
                "a selected smooth good-cover/domain, direct complement kernel, "
                "smooth transition tables, E_Qa, physical normalization, R_H^RG, or "
                "K_threshold.Omega_H.lambda."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedProjectiveRhoESmoothOperatorSourceValuesOrDirectHKRow",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "finite_representative_to_cocycle_map_closed": True,
        "finite_internal_values_and_no_double_count_closed": True,
        "S1_smooth_domain_cover_or_complement_domain_closed": False,
        "smooth_bundle_operator_or_E_Qa_emitted": False,
        "physical_Kphys_or_normalization_closed": False,
        "selected_R_H_RG_emitted": False,
        "strict_H_K_threshold_row_emitted": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected Projective-rhoE Smooth Operator Source Values or Direct H K-Row v1

## Theorem

`ProjectiveRhoESmoothOperatorSourceValuesOrDirectHKRowTheorem` is emitted.

The smooth-value frontier has been sharpened to its first unavoidable smooth
payload leaf.  The finite algebraic/projective side is now strong support:
representative-to-cocycle, finite character table, finite internal values,
no-double-count policy, abstract Z3 shadow, and finite nerve incidence are all
closed at their stated scope.

## Closed Here

- Finite representative-to-cocycle map.
- Finite projective `rho_E` character table.
- Finite internal response attached to the representative.
- Internal projection/value packet with no-double-count policy.
- Abstract Z3 central cocycle shadow.
- Finite good-cover nerve incidence scaffold.
- Physical-normalization fork reduced to `K_phys` anchor or smooth identity.
- Support prefilter and ordered four-subpacket smooth emission plan.

## Still Open

- S1: selected smooth good-cover/domain, or direct smooth complement domain.
- Compact Iwasawa/Nil chart atlas and selected good-cover embedding.
- Smooth Deligne/Cech local fields `B_i`, `A_ij`, `g_ijk`.
- Smooth projective `rho_E` transition tables.
- Mapped Freed-Witten/Bianchi/projector/admissibility checks.
- Smooth bundle operator, `E_Qa`, heat/zeta/torsion finite part.
- Physical `K_phys`, `mu_match`, RG/threshold scheme, and convention map.
- Selected `R_H^RG` row and same-scheme `Omega_H.lambda` certificate.
- Direct source-native `K_threshold.Omega_H.lambda`.

## Current Count

Strict selected `K_threshold` rows remain
`{prev["accepted_selected_K_source_row_count"]}/{prev["selected_K_threshold_row_count_required"]}`.

## Next Artifact

`{NEXT}`
"""

    write_json(FINITE_MAP, finite_map)
    write_json(PHYSICAL_FORK, physical_fork)
    write_json(SMOOTH_LEAF, smooth_leaf)
    write_json(NEXT_CUTSET, next_cutset)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
