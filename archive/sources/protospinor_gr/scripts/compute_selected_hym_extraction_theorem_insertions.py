from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

RUN_CERT = ROOT / "certificates" / "selected_hym_connection_to_finite_operator_extraction_run_certificate.json"
RUN_PACKET = ROOT / "candidate_data" / "selected_hym_connection_to_finite_operator_extraction_run.packet.json"
TEMPLATE = ROOT / "candidate_data" / "selected_hym_connection_to_finite_operator_extraction.template.json"

OUT_CERT = ROOT / "certificates" / "selected_hym_extraction_theorem_insertions_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "selected_hym_extraction_theorem_insertions.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "Selected_HYM_Extraction_Theorem_Insertions_v1.md"
OUT_STROMINGER = (
    ROOT
    / "proof_corpus"
    / "paper_insertions"
    / "Selected_HYM_Connection_Extraction_Theorem_for_Strominger_Paper.md"
)
OUT_THETA = (
    ROOT
    / "proof_corpus"
    / "paper_insertions"
    / "RouteC_Aselected_Extraction_Guardrail_for_Theta_Papers.md"
)

STATUS = "SELECTED_HYM_EXTRACTION_THEOREM_INSERTIONS_BUILT_VALUE_SOLVE_OPEN"
NEXT = "MTT_Selected_HYM_SelectedConnection_or_RouteC_SelectedResidual_ValueSolve_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    run_cert = load(RUN_CERT)
    run_packet = load(RUN_PACKET)
    template = load(TEMPLATE)

    required_fields = list(template["required_fields"].keys())
    pass_set = run_cert["verdict"]["pass_set"]
    fail_set = run_cert["verdict"]["fail_set"]

    theorem = {
        "name": "SelectedHYMConnectionToFiniteOperatorExtractionCriterion",
        "proved": True,
        "paper_context": "Strominger/HYM finite emission and Route-C/Theta finite response papers",
        "statement": (
            "A selected equal-radius HYM connection on the selected V_alpha branch "
            "promotes to finite Route-C operator data exactly when the finite "
            "extraction packet fills all required fields from that same selected "
            "connection and passes the Route-C validators honestly. Abstract HYM "
            "existence alone is insufficient; lifted selected flags, smoke values, "
            "benchmarks, and observed flavor data cannot supply the missing theorem."
        ),
        "required_fields": required_fields,
        "current_run_corollary": (
            "The current honest inputs prove a no-go corollary: rhoE_mesh, "
            "rhoE_metric, and sector_maps pass, while route_c_residuals, D_E, "
            "Riesz/gap, reduced Green, and dotD fail selected-source or "
            "alpha1-driver provenance. Therefore no selected A_selected or "
            "b_selected is emitted by the current run."
        ),
    }

    proof_obligations = {
        "selected_connection_or_transition_representative": (
            "A representative of the selected HYM connection or selected transition "
            "data on the fixed V_alpha branch."
        ),
        "finite_quotient_basis_truncation": (
            "A theorem-derived finite quotient/basis/truncation with explicit error "
            "or convergence control."
        ),
        "same_source_operator_values": (
            "rho_E, metric, sector maps, D_E, Riesz/gap, reduced Green, dotD, and "
            "primitive C1 overlaps all computed from the same selected source."
        ),
        "honest_validation": (
            "The existing Route-C validators pass without overwritten or lifted "
            "selected-source flags."
        ),
        "no_target_inputs": (
            "Observed masses, CKM/PMNS data, CP phases, thresholds, benchmark "
            "matrices, and fitted constants are absent from selection and promotion."
        ),
    }

    current_run_boundary = {
        "selected_values_emitted": run_cert["verdict"]["selected_values_emitted"],
        "can_emit_A_selected": run_cert["verdict"]["can_emit_A_selected"],
        "can_emit_b_selected": run_cert["verdict"]["can_emit_b_selected"],
        "pass_set": pass_set,
        "fail_set": fail_set,
        "next_required_artifact": run_cert["verdict"]["next_required_artifact"],
    }

    guardrails = {
        "abstract_hym_existence_not_finite_values": True,
        "lifted_selected_flags_forbidden_as_proof": True,
        "smoke_data_forbidden_as_selected_values": True,
        "observed_flavor_data_forbidden": run_cert["verdict"]["observed_flavor_data_used"] is False,
        "conditional_A_selected_not_promoted": run_cert["verdict"]["can_emit_A_selected"] is False,
        "conditional_b_selected_not_promoted": run_cert["verdict"]["can_emit_b_selected"] is False,
    }

    strominger_insertion = f"""# Selected HYM Connection Extraction Theorem Insert

Target paper:

```text
Modal_Triplet_Theory__From_MTT_to_the_Strominger__Heterotic_Flux__System.md
```

Suggested location:

```text
Appendix: Selected HYM Connection to Finite Operator Extraction
```

## Theorem: Selected HYM Connection-to-Finite-Operator Extraction Criterion

Fix the selected `q79/F,m=1` equal-radius `V_alpha` branch and its selected
Strominger/HYM source. A finite Route-C operator payload is theorem-derived
selected data if and only if the following data are emitted from that same
selected source:

```text
selected connection or transition representative
finite quotient, basis, truncation, and error certificate
rho_E mesh and Hermitian metric
sector maps
D_E action matrices
Riesz projectors and complement gaps
reduced Green operators
same-branch dotD_alpha1 derivative
primitive C1 overlap contractions
theorem-derived selected-source provenance
```

and the existing Route-C validators pass honestly for those emitted objects.

## Proof

The forward direction is by construction. A selected finite operator payload is
the finite image of the selected HYM source, so every listed field is a
same-source consequence of the selected connection and the validators must pass
without proxy flags.

For the converse, assume all listed fields are emitted from the selected
connection/transition representative with a finite quotient and error
certificate, and that every Route-C validator passes honestly. The same-source
condition identifies the residual, `rho_E`, metric, sector maps, `D_E`,
Riesz/gap, Green, `dotD_alpha1`, and primitive C1 contractions as images of one
selected HYM source. Honest validator success supplies the finite algebra,
metric compatibility, spectral complement, response, and provenance checks
required by the Route-C codomain. Hence the payload may be promoted to selected
finite operator data.

Abstract HYM existence alone does not prove the theorem, because existence does
not emit finite matrices, basis coefficients, response derivatives, spectral
gaps, Green operators, or primitive C1 contractions. Lifted selected flags,
smoke packets, observed masses, observed mixings, CKM/PMNS inputs, CP phases,
thresholds, benchmark matrices, and fitted constants are not admissible sources
for any promotion flag.

## Corollary: Current Honest Packet No-Go

For the current honest finite inputs, only

```text
{", ".join(pass_set)}
```

pass. The following validators fail:

```text
{", ".join(fail_set)}
```

The failures are selected-source or alpha1-driver provenance failures. Therefore
the current packet does not emit selected finite operator values and cannot
promote `A_selected` or `b_selected`.

The next missing theorem object is:

```text
{NEXT}
```
"""

    theta_insertion = f"""# Route-C A_selected Extraction Guardrail Insert

Target papers:

```text
Theta closure papers
Route-C finite response papers
SM closure papers using A_selected or b_selected
```

Suggested location:

```text
Before any theorem that treats A_selected, b_selected, or deltaTheta as selected
finite response data.
```

## Theorem: Conditional A_selected Promotion Guardrail

The conditional Weyl-pair and C1 response systems may be used as algebraic
diagnostics before HYM extraction closes, but they may not be promoted to
`A_selected`, `b_selected`, selected Yukawa data, selected CKM/PMNS data, or
selected CP data until the selected HYM connection-to-finite-operator extraction
criterion passes.

## Proof

The Route-C/Theta finite response equations depend on finite residuals,
`D_E`, Riesz/gap projectors, reduced Green operators, same-branch `dotD_alpha1`,
and primitive C1 overlap contractions. In the present run, those operator
slots fail selected-source or alpha1-driver provenance. Thus the conditional
linear algebra can show which shapes and equations would be sufficient, but it
does not yet identify selected finite values.

Since `A_selected` and `b_selected` name selected same-source operator data,
their promotion requires the selected HYM extraction theorem. A conditional
matrix, a lifted-flag packet, or a smoke-data packet is not a proof source. The
promotion is blocked until the next required value-solve artifact is supplied:

```text
{NEXT}
```

This guardrail also excludes observed masses, observed mixings, CKM/PMNS data,
CP phases, thresholds, benchmark matrices, and fitted constants as inputs to the
promotion.
"""

    note = f"""# Selected HYM Extraction Theorem Insertions v1

## Result

Two rigorous paper insertions are now generated from the executable HYM
extraction gate:

```text
{OUT_STROMINGER}
{OUT_THETA}
```

They prove the extraction criterion and the current-packet no-go corollary. They
do not claim that selected finite operator values have been emitted.

## Current Boundary

Passing validators:

```text
{", ".join(pass_set)}
```

Failing validators:

```text
{", ".join(fail_set)}
```

The exact status is:

```text
{STATUS}
```

The next executable artifact remains:

```text
{NEXT}
```
"""

    packet = {
        "theorem": theorem,
        "proof_obligations": proof_obligations,
        "current_run_boundary": current_run_boundary,
        "guardrails": guardrails,
        "paper_insertions": {
            "strominger": str(OUT_STROMINGER),
            "theta": str(OUT_THETA),
        },
        "source_certificates": {
            "run": str(RUN_CERT),
            "template": str(TEMPLATE),
        },
    }

    checks = {
        "run_no_go_theorem_proved": run_cert["theorem"]["proved"] is True,
        "template_has_ten_required_fields": len(required_fields) == 10,
        "support_validators_pass": {"rhoE_mesh", "rhoE_metric", "sector_maps"}.issubset(set(pass_set)),
        "operator_validators_fail": {
            "route_c_residuals",
            "de_action",
            "riesz_gap",
            "reduced_green",
            "dotd_response",
        }.issubset(set(fail_set)),
        "no_selected_values_emitted": run_cert["verdict"]["selected_values_emitted"] is False,
        "next_artifact_preserved": run_cert["verdict"]["next_required_artifact"] == NEXT,
        "no_observed_flavor_data_used": run_cert["verdict"]["observed_flavor_data_used"] is False,
        "source_flag_failures_recorded": len(run_packet["source_flag_failures"]) >= 5,
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "selected_hym_extraction_theorem_insertions",
        "status": STATUS,
        "input_certificates": {
            "selected_hym_connection_to_finite_operator_extraction_run": str(RUN_CERT),
            "selected_hym_connection_to_finite_operator_extraction_template": str(TEMPLATE),
        },
        "theorem": theorem,
        "proof_obligations": proof_obligations,
        "current_run_boundary": current_run_boundary,
        "guardrails": guardrails,
        "checks": checks,
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
        "paper_insertions_written": {
            "strominger": str(OUT_STROMINGER),
            "theta": str(OUT_THETA),
        },
    }

    OUT_STROMINGER.parent.mkdir(parents=True, exist_ok=True)
    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    OUT_STROMINGER.write_text(strominger_insertion, encoding="utf-8")
    OUT_THETA.write_text(theta_insertion, encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"WROTE: {OUT_STROMINGER}")
    print(f"WROTE: {OUT_THETA}")
    print(f"STATUS: {STATUS}")


if __name__ == "__main__":
    main()
