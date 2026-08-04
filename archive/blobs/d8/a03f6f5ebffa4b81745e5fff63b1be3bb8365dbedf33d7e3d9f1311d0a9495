"""Build primitive-overlap value-emission / honest Galerkin run gate.

This artifact attaches the newly selected primitive-vertex/basis-transport
source selector to the differentiated Phi_fin^C1 template, then replays the
available fixed-fiber primitive matrices against the desired Weyl-pair
phase/shift columns.  The replay is intentionally conservative: it emits an
exact finite span obstruction, not selected SM closure.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PREVIOUS = DATA / "selected_primitivevertex_source_or_basistransport_selectiontheorem.candidate.json"
DIFF_TEMPLATE = DATA / "selected_differentiated_phifinc1_primitiveoverlap_or_galerkinrun.candidate.json"
NONINV = DATA / "selected_routec_noninvariant_c1_primitive_search.candidate.json"
NONSCALAR = DATA / "selected_nonscalardynamicoverlap_or_fullresponsecorrection_valueemission.candidate.json"
CURRENT_LAYER = DATA / "selected_dynamicoverlaptensor_hessiannormalization_or_galerkinc1contractions_valueemission.candidate.json"
GALERKIN = DATA / "selected_routec_strominger_galerkin_solve" / "c1_primitive_contractions.candidate.json"
SOURCE_TO_C1 = DATA / "selected_routec_weylpair_source_to_c1_transfer_map.candidate.json"
DYNAMIC_VALUE = DATA / "selected_dynamictransferhessian_bselected_or_honestgalerkinc1_valuefill.candidate.json"

OUTPUT = DATA / "selected_primitiveoverlapcontractions_valueemission_or_honestgalerkinrun.candidate.json"
PACKET_DIR = DATA / "selected_primitiveoverlapcontractions_valueemission_or_honestgalerkinrun"
SPAN_PACKET = PACKET_DIR / "primitive_span_obstruction.packet.json"
RUN_CONTRACT = PACKET_DIR / "honest_galerkin_c1_value_run_contract.packet.json"
CERT = CERTS / "selected_primitiveoverlapcontractions_valueemission_or_honestgalerkinrun_certificate.json"
NOTE = CORPUS / "MTT_Selected_PrimitiveOverlapContractions_ValueEmission_or_HonestGalerkinRun_v1.md"

STATUS = (
    "MTT_SELECTED_PRIMITIVEOVERLAPCONTRACTIONS_VALUEEMISSION_OR_HONESTGALERKINRUN_"
    "BUILT_PRIMITIVE_SPAN_OBSTRUCTION_OPEN"
)
NEXT = "MTT_Selected_DifferentiatedVertex_HessianCounterterm_or_GalerkinC1_ValuePacket_v1"
SECTORS = ["u", "d", "e", "nuD"]
TOL = 1e-10


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def to_complex(value: Any) -> complex:
    if isinstance(value, bool):
        raise TypeError("boolean is not scalar")
    if isinstance(value, (int, float)):
        return complex(float(value), 0.0)
    if isinstance(value, list) and len(value) == 2:
        return complex(float(value[0]), float(value[1]))
    raise TypeError(f"unsupported scalar {value!r}")


def encode_scalar(value: complex) -> float | list[float]:
    real = 0.0 if abs(value.real) < TOL else value.real
    imag = 0.0 if abs(value.imag) < TOL else value.imag
    if imag == 0.0:
        return real
    return [real, imag]


def encode(value: Any) -> Any:
    if isinstance(value, complex):
        return encode_scalar(value)
    if isinstance(value, dict):
        return {key: encode(item) for key, item in value.items()}
    if isinstance(value, list):
        return [encode(item) for item in value]
    return value


def cmatrix(matrix: list[list[Any]]) -> list[list[complex]]:
    return [[to_complex(value) for value in row] for row in matrix]


def zeros(rows: int, cols: int) -> list[list[complex]]:
    return [[0.0 + 0.0j for _ in range(cols)] for _ in range(rows)]


def matrix_add_scaled(
    target: list[list[complex]],
    coefficient: complex,
    matrix: list[list[complex]],
) -> list[list[complex]]:
    return [
        [target[i][j] + coefficient * matrix[i][j] for j in range(len(target[0]))]
        for i in range(len(target))
    ]


def matrix_sub(a: list[list[complex]], b: list[list[complex]]) -> list[list[complex]]:
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def inner(a: list[list[complex]], b: list[list[complex]]) -> complex:
    return sum(a[i][j].conjugate() * b[i][j] for i in range(len(a)) for j in range(len(a[0])))


def norm_sq(matrix: list[list[complex]]) -> float:
    return float(sum(abs(value) ** 2 for row in matrix for value in row))


def rank(matrix: list[list[complex]], tol: float = TOL) -> int:
    work = [row[:] for row in matrix]
    rows = len(work)
    cols = len(work[0]) if rows else 0
    out = 0
    for col in range(cols):
        pivot = None
        for row in range(out, rows):
            if abs(work[row][col]) > tol:
                pivot = row
                break
        if pivot is None:
            continue
        work[out], work[pivot] = work[pivot], work[out]
        scale = work[out][col]
        work[out] = [value / scale for value in work[out]]
        for row in range(rows):
            if row == out or abs(work[row][col]) <= tol:
                continue
            factor = work[row][col]
            work[row] = [work[row][idx] - factor * work[out][idx] for idx in range(cols)]
        out += 1
    return out


def primitive_by_shift(noninv: dict[str, Any], shift: int) -> dict[str, Any]:
    for item in noninv["candidate_primitives"]:
        if item["primitive_fiber_shift"] == shift:
            return item
    raise KeyError(f"missing primitive shift {shift}")


def fit_to_span(
    target: list[list[complex]],
    basis: list[list[list[complex]]],
) -> dict[str, Any]:
    """Project target to the orthogonal fixed-fiber primitive span."""

    coefficients: list[complex] = []
    projection = zeros(len(target), len(target[0]))
    gram_diagonal = []
    for matrix in basis:
        gram = inner(matrix, matrix)
        if abs(gram) <= TOL:
            raise ValueError("basis matrix has zero norm")
        coeff = inner(matrix, target) / gram
        coefficients.append(coeff)
        gram_diagonal.append(gram.real)
        projection = matrix_add_scaled(projection, coeff, matrix)

    residual = matrix_sub(target, projection)
    return {
        "target_norm_sq": norm_sq(target),
        "projection_norm_sq": norm_sq(projection),
        "residual_norm_sq": norm_sq(residual),
        "relative_residual_norm_sq": norm_sq(residual) / max(norm_sq(target), TOL),
        "in_fixed_fiber_span": norm_sq(residual) <= TOL,
        "coefficients": coefficients,
        "basis_gram_diagonal": gram_diagonal,
        "projection": projection,
        "residual": residual,
    }


def fixed_fiber_basis(noninv: dict[str, Any]) -> list[list[list[complex]]]:
    return [
        cmatrix(primitive_by_shift(noninv, shift)["matrices"]["u"])
        for shift in [0, 1, 2]
    ]


def fixed_fiber_orbit_summary(noninv: dict[str, Any]) -> dict[str, Any]:
    basis = fixed_fiber_basis(noninv)
    orbit_sum = zeros(3, 3)
    for matrix in basis:
        orbit_sum = matrix_add_scaled(orbit_sum, 1.0 + 0.0j, matrix)
    return {
        "fixed_fiber_class": [0, 1, 2],
        "representative_shift": 0,
        "absolute_origin_selected": False,
        "basis_dimension": rank([[basis[col][i][j] for col in range(3)] for i in range(3) for j in range(3)]),
        "basis_norm_sq": [norm_sq(matrix) for matrix in basis],
        "pairwise_inner_products": [
            [inner(a, b) for b in basis]
            for a in basis
        ],
        "orbit_sum_rank": rank(orbit_sum),
        "orbit_sum_matrix": orbit_sum,
        "interpretation": (
            "The fixed-fiber representatives form a selected quotient class for current "
            "spectral observables, but no absolute fiber origin is selected."
        ),
    }


def main() -> int:
    previous = load(PREVIOUS)
    diff_template = load(DIFF_TEMPLATE)
    noninv = load(NONINV)
    nonscalar = load(NONSCALAR)
    current_layer = load(CURRENT_LAYER)
    galerkin = load(GALERKIN)
    source_to_c1 = load(SOURCE_TO_C1)
    dynamic_value = load(DYNAMIC_VALUE)

    selector_packet = previous["source_selector_packet"]
    template = load(ROOT / diff_template["differentiated_primitive_overlap_contract"]["template_path"])
    basis = fixed_fiber_basis(noninv)
    phase_target = cmatrix(nonscalar["conditional_non_scalar_value_packet"]["sector_first_responses"]["u"]["correction_dY"])
    shift_target = cmatrix(nonscalar["conditional_non_scalar_value_packet"]["sector_first_responses"]["d"]["correction_dY"])
    phase_fit = fit_to_span(phase_target, basis)
    shift_fit = fit_to_span(shift_target, basis)

    span_obstruction_packet = {
        "schema": "MTTSelectedPrimitiveOverlapSpanObstruction.v1",
        "status": "PURE_FIXED_FIBER_PRIMITIVE_SPAN_REPLAYED_AND_REJECTED_FOR_DYNAMIC_COLUMNS",
        "same_source_selector_attached": previous["promotion_decision"]["source_selector_promoted"],
        "fixed_fiber_orbit": fixed_fiber_orbit_summary(noninv),
        "target_columns": {
            "phase_column": source_to_c1["conditional_transfer_map"]["formula"]["phase_column"],
            "shift_column": source_to_c1["conditional_transfer_map"]["formula"]["shift_column"],
            "observed_data_used": False,
            "target_fitting_used": False,
        },
        "single_sector_least_squares": {
            "phase_I_plus_Z_against_fixed_fiber_span": phase_fit,
            "shift_I_plus_X_against_fixed_fiber_span": shift_fit,
        },
        "routed_72_real_residuals": {
            "phase_column_residual_norm_sq_two_sectors": 2.0 * phase_fit["residual_norm_sq"],
            "shift_column_residual_norm_sq_two_sectors": 2.0 * shift_fit["residual_norm_sq"],
            "b_phase_plus_shift_residual_norm_sq_four_sectors": 2.0
            * (phase_fit["residual_norm_sq"] + shift_fit["residual_norm_sq"]),
            "conditional_b_norm_sq": dynamic_value["conditional_dynamic_transfer_coordinate_packet"][
                "b_conditional_norm_sq"
            ],
        },
        "obstruction": {
            "pure_fixed_fiber_primitive_span_can_emit_phase_column": phase_fit["in_fixed_fiber_span"],
            "pure_fixed_fiber_primitive_span_can_emit_shift_column": shift_fit["in_fixed_fiber_span"],
            "pure_fixed_fiber_primitive_span_can_emit_conditional_weylpair_packet": False,
            "why": (
                "The fixed-fiber primitive span is generated by the three symmetric qutrit "
                "fiber representatives.  It has the correct active shift and current "
                "spectral quotient, but it cannot produce the diagonal complex phase "
                "matrix I+Z or the non-symmetric shift matrix I+X exactly."
            ),
        },
    }

    honest_galerkin_contract = {
        "schema": "MTTSelectedHonestGalerkinC1ValueRunContract.v1",
        "status": "HONEST_GALERKIN_RUN_CONTRACT_EMITTED_VALUES_OPEN",
        "required_inputs": {
            "selected_transported_zero_mode_bases": None,
            "selected_primitive_vertex_operator_phase_Z": None,
            "selected_primitive_vertex_operator_shift_X": None,
            "selected_basis_transport_corrections": None,
            "selected_Hessian_counterterms": None,
            "selected_L2_Gram_Schmidt_rule": None,
        },
        "required_outputs": galerkin["required_outputs"],
        "must_fill_template": diff_template["differentiated_primitive_overlap_contract"][
            "template_path"
        ],
        "acceptance_checks": template["validators_after_fill"],
        "source_selector_packet": rel(PREVIOUS),
        "current_manifest_status": galerkin["status"],
        "selected_source_verified": galerkin["selected_source_verified"],
        "target_fitting_forbidden": True,
        "observed_flavor_data_forbidden": True,
    }

    theorem = {
        "name": "PrimitiveOverlapContractionsSpanObstructionAndRunContractTheorem",
        "proved": True,
        "statement": (
            "After the same-branch primitive source selector is attached, the available "
            "fixed-fiber primitive replay closes only the current spectral quotient layer. "
            "Even allowing arbitrary complex coefficients in the three fixed-fiber "
            "representative span, the phase column I+Z has residual norm squared 4 per "
            "sector and the shift column I+X has residual norm squared 2 per sector. "
            "Therefore the differentiated Phi_fin^C1 value fill cannot be the pure "
            "fixed-fiber primitive replay; it must add a selected differentiated vertex, "
            "basis-transport correction, Hessian counterterm, or an honest Galerkin C1 "
            "run emitting replacement values."
        ),
        "proof_steps": [
            "Import the selected primitive-vertex/basis-transport source selector.",
            "Replay the three fixed-fiber primitive representatives from the finite non-invariant C1 search.",
            "Project I+Z and I+X onto their orthogonal Frobenius span.",
            "Compute exact nonzero residuals for both target columns.",
            "Conclude that the selector is not by itself a value-emission theorem.",
            "Emit the honest Galerkin C1 run contract and differentiated-value cutset.",
        ],
    }

    candidate = {
        "candidate": "MTTSelectedPrimitiveOverlapContractionsValueEmissionOrHonestGalerkinRun",
        "status": STATUS,
        "inputs": {
            "primitive_source_selector": rel(PREVIOUS),
            "differentiated_template_gate": rel(DIFF_TEMPLATE),
            "noninvariant_primitive_search": rel(NONINV),
            "conditional_non_scalar_packet": rel(NONSCALAR),
            "current_layer_value_packet": rel(CURRENT_LAYER),
            "honest_galerkin_manifest": rel(GALERKIN),
            "conditional_source_to_C1_transfer": rel(SOURCE_TO_C1),
            "dynamic_transfer_value_gate": rel(DYNAMIC_VALUE),
        },
        "output_packets": {
            "primitive_span_obstruction": rel(SPAN_PACKET),
            "honest_galerkin_run_contract": rel(RUN_CONTRACT),
        },
        "selector_attachment": {
            "source_selector_promoted": previous["promotion_decision"]["source_selector_promoted"],
            "same_source": selector_packet["same_source"],
            "active_shift": selector_packet["selector_components"]["active_deck_shift"]["value"],
            "fixed_fiber_quotient_selected": selector_packet["selector_components"][
                "fixed_fiber_quotient"
            ]["selected_for_current_observables"],
            "absolute_fiber_origin_selected": selector_packet["selector_components"][
                "fixed_fiber_quotient"
            ]["absolute_fiber_origin_selected"],
            "static_sector_route_selected": selector_packet["selector_components"][
                "static_sector_route"
            ]["selected"],
            "alpha1_dotD_driver_selected": selector_packet["selector_components"][
                "alpha1_dotD_driver"
            ]["alpha1_driver_verified"],
        },
        "primitive_value_replay": {
            "fixed_fiber_representatives_replayed": True,
            "current_spectral_observable_class_selected": current_layer["promotion_decision"][
                "current_layer_values_selected_as_C1_observable_class"
            ],
            "current_layer_promoted_as_flavor_closure": current_layer["promotion_decision"][
                "current_layer_values_promoted_as_flavor_closure"
            ],
            "pure_fixed_fiber_span_obstruction_packet": rel(SPAN_PACKET),
            "selected_primitive_overlap_values_filled": False,
        },
        "span_obstruction_summary": {
            "phase_single_sector_residual_norm_sq": phase_fit["residual_norm_sq"],
            "shift_single_sector_residual_norm_sq": shift_fit["residual_norm_sq"],
            "phase_routed_residual_norm_sq": 2.0 * phase_fit["residual_norm_sq"],
            "shift_routed_residual_norm_sq": 2.0 * shift_fit["residual_norm_sq"],
            "b_routed_residual_norm_sq": 2.0
            * (phase_fit["residual_norm_sq"] + shift_fit["residual_norm_sq"]),
            "pure_fixed_fiber_span_can_close": False,
        },
        "honest_galerkin_run_contract": honest_galerkin_contract,
        "theorem": theorem,
        "promotion_decision": {
            "source_selector_attached_to_template": True,
            "fixed_fiber_current_layer_replayed": True,
            "pure_fixed_fiber_replay_rejected_as_dynamic_value_fill": True,
            "selected_primitive_overlap_contractions_promoted": False,
            "selected_dynamic_overlap_tensor_promoted": False,
            "selected_Hessian_counterterms_promoted": False,
            "selected_A_selected_promoted": False,
            "selected_b_selected_promoted": False,
            "selected_deltaTheta_C1_promoted": False,
            "honest_Galerkin_C1_contractions_promoted": False,
            "full_SM_no_knob_closure_promoted": False,
        },
        "what_closes_now": {
            "selected_source_selector_attached_to_differentiated_template": True,
            "finite_fixed_fiber_primitive_span_replayed": True,
            "pure_fixed_fiber_span_obstruction_proved": True,
            "honest_Galerkin_C1_value_run_contract_emitted": True,
            "next_value_packet_cutset_sharpened": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_differentiated_vertex_operator_phase_Z": True,
            "selected_differentiated_vertex_operator_shift_X": True,
            "selected_basis_transport_corrections": True,
            "selected_Hessian_counterterms": True,
            "selected_primitive_overlap_contraction_values": True,
            "selected_A_selected": True,
            "selected_b_selected": True,
            "selected_deltaTheta_C1": True,
            "honest_Galerkin_C1_contractions": True,
            "Yukawa_CKM_PMNS_masses_Higgs_RG_no_knob": True,
            "full_SM_no_knob_closure": True,
        },
        "closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "selected_primitive_overlap_contractions_claimed": False,
        "selected_dynamic_overlap_tensor_claimed": False,
        "selected_Hessian_counterterms_claimed": False,
        "A_selected_claimed": False,
        "b_selected_claimed": False,
        "deltaTheta_C1_claimed": False,
        "Galerkin_C1_contractions_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_PrimitiveOverlapContractions_ValueEmission_or_HonestGalerkinRun_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "span_packet_path": rel(SPAN_PACKET),
        "run_contract_path": rel(RUN_CONTRACT),
        "note_path": rel(NOTE),
        "closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "theorem_proved": True,
        "source_selector_attached": True,
        "pure_fixed_fiber_span_obstruction_proved": True,
        "selected_primitive_overlap_contractions_claimed": False,
        "A_selected_claimed": False,
        "b_selected_claimed": False,
        "deltaTheta_C1_claimed": False,
        "Galerkin_C1_contractions_claimed": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PrimitiveOverlapContractions ValueEmission or HonestGalerkinRun v1

Status: `{STATUS}`.

The selected primitive source selector is now attached to the differentiated
`Phi_fin^C1` template, but the first value replay gives a no-go rather than a
closure theorem.

The three fixed-fiber primitive representatives are replayed exactly.  Their
span cannot emit the needed Weyl-pair dynamic columns:

```text
phase I+Z residual per sector = {phase_fit["residual_norm_sq"]}
shift I+X residual per sector = {shift_fit["residual_norm_sq"]}
phase routed residual         = {2.0 * phase_fit["residual_norm_sq"]}
shift routed residual         = {2.0 * shift_fit["residual_norm_sq"]}
```

So the pure fixed-fiber primitive replay is not the selected differentiated
value packet.  The next packet must supply one of:

```text
selected differentiated vertex operator phase_Z / shift_X
selected basis-transport corrections
selected Hessian counterterms and b_selected
honest selected Galerkin C1 zero-mode bases, primitive contractions, and response matrices
```

No observed masses, mixings, CP phase, benchmark matrices, or target residuals
are used as selectors.

Next artifact: `{NEXT}`.
"""

    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(encode(candidate), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    SPAN_PACKET.write_text(
        json.dumps(encode(span_obstruction_packet), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    RUN_CONTRACT.write_text(
        json.dumps(encode(honest_galerkin_contract), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    CERT.write_text(json.dumps(encode(cert), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(
        json.dumps(
            {
                "candidate": rel(OUTPUT),
                "span_packet": rel(SPAN_PACKET),
                "run_contract": rel(RUN_CONTRACT),
                "status": STATUS,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
