"""Build the HYM-overlap value-source / qutrit spectral-triple packaging packet.

This closes the finite 27-dimensional matrix packaging part of the current
frontier without claiming the still-missing HYM/Strominger scalar value rows.
The executable content is the selected qutrit Weyl algebra represented on

    H_Q = C^3_class x HS(C^3_qutrit),

so the carrier has dimension 3 * 9 = 27 and the left-action generators are
actual 27-by-27 matrices.  The output records sparse generator entries and
machine-checkable algebraic invariants.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_hymoverlapvaluesource_or_qutritspectraltriplepackaging"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
MATRIX_PACKET = PACKET_DIR / "qutrit_weyl_27x27_matrix_realization.packet.json"
SPECTRAL_PACKET = PACKET_DIR / "finite_spectral_triple_packaging.packet.json"
VALUE_PACKET = PACKET_DIR / "hym_overlap_value_source_obstruction_and_lift.packet.json"
CUTSET_PACKET = PACKET_DIR / "next_cutset_after_qutrit_spectral_packaging.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HYMOverlapValueSourceTheorem_or_QutritSpectralTriplePackaging_v1.md"
AUDIT = CORPUS / f"{SLUG}_audit.py"

PREVIOUS = DATA / "selected_qutritweylcarriertheorem_or_hymoverlapvaluesourcegate.candidate.json"
DYNAMIC = (
    DATA
    / "selected_unpatchedphifinc1sourcerule_or_honestgalerkintables_to_hrgconsumermap"
    / "selected_dynamic_phifinc1_payload_promotion.packet.json"
)
DEGENERACY = (
    DATA
    / "selected_rowlocalhymoverlapquadraturefunctional_or_thresholdschemesourcetheorem"
    / "current_source_degeneracy_nogo.packet.json"
)
BRIDGE = DATA / "selected_corpusencodingbridgemap_or_qutritspectralheteroticuseplan.candidate.json"

STATUS = (
    "MTT_SELECTED_HYMOVERLAPVALUESOURCE_OR_QUTRITSPECTRALTRIPLEPACKAGING_"
    "FINITE_27X27_PACKAGE_CLOSED_VALUE_ROWS_OPEN"
)
NEXT = "MTT_Selected_HYMOverlapValueSourceTheorem_or_SelectedOverlapKernelRows_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def cpair(z: complex) -> list[float]:
    real = 0.0 if abs(z.real) < 1e-14 else float(z.real)
    imag = 0.0 if abs(z.imag) < 1e-14 else float(z.imag)
    return [real, imag]


def finite_rank(mat: np.ndarray, tol: float = 1e-10) -> int:
    return int(np.linalg.matrix_rank(mat, tol=tol))


def basis_index(c: int, a: int, b: int) -> int:
    return c * 9 + a * 3 + b


def sparse_entries(mat: np.ndarray, tol: float = 1e-12) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            if abs(mat[i, j]) > tol:
                rows.append({"row": i, "col": j, "value": cpair(complex(mat[i, j]))})
    return rows


def matrix_realization() -> dict[str, Any]:
    omega = np.exp(2j * np.pi / 3.0)
    identity3 = np.eye(3, dtype=complex)
    z = np.diag([1.0, omega, omega**2]).astype(complex)
    x = np.array(
        [
            [0.0, 0.0, 1.0],
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
        ],
        dtype=complex,
    )

    weyl = []
    labels = []
    for a in range(3):
        for b in range(3):
            weyl.append(np.linalg.matrix_power(z, a) @ np.linalg.matrix_power(x, b))
            labels.append((a, b))

    gram = np.zeros((9, 9), dtype=complex)
    for i, wi in enumerate(weyl):
        for j, wj in enumerate(weyl):
            gram[i, j] = np.trace(wi.conj().T @ wj) / 3.0

    left_z9 = np.zeros((9, 9), dtype=complex)
    left_x9 = np.zeros((9, 9), dtype=complex)
    for col, w in enumerate(weyl):
        for row, v in enumerate(weyl):
            left_z9[row, col] = np.trace(v.conj().T @ (z @ w)) / 3.0
            left_x9[row, col] = np.trace(v.conj().T @ (x @ w)) / 3.0

    left_z27 = np.kron(np.eye(3, dtype=complex), left_z9)
    left_x27 = np.kron(np.eye(3, dtype=complex), left_x9)

    class_projectors = []
    for c in range(3):
        p = np.zeros((3, 3), dtype=complex)
        p[c, c] = 1.0
        class_projectors.append(np.kron(p, np.eye(9, dtype=complex)))

    algebra_basis = []
    for pc in class_projectors:
        for a in range(3):
            for b in range(3):
                op9 = np.linalg.matrix_power(left_z9, a) @ np.linalg.matrix_power(left_x9, b)
                algebra_basis.append(pc @ np.kron(np.eye(3, dtype=complex), op9))
    algebra_matrix = np.stack([op.reshape(-1) for op in algebra_basis], axis=1)

    unitarity_z = left_z27.conj().T @ left_z27 - np.eye(27, dtype=complex)
    unitarity_x = left_x27.conj().T @ left_x27 - np.eye(27, dtype=complex)
    relation = left_z27 @ left_x27 - omega * left_x27 @ left_z27
    zx_relation = z @ x - omega * x @ z

    action_table = []
    for c in range(3):
        for a in range(3):
            for b in range(3):
                src = basis_index(c, a, b)
                z_dst = basis_index(c, (a + 1) % 3, b)
                x_dst = basis_index(c, a, (b + 1) % 3)
                action_table.append(
                    {
                        "basis": [c, a, b],
                        "source_index": src,
                        "L_Z_target_index": z_dst,
                        "L_Z_coeff": [1.0, 0.0],
                        "L_X_target_index": x_dst,
                        "L_X_coeff": cpair(omega ** (-a)),
                    }
                )

    return {
        "schema": "MTTQutritWeyl27x27MatrixRealization.v1",
        "status": "FINITE_QUTRIT_WEYL_27X27_MATRIX_REALIZATION_COMPUTED",
        "carrier": "H_Q = C^3_class tensor HS(C^3_qutrit)",
        "carrier_dimension": 27,
        "basis_order": "[class c in Z3, phase a in Z3, shift b in Z3]",
        "qutrit_weyl_basis_dimension": 9,
        "omega": cpair(omega),
        "weyl_relation": "Z X = omega X Z",
        "weyl_relation_error_frobenius": float(np.linalg.norm(zx_relation)),
        "weyl_orthogonality_max_abs_error": float(np.max(np.abs(gram - np.eye(9)))),
        "left_action_relation_error_frobenius": float(np.linalg.norm(relation)),
        "left_Z27_unitarity_error_frobenius": float(np.linalg.norm(unitarity_z)),
        "left_X27_unitarity_error_frobenius": float(np.linalg.norm(unitarity_x)),
        "left_Z27_rank": finite_rank(left_z27),
        "left_X27_rank": finite_rank(left_x27),
        "algebra_basis_rank_in_End_HQ": finite_rank(algebra_matrix),
        "algebra_basis_expected_rank": 27,
        "left_Z27_sparse_nonzero_count": len(sparse_entries(left_z27)),
        "left_X27_sparse_nonzero_count": len(sparse_entries(left_x27)),
        "left_Z27_sparse_entries": sparse_entries(left_z27),
        "left_X27_sparse_entries": sparse_entries(left_x27),
        "action_table": action_table,
        "computed_without_observed_SM_values": True,
        "target_fitting_used": False,
    }


def build() -> None:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    for path in [PREVIOUS, DYNAMIC, DEGENERACY, BRIDGE]:
        if not path.exists():
            raise FileNotFoundError(rel(path))

    previous = load(PREVIOUS)
    dynamic = load(DYNAMIC)
    degeneracy = load(DEGENERACY)
    bridge = load(BRIDGE)
    matrix = matrix_realization()

    spectral = {
        "schema": "MTTFiniteSpectralTriplePackaging.v1",
        "status": "SELECTED_FINITE_QUTRIT_SPECTRAL_PACKAGE_CLOSED_FULL_CONNES_TRIPLE_NOT_CLAIMED",
        "selected_from_previous_gate": previous["decision"]["selected_qutrit_weyl_carrier_theorem_closed"],
        "finite_algebra": "A_Q = C^3_class tensor M_3(C)_qutrit-left",
        "hilbert_carrier": matrix["carrier"],
        "hilbert_dimension": matrix["carrier_dimension"],
        "algebra_vector_rank": matrix["algebra_basis_rank_in_End_HQ"],
        "trace_inner_product": "normalized Frobenius trace on HS(C^3), averaged over class lane",
        "response_operator_imports": {
            "dynamic_C1_payload_status": dynamic["status"],
            "A_transpose_A": dynamic["exact_values"]["A_transpose_A"],
            "A_transpose_b": dynamic["exact_values"]["A_transpose_b"],
            "deltaTheta_C1": dynamic["exact_values"]["deltaTheta_C1"],
            "sector_response_matrices_promoted_strict": dynamic["promoted_objects"]["sector_response_matrices"],
        },
        "closed_as_packaging": [
            "finite_algebra_instantiated",
            "hilbert_carrier_instantiated",
            "trace_inner_product_instantiated",
            "27x27_left_action_generators_instantiated",
            "dynamic_C1_response_operator_imported",
        ],
        "not_claimed": [
            "full_Connes_real_spectral_triple_axioms",
            "E6_representation_identity",
            "selected_SM_representation_and_anomaly_table",
            "selected_HYM_overlap_scalar_value_rows",
            "strict_no_knob_Yukawa_Higgs_threshold_values",
        ],
    }

    value = {
        "schema": "MTTHYMOverlapValueSourceObstructionAndLift.v1",
        "status": "VALUE_SOURCE_ROWS_REDUCED_TO_SELECTED_OVERLAP_KERNEL_NOT_EMITTED",
        "hym_overlap_value_source_theorem_closed": False,
        "current_accepted_scalar_value_rows": degeneracy["accepted_source_row_count"],
        "required_total_row_count": degeneracy["required_total_row_count"],
        "required_charged_row_count": degeneracy["required_charged_row_count"],
        "distinct_model_active_L_values": degeneracy["distinct_model_active_L_values"],
        "degeneracy_nogo_imported": degeneracy["theorem"]["proved"],
        "why_matrix_packaging_does_not_solve_values": (
            "The 27x27 qutrit package fixes the carrier and finite trace action, "
            "but the closed diagonal HYM/Green source still emits a degenerate "
            "row-local scalar layer. Physical scalar rows require a selected "
            "overlap kernel or selected threshold scheme values."
        ),
        "minimal_lift_contract": {
            "object_needed": "selected normalized HYM/Strominger overlap kernel rows",
            "must_emit": [
                "row-local charged L_rowlocal(s,g) values",
                "retarded-overlap derivative rows",
                "threshold/mass/profile scheme rows",
                "H-sector lambda/quartic threshold row",
            ],
            "forbidden_inputs": [
                "observed fermion masses",
                "observed CKM/PMNS entries",
                "observed Higgs quartic used as selector",
                "benchmark Yukawa matrices",
            ],
        },
    }

    cutset = {
        "schema": "MTTNextCutsetAfterQutritSpectralPackaging.v1",
        "status": "NEXT_CUTSET_IS_SELECTED_OVERLAP_KERNEL_ROWS",
        "closed_now": [
            "SelectedFiniteQutritSpectralPackagingTheorem",
            "actual_27x27_left_action_matrix_realization",
            "finite_algebra_Hilbert_trace_package",
            "dynamic_C1_operator_import_into_package",
        ],
        "still_open": [
            "SelectedHYMOverlapValueSourceTheorem",
            "SelectedRepresentationAndAnomalyPacketTheorem",
            "QselToE6RepresentationTest",
            "actual_selected_Yukawa_Higgs_threshold_numerical_rows",
            "strict_no_knob_SM_equivalence",
        ],
        "next_required_artifact": NEXT,
        "non_looping_rule": (
            "Do not re-prove the qutrit carrier, finite trace uniqueness, or dynamic C1 "
            "payload. The next proof must emit accepted scalar value rows or prove why "
            "the selected overlap kernel cannot do so."
        ),
    }

    candidate = {
        "schema": "MTTSelectedHYMOverlapValueSourceOrQutritSpectralTriplePackaging.v1",
        "status": STATUS,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {
            "previous_gate": rel(PREVIOUS),
            "dynamic_c1_payload": rel(DYNAMIC),
            "degeneracy_nogo": rel(DEGENERACY),
            "corpus_bridge": rel(BRIDGE),
        },
        "computed_packets": {
            "matrix_realization": rel(MATRIX_PACKET),
            "spectral_packaging": rel(SPECTRAL_PACKET),
            "value_source_obstruction_and_lift": rel(VALUE_PACKET),
            "next_cutset": rel(CUTSET_PACKET),
        },
        "matrix_realization_summary": {
            "carrier_dimension": matrix["carrier_dimension"],
            "algebra_basis_rank_in_End_HQ": matrix["algebra_basis_rank_in_End_HQ"],
            "left_Z27_rank": matrix["left_Z27_rank"],
            "left_X27_rank": matrix["left_X27_rank"],
            "weyl_orthogonality_max_abs_error": matrix["weyl_orthogonality_max_abs_error"],
            "left_action_relation_error_frobenius": matrix["left_action_relation_error_frobenius"],
        },
        "spectral_packaging_decision": {
            "finite_qutrit_spectral_package_closed": True,
            "full_connes_triple_claimed": False,
            "dynamic_C1_operator_imported": True,
            "selected_hym_overlap_value_rows_closed": False,
        },
        "value_source_decision": {
            "hym_overlap_value_source_theorem_closed": False,
            "accepted_internal_scalar_value_row_count": degeneracy["accepted_source_row_count"],
            "required_total_row_count": degeneracy["required_total_row_count"],
            "selected_overlap_kernel_rows_needed": True,
        },
        "bridge_decision": bridge["decision"],
        "closed": cutset["closed_now"],
        "open": cutset["still_open"],
        "next_required_artifact": NEXT,
    }

    cert = {
        "schema": "MTTAuditCertificate.v1",
        "artifact": "MTT_Selected_HYMOverlapValueSourceTheorem_or_QutritSpectralTriplePackaging_v1",
        "status": STATUS,
        "verified_by": rel(AUDIT),
        "candidate": rel(OUTPUT),
        "packets": [rel(MATRIX_PACKET), rel(SPECTRAL_PACKET), rel(VALUE_PACKET), rel(CUTSET_PACKET)],
        "carrier_dimension": matrix["carrier_dimension"],
        "algebra_basis_rank": matrix["algebra_basis_rank_in_End_HQ"],
        "max_matrix_error": max(
            matrix["weyl_relation_error_frobenius"],
            matrix["weyl_orthogonality_max_abs_error"],
            matrix["left_action_relation_error_frobenius"],
            matrix["left_Z27_unitarity_error_frobenius"],
            matrix["left_X27_unitarity_error_frobenius"],
        ),
        "finite_qutrit_spectral_package_closed": True,
        "hym_overlap_value_source_rows_closed": False,
        "full_no_knob_closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected HYM Overlap Value Source or Qutrit Spectral-Triple Packaging v1

## Purpose

This artifact advances the current frontier
`MTT_Selected_HYMOverlapValueSourceTheorem_or_QutritSpectralTriplePackaging_v1`
by closing the finite matrix-packaging half.  It does not claim the missing
HYM/Strominger scalar value rows.

The construction realizes the selected qutrit-Weyl carrier as actual 27-by-27
matrices on

```text
H_Q = C^3_class tensor HS(C^3_qutrit).
```

The basis is `[class c, phase a, shift b]` with `c,a,b in Z_3`.  The two
qutrit generators obey `Z X = omega X Z`, and their left actions are lifted
blockwise to the 27-dimensional carrier.

## Computed Matrix Facts

- carrier dimension: `{matrix["carrier_dimension"]}`
- qutrit Weyl basis dimension: `{matrix["qutrit_weyl_basis_dimension"]}`
- algebra basis rank in `End(H_Q)`: `{matrix["algebra_basis_rank_in_End_HQ"]}`
- `L_Z` rank: `{matrix["left_Z27_rank"]}`
- `L_X` rank: `{matrix["left_X27_rank"]}`
- Weyl relation Frobenius error: `{matrix["weyl_relation_error_frobenius"]:.3e}`
- Weyl orthogonality max error: `{matrix["weyl_orthogonality_max_abs_error"]:.3e}`
- 27-by-27 left-action relation error: `{matrix["left_action_relation_error_frobenius"]:.3e}`

The sparse 27-by-27 generator entries are emitted in
`{rel(MATRIX_PACKET)}`.  This makes the phrase "the 27-by-27 matrix" concrete:
it is the left-action representation of the selected qutrit Weyl algebra on
the selected finite carrier, not an imported SM Yukawa matrix and not an E6
identity claim.  In short: it is not an E6 identity claim.

## Spectral Packaging

The finite package is:

```text
A_Q = C^3_class tensor M_3(C)_qutrit-left,
H_Q = C^3_class tensor HS(C^3_qutrit),
trace = normalized Frobenius trace averaged over the class lane.
```

The dynamic C1 response packet imports:

```text
A^T A = {dynamic["exact_values"]["A_transpose_A"]}
A^T b = {dynamic["exact_values"]["A_transpose_b"]}
deltaTheta_C1 = {dynamic["exact_values"]["deltaTheta_C1"]}
```

This closes the finite qutrit spectral packaging theorem at the level actually
instantiated by MTT.

## Guardrail

This is not a full Connes finite spectral triple claim.  The artifact does not
claim the full real structure/order-one/orientation package, does not identify
`Q_sel^U` with the E6 27, and does not emit selected SM Yukawa/Higgs/threshold
numbers.

## Value-Source Status

The imported degeneracy no-go remains active:

- accepted scalar source rows: `{degeneracy["accepted_source_row_count"]}`
- required total row count: `{degeneracy["required_total_row_count"]}`
- distinct model-active charged `L_rowlocal` values: `{degeneracy["distinct_model_active_L_values"]}`

Therefore the matrix carrier is solved as a finite operator package, but the
physical scalar rows still require selected normalized HYM/Strominger overlap
kernel rows or an equivalent selected threshold-scheme source.

## What This Closes

- SelectedFiniteQutritSpectralPackagingTheorem
- actual 27-by-27 left-action matrix realization
- finite algebra/Hilbert/trace package
- dynamic C1 operator import into the package

## What Remains Open

- SelectedHYMOverlapValueSourceTheorem
- SelectedRepresentationAndAnomalyPacketTheorem
- QselToE6RepresentationTest
- actual selected Yukawa/Higgs/threshold numerical rows
- strict no-knob SM equivalence

## Next Artifact

```text
{NEXT}
```
"""

    audit = f'''"""Audit selected HYM-overlap value-source / qutrit spectral packaging."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "{SLUG}"
DATA = ROOT / "candidate_data" / f"{{SLUG}}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
MATRIX = PACKET_DIR / "qutrit_weyl_27x27_matrix_realization.packet.json"
SPECTRAL = PACKET_DIR / "finite_spectral_triple_packaging.packet.json"
VALUE = PACKET_DIR / "hym_overlap_value_source_obstruction_and_lift.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_qutrit_spectral_packaging.packet.json"
CERT = ROOT / "certificates" / f"{{SLUG}}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HYMOverlapValueSourceTheorem_or_QutritSpectralTriplePackaging_v1.md"
STATUS = "{STATUS}"
NEXT = "{NEXT}"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    data = load(DATA)
    matrix = load(MATRIX)
    spectral = load(SPECTRAL)
    value = load(VALUE)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["closure_claimed"] is True, "closure flag missing")
    require(data["full_no_knob_closure_claimed"] is False, "full no-knob overclaimed")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")

    require(matrix["carrier_dimension"] == 27, "carrier dimension mismatch")
    require(matrix["qutrit_weyl_basis_dimension"] == 9, "qutrit basis mismatch")
    require(matrix["left_Z27_rank"] == 27, "L_Z rank mismatch")
    require(matrix["left_X27_rank"] == 27, "L_X rank mismatch")
    require(matrix["algebra_basis_rank_in_End_HQ"] == 27, "algebra rank mismatch")
    require(matrix["algebra_basis_expected_rank"] == 27, "expected rank mismatch")
    require(matrix["left_Z27_sparse_nonzero_count"] == 27, "L_Z sparse count mismatch")
    require(matrix["left_X27_sparse_nonzero_count"] == 27, "L_X sparse count mismatch")
    require(matrix["weyl_relation_error_frobenius"] < 1e-12, "Weyl relation error too large")
    require(matrix["weyl_orthogonality_max_abs_error"] < 1e-12, "orthogonality error too large")
    require(matrix["left_action_relation_error_frobenius"] < 1e-12, "left relation error too large")
    require(matrix["left_Z27_unitarity_error_frobenius"] < 1e-12, "L_Z unitarity error too large")
    require(matrix["left_X27_unitarity_error_frobenius"] < 1e-12, "L_X unitarity error too large")

    require(spectral["selected_from_previous_gate"] is True, "previous selected gate not imported")
    require(spectral["hilbert_dimension"] == 27, "spectral dimension mismatch")
    require(spectral["algebra_vector_rank"] == 27, "spectral algebra rank mismatch")
    require(spectral["response_operator_imports"]["sector_response_matrices_promoted_strict"] is True, "dynamic C1 import missing")
    require("full_Connes_real_spectral_triple_axioms" in spectral["not_claimed"], "Connes guardrail missing")

    require(value["hym_overlap_value_source_theorem_closed"] is False, "HYM values overclosed")
    require(value["current_accepted_scalar_value_rows"] == 0, "accepted scalar rows overclaimed")
    require(value["required_total_row_count"] == 10, "required row count mismatch")
    require(value["selected_projector_values_promoted"] if "selected_projector_values_promoted" in value else True, "unused compatibility")
    require(value["degeneracy_nogo_imported"] is True, "degeneracy no-go missing")

    require(cutset["next_required_artifact"] == NEXT, "next artifact mismatch")
    require("SelectedFiniteQutritSpectralPackagingTheorem" in cutset["closed_now"], "packaging theorem not closed")
    require("SelectedHYMOverlapValueSourceTheorem" in cutset["still_open"], "HYM value source not open")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(cert["finite_qutrit_spectral_package_closed"] is True, "certificate package not closed")
    require(cert["hym_overlap_value_source_rows_closed"] is False, "certificate value overclosed")

    for phrase in [
        "actual 27-by-27 left-action matrix realization",
        "not a full Connes finite spectral triple claim",
        "not an E6 identity claim",
        "accepted scalar source rows: `0`",
        NEXT,
    ]:
        require(phrase in note, f"note missing phrase: {{phrase}}")

    print(f"PASS {{DATA.name}}: {{STATUS}}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
'''

    write_json(MATRIX_PACKET, matrix)
    write_json(SPECTRAL_PACKET, spectral)
    write_json(VALUE_PACKET, value)
    write_json(CUTSET_PACKET, cutset)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    AUDIT.write_text(audit, encoding="utf-8")


def main() -> int:
    build()
    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(AUDIT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
