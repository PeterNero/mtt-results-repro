"""Build the selected HYM-connection to finite-operator extraction contract."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
Q79 = ROOT.parent / "mtt-q79-proof-repro"

OUT_CANDIDATE = ROOT / "candidate_data" / "selected_hym_connection_to_finite_operator_extraction.candidate.json"
OUT_CERT = ROOT / "certificates" / "selected_hym_connection_to_finite_operator_extraction_certificate.json"
OUT_PROOF = ROOT / "proof_corpus" / "MTT_Selected_HYM_Connection_to_Finite_Operator_Extraction_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    operator_gate_path = ROOT / "candidate_data" / "selected_routec_hym_operator_values_gate.candidate.json"
    hym_bridge_path = ROOT / "candidate_data" / "selected_routec_equalradius_gauduchon_hym_bridge.candidate.json"
    ah_source_path = ROOT / "candidate_data" / "selected_routec_ah_source_selection_or_routec_selected_residual.candidate.json"
    smooth_bn_path = ROOT / "candidate_data" / "selected_routec_smooth_bn_galerkin_lift.candidate.json"
    de_bn_path = ROOT / "candidate_data" / "selected_routec_de_action_on_smooth_bn.candidate.json"
    sector_dotd_path = ROOT / "candidate_data" / "selected_routec_sector_projectors_dotd_on_smooth_bn.candidate.json"
    q79_hym_attempt_path = Q79 / "candidate_data" / "selected_hym_operator_source_attempt.candidate.json"

    operator_gate = load(operator_gate_path)
    hym_bridge = load(hym_bridge_path)
    ah_source = load(ah_source_path)
    smooth_bn = load(smooth_bn_path)
    de_bn = load(de_bn_path)
    sector_dotd = load(sector_dotd_path)
    q79_hym_attempt = load(q79_hym_attempt_path)

    abstract_hym_closed = hym_bridge["HYM_existence_bridge"]["abstract_HYM_existence_for_selected_bundle_metric"] is True
    selected_ah_layer = ah_source["selected_AH_goodcover_stability_layer"]["proved"] is True
    operator_gate_instantiated = operator_gate["what_closes_now"]["operator_value_gate_instantiated_after_HYM_existence"] is True

    # These are intentionally strict: an abstract existence theorem is not a
    # finite connection representative and does not select a numerical gauge.
    selected_connection_representative_emitted = False
    selected_cover_basis_quadrature_closed = (
        smooth_bn["B_N_scaffold"]["passes_B_N_payload_gate"] is True
        if "B_N_scaffold" in smooth_bn
        else False
    )
    selected_de_from_connection_emitted = False
    selected_truncation_error_contract_closed = False

    first_de_emission_closed = all(
        [
            abstract_hym_closed,
            selected_ah_layer,
            selected_connection_representative_emitted,
            selected_cover_basis_quadrature_closed,
            selected_de_from_connection_emitted,
            selected_truncation_error_contract_closed,
        ]
    )

    candidate = {
        "candidate": "MTTSelectedHYMConnectionToFiniteOperatorExtraction",
        "status": "MTT_SELECTED_HYM_CONNECTION_TO_FINITE_OPERATOR_EXTRACTION_CONTRACT_BUILT_CONNECTION_REPRESENTATIVE_OPEN",
        "closure_claimed": False,
        "target_fitting_used": False,
        "inputs": {
            "operator_value_gate": str(operator_gate_path),
            "equalradius_HYM_bridge": str(hym_bridge_path),
            "selected_AH_source_layer": str(ah_source_path),
            "smooth_BN_galerkin_lift": str(smooth_bn_path),
            "DE_action_on_smooth_BN": str(de_bn_path),
            "sector_projectors_dotD_on_smooth_BN": str(sector_dotd_path),
            "q79_selected_hym_operator_source_attempt": str(q79_hym_attempt_path),
        },
        "extraction_contract": {
            "name": "Selected_HYM_Connection_to_Finite_Operator_Extraction.v1",
            "input_objects": [
                "selected AH/Cech V_alpha extension 0 -> L -> V_alpha -> L^-1 -> 0",
                "selected equal-radius Gauduchon metric",
                "abstract selected HYM connection class from Li-Yau/Gauduchon",
                "selected good-cover/AH section basis and finite Galerkin basis B_N",
                "selected quadrature and truncation/error budget",
            ],
            "output_objects": [
                "selected HYM connection representative A_HYM in fixed gauge",
                "rho_E transition and metric tables",
                "D_E action and stiffness matrices",
                "Riesz projectors, complement gaps, and reduced Green operators",
                "dotD_alpha1 source and horizontal response vectors",
                "C1/overlap primitive contractions",
            ],
            "acceptance_boundary": operator_gate["needed_extraction_theorem"]["minimum_validator_target"],
            "guardrails": [
                "do not copy smoke matrices as selected values",
                "do not flip lifted flags without a source theorem",
                "do not use observed masses, mixings, or residual targets to choose the connection",
                "do not treat abstract HYM existence as a finite operator table",
            ],
        },
        "straight_path": {
            "stage_E0_selected_bundle_and_metric": {
                "closed": abstract_hym_closed and selected_ah_layer,
                "selected_AH_source_layer": selected_ah_layer,
                "abstract_HYM_existence": abstract_hym_closed,
            },
            "stage_E1_connection_representative": {
                "closed": selected_connection_representative_emitted,
                "missing": [
                    "gauge-fixed HYM connection one-form or connection matrix on the selected AH/good-cover representative",
                    "normalization linking the Li-Yau/Gauduchon abstract solution to the finite validator conventions",
                    "proof that Pic0/holonomy-sensitive choices are fixed or quotient-invariant at operator layer",
                ],
            },
            "stage_E2_finite_basis_quadrature": {
                "closed": selected_cover_basis_quadrature_closed,
                "support_from_prior_BN_scaffold": {
                    "smooth_BN_artifact_status": smooth_bn["status"],
                    "selected_DE_action_artifact_status": de_bn["status"],
                    "sector_dotD_artifact_status": sector_dotd["status"],
                },
                "missing": [
                    "basis payload accepted as selected, not scaffold",
                    "basis functions tied to the selected HYM connection representative",
                    "quadrature and truncation errors controlled for the actual HYM operator",
                ],
            },
            "stage_E3_DE_emission": {
                "closed": selected_de_from_connection_emitted,
                "first_attempt_result": "blocked before matrix emission because E1 connection representative and E2 selected basis/quadrature are open",
                "why_smoke_or_lifted_DE_is_insufficient": operator_gate["lifted_flag_diagnostic"]["guardrail"],
            },
            "stage_E4_spectral_response_C1": {
                "closed": False,
                "depends_on": [
                    "selected D_E matrices",
                    "selected spectral gap and Green operator",
                    "selected dotD_alpha1 driver",
                    "selected primitive overlap tensor",
                ],
            },
        },
        "superset_strategy": {
            "straight_path": "selected HYM connection -> selected finite basis/quadrature -> selected D_E -> spectral response/C1",
            "combined_support_paths": [
                "AH/Cech source fixes the holomorphic bundle and Ext class",
                "rho_UV/constants branch supplies the selected equal-radius metric",
                "Route-C/Galerkin smoke supplies validator schemas only",
                "smooth B_N scaffold supplies a candidate basis shape but not selected HYM extraction",
            ],
            "locked_target": "selected equal-radius q79/F,m=1 V_alpha branch",
            "target_fitting_used": False,
        },
        "first_DE_emission_attempt": {
            "attempted": True,
            "closed": first_de_emission_closed,
            "result": "NOT_EMITTED",
            "minimal_missing_primitive": "gauge_fixed_selected_HYM_connection_representative",
            "secondary_missing_primitive": "selected_finite_basis_quadrature_error_contract_for_that_connection",
            "legal_next_computation": "construct a finite Newton/Galerkin HYM solve on the selected AH/Cech bundle and equal-radius metric, with gauge fixing and a posteriori residual/error certificate",
        },
        "what_closes_now": {
            "extraction_contract_formalized": True,
            "stage_order_locked": True,
            "first_DE_emission_attempt_executed": True,
            "abstract_HYM_no_longer_blocker": abstract_hym_closed,
            "missing_primitive_identified": True,
        },
        "what_remains_open": {
            "gauge_fixed_selected_HYM_connection_representative": True,
            "selected_finite_basis_quadrature_error_contract": True,
            "selected_D_E_matrices_from_connection": True,
            "selected_Riesz_Green_dotD_C1_overlap": True,
            "full_SM_or_no_knob_closure": True,
        },
        "next_required_artifact": "MTT_Selected_HYM_GaugeFixed_Connection_Representative_or_Galerkin_Solve_v1",
    }

    cert = {
        "certificate": "MTT_Selected_HYM_Connection_to_Finite_Operator_Extraction_v1",
        "status": candidate["status"],
        "closure_claimed": False,
        "extraction_contract_formalized": True,
        "first_DE_emission_closed": first_de_emission_closed,
        "minimal_missing_primitive": candidate["first_DE_emission_attempt"]["minimal_missing_primitive"],
        "next_required_artifact": candidate["next_required_artifact"],
    }

    proof = """# MTT Selected HYM Connection to Finite Operator Extraction v1

## Claim

The extraction theorem is now formalized.  The abstract HYM existence result
does not by itself emit finite operator matrices.  The first selected `D_E`
emission attempt is blocked exactly at the missing gauge-fixed HYM connection
representative and the finite basis/quadrature/error contract for that
representative.

## Contract

The legal extraction chain is:

```text
selected AH/Cech V_alpha
+ selected equal-radius Gauduchon metric
+ selected gauge-fixed HYM connection A_HYM
+ selected finite basis/quadrature B_N
=> rho_E, metric, D_E, Riesz/Green, dotD, C1/overlap data
```

Smoke matrices and lifted selected flags remain validator-schema support only.
They cannot be copied into selected values.

## Next Computation

Build the selected gauge-fixed HYM representative, either analytically in the
selected AH/good-cover coordinates or numerically by a finite Newton/Galerkin
HYM solve with an a posteriori residual and truncation certificate.  Once that
representative exists, `D_E` is the first emitted operator, followed by
Riesz/Green, `dotD`, and C1/overlap tensors.
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
