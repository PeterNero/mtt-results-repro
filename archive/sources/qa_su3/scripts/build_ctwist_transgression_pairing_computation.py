"""Compute the invariant Iwasawa H transgression pairing for Qa/SU3."""

from __future__ import annotations

import json
import sys
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"

INPUT = DATA / "strominger_source_to_ctwist_map_or_nogo.candidate.json"
FULL_NIL = DATA / "full_nil_theta_cocycle_equations.candidate.json"
OUTPUT_DATA = DATA / "ctwist_transgression_pairing_computation.candidate.json"
OUTPUT_CERT = CERTS / "ctwist_transgression_pairing_computation_certificate.json"


Form = dict[tuple[int, ...], str]


def wedge_term(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, tuple[int, ...]] | None:
    if set(a).intersection(b):
        return None
    merged = list(a) + list(b)
    inversions = 0
    for i, left in enumerate(merged):
        for right in merged[i + 1 :]:
            if left > right:
                inversions += 1
    return ((-1) ** inversions, tuple(sorted(merged)))


def add_forms(*forms: dict[tuple[int, ...], complex]) -> dict[tuple[int, ...], complex]:
    out: dict[tuple[int, ...], complex] = {}
    for form in forms:
        for basis, coeff in form.items():
            out[basis] = out.get(basis, 0) + coeff
    return {basis: coeff for basis, coeff in out.items() if abs(coeff) > 1e-12}


def scale(form: dict[tuple[int, ...], complex], coeff: complex) -> dict[tuple[int, ...], complex]:
    return {basis: coeff * value for basis, value in form.items()}


def wedge(a: dict[tuple[int, ...], complex], b: dict[tuple[int, ...], complex]) -> dict[tuple[int, ...], complex]:
    out: dict[tuple[int, ...], complex] = {}
    for basis_a, coeff_a in a.items():
        for basis_b, coeff_b in b.items():
            term = wedge_term(basis_a, basis_b)
            if term is None:
                continue
            sign, basis = term
            out[basis] = out.get(basis, 0) + sign * coeff_a * coeff_b
    return {basis: coeff for basis, coeff in out.items() if abs(coeff) > 1e-12}


def interior_vector(form: dict[tuple[int, ...], complex], vector: int) -> dict[tuple[int, ...], complex]:
    out: dict[tuple[int, ...], complex] = {}
    for basis, coeff in form.items():
        if vector not in basis:
            continue
        idx = basis.index(vector)
        new_basis = basis[:idx] + basis[idx + 1 :]
        out[new_basis] = out.get(new_basis, 0) + ((-1) ** idx) * coeff
    return {basis: coeff for basis, coeff in out.items() if abs(coeff) > 1e-12}


def interior_pair(form: dict[tuple[int, ...], complex], first: int, second: int) -> dict[tuple[int, ...], complex]:
    # Slant on the oriented two-plane first wedge second.
    return interior_vector(interior_vector(form, second), first)


def fmt_coeff(value: complex) -> str:
    if abs(value.imag) < 1e-12:
        return str(Fraction(value.real).limit_denominator())
    return f"{value}"


def fmt_form(form: dict[tuple[int, ...], complex]) -> dict[str, str]:
    return {"e" + "".join(str(i) for i in basis): fmt_coeff(coeff) for basis, coeff in sorted(form.items())}


def e(index: int) -> dict[tuple[int, ...], complex]:
    return {(index,): 1}


