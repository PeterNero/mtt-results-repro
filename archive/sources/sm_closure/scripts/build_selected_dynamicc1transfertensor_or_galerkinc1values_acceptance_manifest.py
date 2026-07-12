"""Build strict acceptance manifest for selected dynamic C1 transfer tensor values."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PREVIOUS = DATA / "selected_enrichedweylpairsourceprovenance_or_galerkinc1values.candidate.json"
STATIC_PACKET = (
    DATA
    / "selected_enrichedweylpairsourceprovenance_or_galerkinc1values"
    / "static_enriched_weylpair_source_provenance.packet.json"
)
DYNAMIC_PACKET = (
    DATA
    / "selected_enrichedweylpairsourceprovenance_or_galerkinc1values"
    / "dynamic_c1_value_boundary.packet.json"
)
GALERKIN_PACKET = (
    DATA
    / "selected_enrichedweylpairsourceprovenance_or_galerkinc1values"
    / "galerkin_c1_values_fallback.packet.json"
)
PHIFIN_TEMPLATE = (
    DATA
    / "selected_differentiated_phifinc1_primitiveoverlap_or_galerkinrun"
    / "primitive_overlap_contractions.template.json"
)
VALUE_RUN = (
    DATA
    / "selected_weylpairsourceemission_or_honestgalerkinc1execution_valuerun"
    / "conditional_weylpair_value_run.packet.json"
)

OUTPUT = DATA / "selected_dynamicc1transfertensor_or_galerkinc1values_acceptance_manifest.candidate.json"
PACKET_DIR = DATA / "selected_dynamicc1transfertensor_or_galerkinc1values_acceptance_manifest"
STRICT = PACKET_DIR / "strict_dynamic_c1_transfer_tensor_acceptance.packet.json"
DUAL = PACKET_DIR / "dual_path_value_fill_contract.packet.json"
CERT = CERTS / "selected_dynamicc1transfertensor_or_galerkinc1values_acceptance_manifest_certificate.json"
NOTE = CORPUS / "MTT_Selected_DynamicC1TransferTensor_or_GalerkinC1Values_AcceptanceManifest_v1.md"

STATUS = "MTT_SELECTED_DYNAMICC1TRANSFERTENSOR_OR_GALERKINC1VALUES_ACCEPTANCE_MANIFEST_BUILT_VALUES_OPEN"
NEXT = "MTT_Selected_DynamicC1TransferTensor_ValueEmission_or_HonestGalerkinC1Run_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    static = load(STATIC_PACKET)
    dynamic = load(DYNAMIC_PACKET)
    galerkin = load(GALERKIN_PACKET)
    phifin = load(PHIFIN_TEMPLATE)
    value_run = load(VALUE_RUN)

    strict_packet = {
        "schema": "MTTStrictDynamicC1TransferTensorAcceptance.v1",
        "status": "STRICT_ACCEPTANCE_MANIFEST_BUILT_VALUES_OPEN",
        "coordinate_system": {
            "name": "fixed_72_real_C1_coordinate_system",
            "sectors": ["u", "e", "d", "nuD"],
            "per_sector_matrix_shape": [3, 3],
            "real_coordinates_per_sector": 18,
            "total_real_coordinates": 72,
        },
        "static_source_prerequisites": {
            "static_enriched_weylpair_source_provenance_closed": static["provenance_closed"],
            "phase_route": static["static_sector_route"]["phase_Z_to"],
            "shift_route": static["static_sector_route"]["shift_X_to"],
            "singlet_rule": static["static_sector_route"]["shift_non10_side"]["matter_slots"],
            "trace_transfer_normalization_selected": static["static_normalization"][
                "static_trace_innerproduct_normalization_selected"
            ],
        },
        "dynamic_value_acceptance": {
            "A_selected_72_real_columns_required": True,
            "b_selected_72_real_source_vector_required": True,
            "deltaTheta_C1_must_be_solved_from_selected_values": True,
            "required_rank_or_replacement_theorem": 2,
            "must_report_A_transpose_A": True,
            "must_report_A_transpose_b": True,
            "must_report_sector_response_matrices": True,
            "must_report_nonzero_family_rank_or_countertheorem": True,
            "must_not_use_observed_flavor_constants": True,
            "must_not_select_by_target_residual": True,
        },
        "conditional_reference_not_a_promotion": {
            "rank": value_run["rank"],
            "condition_number": value_run["condition_number"],
            "A_transpose_A_if_promoted": value_run["A_transpose_A_if_promoted"],
            "A_transpose_b_if_promoted": value_run["A_transpose_b_if_promoted"],
            "deltaTheta_if_promoted": value_run["deltaTheta_conditional"],
            "operator_is_A_selected": False,
            "source_vector_is_b_selected": False,
        },
        "current_value_status": {
            "dynamic_transfer_tensor_emitted": False,
            "A_selected_emitted": False,
            "b_selected_emitted": False,
            "deltaTheta_C1_promoted": False,
            "honest_Galerkin_values_emitted": False,
            "SM_parity_dynamic_packet_closed": False,
        },
    }

    dual_packet = {
        "schema": "MTTDualPathDynamicC1ValueFillContract.v1",
        "status": "DUAL_PATH_CONTRACT_READY_VALUES_OPEN",
        "lane_A_same_source_dynamic_transfer": {
            "description": "Promote selected Phi_fin^C1 differentiated transfer from the same source spine.",
            "required_inputs": [
                "selected differentiated Phi_fin^C1 source-to-C1 transfer tensor",
                "selected primitive C1 overlap contractions or equivalent Hessian blocks",
                "selected Hessian/source-vector normalization emitting b_selected",
                "same-source proof tying the emitted tensor to the static Weyl route",
            ],
            "acceptance_outputs": [
                "A_selected_72_real_columns",
                "b_selected_72_real_source_vector",
                "deltaTheta_C1",
                "sector_response_matrices",
            ],
            "currently_closed": False,
        },
        "lane_B_honest_galerkin_c1_run": {
            "description": "Replace the conditional Weyl packet with selected Galerkin C1 contractions.",
            "required_inputs": galerkin["required_inputs"],
            "acceptance_checks": galerkin["acceptance_checks"],
            "required_outputs": galerkin["required_outputs"],
            "currently_closed": False,
        },
        "template_alignment": {
            "primitive_overlap_template": rel(PHIFIN_TEMPLATE),
            "template_requires_A_columns": "A_selected_72_real_columns"
            in json.dumps(phifin),
            "template_requires_b_vector": "b_selected_72_real_source_vector"
            in json.dumps(phifin),
        },
        "superset_strategy": {
            "straight_path": "Lane A: selected same-source dynamic transfer theorem.",
            "superset_path": "Lane B: independent honest Galerkin C1 execution may replace the conditional Weyl packet.",
            "locked_target": "Both lanes must emit the same typed 72-real C1 objects before any SM-parity dynamic closure claim.",
        },
    }

    candidate = {
        "candidate": "MTTSelectedDynamicC1TransferTensorOrGalerkinC1ValuesAcceptanceManifest",
        "status": STATUS,
        "inputs": {
            "previous_static_provenance_gate": rel(PREVIOUS),
            "static_packet": rel(STATIC_PACKET),
            "dynamic_boundary_packet": rel(DYNAMIC_PACKET),
            "galerkin_fallback_packet": rel(GALERKIN_PACKET),
            "primitive_overlap_template": rel(PHIFIN_TEMPLATE),
            "conditional_value_run": rel(VALUE_RUN),
        },
        "output_packets": {
            "strict_acceptance": rel(STRICT),
            "dual_path_contract": rel(DUAL),
        },
        "what_closes_now": {
            "dynamic_C1_acceptance_manifest": True,
            "lane_A_lane_B_target_equivalence": True,
            "72_real_coordinate_target_locked": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "selected_dynamic_source_to_C1_transfer_tensor": True,
            "selected_primitive_C1_overlap_contractions": True,
            "theorem_derived_A_selected": True,
            "theorem_derived_b_selected": True,
            "selected_deltaTheta_C1": True,
            "honest_selected_Galerkin_C1_execution_values": True,
            "SM_parity_dynamic_packet_closure": True,
            "true_SM_equivalence_closure": True,
            "full_no_knob_flavor_closure": True,
        },
        "promotion_decision": {
            "A_selected_promoted": False,
            "b_selected_promoted": False,
            "deltaTheta_C1_promoted": False,
            "honest_Galerkin_C1_execution_promoted": False,
            "SM_parity_dynamic_packet_closed": False,
        },
        "observed_data_used": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_DynamicC1TransferTensor_or_GalerkinC1Values_AcceptanceManifest_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "strict_acceptance_packet_path": rel(STRICT),
        "dual_path_contract_path": rel(DUAL),
        "closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected DynamicC1TransferTensor or GalerkinC1Values AcceptanceManifest v1

Status: `{STATUS}`.

This does not emit new physical values.  It locks the exact target that the
next proof/calculation must fill after the static enriched Weyl-pair provenance
gate:

```text
fixed C1 coordinate system: 4 sectors x 3x3 complex = 72 real coordinates
Lane A: selected same-source dynamic Phi_fin^C1 transfer tensor
Lane B: honest selected Galerkin C1 contraction run
Locked target: A_selected, b_selected, deltaTheta_C1, sector response matrices
```

The current conditional reference remains useful but unpromoted:

```text
A^T A = {value_run["A_transpose_A_if_promoted"]}
A^T b = {value_run["A_transpose_b_if_promoted"]}
deltaTheta = {value_run["deltaTheta_conditional"]}
```

The superset strategy is now explicit: Lane A and Lane B are different routes,
but both are constrained to emit the same typed 72-real C1 objects.  Neither
observed flavor constants nor target residuals may select the source.

Next artifact: `{NEXT}`.
"""

    STRICT.write_text(json.dumps(strict_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    DUAL.write_text(json.dumps(dual_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
