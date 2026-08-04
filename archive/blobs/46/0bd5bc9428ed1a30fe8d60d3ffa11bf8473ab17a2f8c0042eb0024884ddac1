from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"

PREV_IMPORT = ROOT / "certificates" / "routec_primitive_source_selection_audit_import_certificate.json"
SRC_CERT = SM / "certificates" / "selected_routec_fiberclass_observable_invariance_or_gaugefix_certificate.json"
SRC_DATA = SM / "candidate_data" / "selected_routec_fiberclass_observable_invariance_or_gaugefix.candidate.json"

OUT_CERT = ROOT / "certificates" / "routec_fiberclass_observable_invariance_import_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "routec_fiberclass_observable_invariance_import.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "RouteC_FiberClass_Observable_Invariance_Import_v1.md"

STATUS = "ROUTEC_FIBERCLASS_OBSERVABLE_INVARIANCE_IMPORTED_GAUGEFIX_OPEN"
NEXT_ARTIFACT = "MTT_Selected_RouteC_HigherOrder_or_FullResponse_FlavorSplitting_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV_IMPORT)
    src_cert = load(SRC_CERT)
    src = load(SRC_DATA)

    path_a = src["path_A_observable_invariance"]
    path_b = src["path_B_absolute_gauge_fix"]
    combined = src["combined_result"]
    obs = path_a["fixed_shift_observables"]
    base = obs["0"]

    closed_now = {
        "previous_fiber_class_reduction_imported": prev["theorem"]["proved"],
        "source_theorem_proved": src["theorem"]["proved"],
        "observable_invariance_under_fixed_fiber_class_for_current_C1_spectrum": src_cert["what_closes"][
            "observable_invariance_under_fixed_fiber_class_for_current_C1_spectrum"
        ],
        "absolute_fiber_origin_not_needed_for_current_spectral_invariants": src_cert["what_closes"][
            "absolute_fiber_origin_not_needed_for_current_spectral_invariants"
        ],
        "canonical_shift0_computation_gauge_allowed": src_cert["what_closes"][
            "canonical_shift0_computation_gauge_allowed"
        ],
        "no_observed_flavor_data_used": src_cert["what_closes"]["no_observed_flavor_data_used"],
    }

    spectral_checks = {
        "fixed_shift_observables_identical": obs["1"] == base and obs["2"] == base,
        "all_sector_YYstar_scalar_identity": all(
            sector["YYstar_is_scalar_identity"] is True
            for by_shift in obs.values()
            for sector in by_shift.values()
        ),
        "all_sector_rank_three": all(
            sector["rank"] == 3 for by_shift in obs.values() for sector in by_shift.values()
        ),
        "all_sector_degenerate_threefold_spectrum": all(
            len(set(sector["singular_values_squared_if_scalar_identity"])) == 1
            for by_shift in obs.values()
            for sector in by_shift.values()
        ),
    }

    gaugefix_checks = {
        "absolute_gauge_fix_attempted": path_b["attempted"] is True,
        "absolute_gauge_fix_not_proved": path_b["proved"] is False,
        "physical_absolute_origin_not_selected": path_b["physical_absolute_origin_selected"] is False,
        "shift0_available_as_computation_gauge": path_b["canonical_computation_gauge_available"] is True
        and path_b["canonical_computation_gauge"] == "fiber_shift_0",
        "operator_level_projective_rhoE_not_promoted": path_b["required_markers"][
            "operator_level_projective_rhoE_promoted"
        ]
        is False,
        "rhoE_not_selected_by_mtt": path_b["required_markers"]["rhoE_selected_by_mtt"] is False,
    }

    open_gate_checks = {
        "current_layer_not_physical_flavor_closure": path_a["does_not_prove_physical_flavor_closure"] is True,
        "selected_observable_class_proved": combined["selected_C1_observable_class_proved_at_current_layer"]
        is True,
        "selected_unique_C1_matrix_not_proved": combined["selected_unique_C1_matrix_proved"] is False,
        "fiber_origin_not_needed_current_spectral_observables": combined[
            "fiber_origin_needed_for_current_spectral_observables"
        ]
        is False,
        "fiber_origin_needed_for_future_matrix_entries_or_corrections": combined[
            "fiber_origin_needed_for_full_matrix_entries_or_future_noncommuting_corrections"
        ]
        is True,
        "closure_not_claimed": src["closure_claimed"] is False,
        "target_fitting_not_used": src["target_fitting_used"] is False,
        "next_artifact_is_higher_order_or_full_response": src["next_required_artifact"] == NEXT_ARTIFACT,
    }

    still_open_checks = {key: value is True for key, value in src["what_remains_open"].items()}

    theorem = {
        "name": "RouteCFiberClassObservableInvarianceImportTheorem",
        "proved": all(closed_now.values())
        and all(spectral_checks.values())
        and all(gaugefix_checks.values())
        and all(open_gate_checks.values())
        and all(still_open_checks.values()),
        "statement": (
            "For the imported Route-C finite C1 layer, fixed qutrit fiber shifts "
            "0,1,2 have identical spectral invariants: each sector matrix is a "
            "scalar multiple of a permutation matrix, so YY* is scalar identity. "
            "Shift 0 is therefore a legal computation gauge for current spectral "
            "invariants. This does not prove a unique selected C1 matrix or "
            "physical flavor closure; the remaining gate is selected higher-order "
            "or full-response flavor splitting."
        ),
    }

    verdict = {
        "selected_C1_observable_class_proved_at_current_layer": True,
        "selected_unique_C1_matrix_proved": False,
        "shift0_computation_gauge_allowed": True,
        "absolute_fiber_origin_selected": False,
        "current_layer_has_degenerate_singular_spectrum": True,
        "physical_flavor_closure_claimed": False,
        "observed_flavor_data_used": False,
        "next_required_artifact": NEXT_ARTIFACT,
    }

    packet = {
        "theorem": theorem,
        "source_status": src["status"],
        "closed_now": closed_now,
        "spectral_checks": spectral_checks,
        "gaugefix_checks": gaugefix_checks,
        "open_gate_checks": open_gate_checks,
        "still_open_checks": still_open_checks,
        "path_A_observable_invariance": path_a,
        "path_B_absolute_gauge_fix": path_b,
        "combined_result": combined,
        "what_remains_open": src["what_remains_open"],
        "verdict": verdict,
    }

    note = """# Route-C Fiber-Class Observable Invariance Import v1

## Result

The fixed qutrit fiber class no longer blocks current spectral C1 observables.

For fiber shifts `0`, `1`, and `2`, every current finite C1 sector matrix is a
scalar multiple of a permutation matrix. Hence `Y Y*` is scalar identity and the
following observables are identical across the fixed-fiber class:

```text
rank
absolute determinant
traces of powers of Y Y*
singular spectrum
```

Shift `0` is therefore legal as a computation gauge for this current spectral
layer.

## Boundary

The absolute gauge-fix path remains open. The selected source certificates do
not mark a qutrit fiber origin and do not prove operator-level basis transport.

This also does not close physical flavor. The same scalar-permutation result
means the current layer has degenerate singular values and cannot by itself
produce Yukawa hierarchy, CKM, PMNS, or CP structure.

No observed flavor data were used.

## Status

```text
ROUTEC_FIBERCLASS_OBSERVABLE_INVARIANCE_IMPORTED_GAUGEFIX_OPEN
```

The next required artifact is:

```text
MTT_Selected_RouteC_HigherOrder_or_FullResponse_FlavorSplitting_v1
```
"""

    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(
        json.dumps(
            {
                "program": "MTT protospinor GR response proof",
                "certificate": "routec_fiberclass_observable_invariance_import",
                "status": STATUS,
                "input_certificates": {
                    "routec_primitive_source_selection_audit_import": str(PREV_IMPORT),
                    "selected_routec_fiberclass_observable_invariance_or_gaugefix": str(SRC_CERT),
                },
                "theorem": theorem,
                "closed_now": closed_now,
                "spectral_checks": spectral_checks,
                "gaugefix_checks": gaugefix_checks,
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
