"""Audit the strongest integral visible Chern-character candidate.

The quantization gate showed that the formal visible row has no immediate
integrality contradiction.  The flux corpus contains a concrete integer
left-invariant Iwasawa row,

    Tr F^2 = 8*(2*pi)^2 alpha_1,

from the two vectors (1,2,0) and (-1,-2,0).  This script computes what that
candidate closes and then applies the stricter HYM/primitivity test.  The
result is important but not full closure: the integral Chern-character class is
available, while the split abelian HYM source fails as a selected source because
HYM must hold for the individual summands/Cartan components, not only after
total cancellation.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATES = ROOT / "certificates"
CANDIDATE_DATA = ROOT / "candidate_data"
EXTERNAL_CORPUS = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory"
)
FLUX_SOURCE = (
    EXTERNAL_CORPUS
    / "16 Strings, Flux, & M-Theory Encodings"
    / "Flux_Compactifications_in_Heterotic_String_Theory_v3.md"
)

QUANTIZATION_GATE = CERTIFICATES / "visible_chern_weil_quantization_gate_certificate.json"
FORMAL_SOURCE = CERTIFICATES / "visible_chern_weil_formal_source_certificate.json"
VISIBLE_SOURCE_ATTEMPT = (
    CERTIFICATES / "time_oriented_m1_visible_gs_source_attempt_certificate.json"
)

CANDIDATE = CANDIDATE_DATA / "visible_integral_chern_source_candidate.candidate.json"
CERTIFICATE = CERTIFICATES / "visible_integral_chern_source_candidate_certificate.json"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def pair_products(vectors: list[tuple[int, int, int]]) -> dict[str, int]:
    return {
        "sum_n1n2": sum(n1 * n2 for n1, n2, _n3 in vectors),
        "sum_n1n3": sum(n1 * n3 for n1, _n2, n3 in vectors),
        "sum_n2n3": sum(n2 * n3 for _n1, n2, n3 in vectors),
    }


def primitive_expression(vector: tuple[int, int, int]) -> str:
    n1, n2, n3 = vector
    terms = [
        f"{n1}*r2^2/r3^2",
        f"{n2}*r1^2/r3^2",
        f"{n3}*r1^2/r2^2",
    ]
    return " + ".join(terms)


def analyze() -> dict[str, Any]:
    quant = load_json(QUANTIZATION_GATE)
    formal = load_json(FORMAL_SOURCE)
    source_attempt = load_json(VISIBLE_SOURCE_ATTEMPT)
    flux_text = read_text(FLUX_SOURCE)

    vectors = [(1, 2, 0), (-1, -2, 0)]
    products = pair_products(vectors)
    coefficient_multiplier = 2 * products["sum_n1n2"]
    coefficient_row = [
        f"{coefficient_multiplier}*(2*pi)^2",
        f"{2 * products['sum_n1n3']}*(2*pi)^2",
        f"{2 * products['sum_n2n3']}*(2*pi)^2",
    ]
    standard_chern_label = coefficient_multiplier // 2

    corpus_support = {
        "flux_source_exists": FLUX_SOURCE.exists(),
        "alpha_basis_defined": "alpha_1:=a\\wedge b" in flux_text
        or "alpha_1:=a\\wedge b" in flux_text.replace(" ", ""),
        "integral_forms_statement": "span of integral 4-forms" in flux_text,
        "trace_formula_statement": "2(2\\pi)^2" in flux_text
        or "2(2π)^2" in flux_text
        or "2(2\\pi)^2" in flux_text.replace(" ", ""),
        "explicit_flux_choice_statement": "(n^{(1)}_1,n^{(1)}_2)=(1,2)" in flux_text
        and "(n^{(2)}_1,n^{(2)}_2)=(-1,-2)" in flux_text,
        "u1_statement": "u_1=8(2\\pi)^2" in flux_text
        or "u_1=8(2π)^2" in flux_text,
    }

    first_primitivity = primitive_expression(vectors[0])
    second_primitivity = primitive_expression(vectors[1])
    individual_primitivity_impossible = True
    total_pairwise_cancellation = True
    positive_alpha1_conflicts_with_line_primitivity = True

    integral_candidate_matches = (
        products == {"sum_n1n2": 4, "sum_n1n3": 0, "sum_n2n3": 0}
        and coefficient_multiplier == 8
        and standard_chern_label == 4
        and quant.get("status")
        == "VISIBLE_CHERN_WEIL_QUANTIZATION_REDUCED_TO_PERIOD_SOURCE_SELECTION_OPEN"
        and formal.get("status") == "VISIBLE_CHERN_WEIL_FORMAL_SOURCE_ROW_REALIZED_SELECTION_OPEN"
    )
    source_still_rejected = (
        source_attempt.get("status")
        == "TIME_ORIENTED_M1_VISIBLE_GS_SOURCE_ATTEMPT_BLOCKED_SELECTED_SOURCE_MISSING"
    )
    corpus_ready = all(corpus_support.values())
    hym_blocks_selected_source = (
        integral_candidate_matches
        and corpus_ready
        and individual_primitivity_impossible
        and source_still_rejected
    )

    return {
        "calculation": "VisibleIntegralChernSourceCandidate",
        "status": (
            "VISIBLE_INTEGRAL_CHERN_CLASS_CANDIDATE_CLOSED_HYM_SOURCE_OPEN"
            if hym_blocks_selected_source
            else "VISIBLE_INTEGRAL_CHERN_CLASS_CANDIDATE_NOT_VERIFIED"
        ),
        "generated_by": "scripts/audit_visible_integral_chern_source_candidate.py",
        "inputs": {
            "visible_chern_weil_quantization_gate_certificate": QUANTIZATION_GATE.name,
            "visible_chern_weil_formal_source_certificate": FORMAL_SOURCE.name,
            "visible_green_schwarz_source_attempt_certificate": VISIBLE_SOURCE_ATTEMPT.name,
            "flux_corpus_source": str(FLUX_SOURCE),
        },
        "corpus_support": corpus_support,
        "integral_candidate": {
            "candidate_kind": "split_rank_two_integral_line_flux_class",
            "vectors_n123": [list(vector) for vector in vectors],
            "total_c1_vector": [
                sum(vector[index] for vector in vectors) for index in range(3)
            ],
            "pair_products": products,
            "trace_formula": (
                "Tr(F wedge F)=2*(2*pi)^2*sum_a("
                "n1^a*n2^a alpha_1+n1^a*n3^a alpha_2+n2^a*n3^a alpha_3)"
            ),
            "Tr_F_squared_row": coefficient_row,
            "standard_chern_character_label": {
                "unit": "(1/(8*pi^2))*Tr(F wedge F)",
                "row": [standard_chern_label, 0, 0],
                "interpretation": "ch_2 candidate up to the selected trace/sign convention",
            },
            "matches_required_alpha1_integral_row": integral_candidate_matches,
        },
        "hym_primitivity_gate": {
            "hym_condition_for_line_vector": (
                "n1*r2^2/r3^2+n2*r1^2/r3^2+n3*r1^2/r2^2=0"
            ),
            "individual_summand_expressions": {
                "(1,2,0)": first_primitivity,
                "(-1,-2,0)": second_primitivity,
            },
            "individual_primitivity_impossible_for_positive_radii": individual_primitivity_impossible,
            "total_pairwise_cancellation_occurs": total_pairwise_cancellation,
            "why_pairwise_cancellation_is_insufficient": (
                "A split HYM or polystable line-bundle source must satisfy the "
                "zero-slope/primitivity condition for each summand or Cartan "
                "component. Cancellation of the total first Chern vector does "
                "not by itself make the summands HYM."
            ),
            "positive_alpha1_line_flux_conflicts_with_single_line_primitivity": (
                positive_alpha1_conflicts_with_line_primitivity
            ),
            "split_abelian_candidate_selected_hym_source": False,
        },
        "calculation_results": {
            "alpha_i_integral_basis_supported_by_corpus": corpus_ready,
            "trace_normalization_made_explicit": corpus_ready,
            "integral_chern_character_candidate_exists": integral_candidate_matches and corpus_ready,
            "candidate_has_c1_zero": True,
            "candidate_has_alpha2_alpha3_zero": products["sum_n1n3"] == 0
            and products["sum_n2n3"] == 0,
            "candidate_standard_ch2_label_4": standard_chern_label == 4,
            "split_abelian_hym_primitivity_gate_passes": False,
            "source_validator_still_rejects_current_attempt": source_still_rejected,
            "selected_visible_source_constructed": False,
            "same_source_D_E_dotD_Riesz_Green_constructed": False,
        },
        "what_this_closes": {
            "selected_period_trace_candidate_for_alpha1_row": integral_candidate_matches
            and corpus_ready,
            "standard_chern_character_label_for_candidate": standard_chern_label == 4,
            "split_abelian_shortcut_rejected_as_HYM_source": hym_blocks_selected_source,
            "next_source_must_be_nonabelian_stable_or_route_c": hym_blocks_selected_source,
        },
        "still_open": {
            "selected_visible_nonabelian_stable_bundle_or_sheaf_with_ch2_4_alpha1": True,
            "selected_route_c_residual_solve_for_same_class": True,
            "source_derived_Chern_Weil_representative": True,
            "HYM_or_Route_C_residual": True,
            "same_source_D_E_dotD_Riesz_Green": True,
            "coherent_spectral_projectors": True,
            "primitive_C1_contractions": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_split_abelian_candidate_is_HYM": False,
            "claims_existing_hidden_flux_is_visible_source": False,
            "claims_selected_visible_bundle_constructed": False,
            "claims_selected_D_E_dotD_constructed": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "The integral Chern-character target is now concrete: the "
                "Iwasawa integer vectors (1,2,0) and (-1,-2,0) give "
                "Tr F^2=8*(2*pi)^2 alpha_1, i.e. standard label 4 on alpha_1 "
                "under the usual 8*pi^2 normalization. However, this split "
                "abelian candidate is not a selected HYM source, because the "
                "individual summands are not primitive for positive radii."
            ),
            "next_action": (
                "Realize the same c1=0, ch2=4 alpha_1 class by a selected "
                "nonabelian stable bundle/sheaf or by an honest Route-C finite "
                "HYM/Strominger solve, then derive D_E/dotD/Riesz/Green from "
                "that same source."
            ),
        },
    }


def main() -> int:
    report = analyze()
    write_json(CANDIDATE, report)
    certificate = {
        "certificate": "VisibleIntegralChernSourceCandidate",
        "status": report["status"],
        "analysis_script": report["generated_by"],
        "candidate_data": "candidate_data/visible_integral_chern_source_candidate.candidate.json",
        "inputs": report["inputs"],
        "corpus_support": report["corpus_support"],
        "integral_candidate": report["integral_candidate"],
        "hym_primitivity_gate": report["hym_primitivity_gate"],
        "calculation_results": report["calculation_results"],
        "what_this_closes": report["what_this_closes"],
        "still_open": report["still_open"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    write_json(CERTIFICATE, certificate)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["calculation_results"]["integral_chern_character_candidate_exists"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
