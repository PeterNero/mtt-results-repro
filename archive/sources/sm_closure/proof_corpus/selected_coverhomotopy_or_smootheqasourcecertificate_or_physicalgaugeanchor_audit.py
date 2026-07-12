"""Audit cover-homotopy / smooth-EQa / physical-gauge-anchor frontier packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_coverhomotopy_or_smootheqasourcecertificate_or_physicalgaugeanchor"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
COVER_LANE = PACKET_DIR / "cover_homotopy_flat_torsion_lane.packet.json"
SMOOTHEQA_LANE = PACKET_DIR / "smootheqa_bn27_or_bundle_connection_lane.packet.json"
PHYSICAL_LANE = PACKET_DIR / "physical_gauge_anchor_lane.packet.json"
NEXT_CUTSET = PACKET_DIR / "next_cutset_after_cover_smootheqa_physical_anchor.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_CoverHomotopyOrSmoothEQaSourceCertificate_or_PhysicalGaugeAnchor_or_DirectHKRow_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_COVERHOMOTOPY_OR_SMOOTHEQASOURCECERTIFICATE_OR_"
    "PHYSICALGAUGEANCHOR_CONTRACTED_TO_FLATTORSION_BN27_OR_OMEGA0"
)
NEXT = "MTT_Selected_FlatTorsionSmoothPromotion_or_SelectedBundleAOrBN27Source_or_PhysicalOmega0_or_DirectHKRow_v1"


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
    cover = load(COVER_LANE)
    smootheqa = load(SMOOTHEQA_LANE)
    physical = load(PHYSICAL_LANE)
    cutset = load(NEXT_CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("cover lane", cover),
        ("smooth E_Qa lane", smootheqa),
        ("physical lane", physical),
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
        "invariant_B_dB_equals_H_closed",
        "B_only_tau_obstruction_closed",
        "formal_flat_torsion_values_built",
        "symbolic_transition_template_built",
        "ctau_positive_convention_closed",
        "oriented_BN27_table_support_closed",
        "direct_HK_exit_still_allowed",
    ]:
        require(decision[key] is True, f"decision support missing {key}")
    for key in [
        "smooth_flat_torsion_or_transition_source_promoted",
        "source_owned_positive_operator_or_smooth_EQa_closed",
        "selected_bundle_A_or_direct_BN27_source_closed",
        "physical_Omega0_or_Kphys_anchor_closed",
        "local_determinant_threshold_vector_closed",
        "selected_R_H_RG_emitted",
        "selected_K_threshold_Omega_H_lambda",
        "strict_H_K_threshold_row_emitted",
        "full_no_knob_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"decision overclosed {key}")
    require(decision["accepted_selected_K_source_row_count"] == 9, "K row count")
    require(decision["selected_K_threshold_row_count_required"] == 10, "required K rows")

    b = cover["invariant_B_layer"]
    require(b["B_candidate"] == "6 e5 wedge e6", "B candidate")
    require(b["invariant_B_candidate_found"] is True, "B found")
    require(b["dB_equals_H"] is True, "dB=H")
    require(b["dB_equals_H_in_stored_invariant_coframe"] is True, "coframe dB=H")
    require(b["B_only_tau_obstruction_identified"] is True, "tau obstruction")
    require(b["can_derive_nonzero_tau_from_B_only"] is False, "tau overderived")
    require(b["selected_cover_homotopy_emitted"] is False, "cover overemitted")
    require(b["selected_local_B_i_values_emitted"] is False, "local B overemitted")
    flat = cover["flat_torsion_layer"]
    for key in [
        "formal_flat_torsion_values_built",
        "all_triples_match_tau",
        "all_products_cancel_to_P",
        "exact_B_curvature_layer_closed",
        "formal_Z3_flat_torsion_value_packet",
    ]:
        require(flat[key] is True, f"flat support missing {key}")
    require(flat["promotable_now"] is False, "flat promotable")
    require(flat["same_branch_smooth_values_found"] is False, "smooth values found")
    template = cover["symbolic_transition_template"]
    for key in [
        "symbolic_smooth_transition_template_built",
        "exact_B_plus_flat_torsion_split_consistent",
        "formal_cocycle_law_passes",
        "formal_unitarity_passes_for_scalar_U1_phases",
        "formal_projective_cocycle_validator",
    ]:
        require(template[key] is True, f"template support missing {key}")
    for key in ["smooth_source_promoted", "smooth_transition_tables_source_selected", "S1_closed"]:
        require(template[key] is False, f"template overclosed {key}")

    ctau = smootheqa["ctau_dirac_convention"]
    require(ctau["ctau_chiral_dirac_convention_source_selected"] is True, "ctau convention")
    require(ctau["ctau_positive_finitepart_convention_closed"] is True, "ctau positive")
    require(ctau["ctau_supplies_orientation"] is True, "ctau orientation")
    require(ctau["ctau_supplies_nonzero_threshold_magnitude"] is False, "ctau magnitude")
    require(ctau["ctau_logdet_value_full_BN"] == 0.0, "ctau logdet")
    require(ctau["smooth_E_Qa_magnitude_source_closed"] is False, "ctau E_Qa overclosed")
    product = smootheqa["oriented_product_support"]
    for key in [
        "same_BN_domain_for_Ctau_and_PhiFin_positive_gap",
        "commutation_or_simultaneous_functional_calculus_closed",
        "oriented_product_table_built",
    ]:
        require(product[key] is True, f"product support missing {key}")
    require(product["oriented_abs_sector_logdet_sum"] == 18.339036754911856, "oriented abs")
    require(product["PhiFin_all_positive_logdet"] == 27.508555132367775, "all positive")
    require(product["oriented_product_operator_source_emitted"] is False, "product source")
    require(product["heterotic_threshold_magnitude_promoted"] is False, "threshold promoted")
    source = smootheqa["sourceownership_fill"]
    require(source["oriented_table_values_ready_to_consume"] is True, "table ready")
    require(source["oriented_abs_sector_logdet_exact"] == "log(92160000)", "exact abs")
    require(source["positive_magnitude_sourceownership_attempted"] is True, "ownership attempted")
    require(source["minimal_source_packet_written"] is True, "minimal packet")
    for key in [
        "source_owned_positive_PhiFin_magnitude",
        "smooth_EQa_emission_closed",
        "direct_source_owned_positive_operator_closed",
        "smooth_EQa_payload_closed",
    ]:
        require(source[key] is False, f"sourceownership overclosed {key}")
    direct = smootheqa["direct_BN27_or_smooth_A"]
    require(direct["frontier_matrix_built"] is True, "frontier matrix")
    require("selected_bundle connection A".replace(" ", "_") not in direct, "sanity")
    require(direct["direct_selected_BN27_source_found"] is False, "direct BN27 found")
    require(direct["selected_bundle_connection_A_found"] is False, "bundle A found")
    require(direct["smooth_EQa_quotient_closed"] is False, "smooth quotient")
    bridge = smootheqa["BN27_bridge"]
    require(bridge["BN27_bridge_gate_executed"] is True, "BN27 gate")
    require(bridge["embedding_support_insufficient"] is True, "embedding insufficient")
    require(bridge["orbitclosure_source_request_built"] is True, "orbit request")
    require(bridge["BN27_orbitclosure_source_bridge_closed"] is False, "orbit bridge")
    require(bridge["smooth_EQa_quotient_to_BN27_closed"] is False, "E_Qa BN27")

    pdec = physical["decision"]
    require(pdec["physical_anchor_closed"] is False, "physical anchor")
    require(pdec["threshold_vector_closed"] is False, "threshold vector")
    require(pdec["physical_electroweak_matching_closed"] is False, "EW matching")
    require(pdec["convention_reconciliation_closed"] is False, "convention")
    require("K_phys or Omega_0/ell_p/kappa_11/alpha_prime physical anchor" in pdec["minimal_remaining_objects"], "Omega0 missing")
    require("lambda_12 or full Delta_a^sel selected local determinant vector" in pdec["minimal_remaining_objects"], "det vector missing")

    require(
        cutset["status"] == "NEXT_FRONTIER_FLAT_TORSION_SMOOTH_PROMOTION_OR_BUNDLE_A_BN27_OR_OMEGA0",
        "cutset status",
    )
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    for phrase in [
        "invariant B candidate B=6 e5 wedge e6 with dB=H",
        "formal Z3 flat torsion/projective transition values built",
        "C_tau chiral Dirac positive finitepart convention closed",
        "physical electroweak matching reduced to Omega0/K_phys plus local determinant vector",
    ]:
        require(phrase in cutset["closed_here"], f"closed phrase missing {phrase}")
    for phrase in [
        "selected smooth flat-torsion Deligne representative or projective transition functions",
        "selected bundle connection A/F_A or equivalent smooth projective rhoE transition packet",
        "direct selected BN27 heterotic source or BN27 orbit-closure theorem",
        "physical Omega0/K_phys/action-unit anchor",
        "direct source-native K_threshold.Omega_H.lambda",
    ]:
        require(phrase in cutset["still_open"], f"open phrase missing {phrase}")

    for phrase in [
        "CoverHomotopyOrSmoothEQaSourceCertificateOrPhysicalGaugeAnchorTheorem",
        "Cover lane: invariant `B = 6 e5 wedge e6`",
        "Smooth `E_Qa` lane: `C_tau`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: cover/smooth-EQa/physical-anchor exits contracted to flat torsion, BN27/bundle-A, or Omega0; H row open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
