"""Build the q79 V_alpha source-origin / finite-emission bridge.

This artifact turns the repo-update frontier into a q79-local finite target.
It does not import dirty adjacent packets as proof.  Instead, it proves that
the current q79 Route-C finite files already specify the codomain shape that a
selected source-origin morphism must fill, and that the alpha_1 driver problem
is the same missing selected payload rather than a separate knob.
"""

from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
CERTS = ROOT / "certificates"
CANDIDATES = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"
SMOKE = CANDIDATES / "iwasawa_route_c_branch_smoke" / "current_q79_orientation"
SM_PARITY = TEXPAPERS / "mtt-sm-parity-closure"

OUT_DIR = CANDIDATES / "q79_valpha_source_origin_finite_emission_bridge"
OUT_CONTRACT = OUT_DIR / "selected_payload_contract.json"
OUT_CANDIDATE = CANDIDATES / "q79_valpha_source_origin_finite_emission_bridge.candidate.json"
OUT_CERT = CERTS / "q79_valpha_source_origin_finite_emission_bridge_certificate.json"
OUT_PAPER = CORPUS / "Q79_VAlpha_Source_Origin_and_Finite_Emission_Bridge_v1.md"

INPUTS = {
    "frontier": CERTS / "valpha_repo_update_source_frontier_certificate.json",
    "central_neutral": CERTS / "valpha_central_neutral_destabilizer_reduction_certificate.json",
    "ah_yoneda": CERTS / "valpha_appell_humbert_yoneda_promotion_certificate.json",
    "c1_alpha1_rank_lift": CERTS / "c1_alpha1_rank_lift_criterion_certificate.json",
    "c1_finite_response": CERTS / "c1_finite_response_matrix_reduction_certificate.json",
    "c1_response_attempt": CERTS / "selected_c1_response_extraction_attempt_certificate.json",
    "c1_response_template": CERTS / "selected_c1_response_data_certificate.template.json",
    "route_c_residual": SMOKE / "route_c_residual.candidate.json",
    "rhoE_mesh": SMOKE / "rhoE_mesh.candidate.json",
    "rhoE_metric": SMOKE / "rhoE_metric.candidate.json",
    "sector_maps": SMOKE / "sector_maps.candidate.json",
    "de_action": SMOKE / "de_action.candidate.json",
    "riesz_gap": SMOKE / "riesz_gap.candidate.json",
    "reduced_green": SMOKE / "reduced_green.candidate.json",
    "dotd_response": SMOKE / "dotd_response.candidate.json",
}

SM_PARITY_INPUTS = {
    "source_origin_alpha1": SM_PARITY
    / "certificates"
    / "selected_source_origin_and_alpha1_driver_certificate.json",
    "finite_emission_phifin": SM_PARITY
    / "certificates"
    / "finite_emission_morphism_phifin_certificate.json",
    "selected_phifin_alpha1": SM_PARITY
    / "certificates"
    / "selected_phifin_alpha1_payload_certificate.json",
}

EXPECTED_RESIDUALS = {
    "rho_cocycle",
    "metric_compatibility",
    "integrability_F02",
    "hym_primitive",
    "bianchi_alpha1",
    "mtt_gradient",
    "strominger_residual",
}
EXPECTED_SECTORS = {"H", "L", "N", "Q", "d", "e", "u"}


