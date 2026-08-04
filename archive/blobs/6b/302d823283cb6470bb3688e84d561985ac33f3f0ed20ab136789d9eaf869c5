"""Build the minimal source-amendment or direct-operator-row gate for U1/Y."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"
TEXPAPERS = ROOT.parent
NONSM = TEXPAPERS / "mtt-nonsm-constants-no-knob"
SM = TEXPAPERS / "mtt-sm-parity-closure"

INPUTS = {
    "u1_section_row_gate": DATA / "selected_u1_hypercharge_section_ring_or_twisted_module_operator_row.candidate.json",
    "local_determinant_attempt": DATA / "selected_u1_hypercharge_local_determinant_spectrum_attempt.candidate.json",
    "u1_projector": DATA / "selected_u1_quotient_projector_pperp_and_trace_policy.candidate.json",
    "projective_gerbe_promotion": SM / "candidate_data" / "projective_gerbe_rhoe_source_promotion.candidate.json",
    "twisted_gerbe_fill": NONSM / "certificates" / "selected_qa_su3_twisted_gerbe_source_packet_fill_attempt_certificate.json",
    "visible_rank2_valpha": NONSM / "certificates" / "selected_qa_su3_visible_rank2_valpha_source_attempt_certificate.json",
    "valpha_integral_lift_gap": NONSM / "certificates" / "selected_qa_su3_valpha_s3_integral_lift_gap_import_certificate.json",
}

OUTPUT_DATA = DATA / "selected_u1_hypercharge_minimal_source_amendment_or_direct_operator_row.candidate.json"
OUTPUT_CERT = CERTS / "selected_u1_hypercharge_minimal_source_amendment_or_direct_operator_row_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1_Hypercharge_Minimal_Source_Amendment_or_Direct_Operator_Row_v1.md"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    section_gate = load(INPUTS["u1_section_row_gate"])
    determinant_attempt = load(INPUTS["local_determinant_attempt"])
    u1_projector = load(INPUTS["u1_projector"])
    projective = load(INPUTS["projective_gerbe_promotion"])
    twisted = load(INPUTS["twisted_gerbe_fill"])
    valpha = load(INPUTS["visible_rank2_valpha"])
    lift_gap = load(INPUTS["valpha_integral_lift_gap"])

    source_amendment_fields = [
        {
            "field": "U1/Y charge object",
            "current_status": "PARTIAL_STRUCTURAL",
            "support": [
                "topology-only hypercharge selects the charge pattern",
                "P_perp selects the rank-2 quotient carrier",
                "S3 gerbe data can supply an adjacent projective finite source",
            ],
            "missing": "same-source declaration that this charge object is the U1/Y threshold bundle/module/local system",
        },
        {
            "field": "transition/automorphy/cocycle data and compact domain",
            "current_status": "PARTIAL_PROJECTIVE_ONLY",
            "support": [
                "projective gerbe promotion closes S3 flat Deligne class, central-cocycle map, Freed-Witten, and projector retention",
                "V_alpha lane has conditional Appell-Humbert automorphy for an adjacent visible rank-2 source",
            ],
            "missing": "selected U1/Y transition or twisted cocycle data on the threshold domain, with target-vs-swapped and Pic0 degeneracy broken if the integral lane is used",
        },
        {
            "field": "connection or threshold-operator formula",
            "current_status": "OPEN",
            "support": [
                "Chern-Weil/operator source is named as the next object in sibling promotion gates",
            ],
            "missing": "explicit U1/Y operator row: connection, Laplace/Dirac/BRST/Weitzenbock formula, or D_E/rho_E transition data",
        },
        {
            "field": "P_perp compatibility and zero-mode quotient policy",
            "current_status": "PARTIAL_INDEX_ONLY",
            "support": [
                "P_perp^2=P_perp, rank(P_perp)=2, and Tr(P_perp)/Tr(I_3)=2/3 are closed",
            ],
            "missing": "proof that the emitted U1/Y threshold operator acts on V/<s> and uses this zero-mode quotient policy",
        },
        {
            "field": "positive spectrum, multiplicities, hypercharge/index weights",
            "current_status": "OPEN",
            "support": [],
            "missing": "the actual positive eigenvalue list/table or an exact zeta/heat/torsion replacement emitted before comparison",
        },
        {
            "field": "finite determinant prescription and no-target-fit certificate",
            "current_status": "OPEN_NO_TARGET_FIT_CERTIFICATE_READY",
            "support": [
                "existing local determinant template supplies the deterministic accounting contract",
                "all current audits forbid lambda_12 or measured electroweak inputs as selectors",
            ],
            "missing": "selected regularization, scale convention, zero-mode policy, and finite part for this U1/Y row",
        },
    ]

    direct_operator_row_tests = {
        "projective_s3_gerbe_promotion": {
            "status": "PARTIAL_SOURCE_LEVEL_PROMOTION_OPERATOR_ROW_OPEN",
            "source_status": projective["status"],
            "promoted_now": projective["promotion_result"]["source_level_projective_gerbe_rhoE_promoted"],
            "operator_level_promoted": projective["promotion_result"]["operator_level_projective_rhoE_promoted"],
            "remaining_cut_set": projective["promotion_result"]["remaining_cut_set"],
            "verdict": "Useful import: source-level S3 gerbe/projector/Freed-Witten blockers are retired. It still does not emit U1/Y spectra or the Chern-Weil/operator row.",
        },
        "twisted_gerbe_fill_attempt": {
            "status": "PARTIAL_SOURCE_PACKET_OPERATOR_EXIT_OPEN",
            "source_status": twisted["certificate"],
            "filled_fields": twisted["filled_fields"],
            "operator_exit_available": twisted["fill_result"]["operator_exit_available"],
            "determinant_computable_now": twisted["fill_result"]["determinant_computable_now"],
            "verdict": "Good source support for the twisted lane, but no projective rho_E/twisted D_E/torsion finite part.",
        },
        "visible_rank2_valpha_lane": {
            "status": "CONDITIONAL_EXT_MATH_CLOSED_SOURCE_SELECTOR_OPEN",
            "source_status": valpha["status"],
            "conditional_h1": valpha["validated_conditional_ext_packet"]["h1"],
            "selected_source_promotes": valpha["validated_conditional_ext_packet"]["selected_source_promotes"],
            "remaining": valpha["not_closed"],
            "verdict": "It supplies a conditional visible rank-2 route, not a selected U1/Y operator row.",
        },
        "integral_lift_gap": {
            "status": "SELECTOR_REQUIRED_NOT_OPERATOR_ROW",
            "source_status": lift_gap["status"],
            "honest_answer": lift_gap["honest_answer"],
            "next_source_options": lift_gap["next_source_options"],
            "verdict": "The integral lift exists conditionally but does not select target branch, Pic0 quotient, D_E/dotD, or spectrum.",
        },
    }

    decision = {
        "minimal_source_amendment_gate_built": True,
        "direct_operator_row_found": False,
        "source_amendment_currently_sufficient": False,
        "lambda_12_closed": False,
        "strongest_live_route": "projective_s3_gerbe_source_plus_selected_visible_Chern_Weil_or_U1Y_operator_row",
        "next_required_object": "Selected_U1Y_Chern_Weil_or_Projective_RhoE_Operator_Row_Source_v1",
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "SelectedU1HyperchargeMinimalSourceAmendmentOrDirectOperatorRow",
        "status": "U1_HYPERCHARGE_MINIMAL_SOURCE_AMENDMENT_GATE_BUILT_OPERATOR_ROW_OPEN",
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "prior_gate_status": section_gate["status"],
        "u1_projector_status": u1_projector["status"],
        "determinant_attempt_status": determinant_attempt["status"],
        "source_amendment_fields": source_amendment_fields,
        "direct_operator_row_tests": direct_operator_row_tests,
        "decision": decision,
        "guardrails": [
            "Do not promote S3 gerbe source-level closure to U1/Y operator-spectrum closure.",
            "Do not promote conditional V_alpha H1=8 or Appell-Humbert data without source selector and operator row.",
            "Do not use Delta_Qa=log(2008), lambda_12, sin^2(theta_W), or measured gauge couplings to choose spectra.",
            "Do not treat P_perp or the 2/3 trace index as a positive determinant spectrum.",
        ],
        "closure_claimed": True,
        "closure_scope": "minimal_amendment_gate_and_import_triage_only",
        "target_fitting_used": False,
    }

    certificate = {
        "certificate": "SelectedU1HyperchargeMinimalSourceAmendmentOrDirectOperatorRow",
        "status": candidate["status"],
        "candidate_path": rel(OUTPUT_DATA),
        "closed": {
            "minimal_source_amendment_fields_audited": True,
            "projective_s3_source_import_triaged": True,
            "visible_valpha_integral_lift_triaged": True,
            "strongest_live_route_identified": True,
            "no_target_fit_used": True,
        },
        "open": {
            "selected_U1Y_operator_row": True,
            "selected_Chern_Weil_or_projective_rhoE_response": True,
            "selected_positive_spectrum_or_zeta_heat_torsion": True,
            "selected_hypercharge_index_weights": True,
            "lambda_12": True,
        },
        "next_required_object": decision["next_required_object"],
        "target_fitting_used": False,
    }
    return candidate, certificate, render_note(candidate)


def render_note(candidate: dict[str, Any]) -> str:
    fields = "\n".join(
        f"- `{row['field']}`: {row['current_status']}. Missing: {row['missing']}"
        for row in candidate["source_amendment_fields"]
    )
    tests = candidate["direct_operator_row_tests"]
    guardrails = "\n".join(f"- {g}" for g in candidate["guardrails"])
    return f"""# Selected U1 Hypercharge Minimal Source Amendment or Direct Operator Row v1

