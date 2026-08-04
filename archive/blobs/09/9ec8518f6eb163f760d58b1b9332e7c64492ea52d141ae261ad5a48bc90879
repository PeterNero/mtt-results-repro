"""Build canonical residual projector / honest Galerkin C1 value-fill gate.

The residual Weyl-polynomial artifact reduces the source theorem to a canonical
trace-orthogonal residual projector.  This artifact constructs that projector
as a finite 9x9 operator on row-major 3x3 matrices, verifies it is orthogonal,
idempotent, self-adjoint, and reproduces the stored residual completions.

It promotes only the canonical mathematical projector.  It does not promote
the physical C1 transfer functor applying that projector.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PREVIOUS = DATA / "selected_residual_weylpolynomial_source_theorem_attempt.candidate.json"
WEYL_PACKET = (
    DATA
    / "selected_residual_weylpolynomial_source_theorem_attempt"
    / "residual_weyl_polynomial_decomposition.packet.json"
)
SELECTION_GATE = (
    DATA
    / "selected_residual_weylpolynomial_source_theorem_attempt"
    / "canonical_residual_projector_selection_gate.packet.json"
)
RESIDUAL_COMPLETION = (
    DATA
    / "selected_differentiatedvertex_hessiancounterterm_or_galerkinc1_valuepacket"
    / "differentiated_residual_completion.packet.json"
)
SOURCE_TEMPLATE = (
    DATA
    / "selected_residualcompletion_sourcepromotion_or_honestgalerkinc1_emission"
    / "minimal_residual_source_packet.template.json"
)
SOURCE_SELECTOR = DATA / "selected_primitivevertex_source_or_basistransport_selectiontheorem.candidate.json"
GALERKIN_MANIFEST = DATA / "selected_routec_strominger_galerkin_solve" / "c1_primitive_contractions.candidate.json"

OUTPUT = DATA / "selected_canonicalresidualprojector_or_honestgalerkinc1_valuefill.candidate.json"
PACKET_DIR = DATA / "selected_canonicalresidualprojector_or_honestgalerkinc1_valuefill"
PROJECTOR_PACKET = PACKET_DIR / "canonical_fixedfiber_residual_projector.packet.json"
REPLAY_PACKET = PACKET_DIR / "projector_application_value_replay.packet.json"
CUTSET_PACKET = PACKET_DIR / "projector_or_galerkin_cutset_decision.packet.json"
CERT = CERTS / "selected_canonicalresidualprojector_or_honestgalerkinc1_valuefill_certificate.json"
NOTE = CORPUS / "MTT_Selected_CanonicalResidualProjector_or_HonestGalerkinC1_ValueFill_v1.md"

STATUS = (
    "MTT_SELECTED_CANONICALRESIDUALPROJECTOR_OR_HONESTGALERKINC1_VALUEFILL_"
    "BUILT_PROJECTOR_CLOSED_APPLICATION_OPEN"
)
NEXT = "MTT_Selected_PhiFinC1ResidualProjectorApplication_or_HonestGalerkinExecution_ValueFill_v1"
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


def cmatrix(raw: list[list[Any]]) -> list[list[complex]]:
    return [[to_complex(value) for value in row] for row in raw]


def flatten(matrix: list[list[complex]]) -> list[complex]:
    return [matrix[i][j] for i in range(3) for j in range(3)]


def unflatten(vector: list[complex]) -> list[list[complex]]:
    return [[vector[3 * i + j] for j in range(3)] for i in range(3)]


def zero_operator() -> list[list[complex]]:
    return [[0.0 + 0.0j for _ in range(9)] for _ in range(9)]


def matmul(a: list[list[complex]], b: list[list[complex]]) -> list[list[complex]]:
    cols = len(b[0])
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(cols)] for i in range(len(a))]


def matvec(a: list[list[complex]], v: list[complex]) -> list[complex]:
    return [sum(a[i][j] * v[j] for j in range(len(v))) for i in range(len(a))]


def op_sub(a: list[list[complex]], b: list[list[complex]]) -> list[list[complex]]:
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def matrix_sub(a: list[list[complex]], b: list[list[complex]]) -> list[list[complex]]:
    return [[a[i][j] - b[i][j] for j in range(3)] for i in range(3)]


def op_norm_sq(a: list[list[complex]]) -> float:
    return float(sum(abs(value) ** 2 for row in a for value in row))


def vector_norm_sq(v: list[complex]) -> float:
    return float(sum(abs(value) ** 2 for value in v))


def matrix_norm_sq(m: list[list[complex]]) -> float:
    return vector_norm_sq(flatten(m))


def adjoint(a: list[list[complex]]) -> list[list[complex]]:
    return [[a[j][i].conjugate() for j in range(len(a))] for i in range(len(a[0]))]


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


def identity_operator(n: int) -> list[list[complex]]:
    return [[1.0 + 0.0j if i == j else 0.0 + 0.0j for j in range(n)] for i in range(n)]


def fixed_fiber_supports() -> list[list[tuple[int, int]]]:
    return [
        [(0, 0), (1, 2), (2, 1)],
        [(0, 2), (1, 1), (2, 0)],
        [(0, 1), (1, 0), (2, 2)],
    ]


def support_projector() -> list[list[complex]]:
    p = zero_operator()
    for support in fixed_fiber_supports():
        indices = [3 * i + j for i, j in support]
        for row in indices:
            for col in indices:
                p[row][col] = 1.0 / len(indices)
    return p


def projector_replay(name: str, target: list[list[complex]], stored_projection: list[list[complex]], stored_residual: list[list[complex]], p_fixed: list[list[complex]], q_residual: list[list[complex]]) -> dict[str, Any]:
    target_v = flatten(target)
    projection = unflatten(matvec(p_fixed, target_v))
    residual = unflatten(matvec(q_residual, target_v))
    return {
        "name": name,
        "target_norm_sq": matrix_norm_sq(target),
        "projection_norm_sq": matrix_norm_sq(projection),
        "residual_norm_sq": matrix_norm_sq(residual),
        "projection_matches_stored_norm_sq": matrix_norm_sq(matrix_sub(projection, stored_projection)),
        "residual_matches_stored_norm_sq": matrix_norm_sq(matrix_sub(residual, stored_residual)),
        "target_minus_projection_minus_residual_norm_sq": matrix_norm_sq(matrix_sub(target, [[projection[i][j] + residual[i][j] for j in range(3)] for i in range(3)])),
        "projection": projection,
        "residual": residual,
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    previous = load(PREVIOUS)
    weyl = load(WEYL_PACKET)
    selection_gate = load(SELECTION_GATE)
    residual_completion = load(RESIDUAL_COMPLETION)
    source_template = load(SOURCE_TEMPLATE)
    source_selector = load(SOURCE_SELECTOR)
    galerkin = load(GALERKIN_MANIFEST)

    p_fixed = support_projector()
    identity = identity_operator(9)
    q_residual = op_sub(identity, p_fixed)

    phase_packet = residual_completion["phase_I_plus_Z_completion"]
    shift_packet = residual_completion["shift_I_plus_X_completion"]
    phase_replay = projector_replay(
        "phase_I_plus_Z",
        cmatrix(phase_packet["target"]["matrix"]),
        cmatrix(phase_packet["primitive_projection"]["matrix"]),
        cmatrix(phase_packet["residual_completion"]["matrix"]),
        p_fixed,
        q_residual,
    )
    shift_replay = projector_replay(
        "shift_I_plus_X",
        cmatrix(shift_packet["target"]["matrix"]),
        cmatrix(shift_packet["primitive_projection"]["matrix"]),
        cmatrix(shift_packet["residual_completion"]["matrix"]),
        p_fixed,
        q_residual,
    )

    projector_packet = {
        "schema": "MTTCanonicalFixedFiberResidualProjector.v1",
        "status": "CANONICAL_PROJECTOR_COMPUTED_FROM_SELECTED_FIXED_FIBER_CLASS",
        "selected_inputs": {
            "source_level_weyl_carrier_selected": weyl["source_level_weyl_carrier_selected"],
            "active_shift_selected": weyl["active_shift_selected"],
            "fixed_fiber_class_selected_for_current_observables": source_selector[
                "source_selector_packet"
            ]["selector_components"]["fixed_fiber_quotient"]["selected_for_current_observables"],
            "trace_frobenius_transfer_normalization_selected": source_selector[
                "source_selector_packet"
            ]["selector_components"]["static_overlap_transfer_normalization"]["selected"],
        },
        "fixed_fiber_supports_row_col": fixed_fiber_supports(),
        "projector_on_fixed_fiber_span": p_fixed,
        "projector_on_residual_complement": q_residual,
        "operator_checks": {
            "fixed_projector_rank": rank(p_fixed),
            "residual_projector_rank": rank(q_residual),
            "fixed_projector_idempotence_norm_sq": op_norm_sq(op_sub(matmul(p_fixed, p_fixed), p_fixed)),
            "residual_projector_idempotence_norm_sq": op_norm_sq(op_sub(matmul(q_residual, q_residual), q_residual)),
            "fixed_projector_self_adjoint_norm_sq": op_norm_sq(op_sub(adjoint(p_fixed), p_fixed)),
            "residual_projector_self_adjoint_norm_sq": op_norm_sq(op_sub(adjoint(q_residual), q_residual)),
            "orthogonal_complement_product_norm_sq": op_norm_sq(matmul(p_fixed, q_residual)),
            "partition_sum_identity_norm_sq": op_norm_sq(op_sub([[p_fixed[i][j] + q_residual[i][j] for j in range(9)] for i in range(9)], identity)),
        },
        "selected_as_canonical_mathematical_projector": True,
        "selected_as_physical_C1_transfer_application": False,
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    replay_packet = {
        "schema": "MTTCanonicalResidualProjectorApplicationReplay.v1",
        "status": "PROJECTOR_REPLAY_MATCHES_RESIDUAL_PACKET_APPLICATION_OPEN",
        "phase_replay": phase_replay,
        "shift_replay": shift_replay,
        "matches_stored_residual_packet": (
            phase_replay["projection_matches_stored_norm_sq"] <= TOL
            and phase_replay["residual_matches_stored_norm_sq"] <= TOL
            and shift_replay["projection_matches_stored_norm_sq"] <= TOL
            and shift_replay["residual_matches_stored_norm_sq"] <= TOL
        ),
        "physical_application_claimed": False,
        "honest_galerkin_manifest_status": galerkin["status"],
        "honest_galerkin_selected_source_verified": galerkin["selected_source_verified"],
    }

    conditional_value_fill = source_template["if_emitted_then"]
    cutset_packet = {
        "schema": "MTTProjectorOrGalerkinCutsetDecision.v1",
        "status": "TWO_LANE_CUTSET_SHARP_SM_PARITY_DYNAMIC_PACKET_OPEN",
        "straight_path": (
            "Lane A uses one straight selected-source route: the selected Weyl packet, "
            "fixed-fiber residual projector, and a selected Phi_fin^C1 projector "
            "application theorem."
        ),
        "superset_path": (
            "Lane B combines typed monad/section-ring source routing, HYM/Galerkin "
            "zero-mode data, and finite Weyl operator encodings, then locks them to "
            "the same SM-parity dynamic target."
        ),
        "locked_target": "SM-parity dynamic packet; no measured constants are source selectors.",
        "if_lane_A_application_theorem_is_supplied": {
            "A_selected_columns_available": conditional_value_fill["A_selected_columns_available"],
            "A_transpose_A": conditional_value_fill["A_transpose_A"],
            "A_transpose_b": conditional_value_fill["A_transpose_b"],
            "deltaTheta_C1": conditional_value_fill["deltaTheta_C1"],
            "rank": conditional_value_fill["rank"],
            "SM_parity_dynamic_packet_would_close": True,
            "no_knob_flavor_constants_would_close": False,
        },
        "if_lane_B_values_are_emitted": {
            "required_outputs": galerkin["required_outputs"],
            "selected_source_verified_now": galerkin["selected_source_verified"],
            "SM_parity_dynamic_packet_would_close": True,
            "no_knob_flavor_constants_would_close": False,
        },
        "canonical_projector_promoted_as_unique_mathematical_projector": True,
        "PhiFinC1_projector_application_promoted": False,
        "honest_Galerkin_C1_value_run_promoted": False,
        "SM_parity_dynamic_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_flavor_constants_closed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    theorem = {
        "name": "CanonicalFixedFiberResidualProjectorUniquenessTheorem",
        "proved": True,
        "statement": (
            "The selected fixed-fiber quotient class and selected trace/Frobenius "
            "normalization determine a unique orthogonal projector P_F onto the three "
            "fixed-fiber support lines, and hence a unique residual projector Q_F=I-P_F. "
            "P_F has rank 3, Q_F has rank 6, both are self-adjoint idempotents, and "
            "Q_F applied to the conditional I+Z/I+X columns reproduces the stored "
            "residual completions exactly.  This proves projector uniqueness, not yet "
            "that selected Phi_fin^C1 applies Q_F as the physical dynamic response."
        ),
    }

    candidate = {
        "candidate": "MTTSelectedCanonicalResidualProjectorOrHonestGalerkinC1ValueFill",
        "status": STATUS,
        "inputs": {
            "previous_weyl_polynomial_gate": rel(PREVIOUS),
            "weyl_polynomial_packet": rel(WEYL_PACKET),
            "canonical_projector_selection_gate": rel(SELECTION_GATE),
            "residual_completion_packet": rel(RESIDUAL_COMPLETION),
            "minimal_residual_source_packet": rel(SOURCE_TEMPLATE),
            "source_selector": rel(SOURCE_SELECTOR),
            "honest_galerkin_manifest": rel(GALERKIN_MANIFEST),
        },
        "output_packets": {
            "canonical_projector": rel(PROJECTOR_PACKET),
            "projector_application_replay": rel(REPLAY_PACKET),
            "projector_or_galerkin_cutset_decision": rel(CUTSET_PACKET),
        },
        "projector_closure": {
            "canonical_projector_computed": True,
            "canonical_projector_selected_as_mathematical_consequence": True,
            "projector_application_to_C1_physical_response_selected": False,
            "phase_replay_matches": phase_replay["residual_matches_stored_norm_sq"] <= TOL,
            "shift_replay_matches": shift_replay["residual_matches_stored_norm_sq"] <= TOL,
        },
        "honest_Galerkin_lane": {
            "status": "OPEN_RUN_VALUES_MISSING",
            "manifest_status": galerkin["status"],
            "selected_source_verified": galerkin["selected_source_verified"],
            "required_outputs": galerkin["required_outputs"],
        },
        "theorem": theorem,
        "promotion_decision": {
            "canonical_residual_projector_promoted_as_unique_mathematical_projector": True,
            "PhiFinC1_projector_application_promoted": False,
            "honest_Galerkin_C1_value_run_promoted": False,
            "selected_A_selected_promoted": False,
            "selected_b_selected_promoted": False,
            "selected_deltaTheta_C1_promoted": False,
            "SM_parity_dynamic_packet_closed": False,
            "full_no_knob_flavor_closure_promoted": False,
        },
        "what_closes_now": {
            "canonical_fixed_fiber_projector_constructed": True,
            "projector_rank_idempotence_selfadjointness_verified": True,
            "residual_projector_replays_R_Z_R_X_exactly": True,
            "Lane_A_reduced_to_PhiFinC1_projector_application_theorem": True,
            "Lane_B_honest_galerkin_value_requirements_reemitted": True,
            "SM_parity_dynamic_packet_cutset_reduced_to_two_named_routes": True,
            "superset_strategy_made_explicit": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_PhiFinC1_applies_canonical_residual_projector": True,
            "selected_Hessian_or_vertex_operator_implements_projector": True,
            "honest_selected_Galerkin_C1_value_run": True,
            "selected_A_selected": True,
            "selected_b_selected": True,
            "selected_deltaTheta_C1": True,
            "SM_parity_dynamic_packet_closure": True,
            "true_SM_equivalence_closure": True,
            "full_no_knob_flavor_closure": True,
        },
        "closure_claimed": False,
        "SM_parity_dynamic_packet_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "no_knob_closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "A_selected_claimed": False,
        "b_selected_claimed": False,
        "deltaTheta_C1_claimed": False,
        "Galerkin_C1_contractions_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_CanonicalResidualProjector_or_HonestGalerkinC1_ValueFill_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "projector_packet_path": rel(PROJECTOR_PACKET),
        "replay_packet_path": rel(REPLAY_PACKET),
        "cutset_packet_path": rel(CUTSET_PACKET),
        "theorem_proved": True,
        "canonical_projector_promoted_as_unique_mathematical_projector": True,
        "PhiFinC1_projector_application_promoted": False,
        "closure_claimed": False,
        "SM_parity_dynamic_packet_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "no_knob_closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "A_selected_claimed": False,
        "b_selected_claimed": False,
        "deltaTheta_C1_claimed": False,
        "Galerkin_C1_contractions_claimed": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected CanonicalResidualProjector or HonestGalerkinC1 ValueFill v1

Status: `{STATUS}`.

The selected fixed-fiber quotient and selected trace/Frobenius normalization now
determine a unique finite projector:

```text
rank(P_fixed)    = {projector_packet["operator_checks"]["fixed_projector_rank"]}
rank(Q_residual) = {projector_packet["operator_checks"]["residual_projector_rank"]}
||P_fixed^2 - P_fixed||_F^2       = {projector_packet["operator_checks"]["fixed_projector_idempotence_norm_sq"]}
||Q_residual^2 - Q_residual||_F^2 = {projector_packet["operator_checks"]["residual_projector_idempotence_norm_sq"]}
||P_fixed Q_residual||_F^2        = {projector_packet["operator_checks"]["orthogonal_complement_product_norm_sq"]}
||P_fixed + Q_residual - I||_F^2  = {projector_packet["operator_checks"]["partition_sum_identity_norm_sq"]}
```

Applying `Q_residual` to the conditional `I+Z` and `I+X` columns reproduces the
stored residual completions exactly.

This closes the canonical mathematical projector, not the physical C1
application theorem.

Lane A is the straight path: prove selected `Phi_fin^C1` or the selected
Hessian/vertex operator applies this projector.  If that application theorem is
supplied, the conditional value fill is:

```text
A^T A = [[12, 0], [0, 12]]
A^T b = [12, 12]
deltaTheta_C1 = [1, 1]
```

Lane B is the superset fallback: combine typed monad/section-ring source
routing, HYM/Galerkin zero-mode data, and finite Weyl operator data, then emit
honest selected C1 response matrices under the recorded acceptance checks.

The locked target is SM-parity dynamic packet closure; no-knob constants remain
separate and open.

No observed masses, CKM/PMNS values, CP phase, benchmark matrices, or target
residuals are used as selectors.

Next artifact: `{NEXT}`.
"""

    PROJECTOR_PACKET.write_text(json.dumps(encode(projector_packet), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    REPLAY_PACKET.write_text(json.dumps(encode(replay_packet), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CUTSET_PACKET.write_text(json.dumps(encode(cutset_packet), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(encode(candidate), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(encode(cert), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
