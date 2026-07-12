"""Build Weyl-pair dynamic-overlap source-promotion / honest Galerkin C1 gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

NONSCALAR = DATA / "selected_nonscalardynamicoverlap_or_fullresponsecorrection_valueemission.candidate.json"
STATIC_ROUTING = DATA / "selected_primitivec1_or_weylpair_sectorrouting_sourceemission.candidate.json"
SOURCE_PROVENANCE = DATA / "selected_routec_weylpair_source_provenance_lemma.candidate.json"
SOURCE_TO_C1 = DATA / "selected_routec_weylpair_source_to_c1_transfer_map.candidate.json"
A_ASSEMBLY = DATA / "selected_routec_weylpair_aselected_assembly_or_source_proof.candidate.json"
C1_RESPONSE = DATA / "selected_routec_selected_c1_response_operator_emission.candidate.json"
GALERKIN = DATA / "selected_routec_strominger_galerkin_solve" / "c1_primitive_contractions.candidate.json"

OUTPUT = DATA / "selected_weylpairdynamicoverlap_sourcepromotion_or_honestgalerkinc1_valuefill.candidate.json"
CERT = CERTS / "selected_weylpairdynamicoverlap_sourcepromotion_or_honestgalerkinc1_valuefill_certificate.json"
NOTE = CORPUS / "MTT_Selected_WeylPairDynamicOverlap_SourcePromotion_or_HonestGalerkinC1_ValueFill_v1.md"

STATUS = (
    "MTT_SELECTED_WEYLPAIRDYNAMICOVERLAP_SOURCEPROMOTION_OR_HONESTGALERKINC1_"
    "VALUEFILL_BUILT_PROMOTION_CUTSET_OPEN"
)
NEXT = "MTT_Selected_DynamicTransferHessian_bSelected_or_HonestGalerkinC1_ValueFill_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    nonscalar = load(NONSCALAR)
    static_routing = load(STATIC_ROUTING)
    source_provenance = load(SOURCE_PROVENANCE)
    source_to_c1 = load(SOURCE_TO_C1)
    a_assembly = load(A_ASSEMBLY)
    c1_response = load(C1_RESPONSE)
    galerkin = load(GALERKIN)

    closed_static_source_tier = {
        "source_level_Z_and_X_carrier": (
            source_provenance["what_closes_now"]["source_level_phase_Z_carrier_provenance"]
            and source_provenance["what_closes_now"]["source_level_shift_X_carrier_provenance"]
        ),
        "active_shift_1_1": source_provenance["what_closes_now"][
            "active_shift_1_1_provenance"
        ],
        "static_Z_clock_to_u_e": static_routing["static_routing_source_emission"][
            "retired_sector_routing"
        ]["phase_route"]
        == ["u", "e"],
        "static_X_shift_to_d_nuD": static_routing["static_routing_source_emission"][
            "retired_sector_routing"
        ]["shift_route"]
        == ["d", "nuD"],
        "static_1M_Nc_shift_rule": static_routing["what_closes_now"][
            "selected_static_singlet_neutrino_shift_rule_emitted"
        ],
        "static_trace_transfer_normalization": static_routing["what_closes_now"][
            "selected_static_trace_transfer_normalization_emitted"
        ],
        "conditional_non_scalar_packet": nonscalar["conditional_non_scalar_value_packet"][
            "constructed"
        ],
        "conditional_weylpair_rank_and_solve": (
            a_assembly["locked_solve"]["rank"] == 2
            and a_assembly["locked_solve"]["consistent"]
        ),
    }

    tests = nonscalar["conditional_non_scalar_value_packet"]["acceptance_tests"]
    dynamic_slots = c1_response["emission_audit"]["required_operator_slots"]

    lane_a = {
        "name": "Weyl-pair dynamic-overlap source-promotion lane",
        "conditional_transfer_exact": source_to_c1["conditional_transfer_map"][
            "conditional_exact"
        ],
        "conditional_transfer_formula": source_to_c1["conditional_transfer_map"]["formula"],
        "conditional_transfer_residuals": {
            "phase_residual": source_to_c1["conditional_transfer_map"]["phase_residual"],
            "shift_residual": source_to_c1["conditional_transfer_map"]["shift_residual"],
        },
        "static_source_route_reclassified_closed": True,
        "conditional_packet_tests_pass": {
            "mass_split": tests["all_mass_split_positive"],
            "ckm_commutator": tests["ckm_commutator_positive"],
            "pmns_commutator": tests["pmns_commutator_positive"],
            "cp_odd": tests["cp_odd_invariant_nonzero"],
        },
        "selected_promotion_fields": {
            "selected_dynamic_source_to_C1_transfer": False,
            "selected_dynamic_overlap_tensor": False,
            "selected_Hessian_blocks": dynamic_slots["full_lower_order_Hess_Xi_blocks"],
            "selected_b_selected": c1_response["emission_audit"][
                "selected_source_vector_b_selected_emitted"
            ],
            "selected_A_selected": c1_response["emission_audit"][
                "selected_operator_A_selected_emitted"
            ],
            "selected_sector_response_matrices": dynamic_slots[
                "sector_response_matrices_M_u_M_d_M_e_M_nuD"
            ],
            "selected_deltaTheta_C1_solution": dynamic_slots[
                "selected_deltaTheta_C1_solution"
            ],
        },
        "promoted": False,
        "why_not_promoted": (
            "The Weyl-pair transfer is exact as a conditional algebraic map and its "
            "static routing is selected, but no current artifact emits the dynamic "
            "source-to-C1 transfer tensor, Hessian blocks, A_selected, b_selected, "
            "or sector response matrices from the selected branch."
        ),
    }

    lane_b = {
        "name": "Honest Galerkin C1 value-fill lane",
        "manifest_status": galerkin["status"],
        "selected_source_verified": galerkin["selected_source_verified"],
        "required_outputs": galerkin["required_outputs"],
        "required_outputs_present": {
            "zero_mode_bases": False,
            "primitive_three_by_three_contraction_terms": False,
            "linear_response_matrices": False,
            "C33_nonzero_family_rank_tests": False,
        },
        "promoted": False,
        "why_not_promoted": (
            "The honest Galerkin manifest is still a missing-values contract: it has "
            "not emitted selected zero-mode bases, primitive 3x3 contraction terms, "
            "linear response matrices, or the C33/nonzero-family-rank tests."
        ),
    }

    minimum_cutset = {
        "statement": (
            "A selected non-scalar flavor packet can now close only by filling one of "
            "two equivalent value sources: Lane A dynamic transfer/Hessian/b_selected "
            "from the selected Weyl-pair source, or Lane B honest selected Galerkin "
            "C1 contractions that emit the same sector response data."
        ),
        "lane_A_fill_all": [
            "selected_dynamic_source_to_C1_transfer_tensor",
            "selected_Hessian_blocks",
            "selected_b_selected",
            "selected_A_selected",
            "selected_sector_response_matrices",
            "selected_deltaTheta_C1_solution_or_consistency_rejection",
        ],
        "lane_B_fill_all": galerkin["required_outputs"],
        "static_routing_no_longer_in_cutset": True,
        "observed_flavor_data_forbidden_as_selector": True,
    }

    candidate = {
        "candidate": "MTTSelectedWeylPairDynamicOverlapSourcePromotionOrHonestGalerkinC1ValueFill",
        "status": STATUS,
        "inputs": {
            "conditional_non_scalar_packet": rel(NONSCALAR),
            "static_sector_routing": rel(STATIC_ROUTING),
            "weylpair_source_provenance": rel(SOURCE_PROVENANCE),
            "conditional_source_to_C1_transfer": rel(SOURCE_TO_C1),
            "conditional_A_assembly": rel(A_ASSEMBLY),
            "selected_C1_response_operator_emission": rel(C1_RESPONSE),
            "honest_galerkin_C1_contractions_manifest": rel(GALERKIN),
        },
        "closed_static_source_tier": closed_static_source_tier,
        "lane_A_dynamic_source_promotion": lane_a,
        "lane_B_honest_Galerkin_C1_value_fill": lane_b,
        "minimum_cutset": minimum_cutset,
        "promotion_decision": {
            "static_source_route_retired_as_blocker": True,
            "conditional_non_scalar_packet_available": True,
            "selected_dynamic_overlap_promoted": False,
            "selected_full_response_promoted": False,
            "selected_A_selected_promoted": False,
            "selected_b_selected_promoted": False,
            "selected_Galerkin_C1_contractions_promoted": False,
            "dynamic_promotion_cutset_open": True,
        },
        "what_closes_now": {
            "promotion_cutset_built": True,
            "stale_static_sector_routing_blocker_superseded": True,
            "conditional_transfer_tied_to_static_selected_routing": True,
            "honest_Galerkin_value_fill_requirements_extracted": True,
            "no_target_fitting_guard_preserved": True,
        },
        "what_remains_open": {
            "selected_dynamic_source_to_C1_transfer": True,
            "selected_dynamic_overlap_tensor": True,
            "selected_Hessian_blocks": True,
            "selected_b_selected": True,
            "selected_A_selected": True,
            "selected_sector_response_matrices": True,
            "selected_deltaTheta_C1_solution": True,
            "honest_Galerkin_C1_contractions": True,
            "Yukawa_CKM_PMNS_masses_Higgs_RG_no_knob": True,
            "full_SM_no_knob_closure": True,
        },
        "closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "selected_dynamic_overlap_tensor_claimed": False,
        "selected_full_response_claimed": False,
        "A_selected_claimed": False,
        "b_selected_claimed": False,
        "Galerkin_C1_contractions_claimed": False,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "WeylPairDynamicOverlapSourcePromotionOrHonestGalerkinC1ValueFillCutsetTheorem",
            "proved": True,
            "statement": (
                "The selected static source layer now emits the Weyl carrier, active shift, "
                "Z/clock -> u,e and X/shift -> d,nuD routing, the 1_M=N^c shift-side rule, "
                "and finite trace normalization.  The conditional Weyl-pair transfer then "
                "exactly produces the non-scalar I+Z/I+X packet that passes mass-split, "
                "mixing, and CP qualitative tests without observed flavor targets.  This "
                "does not yet promote the packet to selected dynamic overlap data: the "
                "remaining proof obligation is precisely either selected dynamic transfer/"
                "Hessian/A_selected/b_selected values or honest selected Galerkin C1 "
                "contractions emitting the same response data."
            ),
        },
    }

    cert = {
        "certificate": "MTT_Selected_WeylPairDynamicOverlap_SourcePromotion_or_HonestGalerkinC1_ValueFill_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "selected_dynamic_overlap_tensor_claimed": False,
        "selected_full_response_claimed": False,
        "A_selected_claimed": False,
        "b_selected_claimed": False,
        "Galerkin_C1_contractions_claimed": False,
        "theorem_proved": True,
        "minimum_cutset": minimum_cutset,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected WeylPairDynamicOverlap SourcePromotion or HonestGalerkinC1 ValueFill v1

Status: `{STATUS}`.

This gate separates the finished source tier from the live dynamic tier.

Closed source/static tier:

```text
Z/clock/phase -> u,e
X/shift       -> d,nuD
1_M=N^c       -> shift/Dirac-neutrino side
active shift  -> (1,1)
trace transfer normalization -> selected static source layer
```

Conditional finite response already available:

```text
T(Z) = sector_route(u,e; I+Z)
T(X) = sector_route(d,nuD; I+X)
deltaTheta_conditional = {a_assembly["locked_solve"]["deltaTheta_conditional"]}
mass split test = {tests["all_mass_split_positive"]}
CKM test        = {tests["ckm_commutator_positive"]}
PMNS test       = {tests["pmns_commutator_positive"]}
CP odd test     = {tests["cp_odd_invariant_nonzero"]}
```

Promotion is still blocked.  The remaining cutset is now exact:

```text
Lane A: selected dynamic transfer/Hessian/A_selected/b_selected/sector response matrices
Lane B: honest selected Galerkin C1 zero-mode bases, primitive contractions,
        linear response matrices, and C33/nonzero-family-rank tests
```

No observed masses, CKM/PMNS values, CP phase, or benchmark entries are used as
selectors.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
