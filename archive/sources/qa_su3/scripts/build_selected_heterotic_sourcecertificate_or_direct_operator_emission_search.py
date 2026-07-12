"""Build the heterotic source-certificate or direct-operator-emission search gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"
NONSM = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-nonsm-constants-no-knob")
PROTO = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-protospinor-gr-response-proof")
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")

INPUTS = {
    "value_fill": DATA / "selected_heterotic_endomorphism_threshold_valuepacket_fill.candidate.json",
    "analytic_payload": DATA / "selected_heterotic_strominger_analytic_torsion_or_threshold_operator_payload.candidate.json",
    "hym_ou_completion": NONSM / "proof_corpus" / "Selected_Qa_SU3_HYM_Strominger_Weitzenbock_OU_Completion_v1.md",
    "hym_extraction_spec": PROTO / "proof_corpus" / "Selected_HYM_Connection_to_Finite_Operator_Extraction_Spec_v1.md",
    "hym_extraction_run": PROTO / "proof_corpus" / "Selected_HYM_Connection_to_Finite_Operator_Extraction_Run_v1.md",
    "diagonal_hym_payload": PROTO / "proof_corpus" / "Selected_Diagonal_HYM_Operator_Payload_Extraction_v1.md",
    "q79_typed_witness": Q79 / "proof_corpus" / "Q79_Typed_Monad_Cech_or_HYM_Connection_Witness_v1.md",
}

OUTPUT_DATA = DATA / "selected_heterotic_sourcecertificate_or_direct_operator_emission_search.candidate.json"
OUTPUT_CERT = CERTS / "selected_heterotic_sourcecertificate_or_direct_operator_emission_search_certificate.json"
OUTPUT_TEMPLATE = DATA / "selected_heterotic_torsional_endomorphism_or_ou_mode_weights.template.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_SourceCertificate_or_DirectOperatorEmission_Search_v1.md"

STATUS = "HETEROTIC_SOURCECERTIFICATE_OR_DIRECT_OPERATOR_EMISSION_SEARCH_BUILT_TORSIONAL_E_OR_OU_NEXT"
NEXT = "Selected_Heterotic_TorsionalEndomorphism_or_OU_ModeWeights_v1"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def scan_text(path: Path, terms: list[str]) -> dict[str, Any]:
    text = read(path) if path.exists() else ""
    return {
        "path": str(path),
        "present": path.exists(),
        "terms": {term: term in text for term in terms},
    }


def build_template() -> dict[str, Any]:
    return {
        "schema": "SelectedHeteroticTorsionalEndomorphismOrOUModeWeights.v1",
        "status": "OPEN_VALUES_REQUIRED",
        "source_certificate": {
            "same_branch_selected_HYM_or_Strominger_source": None,
            "fixed_gauge_and_quotient_domain": None,
            "same_branch_as_internal_lambda12_stack": None,
        },
        "torsional_endomorphism_lane": {
            "connection_A": None,
            "torsion_H_or_Bismut_data": None,
            "curvature_R_plus_trace_row": None,
            "Weitzenbock_E_Qa_on_uE_one_forms": None,
            "positivity_or_kernel_policy": None,
        },
        "ou_mode_weight_lane": {
            "mode_basis": None,
            "gamma_nk_weights": None,
            "finite_truncation_and_error_bound": None,
            "zeta_or_heat_regularization": None,
        },
        "direct_finite_operator_lane": {
            "rho_E_mesh_metric_tables": None,
            "D_E_action": None,
            "Riesz_projectors_and_gap": None,
            "reduced_Green": None,
            "dotD_or_threshold_derivative": None,
        },
        "output": {
            "endomorphism_E_or_equivalent_operator_block": None,
            "spectrum_heat_torsion_finite_part": None,
            "trace_weights_and_threshold_convention": None,
            "computed_dimensionless_threshold_value": None,
        },
        "forbidden": [
            "select mu by target residual or convenience",
            "insert arbitrary OU weights",
            "promote diagonal/rank-2 HYM support as Qa/SU3 threshold value",
            "reuse retired printed HYM matrix entries",
            "use observed electroweak data to fill any entry",
        ],
    }


def build() -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], str]:
    value_fill = load_json(INPUTS["value_fill"])
    analytic_payload = load_json(INPUTS["analytic_payload"])
    template = build_template()

    source_scans = {
        "hym_ou_completion": scan_text(
            INPUTS["hym_ou_completion"],
            ["actual torsional Weitzenbock endomorphism", "OU weights", "mu selected: no", "Selected_Qa_SU3_Torsional_Endomorphism_or_OU_Mode_Weights_v1"],
        ),
        "hym_extraction_spec": scan_text(
            INPUTS["hym_extraction_spec"],
            ["rho_E mesh", "D_E action matrices", "Riesz projectors", "theorem-derived selected-source flags"],
        ),
        "hym_extraction_run": scan_text(
            INPUTS["hym_extraction_run"],
            ["rhoE_mesh", "D_E action", "fail", "source/provenance failures"],
        ),
        "diagonal_hym_payload": scan_text(
            INPUTS["diagonal_hym_payload"],
            ["H = diag(exp(s), exp(-s))", "A_diag = d s * T3", "not validator-ready", "shared-circle"],
        ),
        "q79_typed_witness": scan_text(
            INPUTS["q79_typed_witness"],
            ["typed monad", "HYM", "D_E", "same selected source"],
        ),
    }

    routes = {
        "A_source_certificate_search": {
            "status": "SUPPORT_FOUND_VALUES_OPEN",
            "support": [
                "Strominger fixed-sector/HYM framework is present.",
                "Typed monad/Cech or HYM witness contracts exist in sibling repos.",
                "Current Qa/SU3 fill attempt still has no same-branch source certificate.",
            ],
            "closes_now": False,
            "why_not": value_fill["missing_fields"],
        },
        "B_direct_operator_emission": {
            "status": "PRIMARY_NEXT_ROUTE_TORSIONAL_E_OR_OU_WEIGHTS",
            "support": [
                "Metric-weighted real Chern block is positive on su3 samples but does not select mu.",
                "The external extraction spec names rho_E, D_E, Riesz/gap, Green, and derivative tables as acceptance payloads.",
                "The honest extraction run fails exactly at source/provenance and downstream operator validators.",
            ],
            "must_compute_next": [
                "torsional Weitzenbock endomorphism on u(E)-valued one-forms",
                "mode-by-mode OU weights gamma_{n,k}^{-1}",
                "fixed-gauge quotient and residual kernel policy",
                "finite heat/zeta/torsion determinant in the selected domain",
            ],
            "closes_now": False,
        },
        "C_diagonal_rank2_import": {
            "status": "USEFUL_SUBPAYLOAD_NOT_QA_SU3_THRESHOLD",
            "support": [
                "Diagonal HYM payload emits H=diag(exp(s),exp(-s)) and A_diag=ds*T3.",
                "Residual is small and determinant is fixed.",
            ],
            "why_not": "It is rank-2/End0 support and explicitly not validator-ready rhoE/D_E/Riesz/Green/dotD data for the Qa/SU3 threshold.",
            "closes_now": False,
        },
        "D_projective_or_local_system_recheck": {
            "status": "RETIRED_OR_AUXILIARY_FOR_THIS_GATE",
            "why_not": [
                "ordinary rank-one local system cannot carry q64 center",
                "U64 projective carrier lacks operator-domain bridge and finite part",
            ],
            "closes_now": False,
        },
    }

    candidate = {
        "candidate": "SelectedHeteroticSourceCertificateOrDirectOperatorEmissionSearch",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            "value_fill": value_fill["status"],
            "analytic_payload": analytic_payload["status"],
        },
        "source_scans": source_scans,
        "route_tests": routes,
        "decision": {
            "source_certificate_found": False,
            "direct_operator_emission_found": False,
            "diagonal_rank2_support_imported": True,
            "primary_next_route": "torsional_endomorphism_or_OU_mode_weights",
            "next_required_artifact": NEXT,
            "selected_values_available": False,
            "target_fitting_used": False,
        },
        "theorem": {
            "name": "SourceCertificateOrDirectOperatorEmissionSearchTheorem",
            "proved": True,
            "statement": (
                "The current corpus and sibling repositories contain real support for the "
                "Strominger/HYM source architecture and finite-operator extraction pipeline, "
                "but no same-branch selected source certificate or direct Qa/SU3 threshold "
                "operator emission is present. The strongest non-redundant next computation "
                "is the torsional Weitzenbock endomorphism or OU mode-weight packet for the "
                "selected compact Nil/Iwasawa HYM/Strominger domain."
            ),
        },
        "next_template_path": rel(OUTPUT_TEMPLATE),
        "guardrails": {
            "uses_observed_electroweak_data": False,
            "uses_target_residual_scan": False,
            "promotes_diagonal_rank2_payload": False,
            "promotes_extraction_spec_without_values": False,
            "promotes_failed_extraction_run": False,
            "promotes_projective_carrier_as_closure": False,
            "claims_measured_electroweak_closure": False,
            "target_fitting_used": False,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    cert = {
        "certificate": "SelectedHeteroticSourceCertificateOrDirectOperatorEmissionSearch",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "template_path": rel(OUTPUT_TEMPLATE),
        "note_path": rel(OUTPUT_NOTE),
        "source_certificate_found": False,
        "direct_operator_emission_found": False,
        "primary_next_route": candidate["decision"]["primary_next_route"],
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
    }
    return candidate, cert, template, render_note(candidate, cert, template)


def render_note(candidate: dict[str, Any], cert: dict[str, Any], template: dict[str, Any]) -> str:
    return f"""# Selected Heterotic SourceCertificate or DirectOperatorEmission Search v1

## Result

```text
status = {candidate["status"]}
source_certificate_found = false
direct_operator_emission_found = false
primary_next_route = {candidate["decision"]["primary_next_route"]}
next_required_artifact = {candidate["decision"]["next_required_artifact"]}
```

## Route Tests

```json
{json.dumps(candidate["route_tests"], indent=2, sort_keys=True)}
```

## Source Scans

```json
{json.dumps(candidate["source_scans"], indent=2, sort_keys=True)}
```

## Theorem

{candidate["theorem"]["statement"]}

## Next Template

```json
{json.dumps(template, indent=2, sort_keys=True)}
```

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
