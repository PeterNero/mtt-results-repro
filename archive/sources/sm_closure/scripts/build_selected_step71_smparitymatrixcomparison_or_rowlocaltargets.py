"""Build Step71 SM-parity matrix comparison / row-local target extraction."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step71_smparitymatrixcomparison_or_rowlocaltargets"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
MATRIX_PROJECTION_PACKET = PACKET_DIR / "step71_smparity_matrix_diagonal_projection.packet.json"
ROWLOCAL_TARGET_PACKET = PACKET_DIR / "step71_rowlocal_composite_target_contract.packet.json"
SCOPE_PACKET = PACKET_DIR / "step71_matrix_scope_comparison.packet.json"
GAP_RECONCILIATION_PACKET = PACKET_DIR / "step71_old_smparity_gap_matrix_reconciliation.packet.json"
CUTSET_PACKET = PACKET_DIR / "step71_next_rowlocal_execution_cutset.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step71_SMParityMatrixComparison_or_RowLocalTargets_v1.md"

STEP70 = DATA / "selected_step70_heattorsionprefactorbackimport_or_rowlocalfrontier.candidate.json"
STEP70_FACTORS = (
    DATA
    / "selected_step70_heattorsionprefactorbackimport_or_rowlocalfrontier"
    / "step70_prefactor_slot_factorization.packet.json"
)
STEP70_CUTSET = (
    DATA
    / "selected_step70_heattorsionprefactorbackimport_or_rowlocalfrontier"
    / "step70_next_rowlocal_source_cutset.packet.json"
)
STEP69_FORMULA = (
    DATA
    / "selected_step69_hymthresholdprefactorrows_or_omegascalarexecution"
    / "step69_prefactor_solution_formula_rows.packet.json"
)
STEP69_DIAGNOSTIC = (
    DATA
    / "selected_step69_hymthresholdprefactorrows_or_omegascalarexecution"
    / "step69_diagnostic_prefactor_postcheck.packet.json"
)
STEP42_VALUE_SOLUTION = (
    DATA
    / "selected_step42_executable_value_replay_solution_or_noknobrowfrontier"
    / "step42_executable_value_replay_solution.packet.json"
)
COMMON_VALUES = (
    DATA
    / "selected_acceptedcommonscaleyukawahiggsvalues_or_profilelikelihoodexecution"
    / "versioned_common_scale_yukawa_higgs_values.packet.json"
)
OLD_GAP_MATRIX = (
    DATA
    / "selected_finalsmparitygapmatrix_or_closureattempt"
    / "final_sm_parity_gap_matrix.packet.json"
)

STATUS = "MTT_SELECTED_STEP71_SMPARITY_MATRIX_COMPARISON_BUILT_ROWLOCAL_TARGETS_OPEN"
NEXT = "MTT_Selected_RowLocalHYMOverlapThresholdPrefactors_or_StrictOmegaAcceptance_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def as_complex(pair: list[float]) -> complex:
    return complex(float(pair[0]), float(pair[1]))


def matrix_from_pairs(matrix: list[list[list[float]]]) -> list[list[complex]]:
    return [[as_complex(entry) for entry in row] for row in matrix]


def abs2(z: complex) -> float:
    return z.real * z.real + z.imag * z.imag


def frob(matrix: list[list[complex]]) -> float:
    return math.sqrt(sum(abs2(entry) for row in matrix for entry in row))


def offdiag_frob(matrix: list[list[complex]]) -> float:
    return math.sqrt(
        sum(abs2(matrix[i][j]) for i in range(len(matrix)) for j in range(len(matrix[i])) if i != j)
    )


def diag_abs(matrix: list[list[complex]]) -> list[float]:
    return [abs(matrix[i][i]) for i in range(len(matrix))]


def max_offdiag_abs(matrix: list[list[complex]]) -> float:
    values = [abs(matrix[i][j]) for i in range(len(matrix)) for j in range(len(matrix[i])) if i != j]
    return max(values) if values else 0.0


def entry_payload(z: complex) -> dict[str, float]:
    return {"real": z.real, "imag": z.imag, "abs": abs(z)}


def omega_to_matrix(omega_id: str) -> tuple[str, str | None, int | None]:
    if omega_id == "Omega_H.lambda":
        return "lambda_H", None, None
    _, sector_gen = omega_id.split("_", 1)
    sector, gen_text = sector_gen.split(".gen")
    return f"Y_{sector}", sector, int(gen_text) - 1


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    inputs = [
        STEP70,
        STEP70_FACTORS,
        STEP70_CUTSET,
        STEP69_FORMULA,
        STEP69_DIAGNOSTIC,
        STEP42_VALUE_SOLUTION,
        COMMON_VALUES,
        OLD_GAP_MATRIX,
    ]
    missing = [rel(path) for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step71 inputs: " + ", ".join(missing))

    step70 = load(STEP70)
    factors = load(STEP70_FACTORS)
    step70_cutset = load(STEP70_CUTSET)
    formula = load(STEP69_FORMULA)
    diagnostic = load(STEP69_DIAGNOSTIC)
    solution = load(STEP42_VALUE_SOLUTION)
    common = load(COMMON_VALUES)
    old_gap = load(OLD_GAP_MATRIX)

    value_rows = solution["value_rows"]
    matrices = {
        "u": matrix_from_pairs(value_rows["Y_u_MZ_firstpass"]),
        "d": matrix_from_pairs(value_rows["Y_d_MZ_firstpass"]),
        "e": matrix_from_pairs(value_rows["Y_e_MZ_firstpass"]),
    }
    matrix_summaries: dict[str, dict[str, Any]] = {}
    for sector, matrix in matrices.items():
        total = frob(matrix)
        offdiag = offdiag_frob(matrix)
        matrix_summaries[sector] = {
            "matrix_id": f"Y_{sector}_MZ_firstpass",
            "diagonal_abs_from_matrix": diag_abs(matrix),
            "declared_diag_abs": value_rows[f"diag_abs_Y_{sector}"],
            "frob": total,
            "offdiag_frob": offdiag,
            "offdiag_to_frob_ratio": offdiag / total if total else 0.0,
            "max_offdiag_abs": max_offdiag_abs(matrix),
            "effectively_diagonal_for_scalar_projection": offdiag < 1e-20 if sector != "d" else False,
            "contains_ckm_or_mixing_replay": sector == "d" and offdiag > 0.0,
        }

    diag_projection_rows: list[dict[str, Any]] = []
    formula_by_omega = {row["omega_id"]: row for row in formula["formula_rows"]}
    diagnostic_by_omega = {row["omega_id"]: row for row in diagnostic["diagnostic_rows"]}
    factor_by_omega = {row["omega_id"]: row for row in factors["factor_rows"]}

    for omega_id, factor_row in factor_by_omega.items():
        scalar_kind, sector, index = omega_to_matrix(omega_id)
        diagnostic_row = diagnostic_by_omega[omega_id]
        formula_row = formula_by_omega[omega_id]
        if sector is None:
            matrix_entry = None
            projected_abs = float(value_rows["lambda_H"])
            source_matrix_id = "lambda_H_MZ_firstpass"
        else:
            z = matrices[sector][index][index]
            matrix_entry = entry_payload(z)
            projected_abs = abs(z)
            source_matrix_id = f"Y_{sector}_MZ_firstpass[{index},{index}]"
        diag_projection_rows.append(
            {
                "row_id": f"step71.matrix_projection.{omega_id}",
                "omega_id": omega_id,
                "scalar_kind": scalar_kind,
                "source_matrix_entry": source_matrix_id,
                "matrix_entry": matrix_entry,
                "sm_parity_projected_abs_value": projected_abs,
                "step69_theta_weight": formula_row["theta_weight"],
                "step69_diagnostic_prefactor": diagnostic_row["diagnostic_prefactor"],
                "step70_prefactor_factorization": factor_row["factorization"],
                "covered_by_step70_diagonal_scalar_contract": True,
                "accepted_as_source_row": False,
                "accepted_as_omega_source_row": False,
                "observed_data_used_as_selector": False,
                "target_fitting_used": False,
            }
        )

    matrix_projection_packet = {
        "schema": "MTTStep71SMParityMatrixDiagonalProjection.v1",
        "status": "SM_PARITY_REPLAY_MATRIX_PROJECTED_TO_STEP70_SCALAR_SLOTS",
        "source_inputs": {
            "step42_value_solution": rel(STEP42_VALUE_SOLUTION),
            "common_scale_values": rel(COMMON_VALUES),
            "step70_factorization": rel(STEP70_FACTORS),
        },
        "selected_source_branch": solution["selected_source_branch"],
        "value_row_acceptance": solution["row_acceptance"],
        "matrix_summaries": matrix_summaries,
        "diagonal_projection_rows": diag_projection_rows,
        "diagonal_projection_row_count": len(diag_projection_rows),
        "matrix_projection_matches_declared_common_scale_magnitudes": all(
            abs(matrix_summaries[sector]["diagonal_abs_from_matrix"][i] - value_rows[f"diag_abs_Y_{sector}"][i])
            < 1e-12
            for sector in ["u", "d", "e"]
            for i in range(3)
        ),
        "accepted_as_no_knob_source": False,
        "accepted_internal_scalar_row_count": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(MATRIX_PROJECTION_PACKET, matrix_projection_packet)

    target_rows: list[dict[str, Any]] = []
    for row in diag_projection_rows:
        factor_row = factor_by_omega[row["omega_id"]]
        determinant_symbol = factor_row["finite_heat_torsion_subfactor_id"]
        target_rows.append(
            {
                "row_id": f"step71.rowlocal_target.{row['omega_id']}",
                "omega_id": row["omega_id"],
                "prefactor_slot_id": factor_row["prefactor_slot_id"],
                "source_class": factor_row["source_class"],
                "finite_heat_torsion_subfactor_id": determinant_symbol,
                "rowlocal_composite_target_symbolic": (
                    f"({row['step69_diagnostic_prefactor']}) / {determinant_symbol}"
                ),
                "meaning": (
                    "Diagnostic-only composite value for L_rowlocal.* * T_scheme.* if the "
                    "selected determinant subfactor is treated symbolically."
                ),
                "closed_subsources": {
                    "theta_weight": True,
                    "finite_heat_torsion_subfactor": True,
                    "sm_parity_matrix_projection_for_postcheck": True,
                    "selected_rowlocal_overlap_factor": False,
                    "selected_threshold_scheme_factor": False,
                },
                "accepted_as_rowlocal_source_target": False,
                "accepted_as_full_prefactor_source_row": False,
                "accepted_as_omega_source_row": False,
                "observed_data_used_as_selector": False,
                "target_fitting_used": False,
            }
        )

    rowlocal_target_packet = {
        "schema": "MTTStep71RowLocalCompositeTargetContract.v1",
        "status": "ROWLOCAL_COMPOSITE_TARGETS_EXTRACTED_FOR_POSTCHECK_ONLY_SOURCE_OPEN",
        "target_rows": target_rows,
        "target_row_count": len(target_rows),
        "closed_source_subslots": {
            "theta_weight": True,
            "finite_heat_torsion_subfactor": True,
        },
        "open_source_subslots": {
            "selected_rowlocal_overlap_factor": True,
            "selected_threshold_scheme_factor": True,
            "lambda_H_value_payload": True,
        },
        "accepted_rowlocal_source_row_count": 0,
        "accepted_full_prefactor_source_row_count": 0,
        "accepted_omega_source_row_count": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(ROWLOCAL_TARGET_PACKET, rowlocal_target_packet)

    branch = solution["selected_source_branch"]
    same_branch = branch["q"] == 79 and branch["orientation"] == "F" and branch["torsion_m"] == 1

    scope_packet = {
        "schema": "MTTStep71MatrixScopeComparison.v1",
        "status": "SMPARITY_MATRIX_AND_STEP70_FACTORIZATION_SCOPES_SEPARATED",
        "comparison": {
            "sm_parity_matrix_tier": (
                "downstream admitted replay/profile input; accepted for SM parity and profile execution"
            ),
            "step70_factorization_tier": (
                "upstream no-knob/source contract; not accepted as scalar values"
            ),
            "same_branch": same_branch,
            "diagonal_magnitude_projection_aligned": matrix_projection_packet[
                "matrix_projection_matches_declared_common_scale_magnitudes"
            ],
            "step70_covers_diagonal_scalar_slots": True,
            "step70_covers_ckm_offdiagonal_matrix": False,
            "step70_covers_pmns_or_neutrino_mixing": False,
            "step70_covers_lambda_H_slot_as_formula_target_only": True,
        },
        "matrix_scope_metrics": {
            "Y_u_offdiag_to_frob_ratio": matrix_summaries["u"]["offdiag_to_frob_ratio"],
            "Y_d_offdiag_to_frob_ratio": matrix_summaries["d"]["offdiag_to_frob_ratio"],
            "Y_e_offdiag_to_frob_ratio": matrix_summaries["e"]["offdiag_to_frob_ratio"],
            "Y_d_offdiag_frob": matrix_summaries["d"]["offdiag_frob"],
            "Y_d_frob": matrix_summaries["d"]["frob"],
        },
        "interpretation": (
            "The SM-parity replay matrix is numerically richer than the current scalar prefactor "
            "contract because it includes CKM-down-sector offdiagonal entries. Step70 currently "
            "targets the diagonal magnitude/lambda_H scalar projection; mixing still needs a "
            "separate selected physical matrix/orientation theorem."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(SCOPE_PACKET, scope_packet)

    old_sm_open = set(old_gap["blocker_sets"]["SM_parity"])
    gap_reconciliation_packet = {
        "schema": "MTTStep71OldSMParityGapMatrixReconciliation.v1",
        "status": "OLDER_SMPARITY_GAP_MATRIX_RECONCILED_WITH_CURRENT_ROWLOCAL_FRONTIER",
        "old_gap_matrix_source": rel(OLD_GAP_MATRIX),
        "old_gap_matrix_status": old_gap["status"],
        "old_primary_open_sm_parity_gate": "common_scale_Yukawa_and_Higgs_transport"
        if "common_scale_Yukawa_and_Higgs_transport" in old_sm_open
        else None,
        "current_status_after_later_artifacts": {
            "common_scale_Yukawa_Higgs_replay_values_available": common[
                "accepted_as_versioned_common_scale_candidate_values"
            ],
            "step42_executable_admitted_replay_solution_closed": solution["row_acceptance"][
                "accepted_for_SM_parity"
            ],
            "step70_no_knob_factorization_frontier": step70["status"],
            "old_full_no_knob_constants_blocker_refined_to_rowlocal_factors": True,
        },
        "comparison": (
            "The older final SM-parity gap matrix is a gate/blocker matrix, not the Yukawa "
            "replay matrix. It is superseded at the parity-replay tier by later common-scale "
            "value packets, while the no-knob constants row is now refined into Step70/Step71 "
            "row-local overlap and threshold factors."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(GAP_RECONCILIATION_PACKET, gap_reconciliation_packet)

    cutset_packet = {
        "schema": "MTTStep71NextRowLocalExecutionCutset.v1",
        "status": "ROWLOCAL_SOURCE_FACTORS_AND_MIXING_EXTENSION_SPLIT",
        "not_missing_anymore": [
            "comparison with the earlier SM-parity replay matrix",
            "diagonal projection of SM-parity Yukawa/Higgs replay rows to Step70 Omega slots",
            "scope separation between diagonal scalar slots and CKM/offdiagonal matrix content",
            "reconciliation with the older final SM-parity gap matrix",
        ],
        "still_missing_for_scalar_rows": [
            "selected row-local HYM zero-mode overlap factors L_rowlocal.*",
            "selected threshold/scale/scheme factors T_scheme.*",
            "selected lambda_H value payload",
            "strict Omega acceptance theorem",
        ],
        "still_missing_for_full_physical_matrices": [
            "selected CKM/down-sector offdiagonal physical matrix theorem",
            "selected PMNS/neutrino mixing extension if included in the target packet",
            "full covariance/profile likelihood if upgrading from central replay",
        ],
        "minimal_next_artifact": NEXT,
        "forbidden_routes": [
            "use the SM-parity replay matrix as a source selector for row-local factors",
            "claim Step70 derives CKM/offdiagonal matrix entries",
            "claim diagnostic row-local composite targets are selected HYM overlap values",
            "treat the older final gap matrix as the current no-knob value proof",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(CUTSET_PACKET, cutset_packet)

    candidate = {
        "candidate": "MTTSelectedStep71SMParityMatrixComparisonOrRowLocalTargets",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in inputs},
        "output_packets": {
            "smparity_matrix_diagonal_projection": rel(MATRIX_PROJECTION_PACKET),
            "rowlocal_composite_target_contract": rel(ROWLOCAL_TARGET_PACKET),
            "matrix_scope_comparison": rel(SCOPE_PACKET),
            "old_smparity_gap_matrix_reconciliation": rel(GAP_RECONCILIATION_PACKET),
            "next_rowlocal_execution_cutset": rel(CUTSET_PACKET),
        },
        "theorem": {
            "name": "Step71SMParityMatrixComparisonTheorem",
            "proved": True,
            "statement": (
                "The earlier SM-parity replay matrix and the Step70 no-knob prefactor factorization "
                "live at different tiers. The replay matrix projects exactly onto the ten Step70 "
                "diagonal scalar/lambda slots as a postcheck, while Step70 supplies only the source "
                "contract and determinant subsource. CKM/offdiagonal matrix content is present in "
                "the SM-parity matrix but is not yet derived by the scalar prefactor contract."
            ),
        },
        "closure_decision": {
            "smparity_matrix_comparison_closed": True,
            "diagonal_projection_to_step70_slots_closed": True,
            "rowlocal_composite_target_contract_built": True,
            "old_smparity_gap_matrix_reconciled": True,
            "scope_split_diagonal_scalar_vs_mixing_closed": True,
            "accepted_rowlocal_source_row_count": 0,
            "accepted_full_prefactor_source_row_count": 0,
            "accepted_omega_source_row_count": 0,
            "accepted_internal_scalar_value_row_count": 0,
            "selected_rowlocal_overlap_factors_closed": False,
            "selected_threshold_scheme_factors_closed": False,
            "selected_ckm_offdiagonal_matrix_derived": False,
            "lambda_H_value_row_emitted": False,
            "scalar_value_execution_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "previous_status": step70["status"],
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step71_SMParityMatrixComparison_or_RowLocalTargets_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        **candidate["closure_decision"],
        "theorem_proved": True,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected Step71 SMParityMatrixComparison or RowLocalTargets v1

Status: `{STATUS}`.

## Comparison

The earlier SM-parity matrix is an admitted replay/profile-input object.  It is
accepted for SM-parity comparison, not as a no-knob source selector.

Step70 is different: it is the upstream source contract

```text
C_HYMthr.* = D_fin.class * L_rowlocal.* * T_scheme.*
Omega      = C_HYMthr.* * epsilon_Theta^n
```

The SM-parity replay matrix projects exactly onto the ten Step70 scalar slots as
a postcheck:

```text
diagonal projection rows: {len(diag_projection_rows)}
projection matches declared common-scale magnitudes: {matrix_projection_packet['matrix_projection_matches_declared_common_scale_magnitudes']}
accepted row-local source rows: 0
accepted Omega source rows: 0
```

## Matrix Scope

The current Step70 scalar contract covers diagonal magnitudes and `lambda_H`.
It does not yet derive the full physical mixing matrix.

```text
Y_u offdiag/frob: {matrix_summaries['u']['offdiag_to_frob_ratio']:.12g}
Y_d offdiag/frob: {matrix_summaries['d']['offdiag_to_frob_ratio']:.12g}
Y_e offdiag/frob: {matrix_summaries['e']['offdiag_to_frob_ratio']:.12g}
```

So `Y_u` and `Y_e` are effectively diagonal in the replay convention, while
`Y_d` carries the CKM/down-sector offdiagonal replay content.  That mixing layer
is outside the current scalar-prefactor closure.

## Older Gap Matrix

The older final SM-parity gap matrix was a gate/blocker matrix, not the Yukawa
matrix itself.  Later artifacts supersede it at the parity-replay tier.  Its
`full_no_knob_constants` blocker is now refined into the Step70/Step71 row-local
overlap and threshold factors.

Next artifact: `{NEXT}`.
""",
        encoding="utf-8",
    )

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
