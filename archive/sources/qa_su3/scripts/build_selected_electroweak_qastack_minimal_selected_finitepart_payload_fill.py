"""Fill the minimal selected finite-part payload as far as current sources allow."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "route_gate": DATA / "selected_electroweak_qastack_determinantfunctional_or_selected_abase_emission.candidate.json",
    "trace_equals_27mode": DATA / "selected_u1y_routec_trace_equals_27mode_or_full_hym_replay.candidate.json",
    "localdet_gate": DATA / "selected_electroweak_u1y_localdeterminant_from_27mode_de_gaplayer.candidate.json",
    "conditional_spectrum": DATA / "selected_electroweak_u1y_localdeterminant_from_27mode_de_gaplayer.spectrum_attempt.json",
    "pperp_policy": DATA / "selected_u1_quotient_projector_pperp_and_trace_policy.candidate.json",
    "quotient_lemma": DATA / "selected_electroweak_u1y_quotientdeterminant_lemma.candidate.json",
    "threshold_index": DATA / "u1_su2_threshold_index_source_theorem.candidate.json",
}

OUTPUT_DATA = DATA / "selected_electroweak_qastack_minimal_selected_finitepart_payload_fill.candidate.json"
OUTPUT_CERT = CERTS / "selected_electroweak_qastack_minimal_selected_finitepart_payload_fill_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Electroweak_QaStack_Minimal_SelectedFinitePart_Payload_Fill_v1.md"

STATUS = "ELECTROWEAK_QASTACK_MINIMAL_SELECTED_FINITEPART_PAYLOAD_PARTIAL_FILL_FINITEPART_PROMOTION_OPEN"
NEXT = "Selected_Electroweak_QaStack_FinitePartPolicy_and_IndexScale_SourceTheorem_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    route_gate = load(INPUTS["route_gate"])
    trace = load(INPUTS["trace_equals_27mode"])
    localdet = load(INPUTS["localdet_gate"])
    spectrum = load(INPUTS["conditional_spectrum"])
    pperp = load(INPUTS["pperp_policy"])
    quotient = load(INPUTS["quotient_lemma"])
    threshold_index = load(INPUTS["threshold_index"])

    selected_trace = trace["finite_trace_route"]
    quotient_spectrum = quotient["quotient_positive_spectrum"]
    quotient_logdet = quotient["decision"]["quotient_logdet"]

    filled_payload = {
        "schema": "SelectedElectroweakQaStackMinimalSelectedFinitePartPayload.v1.fill_attempt",
        "source_identity": {
            "selected_by_mtt_for_DE_gap_layer": trace["decision"]["selected_trace_equality_for_27mode_DE"],
            "selected_by_mtt_for_determinant_finite_part": False,
            "same_branch_q79_F_m1": True,
            "no_observed_or_benchmark_inputs": True,
            "source_certificate": trace["inputs"]["q79_trace_equals_27mode"],
            "source_scope": "selected 27-mode D_E gap/Riesz/Green layer only",
        },
        "domain_and_operator": {
            "selected_B_N_basis_id": selected_trace["gap_layer"]["basis_id"],
            "selected_B_N_basis_dimension": selected_trace["gap_layer"]["basis_dimension"],
            "sector_restriction_to_V_mod_s": {
                "status": "SUPPORT_FROM_PPERP_DOMAIN_POLICY_NOT_DETERMINANT_FUNCTIONAL",
                "Pperp_policy_closed": pperp["decision"]["U1_operator_trace_uses_P_perp"],
                "quotient_rank": quotient["rank_accounting"]["quotient_rank"],
                "rank3_carrier": quotient["rank_accounting"]["rank3_carrier"],
            },
            "operator_choice": "direct_BN_finite_part_preferred_A_base_validator_only",
            "positive_eigenvalue_table_on_V_mod_s": {
                "status": "CONDITIONAL_COMPUTABLE_NOT_SELECTED_FINITE_PART",
                "entries": quotient_spectrum,
                "logdet": quotient_logdet,
            },
            "kernel_policy": {
                "status": "PARTIAL",
                "zero_shared_line_removed_before_positive_determinant": True,
                "rank3_model_kernel_multiplicity": spectrum["rank3_model_kernel_multiplicity"],
                "reason_open": "No same-source theorem yet says this kernel policy defines the selected electroweak finite part.",
            },
            "H_zero_cluster_policy": {
                "status": "OPEN_NEUTRAL_FOR_CURRENT_ETA1",
                "selected_eta_N": spectrum["H_sector_zero_cluster_shift_candidate"]["selected_eta_N"],
                "current_logdet_delta_if_included": 0.0,
                "reason_open": spectrum["H_sector_zero_cluster_shift_candidate"]["reason"],
            },
        },
        "finite_part": {
            "regularization": {
                "status": "CONDITIONAL_FINITE_POSITIVE_ZETA_LOGDET_ONLY",
                "candidate_formula": quotient["quotient_logdet"]["formula"],
                "candidate_value": quotient_logdet,
                "selected_as_finite_part": False,
            },
            "index_weights": {
                "status": "INDEX_SOURCE_THEOREM_SUPPORT_NOT_DETERMINANT_WEIGHT_PROMOTION",
                "U1_index_support": pperp["decision"]["selected_U1_index"],
                "SU2_index_support": pperp["decision"]["selected_SU2_index"],
                "threshold_index_promotion_open": threshold_index["decision"]["promoted_to_selected_threshold_index"],
            },
            "determinant_scale": {
                "status": "OPEN",
                "candidate_internal_mu": None,
                "reason_open": "No source-emitted internal determinant scale or scale-cancellation theorem is present for this finite part.",
            },
            "p_a_value": {
                "status": "NOT_PROMOTED",
                "conditional_value_if_all_finitepart_policies_close": quotient_logdet,
            },
        },
        "electroweak_completion_only_after_payload": {
            "same_scheme_SU2_row_or_cancellation": {
                "status": "OPEN",
                "reason": localdet["required_functional"]["must_select"][3],
            },
            "lambda12_formula": {
                "status": "FORBIDDEN_UNTIL_P_A_AND_SU2_CLOSE",
                "value": None,
            },
        },
    }

    blockers = {
        "regularization_finite_part_selected": False,
        "index_weights_promoted_to_determinant_weights": False,
        "determinant_scale_selected": False,
        "same_scheme_SU2_row_or_cancellation": False,
        "p_a_promotable": False,
    }

    candidate = {
        "candidate": "SelectedElectroweakQaStackMinimalSelectedFinitePartPayloadFill",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_status": route_gate["status"],
        "filled_payload": filled_payload,
        "blockers": blockers,
        "decision": {
            "source_identity_for_DE_gap_layer_filled": True,
            "V_mod_s_positive_table_computed_conditionally": True,
            "kernel_policy_partially_filled": True,
            "H_zero_cluster_currently_logdet_neutral": True,
            "regularization_finite_part_selected": False,
            "index_weights_promoted_to_determinant_weights": False,
            "determinant_scale_selected": False,
            "selected_p_a_promoted": False,
            "lambda_12_closed": False,
            "measured_electroweak_closure": False,
            "current_source_nogo_proved": True,
            "mathematical_impossibility_claimed": False,
            "target_fitting_used": False,
            "next_required_artifact": NEXT,
        },
        "theorem": {
            "name": "MinimalFinitePartPayloadCurrentSourcePartialFill",
            "proved": True,
            "statement": (
                "The current source fills the selected D_E gap-layer identity and a "
                "conditional positive table on V/<s>, with zero shared-line removal "
                "and H zero-cluster neutrality for eta_N=1. It does not select the "
                "finite zeta/heat/torsion regularization as the electroweak finite "
                "part, does not promote index support to determinant weights, and "
                "does not emit a determinant scale. Therefore p_a and lambda_12 remain open."
            ),
        },
        "minimal_next_payload": {
            "name": NEXT,
            "must_emit": [
                "finite-part regularization theorem selecting finite positive zeta/logdet on V/<s>",
                "source theorem promoting the 2/3 and 1 index support to determinant weights or replacing them",
                "selected determinant scale mu or scale-cancellation theorem",
                "same-scheme SU2 determinant row or exact cancellation before lambda_12",
            ],
        },
        "guardrails": {
            "promotes_conditional_positive_table": False,
            "promotes_Pperp_index_as_determinant_weight": False,
            "promotes_eta1_neutrality_as_policy": False,
            "promotes_selected_p_a": False,
            "claims_lambda12": False,
            "claims_measured_electroweak_closure": False,
            "uses_observed_electroweak_data": False,
            "target_fitting_used": False,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "SelectedElectroweakQaStackMinimalSelectedFinitePartPayloadFill",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "source_identity_for_DE_gap_layer_filled": True,
        "V_mod_s_positive_table_computed_conditionally": True,
        "regularization_finite_part_selected": False,
        "selected_p_a_promoted": False,
        "lambda_12_closed": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
    }
    return candidate, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    lines = [
        "# Selected Electroweak QaStack Minimal SelectedFinitePart Payload Fill v1",
        "",
        "## Result",
        "",
        "```text",
        f"status = {candidate['status']}",
        "source_identity_for_DE_gap_layer_filled = true",
        "V_mod_s_positive_table_computed_conditionally = true",
        "regularization_finite_part_selected = false",
        "selected_p_a_promoted = false",
        "lambda_12_closed = false",
        f"next_required_artifact = {candidate['decision']['next_required_artifact']}",
        "```",
        "",
        "The minimal finite-part payload is partially filled. The selected `D_E` gap",
        "layer and the conditional `V/<s>` positive table are available, but the",
        "finite-part promotion fields are still not source-selected.",
        "",
        "## Filled Payload",
        "",
        "```json",
        json.dumps(candidate["filled_payload"], indent=2, sort_keys=True),
        "```",
        "",
        "## Blockers",
        "",
        "```json",
        json.dumps(candidate["blockers"], indent=2, sort_keys=True),
        "```",
        "",
        "## Theorem",
        "",
        candidate["theorem"]["statement"],
        "",
        "## Minimal Next Payload",
        "",
        f"Next artifact: `{candidate['minimal_next_payload']['name']}`.",
        "",
    ]
    for item in candidate["minimal_next_payload"]["must_emit"]:
        lines.append(f"- {item}")
    lines.extend(
        [
            "",
            "## Guardrails",
            "",
            "- The conditional positive table is not promoted as `p_a`.",
            "- `P_perp` index support is not promoted as determinant weighting.",
            "- Current eta_N=1 zero-cluster neutrality is not promoted as a policy theorem.",
            "- `lambda_12` and measured electroweak closure remain open.",
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
    DATA.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    PROOF.mkdir(parents=True, exist_ok=True)
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
