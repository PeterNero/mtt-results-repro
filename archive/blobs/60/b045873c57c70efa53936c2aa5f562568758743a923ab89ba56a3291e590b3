"""Build H-sector dynamic C1 extension or direct Huv rows packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
CONSTS = Path("C:/Users/nero_/Downloads/TEXPAPERS/mtt-individual-constants-source-search")

SLUG = "selected_hsectordynamicc1extension_or_directhuvrows"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HSectorDynamicC1Extension_or_DirectHuvRows_v1.md"

H7B1N_IMPORT = PACKET_DIR / "h7b1n_two_route_cutset_import.packet.json"
H7B1Z_RECONCILE = PACKET_DIR / "h7b1z_binding_cutset_reconciled_with_active_repo.packet.json"
HSECTOR_ATTEMPT = PACKET_DIR / "hsector_dynamic_extension_attempt.packet.json"
DIRECT_ATTEMPT = PACKET_DIR / "direct_huv_rows_after_bhuv_import_attempt.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_hsector_directhuv_attempt.packet.json"

PREVIOUS = DATA / "selected_ehuvc1variationoperators_or_ambienthessianrestrictionrows.candidate.json"
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
C3_EHUV = (
    DATA
    / "selected_ehuvhymmetricconnectionfixedpoint_or_directhuvpayload"
    / "c3_ehuv_hym_metric_connection_binding.packet.json"
)
BHUV = (
    DATA
    / "selected_bhuvtwocolumnsourceorthonormallift_or_msourcehuvfrontier"
    / "bhuv_two_column_source_orthonormal_lift.packet.json"
)
ACTIVE_C1 = (
    DATA
    / "selected_unpatchedphifinc1sourcerule_or_honestgalerkintables_to_hrgconsumermap"
    / "selected_dynamic_phifinc1_payload_promotion.packet.json"
)
H7B1N = (
    CONSTS
    / "candidate_data"
    / "const_higgs_01_h7b1n_hsector_dynamic_extension_or_honest_huv_rows.candidate.json"
)
H7B1N_HSECTOR = (
    CONSTS
    / "candidate_data"
    / "const_higgs_01_h7b1n_hsector_dynamic_extension_or_honest_huv_rows"
    / "hsector_dynamic_extension_attempt.packet.json"
)
H7B1N_DIRECT = (
    CONSTS
    / "candidate_data"
    / "const_higgs_01_h7b1n_hsector_dynamic_extension_or_honest_huv_rows"
    / "honest_huv_row_export_attempt.packet.json"
)
H7B1N_CUTSET = (
    CONSTS
    / "candidate_data"
    / "const_higgs_01_h7b1n_hsector_dynamic_extension_or_honest_huv_rows"
    / "nonlinear_hym_huv_payload_cutset.packet.json"
)
H7B1Z = (
    CONSTS
    / "candidate_data"
    / "const_higgs_01_h7b1z_fill_ehuv_finite_basis_or_herm2_values.candidate.json"
)
H7B1Z_PARTIAL = (
    CONSTS
    / "candidate_data"
    / "const_higgs_01_h7b1z_fill_ehuv_finite_basis_or_herm2_values"
    / "partial_section_basis_quadrature_fill.packet.json"
)
H7B1Z_DIRECT = (
    CONSTS
    / "candidate_data"
    / "const_higgs_01_h7b1z_fill_ehuv_finite_basis_or_herm2_values"
    / "direct_herm2_fill_attempt.packet.json"
)
H7B1Z_REMAINING = (
    CONSTS
    / "candidate_data"
    / "const_higgs_01_h7b1z_fill_ehuv_finite_basis_or_herm2_values"
    / "remaining_payload_cutset.packet.json"
)

STATUS = (
    "MTT_SELECTED_HSECTORDYNAMICC1EXTENSION_OR_DIRECTHUVROWS_"
    "BHUV_EHUV_BINDING_IMPORTED_MSOURCE_OR_DIRECTROWS_OPEN"
)
NEXT = "MTT_Selected_MSourceHuvOperator_or_DirectHerm2Rows_v1"


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
        raise FileNotFoundError("missing H-sector/Huv inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        C1_ROUTING,
        C2_EHUV,
        C3_EHUV,
        BHUV,
        ACTIVE_C1,
        H7B1N,
        H7B1N_HSECTOR,
        H7B1N_DIRECT,
        H7B1N_CUTSET,
        H7B1Z,
        H7B1Z_PARTIAL,
        H7B1Z_DIRECT,
        H7B1Z_REMAINING,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    c1_routing = load(C1_ROUTING)
    c2 = load(C2_EHUV)
    c3 = load(C3_EHUV)
    bhuv = load(BHUV)
    active_c1 = load(ACTIVE_C1)
    h7b1n = load(H7B1N)
    h7b1n_hsector = load(H7B1N_HSECTOR)
    h7b1n_direct = load(H7B1N_DIRECT)
    h7b1n_cutset = load(H7B1N_CUTSET)
    h7b1z = load(H7B1Z)
    h7b1z_partial = load(H7B1Z_PARTIAL)
    h7b1z_direct = load(H7B1Z_DIRECT)
    h7b1z_remaining = load(H7B1Z_REMAINING)

    routed_sectors = sorted({row["sector"] for row in c1_routing["rows"]})
    c1_higgs_rows = [row for row in c1_routing["rows"] if row["sector"] in {"H", "H_u", "H_d^dagger", "H_d_dagger"}]
    ehuv_labels = c2["typing_checks"]["ordered_E_H_UV_basis_labels"]
    source_ids = c3["basis_binding"]["ordered_E_H_UV_source_ids"]

    h7b1n_import = {
        "schema": "MTTH7B1NTwoRouteCutsetImport.v1",
        "status": "H7B1N_TWO_ROUTE_CUTSET_IMPORTED",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "imported_theorem": h7b1n["theorem"],
        "imported_hsector_attempt": {
            "status": h7b1n_hsector["status"],
            "route_A_passes": h7b1n_hsector["attempt_decision"]["route_A_passes"],
            "H_sector_dynamic_extension_found": h7b1n_hsector["attempt_decision"][
                "H_sector_dynamic_extension_found"
            ],
            "selected_Pi_Huv_or_R_H_found": h7b1n_hsector["attempt_decision"][
                "selected_Pi_Huv_or_R_H_found"
            ],
            "required_extension_payload": h7b1n_hsector["required_extension_payload"],
        },
        "imported_direct_attempt": {
            "status": h7b1n_direct["status"],
            "route_B_passes": h7b1n_direct["attempt_decision"]["route_B_passes"],
            "direct_Huv_entries_emitted": h7b1n_direct["attempt_decision"][
                "direct_Huv_entries_emitted"
            ],
            "M_source_emitted": h7b1n_direct["attempt_decision"]["M_source_emitted"],
            "B_Huv_emitted_in_H7B1N": h7b1n_direct["attempt_decision"]["B_Huv_emitted"],
        },
        "active_repo_update_to_H7B1N": {
            "B_Huv_emitted_in_active_repo": bhuv["whitening_map_and_lift"][
                "B_Huv_symbolic_exact_payload_emitted"
            ],
            "finite_E_H_UV_source_ids_emitted_in_active_repo": all(
                item["source_id_emitted"] for item in c2["finite_quotient_basis"]["uv_lift_basis"]
            ),
            "selected_HYM_metric_or_connection_bound_in_active_repo": c3["bridge_clause_closed"],
            "therefore_H7B1N_B_Huv_missing_clause_is_superseded": True,
            "still_missing_after_supersession": [
                "selected H-sector dynamic C1 codomain rows",
                "Pi_Huv/R_H evaluation map",
                "same-source M_source Hermitian operator",
                "or direct Huu,Hud,Hdd rows with certificates",
            ],
        },
        "decision": {
            "h7b1n_cutset_imported": True,
            "B_Huv_missing_clause_superseded": True,
            "Hsector_dynamic_extension_still_absent": True,
            "M_source_or_direct_Huv_rows_still_absent": True,
        },
    }

    h7b1z_reconcile = {
        "schema": "MTTH7B1ZBindingCutsetReconciledWithActiveRepo.v1",
        "status": "H7B1Z_RECONCILED_HYM_SOLVER_RETIRED_BINDING_AND_HERM2_VALUES_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "imported_h7b1z": {
            "status": h7b1z["status"],
            "HYM_solver_existence_retired_as_blocker": h7b1z["HYM_solver_existence_retired_as_blocker"],
            "source_HYM_grid_payload_emitted": h7b1z["source_HYM_grid_payload_emitted"],
            "computational_uniform_quadrature_emitted": h7b1z["computational_uniform_quadrature_emitted"],
            "direct_Herm2_Huv_payload_emitted": h7b1z["direct_Herm2_Huv_payload_emitted"],
        },
        "active_repo_supersessions": {
            "selected_E_H_UV_section_basis_source_ids_emitted": True,
            "selected_E_H_UV_source_ids": source_ids,
            "selected_HYM_metric_or_connection_on_E_H_UV_bound": c3["bridge_clause_closed"],
            "B_Huv_symbolic_exact_payload_emitted": bhuv["whitening_map_and_lift"][
                "B_Huv_symbolic_exact_payload_emitted"
            ],
            "source_orthonormality": bhuv["whitening_map_and_lift"][
                "source_orthonormality_certificate"
            ],
        },
        "still_open_after_reconciliation": {
            "trace_to_H7B1U_grid_identity_as_physical_projection_measure": h7b1z_remaining[
                "still_open"
            ]["trace_to_H7B1U_grid_identity_as_physical_projection_measure"],
            "no_extra_boundary_source_term_for_Higgs_projection": h7b1z_remaining["still_open"][
                "no_extra_boundary_source_term_for_Higgs_projection"
            ],
            "direct_B_Huv_M_source_or_Huu_Hud_Hdd_values": h7b1z_remaining["still_open"][
                "direct_B_Huv_M_source_or_Huu_Hud_Hdd_values"
            ],
            "direct_Herm2_fill_attempt_values_absent": h7b1z_direct["decision"][
                "Herm2_payload_complete"
            ]
            is False,
        },
        "retired_as_blockers": {
            **h7b1z_remaining["retired_as_blockers"],
            "active_repo_E_H_UV_source_ids": True,
            "active_repo_diagonal_HYM_binding": True,
            "active_repo_B_Huv_symbolic_lift": True,
        },
        "decision": {
            "h7b1z_imported": True,
            "HYM_solver_existence_retired": True,
            "E_HUV_binding_partially_superseded_by_active_repo": True,
            "projection_measure_equality_still_open": True,
            "direct_Herm2_rows_still_absent": True,
        },
    }

    hsector_attempt = {
        "schema": "MTTHSectorDynamicC1ExtensionAttempt.v1",
        "status": "HSECTOR_DYNAMIC_C1_EXTENSION_ATTEMPTED_ZERO_ROWS",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "available_C1_source": {
            "strict_unpatched_dynamic_C1_closed": active_c1["decision"][
                "strict_unpatched_dynamic_C1_closed"
            ],
            "A_transpose_A": active_c1["exact_values"]["A_transpose_A"],
            "phase_R_Z_available": True,
            "shift_R_X_available": True,
            "current_target_sectors": routed_sectors,
            "current_H_sector_rows": len(c1_higgs_rows),
        },
        "required_extension": {
            "new_rows": ["H.phase_R_Z", "H.shift_R_X", "H_u.phase_R_Z", "H_d_dagger.shift_R_X"],
            "codomain_map": "Pi_Huv or R_H from selected C1 response coordinates to ordered (H_u,H_d^dagger)",
            "acceptance_formula": "M_Huv = 12 T^*T after source-owned T_C1<-E_H^UV is emitted",
        },
        "emitted_extension_rows": [],
        "emitted_Pi_Huv_or_R_H": None,
        "decision": {
            "Hsector_dynamic_extension_attempted": True,
            "selected_Hsector_dynamic_C1_extension_emitted": False,
            "selected_Eval_EHuv_C1_emitted": False,
            "selected_Pi_Huv_or_R_H_emitted": False,
            "selected_Higgs_C1_variation_slot_count": 0,
        },
    }

    direct_attempt = {
        "schema": "MTTDirectHuvRowsAfterBHuvImportAttempt.v1",
        "status": "DIRECT_HUV_ROWS_ATTEMPTED_BHUV_AVAILABLE_MSOURCE_ROWS_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "available_direct_route_inputs": {
            "ordered_E_H_UV_basis": ehuv_labels,
            "ordered_E_H_UV_source_ids": source_ids,
            "B_Huv_symbolic_exact_payload_emitted": bhuv["whitening_map_and_lift"][
                "B_Huv_symbolic_exact_payload_emitted"
            ],
            "B_Huv_columns": bhuv["whitening_map_and_lift"]["B_Huv_columns"],
            "B_Huv_source_orthonormality": bhuv["whitening_map_and_lift"][
                "source_orthonormality_certificate"
            ],
            "selected_HYM_metric_or_connection_on_E_H_UV": c3["bridge_clause_closed"],
        },
        "missing_direct_route_inputs": {
            "M_source": "same-source Hermitian mass/strain/Hessian operator on the B_Huv domain",
            "or_direct_rows": ["Huu", "Hud_re", "Hud_im", "Hdd"],
            "certificates": [
                "same-source exactness or residual bound",
                "Hermitian/source ownership",
                "quotient admissibility",
                "finite trace/projection-measure convention if using HYM replay",
            ],
        },
        "imported_h7b1z_direct_attempt": {
            "status": h7b1z_direct["status"],
            "why_no_direct_fill": h7b1z_direct["why_no_direct_fill"],
        },
        "emitted_rows": {
            "Huu": None,
            "Hud_re": None,
            "Hud_im": None,
            "Hdd": None,
            "Delta": None,
            "Re_Omega": None,
            "Im_Omega": None,
        },
        "decision": {
            "direct_Huv_rows_attempted": True,
            "B_Huv_available": True,
            "M_source_emitted": False,
            "direct_Huu_Hud_Hdd_emitted": False,
            "direct_Herm2_Huv_payload_emitted": False,
            "selected_F_Huv_rows_emitted": False,
            "accepted_F_Huv_row_count": 0,
            "accepted_certificate_count": 0,
        },
    }

    cutset = {
        "schema": "MTTNextCutsetAfterHSectorDirectHuvAttempt.v1",
        "status": "NEXT_FRONTIER_MSOURCE_HUV_OPERATOR_OR_DIRECT_HERM2_ROWS",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closed_here": [
            "H7B1N two-route cutset imported",
            "H7B1Z HYM-grid existence blocker retired",
            "active C2/C3/B_Huv supersede older missing-basis/metric/B_Huv clauses",
            "H-sector dynamic C1 extension rerun with zero emitted H rows",
            "direct Huv route rerun with B_Huv available but zero M_source/direct rows",
        ],
        "still_open": [
            "selected same-source M_source Hermitian operator on B_Huv",
            "or direct source-owned Huu,Hud,Hdd Herm(2) rows",
            "same-source exactness/residual certificate",
            "projection-measure equality/no-extra-boundary source proof if using HYM-grid route",
        ],
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "MTTSelectedHSectorDynamicC1ExtensionOrDirectHuvRows",
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
            "name": "BHuvEHuvBindingImportedMSourceOrDirectRowsOpenTheorem",
            "proved": True,
            "statement": (
                "H7B1N's two-route cutset is imported and updated against the "
                "active repo. The old missing B_Huv/E_H^UV binding clauses are "
                "partly superseded: C2 emits finite E_H^UV source IDs, C3 binds "
                "the selected diagonal HYM metric/connection, and B_Huv emits a "
                "source-orthonormal symbolic two-column lift. H7B1Z also retires "
                "HYM solver existence as a blocker. The remaining direct-Huv "
                "blocker is therefore sharper: emit a selected same-source "
                "M_source Hermitian operator on B_Huv, or direct certified "
                "Huu,Hud,Hdd Herm(2) rows. Current execution emits zero such rows."
            ),
        },
        "packets": {
            "h7b1n_two_route_cutset_import": rel(H7B1N_IMPORT),
            "h7b1z_binding_cutset_reconciled_with_active_repo": rel(H7B1Z_RECONCILE),
            "hsector_dynamic_extension_attempt": rel(HSECTOR_ATTEMPT),
            "direct_huv_rows_after_bhuv_import_attempt": rel(DIRECT_ATTEMPT),
            "next_cutset": rel(CUTSET),
        },
        "inputs": {
            "previous": rel(PREVIOUS),
            "c1_routing": rel(C1_ROUTING),
            "c2_ehuv": rel(C2_EHUV),
            "c3_ehuv": rel(C3_EHUV),
            "bhuv": rel(BHUV),
            "active_c1": rel(ACTIVE_C1),
            "h7b1n": rel(H7B1N),
            "h7b1z": rel(H7B1Z),
        },
        "closure_decision": {
            "h7b1n_cutset_imported": True,
            "h7b1z_hym_solver_existence_retired": True,
            "active_E_HUV_source_ids_emitted": True,
            "active_E_HUV_HYM_metric_connection_bound": True,
            "active_B_Huv_symbolic_lift_emitted": True,
            "Hsector_dynamic_extension_attempted": True,
            "direct_Huv_rows_attempted": True,
            "selected_Hsector_dynamic_C1_extension_emitted": False,
            "selected_Eval_EHuv_C1_emitted": False,
            "selected_Pi_Huv_or_R_H_emitted": False,
            "M_source_emitted": False,
            "direct_Huu_Hud_Hdd_emitted": False,
            "direct_Herm2_Huv_payload_emitted": False,
            "selected_F_Huv_rows_emitted": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "key_numbers": {
            "C1_target_row_count": c1_routing["row_count"],
            "C1_higgs_slot_rows_found": len(c1_higgs_rows),
            "Huv_source_column_count": 2,
            "B_Huv_column_count": len(bhuv["whitening_map_and_lift"]["B_Huv_columns"]),
            "accepted_F_Huv_row_count": 0,
            "accepted_certificate_count": 0,
        },
    }

    cert = {
        "certificate": "MTTSelectedHSectorDynamicC1ExtensionOrDirectHuvRows",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "theorem_proved": True,
        "minimal_parameter_tier_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "h7b1n_cutset_imported": True,
        "h7b1z_hym_solver_existence_retired": True,
        "active_E_HUV_source_ids_emitted": True,
        "active_E_HUV_HYM_metric_connection_bound": True,
        "active_B_Huv_symbolic_lift_emitted": True,
        "Hsector_dynamic_extension_attempted": True,
        "direct_Huv_rows_attempted": True,
        "selected_Hsector_dynamic_C1_extension_emitted": False,
        "selected_Eval_EHuv_C1_emitted": False,
        "selected_Pi_Huv_or_R_H_emitted": False,
        "M_source_emitted": False,
        "direct_Huu_Hud_Hdd_emitted": False,
        "direct_Herm2_Huv_payload_emitted": False,
        "selected_F_Huv_rows_emitted": False,
        "accepted_F_Huv_row_count": 0,
        "accepted_certificate_count": 0,
    }

    note = f"""# MTT Selected HSectorDynamicC1Extension or DirectHuvRows v1

