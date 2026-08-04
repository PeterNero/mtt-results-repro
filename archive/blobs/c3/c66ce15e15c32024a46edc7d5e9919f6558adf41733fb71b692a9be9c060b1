"""Build the selected normalized Ext local-form table checkpoint."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
Q79 = ROOT.parent / "mtt-q79-proof-repro"

OUT_CANDIDATE = ROOT / "candidate_data" / "selected_normalized_ext_local_form_table.candidate.json"
OUT_CERT = ROOT / "certificates" / "selected_normalized_ext_local_form_table_certificate.json"
OUT_PROOF = ROOT / "proof_corpus" / "MTT_Selected_Normalized_Ext_Local_Form_Table_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    direct_table_path = ROOT / "candidate_data" / "selected_end0_direct_differential_table_from_ah_ext_forms.candidate.json"
    yoneda_path = Q79 / "candidate_data" / "valpha_kunneth_yoneda_scalar_proof.candidate.json"
    source_hunt_path = Q79 / "candidate_data" / "visible_rank2_l2_cohomology_source_hunt.candidate.json"
    cohomology_path = Q79 / "candidate_data" / "visible_rank2_l2_pullback_cech_attempt.cohomology.json"

    direct_table = load(direct_table_path)
    yoneda = load(yoneda_path)
    source_hunt = load(source_hunt_path)
    cohomology = load(cohomology_path)

    ext_label = cohomology["reported_cohomology"]["nonzero_extension_class_label"]
    ext_vector = cohomology["reported_cohomology"]["extension_class_vector_C1"]
    yoneda_packet = yoneda["reduced_kunneth_yoneda_scalar"]
    yoneda_selected_label = yoneda_packet["selected_ext_label"]
    yoneda_selected_vector = yoneda_packet["selected_ext_vector"]
    yoneda_image = yoneda_packet["target_vector"]

    cohomological_normalization_closed = all(
        [
            direct_table["Ext_local_form_template"]["built"] is True,
            ext_label == "theta_plus_0_tensor_eta_minus_0",
            ext_vector == [1, 0, 0, 0, 0, 0, 0, 0],
            yoneda_selected_label == ext_label,
            yoneda_selected_vector == ext_vector,
            yoneda_image[0] == 1,
        ]
    )

    l2_theta_quadrature_closed = False
    overlap_trivialization_table_closed = False
    hermitian_extension_metric_closed = False
    hodge_lambda_table_closed = False
    newton_ready = all(
        [
            cohomological_normalization_closed,
            l2_theta_quadrature_closed,
            overlap_trivialization_table_closed,
            hermitian_extension_metric_closed,
            hodge_lambda_table_closed,
        ]
    )

    candidate = {
        "candidate": "MTTSelectedNormalizedExtLocalFormTable",
        "status": "MTT_SELECTED_NORMALIZED_EXT_LOCAL_FORM_TABLE_BUILT_L2_THETA_QUADRATURE_OPEN",
        "closure_claimed": False,
        "target_fitting_used": False,
        "inputs": {
            "direct_End0_AH_Ext_form_table": str(direct_table_path),
            "q79_reduced_Kunneth_Yoneda_scalar_proof": str(yoneda_path),
            "q79_rank2_L2_cohomology_source_hunt": str(source_hunt_path),
            "q79_pullback_Cech_cohomology": str(cohomology_path),
        },
        "selected_ext_identity": {
            "label": ext_label,
            "cohomology_vector_C1": ext_vector,
            "local_form_row_id": "eta_00",
            "central_shared_circle_degree": 0,
            "line_degree": "L^2=(2,-4,0)",
            "source_basis": "selected q79 terminal-section/Kunneth theta ladder basis",
        },
        "normalization_policy": {
            "cohomological_normalization_closed": cohomological_normalization_closed,
            "cohomological_coefficient": 1,
            "meaning": "The selected Ext representative is the first unit vector in the selected Cech/Kunneth basis. This fixes the algebraic row and scalar coefficient used by the direct End0 local-form table.",
            "theta_function_basis_declared": True,
            "theta_function_basis": {
                "E1_positive_section": "Theta_{2,0}(z1; tau=i)",
                "E2_negative_serre_dual_representative": "Eta_{-4,0}(z2; tau=i) dbar_z2",
                "central_factor": "1",
                "symbolic_local_form": "Theta_{2,0}(z1; i) tensor Eta_{-4,0}(z2; i) dbar_z2",
            },
            "L2_theta_quadrature_closed": l2_theta_quadrature_closed,
            "overlap_trivialization_table_closed": overlap_trivialization_table_closed,
            "hermitian_extension_metric_closed": hermitian_extension_metric_closed,
            "Hodge_Lambda_table_closed": hodge_lambda_table_closed,
            "guardrail": "The unit coefficient is a cohomological/basis normalization, not a computed physical L2 norm or HYM metric normalization.",
        },
        "local_form_table": [
            {
                "row_id": "eta_00",
                "selected": True,
                "source_label": ext_label,
                "cohomology_vector_index": 0,
                "cohomology_coefficient": 1,
                "symbolic_Cech_label": "theta_plus_0_tensor_eta_minus_0",
                "symbolic_Dolbeault_representative": "Theta_{2,0}(z1; i) tensor Eta_{-4,0}(z2; i) dbar_z2",
                "support": [
                    "E1 degree +2 theta section",
                    "E2 degree -4 Serre-dual H1 representative",
                    "central shared circle degree 0",
                ],
                "l2_norm_value": None,
                "overlap_transition_values": None,
                "newton_ready": False,
            }
        ],
        "yoneda_scalar_support": {
            "reduced_Kunneth_matrix_imported": True,
            "selected_ext_label": yoneda_selected_label,
            "selected_ext_vector": yoneda_selected_vector,
            "selected_ext_image": yoneda_image,
            "selected_row_scalar": 1,
            "nonzero_image": yoneda_image[0] == 1,
            "use_in_this_artifact": "support path for the unit cohomological scalar; it does not replace the missing analytic local overlap/quadrature table",
        },
        "superset_strategy": {
            "straight_path": "Direct AH/Ext -> normalized symbolic Dolbeault row -> End_0 local differential table.",
            "support_path": "Reduced Kunneth/Yoneda scalar and terminal-section cohomology are imported only to lock the basis coefficient and nonzero row.",
            "locked_target": "selected q79/F,m=1 V_alpha branch with L=(1,-2,0), L^2=(2,-4,0), no measured constants.",
            "not_used": "No observed SM masses, mixings, or benchmark constants are used to select or normalize the Ext row.",
        },
        "newton_readiness": {
            "ready": newton_ready,
            "cohomological_row_ready": cohomological_normalization_closed,
            "l2_theta_quadrature_closed": l2_theta_quadrature_closed,
            "overlap_trivialization_table_closed": overlap_trivialization_table_closed,
            "hermitian_extension_metric_closed": hermitian_extension_metric_closed,
            "hodge_lambda_table_closed": hodge_lambda_table_closed,
            "first_blocker": "selected_L2_theta_quadrature_and_overlap_table_for_eta_00",
        },
        "what_closes_now": {
            "selected_Ext_row_eta_00_fixed": True,
            "cohomological_scalar_normalization_fixed_to_one": cohomological_normalization_closed,
            "central_shared_circle_degree_zero_preserved": True,
            "symbolic_Dolbeault_representative_declared": True,
        },
        "what_remains_open": {
            "actual_L2_norm_integral": True,
            "theta_quadrature_values": True,
            "overlap_trivialization_table": True,
            "partition_of_unity_or_equivalent_global_Dolbeault_representative": True,
            "selected_HYM_metric_connection_correction": True,
            "Hodge_Lambda_quadrature_gauge_projector_tables": True,
            "selected_Newton_Galerkin_coefficients": True,
            "full_SM_or_no_knob_closure": True,
        },
        "next_required_artifact": "MTT_Selected_Ext_L2_Theta_Quadrature_Table_v1",
    }

    cert = {
        "certificate": "MTT_Selected_Normalized_Ext_Local_Form_Table_v1",
        "status": candidate["status"],
        "closure_claimed": False,
        "target_fitting_used": False,
        "selected_Ext_row_eta_00_fixed": True,
        "cohomological_normalization_closed": cohomological_normalization_closed,
        "selected_row_scalar": 1,
        "l2_theta_quadrature_closed": l2_theta_quadrature_closed,
        "newton_ready": newton_ready,
        "first_blocker": candidate["newton_readiness"]["first_blocker"],
        "next_required_artifact": candidate["next_required_artifact"],
    }

    proof = """# MTT Selected Normalized Ext Local Form Table v1

