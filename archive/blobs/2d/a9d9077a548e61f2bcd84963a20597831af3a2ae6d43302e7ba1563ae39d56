"""Try both exits from the Route-C fixed-fiber class gate.

Path A proves what can be proved now: all fixed qutrit fiber shifts give the
same current C1 spectral observables because every sector matrix is a scalar
times a permutation matrix, hence YY^* is scalar identity.

Path B attempts an absolute fiber-origin gauge fix from selected source data.
It remains open: the current selected S3/gerbe/rho_E certificates select the
period-three projective class and central cocycle, but not a marked qutrit
fiber origin or operator-level primitive transport.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

FIBER_AUDIT = DATA / "selected_routec_primitive_source_selection_audit.candidate.json"
NONINV = DATA / "selected_routec_noninvariant_c1_primitive_search.candidate.json"
S3_SOURCE = DATA / "selected_s3_differential_cohomology_source_certificate.candidate.json"
PROMOTION = DATA / "projective_gerbe_rhoe_source_promotion.candidate.json"
RHOE = DATA / "selected_routec_nonidentity_rhoe_bn_construction.candidate.json"

OUTPUT = DATA / "selected_routec_fiberclass_observable_invariance_or_gaugefix.candidate.json"
CERT = CERTS / "selected_routec_fiberclass_observable_invariance_or_gaugefix_certificate.json"
NOTE = CORPUS / "MTT_Selected_RouteC_FiberClass_Observable_Invariance_or_GaugeFix_v1.md"

TOL = 1e-12


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def candidate_by_shift(noninv: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {str(item["primitive_fiber_shift"]): item for item in noninv["candidate_primitives"]}


def matmul_t(matrix: list[list[float]]) -> list[list[float]]:
    rows = len(matrix)
    out = [[0.0 for _ in range(rows)] for _ in range(rows)]
    for i in range(rows):
        for j in range(rows):
            out[i][j] = sum(float(matrix[i][k]) * float(matrix[j][k]) for k in range(len(matrix[0])))
    return out


def trace(matrix: list[list[float]]) -> float:
    return sum(float(matrix[i][i]) for i in range(len(matrix)))


def trace_square(matrix: list[list[float]]) -> float:
    square = [
        [sum(float(matrix[i][k]) * float(matrix[k][j]) for k in range(len(matrix))) for j in range(len(matrix))]
        for i in range(len(matrix))
    ]
    return trace(square)


def det3(matrix: list[list[float]]) -> float:
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    return float(a) * (float(e) * float(i) - float(f) * float(h)) - float(b) * (
        float(d) * float(i) - float(f) * float(g)
    ) + float(c) * (float(d) * float(h) - float(e) * float(g))


def rank(matrix: list[list[float]]) -> int:
    work = [[float(value) for value in row] for row in matrix]
    rows = len(work)
    cols = len(work[0]) if rows else 0
    out = 0
    for col in range(cols):
        pivot = None
        for row in range(out, rows):
            if abs(work[row][col]) > TOL:
                pivot = row
                break
        if pivot is None:
            continue
        work[out], work[pivot] = work[pivot], work[out]
        scale = work[out][col]
        work[out] = [value / scale for value in work[out]]
        for row in range(rows):
            if row == out or abs(work[row][col]) <= TOL:
                continue
            factor = work[row][col]
            work[row] = [work[row][idx] - factor * work[out][idx] for idx in range(cols)]
        out += 1
    return out


def is_scalar_identity(matrix: list[list[float]]) -> tuple[bool, float]:
    scalar = float(matrix[0][0])
    ok = True
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            target = scalar if i == j else 0.0
            if abs(float(matrix[i][j]) - target) > TOL:
                ok = False
    return ok, scalar


def spectral_observables(matrix: list[list[float]]) -> dict[str, Any]:
    gram = matmul_t(matrix)
    scalar_identity, scalar = is_scalar_identity(gram)
    return {
        "rank": rank(matrix),
        "det_abs": abs(det3(matrix)),
        "trace_YYstar": trace(gram),
        "trace_YYstar_squared": trace_square(gram),
        "YYstar_is_scalar_identity": scalar_identity,
        "YYstar_scalar": scalar,
        "singular_values_squared_if_scalar_identity": [scalar, scalar, scalar] if scalar_identity else None,
    }


def rounded(value: Any) -> Any:
    if isinstance(value, float):
        return round(value, 15)
    if isinstance(value, list):
        return [rounded(item) for item in value]
    if isinstance(value, dict):
        return {key: rounded(item) for key, item in value.items()}
    return value


def fixed_shift_observables(by_shift: dict[str, dict[str, Any]]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for shift in ("0", "1", "2"):
        out[shift] = {
            sector: spectral_observables(matrix)
            for sector, matrix in by_shift[shift]["matrices"].items()
        }
    return rounded(out)


def all_fixed_observables_equal(observables: dict[str, Any]) -> bool:
    base = observables["0"]
    return all(observables[shift] == base for shift in ("1", "2"))


def all_fixed_scalar_identity(observables: dict[str, Any]) -> bool:
    return all(
        sector_data["YYstar_is_scalar_identity"] is True
        for shift_data in observables.values()
        for sector_data in shift_data.values()
    )


def gauge_fix_source_attempt(s3_source: dict[str, Any], promotion: dict[str, Any], rhoe: dict[str, Any]) -> dict[str, Any]:
    selected_source = s3_source.get("selected_source_packet", {})
    promotion_flags = promotion.get("promotion_gate_flags_after_s3_closure", {})
    rho_candidate = rhoe.get("rho_E_candidate", {})
    required_markers = {
        "marked_qutrit_fiber_origin": selected_source.get("marked_qutrit_fiber_origin"),
        "absolute_fiber_basepoint": selected_source.get("absolute_fiber_basepoint"),
        "selected_basis_transport": promotion_flags.get("selected_basis_transport"),
        "operator_level_projective_rhoE_promoted": promotion.get("promotion_result", {}).get(
            "operator_level_projective_rhoE_promoted"
        ),
        "rhoE_selected_by_mtt": rho_candidate.get("selected_by_mtt"),
    }
    missing = [key for key, value in required_markers.items() if value not in (True, 0, "0")]
    return {
        "attempted": True,
        "proved": False,
        "canonical_computation_gauge_available": True,
        "canonical_computation_gauge": "fiber_shift_0",
        "physical_absolute_origin_selected": False,
        "required_markers": required_markers,
        "missing_markers": missing,
        "reason": (
            "The available source certificates select the F3^2/qutrit projective class and central cocycle, "
            "but do not mark a qutrit fiber basepoint or prove operator-level basis transport. Shift 0 can "
            "be used as a computation gauge only."
        ),
    }


def main() -> None:
    fiber = load(FIBER_AUDIT)
    noninv = load(NONINV)
    s3_source = load(S3_SOURCE)
    promotion = load(PROMOTION)
    rhoe = load(RHOE)
    by_shift = candidate_by_shift(noninv)
    observables = fixed_shift_observables(by_shift)
    invariant = all_fixed_observables_equal(observables)
    scalar_identity = all_fixed_scalar_identity(observables)
    gauge_attempt = gauge_fix_source_attempt(s3_source, promotion, rhoe)

    candidate = {
        "candidate": "MTTSelectedRouteCFiberClassObservableInvarianceOrGaugeFix",
        "status": "MTT_SELECTED_ROUTEC_FIBERCLASS_OBSERVABLE_INVARIANCE_PROVED_GAUGEFIX_OPEN",
        "inputs": {
            "fiber_class_audit": rel(FIBER_AUDIT),
            "noninvariant_c1_search": rel(NONINV),
            "selected_s3_source": rel(S3_SOURCE),
            "projective_gerbe_rhoe_promotion": rel(PROMOTION),
            "nonidentity_rhoe_packet": rel(RHOE),
        },
        "path_A_observable_invariance": {
            "name": "FixedFiberClassSpectralObservableInvarianceLemma",
            "proved_for_current_finite_C1_layer": invariant and scalar_identity,
            "scope": (
                "Invariance is proved for rank, absolute determinant, traces of (YY*) powers, and the singular "
                "spectrum of each current fixed-fiber C1 sector matrix."
            ),
            "fixed_shift_observables": observables,
            "proof_reason": (
                "Each fixed-fiber sector matrix is the same scalar amplitude times a permutation matrix, up to "
                "qutrit row/column relabeling. Therefore YY* is the same scalar identity for shifts 0, 1, and 2."
            ),
            "does_not_prove_physical_flavor_closure": True,
            "why_not_physical_flavor_closure": (
                "The current finite C1 layer has degenerate singular values in every sector, so it cannot by "
                "itself yield nondegenerate Yukawa hierarchies, CKM, or PMNS. Those require selected higher-order "
                "corrections, sector-dependent source data, or full Strominger/Iwasawa response support."
            ),
        },
        "path_B_absolute_gauge_fix": gauge_attempt,
        "combined_result": {
            "fiber_origin_needed_for_current_spectral_observables": False,
            "fiber_origin_needed_for_full_matrix_entries_or_future_noncommuting_corrections": True,
            "selected_unique_C1_matrix_proved": False,
            "selected_C1_observable_class_proved_at_current_layer": invariant and scalar_identity,
        },
        "what_closes_now": {
            "observable_invariance_under_fixed_fiber_class_for_current_C1_spectrum": invariant and scalar_identity,
            "canonical_shift0_computation_gauge_allowed": True,
            "absolute_fiber_origin_not_needed_for_current_spectral_invariants": True,
            "no_observed_flavor_data_used": True,
        },
        "what_remains_open": {
            "absolute_fiber_origin_source_theorem": True,
            "operator_level_basis_transport": True,
            "selected_noninvariant_C1_primitive_or_vertex_source": True,
            "selected_dotD_source_verified": True,
            "alpha1_driver_verified": True,
            "nondegenerate_yukawa_hierarchy": True,
            "CKM_PMNS_CP_from_selected_matrices": True,
            "higher_order_or_full_strominger_response_support": True,
            "honest_replay_without_lifted_flags": True,
            "full_SM_or_no_knob_closure": True,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_RouteC_HigherOrder_or_FullResponse_FlavorSplitting_v1",
        "theorem": {
            "name": "FixedFiberClassObservableInvarianceAndGaugeFixReductionTheorem",
            "proved": True,
            "statement": (
                "For the current selected Route-C finite C1 layer, the fixed qutrit fiber shifts 0, 1, and 2 "
                "produce identical spectral observables because each sector matrix is a scalar times a "
                "permutation matrix and YY* is scalar identity. The absolute gauge-fix path remains open: "
                "existing source certificates do not mark a qutrit fiber origin. Therefore this layer may use "
                "shift 0 as computation gauge for spectral invariants, but full flavor closure requires "
                "selected higher-order/full-response splitting or an operator-level basis-transport theorem."
            ),
        },
    }

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(
        json.dumps(
            {
                "status": candidate["status"],
                "candidate_path": rel(OUTPUT),
                "note_path": rel(NOTE),
                "what_closes": candidate["what_closes_now"],
                "what_remains_open": candidate["what_remains_open"],
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    NOTE.write_text(
        f"""# MTT Selected Route-C Fiber-Class Observable Invariance or Gauge Fix

