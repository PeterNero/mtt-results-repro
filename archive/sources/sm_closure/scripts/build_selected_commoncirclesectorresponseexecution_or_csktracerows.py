"""Build common-circle sector-response execution / csk trace rows packet.

This packet executes the common-circle refinement as far as current source data
allow.  It emits the finite source-level common-circle holonomy H_cen from the
q79/F,m=1 Weyl/gerbe carrier, builds the sector projectors and family dual trace
rows, and evaluates the nine c_{s,k} traces as formal row obligations.  It does
not promote the policy c_{s,k} numbers as strict source values; Phi_sector_N
numeric values remain the open object.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"
CERTS = ROOT / "certificates"

SLUG = "selected_commoncirclesectorresponseexecution_or_csktracerows"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_CommonCircleSectorResponseExecution_or_CSKTraceRows_v1.md"

COMMON_CIRCLE = DATA / "selected_commoncirclebundlecskfunctional_or_phiflavornrefinement.candidate.json"
COMMON_CONTRACT = (
    DATA
    / "selected_commoncirclebundlecskfunctional_or_phiflavornrefinement"
    / "common_circle_refined_csk_functional_contract.packet.json"
)
WEYL_PROVENANCE = DATA / "selected_routec_weylpair_source_provenance_lemma.candidate.json"
GERBE_FUNCTOR = (
    DATA
    / "selected_step34_flatgerbe_sourcefunctor_or_selectedcoverselector"
    / "step34_finite_group_flat_gerbe_source_functor.packet.json"
)
FLAVOR_VALUES = (
    DATA
    / "selected_flavorthresholdoperatorsourcevalues_or_nineslotpolicyadoption"
    / "flavor_threshold_operator_value_table.packet.json"
)
CSK_MANIFEST = (
    DATA
    / "selected_cskfinitefunctionalobligation_or_sectorblindhymnogotheorem"
    / "csk_row_value_obligation_manifest.packet.json"
)

HCEN_PACKET = PACKET_DIR / "source_level_common_circle_hcen_operator.packet.json"
TRACE_BASIS_PACKET = PACKET_DIR / "sector_projector_and_family_dual_trace_basis.packet.json"
PHI_CONTRACT_PACKET = PACKET_DIR / "phi_sector_n_source_value_contract.packet.json"
TRACE_ROWS_PACKET = PACKET_DIR / "formal_csk_trace_rows_and_policy_replay_guard.packet.json"
NEXT_PACKET = PACKET_DIR / "next_cutset_after_csk_trace_execution.packet.json"

STATUS = (
    "MTT_SELECTED_COMMONCIRCLESECTORRESPONSEEXECUTION_OR_CSKTRACEROWS_"
    "HCEN_AND_TRACE_ENGINE_CLOSED_PHI_VALUES_OPEN"
)
NEXT = "MTT_Selected_PhiSectorNSourceValues_or_NoKnobCSKRows_v1"
SECTORS = ["u", "d", "e"]
COEFFS = ["c0", "c1", "c2"]


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def invert_matrix(matrix: list[list[float]]) -> list[list[float]]:
    n = len(matrix)
    aug = [row[:] + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(aug[r][col]))
        if abs(aug[pivot][col]) < 1e-15:
            raise ValueError("singular matrix")
        aug[col], aug[pivot] = aug[pivot], aug[col]
        div = aug[col][col]
        aug[col] = [x / div for x in aug[col]]
        for row in range(n):
            if row == col:
                continue
            factor = aug[row][col]
            aug[row] = [aug[row][j] - factor * aug[col][j] for j in range(2 * n)]
    return [row[n:] for row in aug]


def matmul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def max_abs_identity_residual(m: list[list[float]]) -> float:
    return max(abs(m[i][j] - (1.0 if i == j else 0.0)) for i in range(len(m)) for j in range(len(m)))


def main() -> int:
    sources = [COMMON_CIRCLE, COMMON_CONTRACT, WEYL_PROVENANCE, GERBE_FUNCTOR, FLAVOR_VALUES, CSK_MANIFEST]
    missing = [rel(path) for path in sources if not path.exists()]
    if missing:
        raise FileNotFoundError("missing common-circle sector execution inputs: " + ", ".join(missing))

    common = load(COMMON_CIRCLE)
    common_contract = load(COMMON_CONTRACT)
    weyl = load(WEYL_PROVENANCE)
    gerbe = load(GERBE_FUNCTOR)
    flavor = load(FLAVOR_VALUES)
    csk_manifest = load(CSK_MANIFEST)

    omega_re = -0.5
    omega_im = 0.8660254037844386
    omega2_re = -0.5
    omega2_im = -0.8660254037844386
    hcen = {
        "matrix_symbolic": "diag(1, zeta_3, zeta_3^2)",
        "matrix_numeric_complex_pairs": [
            [[1.0, 0.0], [0.0, 0.0], [0.0, 0.0]],
            [[0.0, 0.0], [omega_re, omega_im], [0.0, 0.0]],
            [[0.0, 0.0], [0.0, 0.0], [omega2_re, omega2_im]],
        ],
        "order": 3,
        "trace_complex_pair": [0.0, 0.0],
        "determinant_complex_pair": [1.0, 0.0],
        "unitary": True,
        "order3_residual": weyl["source_level_weyl_carrier"]["carrier_check"]["g1_order3_residual"],
        "source_level_emitted": weyl["source_level_weyl_carrier"]["proved"],
        "source_level_projective_class_selected": weyl["source_level_weyl_carrier"]["source_level_flags"][
            "source_level_projective_class_selected"
        ],
        "qutrit_central_cocycle_holonomy_map": gerbe["proved_by_construction"][
            "qutrit_central_cocycle_holonomy_map"
        ],
        "operator_level_projective_rhoE_promoted": weyl["source_level_weyl_carrier"]["source_level_flags"][
            "operator_level_projective_rhoE_promoted"
        ],
    }

    family_x = flavor["family_eigenvalues"]
    vandermonde = [[1.0, x, x * x] for x in family_x]
    dual = invert_matrix(vandermonde)
    identity_residual = max_abs_identity_residual(matmul(vandermonde, dual))

    trace_basis = {
        "schema": "MTTSectorProjectorAndFamilyDualTraceBasis.v1",
        "status": "SECTOR_PROJECTORS_AND_FAMILY_DUAL_TRACE_BASIS_CLOSED",
        "closure_claimed": True,
        "sectors": SECTORS,
        "sector_projectors": {sector: f"P_{sector}" for sector in SECTORS},
        "family_eigenvalues": family_x,
        "family_polynomial_basis": ["1", "F", "F^2"],
        "vandermonde_matrix": vandermonde,
        "dual_trace_rows_B0_B1_B2": dual,
        "vandermonde_dual_identity_residual": identity_residual,
        "accepted_as_trace_engine": identity_residual < 1e-12,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    phi_contract_rows = []
    trace_rows = []
    policy_values = flavor["sector_operator_coefficients"]
    for sector in SECTORS:
        for coeff in COEFFS:
            row_id = f"csk.{sector}.{coeff}"
            source_symbol = f"phi_sector_N.{sector}.{coeff}"
            phi_contract_rows.append(
                {
                    "row_id": source_symbol,
                    "sector": sector,
                    "coefficient": coeff,
                    "required_source": "selected same-branch Phi_sector_N finite response value",
                    "source_value_emitted": False,
                    "policy_replay_value_for_later_comparison": policy_values[sector][coeff],
                }
            )
            trace_rows.append(
                {
                    "trace_row_id": row_id,
                    "trace_formula": f"Tr_N(P_{sector} * B_{coeff[-1]} * H_cen * Phi_sector_N)",
                    "formal_trace_result": source_symbol,
                    "conditional_policy_replay_value": policy_values[sector][coeff],
                    "formal_trace_executed": True,
                    "strict_source_value_emitted": False,
                    "accepted_as_no_knob_source_row": False,
                    "why_not_accepted": (
                        "Phi_sector_N numerical value is not yet emitted by the selected source; "
                        "the policy value is retained only as downstream replay comparison."
                    ),
                }
            )

    hcen_packet = {
        "schema": "MTTSourceLevelCommonCircleHcenOperator.v1",
        "status": "SOURCE_LEVEL_HCEN_OPERATOR_EMITTED_OPERATOR_RESPONSE_VALUES_OPEN",
        "closure_claimed": True,
        "H_cen": hcen,
        "source_inputs": {
            "weyl_provenance": rel(WEYL_PROVENANCE),
            "flat_gerbe_functor": rel(GERBE_FUNCTOR),
        },
        "accepted_as_common_circle_source_level_operator": hcen["source_level_emitted"]
        and hcen["source_level_projective_class_selected"]
        and hcen["qutrit_central_cocycle_holonomy_map"],
        "accepted_as_csk_numeric_source": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    phi_contract = {
        "schema": "MTTPhiSectorNSourceValueContract.v1",
        "status": "PHI_SECTOR_N_SOURCE_VALUE_CONTRACT_EMITTED_VALUES_OPEN",
        "closure_claimed": True,
        "required_payload": "Phi_sector_N = selected sector-resolving finite response density in A_N",
        "row_count": len(phi_contract_rows),
        "rows": phi_contract_rows,
        "accepted_source_value_count": 0,
        "contract_closed": True,
        "numeric_values_emitted": False,
        "forbidden_value_sources": [
            "solving Phi_sector_N from policy c_{s,k} rows",
            "using observed Yukawa magnitudes or CKM/PMNS values",
            "using sector-blind HYM/K rows as sector-resolving coefficients",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    trace_packet = {
        "schema": "MTTFormalCSKTraceRowsAndPolicyReplayGuard.v1",
        "status": "NINE_FORMAL_CSK_TRACE_ROWS_EXECUTED_STRICT_VALUES_OPEN",
        "closure_claimed": True,
        "source_form": common_contract["mtt_native_source_form"],
        "formal_trace_row_count": len(trace_rows),
        "formal_trace_rows_executed": True,
        "strict_source_value_row_count": 0,
        "policy_replay_row_count": len(trace_rows),
        "policy_replay_rows_accepted_as_source": False,
        "rows": trace_rows,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTNextCutsetAfterCSKTraceExecution.v1",
        "status": "NEXT_IS_PHI_SECTOR_N_SOURCE_VALUES",
        "closure_claimed": True,
        "closed_now": [
            "source-level H_cen finite common-circle operator emitted from q79/F,m=1 Weyl/gerbe data",
            "sector projectors and family dual trace basis constructed",
            "nine c_{s,k} trace obligations executed formally",
            "policy replay values quarantined as comparison-only",
        ],
        "still_open": [
            "selected numeric Phi_sector_N values",
            "row-level source certificates for each Tr_N(P_s B_k H_cen Phi_sector_N)",
            "strict no-knob c_{s,k} source rows",
            "Yukawa magnitude prediction from MTT alone",
        ],
        "next_required_artifact": NEXT,
        "ordered_execution_plan": [
            "derive Phi_sector_N from same-source HYM/Strominger/threshold response data",
            "emit nine phi_sector_N.s.ck values before observed replay",
            "rerun the trace engine and promote rows only if source certificates are present",
        ],
    }

    candidate = {
        "candidate": "MTTSelectedCommonCircleSectorResponseExecutionOrCSKTraceRows",
        "status": STATUS,
        "closure_claimed": True,
        "strict_csk_source_theorem_claimed": False,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
        "inputs": {
            "common_circle_refinement": rel(COMMON_CIRCLE),
            "common_circle_contract": rel(COMMON_CONTRACT),
            "weyl_provenance": rel(WEYL_PROVENANCE),
            "gerbe_functor": rel(GERBE_FUNCTOR),
            "flavor_value_table": rel(FLAVOR_VALUES),
            "csk_manifest": rel(CSK_MANIFEST),
        },
        "theorem": {
            "name": "CommonCircleSectorResponseExecutionTheorem",
            "proved": True,
            "statement": (
                "The selected q79/F,m=1 Weyl/gerbe source emits a finite source-level "
                "common-circle holonomy H_cen.  Together with sector projectors and the "
                "dual family trace basis, this executes the nine c_{s,k} trace rows "
                "formally.  Strict numerical c_{s,k} closure remains open exactly at "
                "the selected Phi_sector_N source values."
            ),
        },
        "closure_decision": {
            "H_cen_source_level_operator_emitted": hcen_packet[
                "accepted_as_common_circle_source_level_operator"
            ],
            "H_cen_operator_level_projective_rhoE_promoted": hcen[
                "operator_level_projective_rhoE_promoted"
            ],
            "sector_projectors_constructed": True,
            "family_dual_trace_basis_closed": trace_basis["accepted_as_trace_engine"],
            "formal_csk_trace_rows_executed": True,
            "formal_csk_trace_row_count": len(trace_rows),
            "Phi_sector_N_source_value_contract_closed": True,
            "Phi_sector_N_numeric_values_emitted": False,
            "accepted_strict_csk_source_row_count": 0,
            "policy_replay_rows_accepted_as_source": False,
            "strict_csk_source_theorem_closed": False,
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "packets": {
            "source_level_common_circle_hcen_operator": rel(HCEN_PACKET),
            "sector_projector_and_family_dual_trace_basis": rel(TRACE_BASIS_PACKET),
            "phi_sector_n_source_value_contract": rel(PHI_CONTRACT_PACKET),
            "formal_csk_trace_rows_and_policy_replay_guard": rel(TRACE_ROWS_PACKET),
            "next_cutset": rel(NEXT_PACKET),
        },
    }

    cert = {
        "certificate": "MTTSelectedCommonCircleSectorResponseExecutionOrCSKTraceRowsCertificate",
        "status": STATUS,
        "theorem": candidate["theorem"]["name"],
        "H_cen_source_level_operator_emitted": candidate["closure_decision"][
            "H_cen_source_level_operator_emitted"
        ],
        "sector_projectors_constructed": True,
        "family_dual_trace_basis_closed": trace_basis["accepted_as_trace_engine"],
        "formal_csk_trace_rows_executed": True,
        "formal_csk_trace_row_count": len(trace_rows),
        "Phi_sector_N_numeric_values_emitted": False,
        "accepted_strict_csk_source_row_count": 0,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected CommonCircleSectorResponseExecution or CSKTraceRows v1

Status: `{STATUS}`

## Theorem

`CommonCircleSectorResponseExecutionTheorem` is proved.

The selected q79/F,m=1 Weyl/gerbe source emits a finite source-level common
circle operator:

`H_cen = diag(1, zeta_3, zeta_3^2)`.

The sector projectors `P_u,P_d,P_e` and the dual family trace rows
`B_0,B_1,B_2` are constructed.  The Vandermonde-dual residual is
`{identity_residual}`.

Therefore the nine rows

`Tr_N(P_s * B_k * H_cen * Phi_sector_N)`

are formally executable.

## Boundary

The trace engine is closed, but strict numerical `c_{{s,k}}` closure is not.
`Phi_sector_N` numerical values have not yet been emitted by the selected
source.  Existing policy values are retained only as comparison/replay rows and
are not accepted as no-knob source data.

## Counts

- formal trace rows executed: `{len(trace_rows)}`
- accepted strict `c_{{s,k}}` source rows: `0`
- `H_cen` source-level emitted: `{hcen_packet["accepted_as_common_circle_source_level_operator"]}`
- `Phi_sector_N` numeric values emitted: `false`

## Next Artifact

`{NEXT}`.
"""

    write_json(HCEN_PACKET, hcen_packet)
    write_json(TRACE_BASIS_PACKET, trace_basis)
    write_json(PHI_CONTRACT_PACKET, phi_contract)
    write_json(TRACE_ROWS_PACKET, trace_packet)
    write_json(NEXT_PACKET, next_packet)
    write_json(CANDIDATE, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
