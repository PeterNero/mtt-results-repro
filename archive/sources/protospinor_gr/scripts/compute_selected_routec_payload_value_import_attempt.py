from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"
Q79 = ROOT.parent / "mtt-q79-proof-repro"

INTERFACE = ROOT / "certificates" / "selected_matter_payload_import_interface_certificate.json"
SPECTRAL_RETENTION = SM / "certificates" / "selected_spectral_galerkin_projector_retention_data_certificate.json"
FIRST_RUN = SM / "certificates" / "selected_routec_strominger_galerkin_first_run_certificate.json"
SOURCE_SELECTOR = SM / "certificates" / "selected_routec_source_selector_and_basis_theorem_certificate.json"
HYM_PIPELINE = SM / "certificates" / "selected_routec_hym_operator_pipeline_certificate.json"
HYM_VALUE_SEARCH = SM / "certificates" / "selected_routec_hym_value_search_certificate.json"
SECTOR_DOTD = SM / "certificates" / "selected_routec_sector_projectors_dotd_on_smooth_bn_certificate.json"
CORRECTION_EMISSION = SM / "certificates" / "selected_routec_correction_source_emission_or_selected_galerkin_values_certificate.json"
DE_ACTION = SM / "candidate_data" / "selected_routec_strominger_galerkin_solve" / "de_action.candidate.json"
C1_PRIMS = SM / "candidate_data" / "selected_routec_strominger_galerkin_solve" / "c1_primitive_contractions.candidate.json"
FULL_SM = Q79 / "certificates" / "selected_full_sm_data_theorem_attempt_certificate.json"

