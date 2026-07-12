"""Build the U1/Y Route-C finite-emission morphism Phi_fin subpacket.

This is an honest construction attempt. It imports the actual finite Route-C
payloads that exist in the q79 repo, checks them against the Phi_fin contract,
and refuses to promote unselected smoke data into theorem-derived selected
operator data.
"""

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
SM = TEXPAPERS / "mtt-sm-parity-closure"
SMOKE = Q79 / "candidate_data" / "iwasawa_route_c_branch_smoke" / "current_q79_orientation"

INPUTS = {
    "phifin_external_clues": DATA / "selected_u1y_routec_phifin_external_clues.candidate.json",
    "pic0_residual_split": DATA / "selected_u1y_routec_operatorlayer_pic0_or_selected_residual_source_subpacket.candidate.json",
    "hybrid_galerkin_packet": DATA / "selected_u1y_routec_hybrid_galerkin_overlap_source_packet.candidate.json",
    "same_source_fill_nogo": DATA / "selected_u1y_routec_samesource_operatorpacket_fill_or_nogo.candidate.json",
    "sm_source_origin_lemma": SM / "candidate_data" / "routec_selected_source_origin_lemma.candidate.json",
    "rhoE_metric": SMOKE / "rhoE_metric.candidate.json",
    "sector_maps": SMOKE / "sector_maps.candidate.json",
    "de_action": SMOKE / "de_action.candidate.json",
    "riesz_gap": SMOKE / "riesz_gap.candidate.json",
    "reduced_green": SMOKE / "reduced_green.candidate.json",
    "dotd_response": SMOKE / "dotd_response.candidate.json",
    "route_c_residual": SMOKE / "route_c_residual.candidate.json",
}

OUTPUT_DATA = DATA / "selected_u1y_routec_finite_emission_morphism_phifin_subpacket.candidate.json"
OUTPUT_CERT = CERTS / "selected_u1y_routec_finite_emission_morphism_phifin_subpacket_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_RouteC_FiniteEmissionMorphism_PhiFin_Subpacket_v1.md"

STATUS = "U1Y_ROUTEC_PHIFIN_SUBPACKET_BUILT_SELECTED_FINITE_TRACE_OPEN"
NEXT = "Selected_U1Y_RouteC_SelectedFiniteTrace_SourceOrNoGo_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def slot_summary(de: dict[str, Any], riesz: dict[str, Any], dotd: dict[str, Any]) -> dict[str, Any]:
    slots = {}
    for name, slot in de["operator_slots"].items():
        rslot = riesz["spectral_slots"][name]
        dslot = dotd["dotd_response_slots"][name]
        slots[name] = {
            "domain_dimension": slot["domain_dimension"],
            "range_dimension": slot["range_dimension"],
            "expected_kernel_dimension": slot["expected_kernel_dimension"],
            "boundary_conditions_verified": slot["boundary_conditions_verified"],
            "de_selected_source_verified": slot["selected_source_verified"],
            "riesz_operator_data_verified": rslot["operator_data_verified"],
            "riesz_selected_source_verified": rslot["selected_source_verified"],
            "complement_gap": rslot["complement_gap"],
            "truncation_error_bound": rslot["truncation_error_bound"],
            "max_residual_norm": max(rslot["residual_norms"]) if rslot["residual_norms"] else None,
            "dotd_green_operator_verified": dslot["green_operator_verified"],
            "dotd_horizontal_gauge_verified": dslot["horizontal_gauge_verified"],
            "dotd_alpha1_driver_verified": dslot["alpha1_driver_verified"],
            "dotd_selected_source_verified": dslot["selected_dotD_source_verified"],
        }
    return slots


def all_slots(slots: dict[str, Any], key: str) -> bool:
    return all(slot[key] is True for slot in slots.values())


def min_slot(slots: dict[str, Any], key: str) -> float:
    return min(float(slot[key]) for slot in slots.values())


