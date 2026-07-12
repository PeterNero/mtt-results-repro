"""Build the fiber-origin / gauge-invariant C1 observable theorem gate."""

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
PROTO = TEXPAPERS / "mtt-protospinor-gr-response-proof"

INPUTS = {
    "external_noninvariant_import": DATA / "selected_u1y_routec_external_noninvariant_c1_candidate_import.candidate.json",
    "sm_primitive_fibershift_theorem": SM / "certificates" / "selected_primitivefibershift_or_typedretardedselector_sourcetheorem_certificate.json",
    "sm_primitive_fibershift_candidate": SM / "candidate_data" / "selected_primitivefibershift_or_typedretardedselector_sourcetheorem.candidate.json",
    "sm_fiberclass_invariance": SM / "certificates" / "selected_routec_fiberclass_observable_invariance_or_gaugefix_certificate.json",
    "q79_basis_transport_candidate": Q79 / "certificates" / "su5_qutrit_basis_transport_heavy_link_candidate_certificate.json",
    "proto_basis_transport_reduction": PROTO / "certificates" / "routec_basis_transport_gate_reduction_import_certificate.json",
}

OUTPUT_DATA = DATA / "selected_u1y_routec_fiberorigin_or_gaugeinvariant_c1observable_theorem.candidate.json"
OUTPUT_CERT = CERTS / "selected_u1y_routec_fiberorigin_or_gaugeinvariant_c1observable_theorem_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_RouteC_FiberOrigin_or_GaugeInvariantC1Observable_Theorem_v1.md"

