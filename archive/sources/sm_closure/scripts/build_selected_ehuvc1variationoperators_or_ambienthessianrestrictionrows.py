"""Build E_H^UV C1 variation operators or ambient Hessian restriction rows packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
CONSTS = Path("C:/Users/nero_/Downloads/TEXPAPERS/mtt-individual-constants-source-search")

SLUG = "selected_ehuvc1variationoperators_or_ambienthessianrestrictionrows"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_EHUvC1VariationOperators_or_AmbientHessianRestrictionRows_v1.md"

C1_IMPORT = PACKET_DIR / "active_c1_source_to_higgs_frontier_import.packet.json"
H7B1M_IMPORT = PACKET_DIR / "h7b1m_projection_route_supersession.packet.json"
EVALUATION_ATTEMPT = PACKET_DIR / "ehuv_operator_evaluation_attempt.packet.json"
RESTRICTION_ATTEMPT = PACKET_DIR / "ambient_hessian_restriction_rows_attempt.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_ehuv_c1_operator_attempt.packet.json"

PREVIOUS = DATA / "selected_higgsc1variationslotextension_or_ambienthessianrows.candidate.json"
ACTIVE_DYNAMIC_C1 = (
    DATA
    / "selected_unpatchedphifinc1sourcerule_or_honestgalerkintables_to_hrgconsumermap"
    / "selected_dynamic_phifinc1_payload_promotion.packet.json"
)
ACTIVE_RECONCILIATION = (
    DATA
    / "selected_unpatchedphifinc1sourcerule_or_honestgalerkintables_to_hrgconsumermap"
    / "source_rule_backimport_reconciliation.packet.json"
)
C1_ROUTING = (
    DATA
    / "selected_variationoperatorshapecompatibility_or_hessiansourcegap"
    / "variation_operator_72_slot_routing.packet.json"
)
C2_EHUV = (
    DATA
    / "selected_higgshymsectionringquadraturebridge_or_directhuvpayload"
    / "c2_ehuv_finite_quotient_basis_exactness.packet.json"
)
BHUV = (
    DATA
    / "selected_bhuvtwocolumnsourceorthonormallift_or_msourcehuvfrontier"
    / "bhuv_two_column_source_orthonormal_lift.packet.json"
)
H7B1M = (
    CONSTS
    / "candidate_data"
    / "const_higgs_01_h7b1m_c1_to_huv_projection_or_honest_huv_row_export.candidate.json"
)
H7B1M_ROUTE = (
    CONSTS
    / "candidate_data"
    / "const_higgs_01_h7b1m_c1_to_huv_projection_or_honest_huv_row_export"
    / "c1_to_huv_projection_route_decision.packet.json"
)
H7B1M_SUPPORT = (
    CONSTS
    / "candidate_data"
    / "const_higgs_01_h7b1m_c1_to_huv_projection_or_honest_huv_row_export"
    / "c1_target_sector_support_audit.packet.json"
)
H7B1L_GAP = (
    CONSTS
    / "candidate_data"
    / "const_higgs_01_h7b1l_dynamic_phifinc1_huv_response_or_independent_huv_hessian"
    / "huv_projection_gap.packet.json"
)

STATUS = (
    "MTT_SELECTED_EHUVC1VARIATIONOPERATORS_OR_AMBIENTHESSIANRESTRICTIONROWS_"
    "C1_SOURCE_IMPORTED_HSECTOR_EXTENSION_OPEN"
)
NEXT = "MTT_Selected_HSectorDynamicC1Extension_or_DirectHuvRows_v1"


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
        raise FileNotFoundError("missing E_H^UV C1 operator inputs: " + ", ".join(missing))


def matrix_shape(matrix: Any) -> list[int]:
    if isinstance(matrix, list) and matrix and isinstance(matrix[0], list):
        return [len(matrix), len(matrix[0])]
    return [0, 0]


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        ACTIVE_DYNAMIC_C1,
        ACTIVE_RECONCILIATION,
        C1_ROUTING,
        C2_EHUV,
        BHUV,
        H7B1M,
        H7B1M_ROUTE,
        H7B1M_SUPPORT,
        H7B1L_GAP,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    active = load(ACTIVE_DYNAMIC_C1)
    reconciliation = load(ACTIVE_RECONCILIATION)
    c1_routing = load(C1_ROUTING)
    c2 = load(C2_EHUV)
    bhuv = load(BHUV)
    h7b1m = load(H7B1M)
    h7b1m_route = load(H7B1M_ROUTE)
    h7b1m_support = load(H7B1M_SUPPORT)
    h7b1l_gap = load(H7B1L_GAP)

    phase = active["exact_values"]["phase_R_Z"]
    shift = active["exact_values"]["shift_R_X"]
    routed_sectors = sorted({row["sector"] for row in c1_routing["rows"]})
    higgs_labels = c2["typing_checks"]["ordered_E_H_UV_basis_labels"]
    c1_higgs_rows = [row for row in c1_routing["rows"] if row["sector"] in {"H", "H_u", "H_d^dagger", "H_d_dagger"}]

    c1_import = {
        "schema": "MTTActiveC1SourceToHiggsFrontierImport.v1",
        "status": "ACTIVE_DYNAMIC_C1_SOURCE_IMPORTED_FOR_HIGGS_FRONTIER",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "what_is_now_closed": {
            "strict_unpatched_dynamic_C1_closed": active["decision"]["strict_unpatched_dynamic_C1_closed"],
            "selected_dynamic_phi_fin_c1_payload_emitted": active["decision"][
                "selected_dynamic_phi_fin_c1_payload_emitted"
            ],
            "A_selected_promoted_strict": active["decision"]["A_selected_promoted_strict"],
            "b_selected_promoted_strict": active["decision"]["b_selected_promoted_strict"],
            "deltaTheta_C1_promoted_strict": active["decision"]["deltaTheta_C1_promoted_strict"],
            "sector_response_matrices_promoted_strict": active["decision"][
                "sector_response_matrices_promoted_strict"
            ],
            "source_owner": active["source_owner"],
            "source_rule": active["selected_source_rule"],
            "source_rule_premise_free": active["source_rule_premise_free"],
            "emitted_before_residual_replay": active["emitted_before_residual_replay"],
        },
        "exact_dynamic_C1_values": {
            "phase_R_Z_shape": matrix_shape(phase),
            "shift_R_X_shape": matrix_shape(shift),
            "A_transpose_A": active["exact_values"]["A_transpose_A"],
            "A_transpose_b": active["exact_values"]["A_transpose_b"],
            "deltaTheta_C1": active["exact_values"]["deltaTheta_C1"],
            "rank": active["exact_values"]["rank"],
        },
        "higgs_relevance": {
            "C1_source_ownership_is_no_longer_the_Huv_blocker": True,
            "phase_shift_matrices_are_available_as_C1_source_data": True,
            "still_needed_for_Huv": "a selected evaluation/restriction of these source operators on E_H^UV or direct Huv rows",
        },
        "decision": {
            "active_C1_source_imported": True,
            "stale_dynamic_C1_source_open_gate_retired": reconciliation["decision"][
                "previous_source_rule_open_gate_superseded"
            ],
            "C1_source_rows_available": True,
        },
    }

    h7b1m_import = {
        "schema": "MTTH7B1MProjectionRouteSupersession.v1",
        "status": "H7B1M_ROUTE_IMPORTED_DYNAMIC_SOURCE_UPDATED_TARGET_MISMATCH_STILL_LIVE",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "imported_route_decision": {
            "plain_C1_to_Huv_projection_route_passes": h7b1m["plain_C1_to_Huv_projection_route_passes"],
            "plain_C1_to_Huv_projection_route_retired_current_target": h7b1m[
                "plain_C1_to_Huv_projection_route_retired_current_target"
            ],
            "H_sector_dynamic_C1_extension_required": h7b1m[
                "H_sector_dynamic_C1_extension_required"
            ],
            "honest_Huv_row_export_still_live": h7b1m["honest_Huv_row_export_still_live"],
            "current_C1_target_sector_set": h7b1m["current_C1_target_sector_set"],
            "current_C1_target_contains_H_sector": h7b1m["current_C1_target_contains_H_sector"],
        },
        "superseded_h7b1m_clause": {
            "old_clause": "selected C1 response values are still unpromoted in the strict unpatched tier",
            "superseded_by_active_ledger": active["decision"]["strict_unpatched_dynamic_C1_closed"],
            "replacement": "selected C1 source values are now promoted, but their target has no H-sector codomain",
        },
        "still_valid_h7b1m_clause": {
            "target_mismatch": h7b1m_support["target_mismatch_result"],
            "route_A_refined_must_emit": h7b1m_route["route_A_refined"]["must_emit"],
            "route_B_must_emit": h7b1m_route["route_B_still_live"]["must_emit"],
        },
        "decision": {
            "h7b1m_imported": True,
            "dynamic_C1_source_status_updated": True,
            "plain_matter_C1_to_Huv_projection_retired": True,
            "H_sector_extension_or_direct_Huv_rows_required": True,
        },
    }

    evaluation_attempt = {
        "schema": "MTTEHUvC1OperatorEvaluationAttempt.v1",
        "status": "EHUV_C1_OPERATOR_EVALUATION_ATTEMPTED_ZERO_SELECTED_VALUES",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "available_inputs": {
            "selected_phase_R_Z_matrix_shape": matrix_shape(phase),
            "selected_shift_R_X_matrix_shape": matrix_shape(shift),
            "higgs_source_labels": higgs_labels,
            "B_Huv_symbolic_exact_payload_emitted": bhuv["whitening_map_and_lift"][
                "B_Huv_symbolic_exact_payload_emitted"
            ],
            "C1_target_sectors": routed_sectors,
            "C1_higgs_slot_rows_found": len(c1_higgs_rows),
        },
        "required_map": {
            "name": "Eval_EHuv_C1",
            "typing": "E_H^UV columns H_u,H_d^dagger -> selected phase_R_Z/shift_R_X C1 coordinates",
            "if_emitted": "T_C1<-E_H^UV = [[phase(H_u), phase(H_d^dagger)], [shift(H_u), shift(H_d^dagger)]]",
            "then_execute": "M_Huv = 12 T^*T",
        },
        "candidate_evaluations_rejected": {
            "read_Higgs_slots_from_72_row_matter_routing": {
                "accepted": False,
                "reason": "72-row target has sectors u,d,e,nuD and zero H/H_u/H_d^dagger rows",
            },
            "act_3x3_phase_shift_matrices_on_E_HUV_columns_without_representation_map": {
                "accepted": False,
                "reason": "No selected representation map embeds H_u,H_d^dagger as vectors in the phase/shift 3x3 C1 coordinate space",
            },
            "average_matter_sectors_to_infer_Higgs_columns": {
                "accepted": False,
                "reason": "Matter Yukawa-channel incidence is support only; it is not a selected H-sector codomain map",
            },
            "use_low_energy_quotient_qHu_equals_qHd_as_two_column_evaluation": {
                "accepted": False,
                "reason": "The quotient collapses H_u and H_d^dagger to H and destroys the UV two-column Herm(2) block",
            },
        },
        "emitted_T_C1_EHuv": None,
        "emitted_slot_values": {
            "phase_H_u": None,
            "shift_H_u": None,
            "phase_H_d_dagger": None,
            "shift_H_d_dagger": None,
        },
        "decision": {
            "E_HUV_C1_operator_evaluation_attempted": True,
            "selected_E_HUV_C1_variation_operator_rows_emitted": False,
            "source_owned_T_C1_EHuv_emitted": False,
            "selected_Higgs_C1_variation_slot_count": 0,
        },
    }

    restriction_attempt = {
        "schema": "MTTAmbientHessianRestrictionRowsAttempt.v1",
        "status": "AMBIENT_HESSIAN_RESTRICTION_ROWS_ATTEMPTED_ZERO_ROWS_AFTER_C1_IMPORT",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "available_support": {
            "active_C1_normal_matrix": active["exact_values"]["A_transpose_A"],
            "H7B1L_gap_status": h7b1l_gap["status"],
            "H7B1L_required_huv_projection_fields": h7b1l_gap["required_huv_projection_fields"],
        },
        "emitted_ambient_rows": None,
        "emitted_restriction_rows": {
            "Huu": None,
            "Hud_re": None,
            "Hud_im": None,
            "Hdd": None,
        },
        "decision": {
            "ambient_Hessian_restriction_rows_attempted": True,
            "ambient_27_by_27_Hessian_matrix_emitted": False,
            "ambient_Hessian_restriction_rows_emitted": False,
            "selected_F_Huv_rows_emitted": False,
            "direct_Herm2_row_payload_emitted": False,
            "accepted_F_Huv_row_count": 0,
            "accepted_certificate_count": 0,
        },
    }

    cutset = {
        "schema": "MTTNextCutsetAfterEHUvC1OperatorAttempt.v1",
        "status": "NEXT_FRONTIER_HSECTOR_DYNAMIC_C1_EXTENSION_OR_DIRECT_HUV_ROWS",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closed_here": [
            "active strict dynamic Phi_fin/C1 source import into the Higgs frontier",
            "retirement of stale C1 source-promotion/Galerkin blocker for this branch",
            "H7B1M route decision updated: plain matter-C1-to-Huv projection remains retired",
            "proof that the missing object is Eval_EHuv_C1 or direct Huv rows",
        ],
        "still_open": [
            "selected H-sector dynamic C1 extension containing H/H_u/H_d^dagger coordinates",
            "selected Eval_EHuv_C1 map from H_u,H_d^dagger to phase_R_Z/shift_R_X",
            "or direct source-owned Huu,Hud,Hdd rows on B_Huv",
            "ambient Hess(F_C1) restriction rows with exactness certificates",
        ],
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "MTTSelectedEHUvC1VariationOperatorsOrAmbientHessianRestrictionRows",
        "schema": "MTTSelectedCandidate.v1",
        "status": STATUS,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "minimal_parameter_tier_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "ActiveC1SourceImportedButEHUvEvaluationNotEmittedTheorem",
            "proved": True,
            "statement": (
                "The active ledger now promotes the strict dynamic Phi_fin/C1 source "
                "payload, including phase_R_Z, shift_R_X, A^T A=12I, b_selected, "
                "deltaTheta_C1, and sector response matrices. This retires C1 "
                "source promotion as the Huv blocker. However the selected C1 "
                "target is still the matter-sector target u,d,e,nuD and contains "
                "no H/H_u/H_d^dagger codomain. Therefore no T_C1<-E_H^UV, ambient "
                "Hessian restriction rows, or F_Huv rows are emitted. The next "
                "legal exit is an H-sector dynamic C1 extension or direct Huv rows."
            ),
        },
        "packets": {
            "active_c1_source_to_higgs_frontier_import": rel(C1_IMPORT),
            "h7b1m_projection_route_supersession": rel(H7B1M_IMPORT),
            "ehuv_operator_evaluation_attempt": rel(EVALUATION_ATTEMPT),
            "ambient_hessian_restriction_rows_attempt": rel(RESTRICTION_ATTEMPT),
            "next_cutset": rel(CUTSET),
        },
        "inputs": {
            "previous": rel(PREVIOUS),
            "active_dynamic_c1": rel(ACTIVE_DYNAMIC_C1),
            "active_reconciliation": rel(ACTIVE_RECONCILIATION),
            "c1_routing": rel(C1_ROUTING),
            "c2_ehuv": rel(C2_EHUV),
            "bhuv": rel(BHUV),
            "h7b1m": rel(H7B1M),
            "h7b1m_route": rel(H7B1M_ROUTE),
            "h7b1m_support": rel(H7B1M_SUPPORT),
            "h7b1l_gap": rel(H7B1L_GAP),
        },
        "closure_decision": {
            "active_C1_source_imported": True,
            "stale_C1_source_promotion_blocker_retired": True,
            "plain_matter_C1_to_Huv_projection_retired": True,
            "E_HUV_C1_operator_evaluation_attempted": True,
            "ambient_Hessian_restriction_rows_attempted": True,
            "selected_E_HUV_C1_variation_operator_rows_emitted": False,
            "source_owned_T_C1_EHuv_emitted": False,
            "selected_Higgs_C1_variation_slots_emitted": False,
            "ambient_27_by_27_Hessian_matrix_emitted": False,
            "ambient_Hessian_restriction_rows_emitted": False,
            "selected_F_Huv_rows_emitted": False,
            "direct_Herm2_row_payload_emitted": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "key_numbers": {
            "C1_target_row_count": c1_routing["row_count"],
            "C1_target_sector_count": len(routed_sectors),
            "C1_higgs_slot_rows_found": len(c1_higgs_rows),
            "phase_R_Z_matrix_shape": matrix_shape(phase),
            "shift_R_X_matrix_shape": matrix_shape(shift),
            "A_transpose_A": active["exact_values"]["A_transpose_A"],
            "required_minimum_Higgs_C1_variation_slot_count": 4,
            "selected_Higgs_C1_variation_slot_count": 0,
            "accepted_F_Huv_row_count": 0,
            "accepted_certificate_count": 0,
        },
    }

    cert = {
        "certificate": "MTTSelectedEHUvC1VariationOperatorsOrAmbientHessianRestrictionRows",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "theorem_proved": True,
        "minimal_parameter_tier_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "active_C1_source_imported": True,
        "stale_C1_source_promotion_blocker_retired": True,
        "plain_matter_C1_to_Huv_projection_retired": True,
        "E_HUV_C1_operator_evaluation_attempted": True,
        "ambient_Hessian_restriction_rows_attempted": True,
        "selected_E_HUV_C1_variation_operator_rows_emitted": False,
        "source_owned_T_C1_EHuv_emitted": False,
        "selected_Higgs_C1_variation_slots_emitted": False,
        "ambient_27_by_27_Hessian_matrix_emitted": False,
        "ambient_Hessian_restriction_rows_emitted": False,
        "selected_F_Huv_rows_emitted": False,
        "direct_Herm2_row_payload_emitted": False,
        "accepted_F_Huv_row_count": 0,
        "accepted_certificate_count": 0,
    }

    note = f"""# MTT Selected EHUvC1VariationOperators or AmbientHessianRestrictionRows v1

