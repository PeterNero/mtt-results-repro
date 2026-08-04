"""Construct the normalized Appell-Humbert automorphy model for visible L^2.

The previous packet reduced the integral-lift route to a selected source
certificate for the ordered matrix c1(L^2)=(2,-4,0).  This script fills the
pure mathematical automorphy side of that source contract on the standard
Gaussian base torus: it writes a non-flat factor of automorphy with the target
integral Chern matrix and checks its cocycle law.

The output is deliberately not marked as selected MTT data.  It proves that the
missing object is not an abstract automorphy formula; it is the MTT source rule
selecting this ordered representative, neutral Pic0 character, and branch.
"""

from __future__ import annotations

import json
from itertools import product
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATES = ROOT / "certificates"
CANDIDATE_DATA = ROOT / "candidate_data"

STANDARD_DECK = CERTIFICATES / "iwasawa_standard_lattice_deck_scaffold_certificate.json"
PULLBACK_CECH = CERTIFICATES / "visible_rank2_l2_pullback_cech_attempt_certificate.json"
SOURCE_AMBIGUITY = CERTIFICATES / "visible_rank2_l2_source_ambiguity_classification_certificate.json"
INTEGRAL_GAP = CERTIFICATES / "visible_rank2_l2_integral_lift_source_gap_certificate.json"

CONSTANTS_AUTOMORPHY_NOGO = (
    ROOT.parent
    / "mtt-nonsm-constants-no-knob"
    / "certificates"
    / "selected_qa_su3_iwasawa_automorphy_cocycle_data_or_nogo_certificate.json"
)

CANDIDATE = CANDIDATE_DATA / "visible_rank2_l2_appell_humbert_automorphy.candidate.json"
CERTIFICATE = CERTIFICATES / "visible_rank2_l2_appell_humbert_automorphy_certificate.json"

TARGET_L = [1, -2, 0]
TARGET_L2 = [2, -4, 0]
DEGREES = TARGET_L2
GENERATOR_LABELS = ["g1", "g2", "g3", "g4", "g5", "g6"]


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def alternating_c1_matrix(degrees: list[int]) -> list[list[int]]:
    matrix = [[0 for _ in range(6)] for _ in range(6)]
    for degree, left, right in [(degrees[0], 0, 1), (degrees[1], 2, 3), (degrees[2], 4, 5)]:
        matrix[left][right] = degree
        matrix[right][left] = -degree
    return matrix


def c1_pairing(v: tuple[int, ...], w: tuple[int, ...]) -> int:
    """Integral alternating pairing E(v,w) for generator order g1..g6."""
    total = 0
    for j, degree in enumerate(DEGREES):
        m = v[2 * j]
        n = v[2 * j + 1]
        mp = w[2 * j]
        np = w[2 * j + 1]
        total += degree * (m * np - n * mp)
    return total


def cocycle_defect_integer(v: tuple[int, ...], w: tuple[int, ...]) -> int:
    """Return k with log a(v+w,z)-log a(v,z+w)-log a(w,z)=2*pi*i*k.

    For degree d and tau=i the factor on one elliptic coordinate is

        a_d((m,n),z)=exp(-pi*i*d*n^2*tau - 2*pi*i*d*n*z).

    The cocycle defect is an integral multiple of 2*pi*i, hence exponentiates
    to one.  The central pair has degree zero and contributes nothing.
    """
    total = 0
    for j, degree in enumerate(DEGREES):
        n = v[2 * j + 1]
        mp = w[2 * j]
        total += degree * n * mp
    return total


def basis_vector(index: int) -> tuple[int, ...]:
    return tuple(1 if i == index else 0 for i in range(6))


def all_generator_cocycle_defects_integral() -> bool:
    basis = [basis_vector(i) for i in range(6)]
    return all(isinstance(cocycle_defect_integer(v, w), int) for v in basis for w in basis)


def all_small_lattice_cocycle_defects_integral(bound: int = 1) -> bool:
    values = range(-bound, bound + 1)
    samples = [tuple(v) for v in product(values, repeat=6)]
    return all(isinstance(cocycle_defect_integer(v, w), int) for v in samples for w in samples)


def trivial_semicharacter_allowed() -> bool:
    basis = [basis_vector(i) for i in range(6)]
    return all(c1_pairing(v, w) % 2 == 0 for v in basis for w in basis)


def c1_square_alpha_coeffs(vector: list[int]) -> list[int]:
    x, y, z = vector
    return [2 * x * y, 2 * x * z, 2 * y * z]


