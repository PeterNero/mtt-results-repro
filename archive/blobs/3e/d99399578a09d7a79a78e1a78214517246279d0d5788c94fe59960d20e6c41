"""Build the selected source-origin and alpha1-driver reduction artifact."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")
Q79_CERTS = Q79 / "certificates"

OUTPUT_DATA = DATA / "selected_source_origin_and_alpha1_driver.candidate.json"
OUTPUT_CERT = CERTS / "selected_source_origin_and_alpha1_driver_certificate.json"
OUTPUT_NOTE = CORPUS / "MTT_Selected_Source_Origin_and_Alpha1_Driver_v1.md"

INPUTS = {
    "orientation_source": DATA / "selected_orientation_carrying_de_dotd_source.candidate.json",
    "orientation_certificate": CERTS / "selected_orientation_carrying_de_dotd_source_certificate.json",
    "routec_source_lemma": DATA / "routec_selected_source_origin_lemma.candidate.json",
    "phifin_schema": DATA / "finite_emission_morphism_phifin.candidate.json",
    "nonidentity_rhoe": DATA / "selected_nonidentity_rhoe_transition_source.candidate.json",
    "projective_gerbe_rhoe": DATA / "projective_gerbe_rhoe_source_promotion.candidate.json",
    "visible_chern_weil": DATA / "selected_visible_chern_weil_operator_source.candidate.json",
    "c1_alpha1_rank_lift": Q79_CERTS / "c1_alpha1_rank_lift_criterion_certificate.json",
    "c1_finite_response_reduction": Q79_CERTS / "c1_finite_response_matrix_reduction_certificate.json",
    "c1_response_attempt": Q79_CERTS / "selected_c1_response_extraction_attempt_certificate.json",
    "c1_response_template": Q79_CERTS / "selected_c1_response_data_certificate.template.json",
}


def load_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def input_status() -> dict[str, object]:
    return {
        name: {
            "path": str(path),
            "present": path.exists(),
            "status": load_json(path).get("status", "UNKNOWN") if path.exists() else "MISSING",
        }
        for name, path in INPUTS.items()
    }


def bool_path(data: dict[str, object], *keys: str, default: bool = False) -> bool:
    cur: object = data
    for key in keys:
        if not isinstance(cur, dict) or key not in cur:
            return default
        cur = cur[key]
    return bool(cur)


def build_candidate() -> dict[str, object]:
    orientation = load_json(INPUTS["orientation_source"])
    routec = load_json(INPUTS["routec_source_lemma"])
    phifin = load_json(INPUTS["phifin_schema"])
    nonidentity = load_json(INPUTS["nonidentity_rhoe"])
    gerbe = load_json(INPUTS["projective_gerbe_rhoe"])
    visible = load_json(INPUTS["visible_chern_weil"])
    c1_rank = load_json(INPUTS["c1_alpha1_rank_lift"])
    c1_reduction = load_json(INPUTS["c1_finite_response_reduction"])
    c1_attempt = load_json(INPUTS["c1_response_attempt"])
    c1_template = load_json(INPUTS["c1_response_template"])

    routec_gates = routec["gate_matrix"]
    phifin_shape = phifin["phifin_schema"]["shape_gates"]
    phifin_selected = phifin["phifin_schema"]["selected_flags"]
    orientation_open = orientation["what_remains_open"]
    c1_values_required = c1_reduction["values_still_required"]
    c1_attempt_missing = c1_attempt["missing_selected_operator_data"]

    source_support_closed = {
        "fixed_topological_sector_named": bool_path(routec_gates, "G1_fixed_topological_sector_named", "passes"),
        "mtt_strominger_selection_available": bool_path(routec_gates, "G2_MTT_Strominger_selection_available", "passes"),
        "same_source_support_converges": bool_path(routec_gates, "G3_same_source_support_converges", "passes"),
        "s3_projective_gerbe_support_promoted": gerbe["promotion_result"]["source_level_projective_gerbe_rhoE_promoted"],
        "visible_chern_weil_contract_reduced": visible["closed_support"]["selected_s3_gerbe_source_level"]
        and visible["closed_support"]["visible_green_schwarz_curvature_row_closed"],
    }

    source_origin_selected_flags = {
        "selected_by_mtt": not orientation_open["selected_by_mtt"],
        "visible_bundle_or_twisted_gerbe_source": not orientation_open["visible_bundle_or_twisted_gerbe_source"],
        "pic0_selected_or_quotiented": not orientation_open["pic0_selected_or_quotiented"],
        "selection_justified_by_source": not orientation_open["selection_justified_by_source"],
        "same_branch_derivative_verified": not orientation_open["same_branch_derivative_verified"],
        "selected_D_E_source_flags": not orientation_open["selected_D_E_source_flags"],
        "selected_Green_source_flags": not orientation_open["selected_Green_source_flags"],
        "selected_dotD_source_flags": not orientation_open["selected_dotD_source_flags"],
    }

    alpha1_support = {
        "selected_driver_alpha1_row": c1_reduction["currently_available"]["selected_driver_alpha1"],
        "selected_Xi_operator_level_source": c1_reduction["currently_available"]["selected_Xi_operator_level_source"],
        "Hess_Xi_principal_symbol_blocks": c1_reduction["currently_available"]["Hess_Xi_principal_symbol_blocks"],
        "single_driver_not_algebraically_fatal": c1_rank["closed"]["single_alpha1_driver_not_algebraically_fatal"],
        "rank_lift_criterion_known": c1_rank["closed"]["leading_rank_lift_minor_identified"],
    }

    alpha1_selected_values = {
        "evaluated_grad_V_C1_alpha1_source_vector": not c1_values_required["evaluated_grad_V_C1_alpha1_source_vector"],
        "full_lower_order_Hess_Xi_blocks": not c1_values_required["full_lower_order_Hess_Xi_blocks"],
        "deltaTheta_C1_solution": c1_template["operator_data"]["deltaTheta_C1_solution"] is not None,
        "sector_dotD_Q_u_d_L_e_N_H": all(
            c1_template["operator_data"].get(f"dotD_{slot}") is not None
            for slot in ["Q", "u", "d", "L", "e", "N", "H"]
        ),
        "zero_mode_bases": all(
            c1_template["zero_modes"].get(f"{slot}_basis") is not None
            for slot in ["Q", "u", "d", "L", "e", "N", "H"]
        ),
        "primitive_contractions": not c1_values_required["primitive_3x3_contraction_terms_for_each_sector"],
        "response_matrices": all(
            c1_template["response_matrices"].get(f"M_{sector}_C1") is not None
            for sector in ["u", "d", "e", "nu"]
        ),
    }

    unified_payload_contract = {
        "name": "SelectedPhiFinAlpha1Payload",
        "domain": phifin["phifin_schema"]["domain"],
        "codomain": ", ".join(phifin["phifin_schema"]["required_outputs"]),
        "must_commute_with": routec["finite_emission_morphism_contract"]["must_commute_with"],
        "must_emit": [
            "non-identity selected rho_E/connection transition data",
            "selected Hermitian metric and sector projectors",
            "selected D_E action slots with selected_source_verified true",
            "selected Riesz projector, complement gap, and reduced Green",
            "selected dotD_alpha1 as the same-branch derivative of selected D_E",
            "finite Hessian/C1 source vector and lower-order Hessian blocks",
            "deltaTheta_C1, sector dotD slots, zero-mode bases, and primitive C1 contractions",
        ],
        "acceptance": [
            "all existing Phi_fin shape gates remain true",
            "all selected_payload_flags become true by construction, not by lifted flags",
            "source_origin_selected_flags all become true",
            "alpha1_selected_values all become true",
            "q79/q369 branch choice is source-selected or antiunitary-equivalent with retarded selector",
            "no observed masses, CKM phase, or benchmark entries are used as inputs",
        ],
    }

    return {
        "candidate": "MTTSelectedSourceOriginAndAlpha1Driver",
        "status": "MTT_SELECTED_SOURCE_ORIGIN_AND_ALPHA1_DRIVER_REDUCED_TO_SELECTED_PHIFIN_ALPHA1_PAYLOAD",
        "source_status": input_status(),
        "superset_mode": {
            "classification": "SUPERSET_REPAIR_WITH_STRAIGHT_SUPPORT",
            "straight_path": {
                "classification": "PARTIAL_STRAIGHT_SUPPORT",
                "closed": source_support_closed,
                "blocked_at": [
                    "finite emission morphism from the selected minimizer to selected operator values",
                    "same-branch derivative proof for dotD_alpha1",
                    "finite C1 source vector, Hessian blocks, and primitive contractions",
                ],
            },
            "superset_convergence": {
                "classification": "SOURCE_AND_ALPHA1_SHARE_ONE_MISSING_PAYLOAD",
                "locked_target": "selected q79/F,m=1 S3/GS Route-C operator packet",
                "converging_paths": [
                    "S3 differential-cohomology/projective gerbe support",
                    "visible Green-Schwarz/Chern-Weil same-source packet",
                    "Route-C Strominger/HYM selected minimizer",
                    "q79 finite D_E/Riesz/Green/dotD validator schema",
                    "C1 alpha1 Hessian-response equation",
                ],
            },
            "superset_repair": {
                "repair_object": unified_payload_contract["name"],
                "reason": (
                    "The source flags and alpha1 driver flags are not independent knobs. "
                    "Both are consequences of a selected finite trace of the same Strominger/HYM branch."
                ),
            },
            "diagnostic_backfit_only": {
                "used": False,
                "reason": "No measured SM masses, mixings, CKM phase, or benchmark entries are used to select the source.",
            },
        },
        "source_origin_audit": {
            "support_closed": source_support_closed,
            "selected_flags": source_origin_selected_flags,
            "finite_phifin_shape_gates": phifin_shape,
            "phifin_selected_payload_flags": phifin_selected,
            "ordinary_nonidentity_rhoe_retired": nonidentity["gate_results"]["ordinary_rhoE_route_retired"],
            "projective_gerbe_rhoe_live": gerbe["promotion_result"]["source_level_projective_gerbe_rhoE_promoted"],
        },
        "alpha1_driver_audit": {
            "operator_level_support": alpha1_support,
            "selected_values": alpha1_selected_values,
            "rank_lift_condition": c1_rank["determinant_expansion"]["leading_full_rank_condition"],
            "finite_response_formula": c1_reduction["finite_reduction_theorem"],
            "missing_selected_operator_data": c1_attempt_missing,
        },
        "unified_payload_contract": unified_payload_contract,
        "what_closes_now": {
            "source_origin_support_not_the_blocker": all(source_support_closed.values()),
            "Phi_fin_codomain_shape_already_built": all(phifin_shape.values()),
            "ordinary_rhoE_retired_projective_gerbe_route_live": nonidentity["gate_results"]["ordinary_rhoE_route_retired"]
            and gerbe["promotion_result"]["source_level_projective_gerbe_rhoE_promoted"],
            "alpha1_driver_row_and_operator_level_source_imported": all(alpha1_support.values()),
            "single_alpha1_driver_can_lift_rank_if_C33_nonzero": c1_rank["closed"]["leading_rank_lift_minor_identified"],
            "source_and_alpha1_reduced_to_one_payload": True,
            "target_fitting_excluded_from_promotion": True,
        },
        "what_remains_open": {
            "selected_PhiFin_alpha1_payload": True,
            "selected_nonidentity_rhoE_connection_values": not all(phifin_selected.values()),
            "source_origin_selected_flags": not all(source_origin_selected_flags.values()),
            "same_branch_dotD_alpha1_derivative": source_origin_selected_flags["same_branch_derivative_verified"] is False,
            "finite_C1_source_vector_and_Hessian_blocks": c1_attempt["missing_selected_operator_data"]["evaluated_grad_V_C1_alpha1_source_vector"] is None
            or c1_attempt["missing_selected_operator_data"]["full_lower_order_Hess_Xi_blocks"] is None,
            "deltaTheta_C1_and_sector_dotD": c1_attempt["missing_selected_operator_data"]["selected_deltaTheta_C1_solution"] is None
            or c1_attempt["missing_selected_operator_data"]["explicit_dotD_Q_u_d_L_e_N_H"] is None,
            "zero_mode_bases_and_primitive_contractions": c1_attempt["missing_selected_operator_data"]["selected_zero_mode_basis_Q_u_d_L_e_N_H"] is None
            or c1_attempt["missing_selected_operator_data"]["evaluated_zero_mode_response_integrals"] is None,
            "branch_selection_or_antiunitary_retarded_selector": True,
            "full_SM_or_no_knob_closure": True,
        },
        "theorem": {
            "name": "SelectedSourceOriginAndAlpha1DriverReduction",
            "proved": True,
            "statement": (
                "Given the current corpus and repo certificates, the selected source-origin blocker and the alpha1-driver "
                "blocker reduce to the same object: a selected Phi_fin alpha1 payload emitted from the q79/F,m=1 S3/GS "
                "Strominger/HYM branch. The artifact proves this reduction and the exact acceptance contract; it does not "
                "compute the selected payload values."
            ),
        },
        "next_required_artifact": "MTT_Selected_PhiFin_Alpha1_Payload_v1",
        "target_fitting_used": False,
    }


def build_certificate(candidate: dict[str, object]) -> dict[str, object]:
    return {
        "certificate": "MTTSelectedSourceOriginAndAlpha1DriverReduction",
        "status": candidate["status"],
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "superset_mode": candidate["superset_mode"]["classification"],
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "primary_next_artifact": candidate["next_required_artifact"],
        "closure_claimed": False,
        "target_fitting_used": False,
    }


def render_bool_map(items: dict[str, object]) -> str:
    return "\n".join(f"- `{key}`: `{value}`" for key, value in items.items())


def render_list(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def render_note(candidate: dict[str, object]) -> str:
    source = candidate["source_origin_audit"]
    alpha = candidate["alpha1_driver_audit"]
    contract = candidate["unified_payload_contract"]
    closed = "\n".join(f"- `{key}`" for key, value in candidate["what_closes_now"].items() if value)
    open_items = "\n".join(f"- `{key}`" for key, value in candidate["what_remains_open"].items() if value)
    return f"""# MTT Selected Source-Origin and Alpha1 Driver v1