## Claim

The selected Ext row for the direct `End_0(V_alpha)` route is now fixed at the
cohomological local-form level:

```text
eta_00 = Theta_{2,0}(z1; i) tensor Eta_{-4,0}(z2; i) dbar_z2
```

It represents the selected Cech/Kunneth basis label
`theta_plus_0_tensor_eta_minus_0` with coefficient `1` in
`H^1(X,L^2)`, where `L^2=(2,-4,0)` and the shared circle degree is zero.

## Straight Path

The straight path is:

```text
selected AH/Ext source -> eta_00 symbolic Dolbeault row -> End_0 local table
```

This is the direct `V_alpha`/`End_0(V_alpha)` route.  It does not pass through
the gerbe-twisted `B_N` scaffold as a proof source.

## Superset Support Path

The reduced q79 Kunneth/Yoneda scalar proof is used only as support for the
basis coefficient.  In that model, the selected vector

```text
[1,0,0,0,0,0,0,0]
```

maps to a nonzero target vector with first coefficient `1`.  This locks the
cohomological scalar of the selected row, but it is not an analytic HYM or
quadrature computation.

## Guardrail

The coefficient `1` is a cohomological normalization in the selected basis.  It
is not a physical `L2` norm, not a Hermitian extension-metric normalization, and
not a computed overlap integral.

## What Remains

The next true gate is the selected `L2` theta quadrature and overlap table for
`eta_00`: theta norms, transition-compatible overlap values, an equivalent
global Dolbeault representative or partition-of-unity table, and the Hodge /
Lambda / gauge-projector data needed by the Newton-Galerkin solve.

## Next Artifact

`MTT_Selected_Ext_L2_Theta_Quadrature_Table_v1`.
"""

    OUT_CANDIDATE.parent.mkdir(parents=True, exist_ok=True)
    OUT_CERT.parent.mkdir(parents=True, exist_ok=True)
    OUT_PROOF.parent.mkdir(parents=True, exist_ok=True)
    OUT_CANDIDATE.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_PROOF.write_text(proof, encoding="utf-8")
    print(f"Wrote {OUT_CANDIDATE}")
    print(f"Wrote {OUT_CERT}")
    print(f"Wrote {OUT_PROOF}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
