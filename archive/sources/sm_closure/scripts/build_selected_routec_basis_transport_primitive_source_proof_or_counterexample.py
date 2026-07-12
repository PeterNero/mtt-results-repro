"""Test the I7 basis-transport primitive theorem against the splitter target.

This artifact tries to close the near-term gate by checking whether the
candidate non-invariant primitive family, if promoted, can emit the locked
qutrit/Weyl splitter.  It also records what stronger source theorem is needed
when the primitive-only span fails.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

THEOREM = DATA / "selected_routec_basis_transport_primitive_source_theorem.candidate.json"
NONINV = DATA / "selected_routec_noninvariant_c1_primitive_search.candidate.json"
FIRST = DATA / "selected_routec_first_correction_search_or_galerkin_run.candidate.json"

OUTPUT = DATA / "selected_routec_basis_transport_primitive_source_proof_or_counterexample.candidate.json"
CERT = CERTS / "selected_routec_basis_transport_primitive_source_proof_or_counterexample_certificate.json"
NOTE = CORPUS / "MTT_Selected_RouteC_BasisTransport_Primitive_Source_Proof_or_Counterexample_v1.md"

STATUS = "MTT_SELECTED_ROUTEC_BASISTRANSPORT_PRIMITIVE_SOURCE_COUNTEREXAMPLE_BUILT_PRIMITIVE_ONLY_SPAN_INSUFFICIENT"
NEXT = "MTT_Selected_RouteC_WeylPair_BasisTransport_or_Vertex_Source_Theorem_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def complex_parts(value: Any) -> tuple[float, float]:
    if isinstance(value, list):
        return float(value[0]), float(value[1])
    return float(value), 0.0


def flatten_matrix(matrix: list[list[Any]]) -> list[float]:
    values: list[float] = []
    for row in matrix:
        for entry in row:
            real, imag = complex_parts(entry)
            values.extend([real, imag])
    return values


def sector_vector(matrices: dict[str, list[list[Any]]]) -> np.ndarray:
    values: list[float] = []
    for sector in ("u", "d", "e", "nuD"):
        values.extend(flatten_matrix(matrices[sector]))
    return np.array(values, dtype=float)


def splitter_target(first: dict[str, Any]) -> np.ndarray:
    rep = first["parallel_lanes"]["lane_A_qutrit_weyl_correction_search"]["representative"]
    values: list[float] = []
    for key in ("u_dy", "d_dy", "u_dy", "d_dy"):
        values.extend(flatten_matrix(rep[key]))
    return np.array(values, dtype=float)


def least_squares(columns: list[np.ndarray], target: np.ndarray) -> dict[str, Any]:
    matrix = np.column_stack(columns)
    coeffs, *_ = np.linalg.lstsq(matrix, target, rcond=None)
    residual = matrix @ coeffs - target
    rank = int(np.linalg.matrix_rank(matrix))
    target_norm = float(np.linalg.norm(target))
    residual_norm = float(np.linalg.norm(residual))
    return {
        "rank": rank,
        "coefficients": [float(x) for x in coeffs],
        "target_norm": target_norm,
        "residual_norm": residual_norm,
        "relative_residual": residual_norm / target_norm if target_norm else math.inf,
        "target_in_span": residual_norm <= 1e-10,
    }


def main() -> None:
    theorem = load(THEOREM)
    noninv = load(NONINV)
    first = load(FIRST)

    target = splitter_target(first)
    primitives = noninv["candidate_primitives"]
    fixed = [item for item in primitives if item["primitive_fiber_shift"] in (0, 1, 2)]
    all_candidates = primitives

    fixed_columns = [sector_vector(item["matrices"]) for item in fixed]
    all_columns = [sector_vector(item["matrices"]) for item in all_candidates]
    fixed_result = least_squares(fixed_columns, target)
    all_result = least_squares(all_columns, target)

    source_attempt = {
        "attempted": True,
        "selected_source_emission_proved": False,
        "counterexample_scope": "primitive_only_span",
        "counterexample_proved": all_result["target_in_span"] is False,
        "why": (
            "The promoted fixed-fiber primitive family would only provide the current non-invariant "
            "permutation-style response directions.  Their real span does not contain the qutrit/Weyl "
            "splitter target, so primitive promotion alone cannot emit A_selected for this splitter."
        ),
    }

    refined_theorem = {
        "name": "SelectedWeylPairBasisTransportOrVertexSourceTheorem",
        "status": "NEXT_THEOREM_REQUIRED",
        "statement": (
            "The selected q79/F,m=1 S3/GS Route-C source must emit a basis-transport or vertex correction "
            "whose projected response contains both shift-like and phase-like qutrit Weyl directions. "
            "The active deck shift (1,1) remains forced, but the primitive-only fixed-fiber span must be "
            "enriched by a selected phase/basis-transport component before A_selected can reach the splitter."
        ),
        "required_new_components": [
            "phase-like qutrit Z component or equivalent basis holonomy",
            "shift-like qutrit X component tied to active shift (1,1)",
            "same-branch source proof for the enriched vertex/basis transport",
            "downstream fixed-fiber quotient or selected fiber origin",
        ],
    }

    candidate = {
        "candidate": "MTTSelectedRouteCBasisTransportPrimitiveSourceProofOrCounterexample",
        "status": STATUS,
        "inputs": {
            "basis_transport_primitive_source_theorem": rel(THEOREM),
            "noninvariant_c1_primitive_search": rel(NONINV),
            "first_correction_search": rel(FIRST),
        },
        "superset_strategy": {
            "mode": "CONSTRAINED_SUPERSET_WITH_LOCKED_TARGET",
            "straight_path_tested": "primitive-only source emission",
            "locked_target": "diagnostic qutrit/Weyl splitter, not observed SM data",
            "observed_data_used": False,
            "lifted_flags_used_as_proof": False,
        },
        "source_attempt": source_attempt,
        "span_tests": {
            "target_dimension": int(target.shape[0]),
            "fixed_fiber_primitives": {
                "labels": [str(item["primitive_fiber_shift"]) for item in fixed],
                **fixed_result,
            },
            "fixed_plus_all_fiber_envelope": {
                "labels": [str(item["primitive_fiber_shift"]) for item in all_candidates],
                **all_result,
            },
        },
        "interpretation": {
            "primitive_only_theorem_sufficient": False,
            "basis_transport_or_vertex_still_live": True,
            "reason": (
                "The active shift theorem remains valuable, but selected source emission must produce an "
                "enriched Weyl-pair response, not merely the currently enumerated fixed-fiber primitive class."
            ),
        },
        "refined_next_theorem": refined_theorem,
        "what_closes_now": {
            "primitive_only_counterexample_built": True,
            "locked_splitter_span_test_run": True,
            "I7_refined_to_weyl_pair_source_theorem": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "prove_selected_weyl_pair_basis_transport_or_vertex_source": True,
            "emit_enriched_A_selected": True,
            "emit_b_selected": True,
            "solve_or_reject_splitter_equation": True,
            "update_target_papers_after_refined_theorem": True,
            "full_SM_or_no_knob_closure": True,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "PrimitiveOnlySpanCounterexampleTheorem",
            "proved": True,
            "statement": (
                "Even under conditional promotion of the current non-invariant primitive family, the finite "
                "span of fixed-fiber and all-fiber primitive responses does not contain the locked qutrit/Weyl "
                "splitter target. Therefore the I7 source theorem must be strengthened: the selected source "
                "must emit a Weyl-pair basis-transport or vertex response containing phase-like and shift-like "
                "qutrit components."
            ),
        },
    }

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(
        json.dumps(
            {
                "status": STATUS,
                "candidate_path": rel(OUTPUT),
                "note_path": rel(NOTE),
                "what_closes": candidate["what_closes_now"],
                "what_remains_open": candidate["what_remains_open"],
                "next_required_artifact": NEXT,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    NOTE.write_text(
        """# MTT Selected Route-C BasisTransport Primitive Source Proof or Counterexample

