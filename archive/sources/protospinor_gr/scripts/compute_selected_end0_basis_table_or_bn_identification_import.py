from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"
Q79 = ROOT.parent / "mtt-q79-proof-repro"

ADJOINT_IMPORT = ROOT / "certificates" / "selected_hym_newton_galerkin_or_adjoint_functor_import_certificate.json"
END0_CERT = SM / "certificates" / "selected_end0_basis_differential_table_or_bn_identification_certificate.json"
END0_PACKET = SM / "candidate_data" / "selected_end0_basis_differential_table_or_bn_identification.candidate.json"
ORDERED_SOURCE = Q79 / "candidate_data" / "terminal_admissible_section_source" / "visible_rank2_l2_ordered_source.selected_under_section_principle.json"
AH_CERT = Q79 / "certificates" / "visible_rank2_l2_appell_humbert_automorphy_certificate.json"
AH_PACKET = Q79 / "candidate_data" / "visible_rank2_l2_appell_humbert_automorphy.candidate.json"
CECH_FIXTURE = Q79 / "candidate_data" / "visible_rank2_l2_pullback_cech_attempt.cohomology.json"

OUT_CERT = ROOT / "certificates" / "selected_end0_basis_table_or_bn_identification_import_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "selected_end0_basis_table_or_bn_identification_import.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "Selected_End0_Basis_Table_or_BN_Identification_Import_v1.md"