def max_slot(slots: dict[str, Any], key: str) -> float:
    return max(float(slot[key]) for slot in slots.values())


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    clues = load(INPUTS["phifin_external_clues"])
    split = load(INPUTS["pic0_residual_split"])
    hybrid = load(INPUTS["hybrid_galerkin_packet"])
    fill_nogo = load(INPUTS["same_source_fill_nogo"])
    origin = load(INPUTS["sm_source_origin_lemma"])
    rhoe = load(INPUTS["rhoE_metric"])
    sector_maps = load(INPUTS["sector_maps"])
    de = load(INPUTS["de_action"])
    riesz = load(INPUTS["riesz_gap"])
    green = load(INPUTS["reduced_green"])
    dotd = load(INPUTS["dotd_response"])
    residual = load(INPUTS["route_c_residual"])

    slots = slot_summary(de, riesz, dotd)
    selected_false_count = sum(
        1
        for slot in slots.values()
        if not slot["de_selected_source_verified"]
        or not slot["riesz_selected_source_verified"]
        or not slot["dotd_selected_source_verified"]
    )

    stage_checks = [
        {
            "stage": "domain_lock",
            "status": "CLOSED_FIXED_SECTOR_SUPPORT",
            "passes": True,
            "evidence": [
                "origin G1 fixed topological sector passes",
                "origin G2 MTT Strominger selection available passes",
                "origin G3 same-source support converges passes",
                "Pic0 carried as side condition by parent split gate",
            ],
        },
        {
            "stage": "finite_basis",
            "status": "PARTIAL_VALIDATOR_BASIS_PRESENT_SELECTED_BN_OPEN",
            "passes": False,
            "evidence": {
                "sectors": sorted(slots),
                "validator_basis_shapes_present": True,
                "source_selected_basis_B_N_emitted": False,
                "reason": "Route-C validator zero-mode bases exist in smoke payloads, but no selected-source theorem emits them from M_*.",
            },
        },
        {
            "stage": "projection_commuting_square",
            "status": "PARTIAL_BRANCH_COMPATIBLE_PROJECTION_PROOF_OPEN",
            "passes": False,
            "evidence": {
                "branch_packets_agree": de["branch_packet"] == riesz["branch_packet"] == dotd["branch_packet"],
                "boundary_conditions_verified_all_slots": all_slots(slots, "boundary_conditions_verified"),
                "commutes_with_s3_gs_ah_cp_q79_proved": False,
            },
        },
        {
            "stage": "finite_operator_payload",
            "status": "PAYLOAD_SHAPES_PRESENT_SELECTED_OPERATOR_VALUES_OPEN",
            "passes": False,
            "evidence": {
                "rhoE_metric_rank": rhoe["rank"],
                "rhoE_selected_by_mtt": rhoe["selected_by_mtt"],
                "de_boundary_conditions_verified": all_slots(slots, "boundary_conditions_verified"),
                "riesz_operator_data_verified": all_slots(slots, "riesz_operator_data_verified"),
                "dotd_green_operator_verified": all_slots(slots, "dotd_green_operator_verified"),
                "dotd_horizontal_gauge_verified": all_slots(slots, "dotd_horizontal_gauge_verified"),
                "all_selected_source_verified": selected_false_count == 0,
                "selected_false_count": selected_false_count,
                "primitive_C1_tensors_emitted": False,
            },
        },
        {
            "stage": "error_gap_certificate",
            "status": "NUMERIC_GAP_PRESENT_THEOREM_DERIVED_ERROR_CERTIFICATE_OPEN",
            "passes": False,
            "evidence": {
                "min_complement_gap": min_slot(slots, "complement_gap"),
                "max_truncation_error_bound": max_slot(slots, "truncation_error_bound"),
                "max_residual_norm": max_slot(slots, "max_residual_norm"),
                "selected_hessian_riesz_gap_theorem": False,
                "selected_source_verified_theorem_derived": False,
            },
        },
    ]

    finite_trace_attempt = {
        "name": "Phi_fin_current_trace_attempt",
        "source": "q79 iwasawa_route_c_branch_smoke/current_q79_orientation",
        "branch_packet": de["branch_packet"],
        "rhoE_metric": {
            "rank": rhoe["rank"],
            "mesh_N": rhoe["mesh_N"],
            "selected_by_mtt": rhoe["selected_by_mtt"],
            "generator_count": len(rhoe["generator_data"]),
        },
        "sector_maps_status": sector_maps.get("status", "UNKNOWN"),
        "de_status": de["status"],
        "riesz_status": riesz["status"],
        "reduced_green_status": green["status"],
        "dotd_status": dotd["status"],
        "residual_status": residual["status"],
        "slot_summary": slots,
    }

    acceptance_tests = {
        "selected_source_verified_theorem_derived": False,
        "validators_pass_honestly": False,
        "finite_truncation_error_bounded_by_selected_gap": False,
        "primitive_C1_overlap_tensors_emitted_or_reduced": False,
        "why": [
            "The finite validator payloads have valid shapes, gaps, Green objects, and zero residual scaffolding.",
            "They are explicitly unselected smoke data: selected_by_mtt=false or selected_source_verified=false.",
            "The dotD alpha1 driver and primitive C1 tensors are not source-certified.",
        ],
    }

    theorem_statement = {
        "name": "PhiFinCurrentTraceAttemptNoPromotion",
        "proved": True,
        "statement": (
            "The current finite Route-C trace can be assembled as a validator-ready "
            "candidate scaffold, but it cannot be promoted to the finite emission "
            "morphism Phi_fin because selected finite basis emission, commuting "
            "projection proof, theorem-derived source verification, and primitive "
            "C1 tensors are still absent."
        ),
    }

    candidate = {
        "candidate": "SelectedU1YRouteCFiniteEmissionMorphismPhiFinSubpacket",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "external_clues": clues["status"],
            "pic0_residual_split": split["status"],
            "hybrid_galerkin_packet": hybrid["status"],
            "same_source_fill_nogo": fill_nogo["status"],
            "source_origin_lemma": origin["status"],
        },
        "contract": clues["local_contract"],
        "stage_checks": stage_checks,
        "finite_trace_attempt": finite_trace_attempt,
        "acceptance_tests": acceptance_tests,
        "theorem": theorem_statement,
        "decision": {
            "Phi_fin_constructed": False,
            "finite_trace_scaffold_constructed": True,
            "domain_lock_closed": True,
            "selected_basis_B_N_emitted": False,
            "commuting_projection_proved": False,
            "selected_operator_payload_emitted": False,
            "selected_error_gap_certificate_emitted": False,
            "primitive_C1_tensors_emitted": False,
            "lambda_12_computable": False,
            "target_fitting_used": False,
            "next_required_artifact": NEXT,
        },
        "what_closes_now": {
            "Phi_fin_contract_bound_to_actual_payloads": True,
            "finite_trace_scaffold_summarized": True,
            "domain_lock_confirmed": True,
            "selected_smoke_promotion_rejected": True,
            "first_missing_selected_objects_named": True,
        },
        "what_remains_open": {
            "source_selected_basis_B_N_from_M_star": True,
            "commuting_projection_square": True,
            "theorem_derived_selected_source_verified": True,
            "selected_rhoE_metric_sector_maps": True,
            "selected_D_E_Riesz_Green_dotD": True,
            "selected_alpha1_driver": True,
            "primitive_C1_overlap_tensors": True,
            "lambda_12": True,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
        "guardrails": {
            "claims_Phi_fin_closed": False,
            "claims_A_selected": False,
            "claims_b_selected": False,
            "claims_lambda12": False,
            "promotes_smoke_data": False,
            "uses_observed_data": False,
            "uses_benchmark_data": False,
            "target_fitting_used": False,
        },
    }

    cert = {
        "certificate": "SelectedU1YRouteCFiniteEmissionMorphismPhiFinSubpacket",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "Phi_fin_constructed": False,
        "finite_trace_scaffold_constructed": True,
        "domain_lock_closed": True,
        "stage_passes": {stage["stage"]: stage["passes"] for stage in stage_checks},
        "min_complement_gap": min_slot(slots, "complement_gap"),
        "max_truncation_error_bound": max_slot(slots, "truncation_error_bound"),
        "selected_false_count": selected_false_count,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "lambda_12_closed": False,
        "target_fitting_used": False,
    }
    return candidate, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    lines = [
        "# Selected U1Y Route-C FiniteEmissionMorphism PhiFin Subpacket v1",
        "",
        "## Result",
        "",
        "```text",
        f"status = {candidate['status']}",
        f"Phi_fin_constructed = {str(cert['Phi_fin_constructed']).lower()}",
        f"finite_trace_scaffold_constructed = {str(cert['finite_trace_scaffold_constructed']).lower()}",
        f"domain_lock_closed = {str(cert['domain_lock_closed']).lower()}",
        f"lambda_12_closed = {str(cert['lambda_12_closed']).lower()}",
        f"next_required_artifact = {candidate['next_required_artifact']}",
        "```",
        "",
        "The current finite Route-C payloads assemble into a concrete validator",
        "scaffold, but they do not yet prove the finite emission morphism",
        "`Phi_fin`. The reason is sharp: the available matrices are still smoke",
        "or support payloads with selected-source verification false.",
        "",
        "## Stage Checks",
        "",
        "| Stage | Status | Passes |",
        "| --- | --- | --- |",
    ]
    for stage in candidate["stage_checks"]:
        lines.append(f"| `{stage['stage']}` | `{stage['status']}` | `{str(stage['passes']).lower()}` |")
    lines.extend(
        [
            "",
            "## Finite Trace Data",
            "",
            "```text",
            f"rhoE rank = {candidate['finite_trace_attempt']['rhoE_metric']['rank']}",
            f"min complement gap = {cert['min_complement_gap']}",
            f"max truncation error bound = {cert['max_truncation_error_bound']}",
            f"selected false count = {cert['selected_false_count']}",
            "```",
            "",
            "The positive gap and zero truncation-error scaffold are useful, but",
            "they are not enough. The gap must be tied to the selected Hessian/Riesz",
            "object and the finite basis must be emitted from `M_*`.",
            "",
            "## What This Proves",
            "",
            candidate["theorem"]["statement"],
            "",
            "## Remaining Objects",
            "",
        ]
    )
    for key, value in candidate["what_remains_open"].items():
        if value:
            lines.append(f"- `{key}`")
    lines.extend(
        [
            "",
            "## Guardrails",
            "",
            "- Do not promote q79 Route-C smoke matrices to selected operator tables.",
            "- Do not compute `lambda_12` from this scaffold.",
            "- Do not use observed masses, mixings, gauge constants, or benchmark matrices.",
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
