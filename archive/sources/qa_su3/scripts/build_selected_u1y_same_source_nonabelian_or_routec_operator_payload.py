"""Attempt the selected U1/Y same-source operator payload across three lanes."""

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

INPUTS = {
    "prior_u1y_gate": DATA / "selected_u1y_chern_weil_or_projective_rhoe_operator_row_source.candidate.json",
    "u1_projector_policy": DATA / "selected_u1_quotient_projector_pperp_and_trace_policy.candidate.json",
    "selected_visible_cw_source": SM / "candidate_data" / "selected_visible_chern_weil_operator_source.candidate.json",
    "routec_c1_emission": SM / "candidate_data" / "selected_routec_selected_c1_response_operator_emission.candidate.json",
    "projective_gerbe_rhoe_promotion": SM / "candidate_data" / "projective_gerbe_rhoe_source_promotion.candidate.json",
    "zero_mode_dotd_interface": Q79 / "certificates" / "selected_zero_mode_basis_dotd_interface_certificate.json",
}

OUTPUT_DATA = DATA / "selected_u1y_same_source_nonabelian_or_routec_operator_payload.candidate.json"
OUTPUT_CERT = CERTS / "selected_u1y_same_source_nonabelian_or_routec_operator_payload_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_Same_Source_Nonabelian_or_RouteC_Operator_Payload_v1.md"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def flag(value: Any) -> bool:
    return value is True


def lane_result(lane_id: str, requirements: list[dict[str, Any]], source_status: str, verdict: str) -> dict[str, Any]:
    missing = [r["field"] for r in requirements if not flag(r["satisfied"])]
    return {
        "lane_id": lane_id,
        "source_status": source_status,
        "requirements": requirements,
        "missing_fields": missing,
        "accepted": len(missing) == 0,
        "verdict": verdict,
    }


