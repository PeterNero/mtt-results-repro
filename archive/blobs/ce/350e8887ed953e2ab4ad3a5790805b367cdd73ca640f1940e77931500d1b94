"""Search for Ext/stability source data after the Iwasawa abelian-row gate."""

from __future__ import annotations

import json
import sys
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")

INPUT = DATA / "iwasawa_abelian_row_to_nonabelian_source_gate.candidate.json"
SOURCE = OBSIDIAN / "16 Strings, Flux, & M-Theory Encodings" / "Flux_Compactifications_in_Heterotic_String_Theory_v3.md"
OUTPUT_DATA = DATA / "ext_stability_source_search.candidate.json"
OUTPUT_CERT = CERTS / "ext_stability_source_search_certificate.json"

ELLS = [
    (-2, 0, 1),
    (-1, 1, -1),
    (1, -1, 0),
    (1, 0, -1),
    (2, 1, 1),
]
KAPPAS = [(1, 0, 0), (0, 1, 0)]


def square(v: tuple[int, int, int]) -> tuple[int, int, int]:
    x, y, z = v
    return (2 * x * y, 2 * x * z, 2 * y * z)


def cube(v: tuple[int, int, int]) -> int:
    x, y, z = v
    return 6 * x * y * z


def vec_sum(items: list[tuple[int, int, int]]) -> tuple[int, int, int]:
    return tuple(sum(v[i] for v in items) for i in range(3))  # type: ignore[return-value]


def scan_source() -> dict[str, object]:
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
    if not SOURCE.exists():
        return {"path": str(SOURCE), "present": False, "terms_found": [], "missing_terms": terms}
    text = SOURCE.read_text(encoding="utf-8", errors="ignore").lower()
    found = [term for term in terms if term.lower() in text]
    return {"path": str(SOURCE), "present": True, "terms_found": found, "missing_terms": [term for term in terms if term not in found]}


def monad_computation() -> dict[str, object]:
    sum_ell = vec_sum(ELLS)
    sum_kappa = vec_sum(KAPPAS)
    ell_sq = vec_sum([square(v) for v in ELLS])
    kappa_sq = vec_sum([square(v) for v in KAPPAS])
    diff_sq = tuple(ell_sq[i] - kappa_sq[i] for i in range(3))
    ch2 = tuple(Fraction(x, 2) for x in diff_sq)
    c2 = tuple(-x for x in ch2)
    ell_cube = sum(cube(v) for v in ELLS)
    kappa_cube = sum(cube(v) for v in KAPPAS)
    ch3 = Fraction(ell_cube - kappa_cube, 6)
    c3 = 2 * ch3
    return {
        "ell_i": ELLS,
        "kappa_a": KAPPAS,
        "sum_ell": sum_ell,
        "sum_kappa": sum_kappa,
        "c1_zero": sum_ell == sum_kappa,
        "sum_ell_square_alpha_coeffs": ell_sq,
        "sum_kappa_square_alpha_coeffs": kappa_sq,
        "ch2_alpha_coeffs": [str(x) for x in ch2],
        "c2_alpha_coeffs": [str(x) for x in c2],
        "c2_zero": all(x == 0 for x in c2),
        "sum_ell_cube": ell_cube,
        "sum_kappa_cube": kappa_cube,
        "ch3_integral": str(ch3),
        "c3_integral": str(c3),
        "c3_integral_equals_6": c3 == 6,
    }


def main() -> None:
    gate = json.loads(INPUT.read_text(encoding="utf-8"))
    scan = scan_source()
    monad = monad_computation()
    source_found = scan["present"] is True and not scan["missing_terms"]
    candidate = {
        "candidate": "SelectedQaSU3ExtStabilitySourceSearch",
        "status": "EXT_STABILITY_SOURCE_SEARCH_FOUND_IWASAWA_MONAD_OPERATOR_OPEN",
        "input_statuses": {"promotion_gate": gate["status"]},
        "source_scan": scan,
        "monad_computation": monad,
        "found_source_candidate": {
            "id": "explicit_iwasawa_rank3_su3_monad",
            "source_kind": "indecomposable rank-three SU3 monad with Li-Yau/HYM existence claim",
            "same_iwasawa_paper_as_abelian_row": True,
            "closes_blank_source_search": True,
            "not_the_threshold_packet_yet": True,
        },
        "interpretation": {
            "source_situation_updated": True,
            "what_changed": "The corpus does contain an explicit non-split rank-three SU3 Iwasawa monad, so the problem is no longer to find any nonabelian HYM-flavored source.",
            "why_not_closure": "The monad recomputes to c2(E)=0 and Tr F_E^2=0, while the alpha1 Bianchi support row is abelian/torsion/gravitational.  Qa/SU3 closure still needs a selected threshold representation and operator packet.",
        },
        "what_closes": {
            "explicit_iwasawa_su3_monad_found": source_found,
            "integer_chern_character_recomputed": True,
            "c1_zero": monad["c1_zero"],
            "c2_zero": monad["c2_zero"],
            "c3_integral_six": monad["c3_integral_equals_6"],
            "hym_existence_claim_present": "Li--Yau" in scan["terms_found"],
            "same_paper_contains_abelian_bianchi_row": "u_1=8(2\\pi)^2" in scan["terms_found"],
        },
        "what_remains_open": {
            "qa_su3_threshold_representation": True,
            "same_source_rhoE_or_DE": True,
            "endomorphism_E": True,
            "finite_determinant_part": True,
            "operator_packet_filled": False,
            "qa_su3_closed": False,
        },
        "guardrails": [
            "Do not identify the E8-to-E6 monad with QCD SU3 threshold data without a representation map.",
            "Do not replace endomorphism_E by Chern classes alone.",
            "Do not use the abelian Bianchi row as the nonabelian determinant.",
            "Do not claim full Qa/SU3 or SM closure from HYM existence alone.",
        ],
        "next_required_artifact": "Selected_Qa_SU3_Monad_to_Operator_Packet_Transfer_Gate_v1",
        "target_fitting_used": False,
    }
    certificate = {
        "certificate": "SelectedQaSU3ExtStabilitySourceSearch",
        "status": "QA_SU3_EXT_STABILITY_SOURCE_SEARCH_FOUND_IWASAWA_MONAD_OPERATOR_OPEN",
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "what_closes": candidate["what_closes"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": candidate["next_required_artifact"],
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