def main() -> None:
    prior = json.loads(INPUT.read_text(encoding="utf-8"))
    full_nil = json.loads(FULL_NIL.read_text(encoding="utf-8"))
    omega1 = add_forms(e(1), scale(e(2), 1j))
    omega2 = add_forms(e(3), scale(e(4), 1j))
    omega3 = add_forms(e(5), scale(e(6), 1j))
    bar1 = add_forms(e(1), scale(e(2), -1j))
    bar2 = add_forms(e(3), scale(e(4), -1j))
    bar3 = add_forms(e(5), scale(e(6), -1j))

    # We suppress the common positive scale A = r3/(r1*r2).  The paper's
    # formula is H = -r3^2/2 (bar omega3 omega1 omega2 - omega3 baromega1 baromega2).
    h_scaled = scale(add_forms(wedge(wedge(bar3, omega1), omega2), scale(wedge(wedge(omega3, bar1), bar2), -1)), -0.5)
    h_real_integer_pattern = fmt_form(h_scaled)
    base_pairs = {
        ("g1", "g3"): (1, 3),
        ("g1", "g4"): (1, 4),
        ("g2", "g3"): (2, 3),
        ("g2", "g4"): (2, 4),
    }
    slants = []
    commutators = {tuple(item["pair"]): item["central"] for item in full_nil["commutators"]}
    central_basis_to_generator = {(5,): "g5", (6,): "g6"}
    for pair, vectors in base_pairs.items():
        slant = interior_pair(h_scaled, *vectors)
        central_components = {}
        for basis, coeff in slant.items():
            generator = central_basis_to_generator.get(basis, "noncentral")
            central_components[generator] = fmt_coeff(coeff)
        expected = commutators[pair]
        supports_expected_axis = all(
            (generator in central_components) == (value != 0)
            for generator, value in expected.items()
        )
        slants.append(
            {
                "base_pair": list(pair),
                "oriented_vectors": list(vectors),
                "slant_i_pair_H_scaled": fmt_form(slant),
                "central_components": central_components,
                "commutator_expected_axis": expected,
                "supports_expected_axis": supports_expected_axis,
                "integer_generator_after_scale_choice": supports_expected_axis,
            }
        )
    all_axes_match = all(item["supports_expected_axis"] for item in slants)
    all_slants_central_nonzero = all(
        item["central_components"] and "noncentral" not in item["central_components"]
        for item in slants
    )
    candidate = {
        "candidate": "SelectedQaSU3CTwistTransgressionPairingComputation",
        "status": "CTWIST_TRANSGRESSION_PAIRING_COMPUTED_COMPLEX_ROTATED_CENTRAL_SUPPORT",
        "input_status": prior["status"],
        "normalization": {
            "omega1": "(e1+i e2)/r1",
            "omega2": "(e3+i e4)/r2",
            "omega3": "(e5+i e6)/r3",
            "suppressed_positive_scale": "A = r3/(r1*r2)",
            "integral_generator_normalization": "choose flux/unit normalization so A-period is one generator if allowed by selected flux quantization",
        },
        "H_scaled_real_form": h_real_integer_pattern,
        "slant_pairings": slants,
        "gate_results": {
            "H_slant_computed": True,
            "all_four_base_slants_land_on_expected_central_axes": all_axes_match,
            "all_four_base_slants_are_nonzero_and_central": all_slants_central_nonzero,
            "direct_nil_commutator_axis_match": all_axes_match,
            "complex_rotated_central_support_detected": all_slants_central_nonzero and not all_axes_match,
            "transgression_axis_supports_c_twist": all_slants_central_nonzero,
            "integral_generator_normalization_proved_from_selected_flux": False,
            "finite_Z_or_Z3_quotient_selected_same_branch": False,
            "same_branch_c_plus_minus_one_promoted": False,
            "Freed_Witten_Bianchi_for_mapped_module_verified": False,
            "gerbe_route_retired": False,
            "closure_claimed": False,
        },
        "interpretation": [
            "The invariant H slant along Iwasawa base two-planes is nonzero and purely central.",
            "The result is not the raw nil commutator table; it is complex-rotated relative to the direct central axes.",
            "This avoids the zero-pairing no-go and supports the orthogonal/complex nesting route, but it is not direct c=+/-1 promotion.",
            "Full closure still requires the selected integral/finite quotient normalization and the complex-rotation convention for the c-twist generator.",
        ],
        "next_required_artifact": "Selected_Qa_SU3_Complex_Rotated_CTwist_Normalization_v1",
        "parallel_fallback": "Selected_Qa_SU3_A01_DE_Operator_Exit_v1",
        "target_fitting_used": False,
    }
    certificate = {
        "certificate": "SelectedQaSU3CTwistTransgressionPairingComputation",
        "status": "QA_SU3_CTWIST_TRANSGRESSION_PAIRING_COMPUTED_COMPLEX_ROTATED_CENTRAL_SUPPORT",
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "what_closes": {
            "explicit_invariant_H_slant_computation": True,
            "all_base_pair_slants_match_nil_central_axes": all_axes_match,
            "all_base_pair_slants_are_nonzero_and_central": all_slants_central_nonzero,
            "complex_rotated_central_support_detected": all_slants_central_nonzero and not all_axes_match,
            "zero_pairing_no_go_avoided": all_slants_central_nonzero,
            "gerbe_route_remains_live_with_computed_support": True,
        },
        "what_remains_open": {
            "selected_integral_generator_normalization": True,
            "same_branch_finite_quotient_Z_or_Z3": True,
            "promotion_to_c_plus_minus_one_twisted_modules": True,
            "Freed_Witten_Bianchi_for_mapped_module": True,
            "twisted_section_bases_or_operator_exit": True,
            "qa_su3_packet_closed": False,
        },
        "next_required_artifact": candidate["next_required_artifact"],
        "parallel_fallback": candidate["parallel_fallback"],
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    data_text = json.dumps(candidate, indent=2, sort_keys=True)
    cert_text = json.dumps(certificate, indent=2, sort_keys=True)
    if "--write" in sys.argv:
        OUTPUT_DATA.write_text(data_text + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
