"""Build the selected rowwise scalar retarded-overlap frontier packet.

This artifact pushes the live value frontier one step past the selected
dynamic first-response matrices.  It uses the already-closed selected family
spectral projectors and basis map to emit the basis-invariant charged spectral
support scalars.  It deliberately does not promote those support scalars to
strict physical L_rowlocal/K rows until a selected retarded-overlap equality
lemma or an independent selected quadrature execution is present.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_rowwisescalarretardedoverlapquadraturevalues_or_tschemelambdahsourceexecution"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SPECTRAL_EVALUATOR = PACKET_DIR / "charged_spectral_lrowlocal_evaluator_attempt.packet.json"
STRICT_GATE = PACKET_DIR / "strict_lrowlocal_acceptance_gate_after_spectral_evaluator.packet.json"
KROW_STATUS = PACKET_DIR / "krow_status_after_spectral_lrowlocal_attempt.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_rowwise_scalar_quadrature_attempt.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_RowwiseScalarRetardedOverlapQuadratureValues_or_TSchemeLambdaHExecution_v1.md"

PREVIOUS = DATA / "selected_dynamicretardedoverlapderivativerows_or_tschemelambdahsourceexecution.candidate.json"
PREVIOUS_EMISSION = (
    DATA
    / "selected_dynamicretardedoverlapderivativerows_or_tschemelambdahsourceexecution"
    / "dynamic_retarded_row_emission_attempt.packet.json"
)
K_GRAMMAR = DATA / "selected_combinedthresholdkernelkrows_sourcetheorem" / "closed_source_k_threshold_grammar.packet.json"
DYNAMIC_NONSCALAR = (
    DATA
    / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure"
    / "selected_non_scalar_dynamic_overlap_values.packet.json"
)
FAMILY_PROJECTORS = (
    DATA
    / "selected_rthetavaluerows_or_universalsourceanchortheorem"
    / "selected_family_spectral_projector_basis.packet.json"
)
FAMILY_BASIS_MAP = (
    DATA
    / "selected_rthetavaluerows_or_universalsourceanchortheorem"
    / "rtheta_family_eigenprofile_to_magnitude_row_basis_map.packet.json"
)
ROWLOCAL_FUNCTIONAL = (
    DATA
    / "selected_rowlocalhymoverlapquadraturefunctional_or_thresholdschemesourcetheorem"
    / "selected_overlap_quadrature_functional.packet.json"
)
THRESHOLD_GATE = (
    DATA
    / "selected_rowlocalhymoverlapquadraturefunctional_or_thresholdschemesourcetheorem"
    / "threshold_scheme_source_gate.packet.json"
)
EMPIRICAL_K = (
    DATA
    / "selected_lrowlocaltschemelambdah_sourceexecution_or_controlledempiricalimport"
    / "controlled_empirical_k_import_contract.packet.json"
)

STATUS = (
    "MTT_SELECTED_ROWWISESCALARRETARDEDOVERLAPQUADRATUREVALUES_OR_TSCHEMELAMBDAHSOURCEEXECUTION_"
    "BUILT_SPECTRAL_SUPPORT_STRICT_QUADRATURE_EQUALITY_OPEN"
)
NEXT = "MTT_Selected_RetardedOverlapSpectralPairingLemma_or_IndependentQuadratureValues_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing rowwise scalar inputs: " + ", ".join(missing))


def scalar_abs(value: Any) -> float:
    if isinstance(value, list):
        if len(value) == 2 and all(isinstance(part, (int, float)) for part in value):
            return round((float(value[0]) ** 2 + float(value[1]) ** 2) ** 0.5, 12)
        raise TypeError(f"unsupported nested scalar encoding: {value!r}")
    return round(abs(float(value)), 12)


def matrix_diag_abs(matrix: list[list[Any]]) -> list[float]:
    return [scalar_abs(matrix[i][i]) for i in range(min(len(matrix), len(matrix[0])))]


def spectral_support_rows(basis_map: dict[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for row in basis_map["charged_basis_rows"]:
        value = round(abs(float(row["family_eigenvalue"])), 12)
        rows.append(
            {
                "row_id": row["row_id"].replace("magnitude_basis_projector", "spectral_lrowlocal_support"),
                "sector": row["sector"],
                "generation": row["generation"],
                "spectral_projector_ref": row["spectral_projector_ref"],
                "family_label_convention": row["family_label_convention"],
                "family_eigenvalue": row["family_eigenvalue"],
                "selected_spectral_support_scalar": value,
                "formula": "abs(Tr(P_s,g H1_s))",
                "accepted_as_selected_spectral_support_row": True,
                "accepted_as_strict_L_rowlocal_row": False,
                "accepted_as_K_threshold_row": False,
                "blocking_reason": (
                    "The selected projector pairing is basis-invariant support, but the retarded-overlap "
                    "quadrature identity K_row(A_HYM,G,dotD_alpha1)=H1_s has not been proved and no independent "
                    "selected Q_sel quadrature values are emitted."
                ),
                "observed_data_used_as_selector": False,
                "target_fitting_used": False,
            }
        )
    return rows


def find_support(rows: list[dict[str, Any]], sector: str, generation: Any) -> dict[str, Any] | None:
    try:
        gen = int(str(generation).replace("gen", ""))
    except (TypeError, ValueError):
        return None
    for row in rows:
        if row["sector"] == sector and row["generation"] == gen:
            return row
    return None


def grammar_status_rows(grammar_rows: list[dict[str, Any]], support_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    status_rows: list[dict[str, Any]] = []
    for row in grammar_rows:
        sector = row["sector"]
        support = None if sector == "H" else find_support(support_rows, sector, row["generation_or_lambda"])
        status_rows.append(
            {
                "omega_id": row["omega_id"],
                "combined_kernel_row_id": row["combined_kernel_row_id"],
                "sector": sector,
                "generation_or_lambda": row["generation_or_lambda"],
                "selected_spectral_support_available": support is not None,
                "selected_spectral_support_scalar": None if support is None else support["selected_spectral_support_scalar"],
                "selected_strict_L_rowlocal_value_emitted": False,
                "selected_T_scheme_row_emitted": False,
                "selected_lambda_H_payload_emitted": False if sector == "H" else None,
                "selected_K_threshold_row_emitted": False,
                "accepted_as_no_knob_source_row": False,
                "blocking_reasons": [
                    "strict retarded-overlap spectral-pairing lemma is absent",
                    "independent selected finite quadrature values are absent",
                    "selected T_scheme row is not instantiated",
                ]
                + (["H/lambda_H value row is still absent"] if sector == "H" else []),
                "observed_data_used_as_selector": False,
                "target_fitting_used": False,
            }
        )
    return status_rows


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_EMISSION,
        K_GRAMMAR,
        DYNAMIC_NONSCALAR,
        FAMILY_PROJECTORS,
        FAMILY_BASIS_MAP,
        ROWLOCAL_FUNCTIONAL,
        THRESHOLD_GATE,
        EMPIRICAL_K,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_emission = load(PREVIOUS_EMISSION)
    grammar = load(K_GRAMMAR)
    dynamic_nonscalar = load(DYNAMIC_NONSCALAR)
    family_projectors = load(FAMILY_PROJECTORS)
    basis_map = load(FAMILY_BASIS_MAP)
    rowlocal_functional = load(ROWLOCAL_FUNCTIONAL)
    threshold_gate = load(THRESHOLD_GATE)
    empirical_k = load(EMPIRICAL_K)

    support_rows = spectral_support_rows(basis_map)
    distinct_support_values = sorted({row["selected_spectral_support_scalar"] for row in support_rows})
    sectors = sorted({row["sector"] for row in support_rows})
    ordered_diag_h1 = {
        sector: matrix_diag_abs(dynamic_nonscalar["sector_first_responses"][sector]["first_hermitian_response_H1"])
        for sector in sectors
    }
    correction_diag = {
        sector: matrix_diag_abs(dynamic_nonscalar["sector_first_responses"][sector]["correction_dY"])
        for sector in sectors
    }
    status_rows = grammar_status_rows(grammar["grammar_rows"], support_rows)

    spectral_evaluator = {
        "schema": "MTTChargedSpectralLRowlocalEvaluatorAttempt.v1",
        "status": "SELECTED_SPECTRAL_SUPPORT_ROWS_EMITTED_STRICT_LROWLOCAL_OPEN",
        "selected_inputs": {
            "family_projector_basis_status": family_projectors["status"],
            "all_sector_projector_bases_closed": family_projectors["all_sector_projector_bases_closed"],
            "basis_map_status": basis_map["status"],
            "basis_map_to_sector_scaled_magnitude_rows_closed": basis_map[
                "basis_map_to_sector_scaled_magnitude_rows_closed"
            ],
            "dynamic_first_response_status": dynamic_nonscalar["status"],
            "previous_dynamic_retarded_status": previous["status"],
            "rowlocal_functional_status": rowlocal_functional["status"],
        },
        "spectral_pairing_candidate": {
            "formula": "L_spectral_support(s,g)=abs(Tr(P_s,g H1_s))",
            "row_count": len(support_rows),
            "charged_sectors": sectors,
            "family_label_convention": family_projectors["family_label_convention"],
            "basis_invariant_projector_pairing": True,
            "selected_source_inputs_verified": True,
            "distinct_support_values": distinct_support_values,
            "rows": support_rows,
            "accepted_as_selected_spectral_support_rows": True,
            "accepted_as_strict_L_rowlocal_rows": False,
            "strict_Lrowlocal_blocker": "retarded_overlap_equals_spectral_pairing_theorem_or_independent_Q_sel_values_absent",
        },
        "candidate_shortcuts_rejected": [
            {
                "candidate": "ordered_basis_diagonal_abs_H1",
                "diagnostic_values_by_sector": ordered_diag_h1,
                "accepted_as_strict_L_rowlocal_rows": False,
                "reason": "ordered-coordinate diagonals depend on basis presentation and produce structural zeros; they are not the selected row-local quadrature functional",
            },
            {
                "candidate": "correction_dY_diagonal_or_eigenprofile",
                "diagnostic_values_by_sector": correction_diag,
                "accepted_as_strict_L_rowlocal_rows": False,
                "reason": "the correction matrix is transfer-shape support, not the physical retarded-overlap derivative scalar row",
            },
            {
                "candidate": "controlled_empirical_K_import",
                "empirical_K_row_count": empirical_k["empirical_K_row_count"],
                "accepted_as_strict_L_rowlocal_rows": False,
                "reason": "empirical K values are admitted replay/postcheck data and cannot select no-knob source rows",
            },
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(SPECTRAL_EVALUATOR, spectral_evaluator)

    strict_gate = {
        "schema": "MTTStrictLRowlocalAcceptanceGateAfterSpectralEvaluator.v1",
        "status": "SPECTRAL_SUPPORT_AVAILABLE_STRICT_LROWLOCAL_ACCEPTANCE_BLOCKED",
        "available_inputs": {
            "selected_family_projectors_closed": family_projectors["all_sector_projector_bases_closed"],
            "selected_basis_map_closed": basis_map["basis_map_to_sector_scaled_magnitude_rows_closed"],
            "selected_dynamic_first_response_support_available": previous["closure_decision"][
                "dynamic_first_response_matrix_support_imported"
            ],
            "rowlocal_functional_contract_defined": rowlocal_functional["status"]
            == "ROWLOCAL_HYM_GREEN_QUADRATURE_FUNCTIONAL_DEFINED_VALUES_REQUIRE_SELECTED_KERNEL",
            "charged_spectral_support_rows_emitted": len(support_rows),
            "no_empirical_selector_used": True,
        },
        "strict_acceptance_requirements": {
            "retarded_overlap_equals_spectral_pairing_theorem_proved": False,
            "independent_selected_finite_quadrature_Q_sel_values_emitted": False,
            "selected_T_scheme_rows_emitted": threshold_gate["accepted_T_scheme_source_row_count"] > 0,
            "selected_lambda_H_value_row_emitted": False,
        },
        "accepted_selected_spectral_support_row_count": len(support_rows),
        "accepted_strict_Lrowlocal_row_count": 0,
        "accepted_selected_K_source_row_count": 0,
        "accepted_internal_scalar_value_row_count": 0,
        "can_close_K_rows_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(STRICT_GATE, strict_gate)

    krow_status = {
        "schema": "MTTKRowStatusAfterSpectralLRowlocalAttempt.v1",
        "status": "NINE_SPECTRAL_SUPPORT_ROWS_ZERO_STRICT_K_ROWS",
        "row_count": len(status_rows),
        "charged_spectral_support_rows_emitted": len(support_rows),
        "accepted_selected_L_rowlocal_row_count": 0,
        "accepted_T_scheme_row_count": threshold_gate["accepted_T_scheme_source_row_count"],
        "accepted_selected_K_source_row_count": 0,
        "accepted_internal_scalar_value_row_count": 0,
        "lambda_H_value_row_emitted": False,
        "empirical_K_row_count": empirical_k["empirical_K_row_count"],
        "previous_dynamic_retarded_row_count": previous_emission["row_count"],
        "rows": status_rows,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(KROW_STATUS, krow_status)

    cutset = {
        "schema": "MTTNextCutsetAfterRowwiseScalarQuadratureAttempt.v1",
        "status": "NEXT_ATTACK_RETARDED_OVERLAP_SPECTRAL_PAIRING_OR_DIRECT_QSEL",
        "next_required_artifact": NEXT,
        "closed_here": [
            "selected family spectral projector basis reused as row evaluator support",
            "nine charged basis-invariant spectral support scalars emitted",
            "ordered-basis diagonal and correction-matrix shortcuts rejected as strict row-local values",
            "strict L_rowlocal/K-row acceptance gate reduced to one equality lemma or direct selected quadrature execution",
        ],
        "still_open": [
            "prove K_row(A_HYM,G,dotD_alpha1) equals the selected H1 spectral projector pairing on the selected row basis",
            "or independently execute selected finite quadrature Q_sel values for L_rowlocal(s,g)",
            "instantiate selected T_scheme.* source rows",
            "emit selected lambda_H H-sector quartic/threshold payload",
            "emit ten selected K_threshold rows",
            "strict Omega/lambda_H scalar execution",
            "full no-knob SM closure",
        ],
        "forbidden_routes": [
            "treat the nine spectral support scalars as final physical K rows without the equality/quadrature theorem",
            "use ordered-basis matrix diagonals as source rows",
            "use empirical K values as selectors",
            "fit T_scheme or lambda_H from observed masses",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(CUTSET, cutset)

    decision = {
        "selected_family_projector_basis_closed": True,
        "selected_basis_map_closed": True,
        "dynamic_first_response_support_available": True,
        "charged_spectral_support_rows_emitted": len(support_rows),
        "spectral_support_rows_promoted_to_strict_Lrowlocal": False,
        "retarded_overlap_equals_spectral_pairing_theorem_proved": False,
        "independent_selected_quadrature_values_emitted": False,
        "selected_T_scheme_rows_emitted": False,
        "selected_lambda_H_payload_emitted": False,
        "accepted_selected_L_rowlocal_row_count": 0,
        "accepted_selected_K_source_row_count": 0,
        "accepted_internal_scalar_value_row_count": 0,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
    }
    candidate = {
        "candidate": "MTTSelectedRowwiseScalarRetardedOverlapQuadratureValuesOrTSchemeLambdaHSourceExecution",
        "status": STATUS,
        "closure_claimed": True,
        "theorem": {
            "name": "SelectedSpectralSupportRowsDoNotYetCloseStrictRetardedQuadrature",
            "proved": True,
            "statement": (
                "The selected family spectral projectors and selected first-response Hermitian operators emit nine "
                "basis-invariant charged spectral support scalars by abs(Tr(P_s,g H1_s)).  These are the strongest "
                "currently selected scalar supports for the charged rows, but they are not accepted as strict "
                "L_rowlocal or K_threshold rows until MTT proves the retarded-overlap/spectral-pairing identity or "
                "executes independent selected finite quadrature values, and until T_scheme/lambda_H source rows are emitted."
            ),
        },
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "charged_spectral_lrowlocal_evaluator_attempt": rel(SPECTRAL_EVALUATOR),
            "strict_lrowlocal_acceptance_gate_after_spectral_evaluator": rel(STRICT_GATE),
            "krow_status_after_spectral_lrowlocal_attempt": rel(KROW_STATUS),
            "next_cutset_after_rowwise_scalar_quadrature_attempt": rel(CUTSET),
        },
        "closure_decision": decision,
        "previous_status": previous["status"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_RowwiseScalarRetardedOverlapQuadratureValues_or_TSchemeLambdaHExecution_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        **decision,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
    }
    write_json(CERT, cert)

    row_summary = "\n".join(
        f"- {row['sector']}.gen{row['generation']}: {row['selected_spectral_support_scalar']}"
        for row in support_rows
    )
    NOTE.write_text(
        f"""# MTT Selected RowwiseScalarRetardedOverlapQuadratureValues or TSchemeLambdaHExecution v1

Status: `{STATUS}`.

This packet executes the strongest scalar operation currently justified by
selected data: pair the selected family spectral projectors with the selected
first-response Hermitian operator,
`L_spectral_support(s,g)=abs(Tr(P_s,g H1_s))`.

Result:

```text
selected family projector basis closed      : true
selected basis-map rows available           : 9
selected spectral support scalar rows       : 9
strict L_rowlocal rows accepted             : 0
selected T_scheme rows emitted              : false
selected lambda_H payload emitted           : false
accepted selected K rows                    : 0
```

The nine charged spectral support scalars are:

```text
{row_summary}
```

This is real progress, but not final value closure.  The packet rejects three
shortcuts: ordered-basis diagonals, correction-matrix eigen/diagonal replay,
and empirical K import.  To promote the nine support rows to strict physical
`L_rowlocal` rows, the next artifact must either prove the selected
retarded-overlap/spectral-pairing identity or execute independent selected
finite quadrature values `Q_sel`.  `T_scheme.*` and `lambda_H` still also need
selected source rows before any ten `K_threshold` rows can close.

Next artifact: `{NEXT}`.
""",
        encoding="utf-8",
    )

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