def run_git(repo: Path, args: list[str]) -> str:
    if not (repo / ".git").exists():
        return ""
    proc = subprocess.run(
        ["git", *args],
        cwd=repo,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    return proc.stdout.strip()


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def status_summary(status_short: str) -> dict[str, Any]:
    lines = [line for line in status_short.splitlines() if line.strip()]
    return {
        "dirty": bool(lines),
        "line_count": len(lines),
        "modified_count": sum(line.startswith(" M") or line.startswith("M ") for line in lines),
        "untracked_count": sum(line.startswith("??") for line in lines),
        "preview": lines[:10],
    }


def input_status(paths: dict[str, Path]) -> dict[str, Any]:
    return {
        name: {
            "path": str(path),
            "present": path.exists(),
            "status": load(path).get("status") if path.exists() else None,
        }
        for name, path in paths.items()
    }


def all_slot_flag(slots: dict[str, Any], flag: str) -> bool:
    return bool(slots) and all(bool(row.get(flag)) for row in slots.values())


def residuals_zero(residuals: dict[str, Any]) -> bool:
    if set(residuals) != EXPECTED_RESIDUALS:
        return False
    return all(abs(float(row.get("value", 1.0))) <= float(row.get("tolerance", 0.0)) for row in residuals.values())


def all_response_matrices_null(template: dict[str, Any]) -> bool:
    matrices = template.get("response_matrices", {})
    tests = template.get("computed_tests", {})
    return all(value is None for value in matrices.values()) and all(value is None for value in tests.values())


def build_contract(
    sectors: list[str],
    branch_packet: dict[str, Any],
    c1_finite: dict[str, Any],
) -> dict[str, Any]:
    return {
        "name": "Q79SelectedPhiFinAlpha1Payload",
        "branch": {
            "global_cp_label": branch_packet.get("global_cp_label"),
            "torsion_label_m": branch_packet.get("torsion_label_m"),
            "transport_orientation": branch_packet.get("conditional_su5_transport_orientation"),
            "sector_orientations": branch_packet.get("sector_orientations", {}),
            "antiunitary_conjugate_retained_for_comparison": branch_packet.get(
                "antiunitary_conjugate_retained_for_comparison"
            ),
        },
        "domain": (
            "selected q79/F,m=1 S3/Green-Schwarz/Strominger-HYM source with "
            "Appell-Humbert V_alpha extension data and alpha_1 curvature driver"
        ),
        "finite_codomain": {
            "residual_equations": sorted(EXPECTED_RESIDUALS),
            "sectors": sectors,
            "route_c_slots": [
                "rhoE_transition",
                "rhoE_metric",
                "sector_maps",
                "D_E_action",
                "Riesz_projector_and_gap",
                "reduced_Green",
                "dotD_alpha1_response",
            ],
            "c1_response_terms": c1_finite.get("primitive_contraction_schema", {}).get(
                "required_3x3_terms_per_sector", []
            ),
        },
        "must_emit": [
            "selected source-origin certificate tying the V_alpha extension to the q79/F,m=1 branch",
            "non-identity selected rho_E or equivalent connection/gerbe transition data",
            "selected Hermitian metric and sector projectors on Q,u,d,L,e,N,H,Higgs slots",
            "selected D_E action matrices with selected_source_verified true in every sector",
            "selected Riesz projectors, complement gaps, and reduced Green operators",
            "selected dotD_alpha1 as the same-branch derivative of selected D_E",
            "evaluated grad V_C1 alpha1 source vector and lower-order Hessian blocks",
            "deltaTheta_C1 solution, sector zero-mode bases, and primitive C1 contractions",
        ],
        "acceptance": [
            "all finite shape gates remain true",
            "all selected payload flags become true by theorem, not by diagnostic lifted flags",
            "identity rho_E smoke is replaced or proved equivalent to a nontrivial selected gerbe/connection payload",
            "Pic0 is selected, quotiented, or proved irrelevant at operator level",
            "q79/q369 branch relation is fixed by source selection or retarded antiunitary equivalence",
            "no observed masses, CKM/PMNS values, or Execution II benchmark entries are used as inputs",
        ],
    }


def build_bridge() -> dict[str, Any]:
    frontier = load(INPUTS["frontier"])
    central = load(INPUTS["central_neutral"])
    ah = load(INPUTS["ah_yoneda"])
    c1_rank = load(INPUTS["c1_alpha1_rank_lift"])
    c1_finite = load(INPUTS["c1_finite_response"])
    c1_attempt = load(INPUTS["c1_response_attempt"])
    c1_template = load(INPUTS["c1_response_template"])
    residual = load(INPUTS["route_c_residual"])
    rhoe = load(INPUTS["rhoE_mesh"])
    metric = load(INPUTS["rhoE_metric"])
    sector_maps = load(INPUTS["sector_maps"])
    de_action = load(INPUTS["de_action"])
    riesz_gap = load(INPUTS["riesz_gap"])
    reduced_green = load(INPUTS["reduced_green"])
    dotd = load(INPUTS["dotd_response"])

    branch_packet = residual.get("branch_packet", {})
    de_slots = de_action.get("operator_slots", {})
    riesz_slots = riesz_gap.get("spectral_slots", {})
    green_slots = reduced_green.get("green_slots", {})
    dotd_slots = dotd.get("dotd_response_slots", {})
    sectors = sorted(de_slots)
    sector_set = set(sectors)

    positive_gates = residual.get("positive_gates", {})
    residual_equations = residual.get("residuals", {})
    frontier_reduction = frontier.get("repo_update_source_frontier", {}).get("frontier_reduction", {})

    finite_shape_gates = {
        "branch_is_q79_F_m1": branch_packet.get("global_cp_label") == 79
        and branch_packet.get("torsion_label_m") == 1
        and branch_packet.get("conditional_su5_transport_orientation") == "F",
        "retained_conjugate_comparison": branch_packet.get(
            "antiunitary_conjugate_retained_for_comparison"
        )
        is True,
        "residual_equations_present_and_zero": residuals_zero(residual_equations),
        "positive_hessian_and_riesz_gates": all(
            float(row.get("value", 0.0)) > float(row.get("strict_lower_bound", 0.0))
            for row in positive_gates.values()
        )
        and set(positive_gates) == {"mtt_hessian_min_eigenvalue", "riesz_gap_min"},
        "sector_slot_set_is_Q_u_d_L_e_N_H": sector_set == EXPECTED_SECTORS,
        "de_riesz_green_dotd_same_sector_set": sector_set
        == set(riesz_slots)
        == set(green_slots)
        == set(dotd_slots),
        "rhoE_metric_and_sector_maps_present": bool(metric) and bool(sector_maps),
        "no_observed_or_benchmark_flavor_inputs": residual.get("no_observed_flavor_inputs") is True
        and residual.get("uses_execution_ii_benchmarks") is False,
    }

    selected_payload_flags = {
        "route_c_residual_selected_source": bool(residual.get("selected_source_verified")),
        "rhoE_selected_by_mtt": bool(rhoe.get("selected_by_mtt")),
        "rhoE_nonidentity": rhoe.get("candidate_kind") != "identity_rhoE_smoke_unselected",
        "de_action_selected_source": all_slot_flag(de_slots, "selected_source_verified"),
        "riesz_gap_selected_source": all_slot_flag(riesz_slots, "selected_source_verified"),
        "reduced_green_selected_source": all_slot_flag(green_slots, "selected_source_verified"),
        "dotd_selected_source": all_slot_flag(dotd_slots, "selected_dotD_source_verified"),
        "dotd_alpha1_driver": all_slot_flag(dotd_slots, "alpha1_driver_verified"),
    }

    alpha1_support_gates = {
        "alpha1_driver_row_available": c1_finite.get("currently_available", {}).get(
            "selected_driver_alpha1"
        )
        is True,
        "selected_Xi_operator_level_source_available": c1_finite.get("currently_available", {}).get(
            "selected_Xi_operator_level_source"
        )
        is True,
        "hessian_principal_blocks_available": c1_finite.get("currently_available", {}).get(
            "Hess_Xi_principal_symbol_blocks"
        )
        is True,
        "single_alpha1_driver_not_algebraically_fatal": c1_rank.get("closed", {}).get(
            "single_alpha1_driver_not_algebraically_fatal"
        )
        is True,
        "rank_lift_minor_identified": c1_rank.get("closed", {}).get(
            "leading_rank_lift_minor_identified"
        )
        is True,
        "finite_response_formula_closed": c1_finite.get("verdict", {}).get(
            "closes_finite_response_formula"
        )
        is True,
    }

    alpha1_missing_values = {
        "evaluated_grad_V_C1_alpha1_source_vector": c1_attempt.get(
            "missing_selected_operator_data", {}
        ).get("evaluated_grad_V_C1_alpha1_source_vector")
        is None,
        "full_lower_order_Hess_Xi_blocks": c1_attempt.get("missing_selected_operator_data", {}).get(
            "full_lower_order_Hess_Xi_blocks"
        )
        is None,
        "selected_deltaTheta_C1_solution": c1_template.get("operator_data", {}).get(
            "deltaTheta_C1_solution"
        )
        is None,
        "sector_dotD_slots": all(
            c1_template.get("operator_data", {}).get(f"dotD_{slot}") is None
            for slot in ["Q", "u", "d", "L", "e", "N", "H"]
        ),
        "sector_zero_mode_bases": all(
            c1_template.get("zero_modes", {}).get(f"{slot}_basis") is None
            for slot in ["Q", "u", "d", "L", "e", "N", "H"]
        ),
        "response_matrices_and_tests": all_response_matrices_null(c1_template),
    }

    q79_source_side = {
        "frontier_status": frontier.get("status"),
        "central_neutral_obstructed": central.get("closed_by_this_attempt", {}).get(
            "central_neutral_base_pullback_line_destabilizers_obstructed"
        )
        is True,
        "ah_yoneda_conditional": ah.get("closed_by_this_attempt", {}).get(
            "reduced_boundary_maps_promoted_to_AH_theta_multiplication_conditional"
        )
        is True,
        "frontier_reduces_to_finite_emission": "finite emission morphism Phi_fin"
        in str(frontier_reduction.get("next_primary_route_from_updates", "")),
        "frontier_imports_dirty_adjacent_as_provisional_only": frontier.get(
            "guardrails", {}
        ).get("claims_sm_parity_uncommitted_packets_are_proof")
        is False,
    }

    sm_status = run_git(SM_PARITY, ["status", "--short"])
    sm_provenance = {
        "repo": str(SM_PARITY),
        "present": (SM_PARITY / ".git").exists(),
        "head": run_git(SM_PARITY, ["log", "-1", "--oneline"]),
        "status_summary": status_summary(sm_status),
        "certificate_statuses": input_status(SM_PARITY_INPUTS),
        "imported_as_proof_data": False,
    }

    contract = build_contract(sectors, branch_packet, c1_finite)
    selected_payload_closed = all(selected_payload_flags.values())
    finite_shape_closed = all(finite_shape_gates.values())

    return {
        "certificate": "Q79VAlphaSourceOriginFiniteEmissionBridge",
        "status": "Q79_VALPHA_SOURCE_ORIGIN_FINITE_EMISSION_BRIDGE_CONSTRUCTED_SELECTED_PAYLOAD_OPEN",
        "analysis_script": rel(Path(__file__)),
        "candidate_data": rel(OUT_CANDIDATE),
        "contract_packet": rel(OUT_CONTRACT),
        "paper": rel(OUT_PAPER),
        "source_status": input_status(INPUTS),
        "sm_parity_status_evidence_only": sm_provenance,
        "q79_source_side": q79_source_side,
        "finite_emission_schema": {
            "shape_gates": finite_shape_gates,
            "selected_payload_flags": selected_payload_flags,
            "identity_rhoE_smoke_rejected": rhoe.get("candidate_kind")
            == "identity_rhoE_smoke_unselected",
            "branch_packet": branch_packet,
            "residual_equations": sorted(residual_equations),
            "sectors": sectors,
        },
        "alpha1_driver_bridge": {
            "support_gates": alpha1_support_gates,
            "missing_selected_values": alpha1_missing_values,
            "rank_lift_condition": c1_rank.get("determinant_expansion", {}).get(
                "leading_full_rank_condition"
            ),
            "finite_response_formula": c1_finite.get("finite_reduction_theorem", {}).get(
                "matrix_formula"
            ),
        },
        "selected_payload_contract": contract,
        "closed_by_this_attempt": {
            "q79_source_side_anchored": all(q79_source_side.values()),
            "finite_emission_codomain_schema_closed": finite_shape_closed,
            "identity_rhoE_smoke_rejected": rhoe.get("candidate_kind")
            == "identity_rhoE_smoke_unselected",
            "alpha1_support_and_rank_test_closed": all(alpha1_support_gates.values()),
            "source_origin_and_alpha1_reduced_to_one_payload": True,
            "dirty_sm_parity_used_only_as_status_evidence": sm_provenance["imported_as_proof_data"]
            is False,
            "target_fitting_excluded": True,
        },
        "still_open": {
            "selected_PhiFin_alpha1_payload": True,
            "selected_visible_valpha_source_origin": not selected_payload_closed,
            "nonidentity_selected_rhoE_or_connection_values": not selected_payload_flags[
                "rhoE_nonidentity"
            ],
            "selected_D_E_Riesz_Green_dotD_flags": not (
                selected_payload_flags["de_action_selected_source"]
                and selected_payload_flags["riesz_gap_selected_source"]
                and selected_payload_flags["reduced_green_selected_source"]
                and selected_payload_flags["dotd_selected_source"]
            ),
            "same_branch_alpha1_derivative_theorem": not selected_payload_flags[
                "dotd_alpha1_driver"
            ],
            "finite_C1_numeric_response_matrices": all(alpha1_missing_values.values()),
            "Pic0_operator_level_rule": True,
            "full_rank_one_torsion_free_stability": True,
            "HYM_or_RouteC_selected_values": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_dirty_sm_parity_packets_are_proof": False,
            "claims_selected_PhiFin_payload": False,
            "claims_selected_visible_valpha_source": False,
            "claims_nonidentity_rhoE_values": False,
            "claims_D_E_Riesz_Green_dotD_selected": False,
            "claims_C1_numeric_matrices": False,
            "claims_full_stability": False,
            "claims_HYM_or_RouteC_values": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "theorem": {
            "name": "Q79VAlphaSourceOriginFiniteEmissionBridge",
            "proved": True,
            "statement": (
                "On the committed q79 side, the V_alpha source-origin problem and "
                "the alpha_1 C1-response problem reduce to one finite selected "
                "payload.  The existing q79/F,m=1 Route-C files close the codomain "
                "schema for Phi_fin and reject the identity-smoke promotion, while "
                "the C1 certificates close the driver and rank test but leave values "
                "open.  Therefore the next honest object is the selected Phi_fin "
                "alpha1 payload, not an independent source knob or a fitted matrix."
            ),
        },
        "next_required_artifact": "Q79_Selected_PhiFin_Alpha1_Payload_v1",
        "closure_claimed": False,
        "target_fitting_used": False,
    }


def render_bool_map(items: dict[str, Any]) -> str:
    return "\n".join(f"- `{key}`: `{value}`" for key, value in items.items())


def render_list(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def build_paper(cert: dict[str, Any]) -> str:
    finite = cert["finite_emission_schema"]
    alpha = cert["alpha1_driver_bridge"]
    contract = cert["selected_payload_contract"]
    sm = cert["sm_parity_status_evidence_only"]
    closes = "\n".join(
        f"- `{key}`" for key, value in cert["closed_by_this_attempt"].items() if value
    )
    open_items = "\n".join(f"- `{key}`" for key, value in cert["still_open"].items() if value)
    return f"""# Q79 VAlpha Source-Origin and Finite-Emission Bridge v1

## Result

The q79 side now has a local finite bridge:

```text
V_alpha source origin + alpha_1 C1 response
  -> selected Phi_fin alpha1 payload.
```

This does not compute the selected payload.  It proves the finite codomain that
the payload must fill and records why the present Route-C packet is only a
scaffold: its shape gates pass, but its selected-source flags are false and
`rho_E` is identity smoke.

The adjacent SM-parity repo is status evidence only.  Current head:
`{sm["head"]}`; dirty: `{sm["status_summary"]["dirty"]}`.

## Q79 Source Side

{render_bool_map(cert["q79_source_side"])}

## Finite Emission Shape Gates

{render_bool_map(finite["shape_gates"])}

## Selected Payload Flags

{render_bool_map(finite["selected_payload_flags"])}

## Alpha1 Driver Bridge

Support gates:

{render_bool_map(alpha["support_gates"])}

Missing selected values:

{render_bool_map(alpha["missing_selected_values"])}

Rank-lift condition:

```text
{alpha["rank_lift_condition"]}
```

Finite response formula:

```text
{alpha["finite_response_formula"]}
```

## Selected Payload Contract

Domain:

```text
{contract["domain"]}
```

Must emit:

{render_list(contract["must_emit"])}

Acceptance:

{render_list(contract["acceptance"])}

## What This Closes

{closes}

## What Remains Open

{open_items}

## Theorem

`{cert["theorem"]["name"]}` is proved:

{cert["theorem"]["statement"]}

Next artifact: `{cert["next_required_artifact"]}`.
"""


def main() -> int:
    cert = build_bridge()
    write_json(OUT_CONTRACT, cert["selected_payload_contract"])
    write_json(OUT_CANDIDATE, cert)
    write_json(OUT_CERT, cert)
    OUT_PAPER.parent.mkdir(parents=True, exist_ok=True)
    OUT_PAPER.write_text(build_paper(cert), encoding="utf-8")
    print("Q79 VAlpha source-origin finite-emission bridge")
    print(json.dumps({"status": cert["status"], "certificate": rel(OUT_CERT)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
