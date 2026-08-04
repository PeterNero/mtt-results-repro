"""Build the selected U1/Y Chern-Weil or projective rho_E operator-row gate."""

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
Q79 = TEXPAPERS / "mtt-q79-proof-repro"
NONSM = TEXPAPERS / "mtt-nonsm-constants-no-knob"

INPUTS = {
    "u1y_minimal_gate": DATA / "selected_u1_hypercharge_minimal_source_amendment_or_direct_operator_row.candidate.json",
    "selected_visible_cw_source": SM / "candidate_data" / "selected_visible_chern_weil_operator_source.candidate.json",
    "routec_c1_emission": SM / "candidate_data" / "selected_routec_selected_c1_response_operator_emission.candidate.json",
    "zero_mode_dotd_interface": Q79 / "certificates" / "selected_zero_mode_basis_dotd_interface_certificate.json",
    "q79_c1_extraction": Q79 / "certificates" / "selected_c1_response_extraction_attempt_certificate.json",
    "nonsm_m1_cw_attempt": NONSM / "certificates" / "selected_qa_su3_m1_cw_operator_source_attempt_certificate.json",
}

OUTPUT_DATA = DATA / "selected_u1y_chern_weil_or_projective_rhoe_operator_row_source.candidate.json"
OUTPUT_CERT = CERTS / "selected_u1y_chern_weil_or_projective_rhoe_operator_row_source_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_Chern_Weil_or_Projective_RhoE_Operator_Row_Source_v1.md"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    minimal = load(INPUTS["u1y_minimal_gate"])
    visible_cw = load(INPUTS["selected_visible_cw_source"])
    routec_c1 = load(INPUTS["routec_c1_emission"])
    zero_dotd = load(INPUTS["zero_mode_dotd_interface"])
    q79_c1 = load(INPUTS["q79_c1_extraction"])
    nonsm_cw = load(INPUTS["nonsm_m1_cw_attempt"])

    imported_reductions = {
        "selected_visible_cw_source": {
            "status": visible_cw["status"],
            "theorem": visible_cw["theorem"]["statement"],
            "closed_support": visible_cw["closed_support"],
            "open_cut_set": visible_cw["open_gates"]["same_source_cut_set"],
            "next_required_artifact": visible_cw["next_required_artifact"],
            "verdict": "This is the strongest same-family source reduction, but it does not emit the selected visible operator source.",
        },
        "routec_c1_operator_emission": {
            "status": routec_c1["status"],
            "theorem": routec_c1["theorem"]["statement"],
            "what_closes_now": routec_c1["what_closes_now"],
            "what_remains_open": routec_c1["what_remains_open"],
            "next_required_artifact": routec_c1["next_required_artifact"],
            "verdict": "This supplies the operator-emission contract, but A_selected and b_selected are not emitted.",
        },
        "zero_mode_dotd_interface": {
            "status": zero_dotd["status"],
            "closed_inputs": list(zero_dotd["closed_inputs"].keys()),
            "completion_gates": zero_dotd["completion_gates"],
            "verdict": "This gives the no-proxy slot contract for zero modes and dotD, but all sector values remain open.",
        },
        "q79_c1_extraction": {
            "status": q79_c1["status"],
            "attempt_result": q79_c1["attempt_result"],
            "missing_selected_operator_data": q79_c1["missing_selected_operator_data"],
            "verdict": "Reusable C1 extraction pattern only; selected finite operator data remain missing.",
        },
        "nonsm_m1_cw_attempt": {
            "status": nonsm_cw["status"],
            "honest_answer": nonsm_cw["honest_answer"],
            "relation_to_common_payload": nonsm_cw["relation_to_common_payload"],
            "verdict": "Confirms the Chern-Weil row is viable but not closed; the first unfilled common payload is still selected_source_certificate.",
        },
    }

    required_payload = [
        {
            "item": "selected source certificate",
            "status": "OPEN",
            "why": "Visible CW source and M1 CW attempt both reduce to same-source selection, not emitted source data.",
        },
        {
            "item": "selected U1/Y or visible bundle/sheaf/operator row",
            "status": "OPEN",
            "why": "Current imports identify source shapes, but no U1/Y threshold operator row is printed.",
        },
        {
            "item": "Chern-Weil or projective rho_E row derived from selected source",
            "status": "OPEN",
            "why": "Chern-Weil row is structurally viable; same-source derivation remains open.",
        },
        {
            "item": "coherent spectral projectors and P_perp compatibility",
            "status": "PARTIAL",
            "why": "P_perp index is closed and S3 projector retention is source-level closed, but U1/Y operator projector retention is not.",
        },
        {
            "item": "D_E, Riesz/Green, dotD response",
            "status": "OPEN",
            "why": "Zero-mode/dotD interface is formulated; no sector-resolved values are supplied.",
        },
        {
            "item": "primitive C1 contractions or equivalent U1/Y threshold finite part",
            "status": "OPEN",
            "why": "C1 emission audit separates zero canonical response from nonzero unselected candidates; selected contractions remain open.",
        },
        {
            "item": "positive spectrum or exact zeta/heat/torsion finite part with weights",
            "status": "OPEN",
            "why": "No imported artifact emits U1/Y positive eigenvalues, index weights, or determinant finite part.",
        },
    ]

    decision = {
        "operator_row_source_gate_built": True,
        "selected_U1Y_chern_weil_or_projective_rhoE_row_found": False,
        "selected_D_E_Riesz_Green_dotD_found": False,
        "selected_positive_spectrum_or_finite_part_found": False,
        "lambda_12_closed": False,
        "strongest_reduction": "same_source_nonabelian_or_RouteC_operator_payload",
        "next_required_object": "Selected_U1Y_Same_Source_Nonabelian_or_RouteC_Operator_Payload_v1",
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "SelectedU1YChernWeilOrProjectiveRhoEOperatorRowSource",
        "status": "U1Y_CHERN_WEIL_OR_PROJECTIVE_RHOE_ROW_SOURCE_GATE_BUILT_SAME_SOURCE_PAYLOAD_OPEN",
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "prior_gate_status": minimal["status"],
        "imported_reductions": imported_reductions,
        "required_payload": required_payload,
        "decision": decision,
        "guardrails": [
            "Do not promote selected S3/projective gerbe source support to operator-row closure.",
            "Do not promote C1 formal insertion calculus without selected A_selected and b_selected.",
            "Do not use nonzero unselected non-invariant C1 candidates as selected threshold data.",
            "Do not use measured electroweak data, lambda_12, or residuals to choose the U1/Y row.",
        ],
        "closure_claimed": True,
        "closure_scope": "operator_row_source_gate_and_import_reduction_only",
        "target_fitting_used": False,
    }

    certificate = {
        "certificate": "SelectedU1YChernWeilOrProjectiveRhoEOperatorRowSource",
        "status": candidate["status"],
        "candidate_path": rel(OUTPUT_DATA),
        "closed": {
            "visible_cw_source_reduction_imported": True,
            "routec_c1_emission_contract_imported": True,
            "zero_mode_dotd_interface_imported": True,
            "same_source_payload_cut_set_identified": True,
            "no_target_fit_used": True,
        },
        "open": {
            "selected_source_certificate": True,
            "selected_U1Y_operator_row": True,
            "selected_Chern_Weil_or_projective_rhoE_row": True,
            "selected_D_E_Riesz_Green_dotD": True,
            "selected_C1_or_threshold_finite_part": True,
            "selected_positive_spectrum_or_zeta_heat_torsion": True,
            "lambda_12": True,
        },
        "next_required_object": decision["next_required_object"],
        "target_fitting_used": False,
    }
    return candidate, certificate, render_note(candidate)