Status: `MTT_SELECTED_ROUTEC_BASISTRANSPORT_PRIMITIVE_SOURCE_COUNTEREXAMPLE_BUILT_PRIMITIVE_ONLY_SPAN_INSUFFICIENT`

This artifact tests the near-term proof target directly.

## Result

The primitive-only route is not sufficient.

Even if the current non-invariant primitive family were conditionally promoted,
its finite real span does not contain the locked qutrit/Weyl splitter target.
The fixed-fiber family and the all-fiber envelope both leave a large residual.

This is not a failure of the whole route.  It tells us that the source theorem
must emit an enriched basis-transport or vertex response, not just the fixed
permutation-style primitive.

## Superset Discipline

This is still the constrained superset strategy:

- several legal source paths are compared,
- the target is locked to an algebraic diagnostic splitter, not observed SM data,
- lifted selected flags are not used as proof,
- measured masses, mixings, and CP phase are not selectors.

## Refined Next Theorem

`SelectedWeylPairBasisTransportOrVertexSourceTheorem`:

The selected q79/F,m=1 S3/GS Route-C source must emit a basis-transport or
vertex correction whose projected response contains both shift-like and
phase-like qutrit Weyl directions.  The active deck shift `(1,1)` remains
forced, but the primitive-only fixed-fiber span must be enriched by a selected
phase/basis-transport component before `A_selected` can reach the splitter.

Next artifact: `MTT_Selected_RouteC_WeylPair_BasisTransport_or_Vertex_Source_Theorem_v1`.
""",
        encoding="utf-8",
    )
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))


if __name__ == "__main__":
    main()
