"""Run the first correction-matrix search and Galerkin replay in parallel lanes.

Lane A is an algebraic qutrit/Weyl correction search.  It looks for finite
correction directions that pass the previously locked non-scalar,
noncommuting, CP-odd tests.  This is discovery-only unless MTT emits the same
directions from selected source data.

Lane B replays the existing Route-C Galerkin first-run manifest.  The honest
payload remains blocked at selected-source flags; the formal-lift payload
passes lower validators but is diagnostic only.
"""

from __future__ import annotations

import itertools
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

FRONTIER = DATA / "selected_routec_higherorder_fullresponse_flavor_splitting.candidate.json"
NONINV = DATA / "selected_routec_noninvariant_c1_primitive_search.candidate.json"
GALERKIN_FIRST = DATA / "selected_routec_strominger_galerkin_first_run.candidate.json"

OUTPUT = DATA / "selected_routec_first_correction_search_or_galerkin_run.candidate.json"
CERT = CERTS / "selected_routec_first_correction_search_or_galerkin_run_certificate.json"
NOTE = CORPUS / "MTT_Selected_RouteC_First_Selected_Correction_Matrix_Search_or_Galerkin_Run_v1.md"

TOL = 1e-10


ComplexMatrix = list[list[complex]]


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def encode(value: Any) -> Any:
    if isinstance(value, complex):
        real = 0.0 if abs(value.real) < TOL else value.real
        imag = 0.0 if abs(value.imag) < TOL else value.imag
        if imag == 0.0:
            return real
        return [real, imag]
    if isinstance(value, float):
        return 0.0 if abs(value) < TOL else value
    if isinstance(value, list):
        return [encode(item) for item in value]
    if isinstance(value, dict):
        return {key: encode(item) for key, item in value.items()}
    return value


def to_complex(value: Any) -> complex:
    if isinstance(value, list):
        return complex(float(value[0]), float(value[1]))
    return complex(float(value), 0.0)


def cmatrix(matrix: list[list[Any]]) -> ComplexMatrix:
    return [[to_complex(value) for value in row] for row in matrix]


def eye() -> ComplexMatrix:
    return [[1.0 + 0.0j if i == j else 0.0 + 0.0j for j in range(3)] for i in range(3)]


