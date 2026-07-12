"""Build pure-Weyl rows source-identity frontier / honest kernel export gate.

The pure-Weyl coefficient artifact left the next target as zero-mode/Hessian/
primitive-row execution.  The wider corpus already contains stronger evidence:
model-active zero-mode values, accepted dynamic dotD trace binding, exact
conditional Hessian/b linear algebra, exact 72 primitive-row support, and a
conditional Route-B validator pass.  This artifact reconciles that work with
the current pure-Weyl branch and records the sharper frontier:

    derive the unpatched SelectedFiniteC1SourceIdentityPrinciple, or
    export an honest independent 110-row finite-C1 kernel table.

The local/principle-insertion path is kept as patched support only.  No
unpatched/full-SM/no-knob closure is claimed here.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_pureweylrows_sourceidentityfrontier_or_honestkernelexport"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
RECONCILIATION = PACKET_DIR / "retired_numeric_blockers_reconciliation.packet.json"
SOURCE_REDUCTION = PACKET_DIR / "pure_weyl_rows_source_identity_reduction.packet.json"
FINAL_ROUTES = PACKET_DIR / "final_two_route_after_pure_weyl.packet.json"
NEXT_ORDER = PACKET_DIR / "next_execution_order_after_source_identity_frontier.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PureWeylRows_SourceIdentityFrontier_or_HonestKernelExport_v1.md"

PURE_WEYL = DATA / "selected_pureweylcoefficientrows_or_primitivec1formulaexecution.candidate.json"
HYM_VALUES = DATA / "selected_hym_projector_zeromode_basis_value_emission.candidate.json"
TRACE_BINDING = DATA / "selected_primitiverowsexecution_or_dynamicdotdtracebinding.candidate.json"
DYNAMIC_HESSIAN = DATA / "selected_dynamictransferhessian_bselected_or_honestgalerkinc1_valuefill.candidate.json"
REPLAY_INDEPENDENCE = DATA / "selected_primitiverows_replayindependencelemma_or_sourceidentitybackfill.candidate.json"
PRERESIDUAL = DATA / "selected_preresidualweylvariationselectionlemma_or_honestquadraturesource.candidate.json"
KERNEL_ATTEMPT = DATA / "selected_preresidualvariation_hessiansourcekernel_attempt_or_actionaxiom.candidate.json"
SECTOR_ROWS = DATA / "selected_psm_c1_06_sectorrows_or_replayindependencecertificate.candidate.json"
UNPATCHED_FINAL = DATA / "selected_unpatchedfinitec1sourceidentity_or_honestindependentkernelexport.candidate.json"
LOCAL_PRINCIPLE = DATA / "selected_finitec1sourceidentityprincipleinsertion_or_selectedactionderivation.candidate.json"

STATUS = (
    "MTT_SELECTED_PUREWEYLROWS_SOURCEIDENTITYFRONTIER_BUILT_NUMERIC_BLOCKERS_"
    "RETIRED_FINAL_TWO_ROUTE_OPEN"
)
NEXT = "MTT_Selected_HonestKernelExport_RowSourceFill_or_SourceIdentityDerivationAttempt_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    pure_weyl = load(PURE_WEYL)
    hym_values = load(HYM_VALUES)
    trace_binding = load(TRACE_BINDING)
    dynamic_hessian = load(DYNAMIC_HESSIAN)
    replay = load(REPLAY_INDEPENDENCE)
    preresidual = load(PRERESIDUAL)
    kernel_attempt = load(KERNEL_ATTEMPT)
    sector_rows = load(SECTOR_ROWS)
    unpatched_final = load(UNPATCHED_FINAL)
    local_principle = load(LOCAL_PRINCIPLE)

    model_zero_modes_emitted = hym_values["what_closes_now"][
        "ordered_zero_mode_basis_ids_emitted"
    ]
    model_zero_modes_selected = hym_values["validator_result"][
        "selected_HYM_projector_values_promoted"
    ]
    dynamic_trace_bound = trace_binding["promotion_decision"][
        "dynamic_dotD_trace_binding_accepted"
    ]
    no_linear_algebra_obstruction = dynamic_hessian["promotion_gate"][
        "no_linear_algebra_obstruction"
    ]
    conditional_routeb_validates = sector_rows["closure_decision"][
        "conditional_RouteB_validator_passes"
    ]
    unpatched_routeb_validates = sector_rows["closure_decision"][
        "unpatched_RouteB_validator_passes"
    ]
    source_identity_unpatched = unpatched_final["closure_decision"][
        "source_identity_unpatched_derived"
    ]
    honest_export_emitted = unpatched_final["closure_decision"][
        "honest_kernel_export_emitted"
    ]
    patched_spine_closed = local_principle["patched_spine_closure_claimed"]

    reconciliation = {
        "schema": "MTTRetiredNumericBlockersReconciliationAfterPureWeylRows.v1",
        "status": "NUMERIC_AND_LINEAR_ALGEBRA_SUPPORT_MAXIMIZED_SOURCE_PROMOTION_OPEN",
        "pure_weyl_previous_status": pure_weyl["status"],
        "old_blocker_reconciliation": {
            "zero_mode_basis_values": {
                "model_active_values_emitted": model_zero_modes_emitted,
                "selected_HYM_source_promoted": model_zero_modes_selected,
                "remaining_interpretation": (
                    "The zero-mode numbers are not missing; their selected HYM/Strominger "
                    "source provenance is still missing."
                ),
            },
            "dynamic_dotD_trace_binding": {
                "accepted": dynamic_trace_bound,
                "remaining_interpretation": "Not an active blocker for this frontier.",
            },
            "finite_Hessian_C1_source_blocks": {
                "conditional_Gram": dynamic_hessian["conditional_dynamic_transfer_coordinate_packet"][
                    "Gram_A_transpose_A"
                ],
                "conditional_A_transpose_b": dynamic_hessian[
                    "conditional_dynamic_transfer_coordinate_packet"
                ]["A_transpose_b_conditional"],
                "conditional_deltaTheta": dynamic_hessian[
                    "conditional_dynamic_transfer_coordinate_packet"
                ]["deltaTheta_conditional_from_Gram_solve"],
                "no_linear_algebra_obstruction": no_linear_algebra_obstruction,
                "selected_Hessian_b_source_emitted": dynamic_hessian["promotion_gate"][
                    "selected_Hessian_bselected_emitted"
                ],
            },
            "primitive_C1_contractions": {
                "exact_72_rows_support_present": replay["what_closes_now"][
                    "validator_no_value_obstruction_after_source_ordering"
                ],
                "source_ordering_lemma_proved": replay["source_ordering_lemma_proved_now"],
                "pre_residual_normal_form_locked": preresidual["what_closes_now"][
                    "PSM_C1_02_RZ_RX_normal_form_locked"
                ],
                "route_A_validator_passes": preresidual["route_A_validator_passes"],
                "route_B_honest_quadrature_emitted": preresidual[
                    "route_B_honest_quadrature_emitted"
                ],
            },
            "sector_rows": {
                "conditional_full_RouteB_validator_passes": conditional_routeb_validates,
                "unpatched_RouteB_validator_passes": unpatched_routeb_validates,
            },
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(RECONCILIATION, reconciliation)

    source_reduction = {
        "schema": "MTTPureWeylRowsSourceIdentityReduction.v1",
        "status": "PURE_WEYL_ROWS_REDUCED_TO_SOURCE_IDENTITY_OR_HONEST_EXPORT",
        "patched_local_principle_boundary": {
            "patched_spine_closure_claimed": patched_spine_closed,
            "strict_110row_validator_passes_under_principle": local_principle[
                "what_closes_now"
            ]["strict_110row_source_id_validator_passes_under_principle"],
            "unpatched_SelectedFiniteC1SourceIdentityTheorem": False,
            "use_as_full_no_knob_proof": False,
        },
        "unpatched_requirements": {
            "derive_SelectedFiniteC1SourceIdentityPrinciple": source_identity_unpatched,
            "emit_honest_independent_110row_kernel_export": honest_export_emitted,
            "required_independent_rows": {
                "primitive_contractions": 72,
                "hessian_source": 2,
                "sector_matrices": 36,
                "total": 110,
            },
        },
        "pure_weyl_rows_unpatched_emitted": (
            source_identity_unpatched or honest_export_emitted
        ),
        "pure_weyl_rows_closed_under_local_principle_only": patched_spine_closed,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(SOURCE_REDUCTION, source_reduction)

    final_routes = {
        "schema": "MTTFinalTwoRouteAfterPureWeylRows.v1",
        "status": "TWO_LEGAL_FINISHING_ROUTES_OPEN",
        "route_A_source_identity_derivation": {
            "name": "derive SelectedFiniteC1SourceIdentityPrinciple",
            "current_status": source_identity_unpatched,
            "must_prove": [
                "selected pre-residual Phi_fin^C1 action functional",
                "same-source Hessian/b_selected ownership",
                "boundary/source vanishing before residual replay",
                "sector functor assembly and replay independence",
            ],
        },
        "route_B_honest_independent_kernel_export": {
            "name": "emit honest independent finite-C1 kernel table",
            "current_status": honest_export_emitted,
            "must_emit": [
                "72 primitive contraction rows",
                "2 Hessian/source rows",
                "36 sector response matrix rows",
                "exactness or numerical error certificates",
                "provenance independent of residual-projector replay and observed data",
            ],
        },
        "forbidden_closure_routes": [
            "use the local source identity principle as an unpatched proof",
            "use observed masses, CKM, PMNS, or Higgs values to select a row",
            "treat model-active zero-mode values as selected HYM/Strominger values without provenance",
            "treat conditional Hessian/b data as selected source rows without source identity",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(FINAL_ROUTES, final_routes)

    next_order = {
        "schema": "MTTNextExecutionOrderAfterSourceIdentityFrontier.v1",
        "status": "NEXT_ATTACK_SOURCE_IDENTITY_FIRST_HONEST_EXPORT_FALLBACK",
        "recommended_next": {
            "artifact": NEXT,
            "reason": (
                "The local principle demonstrates sufficiency, and the conditional Route-B "
                "validator demonstrates no row-value obstruction.  The shortest full-closure "
                "route is therefore to derive the finite-C1 source identity from selected MTT "
                "geometry; the fallback is an honest independent 110-row kernel export."
            ),
        },
        "execution_order": [
            "try to derive SelectedFiniteC1SourceIdentityPrinciple from selected action/variation",
            "if derivation fails, build independent 110-row export schema with exactness/error certificates",
            "only after one route closes, emit pure Weyl rows lambda_static*Z and lambda_static*X",
            "then rerun lambda representative/coexistence, physical matrices, and no-knob value rows",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(NEXT_ORDER, next_order)

    theorem_proved = (
        pure_weyl["closure_decision"]["pure_Weyl_rows_emitted"] is False
        and model_zero_modes_emitted is True
        and dynamic_trace_bound is True
        and no_linear_algebra_obstruction is True
        and conditional_routeb_validates is True
        and source_identity_unpatched is False
        and honest_export_emitted is False
    )

    candidate = {
        "candidate": "MTTSelectedPureWeylRowsSourceIdentityFrontierOrHonestKernelExport",
        "status": STATUS,
        "inputs": {
            "pure_weyl_gate": rel(PURE_WEYL),
            "hym_projector_zeromode_values": rel(HYM_VALUES),
            "dynamic_dotd_trace_binding": rel(TRACE_BINDING),
            "dynamic_transfer_hessian_bselected": rel(DYNAMIC_HESSIAN),
            "primitive_replay_independence": rel(REPLAY_INDEPENDENCE),
            "pre_residual_weyl_normal_form": rel(PRERESIDUAL),
            "pre_residual_variation_hessian_kernel_attempt": rel(KERNEL_ATTEMPT),
            "psm_c1_06_sector_rows": rel(SECTOR_ROWS),
            "unpatched_final_two_route_contract": rel(UNPATCHED_FINAL),
            "local_principle_insertion_boundary": rel(LOCAL_PRINCIPLE),
        },
        "output_packets": {
            "retired_numeric_blockers_reconciliation": rel(RECONCILIATION),
            "pure_weyl_rows_source_identity_reduction": rel(SOURCE_REDUCTION),
            "final_two_route_after_pure_weyl": rel(FINAL_ROUTES),
            "next_execution_order_after_source_identity_frontier": rel(NEXT_ORDER),
        },
        "theorem": {
            "name": "PureWeylRowsSourceIdentityFrontierReductionTheorem",
            "proved": theorem_proved,
            "statement": (
                "Combining the pure-Weyl row gate with the advanced finite-C1 source stack shows "
                "that the remaining obstruction is not discovery of zero modes, dotD trace binding, "
                "Hessian linear algebra, or primitive row values.  Those are available as model-active, "
                "conditional, or validator-ready support.  Unpatched promotion of pure Weyl rows now "
                "requires exactly one of two legal source completions: derive the SelectedFiniteC1SourceIdentityPrinciple "
                "from selected MTT geometry, or emit an honest independent 110-row finite-C1 kernel export."
            ),
        },
        "what_closes_now": {
            "old_zero_mode_hessian_primitive_wording_reconciled": True,
            "dynamic_dotD_trace_binding_retired_as_blocker": True,
            "numeric_and_linear_algebra_obstruction_retired": True,
            "local_principle_sufficiency_boundary_recorded": True,
            "final_two_legal_routes_identified": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "SelectedFiniteC1SourceIdentityPrinciple_unpatched": True,
            "honest_independent_110row_kernel_export": True,
            "pure_Weyl_rows_unpatched_source_promotion": True,
            "lambda_representative_or_coexistence_after_rows": True,
            "selected_second_order_physical_matrices": True,
            "accepted_Yukawa_CKM_PMNS_mass_value_rows": True,
            "true_SM_equivalence": True,
            "full_no_knob_closure": True,
        },
        "closure_decision": {
            "pure_Weyl_rows_emitted_unpatched": False,
            "patched_local_principle_suffices_conditionally": patched_spine_closed,
            "source_identity_unpatched_derived": source_identity_unpatched,
            "honest_kernel_export_emitted": honest_export_emitted,
            "selected_second_order_physical_matrices_promoted": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "previous_status": pure_weyl["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_PureWeylRows_SourceIdentityFrontier_or_HonestKernelExport_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": theorem_proved,
        "dynamic_dotD_trace_binding_retired_as_blocker": True,
        "numeric_and_linear_algebra_obstruction_retired": True,
        "source_identity_unpatched_derived": source_identity_unpatched,
        "honest_kernel_export_emitted": honest_export_emitted,
        "pure_Weyl_rows_emitted_unpatched": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected PureWeylRows SourceIdentityFrontier or HonestKernelExport v1

Status: `{STATUS}`.

The older blocker label was too broad.  Against the current corpus:

```text
model-active zero-mode values emitted       : {str(model_zero_modes_emitted).lower()}
selected HYM zero-mode provenance promoted : {str(model_zero_modes_selected).lower()}
dynamic dotD trace binding accepted        : {str(dynamic_trace_bound).lower()}
conditional Hessian/b linear algebra exact : {str(no_linear_algebra_obstruction).lower()}
conditional Route-B validator passes       : {str(conditional_routeb_validates).lower()}
unpatched source identity derived          : {str(source_identity_unpatched).lower()}
honest independent kernel export emitted   : {str(honest_export_emitted).lower()}
pure Weyl rows emitted unpatched           : false
full SM closure                            : false
```

So the next wall is now sharp: derive the
`SelectedFiniteC1SourceIdentityPrinciple` from selected MTT geometry, or export
an honest independent finite-C1 kernel table with 110 rows
(`72 + 2 + 36`) and exactness/error certificates.

The local source-identity principle remains valid as a patched sufficiency
boundary, but it is not an unpatched no-knob proof.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