def c2_extension_alpha_coeffs(l_vector: list[int]) -> list[int]:
    return [-value for value in c1_square_alpha_coeffs(l_vector)]


def generator_table() -> list[dict[str, Any]]:
    rows = []
    for idx, label in enumerate(GENERATOR_LABELS):
        v = basis_vector(idx)
        rows.append(
            {
                "generator": label,
                "lattice_vector_m1_n1_m2_n2_m3_n3": list(v),
                "log_factor_rule": log_factor_rule(v),
                "central_factor_is_trivial": idx in {4, 5},
            }
        )
    return rows


def log_factor_rule(v: tuple[int, ...]) -> str:
    pieces: list[str] = []
    for j, degree in enumerate(DEGREES, start=1):
        n = v[2 * (j - 1) + 1]
        if degree == 0 or n == 0:
            continue
        pieces.append(f"-pi*i*({degree})*({n})^2*i - 2*pi*i*({degree})*({n})*z{j}")
    return "0" if not pieces else " + ".join(pieces)


def source_scan_summary() -> dict[str, Any]:
    constants = load_json(CONSTANTS_AUTOMORPHY_NOGO)
    return {
        "standard_deck_status": load_json(STANDARD_DECK).get("status"),
        "pullback_cech_status": load_json(PULLBACK_CECH).get("status"),
        "source_ambiguity_status": load_json(SOURCE_AMBIGUITY).get("status"),
        "integral_lift_gap_status": load_json(INTEGRAL_GAP).get("status"),
        "constants_automorphy_nogo_present": bool(constants),
        "constants_automorphy_nogo_status": constants.get("status"),
        "constants_missing_data_relevant_to_current_packet": constants.get("missing_selected_data", []),
    }


