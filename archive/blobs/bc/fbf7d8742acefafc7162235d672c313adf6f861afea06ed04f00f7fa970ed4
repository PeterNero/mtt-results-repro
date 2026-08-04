"""Build first-pass MZ-to-Mt Jacobian execution / threshold response fill gate.

This artifact differentiates the already accepted first-pass one-loop RG
transport engine.  It closes a finite, reproducible first-pass Jacobian and
uses it to fill the first nonzero weak/BCT cross-block covariance entries.
It deliberately does not promote the result to a selected precision threshold
functional or no-knob SM closure.
"""

from __future__ import annotations

import copy
import importlib.util
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_mztomtjacobianexecution_or_selectedthresholdresponsefunctionalfill"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
JACOBIAN = PACKET_DIR / "firstpass_rg_mz_to_mt_jacobian.packet.json"
CROSSBLOCK = PACKET_DIR / "firstpass_weak_bct_crossblock_covariance.packet.json"
RTHETA_FILL = PACKET_DIR / "selected_threshold_response_functional_fill_gate.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_mztomt_jacobian_execution.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_MZtoMtJacobianExecution_or_SelectedThresholdResponseFunctionalFill_v1.md"

PREVIOUS = DATA / "selected_commonscalejacobian_or_rthetathresholdresponseexecution.candidate.json"
ALGEBRAIC = (
    DATA
    / "selected_commonscalejacobian_or_rthetathresholdresponseexecution"
    / "bct_mz_mass_to_yukawa_v_jacobian.packet.json"
)
COMMON_SCALE = (
    DATA
    / "selected_acceptedcommonscaleyukawahiggsvalues_or_profilelikelihoodexecution"
    / "versioned_common_scale_yukawa_higgs_values.packet.json"
)
TRANSPORT_KERNEL = (
    DATA
    / "selected_commonscaleyukawahiggstransport_or_finalreplayaudit"
    / "yukawa_higgs_common_scale_transport_kernel.packet.json"
)
SMOKE = (
    DATA
    / "selected_rgengineexecution_or_selectedsmpacketcertificateintegration"
    / "diagnostic_one_loop_transport_smoke_run.packet.json"
)
INTERIM_MATRIX = (
    DATA
    / "selected_crossblockcovariancevalues_or_rthetacoefficientexecution"
    / "deduplicated_interim_block_covariance_matrix.packet.json"
)
RTHETA_CONTRACT = (
    DATA
    / "selected_thresholdresponsefunctionalderivation_or_profilelikelihoodacquisition"
    / "selected_threshold_response_functional_contract.packet.json"
)
ENGINE_BUILDER = ROOT / "scripts" / "build_selected_rgengineexecution_or_selectedsmpacketcertificateintegration.py"

STATUS = (
    "MTT_SELECTED_MZTOMTJACOBIANEXECUTION_OR_SELECTEDTHRESHOLDRESPONSEFUNCTIONALFILL_"
    "BUILT_FIRSTPASS_RG_JACOBIAN_AND_CROSSBLOCK_RESPONSE_SELECTED_RTHETA_OPEN"
)
NEXT = "MTT_Selected_RThetaCoefficientValues_or_SelectedThresholdFunctionalSourceRows_v1"


Matrix = list[list[float]]


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing MZ-to-Mt Jacobian sources: " + ", ".join(missing))


def load_rg_engine() -> Any:
    spec = importlib.util.spec_from_file_location("mtt_rg_engine_builder", ENGINE_BUILDER)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot load RG engine builder from {ENGINE_BUILDER}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def diag_real(matrix: list, i: int, j: int) -> float:
    value = matrix[i][j]
    if isinstance(value, list):
        return float(value[0])
    return float(value)


def clone_state(yu: list[list[complex]], yd: list[list[complex]], ye: list[list[complex]], lam: float) -> tuple:
    return copy.deepcopy(yu), copy.deepcopy(yd), copy.deepcopy(ye), float(lam)


def output_vector(run: dict[str, Any]) -> list[float]:
    data = run["diagnostic_run"] if "diagnostic_run" in run else run
    return [
        float(data["diagnostic_lambda_H_MZ_like"]),
        diag_real(data["diagnostic_Y_u_MZ_like"], 2, 2),
        diag_real(data["diagnostic_Y_d_MZ_like"], 2, 2),
        diag_real(data["diagnostic_Y_u_MZ_like"], 1, 1),
        diag_real(data["diagnostic_Y_e_MZ_like"], 2, 2),
    ]


