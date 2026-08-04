"""Import Route-C Galerkin execution cutset and primitive search."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SM = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure")

PREVIOUS = CERTS / "visible_routec_phifin_alpha1_derivative_fill_reduction_certificate.json"
SOLVE_SPEC = SM / "certificates" / "selected_routec_strominger_galerkin_solve_spec_certificate.json"
FIRST_RUN = SM / "certificates" / "selected_routec_strominger_galerkin_first_run_certificate.json"
FIRST_RUN_PACKET = SM / "candidate_data" / "selected_routec_strominger_galerkin_first_run.candidate.json"
SELECTOR = SM / "certificates" / "selected_routec_source_selector_and_basis_theorem_certificate.json"
PROVENANCE_BASIS = SM / "certificates" / "selected_routec_source_provenance_or_basis_certificate_certificate.json"
PROVENANCE_BASIS_PACKET = SM / "candidate_data" / "selected_routec_source_provenance_or_basis_certificate.candidate.json"
EMISSION = SM / "certificates" / "selected_phifin_payload_or_bn_basis_emission_certificate.json"
R1_R4 = SM / "certificates" / "selected_routec_r1_source_or_r4_bn_basis_fill_certificate.json"
PRIMITIVE_SEARCH = SM / "certificates" / "selected_routec_selected_primitive_emission_search_certificate.json"
NONIDENTITY_RHOE = SM / "certificates" / "selected_routec_nonidentity_rhoe_bn_construction_certificate.json"
SMOOTH_BN = SM / "certificates" / "selected_routec_smooth_bn_galerkin_lift_certificate.json"
DE_SMOOTH_BN = SM / "certificates" / "selected_routec_de_action_on_smooth_bn_certificate.json"
DOTD_SMOOTH_BN = SM / "certificates" / "selected_routec_sector_projectors_dotd_on_smooth_bn_certificate.json"
C1_SMOOTH_BN = SM / "certificates" / "selected_routec_c1_primitive_response_on_smooth_bn_certificate.json"

OUTPUT_PACKET = DATA / "routec_galerkin_execution_cutset_and_primitive_search.candidate.json"
OUTPUT_CERT = CERTS / "routec_galerkin_execution_cutset_and_primitive_search_certificate.json"
OUTPUT_NOTE = CORPUS / "RouteC_Galerkin_Execution_Cutset_and_Primitive_Search_v1.md"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    solve = load(SOLVE_SPEC)
    first = load(FIRST_RUN)
    first_packet = load(FIRST_RUN_PACKET)
    selector = load(SELECTOR)
    provenance_basis = load(PROVENANCE_BASIS)
    provenance_basis_packet = load(PROVENANCE_BASIS_PACKET)
    emission = load(EMISSION)
    r1_r4 = load(R1_R4)
    primitive = load(PRIMITIVE_SEARCH)
    nonidentity = load(NONIDENTITY_RHOE)
    smooth_bn = load(SMOOTH_BN)
    de_bn = load(DE_SMOOTH_BN)
    dotd_bn = load(DOTD_SMOOTH_BN)
    c1_bn = load(C1_SMOOTH_BN)

    closure_vector = emission["closure_vector"]
    remains = primitive["what_remains_open"]
    checks = {
        "C0_previous_frontier_is_routec_galerkin_solve_spec": previous[
            "frontier_update"
        ]["current_next"]
        == "MTT_Selected_RouteC_Strominger_Galerkin_Solve_Spec_v1",
        "C1_solve_spec_built_values_open": solve["status"]
        == "MTT_SELECTED_ROUTEC_STROMINGER_GALERKIN_SOLVE_SPEC_BUILT_VALUES_OPEN"
        and solve["closure_claimed"] is False
        and solve["primary_next_artifact"]
        == "MTT_Selected_RouteC_Strominger_Galerkin_First_Run_v1",
        "C2_first_run_fills_manifest_but_selector_open": first["status"]
        == "MTT_SELECTED_ROUTEC_STROMINGER_GALERKIN_FIRST_RUN_MANIFEST_FILLED_SELECTOR_OPEN"
        and all(first["manifest_filled"].values())
        and first["formal_lift_lower_validators_all_pass"]
        and first["formal_lift_promotion_passes"]
        and first["proof_promotion_allowed"] is False
        and first_packet["validation"]["honest_root_all_pass"] is False
        and first["primary_next_artifact"]
        == "MTT_Selected_RouteC_Source_Selector_and_Basis_Theorem_v1",
        "C3_selector_basis_cutset_locked": selector["status"]
        == "MTT_SELECTED_ROUTEC_SOURCE_SELECTOR_AND_BASIS_CALCULATION_LOCKED_SELECTOR_OPEN"
        and selector["locked_conditions"]
        == ["C1_source_selector_condition", "C2_basis_condition"]
        and selector["closure_claimed"] is False
        and selector["primary_next_artifact"]
        == "MTT_Selected_RouteC_Source_Provenance_or_Basis_Certificate_v1",
        "C4_provenance_and_basis_support_closed_primitives_open": provenance_basis[
            "status"
        ]
        == "MTT_SELECTED_ROUTEC_PROVENANCE_AND_BASIS_ATTEMPT_SUPPORT_CLOSED_PRIMITIVES_OPEN"
        and provenance_basis["support_closed"]["basis_support_closed"]
        and provenance_basis["support_closed"]["provenance_support_closed"]
        and provenance_basis["provenance_closed"] is False
        and provenance_basis["basis_closed"] is False
        and provenance_basis_packet["provenance_gate"]["minimal_missing_primitive"]
        == "Phi_fin_selected_payload"
        and provenance_basis_packet["basis_gate"]["minimal_missing_primitive"]
        == "quotient_valid_B_N_basis_certificate",
        "C5_emission_contracts_lock_R1_to_R6_without_closure": emission[
            "status"
        ]
        == "MTT_SELECTED_PHIFIN_OR_BN_EMISSION_CONTRACTS_LOCKED_VALUES_OPEN"
        and all(value is False for value in closure_vector.values())
        and emission["primary_next_artifact"]
        == "MTT_Selected_RouteC_R1_Source_Certificate_or_R4_BN_Basis_Fill_v1",
        "C6_R1_R4_attempt_blocked_by_unemitted_primitives": r1_r4["status"]
        == "MTT_SELECTED_ROUTEC_R1_R4_FILL_ATTEMPT_BLOCKED_BY_UNEMITTED_SELECTED_PRIMITIVES"
        and r1_r4["R1_closed"] is False
        and r1_r4["R4_closed"] is False
        and r1_r4["R6_ready"] is False
        and r1_r4["primary_next_artifact"]
        == "MTT_Selected_RouteC_Selected_Primitive_Emission_Search_v1",
        "C7_primitive_search_executed_no_legal_emission_found": primitive[
            "status"
        ]
        == "MTT_SELECTED_ROUTEC_PRIMITIVE_EMISSION_SEARCH_EXECUTED_NO_LEGAL_EMISSION_FOUND"
        and primitive["what_closes"]["primitive_search_executed"]
        and primitive["what_closes"]["formal_lift_rejected_as_proof"]
        and all(remains[key] is True for key in closure_vector),
        "C8_constructive_numeric_ladder_exists_but_source_promotion_open": nonidentity[
            "status"
        ]
        == "MTT_SELECTED_ROUTEC_NONIDENTITY_RHOE_NUMERICAL_PACKET_BUILT_BN_STILL_OPEN"
        and smooth_bn["what_closes"]["smooth_scalar_basis_functions_phi_m_emitted"]
        and de_bn["what_closes"]["D_E_matrix_on_27_mode_BN_emitted"]
        and dotd_bn["what_closes"]["dotD_alpha1_matrix_in_same_basis_emitted"]
        and c1_bn["what_closes"]["primitive_C1_contraction_engine_built"]
        and nonidentity["what_remains_open"]["R2_source_promotion_for_rhoE"]
        and smooth_bn["what_remains_open"]["selected_D_E_action_on_basis"]
        and de_bn["what_remains_open"]["selected_D_E_source_promotion"]
        and dotd_bn["what_remains_open"]["selected_source_flags_promoted"]
        and c1_bn["what_remains_open"]["selected_noninvariant_C1_primitive_or_vertex"],
    }

    return {
        "packet": "RouteC_Galerkin_Execution_Cutset_and_Primitive_Search_v1",
        "status": "ROUTEC_GALERKIN_EXECUTION_REDUCED_TO_PRIMITIVE_EMISSION_AND_SOURCE_PROMOTION_OPEN",
        "inputs": {
            "previous": str(PREVIOUS.relative_to(ROOT)),
            "solve_spec": str(SOLVE_SPEC),
            "first_run": str(FIRST_RUN),
            "selector_basis_cutset": str(SELECTOR),
            "provenance_or_basis": str(PROVENANCE_BASIS),
            "emission_contract": str(EMISSION),
            "r1_r4_fill": str(R1_R4),
            "primitive_search": str(PRIMITIVE_SEARCH),
            "nonidentity_rhoe": str(NONIDENTITY_RHOE),
            "smooth_bn": str(SMOOTH_BN),
            "de_smooth_bn": str(DE_SMOOTH_BN),
            "dotd_smooth_bn": str(DOTD_SMOOTH_BN),
            "c1_smooth_bn": str(C1_SMOOTH_BN),
        },
        "theorem": {
            "name": "RouteCGalerkinExecutionCutsetAndPrimitiveSearchTheorem",
            "proved": all(checks.values()),
            "statement": (
                "The selected Route-C/Strominger Galerkin solve has an "
                "executable spec and a filled first-run manifest.  The honest "
                "root payload fails exactly at selected-source/basis provenance, "
                "while the formal lift passes only as diagnostic algebra.  The "
                "remaining proof is reduced to primitive emission: selected "
                "Phi_fin payload/source promotion and quotient-valid B_N basis "
                "certification, followed by honest replay without lifted flags."
            ),
        },
        "checks": checks,
        "execution_chain": {
            "solve_spec_next": solve["primary_next_artifact"],
            "first_run_next": first["primary_next_artifact"],
            "selector_next": selector["primary_next_artifact"],
            "provenance_basis_next": provenance_basis["primary_next_artifact"],
            "emission_next": emission["primary_next_artifact"],
            "r1_r4_next": r1_r4["primary_next_artifact"],
            "primitive_search_status": primitive["status"],
        },
        "cutset": {
            "locked_conditions": selector["locked_conditions"],
            "provenance_minimal_missing_primitive": provenance_basis_packet[
                "provenance_gate"
            ]["minimal_missing_primitive"],
            "basis_minimal_missing_primitive": provenance_basis_packet["basis_gate"][
                "minimal_missing_primitive"
            ],
            "R1_to_R6_closure_vector": closure_vector,
            "R1_to_R6_remaining_open": primitive["what_remains_open"],
        },
        "constructive_numeric_ladder": {
            "nonidentity_rhoE_packet_built": nonidentity["what_closes"][
                "nonidentity_projective_rhoE_candidate_built"
            ],
            "smooth_BN_basis_scaffold_built": smooth_bn["what_closes"][
                "smooth_scalar_basis_functions_phi_m_emitted"
            ],
            "DE_matrix_on_27_mode_BN_built": de_bn["what_closes"][
                "D_E_matrix_on_27_mode_BN_emitted"
            ],
            "dotD_alpha1_matrix_same_basis_built": dotd_bn["what_closes"][
                "dotD_alpha1_matrix_in_same_basis_emitted"
            ],
            "C1_engine_built_zero_canonical_response": c1_bn["what_closes"][
                "canonical_tensor_zero_response_result_proved_finitely"
            ],
            "still_open": {
                "R2_source_promotion_for_rhoE": nonidentity["what_remains_open"][
                    "R2_source_promotion_for_rhoE"
                ],
                "selected_D_E_action_on_basis": smooth_bn["what_remains_open"][
                    "selected_D_E_action_on_basis"
                ],
                "selected_D_E_source_promotion": de_bn["what_remains_open"][
                    "selected_D_E_source_promotion"
                ],
                "selected_source_flags_promoted": dotd_bn["what_remains_open"][
                    "selected_source_flags_promoted"
                ],
                "selected_noninvariant_C1_primitive_or_vertex": c1_bn[
                    "what_remains_open"
                ]["selected_noninvariant_C1_primitive_or_vertex"],
            },
        },
        "frontier_update": {
            "old_next": previous["frontier_update"]["current_next"],
            "current_next": "MTT_Selected_RouteC_Primitive_SourcePromotion_or_BNBasis_Emission_v1",
            "why": (
                "The solve infrastructure, first-run manifest, and downstream "
                "algebra are already tested.  Existing numerical scaffolds "
                "construct nonidentity rhoE, smooth B_N, D_E, dotD, and C1 "
                "engines, but source promotion and quotient-valid selected "
                "basis/primitive emission remain open."
            ),
        },
        "guardrails": {
            "does_not_use_formal_lift_as_proof": True,
            "does_not_claim_selected_source_flags": True,
            "does_not_claim_quotient_valid_BN_basis": True,
            "does_not_claim_honest_replay_without_lifted_flags": True,
            "does_not_claim_nonzero_C1_response": True,
            "does_not_claim_full_SM_or_no_knob_closure": True,
            "does_not_use_observed_or_benchmark_inputs": True,
        },
        "verdict": {
            "what_closes_now": (
                "The Route-C Galerkin branch is reduced from a broad solve "
                "request to a primitive-emission/source-promotion target."
            ),
            "what_remains": (
                "Prove selected source promotion for the nonidentity rhoE/smooth "
                "B_N ladder or emit a quotient-valid B_N basis and selected "
                "Phi_fin payload, then rerun validators without lifted flags."
            ),
            "next_required_artifact": "MTT_Selected_RouteC_Primitive_SourcePromotion_or_BNBasis_Emission_v1",
        },
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "RouteCGalerkinExecutionCutsetAndPrimitiveSearch",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "checks": packet["checks"],
        "frontier_update": packet["frontier_update"],
        "guardrails": packet["guardrails"],
        "verdict": packet["verdict"],
    }


def render_note(cert: dict[str, Any], packet: dict[str, Any]) -> str:
    return f"""# RouteC Galerkin Execution Cutset and Primitive Search v1

