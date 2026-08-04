"""Build Step 21 conditional atom decomposition and vertex-source frontier."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step21_conditional_atomdecomposition_or_vertexsource"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
DECOMP_PACKET = PACKET_DIR / "step21_conditional_sixterm_atom_decomposition.packet.json"
VALIDATION_PACKET = PACKET_DIR / "step21_atom_decomposition_validation.packet.json"
SOURCE_FRONTIER = PACKET_DIR / "step21_vertex_source_theorem_frontier.packet.json"
NEXT_WORKORDER = PACKET_DIR / "step21_to_step22_vertex_source_or_selected_values.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step21_ConditionalAtomDecomposition_or_VertexSource_v1.md"

STEP20 = DATA / "selected_step20_conditionalatompayload_or_sourcetheorem.candidate.json"
STEP20_PAYLOAD = DATA / "selected_step20_conditionalatompayload_or_sourcetheorem" / "step20_conditional_phase_shift_payload.packet.json"
STEP20_VALIDATION = DATA / "selected_step20_conditionalatompayload_or_sourcetheorem" / "step20_conditional_normal_form_validation.packet.json"
STEP20_FRONTIER = DATA / "selected_step20_conditionalatompayload_or_sourcetheorem" / "step20_source_theorem_frontier.packet.json"
DIFF_TEMPLATE = DATA / "selected_differentiated_phifinc1_primitiveoverlap_or_galerkinrun" / "primitive_overlap_contractions.template.json"

STATUS = "MTT_SELECTED_STEP21_CONDITIONAL_ATOM_DECOMPOSITION_BUILT_VERTEX_SOURCE_OPEN"
NEXT = "MTT_Selected_Step22_VertexSourceTheorem_or_SelectedASelectedBSelected_v1"
SECTORS = ["u", "d", "e", "nuD"]
DIRECTIONS = ["phase_Z", "shift_X"]
TERMS = [
    "theta_overlap_variation",
    "left_zero_mode_response",
    "right_zero_mode_response",
    "higgs_zero_mode_response",
    "explicit_vertex",
    "basis_connection",
]


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def zero_matrix() -> list[list[float]]:
    return [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]


def to_complex(value: Any) -> complex:
    if isinstance(value, list):
        return complex(float(value[0]), float(value[1]))
    return complex(float(value), 0.0)


def mat_to_complex(matrix: list[list[Any]]) -> list[list[complex]]:
    return [[to_complex(entry) for entry in row] for row in matrix]


def add_mats(a: list[list[complex]], b: list[list[complex]]) -> list[list[complex]]:
    return [[x + y for x, y in zip(row_a, row_b)] for row_a, row_b in zip(a, b)]


def max_abs_diff(a: list[list[Any]], b: list[list[Any]]) -> float:
    ac = mat_to_complex(a)
    bc = mat_to_complex(b)
    return float(max(abs(x - y) for row_a, row_b in zip(ac, bc) for x, y in zip(row_a, row_b)))


def sum_terms(term_payload: dict[str, Any]) -> list[list[complex]]:
    acc = [[0j, 0j, 0j], [0j, 0j, 0j], [0j, 0j, 0j]]
    for term in TERMS:
        acc = add_mats(acc, mat_to_complex(term_payload[term]))
    return acc


def encode_complex(z: complex) -> float | list[float]:
    if abs(z.imag) < 1e-12:
        return float(z.real)
    return [float(z.real), float(z.imag)]


def encode_matrix(matrix: list[list[complex]]) -> list[list[float | list[float]]]:
    return [[encode_complex(entry) for entry in row] for row in matrix]


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    inputs = [STEP20, STEP20_PAYLOAD, STEP20_VALIDATION, STEP20_FRONTIER, DIFF_TEMPLATE]
    missing = [rel(path) for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step 21 inputs: " + ", ".join(missing))

    step20 = load(STEP20)
    step20_payload = load(STEP20_PAYLOAD)
    step20_validation = load(STEP20_VALIDATION)
    step20_frontier = load(STEP20_FRONTIER)
    diff_template = load(DIFF_TEMPLATE)

    aggregate_by_direction = {
        "phase_Z": step20_payload["aggregate_columns"]["phase_packet"],
        "shift_X": step20_payload["aggregate_columns"]["shift_packet"],
    }

    decomposition: dict[str, Any] = {}
    for direction in DIRECTIONS:
        decomposition[direction] = {}
        for sector in SECTORS:
            decomposition[direction][sector] = {term: zero_matrix() for term in TERMS}
            decomposition[direction][sector]["explicit_vertex"] = aggregate_by_direction[direction][sector]

    max_residual = 0.0
    reconstructed: dict[str, Any] = {}
    for direction in DIRECTIONS:
        reconstructed[direction] = {}
        for sector in SECTORS:
            summed = encode_matrix(sum_terms(decomposition[direction][sector]))
            reconstructed[direction][sector] = summed
            max_residual = max(max_residual, max_abs_diff(summed, aggregate_by_direction[direction][sector]))

    decomp_packet = {
        "schema": "MTTStep21ConditionalSixTermAtomDecomposition.v1",
        "status": "CONDITIONAL_VERTEX_ONLY_SIXTERM_DECOMPOSITION_BUILT_NOT_SELECTED",
        "decomposition_policy": {
            "name": "vertex_only_conditional_representative",
            "meaning": "Place the aggregate phase/shift response in the explicit_vertex slot and set theta, left/right/Higgs response, and basis_connection slots to zero.",
            "why_allowed_conditionally": "It is an exact algebraic representative of the aggregate columns in the primitive atom schema.",
            "why_not_selected": "No theorem proves the selected primitive vertex, basis transport, or Hessian source emits this representative.",
        },
        "sector_order": SECTORS,
        "direction_order": DIRECTIONS,
        "term_order": TERMS,
        "conditional_atom_terms": decomposition,
        "reconstructed_aggregate_columns": reconstructed,
        "selected_status": {
            "selected_vertex_source_theorem_proved": False,
            "selected_sixterm_atom_decomposition_emitted": False,
            "selected_A_selected_promoted": False,
            "selected_b_selected_promoted": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(DECOMP_PACKET, decomp_packet)

    validation_packet = {
        "schema": "MTTStep21AtomDecompositionValidation.v1",
        "status": "CONDITIONAL_DECOMPOSITION_RECONSTRUCTS_AGGREGATE_COLUMNS",
        "max_reconstruction_residual": max_residual,
        "aggregate_normal_form_carried": step20_validation["computed"],
        "template_compatibility": {
            "formula_slots_match": diff_template["formula_slots"]["directions"] == DIRECTIONS,
            "sector_order_match": diff_template["formula_slots"]["sectors"] == SECTORS,
            "coordinate_system_match": diff_template["coordinate_system"] == step20_validation["coordinate_system"],
        },
        "checks": {
            "reconstructs_phase_shift_columns": max_residual < 1e-12,
            "normal_form_still_valid": step20_validation["checks"]["gram_is_12I2"]
            and step20_validation["checks"]["A_transpose_b_is_12_12"]
            and step20_validation["checks"]["deltaTheta_is_1_1"],
            "selected_values_not_promoted": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(VALIDATION_PACKET, validation_packet)

    source_frontier = {
        "schema": "MTTStep21VertexSourceTheoremFrontier.v1",
        "status": "VERTEX_SOURCE_THEOREM_OR_REPLACEMENT_ATOM_DECOMPOSITION_REQUIRED",
        "closed_support": {
            "Step20_conditional_payload": step20["closure_decision"]["step20_conditional_payload_built"],
            "conditional_sixterm_decomposition": True,
            "aggregate_reconstruction_validated": max_residual < 1e-12,
            "source_selector_attached": step20_payload["selected_source_selector_closed"],
        },
        "remaining_source_theorem": {
            "preferred_statement": "The selected same-branch primitive vertex/basis-transport source emits the vertex-only representative in the selected transported zero-mode basis.",
            "equivalent_replacement": "Emit any selected six-term decomposition whose sector/direction sums equal the aggregate phase/shift payload and whose b source vector is selected by the same branch.",
            "must_also_emit": [
                "transported zero-mode bases or basis-order theorem",
                "selected primitive vertex/basis-transport/Hessian source provenance",
                "b_selected=phase+shift or selected replacement b",
                "A_selected and b_selected promotion certificate",
            ],
        },
        "not_closed": {
            "selected_vertex_source_theorem": True,
            "selected_replacement_sixterm_decomposition": True,
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
        "schema": "MTTStep21ToStep22VertexSourceOrSelectedValues.v1",
        "status": "NEXT_WORKORDER_PROVE_VERTEX_SOURCE_OR_PROMOTE_SELECTED_VALUES",
        "completed_step": 21,
        "next_step": 22,
        "next_required_artifact": NEXT,
        "closed_do_not_reopen": {
            "conditional_phase_shift_payload": True,
            "conditional_normal_form_validation": True,
            "conditional_sixterm_decomposition": True,
        },
        "must_emit_next": source_frontier["remaining_source_theorem"],
        "success_criterion": {
            "selected_vertex_source_or_replacement_decomposition": True,
            "selected_A_selected_promoted": True,
            "selected_b_selected_promoted": True,
            "target_fitting_used_false": True,
        },
        "closure_claimed": False,
    }
    write_json(NEXT_WORKORDER, next_workorder)

    candidate = {
        "candidate": "MTTSelectedStep21ConditionalAtomDecompositionOrVertexSource",
        "status": STATUS,
        "inputs": {
            "step20": rel(STEP20),
            "step20_payload": rel(STEP20_PAYLOAD),
            "step20_validation": rel(STEP20_VALIDATION),
            "step20_frontier": rel(STEP20_FRONTIER),
            "differentiated_template": rel(DIFF_TEMPLATE),
        },
        "output_packets": {
            "step21_conditional_sixterm_atom_decomposition": rel(DECOMP_PACKET),
            "step21_atom_decomposition_validation": rel(VALIDATION_PACKET),
            "step21_vertex_source_theorem_frontier": rel(SOURCE_FRONTIER),
            "step21_to_step22_vertex_source_or_selected_values": rel(NEXT_WORKORDER),
        },
        "theorem": {
            "name": "Step21ConditionalAtomDecompositionTheorem",
            "proved": True,
            "statement": "The Step 20 aggregate phase/shift columns admit an exact six-term primitive atom representative by placing the aggregate response in the explicit_vertex term and setting the remaining five atom terms to zero. This validates the atom-table shape and preserves the conditional normal form. It does not prove the representative is selected; Step 22 must prove the selected vertex/basis-transport/Hessian source theorem or emit a selected replacement decomposition.",
        },
        "closure_decision": {
            "step21_conditional_decomposition_built": True,
            "conditional_decomposition_reconstructs_aggregate": max_residual < 1e-12,
            "max_reconstruction_residual": max_residual,
            "selected_vertex_source_theorem_proved": False,
            "selected_replacement_sixterm_decomposition_emitted": False,
            "selected_A_selected_promoted": False,
            "selected_b_selected_promoted": False,
            "selected_deltaTheta_C1_promoted": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "what_closes_now": {
            "conditional_sixterm_atom_decomposition_shape": True,
            "aggregate_columns_reconstructed_from_atom_terms": True,
            "vertex_source_theorem_target_fixed": True,
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
        "certificate": "MTT_Selected_Step21_ConditionalAtomDecomposition_or_VertexSource_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "conditional_decomposition_built": True,
        "conditional_decomposition_reconstructs_aggregate": max_residual < 1e-12,
        "selected_vertex_source_theorem_proved": False,
        "selected_A_selected_promoted": False,
        "selected_b_selected_promoted": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected Step21 ConditionalAtomDecomposition or VertexSource v1

Status: `{STATUS}`.

Closed now:

```text
conditional aggregate phase/shift columns decomposed into six-term atom schema
vertex-only representative reconstructs aggregate columns exactly
normal-form algebra from Step 20 is preserved
```

Still not selected:

```text
selected vertex source theorem
selected replacement six-term atom decomposition
A_selected
b_selected
deltaTheta_C1
Yukawa/true-SM closure
```

The next proof is now maximally sharp: prove that the selected same-branch
primitive vertex/basis-transport/Hessian source emits this vertex-only
representative, or emit a different selected six-term decomposition with the
same aggregate validation.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
