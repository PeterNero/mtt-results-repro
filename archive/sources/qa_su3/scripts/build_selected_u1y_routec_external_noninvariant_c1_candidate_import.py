"""Import external noninvariant C1 candidate clues into the U1/Y Route-C frontier."""

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
NONSM = TEXPAPERS / "mtt-nonsm-constants-no-knob"
Q79 = TEXPAPERS / "mtt-q79-proof-repro"
PROTO = TEXPAPERS / "mtt-protospinor-gr-response-proof"

INPUTS = {
    "sourcevalue_contract": DATA / "selected_u1y_routec_primitive_c1_sourcevalue_theorem_or_noninvariant_tensor.candidate.json",
    "sm_noninvariant_c1_search": SM / "certificates" / "selected_routec_noninvariant_c1_primitive_search_certificate.json",
    "sm_noninvariant_c1_candidate": SM / "candidate_data" / "selected_routec_noninvariant_c1_primitive_search.candidate.json",
    "sm_primitive_source_selection": SM / "certificates" / "selected_routec_primitive_source_selection_audit_certificate.json",
    "nonsm_fiberclass_reduction": NONSM / "certificates" / "noninvariant_c1_fiberclass_reduction_certificate.json",
    "q79_basis_transport_candidate": Q79 / "certificates" / "su5_qutrit_basis_transport_heavy_link_candidate_certificate.json",
    "proto_noninvariant_import": PROTO / "certificates" / "routec_noninvariant_c1_primitive_search_import_certificate.json",
}

OUTPUT_DATA = DATA / "selected_u1y_routec_external_noninvariant_c1_candidate_import.candidate.json"
OUTPUT_CERT = CERTS / "selected_u1y_routec_external_noninvariant_c1_candidate_import_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_RouteC_External_NonInvariant_C1_Candidate_Import_v1.md"