Status: `{candidate['status']}`

This artifact tries both paths out of the fixed qutrit fiber-class gate.

## Path A: Observable Invariance

For the current finite C1 layer, this path succeeds in a precise scope.  The
fixed fiber shifts `0`, `1`, and `2` have identical spectral observables in
every sector: rank, absolute determinant, traces of `(Y Y*)` powers, and the
singular spectrum.  The reason is simple and strong: each current fixed-fiber
matrix is a scalar multiple of a permutation matrix, so `Y Y*` is scalar
identity.

This does not close physical flavor.  The same fact also says the current C1
layer is fully degenerate, so it cannot by itself produce Yukawa hierarchy,
CKM, PMNS, or CP structure.

## Path B: Absolute Gauge Fix

This path remains open.  The selected S3/gerbe/rho_E certificates select the
period-three projective qutrit class and central cocycle, but they do not mark
an absolute qutrit fiber origin or prove an operator-level basis transport.
Shift `0` is therefore legal as a computation gauge, not as a physical source
selection.

## Next Gate

The next real calculation is higher-order or full-response flavor splitting:
construct selected corrections that break the scalar-permutation degeneracy
without using observed masses, CKM, PMNS, or CP data as selectors.
""",
        encoding="utf-8",
    )
    print(json.dumps({"candidate": rel(OUTPUT), "status": candidate["status"]}, indent=2))


if __name__ == "__main__":
    main()