## Result

```text
direct_operator_row_found = false
source_amendment_currently_sufficient = false
lambda_12_closed = false
target_fitting_used = false
```

The stronger sibling source data help, but they do not yet emit a U1/Y
threshold operator row. The frontier is now a direct operator-source problem,
not a charge/topology/projector problem.

## Minimal Amendment Field Audit

{fields}

## Direct Operator Row Tests

```text
projective_s3_gerbe_promotion = {tests["projective_s3_gerbe_promotion"]["status"]}
twisted_gerbe_fill_attempt = {tests["twisted_gerbe_fill_attempt"]["status"]}
visible_rank2_valpha_lane = {tests["visible_rank2_valpha_lane"]["status"]}
integral_lift_gap = {tests["integral_lift_gap"]["status"]}
```

Strongest current live route:

```text
{candidate["decision"]["strongest_live_route"]}
```

The S3/projective gerbe import retires source-level gerbe, central-cocycle,
Freed-Witten, and projector blockers, but it still lacks the selected
Chern-Weil/operator response, coherent spectral projectors, `D_E`, Riesz/Green,
`dotD`, primitive `C1` contractions, and U1/Y finite determinant row.

## Guardrails

{guardrails}

## Decision

```text
next_required_object = {candidate["decision"]["next_required_object"]}
```
"""


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    missing = [str(path) for path in INPUTS.values() if not path.exists()]
    if missing:
        print("Missing inputs:")
        print("\n".join(missing))
        return 1
    candidate, certificate, note = build()
    write_json(OUTPUT_DATA, candidate)
    write_json(OUTPUT_CERT, certificate)
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(f"Wrote {OUTPUT_DATA}")
    print(f"Wrote {OUTPUT_CERT}")
    print(f"Wrote {OUTPUT_NOTE}")
    print(certificate["status"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
