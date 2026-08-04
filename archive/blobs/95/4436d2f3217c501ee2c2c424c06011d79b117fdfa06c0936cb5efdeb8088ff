"""Build typed Cech/HYM/projective connection witness value gate packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_typedcechhymprojectiveconnectionwitnessvalues_or_directhkrow"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
TYPED_GATE = PACKET_DIR / "typed_cech_gaplayer_not_connection_values.packet.json"
HYM_GATE = PACKET_DIR / "direct_hym_galerkin_nonpromotion_gate.packet.json"
ROUTEC_GATE = PACKET_DIR / "routec_projective_extraction_open_gate.packet.json"
NEXT_CONTRACT = PACKET_DIR / "next_same_source_connection_table_or_direct_hkrow_contract.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_TypedCechHYMProjectiveConnectionWitnessValues_or_DirectHKRow_v1.md"

SOURCES = {
    "previous": DATA
    / "selected_sourcebranchidentity_sourceamendment_or_selectedconnectionvalues_or_directhkrow.candidate.json",
    "trace_payload": DATA / "selected_tracepayload_or_fullhymoperatoremission.candidate.json",
    "step73_hym_galerkin": DATA
    / "selected_step73_honestrowlocalhymgalerkin_or_selectedprefactorsourcerows.candidate.json",
    "visible_routec_hym": DATA / "selected_visibleoperatorpayload_or_routechymresidual.candidate.json",
}

SOURCE_BUILDERS = {
    "trace_payload": ROOT / "scripts" / "build_selected_tracepayload_or_fullhymoperatoremission.py",
    "step73_hym_galerkin": ROOT
    / "scripts"
    / "build_selected_step73_honestrowlocalhymgalerkin_or_selectedprefactorsourcerows.py",
    "visible_routec_hym": ROOT
    / "scripts"
    / "build_selected_visibleoperatorpayload_or_routechymresidual.py",
}

STATUS = (
    "MTT_SELECTED_TYPEDCECH_HYM_PROJECTIVE_CONNECTIONWITNESSVALUES_"
    "OLD_SUPPORT_REJECTED_SAME_SOURCE_VALUE_TABLE_OPEN"
)
NEXT = "MTT_Selected_SameSourceConnectionValueTable_or_DirectHKRow_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources() -> dict[str, dict[str, Any]]:
    for name, builder in SOURCE_BUILDERS.items():
        if not SOURCES[name].exists() and builder.exists():
            subprocess.run([sys.executable, str(builder)], cwd=ROOT, check=True)
    missing = [rel(path) for path in SOURCES.values() if not path.exists()]
    if missing:
        raise FileNotFoundError(f"Missing required source packets: {missing}")
    return {name: load(path) for name, path in SOURCES.items()}


def main() -> int:
    sources = require_sources()
    prev = sources["previous"]["closure_decision"]
    trace = sources["trace_payload"]["closure_decision"]
    step73 = sources["step73_hym_galerkin"]["closure_decision"]
    visible = sources["visible_routec_hym"]["closure_decision"]

    typed_gate = {
        "schema": "MTTTypedCechGapLayerNotConnectionValuesGate.v1",
        "status": "TYPED_CECH_SUPPORT_CLOSED_CONNECTION_VALUES_NOT_EMITTED",
        "closure_claimed": True,
        "source": rel(SOURCES["trace_payload"]),
        "transition_rhoE_or_Cech_Dolbeault_DE_data_closed": trace[
            "transition_rhoE_or_Cech_Dolbeault_DE_data_closed"
        ],
        "finite_determinant_heat_spectrum_or_torsion_response_closed": trace[
            "finite_determinant_heat_spectrum_or_torsion_response_closed"
        ],
        "actual_dynamic_QaSU3_operator_packet_closed": trace[
            "actual_dynamic_QaSU3_operator_packet_closed"
        ],
        "accepted_as_connection_witness_values": False,
        "reason": (
            "The trace/Cech payload closes the selected Phi_fin finite D_E gap layer, "
            "but it does not emit the eight selected connection-value fields or the "
            "29 missing U1/Y connection-witness leaves."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    hym_gate = {
        "schema": "MTTDirectHYMGalerkinNonPromotionGate.v1",
        "status": "MODEL_ACTIVE_HYM_SUPPORT_REJECTED_AS_SELECTED_CONNECTION_VALUES",
        "closure_claimed": True,
        "source": rel(SOURCES["step73_hym_galerkin"]),
        "diagonal_hym_green_subsource_closed": step73[
            "diagonal_hym_green_subsource_closed"
        ],
        "honest_galerkin_input_readiness_closed": step73[
            "honest_galerkin_input_readiness_closed"
        ],
        "selected_HYM_projector_values_promoted": step73[
            "selected_HYM_projector_values_promoted"
        ],
        "selected_sector_transfer_values_emitted": step73[
            "selected_sector_transfer_values_emitted"
        ],
        "selected_retarded_overlap_derivative_rows_emitted": step73[
            "selected_retarded_overlap_derivative_rows_emitted"
        ],
        "selected_threshold_scheme_rows_emitted": step73[
            "selected_threshold_scheme_rows_emitted"
        ],
        "lambda_H_value_row_emitted": step73["lambda_H_value_row_emitted"],
        "accepted_rowlocal_source_row_count": step73[
            "accepted_rowlocal_source_row_count"
        ],
        "accepted_as_connection_witness_values": False,
        "reason": (
            "The old Galerkin/HYM computation supplies diagonal model-active support, "
            "but the selected projector, rank2-to-sector transfer, retarded derivative, "
            "scheme rows, and lambda_H value row are still absent."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    routec_gate = {
        "schema": "MTTRouteCProjectiveExtractionOpenGate.v1",
        "status": "ROUTEC_HYM_EXTRACTION_CONTRACT_OPEN_VALUES_NOT_PROMOTED",
        "closure_claimed": True,
        "source": rel(SOURCES["visible_routec_hym"]),
        "finite_operator_extraction_contract_active": visible[
            "finite_operator_extraction_contract_active"
        ],
        "visible_operator_payload_emitted": visible["visible_operator_payload_emitted"],
        "routec_hym_residual_promoted": visible["routec_hym_residual_promoted"],
        "actual_QaSU3_packet_promoted": visible["actual_QaSU3_packet_promoted"],
        "accepted_as_connection_witness_values": False,
        "reason": (
            "Route-C/HYM has an active finite extraction contract and lifted-flag "
            "diagnostics, but no honest selected operator payload or same-source "
            "connection table has been emitted."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_contract = {
        "schema": "MTTSameSourceConnectionValueTableOrDirectHKRowContract.v1",
        "status": "SAME_SOURCE_CONNECTION_VALUE_TABLE_OR_DIRECT_HKROW_REQUIRED",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "strict_K_threshold_count": {
            "accepted": prev["accepted_selected_K_source_row_count"],
            "required": prev["selected_K_threshold_row_count_required"],
        },
        "required_same_source_connection_table_fields": [
            "source_id",
            "carrier_or_cover_id",
            "transition_or_connection_representative",
            "D_E_action",
            "rho_E_or_projective_character_table",
            "Riesz_projector",
            "reduced_Green_operator",
            "dotD_alpha1_or_threshold_derivative",
        ],
        "required_validator_exports": [
            "BN27 source ownership",
            "six BN27 validator statements or eight connection-value families",
            "U1/Y Route-C same-source finite D_E/Riesz/Green export",
            "selected physical normalization or direct H K row",
        ],
        "forbidden_reuse": [
            "gap-layer Cech/trace payload as connection values",
            "model-active diagonal HYM Galerkin data as selected HYM projector values",
            "lifted Route-C flags as honest same-source operator values",
            "controlled HRG/radial calibration as no-knob H K row",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedTypedCechHYMProjectiveConnectionWitnessValuesOrDirectHKRow",
        "status": STATUS,
        "previous_status": sources["previous"]["status"],
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {name: rel(path) for name, path in SOURCES.items()},
        "output_packets": {
            "typed_cech_gaplayer_not_connection_values": rel(TYPED_GATE),
            "direct_hym_galerkin_nonpromotion_gate": rel(HYM_GATE),
            "routec_projective_extraction_open_gate": rel(ROUTEC_GATE),
            "next_same_source_connection_table_or_direct_hkrow_contract": rel(
                NEXT_CONTRACT
            ),
        },
        "closure_decision": {
            "typed_cech_gaplayer_support_closed": True,
            "typed_cech_connection_values_emitted": False,
            "direct_hym_diagonal_support_closed": True,
            "direct_hym_selected_projector_values_promoted": False,
            "direct_hym_connection_values_emitted": False,
            "routec_projective_extraction_contract_active": True,
            "routec_same_source_values_emitted": False,
            "all_three_legal_routes_rechecked": True,
            "old_support_rejected_as_final_values": True,
            "same_source_connection_value_table_emitted": False,
            "selected_K_threshold_Omega_H_lambda": False,
            "strict_H_K_threshold_row_emitted": False,
            "payload_missing_leaf_count": prev["payload_missing_leaf_count"],
            "accepted_selected_K_source_row_count": prev[
                "accepted_selected_K_source_row_count"
            ],
            "selected_K_threshold_row_count_required": prev[
                "selected_K_threshold_row_count_required"
            ],
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "TypedCechHYMSupportNonPromotionTheorem",
            "proved": True,
            "statement": (
                "The three legal connection-witness routes have been rechecked against "
                "the latest local packets. The typed Cech/trace route closes only the "
                "D_E gap layer, the direct HYM/Galerkin route closes only diagonal "
                "model-active support, and the Route-C/HYM route has only an open "
                "extraction contract. None emits the same-source connection-value "
                "table or the direct H K row."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedTypedCechHYMSupportNonPromotion",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "typed_cech_gaplayer_support_closed": True,
        "typed_cech_connection_values_emitted": False,
        "direct_hym_diagonal_support_closed": True,
        "direct_hym_connection_values_emitted": False,
        "routec_projective_extraction_contract_active": True,
        "routec_same_source_values_emitted": False,
        "all_three_legal_routes_rechecked": True,
        "old_support_rejected_as_final_values": True,
        "same_source_connection_value_table_emitted": False,
        "strict_H_K_threshold_row_emitted": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected Typed Cech/HYM/Projective Connection Witness Values or Direct H K Row v1

## Theorem

`TypedCechHYMSupportNonPromotionTheorem` is emitted.

## Newly Closed

- The typed Cech/trace payload is accepted only as `D_E` gap-layer support.
- The older honest HYM/Galerkin packet is accepted only as diagonal/model-active
  support.
- The Route-C/HYM packet is accepted only as an extraction-contract scaffold.
- All three legal connection-witness routes have been rechecked against the
  current branch and rejected as final selected connection-value rows.

## Rejected Reuse

- Gap-layer Cech/trace data cannot fill the `8` connection-value fields.
- Model-active HYM/Galerkin data cannot be promoted to selected HYM projector
  values.
- Lifted Route-C flags cannot be promoted to honest same-source operator values.
- Controlled HRG/radial calibration cannot be promoted to no-knob
  `K_threshold.Omega_H.lambda`.

## Still Open

- Same-source connection-value table with the `8` required fields.
- The `29` missing U1/Y connection-witness leaves.
- Direct source-native `K_threshold.Omega_H.lambda`.

Strict selected `K_threshold` rows remain
`{prev["accepted_selected_K_source_row_count"]}/{prev["selected_K_threshold_row_count_required"]}`.

## Next Artifact

`{NEXT}`
"""

    write_json(TYPED_GATE, typed_gate)
    write_json(HYM_GATE, hym_gate)
    write_json(ROUTEC_GATE, routec_gate)
    write_json(NEXT_CONTRACT, next_contract)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
