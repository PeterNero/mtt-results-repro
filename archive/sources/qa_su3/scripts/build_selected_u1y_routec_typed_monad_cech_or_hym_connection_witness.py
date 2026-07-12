"""Build the U1/Y Route-C typed monad/Cech or HYM connection witness contract."""

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

INPUTS = {
    "u1y_source_or_typed_de_gate": DATA / "selected_u1y_routec_selected_source_certificate_or_typed_de_construction.candidate.json",
    "q79_typed_monad_cech_or_hym_witness": Q79 / "certificates" / "q79_typed_monad_cech_or_hym_connection_witness_certificate.json",
    "q79_finite_connection_solve_execution": Q79 / "certificates" / "q79_selected_finite_connection_solve_execution_certificate.json",
}

OUTPUT_DATA = DATA / "selected_u1y_routec_typed_monad_cech_or_hym_connection_witness.candidate.json"
OUTPUT_PAYLOAD = DATA / "selected_u1y_routec_typed_monad_cech_or_hym_connection_witness.open.json"
OUTPUT_CERT = CERTS / "selected_u1y_routec_typed_monad_cech_or_hym_connection_witness_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_RouteC_TypedMonadCech_or_HYMConnectionWitness_v1.md"

STATUS = "U1Y_ROUTEC_TYPED_MONAD_CECH_OR_HYM_CONNECTION_WITNESS_CONTRACT_BUILT_VALUES_OPEN"
NEXT = "Selected_U1Y_RouteC_FiniteHYMConnectionSolve_or_TypedCechPayload_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def status_of(key: str, data: dict[str, Any]) -> dict[str, Any]:
    return {
        "path": rel(INPUTS[key]),
        "present": INPUTS[key].exists(),
        "status": data.get("status", "UNKNOWN"),
        "next_required_artifact": data.get("next_required_artifact"),
        "guardrails": data.get("guardrails"),
    }


def make_payload() -> dict[str, Any]:
    return {
        "schema": "SelectedU1YRouteCTypedMonadCechOrHYMConnectionWitnessPayload.v1",
        "status": "OPEN_VALUES_REQUIRED",
        "branch": {
            "orientation": "F",
            "q": 79,
            "torsion_label_m": 1,
            "antiunitary_partner_retained": True,
        },
        "typed_monad_cech_payload": {
            "typed_f_sections": None,
            "typed_g_sections": None,
            "line_bundle_transition_functions": None,
            "cech_cover": None,
            "cocycle_checks": None,
            "g_after_f_zero_certificate": None,
            "exactness_or_torsion_free_sheaf_control": None,
            "selected_H1_E_representatives": None,
            "sector_projection_maps_Q_u_d_L_e_N_H": None,
        },
        "direct_hym_payload": {
            "selected_holomorphic_bundle_or_sheaf_model": None,
            "selected_gauduchon_or_balanced_metric": None,
            "hym_connection_coefficients": None,
            "gauge_fixing": None,
            "curvature_residual_bounds": None,
            "bianchi_strominger_row": None,
        },
        "finite_routec_solve_payload": {
            "nonidentity_selected_rhoE_boundary_matrices": None,
            "local_A01_or_discrete_connection_variables": None,
            "routec_residual_values": None,
            "selection_functional_or_positive_hessian_gap": None,
            "finite_basis_BN": None,
            "DE_action": None,
            "riesz_gap": None,
            "reduced_green": None,
            "dotD_alpha1": None,
            "primitive_C1_contractions": None,
        },
        "same_source_requirements": {
            "source_certificate": None,
            "same_source_ChernWeil_GS_row": None,
            "same_branch_derivative": None,
            "orientation_selection": None,
            "no_lifted_selected_flags": True,
            "no_observed_or_benchmark_inputs": True,
        },
    }


def missing_leaf_count(value: Any) -> int:
    if value is None:
        return 1
    if isinstance(value, dict):
        return sum(missing_leaf_count(v) for v in value.values())
    if isinstance(value, list):
        return sum(missing_leaf_count(v) for v in value)
    return 0