def req(field: str, satisfied: bool, evidence: str) -> dict[str, Any]:
    return {"field": field, "satisfied": satisfied, "evidence": evidence}


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    prior = load(INPUTS["prior_u1y_gate"])
    projector = load(INPUTS["u1_projector_policy"])
    visible = load(INPUTS["selected_visible_cw_source"])
    routec = load(INPUTS["routec_c1_emission"])
    projective = load(INPUTS["projective_gerbe_rhoe_promotion"])
    zero_dotd = load(INPUTS["zero_mode_dotd_interface"])

    projector_ok = (
        projector["decision"]["explicit_U1_P_perp_projector"]
        and projector["decision"]["U1_operator_trace_uses_P_perp"]
        and projector["decision"]["selected_U1_index"] == "2/3"
    )

    visible_open = visible["open_gates"]["same_source_cut_set"]
    visible_lane = lane_result(
        "A_nonabelian_visible_bundle_sheaf_chern_weil",
        [
            req("source_certificate", False, "visible source reduction names the same-source packet but does not emit the selected source certificate"),
            req("selected_U1Y_bundle_sheaf_or_operator_row", False, "selected_visible_operator_source_closed=false"),
            req("chern_weil_row_from_same_source", not visible_open["Chern_Weil_row_derived_from_selected_source"], "Chern-Weil row remains in the same-source cut set"),
            req("P_perp_projector_compatibility", projector_ok, "U1 quotient projector and trace policy are closed as index-only support"),
            req("sector_D_E_dotD_Riesz_Green", not visible_open["selected_D_E_dotD_Riesz_Green"], "selected D_E/dotD/Riesz/Green remains open"),
            req("primitive_C1_or_overlap_contractions", not visible_open["primitive_C1_contractions"], "primitive C1 contractions remain open"),
            req("positive_spectrum_or_finite_part_with_weights", False, "no visible-source positive spectrum, zeta/heat/torsion, or determinant finite part is emitted"),
        ],
        visible["status"],
        "Rejected as closure: the formal visible Chern-Weil route is the right shape, but the selected source and operator row are not emitted.",
    )

    routec_open = routec["what_remains_open"]
    routec_lane = lane_result(
        "B_routec_finite_hym_strominger_c1_payload",
        [
            req("A_selected", not routec_open["emit_selected_A_selected"], "Route-C audit says emit_selected_A_selected remains open"),
            req("b_selected", not routec_open["emit_selected_b_selected"], "Route-C audit says emit_selected_b_selected remains open"),
            req("selected_Hess_Xi_finite_blocks", not routec_open["selected_Hess_Xi_finite_blocks"], "selected lower-order Hessian blocks remain open"),
            req("selected_zero_mode_bases_and_Gram_Schmidt", not routec_open["selected_zero_mode_bases_and_Gram_Schmidt"], "selected zero-mode bases and L2 rule remain open"),
            req("selected_dotD", not routec_open["selected_dotD_Q_u_d_L_e_N_H"], "selected dotD operators remain open"),
            req("selected_sector_response_matrices", not routec_open["selected_sector_response_matrices"], "selected response matrices remain open"),
            req("primitive_C1_contractions_or_threshold_finite_part", not routec_open["selected_primitive_C1_contractions"], "selected primitive contractions remain open"),
            req("P_perp_projector_compatibility", projector_ok, "U1 quotient projector and trace policy are available as index-only support"),
        ],
        routec["status"],
        "Rejected as closure: Route-C supplies the emission contract, but the selected operator/vector and sector response data are absent.",
    )

    projective_flags = projective["promotion_gate_flags_after_s3_closure"]
    projective_cut = projective["promotion_result"]["remaining_cut_set"]
    projective_lane = lane_result(
        "C_projective_gerbe_rhoE_packet",
        [
            req("selected_projective_source_level", projective["promotion_result"]["source_level_projective_gerbe_rhoE_promoted"], "S3/projective gerbe source-level promotion is closed"),
            req("selected_Deligne_or_gerbe_representative", projective_flags["fixed_differential_cohomology_class"], "fixed differential cohomology class is closed at source level"),
            req("map_to_central_cocycle", projective_flags["map_to_central_cocycle_verified"], "central cocycle map is verified at source level"),
            req("Freed_Witten_and_Bianchi", projective_flags["freed_witten_verified"] and projective_flags["green_schwarz_bianchi_verified"], "source-level FW/Bianchi support is closed"),
            req("coherent_spectral_projectors", not projective_cut["coherent_spectral_zero_mode_projectors"], "coherent spectral projectors remain in the cut set"),
            req("projective_rhoE_operator_tables", projective["promotion_result"]["operator_level_projective_rhoE_promoted"], "operator-level projective rhoE is explicitly not promoted"),
            req("D_E_Riesz_Green_dotD", not projective_cut["selected_D_E_dotD_Riesz_Green"], "selected D_E/dotD/Riesz/Green remains open"),
            req("primitive_C1_or_finite_part", not projective_cut["primitive_C1_contractions"], "primitive C1 contractions remain open"),
            req("P_perp_projector_compatibility", projector_ok, "U1 quotient projector and trace policy are available as index-only support"),
        ],
        projective["status"],
        "Rejected as closure: projective/S3 support is strong at source level, but no rhoE operator tables or finite determinant part are emitted.",
    )

    lanes = [routec_lane, projective_lane, visible_lane]
    accepted_lanes = [lane["lane_id"] for lane in lanes if lane["accepted"]]

    acceptance_contract = [
        "same_source=true for the selected source, operator row, projectors, response data, and finite part",
        "target_fitting_used=false; no measured electroweak data, lambda_12, or residuals may select the payload",
        "at least one of the three lanes must emit a selected source certificate and U1/Y operator row",
        "P_perp compatibility must be explicit, not inferred from topology alone",
        "D_E/rhoE/Riesz/Green/dotD or equivalent finite torsion/heat/zeta payload must be printed",
        "lambda_12 may be computed only after the finite part is emitted",
    ]

    decision = {
        "three_lane_plan_executed": True,
        "accepted_lanes": accepted_lanes,
        "selected_U1Y_same_source_payload_found": bool(accepted_lanes),
        "selected_U1Y_operator_row_found": bool(accepted_lanes),
        "selected_projector_compatibility_found": projector_ok,
        "selected_finite_part_found": False,
        "lambda_12_computable": False,
        "lambda_12_closed": False,
        "target_fitting_used": False,
        "strongest_live_lane_order": [
            "B_routec_finite_hym_strominger_c1_payload",
            "C_projective_gerbe_rhoE_packet",
            "A_nonabelian_visible_bundle_sheaf_chern_weil",
        ],
        "next_required_object": "Selected_U1Y_RouteC_or_ProjectiveRhoE_Selected_Operator_Tables_v1",
    }

    candidate = {
        "candidate": "SelectedU1YSameSourceNonabelianOrRouteCOperatorPayload",
        "status": "U1Y_SAME_SOURCE_NONABELIAN_OR_ROUTEC_PAYLOAD_ATTEMPTED_OPERATOR_TABLES_OPEN",
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "prior_status": prior["status"],
        "acceptance_contract": acceptance_contract,
        "lane_attempts": lanes,
        "zero_mode_dotd_completion_gates": zero_dotd["completion_gates"],
        "closed_support": {
            "u1_pperp_projector_index_policy": projector_ok,
            "routec_emission_contract": True,
            "projective_s3_source_level_support": projective["promotion_result"]["source_level_projective_gerbe_rhoE_promoted"],
            "visible_chern_weil_reduction": visible["status"] == "MTT_SELECTED_VISIBLE_CW_OPERATOR_SOURCE_REDUCED_TO_SAME_SOURCE_NONABELIAN_OR_ROUTEC_PACKET",
            "three_lane_acceptance_validator_built": True,
        },
        "open": {
            "selected_source_certificate": True,
            "selected_U1Y_operator_row": True,
            "selected_operator_tables": True,
            "selected_D_E_Riesz_Green_dotD": True,
            "selected_C1_or_threshold_finite_part": True,
            "selected_positive_spectrum_or_zeta_heat_torsion": True,
            "lambda_12": True,
        },
        "decision": decision,
        "guardrails": [
            "Do not count source-level S3/projective support as operator-level rhoE closure.",
            "Do not count the P_perp index theorem as a local determinant spectrum.",
            "Do not use nonzero unselected Route-C candidates as selected response matrices.",
            "Do not use lambda_12, measured electroweak data, or residual scans to fill missing entries.",
        ],
        "closure_claimed": True,
        "closure_scope": "three_lane_acceptance_attempt_and_blocker_localization_only",
        "target_fitting_used": False,
    }

    certificate = {
        "certificate": "SelectedU1YSameSourceNonabelianOrRouteCOperatorPayload",
        "status": candidate["status"],
        "candidate_path": rel(OUTPUT_DATA),
        "closed": {
            "three_lane_plan_executed": True,
            "acceptance_contract_built": True,
            "u1_pperp_projector_compatibility_available": projector_ok,
            "routec_blockers_localized": True,
            "projective_rhoe_blockers_localized": True,
            "visible_chern_weil_blockers_localized": True,
            "no_target_fit_used": True,
        },
        "open": candidate["open"],
        "accepted_lanes": accepted_lanes,
        "next_required_object": decision["next_required_object"],
        "target_fitting_used": False,
    }
    return candidate, certificate, render_note(candidate)