## Result

Status: `{cert["status"]}`

The Route-C/Strominger Galerkin solve is no longer a vague missing calculation.
The executable spec, manifest, cutset theorem, R1/R4 fill attempt, and strict
primitive search reduce the branch to primitive emission/source promotion.
Existing scaffolds construct nonidentity `rho_E`, smooth `B_N`, `D_E`,
`dotD_alpha1`, and a C1 engine, but they do not yet promote selected source
flags or a quotient-valid selected `B_N` basis.

## Checks

```json
{json.dumps(packet["checks"], indent=2, sort_keys=True)}
```

## Execution Chain

```json
{json.dumps(packet["execution_chain"], indent=2, sort_keys=True)}
```

## Cutset

```json
{json.dumps(packet["cutset"], indent=2, sort_keys=True)}
```

## Constructive Numeric Ladder

```json
{json.dumps(packet["constructive_numeric_ladder"], indent=2, sort_keys=True)}
```

## Frontier Update

```json
{json.dumps(packet["frontier_update"], indent=2, sort_keys=True)}
```
"""


def main() -> int:
    packet = build_packet()
    cert = build_certificate(packet)
    if "--write" in sys.argv:
        OUTPUT_PACKET.write_text(
            json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        OUTPUT_CERT.write_text(
            json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        OUTPUT_NOTE.write_text(render_note(cert, packet), encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
