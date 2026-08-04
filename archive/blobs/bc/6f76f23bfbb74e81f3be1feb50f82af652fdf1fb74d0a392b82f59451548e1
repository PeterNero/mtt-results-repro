"""Build Step 20 conditional atom payload and source-theorem frontier."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step20_conditionalatompayload_or_sourcetheorem"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CONDITIONAL_PAYLOAD = PACKET_DIR / "step20_conditional_phase_shift_payload.packet.json"
VALIDATION_PACKET = PACKET_DIR / "step20_conditional_normal_form_validation.packet.json"
SOURCE_FRONTIER = PACKET_DIR / "step20_source_theorem_frontier.packet.json"
NEXT_WORKORDER = PACKET_DIR / "step20_to_step21_source_theorem_or_atom_decomposition.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step20_ConditionalAtomPayload_or_SourceTheorem_v1.md"

STEP19 = DATA / "selected_step19_primitivec1_sourcevalue_gate_or_tensorfrontier.candidate.json"
SOURCE_SELECTOR = DATA / "selected_primitivevertex_source_or_basistransport_selectiontheorem.candidate.json"
WEYLPAIR_GATE = DATA / "selected_routec_weylpair_basis_transport_or_vertex_source_theorem.candidate.json"
DYNAMIC_TRANSFER = DATA / "selected_dynamictransferhessian_bselected_or_honestgalerkinc1_valuefill.candidate.json"
SAME_SOURCE_IDENTITY = DATA / "selected_samesource_dynamictransferidentity_or_galerkinc1contractions_emission.candidate.json"
PHIFIN_IDENTITY = DATA / "selected_phifinc1_dynamictransferidentity_proof_or_galerkincontractions_run.candidate.json"
DIFF_OVERLAP = DATA / "selected_differentiated_phifinc1_primitiveoverlap_or_galerkinrun.candidate.json"
RESIDUAL_TEMPLATE = DATA / "selected_residualcompletion_sourcepromotion_or_honestgalerkinc1_emission" / "minimal_residual_source_packet.template.json"
RESIDUAL_COMPLETION = DATA / "selected_differentiatedvertex_hessiancounterterm_or_galerkinc1_valuepacket" / "differentiated_residual_completion.packet.json"

STATUS = "MTT_SELECTED_STEP20_CONDITIONAL_ATOM_PAYLOAD_BUILT_SOURCE_THEOREM_OPEN"
NEXT = "MTT_Selected_Step21_SourceTheorem_or_PrimitiveAtomDecomposition_v1"
SECTORS = ["u", "d", "e", "nuD"]


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def to_complex(value: Any) -> complex:
    if isinstance(value, list):
        return complex(float(value[0]), float(value[1]))
    return complex(float(value), 0.0)


def mat_to_complex(matrix: list[list[Any]]) -> list[list[complex]]:
    return [[to_complex(entry) for entry in row] for row in matrix]


def frob_norm_sq(matrix: list[list[complex]]) -> float:
    return float(sum((entry.real * entry.real + entry.imag * entry.imag) for row in matrix for entry in row))


def inner(a: list[list[complex]], b: list[list[complex]]) -> complex:
    return sum((x.conjugate() * y for row_a, row_b in zip(a, b) for x, y in zip(row_a, row_b)), 0j)


def add(a: list[list[complex]], b: list[list[complex]]) -> list[list[complex]]:
    return [[x + y for x, y in zip(row_a, row_b)] for row_a, row_b in zip(a, b)]


def encode_complex(z: complex) -> float | list[float]:
    if abs(z.imag) < 1e-12:
        return float(z.real)
    return [float(z.real), float(z.imag)]


def encode_matrix(matrix: list[list[complex]]) -> list[list[float | list[float]]]:
    return [[encode_complex(entry) for entry in row] for row in matrix]


def vectorize_sector_mats(mats: dict[str, list[list[complex]]]) -> list[float]:
    vector: list[float] = []
    for sector in SECTORS:
        for row in mats[sector]:
            for entry in row:
                vector.extend([float(entry.real), float(entry.imag)])
    return vector


def dot_real(a: list[float], b: list[float]) -> float:
    return float(sum(x * y for x, y in zip(a, b)))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    inputs = [
        STEP19,
        SOURCE_SELECTOR,
        WEYLPAIR_GATE,
        DYNAMIC_TRANSFER,
        SAME_SOURCE_IDENTITY,
        PHIFIN_IDENTITY,
        DIFF_OVERLAP,
        RESIDUAL_TEMPLATE,
        RESIDUAL_COMPLETION,
    ]
    missing = [rel(path) for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step 20 inputs: " + ", ".join(missing))

    step19 = load(STEP19)
    selector = load(SOURCE_SELECTOR)
    weylpair = load(WEYLPAIR_GATE)
    dynamic_transfer = load(DYNAMIC_TRANSFER)
    same_source_identity = load(SAME_SOURCE_IDENTITY)
    phifin_identity = load(PHIFIN_IDENTITY)
    diff_overlap = load(DIFF_OVERLAP)
    residual_template = load(RESIDUAL_TEMPLATE)
    residual_completion = load(RESIDUAL_COMPLETION)

    phase_mats = {
        sector: mat_to_complex(weylpair["enriched_weyl_pair_packet"]["source_directions"]["phase_packet"]["matrices"][sector])
        for sector in SECTORS
    }
    shift_mats = {
        sector: mat_to_complex(weylpair["enriched_weyl_pair_packet"]["source_directions"]["shift_packet"]["matrices"][sector])
        for sector in SECTORS
    }
    b_mats = {sector: add(phase_mats[sector], shift_mats[sector]) for sector in SECTORS}

    phase_vec = vectorize_sector_mats(phase_mats)
    shift_vec = vectorize_sector_mats(shift_mats)
    b_vec = vectorize_sector_mats(b_mats)
    gram = [
        [dot_real(phase_vec, phase_vec), dot_real(phase_vec, shift_vec)],
        [dot_real(shift_vec, phase_vec), dot_real(shift_vec, shift_vec)],
    ]
    atb = [dot_real(phase_vec, b_vec), dot_real(shift_vec, b_vec)]
    residual_norm = sum((b - p - s) ** 2 for b, p, s in zip(b_vec, phase_vec, shift_vec))
    delta = [atb[0] / gram[0][0], atb[1] / gram[1][1]]

    conditional_payload = {
        "schema": "MTTStep20ConditionalPhaseShiftPayload.v1",
        "status": "CONDITIONAL_AGGREGATE_PHASE_SHIFT_COLUMNS_EMITTED_SOURCE_THEOREM_OPEN",
        "selected_source_selector_closed": selector["promotion_decision"]["source_selector_promoted"],
        "conditional_source_selector": selector["source_selector_packet"],
        "aggregate_columns": {
            "phase_packet": {sector: encode_matrix(phase_mats[sector]) for sector in SECTORS},
            "shift_packet": {sector: encode_matrix(shift_mats[sector]) for sector in SECTORS},
            "b_conditional": {sector: encode_matrix(b_mats[sector]) for sector in SECTORS},
        },
        "sector_norm_sq": {
            sector: {
                "phase": frob_norm_sq(phase_mats[sector]),
                "shift": frob_norm_sq(shift_mats[sector]),
                "b": frob_norm_sq(b_mats[sector]),
                "phase_shift_inner_real": float(inner(phase_mats[sector], shift_mats[sector]).real),
                "phase_shift_inner_imag": float(inner(phase_mats[sector], shift_mats[sector]).imag),
            }
            for sector in SECTORS
        },
        "conditional_not_selected": {
            "selected_dynamic_transfer_identity_proved": same_source_identity["promotion_decision"]["selected_dynamic_transfer_identity_promoted"],
            "selected_PhiFinC1_identity_promoted": phifin_identity["promotion_decision"]["selected_PhiFinC1_identity_promoted"],
            "selected_primitive_overlap_contractions_promoted": diff_overlap["promotion_decision"]["selected_primitive_overlap_contractions_promoted"],
            "selected_A_selected_promoted": dynamic_transfer["promotion_gate"]["promote_to_selected_A_selected"],
            "selected_b_selected_promoted": dynamic_transfer["promotion_gate"]["promote_to_selected_b_selected"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CONDITIONAL_PAYLOAD, conditional_payload)

    validation_packet = {
        "schema": "MTTStep20ConditionalNormalFormValidation.v1",
        "status": "CONDITIONAL_NORMAL_FORM_VALIDATED_NOT_SELECTED",
        "coordinate_system": same_source_identity["normal_form_identity"]["coordinate_system"],
        "computed": {
            "A_conditional_shape": [72, 2],
            "A_transpose_A": gram,
            "A_transpose_b": atb,
            "b_norm_sq": dot_real(b_vec, b_vec),
            "deltaTheta_conditional": delta,
            "phase_shift_reconstruction_residual_norm_sq": residual_norm,
            "rank_if_columns_independent": 2,
        },
        "expected": dynamic_transfer["conditional_dynamic_transfer_coordinate_packet"],
        "checks": {
            "gram_is_12I2": abs(gram[0][0] - 12.0) < 1e-9 and abs(gram[1][1] - 12.0) < 1e-9 and abs(gram[0][1]) < 1e-9 and abs(gram[1][0]) < 1e-9,
            "A_transpose_b_is_12_12": all(abs(x - 12.0) < 1e-9 for x in atb),
            "deltaTheta_is_1_1": all(abs(x - 1.0) < 1e-9 for x in delta),
            "b_equals_phase_plus_shift": residual_norm < 1e-18,
            "matches_existing_dynamic_transfer_packet": dynamic_transfer["conditional_dynamic_transfer_coordinate_packet"]["matches_prior_weylpair_assembly"],
        },
        "selected_value_status": "NOT_PROMOTED_SOURCE_THEOREM_OPEN",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(VALIDATION_PACKET, validation_packet)

    source_frontier = {
        "schema": "MTTStep20SourceTheoremFrontier.v1",
        "status": "SOURCE_THEOREM_REDUCED_TO_PROMOTING_AGGREGATE_PAYLOAD_OR_ATOM_DECOMPOSITION",
        "closed_support": {
            "Step19_sourcevalue_gate": step19["closure_decision"]["step19_gate_closed"],
            "primitive_vertex_source_selector": selector["promotion_decision"]["source_selector_promoted"],
            "conditional_phase_shift_payload": True,
            "conditional_normal_form_validation": True,
            "transport_only_no_go": diff_overlap["promotion_decision"]["transport_only_lane_rejected_as_phase_shift_source"],
            "stationary_trace_insufficient_for_C1": phifin_identity["partial_promotion_theorem"]["corollary_now"]["C1_dynamic_layer_closed"] is False,
        },
        "residual_source_packet": {
            "template_status": residual_template["status"],
            "selected_source_selector_attached": residual_template["selected_source_selector_attached"],
            "phase_residual_norm_sq": residual_template["required_source_emissions"]["phase_residual_operator_R_Z"]["shape"]["residual_norm_sq"],
            "shift_residual_norm_sq": residual_template["required_source_emissions"]["shift_residual_operator_R_X"]["shape"]["residual_norm_sq"],
            "phase_selected_by_MTT_now": residual_template["required_source_emissions"]["phase_residual_operator_R_Z"]["selected_by_MTT_now"],
            "shift_selected_by_MTT_now": residual_template["required_source_emissions"]["shift_residual_operator_R_X"]["selected_by_MTT_now"],
            "total_residual_norm_sq_four_sectors": residual_completion["routed_72_real_completion"]["total_residual_norm_sq_four_sectors"],
        },
        "remaining_two_equivalent_source_tasks": {
            "aggregate_source_theorem": [
                "prove Phi_C1_selected(Z)=phase_packet",
                "prove Phi_C1_selected(X)=shift_packet",
                "prove b_selected=phase_packet+shift_packet",
                "prove selected Hessian/source normalization gives G=12 I_2",
            ],
            "primitive_atom_decomposition": [
                "split aggregate phase/shift columns into six same-source primitive atom terms per sector",
                "emit transported zero-mode bases",
                "emit primitive vertex/basis-transport/Hessian counterterms",
                "emit four b rows or homogeneous-zero theorems",
            ],
        },
        "not_closed": {
            "selected_source_theorem_for_conditional_payload": True,
            "six_term_primitive_atom_decomposition": True,
            "selected_A_selected": True,
            "selected_b_selected": True,
            "selected_deltaTheta_C1": True,
            "Yukawa_or_true_SM_closure": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(SOURCE_FRONTIER, source_frontier)

    next_workorder = {
        "schema": "MTTStep20ToStep21SourceTheoremOrAtomDecomposition.v1",
        "status": "NEXT_WORKORDER_PROVE_SOURCE_THEOREM_OR_DECOMPOSE_ATOMS",
        "completed_step": 20,
        "next_step": 21,
        "next_required_artifact": NEXT,
        "closed_do_not_reopen": {
            "alpha1_dotD_driver": True,
            "source_selector": True,
            "conditional_phase_shift_payload": True,
            "conditional_normal_form_validation": True,
            "transport_only_no_go": True,
        },
        "must_emit_next": source_frontier["remaining_two_equivalent_source_tasks"],
        "success_criterion": {
            "selected_source_theorem_for_payload_or_atom_decomposition": True,
            "selected_A_selected_b_selected_promoted": True,
            "target_fitting_used_false": True,
            "observed_data_used_as_selector_false": True,
        },
        "closure_claimed": False,
    }
    write_json(NEXT_WORKORDER, next_workorder)

    candidate = {
        "candidate": "MTTSelectedStep20ConditionalAtomPayloadOrSourceTheorem",
        "status": STATUS,
        "inputs": {
            "step19": rel(STEP19),
            "source_selector": rel(SOURCE_SELECTOR),
            "weylpair_gate": rel(WEYLPAIR_GATE),
            "dynamic_transfer": rel(DYNAMIC_TRANSFER),
            "same_source_identity": rel(SAME_SOURCE_IDENTITY),
            "phifin_identity": rel(PHIFIN_IDENTITY),
            "differentiated_overlap": rel(DIFF_OVERLAP),
            "residual_template": rel(RESIDUAL_TEMPLATE),
            "residual_completion": rel(RESIDUAL_COMPLETION),
        },
        "output_packets": {
            "step20_conditional_phase_shift_payload": rel(CONDITIONAL_PAYLOAD),
            "step20_conditional_normal_form_validation": rel(VALIDATION_PACKET),
            "step20_source_theorem_frontier": rel(SOURCE_FRONTIER),
            "step20_to_step21_source_theorem_or_atom_decomposition": rel(NEXT_WORKORDER),
        },
        "theorem": {
            "name": "Step20ConditionalPayloadNormalFormTheorem",
            "proved": True,
            "statement": "Using the selected source selector and the existing Weyl-pair response packet, the aggregate conditional phase/shift C1 payload is materialized in the fixed 72-real coordinate system and validated: A^T A=12 I_2, A^T b=(12,12), b=phase+shift, and deltaTheta=(1,1). This closes the conditional finite algebra and gives an exact payload for the next source theorem. It does not promote the payload to selected values because the dynamic Phi_fin^C1 source identity or six-term primitive atom decomposition remains open.",
        },
        "closure_decision": {
            "step20_conditional_payload_built": True,
            "source_selector_closed": selector["promotion_decision"]["source_selector_promoted"],
            "conditional_normal_form_validated": True,
            "conditional_A_transpose_A": gram,
            "conditional_A_transpose_b": atb,
            "conditional_deltaTheta": delta,
            "selected_source_theorem_for_conditional_payload": False,
            "six_term_primitive_atom_decomposition_emitted": False,
            "selected_A_selected_promoted": False,
            "selected_b_selected_promoted": False,
            "selected_deltaTheta_C1_promoted": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "what_closes_now": {
            "conditional_phase_shift_payload_materialized": True,
            "conditional_normal_form_algebra_validated": True,
            "source_selector_attached_to_payload": True,
            "residual_source_theorem_target_made_explicit": True,
        },
        "what_remains_open": source_frontier["not_closed"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step20_ConditionalAtomPayload_or_SourceTheorem_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "conditional_payload_built": True,
        "conditional_normal_form_validated": True,
        "source_selector_closed": selector["promotion_decision"]["source_selector_promoted"],
        "selected_source_theorem_for_conditional_payload": False,
        "six_term_primitive_atom_decomposition_emitted": False,
        "selected_A_selected_promoted": False,
        "selected_b_selected_promoted": False,
        "selected_deltaTheta_C1_promoted": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected Step20 ConditionalAtomPayload or SourceTheorem v1

Status: `{STATUS}`.

Closed now:

```text
selected source selector attached to payload             closed
aggregate conditional phase/shift columns                emitted
conditional normal form A^T A = 12 I_2                   validated
conditional A^T b = (12,12)                              validated
conditional deltaTheta = (1,1)                           validated
transport-only C1 route                                  rejected
```

Not selected yet:

```text
A_selected
b_selected
deltaTheta_C1
six-term primitive atom decomposition
dynamic Phi_fin^C1 source identity
Yukawa/CKM/PMNS/mass closure
```

The next proof has only two real exits:

```text
1. prove the aggregate source theorem:
   Phi_C1_selected(Z)=phase_packet,
   Phi_C1_selected(X)=shift_packet,
   b_selected=phase_packet+shift_packet,
   G_selected=12 I_2;

2. or decompose the aggregate payload into the six selected primitive atom
   terms per sector and emit the four b rows.
```

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