def render_lane(lane: dict[str, Any]) -> str:
    rows = "\n".join(
        f"- `{item['field']}`: {'PASS' if item['satisfied'] else 'OPEN'} - {item['evidence']}"
        for item in lane["requirements"]
    )
    return f"""### {lane["lane_id"]}

```text
source_status = {lane["source_status"]}
accepted = {str(lane["accepted"]).lower()}
```

{rows}

Verdict: {lane["verdict"]}
"""


def render_note(candidate: dict[str, Any]) -> str:
    contract = "\n".join(f"- {item}" for item in candidate["acceptance_contract"])
    lanes = "\n".join(render_lane(lane) for lane in candidate["lane_attempts"])
    guardrails = "\n".join(f"- {item}" for item in candidate["guardrails"])
    decision = candidate["decision"]
    return f"""# Selected U1Y Same-Source Nonabelian or Route-C Operator Payload v1

## Result

```text
three_lane_plan_executed = true
selected_U1Y_same_source_payload_found = false
selected_U1Y_operator_row_found = false
selected_projector_compatibility_found = true
selected_finite_part_found = false
lambda_12_computable = false
lambda_12_closed = false
target_fitting_used = false
```

The three-lane plan has now been executed as an acceptance gate. It does not
close `lambda_12`, but it isolates the exact missing selected operator tables.

## Acceptance Contract

{contract}

## Lane Attempts

{lanes}

## Guardrails

{guardrails}

## Decision

```text
accepted_lanes = {decision["accepted_lanes"]}
strongest_live_lane_order = {decision["strongest_live_lane_order"]}
next_required_object = {decision["next_required_object"]}
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