OUT_CERT = ROOT / "certificates" / "selected_routec_payload_value_import_attempt_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "Selected_RouteC_Payload_Value_Import_Attempt_v1.md"
OUT_PACKET = ROOT / "candidate_data" / "selected_routec_payload_value_import_attempt.packet.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    interface = load(INTERFACE)
    spectral = load(SPECTRAL_RETENTION)
    first_run = load(FIRST_RUN)
    selector = load(SOURCE_SELECTOR)
    hym_pipeline = load(HYM_PIPELINE)
    hym_search = load(HYM_VALUE_SEARCH)
    sector_dotd = load(SECTOR_DOTD)
    correction = load(CORRECTION_EMISSION)
    de_action = load(DE_ACTION)
    c1_prims = load(C1_PRIMS)
    full_sm = load(FULL_SM)

    sector_flags = {
        sector: slot.get("selected_source_verified")
        for sector, slot in de_action.get("operator_slots", {}).items()
    }
    all_de_selected = bool(sector_flags) and all(flag is True for flag in sector_flags.values())

    attempted_import = {
        "selected_spectral_projector_retention": {
            "status": spectral["status"],
            "promotable": spectral["closure_claimed"] is True,
            "next": spectral["primary_next_artifact"],
        },
        "routec_strominger_galerkin_first_run": {
            "status": first_run["status"],
            "manifest_filled": first_run["manifest_filled"],
            "proof_promotion_allowed": first_run["proof_promotion_allowed"],
            "promotable": first_run["proof_promotion_allowed"] is True,
            "next": first_run["primary_next_artifact"],
        },
        "routec_source_selector_and_basis": {
            "status": selector["status"],
            "promotable": selector["closure_claimed"] is True,
            "next": selector["primary_next_artifact"],
        },
        "routec_hym_pipeline": {
            "status": hym_pipeline["status"],
            "promotable": hym_pipeline["closure_claimed"] is True,
            "next": hym_pipeline["next_required_artifact"],
        },
        "routec_hym_value_search": {
            "status": hym_search["status"],
            "promotable": hym_search["closure_claimed"] is True,
            "next": hym_search["next_required_artifact"],
        },
        "sector_projectors_dotd_on_smooth_bn": {
            "status": sector_dotd["status"],
            "promotable": False,
            "what_closes": sector_dotd["what_closes"],
            "what_remains_open": sector_dotd["what_remains_open"],
        },
        "correction_source_emission": {
            "status": correction["status"],
            "promotable": False,
            "next": correction["next_required_artifact"],
        },
        "de_action_candidate": {
            "status": de_action["status"],
            "selected_by_mtt": de_action["selected_by_mtt"],
            "all_sector_selected_source_verified": all_de_selected,
            "sector_selected_flags": sector_flags,
            "promotable": de_action["selected_by_mtt"] is True and all_de_selected,
        },
        "c1_primitive_contractions": {
            "status": c1_prims["status"],
            "selected_source_verified": c1_prims["selected_source_verified"],
            "promotable": c1_prims["selected_source_verified"] is True,
        },
    }

    import_slot_resolution = {
        "selected_source_branch": {
            "resolved": False,
            "best_evidence": hym_search["status"],
            "blocker": "RouteC_selected_source_origin_lemma",
        },
        "selected_sector_projectors_and_zero_modes": {
            "resolved": False,
            "best_evidence": sector_dotd["status"],
            "blocker": "selected_source_flags_promoted and quotient-valid selected Galerkin basis",
        },
        "selected_DE_Riesz_Green_dotD": {
            "resolved": False,
            "best_evidence": first_run["status"],
            "blocker": "proof-usable selected de-response packet",
        },
        "finite_C1_Hessian_deltaTheta": {
            "resolved": False,
            "best_evidence": correction["status"],
            "blocker": "selected deltaTheta_C1 solution and full lower-order Hess_Xi blocks",
        },
        "primitive_overlap_contractions": {
            "resolved": False,
            "best_evidence": c1_prims["status"],
            "blocker": "primitive C1 contractions from honest selected source",
        },
        "family_kinetic_metrics": {
            "resolved": False,
            "best_evidence": full_sm["status"],
            "blocker": "selected family kinetic metrics K_Q,K_u,K_d,K_L,K_e,K_N",
        },
        "neutral_higgs_matching_data": {
            "resolved": False,
            "best_evidence": full_sm["status"],
            "blocker": "neutral operator, Higgs boundary, and RG/threshold matching",
        },
    }

    selected_values_promotable = all(row["promotable"] for row in attempted_import.values())
    all_interface_slots_resolved = all(row["resolved"] for row in import_slot_resolution.values())

    verdict = {
        "attempt_executed": True,
        "selected_values_promotable": selected_values_promotable,
        "all_interface_slots_resolved": all_interface_slots_resolved,
        "selected_matter_payload_import_closed": False,
        "selected_matter_stress_coefficients_closed": False,
        "honest_candidate_data_available": True,
        "proof_usable_selected_values_available": False,
        "next_required_artifact": "MTT_RouteC_Selected_Source_Origin_Lemma_v1_or_Selected_DeltaTheta_C1_Solve_v1",
    }

    guardrails = {
        "does_not_lift_formal_flags": True,
        "does_not_promote_unselected_smoke_payload": True,
        "does_not_use_observed_or_benchmark_inputs": True,
        "does_not_claim_full_SM": full_sm["attempt_result"]["safe_to_claim_theorem"] is False,
        "does_not_claim_selected_matter_stress": True,
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "selected_routec_payload_value_import_attempt",
        "status": "SELECTED_ROUTEC_PAYLOAD_VALUE_IMPORT_ATTEMPT_BLOCKED_SOURCE_VALUES_OPEN",
        "input_certificates": {
            "selected_matter_payload_import_interface": str(INTERFACE),
            "selected_spectral_galerkin_projector_retention": str(SPECTRAL_RETENTION),
            "routec_strominger_galerkin_first_run": str(FIRST_RUN),
            "routec_source_selector_and_basis": str(SOURCE_SELECTOR),
            "routec_hym_pipeline": str(HYM_PIPELINE),
            "routec_hym_value_search": str(HYM_VALUE_SEARCH),
            "sector_projectors_dotd_on_smooth_bn": str(SECTOR_DOTD),
            "correction_source_emission_or_selected_galerkin_values": str(CORRECTION_EMISSION),
            "de_action_candidate": str(DE_ACTION),
            "c1_primitive_contractions": str(C1_PRIMS),
            "selected_full_sm_data_theorem_attempt": str(FULL_SM),
        },
        "interface_status": interface["status"],
        "attempted_import": attempted_import,
        "import_slot_resolution": import_slot_resolution,
        "verdict": verdict,
        "guardrails": guardrails,
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }

    packet = {
        "candidate": "SelectedRouteCPayloadValueImportAttempt",
        "can_import_to_gr_stress_gate": False,
        "attempted_import": attempted_import,
        "import_slot_resolution": import_slot_resolution,
        "next_required_artifact": verdict["next_required_artifact"],
    }

    note = """# Selected Route-C Payload Value Import Attempt v1

## Result

The selected matter payload import was attempted against the latest q79 and
sm-parity Route-C/Strominger/Galerkin artifacts.

The honest result is blocked, but sharply:

```text
manifest data exist
formal/lifted diagnostic pipeline exists
sector projector and dotD model-active data exist
selected-source promotion is still open
primitive C1 contractions are still open
```

Therefore no selected matter stress coefficients can yet be imported into the
GR response theorem.

## Why It Does Not Promote

The available `D_E`, Green, dotD, sector-projector, and C1 files are support
or diagnostic payloads. They still carry unselected flags such as:

```text
selected_by_mtt = false
selected_source_verified = false
alpha1_driver_verified = false
proof_promotion_allowed = false
```

Promoting those would be exactly the kind of hidden fitting/flag-lifting the
program is designed to avoid.

## Next Required Object

```text
MTT_RouteC_Selected_Source_Origin_Lemma_v1
```

or, if the source origin is supplied independently:

```text
MTT_Selected_RouteC_Splitter_Source_Emission_Contract_or_Selected_DeltaTheta_C1_Solve_v1
```

Only after that can the selected payload template be filled and the GR
stress-response coefficients be promoted.
"""

    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"WROTE: {OUT_PACKET}")
    print("STATUS: SELECTED_ROUTEC_PAYLOAD_VALUE_IMPORT_ATTEMPT_BLOCKED_SOURCE_VALUES_OPEN")


if __name__ == "__main__":
    main()
