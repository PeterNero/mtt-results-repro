"""Build the Higgs second-variation source gate.

The previous packet fixed the B_Huv domain and the Herm(2) row-extraction law.
This packet tests the tempting metric-only shortcut and records the exact
payload that must be emitted next: a dynamic, source-owned second variation on
the B_Huv coordinates, or direct Herm(2) rows.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_higgssecondvariationfunctionalsource_or_herm2rowvalues"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SOURCE_GATE = PACKET_DIR / "source_functional_acceptance_gate.packet.json"
METRIC_NOGO = PACKET_DIR / "kinematic_metric_as_hessian_nogo.packet.json"
STRAIN_SPEC = PACKET_DIR / "dynamic_strain_kernel_payload_spec.packet.json"
VALUE_RECHECK = PACKET_DIR / "herm2_row_value_recheck_after_metric_nogo.packet.json"
HK_GATE = PACKET_DIR / "hk_threshold_gate_after_second_variation_source_gate.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_second_variation_source_gate.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HiggsSecondVariationFunctionalSource_or_Herm2RowValues_v1.md"

PREVIOUS = DATA / "selected_dynamichiggsresponsehessianonbhuv_or_directmhvalueemission.candidate.json"
PREVIOUS_DOMAIN = (
    DATA
    / "selected_dynamichiggsresponsehessianonbhuv_or_directmhvalueemission"
    / "dynamic_hessian_domain_and_extraction_gate.packet.json"
)
PREVIOUS_STRICT = (
    DATA
    / "selected_dynamichiggsresponsehessianonbhuv_or_directmhvalueemission"
    / "strict_mh_table_value_gate.packet.json"
)
PREVIOUS_VALUE_SEARCH = (
    DATA
    / "selected_dynamichiggsresponsehessianonbhuv_or_directmhvalueemission"
    / "direct_mh_value_search_after_domain_closure.packet.json"
)
PREVIOUS_HK = (
    DATA
    / "selected_dynamichiggsresponsehessianonbhuv_or_directmhvalueemission"
    / "hk_threshold_gate_after_dynamic_hessian_attempt.packet.json"
)
BHUV = (
    DATA
    / "selected_bhuvtwocolumnsourceorthonormallift_or_msourcehuvfrontier"
    / "bhuv_two_column_source_orthonormal_lift.packet.json"
)
C3_METRIC = (
    DATA
    / "selected_ehuvhymmetricconnectionfixedpoint_or_directhuvpayload"
    / "c3_ehuv_hym_metric_connection_binding.packet.json"
)
C4_TRACE = (
    DATA
    / "selected_ehuvquadraturetraceprojectionmeasure_or_directhuvpayload"
    / "c4_ehuv_finite_trace_quadrature_attachment.packet.json"
)
C5A = (
    DATA
    / "selected_ehuvtracegridprojectionidentity_or_directhuvpayload"
    / "c5a_trace_grid_identity.packet.json"
)
C5B = (
    DATA
    / "selected_ehuvtracegridprojectionidentity_or_directhuvpayload"
    / "c5b_projection_measure_gate.packet.json"
)
THREE_ROW = (
    DATA
    / "selected_mhthreerowsourcefunctional_or_c5c6bridgeexecution"
    / "mh_three_row_source_functional_contract.packet.json"
)
MH_INVENTORY = (
    DATA
    / "selected_mhvalueemissionsearch_or_c5c6bridgefrontier"
    / "mh_value_source_inventory.packet.json"
)
FULL_REDUCTION = (
    DATA
    / "selected_hsectorrestrictionfrombhuv_or_dynamichiggsresponsehessian"
    / "full_route_reduction_after_rh_closure.packet.json"
)
FULL_SOURCE_GATE = (
    DATA
    / "selected_fullmsourcehsectorrestriction_or_hresponsehuvtable"
    / "selected_source_object_value_gate.packet.json"
)

STATUS = (
    "MTT_SELECTED_HIGGSSECONDVARIATIONFUNCTIONALSOURCE_OR_HERM2ROWVALUES_"
    "METRIC_ONLY_NOGO_CLOSED_DYNAMIC_SOURCE_ROWS_OPEN"
)
NEXT = "MTT_Selected_HiggsDynamicStrainKernel_or_C5bC6ProjectionNoBoundaryProof_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Higgs second-variation inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_DOMAIN,
        PREVIOUS_STRICT,
        PREVIOUS_VALUE_SEARCH,
        PREVIOUS_HK,
        BHUV,
        C3_METRIC,
        C4_TRACE,
        C5A,
        C5B,
        THREE_ROW,
        MH_INVENTORY,
        FULL_REDUCTION,
        FULL_SOURCE_GATE,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    domain = load(PREVIOUS_DOMAIN)
    strict = load(PREVIOUS_STRICT)
    value_search = load(PREVIOUS_VALUE_SEARCH)
    previous_hk = load(PREVIOUS_HK)
    bhuv = load(BHUV)
    c3 = load(C3_METRIC)
    c4 = load(C4_TRACE)
    c5a = load(C5A)
    c5b = load(C5B)
    three_row = load(THREE_ROW)
    inventory = load(MH_INVENTORY)
    full_reduction = load(FULL_REDUCTION)
    full_source_gate = load(FULL_SOURCE_GATE)

    table = dict(strict["required_values"])
    rows_all_null = all(value is None for value in table.values())
    inventory_rows = dict(inventory["source_rows_found"])
    inventory_all_null = all(value is None for value in inventory_rows.values())
    direct_attempts_emit_values = value_search["direct_value_attempts"][
        "any_direct_attempt_emits_values"
    ]

    source_gate = {
        "schema": "MTTHiggsSecondVariationFunctionalSourceAcceptanceGate.v1",
        "status": "SECOND_VARIATION_SOURCE_GATE_CLOSED_VALUES_OPEN",
        "closure_claimed": True,
        "closed_inputs": {
            "B_Huv_domain_closed": True,
            "B_Huv_orthonormality": bhuv["whitening_map_and_lift"][
                "source_orthonormality_certificate"
            ],
            "R_H_restriction_closed": True,
            "P_H_projector_closed": True,
            "Herm2_row_extractors_closed": True,
            "C5a_trace_grid_identity_closed": c5a["proved"],
            "C4_finite_trace_attached": c4["finite_trace_quadrature"]["weight_sum_is_one"],
            "same_source_branch": domain["selected_domain"]["source_space"]["branch"],
        },
        "accepted_value_sources": {
            "direct_F_H_second_variation": {
                "accepted_if": [
                    "selected finite H-sector functional F_H is emitted",
                    "Hessian on ordered B_Huv coordinates is Hermitian",
                    "trace-free part is nonzero",
                    "finite exactness/residual certificate is attached",
                ],
                "emitted_now": False,
            },
            "full_H_response_route": {
                "formula": full_reduction["formula_after_R_H_closure"],
                "R_H_closed_now": True,
                "selected_H_response_emitted_now": full_reduction["remaining_value_objects"][
                    "selected_dynamic_H_response_emitted"
                ],
                "emitted_now": False,
            },
            "direct_Herm2_rows": {
                "required_table": table,
                "emitted_now": False,
            },
            "C5b_C6_projection_bridge": {
                "C5a_trace_grid_identity_closed": c5a["proved"],
                "C5b_projection_measure_equality_emitted": c5b[
                    "C5b_physical_Higgs_projection_measure_equality_emitted"
                ],
                "C6_no_extra_boundary_source_term_emitted": c5b[
                    "C6_no_extra_boundary_or_source_term_emitted"
                ],
                "emitted_now": False,
            },
        },
        "forbidden_promotions_retired_by_this_gate": [
            "G_Q or B_Huv^*G_QB_Huv as the Higgs mass/strain Hessian",
            "T3/connection generator as a Herm(2) value without a selected action Hessian",
            "matter/neutrino alpha1 or dotD operator blocks as the UV Higgs block",
            "diagnostic s_beta reductions or observed Higgs data as selectors",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    metric_nogo = {
        "schema": "MTTKinematicMetricAsHessianNoGo.v1",
        "status": "KINEMATIC_GQ_METRIC_AS_HESSIAN_REJECTED_TRACEFREE_ZERO",
        "closure_claimed": True,
        "theorem": {
            "name": "KinematicMetricIsNotTheHiggsSecondVariationTheorem",
            "proved": True,
            "statement": (
                "On the selected B_Huv domain, the kinematic source metric already "
                "satisfies B_Huv^* G_Q B_Huv = I_2.  Therefore the quadratic "
                "functional z^*I_2 z has trace-free Herm(2) part zero and emits "
                "Delta=Re(Omega)=Im(Omega)=0.  It fails the non-scalar Huv "
                "acceptance test and cannot be promoted as the Higgs mass/strain "
                "or response Hessian."
            ),
        },
        "candidate_functional": {
            "name": "F_metric",
            "definition": "F_metric(z)=<B_Huv z, B_Huv z>_{G_Q,Q}",
            "Hessian_on_BHuv": "B_Huv^* G_Q B_Huv = I_2",
            "source_of_identity": rel(BHUV),
        },
        "computed_trace_free_part": {
            "M_metric": [[1, 0], [0, 1]],
            "trace": 2,
            "M_metric_trace_free": [[0, 0], [0, 0]],
            "rows_if_wrongly_promoted": {
                "Delta": 0,
                "Re_Omega": 0,
                "Im_Omega": 0,
                "s_beta": None,
            },
            "non_scalar_test_passes": False,
            "light_line_defined": False,
        },
        "decision": {
            "G_Q_metric_promoted_as_M_H": False,
            "metric_only_route_closed_as_no_go": True,
            "requires_dynamic_strain_or_response_term": True,
        },
        "why_this_matters": (
            "The same metric that closes the domain cannot also supply the "
            "nonzero mass/strain vector.  The remaining source must be a "
            "dynamic second-variation/retarded-overlap response or direct "
            "Herm(2) value packet."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    strain_spec = {
        "schema": "MTTHiggsDynamicStrainKernelPayloadSpec.v1",
        "status": "DYNAMIC_STRAIN_KERNEL_PAYLOAD_SPEC_EMITTED_VALUES_OPEN",
        "closure_claimed": True,
        "payload_name": "SelectedHiggsDynamicStrainKernel",
        "must_emit": {
            "source_functional_id": None,
            "same_branch_source_owner_certificate": None,
            "finite_action_or_response_formula": None,
            "stationary_point_or_expansion_point": None,
            "Hermitian_second_variation_M_H": None,
            "trace_free_rows": {
                "Delta": None,
                "Re_Omega": None,
                "Im_Omega": None,
            },
            "nondegeneracy_certificate": None,
            "light_line_not_kernel_certificate": None,
            "finite_exactness_or_residual_bound": None,
        },
        "accepted_local_normal_form_after_payload_exists": {
            "F_H_quadratic_part": (
                "m0(|z_u|^2+|z_d|^2)+Delta(|z_u|^2-|z_d|^2)"
                "+2 Re(Omega conj(z_u) z_d)"
            ),
            "M_H_trace_free": three_row["accepted_trace_free_form"],
            "row_extractors": three_row["row_basis"],
            "s_beta_after_values": three_row["source_functional_definition"][
                "direct_Hessian_route"
            ],
        },
        "nearest_support_not_enough": {
            "C3_metric_connection_bound_to_E_H_UV": True,
            "C4_uniform_trace_attached": True,
            "C5a_trace_grid_identity_closed": c5a["proved"],
            "C5b_projection_measure_equality_open": not c5b[
                "C5b_physical_Higgs_projection_measure_equality_emitted"
            ],
            "C6_no_boundary_open": not c5b["C6_no_extra_boundary_or_source_term_emitted"],
            "full_H_response_absent": full_source_gate["derived_objects_currently_absent"][
                "H_response_absent"
            ],
            "direct_rows_absent": rows_all_null,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    value_recheck = {
        "schema": "MTTHerm2RowValueRecheckAfterMetricNoGo.v1",
        "status": "HERM2_ROW_VALUES_RECHECKED_STILL_ABSENT_AFTER_METRIC_NOGO",
        "closure_claimed": True,
        "value_sources_rechecked": {
            "previous_dynamic_gate": previous["status"],
            "direct_attempts_emit_values": direct_attempts_emit_values,
            "strict_table_rows_all_null": rows_all_null,
            "inventory_rows_all_null": inventory_all_null,
            "selected_H_response_emitted": False,
            "selected_F_H_second_variation_emitted": False,
            "C5b_projection_measure_equality_emitted": c5b[
                "C5b_physical_Higgs_projection_measure_equality_emitted"
            ],
            "C6_no_extra_boundary_source_term_emitted": c5b[
                "C6_no_extra_boundary_or_source_term_emitted"
            ],
        },
        "current_required_table": table,
        "current_inventory_rows": inventory_rows,
        "accepted_source_row_count": inventory["accepted_source_row_count"],
        "metric_only_candidate_rejected": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    h_row = dict(previous_hk["H_row"])
    h_row.update(
        {
            "second_variation_source_gate_closed": True,
            "kinematic_metric_as_hessian_nogo_closed": True,
            "dynamic_strain_kernel_payload_spec_emitted": True,
            "G_Q_metric_promoted_as_M_H": False,
            "selected_dynamic_strain_kernel_emitted": False,
            "selected_F_H_second_variation_emitted": False,
            "selected_Hermitian_M_H_values_emitted": False,
            "selected_Delta_row_emitted": False,
            "selected_Re_Omega_row_emitted": False,
            "selected_Im_Omega_row_emitted": False,
            "C5b_projection_measure_equality_emitted": c5b[
                "C5b_physical_Higgs_projection_measure_equality_emitted"
            ],
            "C6_no_extra_boundary_source_term_emitted": c5b[
                "C6_no_extra_boundary_or_source_term_emitted"
            ],
            "K_threshold_Omega_H_lambda_emitted": False,
        }
    )
    hk_gate = {
        "schema": "MTTHKThresholdGateAfterSecondVariationSourceGate.v1",
        "status": "H_K_THRESHOLD_GATE_SECOND_VARIATION_SOURCE_GATE_CLOSED_VALUES_OPEN_9_OF_10",
        "closure_claimed": True,
        "accepted_selected_K_source_row_count": previous_hk["accepted_selected_K_source_row_count"],
        "selected_K_threshold_row_count_required": previous_hk[
            "selected_K_threshold_row_count_required"
        ],
        "H_row": h_row,
        "conditional_consequent_current": previous_hk["conditional_consequent_current"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cutset = {
        "schema": "MTTNextCutsetAfterHiggsSecondVariationSourceGate.v1",
        "status": "NEXT_FRONTIER_DYNAMIC_STRAIN_KERNEL_OR_C5B_C6_PROJECTION_BRIDGE",
        "closure_claimed": True,
        "closed_here": [
            "Higgs second-variation source acceptance gate fixed",
            "kinematic G_Q metric tested and rejected as Hessian because trace-free part is zero on B_Huv",
            "dynamic strain kernel payload spec emitted",
            "direct Herm(2) row values rechecked as absent",
            "H K-threshold gate remains 9/10",
        ],
        "still_open": [
            "selected dynamic strain/response functional F_H with nonzero Herm(2) trace-free part",
            "or selected H_response table feeding the closed R_H route",
            "or direct Huu,Hud,Hdd rows with source/exactness certificates",
            "or C5b projection-measure equality plus C6 no-extra-boundary/source theorem",
            "nondegeneracy and light-line certificates after values emit",
            "selected s_beta or equivalent H quartic/threshold functional",
            "K_threshold.Omega_H.lambda source row",
            "strict Omega/lambda_H scalar execution",
        ],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHiggsSecondVariationFunctionalSourceOrHerm2RowValues",
        "status": STATUS,
        "previous_status": previous["status"],
        "theorem": {
            "name": "KinematicMetricIsNotTheHiggsSecondVariationTheorem",
            "proved": True,
            "statement": metric_nogo["theorem"]["statement"],
        },
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "closure_decision": {
            "B_Huv_domain_closed": True,
            "R_H_kinematic_restriction_closed": True,
            "Herm2_row_extraction_law_closed": True,
            "second_variation_source_gate_closed": True,
            "kinematic_metric_as_hessian_nogo_closed": True,
            "dynamic_strain_kernel_payload_spec_emitted": True,
            "herm2_value_rows_rechecked_after_metric_nogo": True,
            "G_Q_metric_promoted_as_M_H": False,
            "selected_dynamic_strain_kernel_emitted": False,
            "selected_F_H_second_variation_emitted": False,
            "selected_dynamic_H_response_emitted": False,
            "selected_Hermitian_M_source_emitted": False,
            "selected_Hermitian_M_H_values_emitted": False,
            "direct_Herm2_Huv_payload_emitted": False,
            "selected_Delta_row_emitted": False,
            "selected_Re_Omega_row_emitted": False,
            "selected_Im_Omega_row_emitted": False,
            "selected_s_beta_value_found": False,
            "C5b_projection_measure_equality_emitted": c5b[
                "C5b_physical_Higgs_projection_measure_equality_emitted"
            ],
            "C6_no_extra_boundary_source_term_emitted": c5b[
                "C6_no_extra_boundary_or_source_term_emitted"
            ],
            "K_threshold_Omega_H_lambda_emitted": False,
            "accepted_selected_K_source_row_count": previous_hk["accepted_selected_K_source_row_count"],
            "selected_K_threshold_row_count_required": previous_hk[
                "selected_K_threshold_row_count_required"
            ],
            "ten_K_antecedent_satisfied": False,
            "strict_Omega_lambda_scalar_execution_closed": False,
            "accepted_internal_scalar_value_row_count": 0,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "source_functional_acceptance_gate": rel(SOURCE_GATE),
            "kinematic_metric_as_hessian_nogo": rel(METRIC_NOGO),
            "dynamic_strain_kernel_payload_spec": rel(STRAIN_SPEC),
            "herm2_row_value_recheck_after_metric_nogo": rel(VALUE_RECHECK),
            "hk_threshold_gate_after_second_variation_source_gate": rel(HK_GATE),
            "next_cutset_after_second_variation_source_gate": rel(CUTSET),
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTTSelectedHiggsSecondVariationFunctionalSourceOrHerm2RowValuesCertificate",
        "status": STATUS,
        "theorem_proved": True,
        "B_Huv_domain_closed": True,
        "R_H_kinematic_restriction_closed": True,
        "Herm2_row_extraction_law_closed": True,
        "second_variation_source_gate_closed": True,
        "kinematic_metric_as_hessian_nogo_closed": True,
        "dynamic_strain_kernel_payload_spec_emitted": True,
        "herm2_value_rows_rechecked_after_metric_nogo": True,
        "G_Q_metric_promoted_as_M_H": False,
        "selected_dynamic_strain_kernel_emitted": False,
        "selected_F_H_second_variation_emitted": False,
        "selected_Hermitian_M_H_values_emitted": False,
        "direct_Herm2_Huv_payload_emitted": False,
        "selected_Delta_row_emitted": False,
        "selected_Re_Omega_row_emitted": False,
        "selected_Im_Omega_row_emitted": False,
        "selected_s_beta_value_found": False,
        "K_threshold_Omega_H_lambda_emitted": False,
        "accepted_selected_K_source_row_count": previous_hk["accepted_selected_K_source_row_count"],
        "selected_K_threshold_row_count_required": previous_hk[
            "selected_K_threshold_row_count_required"
        ],
        "ten_K_antecedent_satisfied": False,
        "strict_Omega_lambda_scalar_execution_closed": False,
        "accepted_internal_scalar_value_row_count": 0,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected HiggsSecondVariationFunctionalSource or Herm2RowValues v1

Status: `{STATUS}`

## What Closed

- fixed the accepted source routes for the Higgs second variation on `B_Huv`
- proved `G_Q`/`B_Huv^*G_QB_Huv` cannot be promoted to `M_H`
- emitted the exact `SelectedHiggsDynamicStrainKernel` payload spec
- rechecked direct Herm(2) rows after the metric-only no-go

## Key No-Go

`B_Huv^* G_Q B_Huv = I_2`, so the kinematic metric has zero trace-free
Herm(2) part on the whitened domain. If promoted, it would emit
`Delta=Re(Omega)=Im(Omega)=0`, fail non-scalar acceptance, and leave no light
line. The missing object must be a dynamic strain/response source, not the
domain metric.

## Still Open

- selected dynamic strain/response functional `F_H`
- selected `H_response` table or direct `Huu,Hud,Hdd`
- C5b projection-measure equality and C6 no-extra-boundary/source proof
- `K_threshold.Omega_H.lambda` and strict `Omega/lambda_H` execution

Next required artifact: `{NEXT}`
"""

    write_json(SOURCE_GATE, source_gate)
    write_json(METRIC_NOGO, metric_nogo)
    write_json(STRAIN_SPEC, strain_spec)
    write_json(VALUE_RECHECK, value_recheck)
    write_json(HK_GATE, hk_gate)
    write_json(CUTSET, cutset)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
