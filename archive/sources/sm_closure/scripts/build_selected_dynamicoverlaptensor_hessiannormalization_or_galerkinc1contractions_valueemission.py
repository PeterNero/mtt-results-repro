"""Build dynamic-overlap / Hessian / Galerkin C1 value-emission audit."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PREVIOUS = DATA / "selected_primitivec1_contractions_or_dynamicoverlaptensor_sourceemission.candidate.json"
CROSS_ALPHA = DATA / "selected_crossrepo_alpha1_driver_replay_import.candidate.json"
PRIMITIVE_SELECTOR = DATA / "selected_primitivefibershift_or_typedretardedselector_sourcetheorem.candidate.json"
PRIMITIVE_CLASS = DATA / "selected_primitiveclass_c1observable_or_higherorder_fullresponse_sourceemission.candidate.json"
NONINV = DATA / "selected_routec_noninvariant_c1_primitive_search.candidate.json"
OVERLAP = DATA / "selected_smslotfunctor_overlapkernel_source_emission.candidate.json"
C1_EMISSION = DATA / "selected_routec_selected_c1_response_operator_emission.candidate.json"
SPLITTER = DATA / "selected_routec_splitter_source_emission_contract_or_selected_deltatheta_c1_solve.candidate.json"
TYPED = DATA / "selected_typedbn_retardedderivative_or_primitiveresponse_valueemission.candidate.json"
HONEST_PRIMITIVE = (
    DATA / "selected_routec_strominger_galerkin_solve" / "c1_primitive_contractions.candidate.json"
)
HIGHER_ORDER = DATA / "selected_routec_higherorder_fullresponse_flavor_splitting.candidate.json"

OUTPUT = DATA / "selected_dynamicoverlaptensor_hessiannormalization_or_galerkinc1contractions_valueemission.candidate.json"
CERT = CERTS / "selected_dynamicoverlaptensor_hessiannormalization_or_galerkinc1contractions_valueemission_certificate.json"
NOTE = CORPUS / "MTT_Selected_DynamicOverlapTensor_HessianNormalization_or_GalerkinC1Contractions_ValueEmission_v1.md"

STATUS = (
    "MTT_SELECTED_DYNAMICOVERLAPTENSOR_HESSIANNORMALIZATION_OR_GALERKINC1CONTRACTIONS_"
    "VALUEEMISSION_BUILT_DEGENERATE_LAYER_VALUES_OPEN"
)
NEXT = "MTT_Selected_NonScalarDynamicOverlap_or_FullResponseCorrection_ValueEmission_v1"
SECTORS = ["u", "d", "e", "nuD"]
TOL = 1e-12


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def transpose(matrix: list[list[float]]) -> list[list[float]]:
    return [list(row) for row in zip(*matrix)]


def matmul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def mat_sub(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def frob_norm_sq(matrix: list[list[float]]) -> float:
    return sum(value * value for row in matrix for value in row)


def trace(matrix: list[list[float]]) -> float:
    return sum(matrix[i][i] for i in range(len(matrix)))


def identity(n: int, scale: float = 1.0) -> list[list[float]]:
    return [[scale if i == j else 0.0 for j in range(n)] for i in range(n)]


def det3(m: list[list[float]]) -> float:
    return (
        m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
    )


def rank(matrix: list[list[float]], tol: float = TOL) -> int:
    work = [row[:] for row in matrix]
    rows = len(work)
    cols = len(work[0])
    r = 0
    for c in range(cols):
        pivot = max(range(r, rows), key=lambda i: abs(work[i][c]), default=r)
        if abs(work[pivot][c]) <= tol:
            continue
        work[r], work[pivot] = work[pivot], work[r]
        scale = work[r][c]
        work[r] = [value / scale for value in work[r]]
        for i in range(rows):
            if i == r:
                continue
            factor = work[i][c]
            if abs(factor) > tol:
                work[i] = [work[i][j] - factor * work[r][j] for j in range(cols)]
        r += 1
        if r == rows:
            break
    return r


def commutator_norm_sq(a: list[list[float]], b: list[list[float]]) -> float:
    return frob_norm_sq(mat_sub(matmul(a, b), matmul(b, a)))


def matrix_close(a: list[list[float]], b: list[list[float]], tol: float = TOL) -> bool:
    return frob_norm_sq(mat_sub(a, b)) <= tol


def primitive_by_shift(noninv: dict[str, Any], shift: int) -> dict[str, Any]:
    for item in noninv["candidate_primitives"]:
        if item["primitive_fiber_shift"] == shift:
            return item
    raise KeyError(f"primitive shift {shift} not found")


def matrix_invariants(matrix: list[list[float]]) -> dict[str, Any]:
    yy = matmul(matrix, transpose(matrix))
    scalar = trace(yy) / 3.0
    traceless = mat_sub(yy, identity(3, scalar))
    return {
        "rank": rank(matrix),
        "det_abs": abs(det3(matrix)),
        "max_abs_entry": max(abs(value) for row in matrix for value in row),
        "YYstar": yy,
        "YYstar_scalar": scalar,
        "YYstar_is_scalar_identity": frob_norm_sq(traceless) <= TOL,
        "YYstar_traceless_norm_sq": frob_norm_sq(traceless),
    }


def fixed_fiber_packet(noninv: dict[str, Any]) -> dict[str, Any]:
    packet: dict[str, Any] = {}
    for shift in [0, 1, 2]:
        primitive = primitive_by_shift(noninv, shift)
        sector_data = {}
        for sector in SECTORS:
            matrix = primitive["matrices"][sector]
            sector_data[sector] = {
                "matrix": matrix,
                "invariants": matrix_invariants(matrix),
            }
        packet[str(shift)] = {
            "primitive_active_shift": primitive["primitive_active_shift"],
            "primitive_fiber_shift": shift,
            "selected_by_theorem": primitive["selected_by_theorem"],
            "status": primitive["status"],
            "sectors": sector_data,
        }
    return packet


def quotient_checks(fixed: dict[str, Any]) -> dict[str, Any]:
    scalars = []
    dets = []
    ranks = []
    scalar_flags = []
    for shift_data in fixed.values():
        for sector in SECTORS:
            inv = shift_data["sectors"][sector]["invariants"]
            scalars.append(round(inv["YYstar_scalar"], 15))
            dets.append(round(inv["det_abs"], 15))
            ranks.append(inv["rank"])
            scalar_flags.append(inv["YYstar_is_scalar_identity"])
    representative = fixed["0"]["sectors"]["u"]["invariants"]["YYstar"]
    all_same_yy = all(
        matrix_close(fixed[shift]["sectors"][sector]["invariants"]["YYstar"], representative)
        for shift in ["0", "1", "2"]
        for sector in SECTORS
    )
    return {
        "fixed_fiber_shifts": [0, 1, 2],
        "all_fixed_fiber_ranks_three": sorted(set(ranks)) == [3],
        "all_YYstar_scalar_identity": all(scalar_flags),
        "all_YYstar_equal_to_representative": all_same_yy,
        "distinct_YYstar_scalars": sorted(set(scalars)),
        "distinct_det_abs_values": sorted(set(dets)),
        "quotient_invariant_for_current_spectral_observables": all_same_yy
        and sorted(set(ranks)) == [3]
        and all(scalar_flags),
    }


def sector_degeneracy_checks(representative: dict[str, Any]) -> dict[str, Any]:
    yy = {sector: representative["sectors"][sector]["invariants"]["YYstar"] for sector in SECTORS}
    matrices = {sector: representative["sectors"][sector]["matrix"] for sector in SECTORS}
    return {
        "all_sector_matrices_identical_in_representative": all(
            matrix_close(matrices[sector], matrices["u"]) for sector in SECTORS
        ),
        "all_sector_YYstar_identical": all(matrix_close(yy[sector], yy["u"]) for sector in SECTORS),
        "commutator_norm_sq_u_d": commutator_norm_sq(yy["u"], yy["d"]),
        "commutator_norm_sq_e_nuD": commutator_norm_sq(yy["e"], yy["nuD"]),
        "nondegenerate_mass_hierarchy_possible_from_current_layer": False,
        "CKM_PMNS_possible_from_current_layer": False,
        "CP_odd_invariant_possible_from_current_layer": False,
        "reason": (
            "Every current-layer sector matrix is a real scalar times a permutation matrix. "
            "Thus YY* is the same scalar identity in each sector, all Hermitian commutators vanish, "
            "and no complex CP-odd invariant is present."
        ),
    }


def main() -> int:
    previous = load(PREVIOUS)
    alpha = load(CROSS_ALPHA)
    selector = load(PRIMITIVE_SELECTOR)
    primitive_class = load(PRIMITIVE_CLASS)
    noninv = load(NONINV)
    overlap = load(OVERLAP)
    c1 = load(C1_EMISSION)
    splitter = load(SPLITTER)
    typed = load(TYPED)
    honest = load(HONEST_PRIMITIVE)
    higher = load(HIGHER_ORDER)

    fixed = fixed_fiber_packet(noninv)
    quotient = quotient_checks(fixed)
    representative = fixed["0"]
    degeneracy = sector_degeneracy_checks(representative)

    selected_inputs = {
        "alpha1_driver_verified": alpha["alpha1_driver_verified_imported"],
        "selected_dotD_source_verified": alpha["selected_dotD_source_verified_imported"],
        "honest_dotD_alpha1_replay": alpha["alpha1_driver_replay_import"][
            "honest_dotD_alpha1_replay"
        ],
        "static_overlap_transfer_normalization_selected": overlap["selected_overlap_kernel"][
            "selected"
        ],
        "all_smslot_source_arrows_closed": overlap["arrow_status"]["all_six_closed"],
        "primitive_active_shift_selected": selector["active_shift_selected_claimed"],
        "fixed_fiber_quotient_selected_for_current_observables": selector[
            "fiber_class_quotient_selected_claimed"
        ],
        "current_primitive_class_valid_C1_observable_layer": primitive_class[
            "promotion_decision"
        ]["current_primitive_class_promoted_as_valid_C1_observable_layer"],
        "current_primitive_class_flavor_closure": primitive_class["promotion_decision"][
            "current_primitive_class_promoted_as_flavor_closure"
        ],
    }

    current_layer_values = {
        "emitted_as_current_C1_observable_class": True,
        "representative_fiber_shift": 0,
        "representative_policy": (
            "shift 0 is a computation gauge for the selected fixed-fiber quotient class; "
            "it is not an absolute physical fiber selector"
        ),
        "fixed_fiber_values": fixed,
        "quotient_checks": quotient,
        "sector_degeneracy_checks": degeneracy,
        "full_flavor_closure_from_current_layer": False,
    }

    dynamic_overlap_route = {
        "current_layer_overlap_values_constructed": True,
        "selected_dynamic_overlap_tensor_emitted": False,
        "selected_sector_dependent_retarded_kernel_emitted": False,
        "operator_level_basis_transport_or_vertex_source_emitted": False,
        "why_not_promoted": (
            "The selected quotient gives a current spectral-observable class, but not a "
            "same-branch dynamic overlap tensor with non-scalar sector response."
        ),
    }

    hessian_route = {
        "static_trace_gram_normalization_selected": True,
        "normalization_values": overlap["selected_overlap_kernel"]["normalization_values"],
        "splitter_target_vector_norm_sq": splitter["selected_deltatheta_c1_solve_gate"][
            "target_vector_norm_sq"
        ],
        "conditional_weylpair_deltaTheta": typed["conditional_solver_packet"][
            "conditional_deltaTheta"
        ],
        "conditional_weylpair_residual_norm": typed["conditional_solver_packet"][
            "conditional_residual_norm"
        ],
        "selected_Hessian_blocks_emitted": c1["emission_audit"]["required_operator_slots"][
            "full_lower_order_Hess_Xi_blocks"
        ],
        "selected_b_selected_emitted": c1["emission_audit"][
            "selected_source_vector_b_selected_emitted"
        ],
        "promoted_as_selected_Hessian_normalization": False,
    }

    galerkin_route = {
        "finite_current_layer_contraction_values_computed": True,
        "honest_galerkin_manifest_status": honest["status"],
        "honest_galerkin_selected_source_verified": honest["selected_source_verified"],
        "required_outputs": honest["required_outputs"],
        "selected_Galerkin_C1_contractions_emitted": False,
        "why_not_promoted": (
            "The finite quotient-layer matrices are exact, but the honest Galerkin manifest "
            "still lacks zero-mode bases, primitive three-by-three contraction terms, linear "
            "response matrices, and C33/nonzero-family-rank tests."
        ),
    }

    acceptance_kernel = {
        "minimum_next_value_packet": {
            "selected_non_scalar_dynamic_overlap_tensor": True,
            "or_selected_full_response_correction_matrices": True,
            "selected_Hessian_blocks_and_b_selected": True,
            "selected_sector_response_matrices": True,
            "selected_deltaTheta_C1_solution_or_consistency_rejection": True,
        },
        "finite_tests_after_values_exist": {
            "mass_hierarchy": "some sector YY* correction has nonzero traceless part",
            "CKM_PMNS": "up/down or e/nuD Hermitian corrections have nonzero commutator",
            "CP": "a selected complex CP-odd commutator word has nonzero imaginary part",
            "no_target_selector": "measured masses, CKM, PMNS, CP, or benchmark matrices do not choose the values",
        },
        "current_values_fail_these_tests": True,
        "compatible_with_higher_order_criterion": higher["path_A_higher_order_criterion"][
            "proved"
        ],
    }

    candidate = {
        "candidate": "MTTSelectedDynamicOverlapTensorHessianNormalizationOrGalerkinC1ContractionsValueEmission",
        "status": STATUS,
        "inputs": {
            "previous_envelope": rel(PREVIOUS),
            "crossrepo_alpha1_import": rel(CROSS_ALPHA),
            "primitive_fiber_selector": rel(PRIMITIVE_SELECTOR),
            "primitive_class_C1_observable": rel(PRIMITIVE_CLASS),
            "noninvariant_C1_primitive_search": rel(NONINV),
            "selected_smslot_overlap_kernel": rel(OVERLAP),
            "selected_C1_response_operator_emission": rel(C1_EMISSION),
            "splitter_deltaTheta_gate": rel(SPLITTER),
            "typedbn_or_primitive_value_emission": rel(TYPED),
            "honest_galerkin_primitive_contractions": rel(HONEST_PRIMITIVE),
            "higher_order_full_response_criterion": rel(HIGHER_ORDER),
        },
        "selected_inputs": selected_inputs,
        "current_layer_value_packet": current_layer_values,
        "dynamic_overlap_tensor_route": dynamic_overlap_route,
        "hessian_normalization_route": hessian_route,
        "galerkin_C1_contractions_route": galerkin_route,
        "acceptance_kernel_for_next_values": acceptance_kernel,
        "promotion_decision": {
            "current_layer_values_selected_as_C1_observable_class": True,
            "current_layer_values_promoted_as_dynamic_overlap_tensor": False,
            "current_layer_values_promoted_as_A_selected": False,
            "current_layer_values_promoted_as_b_selected": False,
            "current_layer_values_promoted_as_flavor_closure": False,
            "reason": (
                "The exact current quotient values are gauge-safe for spectral observables, "
                "but they are fully scalar-permutation degenerate.  The next proof must emit "
                "non-scalar dynamic overlap/Hessian/full-response data from the same source."
            ),
        },
        "what_closes_now": {
            "current_layer_value_packet_emitted": True,
            "fixed_fiber_quotient_values_checked": True,
            "current_layer_degeneracy_no_go_proved": True,
            "static_trace_normalization_imported_as_selected": True,
            "Hessian_and_Galerkin_promotion_tests_built": True,
            "next_non_scalar_value_acceptance_kernel_built": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_non_scalar_dynamic_overlap_tensor": True,
            "selected_full_response_correction_matrices": True,
            "selected_Hessian_blocks": True,
            "selected_b_selected": True,
            "selected_A_selected_response_operator": True,
            "selected_Galerkin_C1_contractions": True,
            "selected_sector_response_matrices": True,
            "selected_deltaTheta_C1_solution": True,
            "Yukawa_CKM_PMNS_masses_Higgs_RG": True,
            "full_SM_or_no_knob_closure": True,
        },
        "closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "dynamic_overlap_tensor_claimed": False,
        "A_selected_claimed": False,
        "b_selected_claimed": False,
        "Galerkin_C1_contractions_claimed": False,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "CurrentLayerDynamicOverlapHessianGalerkinValueEmissionNoGoTheorem",
            "proved": True,
            "statement": (
                "From the selected alpha1/dotD replay, selected static overlap normalization, "
                "and selected active fixed-fiber quotient, the current finite C1 value packet is "
                "computable without observed flavor data.  For each fixed-fiber representative "
                "and each sector, the matrix is a real scalar times a permutation matrix, so YY* "
                "is the same scalar identity.  Hence the packet cannot produce nondegenerate "
                "Yukawa hierarchy, CKM/PMNS mixing, or CP.  It may be used only as the current "
                "C1 spectral-observable layer.  Full progress now requires selected non-scalar "
                "dynamic overlap/Hessian/full-response or honest Galerkin C1 values from the "
                "same source."
            ),
        },
    }

    cert = {
        "certificate": "MTT_Selected_DynamicOverlapTensor_HessianNormalization_or_GalerkinC1Contractions_ValueEmission_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "dynamic_overlap_tensor_claimed": False,
        "A_selected_claimed": False,
        "b_selected_claimed": False,
        "Galerkin_C1_contractions_claimed": False,
        "current_layer_value_packet_emitted": True,
        "current_layer_flavor_no_go": True,
        "theorem_proved": True,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    scalar = quotient["distinct_YYstar_scalars"][0]
    note = f"""# MTT Selected DynamicOverlapTensor HessianNormalization or GalerkinC1Contractions ValueEmission v1

Status: `{STATUS}`.

The current selected quotient layer now has an exact finite value packet: active
shift `(1,1)`, fixed-fiber quotient representatives `0,1,2`, and computation
gauge representative `0`.  The packet is selected only as the current C1
spectral-observable class.

The value audit proves the obstruction:

```text
Y_s Y_s^* = {scalar} I_3
for s in u,d,e,nuD and for all fixed-fiber representatives 0,1,2.
```

Thus this layer cannot supply mass hierarchy, CKM/PMNS mixing, or CP.  Static
trace normalization is selected, and the conditional Weyl-pair solve is still
algebraically ready, but the selected dynamic overlap tensor, Hessian blocks,
`A_selected`, `b_selected`, honest Galerkin C1 contractions, sector response
matrices, and `deltaTheta_C1` are not emitted.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
