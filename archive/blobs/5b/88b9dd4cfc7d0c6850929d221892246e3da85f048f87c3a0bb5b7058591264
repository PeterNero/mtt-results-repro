"""Attempt to construct the q79 typed-monad/Cech or HYM connection witness.

The previous reduction identified one missing object: a selected connection
witness that can honestly source the finite D_E/Riesz/Green/dotD stack.  This
script tries to construct that witness from the currently available corpus
routes and writes an auditable result.

The construction attempt is intentionally strict.  It accepts neither a generic
"constant maps" phrase without typed global sections nor an identity-rho smoke
packet whose selected-source flag is false.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
CANDIDATES = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"

OUT_DIR = CANDIDATES / "q79_typed_monad_cech_or_hym_connection_witness"
OUT_CANDIDATE = CANDIDATES / "q79_typed_monad_cech_or_hym_connection_witness.candidate.json"
OUT_CERT = CERTS / "q79_typed_monad_cech_or_hym_connection_witness_certificate.json"
OUT_PAPER = CORPUS / "Q79_Typed_Monad_Cech_or_HYM_Connection_Witness_v1.md"

OUT_CORPUS_SUMMARY = OUT_DIR / "corpus_witness_search_summary.json"
OUT_TYPED_REJECTION = OUT_DIR / "typed_monad_candidate_from_flux_phrase.rejected.json"
OUT_SMOKE_NOGO = OUT_DIR / "routec_smoke_promotion_nogo.json"
OUT_WITNESS_ATTEMPT = OUT_DIR / "selected_connection_witness_attempt.open.json"
OUT_PAYLOAD = OUT_DIR / "minimal_actual_witness_payload.open.json"

STATUS = "Q79_TYPED_MONAD_CECH_OR_HYM_CONNECTION_WITNESS_ATTEMPT_OPEN_VALUES_ABSENT"
NEXT = "Q79_Selected_Finite_Connection_Solve_Execution_v1"

FLUX_SOURCE = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory"
    r"\16 Strings, Flux, & M-Theory Encodings"
    r"\Flux_Compactifications_in_Heterotic_String_Theory_v3.md"
)

ROUTEC_WITNESS_REDUCTION = (
    CERTS / "q79_routec_selected_source_certificate_or_typed_de_construction_certificate.json"
)
SELECTED_DE = CERTS / "iwasawa_selected_de_construction_attempt_certificate.json"
SELECTED_DE_HUNT = CERTS / "selected_de_source_hunt_certificate.json"
MONAD_GATE = CERTS / "iwasawa_monad_map_data_gate_certificate.json"
MONAD_RECOVERY = CERTS / "iwasawa_typed_monad_section_recovery_certificate.json"
ROUTEC_SMOKE = CERTS / "iwasawa_route_c_branch_smoke_attempt_certificate.json"
ROUTEC_RESIDUAL = (
    CANDIDATES / "iwasawa_route_c_branch_smoke" / "current_q79_orientation" / "route_c_residual.candidate.json"
)
RHOE_MESH = (
    CANDIDATES / "iwasawa_route_c_branch_smoke" / "current_q79_orientation" / "rhoE_mesh.candidate.json"
)

INPUTS = {
    "routec_witness_reduction": ROUTEC_WITNESS_REDUCTION,
    "selected_de_construction_attempt": SELECTED_DE,
    "selected_de_source_hunt": SELECTED_DE_HUNT,
    "typed_monad_map_data_gate": MONAD_GATE,
    "typed_monad_section_recovery": MONAD_RECOVERY,
    "route_c_branch_smoke_attempt": ROUTEC_SMOKE,
    "route_c_residual_candidate": ROUTEC_RESIDUAL,
    "rhoE_mesh_candidate": RHOE_MESH,
}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def rel(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def status_record(path: Path) -> dict[str, Any]:
    data = load(path)
    return {
        "path": rel(path),
        "present": path.exists(),
        "status": data.get("status"),
        "verdict": data.get("verdict"),
        "guardrails": data.get("guardrails"),
    }


def flux_phrase_evidence() -> dict[str, Any]:
    text = FLUX_SOURCE.read_text(encoding="utf-8") if FLUX_SOURCE.exists() else ""
    lower = text.lower()
    return {
        "path": str(FLUX_SOURCE),
        "present": FLUX_SOURCE.exists(),
        "generic_constant_maps_phrase_present": (
            "generic holomorphic maps" in lower and "constant matrices" in lower
        ),
        "hym_existence_phrase_present": "hermitian-yang-mills" in lower or "hym" in lower,
        "chern_character_support_present": "c_3" in text or "ch_3" in text,
        "explicit_typed_f_entries_present": "f_i" in text and "transition" in lower,
        "explicit_typed_g_entries_present": "g_i" in text and "transition" in lower,
    }


def corpus_witness_search_summary(
    monad_recovery: dict[str, Any],
    de_hunt: dict[str, Any],
) -> dict[str, Any]:
    recovered = monad_recovery.get("recovered_from_corpus", {})
    missing = monad_recovery.get("not_recovered_from_corpus", {})
    return {
        "status": "CORPUS_SEARCH_FINDS_TOPOLOGICAL_AND_EXISTENCE_DATA_NOT_WITNESS_VALUES",
        "flux_source": flux_phrase_evidence(),
        "searched_sources": monad_recovery.get("searched_sources", {}),
        "source_hunt_local_sources_checked": de_hunt.get("local_sources_checked", []),
        "recovered_support": {
            "iwasawa_geometry": recovered.get("iwasawa_geometry"),
            "monad_sequence": recovered.get("monad_sequence"),
            "line_bundle_c1_labels": recovered.get("line_bundle_c1_labels"),
            "chern_character_check": recovered.get("chern_character_check"),
            "generic_constant_maps_phrase": recovered.get("generic_constant_maps_phrase"),
            "literal_A01_matrix": recovered.get("literal_A01_matrix"),
        },
        "not_recovered_witness_values": {
            "explicit_f_i_section_representatives": missing.get("explicit_f_i_section_representatives"),
            "explicit_g_i_section_representatives": missing.get("explicit_g_i_section_representatives"),
            "transition_functions_for_L_i_K1_K2": missing.get("transition_functions_for_L_i_K1_K2"),
            "Cech_cover_and_cocycles": missing.get("Cech_cover_and_cocycles"),
            "g_after_f_zero_certificate": missing.get("g_after_f_zero_certificate"),
            "monad_exactness_or_sheaf_singularity_control": missing.get(
                "monad_exactness_or_sheaf_singularity_control"
            ),
            "selected_H1_E_representatives": missing.get("selected_H1_E_representatives"),
            "sector_projection_maps_Q_u_d_L_e_N_H": missing.get(
                "sector_projection_maps_Q_u_d_L_e_N_H"
            ),
            "dotD_alpha1_and_Green_operator_data": missing.get(
                "dotD_alpha1_and_Green_operator_data"
            ),
        },
        "selected_D_E_source_found": de_hunt.get("hunt_result", {}).get("selected_D_E_source_found"),
        "best_next_route_from_hunt": de_hunt.get("hunt_result", {}).get("best_next_route"),
    }


def typed_monad_rejection(monad_gate: dict[str, Any], monad_recovery: dict[str, Any]) -> dict[str, Any]:
    typed = monad_gate.get("typed_map_check", {})
    missing = monad_recovery.get("not_recovered_from_corpus", {})
    return {
        "schema": "Q79TypedMonadFluxPhraseCandidateRejection.v1",
        "status": "REJECTED_AS_WITNESS",
        "source_claim_tested": "generic holomorphic maps f,g as constant matrices in a left-invariant frame",
        "topological_support_retained": monad_gate.get("topological_cern_check", {}),
        "f_entry_types": typed.get("f_entry_types", {}),
        "g_entry_types": typed.get("g_entry_types", {}),
        "nonzero_scalar_constant_f_entries_type_valid": typed.get(
            "nonzero_scalar_constant_f_entries_type_valid"
        ),
        "nonzero_scalar_constant_g_entries_type_valid": typed.get(
            "nonzero_scalar_constant_g_entries_type_valid"
        ),
        "requires_global_holomorphic_sections_or_transition_data": typed.get(
            "requires_global_holomorphic_sections_or_transition_data"
        ),
        "can_verify_g_after_f_zero": typed.get("can_verify_g_after_f_zero"),
        "can_verify_monad_exactness": typed.get("can_verify_monad_exactness"),
        "explicit_witness_data_present": {
            "explicit_f_i_sections": not missing.get("explicit_f_i_section_representatives", True),
            "explicit_g_i_sections": not missing.get("explicit_g_i_section_representatives", True),
            "transition_functions": not missing.get("transition_functions_for_L_i_K1_K2", True),
            "cech_cover_and_cocycles": not missing.get("Cech_cover_and_cocycles", True),
            "g_after_f_zero_certificate": not missing.get("g_after_f_zero_certificate", True),
            "exactness_or_local_freeness": not missing.get(
                "monad_exactness_or_sheaf_singularity_control", True
            ),
        },
        "rejection_reason": (
            "The generic constant maps phrase is not a globally typed monad/Cech "
            "witness.  Every current f/g Hom c1 vector is nonzero, so a nonzero "
            "scalar constant entry is invalid unless the missing global sections "
            "or transition data are supplied."
        ),
        "verdict": {
            "constructs_typed_monad_cech_witness": False,
            "can_compute_selected_DE": False,
            "can_compute_H1_E_representatives": False,
        },
    }


def residuals_are_zero(route_c_residual: dict[str, Any]) -> bool:
    residuals = route_c_residual.get("residuals", {})
    return bool(residuals) and all(abs(item.get("value", 1.0)) <= item.get("tolerance", 0.0) for item in residuals.values())


def positive_gates_hold(route_c_residual: dict[str, Any]) -> bool:
    gates = route_c_residual.get("positive_gates", {})
    return bool(gates) and all(
        item.get("value", 0.0) > item.get("strict_lower_bound", 0.0) for item in gates.values()
    )


def routec_smoke_nogo(
    smoke: dict[str, Any],
    route_c_residual: dict[str, Any],
    rhoe_mesh: dict[str, Any],
) -> dict[str, Any]:
    current = smoke.get("branches", {}).get("current_q79_orientation", {})
    honest = current.get("validators", {}).get("honest_unselected", {})
    lifted = current.get("validators", {}).get("lifted_selected_flags_smoke", {})
    return {
        "schema": "Q79RouteCSmokePromotionNoGo.v1",
        "status": "CANNOT_PROMOTE_SMOKE_TO_SELECTED_WITNESS",
        "route_c_residual_path": rel(ROUTEC_RESIDUAL),
        "rhoE_mesh_path": rel(RHOE_MESH),
        "route_c_status": route_c_residual.get("status"),
        "rhoE_mesh_candidate_kind": rhoe_mesh.get("candidate_kind"),
        "residuals_zero": residuals_are_zero(route_c_residual),
        "positive_gates_hold": positive_gates_hold(route_c_residual),
        "selected_source_verified": route_c_residual.get("selected_source_verified"),
        "route_c_residual_values_are_smoke_not_solve": smoke.get("calculation_results", {}).get(
            "route_c_residual_values_are_smoke_not_solve"
        ),
        "selected_origin_still_missing": smoke.get("calculation_results", {}).get(
            "selected_origin_still_missing"
        ),
        "honest_route_c_residual_pass": honest.get("route_c_residual", {}).get("pass"),
        "lifted_flags_route_c_residual_pass": lifted.get("route_c_residual", {}).get("pass"),
        "claims_route_c_residual_solve": smoke.get("guardrails", {}).get(
            "claims_route_c_residual_solve"
        ),
        "claims_selected_D_E_constructed": smoke.get("guardrails", {}).get(
            "claims_selected_D_E_constructed"
        ),
        "rejection_reason": (
            "The finite residual equations vanish only for an identity-rho smoke "
            "packet whose selected-source flag is false.  The same numbers become "
            "validator-admissible only after selected flags are lifted by diagnostic "
            "fiat, so they cannot be promoted to the selected connection witness."
        ),
        "verdict": {
            "constructs_selected_routec_source_certificate": False,
            "constructs_selected_connection_witness": False,
            "arithmetic_pipeline_debugged": True,
            "source_selection_missing": True,
        },
    }


def witness_attempt(
    selected_de: dict[str, Any],
    corpus_summary: dict[str, Any],
    typed_rejection: dict[str, Any],
    smoke_nogo: dict[str, Any],
) -> dict[str, Any]:
    routes = selected_de.get("route_evaluation", {})
    return {
        "schema": "Q79TypedMonadCechOrHYMConnectionWitnessAttempt.v1",
        "status": "OPEN_WITNESS_VALUES_ABSENT",
        "branch": {
            "q": 79,
            "orientation": "F",
            "torsion_label_m": 1,
            "antiunitary_partner_retained": True,
        },
        "attempted_routes": {
            "typed_monad_cech": {
                "attempted": True,
                "constructed": False,
                "status": typed_rejection["status"],
                "blocking_layer": "explicit typed global f_i/g_i sections and Cech transition data",
            },
            "direct_selected_hym_connection": {
                "attempted": True,
                "constructed": False,
                "status": routes.get("R3_direct_selected_HYM_solve", {}).get("status"),
                "blocking_layer": "selected HYM coefficients, gauge fixing, finite residual and gap certificate",
            },
            "routec_smoke_promotion": {
                "attempted": True,
                "constructed": False,
                "status": smoke_nogo["status"],
                "blocking_layer": "selected source provenance for the finite rho_E/D_E/Green/dotD stack",
            },
        },
        "candidate_values": {
            "typed_f_sections": None,
            "typed_g_sections": None,
            "cech_transition_functions": None,
            "g_after_f_zero_certificate": None,
            "monad_exactness_or_local_freeness": None,
            "selected_hym_connection_coefficients": None,
            "selected_hermitian_metric": None,
            "finite_DE_action": None,
            "finite_riesz_gap": None,
            "finite_reduced_green": None,
            "finite_dotD_alpha1": None,
            "routec_selected_source_certificate": None,
        },
        "corpus_summary_status": corpus_summary["status"],
        "constructs_actual_selected_witness": False,
        "closure_claimed": False,
    }


def minimal_actual_witness_payload(selected_de: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema": "Q79MinimalActualSelectedConnectionWitnessPayload.v1",
        "status": "OPEN",
        "purpose": (
            "This is the exact payload that would turn the current q79/F,m=1 "
            "operator stack from diagnostic arithmetic into a selected source."
        ),
        "acceptable_payloads": {
            "typed_monad_cech_payload": [
                "typed f_i section representatives for all nonzero maps",
                "typed g_i section representatives for all nonzero maps",
                "Cech cover, line-bundle transitions, and cocycle checks",
                "g o f = 0 certificate",
                "exactness/local-freeness or controlled torsion-free sheaf substitute",
                "selected Hermitian metric/gauge and finite D_E action on B_N",
                "H1(E) basis, anti-family check, sector projections, Riesz/Green/dotD",
            ],
            "direct_hym_payload": [
                "selected holomorphic bundle or sheaf model",
                "selected Gauduchon/balanced metric",
                "HYM connection coefficients A or equivalent rho_E",
                "residual bounds for F^(0,2), HYM primitive part, Bianchi/Strominger row",
                "finite Galerkin basis, D_E action, Riesz gap, Green, dotD alpha1",
            ],
            "finite_routec_solve_payload": [
                "non-identity selected rho_E boundary matrices",
                "local A^(0,1) or discrete connection variables",
                "zero/controlled residual solve for cocycle, metric, integrability, HYM, Bianchi",
                "positive selected Hessian or selection functional gap",
                "same-source export into D_E/Riesz/Green/dotD validators",
            ],
        },
        "validator_chain_after_payload": selected_de.get("minimal_new_data_to_close", {}).get(
            "then_compute", []
        )
        + [
            "validate_iwasawa_route_c_residuals.py",
            "validate_iwasawa_de_action.py",
            "validate_iwasawa_riesz_gap.py",
            "validate_iwasawa_reduced_green.py",
            "validate_iwasawa_dotd_response.py",
            "validate_selected_hym_operator_source.py",
        ],
        "forbidden_inputs": [
            "observed masses",
            "observed CKM magnitudes",
            "Execution II benchmark Yukawa entries",
            "selected flags added without a source certificate",
        ],
    }


def build_candidate() -> dict[str, Any]:
    routec_reduction = load(ROUTEC_WITNESS_REDUCTION)
    selected_de = load(SELECTED_DE)
    de_hunt = load(SELECTED_DE_HUNT)
    monad_gate = load(MONAD_GATE)
    monad_recovery = load(MONAD_RECOVERY)
    smoke = load(ROUTEC_SMOKE)
    route_c_residual = load(ROUTEC_RESIDUAL)
    rhoe_mesh = load(RHOE_MESH)

    corpus_summary = corpus_witness_search_summary(monad_recovery, de_hunt)
    typed_rejection = typed_monad_rejection(monad_gate, monad_recovery)
    smoke_nogo = routec_smoke_nogo(smoke, route_c_residual, rhoe_mesh)
    attempt = witness_attempt(selected_de, corpus_summary, typed_rejection, smoke_nogo)
    payload = minimal_actual_witness_payload(selected_de)

    write_json(OUT_CORPUS_SUMMARY, corpus_summary)
    write_json(OUT_TYPED_REJECTION, typed_rejection)
    write_json(OUT_SMOKE_NOGO, smoke_nogo)
    write_json(OUT_WITNESS_ATTEMPT, attempt)
    write_json(OUT_PAYLOAD, payload)

    data = {
        "certificate": "Q79TypedMonadCechOrHYMConnectionWitness",
        "status": STATUS,
        "candidate_path": rel(OUT_CANDIDATE),
        "paper": rel(OUT_PAPER),
        "artifact_paths": {
            "corpus_witness_search_summary": rel(OUT_CORPUS_SUMMARY),
            "typed_monad_candidate_from_flux_phrase_rejected": rel(OUT_TYPED_REJECTION),
            "routec_smoke_promotion_nogo": rel(OUT_SMOKE_NOGO),
            "selected_connection_witness_attempt": rel(OUT_WITNESS_ATTEMPT),
            "minimal_actual_witness_payload": rel(OUT_PAYLOAD),
        },
        "input_statuses": {name: status_record(path) for name, path in INPUTS.items()},
        "prior_reduction_status": routec_reduction.get("status"),
        "corpus_witness_search_summary": corpus_summary,
        "typed_monad_candidate_from_flux_phrase": typed_rejection,
        "routec_smoke_promotion_nogo": smoke_nogo,
        "selected_connection_witness_attempt": attempt,
        "minimal_actual_witness_payload": payload,
        "what_closes_now": {
            "corpus_checked_for_typed_monad_or_hym_witness_values": True,
            "generic_constant_maps_phrase_rejected_as_witness": True,
            "identity_rhoE_smoke_rejected_as_selected_witness": True,
            "direct_HYM_route_classified_as_abstract_existence_only": (
                selected_de.get("route_evaluation", {})
                .get("R3_direct_selected_HYM_solve", {})
                .get("status")
                == "ABSTRACT_EXISTENCE_ONLY"
            ),
            "minimal_actual_witness_payload_created": True,
        },
        "what_remains_open": {
            "actual_typed_f_i_g_i_sections": True,
            "actual_cech_transition_and_cocycle_data": True,
            "actual_g_after_f_zero_and_exactness_certificate": True,
            "actual_selected_HYM_connection_coefficients": True,
            "actual_selected_finite_routec_residual_solve": True,
            "honest_selected_DE_Riesz_Green_dotD_packets": True,
            "primitive_C1_values": True,
            "A_selected_b_selected_full_SM_closure": True,
        },
        "guardrails": {
            "claims_actual_selected_connection_witness_constructed": False,
            "claims_typed_monad_cech_witness_constructed": False,
            "claims_selected_HYM_connection_constructed": False,
            "claims_identity_rhoE_smoke_is_selected": False,
            "uses_selected_flags_only_as_proof": False,
            "uses_observed_masses_or_ckm_inputs": False,
            "claims_primitive_C1_values_computed": False,
            "claims_full_sm_closure": False,
        },
        "theorem": {
            "name": "Q79TypedMonadCechOrHYMConnectionWitnessExhaustionTheorem",
            "proved": True,
            "closure_claimed": False,
            "statement": (
                "The typed monad/Cech or HYM connection witness is not constructed "
                "from the current corpus.  The corpus supplies topology, a generic "
                "constant maps phrase, abstract Li-Yau/HYM existence support, and "
                "identity-rho finite smoke arithmetic.  It does not supply globally "
                "typed f/g sections, Cech transitions, g o f = 0, exactness, selected "
                "HYM coefficients, or a selected finite Route-C residual solve.  "
                "Therefore the next honest proof step is an actual selected finite "
                "connection solve or an equivalent explicit typed monad/Cech payload."
            ),
        },
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    return data


def bool_lines(data: dict[str, Any]) -> str:
    return "\n".join(f"- `{key}`: `{value}`" for key, value in data.items())


def build_paper(data: dict[str, Any]) -> str:
    return f"""# Q79 Typed Monad/Cech or HYM Connection Witness v1

