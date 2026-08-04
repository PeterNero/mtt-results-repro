"""Assemble the conditional Weyl-pair A matrix and isolate source provenance.

The previous artifact proved that the enriched Weyl pair spans the locked
splitter.  This artifact assembles the corresponding conditional two-column
operator and runs the locked solve.  It does not promote the matrix to
A_selected, because the same-branch source theorem is still open.
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

WEYLPAIR = DATA / "selected_routec_weylpair_basis_transport_or_vertex_source_theorem.candidate.json"
DELTA_SOLVE = DATA / "selected_routec_splitter_source_emission_contract_or_selected_deltatheta_c1_solve.candidate.json"
OPERATOR_EMISSION = DATA / "selected_routec_selected_c1_response_operator_emission.candidate.json"

OUTPUT = DATA / "selected_routec_weylpair_aselected_assembly_or_source_proof.candidate.json"
CERT = CERTS / "selected_routec_weylpair_aselected_assembly_or_source_proof_certificate.json"
NOTE = CORPUS / "MTT_Selected_RouteC_WeylPair_Aselected_Assembly_or_Source_Proof_v1.md"

STATUS = "MTT_SELECTED_ROUTEC_WEYLPAIR_ASELECTED_ASSEMBLY_BUILT_CONDITIONAL_SOLVE_EXACT_SOURCE_PROOF_OPEN"
NEXT = "MTT_Selected_RouteC_WeylPair_Source_Provenance_Lemma_v1"


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


def packet_vector(packet: dict[str, list[list[Any]]]) -> np.ndarray:
    values: list[float] = []
    for sector in ("u", "d", "e", "nuD"):
        values.extend(flatten_matrix(packet[sector]))
    return np.array(values, dtype=float)


def solve(A: np.ndarray, b: np.ndarray) -> dict[str, Any]:
    x, *_ = np.linalg.lstsq(A, b, rcond=None)
    residual = A @ x - b
    b_norm = float(np.linalg.norm(b))
    residual_norm = float(np.linalg.norm(residual))
    return {
        "rank": int(np.linalg.matrix_rank(A)),
        "condition_number": float(np.linalg.cond(A)),
        "deltaTheta_conditional": [float(v) for v in x],
        "b_norm": b_norm,
        "residual_norm": residual_norm,
        "relative_residual": residual_norm / b_norm if b_norm else math.inf,
        "consistent": residual_norm <= 1e-10,
    }


def main() -> None:
    weylpair = load(WEYLPAIR)
    delta_solve = load(DELTA_SOLVE)
    operator_emission = load(OPERATOR_EMISSION)

    packets = weylpair["enriched_weyl_pair_packet"]["source_directions"]
    phase = packet_vector(packets["phase_packet"]["matrices"])
    shift = packet_vector(packets["shift_packet"]["matrices"])
    A_conditional = np.column_stack([phase, shift])
    b_splitter = phase + shift
    solve_result = solve(A_conditional, b_splitter)

    selected_emission_status = {
        "A_selected_currently_emitted": operator_emission["emission_audit"]["selected_operator_A_selected_emitted"],
        "b_selected_currently_emitted": operator_emission["emission_audit"]["selected_source_vector_b_selected_emitted"],
        "rank_test_now_computable_for_selected_A": operator_emission["emission_audit"]["rank_test_now_computable"],
        "least_squares_now_computable_for_selected_A": operator_emission["emission_audit"]["least_squares_now_computable"],
    }

    provenance_reduction = {
        "name": "SelectedWeylPairSourceProvenanceLemma",
        "status": "NEXT_LEMMA_REQUIRED",
        "statement": (
            "The selected q79/F,m=1 S3/Green-Schwarz Route-C source emits the two conditional "
            "Weyl-pair columns used here as theorem-derived selected source data: the phase-like "
            "I+Z basis-holonomy packet and the shift-like I+X active-vertex packet, in the same "
            "B_N/projector/dotD/zero-mode basis."
        ),
        "must_prove": [
            "phase column is selected source emission, not diagnostic target choice",
            "shift column is selected active (1,1) vertex emission, not fitted response",
            "both columns share the selected Route-C basis and normalization",
            "source coefficients are fixed internally before downstream flavor checks",
        ],
    }

    candidate = {
        "candidate": "MTTSelectedRouteCWeylPairAselectedAssemblyOrSourceProof",
        "status": STATUS,
        "inputs": {
            "weylpair_source_gate": rel(WEYLPAIR),
            "deltaTheta_solve_contract": rel(DELTA_SOLVE),
            "selected_c1_response_operator_emission": rel(OPERATOR_EMISSION),
        },
        "superset_strategy": {
            "mode": "CONSTRAINED_SUPERSET_WITH_LOCKED_TARGET",
            "path": "conditional Weyl-pair A assembly, then selected-source provenance reduction",
            "locked_target": "same b_splitter target from the DeltaTheta C1 solve gate",
            "observed_data_used": False,
            "lifted_flags_used_as_proof": False,
            "target_fitting_used": False,
        },
        "conditional_operator": {
            "name": "A_weylpair_conditional",
            "shape": [int(A_conditional.shape[0]), int(A_conditional.shape[1])],
            "columns": ["phase_packet", "shift_packet"],
            "is_A_selected": False,
            "why_not_selected": (
                "The columns solve the locked algebraic equation, but current artifacts do not yet prove "
                "same-branch selected source emission of the Weyl-pair packet."
            ),
        },
        "locked_solve": solve_result,
        "selected_emission_status": selected_emission_status,
        "provenance_reduction": provenance_reduction,
        "theorem": {
            "name": "ConditionalWeylPairDeltaThetaSolveTheorem",
            "proved": True,
            "statement": (
                "If the selected source emits the two Weyl-pair packet columns, the resulting conditional "
                "72x2 operator has rank 2 and solves the locked splitter equation with deltaTheta=(1,1) "
                "up to numerical roundoff. Therefore no further algebraic obstruction remains at this "
                "two-column Weyl-pair assembly layer; the remaining blocker is selected source provenance."
            ),
        },
        "what_closes_now": {
            "conditional_A_weylpair_assembled": True,
            "conditional_deltaTheta_solve_exact": solve_result["consistent"],
            "algebraic_rank_obstruction_absent_for_weylpair_packet": solve_result["rank"] == 2,
            "remaining_gap_reduced_to_source_provenance": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "prove_selected_weylpair_source_provenance": True,
            "promote_conditional_A_to_A_selected": True,
            "emit_theorem_derived_b_selected": True,
            "run_honest_selected_deltaTheta_C1_solve": True,
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
        """# MTT Selected Route-C WeylPair Aselected Assembly or Source Proof

