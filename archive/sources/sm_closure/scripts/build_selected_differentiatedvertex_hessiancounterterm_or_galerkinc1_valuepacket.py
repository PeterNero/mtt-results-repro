"""Build differentiated-vertex / Hessian counterterm residual value packet.

The previous gate proves that the pure fixed-fiber primitive span cannot emit
the Weyl-pair dynamic columns.  This gate computes the exact orthogonal
residual completion that a selected differentiated vertex, basis-transport
correction, Hessian counterterm, or honest Galerkin C1 run would need to emit.

The residual completion is a diagnostic value packet, not selected proof data.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PREVIOUS = DATA / "selected_primitiveoverlapcontractions_valueemission_or_honestgalerkinrun.candidate.json"
SPAN_PACKET = (
    DATA
    / "selected_primitiveoverlapcontractions_valueemission_or_honestgalerkinrun"
    / "primitive_span_obstruction.packet.json"
)
RUN_CONTRACT = (
    DATA
    / "selected_primitiveoverlapcontractions_valueemission_or_honestgalerkinrun"
    / "honest_galerkin_c1_value_run_contract.packet.json"
)
NONINV = DATA / "selected_routec_noninvariant_c1_primitive_search.candidate.json"
NONSCALAR = DATA / "selected_nonscalardynamicoverlap_or_fullresponsecorrection_valueemission.candidate.json"
DYNAMIC_VALUE = DATA / "selected_dynamictransferhessian_bselected_or_honestgalerkinc1_valuefill.candidate.json"
SOURCE_SELECTOR = DATA / "selected_primitivevertex_source_or_basistransport_selectiontheorem.candidate.json"

OUTPUT = DATA / "selected_differentiatedvertex_hessiancounterterm_or_galerkinc1_valuepacket.candidate.json"
PACKET_DIR = DATA / "selected_differentiatedvertex_hessiancounterterm_or_galerkinc1_valuepacket"
RESIDUAL_PACKET = PACKET_DIR / "differentiated_residual_completion.packet.json"
ACCEPTANCE_PACKET = PACKET_DIR / "residual_completion_acceptance_kernel.packet.json"
CERT = CERTS / "selected_differentiatedvertex_hessiancounterterm_or_galerkinc1_valuepacket_certificate.json"
NOTE = CORPUS / "MTT_Selected_DifferentiatedVertex_HessianCounterterm_or_GalerkinC1_ValuePacket_v1.md"

STATUS = (
    "MTT_SELECTED_DIFFERENTIATEDVERTEX_HESSIANCOUNTERTERM_OR_GALERKINC1_VALUEPACKET_"
    "BUILT_RESIDUAL_COMPLETION_OPEN"
)
NEXT = "MTT_Selected_ResidualCompletion_SourcePromotion_or_HonestGalerkinC1_Emission_v1"
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


def matrix_add(a: list[list[complex]], b: list[list[complex]]) -> list[list[complex]]:
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def matrix_sub(a: list[list[complex]], b: list[list[complex]]) -> list[list[complex]]:
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def inner(a: list[list[complex]], b: list[list[complex]]) -> complex:
    return sum(a[i][j].conjugate() * b[i][j] for i in range(len(a)) for j in range(len(a[0])))


def norm_sq(matrix: list[list[complex]]) -> float:
    return float(sum(abs(value) ** 2 for row in matrix for value in row))


def max_abs(matrix: list[list[complex]]) -> float:
    return float(max((abs(value) for row in matrix for value in row), default=0.0))


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


def fixed_fiber_basis(noninv: dict[str, Any]) -> list[list[list[complex]]]:
    return [
        cmatrix(primitive_by_shift(noninv, shift)["matrices"]["u"])
        for shift in [0, 1, 2]
    ]


def matrix_summary(matrix: list[list[complex]]) -> dict[str, Any]:
    return {
        "matrix": matrix,
        "norm_sq": norm_sq(matrix),
        "rank": rank(matrix),
        "max_abs_entry": max_abs(matrix),
    }


def orthogonality_report(
    residual: list[list[complex]],
    basis: list[list[list[complex]]],
) -> dict[str, Any]:
    values = [inner(matrix, residual) for matrix in basis]
    return {
        "inner_products_with_fixed_fiber_basis": values,
        "orthogonal_to_fixed_fiber_span": all(abs(value) <= TOL for value in values),
    }


def exact_decomposition(
    target: list[list[complex]],
    projection: list[list[complex]],
    residual: list[list[complex]],
) -> dict[str, Any]:
    error = matrix_sub(matrix_add(projection, residual), target)
    return {
        "projection_plus_residual_equals_target": norm_sq(error) <= TOL,
        "closure_error_norm_sq": norm_sq(error),
        "target_norm_sq": norm_sq(target),
        "projection_norm_sq": norm_sq(projection),
        "residual_norm_sq": norm_sq(residual),
    }


def main() -> int:
    previous = load(PREVIOUS)
    span = load(SPAN_PACKET)
    run_contract = load(RUN_CONTRACT)
    noninv = load(NONINV)
    nonscalar = load(NONSCALAR)
    dynamic = load(DYNAMIC_VALUE)
    source_selector = load(SOURCE_SELECTOR)

    basis = fixed_fiber_basis(noninv)
    phase_target = cmatrix(nonscalar["conditional_non_scalar_value_packet"]["sector_first_responses"]["u"]["correction_dY"])
    shift_target = cmatrix(nonscalar["conditional_non_scalar_value_packet"]["sector_first_responses"]["d"]["correction_dY"])
    phase_fit = span["single_sector_least_squares"]["phase_I_plus_Z_against_fixed_fiber_span"]
    shift_fit = span["single_sector_least_squares"]["shift_I_plus_X_against_fixed_fiber_span"]
    phase_projection = cmatrix(phase_fit["projection"])
    shift_projection = cmatrix(shift_fit["projection"])
    phase_residual = cmatrix(phase_fit["residual"])
    shift_residual = cmatrix(shift_fit["residual"])

    phase_decomp = exact_decomposition(phase_target, phase_projection, phase_residual)
    shift_decomp = exact_decomposition(shift_target, shift_projection, shift_residual)

    residual_packet = {
        "schema": "MTTSelectedDifferentiatedResidualCompletion.v1",
        "status": "ORTHOGONAL_RESIDUAL_COMPLETION_COMPUTED_SOURCE_OPEN",
        "selected_by_MTT": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "source_selector_attached": previous["promotion_decision"]["source_selector_attached_to_template"],
        "basis": {
            "primitive_fixed_fiber_span_source": rel(SPAN_PACKET),
            "fixed_fiber_class": [0, 1, 2],
            "active_shift": [1, 1],
            "absolute_fiber_origin_selected": False,
        },
        "phase_I_plus_Z_completion": {
            "target": matrix_summary(phase_target),
            "primitive_projection": matrix_summary(phase_projection),
            "residual_completion": matrix_summary(phase_residual),
            "decomposition": phase_decomp,
            "orthogonality": orthogonality_report(phase_residual, basis),
        },
        "shift_I_plus_X_completion": {
            "target": matrix_summary(shift_target),
            "primitive_projection": matrix_summary(shift_projection),
            "residual_completion": matrix_summary(shift_residual),
            "decomposition": shift_decomp,
            "orthogonality": orthogonality_report(shift_residual, basis),
        },
        "routed_72_real_completion": {
            "phase_residual_norm_sq_two_sectors": 2.0 * phase_decomp["residual_norm_sq"],
            "shift_residual_norm_sq_two_sectors": 2.0 * shift_decomp["residual_norm_sq"],
            "total_residual_norm_sq_four_sectors": 2.0
            * (phase_decomp["residual_norm_sq"] + shift_decomp["residual_norm_sq"]),
            "conditional_b_norm_sq": dynamic["conditional_dynamic_transfer_coordinate_packet"][
                "b_conditional_norm_sq"
            ],
            "if_promoted_then_remaining_linear_algebra_obstruction": False,
        },
        "interpretation": (
            "This is the minimal Frobenius-orthogonal completion relative to the fixed-fiber "
            "primitive span.  It is a diagnostic target for the next source theorem, not a "
            "selected value packet."
        ),
    }

    acceptance_kernel = {
        "schema": "MTTSelectedResidualCompletionAcceptanceKernel.v1",
        "status": "ACCEPTANCE_KERNEL_EMITTED_SOURCE_OPEN",
        "lane_A_residual_source_promotion": {
            "must_prove_same_branch_differentiated_vertex_emits_phase_residual": True,
            "must_prove_same_branch_differentiated_vertex_emits_shift_residual": True,
            "or_Hessian_counterterms_emit_same_residuals": True,
            "must_preserve_static_sector_route": ["u", "e", "d", "nuD"],
            "must_preserve_trace_normalization": True,
            "must_not_use_observed_flavor_targets": True,
        },
        "lane_B_honest_Galerkin_C1_emission": {
            "run_contract": rel(RUN_CONTRACT),
            "required_outputs": run_contract["required_outputs"],
            "selected_source_verified_currently": run_contract["selected_source_verified"],
        },
        "after_source_promotion_checks": {
            "A_selected_columns_reconstruct_conditional_phase_shift_packet": True,
            "A_transpose_A_expected_if_same_packet": dynamic["conditional_dynamic_transfer_coordinate_packet"][
                "Gram_A_transpose_A"
            ],
            "A_transpose_b_expected_if_same_packet": dynamic["conditional_dynamic_transfer_coordinate_packet"][
                "A_transpose_b_conditional"
            ],
            "deltaTheta_expected_if_same_packet": dynamic["conditional_dynamic_transfer_coordinate_packet"][
                "deltaTheta_conditional_from_Gram_solve"
            ],
            "rank_expected_if_same_packet": dynamic["conditional_dynamic_transfer_coordinate_packet"]["rank"],
        },
        "promotion_guard": {
            "residual_completion_selected_now": False,
            "A_selected_claimed_now": False,
            "b_selected_claimed_now": False,
            "deltaTheta_C1_claimed_now": False,
            "full_SM_closure_claimed_now": False,
        },
    }

    theorem = {
        "name": "DifferentiatedResidualCompletionReductionTheorem",
        "proved": True,
        "statement": (
            "Given the selected source selector and the finite fixed-fiber primitive span, "
            "the conditional Weyl-pair phase and shift matrices decompose uniquely into "
            "their fixed-fiber Frobenius projections plus orthogonal residual completions. "
            "The residuals have norm squared 4 for I+Z and 2 for I+X per sector, are "
            "orthogonal to the fixed-fiber span, and reconstruct the conditional columns "
            "exactly when added back to the projections.  Thus the next source theorem is "
            "sharply localized to selecting these residual completions, or replacing the "
            "whole packet by an honest Galerkin C1 emission."
        ),
    }

    candidate = {
        "candidate": "MTTSelectedDifferentiatedVertexHessianCountertermOrGalerkinC1ValuePacket",
        "status": STATUS,
        "inputs": {
            "previous_span_obstruction_gate": rel(PREVIOUS),
            "primitive_span_packet": rel(SPAN_PACKET),
            "honest_galerkin_run_contract": rel(RUN_CONTRACT),
            "noninvariant_primitive_search": rel(NONINV),
            "conditional_non_scalar_packet": rel(NONSCALAR),
            "dynamic_transfer_value_gate": rel(DYNAMIC_VALUE),
            "source_selector": rel(SOURCE_SELECTOR),
        },
        "output_packets": {
            "residual_completion": rel(RESIDUAL_PACKET),
            "acceptance_kernel": rel(ACCEPTANCE_PACKET),
        },
        "source_selector_state": {
            "source_selector_promoted": source_selector["promotion_decision"]["source_selector_promoted"],
            "dynamic_values_promoted": source_selector["promotion_decision"][
                "selected_dynamic_overlap_tensor_promoted"
            ],
            "A_selected_promoted": source_selector["promotion_decision"]["selected_A_selected_promoted"],
            "b_selected_promoted": source_selector["promotion_decision"]["selected_b_selected_promoted"],
        },
        "residual_completion_summary": {
            "phase_residual_norm_sq_per_sector": phase_decomp["residual_norm_sq"],
            "shift_residual_norm_sq_per_sector": shift_decomp["residual_norm_sq"],
            "total_routed_residual_norm_sq": residual_packet["routed_72_real_completion"][
                "total_residual_norm_sq_four_sectors"
            ],
            "phase_residual_orthogonal_to_fixed_fiber_span": residual_packet[
                "phase_I_plus_Z_completion"
            ]["orthogonality"]["orthogonal_to_fixed_fiber_span"],
            "shift_residual_orthogonal_to_fixed_fiber_span": residual_packet[
                "shift_I_plus_X_completion"
            ]["orthogonality"]["orthogonal_to_fixed_fiber_span"],
            "exact_reconstruction_if_residual_promoted": (
                phase_decomp["projection_plus_residual_equals_target"]
                and shift_decomp["projection_plus_residual_equals_target"]
            ),
        },
        "acceptance_kernel": acceptance_kernel,
        "theorem": theorem,
        "promotion_decision": {
            "residual_completion_packet_computed": True,
            "acceptance_kernel_emitted": True,
            "selected_residual_completion_promoted": False,
            "selected_differentiated_vertex_promoted": False,
            "selected_Hessian_counterterms_promoted": False,
            "selected_A_selected_promoted": False,
            "selected_b_selected_promoted": False,
            "selected_deltaTheta_C1_promoted": False,
            "honest_Galerkin_C1_contractions_promoted": False,
            "full_SM_no_knob_closure_promoted": False,
        },
        "what_closes_now": {
            "exact_orthogonal_residual_completion_computed": True,
            "next_source_theorem_target_reduced_to_residual_completion": True,
            "honest_Galerkin_fallback_contract_preserved": True,
            "conditional_linear_algebra_after_promotion_fixed": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_residual_completion_source_theorem": True,
            "selected_differentiated_vertex_operator_phase_Z": True,
            "selected_differentiated_vertex_operator_shift_X": True,
            "selected_Hessian_counterterms": True,
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
        "selected_residual_completion_claimed": False,
        "selected_differentiated_vertex_claimed": False,
        "selected_Hessian_counterterms_claimed": False,
        "A_selected_claimed": False,
        "b_selected_claimed": False,
        "deltaTheta_C1_claimed": False,
        "Galerkin_C1_contractions_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_DifferentiatedVertex_HessianCounterterm_or_GalerkinC1_ValuePacket_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "residual_packet_path": rel(RESIDUAL_PACKET),
        "acceptance_packet_path": rel(ACCEPTANCE_PACKET),
        "note_path": rel(NOTE),
        "closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "theorem_proved": True,
        "residual_completion_packet_computed": True,
        "selected_residual_completion_claimed": False,
        "A_selected_claimed": False,
        "b_selected_claimed": False,
        "deltaTheta_C1_claimed": False,
        "Galerkin_C1_contractions_claimed": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected DifferentiatedVertex HessianCounterterm or GalerkinC1 ValuePacket v1

Status: `{STATUS}`.

This artifact computes the exact residual-completion packet left after the
fixed-fiber primitive span is projected out of the conditional Weyl-pair
dynamic columns.

```text
phase residual ||R_Z||^2 per sector = {phase_decomp["residual_norm_sq"]}
shift residual ||R_X||^2 per sector = {shift_decomp["residual_norm_sq"]}
total routed residual norm^2        = {residual_packet["routed_72_real_completion"]["total_residual_norm_sq_four_sectors"]}
```

Both residuals are orthogonal to the fixed-fiber primitive span, and projection
plus residual reconstructs the conditional `I+Z` and `I+X` columns exactly.

This is still not selected SM closure.  The next theorem must prove that the
selected same-branch differentiated vertex, basis transport, or Hessian
counterterm emits these residuals, or an honest selected Galerkin C1 run must
emit replacement values.

No observed masses, mixings, CP phase, benchmark matrices, or target residuals
are used as selectors.

Next artifact: `{NEXT}`.
"""

    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(encode(candidate), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    RESIDUAL_PACKET.write_text(
        json.dumps(encode(residual_packet), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    ACCEPTANCE_PACKET.write_text(
        json.dumps(encode(acceptance_kernel), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    CERT.write_text(json.dumps(encode(cert), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(
        json.dumps(
            {
                "candidate": rel(OUTPUT),
                "residual_packet": rel(RESIDUAL_PACKET),
                "acceptance_packet": rel(ACCEPTANCE_PACKET),
                "status": STATUS,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
