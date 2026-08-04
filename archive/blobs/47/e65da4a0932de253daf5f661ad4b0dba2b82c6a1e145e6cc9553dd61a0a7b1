"""Reduce the Qa/SU3 HYM mu problem to a source-selected operator gate.

The previous artifact extracted the explicit Iwasawa HYM connection matrix and
showed that it contains a positive continuous parameter mu.  This script checks
whether the corpus supplies an independent rule that selects mu or the
operator/domain needed to select it.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
HYM_CERT = (
    ROOT
    / "certificates"
    / "selected_qa_su3_hym_color_connection_spectrum_or_torsion_certificate.json"
)

CORPUS = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")
HETEROTIC_EXPLICIT = (
    CORPUS
    / "16 Strings, Flux, & M-Theory Encodings"
    / "Flux_Compactifications_in_Heterotic_String_Theory_v3.md"
)
STROMINGER_SELECTION = (
    CORPUS
    / "16 Strings, Flux, & M-Theory Encodings"
    / "Modal_Triplet_Theory__From_MTT_to_the_Strominger__Heterotic_Flux__System.md"
)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def has(path: Path, terms: list[str]) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""
    return {
        "path": str(path),
        "present": path.exists(),
        "terms_found": [term for term in terms if term in text],
        "missing_terms": [term for term in terms if term not in text],
    }


def candidate_routes() -> dict[str, Any]:
    return {
        "chern_classes_and_bianchi": {
            "status": "REJECTED_FOR_MU_SELECTION",
            "reason": (
                "The source reports c1=0, c2=0 / Tr F_E wedge F_E=0, and "
                "c3=6, while still stating F_E != 0. These are topological "
                "and anomaly data, not a nonzero-spectrum or mu-selection rule."
            ),
        },
        "li_yau_hym_uniqueness": {
            "status": "REJECTED_AS_NUMERIC_MU_RULE",
            "reason": (
                "Li-Yau uniqueness fixes the HYM connection up to unitary gauge "
                "after the holomorphic structure and metric are fixed. The "
                "explicit family still states mu>0, so this does not by itself "
                "choose one value of mu."
            ),
        },
        "unit_frobenius_or_mu_equals_one": {
            "status": "FORBIDDEN_UNSOURCED_NORMALIZATION",
            "diagnostic_equation": "2*mu + mu^2 = 3 would give mu=1",
            "reason": (
                "That is a convenient normalization, not a corpus-selected "
                "physical condition. Using it would introduce a knob unless a "
                "source rule identifies this norm."
            ),
        },
        "strominger_selection_hessian": {
            "status": "BEST_LEGAL_ROUTE_BUT_NUMERIC_DATA_OPEN",
            "selected_operator_domain_candidate": (
                "bundle Yang-Mills Laplacian Delta_A acting on u(E)-valued "
                "1-forms, modulo symmetries, with the coherent spectral "
                "projector and OU lifting terms"
            ),
            "reason": (
                "The Strominger-selection corpus states that the Hessian block "
                "for bundle variations is Delta_A on u(E)-valued 1-forms, and "
                "that OU weights can lift residual moduli. This is the first "
                "source-selected domain capable of selecting mu, but the actual "
                "eigenvalues/OU weights on the explicit Iwasawa HYM family are "
                "not supplied."
            ),
        },
        "compact_nil_reuse": {
            "status": "CONDITIONAL_COMPATIBILITY_OPEN",
            "reason": (
                "The prior Qa determinant branch lives on compact Nil Hodge data. "
                "Importing Iwasawa HYM data requires a bridge proving that the "
                "same Qa operator/domain is being evaluated."
            ),
        },
    }


def main() -> int:
    hym = load(HYM_CERT)
    explicit_check = has(
        HETEROTIC_EXPLICIT,
        [
            r"\mu>0",
            "bundle moduli enter continuously",
            "overall volume/shape modulus remains",
            "F_E\\neq 0",
            r"\mathrm{Tr}F_E\wedge F_E=0",
        ],
    )
    selection_check = has(
        STROMINGER_SELECTION,
        [
            "unique local minimizer",
            "OU term adds a positive quadratic form",
            "bundle via the Yang--Mills Laplacian",
            r"\Delta_A",
            "acting on $\\mathfrak{u}(E)$--valued 1--forms",
            "fixed gauges",
            "modulo symmetries",
        ],
    )

    output = {
        "status": "QA_SU3_HYM_OPERATOR_DOMAIN_REDUCED_MU_SELECTION_OPEN",
        "input_hym_status": hym["status"],
        "source_checks": {
            "explicit_iwasawa_hym_family": explicit_check,
            "strominger_selection_hessian": selection_check,
        },
        "candidate_routes": candidate_routes(),
        "selected_next_operator_gate": {
            "operator": "Delta_A",
            "domain": "u(E)-valued 1-forms on the Iwasawa HYM bundle, in fixed gauges and modulo symmetries",
            "selection_functional": "Strominger/MTT selection potential Xi plus coherent projector and OU lifting term",
            "representation_for_mu_lifting": "adjoint bundle End(E) / u(E), not the fundamental matter bundle E",
            "status": "DOMAIN_SELECTED_SPECTRUM_AND_OU_WEIGHTS_OPEN",
        },
        "why_mu_is_still_not_selected": [
            "The explicit Iwasawa paper states mu>0 and says bundle moduli enter continuously at this order.",
            "Chern classes, Tr F_E wedge F_E, and c3 are independent of a full spectral determinant.",
            "The Strominger selection theorem identifies the correct Hessian/operator block but does not compute the Delta_A eigenvalues or OU weights for the explicit mu-family.",
            "Choosing mu=1 by unit norm or convenience would be an unsourced normalization.",
        ],
        "remaining_required_data": [
            "write Delta_A(mu) explicitly in the invariant Iwasawa frame",
            "fix gauge and quotient symmetry directions for u(E)-valued 1-forms",
            "compute the invariant-band eigenvalues lambda_k(mu)",
            "import or derive the OU weights gamma_{n,k}^{-1}",
            "minimize the sourced Xi/Hessian contribution in mu before any Qa/SU3 residual comparison",
            "only then evaluate the zeta determinant or analytic torsion response",
        ],
        "computed_numeric_response": None,
        "verdict": {
            "mu_selected": False,
            "operator_domain_selected_for_next_gate": True,
            "representation_reduced_for_mu_lifting": "adjoint_uE_valued_one_forms",
            "selected_spectrum_or_torsion_available": False,
            "can_close_Qa_SU3_now": False,
            "target_fitting_used": False,
            "full_SM_closure_achieved": False,
            "next_required_artifact": "Selected_Qa_SU3_HYM_Delta_A_Mu_Spectrum_Computation_v1",
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
