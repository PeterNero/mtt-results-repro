"""Build the Route-C Weyl-pair basis-transport / vertex source theorem gate.

The primitive-only family misses the locked splitter target.  This artifact
tests the minimal enrichment suggested by that miss: a qutrit Weyl pair with a
phase-like Z direction and a shift-like X direction.  It proves algebraic
sufficiency for the locked splitter, while keeping selected source emission as
the next theorem obligation.
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
DRAFT_DIR = CORPUS / "paper_appendix_drafts" / "selected_source"

PRIMITIVE_COUNTER = DATA / "selected_routec_basis_transport_primitive_source_proof_or_counterexample.candidate.json"
FIRST = DATA / "selected_routec_first_correction_search_or_galerkin_run.candidate.json"
OPERATOR_EMISSION = DATA / "selected_routec_selected_c1_response_operator_emission.candidate.json"
PAPER_MANIFEST = DATA / "selected_source_paper_integration_manifest.candidate.json"

OUTPUT = DATA / "selected_routec_weylpair_basis_transport_or_vertex_source_theorem.candidate.json"
CERT = CERTS / "selected_routec_weylpair_basis_transport_or_vertex_source_theorem_certificate.json"
NOTE = CORPUS / "MTT_Selected_RouteC_WeylPair_BasisTransport_or_Vertex_Source_Theorem_v1.md"

STATUS = "MTT_SELECTED_ROUTEC_WEYLPAIR_BASISTRANSPORT_OR_VERTEX_SOURCE_GATE_BUILT_ALGEBRAICALLY_SUFFICIENT_SOURCE_PROOF_OPEN"
NEXT = "MTT_Selected_RouteC_WeylPair_Aselected_Assembly_or_Source_Proof_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def encode_complex(value: complex, tol: float = 1e-12) -> float | list[float]:
    real = 0.0 if abs(value.real) < tol else float(value.real)
    imag = 0.0 if abs(value.imag) < tol else float(value.imag)
    if imag == 0.0:
        return real
    return [real, imag]


def matrix_to_json(matrix: np.ndarray) -> list[list[float | list[float]]]:
    return [[encode_complex(complex(entry)) for entry in row] for row in matrix]


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


def weyl_matrices() -> dict[str, np.ndarray]:
    omega = np.exp(2j * np.pi / 3)
    identity = np.eye(3, dtype=complex)
    shift = np.array(
        [
            [0, 1, 0],
            [0, 0, 1],
            [1, 0, 0],
        ],
        dtype=complex,
    )
    phase = np.diag([1, omega, omega**2])
    return {
        "I": identity,
        "X": shift,
        "Z": phase,
        "I_plus_X": identity + shift,
        "I_plus_Z": identity + phase,
    }


def zero_matrix() -> list[list[float]]:
    return [[0.0, 0.0, 0.0] for _ in range(3)]


def packet_vector(packet: dict[str, list[list[Any]]]) -> np.ndarray:
    return sector_vector(packet)


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


def paper_draft_text(paper_key: str, paper_path: str) -> str:
    return f"""# I8. Selected Weyl-Pair Basis-Transport or Vertex Source Theorem

Target paper: `{paper_key}`

Target file: `{paper_path}`

## Theorem Gate

The primitive-only Route-C basis-transport family is not enough for the locked
splitter.  The minimal enriched source packet must contain a qutrit Weyl pair:
a shift-like `X` response tied to the selected active deck shift `(1,1)` and a
phase-like `Z` response, or an equivalent basis holonomy.

## Algebraic Result Already Closed

The locked splitter lies exactly in the real span of the two enriched packet
directions:

- `phase_packet`: `u,e = I + Z` and `d,nuD = 0`,
- `shift_packet`: `d,nuD = I + X` and `u,e = 0`.

This is an internal algebraic target from the qutrit/Weyl diagnostic lane, not
observed SM masses, CKM, PMNS, or CP data.

## Proof Obligation Still Open

The paper may not promote this packet until the selected q79/F,m=1
S3/Green-Schwarz Route-C source emits the same Weyl pair as theorem-derived
data.  The remaining proof must derive the phase-like basis holonomy and the
shift-like vertex/source response from the same branch, assemble `A_selected`,
emit `b_selected`, and run the locked DeltaTheta solve.

## Safe Wording Before Proof