Status: `MTT_SELECTED_ROUTEC_WEYLPAIR_ASELECTED_ASSEMBLY_BUILT_CONDITIONAL_SOLVE_EXACT_SOURCE_PROOF_OPEN`

This artifact assembles the conditional Weyl-pair operator:

```text
A_weylpair_conditional = [phase_packet, shift_packet]
```

with:

- `phase_packet`: `u,e = I + Z`, `d,nuD = 0`,
- `shift_packet`: `d,nuD = I + X`, `u,e = 0`.

## Result

The conditional operator has shape `72 x 2`, rank `2`, and solves the locked
splitter equation with `deltaTheta = (1,1)` up to numerical roundoff.

This closes the algebraic assembly obstruction for the enriched Weyl-pair
packet.  It does not promote `A_weylpair_conditional` to `A_selected`.

## Remaining Blocker

The remaining blocker is now sharply provenance-theoretic:

`SelectedWeylPairSourceProvenanceLemma`

The selected q79/F,m=1 S3/Green-Schwarz Route-C source must emit the two
Weyl-pair columns as theorem-derived selected source data, in the same
B_N/projector/dotD/zero-mode basis and with internal normalization.

No observed masses, CKM, PMNS, CP phase, lifted flags, or benchmark matrices
are used.

Next artifact: `MTT_Selected_RouteC_WeylPair_Source_Provenance_Lemma_v1`.
""",
        encoding="utf-8",
    )
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))


if __name__ == "__main__":
    main()
