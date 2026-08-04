"""Build the c-twist period-normalization gate or A01 exit decision."""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")

NORMALIZATION = DATA / "complex_rotated_ctwist_normalization.candidate.json"
TRANSGRESSION = DATA / "ctwist_transgression_pairing_computation.candidate.json"
OUTPUT_DATA = DATA / "ctwist_period_normalization_or_a01_exit.candidate.json"
OUTPUT_CERT = CERTS / "ctwist_period_normalization_or_a01_exit_certificate.json"

SOURCES = {
    "iwasawa_flux": OBSIDIAN
    / "16 Strings, Flux, & M-Theory Encodings"
    / "Flux_Compactifications_in_Heterotic_String_Theory_v3.md",
    "m_theory_integrality": OBSIDIAN
    / "16 Strings, Flux, & M-Theory Encodings"
    / "Modal_Triplet_Theory__From_MTT_to_M_theory.md",
    "q79_s3": Q79 / "proof_corpus" / "Visible_Twisted_S3_Class_Restriction_Closure_v1.md",
}


def scan(path: Path, terms: dict[str, str]) -> dict[str, object]:
    if not path.exists():
        return {"path": str(path), "present": False, "terms": {key: False for key in terms}}
    text = path.read_text(encoding="utf-8", errors="ignore").lower()
    return {
        "path": str(path),
        "present": True,
        "terms": {key: term.lower() in text for key, term in terms.items()},
    }


def evidence_row(
    route_id: str,
    verdict: str,
    closes: list[str],
    obstruction: list[str],
    promotes_period_unit: bool,
) -> dict[str, object]:
    return {
        "route_id": route_id,
        "verdict": verdict,
        "what_it_closes": closes,
        "obstruction_to_period_promotion": obstruction,
        "promotes_A_unit_or_finite_quotient": promotes_period_unit,
    }