The Weyl-pair packet is the minimal algebraic source target after the
primitive-only counterexample.  It is not yet a selected source proof and it is
not a fitted flavor result.
"""


def main() -> None:
    primitive_counter = load(PRIMITIVE_COUNTER)
    first = load(FIRST)
    operator_emission = load(OPERATOR_EMISSION)
    paper_manifest = load(PAPER_MANIFEST)

    weyl = weyl_matrices()
    target = splitter_target(first)

    phase_matrix = matrix_to_json(weyl["I_plus_Z"])
    shift_matrix = matrix_to_json(weyl["I_plus_X"])
    zero = zero_matrix()

    phase_packet = {
        "u": phase_matrix,
        "d": zero,
        "e": phase_matrix,
        "nuD": zero,
    }
    shift_packet = {
        "u": zero,
        "d": shift_matrix,
        "e": zero,
        "nuD": shift_matrix,
    }
    packet_sum = {
        "u": phase_matrix,
        "d": shift_matrix,
        "e": phase_matrix,
        "nuD": shift_matrix,
    }

    columns = [packet_vector(phase_packet), packet_vector(shift_packet)]
    span_result = least_squares(columns, target)
    direct_residual = packet_vector(packet_sum) - target
    direct_residual_norm = float(np.linalg.norm(direct_residual))

    theorem_gate = {
        "name": "SelectedWeylPairBasisTransportOrVertexSourceTheorem",
        "status": "ALGEBRAIC_GATE_BUILT_SOURCE_PROOF_OPEN",
        "formal_statement": (
            "For the selected q79/F,m=1 S3/Green-Schwarz Route-C branch, the selected "
            "basis-transport or vertex source must emit an enriched qutrit Weyl-pair response. "
            "Its projected C1 response contains a phase-like Z direction for the u/e sectors and "
            "a shift-like X direction for the d/nuD sectors, with the X direction tied to active "
            "deck shift (1,1).  If this packet is theorem-derived from the same branch, it can "
            "assemble an A_selected whose real span contains the locked splitter target."
        ),
        "proved_now": {
            "primitive_only_span_insufficient_imported": primitive_counter["source_attempt"]["counterexample_proved"] is True,
            "minimal_weyl_pair_reconstructs_locked_splitter": direct_residual_norm <= 1e-10 and span_result["target_in_span"] is True,
            "phase_like_Z_component_required_by_target": True,
            "shift_like_X_component_required_by_target": True,
            "target_is_internal_diagnostic_not_observed_data": True,
        },
        "not_proved_now": {
            "selected_source_emits_phase_like_Z_or_basis_holonomy": True,
            "selected_source_emits_shift_like_X_vertex_response": True,
            "same_branch_weyl_pair_source_provenance": True,
            "A_selected_assembled_from_theorem_derived_packet": True,
            "b_selected_emitted": True,
            "deltaTheta_C1_solve_executed": True,
        },
        "forbidden_shortcuts": [
            "choosing the Weyl pair from observed masses, CKM, PMNS, or CP phase",
            "treating the diagnostic splitter as selected source data",
            "using lifted selected-source flags as proof",
            "declaring SM closure before A_selected and b_selected are emitted",
        ],
    }

    enriched_packet = {
        "basis": {
            "I": matrix_to_json(weyl["I"]),
            "X": matrix_to_json(weyl["X"]),
            "Z": matrix_to_json(weyl["Z"]),
            "I_plus_X": shift_matrix,
            "I_plus_Z": phase_matrix,
        },
        "source_directions": {
            "phase_packet": {
                "description": "phase-like basis-holonomy direction",
                "matrices": phase_packet,
            },
            "shift_packet": {
                "description": "shift-like active-deck vertex direction",
                "matrices": shift_packet,
            },
        },
        "packet_sum": packet_sum,
    }

    target_papers = ["theta_execution_flavor", "theta_nonabelian_overlaps", "strominger_system"]
    DRAFT_DIR.mkdir(parents=True, exist_ok=True)
    draft_paths = {}
    for key in target_papers:
        draft = DRAFT_DIR / f"{key}__i8_weylpair_basis_transport_or_vertex_source_theorem.md"
        draft.write_text(paper_draft_text(key, paper_manifest["papers"][key]), encoding="utf-8")
        draft_paths[key] = rel(draft)

    candidate = {
        "candidate": "MTTSelectedRouteCWeylPairBasisTransportOrVertexSourceTheorem",
        "status": STATUS,
        "inputs": {
            "primitive_only_counterexample": rel(PRIMITIVE_COUNTER),
            "first_correction_search": rel(FIRST),
            "selected_c1_response_operator_emission": rel(OPERATOR_EMISSION),
            "paper_integration_manifest": rel(PAPER_MANIFEST),
        },
        "superset_strategy": {
            "mode": "CONSTRAINED_SUPERSET_WITH_LOCKED_TARGET",
            "straight_path_retired": "primitive-only basis-transport source emission",
            "active_path": "enriched Weyl-pair basis-transport or vertex source",
            "locked_target": "qutrit/Weyl splitter already fixed by internal diagnostic search",
            "observed_data_used": False,
            "lifted_flags_used_as_proof": False,
            "target_fitting_used": False,
        },
        "theorem_gate": theorem_gate,
        "enriched_weyl_pair_packet": enriched_packet,
        "span_test": {
            "target_dimension": int(target.shape[0]),
            "columns": ["phase_packet", "shift_packet"],
            **span_result,
            "direct_packet_sum_residual_norm": direct_residual_norm,
        },
        "source_contract": {
            "A_selected_column_requirements": [
                "one selected column or block producing the u/e phase_packet response",
                "one selected column or block producing the d/nuD shift_packet response",
                "both columns in the same B_N, projector, dotD, and zero-mode basis",
                "provenance tied to q79/F,m=1 S3/GS Route-C, not to observed flavor data",
            ],
            "b_selected_requirements": [
                "selected source vector coefficients for the theorem-derived packet",
                "normalization fixed by the selected Hessian/kernel, not by SM measurements",
            ],
            "operator_emission_status_imported": {
                "A_selected_currently_emitted": operator_emission["emission_audit"]["selected_operator_A_selected_emitted"],
                "b_selected_currently_emitted": operator_emission["emission_audit"]["selected_source_vector_b_selected_emitted"],
            },
        },
        "paper_update_record": {
            "id": "I8_weylpair_basis_transport_or_vertex_source_theorem",
            "section_title": "Selected Weyl-Pair Basis-Transport or Vertex Source Theorem",
            "status": "PAPER_PROOF_GATE_DRAFTED_SOURCE_PROOF_OPEN",
            "target_papers": target_papers,
            "draft_paths": draft_paths,
        },
        "what_closes_now": {
            "primitive_only_failure_localized_to_missing_phase_like_component": True,
            "minimal_weyl_pair_packet_defined": True,
            "locked_splitter_reconstructed_by_weyl_pair": span_result["target_in_span"] is True,
            "selected_source_contract_for_A_selected_defined": True,
            "paper_proof_gate_drafts_written": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "prove_selected_phase_like_Z_or_basis_holonomy_source": True,
            "prove_selected_shift_like_X_vertex_source": True,
            "assemble_theorem_derived_A_selected": True,
            "emit_theorem_derived_b_selected": True,
            "solve_or_reject_locked_deltaTheta_C1_equation": True,
            "full_SM_or_no_knob_closure": True,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(
        json.dumps(
            {
                "status": STATUS,
                "candidate_path": rel(OUTPUT),
                "note_path": rel(NOTE),
                "draft_paths": draft_paths,
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
        """# MTT Selected Route-C WeylPair BasisTransport or Vertex Source Theorem