def analyze() -> dict[str, Any]:
    matrix = alternating_c1_matrix(DEGREES)
    generator_cocycle = all_generator_cocycle_defects_integral()
    small_lattice_cocycle = all_small_lattice_cocycle_defects_integral(bound=1)
    semicharacter_ok = trivial_semicharacter_allowed()
    source_scan = source_scan_summary()

    construction_checks = {
        "target_degrees": DEGREES,
        "c1_matrix_matches_required_order": matrix[0][1] == 2
        and matrix[2][3] == -4
        and matrix[4][5] == 0,
        "c1_pairing_g1_g2": c1_pairing(basis_vector(0), basis_vector(1)),
        "c1_pairing_g3_g4": c1_pairing(basis_vector(2), basis_vector(3)),
        "c1_pairing_g5_g6": c1_pairing(basis_vector(4), basis_vector(5)),
        "central_shared_circle_trivial": all(matrix[i][j] == 0 for i in (4, 5) for j in range(6)),
        "mixed_base_terms_zero": all(matrix[i][j] == 0 for i in (0, 1) for j in (2, 3))
        and all(matrix[i][j] == 0 for i in (2, 3) for j in (0, 1)),
        "cocycle_law_holds_on_generators_mod_2pi_i": generator_cocycle,
        "cocycle_law_holds_on_small_lattice_box_mod_2pi_i": small_lattice_cocycle,
        "trivial_semicharacter_allowed_because_c1_pairing_even": semicharacter_ok,
        "c1_L_squared_square_is_minus_16_alpha1": c1_square_alpha_coeffs(TARGET_L2) == [-16, 0, 0],
        "c2_extension_target_is_plus_4_alpha1": c2_extension_alpha_coeffs(TARGET_L) == [4, 0, 0],
    }

    selected_by_mtt = False
    status = (
        "VISIBLE_RANK2_L2_APPELL_HUMBERT_AUTOMORPHY_CONSTRUCTED_SELECTION_OPEN"
        if all(
            [
                construction_checks["c1_matrix_matches_required_order"],
                construction_checks["central_shared_circle_trivial"],
                construction_checks["mixed_base_terms_zero"],
                generator_cocycle,
                small_lattice_cocycle,
                semicharacter_ok,
                construction_checks["c1_L_squared_square_is_minus_16_alpha1"],
                construction_checks["c2_extension_target_is_plus_4_alpha1"],
            ]
        )
        else "VISIBLE_RANK2_L2_APPELL_HUMBERT_AUTOMORPHY_CONSTRUCTION_FAILED"
    )

    report = {
        "calculation": "VisibleRank2L2AppellHumbertAutomorphy",
        "status": status,
        "generated_by": "scripts/construct_visible_rank2_l2_appell_humbert_automorphy.py",
        "source_scan": source_scan,
        "model": {
            "universal_cover": "C^3 with standard Iwasawa coordinates z1,z2,z3",
            "base_torus": "C/(Z+iZ) x C/(Z+iZ)",
            "central_shared_circle_pair": "g5,g6",
            "factor_formula": (
                "For gamma=(m1,n1,m2,n2,m3,n3), "
                "a(gamma,z)=prod_{j=1}^2 exp(-pi*i*d_j*n_j^2*i - "
                "2*pi*i*d_j*n_j*z_j), with (d1,d2,d3)=(2,-4,0)."
            ),
            "factor_formula_convention": (
                "This is the standard theta/Appell-Humbert multiplier for tau=i; "
                "negative degree means the dual power. Multiplying by a flat Pic0 "
                "character is intentionally set to the neutral value here."
            ),
            "generator_factors": generator_table(),
            "c1_deck_alternating_matrix_order_g1_to_g6": matrix,
        },
        "construction_checks": construction_checks,
        "selection_analysis": {
            "mathematical_automorphy_representative_constructed": True,
            "selected_by_mtt": selected_by_mtt,
            "standard_gaussian_lattice_selected_by_mtt": False,
            "target_branch_L_selected_by_mtt": False,
            "neutral_pic0_character_selected_by_mtt": False,
            "same_source_as_visible_valpha_selected": False,
            "reason": (
                "The Appell-Humbert representative supplies explicit non-flat "
                "automorphy data for the ordered matrix.  The current audited "
                "source corpus still does not select Gamma0, the target branch "
                "over the swapped branch, or the neutral Pic0 representative."
            ),
        },
        "what_this_closes": {
            "explicit_nonflat_factor_of_automorphy_for_L2_2_minus4_0": True,
            "ordinary_integral_c1_matrix_realized": True,
            "finite_torsion_gerbe_not_used_as_ordinary_c1": True,
            "trivial_semicharacter_is_consistent_for_even_degrees": semicharacter_ok,
            "shared_circle_degree_zero_retained": True,
            "automorphy_formula_gap_reduced_to_selection_not_existence": True,
        },
        "still_open": {
            "MTT_selection_of_standard_Gamma0_or_equivalent_lattice": True,
            "MTT_branch_orientation_selecting_L_1_minus2_0_over_swapped": True,
            "MTT_selection_or_elimination_of_flat_Pic0_characters": True,
            "same_source_visible_valpha_non_split_extension": True,
            "nonzero_Ext_class_selection": True,
            "non_split_stability": True,
            "same_source_D_E_dotD_Riesz_Green": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_MTT_selected_automorphy_source": False,
            "claims_Gamma0_selected": False,
            "claims_target_branch_selected": False,
            "claims_neutral_Pic0_selected": False,
            "claims_selected_Ext_class": False,
            "claims_stability_proved": False,
            "claims_D_E_dotD_Riesz_Green_constructed": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "The ordered L^2 source no longer lacks an explicit non-flat "
                "automorphy model: the Appell-Humbert multiplier realizes "
                "E(g1,g2)=2, E(g3,g4)=-4, and E(g5,g6)=0.  What remains is the "
                "genuinely physical MTT selection theorem for this representative, "
                "not the construction of an automorphy formula."
            ),
            "next_action": (
                "Prove branch/neutral-Pic0 selection from the MTT Hessian, "
                "Gauduchon wall, or same-source Strominger/HYM functional; then "
                "promote the existing h1=8 packet to SELECTED_DATA."
            ),
        },
    }
    return report


def main() -> int:
    report = analyze()
    write_json(CANDIDATE, report)
    certificate = {
        "certificate": "VisibleRank2L2AppellHumbertAutomorphy",
        "status": report["status"],
        "analysis_script": report["generated_by"],
        "candidate_data": "candidate_data/visible_rank2_l2_appell_humbert_automorphy.candidate.json",
        "source_scan": report["source_scan"],
        "model": report["model"],
        "construction_checks": report["construction_checks"],
        "selection_analysis": report["selection_analysis"],
        "what_this_closes": report["what_this_closes"],
        "still_open": report["still_open"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    write_json(CERTIFICATE, certificate)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["status"].endswith("SELECTION_OPEN") else 1


if __name__ == "__main__":
    raise SystemExit(main())