STATUS = "U1Y_ROUTEC_FIBERCLASS_C1_OBSERVABLE_QUOTIENT_CLOSED_MATRIX_REPRESENTATIVE_OPEN"
NEXT = "Selected_U1Y_RouteC_PrimitiveClass_C1Observable_or_HigherOrderFullResponse_SourceEmission_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    external = load(INPUTS["external_noninvariant_import"])
    sm_cert = load(INPUTS["sm_primitive_fibershift_theorem"])
    sm_candidate = load(INPUTS["sm_primitive_fibershift_candidate"])
    sm_invariance = load(INPUTS["sm_fiberclass_invariance"])
    q79_transport = load(INPUTS["q79_basis_transport_candidate"])
    proto_transport = load(INPUTS["proto_basis_transport_reduction"])

    primitive_selector = sm_candidate["primitive_selector"]
    observable_payload = sm_candidate["observable_class_payload"]
    invariant_values = primitive_selector["invariant_spectral_observables"]

    quotient_theorem = {
        "active_shift_selected": sm_cert["active_shift_selected_claimed"],
        "selected_active_shift": primitive_selector["selected_active_shift"],
        "fiber_class_quotient_selected": sm_cert["fiber_class_quotient_selected_claimed"],
        "fixed_fiber_class": primitive_selector["fixed_fiber_class"],
        "computation_representative": primitive_selector["canonical_computation_representative"],
        "absolute_fiber_shift_selected": sm_cert["absolute_fiber_shift_selected_claimed"],
        "absolute_fiber_origin_not_hidden_knob": sm_cert["what_closes"][
            "absolute_fiber_origin_not_used_as_hidden_knob"
        ],
        "why_quotient_allowed": primitive_selector["why_quotient_is_allowed"],
        "why_absolute_shift_not_selected": primitive_selector["why_absolute_shift_not_selected"],
    }

    spectral_observable_summary = {
        "sectors": ["u", "d", "e", "nuD"],
        "fiber_shifts": primitive_selector["fixed_fiber_class"],
        "rank_invariant": all(
            invariant_values[str(shift)][sector]["rank"] == 3
            for shift in primitive_selector["fixed_fiber_class"]
            for sector in ["u", "d", "e", "nuD"]
        ),
        "YYstar_scalar_identity_invariant": all(
            invariant_values[str(shift)][sector]["YYstar_is_scalar_identity"] is True
            for shift in primitive_selector["fixed_fiber_class"]
            for sector in ["u", "d", "e", "nuD"]
        ),
        "YYstar_scalar": invariant_values["0"]["u"]["YYstar_scalar"],
        "det_abs": invariant_values["0"]["u"]["det_abs"],
        "representative_for_computation": observable_payload["representative_for_computation"],
        "current_layer_flavor_splitting_possible": observable_payload["current_layer_flavor_splitting_possible"],
        "reason": observable_payload["reason"],
    }

    downstream_boundary = {
        "can_promote_fixed_fiber_representative_for_current_spectral_observables": True,
        "can_promote_fixed_fiber_representative_for_full_C1_matrix_operator": False,
        "can_compute_A_selected": False,
        "can_compute_b_selected": False,
        "can_compute_yukawa_hierarchy": False,
        "can_compute_CKM_PMNS_CP": False,
        "reason": (
            "The quotient class is spectrally invariant and scalar-permutation degenerate. "
            "It is enough for current C1 spectral observables, but not for a selected matrix "
            "representative or nondegenerate flavor closure."
        ),
    }

    live_routes = {
        "higher_order_or_full_response": sm_cert["what_remains_open"]["selected_higher_order_or_full_response_matrices"],
        "operator_level_basis_transport": sm_cert["what_remains_open"]["operator_level_basis_transport"],
        "basis_transport_candidate_viable": q79_transport["verdict"][
            "representation_split_fourier_transport_is_a_viable_exact_candidate"
        ],
        "basis_transport_selected": q79_transport["guardrails"]["selected_by_MTT"],
        "proto_basis_transport_reduction_status": proto_transport["status"],
        "proto_basis_transport_open": proto_transport["still_open"]["operator_level_basis_transport"],
    }

    decision = {
        "fiberclass_quotient_for_current_C1_spectral_observables_closed": True,
        "active_shift_1_1_selected_for_current_C1_layer": True,
        "shift0_allowed_as_computation_gauge": True,
        "absolute_fiber_origin_selected": False,
        "absolute_fiber_origin_used_as_hidden_knob": False,
        "selected_matrix_representative_for_full_C1_operator": False,
        "A_selected_computable": False,
        "b_selected_computable": False,
        "lambda_12_computable": False,
        "Yukawa_or_full_SM_closure": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "SelectedU1YRouteCFiberOriginOrGaugeInvariantC1ObservableTheorem",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            "external_noninvariant_import": external["status"],
            "sm_primitive_fibershift_theorem": sm_cert["status"],
            "sm_fiberclass_invariance": sm_invariance["status"],
            "q79_basis_transport_candidate": q79_transport["status"],
            "proto_basis_transport_reduction": proto_transport["status"],
        },
        "quotient_theorem": quotient_theorem,
        "spectral_observable_summary": spectral_observable_summary,
        "downstream_boundary": downstream_boundary,
        "live_routes": live_routes,
        "decision": decision,
        "theorem": {
            "name": "U1YRouteCFiberClassC1ObservableQuotientTheorem",
            "proved": True,
            "statement": (
                "For the current finite primitive C1 spectral-observable layer, the "
                "active shift (1,1) is selected and fixed fiber shifts 0,1,2 form one "
                "selected quotient class. Shift 0 is therefore a legal computation gauge "
                "for rank, determinant absolute value, traces/singular spectrum of YY*, "
                "and related current C1 spectral invariants. This does not select an "
                "absolute fiber origin or a full matrix representative for A_selected. "
                "The quotient-class matrices are scalar-permutation degenerate, so "
                "nondegenerate Yukawa hierarchy, CKM/PMNS, CP, b_selected, and lambda_12 "
                "still require selected higher-order/full-response data or operator-level "
                "basis transport from the same source."
            ),
        },
        "what_closes_now": {
            "active_shift_1_1_selected_for_current_C1_layer": True,
            "fixed_fiber_quotient_class_selected_for_current_C1_spectral_observables": True,
            "shift0_computation_gauge_allowed": True,
            "absolute_fiber_origin_hidden_knob_rejected": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_matrix_representative_for_full_C1_operator": True,
            "operator_level_basis_transport": True,
            "selected_higher_order_or_full_response_matrices": True,
            "selected_b_selected": True,
            "A_selected": True,
            "b_selected": True,
            "lambda_12": True,
            "Yukawa_or_full_SM_closure": True,
        },
        "guardrails": {
            "claims_absolute_fiber_origin_selected": False,
            "claims_full_C1_matrix_representative": False,
            "claims_A_selected": False,
            "claims_b_selected": False,
            "claims_lambda12": False,
            "claims_Yukawa_or_full_SM_closure": False,
            "uses_observed_data": False,
            "uses_benchmark_data": False,
            "uses_locked_target_columns": False,
            "uses_diagnostic_lambda12_values": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "SelectedU1YRouteCFiberOriginOrGaugeInvariantC1ObservableTheorem",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "fiberclass_quotient_for_current_C1_spectral_observables_closed": True,
        "active_shift_1_1_selected_for_current_C1_layer": True,
        "shift0_allowed_as_computation_gauge": True,
        "absolute_fiber_origin_selected": False,
        "selected_matrix_representative_for_full_C1_operator": False,
        "A_selected_computable": False,
        "b_selected_computable": False,
        "lambda_12_computable": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    return candidate, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    obs = candidate["spectral_observable_summary"]
    lines = [
        "# Selected U1Y Route-C FiberOrigin or GaugeInvariant C1Observable Theorem v1",
        "",
        "## Result",
        "",
        "```text",
        f"status = {candidate['status']}",
        f"fiberclass_quotient_for_current_C1_spectral_observables_closed = {str(cert['fiberclass_quotient_for_current_C1_spectral_observables_closed']).lower()}",
        f"active_shift_1_1_selected_for_current_C1_layer = {str(cert['active_shift_1_1_selected_for_current_C1_layer']).lower()}",
        f"shift0_allowed_as_computation_gauge = {str(cert['shift0_allowed_as_computation_gauge']).lower()}",
        f"absolute_fiber_origin_selected = {str(cert['absolute_fiber_origin_selected']).lower()}",
        f"selected_matrix_representative_for_full_C1_operator = {str(cert['selected_matrix_representative_for_full_C1_operator']).lower()}",
        f"A_selected_computable = {str(cert['A_selected_computable']).lower()}",
        f"b_selected_computable = {str(cert['b_selected_computable']).lower()}",
        f"next_required_artifact = {candidate['next_required_artifact']}",
        "```",
        "",
        "This imports the useful quotient theorem: shift `0` is a legal computation",
        "representative for current C1 spectral observables. It is not a physical",
        "absolute fiber origin and not a full selected matrix representative.",
        "",
        "## Current Spectral Class",
        "",
        f"- `YY*` scalar: `{obs['YYstar_scalar']}`",
        f"- `|det|`: `{obs['det_abs']}`",
        f"- rank invariant across fixed shifts: `{obs['rank_invariant']}`",
        f"- flavor splitting at this layer: `{obs['current_layer_flavor_splitting_possible']}`",
        "",
        "## Next",
        "",
        "- selected higher-order/full-response matrices, or",
        "- operator-level basis transport from the same source, then",
        "- `A_selected`, `b_selected`, and no-proxy flavor observables.",
        "",
        "## Guardrails",
        "",
        "- Do not use shift `0` as a hidden absolute fiber-origin knob.",
        "- Do not compute Yukawas, CKM/PMNS, CP, or `lambda_12` from the quotient-class representative alone.",
        "",
        "## Certificate",
        "",
        "```json",
        json.dumps(cert, indent=2, sort_keys=True),
        "```",
        "",
    ]
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