STATUS = "SELECTED_END0_BN_IDENTIFICATION_REJECTED_DIRECT_TABLE_REDUCED_TO_AH_EXT_LOCAL_FORMS"
NEXT = "MTT_Selected_End0_Direct_Differential_Table_From_AH_Ext_Forms_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    adjoint_import = load(ADJOINT_IMPORT)
    end0_cert = load(END0_CERT)
    end0 = load(END0_PACKET)
    ordered = load(ORDERED_SOURCE)
    ah_cert = load(AH_CERT)
    ah = load(AH_PACKET)
    cech = load(CECH_FIXTURE)

    path_a = end0["path_A_identify_existing_BN"]
    path_b = end0["path_B_direct_End0_table"]
    ah_checks = ah_cert["construction_checks"]
    ah_boolean_check_keys = [
        "c1_L_squared_square_is_minus_16_alpha1",
        "c1_matrix_matches_required_order",
        "c2_extension_target_is_plus_4_alpha1",
        "central_shared_circle_trivial",
        "cocycle_law_holds_on_generators_mod_2pi_i",
        "cocycle_law_holds_on_small_lattice_box_mod_2pi_i",
        "mixed_base_terms_zero",
        "trivial_semicharacter_allowed_because_c1_pairing_even",
    ]
    ah_numeric_checks_pass = (
        ah_checks["c1_pairing_g1_g2"] == 2
        and ah_checks["c1_pairing_g3_g4"] == -4
        and ah_checks["c1_pairing_g5_g6"] == 0
        and ah_checks["target_degrees"] == [2, -4, 0]
    )
    ah_cocycle_checks_pass = (
        all(ah_checks[key] is True for key in ah_boolean_check_keys) and ah_numeric_checks_pass
    )
    ordered_source = ordered["source"]
    pic0 = ordered["pic0_resolution"]
    cech_source = cech["source"]

    direct_table_attempt = {
        "attempted": True,
        "closed": False,
        "closed_inputs": {
            "ordered_rank2_source_selected_or_pic0_quotiented": ordered_source["selected_by_mtt"] is True,
            "ordered_c1_matrix_available": bool(ordered["target"]["c1_deck_matrix_order_g1_to_g6"]),
            "appell_humbert_multiplier_constructed": ah["selection_analysis"]["mathematical_automorphy_representative_constructed"] is True,
            "appell_humbert_cocycle_checks_pass": ah_cocycle_checks_pass,
            "h1_fixture_available": cech["reported_cohomology"]["h1"] == 8,
            "universal_end0_algebra_available": bool(path_b["emitted_universal_tables"]["ad_matrices"]),
            "iwasawa_structural_dbar_available": path_b["emitted_universal_tables"][
                "Iwasawa_left_invariant_dbar_rules"
            ]["dbar_e3"]
            == "e1 wedge e2",
        },
        "open_inputs": {
            "selected_ext_class_as_local_forms": cech_source["selected_by_mtt"] is False,
            "operator_layer_pic0_or_holonomy_resolution": pic0["scope"] == "ordered_chern_h1_curvature_layer_only",
            "selected_A_HYM_connection_terms": path_b["what_is_still_not_selected"][
                "selected_A_HYM_connection_terms"
            ],
            "selected_End0_local_basis": path_b["what_is_still_not_selected"]["selected_End0_local_basis"],
            "selected_Hodge_Lambda_table_for_equalradius_metric": path_b["what_is_still_not_selected"][
                "selected_Hodge_Lambda_table_for_equalradius_metric"
            ],
            "selected_quadrature_table": path_b["what_is_still_not_selected"]["selected_quadrature_table"],
            "selected_gauge_projector": path_b["what_is_still_not_selected"]["selected_gauge_projector"],
        },
        "reason": (
            "The selected ordered AH/Chern layer and explicit Appell-Humbert "
            "automorphy formula are available, but the operator-level direct "
            "End0 table needs local section/Ext forms, Pic0/holonomy resolution, "
            "connection terms, Hodge/Lambda, quadrature, and gauge projectors."
        ),
    }

    theorem = {
        "name": "SelectedEnd0BasisTableOrBNIdentificationImportNoGo",
        "proved": True,
        "closure_claimed": False,
        "statement": (
            "The dual End0 table gate is imported. The existing 27-mode B_N "
            "basis is rejected as a selected End_0(V_alpha) differential table "
            "because it is gerbe-twisted projective rather than ordinary adjoint "
            "bundle data. The rigorous route is the direct End0 table from "
            "selected AH/Appell-Humbert and Ext local forms. The selected ordered "
            "Chern/H1 layer and AH automorphy formula are present, but selected "
            "operator-level local forms, Pic0/holonomy resolution, HYM connection "
            "terms, Hodge/Lambda, quadrature, and gauge-projector tables remain open."
        ),
    }

    what_closes_now = {
        "dual_path_attempt_imported": end0_cert["both_paths_tested"] is True,
        "BN_identification_rejected_at_selected_End0_level": path_a["closed"] is False
        and path_a["result"] == "REJECTED_AS_SELECTED_END0_TABLE",
        "BN_retained_as_scaffold": path_a["support_retained"]["dimension_match_27"] is True
        and path_a["support_retained"]["zero_cluster_dimension_3"] is True,
        "direct_End0_universal_algebra_imported": end0["what_closes_now"][
            "direct_End0_universal_algebra_and_invariant_dbar_table_emitted"
        ],
        "ordered_AH_source_layer_available": ordered_source["selected_by_mtt"] is True,
        "explicit_AH_automorphy_formula_available": ah["selection_analysis"][
            "mathematical_automorphy_representative_constructed"
        ]
        is True,
        "direct_table_closed_inputs_classified": all(direct_table_attempt["closed_inputs"].values()),
        "target_fitting_excluded": (
            adjoint_import["what_closes_now"]["target_fitting_excluded"] is True
            and end0_cert["target_fitting_used"] is False
            and ordered_source["uses_observed_flavor_inputs"] is False
            and ordered_source["uses_benchmark_flavor_inputs"] is False
            and ah_cert["guardrails"]["uses_observed_flavor_data"] is False
            and ah_cert["guardrails"]["uses_benchmark_flavor_entries"] is False
        ),
    }

    what_remains_open = {
        "selected_Ext_class_as_local_forms": direct_table_attempt["open_inputs"]["selected_ext_class_as_local_forms"],
        "operator_layer_pic0_or_holonomy_resolution": direct_table_attempt["open_inputs"][
            "operator_layer_pic0_or_holonomy_resolution"
        ],
        "selected_A_HYM_connection_terms": direct_table_attempt["open_inputs"]["selected_A_HYM_connection_terms"],
        "selected_End0_local_basis": direct_table_attempt["open_inputs"]["selected_End0_local_basis"],
        "selected_Hodge_Lambda_quadrature_gauge_projector_tables": (
            direct_table_attempt["open_inputs"]["selected_Hodge_Lambda_table_for_equalradius_metric"]
            and direct_table_attempt["open_inputs"]["selected_quadrature_table"]
            and direct_table_attempt["open_inputs"]["selected_gauge_projector"]
        ),
        "selected_Newton_Galerkin_coefficients": end0["what_remains_open"]["selected_Newton_Galerkin_coefficients"],
    }

    packet = {
        "theorem": theorem,
        "imported_statuses": {
            "adjoint_import": adjoint_import["status"],
            "end0_dual_path": end0_cert["status"],
            "ordered_source": ordered["status"],
            "appell_humbert": ah_cert["status"],
            "cech_fixture": cech["status"],
        },
        "path_A_BN": path_a,
        "path_B_direct_End0": path_b,
        "direct_table_attempt": direct_table_attempt,
        "what_closes_now": what_closes_now,
        "what_remains_open": what_remains_open,
        "guardrails": {
            "does_not_identify_projective_BN_with_ordinary_End0": True,
            "does_not_use_unselected_cech_fixture_as_selected_ext_forms": True,
            "does_not_use_pic0_quotient_beyond_ordered_chern_h1_curvature_scope": True,
            "does_not_emit_selected_coefficients": True,
            "does_not_use_observed_or_benchmark_data": True,
        },
        "next_required_artifact": NEXT,
        "input_certificates": {
            "end0_dual_path": str(END0_CERT),
            "ordered_source": str(ORDERED_SOURCE),
            "appell_humbert": str(AH_CERT),
            "cech_fixture": str(CECH_FIXTURE),
        },
    }

    checks = {
        "previous_adjoint_gate_open_at_tables": adjoint_import["next_required_artifact"]
        == "MTT_Selected_End0_Basis_Differential_Table_or_BN_Identification_v1",
        "both_paths_tested": end0_cert["both_paths_tested"] is True,
        "path_A_not_closed": end0_cert["path_A_BN_identification_closed"] is False,
        "path_B_not_closed": end0_cert["path_B_direct_table_closed"] is False,
        "winner_path_B": end0_cert["winner_for_rigor"] == "Path B",
        "ordered_source_selected": ordered_source["selected_by_mtt"] is True,
        "pic0_scope_limited": pic0["scope"] == "ordered_chern_h1_curvature_layer_only",
        "ah_formula_constructed": ah["selection_analysis"]["mathematical_automorphy_representative_constructed"] is True,
        "cech_fixture_not_selected": cech_source["selected_by_mtt"] is False,
        "all_closes_true": all(what_closes_now.values()),
        "all_open_true": all(what_remains_open.values()),
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "selected_end0_basis_table_or_bn_identification_import",
        "status": STATUS,
        "theorem": theorem,
        "checks": checks,
        "what_closes_now": what_closes_now,
        "what_remains_open": what_remains_open,
        "next_required_artifact": NEXT,
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }

    note = f"""# Selected End0 Basis Table or BN Identification Import v1

## Result

The finite-table gate advances, but does not close.

Path A is rejected:

```text
B_N is a useful 27-mode gerbe-twisted projective scaffold.
B_N is not yet a selected ordinary End_0(V_alpha) differential table.
```

Path B is the rigorous route:

```text
build End_0(V_alpha) directly from selected AH/Appell-Humbert data,
selected Ext local forms, and selected HYM connection terms.
```

What closes now:

```text
ordered AH/Chern/H1 source layer is selected or Pic0-quotiented
explicit Appell-Humbert automorphy formula is available
universal End0 adjoint algebra and invariant Iwasawa dbar support are available
```

What remains open:

```text
selected Ext class as local forms
operator-level Pic0/holonomy resolution
selected A_HYM connection terms
selected End0 local basis
Hodge/Lambda, quadrature, and gauge-projector tables
```

Status:

```text
{STATUS}
```

Next:

```text
{NEXT}
```
"""

    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {STATUS}")


if __name__ == "__main__":
    main()