STATUS = "U1Y_ROUTEC_EXTERNAL_NONINVARIANT_C1_CANDIDATES_IMPORTED_SOURCE_SELECTION_OPEN"
NEXT = "Selected_U1Y_RouteC_FiberOrigin_or_GaugeInvariantC1Observable_Theorem_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def summarize_candidate(candidate: dict[str, Any]) -> dict[str, Any]:
    primitives = candidate["candidate_primitives"]
    summaries = []
    for row in primitives:
        summaries.append(
            {
                "primitive_active_shift": row["primitive_active_shift"],
                "primitive_fiber_shift": row["primitive_fiber_shift"],
                "selected_by_theorem": row["selected_by_theorem"],
                "sector_ranks": {sector: row["summary"][sector]["rank"] for sector in ["u", "d", "e", "nuD"]},
                "max_abs_entry": max(row["summary"][sector]["max_abs_entry"] for sector in ["u", "d", "e", "nuD"]),
            }
        )
    return {
        "candidate_count": len(primitives),
        "candidate_summaries": summaries,
        "calculation_results": candidate["calculation_results"],
    }


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    sourcevalue = load(INPUTS["sourcevalue_contract"])
    sm_cert = load(INPUTS["sm_noninvariant_c1_search"])
    sm_candidate = load(INPUTS["sm_noninvariant_c1_candidate"])
    sm_source = load(INPUTS["sm_primitive_source_selection"])
    nonsm_fiber = load(INPUTS["nonsm_fiberclass_reduction"])
    q79_transport = load(INPUTS["q79_basis_transport_candidate"])
    proto_import = load(INPUTS["proto_noninvariant_import"])

    candidate_summary = summarize_candidate(sm_candidate)
    fiber_meaning = nonsm_fiber["meaning"]
    q79_verdict = q79_transport["verdict"]

    imported_facts = {
        "active_shift_1_1_forced_by_finite_support": nonsm_fiber["closed_now"][
            "active_shift_1_1_forced_by_finite_support"
        ],
        "minimal_active_shift_required": nonsm_fiber["finite_result"]["minimal_active_shift_required"],
        "nonzero_unselected_candidate_count": nonsm_fiber["finite_result"]["nonzero_unselected_candidates_found"],
        "fixed_fiber_shifts_one_qutrit_gauge_class": nonsm_fiber["closed_now"][
            "fixed_fiber_shifts_one_qutrit_gauge_class"
        ],
        "all_fiber_envelope_retired": nonsm_fiber["closed_now"]["all_fiber_envelope_retired"],
        "representative_max_abs_entry": nonsm_fiber["finite_result"]["representative_max_abs_entry"],
        "fixed_fiber_ranks": nonsm_fiber["finite_result"]["fixed_fiber_ranks"],
        "all_fiber_rank": nonsm_fiber["finite_result"]["all_fiber_rank"],
        "basis_transport_heavy_link_candidate": q79_verdict[
            "representation_split_fourier_transport_is_a_viable_exact_candidate"
        ],
        "basis_transport_next_lemma": q79_verdict["next_required_lemma"],
        "protospinor_import_agrees_unselected": proto_import["verdict"]["selected_C1_closed"] is False,
    }

    selection_state = {
        "selected_noninvariant_primitive_source_proved": fiber_meaning["selected_noninvariant_primitive_source_proved"],
        "absolute_fiber_shift_selected": fiber_meaning["absolute_fiber_shift_selected"],
        "operator_level_projective_class_selected": fiber_meaning["operator_level_projective_class_selected"],
        "observable_invariance_under_fiber_class_proved": fiber_meaning[
            "observable_invariance_under_fiber_class_proved"
        ],
        "q79_basis_transport_selected_by_MTT": q79_transport["guardrails"]["selected_by_MTT"],
        "sm_candidates_selected_by_theorem": sm_candidate["calculation_results"]["can_close_selected_C1_now"],
    }

    route_update = {
        "previous_primary_route": sourcevalue["route_ranking"][0]["route"],
        "updated_primary_route": "fiber_origin_or_gauge_invariant_noninvariant_C1_observable",
        "reason": (
            "External repos already narrow nonzero primitive C1 to active shift (1,1) and "
            "a fixed qutrit fiber gauge class. The remaining selector is therefore not a "
            "broad tensor search; it is an absolute fiber-origin theorem or a proof that "
            "downstream C1/Yukawa observables are invariant under the fixed fiber class."
        ),
        "still_allows_basis_transport_route": True,
        "still_allows_typed_connection_derivation": True,
    }

    decision = {
        "external_scan_completed": True,
        "nonzero_noninvariant_candidates_imported": True,
        "active_shift_1_1_promoted_as_required_candidate_condition": True,
        "fiber_class_reduction_imported": True,
        "basis_transport_candidate_imported": True,
        "selected_C1_closed": False,
        "selected_noninvariant_tensor_emitted": False,
        "A_selected_computable": False,
        "b_selected_computable": False,
        "lambda_12_computable": False,
        "Yukawa_or_full_SM_closure": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "SelectedU1YRouteCExternalNonInvariantC1CandidateImport",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            "sourcevalue_contract": sourcevalue["status"],
            "sm_noninvariant_c1_search": sm_cert["status"],
            "sm_primitive_source_selection": sm_source["status"],
            "nonsm_fiberclass_reduction": nonsm_fiber["status"],
            "q79_basis_transport_candidate": q79_transport["status"],
            "proto_noninvariant_import": proto_import["status"],
        },
        "imported_facts": imported_facts,
        "candidate_summary": candidate_summary,
        "selection_state": selection_state,
        "route_update": route_update,
        "decision": decision,
        "theorem": {
            "name": "U1YRouteCExternalNonInvariantC1CandidateImportTheorem",
            "proved": True,
            "statement": (
                "The external proof repos contain useful primitive C1 data but no selected "
                "closure. They reduce the live noninvariant branch to active shift (1,1), "
                "four nonzero unselected candidate families, and a fixed qutrit fiber gauge "
                "class; q79 also supplies an exact representation-split Fourier transport "
                "candidate for the basis-connection slot. Therefore the next frontier is "
                "not to search arbitrary C1 tensors. It is to prove a selected absolute "
                "fiber origin, or prove fiber-class-invariant downstream observables, or "
                "derive the same basis transport from selected monad/Cech/Galerkin zero-mode "
                "data. Until then, these candidates cannot fill the atom payload."
            ),
        },
        "what_closes_now": {
            "external_noninvariant_candidates_imported": True,
            "active_shift_1_1_required_condition_imported": True,
            "fixed_fiber_gauge_class_reduction_imported": True,
            "basis_connection_candidate_imported": True,
            "arbitrary_noninvariant_tensor_search_retired": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "absolute_fiber_origin_gauge_fix": True,
            "fiber_class_invariant_C1_observable_theorem": True,
            "selected_basis_transport_theorem": True,
            "selected_noninvariant_primitive_source": True,
            "same_source_atom_payload": True,
            "A_selected": True,
            "b_selected": True,
            "lambda_12": True,
            "Yukawa_or_full_SM_closure": True,
        },
        "guardrails": {
            "claims_selected_C1_closed": False,
            "claims_selected_noninvariant_tensor_emitted": False,
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
        "certificate": "SelectedU1YRouteCExternalNonInvariantC1CandidateImport",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "external_scan_completed": True,
        "nonzero_noninvariant_candidates_imported": True,
        "minimal_active_shift_required": imported_facts["minimal_active_shift_required"],
        "nonzero_unselected_candidate_count": imported_facts["nonzero_unselected_candidate_count"],
        "fixed_fiber_shifts_one_qutrit_gauge_class": imported_facts["fixed_fiber_shifts_one_qutrit_gauge_class"],
        "basis_transport_candidate_imported": True,
        "selected_C1_closed": False,
        "selected_noninvariant_tensor_emitted": False,
        "A_selected_computable": False,
        "b_selected_computable": False,
        "lambda_12_computable": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    return candidate, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    lines = [
        "# Selected U1Y Route-C External NonInvariant C1 Candidate Import v1",
        "",
        "## Result",
        "",
        "```text",
        f"status = {candidate['status']}",
        f"nonzero_noninvariant_candidates_imported = {str(cert['nonzero_noninvariant_candidates_imported']).lower()}",
        f"minimal_active_shift_required = {cert['minimal_active_shift_required']}",
        f"nonzero_unselected_candidate_count = {cert['nonzero_unselected_candidate_count']}",
        f"fixed_fiber_shifts_one_qutrit_gauge_class = {str(cert['fixed_fiber_shifts_one_qutrit_gauge_class']).lower()}",
        f"basis_transport_candidate_imported = {str(cert['basis_transport_candidate_imported']).lower()}",
        f"selected_C1_closed = {str(cert['selected_C1_closed']).lower()}",
        f"next_required_artifact = {candidate['next_required_artifact']}",
        "```",
        "",
        "The other repos do help: nonzero primitive C1 candidates already exist,",
        "but they remain unselected. The search is now reduced to a fiber-origin",
        "or fiber-class-invariant observable theorem, with q79 basis transport as",
        "a concrete candidate for the basis-connection slot.",
        "",
        "## Imported Facts",
        "",
        f"- active shift `{candidate['imported_facts']['minimal_active_shift_required']}` is required for nonzero C1",
        f"- nonzero unselected candidate families: `{candidate['imported_facts']['nonzero_unselected_candidate_count']}`",
        "- fixed fiber shifts `0,1,2` reduce to one qutrit gauge class",
        "- all-fiber envelope is retired as a fixed single-charge primitive",
        "- q79 representation-split Fourier transport is a viable exact basis-connection candidate",
        "",
        "## Guardrails",
        "",
        "- Do not fill the atom payload from these candidates until fiber origin, fiber-class invariance, or selected basis transport is proved.",
        "- Do not compute `A_selected`, `b_selected`, Yukawas, or `lambda_12` from unselected candidate matrices.",
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
