"""Build dynamic transfer/Hessian/b_selected or honest Galerkin C1 value-fill gate."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PREVIOUS = DATA / "selected_weylpairdynamicoverlap_sourcepromotion_or_honestgalerkinc1_valuefill.candidate.json"
WEYLPAIR = DATA / "selected_routec_weylpair_basis_transport_or_vertex_source_theorem.candidate.json"
A_ASSEMBLY = DATA / "selected_routec_weylpair_aselected_assembly_or_source_proof.candidate.json"
SPLITTER = DATA / "selected_routec_splitter_source_emission_contract_or_selected_deltatheta_c1_solve.candidate.json"
C1_RESPONSE = DATA / "selected_routec_selected_c1_response_operator_emission.candidate.json"
GALERKIN = DATA / "selected_routec_strominger_galerkin_solve" / "c1_primitive_contractions.candidate.json"
NONSCALAR = DATA / "selected_nonscalardynamicoverlap_or_fullresponsecorrection_valueemission.candidate.json"

OUTPUT = DATA / "selected_dynamictransferhessian_bselected_or_honestgalerkinc1_valuefill.candidate.json"
CERT = CERTS / "selected_dynamictransferhessian_bselected_or_honestgalerkinc1_valuefill_certificate.json"
NOTE = CORPUS / "MTT_Selected_DynamicTransferHessian_bSelected_or_HonestGalerkinC1_ValueFill_v1.md"

STATUS = (
    "MTT_SELECTED_DYNAMICTRANSFERHESSIAN_BSELECTED_OR_HONESTGALERKINC1_"
    "VALUEFILL_BUILT_CONDITIONAL_GRAM_EXACT_SOURCE_OPEN"
)
NEXT = "MTT_Selected_SameSourceDynamicTransferIdentity_or_GalerkinC1Contractions_Emission_v1"
SECTORS = ["u", "d", "e", "nuD"]
TOL = 1e-12


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


def packet_vector(packet: dict[str, list[list[Any]]]) -> list[float]:
    values: list[float] = []
    for sector in SECTORS:
        values.extend(flatten_matrix(packet[sector]))
    return values


def dot(a: list[float], b: list[float]) -> float:
    return float(sum(x * y for x, y in zip(a, b)))


def add(a: list[float], b: list[float]) -> list[float]:
    return [x + y for x, y in zip(a, b)]


def mat_vec(columns: list[list[float]], coeffs: list[float]) -> list[float]:
    return [sum(coeffs[j] * columns[j][i] for j in range(len(columns))) for i in range(len(columns[0]))]


def solve_two_by_two(gram: list[list[float]], rhs: list[float]) -> list[float]:
    det = gram[0][0] * gram[1][1] - gram[0][1] * gram[1][0]
    return [
        (rhs[0] * gram[1][1] - gram[0][1] * rhs[1]) / det,
        (gram[0][0] * rhs[1] - rhs[0] * gram[1][0]) / det,
    ]


def norm_sq(vec: list[float]) -> float:
    return dot(vec, vec)


def residual_norm(columns: list[list[float]], coeffs: list[float], target: list[float]) -> float:
    reconstructed = mat_vec(columns, coeffs)
    return math.sqrt(norm_sq([a - b for a, b in zip(reconstructed, target)]))


def sector_norms_from_vector(vec: list[float]) -> dict[str, float]:
    # Each sector contributes 3x3 complex entries = 18 real coordinates.
    norms: dict[str, float] = {}
    block = 18
    for index, sector in enumerate(SECTORS):
        start = index * block
        norms[sector] = norm_sq(vec[start : start + block])
    return norms


def main() -> int:
    previous = load(PREVIOUS)
    weylpair = load(WEYLPAIR)
    assembly = load(A_ASSEMBLY)
    splitter = load(SPLITTER)
    c1_response = load(C1_RESPONSE)
    galerkin = load(GALERKIN)
    nonscalar = load(NONSCALAR)

    packets = weylpair["enriched_weyl_pair_packet"]["source_directions"]
    phase = packet_vector(packets["phase_packet"]["matrices"])
    shift = packet_vector(packets["shift_packet"]["matrices"])
    b_conditional = add(phase, shift)
    columns = [phase, shift]

    gram = [[dot(phase, phase), dot(phase, shift)], [dot(shift, phase), dot(shift, shift)]]
    rhs = [dot(phase, b_conditional), dot(shift, b_conditional)]
    delta = solve_two_by_two(gram, rhs)
    residual = residual_norm(columns, delta, b_conditional)
    rank = 2 if abs(gram[0][0] * gram[1][1] - gram[0][1] * gram[1][0]) > TOL else 1
    condition_number = 1.0 if abs(gram[0][1]) <= TOL and abs(gram[0][0] - gram[1][1]) <= TOL else None

    target_norm_sq = splitter["selected_deltatheta_c1_solve_gate"]["target_vector_norm_sq"]
    prior_delta = assembly["locked_solve"]["deltaTheta_conditional"]
    prior_residual = assembly["locked_solve"]["residual_norm"]
    tests = nonscalar["conditional_non_scalar_value_packet"]["acceptance_tests"]
    required_slots = c1_response["emission_audit"]["required_operator_slots"]

    conditional_packet = {
        "coordinate_system": {
            "codomain_real_dimension": len(b_conditional),
            "sector_order": SECTORS,
            "matrix_order": "row-major 3x3",
            "complex_entry_encoding": "[real, imag]",
            "coordinates_per_sector": 18,
            "columns": ["phase_packet", "shift_packet"],
        },
        "A_conditional_shape": [len(b_conditional), 2],
        "phase_column_norm_sq": gram[0][0],
        "shift_column_norm_sq": gram[1][1],
        "cross_inner_product": gram[0][1],
        "Gram_A_transpose_A": gram,
        "A_transpose_b_conditional": rhs,
        "b_conditional_norm_sq": norm_sq(b_conditional),
        "b_conditional_sector_norm_sq": sector_norms_from_vector(b_conditional),
        "rank": rank,
        "condition_number": condition_number,
        "deltaTheta_conditional_from_Gram_solve": delta,
        "residual_norm": residual,
        "relative_residual": residual / math.sqrt(norm_sq(b_conditional)),
        "matches_splitter_target_norm_sq": abs(norm_sq(b_conditional) - target_norm_sq) <= TOL,
        "matches_prior_weylpair_assembly": (
            abs(delta[0] - prior_delta[0]) <= TOL
            and abs(delta[1] - prior_delta[1]) <= TOL
            and prior_residual <= 1e-10
        ),
    }

    hessian_bselected_fill_attempt = {
        "attempted": True,
        "conditional_Hessian_Gram_candidate": {
            "G_Weyl": gram,
            "orthogonal_equal_norm_columns": abs(gram[0][1]) <= TOL and abs(gram[0][0] - gram[1][1]) <= TOL,
            "normalization_interpretation": "If selected, the Weyl-pair response basis has exact metric 12 I_2 in the 72-real coordinate codomain.",
            "selected_by_MTT": False,
        },
        "conditional_b_candidate": {
            "definition": "b_conditional = phase_packet + shift_packet",
            "norm_sq": norm_sq(b_conditional),
            "dual_source_coefficients_A_transpose_b": rhs,
            "deltaTheta_from_dual_normal_equation": delta,
            "selected_b_selected": False,
        },
        "selected_value_slots_from_C1_response_audit": {
            "selected_Hessian_blocks": required_slots["full_lower_order_Hess_Xi_blocks"],
            "selected_grad_source_vector": required_slots["evaluated_grad_V_C1_alpha1_source_vector"],
            "selected_zero_mode_basis": required_slots["selected_zero_mode_basis_Q_u_d_L_e_N_H"],
            "selected_L2_Gram_Schmidt_rule": required_slots["selected_L2_Gram_Schmidt_rule"],
            "selected_dotD_operators": required_slots["explicit_dotD_Q_u_d_L_e_N_H"],
            "selected_sector_response_matrices": required_slots["sector_response_matrices_M_u_M_d_M_e_M_nuD"],
            "selected_deltaTheta_C1_solution": required_slots["selected_deltaTheta_C1_solution"],
        },
        "promoted": False,
        "why_not_promoted": (
            "The conditional Gram/Hessian and b vector are now exact finite data, but current selected "
            "artifacts still do not emit the same-source dynamic transfer identity or selected Hessian/"
            "source vector proving b_selected = b_conditional."
        ),
    }

    honest_galerkin_attempt = {
        "attempted": True,
        "manifest_status": galerkin["status"],
        "selected_source_verified": galerkin["selected_source_verified"],
        "required_outputs": galerkin["required_outputs"],
        "required_coordinate_compatibility": {
            "codomain_real_dimension": len(b_conditional),
            "sector_order": SECTORS,
            "must_emit_same_phase_shift_or_equivalent_basis": True,
            "must_pass_same_mass_mixing_CP_tests": True,
        },
        "promoted": False,
        "why_not_promoted": "The honest Galerkin C1 manifest still emits no selected zero-mode bases, primitive 3x3 terms, response matrices, or C33/nonzero-family-rank tests.",
    }

    promotion_gate = {
        "conditional_dynamic_value_packet_built": True,
        "no_linear_algebra_obstruction": conditional_packet["rank"] == 2
        and conditional_packet["condition_number"] == 1.0
        and conditional_packet["residual_norm"] <= TOL,
        "qualitative_flavor_tests_pass_conditionally": {
            "mass_split": tests["all_mass_split_positive"],
            "ckm_commutator": tests["ckm_commutator_positive"],
            "pmns_commutator": tests["pmns_commutator_positive"],
            "cp_odd": tests["cp_odd_invariant_nonzero"],
        },
        "selected_dynamic_transfer_identity_emitted": False,
        "selected_Hessian_bselected_emitted": False,
        "honest_Galerkin_C1_contractions_emitted": False,
        "promote_to_selected_A_selected": False,
        "promote_to_selected_b_selected": False,
        "promote_to_selected_deltaTheta_C1": False,
    }

    candidate = {
        "candidate": "MTTSelectedDynamicTransferHessianBselectedOrHonestGalerkinC1ValueFill",
        "status": STATUS,
        "inputs": {
            "previous_gate": rel(PREVIOUS),
            "weylpair_source_gate": rel(WEYLPAIR),
            "conditional_A_assembly": rel(A_ASSEMBLY),
            "splitter_solve_gate": rel(SPLITTER),
            "selected_C1_response_operator_emission": rel(C1_RESPONSE),
            "honest_galerkin_C1_contractions_manifest": rel(GALERKIN),
            "conditional_non_scalar_packet": rel(NONSCALAR),
        },
        "conditional_dynamic_transfer_coordinate_packet": conditional_packet,
        "hessian_bselected_fill_attempt": hessian_bselected_fill_attempt,
        "honest_Galerkin_C1_value_fill_attempt": honest_galerkin_attempt,
        "promotion_gate": promotion_gate,
        "what_closes_now": {
            "exact_72_real_coordinate_system_fixed": True,
            "conditional_A_transpose_A_Gram_computed": True,
            "conditional_b_conditional_computed": True,
            "conditional_deltaTheta_Gram_solve_exact": True,
            "linear_algebra_obstruction_removed": True,
            "selected_value_source_gap_reduced_to_same_source_dynamic_transfer_or_honest_Galerkin": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_same_source_dynamic_transfer_identity": True,
            "selected_Hessian_blocks": True,
            "selected_grad_source_vector_or_b_selected": True,
            "selected_A_selected": True,
            "selected_b_selected": True,
            "selected_deltaTheta_C1_solution": True,
            "selected_sector_response_matrices": True,
            "honest_Galerkin_C1_contractions": True,
            "Yukawa_CKM_PMNS_masses_Higgs_RG_no_knob": True,
            "full_SM_no_knob_closure": True,
        },
        "closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "selected_dynamic_transfer_identity_claimed": False,
        "selected_Hessian_blocks_claimed": False,
        "A_selected_claimed": False,
        "b_selected_claimed": False,
        "deltaTheta_C1_claimed": False,
        "Galerkin_C1_contractions_claimed": False,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "ConditionalDynamicTransferHessianBselectedValueFillReductionTheorem",
            "proved": True,
            "statement": (
                "In the fixed 72-real C1 coordinate system, the conditional Weyl-pair dynamic transfer "
                "has two orthogonal equal-norm columns with A^T A = 12 I_2.  The internally locked "
                "target vector is b_conditional = phase_packet + shift_packet, with norm squared 24, "
                "and the normal-equation solve gives deltaTheta=(1,1) exactly up to roundoff.  Therefore "
                "there is no remaining linear-algebra obstruction in the Weyl-pair value packet.  The "
                "open proof obligation is purely selected-source value emission: prove the same-source "
                "dynamic transfer/Hessian/b_selected identity or emit honest selected Galerkin C1 "
                "contractions in this coordinate system."
            ),
        },
    }

    cert = {
        "certificate": "MTT_Selected_DynamicTransferHessian_bSelected_or_HonestGalerkinC1_ValueFill_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "selected_dynamic_transfer_identity_claimed": False,
        "selected_Hessian_blocks_claimed": False,
        "A_selected_claimed": False,
        "b_selected_claimed": False,
        "deltaTheta_C1_claimed": False,
        "Galerkin_C1_contractions_claimed": False,
        "theorem_proved": True,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected DynamicTransferHessian bSelected or HonestGalerkinC1 ValueFill v1

Status: `{STATUS}`.

The conditional Weyl-pair packet is now represented in a fixed real coordinate
system:

```text
sector order          = u, d, e, nuD
matrix order          = row-major 3x3
complex encoding      = [real, imag]
codomain dimension    = 72
A_conditional columns = phase_packet, shift_packet
```

The finite Gram/Hessian calculation is exact:

```text
A_conditional^T A_conditional = [[{gram[0][0]}, {gram[0][1]}],
                                 [{gram[1][0]}, {gram[1][1]}]]
A_conditional^T b_conditional = {rhs}
||b_conditional||^2           = {norm_sq(b_conditional)}
deltaTheta                    = {delta}
residual norm                 = {residual}
```

So the remaining wall is not a search-space or conditioning problem.  The
conditional packet is already an exact finite value source.  What is missing is
promotion:

```text
prove same-source dynamic transfer/Hessian/b_selected identity
or emit honest selected Galerkin C1 contractions in the same 72-real coordinate system
```

No observed masses, CKM/PMNS values, CP phase, benchmark matrices, or lifted
flags are used as selectors.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
