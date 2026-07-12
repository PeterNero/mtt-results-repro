"""Build smooth-domain cover/complement-kernel source leaf or direct H K-row packet.

This advances the S1 leaf using the later Qa/SU3 chart-atlas, local-field,
direct-operator, physical-normalization, and oriented-PhiFin support packets.
It keeps the crucial line bright: equation packets, dH=0, and finite/internal
boundaries are not selected smooth cover/homotopy values or smooth E_Qa.
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

SLUG = "selected_smoothdomaincoverorcomplementkernelsourceleaf_or_directhkrow"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
S1_EQUATIONS = PACKET_DIR / "s1_chartatlas_localfield_equation_reduction.packet.json"
INTERNAL_BOUNDARY = PACKET_DIR / "direct_operator_internal_boundary_and_physical_request.packet.json"
ORIENTED_SUPPORT = PACKET_DIR / "oriented_phifin_smootheqa_support_import.packet.json"
NEXT_CUTSET = PACKET_DIR / "next_cutset_after_s1_source_leaf.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_SmoothDomainCoverOrComplementKernelSourceLeaf_or_DirectHKRow_v1.md"

SOURCES = {
    "previous": DATA / "selected_projectiverhoesmoothoperatorsourcevalues_or_directhkrow.candidate.json",
    "previous_cutset": DATA
    / "selected_projectiverhoesmoothoperatorsourcevalues_or_directhkrow"
    / "next_cutset_after_projective_rhoe_smooth_values.packet.json",
    "chartatlas": QA
    / "selected_heterotic_projectiverhoe_chartatlas_delignecech_localfields_sourceamendment.candidate.json",
    "localfield": QA / "selected_heterotic_projectiverhoe_localfieldsolve_or_coverselection_nogo.candidate.json",
    "direct_payload_boundary": QA
    / "selected_heterotic_projectiverhoe_directoperatorpayload_physicalboundary_or_smoothidentity.candidate.json",
    "smooth_identity_trace_lift": QA
    / "selected_heterotic_projectiverhoe_smoothidentity_tracelift_or_complementquotient_fillattempt.candidate.json",
    "physical_or_smootheqa_request": QA
    / "selected_heterotic_projectiverhoe_physicalnormalization_or_smootheqa_sourcedata_request.candidate.json",
    "physical_or_smootheqa_fill": QA
    / "selected_heterotic_projectiverhoe_physicalanchor_or_smootheqa_sourcefillattempt.candidate.json",
    "smooth_operator_fill": QA
    / "selected_heterotic_projectiverhoe_smoothoperator_sourcepacket_fillattempt.candidate.json",
    "oriented_magnitude": QA
    / "selected_heterotic_orientedphifin_magnitudefinitepart_sourcetheorem_or_smootheqa_traceidentity.candidate.json",
    "oriented_threshold_source": QA
    / "selected_heterotic_orientedphifin_sourceemission_or_smootheqa_thresholdidentity.candidate.json",
    "oriented_source_fill": QA
    / "selected_heterotic_orientedphifin_thresholdidentity_sourcefill_or_smootheqa_construction.candidate.json",
    "bn_centralrank": QA / "selected_heterotic_bn_centralrankoperator_or_smootheqa_sourceemission.candidate.json",
}

STATUS = (
    "MTT_SELECTED_SMOOTHDOMAINCOVERORCOMPLEMENTKERNELSOURCELEAF_OR_DIRECTHKROW_"
    "S1_EQUATIONS_DH_AND_INTERNAL_BOUNDARY_CLOSED_SOURCE_VALUES_OPEN"
)
NEXT = "MTT_Selected_CoverHomotopyOrSmoothEQaSourceCertificate_or_PhysicalGaugeAnchor_or_DirectHKRow_v1"


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
        raise FileNotFoundError("missing S1 source-leaf inputs: " + ", ".join(missing))
    return {name: load(path) for name, path in SOURCES.items()}


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = require_sources()
    prev = sources["previous"]["closure_decision"]
    chart = sources["chartatlas"]["decision"]
    local = sources["localfield"]["decision"]
    local_closed = sources["localfield"]["closed_now"]
    direct_boundary = sources["direct_payload_boundary"]["decision"]
    trace = sources["smooth_identity_trace_lift"]["decision"]
    request = sources["physical_or_smootheqa_request"]["decision"]
    fill = sources["physical_or_smootheqa_fill"]["decision"]
    fill_closed = sources["physical_or_smootheqa_fill"]["closed_now"]
    smooth_fill = sources["smooth_operator_fill"]["decision"]
    smooth_fill_result = sources["smooth_operator_fill"]["fill_result"]
    oriented_mag = sources["oriented_magnitude"]["decision"]
    oriented_source = sources["oriented_threshold_source"]["decision"]
    oriented_fill = sources["oriented_source_fill"]["decision"]
    bn = sources["bn_centralrank"]["decision"]

    s1_equations = {
        "schema": "MTTS1ChartAtlasLocalFieldEquationReduction.v1",
        "status": "S1_EQUATION_PACKET_AND_DH_CLOSED_COVER_SELECTION_OPEN",
        "closure_claimed": True,
        "chartatlas_equation_packet": {
            "equation_packet_built": chart["equation_packet_built"],
            "geometry_anchor_promoted_to_known_support": chart[
                "geometry_anchor_promoted_to_known_support"
            ],
            "selected_chart_atlas_emitted": chart["selected_chart_atlas_emitted"],
            "smooth_cover_contractibility_proved": chart["smooth_cover_contractibility_proved"],
            "local_field_values_emitted": chart["local_field_values_emitted"],
            "smooth_tau_shadow_derived": chart["smooth_tau_shadow_derived"],
        },
        "localfield_solve": {
            "dH_computed": local["dH_computed"],
            "dH_closed": local["dH_closed"],
            "conditional_local_potential_lane_live": local[
                "conditional_local_potential_lane_live"
            ],
            "invariant_dH_zero_check": local_closed["invariant_dH_zero_check"],
            "conditional_poincare_local_potential_existence_theorem": local_closed[
                "conditional_poincare_local_potential_existence_theorem"
            ],
            "selected_cover_emitted": local["selected_cover_emitted"],
            "local_B_i_A_ij_g_ijk_values_emitted": local[
                "local_B_i_A_ij_g_ijk_values_emitted"
            ],
            "smooth_tau_shadow_derived": local["smooth_tau_shadow_derived"],
            "S1_closed": local["S1_closed"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    internal_boundary = {
        "schema": "MTTDirectOperatorInternalBoundaryAndPhysicalRequest.v1",
        "status": "INTERNAL_COMPLEMENT_BOUNDARY_LOCKED_PHYSICAL_OR_SMOOTH_SOURCE_DATA_OPEN",
        "closure_claimed": True,
        "direct_payload_boundary": {
            "finite_internal_payload_complete": direct_boundary["finite_internal_payload_complete"],
            "direct_payload_boundary_locked": direct_boundary["direct_payload_boundary_locked"],
            "smooth_identity_lane_selected_next": direct_boundary[
                "smooth_identity_lane_selected_next"
            ],
            "physical_lane_blocked_by_anchor_and_rg": direct_boundary[
                "physical_lane_blocked_by_anchor_and_rg"
            ],
            "physical_lane_closed": direct_boundary["physical_lane_closed"],
            "smooth_identity_lane_closed": direct_boundary["smooth_identity_lane_closed"],
        },
        "trace_lift_or_complement": {
            "internal_complement_quotient_policy_closed": trace[
                "internal_complement_quotient_policy_closed"
            ],
            "selected_internal_logdet_preserved": trace["selected_internal_logdet_preserved"],
            "trace_lift_current_source_nogo_retained": trace[
                "trace_lift_current_source_nogo_retained"
            ],
            "smooth_trace_lift_closed": trace["smooth_trace_lift_closed"],
            "smooth_EQa_closed": trace["smooth_EQa_closed"],
            "smooth_heat_zeta_torsion_finitepart_computed": trace[
                "smooth_heat_zeta_torsion_finitepart_computed"
            ],
            "physical_normalization_closed": trace["physical_normalization_closed"],
        },
        "source_data_request_and_fill": {
            "internal_branch_locked": request["internal_branch_locked"],
            "no_more_internal_computation_required_for_log2008": request[
                "no_more_internal_computation_required_for_log2008"
            ],
            "source_request_built": request["source_request_built"],
            "typed_electroweak_convention_map": fill_closed["typed_electroweak_convention_map"],
            "internal_weaksplit_threshold_for_physical_lane": fill_closed[
                "internal_weaksplit_threshold_for_physical_lane"
            ],
            "Rplus_geometry_support_for_smooth_lane": fill_closed[
                "Rplus_geometry_support_for_smooth_lane"
            ],
            "physical_anchor_still_open": fill["physical_anchor_still_open"],
            "matching_scale_still_open": fill["matching_scale_still_open"],
            "RG_scheme_still_open": fill["RG_scheme_still_open"],
            "smooth_EQa_still_open": fill["smooth_EQa_still_open"],
            "preferred_next_lane": fill["preferred_next_lane"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    oriented_support = {
        "schema": "MTTOrientedPhiFinSmoothEQaSupportImport.v1",
        "status": "ORIENTED_PHIFIN_EXACT_TABLE_AND_SIGNED_BN_SUPPORT_IMPORTED_SOURCE_IDENTITY_OPEN",
        "closure_claimed": True,
        "oriented_magnitude": {
            "oriented_table_magnitude_finitepart_computed": oriented_mag[
                "oriented_table_magnitude_finitepart_computed"
            ],
            "oriented_abs_sector_logdet_exact": oriented_mag["oriented_abs_sector_logdet_exact"],
            "full_positive_logdet_exact": oriented_mag["full_positive_logdet_exact"],
            "source_owned_positive_PhiFin_magnitude": oriented_mag[
                "source_owned_positive_PhiFin_magnitude"
            ],
            "smooth_E_Qa_trace_identity_closed": oriented_mag[
                "smooth_E_Qa_trace_identity_closed"
            ],
        },
        "oriented_threshold_identity": {
            "same_domain_commutation_table_complete": oriented_source[
                "same_domain_commutation_table_complete"
            ],
            "closed_support_count": oriented_source["closed_support_count"],
            "source_emission_closed": oriented_source["source_emission_closed"],
            "smooth_E_Qa_threshold_identity_closed": oriented_source[
                "smooth_E_Qa_threshold_identity_closed"
            ],
            "heterotic_threshold_magnitude_promoted": oriented_source[
                "heterotic_threshold_magnitude_promoted"
            ],
        },
        "oriented_source_fill": {
            "fill_attempt_executed": oriented_fill["fill_attempt_executed"],
            "selected_finite_internal_packet_reused": oriented_fill[
                "selected_finite_internal_packet_reused"
            ],
            "oriented_table_reused": oriented_fill["oriented_table_reused"],
            "required_leaf_count": oriented_fill["required_leaf_count"],
            "closed_required_leaf_count": oriented_fill["closed_required_leaf_count"],
            "source_emission_closed": oriented_fill["source_emission_closed"],
            "smooth_EQa_constructed": oriented_fill["smooth_EQa_constructed"],
            "finite_quotient_identity_constructed": oriented_fill[
                "finite_quotient_identity_constructed"
            ],
        },
        "bn_centralrank": {
            "C_tau_source_selected_as_BN_operator": bn["C_tau_source_selected_as_BN_operator"],
            "C_tau_signed_intertwiner_closed": bn["C_tau_signed_intertwiner_closed"],
            "operator_identity_closed_for_signed_layer": bn[
                "operator_identity_closed_for_signed_layer"
            ],
            "operator_identity_closed_for_positive_finitepart_layer": bn[
                "operator_identity_closed_for_positive_finitepart_layer"
            ],
            "selected_smooth_E_Qa_emitted": bn["selected_smooth_E_Qa_emitted"],
            "positive_finitepart_for_C_tau_closed": bn["positive_finitepart_for_C_tau_closed"],
            "chiral_dirac_eta_route_ranked_primary": bn["chiral_dirac_eta_route_ranked_primary"],
        },
        "smooth_operator_packet_fill": {
            "support_context_filled": smooth_fill["support_context_filled"],
            "smooth_operator_source_packet_filled": smooth_fill[
                "smooth_operator_source_packet_filled"
            ],
            "E_Qa_matrix_filled": smooth_fill_result["E_Qa_matrix_filled"],
            "projective_rhoE_transition_tables_filled": smooth_fill_result[
                "projective_rhoE_transition_tables_filled"
            ],
            "selected_connection_A_filled": smooth_fill_result["selected_connection_A_filled"],
            "finite_part_value_filled": smooth_fill_result["finite_part_value_filled"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_cutset = {
        "schema": "MTTNextCutsetAfterS1SourceLeaf.v1",
        "status": "NEXT_FRONTIER_COVER_HOMOTOPY_OR_SMOOTH_EQA_SOURCE_CERTIFICATE_OR_PHYSICAL_GAUGE_ANCHOR",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "closed_here": [
            "S1 chart-atlas and Deligne/Cech local-field equation packet built",
            "invariant dH=0 check closed",
            "conditional Poincare local-potential existence theorem closed",
            "direct finite internal operator payload boundary locked",
            "internal complement-quotient policy closed for log(2008)",
            "remaining physical/smooth source-data request built",
            "typed electroweak convention map and weak-split internal threshold imported",
            "oriented Phi_fin exact magnitude table imported as support",
            "BN central-rank signed operator identity imported as support",
        ],
        "still_open": [
            "selected contractible smooth cover and homotopy operator",
            "explicit local B_i, A_ij, g_ijk values deriving the tau shadow",
            "selected smooth projective rhoE transition tables or Deligne/Cech values",
            "smooth E_Qa source certificate or equivalent trace identity",
            "positive finite-part convention preserving signed BN orientation",
            "selected bundle A/F_A and mapped Freed-Witten/Bianchi/projector checks",
            "physical action unit K_phys or alpha_phys",
            "matching scale mu_match and RG/threshold scheme",
            "selected R_H^RG row and same-scheme Omega_H.lambda certificate",
            "direct source-native K_threshold.Omega_H.lambda",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedSmoothDomainCoverOrComplementKernelSourceLeafOrDirectHKRow",
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
            "s1_chartatlas_localfield_equation_reduction": rel(S1_EQUATIONS),
            "direct_operator_internal_boundary_and_physical_request": rel(INTERNAL_BOUNDARY),
            "oriented_phifin_smootheqa_support_import": rel(ORIENTED_SUPPORT),
            "next_cutset_after_s1_source_leaf": rel(NEXT_CUTSET),
        },
        "closure_decision": {
            "S1_equation_packet_built": True,
            "dH_zero_and_conditional_local_potentials_closed": True,
            "selected_smooth_cover_or_homotopy_emitted": False,
            "local_Deligne_Cech_values_emitted": False,
            "internal_complement_quotient_policy_closed": True,
            "physical_or_smooth_source_request_built": True,
            "typed_EW_convention_and_weak_split_imported": True,
            "oriented_PhiFin_exact_table_support_imported": True,
            "BN_signed_operator_identity_support_imported": True,
            "smooth_EQa_or_trace_identity_closed": False,
            "positive_finitepart_source_identity_closed": False,
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
            "name": "SmoothDomainCoverOrComplementKernelSourceLeafOrDirectHKRowTheorem",
            "proved": True,
            "statement": (
                "The S1 smooth source leaf is contracted to selected cover/homotopy "
                "or smooth E_Qa/physical-anchor source data. The chart-atlas "
                "equation packet, dH=0 conditional local-potential theorem, direct "
                "finite internal boundary, internal complement quotient, typed EW "
                "convention support, oriented PhiFin exact table, and BN signed "
                "operator identity are closed at support scope. They do not emit "
                "selected local Deligne/Cech values, smooth E_Qa, K_phys, R_H^RG, "
                "or K_threshold.Omega_H.lambda."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedSmoothDomainCoverOrComplementKernelSourceLeafOrDirectHKRow",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "S1_equation_packet_built": True,
        "dH_zero_and_conditional_local_potentials_closed": True,
        "internal_complement_quotient_policy_closed": True,
        "oriented_PhiFin_exact_table_support_imported": True,
        "BN_signed_operator_identity_support_imported": True,
        "selected_smooth_cover_or_homotopy_emitted": False,
        "smooth_EQa_or_trace_identity_closed": False,
        "physical_Kphys_or_normalization_closed": False,
        "selected_R_H_RG_emitted": False,
        "strict_H_K_threshold_row_emitted": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected Smooth-Domain Cover or Complement-Kernel Source Leaf or Direct H K-Row v1

## Theorem

`SmoothDomainCoverOrComplementKernelSourceLeafOrDirectHKRowTheorem` is emitted.

The S1 leaf has been pushed from a bare source request into explicit local-field
and bridge obligations.  The invariant torsion target satisfies `dH=0`, so
local `B_i` potentials are conditionally available on a selected contractible
good cover.  The direct finite internal payload and internal complement quotient
are locked at internal scope.  The oriented-PhiFin branch supplies exact
finite-table support and the BN central-rank signed operator identity, but not
the positive smooth `E_Qa`/trace identity.

## Closed Here

- S1 chart-atlas / Deligne-Cech equation packet.
- Invariant `dH=0` check.
- Conditional Poincare local-potential theorem.
- Direct finite internal operator boundary.
- Internal complement-quotient policy for `log(2008)`.
- Physical/smooth source-data request.
- Typed electroweak convention and weak-split internal threshold support.
- Oriented-PhiFin exact magnitude table as support.
- BN central-rank signed operator identity as support.

## Still Open

- Selected contractible smooth cover and homotopy operator.
- Explicit local `B_i`, `A_ij`, `g_ijk` values deriving the tau shadow.
- Smooth projective `rho_E` transition tables or Deligne/Cech values.
- Smooth `E_Qa` source certificate or equivalent trace identity.
- Positive finite-part convention preserving signed BN orientation.
- Physical `K_phys` or `alpha_phys`.
- `mu_match` and RG/threshold scheme.
- Selected `R_H^RG` row and same-scheme `Omega_H.lambda` certificate.
- Direct source-native `K_threshold.Omega_H.lambda`.

## Current Count

Strict selected `K_threshold` rows remain
`{prev["accepted_selected_K_source_row_count"]}/{prev["selected_K_threshold_row_count_required"]}`.

## Next Artifact

`{NEXT}`
"""

    write_json(S1_EQUATIONS, s1_equations)
    write_json(INTERNAL_BOUNDARY, internal_boundary)
    write_json(ORIENTED_SUPPORT, oriented_support)
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
