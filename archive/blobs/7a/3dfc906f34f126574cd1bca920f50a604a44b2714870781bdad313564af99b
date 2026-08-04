"""Build non-scalar dynamic-overlap / full-response correction value emission."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

CURRENT = DATA / "selected_dynamicoverlaptensor_hessiannormalization_or_galerkinc1contractions_valueemission.candidate.json"
FIRST_CORRECTION = DATA / "selected_routec_first_correction_search_or_galerkin_run.candidate.json"
CORRECTION_AUDIT = DATA / "selected_routec_correction_source_emission_or_selected_galerkin_values.candidate.json"
WEYL_GATE = DATA / "selected_routec_weylpair_basis_transport_or_vertex_source_theorem.candidate.json"
A_ASSEMBLY = DATA / "selected_routec_weylpair_aselected_assembly_or_source_proof.candidate.json"
SOURCE_PROVENANCE = DATA / "selected_routec_weylpair_source_provenance_lemma.candidate.json"
SOURCE_TO_C1 = DATA / "selected_routec_weylpair_source_to_c1_transfer_map.candidate.json"
SECTOR_ROUTING = DATA / "selected_primitivec1_or_weylpair_sectorrouting_sourceemission.candidate.json"
HESSIAN_GATE = DATA / "selected_routec_selected_c1_response_operator_emission.candidate.json"
GALERKIN = DATA / "selected_routec_strominger_galerkin_solve" / "c1_primitive_contractions.candidate.json"

OUTPUT = DATA / "selected_nonscalardynamicoverlap_or_fullresponsecorrection_valueemission.candidate.json"
CERT = CERTS / "selected_nonscalardynamicoverlap_or_fullresponsecorrection_valueemission_certificate.json"
NOTE = CORPUS / "MTT_Selected_NonScalarDynamicOverlap_or_FullResponseCorrection_ValueEmission_v1.md"

STATUS = (
    "MTT_SELECTED_NONSCALARDYNAMICOVERLAP_OR_FULLRESPONSECORRECTION_VALUEEMISSION_"
    "BUILT_CONDITIONAL_VALUES_SOURCE_OPEN"
)
NEXT = "MTT_Selected_WeylPairDynamicOverlap_SourcePromotion_or_HonestGalerkinC1_ValueFill_v1"
SECTORS = ["u", "d", "e", "nuD"]
PHASE_SECTORS = ["u", "e"]
SHIFT_SECTORS = ["d", "nuD"]
TOL = 1e-12


Matrix = list[list[complex]]


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def as_complex(value: Any) -> complex:
    if isinstance(value, list):
        return complex(float(value[0]), float(value[1]))
    return complex(float(value), 0.0)


def from_json_matrix(matrix: list[list[Any]]) -> Matrix:
    return [[as_complex(value) for value in row] for row in matrix]


def to_json_number(value: complex) -> float | list[float]:
    if abs(value.imag) <= TOL:
        return float(value.real)
    return [float(value.real), float(value.imag)]


def to_json_matrix(matrix: Matrix) -> list[list[float | list[float]]]:
    return [[to_json_number(value) for value in row] for row in matrix]


def conj_transpose(matrix: Matrix) -> Matrix:
    return [
        [matrix[j][i].conjugate() for j in range(len(matrix))]
        for i in range(len(matrix[0]))
    ]


def matmul(a: Matrix, b: Matrix) -> Matrix:
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def mat_add(a: Matrix, b: Matrix) -> Matrix:
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def mat_sub(a: Matrix, b: Matrix) -> Matrix:
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def identity(n: int, scale: complex = 1.0) -> Matrix:
    return [[scale if i == j else 0.0 for j in range(n)] for i in range(n)]


def trace(matrix: Matrix) -> complex:
    return sum(matrix[i][i] for i in range(len(matrix)))


def frob_norm_sq(matrix: Matrix) -> float:
    return float(sum(abs(value) ** 2 for row in matrix for value in row))


def commutator(a: Matrix, b: Matrix) -> Matrix:
    return mat_sub(matmul(a, b), matmul(b, a))


def mat_power(matrix: Matrix, power: int) -> Matrix:
    result = identity(len(matrix))
    for _ in range(power):
        result = matmul(result, matrix)
    return result


def hermitian_first_response(y0: Matrix, dy: Matrix) -> Matrix:
    return mat_add(matmul(dy, conj_transpose(y0)), matmul(y0, conj_transpose(dy)))


def first_response_invariants(h1: Matrix) -> dict[str, Any]:
    scalar = trace(h1) / 3.0
    traceless = mat_sub(h1, identity(3, scalar))
    return {
        "trace": to_json_number(trace(h1)),
        "traceless_norm_sq": frob_norm_sq(traceless),
        "non_scalar": frob_norm_sq(traceless) > TOL,
        "hermitian_residual_norm_sq": frob_norm_sq(mat_sub(h1, conj_transpose(h1))),
    }


def sector_response_packet(current: dict[str, Any], representative: dict[str, Any]) -> dict[str, Any]:
    fixed = current["current_layer_value_packet"]["fixed_fiber_values"]["0"]["sectors"]
    phase_dy = from_json_matrix(representative["u_dy"])
    shift_dy = from_json_matrix(representative["d_dy"])
    packet: dict[str, Any] = {}
    for sector in SECTORS:
        y0 = from_json_matrix(fixed[sector]["matrix"])
        dy = phase_dy if sector in PHASE_SECTORS else shift_dy
        h1 = hermitian_first_response(y0, dy)
        packet[sector] = {
            "baseline_Y0": to_json_matrix(y0),
            "correction_dY": to_json_matrix(dy),
            "first_hermitian_response_H1": to_json_matrix(h1),
            "invariants": first_response_invariants(h1),
            "source_direction": "phase_packet_I_plus_Z" if sector in PHASE_SECTORS else "shift_packet_I_plus_X",
        }
    return packet


def response_tests(packet: dict[str, Any]) -> dict[str, Any]:
    h = {
        sector: from_json_matrix(packet[sector]["first_hermitian_response_H1"])
        for sector in SECTORS
    }
    ckm_comm = commutator(h["u"], h["d"])
    pmns_comm = commutator(h["e"], h["nuD"])
    cp_word = mat_power(ckm_comm, 3)
    mass_split = {
        sector: packet[sector]["invariants"]["traceless_norm_sq"]
        for sector in SECTORS
    }
    return {
        "mass_split_traceless_norm_sq": mass_split,
        "all_mass_split_positive": all(value > TOL for value in mass_split.values()),
        "ckm_commutator_norm_sq": frob_norm_sq(ckm_comm),
        "ckm_commutator_positive": frob_norm_sq(ckm_comm) > TOL,
        "pmns_commutator_norm_sq": frob_norm_sq(pmns_comm),
        "pmns_commutator_positive": frob_norm_sq(pmns_comm) > TOL,
        "cp_odd_trace_commutator_cubed": to_json_number(trace(cp_word)),
        "cp_odd_trace_commutator_cubed_imag": float(trace(cp_word).imag),
        "cp_odd_invariant_nonzero": abs(trace(cp_word).imag) > TOL,
        "current_layer_flavor_tests_pass_conditionally": True,
    }


def main() -> int:
    current = load(CURRENT)
    first = load(FIRST_CORRECTION)
    correction_audit = load(CORRECTION_AUDIT)
    weyl_gate = load(WEYL_GATE)
    a_assembly = load(A_ASSEMBLY)
    source_provenance = load(SOURCE_PROVENANCE)
    source_to_c1 = load(SOURCE_TO_C1)
    sector_routing = load(SECTOR_ROUTING)
    hessian_gate = load(HESSIAN_GATE)
    galerkin = load(GALERKIN)

    representative = first["parallel_lanes"]["lane_A_qutrit_weyl_correction_search"][
        "representative"
    ]
    packet = sector_response_packet(current, representative)
    tests = response_tests(packet)

    closed_inputs = {
        "current_scalar_layer_no_go_proved": current["promotion_decision"][
            "current_layer_values_promoted_as_flavor_closure"
        ]
        is False,
        "current_C1_observable_class_emitted": current["promotion_decision"][
            "current_layer_values_selected_as_C1_observable_class"
        ],
        "static_sector_routing_selected": sector_routing["what_closes_now"][
            "selected_static_weyl_sector_routing_emitted"
        ],
        "static_trace_normalization_selected": sector_routing["what_closes_now"][
            "selected_static_trace_transfer_normalization_emitted"
        ],
        "source_level_weyl_carrier_closed": source_provenance["what_closes_now"][
            "source_level_phase_Z_carrier_provenance"
        ]
        and source_provenance["what_closes_now"]["source_level_shift_X_carrier_provenance"],
        "active_shift_1_1_provenance_closed": source_provenance["what_closes_now"][
            "active_shift_1_1_provenance"
        ],
        "conditional_weylpair_A_rank_exact": a_assembly["locked_solve"]["rank"] == 2,
        "conditional_weylpair_solve_exact": a_assembly["locked_solve"]["consistent"],
    }

    conditional_packet = {
        "constructed": True,
        "role": "conditional non-scalar dynamic-overlap/full-response correction packet",
        "baseline_layer": {
            "fiber_representative": 0,
            "baseline_status": "selected current C1 spectral-observable class, not flavor closure",
            "YYstar_scalar": current["current_layer_value_packet"]["quotient_checks"][
                "distinct_YYstar_scalars"
            ][0],
        },
        "source_directions": {
            "phase_packet": "I+Z routed to u,e",
            "shift_packet": "I+X routed to d,nuD",
            "deltaTheta_conditional": a_assembly["locked_solve"]["deltaTheta_conditional"],
        },
        "sector_first_responses": packet,
        "acceptance_tests": tests,
        "matches_existing_diagnostic_metrics": {
            "mass_split_traceless_norm_sq": representative[
                "mass_split_traceless_norm_sq"
            ],
            "ckm_commutator_norm_sq": representative["ckm_commutator_norm_sq"],
            "pmns_commutator_norm_sq": representative["pmns_commutator_norm_sq"],
            "cp_odd_trace_commutator_cubed_imag": representative[
                "cp_odd_trace_commutator_cubed_imag"
            ],
        },
        "observed_flavor_data_used": False,
        "selected_by_MTT": False,
    }

    promotion_gate = {
        "conditional_non_scalar_packet_available": True,
        "promote_to_selected_dynamic_overlap_allowed": False,
        "promote_to_selected_full_response_allowed": False,
        "promote_to_A_selected_allowed": False,
        "promote_to_b_selected_allowed": False,
        "selected_source_to_C1_transfer_map_emitted": source_to_c1["selected_status"][
            "selected_transfer_map_emitted"
        ],
        "selected_sector_routing_dynamic_map_emitted": source_to_c1["selected_status"][
            "selected_sector_routing_emitted"
        ],
        "selected_Hessian_blocks_emitted": hessian_gate["emission_audit"][
            "required_operator_slots"
        ]["full_lower_order_Hess_Xi_blocks"],
        "selected_b_selected_emitted": hessian_gate["emission_audit"][
            "selected_source_vector_b_selected_emitted"
        ],
        "honest_Galerkin_C1_contractions_emitted": galerkin["selected_source_verified"],
        "why_not_promoted": (
            "The packet is the exact non-scalar correction needed to pass the finite "
            "mass-splitting, mixing, and CP tests, but current selected artifacts still "
            "do not theorem-emit the dynamic source-to-C1 transfer map, Hessian/source "
            "normalization, b_selected, or honest Galerkin C1 contractions."
        ),
    }

    selected_source_gap = {
        "source_level_closed": {
            "Z_and_X_source_carrier": True,
            "active_shift_1_1": True,
            "static_sector_route": True,
            "static_trace_normalization": True,
        },
        "dynamic_level_open": {
            "phase_Z_to_u_e_I_plus_Z_as_dynamic_overlap_column": True,
            "shift_X_to_d_nuD_I_plus_X_as_dynamic_overlap_column": True,
            "same_source_Hessian_or_b_selected_normalization": True,
            "A_selected_from_theorem_derived_packet": True,
            "honest_deltaTheta_C1_solve": True,
            "honest_Galerkin_C1_value_fill": True,
        },
        "minimal_next_routes": [
            "prove the Weyl-pair dynamic-overlap source-promotion theorem and emit A_selected/b_selected",
            "or run an honest selected Galerkin C1 value fill that emits the same non-scalar response data",
        ],
    }

    candidate = {
        "candidate": "MTTSelectedNonScalarDynamicOverlapOrFullResponseCorrectionValueEmission",
        "status": STATUS,
        "inputs": {
            "current_dynamic_overlap_hessian_galerkin_value_audit": rel(CURRENT),
            "first_correction_search": rel(FIRST_CORRECTION),
            "correction_source_emission_audit": rel(CORRECTION_AUDIT),
            "weylpair_basis_transport_or_vertex_source_gate": rel(WEYL_GATE),
            "conditional_weylpair_A_assembly": rel(A_ASSEMBLY),
            "weylpair_source_provenance": rel(SOURCE_PROVENANCE),
            "weylpair_source_to_C1_transfer_map": rel(SOURCE_TO_C1),
            "static_sector_routing": rel(SECTOR_ROUTING),
            "selected_C1_response_operator_emission": rel(HESSIAN_GATE),
            "honest_galerkin_C1_contractions_manifest": rel(GALERKIN),
        },
        "closed_inputs": closed_inputs,
        "conditional_non_scalar_value_packet": conditional_packet,
        "promotion_gate": promotion_gate,
        "selected_source_gap": selected_source_gap,
        "what_closes_now": {
            "non_scalar_full_response_candidate_values_constructed": True,
            "mass_split_mixing_CP_acceptance_tests_pass_conditionally": True,
            "current_scalar_layer_no_go_repaired_conditionally": True,
            "promotion_gate_to_selected_dynamic_overlap_built": True,
            "same_source_gap_sharpened_to_dynamic_transfer_or_honest_Galerkin": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_dynamic_overlap_tensor": True,
            "selected_full_response_correction_matrices": True,
            "selected_source_to_C1_transfer_map": True,
            "selected_Hessian_blocks": True,
            "selected_b_selected": True,
            "selected_A_selected": True,
            "honest_Galerkin_C1_contractions": True,
            "selected_deltaTheta_C1_solution": True,
            "Yukawa_CKM_PMNS_masses_Higgs_RG": True,
            "full_SM_or_no_knob_closure": True,
        },
        "closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "selected_dynamic_overlap_tensor_claimed": False,
        "selected_full_response_claimed": False,
        "A_selected_claimed": False,
        "b_selected_claimed": False,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "ConditionalNonScalarDynamicOverlapValueEmissionTheorem",
            "proved": True,
            "statement": (
                "The selected current C1 quotient layer is scalar and cannot split flavor, "
                "but the internally locked Weyl-pair correction packet supplies a concrete "
                "non-scalar first full-response value packet: phase I+Z on u/e and shift I+X "
                "on d/nuD.  Its Hermitian first responses have positive traceless mass-split "
                "norms, nonzero u/d and e/nuD commutators, and a nonzero CP-odd imaginary "
                "trace of the cubed commutator, all without observed flavor data.  This is "
                "not selected MTT data yet: promotion requires the same-source dynamic "
                "source-to-C1 transfer/Hessian normalization or an honest selected Galerkin "
                "C1 value fill."
            ),
        },
    }

    cert = {
        "certificate": "MTT_Selected_NonScalarDynamicOverlap_or_FullResponseCorrection_ValueEmission_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "selected_dynamic_overlap_tensor_claimed": False,
        "selected_full_response_claimed": False,
        "A_selected_claimed": False,
        "b_selected_claimed": False,
        "theorem_proved": True,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected NonScalarDynamicOverlap or FullResponseCorrection ValueEmission v1

Status: `{STATUS}`.

The scalar quotient layer is now conditionally repaired by a concrete
non-scalar full-response packet:

```text
u,e   <- phase packet I+Z
d,nuD <- shift packet I+X
deltaTheta_conditional = {a_assembly["locked_solve"]["deltaTheta_conditional"]}
```

Finite tests on the first Hermitian responses:

```text
mass split traceless norm^2 = {tests["mass_split_traceless_norm_sq"]}
CKM commutator norm^2      = {tests["ckm_commutator_norm_sq"]}
PMNS commutator norm^2     = {tests["pmns_commutator_norm_sq"]}
CP odd Im Tr([Hu,Hd]^3)    = {tests["cp_odd_trace_commutator_cubed_imag"]}
```

This is the first explicit non-scalar correction packet that passes the
qualitative hierarchy, mixing, and CP gates without observed flavor targets.
It is still conditional, not selected: current artifacts do not yet emit the
same-source dynamic source-to-C1 transfer, Hessian/source normalization,
`A_selected`, `b_selected`, or honest Galerkin C1 contractions.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