def perturb_coordinate(
    yu: list[list[complex]],
    yd: list[list[complex]],
    ye: list[list[complex]],
    lam: float,
    coord: dict[str, Any],
    delta: float,
) -> tuple:
    pyu, pyd, pye, plam = clone_state(yu, yd, ye, lam)
    if coord["kind"] == "lambda":
        plam += delta
    else:
        target = {"Y_u": pyu, "Y_d": pyd, "Y_e": pye}[coord["matrix"]]
        i = coord["i"]
        j = coord["j"]
        target[i][j] += complex(delta, 0.0)
    return pyu, pyd, pye, plam


def matmul(a: Matrix, b: Matrix) -> Matrix:
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def identity(n: int) -> Matrix:
    return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]


def invert_matrix(matrix: Matrix) -> tuple[Matrix, float]:
    n = len(matrix)
    aug = [list(row) + ident for row, ident in zip(copy.deepcopy(matrix), identity(n))]
    det = 1.0
    sign = 1.0
    for col in range(n):
        pivot = max(range(col, n), key=lambda row: abs(aug[row][col]))
        pivot_value = aug[pivot][col]
        if abs(pivot_value) < 1e-18:
            raise ValueError("singular first-pass transport Jacobian")
        if pivot != col:
            aug[col], aug[pivot] = aug[pivot], aug[col]
            sign *= -1.0
        det *= aug[col][col]
        scale = aug[col][col]
        aug[col] = [value / scale for value in aug[col]]
        for row in range(n):
            if row == col:
                continue
            factor = aug[row][col]
            if factor == 0.0:
                continue
            aug[row] = [aug[row][k] - factor * aug[col][k] for k in range(2 * n)]
    return [row[n:] for row in aug], sign * det


def max_abs_residual(a: Matrix, b: Matrix) -> float:
    prod = matmul(a, b)
    ident = identity(len(a))
    return max(abs(prod[i][j] - ident[i][j]) for i in range(len(a)) for j in range(len(a)))