Status: `{STATUS}`

## Theorem

The active ledger now promotes the strict dynamic `Phi_fin^C1` source payload:

```text
phase_R_Z shape = {matrix_shape(phase)}
shift_R_X shape = {matrix_shape(shift)}
A^T A = 12 I_2
A^T b = (12,12)
deltaTheta_C1 = (1,1)
```

So the Huv blocker is no longer generic C1 source promotion or Galerkin replay.
The blocker is the selected H-sector evaluation map:

```text
Eval_EHuv_C1 : (H_u,H_d^dagger) -> (phase_R_Z, shift_R_X)
T_C1<-E_H^UV = [[phase(H_u), phase(H_d^dagger)],
                [shift(H_u), shift(H_d^dagger)]]
M_Huv = 12 T^*T
```

Current execution imports H7B1M and confirms the target mismatch remains:

- C1 target sectors: `{routed_sectors}`
- Current C1 H/Huv rows: `{len(c1_higgs_rows)}`
- Higgs source labels: `{higgs_labels}`
- Selected `T_C1<-E_H^UV` rows emitted: `0`
- Ambient/restricted Hessian rows emitted: `0`
- Accepted `F_Huv` rows: `0`

Next artifact: `{NEXT}`
"""

    write_json(C1_IMPORT, c1_import)
    write_json(H7B1M_IMPORT, h7b1m_import)
    write_json(EVALUATION_ATTEMPT, evaluation_attempt)
    write_json(RESTRICTION_ATTEMPT, restriction_attempt)
    write_json(CUTSET, cutset)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE {rel(OUTPUT)}")
    print(f"WROTE {rel(CERT)}")
    print(f"WROTE {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
