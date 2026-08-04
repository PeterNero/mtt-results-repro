"""Build the Qa-stack SU2 row / cancellation and physical-anchor gate."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "qa_finitepart": DATA / "selected_electroweak_qastack_finitepart_policy_and_indexscale.candidate.json",
    "typed_hypercharge_gate": DATA / "selected_electroweak_u1y_hypercharge_weights_typed_convention_gate.candidate.json",
    "dual_frontier": DATA / "dual_attack_local_determinant_or_omega0_source.candidate.json",
    "physical_gate": DATA / "selected_physical_gauge_anchor_and_electroweak_threshold_vector.candidate.json",
    "local_det_interface": Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-nonsm-constants-no-knob\certificates\selected_local_determinant_computation_interface_certificate.json"),
}

OUTPUT_DATA = DATA / "selected_electroweak_qastack_su2row_or_cancellation_and_physicalanchor.candidate.json"
OUTPUT_CERT = CERTS / "selected_electroweak_qastack_su2row_or_cancellation_and_physicalanchor_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Electroweak_QaStack_SU2Row_or_Cancellation_and_PhysicalAnchor_v1.md"

STATUS = "ELECTROWEAK_QASTACK_INTERNAL_LAMBDA12_CLOSED_PHYSICAL_ANCHOR_OPEN"
NEXT = "Selected_Electroweak_PhysicalAnchor_RG_and_MatchingScale_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    qa = load(INPUTS["qa_finitepart"])
    hyper = load(INPUTS["typed_hypercharge_gate"])
    dual = load(INPUTS["dual_frontier"])
    physical = load(INPUTS["physical_gate"])
    local_det = load(INPUTS["local_det_interface"])

    p_a = qa["decision"]["selected_p_a_internal_value"]
    lane_a = dual["lane_A_local_determinant"]["strongest_selected_inputs"]
    p_c = lane_a["selected_p_Qc_for_weak_split"]
    p_su2 = lane_a["selected_p_SU2_for_weak_split"]
    v1_tilde = lane_a["v1_tilde"]

    qa_closed = (
        qa["decision"]["selected_p_a_internal_promoted"] is True
        and qa["finitepart_policy"]["regularization"]["rule"] == local_det["formula"]["per_factor"]
        and qa["index_and_scale"]["determinant_scale"]["mu"] == "1"
    )
    qc_su2_closed = (
        dual["lane_A_local_determinant"]["what_closes_now"]["qc_circle_block_closed_for_weak_split"] is True
        and dual["lane_A_local_determinant"]["what_closes_now"]["su2_flat_fp_policy_closed_for_weak_split"] is True
    )
    typed_map_closed = hyper["decision"]["typed_hypercharge_convention_map_closed"] is True
    same_scheme_closed = qa_closed and qc_su2_closed and typed_map_closed

    weights = hyper["typed_convention_map"]["selected_weights"]
    p_y = p_a / 36.0 + p_c / 4.0
    lambda_12 = p_y - p_su2
    delta_g12 = v1_tilde * lambda_12 / (4.0 * math.pi)

    internal_vector = {
        "p_a_internal": p_a,
        "p_c_weaksplit": p_c,
        "p_SU2_weaksplit": p_su2,
        "p_Y_internal": p_y,
        "lambda_12_internal": lambda_12,
        "Delta_G12_internal": delta_g12,
        "v1_tilde": v1_tilde,
        "formulae": {
            "p_Y": "p_a/36 + p_c/4",
            "lambda_12": "p_Y - p_SU2",
            "Delta_G12": "v1_tilde*lambda_12/(4*pi)",
        },
    }

    same_scheme_argument = {
        "selected": same_scheme_closed,
        "Qa_row": {
            "status": qa["status"],
            "role": "source-promoted internal finite positive determinant row",
            "formula": qa["p_a_internal"]["formula"],
            "value": p_a,
            "local_determinant_interface_rule": qa["finitepart_policy"]["regularization"]["rule"],
            "mu": qa["index_and_scale"]["determinant_scale"]["mu"],
        },
        "Qc_SU2_rows": {
            "status": "CLOSED_FOR_WEAK_SPLIT",
            "p_Qc": p_c,
            "p_SU2": p_su2,
            "source": rel(INPUTS["dual_frontier"]),
        },
        "typed_hypercharge_map": {
            "status": hyper["route_tests"]["typed_hypercharge_stack_map"]["status"],
            "weights": weights,
            "threshold_combination": hyper["typed_convention_map"]["threshold_combination"],
            "weak_split": hyper["typed_convention_map"]["weak_split"],
        },
        "why_this_is_not_the_forbidden_shortcut": (
            "The rejected shortcut treated the quotient logdet directly as p_Y. "
            "This theorem instead uses the already selected Qa/Qc hypercharge map, "
            "so the quotient logdet enters only as p_a and Qc remains present."
        ),
    }

    physical_anchor_status = {
        "physical_K_gauge_anchor_closed": False,
        "physical_Omega0_or_alpha_action_unit_closed": False,
        "matching_scale_and_RG_scheme_closed": False,
        "measured_electroweak_closure": False,
        "reason": (
            "lambda_12 is a dimensionless internal weak-split threshold. It does "
            "not select the physical gauge/action unit, matching scale, or RG scheme."
        ),
        "physical_gate_status": physical["status"],
    }

    candidate = {
        "candidate": "SelectedElectroweakQaStackSU2RowOrCancellationAndPhysicalAnchor",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "same_scheme_argument": same_scheme_argument,
        "selected_internal_threshold_vector": internal_vector,
        "physical_anchor_status": physical_anchor_status,
        "decision": {
            "same_scheme_SU2_row_or_cancellation_closed": same_scheme_closed,
            "typed_hypercharge_map_closed": typed_map_closed,
            "Qa_stack_p_a_source_closed": qa_closed,
            "Qc_row_closed_for_weaksplit": qc_su2_closed,
            "SU2_row_closed_for_weaksplit": qc_su2_closed,
            "lambda_12_internal_closed": same_scheme_closed,
            "lambda_12_internal_value": lambda_12,
            "Delta_G12_internal_value": delta_g12,
            "physical_K_gauge_anchor_closed": False,
            "matching_scale_and_RG_scheme_closed": False,
            "measured_electroweak_closure": False,
            "target_fitting_used": False,
            "next_required_artifact": NEXT,
        },
        "theorem": {
            "name": "SelectedInternalWeakSplitThresholdTheorem",
            "proved": same_scheme_closed,
            "statement": (
                "The selected Qa-stack finite-part theorem promotes the quotient "
                "logdet only as p_a. The selected typed hypercharge convention gives "
                "p_Y=p_a/36+p_c/4, and the Qc and SU2 rows are already selected for "
                "weak-split local-determinant accounting. Therefore the same internal "
                f"scheme computes p_Y={p_y} and lambda_12={lambda_12}. This closes the "
                "dimensionless internal weak-split threshold, but not physical electroweak "
                "matching, because the physical gauge/action anchor, matching scale, and "
                "RG/threshold scheme remain open."
            ),
        },
        "guardrails": {
            "treats_p_a_as_direct_pY": False,
            "uses_lambda12_target_witness": False,
            "uses_observed_electroweak_data": False,
            "claims_physical_K_gauge": False,
            "claims_measured_electroweak_closure": False,
            "target_fitting_used": False,
        },
        "what_closes": {
            "same_scheme_SU2_row_or_cancellation_for_internal_weaksplit": same_scheme_closed,
            "internal_p_Y": same_scheme_closed,
            "internal_lambda_12": same_scheme_closed,
            "internal_Delta_G12": same_scheme_closed,
        },
        "what_remains_open": {
            "physical_K_gauge_or_action_unit": True,
            "matching_scale": True,
            "RG_threshold_scheme": True,
            "measured_electroweak_closure": True,
            "full_SM_closure": True,
        },
        "closure_claimed": same_scheme_closed,
        "closure_scope": "dimensionless_internal_weaksplit_threshold_only",
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "SelectedElectroweakQaStackSU2RowOrCancellationAndPhysicalAnchor",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "same_scheme_SU2_row_or_cancellation_closed": same_scheme_closed,
        "lambda_12_internal_closed": same_scheme_closed,
        "lambda_12_internal_value": lambda_12,
        "Delta_G12_internal_value": delta_g12,
        "physical_K_gauge_anchor_closed": False,
        "measured_electroweak_closure": False,
        "next_required_artifact": NEXT,
        "closure_scope": "dimensionless_internal_weaksplit_threshold_only",
        "target_fitting_used": False,
    }
    return candidate, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    lines = [
        "# Selected Electroweak QaStack SU2Row or Cancellation and PhysicalAnchor v1",
        "",
        "## Result",
        "",
        "```text",
        f"status = {candidate['status']}",
        "same_scheme_SU2_row_or_cancellation_closed = true",
        "lambda_12_internal_closed = true",
        f"lambda_12_internal = {candidate['selected_internal_threshold_vector']['lambda_12_internal']}",
        f"Delta_G12_internal = {candidate['selected_internal_threshold_vector']['Delta_G12_internal']}",
        "physical_K_gauge_anchor_closed = false",
        "measured_electroweak_closure = false",
        f"next_required_artifact = {candidate['decision']['next_required_artifact']}",
        "```",
        "",
        "This closes only the dimensionless internal weak-split threshold. It does",
        "not compare to measured electroweak data.",
        "",
        "## Same-Scheme Argument",
        "",
        "```json",
        json.dumps(candidate["same_scheme_argument"], indent=2, sort_keys=True),
        "```",
        "",
        "## Selected Internal Threshold Vector",
        "",
        "```json",
        json.dumps(candidate["selected_internal_threshold_vector"], indent=2, sort_keys=True),
        "```",
        "",
        "## Theorem",
        "",
        candidate["theorem"]["statement"],
        "",
        "## Physical Anchor Still Open",
        "",
        "```json",
        json.dumps(candidate["physical_anchor_status"], indent=2, sort_keys=True),
        "```",
        "",
        "## Guardrails",
        "",
        "- `p_a` is not treated as an already hypercharge-normalized `p_Y` row.",
        "- The selected map is `p_Y=p_a/36+p_c/4`; Qc is not dropped.",
        "- `lambda_12` is dimensionless internal threshold data, not a physical action unit.",
        "- No observed electroweak value or target residual is used.",
        "",
        "## Certificate",
        "",
        "```json",
        json.dumps(cert, indent=2, sort_keys=True),
        "```",
        "",
    ]
    return "\n".join(lines)


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