def render_note(candidate: dict[str, Any]) -> str:
    payload = "\n".join(f"- `{row['item']}`: {row['status']}. {row['why']}" for row in candidate["required_payload"])
    imports = candidate["imported_reductions"]
    guardrails = "\n".join(f"- {g}" for g in candidate["guardrails"])
    return f"""# Selected U1Y Chern-Weil or Projective RhoE Operator Row Source v1

## Result

```text
selected_U1Y_chern_weil_or_projective_rhoE_row_found = false
selected_D_E_Riesz_Green_dotD_found = false
selected_positive_spectrum_or_finite_part_found = false
lambda_12_closed = false
target_fitting_used = false
```

This gate imports the strongest available Chern-Weil, projective `rho_E`,
Riesz/Green, `dotD`, and C1-response artifacts. They reduce the problem to one
same-source operator payload, but do not emit it.

## Imported Reductions

```text
selected_visible_cw_source = {imports["selected_visible_cw_source"]["status"]}
routec_c1_operator_emission = {imports["routec_c1_operator_emission"]["status"]}
zero_mode_dotd_interface = {imports["zero_mode_dotd_interface"]["status"]}
q79_c1_extraction = {imports["q79_c1_extraction"]["status"]}
nonsm_m1_cw_attempt = {imports["nonsm_m1_cw_attempt"]["status"]}
```

## Required Same-Source Payload

{payload}

## Guardrails

{guardrails}

## Decision

```text
strongest_reduction = {candidate["decision"]["strongest_reduction"]}
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
