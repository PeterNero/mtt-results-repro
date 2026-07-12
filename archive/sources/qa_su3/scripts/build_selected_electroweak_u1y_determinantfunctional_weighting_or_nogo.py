"""Build the U1/Y determinant-functional weighting or no-go gate."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "localdet_gate": DATA / "selected_electroweak_u1y_localdeterminant_from_27mode_de_gaplayer.candidate.json",
    "conditional_spectrum": DATA / "selected_electroweak_u1y_localdeterminant_from_27mode_de_gaplayer.spectrum_attempt.json",
    "u1_pperp_policy": DATA / "selected_u1_quotient_projector_pperp_and_trace_policy.candidate.json",
    "operator_emission": DATA / "selected_u1y_routec_operator_emission_overlap_from_terminal_slotmap.candidate.json",
    "primitive_lambda_gate": DATA / "selected_u1y_routec_primitive_c1_contractions_or_lambda12_gate.candidate.json",
}

OUTPUT_DATA = DATA / "selected_electroweak_u1y_determinantfunctional_weighting_or_nogo.candidate.json"
OUTPUT_CERT = CERTS / "selected_electroweak_u1y_determinantfunctional_weighting_or_nogo_certificate.json"
OUTPUT_TEMPLATE = DATA / "selected_electroweak_u1y_determinant_functional_source_theorem.template.json"
OUTPUT_NOTE = PROOF / "Selected_Electroweak_U1Y_DeterminantFunctional_Weighting_or_NoGo_v1.md"

STATUS = "ELECTROWEAK_U1Y_DETERMINANT_FUNCTIONAL_WEIGHTING_NOGO_SOURCE_THEOREM_REQUIRED"
NEXT = "Selected_Electroweak_U1Y_DeterminantFunctional_SourceTheorem_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def as_float_fraction(text: str) -> float:
    return float(Fraction(text))


def build_template(required: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema": "SelectedElectroweakU1YDeterminantFunctionalSourceTheorem.v1",
        "status": "OPEN_SELECTED_U1Y_DETERMINANT_FUNCTIONAL_SOURCE_THEOREM_REQUIRED",
        "source_identity": {
            "selected_by_mtt": None,
            "same_source_as_27mode_DE_gap_layer": None,
            "emitted_before_electroweak_comparison": None,
            "source_certificate": None,
        },
        "functional_components": {
            "sector_restriction_to_V_mod_s": None,
            "Pperp_insertion_as_domain_quotient": None,
            "kernel_policy": None,
            "H_zero_cluster_policy": None,
            "hypercharge_index_Dynkin_weights": None,
            "regularization_finite_part": None,
            "same_scheme_SU2_row_or_cancellation": None,
            "lambda12_formula": None,
        },
        "acceptance_contract": required["must_select"],
        "forbidden_inputs": required["must_not_use"],
    }


def build() -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], str]:
    localdet = load(INPUTS["localdet_gate"])
    spectrum = load(INPUTS["conditional_spectrum"])
    pperp = load(INPUTS["u1_pperp_policy"])
    operator_emission = load(INPUTS["operator_emission"])
    primitive_lambda = load(INPUTS["primitive_lambda_gate"])

    logdet = spectrum["conditional_zeta_logdet_positive_complement"]["numeric"]
    pperp_weight = as_float_fraction(pperp["decision"]["selected_U1_index"])
    weighted_logdet = pperp_weight * logdet

    candidate_weighting_tests = {
        "unweighted_rank3_positive_complement": {
            "candidate_finite_part": logdet,
            "status": "REJECTED_AS_UNSELECTED_U1Y_FUNCTIONAL",
            "reason": "The full rank-3 complement spectrum is a model D_E support object. The selected U1 threshold trace theorem says the U1 trace is on V/<s>, not the full rank-3 carrier.",
        },
        "Pperp_weighted_rank3_complement": {
            "candidate_weight": pperp["decision"]["selected_U1_index"],
            "candidate_finite_part": weighted_logdet,
            "status": "CONDITIONAL_MOST_NATURAL_NOT_SELECTED_FINITE_PART",
            "reason": "P_perp selects the quotient index 2/3, so this is the natural conditional weighting. But no source theorem says the zeta determinant finite part is obtained by scalar-multiplying the rank-3 logdet by Tr(Pperp)/Tr(I).",
        },
        "H_zero_cluster_eta1_inclusion": {
            "candidate_delta": 0.0,
            "status": "NEUTRAL_FOR_ETA1_BUT_POLICY_STILL_OPEN",
            "reason": "The current selected eta_N=1 contributes 2*log(1)=0 if included, but policy selection is still required because future nonunit corrections or SU2 matching may depend on the inclusion theorem.",
        },
        "same_scheme_SU2_cancellation": {
            "status": "OPEN",
            "reason": "SU2 weak-split unit index is closed, but no same-scheme SU2 determinant spectrum/finite part or exact cancellation theorem has been emitted.",
        },
        "lambda12_from_conditional_weight": {
            "candidate_U1_finite_part": weighted_logdet,
            "status": "FORBIDDEN_DIAGNOSTIC_ONLY",
            "reason": "The U1 finite part is not selected, and the SU2 same-scheme row is open, so lambda_12 cannot be computed from this conditional weight.",
        },
    }

    selected_support = {
        "Pperp_domain_policy_closed": pperp["decision"]["U1_operator_trace_uses_P_perp"],
        "selected_U1_index": pperp["decision"]["selected_U1_index"],
        "operator_emission_closed_functionally": operator_emission["decision"]["same_branch_functional_operator_emission_closed"],
        "selected_overlap_normalization_emitted": operator_emission["decision"]["selected_overlap_normalization_emitted"],
        "conditional_27mode_positive_complement_available": localdet["decision"]["positive_model_complement_spectrum_available"],
    }

    blocking_no_go = {
        "scope": "current corpus and current same-source artifacts",
        "reason": (
            "The current source closes the quotient domain policy and a conditional "
            "27-mode D_E spectrum, but it does not emit the determinant functional "
            "mapping D_E support to U1/Y finite part."
        ),
        "missing": [
            "source theorem that determinant log finite parts weight by Pperp trace, or an alternative non-scalar quotient determinant",
            "source-selected hypercharge/index/Dynkin determinant weights",
            "kernel/H-zero policy theorem",
            "same-scheme SU2 determinant finite part or exact cancellation theorem",
            "regularization theorem for the finite zeta/heat/torsion part on V/<s>",
        ],
        "not_a_mathematical_impossibility": True,
    }

    required = localdet["required_functional"]
    template = build_template(required)

    decision = {
        "determinant_functional_source_theorem_found": False,
        "Pperp_weighting_promoted": False,
        "conditional_Pperp_weighted_logdet_computed": True,
        "conditional_Pperp_weighted_logdet": weighted_logdet,
        "same_scheme_SU2_row_or_cancellation_closed": False,
        "lambda_12_closed": False,
        "measured_electroweak_closure": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "SelectedElectroweakU1YDeterminantFunctionalWeightingOrNoGo",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            "localdet_gate": localdet["status"],
            "u1_pperp_policy": pperp["status"],
            "operator_emission": operator_emission["status"],
            "primitive_lambda_gate": primitive_lambda["status"],
        },
        "selected_support": selected_support,
        "candidate_weighting_tests": candidate_weighting_tests,
        "blocking_no_go": blocking_no_go,
        "source_theorem_template_path": rel(OUTPUT_TEMPLATE),
        "decision": decision,
        "theorem": {
            "name": "ElectroweakU1YDeterminantFunctionalWeightingCurrentSourceNoGo",
            "proved": True,
            "statement": (
                "In the current corpus, the selected P_perp trace policy and the "
                "27-mode D_E positive complement do not suffice to select a U1/Y "
                "determinant finite part. The scalar 2/3 weighting is the natural "
                "conditional candidate, but promoting it requires a same-source "
                "determinant-functional theorem. Therefore lambda_12 remains open."
            ),
        },
        "guardrails": {
            "uses_observed_electroweak_data": False,
            "uses_lambda12_target_witness": False,
            "promotes_Pperp_weight_as_logdet_theorem": False,
            "promotes_conditional_logdet_to_prediction": False,
            "injects_Qa_log2008": False,
            "claims_lambda12": False,
            "claims_measured_electroweak_closure": False,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "SelectedElectroweakU1YDeterminantFunctionalWeightingOrNoGo",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "template_path": rel(OUTPUT_TEMPLATE),
        "note_path": rel(OUTPUT_NOTE),
        "closed": {
            "current_source_no_go_for_weighting_promotion": True,
            "conditional_Pperp_weighted_logdet_computed": True,
            "minimal_source_theorem_template_written": True,
        },
        "open": {
            "selected_U1Y_determinant_functional": True,
            "same_scheme_SU2_row_or_cancellation": True,
            "lambda_12": True,
            "measured_electroweak_closure": True,
        },
        "conditional_Pperp_weighted_logdet": weighted_logdet,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    return candidate, cert, template, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    return f"""# Selected Electroweak U1Y DeterminantFunctional Weighting or NoGo v1

