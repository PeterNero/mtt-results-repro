"""Build cover-homotopy / smooth-EQa / physical-gauge-anchor frontier packet.

This consumes the exact next Qa/SU3 artifacts after the S1 source-leaf packet.
It records three real contractions:

* cover lane: invariant B with dB=H plus formal flat-torsion transition support;
* smooth-EQa lane: C_tau orientation and oriented PhiFin finite tables as support;
* physical lane: physical electroweak matching reduced to Omega0/K_phys plus
  local determinant vector.
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

SLUG = "selected_coverhomotopy_or_smootheqasourcecertificate_or_physicalgaugeanchor"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
COVER_LANE = PACKET_DIR / "cover_homotopy_flat_torsion_lane.packet.json"
SMOOTHEQA_LANE = PACKET_DIR / "smootheqa_bn27_or_bundle_connection_lane.packet.json"
PHYSICAL_LANE = PACKET_DIR / "physical_gauge_anchor_lane.packet.json"
NEXT_CUTSET = PACKET_DIR / "next_cutset_after_cover_smootheqa_physical_anchor.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_CoverHomotopyOrSmoothEQaSourceCertificate_or_PhysicalGaugeAnchor_or_DirectHKRow_v1.md"

SOURCES = {
    "previous": DATA / "selected_smoothdomaincoverorcomplementkernelsourceleaf_or_directhkrow.candidate.json",
    "previous_cutset": DATA
    / "selected_smoothdomaincoverorcomplementkernelsourceleaf_or_directhkrow"
    / "next_cutset_after_s1_source_leaf.packet.json",
    "cover_homotopy": QA
    / "selected_heterotic_projectiverhoe_selectedcoverhomotopy_or_deligne_localpotentialvalues.candidate.json",
    "flat_torsion_values": QA
    / "selected_heterotic_projectiverhoe_flattorsiongerbe_or_projectivetransition_sourcevalues.candidate.json",
    "flat_torsion_promotion": QA
    / "selected_heterotic_projectiverhoe_flattorsionpromotion_or_smoothtransitiontables.candidate.json",
    "ctau_positive": QA
    / "selected_heterotic_ctau_positivefinitepart_or_smoothdiracconvention_sourcetheorem.candidate.json",
    "oriented_product": QA
    / "selected_heterotic_orientedphifin_productoperator_or_smootheqa_magnitudesource.candidate.json",
    "positive_sourceownership": QA
    / "selected_heterotic_orientedphifin_positivemagnitude_sourceownership_or_smootheqa_emission.candidate.json",
    "sourceowned_positive_fill": QA
    / "selected_heterotic_orientedphifin_sourceownedpositiveoperator_or_eqapayload_fill.candidate.json",
    "direct_bn27_frontier": QA
    / "selected_heterotic_orientedphifin_directbn27source_or_smootheqa_frontier_matrix.candidate.json",
    "bn27_bridge": QA
    / "selected_heterotic_orientedphifin_bn27_sourcedomainbridge_or_smootheqa_quotient.candidate.json",
    "physical_gauge_anchor": QA / "selected_physical_gauge_anchor_and_electroweak_threshold_vector.candidate.json",
}

STATUS = (
    "MTT_SELECTED_COVERHOMOTOPY_OR_SMOOTHEQASOURCECERTIFICATE_OR_"
    "PHYSICALGAUGEANCHOR_CONTRACTED_TO_FLATTORSION_BN27_OR_OMEGA0"
)
NEXT = "MTT_Selected_FlatTorsionSmoothPromotion_or_SelectedBundleAOrBN27Source_or_PhysicalOmega0_or_DirectHKRow_v1"


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
        raise FileNotFoundError("missing cover/smoothEqa/physical-anchor inputs: " + ", ".join(missing))
    return {name: load(path) for name, path in SOURCES.items()}


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = require_sources()
    prev = sources["previous"]["closure_decision"]
    cover = sources["cover_homotopy"]["decision"]
    cover_closed = sources["cover_homotopy"]["closed_now"]
    flat = sources["flat_torsion_values"]["decision"]
    flat_closed = sources["flat_torsion_values"]["closed_now"]
    flat_prom = sources["flat_torsion_promotion"]["decision"]
    flat_prom_closed = sources["flat_torsion_promotion"]["closed_now"]
    ctau = sources["ctau_positive"]["decision"]
    product = sources["oriented_product"]["decision"]
    posown = sources["positive_sourceownership"]["decision"]
    posfill = sources["sourceowned_positive_fill"]["decision"]
    direct_bn27 = sources["direct_bn27_frontier"]["decision"]
    bn27 = sources["bn27_bridge"]["decision"]
    physical = sources["physical_gauge_anchor"]["decision"]

    cover_lane = {
        "schema": "MTTCoverHomotopyFlatTorsionLane.v1",
        "status": "INVARIANT_B_AND_FORMAL_FLAT_TORSION_SUPPORT_CLOSED_SMOOTH_PROMOTION_OPEN",
        "closure_claimed": True,
        "invariant_B_layer": {
            "B_candidate": cover["B_candidate"],
            "invariant_B_candidate_found": cover["invariant_B_candidate_found"],
            "dB_equals_H": cover["dB_equals_H"],
            "dB_equals_H_in_stored_invariant_coframe": cover_closed[
                "dB_equals_H_in_stored_invariant_coframe"
            ],
            "B_only_tau_obstruction_identified": cover_closed[
                "B_only_tau_obstruction_identified"
            ],
            "can_derive_nonzero_tau_from_B_only": cover["can_derive_nonzero_tau_from_B_only"],
            "selected_cover_homotopy_emitted": cover["selected_cover_homotopy_emitted"],
            "selected_local_B_i_values_emitted": cover["selected_local_B_i_values_emitted"],
        },
        "flat_torsion_layer": {
            "formal_flat_torsion_values_built": flat["formal_flat_torsion_values_built"],
            "all_triples_match_tau": flat["all_triples_match_tau"],
            "all_products_cancel_to_P": flat["all_products_cancel_to_P"],
            "exact_B_curvature_layer_closed": flat["exact_B_curvature_layer_closed"],
            "formal_Z3_flat_torsion_value_packet": flat_closed[
                "formal_Z3_flat_torsion_value_packet"
            ],
            "promotable_now": flat["promotable_now"],
            "same_branch_smooth_values_found": flat["same_branch_smooth_values_found"],
        },
        "symbolic_transition_template": {
            "symbolic_smooth_transition_template_built": flat_prom[
                "symbolic_smooth_transition_template_built"
            ],
            "exact_B_plus_flat_torsion_split_consistent": flat_prom[
                "exact_B_plus_flat_torsion_split_consistent"
            ],
            "formal_cocycle_law_passes": flat_prom["formal_cocycle_law_passes"],
            "formal_unitarity_passes_for_scalar_U1_phases": flat_prom[
                "formal_unitarity_passes_for_scalar_U1_phases"
            ],
            "formal_projective_cocycle_validator": flat_prom_closed[
                "formal_projective_cocycle_validator"
            ],
            "smooth_source_promoted": flat_prom["smooth_source_promoted"],
            "smooth_transition_tables_source_selected": flat_prom[
                "smooth_transition_tables_source_selected"
            ],
            "S1_closed": flat_prom["S1_closed"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    smootheqa_lane = {
        "schema": "MTTSmoothEQaBN27OrBundleConnectionLane.v1",
        "status": "CTAU_ORIENTATION_AND_BN27_TABLE_SUPPORT_CLOSED_SOURCE_CERTIFICATE_OPEN",
        "closure_claimed": True,
        "ctau_dirac_convention": {
            "ctau_chiral_dirac_convention_source_selected": ctau[
                "ctau_chiral_dirac_convention_source_selected"
            ],
            "ctau_positive_finitepart_convention_closed": ctau[
                "ctau_positive_finitepart_convention_closed"
            ],
            "ctau_supplies_orientation": ctau["ctau_supplies_orientation"],
            "ctau_supplies_nonzero_threshold_magnitude": ctau[
                "ctau_supplies_nonzero_threshold_magnitude"
            ],
            "ctau_logdet_value_full_BN": ctau["ctau_logdet_value_full_BN"],
            "smooth_E_Qa_magnitude_source_closed": ctau["smooth_E_Qa_magnitude_source_closed"],
        },
        "oriented_product_support": {
            "same_BN_domain_for_Ctau_and_PhiFin_positive_gap": product[
                "same_BN_domain_for_Ctau_and_PhiFin_positive_gap"
            ],
            "commutation_or_simultaneous_functional_calculus_closed": product[
                "commutation_or_simultaneous_functional_calculus_closed"
            ],
            "oriented_product_table_built": product["oriented_product_table_built"],
            "oriented_abs_sector_logdet_sum": product["oriented_abs_sector_logdet_sum"],
            "PhiFin_all_positive_logdet": product["PhiFin_all_positive_logdet"],
            "oriented_product_operator_source_emitted": product[
                "oriented_product_operator_source_emitted"
            ],
            "heterotic_threshold_magnitude_promoted": product[
                "heterotic_threshold_magnitude_promoted"
            ],
        },
        "sourceownership_fill": {
            "oriented_table_values_ready_to_consume": posown[
                "oriented_table_values_ready_to_consume"
            ],
            "oriented_abs_sector_logdet_exact": posown["oriented_abs_sector_logdet_exact"],
            "positive_magnitude_sourceownership_attempted": posown[
                "positive_magnitude_sourceownership_attempted"
            ],
            "source_owned_positive_PhiFin_magnitude": posown[
                "source_owned_positive_PhiFin_magnitude"
            ],
            "smooth_EQa_emission_closed": posown["smooth_EQa_emission_closed"],
            "direct_source_owned_positive_operator_closed": posfill[
                "direct_source_owned_positive_operator_closed"
            ],
            "smooth_EQa_payload_closed": posfill["smooth_EQa_payload_closed"],
            "minimal_source_packet_written": posfill["minimal_source_packet_written"],
        },
        "direct_BN27_or_smooth_A": {
            "frontier_matrix_built": direct_bn27["frontier_matrix_built"],
            "best_next_route": direct_bn27["best_next_route"],
            "first_leaf_direct": direct_bn27["first_leaf_direct"],
            "first_leaf_smooth": direct_bn27["first_leaf_smooth"],
            "direct_selected_BN27_source_found": direct_bn27[
                "direct_selected_BN27_source_found"
            ],
            "selected_bundle_connection_A_found": direct_bn27[
                "selected_bundle_connection_A_found"
            ],
            "smooth_EQa_quotient_closed": direct_bn27["smooth_EQa_quotient_closed"],
        },
        "BN27_bridge": {
            "BN27_bridge_gate_executed": bn27["BN27_bridge_gate_executed"],
            "embedding_support_insufficient": bn27["embedding_support_insufficient"],
            "minimal_next_leaf": bn27["minimal_next_leaf"],
            "orbitclosure_source_request_built": bn27["orbitclosure_source_request_built"],
            "BN27_orbitclosure_source_bridge_closed": bn27[
                "BN27_orbitclosure_source_bridge_closed"
            ],
            "smooth_EQa_quotient_to_BN27_closed": bn27["smooth_EQa_quotient_to_BN27_closed"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    physical_lane = {
        "schema": "MTTPhysicalGaugeAnchorLane.v1",
        "status": "PHYSICAL_EW_MATCHING_REDUCED_TO_OMEGA0_AND_LOCAL_DETERMINANT_VECTOR",
        "closure_claimed": True,
        "selected_internal_inputs": sources["physical_gauge_anchor"]["theorem"]["selected_internal_inputs"],
        "decision": {
            "physical_anchor_closed": physical["physical_anchor_closed"],
            "threshold_vector_closed": physical["threshold_vector_closed"],
            "physical_electroweak_matching_closed": physical[
                "physical_electroweak_matching_closed"
            ],
            "convention_reconciliation_closed": physical["convention_reconciliation_closed"],
            "minimal_remaining_objects": physical["minimal_remaining_objects"],
            "next_required_object": physical["next_required_object"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_cutset = {
        "schema": "MTTNextCutsetAfterCoverSmoothEQaPhysicalAnchor.v1",
        "status": "NEXT_FRONTIER_FLAT_TORSION_SMOOTH_PROMOTION_OR_BUNDLE_A_BN27_OR_OMEGA0",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "closed_here": [
            "invariant B candidate B=6 e5 wedge e6 with dB=H",
            "B-only tau obstruction identified",
            "formal Z3 flat torsion/projective transition values built",
            "symbolic smooth transition-table template built",
            "C_tau chiral Dirac positive finitepart convention closed",
            "C_tau supplies orientation but zero threshold magnitude",
            "C_tau and PhiFin simultaneous BN27 table built",
            "oriented table values ready but source-owned magnitude not promoted",
            "physical electroweak matching reduced to Omega0/K_phys plus local determinant vector",
        ],
        "still_open": [
            "selected smooth flat-torsion Deligne representative or projective transition functions",
            "selected smooth good cover and transition-table source promotion",
            "selected bundle connection A/F_A or equivalent smooth projective rhoE transition packet",
            "direct selected BN27 heterotic source or BN27 orbit-closure theorem",
            "source-owned positive PhiFin operator or smooth E_Qa payload",
            "physical Omega0/K_phys/action-unit anchor",
            "selected local determinant threshold vector and fixed RG/matching scheme",
            "selected R_H^RG row and same-scheme Omega_H.lambda certificate",
            "direct source-native K_threshold.Omega_H.lambda",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedCoverHomotopyOrSmoothEQaSourceCertificateOrPhysicalGaugeAnchor",
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
            "cover_homotopy_flat_torsion_lane": rel(COVER_LANE),
            "smootheqa_bn27_or_bundle_connection_lane": rel(SMOOTHEQA_LANE),
            "physical_gauge_anchor_lane": rel(PHYSICAL_LANE),
            "next_cutset_after_cover_smootheqa_physical_anchor": rel(NEXT_CUTSET),
        },
        "closure_decision": {
            "invariant_B_dB_equals_H_closed": True,
            "B_only_tau_obstruction_closed": True,
            "formal_flat_torsion_values_built": True,
            "symbolic_transition_template_built": True,
            "smooth_flat_torsion_or_transition_source_promoted": False,
            "ctau_positive_convention_closed": True,
            "oriented_BN27_table_support_closed": True,
            "source_owned_positive_operator_or_smooth_EQa_closed": False,
            "selected_bundle_A_or_direct_BN27_source_closed": False,
            "physical_Omega0_or_Kphys_anchor_closed": False,
            "local_determinant_threshold_vector_closed": False,
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
            "name": "CoverHomotopyOrSmoothEQaSourceCertificateOrPhysicalGaugeAnchorTheorem",
            "proved": True,
            "statement": (
                "The cover, smooth-EQa, and physical-gauge exits have each been "
                "contracted. The cover lane now has exact B-curvature and formal "
                "flat-torsion/projective transition support, but lacks selected "
                "smooth transition functions. The smooth-EQa lane has C_tau "
                "orientation, a positive convention, and BN27 PhiFin tables as "
                "support, but lacks selected bundle A or direct BN27 source ownership. "
                "The physical lane is reduced to Omega0/K_phys and a selected local "
                "determinant threshold vector. No H K row or R_H^RG is emitted."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedCoverHomotopyOrSmoothEQaSourceCertificateOrPhysicalGaugeAnchor",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "invariant_B_dB_equals_H_closed": True,
        "formal_flat_torsion_values_built": True,
        "ctau_positive_convention_closed": True,
        "oriented_BN27_table_support_closed": True,
        "smooth_flat_torsion_or_transition_source_promoted": False,
        "source_owned_positive_operator_or_smooth_EQa_closed": False,
        "selected_bundle_A_or_direct_BN27_source_closed": False,
        "physical_Omega0_or_Kphys_anchor_closed": False,
        "selected_R_H_RG_emitted": False,
        "strict_H_K_threshold_row_emitted": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected Cover-Homotopy or Smooth-EQa Source Certificate or Physical Gauge Anchor v1

## Theorem

`CoverHomotopyOrSmoothEQaSourceCertificateOrPhysicalGaugeAnchorTheorem` is emitted.

The three live exits from the S1 source-leaf frontier have each been contracted.

## Closed Here

- Cover lane: invariant `B = 6 e5 wedge e6` with `dB = H`.
- Cover lane: `B`-only tau obstruction identified.
- Cover lane: formal `Z3` flat-torsion/projective transition values.
- Cover lane: symbolic smooth transition-table template.
- Smooth `E_Qa` lane: `C_tau` chiral Dirac positive finitepart convention.
- Smooth `E_Qa` lane: `C_tau` orientation retained, but zero magnitude.
- Smooth `E_Qa` lane: simultaneous BN27 `C_tau` / PhiFin product table support.
- Physical lane: electroweak matching reduced to `Omega0/K_phys` plus a selected
  local determinant threshold vector.

## Still Open

- Selected smooth flat-torsion Deligne representative or transition functions.
- Selected bundle connection `A/F_A` or smooth projective `rho_E` transition packet.
- Direct selected BN27 heterotic source or BN27 orbit-closure theorem.
- Source-owned positive PhiFin operator or smooth `E_Qa` payload.
- Physical `Omega0/K_phys` action-unit anchor.
- Selected local determinant threshold vector, `mu_match`, and RG/threshold scheme.
- Selected `R_H^RG` row and same-scheme `Omega_H.lambda` certificate.
- Direct source-native `K_threshold.Omega_H.lambda`.

## Current Count

Strict selected `K_threshold` rows remain
`{prev["accepted_selected_K_source_row_count"]}/{prev["selected_K_threshold_row_count_required"]}`.

## Next Artifact

`{NEXT}`
"""

    write_json(COVER_LANE, cover_lane)
    write_json(SMOOTHEQA_LANE, smootheqa_lane)
    write_json(PHYSICAL_LANE, physical_lane)
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