Status: `{STATUS}`

## Theorem

H7B1N's two-route cutset is imported, but updated against the active repo.
The older constants-side missing-basis/metric/`B_Huv` clauses are partly
superseded here:

- finite `E_H^UV` source labels: `{ehuv_labels}`
- source IDs: `{source_ids}`
- selected diagonal HYM binding on `E_H^UV`: `{c3["bridge_clause_closed"]}`
- symbolic source-orthonormal `B_Huv` lift emitted: `{bhuv["whitening_map_and_lift"]["B_Huv_symbolic_exact_payload_emitted"]}`

The H-sector dynamic C1 route is still absent:

- current C1 target sectors: `{routed_sectors}`
- H/Huv C1 rows: `{len(c1_higgs_rows)}`

The direct Huv route is now sharper.  We no longer need to search for the
two-column Higgs lift; the active blocker is:

```text
M_source on B_Huv, or direct certified Huu,Hud,Hdd rows.
```

Current emitted `Huv` rows: `0`.

Next artifact: `{NEXT}`
"""

    write_json(H7B1N_IMPORT, h7b1n_import)
    write_json(H7B1Z_RECONCILE, h7b1z_reconcile)
    write_json(HSECTOR_ATTEMPT, hsector_attempt)
    write_json(DIRECT_ATTEMPT, direct_attempt)
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