def build() -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], str]:
    parent = load(INPUTS["u1y_source_or_typed_de_gate"])
    q79_witness = load(INPUTS["q79_typed_monad_cech_or_hym_witness"])
    q79_finite = load(INPUTS["q79_finite_connection_solve_execution"])
    payload = make_payload()

    q79_payload = q79_witness["minimal_actual_witness_payload"]
    witness_attempt = q79_witness["selected_connection_witness_attempt"]
    finite_summary = q79_finite["finite_connection_execution_import_summary"]
    honest_cutset = q79_finite["honest_replay_cutset"]

    payload_counts = {
        "typed_monad_cech_missing": missing_leaf_count(payload["typed_monad_cech_payload"]),
        "direct_hym_missing": missing_leaf_count(payload["direct_hym_payload"]),
        "finite_routec_solve_missing": missing_leaf_count(payload["finite_routec_solve_payload"]),
        "same_source_missing": missing_leaf_count(payload["same_source_requirements"]),
    }

    decision = {
        "contract_built": True,
        "accepts_three_equivalent_witness_routes": True,
        "typed_monad_cech_values_present": False,
        "direct_hym_values_present": False,
        "finite_routec_solve_values_present": False,
        "same_source_certificate_present": False,
        "q79_minimal_payload_imported_as_contract": q79_payload["status"] == "OPEN",
        "finite_prefix_may_seed_but_not_fill_payload": finite_summary["status"] == "FINITE_PREFIX_VALUES_IMPORTED_SOURCE_PROMOTION_OPEN",
        "honest_replay_still_blocked": honest_cutset["status"] == "HONEST_REPLAY_BLOCKED_BY_SOURCE_TRACE_AND_FULL_OPERATOR_PROVENANCE",
        "payload_missing_leaf_count": sum(payload_counts.values()),
        "selected_connection_witness_constructed": False,
        "primitive_C1_values_computed": False,
        "A_selected_or_b_selected_emitted": False,
        "lambda_12_computable": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    theorem = {
        "name": "U1YRouteCTypedMonadCechOrHYMConnectionWitnessContractTheorem",
        "proved": True,
        "statement": (
            "A local U1/Y selected-connection witness contract is constructed. "
            "It accepts exactly three proof-equivalent payload families: typed "
            "monad/Cech data, direct selected HYM/Strominger connection data, or "
            "a finite Route-C solve with selected source provenance and export to "
            "D_E/Riesz/Green/dotD/primitive C1 validators. The current payload is "
            "open: no route supplies values. Existing 27-mode finite data may be "
            "used as seed or comparison data, but not as proof until the same-source "
            "certificate, trace equality, and no-lift replay are supplied."
        ),
    }

    candidate = {
        "candidate": "SelectedU1YRouteCTypedMonadCechOrHYMConnectionWitness",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            key: status_of(key, data)
            for key, data in {
                "u1y_source_or_typed_de_gate": parent,
                "q79_typed_monad_cech_or_hym_witness": q79_witness,
                "q79_finite_connection_solve_execution": q79_finite,
            }.items()
        },
        "payload_path": rel(OUTPUT_PAYLOAD),
        "payload_counts": payload_counts,
        "decision": decision,
        "witness_routes": {
            "typed_monad_cech": q79_payload["acceptable_payloads"]["typed_monad_cech_payload"],
            "direct_hym": q79_payload["acceptable_payloads"]["direct_hym_payload"],
            "finite_routec_solve": q79_payload["acceptable_payloads"]["finite_routec_solve_payload"],
        },
        "blocked_current_attempts": witness_attempt["attempted_routes"],
        "finite_prefix_support": {
            "basis_id": finite_summary["smooth_BN"]["basis_id"],
            "dimension": finite_summary["smooth_BN"]["dimension"],
            "DE_emitted": finite_summary["DE"]["D_E_matrix_on_27_mode_BN_emitted"],
            "dotD_alpha1_emitted": finite_summary["dotD"]["dotD_alpha1_matrix_in_same_basis_emitted"],
            "primitive_C1_engine_built": finite_summary["C1"]["primitive_C1_contraction_engine_built"],
            "selected_by_mtt": finite_summary["nonidentity_rhoE"]["selected_by_mtt"],
        },
        "theorem": theorem,
        "what_closes_now": {
            "local_connection_witness_payload_contract_built": True,
            "typed_monad_cech_route_specified": True,
            "direct_hym_route_specified": True,
            "finite_routec_solve_route_specified": True,
            "same_source_no_lift_requirements_made_machine_readable": True,
            "finite_prefix_values_retained_only_as_nonclosing_support": True,
        },
        "what_remains_open": {
            "fill_any_one_witness_route": True,
            "same_source_certificate": True,
            "selected_trace_equality": True,
            "honest_no_lift_validator_replay": True,
            "primitive_C1_values": True,
            "A_selected": True,
            "b_selected": True,
            "lambda_12": True,
            "full_SM_closure": True,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
        "guardrails": {
            "claims_typed_monad_cech_witness_constructed": False,
            "claims_direct_hym_connection_constructed": False,
            "claims_finite_routec_solve_constructed": False,
            "claims_selected_connection_witness_constructed": False,
            "claims_primitive_C1_values_computed": False,
            "claims_A_selected_or_b_selected": False,
            "claims_lambda12": False,
            "claims_full_sm_closure": False,
            "promotes_finite_prefix_values": False,
            "promotes_lifted_selected_flags": False,
            "uses_observed_or_benchmark_inputs": False,
        },
    }

    cert = {
        "certificate": "SelectedU1YRouteCTypedMonadCechOrHYMConnectionWitness",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "payload_path": rel(OUTPUT_PAYLOAD),
        "note_path": rel(OUTPUT_NOTE),
        "contract_built": decision["contract_built"],
        "accepts_three_equivalent_witness_routes": decision["accepts_three_equivalent_witness_routes"],
        "payload_missing_leaf_count": decision["payload_missing_leaf_count"],
        "selected_connection_witness_constructed": False,
        "primitive_C1_values_computed": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    return candidate, payload, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    lines = [
        "# Selected U1Y Route-C TypedMonadCech or HYMConnectionWitness v1",
        "",
        "## Result",
        "",
        "```text",
        f"status = {candidate['status']}",
        f"contract_built = {str(cert['contract_built']).lower()}",
        f"accepts_three_equivalent_witness_routes = {str(cert['accepts_three_equivalent_witness_routes']).lower()}",
        f"payload_missing_leaf_count = {cert['payload_missing_leaf_count']}",
        f"selected_connection_witness_constructed = {str(cert['selected_connection_witness_constructed']).lower()}",
        f"primitive_C1_values_computed = {str(cert['primitive_C1_values_computed']).lower()}",
        f"next_required_artifact = {candidate['next_required_artifact']}",
        "```",
        "",
        "This creates the local witness contract. It does not fill the witness.",
        "Any one of the three payload families below is enough, provided the data",
        "come from the selected branch and replay without lifted flags.",
        "",
        "## Accepted Witness Routes",
        "",
    ]
    for route, items in candidate["witness_routes"].items():
        lines.append(f"### {route}")
        for item in items:
            lines.append(f"- {item}")
        lines.append("")
    lines.extend(
        [
            "## Finite Prefix Support",
            "",
        ]
    )
    for key, value in candidate["finite_prefix_support"].items():
        lines.append(f"- `{key}`: `{value}`")
    lines.extend(
        [
            "",
            "## Guardrails",
            "",
            "- Finite prefix values are support, not selected provenance.",
            "- One complete witness route is enough; mixing partial routes is not.",
            "- The replay must be honest: no lifted selected-source flags.",
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
    candidate, payload, cert, note = build()
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_PAYLOAD.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_PAYLOAD)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
