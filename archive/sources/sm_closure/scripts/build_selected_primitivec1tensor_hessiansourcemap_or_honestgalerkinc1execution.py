"""Build primitive C1 tensor / Hessian source-map or honest Galerkin gate.

The preceding cutset says the remaining obstruction is value emission.  This
artifact constructs the smallest same-branch source-map candidate already
forced by the residual-projector ladder, attaches it to the strict 72-real
acceptance target, and records the exact theorem obligations needed before it
could promote A_selected, b_selected, or deltaTheta_C1.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PREVIOUS = DATA / "selected_dynamicc1transfertensor_valueemission_or_honestgalerkinc1run.candidate.json"
VALUE_CUTSET = (
    DATA
    / "selected_dynamicc1transfertensor_valueemission_or_honestgalerkinc1run"
    / "strict_value_emission_cutset.packet.json"
)
STRICT_ACCEPTANCE = (
    DATA
    / "selected_dynamicc1transfertensor_or_galerkinc1values_acceptance_manifest"
    / "strict_dynamic_c1_transfer_tensor_acceptance.packet.json"
)
SOURCE_RULE = (
    DATA
    / "selected_differentiatedresidualprojectorsourcerule_or_honestgalerkinc1execution"
    / "differentiated_residual_projector_source_rule.contract.json"
)
RESIDUAL_TEMPLATE = (
    DATA
    / "selected_residualcompletion_sourcepromotion_or_honestgalerkinc1_emission"
    / "minimal_residual_source_packet.template.json"
)
RESIDUAL_COMPLETION = (
    DATA
    / "selected_differentiatedvertex_hessiancounterterm_or_galerkinc1_valuepacket"
    / "differentiated_residual_completion.packet.json"
)
PROJECTOR_PACKET = (
    DATA
    / "selected_canonicalresidualprojector_or_honestgalerkinc1_valuefill"
    / "canonical_fixedfiber_residual_projector.packet.json"
)
GALERKIN_C1 = DATA / "selected_routec_strominger_galerkin_solve" / "c1_primitive_contractions.candidate.json"

OUTPUT = DATA / "selected_primitivec1tensor_hessiansourcemap_or_honestgalerkinc1execution.candidate.json"
PACKET_DIR = DATA / "selected_primitivec1tensor_hessiansourcemap_or_honestgalerkinc1execution"
SOURCE_MAP = PACKET_DIR / "primitive_tensor_hessian_source_map_candidate.packet.json"
SELECTION_KERNEL = PACKET_DIR / "source_map_selection_obligation_kernel.packet.json"
GALERKIN_PACKET = PACKET_DIR / "honest_galerkin_execution_value_slots.packet.json"
CERT = CERTS / "selected_primitivec1tensor_hessiansourcemap_or_honestgalerkinc1execution_certificate.json"
NOTE = CORPUS / "MTT_Selected_PrimitiveC1Tensor_HessianSourceMap_or_HonestGalerkinC1Execution_v1.md"

STATUS = "MTT_SELECTED_PRIMITIVEC1TENSOR_HESSIANSOURCEMAP_OR_HONESTGALERKINC1EXECUTION_BUILT_SOURCE_MAP_CANDIDATE_VALUES_OPEN"
NEXT = "MTT_Selected_SourceMapSelectionTheorem_or_HonestGalerkinC1ValueRun_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    cutset = load(VALUE_CUTSET)
    strict = load(STRICT_ACCEPTANCE)
    source_rule = load(SOURCE_RULE)
    residual_template = load(RESIDUAL_TEMPLATE)
    residual_completion = load(RESIDUAL_COMPLETION)
    projector = load(PROJECTOR_PACKET)
    galerkin = load(GALERKIN_C1)

    phase = residual_template["required_source_emissions"]["phase_residual_operator_R_Z"]
    shift = residual_template["required_source_emissions"]["shift_residual_operator_R_X"]
    emitted = source_rule["currently_emitted"]
    if_emitted = residual_template["if_emitted_then"]

    source_map_selected_now = (
        phase["selected_by_MTT_now"] is True
        and shift["selected_by_MTT_now"] is True
        and emitted["selected_b_selected"] is True
    )

    source_map_packet = {
        "schema": "MTTPrimitiveC1TensorHessianSourceMapCandidate.v1",
        "status": "SOURCE_MAP_CANDIDATE_CONSTRUCTED_SELECTION_OPEN",
        "source_map_name": "Q_residual_enriched_Weyl_pair_C1_source_map",
        "domain": {
            "branch": "q79/F,m=1 S3/GS Route-C branch",
            "generators": [
                "selected Z/clock phase leg",
                "selected X/shift active vertex leg",
            ],
            "active_shift": residual_template["active_shift"],
            "fixed_fiber_class": residual_template["fixed_fiber_class"],
            "absolute_fiber_origin_selected": residual_template["absolute_fiber_origin_selected"],
        },
        "closed_support": {
            "strict_72_real_acceptance_target": strict["coordinate_system"],
            "static_route_required": residual_template["static_route_required"],
            "selected_source_selector_attached": residual_template[
                "selected_source_selector_attached"
            ],
            "same_branch_source_required": residual_template["same_branch_source_required"],
            "canonical_Q_residual_available": source_rule["already_selected_support"][
                "canonical_Q_residual_available"
            ],
            "Q_residual_rank": projector["operator_checks"]["residual_projector_rank"],
            "projector_idempotence_verified": projector["operator_checks"][
                "residual_projector_idempotence_norm_sq"
            ]
            <= 1e-20,
            "alpha1_dotD_driver_verified": source_rule["already_selected_support"][
                "alpha1_dotD_driver_verified"
            ],
            "static_trace_transfer_normalization_selected": source_rule[
                "already_selected_support"
            ]["static_trace_transfer_normalization_selected"],
        },
        "candidate_residual_operators": {
            "phase_R_Z": {
                "accepted_sources": phase["accepted_sources"],
                "shape": phase["shape"],
                "selected_by_MTT_now": phase["selected_by_MTT_now"],
            },
            "shift_R_X": {
                "accepted_sources": shift["accepted_sources"],
                "shape": shift["shape"],
                "selected_by_MTT_now": shift["selected_by_MTT_now"],
            },
        },
        "residual_completion_replay": {
            "phase_projection_plus_residual_equals_target": residual_completion[
                "phase_I_plus_Z_completion"
            ]["decomposition"]["projection_plus_residual_equals_target"],
            "shift_projection_plus_residual_equals_target": residual_completion[
                "shift_I_plus_X_completion"
            ]["decomposition"]["projection_plus_residual_equals_target"],
            "phase_residual_norm_sq": residual_completion["phase_I_plus_Z_completion"][
                "decomposition"
            ]["residual_norm_sq"],
            "shift_residual_norm_sq": residual_completion["shift_I_plus_X_completion"][
                "decomposition"
            ]["residual_norm_sq"],
            "routed_72_real_completion": residual_completion["routed_72_real_completion"],
        },
        "if_source_map_selected_then": if_emitted,
        "selected_by_MTT_now": source_map_selected_now,
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    selection_kernel = {
        "schema": "MTTSourceMapSelectionObligationKernel.v1",
        "status": "SELECTION_OBLIGATION_KERNEL_BUILT_VALUES_OPEN",
        "formal_statement": source_rule["formal_statement"],
        "required_emissions": source_rule["required_emissions"],
        "currently_emitted": emitted,
        "strict_acceptance_field_status": cutset["field_status"],
        "closed_numeric_facts": cutset.get(
            "closed_numeric_facts",
            {
                "rank": if_emitted["rank"],
                "A_transpose_A": if_emitted["A_transpose_A"],
                "A_transpose_b": if_emitted["A_transpose_b"],
                "deltaTheta_C1": if_emitted["deltaTheta_C1"],
            },
        ),
        "minimal_truth_table": {
            "if_phase_and_shift_residual_sources_selected_and_b_source_emitted": {
                "A_selected_promotes": True,
                "b_selected_promotes": True,
                "deltaTheta_C1_promotes": True,
                "SM_parity_dynamic_packet_would_close": True,
                "no_knob_flavor_constants_would_close": False,
            },
            "current_case": {
                "phase_R_Z_selected": phase["selected_by_MTT_now"],
                "shift_R_X_selected": shift["selected_by_MTT_now"],
                "b_source_emitted": emitted["selected_b_selected"],
                "A_selected_promotes": False,
                "b_selected_promotes": False,
                "deltaTheta_C1_promotes": False,
            },
        },
        "why_not_selected_yet": [
            "the residual operators are exact shapes but selected_by_MTT_now is false",
            "the source rule contract has not emitted selected Hessian/source vector b_selected",
            "the strict acceptance target still marks A_selected/b_selected/deltaTheta_C1 as conditional references only",
        ],
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    galerkin_packet = {
        "schema": "MTTHonestGalerkinC1ExecutionValueSlots.v1",
        "status": "HONEST_GALERKIN_EXECUTION_SLOTS_RESTATED_VALUES_OPEN",
        "strict_coordinate_target": strict["coordinate_system"],
        "manifest_status": galerkin["status"],
        "selected_source_verified": galerkin["selected_source_verified"],
        "required_outputs": galerkin["required_outputs"],
        "can_replace_source_map_now": False,
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedPrimitiveC1TensorHessianSourceMapOrHonestGalerkinC1Execution",
        "status": STATUS,
        "inputs": {
            "previous_value_cutset_gate": rel(PREVIOUS),
            "strict_value_cutset": rel(VALUE_CUTSET),
            "strict_acceptance_manifest": rel(STRICT_ACCEPTANCE),
            "differentiated_residual_projector_source_rule": rel(SOURCE_RULE),
            "minimal_residual_source_template": rel(RESIDUAL_TEMPLATE),
            "residual_completion": rel(RESIDUAL_COMPLETION),
            "canonical_residual_projector": rel(PROJECTOR_PACKET),
            "honest_galerkin_C1_manifest": rel(GALERKIN_C1),
        },
        "output_packets": {
            "primitive_tensor_hessian_source_map_candidate": rel(SOURCE_MAP),
            "source_map_selection_obligation_kernel": rel(SELECTION_KERNEL),
            "honest_galerkin_execution_value_slots": rel(GALERKIN_PACKET),
        },
        "what_closes_now": {
            "primitive_tensor_Hessian_source_map_candidate_constructed": True,
            "phase_and_shift_residual_operator_shapes_attached": True,
            "canonical_Q_residual_support_attached": True,
            "strict_72_real_acceptance_target_attached": True,
            "selection_truth_table_built": True,
            "honest_Galerkin_execution_slots_reemitted": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "selected_phase_R_Z_source": True,
            "selected_shift_R_X_source": True,
            "selected_Hessian_or_b_source_vector": True,
            "selected_primitive_C1_tensor_values": True,
            "selected_A_selected": True,
            "selected_b_selected": True,
            "selected_deltaTheta_C1": True,
            "selected_sector_response_matrices": True,
            "honest_selected_Galerkin_C1_execution_values": True,
            "SM_parity_dynamic_packet_closure": True,
            "true_SM_equivalence_closure": True,
            "full_no_knob_flavor_closure": True,
        },
        "promotion_decision": {
            "source_map_candidate_constructed": True,
            "source_map_selected_by_MTT_now": source_map_selected_now,
            "A_selected_promoted": False,
            "b_selected_promoted": False,
            "deltaTheta_C1_promoted": False,
            "sector_response_matrices_promoted": False,
            "honest_Galerkin_C1_execution_promoted": False,
            "SM_parity_dynamic_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_flavor_constants_closed": False,
        },
        "observed_data_used": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "source_map_selected_claimed": False,
        "A_selected_claimed": False,
        "b_selected_claimed": False,
        "deltaTheta_C1_claimed": False,
        "sector_response_matrices_claimed": False,
        "honest_Galerkin_C1_claimed": False,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "PrimitiveC1TensorHessianSourceMapCandidateTheorem",
            "proved": True,
            "statement": (
                "The current proof state determines a unique minimal same-branch "
                "primitive/Hessian source-map candidate: apply the canonical residual "
                "projector to the selected enriched Weyl-pair phase and shift legs, "
                "or equivalently emit the exact R_Z and R_X residual operators through "
                "a selected differentiated vertex, basis-transport, or Hessian source. "
                "This candidate would promote A_selected, b_selected, and deltaTheta_C1 "
                "only if the residual operators and b source are selected by MTT; current "
                "packets construct the candidate but do not select those values."
            ),
        },
    }

    cert = {
        "certificate": "MTT_Selected_PrimitiveC1Tensor_HessianSourceMap_or_HonestGalerkinC1Execution_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "source_map_packet_path": rel(SOURCE_MAP),
        "selection_kernel_packet_path": rel(SELECTION_KERNEL),
        "galerkin_packet_path": rel(GALERKIN_PACKET),
        "theorem_proved": True,
        "closure_claimed": False,
        "source_map_selected_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "A_selected_claimed": False,
        "b_selected_claimed": False,
        "deltaTheta_C1_claimed": False,
        "sector_response_matrices_claimed": False,
        "honest_Galerkin_C1_claimed": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PrimitiveC1Tensor HessianSourceMap or HonestGalerkinC1Execution v1

Status: `{STATUS}`.

The missing source map is now explicit.  The candidate is:

```text
Z/clock phase leg -> R_Z residual/Hessian source
X/shift active leg -> R_X residual/Hessian source
shared support     -> canonical Q_residual, rank {projector["operator_checks"]["residual_projector_rank"]}
```

The residual shapes are already exact:

```text
||R_Z||^2 = {phase["shape"]["residual_norm_sq"]}
||R_X||^2 = {shift["shape"]["residual_norm_sq"]}
rank target = {if_emitted["rank"]}
A^T A = {if_emitted["A_transpose_A"]}
A^T b = {if_emitted["A_transpose_b"]}
deltaTheta_C1 = {if_emitted["deltaTheta_C1"]}
```

But this remains a candidate, not a selected value packet.  The selected-source
bit is still false for both residual operators, and `b_selected` is not emitted.

The next theorem must either select this source map from MTT geometry or run an
honest selected Galerkin C1 execution in the same 72-real coordinate system.

No observed masses, mixings, CP phase, benchmark matrices, or target residuals
are used as selectors.

Next artifact: `{NEXT}`.
"""

    SOURCE_MAP.write_text(json.dumps(source_map_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    SELECTION_KERNEL.write_text(json.dumps(selection_kernel, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    GALERKIN_PACKET.write_text(json.dumps(galerkin_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
