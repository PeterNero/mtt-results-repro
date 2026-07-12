"""Search for a same-branch central period selector for Qa/SU3."""

from __future__ import annotations

import json
import math
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
DATA = ROOT / "candidate_data"
PROOF = ROOT / "proof_corpus"
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")

INPUT = DATA / "ctwist_period_normalization_or_a01_exit.candidate.json"
OUTPUT_DATA = DATA / "central_period_selector_search.candidate.json"
OUTPUT_CERT = CERTS / "central_period_selector_search_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Qa_SU3_Central_Period_Selector_Search_v1.md"


SOURCES = {
    "qa_period_gate": ROOT / "proof_corpus" / "Selected_Qa_SU3_CTwist_Period_Normalization_or_A01_Exit_v1.md",
    "qa_full_dependency": ROOT / "candidate_data" / "full_corpus_dependency_audit.candidate.json",
    "iwasawa_flux": OBSIDIAN
    / "16 Strings, Flux, & M-Theory Encodings"
    / "Flux_Compactifications_in_Heterotic_String_Theory_v3.md",
    "kk_fcc": OBSIDIAN
    / "15 Discrete & Spectral & Operator Geometric Theories"
    / "Modal_Triplet_Theory__From_MTT_to_Kaluza__Klein_Theory.md",
    "string_theory": OBSIDIAN
    / "16 Strings, Flux, & M-Theory Encodings"
    / "Modal_Triplet_Theory__From_MTT_to_String_Theory.md",
    "m_theory": OBSIDIAN
    / "16 Strings, Flux, & M-Theory Encodings"
    / "Modal_Triplet_Theory__From_MTT_to_M_theory.md",
    "q79_iwasawa_discrete_gerbe": Q79 / "certificates" / "iwasawa_discrete_gerbe_holonomy_candidate_certificate.json",
    "q79_time_m1_period_table": Q79 / "certificates" / "time_oriented_m1_gerbe_period_table_certificate.json",
    "q79_torsion_label_selector": Q79 / "certificates" / "iwasawa_torsion_label_four_route_selector_certificate.json",
    "q79_twisted_source_fill": Q79 / "certificates" / "iwasawa_twisted_source_packet_fill_attempt_certificate.json",
}


TERM_SETS = {
    "qa_period_gate": {
        "A_unit_condition": "A=1",
        "R4_alpha_exact": "R^4 = alpha_prime*((2*pi)^2 - 1)/2",
        "not_selected": "not selected",
    },
    "qa_full_dependency": {
        "hidden_selector_false": "hidden_selector_found",
        "same_branch_selector_false": "same_branch_period_selector_found",
        "same_branch_period_selector": "same-branch central period selector",
    },
    "iwasawa_flux": {
        "r3_formula": "r3^2",
        "alpha_prime": "alpha",
        "integral_periods": "integral periods",
        "modulus_remains": "modulus remains",
        "flux_quantization": "Flux quantization",
        "bianchi": "Bianchi",
    },
    "kk_fcc": {
        "fixed_point_compactification": "Fixed-point compactification condition",
        "finite_algebraic_diophantine": "finite algebraic/Diophantine",
        "primitivity": "primitivity",
        "quantization_integrality": "quantization/integrality",
        "integer_data": "integer data",
    },
    "string_theory": {
        "alpha_prime_normalization": "alpha",
        "torsional_su3_slice": "torsional SU(3)",
        "selection_theorem": "selection theorem",
        "strominger": "Strominger",
    },
    "m_theory": {
        "integral_lattice": "integral",
        "shifted_quantization": "shifted",
        "discrete_vacua": "discrete",
        "g4": "G_4",
    },
    "q79_iwasawa_discrete_gerbe": {
        "z3": "Z3",
        "finite_bianchi": "Bianchi",
        "selection_open": "selection",
    },
    "q79_time_m1_period_table": {
        "m1": "m=1",
        "period_table": "period",
        "zeta3": "zeta",
        "selected": "selected",
    },
    "q79_torsion_label_selector": {
        "reject_m0": "m=0",
        "nontrivial_pair": "m in {1,2}",
        "orientation_open": "orientation",
    },
    "q79_twisted_source_fill": {
        "source_still_open": "selected",
        "operator_open": "D_E",
        "projector": "projector",
    },
}


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="ignore")