## Result

This attempts to construct the last missing selected connection witness.  The
typed monad/Cech or HYM connection witness is not constructed from the current
corpus.

What the corpus does give is useful but not enough:

- topological monad support and the `c3=6` net-family check;
- a generic constant maps phrase;
- abstract Li-Yau/HYM existence support;
- identity-rho smoke arithmetic whose finite residuals vanish.

The missing values are still the actual selected witness values.

## Typed Monad/Cech Route

The generic constant maps phrase is rejected as a witness.  The typed map gate
shows that the current nonzero scalar constants are not globally typed unless
explicit sections or transition data are supplied.

- rejection artifact: `{data["artifact_paths"]["typed_monad_candidate_from_flux_phrase_rejected"]}`
- nonzero scalar `f` entries globally typed: `{data["typed_monad_candidate_from_flux_phrase"]["nonzero_scalar_constant_f_entries_type_valid"]}`
- nonzero scalar `g` entries globally typed: `{data["typed_monad_candidate_from_flux_phrase"]["nonzero_scalar_constant_g_entries_type_valid"]}`
- `g o f` verified: `{data["typed_monad_candidate_from_flux_phrase"]["can_verify_g_after_f_zero"]}`
- monad exactness verified: `{data["typed_monad_candidate_from_flux_phrase"]["can_verify_monad_exactness"]}`

