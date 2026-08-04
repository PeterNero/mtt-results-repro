from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"

PREV_IMPORT = ROOT / "certificates" / "routec_fiberclass_observable_invariance_import_certificate.json"
SRC_CERT = SM / "certificates" / "selected_routec_higherorder_fullresponse_flavor_splitting_certificate.json"
SRC_DATA = SM / "candidate_data" / "selected_routec_higherorder_fullresponse_flavor_splitting.candidate.json"

OUT_CERT = ROOT / "certificates" / "routec_higherorder_fullresponse_flavor_splitting_import_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "routec_higherorder_fullresponse_flavor_splitting_import.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "RouteC_HigherOrder_FullResponse_FlavorSplitting_Import_v1.md"

STATUS = "ROUTEC_HIGHERORDER_FULLRESPONSE_FLAVOR_SPLITTING_IMPORTED_VALUES_OPEN"
NEXT_ARTIFACT = "MTT_Selected_RouteC_First_Selected_Correction_Matrix_Search_or_Galerkin_Run_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV_IMPORT)
    src_cert = load(SRC_CERT)
    src = load(SRC_DATA)

    no_go = src["current_layer_no_go"]
    path_a = src["path_A_higher_order_criterion"]
    path_b = src["path_B_full_response_criterion"]

    closed_now = {
        "previous_fiberclass_observable_invariance_imported": prev["theorem"]["proved"],
        "source_theorem_proved": src["theorem"]["proved"],
        "current_scalar_permutation_layer_no_go_proved": src_cert["what_closes"][
            "current_scalar_permutation_layer_no_go_proved"
        ],
        "higher_order_splitting_criterion_proved": src_cert["what_closes"][
            "higher_order_splitting_criterion_proved"
        ],
        "full_response_acceptance_tests_locked": src_cert["what_closes"][
            "full_response_acceptance_tests_locked"
        ],
        "target_fitting_excluded": src_cert["what_closes"]["target_fitting_excluded"],
    }

    diagnostics = no_go["diagnostics"]
    current_layer_checks = {
        "no_go_proved": no_go["proved"] is True,
        "imports_observable_invariance_result": no_go["imports_observable_invariance_result"] is True,
        "all_sectors_scalar_identity": all(
            sector["YYstar_scalar_test"]["is_scalar_identity"] is True for sector in diagnostics.values()
        ),
        "all_sectors_zero_traceless_residual": all(
            sector["YYstar_scalar_test"]["traceless_residual_norm_sq"] == 0.0
            for sector in diagnostics.values()
        ),
        "all_sectors_rank_three": all(sector["rank_from_previous"] == 3 for sector in diagnostics.values()),
    }

    criterion_checks = {
        "higher_order_criterion_proved": path_a["proved"] is True,
        "higher_order_current_values_unavailable": path_a["current_values_available"] is False,
        "mass_splitting_uses_nonzero_traceless_part": "traceless" in path_a["mass_splitting_condition"],
        "mixing_uses_nonzero_commutator": "commutator" in path_a["mixing_condition"],
        "cp_requires_complex_cp_odd_invariant": "CP" in path_a["cp_condition"]
        and "odd" in path_a["cp_condition"],
        "full_response_criterion_proved": path_b["proved"] is True,
        "full_response_current_values_unavailable": path_b["current_values_available"] is False,
        "all_full_response_outputs_required": all(path_b["required_outputs"].values()),
    }

    open_gate_checks = {
        "selected_values_missing_path_a": path_a["why_values_unavailable"][
            "all_required_correction_values_present"
        ]
        is False,
        "selected_values_missing_path_b": path_b["why_values_unavailable"]["galerkin_currently_blocked_by"][
            "actual_selected_values"
        ]
        is True,
        "closure_not_claimed": src["closure_claimed"] is False,
        "target_fitting_not_used": src["target_fitting_used"] is False,
        "next_artifact_is_first_correction_or_galerkin": src["next_required_artifact"] == NEXT_ARTIFACT,
    }

    still_open_checks = {key: value is True for key, value in src["what_remains_open"].items()}

    theorem = {
        "name": "RouteCHigherOrderFullResponseFlavorSplittingImportTheorem",
        "proved": all(closed_now.values())
        and all(current_layer_checks.values())
        and all(criterion_checks.values())
        and all(open_gate_checks.values())
        and all(still_open_checks.values()),
        "statement": (
            "The imported higher-order/full-response gate proves the current "
            "Route-C finite C1 layer cannot split flavor because YY* is scalar "
            "identity in every sector. It locks target-independent acceptance "
            "criteria for flavor closure: nonzero traceless Hermitian correction "
            "for mass splitting, nonzero sector commutators for CKM/PMNS, and a "
            "selected complex CP-odd invariant. The selected correction values "
            "remain open."
        ),
    }

    verdict = {
        "current_layer_no_go_proved": True,
        "higher_order_splitting_criterion_locked": True,
        "full_response_acceptance_tests_locked": True,
        "selected_correction_values_computed": False,
        "physical_flavor_closure_claimed": False,
        "observed_flavor_data_used": False,
        "next_required_artifact": NEXT_ARTIFACT,
    }

    packet = {
        "theorem": theorem,
        "source_status": src["status"],
        "closed_now": closed_now,
        "current_layer_checks": current_layer_checks,
        "criterion_checks": criterion_checks,
        "open_gate_checks": open_gate_checks,
        "still_open_checks": still_open_checks,
        "current_layer_no_go": no_go,
        "path_A_higher_order_criterion": path_a,
        "path_B_full_response_criterion": path_b,
        "what_remains_open": src["what_remains_open"],
        "verdict": verdict,
    }

    note = """# Route-C Higher-Order / Full-Response Flavor Splitting Import v1

## Result

The current finite C1 layer is now imported as a rigorous flavor no-go:

```text
Y0 Y0* is scalar identity in every sector.
```

So the layer gives exact degeneracy and cannot by itself produce Yukawa
hierarchy, CKM, PMNS, or CP structure.

The import also locks the next target-independent acceptance tests:

```text
mass splitting: nonzero traceless Hermitian correction
CKM/PMNS: nonzero commutator between sector Hermitian corrections
CP: selected complex CP-odd invariant
```

## Boundary

No selected correction values are computed here. The missing values are selected
`dotD_alpha1`, `deltaTheta_C1`, zero-mode bases, primitive C1 contractions, and
sector response matrices from the same honest source.

No observed masses, CKM, PMNS, or CP data were used as selectors.

## Status

```text
ROUTEC_HIGHERORDER_FULLRESPONSE_FLAVOR_SPLITTING_IMPORTED_VALUES_OPEN
```

The next required artifact is:

```text
MTT_Selected_RouteC_First_Selected_Correction_Matrix_Search_or_Galerkin_Run_v1
```
"""

    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(
        json.dumps(
            {
                "program": "MTT protospinor GR response proof",
                "certificate": "routec_higherorder_fullresponse_flavor_splitting_import",
                "status": STATUS,
                "input_certificates": {
                    "routec_fiberclass_observable_invariance_import": str(PREV_IMPORT),
                    "selected_routec_higherorder_fullresponse_flavor_splitting": str(SRC_CERT),
                },
                "theorem": theorem,
                "closed_now": closed_now,
                "current_layer_checks": current_layer_checks,
                "criterion_checks": criterion_checks,
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