def main() -> None:
    prior = json.loads(NORMALIZATION.read_text(encoding="utf-8"))
    transgression = json.loads(TRANSGRESSION.read_text(encoding="utf-8"))
    scans = {
        "iwasawa_flux": scan(
            SOURCES["iwasawa_flux"],
            {
                "trace_normalization": "\\mathrm{Tr}(T^2)=1",
                "integral_F_over_2pi": "integral periods of $F/2\\pi$",
                "r3_formula": "r_3^2 = \\frac{8(2\\pi)^2",
                "flux_quantization_automatic": "Flux quantization is automatic",
                "H_integral_periods": "has integral periods",
                "continuous_modulus_remains": "an overall volume/shape modulus remains",
                "large_volume_regime": "large volume and small flux",
            },
        ),
        "m_theory_integrality": scan(
            SOURCES["m_theory_integrality"],
            {
                "integral_lattice": "fixes an integral cohomology lattice",
                "shifted_quantization": "[G_4/2\\pi]-\\frac12\\lambda",
                "discrete_vacua": "Flux quantisation and the tadpole condition restrict",
            },
        ),
        "q79_s3": scan(
            SOURCES["q79_s3"],
            {
                "torsion_label": "torsion label m = 1",
                "finite_table": "F_3^2",
                "central_cocycle": "qutrit central cocycle",
            },
        ),
    }

    # Isotropic branch from the Iwasawa flux paper:
    # r1=r2=R and r3^2 = 8(2pi)^2 / (16/alpha' + 8/R^4).
    # The suppressed transgression scale is A = r3/(r1*r2) = r3/R^2.
    scalar_gate = {
        "branch": "isotropic_iwasawa_r1_eq_r2_eq_R",
        "r3_squared": "8*(2*pi)^2 / (16/alpha_prime + 8/R^4)",
        "A_squared": "(r3/R^2)^2 = (2*pi)^2 / (1 + 2*R^4/alpha_prime)",
        "A_unit_condition": "A=1 iff R^4 = alpha_prime*((2*pi)^2 - 1)/2",
        "numeric_R4_over_alpha_prime_for_A_unit": ((2 * math.pi) ** 2 - 1) / 2,
        "selected_by_current_corpus": False,
    }
    normalization_routes = [
        evidence_row(
            "iwasawa_flux_integral_periods",
            "INTEGRAL_LATTICE_YES_UNIT_NOT_SELECTED",
            [
                "The flux paper fixes trace conventions and integral-period language.",
                "The selected H/Iwasawa flux branch is globally meaningful as a gerbe source.",
                "The isotropic branch yields an explicit scalar condition for A=1.",
            ],
            [
                "The paper says an overall volume/shape modulus remains in the invariant first-order analysis.",
                "No MTT certificate selects R^4/alpha' = ((2*pi)^2-1)/2 for this Qa/SU3 branch.",
                "Integral periods alone give a lattice, not the primitive-period unit for the c-twist quotient.",
            ],
            False,
        ),
        evidence_row(
            "m_theory_integrality_lattice",
            "ABSTRACT_INTEGRALITY_GUARDRAIL_ONLY",
            [
                "The M-theory lift supports integral cohomology lattice selection in topological sectors.",
                "It is compatible with looking for a discrete period selector rather than fitting a real parameter.",
            ],
            [
                "No pushdown map from the M-theory integral class to the Qa/SU3 c-twist central quotient is supplied.",
                "No finite quotient or primitive generator value is computed for the present packet.",
            ],
            False,
        ),
        evidence_row(
            "q79_s3_finite_torsion",
            "OFF_BRANCH_PATTERN_ONLY",
            [
                "q79/S3 remains the strongest example of finite torsion normalization and central cocycle typing.",
            ],
            [
                "It is selected for q79/S3, not for the Qa/SU3 Iwasawa monad packet.",
                "Direct import would mix branches.",
            ],
            False,
        ),
        evidence_row(
            "a01_de_operator_exit",
            "LIVE_REQUIRED_EXIT_IF_PERIOD_SELECTOR_MISSING",
            [
                "Avoids needing an unproved Deligne period selector.",
                "Can certify the packet through selected operator matrices instead of gerbe promotion.",
            ],
            [
                "Requires selected A01/D_E matrices, twisted section bases, and one spectral/rho_E/heat exit.",
            ],
            False,
        ),
    ]
    period_selector_found = any(item["promotes_A_unit_or_finite_quotient"] for item in normalization_routes)
    candidate = {
        "candidate": "SelectedQaSU3CTwistPeriodNormalizationOrA01Exit",
        "status": "CTWIST_PERIOD_NORMALIZATION_SCALAR_GATE_DERIVED_SELECTOR_OPEN_A01_EXIT_REQUIRED",
        "input_statuses": {
            "complex_rotated_normalization": prior["status"],
            "transgression": transgression["status"],
        },
        "source_scans": scans,
        "scalar_period_gate": scalar_gate,
        "normalization_route_tests": normalization_routes,
        "decision": {
            "period_selector_found": period_selector_found,
            "period_selector_open_not_contradicted": True,
            "gerbe_route_retired": False,
            "reason": "The corpus supplies integral-period and finite-torsion patterns, and the transgression scale can be reduced to one explicit scalar condition, but no same-branch MTT selector fixes that scalar or finite quotient for Qa/SU3.",
            "best_next_move": "Search or derive a same-branch selector for R^4/alpha_prime or a finite central quotient; in parallel build the A01/D_E operator exit.",
        },
        "gate_results": {
            "primitive_scaled_ctwist_available": prior["gate_results"]["conditional_c_plus_minus_one_normalization"],
            "absolute_A_unit_condition_derived": True,
            "absolute_A_unit_condition_selected": False,
            "finite_quotient_same_branch_selected": False,
            "period_normalization_promoted": False,
            "A01_DE_exit_required": True,
            "closure_claimed": False,
        },
        "next_required_artifact": "Selected_Qa_SU3_A01_DE_Operator_Exit_v1",
        "parallel_search_artifact": "Selected_Qa_SU3_Central_Period_Selector_Search_v1",
        "target_fitting_used": False,
    }
    certificate = {
        "certificate": "SelectedQaSU3CTwistPeriodNormalizationOrA01Exit",
        "status": "QA_SU3_CTWIST_PERIOD_NORMALIZATION_SCALAR_GATE_DERIVED_SELECTOR_OPEN_A01_EXIT_REQUIRED",
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "what_closes": {
            "absolute_period_scale_reduced_to_scalar_A_unit_condition": True,
            "isotropic_iwasawa_A_unit_equation_derived": True,
            "integral_periods_do_not_by_themselves_select_primitive_c_unit": True,
            "q79_s3_kept_as_guardrail_not_imported": True,
            "A01_DE_exit_marked_required": True,
        },
        "what_remains_open": {
            "same_branch_selector_for_R4_over_alpha_prime_or_A_unit": True,
            "same_branch_finite_central_quotient": True,
            "explicit_Deligne_Cech_source_values": True,
            "Freed_Witten_Bianchi_for_mapped_module": True,
            "selected_A01_DE_operator_matrices": True,
            "qa_su3_packet_closed": False,
        },
        "next_required_artifact": candidate["next_required_artifact"],
        "parallel_search_artifact": candidate["parallel_search_artifact"],
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