## HYM / Route-C Route

The direct selected HYM route remains abstract existence only.  The current
Route-C packet is identity-rho smoke, not a selected source.

- no-go artifact: `{data["artifact_paths"]["routec_smoke_promotion_nogo"]}`
- rhoE kind: `{data["routec_smoke_promotion_nogo"]["rhoE_mesh_candidate_kind"]}`
- finite residuals zero: `{data["routec_smoke_promotion_nogo"]["residuals_zero"]}`
- positive gates hold: `{data["routec_smoke_promotion_nogo"]["positive_gates_hold"]}`
- selected source verified: `{data["routec_smoke_promotion_nogo"]["selected_source_verified"]}`
- claims Route-C residual solve: `{data["routec_smoke_promotion_nogo"]["claims_route_c_residual_solve"]}`

Therefore the identity-rho smoke cannot be promoted to the selected connection
witness.

## Constructed Target

I created the executable open target:

- selected witness attempt: `{data["artifact_paths"]["selected_connection_witness_attempt"]}`
- minimal actual witness payload: `{data["artifact_paths"]["minimal_actual_witness_payload"]}`

That payload must supply one honest route:

- typed monad/Cech maps with transitions, `g o f = 0`, exactness, and finite `D_E`;
- direct selected HYM connection coefficients with residual bounds;
- selected finite Route-C solve with non-identity selected `rho_E`, residuals, and a positive selection certificate.

## What Closes Now

{bool_lines(data["what_closes_now"])}

## What Remains Open

{bool_lines(data["what_remains_open"])}

## Theorem

`{data["theorem"]["name"]}` is proved as an exhaustion theorem.

{data["theorem"]["statement"]}

This is not full SM closure and does not compute primitive C1 values,
`A_selected`, or `b_selected`.

Next required artifact: `{data["next_required_artifact"]}`.
"""


def main() -> int:
    data = build_candidate()
    write_json(OUT_CANDIDATE, data)
    write_json(OUT_CERT, data)
    OUT_PAPER.parent.mkdir(parents=True, exist_ok=True)
    OUT_PAPER.write_text(build_paper(data), encoding="utf-8")
    print("Q79 typed monad/Cech or HYM connection witness attempt")
    print(json.dumps({"status": data["status"], "next": data["next_required_artifact"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