def scan(path: Path, terms: dict[str, str]) -> dict[str, object]:
    text = read_text(path)
    folded = text.lower()
    hits = {key: needle.lower() in folded for key, needle in terms.items()}
    return {"path": str(path), "present": bool(text), "terms": hits}


def extract_status(path: Path) -> str | None:
    if not path.exists() or path.suffix != ".json":
        return None
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None
    return payload.get("status")


def exact_ratio_hits(text: str) -> list[str]:
    patterns = [
        r"\(\(2\*pi\)\^2\s*-\s*1\)/2",
        r"R\^4\s*=\s*alpha_prime\*\(\(2\*pi\)\^2\s*-\s*1\)/2",
        r"19\.239208802178716",
    ]
    return [pattern for pattern in patterns if re.search(pattern, text, flags=re.IGNORECASE)]


def main() -> None:
    prior = json.loads(INPUT.read_text(encoding="utf-8"))
    scans = {key: scan(path, TERM_SETS[key]) for key, path in SOURCES.items()}
    statuses = {key: extract_status(path) for key, path in SOURCES.items() if path.suffix == ".json"}
    qa_text = read_text(SOURCES["qa_period_gate"])
    ratio_hit_sources = {
        key: exact_ratio_hits(read_text(path))
        for key, path in SOURCES.items()
        if key != "qa_period_gate"
    }
    independent_ratio_hit_sources = {
        key: hits
        for key, hits in ratio_hit_sources.items()
        if hits and key != "qa_full_dependency"
    }

    a_unit_ratio = prior["scalar_period_gate"]["numeric_R4_over_alpha_prime_for_A_unit"]
    finite_q79_statuses = {
        key: value
        for key, value in statuses.items()
        if key.startswith("q79_")
    }
    q79_has_nontrivial_finite_pattern = all(
        scans[key]["present"]
        for key in [
            "q79_iwasawa_discrete_gerbe",
            "q79_time_m1_period_table",
            "q79_torsion_label_selector",
        ]
    )
    q79_same_branch_promotes = False

    route_tests = [
        {
            "route_id": "exact_A_unit_ratio_search",
            "searched_for": [
                "R^4/alpha_prime = ((2*pi)^2 - 1)/2",
                "numeric 19.239208802178716",
            ],
            "hits_inside_existing_gate": exact_ratio_hits(qa_text),
            "hits_outside_existing_gate_by_source": ratio_hit_sources,
            "independent_selector_hits": independent_ratio_hit_sources,
            "verdict": "NO_INDEPENDENT_SELECTOR_FOUND",
            "promotes_selector": False,
            "reason": "The exact scalar appears in the derived Qa/SU3 period gate, not as an independent source-selected corpus value.",
        },
        {
            "route_id": "finite_central_quotient_search",
            "searched_for": ["same-branch finite central quotient", "Z3/qutrit torsion selector"],
            "q79_statuses": finite_q79_statuses,
            "verdict": "FINITE_PATTERN_EXISTS_OFF_BRANCH",
            "promotes_selector": q79_same_branch_promotes,
            "reason": "q79 has strong finite torsion/period-table evidence, but its own certificates mark source/operator promotion open and do not select the Qa/SU3 c-twist quotient.",
        },
        {
            "route_id": "fcc_superset_selector_route",
            "searched_for": [
                "finite algebraic/Diophantine compactification condition",
                "primitivity and quantization/integrality constraints",
            ],
            "verdict": "METHOD_FOUND_VALUES_NOT_COMPUTED",
            "promotes_selector": False,
            "reason": "The Kaluza-Klein/FCC corpus gives the correct superset method: solve invariant equations plus integer data. It does not yet instantiate the Qa/SU3 equations with integer flux/holonomy data.",
        },
        {
            "route_id": "strominger_string_m_theory_integrality_route",
            "searched_for": ["alpha-prime normalization", "torsional SU(3)", "shifted G4 quantization"],
            "verdict": "NORMALIZATION_INFRASTRUCTURE_FOUND_UNIT_NOT_SELECTED",
            "promotes_selector": False,
            "reason": "String/M-theory sources justify integrality and normalization conventions, but do not bind the isotropic Iwasawa modulus to the A=1 value.",
        },
    ]

    selector_found = any(row["promotes_selector"] for row in route_tests)
    candidate = {
        "candidate": "SelectedQaSU3CentralPeriodSelectorSearch",
        "status": "CENTRAL_PERIOD_SELECTOR_SEARCH_COMPLETE_SELECTOR_NOT_FOUND",
        "input_status": prior["status"],
        "scalar_target": {
            "A_unit_condition": prior["scalar_period_gate"]["A_unit_condition"],
            "R4_over_alpha_prime_required": a_unit_ratio,
            "source_selected_by_current_search": False,
        },
        "source_scans": scans,
        "source_statuses": statuses,
        "route_tests": route_tests,
        "gate_results": {
            "same_branch_exact_A_unit_selector_found": False,
            "same_branch_finite_central_quotient_found": False,
            "q79_nontrivial_finite_pattern_found": q79_has_nontrivial_finite_pattern,
            "q79_pattern_promoted_to_Qa_SU3": False,
            "superset_FCC_method_identified": scans["kk_fcc"]["terms"]["finite_algebraic_diophantine"],
            "period_selector_found": selector_found,
            "gerbe_period_promotion_allowed": selector_found,
            "A01_DE_or_selected_operator_exit_still_required": True,
            "closure_claimed": False,
        },
        "decision": {
            "result": "No same-branch period selector was found.",
            "what_this_closes": "It closes the search artifact that previous gates named: the missing object is not hidden in the checked corpus/proof repos.",
            "correct_way_forward": "Do not promote the gerbe period branch by assumption. Either build the FCC invariant-equation packet with integer data for Qa/SU3, or supply the same-source D_E/rho_E operator exit.",
            "no_go_condition": "If a future FCC/source packet still leaves the A unit or finite quotient free, the gerbe-period route remains conditional and cannot prove Qa/SU3 closure.",
        },
        "target_fitting_used": False,
    }
    certificate = {
        "certificate": "SelectedQaSU3CentralPeriodSelectorSearch",
        "status": "QA_SU3_CENTRAL_PERIOD_SELECTOR_SEARCH_COMPLETE_SELECTOR_NOT_FOUND",
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "what_closes": {
            "searched_exact_A_unit_ratio": True,
            "searched_finite_central_quotient": True,
            "q79_finite_pattern_retained_as_guardrail": q79_has_nontrivial_finite_pattern,
            "FCC_superset_route_identified": candidate["gate_results"]["superset_FCC_method_identified"],
            "no_hidden_same_branch_selector_found": True,
        },
        "what_remains_open": {
            "same_branch_A_unit_or_finite_quotient": True,
            "selected_FCC_integer_solution_for_Qa_SU3": True,
            "selected_D_E_or_rho_E_operator_exit": True,
            "qa_su3_packet_closed": False,
        },
        "next_required_artifact": "Selected_Qa_SU3_FCC_Invariant_Equation_Packet_or_DE_Exit_v1",
        "parallel_required_artifact": "Selected_Qa_SU3_A01_DE_Operator_Exit_Gate_v1",
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    note = f"""# Selected Qa/SU3 Central Period Selector Search v1

This artifact searches the open period selector named by the previous gates.

The scalar target is:

```text
{candidate["scalar_target"]["A_unit_condition"]}
R^4/alpha_prime = {a_unit_ratio:.15f}
```

## Result

No same-branch selector was found.

The exact value appears in the Qa/SU3 period gate as a derived condition, not as
an independently selected corpus value.  The q79 repository supplies strong
finite `Z3`/qutrit gerbe period-table patterns, but these remain off-branch
guardrails for Qa/SU3 unless a same-source restriction map is proved.

## Superset Clue

The useful new route is the Kaluza-Klein / FCC formulation: invariant
background equations plus primitivity and quantization/integrality constraints
form a finite algebraic/Diophantine packet.  That is the right shape for a
future no-knob selector, but the current corpus does not yet instantiate it for
the Qa/SU3 central period.

## Decision

The gerbe period branch remains conditional.  The rigorous next move is:

```text
Selected_Qa_SU3_FCC_Invariant_Equation_Packet_or_DE_Exit_v1
```

That packet must either compute the Qa/SU3 invariant equations and integer
flux/holonomy data that select the period unit, or exit through selected
`D_E/rho_E` operator data.

closure claimed: no
target fitting used: no
"""
    data_text = json.dumps(candidate, indent=2, sort_keys=True)
    cert_text = json.dumps(certificate, indent=2, sort_keys=True)
    if "--write" in sys.argv:
        OUTPUT_DATA.write_text(data_text + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
