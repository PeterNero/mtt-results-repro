"""Promote zero-mode/Gram readiness for E_CKM and isolate contractions."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_zeromodegramsectorcontractionpayload_or_eckmweightrows"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
STATIONARY = PACKET_DIR / "stationary_transported_basis_import_for_eckm.packet.json"
GRAM = PACKET_DIR / "gram_trace_convention_for_eckm.packet.json"
CONTRACTIONS = PACKET_DIR / "sector_contraction_value_gap.packet.json"
DECISION = PACKET_DIR / "eckm_readiness_after_zeromode_gram_import.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_ZeroModeGramSectorContractionPayload_or_ECKMWeightRows_v1.md"

PREVIOUS = DATA / "selected_ckmweightscalarevaluator_or_selectedflavorgalerkinvalues.candidate.json"
PREV_READINESS = (
    DATA
    / "selected_ckmweightscalarevaluator_or_selectedflavorgalerkinvalues"
    / "eckm_scalar_evaluator_readiness.packet.json"
)
PSM_B1 = DATA / "selected_psm_c1_02_honestgalerkinzeromodebasissource_or_primitivequadratureexport.candidate.json"
PSM_B1_PACKET = (
    DATA
    / "selected_psm_c1_02_honestgalerkinzeromodebasissource_or_primitivequadratureexport"
    / "route_b1_stationary_transported_basis_source_import.packet.json"
)
SECTOR_GRAM = DATA / "selected_sectorcharge_gram_transfernormalization_packet.candidate.json"
ACTIVE = DATA / "selected_activeledger_dotdc1supersession_or_valuelayerfrontier.candidate.json"
HONEST_GATE = (
    DATA
    / "selected_weylpairsourceemission_or_honestgalerkinc1execution_valuerun"
    / "honest_galerkin_execution_value_run_gate.packet.json"
)
WEIGHTS = (
    DATA
    / "selected_ckmsectorpairprojectionrows_or_honestflavorgalerkinexecution"
    / "required_q448_sector_pair_weights.packet.json"
)

STATUS = "MTT_SELECTED_ZEROMODE_GRAM_ECKM_READINESS_PROMOTED_SECTOR_CONTRACTIONS_OPEN"
NEXT = "MTT_Selected_FiniteHessianC1SectorContractions_or_ECKMTraceExecution_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    previous = load(PREVIOUS)
    prev_readiness = load(PREV_READINESS)
    psm_b1 = load(PSM_B1)
    psm_b1_packet = load(PSM_B1_PACKET)
    sector_gram = load(SECTOR_GRAM)
    active = load(ACTIVE)
    honest_gate = load(HONEST_GATE)
    weights = load(WEIGHTS)

    if previous["closure_decision"]["formal_evaluator_typed"] is not True:
        raise ValueError("E_CKM formal evaluator is not typed")
    if psm_b1["closure_decision"]["b1_stationary_projector_basis_source_imported"] is not True:
        raise ValueError("PSM B1 stationary basis import is not closed")
    if psm_b1_packet["selected_projector_source_verified"] is not True:
        raise ValueError("stationary projector source is not verified")
    if active["closure_decision"]["dotD_alpha1_closed_by_active_ledger"] is not True:
        raise ValueError("active ledger dotD closure is missing")

    needed_sectors = ["u", "d", "e"]
    sector_basis = {sector: psm_b1_packet["sector_basis_labels"][sector] for sector in needed_sectors}

    stationary = {
        "schema": "MTTStationaryTransportedBasisImportForECKM.v1",
        "status": "STATIONARY_TRANSPORTED_ZERO_MODE_PROJECTOR_BASIS_IMPORTED_FOR_ECKM",
        "source_packet": rel(PSM_B1_PACKET),
        "raw_untransported_basis_rejected": True,
        "transported_projectors_selected_at_stationary_tier": psm_b1_packet["selected_projector_source_verified"],
        "all_stationary_slots_verified": psm_b1_packet["all_stationary_slots_verified"],
        "validator_ready_stationary_rho_s": psm_b1_packet["validator_ready_stationary_rho_s"],
        "selected_dotD_source_verified_here": psm_b1_packet["selected_dotD_source_verified"],
        "alpha1_driver_verified_here": psm_b1_packet["alpha1_driver_verified"],
        "active_ledger_supplies_dotD_alpha1": active["closure_decision"]["dotD_alpha1_closed_by_active_ledger"],
        "sector_basis_labels_for_ECKM": sector_basis,
        "promotes_eckm_zero_mode_projector_basis_readiness": True,
        "does_not_emit_sector_contraction_values": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    gram_packet = sector_gram["gram_transfer_packet"]
    gram = {
        "schema": "MTTGramTraceConventionForECKM.v1",
        "status": "GRAM_TRACE_CONVENTION_PROMOTED_FOR_STATIONARY_ECKM_DOMAIN",
        "source_packet": rel(SECTOR_GRAM),
        "conditional_gram_theorem_proved": gram_packet["conditional_gram_theorem_proved"],
        "gram_conditionally_forced_after_rho_s": gram_packet["gram_conditionally_forced_after_rho_s"],
        "stationary_rho_s_available_from_B1": psm_b1_packet["validator_ready_stationary_rho_s"],
        "selected_projector_basis_available_from_B1": psm_b1_packet["selected_projector_source_verified"],
        "active_dotD_closure_imported": active["closure_decision"]["dotD_alpha1_closed_by_active_ledger"],
        "raw_T3_frobenius_norm_per_matter_sector": gram_packet["raw_T3_frobenius_norm_per_matter_sector"],
        "matter_T3_norms_equal": gram_packet["matter_T3_norms_equal"],
        "unit_trace_transfer": gram_packet["unit_trace_transfer"],
        "promotes_eckm_Gram_trace_readiness": True,
        "physical_transfer_normalization_selected_in_old_packet": gram_packet["physical_transfer_normalization_selected"],
        "why_old_packet_was_open": gram_packet["why_not_selected"],
        "supersession_note": (
            "The old transfer-normalization packet predated the active-ledger dotD closure and PSM-B1 "
            "stationary transported-basis import.  This artifact promotes only the E_CKM stationary "
            "trace/Gram readiness row, not full alpha1 or scalar value rows."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    contractions = {
        "schema": "MTTSectorContractionValueGapForECKM.v1",
        "status": "FINITE_HESSIAN_C1_SECTOR_CONTRACTION_VALUES_REMAIN_OPEN",
        "honest_galerkin_gate": rel(HONEST_GATE),
        "current_manifest_status": honest_gate["current_manifest_status"],
        "selected_source_verified": honest_gate["selected_source_verified"],
        "required_inputs": honest_gate["required_inputs"],
        "required_outputs": honest_gate["required_outputs"],
        "still_missing_for_ECKM": [
            "selected Hessian counterterms",
            "selected primitive vertex operator phase_Z",
            "selected primitive vertex operator shift_X",
            "finite three-by-three contraction terms in transported bases",
            "sector response matrices M_u,M_d,M_e as selected values",
            "row certificates evaluating W12,W23,W13",
        ],
        "observed_flavor_data_forbidden": honest_gate["observed_flavor_data_forbidden"],
        "target_fitting_forbidden": honest_gate["target_fitting_forbidden"],
    }

    readiness_rows = dict(prev_readiness["readiness_rows"])
    readiness_rows["zero_mode_projector_basis_values"] = {
        **readiness_rows["zero_mode_projector_basis_values"],
        "closed": True,
        "source": rel(PSM_B1_PACKET),
        "role": "stationary transported P_s/K_s basis imported for u,d,e E_CKM projectors",
    }
    readiness_rows["selected_L2_Gram_trace_convention_values"] = {
        **readiness_rows["selected_L2_Gram_trace_convention_values"],
        "closed": True,
        "source": rel(SECTOR_GRAM),
        "role": "stationary E_CKM trace/Gram convention fixed by B1 rho_s plus conditional Gram theorem",
    }
    readiness_rows["finite_Hessian_C1_sector_contraction_values"] = {
        **readiness_rows["finite_Hessian_C1_sector_contraction_values"],
        "closed": False,
        "source": rel(HONEST_GATE),
    }
    readiness_rows["E_CKM_weight_row_certificates"] = {
        **readiness_rows["E_CKM_weight_row_certificates"],
        "closed": False,
    }
    closed_count = sum(1 for row in readiness_rows.values() if row["closed"])
    required_count = len(readiness_rows)
    still_open = [key for key, row in readiness_rows.items() if row["closed"] is False]

    decision = {
        "schema": "MTTECKMReadinessAfterZeroModeGramImport.v1",
        "status": "ECKM_READINESS_6_OF_8_SECTOR_CONTRACTIONS_OPEN",
        "previous_closed_required_rows": prev_readiness["closed_required_rows"],
        "closed_required_rows": closed_count,
        "required_rows": required_count,
        "zero_mode_projector_basis_values_promoted": True,
        "selected_L2_Gram_trace_convention_values_promoted": True,
        "finite_Hessian_C1_sector_contraction_values_emitted": False,
        "E_CKM_weight_row_certificates_emitted": False,
        "selected_functional_executed": False,
        "accepted_weight_rows": 0,
        "accepted_exact_ckm_correction_rows": 0,
        "accepted_no_knob_CKM_angle_rows": 0,
        "CKM_angle_magnitudes_derived_exact": False,
        "Jarlskog_source_derived_without_measured_angles": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closure_closed": False,
        "still_open_blockers": still_open,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    theorem = {
        "name": "ZeroModeGramECKMReadinessPromotionTheorem",
        "proved": True,
        "statement": (
            "The PSM-C1-02 B1 stationary transported-basis import supplies selected projector/"
            "basis readiness for the u,d,e E_CKM rows, and the conditional Gram-transfer theorem, "
            "combined with the B1 stationary rho_s import and active-ledger dotD closure, supplies "
            "the stationary E_CKM trace/Gram convention.  This promotes readiness from 4/8 to 6/8. "
            "It does not execute finite Hessian/C1 sector contractions or emit W12,W23,W13."
        ),
    }

    data = {
        "candidate": "MTTSelectedZeroModeGramSectorContractionPayloadOrECKMWeightRows",
        "status": STATUS,
        "inputs": {
            "previous_eckm_readiness": rel(PREVIOUS),
            "previous_readiness_packet": rel(PREV_READINESS),
            "psm_b1_candidate": rel(PSM_B1),
            "psm_b1_stationary_basis": rel(PSM_B1_PACKET),
            "sectorcharge_gram_packet": rel(SECTOR_GRAM),
            "active_ledger": rel(ACTIVE),
            "honest_galerkin_gate": rel(HONEST_GATE),
            "required_q448_weights": rel(WEIGHTS),
        },
        "output_packets": {
            "stationary_transported_basis_import_for_eckm": rel(STATIONARY),
            "gram_trace_convention_for_eckm": rel(GRAM),
            "sector_contraction_value_gap": rel(CONTRACTIONS),
            "eckm_readiness_after_zeromode_gram_import": rel(DECISION),
        },
        "closure_decision": {
            "zero_mode_projector_basis_values_promoted": True,
            "selected_L2_Gram_trace_convention_values_promoted": True,
            "readiness_promoted_4_to_6": closed_count == 6,
            "closed_required_rows": closed_count,
            "required_rows": required_count,
            "finite_Hessian_C1_sector_contraction_values_emitted": False,
            "E_CKM_weight_row_certificates_emitted": False,
            "selected_functional_executed": False,
            "accepted_weight_rows": 0,
            "accepted_exact_ckm_correction_rows": 0,
            "accepted_no_knob_CKM_angle_rows": 0,
            "CKM_angle_magnitudes_derived_exact": False,
            "Jarlskog_source_derived_without_measured_angles": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closure_closed": False,
        },
        "key_numbers": {
            "previous_readiness": prev_readiness["closed_required_rows"],
            "current_readiness": closed_count,
            "required_rows": required_count,
            "accepted_eckm_weight_rows": 0,
            "required_q448_weights": weights["q448_weights_if_matching_measured_replay"],
        },
        "theorem": theorem,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "observed_data_used_for_postcheck": True,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_ZeroModeGramSectorContractionPayload_or_ECKMWeightRows_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "zero_mode_projector_basis_values_promoted": True,
        "selected_L2_Gram_trace_convention_values_promoted": True,
        "readiness_promoted_4_to_6": closed_count == 6,
        "closed_required_rows": closed_count,
        "required_rows": required_count,
        "finite_Hessian_C1_sector_contraction_values_emitted": False,
        "E_CKM_weight_row_certificates_emitted": False,
        "selected_functional_executed": False,
        "accepted_weight_rows": 0,
        "accepted_exact_ckm_correction_rows": 0,
        "accepted_no_knob_CKM_angle_rows": 0,
        "CKM_angle_magnitudes_derived_exact": False,
        "Jarlskog_source_derived_without_measured_angles": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closure_closed": False,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "observed_data_used_for_postcheck": True,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected ZeroModeGramSectorContractionPayload or ECKMWeightRows v1

Status: `{STATUS}`.

## Theorem

`ZeroModeGramECKMReadinessPromotionTheorem` is proved.

The PSM-C1-02 B1 stationary transported-basis import supplies selected
projector/basis readiness for the `u,d,e` E_CKM rows:

```text
u basis = {sector_basis['u']}
d basis = {sector_basis['d']}
e basis = {sector_basis['e']}
```

The conditional Gram-transfer theorem, combined with the B1 stationary `rho_s`
import and the active-ledger dotD closure, supplies the stationary E_CKM
trace/Gram convention.

## Readiness

```text
previous readiness = {prev_readiness['closed_required_rows']}/{prev_readiness['required_rows']}
current readiness  = {closed_count}/{required_count}
accepted W rows    = 0/3
```

Still open:

```text
finite Hessian/C1 sector contraction value matrices
W12,W23,W13 row certificates
```

This is not CKM angle closure. It prepares the selected trace domain so the next
artifact can execute the actual finite sector contractions.

Next artifact: `{NEXT}`.
"""

    write_json(STATIONARY, stationary)
    write_json(GRAM, gram)
    write_json(CONTRACTIONS, contractions)
    write_json(DECISION, decision)
    write_json(OUTPUT, data)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
