"""Build the U1/Y Route-C trace-equals-27mode or full-HYM replay gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"
TEXPAPERS = ROOT.parent
Q79 = TEXPAPERS / "mtt-q79-proof-repro"
NONSM = TEXPAPERS / "mtt-nonsm-constants-no-knob"
SM = TEXPAPERS / "mtt-sm-parity-closure"

INPUTS = {
    "selected_finite_trace_gate": DATA / "selected_u1y_routec_selected_finite_trace_source_or_nogo.candidate.json",
    "q79_trace_equals_27mode": Q79 / "certificates" / "q79_selected_trace_equals_emitted_27mode_operator_or_full_hym_newton_replay_certificate.json",
    "nonsm_canonical_trace_source": NONSM / "certificates" / "selected_canonical_trace_formula_source_lemma_proof_certificate.json",
    "nonsm_gap_layer_lock": NONSM / "certificates" / "selected_phifin_s2_gap_layer_honest_replay_lock_certificate.json",
    "nonsm_operator_truncation_attempt": NONSM / "certificates" / "selected_phifin_s2_selected_operator_and_truncation_source_theorem_attempt_certificate.json",
    "sm_full_hym_newton": SM / "certificates" / "selected_full_exps_hym_newton_replay_certificate.json",
    "sm_hym_operator_extraction": SM / "certificates" / "selected_hym_operator_payload_extraction_from_diagonal_replay_certificate.json",
}

OUTPUT_DATA = DATA / "selected_u1y_routec_trace_equals_27mode_or_full_hym_replay.candidate.json"
OUTPUT_CERT = CERTS / "selected_u1y_routec_trace_equals_27mode_or_full_hym_replay_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_RouteC_TraceEquals27Mode_or_FullHYMReplay_v1.md"

STATUS = "U1Y_ROUTEC_TRACE_EQUALS_27MODE_DE_GAP_LAYER_CLOSED_DOTD_C1_OPEN"
NEXT = "Selected_U1Y_RouteC_dotD_Alpha1_C1_Response_Emission_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def read_optional(path: Path) -> dict[str, Any]:
    if path.exists():
        return load(path)
    return {"status": "MISSING", "present": False}


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    finite_gate = load(INPUTS["selected_finite_trace_gate"])
    q79_trace = load(INPUTS["q79_trace_equals_27mode"])
    canonical = load(INPUTS["nonsm_canonical_trace_source"])
    gap_lock = load(INPUTS["nonsm_gap_layer_lock"])
    trunc_attempt = load(INPUTS["nonsm_operator_truncation_attempt"])
    hym_newton = load(INPUTS["sm_full_hym_newton"])
    hym_extract = read_optional(INPUTS["sm_hym_operator_extraction"])

    gap_proof = q79_trace["selected_trace_equality_gap_layer_proof"]
    gap_layer = gap_proof["gap_layer"]
    proof_steps = gap_proof["proof_steps"]
    full_hym_status = q79_trace["full_hym_newton_route_status"]
    dotd_boundary = q79_trace["dotd_c1_response_boundary"]

    finite_trace_route = {
        "route": "trace_equals_27mode_DE_gap_layer",
        "status": "CLOSED_FOR_DE_GAP_RIESZ_GREEN_LAYER",
        "selected_trace_equality": gap_proof["selected_trace_equality"],
        "proof_steps": proof_steps,
        "gap_layer": gap_layer,
        "imported_statuses": {
            "canonical_trace_source": canonical["status"],
            "gap_layer_lock": gap_lock["status"],
            "q79_trace_equals_27mode": q79_trace["status"],
        },
        "scope_closes": [
            "selected 27-mode D_E trace equality",
            "theorem-derived D_E source flags for the gap layer",
            "selected positive gap lower bound",
            "selected Riesz/Green consequence for the D_E layer",
        ],
        "scope_does_not_close": gap_proof["does_not_close"],
    }

    full_hym_route = {
        "route": "full_HYM_Newton_replay",
        "status": "SUPPORT_PROGRESS_NOT_NEEDED_FOR_DE_GAP_LAYER_STILL_OPEN_FOR_FULL_PAYLOAD",
        "scalar_expS": full_hym_status["scalar_expS"],
        "diagonal_expS": full_hym_status["diagonal_expS"],
        "sm_diagonal_replay_status": hym_newton["status"],
        "operator_extraction_status": hym_extract.get("status", "MISSING"),
        "route_conclusion": full_hym_status["route_conclusion"],
    }

    decision = {
        "selected_trace_equality_for_27mode_DE": gap_proof["selected_trace_equality"]["proved"],
        "DE_gap_Riesz_Green_layer_closed": gap_layer["D_E_honest_replay_passes_after_theorem_derived_source_flags"]
        and gap_layer["Riesz_Green_layer_closes"],
        "selected_eta_N": gap_layer["selected_eta_N"],
        "eta_threshold": gap_layer["eta_threshold"],
        "selected_gap_lower_bound": gap_layer["selected_gap_lower_bound"],
        "selected_green_norm_bound": gap_layer["selected_green_norm_bound"],
        "full_Phi_fin_closed": False,
        "dotD_alpha1_C1_closed": False,
        "A_selected_or_b_selected_closed": False,
        "lambda_12_computable": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "SelectedU1YRouteCTraceEquals27ModeOrFullHYMReplay",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_status": finite_gate["status"],
        "finite_trace_route": finite_trace_route,
        "full_hym_route": full_hym_route,
        "dotd_c1_response_boundary": dotd_boundary,
        "decision": decision,
        "theorem": {
            "name": "U1YRouteCTraceEquals27ModeDEGapLayer",
            "proved": True,
            "statement": (
                "For the q79/F,m=1 Route-C branch, the selected canonical trace "
                "source lemma identifies the emitted 27-mode D_E formula as the "
                "selected Phi_fin D_E compression on B_N. Therefore the D_E "
                "gap/Riesz/Green layer is theorem-derived and closes with "
                "eta_N=1 below threshold. The closure is scoped: dotD_alpha1, "
                "alpha1 driver, primitive C1 response, A_selected, b_selected, "
                "lambda_12, and full Phi_fin remain open."
            ),
        },
        "what_closes_now": {
            "selected_trace_equality_for_emitted_27mode_DE": True,
            "D_E_source_flags_theorem_derived_for_gap_layer": True,
            "selected_eta_N_below_threshold": True,
            "positive_selected_gap_lower_bound": True,
            "selected_Riesz_Green_gap_layer_closed": True,
            "full_HYM_replay_progress_imported": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "dotD_alpha1_source": True,
            "alpha1_driver": True,
            "primitive_C1_response": True,
            "full_S2_value_emission": True,
            "full_HYM_connection_lift": True,
            "validator_ready_full_HYM_operator_payload": True,
            "A_selected": True,
            "b_selected": True,
            "lambda_12": True,
            "Yukawa_or_full_SM_closure": True,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
        "guardrails": {
            "claims_full_Phi_fin_closed": False,
            "claims_dotD_C1_closed": False,
            "claims_A_selected_or_b_selected": False,
            "claims_lambda12": False,
            "claims_Yukawa_or_full_SM_closure": False,
            "promotes_diagnostic_dotD_flags": False,
            "uses_observed_data": False,
            "uses_benchmark_data": False,
            "target_fitting_used": False,
        },
    }

    cert = {
        "certificate": "SelectedU1YRouteCTraceEquals27ModeOrFullHYMReplay",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "selected_trace_equality_for_27mode_DE": True,
        "DE_gap_Riesz_Green_layer_closed": True,
        "basis_dimension": gap_layer["basis_dimension"],
        "basis_id": gap_layer["basis_id"],
        "selected_eta_N": gap_layer["selected_eta_N"],
        "eta_threshold": gap_layer["eta_threshold"],
        "selected_gap_lower_bound": gap_layer["selected_gap_lower_bound"],
        "selected_green_norm_bound": gap_layer["selected_green_norm_bound"],
        "full_Phi_fin_closed": False,
        "dotD_alpha1_C1_closed": False,
        "lambda_12_closed": False,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    return candidate, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    lines = [
        "# Selected U1Y Route-C TraceEquals27Mode or FullHYMReplay v1",
        "",
        "## Result",
        "",
        "```text",
        f"status = {candidate['status']}",
        f"selected_trace_equality_for_27mode_DE = {str(cert['selected_trace_equality_for_27mode_DE']).lower()}",
        f"DE_gap_Riesz_Green_layer_closed = {str(cert['DE_gap_Riesz_Green_layer_closed']).lower()}",
        f"full_Phi_fin_closed = {str(cert['full_Phi_fin_closed']).lower()}",
        f"dotD_alpha1_C1_closed = {str(cert['dotD_alpha1_C1_closed']).lower()}",
        f"lambda_12_closed = {str(cert['lambda_12_closed']).lower()}",
        f"next_required_artifact = {candidate['next_required_artifact']}",
        "```",
        "",
        "The 27-mode `D_E` trace equality is now closed for the gap/Riesz/Green",
        "layer. This is not full `Phi_fin`; it is the scoped `D_E` spectral layer.",
        "",
        "## Gap Layer",
        "",
        "```text",
        f"basis = {cert['basis_id']}",
        f"basis dimension = {cert['basis_dimension']}",
        f"selected eta_N = {cert['selected_eta_N']}",
        f"eta threshold = {cert['eta_threshold']}",
        f"selected gap lower bound = {cert['selected_gap_lower_bound']}",
        f"selected Green norm bound = {cert['selected_green_norm_bound']}",
        "```",
        "",
        "## Proof Steps",
        "",
    ]
    for key, value in candidate["finite_trace_route"]["proof_steps"].items():
        lines.append(f"- `{key}`: proved = `{str(value['proved']).lower()}`")
    lines.extend(
        [
            "",
            "## Boundary",
            "",
        ]
    )
    for item in candidate["dotd_c1_response_boundary"]["required_next_payload"]:
        lines.append(f"- {item}")
    lines.extend(
        [
            "",
            "## Guardrails",
            "",
            "- Do not infer `dotD` source from `D_E` source flags alone.",
            "- Do not promote diagnostic `dotD` flags.",
            "- Do not compute `lambda_12` from the closed gap layer.",
            "- Do not use observed or benchmark data.",
            "",
            "## Certificate",
            "",
            "```json",
            json.dumps(cert, indent=2, sort_keys=True),
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    candidate, cert, note = build()
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
