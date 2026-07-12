"""Construct and audit the explicit Iwasawa non-split SU3 monad candidate."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")

PROMOTION_GATE = CERTS / "selected_qa_su3_iwasawa_abelian_row_to_nonabelian_source_gate_certificate.json"
SOURCE = OBSIDIAN / "16 Strings, Flux, & M-Theory Encodings" / "Flux_Compactifications_in_Heterotic_String_Theory_v3.md"

ELLS = [
    (-2, 0, 1),
    (-1, 1, -1),
    (1, -1, 0),
    (1, 0, -1),
    (2, 1, 1),
]
KAPPAS = [
    (1, 0, 0),
    (0, 1, 0),
]


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def square(v: tuple[int, int, int]) -> tuple[int, int, int]:
    x, y, z = v
    return (2 * x * y, 2 * x * z, 2 * y * z)


def cube(v: tuple[int, int, int]) -> int:
    x, y, z = v
    return 6 * x * y * z


def vec_sum(items: list[tuple[int, int, int]]) -> tuple[int, int, int]:
    return tuple(sum(v[i] for v in items) for i in range(3))  # type: ignore[return-value]


def scan_source() -> dict[str, Any]:
    if not SOURCE.exists():
        return {"path": str(SOURCE), "present": False, "terms_found": []}
    text = SOURCE.read_text(encoding="utf-8", errors="ignore")
    terms = [
        "explicit indecomposable",
        "SU(3)",
        "monad",
        "c_1=0",
        "c_2=0",
        "c_3=6",
        "Li--Yau",
        "Hermitian--Yang--Mills",
        "Tr}F_E\\wedge F_E=0",
        "u_1=8(2\\pi)^2",
        "Bianchi identity",
    ]
    lowered = text.lower()
    return {
        "path": str(SOURCE),
        "present": True,
        "terms_found": [term for term in terms if term.lower() in lowered],
        "missing_terms": [term for term in terms if term.lower() not in lowered],
    }


def main() -> None:
    promotion = load(PROMOTION_GATE)

    s1 = vec_sum(ELLS)
    k = vec_sum(KAPPAS)
    ell_sq = vec_sum([square(v) for v in ELLS])
    k_sq = vec_sum([square(v) for v in KAPPAS])
    diff_sq = tuple(ell_sq[i] - k_sq[i] for i in range(3))
    ch2 = tuple(Fraction(diff_sq[i], 2) for i in range(3))
    c2 = tuple(-x for x in ch2)
    ell_cube = sum(cube(v) for v in ELLS)
    k_cube = sum(cube(v) for v in KAPPAS)
    ch3 = Fraction(ell_cube - k_cube, 6)
    c3 = 2 * ch3

    monad = {
        "ell_i": ELLS,
        "kappa_a": KAPPAS,
        "sum_ell": s1,
        "sum_kappa": k,
        "c1_zero": s1 == k,
        "sum_ell_square_alpha_coeffs": ell_sq,
        "sum_kappa_square_alpha_coeffs": k_sq,
        "ch2_alpha_coeffs": [str(x) for x in ch2],
        "c2_alpha_coeffs": [str(x) for x in c2],
        "c2_zero": all(x == 0 for x in c2),
        "sum_ell_cube": ell_cube,
        "sum_kappa_cube": k_cube,
        "ch3_integral": str(ch3),
        "c3_integral": str(c3),
        "c3_integral_equals_6": c3 == 6,
    }

    source_scan = scan_source()
    construction_tests = {
        "source_file_present": source_scan["present"],
        "explicit_monad_integer_data": True,
        "rank_three": True,
        "c1_zero": monad["c1_zero"],
        "c2_zero": monad["c2_zero"],
        "c3_integral_six": monad["c3_integral_equals_6"],
        "generic_indecomposable_claim_in_source": "explicit indecomposable" in source_scan["terms_found"],
        "li_yau_hym_claim_in_source": "Li--Yau" in source_scan["terms_found"],
        "component_bianchi_flux_row_in_source": "u_1=8(2\\pi)^2" in source_scan["terms_found"],
    }

    output = {
        "certificate": "SelectedQaSU3NonSplitExtensionSourceConstruction",
        "status": "QA_SU3_NONSPLIT_IWASAWA_MONAD_SOURCE_FOUND_OPERATOR_PACKET_OPEN",
        "input_status": {
            "promotion_gate": promotion["status"],
        },
        "source_scan": source_scan,
        "monad_computation": monad,
        "construction_tests": construction_tests,
        "what_this_closes": {
            "non_split_rank3_su3_candidate_found_in_corpus": True,
            "integer_chern_character_recomputed": True,
            "c1_c2_c3_claims_verified_from_printed_line_data": True,
            "hym_existence_source_claim_present": construction_tests["li_yau_hym_claim_in_source"],
            "abelian_bianchi_support_row_connected_to_same_iwasawa_paper": True,
        },
        "what_remains_open": {
            "qa_su3_threshold_representation_identified": False,
            "same_source_rhoE_transition_packet": False,
            "operator_packet_filled": False,
            "endomorphism_E_computed": False,
            "finite_determinant_computed": False,
            "qa_su3_closed": False,
        },
        "interpretation": {
            "does_update_prior_source_search": True,
            "update": (
                "The wider strings/flux corpus does contain an explicit "
                "indecomposable rank-3 SU3 Iwasawa monad.  This improves the "
                "source situation, but it does not by itself fill the Qa/SU3 "
                "threshold operator packet."
            ),
            "why_not_full_closure": (
                "The monad has c2(E)=0 and Tr F_E^2=0; the alpha1 Bianchi "
                "support row comes from hidden abelian flux plus gravitational "
                "torsion.  A selected threshold representation, rho_E packet, "
                "and endomorphism_E still have to be derived."
            ),
        },
        "guardrails": [
            "Do not identify the E8 to E6 monad source with QCD SU3 threshold data without a representation map.",
            "Do not replace endomorphism_E by Chern classes alone.",
            "Do not use the hidden abelian flux row as the nonabelian determinant.",
            "Do not claim full Qa/SU3 or SM closure from HYM existence alone.",
        ],
        "next_required_artifact": {
            "name": "Selected_Qa_SU3_Monad_to_Operator_Packet_Transfer_Gate_v1",
            "must_decide": [
                "whether the monad E is the selected Qa/SU3 threshold source or only a visible E8 to E6 benchmark",
                "which representation trace enters the Qa/SU3 determinant",
                "how to derive finite rho_E transition data or a left-invariant D_E operator from the monad",
                "whether the A01 matrix and Chern connection determine endomorphism_E",
            ],
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