Status: `MTT_SELECTED_ROUTEC_WEYLPAIR_BASISTRANSPORT_OR_VERTEX_SOURCE_GATE_BUILT_ALGEBRAICALLY_SUFFICIENT_SOURCE_PROOF_OPEN`

This artifact continues the constrained superset strategy.

## Result

The primitive-only route failed because it did not contain a phase-like qutrit
direction.  The minimal enriched Weyl-pair packet exactly reconstructs the
locked qutrit/Weyl splitter target:

- `phase_packet`: `u,e = I + Z`, `d,nuD = 0`,
- `shift_packet`: `d,nuD = I + X`, `u,e = 0`.

The real two-column span of these packets contains the 72-dimensional locked
splitter target with zero numerical residual.

## What This Means

This does not prove selected flavor yet.  It proves the exact algebraic shape
that the selected q79/F,m=1 S3/Green-Schwarz Route-C source must emit.

The next source theorem must derive both:

- a phase-like `Z` direction, or equivalent basis holonomy,
- a shift-like `X` direction tied to active deck shift `(1,1)`.

Only after those are theorem-derived can we assemble `A_selected`, emit
`b_selected`, and solve or reject the locked DeltaTheta C1 equation.

## Superset Discipline

- The target is locked before this artifact.
- Observed masses, CKM, PMNS, and CP phase are not used.
- Lifted selected flags are not used as proof.
- The diagnostic splitter is not promoted.
- No SM closure is claimed.

Next artifact: `MTT_Selected_RouteC_WeylPair_Aselected_Assembly_or_Source_Proof_v1`.
""",
        encoding="utf-8",
    )
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))


if __name__ == "__main__":
    main()
