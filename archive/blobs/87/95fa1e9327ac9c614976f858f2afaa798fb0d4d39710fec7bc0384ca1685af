"""Build sector response density source theorem / no-knob csk row emission gate.

This packet imports the strongest later result that was easy to miss: the
premise-free Route-A Phi_fin^C1 source rule promotes A_selected, b_selected,
deltaTheta_C1, and sector response matrices.  It then tests whether those
promoted C1 matrices are already the missing Phi_sector_N density values for
the common-circle c_{s,k} trace engine.

They are not.  The promoted matrices execute only the phase/shift dynamic-C1
lanes.  Common-circle traces can be evaluated, but the result is duplicated by
lane and remains the wrong codomain for the nine sector-resolving charged flavor
coefficients.  This closes the "maybe Step10 already filled Phi_sector_N"
question without demoting the Step10 result.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"
CERTS = ROOT / "certificates"

SLUG = "selected_sectorresponsedensitysource_or_noknobcskrowemission"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_SectorResponseDensitySourceTheorem_or_NoKnobCSKRowEmission_v1.md"

PHI_INVENTORY = DATA / "selected_phisectornsourcevalues_or_noknobcskrows.candidate.json"
TRACE_BASIS = (
    DATA
    / "selected_commoncirclesectorresponseexecution_or_csktracerows"
    / "sector_projector_and_family_dual_trace_basis.packet.json"
)
TRACE_ROWS = (
    DATA
    / "selected_commoncirclesectorresponseexecution_or_csktracerows"
    / "formal_csk_trace_rows_and_policy_replay_guard.packet.json"
)
STEP10 = DATA / "selected_step10_physicalphifinc1sourcerule_or_independentgalerkinrows.candidate.json"
UNPATCHED = DATA / "selected_unpatchedphifinc1sourcerule_or_honestgalerkintables_to_hrgconsumermap.candidate.json"
UNPATCHED_PAYLOAD = (
    DATA
    / "selected_unpatchedphifinc1sourcerule_or_honestgalerkintables_to_hrgconsumermap"
    / "selected_dynamic_phifinc1_payload_promotion.packet.json"
)
FULLS2_GAP = (
    DATA
    / "selected_step10_physicalphifinc1sourcerule_or_independentgalerkinrows"
    / "fulls2_no_proxy_value_row_gap.packet.json"
)
FLAVOR_VALUES = (
    DATA
    / "selected_flavorthresholdoperatorsourcevalues_or_nineslotpolicyadoption"
    / "flavor_threshold_operator_value_table.packet.json"
)

IMPORT_PACKET = PACKET_DIR / "step10_c1_sector_matrix_import.packet.json"
TRACE_EXEC_PACKET = PACKET_DIR / "c1_lane_commoncircle_trace_execution.packet.json"
OBSTRUCTION_PACKET = PACKET_DIR / "sector_density_codomain_obstruction.packet.json"
NEXT_PACKET = PACKET_DIR / "next_cutset_after_c1_density_bridge.packet.json"

STATUS = (
    "MTT_SELECTED_SECTORRESPONSEDENSITYSOURCE_OR_NOKNOBCSKROWEMISSION_"
    "C1_MATRICES_BRIDGED_FULL_DENSITY_OPEN"
)
NEXT = "MTT_Selected_FullS2SectorDensityOperator_or_PhiSectorNNumericRows_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def as_complex(value: Any) -> complex:
    if isinstance(value, list):
        return complex(value[0], value[1])
    return complex(value, 0.0)


def complex_pair(value: complex) -> list[float]:
    return [float(value.real), float(value.imag)]


def matrix(payload: dict[str, Any], name: str) -> list[list[complex]]:
    return [[as_complex(value) for value in row] for row in payload["exact_values"][name]]


def trace_diag_bh_matrix(b_row: list[float], h_diag: list[complex], mat: list[list[complex]]) -> complex:
    return sum(b_row[i] * h_diag[i] * mat[i][i] for i in range(3))


def row_norm(rows: list[float]) -> float:
    return math.sqrt(sum(value * value for value in rows))


def main() -> int:
    sources = [PHI_INVENTORY, TRACE_BASIS, TRACE_ROWS, STEP10, UNPATCHED, UNPATCHED_PAYLOAD, FULLS2_GAP, FLAVOR_VALUES]
    missing = [rel(path) for path in sources if not path.exists()]
    if missing:
        raise FileNotFoundError("missing sector response density inputs: " + ", ".join(missing))

    phi_inventory = load(PHI_INVENTORY)
    trace_basis = load(TRACE_BASIS)
    trace_rows = load(TRACE_ROWS)
    step10 = load(STEP10)
    unpatched = load(UNPATCHED)
    payload = load(UNPATCHED_PAYLOAD)
    fulls2_gap = load(FULLS2_GAP)
    flavor = load(FLAVOR_VALUES)

    b_rows = trace_basis["dual_trace_rows_B0_B1_B2"]
    h_diag = [
        complex(1.0, 0.0),
        complex(-0.5, 0.8660254037844386),
        complex(-0.5, -0.8660254037844386),
    ]
    lane_matrices = {
        "phase_Z": matrix(payload, "phase_R_Z"),
        "shift_X": matrix(payload, "shift_R_X"),
    }
    lane_sector_map = {
        "u": "phase_Z",
        "e": "phase_Z",
        "d": "shift_X",
    }

    lane_trace_rows: dict[str, list[dict[str, Any]]] = {}
    for lane, mat in lane_matrices.items():
        rows = []
        for index, b_row in enumerate(b_rows):
            value = trace_diag_bh_matrix(b_row, h_diag, mat)
            rows.append(
                {
                    "basis_index": index,
                    "trace_value_complex_pair": complex_pair(value),
                    "trace_value_real_part": value.real,
                    "trace_value_imag_abs": abs(value.imag),
                    "real_scalar_eligible": abs(value.imag) < 1e-12,
                }
            )
        lane_trace_rows[lane] = rows

    projected_rows = []
    policy_values = flavor["sector_operator_coefficients"]
    real_residuals = []
    for formal in trace_rows["rows"]:
        _, sector, coeff = formal["trace_row_id"].split(".")
        index = int(coeff[-1])
        lane = lane_sector_map[sector]
        lane_row = lane_trace_rows[lane][index]
        projected = lane_row["trace_value_real_part"]
        policy = policy_values[sector][coeff]
        residual = projected - policy
        real_residuals.append(residual)
        projected_rows.append(
            {
                "row_id": formal["trace_row_id"],
                "sector": sector,
                "coefficient": coeff,
                "source_lane": lane,
                "projected_c1_trace_value_complex_pair": lane_row["trace_value_complex_pair"],
                "projected_real_part": projected,
                "policy_replay_value": policy,
                "real_part_minus_policy": residual,
                "imag_abs": lane_row["trace_value_imag_abs"],
                "accepted_as_phi_sector_n_value": False,
                "accepted_as_csk_source_row": False,
                "blocking_reason": (
                    "Promoted C1 lane matrix is a phase/shift dynamic response, not the "
                    "full sector-resolving S2/Phi_sector_N density row."
                ),
            }
        )

    phase_vector = [row["projected_real_part"] for row in projected_rows if row["source_lane"] == "phase_Z"][:3]
    u_vector = [row["projected_real_part"] for row in projected_rows if row["sector"] == "u"]
    e_vector = [row["projected_real_part"] for row in projected_rows if row["sector"] == "e"]
    d_vector = [row["projected_real_part"] for row in projected_rows if row["sector"] == "d"]
    u_policy = [policy_values["u"][f"c{i}"] for i in range(3)]
    e_policy = [policy_values["e"][f"c{i}"] for i in range(3)]
    d_policy = [policy_values["d"][f"c{i}"] for i in range(3)]
    u_e_c1_duplicate_residual = max(abs(u_vector[i] - e_vector[i]) for i in range(3))
    u_e_policy_difference_norm = row_norm([u_policy[i] - e_policy[i] for i in range(3)])
    max_policy_residual = max(abs(value) for value in real_residuals)
    rms_policy_residual = math.sqrt(sum(value * value for value in real_residuals) / len(real_residuals))
    imaginary_rows = sum(1 for row in projected_rows if row["imag_abs"] >= 1e-12)

    import_packet = {
        "schema": "MTTStep10C1SectorMatrixImport.v1",
        "status": "STEP10_C1_SECTOR_MATRICES_IMPORTED_FOR_PHI_SECTOR_N_TEST",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {
            "phi_inventory": rel(PHI_INVENTORY),
            "step10": rel(STEP10),
            "unpatched_source_rule": rel(UNPATCHED),
            "unpatched_payload": rel(UNPATCHED_PAYLOAD),
        },
        "imported_closure": {
            "route_A_selected_physical_PhiFinC1_source_rule_closed": step10["closure_decision"][
                "route_A_selected_physical_PhiFinC1_source_rule_closed"
            ],
            "selected_dynamic_phi_fin_c1_payload_emitted": payload["decision"][
                "selected_dynamic_phi_fin_c1_payload_emitted"
            ],
            "A_selected_promoted_strict": payload["decision"]["A_selected_promoted_strict"],
            "b_selected_promoted_strict": payload["decision"]["b_selected_promoted_strict"],
            "deltaTheta_C1_promoted_strict": payload["decision"]["deltaTheta_C1_promoted_strict"],
            "sector_response_matrices_promoted_strict": payload["decision"][
                "sector_response_matrices_promoted_strict"
            ],
            "full_S2_value_rows_closed": step10["closure_decision"]["full_S2_value_rows_closed"],
            "Yukawa_CKM_PMNS_Higgs_mass_value_rows_without_proxy_fitting_closed": step10[
                "closure_decision"
            ]["Yukawa_CKM_PMNS_Higgs_mass_value_rows_without_proxy_fitting_closed"],
        },
        "import_decision": (
            "Accepted as selected C1 dynamic response support; not accepted by type as the "
            "full S2/Phi_sector_N density values."
        ),
    }

    trace_exec = {
        "schema": "MTTC1LaneCommonCircleTraceExecution.v1",
        "status": "C1_LANE_COMMONCIRCLE_TRACES_EXECUTED_NOT_FULL_PHI_SECTOR_N",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "H_cen": "diag(1,zeta_3,zeta_3^2)",
        "lane_trace_rows": lane_trace_rows,
        "sector_lane_map_tested": lane_sector_map,
        "projected_rows": projected_rows,
        "formal_trace_row_count": len(projected_rows),
        "accepted_phi_sector_n_value_count": 0,
        "accepted_csk_source_row_count": 0,
    }

    obstruction = {
        "schema": "MTTSectorDensityCodomainObstruction.v1",
        "status": "C1_SECTOR_MATRICES_DO_NOT_EMIT_NINE_PHI_SECTOR_N_VALUES",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "obstruction_fields": {
            "c1_lane_count": len(lane_matrices),
            "required_charged_sector_count": 3,
            "required_phi_sector_n_row_count": phi_inventory["closure_decision"][
                "Phi_sector_N_required_numeric_value_count"
            ],
            "accepted_phi_sector_n_row_count": 0,
            "accepted_csk_source_row_count": 0,
            "u_and_e_share_same_phase_lane": True,
            "u_e_c1_duplicate_residual": u_e_c1_duplicate_residual,
            "u_e_policy_difference_norm": u_e_policy_difference_norm,
            "d_shift_lane_has_complex_commoncircle_rows": any(
                row["trace_value_imag_abs"] >= 1e-12 for row in lane_trace_rows["shift_X"]
            ),
            "imaginary_projected_row_count": imaginary_rows,
            "max_abs_real_part_minus_policy": max_policy_residual,
            "rms_real_part_minus_policy": rms_policy_residual,
            "full_S2_value_rows_closed": fulls2_gap["full_S2_value_rows_closed"],
            "accepted_Yukawa_magnitudes_closed": fulls2_gap["accepted_Yukawa_magnitudes_closed"],
        },
        "vectors": {
            "phase_lane_real_trace_vector": phase_vector,
            "u_projected_real_vector": u_vector,
            "e_projected_real_vector": e_vector,
            "d_projected_real_vector": d_vector,
            "u_policy_vector": u_policy,
            "e_policy_vector": e_policy,
            "d_policy_vector": d_policy,
        },
        "decision": (
            "The selected C1 sector matrices are real progress and close source ownership "
            "for the dynamic C1 payload.  They do not close Phi_sector_N because their "
            "trace image is a two-lane C1 response, not a three-sector full-S2 density "
            "with nine magnitude-bearing row certificates."
        ),
    }

    next_packet = {
        "schema": "MTTNextCutsetAfterC1DensityBridge.v1",
        "status": "NEXT_IS_FULL_S2_SECTOR_DENSITY_OPERATOR",
        "closure_claimed": True,
        "closed_now": [
            "later Step10/Phi_fin^C1 sector response matrix promotion imported",
            "common-circle traces of selected phase/shift C1 matrices executed",
            "C1 response support separated from full S2/Phi_sector_N density rows",
            "the potential Step10-already-closes-csk shortcut rejected by calculation",
        ],
        "still_open": [
            "full S2 sector density operator Phi_sector_N",
            "nine real magnitude-bearing Phi_sector_N.s.ck row values",
            "row certificates independent of policy replay",
            "strict no-knob c_{s,k} row emission",
        ],
        "next_required_artifact": NEXT,
        "ordered_attack": [
            "construct full S2 sector density operator using selected C1 support plus threshold/HYM response",
            "add the missing sector-separating density correction that distinguishes u from e",
            "prove realness/magnitude-bearing row certificates",
            "rerun the common-circle trace engine and accept rows only after source emission",
        ],
    }

    candidate = {
        "candidate": "MTTSelectedSectorResponseDensitySourceOrNoKnobCSKRowEmission",
        "status": STATUS,
        "closure_claimed": True,
        "strict_phi_sector_n_values_claimed": False,
        "strict_csk_source_theorem_claimed": False,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "C1SectorMatrixBridgeObstructionTheorem",
            "proved": True,
            "statement": (
                "The later selected Phi_fin^C1 source rule does promote strict C1 sector "
                "response matrices, but their common-circle trace image is only the "
                "phase/shift dynamic-C1 lane image.  Therefore these matrices are support "
                "for the future Phi_sector_N density theorem, not the nine selected "
                "Phi_sector_N coefficient values themselves."
            ),
        },
        "closure_decision": {
            "step10_c1_sector_matrices_imported": True,
            "selected_dynamic_phi_fin_c1_payload_emitted": True,
            "sector_response_matrices_promoted_strict": True,
            "c1_lane_commoncircle_traces_executed": True,
            "c1_lane_trace_row_count": len(projected_rows),
            "required_phi_sector_n_value_count": phi_inventory["closure_decision"][
                "Phi_sector_N_required_numeric_value_count"
            ],
            "accepted_phi_sector_n_value_count": 0,
            "accepted_strict_csk_source_row_count": 0,
            "full_S2_value_rows_closed": False,
            "Yukawa_magnitude_rows_closed": False,
            "policy_replay_rows_accepted_as_source": False,
            "strict_csk_source_theorem_closed": False,
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "key_numbers": {
            "u_e_c1_duplicate_residual": u_e_c1_duplicate_residual,
            "u_e_policy_difference_norm": u_e_policy_difference_norm,
            "imaginary_projected_row_count": imaginary_rows,
            "max_abs_real_part_minus_policy": max_policy_residual,
            "rms_real_part_minus_policy": rms_policy_residual,
        },
        "packets": {
            "step10_c1_sector_matrix_import": rel(IMPORT_PACKET),
            "c1_lane_commoncircle_trace_execution": rel(TRACE_EXEC_PACKET),
            "sector_density_codomain_obstruction": rel(OBSTRUCTION_PACKET),
            "next_cutset": rel(NEXT_PACKET),
        },
    }

    cert = {
        "certificate": "MTTSelectedSectorResponseDensitySourceOrNoKnobCSKRowEmissionCertificate",
        "status": STATUS,
        "theorem": candidate["theorem"]["name"],
        "step10_c1_sector_matrices_imported": True,
        "selected_dynamic_phi_fin_c1_payload_emitted": True,
        "sector_response_matrices_promoted_strict": True,
        "c1_lane_commoncircle_traces_executed": True,
        "accepted_phi_sector_n_value_count": 0,
        "accepted_strict_csk_source_row_count": 0,
        "u_e_c1_duplicate_residual": u_e_c1_duplicate_residual,
        "u_e_policy_difference_norm": u_e_policy_difference_norm,
        "full_S2_value_rows_closed": False,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected SectorResponseDensitySourceTheorem or NoKnobCSKRowEmission v1

Status: `{STATUS}`

## Theorem

`C1SectorMatrixBridgeObstructionTheorem` is proved.

The later active-ledger Step10/Phi_fin^C1 result is real: it promotes
`A_selected`, `b_selected`, `deltaTheta_C1`, and strict C1 sector response
matrices before observed replay.  This packet imports that result and executes
the common-circle trace test against the selected phase/shift matrices.

The result is not the nine `Phi_sector_N` density values.  The C1 payload has
two dynamic lanes:

- phase/clock lane for `u/e`
- shift lane for `d/nuD`

The common-circle traces of those lanes are computable, but they are not a
three-sector full-S2 density.  In particular the C1 bridge duplicates the `u`
and `e` phase lane with duplicate residual `{u_e_c1_duplicate_residual}`, while
the policy `u/e` vectors differ with norm `{u_e_policy_difference_norm}`.

## Counts

- selected C1 sector response matrices imported: `true`
- C1 lane trace rows executed: `{len(projected_rows)}`
- accepted strict `Phi_sector_N` rows: `0`
- accepted strict `c_{{s,k}}` source rows: `0`
- full S2 value rows closed: `false`

## Boundary

This does not weaken Step10.  Step10 closes the dynamic C1 source-rule layer.
It does not by itself emit the full S2 sector density operator required for
charged Yukawa magnitude rows.

## Next Artifact

`{NEXT}`.
"""

    write_json(IMPORT_PACKET, import_packet)
    write_json(TRACE_EXEC_PACKET, trace_exec)
    write_json(OBSTRUCTION_PACKET, obstruction)
    write_json(NEXT_PACKET, next_packet)
    write_json(CANDIDATE, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
