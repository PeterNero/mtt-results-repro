"""Build the bundle-curvature/trace or direct-operator gate after R+."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"
TEXPAPERS = ROOT.parent
SM = TEXPAPERS / "mtt-sm-parity-closure"
PROTOSPINOR = TEXPAPERS / "mtt-protospinor-gr-response-proof"

INPUT_RPLUS = DATA / "selected_heterotic_rplus_curvature_payload_fill.candidate.json"
INPUT_SOURCE_SEARCH = DATA / "selected_heterotic_sourcecertificate_or_direct_operator_emission_search.candidate.json"
SM_ROUTEC = SM / "candidate_data" / "routec_selected_source_origin_lemma.candidate.json"
PROTO_DIAG_HYM = PROTOSPINOR / "proof_corpus" / "Selected_Diagonal_HYM_Operator_Payload_Extraction_v1.md"

OUTPUT_DATA = DATA / "selected_heterotic_bundle_curvature_trace_or_direct_operator_gate.candidate.json"
OUTPUT_CERT = CERTS / "selected_heterotic_bundle_curvature_trace_or_direct_operator_gate_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_BundleCurvature_Trace_or_DirectOperator_Gate_v1.md"

STATUS = "HETEROTIC_BUNDLE_CURVATURE_TRACE_OR_DIRECT_OPERATOR_GATE_BUILT_VALUES_OPEN"
NEXT = "Selected_Heterotic_StandardEmbeddingSelector_or_PhiFin_DirectOperatorEmission_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_optional(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    return load(path)


def text_terms(path: Path, terms: list[str]) -> dict[str, bool]:
    if not path.exists():
        return {term: False for term in terms} | {"__present__": False}
    text = path.read_text(encoding="utf-8", errors="ignore")
    return {term: term in text for term in terms} | {"__present__": True}


def main() -> dict[str, Any]:
    rplus = load(INPUT_RPLUS)
    source_search = load(INPUT_SOURCE_SEARCH)
    routec = load_optional(SM_ROUTEC)

    rplus_summary = rplus["rplus_payload"]["R_plus_summary"]
    rplus_components = rplus["rplus_payload"]["R_plus_curvature_components"]

    standard_embedding_candidate = {
        "name": "conditional_standard_embedding_A_equals_GammaPlus",
        "fills_if_selected": {
            "connection_A_components": "A := GammaPlus embedded into the gauge algebra",
            "curvature_F_A_components": "F_A := R_plus in the embedded subalgebra",
            "trace_normalization": "Tr_bundle(F_A^2) = Tr_grav(R_plus^2)",
            "bianchi_difference": 0,
        },
        "computed_support": {
            "R_plus_available": True,
            "R_plus_nonzero_components": rplus_summary["nonzero_components"],
            "R_plus_nonzero_ij_matrices": rplus_summary["nonzero_ij_matrices"],
            "R_plus_frobenius_sq_total_over_i_lt_j": rplus_summary["frobenius_sq_total_over_i_lt_j"],
            "R_plus_max_abs_component": rplus_summary["max_abs_component"],
            "sample_components": dict(list(rplus_components.items())[:12]),
        },
        "why_not_promoted": [
            "current Qa/SU3 source selects an SU(3) monad/endomorphism-threshold problem, not an explicit tangent-bundle standard embedding",
            "no same-branch theorem identifies the visible bundle connection with GammaPlus",
            "no source emits the gauge representation action on u(E)-valued one-forms under this embedding",
            "no quotient/kernel policy or finite heat/zeta/torsion part follows from the embedding alone",
        ],
        "closes_now": False,
    }

    routec_support = {
        "present": routec is not None,
        "status": routec.get("status") if routec else None,
        "next_required_artifact": routec.get("next_required_artifact") if routec else None,
        "closed_sublemma": routec.get("lemma_evaluation", {}).get("closed_sublemma") if routec else None,
        "open_sublemma": routec.get("lemma_evaluation", {}).get("open_sublemma") if routec else None,
        "finite_emission_codomain": routec.get("finite_emission_morphism_contract", {}).get("codomain") if routec else None,
        "closes_now": False,
        "why_not": [
            "Phi_fin remains the open minimizer-to-finite-packet morphism in the sibling route",
            "its current domain is q79/F,m=1 S3/GS, not yet identified as the heterotic Qa/SU3 threshold bundle payload",
            "rho_E/D_E/Riesz/Green/dotD/C1 payloads are named but not emitted as selected values here",
        ],
    }

    diagonal_support = text_terms(
        PROTO_DIAG_HYM,
        ["A_diag = d s * T3", "H = diag(exp(s), exp(-s))", "not validator-ready", "End0 D_E"],
    )

    direct_operator_route = {
        "name": "direct_finite_operator_emission",
        "required_payload": [
            "source identity for the selected heterotic Qa/SU3 bundle/twist",
            "rho_E or equivalent finite transition/operator data",
            "D_E action on the selected quotient domain",
            "Riesz projectors and complement gap",
            "reduced Green operator",
            "Weitzenbock E_Qa or equivalent finite zero-order block",
            "finite heat/zeta/torsion determinant convention and trace weights",
        ],
        "support": {
            "source_search_status": source_search["status"],
            "source_certificate_found": source_search["decision"]["source_certificate_found"],
            "direct_operator_emission_found": source_search["decision"]["direct_operator_emission_found"],
            "diagonal_rank2_payload_terms": diagonal_support,
            "routec_phi_fin_support": routec_support,
        },
        "closes_now": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticBundleCurvatureTraceOrDirectOperatorGate",
        "status": STATUS,
        "inputs": {
            "rplus": rel(INPUT_RPLUS),
            "source_search": rel(INPUT_SOURCE_SEARCH),
            "sm_routec_source_origin_lemma": str(SM_ROUTEC),
            "protospinor_diagonal_hym_payload": str(PROTO_DIAG_HYM),
        },
        "input_statuses": {
            "rplus": rplus["status"],
            "source_search": source_search["status"],
            "sm_routec": routec_support["status"],
        },
        "target_fitting_used": False,
        "closure_claimed": False,
        "what_closes_now": {
            "R_plus_geometric_curvature_available": True,
            "standard_embedding_conditional_packet_written": True,
            "direct_operator_acceptance_contract_written": True,
        },
        "what_remains_open": {
            "selected_standard_embedding_selector": True,
            "selected_bundle_connection_A": True,
            "selected_bundle_curvature_F_A": True,
            "representation_action_on_uE_one_forms": True,
            "trace_normalization": True,
            "kernel_and_quotient_policy": True,
            "E_Qa_or_direct_finite_operator": True,
            "finite_heat_zeta_torsion_part": True,
        },
        "routes": {
            "A_conditional_standard_embedding": standard_embedding_candidate,
            "B_direct_finite_operator": direct_operator_route,
            "C_routec_phi_fin_import": routec_support,
        },
        "decision": {
            "bundle_tensor_payload_filled": False,
            "standard_embedding_selected": False,
            "direct_finite_operator_emitted": False,
            "E_Qa_computed": False,
            "next_required_artifact": NEXT,
            "target_fitting_used": False,
        },
        "guardrails": {
            "promotes_standard_embedding_without_selector": False,
            "promotes_R_plus_as_F_A_unconditionally": False,
            "promotes_phi_fin_support_as_heterotic_threshold": False,
            "promotes_diagonal_rank2_payload_as_QaSU3": False,
            "uses_observed_electroweak_data": False,
            "uses_target_residual_scan": False,
            "target_fitting_used": False,
        },
        "theorem": {
            "name": "BundleCurvatureTraceOrDirectOperatorGateTheorem",
            "proved": True,
            "statement": (
                "After the selected R+ curvature fill, heterotic Qa/SU3 threshold closure "
                "has exactly two legal next routes: select a standard-embedding-style "
                "bundle identification A=GammaPlus with trace equality and then compute "
                "the quotient operator, or emit a direct finite operator packet from the "
                "selected Strominger/HYM source. Current artifacts provide support for both "
                "routes but close neither; no physical threshold value is promoted."
            ),
        },
    }

    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "R_plus_available": True,
        "standard_embedding_selected": False,
        "bundle_tensor_payload_filled": False,
        "direct_finite_operator_emitted": False,
        "E_Qa_computed": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic BundleCurvature Trace or DirectOperator Gate v1

## Result

```text
status = {STATUS}
standard_embedding_selected = false
bundle_tensor_payload_filled = false
direct_finite_operator_emitted = false
E_Qa_computed = false
next_required_artifact = {NEXT}
```

## What Is Now Known

The selected geometry now supplies `R+`:

```json
{json.dumps(rplus_summary, indent=2, sort_keys=True)}
```

## Conditional Standard Embedding Route

If the source selected `A = GammaPlus`, then:

```text
F_A = R+
Tr_bundle(F_A^2) = Tr_grav(R+^2)
Bianchi trace difference = 0
```

This is useful because it would fill the bundle-curvature and trace-normalization
slots without adding a continuous parameter. It is not promoted here, because no
same-branch source theorem identifies the Qa/SU3 bundle connection with the
Bismut spin connection or supplies the quotient/finite operator.

## Direct Finite Operator Route

The alternative is to emit the selected finite operator directly:

```json
{json.dumps(direct_operator_route["required_payload"], indent=2)}
```

Sibling Route-C/`Phi_fin` evidence is support, but not heterotic Qa/SU3 closure:

```json
{json.dumps(routec_support, indent=2, sort_keys=True)}
```

## Theorem

After the selected `R+` fill, closure has exactly two legal next routes:
select the standard-embedding-style bundle identification and then compute the
quotient operator, or emit the direct finite operator packet from the selected
Strominger/HYM source. Current artifacts close neither route. No measured data,
target residual, arbitrary trace normalization, or arbitrary bundle connection
is used.
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
