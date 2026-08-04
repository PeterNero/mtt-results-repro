"""Audit projective-rhoE smooth operator source values or direct H K-row packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_projectiverhoesmoothoperatorsourcevalues_or_directhkrow"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
FINITE_MAP = PACKET_DIR / "finite_representative_cocycle_and_internal_values.packet.json"
PHYSICAL_FORK = PACKET_DIR / "physical_normalization_or_smooth_identity_fork.packet.json"
SMOOTH_LEAF = PACKET_DIR / "smooth_domain_cover_or_complement_leaf.packet.json"
NEXT_CUTSET = PACKET_DIR / "next_cutset_after_projective_rhoe_smooth_values.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_ProjectiveRhoESmoothOperatorSourceValues_or_DirectHKRow_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_PROJECTIVERHOESMOOTHOPERATORSOURCEVALUES_OR_DIRECTHKROW_"
    "FINITE_COCYCLE_AND_NODOUBLECOUNT_CLOSED_S1_SMOOTH_LEAF_OPEN"
)
NEXT = "MTT_Selected_SmoothDomainCoverOrComplementKernelSourceLeaf_or_DirectHKRow_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("closure_claimed") is True, f"{label} closure flag")
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    finite = load(FINITE_MAP)
    fork = load(PHYSICAL_FORK)
    leaf = load(SMOOTH_LEAF)
    cutset = load(NEXT_CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("finite map", finite),
        ("physical fork", fork),
        ("smooth leaf", leaf),
        ("next cutset", cutset),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "certificate status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(cert["next_required_artifact"] == NEXT, "certificate next")
    require(data["theorem"]["proved"] is True, "candidate theorem")
    require(cert["theorem_proved"] is True, "certificate theorem")
    require(data["full_no_knob_closure_claimed"] is False, "candidate no-knob")
    require(data["true_SM_equivalence_claimed"] is False, "candidate true SM")

    decision = data["closure_decision"]
    for key in [
        "finite_representative_to_cocycle_map_closed",
        "finite_internal_values_and_no_double_count_closed",
        "abstract_Z3_shadow_closed",
        "finite_nerve_scaffold_built",
        "support_prefilter_closed",
        "minimal_emission_order_closed",
        "direct_HK_exit_still_allowed",
    ]:
        require(decision[key] is True, f"decision missing closure/support {key}")
    for key in [
        "S1_smooth_domain_cover_or_complement_domain_closed",
        "smooth_transition_tables_emitted",
        "smooth_bundle_operator_or_E_Qa_emitted",
        "physical_Kphys_or_normalization_closed",
        "selected_R_H_RG_emitted",
        "selected_K_threshold_Omega_H_lambda",
        "strict_H_K_threshold_row_emitted",
        "full_no_knob_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"decision overclosed {key}")
    require(decision["accepted_selected_K_source_row_count"] == 9, "K row count")
    require(decision["selected_K_threshold_row_count_required"] == 10, "required K rows")

    rep = finite["finite_representative_to_cocycle"]
    for key in [
        "finite_representative_to_cocycle_map_closed",
        "finite_projective_rhoE_character_table_closed",
        "finite_internal_response_attached",
    ]:
        require(rep[key] is True, f"finite map not closed {key}")
    values = finite["internal_values"]
    for key in [
        "finite_internal_values_reemitted",
        "internal_projection_family_closed",
        "no_double_count_policy_imported",
        "abstract_Z3_shadow_closed",
        "finite_nerve_candidate_built",
        "incidence_fields_closed_at_formal_nerve_level",
    ]:
        require(values[key] is True, f"internal value support missing {key}")
    not_physical = finite["not_promoted_to_smooth_physical_value"]
    require(all(value is False for value in not_physical.values()), "finite support overpromoted")

    internal = fork["internal_interface"]
    require(internal["internal_interface_closed"] is True, "internal interface")
    require(internal["closed_internal_formula"] == "Delta_rhoE_internal = log(2008), K_gauge,int=1", "formula")
    anchor = fork["physical_anchor_lane"]
    require(anchor["physical_lane_has_anchor_slot_but_no_value"] is True, "anchor slot")
    require(anchor["physical_threshold_normalization_closed"] is False, "physical norm")
    require(anchor["physical_anchor_bridge_closed"] is False, "physical anchor")
    require(anchor["measured_coupling_match_claimed"] is False, "measured match")
    smooth = fork["smooth_identity_lane"]
    require(smooth["best_next_lane"] == "smooth_operator_identity_bridge", "best lane")
    require(smooth["smooth_lane_has_geometry_but_no_bundle_operator"] is True, "smooth geometry")
    require(smooth["smooth_operator_identity_proved"] is False, "smooth identity proved")
    require(smooth["smooth_operator_identity_closed"] is False, "smooth identity closed")

    prefilter = leaf["support_prefilter"]
    require(prefilter["support_prefilter_closed"] is True, "prefilter")
    require(prefilter["retired_blockers_count"] == 8, "retired blockers")
    require(prefilter["operator_payload_contract_built"] is True, "payload contract")
    emission = leaf["minimal_emission_order"]
    require(emission["minimal_emission_subpacket_built"] is True, "minimal emission")
    require(emission["subpacket_count"] == 4, "subpacket count")
    require(
        emission["first_leaf_identified"] == "S1_smooth_domain_cover_or_complement_domain",
        "first leaf",
    )
    first = leaf["first_leaf_attempt"]
    require(first["first_leaf_attempted"] is True, "first leaf attempted")
    require(first["current_source_nogo_for_S1"] is True, "S1 no-go")
    require(first["minimal_source_request_built"] is True, "source request")
    require(first["domain_cover_leaf_closed"] is False, "domain cover overclosed")
    require(first["direct_complement_domain_closed"] is False, "complement domain overclosed")

    external = leaf["external_construction_triage"]
    require(external["external_construction_gate_built"] is True, "external gate")
    require(external["candidate_count"] == 4, "candidate count")
    require(external["selected_next_candidate"] == "A_finite_good_cover_nerve", "next candidate")
    require(external["finite_good_cover_nerve_candidate_buildable"] is True, "nerve buildable")
    for key in [
        "any_candidate_closes_S1_now",
        "smooth_domain_or_cover_selected",
        "direct_complement_domain_selected",
    ]:
        require(external[key] is False, f"external overclosed {key}")

    goodcover = leaf["finite_nerve_and_goodcover"]
    require(goodcover["formal_nerve_incidence_available"] is True, "formal nerve")
    require(goodcover["ctwist_deligne_template_available"] is True, "Deligne template")
    for key in [
        "contractible_chart_atlas_emitted",
        "selected_compact_iwasawa_nil_embedding_emitted",
        "local_B_i_A_ij_g_ijk_emitted",
        "tau_shadow_induced_by_smooth_cover",
    ]:
        require(goodcover[key] is False, f"goodcover overclosed {key}")

    nodouble = leaf["no_double_count_and_value_packet"]
    require(nodouble["no_double_count_policy_closed"] is True, "no double count")
    require(nodouble["GR_surface_routing_closed"] is True, "GR routing")
    require(nodouble["finite_internal_quotient_retained"] is True, "finite quotient")
    for key in [
        "exact_complement_quotient_closed",
        "heat_zeta_torsion_factorization_closed",
        "smooth_transition_tables_emitted",
    ]:
        require(nodouble[key] is False, f"value packet overclosed {key}")

    search = leaf["source_search"]
    require(search["source_search_executed"] is True, "source search")
    require(search["goodcover_transition_values_found"] is False, "goodcover values")
    require(search["exact_complement_factorization_found"] is False, "exact complement")
    require(search["can_close_smooth_finitepart_now"] is False, "smooth finitepart")
    require(all(value is False for value in search["blockers"].values()), "source search blockers")

    require(
        cutset["status"] == "NEXT_FRONTIER_S1_SMOOTH_DOMAIN_COVER_OR_COMPLEMENT_KERNEL",
        "cutset status",
    )
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    for phrase in [
        "finite representative-to-cocycle map closed",
        "abstract Z3 central cocycle shadow closed",
        "finite good-cover nerve incidence scaffold built",
        "support prefilter and minimal four-subpacket emission order closed",
    ]:
        require(phrase in cutset["closed_here"], f"closed phrase missing {phrase}")
    for phrase in [
        "S1 smooth good-cover/domain selected by MTT",
        "direct smooth complement domain or complement kernel theorem",
        "smooth bundle operator, E_Qa, heat/zeta/torsion finite part",
        "direct source-native K_threshold.Omega_H.lambda",
    ]:
        require(phrase in cutset["still_open"], f"open phrase missing {phrase}")

    for phrase in [
        "ProjectiveRhoESmoothOperatorSourceValuesOrDirectHKRowTheorem",
        "first unavoidable smooth",
        "Strict selected `K_threshold` rows remain",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: projective-rhoE finite support and no-double-count are closed; S1 smooth leaf remains open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