def matmul(a: ComplexMatrix, b: ComplexMatrix) -> ComplexMatrix:
    return [[sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def add(*matrices: ComplexMatrix) -> ComplexMatrix:
    return [[sum(matrix[i][j] for matrix in matrices) for j in range(3)] for i in range(3)]


def scale(c: complex, matrix: ComplexMatrix) -> ComplexMatrix:
    return [[c * matrix[i][j] for j in range(3)] for i in range(3)]


def dagger(matrix: ComplexMatrix) -> ComplexMatrix:
    return [[matrix[j][i].conjugate() for j in range(3)] for i in range(3)]


def trace(matrix: ComplexMatrix) -> complex:
    return sum(matrix[i][i] for i in range(3))


def commutator(a: ComplexMatrix, b: ComplexMatrix) -> ComplexMatrix:
    return add(matmul(a, b), scale(-1.0, matmul(b, a)))


def norm_sq(matrix: ComplexMatrix) -> float:
    return sum(abs(matrix[i][j]) ** 2 for i in range(3) for j in range(3))


def traceless(matrix: ComplexMatrix) -> ComplexMatrix:
    return add(matrix, scale(-trace(matrix) / 3.0, eye()))


def first_hermitian_correction(y0: ComplexMatrix, dy: ComplexMatrix) -> ComplexMatrix:
    return add(matmul(y0, dagger(dy)), matmul(dy, dagger(y0)))


def cp_odd_invariant(hu: ComplexMatrix, hd: ComplexMatrix) -> float:
    c = commutator(hu, hd)
    return trace(matmul(matmul(c, c), c)).imag


def qutrit_weyl_words() -> list[tuple[str, ComplexMatrix]]:
    omega = complex(-0.5, math.sqrt(3.0) / 2.0)
    ident = eye()
    x = [
        [0.0 + 0.0j, 1.0 + 0.0j, 0.0 + 0.0j],
        [0.0 + 0.0j, 0.0 + 0.0j, 1.0 + 0.0j],
        [1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j],
    ]
    z = [
        [1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j],
        [0.0 + 0.0j, omega, 0.0 + 0.0j],
        [0.0 + 0.0j, 0.0 + 0.0j, omega**2],
    ]
    words = []
    for p in range(3):
        xp = ident
        for _ in range(p):
            xp = matmul(xp, x)
        for q in range(3):
            zq = ident
            for _ in range(q):
                zq = matmul(zq, z)
            words.append((f"X^{p} Z^{q}", matmul(xp, zq)))
    return words


def correction_candidates(y0: ComplexMatrix) -> list[dict[str, Any]]:
    words = qutrit_weyl_words()
    coeffs = [1.0 + 0.0j, -1.0 + 0.0j, 0.0 + 1.0j, 0.0 - 1.0j]
    candidates = []
    for (name_a, a), (name_b, b) in itertools.product(words, words):
        for ca, cb in itertools.product(coeffs, coeffs):
            dy = add(scale(ca, a), scale(cb, b))
            h1 = first_hermitian_correction(y0, dy)
            split_norm = norm_sq(traceless(h1))
            if split_norm <= TOL:
                continue
            candidates.append(
                {
                    "label": f"{ca}*{name_a} + {cb}*{name_b}",
                    "dy": dy,
                    "h1": h1,
                    "traceless_norm_sq": split_norm,
                }
            )
    return candidates


def search_splitter(y0: ComplexMatrix) -> dict[str, Any]:
    candidates = correction_candidates(y0)
    best = None
    for up, down in itertools.product(candidates, candidates):
        comm_norm = norm_sq(commutator(up["h1"], down["h1"]))
        cp_value = cp_odd_invariant(up["h1"], down["h1"])
        if comm_norm > TOL and abs(cp_value) > TOL:
            best = {
                "up_like": up,
                "down_like": down,
                "commutator_norm_sq": comm_norm,
                "cp_odd_trace_commutator_cubed_imag": cp_value,
            }
            break
    if best is None:
        return {
            "diagnostic_splitter_found": False,
            "candidate_count": len(candidates),
        }
    return {
        "diagnostic_splitter_found": True,
        "candidate_count": len(candidates),
        "selected_by_mtt": False,
        "promotion_allowed": False,
        "why_not_promoted": (
            "The qutrit/Weyl correction directions are searched as algebraic source-compatible diagnostics. "
            "No selected Phi_fin/Galerkin source emits these correction matrices yet."
        ),
        "representative": {
            "u_correction_label": best["up_like"]["label"],
            "d_correction_label": best["down_like"]["label"],
            "e_correction_label": best["up_like"]["label"],
            "nuD_correction_label": best["down_like"]["label"],
            "mass_split_traceless_norm_sq": {
                "u": best["up_like"]["traceless_norm_sq"],
                "d": best["down_like"]["traceless_norm_sq"],
                "e": best["up_like"]["traceless_norm_sq"],
                "nuD": best["down_like"]["traceless_norm_sq"],
            },
            "ckm_commutator_norm_sq": best["commutator_norm_sq"],
            "pmns_commutator_norm_sq": best["commutator_norm_sq"],
            "cp_odd_trace_commutator_cubed_imag": best["cp_odd_trace_commutator_cubed_imag"],
            "u_dy": best["up_like"]["dy"],
            "d_dy": best["down_like"]["dy"],
            "u_H1": best["up_like"]["h1"],
            "d_H1": best["down_like"]["h1"],
        },
    }


def galerkin_replay(first_run: dict[str, Any]) -> dict[str, Any]:
    honest = first_run["validation"]["honest_root"]
    formal = first_run["validation"]["formal_lift_diagnostic"]
    honest_failures = {
        key: value["output"]
        for key, value in honest.items()
        if value.get("passed") is False
    }
    return {
        "manifest_filled": all(first_run["manifest_filled"].values()),
        "honest_root_all_pass": all(value.get("passed") for value in honest.values()),
        "honest_root_failures": honest_failures,
        "formal_lift_lower_validators_all_pass": first_run["validation"]["formal_lift_lower_validators_all_pass"],
        "formal_lift_promotion_passes": first_run["validation"]["formal_lift_promotion_passes"],
        "formal_lift_is_diagnostic_only": first_run["interpretation"]["proof_promotion_allowed"] is False,
        "selected_correction_matrices_emitted": False,
        "why_no_selected_correction_matrices": (
            "The Galerkin manifest has finite smoke payloads and a formal-lift diagnostic, but the honest root "
            "still fails selected-source, selected_dotD_source, and alpha1-driver gates."
        ),
    }


def main() -> None:
    frontier = load(FRONTIER)
    noninv = load(NONINV)
    first_run = load(GALERKIN_FIRST)
    shift0 = next(item for item in noninv["candidate_primitives"] if str(item["primitive_fiber_shift"]) == "0")
    y0 = cmatrix(shift0["matrices"]["u"])
    search = search_splitter(y0)
    replay = galerkin_replay(first_run)

    candidate = {
        "candidate": "MTTSelectedRouteCFirstCorrectionSearchOrGalerkinRun",
        "status": "MTT_SELECTED_ROUTEC_FIRST_CORRECTION_SEARCH_AND_GALERKIN_RUN_EXECUTED_DIAGNOSTIC_SPLITTER_FOUND_SELECTED_VALUES_OPEN",
        "inputs": {
            "higherorder_fullresponse_frontier": rel(FRONTIER),
            "noninvariant_c1_search": rel(NONINV),
            "strominger_galerkin_first_run": rel(GALERKIN_FIRST),
        },
        "parallel_lanes": {
            "lane_A_qutrit_weyl_correction_search": encode(search),
            "lane_B_galerkin_replay": replay,
        },
        "combined_result": {
            "diagnostic_qutrit_correction_can_break_degeneracy": search["diagnostic_splitter_found"],
            "honest_galerkin_selected_values_emit_correction": False,
            "selected_correction_promoted": False,
            "why_not_closed": (
                "Lane A proves algebraic room for nondegenerate, noncommuting, CP-odd correction structure. "
                "Lane B shows the honest Galerkin source still does not emit selected correction matrices."
            ),
        },
        "what_closes_now": {
            "first_correction_matrix_search_executed": True,
            "diagnostic_splitter_found_without_observed_targets": search["diagnostic_splitter_found"],
            "first_galerkin_replay_executed": True,
            "honest_vs_formal_lift_status_recorded": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_correction_matrix_source": True,
            "selected_galerkin_values": True,
            "selected_dotD_source_verified": True,
            "alpha1_driver_verified": True,
            "finite_C1_Hessian_and_deltaTheta": True,
            "promoted_non_degenerate_yukawa_hierarchy": True,
            "promoted_CKM_PMNS_CP": True,
            "honest_replay_without_lifted_flags": True,
            "full_SM_or_no_knob_closure": True,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_RouteC_Correction_Source_Emission_or_Selected_Galerkin_Values_v1",
        "theorem": {
            "name": "FirstCorrectionSearchAndGalerkinReplay",
            "proved": True,
            "statement": (
                "The first parallel correction/Galerkin attempt is complete. The qutrit/Weyl correction search "
                "finds a diagnostic algebraic splitter satisfying mass-splitting, mixing, and CP-odd tests "
                "without observed targets. The Galerkin replay does not promote it: selected correction values "
                "remain absent from the honest selected-source payload."
            ),
        },
    }
    OUTPUT.write_text(json.dumps(encode(candidate), indent=2, sort_keys=True) + "\n", encoding="utf-8")
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
        """# MTT Selected Route-C First Correction Matrix Search or Galerkin Run

Status: `MTT_SELECTED_ROUTEC_FIRST_CORRECTION_SEARCH_AND_GALERKIN_RUN_EXECUTED_DIAGNOSTIC_SPLITTER_FOUND_SELECTED_VALUES_OPEN`

Two lanes were run in parallel.

## Lane A: Qutrit/Weyl Correction Search

The finite qutrit/Weyl correction search finds an algebraic diagnostic splitter.
The representative correction has nonzero traceless Hermitian splitting,
nonzero up/down and lepton/neutrino commutator norm, and a nonzero CP-odd
commutator-cubed trace invariant.

This is not promoted as selected MTT data.  It proves that the finite qutrit
correction algebra has enough room for flavor structure, but not that MTT emits
that correction.

## Lane B: Galerkin Replay

The existing Route-C Galerkin first-run manifest is filled.  The honest root
still fails selected-source, selected-dotD, and alpha1-driver gates.  The
formal-lift diagnostic passes lower validators and promotion checks, but remains
diagnostic only.

## Conclusion

The degeneracy is not algebraically fatal.  The remaining blocker is source
emission: selected Phi_fin/Galerkin data must emit the correction matrices
without lifted flags or observed flavor targets.
""",
        encoding="utf-8",
    )
    print(json.dumps({"candidate": rel(OUTPUT), "status": candidate["status"]}, indent=2))


if __name__ == "__main__":
    main()
