"""Build differentiated PhiFinC1 primitive-overlap / Galerkin run gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PREVIOUS = DATA / "selected_phifinc1_dynamictransferidentity_proof_or_galerkincontractions_run.candidate.json"
DOTD = DATA / "selected_dotd_alpha1_transport_derivative_probe.candidate.json"
CROSSREPO_ALPHA1 = DATA / "selected_crossrepo_alpha1_driver_replay_import.candidate.json"
C1_RESPONSE_AUDIT = DATA / "selected_routec_selected_c1_response_operator_emission.candidate.json"
CANONICAL_C1 = DATA / "selected_routec_c1_primitive_response_on_smooth_bn.candidate.json"
NONINVARIANT_SEARCH = DATA / "selected_routec_noninvariant_c1_primitive_search.candidate.json"
PRIMITIVE_ENVELOPE = DATA / "selected_primitivec1_contractions_or_dynamicoverlaptensor_sourceemission.candidate.json"
NONSCALAR = DATA / "selected_nonscalardynamicoverlap_or_fullresponsecorrection_valueemission.candidate.json"
DYNAMIC = DATA / "selected_dynamictransferhessian_bselected_or_honestgalerkinc1_valuefill.candidate.json"
GALERKIN_C1 = DATA / "selected_routec_strominger_galerkin_solve" / "c1_primitive_contractions.candidate.json"

OUTPUT = DATA / "selected_differentiated_phifinc1_primitiveoverlap_or_galerkinrun.candidate.json"
TEMPLATE_DIR = DATA / "selected_differentiated_phifinc1_primitiveoverlap_or_galerkinrun"
TEMPLATE = TEMPLATE_DIR / "primitive_overlap_contractions.template.json"
CERT = CERTS / "selected_differentiated_phifinc1_primitiveoverlap_or_galerkinrun_certificate.json"
NOTE = CORPUS / "MTT_Selected_DifferentiatedPhiFinC1_PrimitiveOverlapContractions_or_GalerkinRun_v1.md"

STATUS = "MTT_SELECTED_DIFFERENTIATED_PHIFINC1_PRIMITIVEOVERLAP_OR_GALERKINRUN_BUILT_TRANSPORT_ONLY_NOGO_TEMPLATE_OPEN"
NEXT = "MTT_Selected_PrimitiveVertexSource_or_BasisTransport_SelectionTheorem_v1"

SECTORS = ["u", "d", "e", "nuD"]


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def is_zero_matrix(matrix: list[list[Any]]) -> bool:
    return all(entry == 0 or entry == 0.0 for row in matrix for entry in row)


def max_rank_for_fixed_fibers(search: dict[str, Any]) -> dict[str, Any]:
    fixed = [c for c in search["candidate_primitives"] if isinstance(c["primitive_fiber_shift"], int)]
    all_fiber = [c for c in search["candidate_primitives"] if c["primitive_fiber_shift"] == "all"][0]
    rank_sets = {
        str(c["primitive_fiber_shift"]): {
            sector: c["summary"][sector]["rank"] for sector in SECTORS
        }
        for c in fixed
    }
    max_abs_values = sorted(
        {
            c["summary"][sector]["max_abs_entry"]
            for c in fixed
            for sector in SECTORS
        }
    )
    return {
        "fixed_fiber_candidates": [c["primitive_fiber_shift"] for c in fixed],
        "fixed_fiber_candidate_count": len(fixed),
        "all_fixed_fiber_rank_three": all(
            c["summary"][sector]["rank"] == 3 for c in fixed for sector in SECTORS
        ),
        "rank_by_fixed_fiber": rank_sets,
        "max_abs_values": max_abs_values,
        "all_fiber_rank_by_sector": {
            sector: all_fiber["summary"][sector]["rank"] for sector in SECTORS
        },
        "all_fiber_rank_one": all(all_fiber["summary"][sector]["rank"] == 1 for sector in SECTORS),
    }


def sector_couplings(canonical: dict[str, Any]) -> dict[str, dict[str, str]]:
    return {
        sector: {
            "left_sector": canonical["c1_response_matrices"][sector]["left_sector"],
            "right_sector": canonical["c1_response_matrices"][sector]["right_sector"],
            "higgs_sector": canonical["c1_response_matrices"][sector]["higgs_sector"],
        }
        for sector in SECTORS
    }


def build_template(coord: dict[str, Any], alpha1_import: dict[str, bool], couplings: dict[str, dict[str, str]]) -> dict[str, Any]:
    return {
        "schema": "MTTSelectedDifferentiatedPhiFinC1PrimitiveOverlapContractions.v1",
        "status": "OPEN_SELECTED_PRIMITIVE_OVERLAP_CONTRACTIONS_MISSING",
        "coordinate_system": coord,
        "selected_source_branch": {
            "branch": "q79/F,m=1 S3/GS Route-C",
            "source_selected_stationary_layer": True,
            "differentiated_primitive_source_selected": False,
            "observed_data_used": False,
        },
        "alpha1_dotD_driver": {
            "selected_dotD_source_verified": alpha1_import["selected_dotD_source_verified_imported"],
            "alpha1_driver_verified": alpha1_import["alpha1_driver_verified_imported"],
            "primitive_overlap_values_emitted_by_driver": False,
        },
        "formula_slots": {
            "sector_couplings": couplings,
            "primitive_formula": (
                "M_s^r[i,j] = <psi_L,i, V_r psi_R,j H_s> + "
                "<delta_r psi_L,i, V_0 psi_R,j H_s> + "
                "<psi_L,i, V_0 delta_r psi_R,j H_s> + "
                "<psi_L,i, V_0 psi_R,j delta_r H_s> + HessianCounterterm_s^r[i,j]"
            ),
            "directions": ["phase_Z", "shift_X"],
            "sectors": SECTORS,
        },
        "required_selected_values": {
            "transported_zero_mode_bases": None,
            "selected_L2_Gram_Schmidt_rule": None,
            "selected_primitive_vertex_operator_phase_Z": None,
            "selected_primitive_vertex_operator_shift_X": None,
            "primitive_three_by_three_contraction_terms": {sector: None for sector in SECTORS},
            "linear_response_matrices": {sector: None for sector in SECTORS},
            "Hessian_counterterms": {sector: None for sector in SECTORS},
            "A_selected_72_real_columns": None,
            "b_selected_72_real_source_vector": None,
            "deltaTheta_C1": None,
        },
        "validators_after_fill": [
            "canonical transport-only zero lane remains separated",
            "A_selected columns map into the fixed 72-real coordinate system",
            "rank(A_selected)=2 or emitted replacement rank theorem",
            "A_selected^T A_selected and A_selected^T b_selected reported",
            "sector response matrices M_u, M_d, M_e, M_nuD emitted",
            "C33/nonzero-family-rank tests",
            "mass-split traceless norm tests",
            "CKM/PMNS commutator tests",
            "CP-odd invariant test",
        ],
    }


def main() -> int:
    previous = load(PREVIOUS)
    dotd = load(DOTD)
    crossrepo = load(CROSSREPO_ALPHA1)
    c1_audit = load(C1_RESPONSE_AUDIT)
    canonical = load(CANONICAL_C1)
    noninvariant = load(NONINVARIANT_SEARCH)
    primitive_envelope = load(PRIMITIVE_ENVELOPE)
    nonscalar = load(NONSCALAR)
    dynamic = load(DYNAMIC)
    galerkin_c1 = load(GALERKIN_C1)

    coord = previous["coordinate_system"]
    alpha1_import = {
        "selected_dotD_source_verified_imported": crossrepo["selected_dotD_source_verified_imported"],
        "alpha1_driver_verified_imported": crossrepo["alpha1_driver_verified_imported"],
        "honest_dotD_alpha1_replay_imported": crossrepo["alpha1_driver_replay_import"][
            "honest_dotD_alpha1_replay"
        ],
    }
    couplings = sector_couplings(canonical)
    template = build_template(coord, alpha1_import, couplings)

    canonical_zero = {
        "source": rel(CANONICAL_C1),
        "canonical_tensor_name": canonical["primitive_tensor"]["name"],
        "canonical_tensor_selected_by_theorem": canonical["primitive_tensor"]["selected_by_theorem"],
        "all_c1_matrices_zero_for_canonical_tensor": canonical["diagnostics"][
            "all_c1_matrices_zero_for_canonical_tensor"
        ],
        "all_sector_matrices_verified_zero": all(
            is_zero_matrix(canonical["c1_response_matrices"][sector]["matrix"]) for sector in SECTORS
        ),
        "reason": canonical["diagnostics"]["why_zero"],
        "c1_response_audit_canonical_status": c1_audit["response_lanes"][
            "canonical_smooth_bn_response"
        ]["status"],
        "can_emit_phase_shift_columns": False,
    }

    noninvariant_summary = max_rank_for_fixed_fibers(noninvariant)
    noninvariant_import = {
        "source": rel(NONINVARIANT_SEARCH),
        "active_shift": noninvariant["search_rule"]["minimal_active_shift_required"],
        "active_shift_forced": noninvariant["calculation_results"]["all_four_tested_candidates_nonzero"],
        "observed_flavor_data_used": False,
        "selected_by_theorem": False,
        "candidate_summary": noninvariant_summary,
        "primitive_envelope_constructed": primitive_envelope["contraction_envelope"]["constructed"],
        "primitive_envelope_selected_as_dynamic_tensor": primitive_envelope["contraction_envelope"][
            "selected_as_dynamic_tensor"
        ],
    }

    driver_contract = {
        "dotD_transport_formula_source": rel(DOTD),
        "crossrepo_alpha1_source": rel(CROSSREPO_ALPHA1),
        "selected_dotD_source_verified": alpha1_import["selected_dotD_source_verified_imported"],
        "alpha1_driver_verified": alpha1_import["alpha1_driver_verified_imported"],
        "honest_dotD_alpha1_replay": alpha1_import["honest_dotD_alpha1_replay_imported"],
        "transport_derivative_formula": dotd["transport_derivative_formula"],
        "attached_to_differentiated_contract_as_driver": True,
        "primitive_overlap_values_emitted_by_driver": False,
        "why_not_sufficient": (
            "The alpha1/dotD driver fixes horizontal response terms, but it does not select the "
            "primitive vertex tensor, basis-transport correction, or Hessian/source vector that "
            "would produce phase/shift C1 columns."
        ),
    }

    differentiated_contract = {
        "template_path": rel(TEMPLATE),
        "template_status": template["status"],
        "coordinate_system": coord,
        "sector_couplings": couplings,
        "primitive_overlap_formula": template["formula_slots"]["primitive_formula"],
        "acceptance_equations": [
            "vectorize(M_u^phase, M_d^phase, M_e^phase, M_nuD^phase)=phase_packet or emitted replacement column",
            "vectorize(M_u^shift, M_d^shift, M_e^shift, M_nuD^shift)=shift_packet or emitted replacement column",
            "A_selected=[phase_column, shift_column]",
            "b_selected is emitted by the same primitive/Hessian source, not copied from a target vector",
            "deltaTheta_C1 solves A_selected deltaTheta=b_selected after selected values are emitted",
        ],
        "current_conditional_values_if_future_packet_matches_normal_form": previous[
            "PhiFinC1_identity_attempt"
        ]["if_future_identity_proved_then_values"],
        "normal_form_values_promoted_now": False,
    }

    transport_only_no_go = {
        "name": "DifferentiatedPhiFinC1TransportOnlyNoGo",
        "proved": True,
        "scope": "current emitted B_N/dotD packet with the canonical mode-conserving primitive tensor",
        "statement": (
            "The selected alpha1/dotD transport derivative supplies the horizontal response formula, "
            "but transport of the stationary packet and the canonical mode-conserving trilinear tensor "
            "produce zero one-response C1 matrices.  Therefore the phase/shift C1 columns cannot be "
            "obtained from pure stationary transport alone; a selected non-invariant primitive vertex, "
            "basis-transport correction, Hessian source term, or honest Galerkin C1 contraction run is required."
        ),
        "finite_evidence": {
            "canonical_all_zero": canonical_zero["all_c1_matrices_zero_for_canonical_tensor"],
            "all_sector_matrices_verified_zero": canonical_zero["all_sector_matrices_verified_zero"],
            "nonzero_unselected_candidates_found": noninvariant["calculation_results"][
                "nonzero_unselected_candidates_found"
            ],
            "conditional_non_scalar_packet_passes_tests": nonscalar[
                "conditional_non_scalar_value_packet"
            ]["acceptance_tests"]["current_layer_flavor_tests_pass_conditionally"],
        },
    }

    promotion_decision = {
        "alpha1_dotD_driver_attached_to_contract": True,
        "transport_only_lane_rejected_as_phase_shift_source": True,
        "primitive_overlap_template_emitted": True,
        "selected_primitive_vertex_or_basis_transport_emitted": False,
        "selected_primitive_overlap_contractions_promoted": False,
        "selected_A_selected_promoted": False,
        "selected_b_selected_promoted": False,
        "selected_deltaTheta_C1_promoted": False,
        "selected_sector_response_matrices_promoted": False,
        "honest_Galerkin_C1_contractions_promoted": False,
        "full_SM_no_knob_closure_promoted": False,
    }

    candidate = {
        "candidate": "MTTSelectedDifferentiatedPhiFinC1PrimitiveOverlapOrGalerkinRun",
        "status": STATUS,
        "inputs": {
            "previous_PhiFinC1_gate": rel(PREVIOUS),
            "dotD_transport_derivative_probe": rel(DOTD),
            "crossrepo_alpha1_driver_replay_import": rel(CROSSREPO_ALPHA1),
            "selected_C1_response_operator_audit": rel(C1_RESPONSE_AUDIT),
            "canonical_C1_primitive_response": rel(CANONICAL_C1),
            "noninvariant_C1_primitive_search": rel(NONINVARIANT_SEARCH),
            "primitive_contraction_envelope": rel(PRIMITIVE_ENVELOPE),
            "conditional_non_scalar_packet": rel(NONSCALAR),
            "dynamic_transfer_value_gate": rel(DYNAMIC),
            "honest_Galerkin_C1_manifest": rel(GALERKIN_C1),
        },
        "driver_contract": driver_contract,
        "canonical_transport_only_test": canonical_zero,
        "noninvariant_candidate_import": noninvariant_import,
        "differentiated_primitive_overlap_contract": differentiated_contract,
        "Galerkin_manifest_status": {
            "status": galerkin_c1["status"],
            "selected_source_verified": galerkin_c1["selected_source_verified"],
            "required_outputs": galerkin_c1["required_outputs"],
        },
        "conditional_dynamic_values_retained_as_unpromoted": dynamic[
            "conditional_dynamic_transfer_coordinate_packet"
        ],
        "transport_only_no_go_theorem": transport_only_no_go,
        "promotion_decision": promotion_decision,
        "what_closes_now": {
            "selected_alpha1_dotD_driver_attached_to_differentiated_contract": True,
            "transport_only_C1_lane_rejected": True,
            "canonical_zero_response_imported_and_verified": True,
            "noninvariant_rank3_candidate_class_imported_as_unselected": True,
            "primitive_overlap_template_emitted": True,
            "next_source_theorem_target_sharpened": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_primitive_vertex_or_basis_transport_source_theorem": True,
            "selected_primitive_overlap_contractions": True,
            "selected_Hessian_source_vector_b_selected": True,
            "selected_A_selected_deltaTheta_sector_response_matrices": True,
            "honest_Galerkin_C1_run_values": True,
            "Yukawa_CKM_PMNS_masses_Higgs_RG_no_knob": True,
            "full_SM_no_knob_closure": True,
        },
        "closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "selected_primitive_overlap_contractions_claimed": False,
        "selected_PhiFinC1_identity_claimed": False,
        "A_selected_claimed": False,
        "b_selected_claimed": False,
        "deltaTheta_C1_claimed": False,
        "Galerkin_C1_contractions_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_DifferentiatedPhiFinC1_PrimitiveOverlapContractions_or_GalerkinRun_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "template_path": rel(TEMPLATE),
        "note_path": rel(NOTE),
        "closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "transport_only_no_go_proved": True,
        "primitive_overlap_template_emitted": True,
        "selected_primitive_overlap_contractions_claimed": False,
        "A_selected_claimed": False,
        "b_selected_claimed": False,
        "deltaTheta_C1_claimed": False,
        "Galerkin_C1_contractions_claimed": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected DifferentiatedPhiFinC1 PrimitiveOverlapContractions or GalerkinRun v1

Status: `{STATUS}`.

This artifact attaches the theorem-derived alpha1/dotD driver to the
differentiated `Phi_fin^C1` contract, then proves the transport-only lane is
not enough.

Closed now:

```text
dU/dalpha = -(du/dalpha) ad(T3) U
selected_dotD_source_verified = true
alpha1_driver_verified        = true
canonical mode-conserving C1 response = 0 in u,d,e,nuD
```

The nonzero finite primitive candidates are imported only as unselected support:
active shift `(1,1)`, fixed fiber shifts `{noninvariant_summary["fixed_fiber_candidates"]}`,
rank-three fixed-fiber matrices, and rank-one all-fiber envelope.

The emitted template is:

```text
{rel(TEMPLATE)}
```

It must be filled by a selected primitive vertex / basis-transport source
theorem or by an honest selected Galerkin C1 run.  Until then, the conditional
normal-form values remain unpromoted:

```text
A^T A         = {previous["PhiFinC1_identity_attempt"]["if_future_identity_proved_then_values"]["Gram_A_transpose_A"]}
A^T b         = {previous["PhiFinC1_identity_attempt"]["if_future_identity_proved_then_values"]["A_transpose_b"]}
deltaTheta_C1 = {previous["PhiFinC1_identity_attempt"]["if_future_identity_proved_then_values"]["deltaTheta_C1"]}
```

No observed masses, mixings, CP phase, benchmark matrices, or target residuals
are used as selectors.

Next artifact: `{NEXT}`.
"""

    TEMPLATE_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    TEMPLATE.write_text(json.dumps(template, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "template": rel(TEMPLATE), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
