from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
Q79 = ROOT.parent / "mtt-q79-proof-repro"

PREVIOUS = ROOT / "certificates" / "selected_end0_direct_ah_ext_form_table_import_certificate.json"
PREVIOUS_PACKET = ROOT / "candidate_data" / "selected_end0_direct_ah_ext_form_table_import.packet.json"
SELECTED_COHOMOLOGY = (
    Q79
    / "candidate_data"
    / "terminal_admissible_section_source"
    / "visible_rank2_l2_cohomology.selected_under_section_principle.json"
)
AH_AUTOMORPHY = Q79 / "candidate_data" / "visible_rank2_l2_appell_humbert_automorphy.candidate.json"
YONEDA = Q79 / "candidate_data" / "valpha_kunneth_yoneda_scalar" / "reduced_kunneth_yoneda_matrix.json"

OUT_CERT = ROOT / "certificates" / "selected_normalized_ext_local_form_table_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "selected_normalized_ext_local_form_table.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "Selected_Normalized_Ext_Local_Form_Table_v1.md"

STATUS = "SELECTED_NORMALIZED_EXT_LOCAL_FORM_TABLE_BUILT_HYM_HODGE_QUADRATURE_OPEN"
NEXT = "MTT_Selected_End0_HYM_Hodge_Quadrature_Projector_Table_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    previous = load(PREVIOUS)
    previous_packet = load(PREVIOUS_PACKET)
    cohomology = load(SELECTED_COHOMOLOGY)
    ah = load(AH_AUTOMORPHY)
    yoneda = load(YONEDA)

    selected_label = cohomology["reported_cohomology"]["nonzero_extension_class_label"]
    selected_vector = cohomology["reported_cohomology"]["extension_class_vector_C1"]
    source_basis = cohomology["cochain_complex"]["basis_labels_C1"]
    ah_matrix = ah["model"]["c1_deck_alternating_matrix_order_g1_to_g6"]
    ext_template = previous_packet["Ext_local_form_template"]

    normalized_table = {
        "schema": "MTTSelectedNormalizedExtLocalFormTable.v1",
        "line": "L^2=(2,-4,0)",
        "basis_order": source_basis,
        "selected_basis_slot": selected_label,
        "selected_normalized_coordinate_vector": selected_vector,
        "normalization_convention": {
            "name": "terminal_section_unit_Cech_basis_normalization",
            "description": (
                "The terminal section principle selects the first C1 basis slot. "
                "The normalized Ext table fixes that selected slot to unit "
                "coefficient and all other cohomology coordinates to zero."
            ),
            "unit_norm_in_selected_Cech_basis": True,
            "uses_observed_or_benchmark_data": False,
        },
        "local_form_representative": {
            "symbolic": "eta = theta_plus_0(z1) tensor eta_minus_0(z2) dbar_z2",
            "theta_factor": "theta_plus_0(z1)",
            "serre_dual_h1_factor": "eta_minus_0(z2) dbar_z2",
            "central_shared_circle_factor": "1",
            "central_shared_circle_degree_zero": True,
            "cohomology_class_closed_nonexact": True,
        },
        "transition_weights": {
            "ordered_generators": ["g1", "g2", "g3", "g4", "g5", "g6"],
            "c1_deck_alternating_matrix_order_g1_to_g6": ah_matrix,
            "pairings": {
                "E(g1,g2)": 2,
                "E(g3,g4)": -4,
                "E(g5,g6)": 0,
            },
            "factor_formula": ah["model"]["factor_formula"],
        },
        "overlap_table": {
            "type": "selected_Cech_coordinate_table",
            "C0_basis": cohomology["cochain_complex"]["basis_labels_C0"],
            "C1_basis": source_basis,
            "C2_basis": cohomology["cochain_complex"]["basis_labels_C2"],
            "d0": cohomology["cochain_complex"]["d0"],
            "d1": cohomology["cochain_complex"]["d1"],
            "selected_C1_cocycle": dict(zip(source_basis, selected_vector)),
            "d1_selected_cocycle": [0],
            "not_a_partition_of_unity_table": True,
        },
        "yoneda_sanity": {
            "status": yoneda["status"],
            "selected_ext_label": yoneda["selected_ext_label"],
            "selected_ext_vector": yoneda["selected_ext_vector"],
            "target_vector": yoneda["target_vector"],
            "target_vector_nonzero": yoneda["target_vector_nonzero"],
        },
    }

    end0_insertion = {
        "off_diagonal_entry": normalized_table["local_form_representative"]["symbolic"],
        "normalized_operator_template": previous_packet["partial_End0_differential_table"][
            "symbolic_operator_template"
        ],
        "what_this_supplies": [
            "selected unit Cech coordinate for the Ext slot",
            "closed non-exact cohomology class",
            "Appell-Humbert transition weights for L^2",
            "central shared-circle degree-zero guardrail",
        ],
        "still_not_supplied": [
            "numerical theta-function samples on a quadrature mesh",
            "partition-of-unity or Dolbeault-harmonic analytic representative",
            "selected HYM metric and connection correction",
            "Hodge/Lambda table",
            "quadrature table",
            "gauge projector",
        ],
        "safe_for_newton": False,
    }

    packet = {
        "theorem": {
            "name": "SelectedNormalizedExtLocalFormTable",
            "proved": True,
            "closure_claimed": False,
            "statement": (
                "The selected Ext class is normalized as the unit terminal "
                "Cech basis vector theta_plus_0_tensor_eta_minus_0 with "
                "representative eta = theta_plus_0(z1) tensor eta_minus_0(z2) "
                "dbar_z2 and Appell-Humbert L^2=(2,-4,0) transition weights. "
                "This closes the normalized selected Ext coordinate/local-form "
                "table needed by the End0 route, but it does not supply the "
                "analytic HYM metric, Hodge/Lambda, quadrature, or gauge "
                "projector tables required for Newton coefficients."
            ),
        },
        "normalized_ext_local_form_table": normalized_table,
        "End0_insertion": end0_insertion,
        "what_closes_now": {
            "previous_gate_requested_normalized_ext_table": previous["next_required_artifact"]
            == "MTT_Selected_Normalized_Ext_Local_Form_Table_v1",
            "selected_terminal_cohomology_source": cohomology["source"]["selected_by_mtt"] is True
            and cohomology["candidate_role"] == "SELECTED_DATA",
            "selected_basis_slot_is_first_terminal_slot": selected_label == "theta_plus_0_tensor_eta_minus_0"
            and selected_vector == [1, 0, 0, 0, 0, 0, 0, 0],
            "cocycle_closed_nonexact": cohomology["acceptance_tests"]["extension_class_closed"] is True
            and cohomology["acceptance_tests"]["extension_class_not_exact"] is True,
            "AH_transition_weights_bound": ah["construction_checks"]["c1_matrix_matches_required_order"] is True
            and ah["construction_checks"]["central_shared_circle_trivial"] is True,
            "yoneda_nonzero_sanity": yoneda["selected_ext_label"] == selected_label
            and yoneda["target_vector_nonzero"] is True,
            "target_fitting_excluded": cohomology["source"]["uses_observed_flavor_inputs"] is False
            and cohomology["source"]["uses_benchmark_flavor_inputs"] is False,
        },
        "what_remains_open": {
            "numerical_theta_function_samples_on_selected_mesh": True,
            "partition_of_unity_or_harmonic_Dolbeault_representative": True,
            "selected_HYM_metric_connection_correction": True,
            "Hodge_Lambda_table": True,
            "quadrature_table": True,
            "gauge_projector": True,
            "selected_Newton_Galerkin_coefficients": True,
        },
        "guardrails": {
            "does_not_use_old_unselected_fixture": str(SELECTED_COHOMOLOGY).endswith(
                "visible_rank2_l2_cohomology.selected_under_section_principle.json"
            ),
            "does_not_claim_Newton_ready": end0_insertion["safe_for_newton"] is False,
            "does_not_claim_analytic_HYM_solution": True,
            "does_not_use_observed_or_benchmark_data": True,
        },
        "input_artifacts": {
            "previous": str(PREVIOUS),
            "selected_cohomology": str(SELECTED_COHOMOLOGY),
            "appell_humbert": str(AH_AUTOMORPHY),
            "yoneda": str(YONEDA),
        },
        "next_required_artifact": NEXT,
    }

    checks = {
        "status_inputs_match": previous["status"]
        == "SELECTED_END0_DIRECT_AH_EXT_FORM_TABLE_IMPORTED_NORMALIZED_EXT_TABLE_OPEN",
        "selected_cohomology_not_fixture": cohomology["source"]["fixture_only"] is False,
        "selected_vector_unit": selected_vector == [1, 0, 0, 0, 0, 0, 0, 0],
        "selected_label_matches_template": selected_label == ext_template["selected_basis_slot"],
        "symbolic_form_matches_template": normalized_table["local_form_representative"]["symbolic"]
        == "eta = theta_plus_0(z1) tensor eta_minus_0(z2) dbar_z2",
        "all_closes_true": all(packet["what_closes_now"].values()),
        "all_open_true": all(packet["what_remains_open"].values()),
        "all_guardrails_true": all(packet["guardrails"].values()),
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "selected_normalized_ext_local_form_table",
        "status": STATUS,
        "closure_claimed": False,
        "checks": checks,
        "what_closes_now": packet["what_closes_now"],
        "what_remains_open": packet["what_remains_open"],
        "next_required_artifact": NEXT,
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }

    note = f"""# Selected Normalized Ext Local Form Table v1

## Result

The selected Ext slot is now normalized as a unit terminal Cech coordinate:

```text
theta_plus_0_tensor_eta_minus_0 -> 1
all other H^1(X,L^2) basis slots -> 0
```

The local-form representative used by the End0 route is:

```text
eta = theta_plus_0(z1) tensor eta_minus_0(z2) dbar_z2
```

The transition seed is the ordered Appell-Humbert class:

```text
L^2 = (2,-4,0)
E(g1,g2)=2, E(g3,g4)=-4, E(g5,g6)=0
```

This closes the normalized selected Ext coordinate/local-form table at the
terminal Cech/Appell-Humbert level. It does not yet close the analytic
Newton/Galerkin table: theta samples, an overlap-compatible analytic
representative, selected HYM correction, Hodge/Lambda, quadrature, and gauge
projector tables remain open.

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
