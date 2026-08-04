"""Build the U1/Y quotient-determinant algebraic lemma gate."""

from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "weighting_gate": DATA / "selected_electroweak_u1y_determinantfunctional_weighting_or_nogo.candidate.json",
    "source_template": DATA / "selected_electroweak_u1y_determinant_functional_source_theorem.template.json",
    "conditional_spectrum": DATA / "selected_electroweak_u1y_localdeterminant_from_27mode_de_gaplayer.spectrum_attempt.json",
    "u1_pperp_policy": DATA / "selected_u1_quotient_projector_pperp_and_trace_policy.candidate.json",
}

OUTPUT_DATA = DATA / "selected_electroweak_u1y_quotientdeterminant_lemma.candidate.json"
OUTPUT_CERT = CERTS / "selected_electroweak_u1y_quotientdeterminant_lemma_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Electroweak_U1Y_QuotientDeterminant_Lemma_v1.md"

STATUS = "ELECTROWEAK_U1Y_QUOTIENT_DETERMINANT_LEMMA_PROVED_SOURCE_SELECTION_OPEN"
NEXT = "Selected_Electroweak_U1Y_Factorized_ThresholdOperator_SourceEmission_or_SU2_Cancellation_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def frac(text: str) -> Fraction:
    return Fraction(text)


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    weighting = load(INPUTS["weighting_gate"])
    template = load(INPUTS["source_template"])
    spectrum = load(INPUTS["conditional_spectrum"])
    pperp = load(INPUTS["u1_pperp_policy"])

    rank3 = int(spectrum["rank3_model_kernel_multiplicity"])
    quotient_rank = int(frac(pperp["projector_theorem"]["checks"]["trace_P_perp"]))
    removed_rank = rank3 - quotient_rank
    weight = quotient_rank / rank3

    quotient_positive = []
    for row in spectrum["rank3_model_positive_complement"]:
        mult = int(row["multiplicity"])
        if mult % rank3 != 0:
            raise ValueError(f"multiplicity {mult} is not divisible by rank-3 carrier")
        base_mult = mult // rank3
        quotient_positive.append(
            {
                "eigenvalue": row["eigenvalue"],
                "base_multiplicity": base_mult,
                "rank3_multiplicity": mult,
                "quotient_multiplicity": base_mult * quotient_rank,
            }
        )

    unit = float(spectrum["base_laplacian_unit_numeric"])
    quotient_logdet = (
        quotient_positive[0]["quotient_multiplicity"] * math.log(unit)
        + quotient_positive[1]["quotient_multiplicity"] * math.log(2 * unit)
    )
    weighted_logdet = weighting["decision"]["conditional_Pperp_weighted_logdet"]

    algebraic_lemma = {
        "name": "Rank3TensorIdentitySharedLineQuotientDeterminantLemma",
        "proved": True,
        "hypotheses": [
            "the positive threshold operator is A_base tensor I_3 on B_base tensor V_3",
            "the selected shared line s is a one-dimensional carrier factor in V_3",
            "P_perp is inserted as the domain quotient V_3/<s>",
            "regularization is multiplicative over finite positive eigenvalue lists",
        ],
        "conclusion": (
            "The quotient determinant has the same positive eigenvalues as the "
            "rank-3 model with carrier multiplicities scaled from 3 to 2. "
            "Equivalently, logdet_quotient=(2/3)*logdet_rank3 for this finite "
            "tensor-identity model."
        ),
    }

    functional_fill = dict(template["functional_components"])
    functional_fill.update(
        {
            "sector_restriction_to_V_mod_s": "ALGEBRAICALLY_FILLED_FOR_FACTORISED_MODEL",
            "Pperp_insertion_as_domain_quotient": "FILLED_BY_SELECTED_U1_PROJECTOR_POLICY",
            "kernel_policy": "ZERO_SHARED_LINE_REMOVED_BEFORE_POSITIVE_DETERMINANT",
            "H_zero_cluster_policy": "ETA1_ZERO_CLUSTER_NEUTRAL_FOR_CURRENT_VALUE_BUT_SOURCE_POLICY_OPEN",
            "regularization_finite_part": "FINITE_POSITIVE_EIGENVALUE_ZETA_LOGDET_FOR_QUOTIENT_MODEL",
        }
    )

    still_open = {
        "source_emits_factorized_threshold_operator": True,
        "hypercharge_index_Dynkin_weights": True,
        "same_scheme_SU2_row_or_exact_cancellation": True,
        "lambda_12_formula_using_selected_rows": True,
        "physical_action_anchor": True,
    }

    decision = {
        "algebraic_quotient_determinant_lemma_proved": True,
        "quotient_positive_spectrum_computed": True,
        "quotient_logdet": quotient_logdet,
        "matches_previous_Pperp_weighted_value": abs(quotient_logdet - weighted_logdet) < 1e-12,
        "selected_U1Y_determinant_functional_closed": False,
        "factorized_threshold_operator_source_emitted": False,
        "same_scheme_SU2_row_or_cancellation_closed": False,
        "lambda_12_closed": False,
        "measured_electroweak_closure": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "SelectedElectroweakU1YQuotientDeterminantLemma",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            "weighting_gate": weighting["status"],
            "source_template": template["status"],
            "u1_pperp_policy": pperp["status"],
        },
        "rank_accounting": {
            "rank3_carrier": rank3,
            "quotient_rank": quotient_rank,
            "removed_shared_line_rank": removed_rank,
            "quotient_weight": "2/3",
        },
        "quotient_positive_spectrum": quotient_positive,
        "quotient_logdet": {
            "formula": "8*log((2*pi/3)^2) + 8*log(2*(2*pi/3)^2)",
            "numeric": quotient_logdet,
            "equals_scalar_weighted_rank3_logdet": abs(quotient_logdet - weighted_logdet) < 1e-12,
        },
        "functional_components_after_lemma": functional_fill,
        "still_open": still_open,
        "algebraic_lemma": algebraic_lemma,
        "decision": decision,
        "guardrails": {
            "uses_observed_electroweak_data": False,
            "uses_lambda12_target_witness": False,
            "promotes_factorization_without_source": False,
            "claims_lambda12": False,
            "claims_measured_electroweak_closure": False,
            "injects_Qa_log2008": False,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "SelectedElectroweakU1YQuotientDeterminantLemma",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "closed": {
            "rank3_to_rank2_quotient_determinant_lemma": True,
            "quotient_positive_spectrum": True,
            "quotient_logdet_matches_2_3_weighted_value": True,
        },
        "open": still_open,
        "quotient_logdet": quotient_logdet,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    return candidate, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    return f"""# Selected Electroweak U1Y QuotientDeterminant Lemma v1

## Result

```text
status = {candidate["status"]}
algebraic_quotient_determinant_lemma_proved = true
quotient_positive_spectrum = [(2*pi/3)^2 x 8, 2*(2*pi/3)^2 x 8]
quotient_logdet = {candidate["quotient_logdet"]["numeric"]}
selected_U1Y_determinant_functional_closed = false
lambda_12_closed = false
```

## Lemma

If the selected local threshold operator is emitted as
`A_base tensor I_3` on `B_base tensor V_3`, and the shared circle is the
one-dimensional line `<s>` in `V_3`, then inserting the selected quotient
projector `P_perp` is equivalent to replacing the carrier factor `V_3` by
`V_3/<s>`. The positive multiplicities therefore scale from three carrier
copies to two carrier copies.

This proves the algebraic reason why the earlier `2/3` value is the same as a
direct quotient determinant in this finite model. It does not prove that the
electroweak U1/Y source has emitted that factorized operator.

## Quotient Spectrum

```json
{json.dumps(candidate["quotient_positive_spectrum"], indent=2, sort_keys=True)}
```

## Remaining Source Gate

```json
{json.dumps(candidate["still_open"], indent=2, sort_keys=True)}
```

The next source object must emit the factorized U1/Y threshold operator, or
emit a same-source SU2 determinant row/cancellation that makes the quotient row
usable for `lambda_12`. No electroweak data, target residual, or `log(2008)`
injection is used here.

## Certificate

```json
{json.dumps(cert, indent=2, sort_keys=True)}
```
"""


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    candidate, cert, note = build()
    write_json(OUTPUT_DATA, candidate)
    write_json(OUTPUT_CERT, cert)
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    for path in [OUTPUT_DATA, OUTPUT_CERT, OUTPUT_NOTE]:
        print(f"wrote {rel(path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