## Result

```text
status = {candidate["status"]}
determinant_functional_source_theorem_found = false
Pperp_weighting_promoted = false
conditional_Pperp_weighted_logdet = {candidate["decision"]["conditional_Pperp_weighted_logdet"]}
lambda_12_closed = false
```

## Candidate Tests

```json
{json.dumps(candidate["candidate_weighting_tests"], indent=2, sort_keys=True)}
```

## Current Source No-Go

```json
{json.dumps(candidate["blocking_no_go"], indent=2, sort_keys=True)}
```

## Next

```text
{candidate["decision"]["next_required_artifact"]}
```

The natural candidate is now clear: apply the selected `P_perp` quotient policy
as a determinant-functional weighting to the 27-mode positive complement. But
this is still a conditional candidate, not a theorem. The next artifact must
derive that determinant functional from the source or replace it with a
non-scalar quotient determinant.

## Certificate

```json
{json.dumps(cert, indent=2, sort_keys=True)}
```
"""


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    candidate, cert, template, note = build()
    write_json(OUTPUT_DATA, candidate)
    write_json(OUTPUT_CERT, cert)
    write_json(OUTPUT_TEMPLATE, template)
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    for path in [OUTPUT_DATA, OUTPUT_CERT, OUTPUT_TEMPLATE, OUTPUT_NOTE]:
        print(f"wrote {rel(path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
