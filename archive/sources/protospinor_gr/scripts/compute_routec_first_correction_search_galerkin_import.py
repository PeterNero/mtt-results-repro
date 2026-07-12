from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"

PREV_IMPORT = ROOT / "certificates" / "routec_higherorder_fullresponse_flavor_splitting_import_certificate.json"
SRC_CERT = SM / "certificates" / "selected_routec_first_correction_search_or_galerkin_run_certificate.json"
SRC_DATA = SM / "candidate_data" / "selected_routec_first_correction_search_or_galerkin_run.candidate.json"

OUT_CERT = ROOT / "certificates" / "routec_first_correction_search_galerkin_import_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "routec_first_correction_search_galerkin_import.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "RouteC_First_Correction_Search_Galerkin_Import_v1.md"

STATUS = "ROUTEC_FIRST_CORRECTION_SEARCH_GALERKIN_IMPORTED_DIAGNOSTIC_SPLITTER_VALUES_OPEN"
NEXT_ARTIFACT = "MTT_Selected_RouteC_Correction_Source_Emission_or_Selected_Galerkin_Values_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV_IMPORT)
    src_cert = load(SRC_CERT)
    src = load(SRC_DATA)

    lane_a = src["parallel_lanes"]["lane_A_qutrit_weyl_correction_search"]
    lane_b = src["parallel_lanes"]["lane_B_galerkin_replay"]
    rep = lane_a["representative"]
    combined = src["combined_result"]

    closed_now = {
        "previous_flavor_splitting_criterion_imported": prev["theorem"]["proved"],
        "source_theorem_proved": src["theorem"]["proved"],
        "first_correction_matrix_search_executed": src_cert["what_closes"][
            "first_correction_matrix_search_executed"
        ],
        "first_galerkin_replay_executed": src_cert["what_closes"]["first_galerkin_replay_executed"],
        "diagnostic_splitter_found_without_observed_targets": src_cert["what_closes"][
            "diagnostic_splitter_found_without_observed_targets"
        ],
        "honest_vs_formal_lift_status_recorded": src_cert["what_closes"][
            "honest_vs_formal_lift_status_recorded"
        ],
        "target_fitting_excluded": src_cert["what_closes"]["target_fitting_excluded"],
    }

    diagnostic_checks = {
        "lane_A_candidate_count_positive": lane_a["candidate_count"] > 0,
        "lane_A_diagnostic_splitter_found": lane_a["diagnostic_splitter_found"] is True,
        "lane_A_not_selected_by_mtt": lane_a["selected_by_mtt"] is False,
        "lane_A_promotion_not_allowed": lane_a["promotion_allowed"] is False,
        "mass_split_traceless_positive_all_sectors": all(
            value > 0 for value in rep["mass_split_traceless_norm_sq"].values()
        ),
        "ckm_commutator_positive": rep["ckm_commutator_norm_sq"] > 0,
        "pmns_commutator_positive": rep["pmns_commutator_norm_sq"] > 0,
        "cp_odd_trace_commutator_cubed_imag_nonzero": abs(
            rep["cp_odd_trace_commutator_cubed_imag"]
        )
        > 0,
    }

    galerkin_checks = {
        "manifest_filled": lane_b["manifest_filled"] is True,
        "honest_root_all_pass_false": lane_b["honest_root_all_pass"] is False,
        "selected_correction_matrices_not_emitted": lane_b["selected_correction_matrices_emitted"] is False,
        "formal_lift_diagnostic_only": lane_b["formal_lift_is_diagnostic_only"] is True,
        "formal_lift_lower_validators_pass": lane_b["formal_lift_lower_validators_all_pass"] is True,
        "formal_lift_promotion_passes_but_not_honest": lane_b["formal_lift_promotion_passes"] is True,
        "honest_failures_record_selected_source": any(
            "selected_source_verified" in item
            for failures in lane_b["honest_root_failures"].values()
            for item in failures
        ),
    }

    open_gate_checks = {
        "diagnostic_can_break_degeneracy": combined["diagnostic_qutrit_correction_can_break_degeneracy"]
        is True,
        "honest_galerkin_does_not_emit": combined["honest_galerkin_selected_values_emit_correction"]
        is False,
        "selected_correction_not_promoted": combined["selected_correction_promoted"] is False,
        "closure_not_claimed": src["closure_claimed"] is False,
        "target_fitting_not_used": src["target_fitting_used"] is False,
        "next_artifact_is_source_emission_or_selected_galerkin": src["next_required_artifact"] == NEXT_ARTIFACT,
    }

    still_open_checks = {key: value is True for key, value in src["what_remains_open"].items()}

    theorem = {
        "name": "RouteCFirstCorrectionSearchGalerkinImportTheorem",
        "proved": all(closed_now.values())
        and all(diagnostic_checks.values())
        and all(galerkin_checks.values())
        and all(open_gate_checks.values())
        and all(still_open_checks.values()),
        "statement": (
            "The imported first correction/Galerkin attempt proves algebraic room "
            "for nondegenerate, noncommuting, CP-odd flavor structure: a qutrit/Weyl "
            "diagnostic splitter passes mass-splitting, CKM/PMNS commutator, and "
            "CP-odd tests without observed targets. It is not selected MTT data: "
            "the honest Galerkin replay does not emit selected correction matrices "
            "because selected-source, selected dotD, and alpha1-driver gates remain open."
        ),
    }

    verdict = {
        "diagnostic_splitter_found": True,
        "diagnostic_candidate_count": lane_a["candidate_count"],
        "mass_split_traceless_positive": True,
        "ckm_commutator_norm_sq": rep["ckm_commutator_norm_sq"],
        "pmns_commutator_norm_sq": rep["pmns_commutator_norm_sq"],
        "cp_odd_trace_commutator_cubed_imag": rep["cp_odd_trace_commutator_cubed_imag"],
        "selected_correction_promoted": False,
        "honest_galerkin_selected_values_emit_correction": False,
        "observed_flavor_data_used": False,
        "next_required_artifact": NEXT_ARTIFACT,
    }

    packet = {
        "theorem": theorem,
        "source_status": src["status"],
        "closed_now": closed_now,
        "diagnostic_checks": diagnostic_checks,
        "galerkin_checks": galerkin_checks,
        "open_gate_checks": open_gate_checks,
        "still_open_checks": still_open_checks,
        "parallel_lanes": src["parallel_lanes"],
        "combined_result": combined,
        "what_remains_open": src["what_remains_open"],
        "verdict": verdict,
    }

    note = """# Route-C First Correction Search / Galerkin Import v1

## Result

The first correction-matrix search and Galerkin replay are now imported.

Lane A finds a diagnostic qutrit/Weyl splitter with:

```text
nonzero traceless Hermitian mass splitting
nonzero CKM and PMNS commutator norms
nonzero CP-odd commutator-cubed trace invariant
```

This proves the current degeneracy is not algebraically fatal. The finite
correction algebra has enough room for flavor structure without observed target
data.

## Boundary

The splitter is not promoted as selected MTT data. Lane B records that the
honest Galerkin replay still fails selected-source, selected-dotD, and
alpha1-driver gates. Formal-lift diagnostics pass lower validators but remain
diagnostic only.

Therefore selected correction matrices, selected Galerkin values, promoted
Yukawa hierarchy, CKM, PMNS, and CP remain open.

## Status

```text
ROUTEC_FIRST_CORRECTION_SEARCH_GALERKIN_IMPORTED_DIAGNOSTIC_SPLITTER_VALUES_OPEN
```

The next required artifact is:

```text
MTT_Selected_RouteC_Correction_Source_Emission_or_Selected_Galerkin_Values_v1
```
"""

    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(
        json.dumps(
            {
                "program": "MTT protospinor GR response proof",
                "certificate": "routec_first_correction_search_galerkin_import",
                "status": STATUS,
                "input_certificates": {
                    "routec_higherorder_fullresponse_flavor_splitting_import": str(PREV_IMPORT),
                    "selected_routec_first_correction_search_or_galerkin_run": str(SRC_CERT),
                },
                "theorem": theorem,
                "closed_now": closed_now,
                "diagnostic_checks": diagnostic_checks,
                "galerkin_checks": galerkin_checks,
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
