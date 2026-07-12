from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"

PREV_IMPORT = ROOT / "certificates" / "routec_sourceemission_stability_chain_import_certificate.json"
SRC_DATA = SM / "candidate_data" / "selected_routec_hym_operator_values_gate.candidate.json"
SRC_CERT = SM / "certificates" / "selected_routec_hym_operator_values_gate_certificate.json"
SRC_NOTE = SM / "proof_corpus" / "MTT_Selected_RouteC_HYM_OperatorValues_or_DERieszGreenDotD_Source_v1.md"

OUT_CERT = ROOT / "certificates" / "routec_hym_operator_values_gate_import_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "routec_hym_operator_values_gate_import.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "RouteC_HYM_Operator_Values_Gate_Import_v1.md"

STATUS = "ROUTEC_HYM_OPERATOR_VALUES_GATE_IMPORTED_EXTRACTION_THEOREM_OPEN"
SOURCE_STATUS = "MTT_SELECTED_ROUTEC_HYM_OPERATOR_VALUES_GATE_BUILT_VALUES_NOT_EMITTED"
NEXT_ARTIFACT = "MTT_Selected_HYM_Connection_to_Finite_Operator_Extraction_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV_IMPORT)
    src = load(SRC_DATA)
    cert = load(SRC_CERT)
    note = SRC_NOTE.read_text(encoding="utf-8")

    input_checks = {
        "previous_import_proved": prev["theorem"]["proved"] is True,
        "previous_next_matches": prev["verdict"]["next_required_artifact"]
        == "MTT_Selected_RouteC_HYM_OperatorValues_or_DERieszGreenDotD_Source_v1",
        "source_status_matches": src["status"] == SOURCE_STATUS,
        "certificate_status_matches": cert["status"] == SOURCE_STATUS,
        "next_artifact_matches": src["next_required_artifact"] == NEXT_ARTIFACT,
        "source_note_present": "concrete finite operator values are not emitted yet" in " ".join(note.split()),
    }

    honest = src["validator_results_on_honest_smoke"]
    lifted = src["lifted_flag_diagnostic"]["validators"]
    honest_checks = {
        "rhoE_mesh_passes": honest["rhoE_mesh"]["pass"] is True,
        "rhoE_metric_passes": honest["rhoE_metric"]["pass"] is True,
        "sector_maps_passes": honest["sector_maps"]["pass"] is True,
        "route_c_residual_fails": honest["route_c_residuals"]["pass"] is False,
        "de_action_fails": honest["de_action"]["pass"] is False,
        "riesz_gap_fails": honest["riesz_gap"]["pass"] is False,
        "reduced_green_fails": honest["reduced_green"]["pass"] is False,
        "dotd_response_fails": honest["dotd_response"]["pass"] is False,
    }
    lifted_checks = {
        "lifted_de_action_passes": lifted["de_action"]["pass"] is True,
        "lifted_riesz_gap_passes": lifted["riesz_gap"]["pass"] is True,
        "lifted_reduced_green_passes": lifted["reduced_green"]["pass"] is True,
        "lifted_dotd_response_passes": lifted["dotd_response"]["pass"] is True,
        "lifted_flags_not_proof": "not theorem-derived values"
        in src["lifted_flag_diagnostic"]["guardrail"],
    }
    source_flag_checks = {
        key: value is False for key, value in src["source_flags_on_honest_smoke"].items()
    }
    extraction_checks = {
        "abstract_HYM_no_longer_blocker": src["what_closes_now"]["abstract_HYM_no_longer_blocker"] is True,
        "extraction_theorem_identified": src["what_closes_now"][
            "exact_missing_extraction_theorem_identified"
        ]
        is True,
        "selected_operator_values_not_closed": src["selected_operator_values_closed"] is False,
        "closure_not_claimed": src["closure_claimed"] is False,
        "target_fitting_not_used": src["target_fitting_used"] is False,
    }

    theorem = {
        "name": "RouteCHYMOperatorValuesGateImportTheorem",
        "proved": all(input_checks.values())
        and all(honest_checks.values())
        and all(lifted_checks.values())
        and all(source_flag_checks.values())
        and all(extraction_checks.values()),
        "statement": (
            "The selected HYM operator-values gate is imported. Abstract HYM "
            "existence is no longer the blocker, honest smoke data pass only "
            "mesh/metric/sector checks while failing selected-source operator "
            "checks, and lifted selected flags pass lower validators only as "
            "schema sufficiency diagnostics. The next theorem must extract "
            "finite rho_E, D_E, Riesz/Green, dotD, and C1/overlap matrices "
            "from the selected HYM connection."
        ),
    }

    verdict = {
        "abstract_HYM_existence_available": True,
        "honest_smoke_partial_support_only": True,
        "lifted_flags_rejected_as_proof": True,
        "selected_rho_E_metric_tables_closed": False,
        "selected_D_E_Riesz_Green_dotD_closed": False,
        "selected_C1_overlap_contractions_closed": False,
        "selected_HYM_connection_values_closed": False,
        "selected_A_selected_emitted": False,
        "selected_b_selected_emitted": False,
        "observed_flavor_data_used": False,
        "next_required_artifact": NEXT_ARTIFACT,
    }

    packet = {
        "theorem": theorem,
        "input_checks": input_checks,
        "honest_checks": honest_checks,
        "lifted_checks": lifted_checks,
        "source_flag_checks": source_flag_checks,
        "extraction_checks": extraction_checks,
        "needed_extraction_theorem": src["needed_extraction_theorem"],
        "validator_results_on_honest_smoke": honest,
        "lifted_flag_diagnostic": src["lifted_flag_diagnostic"],
        "what_closes_now": src["what_closes_now"],
        "what_remains_open": src["what_remains_open"],
        "verdict": verdict,
    }

    note_out = """# Route-C HYM Operator Values Gate Import v1

## Result

The selected HYM operator-values gate is imported.

What closes:

```text
abstract HYM existence is no longer the blocker
honest smoke mesh/metric/sector-map checks pass
honest operator checks fail selected-source flags
lifted-flag operator checks pass only as schema sufficiency diagnostics
the missing extraction theorem is identified
```

What remains open:

```text
selected HYM connection/transition values
selected rho_E and metric tables
selected D_E, Riesz/Green, and dotD
selected C1/overlap primitive contractions
A_selected and b_selected
```

No observed masses, mixings, CP phase, thresholds, benchmark values, or lifted
selected flags are used as selectors.

## Status

```text
ROUTEC_HYM_OPERATOR_VALUES_GATE_IMPORTED_EXTRACTION_THEOREM_OPEN
```

The next required artifact is:

```text
MTT_Selected_HYM_Connection_to_Finite_Operator_Extraction_v1
```
"""

    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(
        json.dumps(
            {
                "program": "MTT protospinor GR response proof",
                "certificate": "routec_hym_operator_values_gate_import",
                "status": STATUS,
                "input_certificate": str(PREV_IMPORT),
                "source_certificate": str(SRC_CERT),
                "theorem": theorem,
                "input_checks": input_checks,
                "honest_checks": honest_checks,
                "lifted_checks": lifted_checks,
                "source_flag_checks": source_flag_checks,
                "extraction_checks": extraction_checks,
                "verdict": verdict,
                "packet_written": str(OUT_PACKET),
                "note_written": str(OUT_NOTE),
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    OUT_NOTE.write_text(note_out, encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {STATUS}")


if __name__ == "__main__":
    main()
