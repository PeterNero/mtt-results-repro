from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"

PREV_IMPORT = ROOT / "certificates" / "routec_deltatheta_c1_solve_gate_import_certificate.json"
SRC_CERT = SM / "certificates" / "selected_routec_selected_c1_response_operator_emission_certificate.json"
SRC_DATA = SM / "candidate_data" / "selected_routec_selected_c1_response_operator_emission.candidate.json"

OUT_CERT = ROOT / "certificates" / "routec_selected_c1_response_operator_emission_import_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "routec_selected_c1_response_operator_emission_import.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "RouteC_Selected_C1_Response_Operator_Emission_Import_v1.md"

STATUS = "ROUTEC_SELECTED_C1_RESPONSE_OPERATOR_EMISSION_IMPORTED_A_SELECTED_NOT_EMITTED"
NEXT_ARTIFACT = "MTT_Selected_RouteC_Selected_C1_Operator_Source_or_Galerkin_Rebuild_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV_IMPORT)
    src_cert = load(SRC_CERT)
    src = load(SRC_DATA)

    emission = src["emission_audit"]
    lanes = src["response_lanes"]
    contract = src["operator_emission_contract"]

    closed_now = {
        "previous_deltatheta_solve_gate_imported": prev["theorem"]["proved"],
        "source_theorem_proved": src["theorem"]["proved"],
        "selected_response_operator_schema_audited": src_cert["what_closes"][
            "selected_response_operator_schema_audited"
        ],
        "q79_template_and_extraction_attempt_imported": src_cert["what_closes"][
            "q79_template_and_extraction_attempt_imported"
        ],
        "canonical_zero_response_separated": src_cert["what_closes"][
            "canonical_zero_response_separated_from_nonzero_unselected_candidates"
        ],
        "A_selected_emission_blocker_identified": src_cert["what_closes"][
            "A_selected_emission_blocker_identified"
        ],
        "target_fitting_excluded": src_cert["what_closes"]["target_fitting_excluded"],
    }

    emission_checks = {
        "A_selected_not_emitted": emission["selected_operator_A_selected_emitted"] is False,
        "b_selected_not_emitted": emission["selected_source_vector_b_selected_emitted"] is False,
        "rank_test_not_computable": emission["rank_test_now_computable"] is False,
        "least_squares_not_computable": emission["least_squares_now_computable"] is False,
        "all_required_operator_slots_false": not any(emission["required_operator_slots"].values()),
        "target_dimension_72": emission["target_dimension_from_previous"] == 72,
    }

    schema_checks = {
        "template_schema_present": emission["template_schema_present"] is True,
        "template_status_open": emission["template_status"] == "OPEN",
        "template_driver_row_present": emission["template_driver_row_present"] is True,
        "template_principal_hessian_blocks_present": emission["template_principal_hessian_blocks_present"]
        is True,
        "template_response_matrices_null": all(emission["template_response_matrices_null"].values()),
        "extraction_attempt_present": emission["extraction_attempt_present"] is True,
        "extraction_attempt_blocked": emission["extraction_attempt_status"]
        == "C1_RESPONSE_EXTRACTION_BLOCKED_MISSING_SELECTED_OPERATOR_DATA",
        "alpha1_driver_row_computed": emission["extraction_attempt_result"]["alpha1_driver_row_computed"]
        is True,
        "M_C1_entries_not_computed": emission["extraction_attempt_result"]["M_C1_alpha1_entries_computed"]
        is False,
        "all_extraction_missing_nulls_true": all(emission["extraction_attempt_missing_nulls"].values()),
    }

    lane_checks = {
        "straight_selected_response_unusable": lanes["straight_selected_c1_response"]["usable_as_proof"]
        is False,
        "canonical_smooth_bn_response_zero": lanes["canonical_smooth_bn_response"]["nonzero_response_found"]
        is False,
        "canonical_smooth_bn_unusable": lanes["canonical_smooth_bn_response"]["usable_as_proof"] is False,
        "noninvariant_candidates_nonzero": lanes["noninvariant_candidate_response"][
            "nonzero_unselected_candidates_found"
        ]
        > 0,
        "noninvariant_candidates_do_not_close_selected_C1": lanes["noninvariant_candidate_response"][
            "can_close_selected_C1_now"
        ]
        is False,
    }

    contract_checks = {
        "contract_name_locked": contract["name"] == "SelectedC1ResponseOperatorEmissionContract",
        "codomain_dimension_72": contract["codomain_real_dimension"] == 72,
        "operator_equation_names_A_selected": "A_selected" in contract["operator_equation"],
        "operator_equation_names_b_selected": "b_selected" in contract["operator_equation"],
        "domain_includes_deformation_coordinates": "selected C1 deformation coordinates after gauge fixing"
        in contract["domain_must_include"],
        "validators_include_rank_and_flavor_tests": len(contract["validators_after_emission"]) >= 6,
        "forbidden_shortcuts_listed": len(contract["forbidden_shortcuts"]) >= 5,
    }

    open_gate_checks = {
        "closure_not_claimed": src["closure_claimed"] is False,
        "target_fitting_not_used": src["target_fitting_used"] is False,
        "next_artifact_is_operator_source_rebuild": src["next_required_artifact"] == NEXT_ARTIFACT,
    }

    still_open_checks = {key: value is True for key, value in src["what_remains_open"].items()}

    theorem = {
        "name": "RouteCSelectedC1ResponseOperatorEmissionImportTheorem",
        "proved": all(closed_now.values())
        and all(emission_checks.values())
        and all(schema_checks.values())
        and all(lane_checks.values())
        and all(contract_checks.values())
        and all(open_gate_checks.values())
        and all(still_open_checks.values()),
        "statement": (
            "The imported selected C1 response-operator emission audit proves "
            "that current selected Route-C/Phi_fin/Galerkin artifacts do not "
            "emit A_selected or b_selected. The canonical smooth B_N response is "
            "zero, non-invariant candidates remain unselected, and the selected "
            "template is schema-correct but values-open. The next object is a "
            "selected C1 operator source or Galerkin rebuild that emits finite "
            "Hessian blocks, alpha1 source vector, dotD operators, zero-mode bases, "
            "primitive contractions, and sector matrices."
        ),
    }

    verdict = {
        "A_selected_emitted": False,
        "b_selected_emitted": False,
        "selected_operator_schema_audited": True,
        "canonical_response_zero": True,
        "nonzero_unselected_candidates_exist": True,
        "rank_test_computable": False,
        "least_squares_computable": False,
        "observed_flavor_data_used": False,
        "next_required_artifact": NEXT_ARTIFACT,
    }

    packet = {
        "theorem": theorem,
        "source_status": src["status"],
        "closed_now": closed_now,
        "emission_checks": emission_checks,
        "schema_checks": schema_checks,
        "lane_checks": lane_checks,
        "contract_checks": contract_checks,
        "open_gate_checks": open_gate_checks,
        "still_open_checks": still_open_checks,
        "emission_audit": emission,
        "response_lanes": lanes,
        "operator_emission_contract": contract,
        "what_remains_open": src["what_remains_open"],
        "verdict": verdict,
    }

    note = """# Route-C Selected C1 Response Operator Emission Import v1

## Result

The selected C1 response operator is not emitted yet.

The q79 template and extraction attempt provide structure: the alpha1 driver
row, curvature source, response chain, and principal Hessian-symbol support.
But the selected finite data remain null:

```text
finite Hessian blocks
selected source vector
deltaTheta_C1
dotD operators
zero-mode bases
primitive contractions
sector response matrices
```

## Lane Separation

```text
canonical smooth B_N C1 response: computed zero
non-invariant primitive candidates: nonzero but unselected
selected C1 template: correct schema but values-open
```

Thus `A_selected` and `b_selected` are still not available, and the locked
DeltaTheta solve cannot honestly run.

## Status

```text
ROUTEC_SELECTED_C1_RESPONSE_OPERATOR_EMISSION_IMPORTED_A_SELECTED_NOT_EMITTED
```

The next required artifact is:

```text
MTT_Selected_RouteC_Selected_C1_Operator_Source_or_Galerkin_Rebuild_v1
```
"""

    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(
        json.dumps(
            {
                "program": "MTT protospinor GR response proof",
                "certificate": "routec_selected_c1_response_operator_emission_import",
                "status": STATUS,
                "input_certificates": {
                    "routec_deltatheta_c1_solve_gate_import": str(PREV_IMPORT),
                    "selected_routec_selected_c1_response_operator_emission": str(SRC_CERT),
                },
                "theorem": theorem,
                "closed_now": closed_now,
                "emission_checks": emission_checks,
                "schema_checks": schema_checks,
                "lane_checks": lane_checks,
                "contract_checks": contract_checks,
                "open_gate_checks": open_gate_checks,
                "still_open_checks": still_open_checks,
                "verdict": verdict,
                "packet_written": str(OUT_PACKET),
                "note_written": str(OUT_NOTE),
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    OUT_NOTE.write_text(note, encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {STATUS}")


if __name__ == "__main__":
    main()