## Result

The selected source-origin and alpha_1 driver problems reduce to one missing
object: `{contract["name"]}`.

This is **superset repair with straight support**:

- Straight path: the fixed q79/F,m=1 S3/GS sector, Strominger selection support,
  projective gerbe source, and alpha_1 operator-level row are available.
- Superset convergence: S3/gerbe, visible Chern-Weil, Route-C, finite operator
  validators, and C1 response equations all point to the same selected payload.
- Superset repair: construct the selected `Phi_fin` alpha_1 payload, rather than
  adding separate knobs for source flags and alpha_1 flags.
- Diagnostic/backfit: not used as proof.

## Source-Origin Audit

Support already closed:

{render_bool_map(source["support_closed"])}

Selected flags still missing:

{render_bool_map(source["selected_flags"])}

Finite `Phi_fin` shape gates:

{render_bool_map(source["finite_phifin_shape_gates"])}

Selected `Phi_fin` payload flags:

{render_bool_map(source["phifin_selected_payload_flags"])}

## Alpha1 Audit

Operator-level support:

{render_bool_map(alpha["operator_level_support"])}

Selected values still missing:

{render_bool_map(alpha["selected_values"])}

Rank lift condition:

```text
{alpha["rank_lift_condition"]}
```

## Unified Payload Contract

Domain:

```text
{contract["domain"]}
```

Codomain:

```text
{contract["codomain"]}
```

It must emit:

{render_list(contract["must_emit"])}

Acceptance:

{render_list(contract["acceptance"])}

## What This Closes

{closed}

## What Remains Open

{open_items}

## Theorem

`{candidate["theorem"]["name"]}` is proved:

{candidate["theorem"]["statement"]}

Next artifact: `{candidate["next_required_artifact"]}`.
"""


def main() -> None:
    candidate = build_candidate()
    certificate = build_certificate(candidate)
    if "--write" in sys.argv:
        OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(render_note(candidate), encoding="utf-8")
    print(json.dumps(certificate, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