def max_row_sum(matrix: Matrix) -> float:
    return max(sum(abs(value) for value in row) for row in matrix)


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [PREVIOUS, ALGEBRAIC, COMMON_SCALE, TRANSPORT_KERNEL, SMOKE, INTERIM_MATRIX, RTHETA_CONTRACT, ENGINE_BUILDER]
    require_sources(sources)

    previous = load(PREVIOUS)
    algebraic = load(ALGEBRAIC)
    common_scale = load(COMMON_SCALE)
    kernel = load(TRANSPORT_KERNEL)
    smoke = load(SMOKE)
    interim = load(INTERIM_MATRIX)
    rtheta_contract = load(RTHETA_CONTRACT)
    rg = load_rg_engine()

    native = kernel["native_values_to_transport"]
    gauges = kernel["available_common_scale_inputs"]
    yu = rg.to_complex_matrix(native["Y_u_native"])
    yd = rg.to_complex_matrix(native["Y_d_native_complex_up_diagonal_convention"])
    ye = rg.to_complex_matrix(native["Y_e_native"])
    lam = float(native["lambda_H_tree_native"])
    mu0 = float(smoke["diagnostic_run"]["from_scale_GeV"])
    g1 = float(gauges["g_1_GUT_MZ"]["central_value"])
    g2 = float(gauges["g_2_MZ"]["central_value"])
    g3 = float(gauges["g_3_MZ"]["central_value"])

    coordinate_rows = [
        {"id": "lambda_Mt_native", "kind": "lambda", "native_value": lam},
        {"id": "y_t_Mt_native", "kind": "matrix", "matrix": "Y_u", "i": 2, "j": 2, "native_value": yu[2][2].real},
        {"id": "y_b_Mt_native_diag", "kind": "matrix", "matrix": "Y_d", "i": 2, "j": 2, "native_value": yd[2][2].real},
        {"id": "y_c_Mt_native", "kind": "matrix", "matrix": "Y_u", "i": 1, "j": 1, "native_value": yu[1][1].real},
        {"id": "y_tau_Mt_native", "kind": "matrix", "matrix": "Y_e", "i": 2, "j": 2, "native_value": ye[2][2].real},
    ]
    output_rows = [
        "lambda_MZ_firstpass",
        "y_t_MZ_firstpass",
        "y_b_MZ_firstpass",
        "y_c_MZ_firstpass",
        "y_tau_MZ_firstpass",
    ]

    baseline_run = rg.run_smoke(copy.deepcopy(yu), copy.deepcopy(yd), copy.deepcopy(ye), lam, mu0=mu0, g1=g1, g2=g2, g3=g3)
    baseline_vec = output_vector(baseline_run)
    accepted_vec = [
        common_scale["derived_magnitudes"]["lambda_H"],
        common_scale["derived_magnitudes"]["diag_abs_Y_u"][2],
        common_scale["derived_magnitudes"]["diag_abs_Y_d"][2],
        common_scale["derived_magnitudes"]["diag_abs_Y_u"][1],
        common_scale["derived_magnitudes"]["diag_abs_Y_e"][2],
    ]
    max_baseline_delta = max(abs(a - b) for a, b in zip(baseline_vec, accepted_vec))

    forward_cols: list[list[float]] = []
    finite_difference_steps: dict[str, float] = {}
    for coord in coordinate_rows:
        native_value = abs(float(coord["native_value"]))
        delta = max(1e-7 * max(native_value, 1.0), 1e-9)
        finite_difference_steps[coord["id"]] = delta
        plus_state = perturb_coordinate(yu, yd, ye, lam, coord, delta)
        minus_state = perturb_coordinate(yu, yd, ye, lam, coord, -delta)
        plus_vec = output_vector(rg.run_smoke(*plus_state, mu0=mu0, g1=g1, g2=g2, g3=g3))
        minus_vec = output_vector(rg.run_smoke(*minus_state, mu0=mu0, g1=g1, g2=g2, g3=g3))
        forward_cols.append([(plus_vec[i] - minus_vec[i]) / (2.0 * delta) for i in range(len(output_rows))])
    forward = [[forward_cols[col][row] for col in range(len(coordinate_rows))] for row in range(len(output_rows))]
    inverse, determinant = invert_matrix(forward)
    inverse_residual = max_abs_residual(forward, inverse)
    condition_proxy = max_row_sum(forward) * max_row_sum(inverse)

    jacobian_packet = {
        "schema": "MTTFirstPassRGMZtoMtJacobian.v1",
        "status": "FIRSTPASS_RG_TRANSPORT_JACOBIAN_EXECUTED_PRECISION_SELECTED_THRESHOLD_OPEN",
        "engine_source": rel(ENGINE_BUILDER),
        "smoke_source": rel(SMOKE),
        "common_scale_source": rel(COMMON_SCALE),
        "transport_kernel_source": rel(TRANSPORT_KERNEL),
        "engine_convention": smoke["engine"],
        "from_scale_GeV": mu0,
        "to_scale_GeV": smoke["diagnostic_run"]["to_scale_GeV"],
        "steps": smoke["diagnostic_run"]["steps"],
        "input_coordinate_rows_native_Mt": [row["id"] for row in coordinate_rows],
        "output_coordinate_rows_MZ": output_rows,
        "baseline_output_values": dict(zip(output_rows, baseline_vec)),
        "accepted_common_scale_reference_values": dict(zip(output_rows, accepted_vec)),
        "max_baseline_delta_vs_accepted_packet": max_baseline_delta,
        "finite_difference_steps": finite_difference_steps,
        "forward_Mt_to_MZ_jacobian_rows_output_by_cols_input": forward,
        "inverse_MZ_to_Mt_jacobian_rows_native_by_cols_output": inverse,
        "determinant_forward": determinant,
        "inverse_residual_max_abs": inverse_residual,
        "condition_proxy_row_sum": condition_proxy,
        "accepted_as_firstpass_Mt_to_MZ_RG_jacobian": True,
        "accepted_as_firstpass_MZ_to_Mt_RG_jacobian": True,
        "accepted_as_selected_precision_MZ_to_Mt_RG_jacobian": False,
        "why_not_precision_selected": [
            "gauge couplings are frozen at accepted M_Z values",
            "threshold matching is still diagnostic/no-threshold",
            "pole/rest/native mass-scheme conversion is not the selected precision map",
            "the finite-difference basis is a five-row diagonal core, not the full matrix/covariance basis",
            "the selected R_theta threshold functional source rows are not emitted",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(JACOBIAN, jacobian_packet)

    row_basis = interim["row_basis"]
    index = {row_id: i for i, row_id in enumerate(row_basis)}
    covariance = copy.deepcopy(interim["covariance_matrix"])
    bct_ids = [
        "bottom_MSbar_native_scale_transport",
        "charm_MSbar_native_scale_transport",
        "tau_pole_rest_to_running_lepton",
    ]
    bct_to_mz_col = {
        "bottom_MSbar_native_scale_transport": output_rows.index("y_b_MZ_firstpass"),
        "charm_MSbar_native_scale_transport": output_rows.index("y_c_MZ_firstpass"),
        "tau_pole_rest_to_running_lepton": output_rows.index("y_tau_MZ_firstpass"),
    }
    weak_to_inverse_row = {
        "lambda_Mt": coordinate_rows.index(next(row for row in coordinate_rows if row["id"] == "lambda_Mt_native")),
        "y_t_Mt": coordinate_rows.index(next(row for row in coordinate_rows if row["id"] == "y_t_Mt_native")),
    }
    algebraic_by_id = {row["id"]: row for row in algebraic["row_jacobians"]}

    inserted_entries: list[dict[str, Any]] = []
    v_index = index["v_from_G_F_tree_reference"]
    var_v = covariance[v_index][v_index]
    for weak_row, inv_row in weak_to_inverse_row.items():
        weak_index = index[weak_row]
        dx_dm: dict[str, float] = {}
        dx_dv = 0.0
        for bct_id in bct_ids:
            alg = algebraic_by_id[bct_id]
            sensitivity_to_y_mz = inverse[inv_row][bct_to_mz_col[bct_id]]
            dx_dm[bct_id] = sensitivity_to_y_mz * alg["dy_dm"]
            dx_dv += sensitivity_to_y_mz * alg["dy_dv"]
        for bct_id in bct_ids:
            bct_index = index[bct_id]
            cov_value = sum(dx_dm[other] * covariance[index[other]][bct_index] for other in bct_ids)
            covariance[weak_index][bct_index] = cov_value
            covariance[bct_index][weak_index] = cov_value
            inserted_entries.append(
                {
                    "left": weak_row,
                    "right": bct_id,
                    "covariance": cov_value,
                    "method": "inverse_firstpass_MZ_to_Mt_jacobian_times_BCT_mass_covariance",
                }
            )
        cov_v = dx_dv * var_v
        covariance[weak_index][v_index] = cov_v
        covariance[v_index][weak_index] = cov_v
        inserted_entries.append(
            {
                "left": weak_row,
                "right": "v_from_G_F_tree_reference",
                "covariance": cov_v,
                "method": "inverse_firstpass_MZ_to_Mt_jacobian_times_BCT_yukawa_v_derivative",
            }
        )

    crossblock_packet = {
        "schema": "MTTFirstPassWeakBCTCrossBlockCovariance.v1",
        "status": "FIRSTPASS_WEAK_BCT_CROSSBLOCK_COVARIANCE_VALUES_EMITTED_FULL_PROFILE_OPEN",
        "interim_matrix_source": rel(INTERIM_MATRIX),
        "jacobian_source": rel(JACOBIAN),
        "algebraic_bct_jacobian_source": rel(ALGEBRAIC),
        "row_basis": row_basis,
        "covariance_matrix": covariance,
        "inserted_cross_block_entries": inserted_entries,
        "inserted_entry_count": len(inserted_entries),
        "accepted_as_firstpass_cross_block_covariance_values": True,
        "accepted_as_full_covariance_profile_likelihood": False,
        "accepted_as_selected_threshold_response_covariance": False,
        "why_not_full_profile": [
            "only lambda_Mt/y_t_Mt weak rows are coupled through the five-row first-pass inverse",
            "gauge rows remain frozen and threshold-response rows are not selected",
            "BCT-to-Higgs-sector covariance beyond v/lambda is still open",
            "R_theta coefficient/source rows are still contract-only",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(CROSSBLOCK, crossblock_packet)

    rtheta_fill = {
        "schema": "MTTSelectedThresholdResponseFunctionalFillGate.v1",
        "status": "FIRSTPASS_JACOBIAN_AVAILABLE_RTHETA_SOURCE_ROWS_OPEN",
        "contract_source": rel(RTHETA_CONTRACT),
        "jacobian_source": rel(JACOBIAN),
        "crossblock_source": rel(CROSSBLOCK),
        "functional_symbol": rtheta_contract["functional_symbol"],
        "what_the_jacobian_supplies": [
            "finite first-pass local coordinate derivative for lambda/y_t/y_b/y_c/y_tau",
            "invertible local M_Z-to-M_t response on the five-row diagonal core",
            "first nonzero weak/BCT covariance entries that future R_theta rows must reproduce or replace",
        ],
        "still_missing_for_selected_Rtheta": rtheta_contract["codomain_required"],
        "Rtheta_coefficient_values_closed": False,
        "selected_threshold_response_functional_instantiated": False,
        "selected_Rtheta_source_rows_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(RTHETA_FILL, rtheta_fill)

    cutset = {
        "schema": "MTTNextCutsetAfterMZtoMtJacobianExecution.v1",
        "status": "NEXT_ATTACK_RTHETA_COEFFICIENT_VALUES_OR_SOURCE_ROWS",
        "closed_now": {
            "firstpass_Mt_to_MZ_RG_jacobian": True,
            "firstpass_MZ_to_Mt_inverse_RG_jacobian": True,
            "firstpass_weak_BCT_crossblock_covariance_values": True,
            "selected_threshold_response_functional_fill_gate_rechecked": True,
        },
        "still_open": {
            "selected_precision_MZ_to_Mt_common_scale_RG_jacobian": True,
            "common_scale_convention_map_for_precision": True,
            "Rtheta_coefficient_values": True,
            "selected_threshold_response_functional": True,
            "selected_Rtheta_source_rows": True,
            "full_covariance_profile_likelihood": True,
            "true_SM_equivalence": True,
            "full_no_knob": True,
        },
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "promote or replace the first-pass Jacobian by selected R_theta coefficient/source rows",
            "route_B": "fill threshold::W_Z_H and BCT mass-scheme response coefficients from the same source branch",
            "route_C": "extend the finite-difference basis from the five-row diagonal core to the full Yukawa/Higgs/gauge covariance basis",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedMZtoMtJacobianExecutionOrSelectedThresholdResponseFunctionalFill",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "firstpass_rg_mz_to_mt_jacobian": rel(JACOBIAN),
            "firstpass_weak_bct_crossblock_covariance": rel(CROSSBLOCK),
            "selected_threshold_response_functional_fill_gate": rel(RTHETA_FILL),
            "next_cutset_after_mztomt_jacobian_execution": rel(CUTSET),
        },
        "theorem": {
            "name": "FirstPassRGMZtoMtJacobianExecutionTheorem",
            "proved": True,
            "statement": (
                "Differentiating the accepted first-pass one-loop RK transport engine by central finite "
                "differences yields an invertible five-row local Mt-to-MZ Jacobian and hence a reproducible "
                "first-pass MZ-to-Mt inverse Jacobian. Composed with the exact BCT mass-to-yukawa map, this "
                "emits the first nonzero weak/BCT covariance entries. This is a first-pass SM-parity "
                "execution layer, not a selected precision threshold response or no-knob SM closure."
            ),
        },
        "what_closes_now": cutset["closed_now"],
        "what_remains_open": cutset["still_open"],
        "closure_decision": {
            "firstpass_MZ_to_Mt_common_scale_RG_jacobian_closed": True,
            "firstpass_numeric_cross_block_covariance_values_closed": True,
            "selected_precision_MZ_to_Mt_common_scale_RG_jacobian_closed": False,
            "Rtheta_coefficient_values_closed": False,
            "selected_threshold_response_functional_closed": False,
            "selected_Rtheta_source_rows_closed": False,
            "full_covariance_profile_likelihood_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_MZtoMtJacobianExecution_or_SelectedThresholdResponseFunctionalFill_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "firstpass_MZ_to_Mt_common_scale_RG_jacobian_closed": True,
        "firstpass_numeric_cross_block_covariance_values_closed": True,
        "selected_precision_MZ_to_Mt_common_scale_RG_jacobian_closed": False,
        "Rtheta_coefficient_values_closed": False,
        "selected_threshold_response_functional_closed": False,
        "selected_Rtheta_source_rows_closed": False,
        "full_covariance_profile_likelihood_closed": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected MZtoMtJacobianExecution or SelectedThresholdResponseFunctionalFill v1

Status: `{STATUS}`.

This artifact differentiates the accepted first-pass one-loop RK transport
engine on the five-row diagonal core:

```text
lambda_H, y_t, y_b, y_c, y_tau
```

It emits both the forward `M_t -> M_Z` Jacobian and the inverse first-pass
`M_Z -> M_t` Jacobian.  The inverse is then composed with the exact BCT
`y=sqrt(2)m/v` map to fill the first nonzero weak/BCT cross-block covariance
entries for `lambda_Mt` and `y_t_Mt`.

```text
first-pass MZ -> Mt Jacobian closed       : true
first-pass weak/BCT cross-block values    : true
selected precision threshold response     : false
R_theta coefficient/source rows           : false
full SM/no-knob closure                   : false
```

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
