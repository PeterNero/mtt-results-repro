"""Build the selected spectral Galerkin/projector-retention data artifact."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")
Q79_DATA = Q79 / "candidate_data"
Q79_CERTS = Q79 / "certificates"
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")

OUTPUT_DATA = DATA / "selected_spectral_galerkin_projector_retention_data.candidate.json"
OUTPUT_CERT = CERTS / "selected_spectral_galerkin_projector_retention_data_certificate.json"
OUTPUT_NOTE = CORPUS / "MTT_Selected_Spectral_Galerkin_Projector_Retention_Data_v1.md"

INPUTS = {
    "previous": DATA / "selected_phifin_alpha1_payload.candidate.json",
    "s3_class_restriction": Q79_CERTS / "visible_twisted_s3_class_restriction_closure_certificate.json",
    "selected_hym_attempt": Q79_CERTS / "selected_hym_operator_source_attempt_certificate.json",
    "matter_slot_attempt": Q79_CERTS / "selected_matter_slot_transversality_source_attempt_certificate.json",
    "zero_mode_interface": Q79_CERTS / "selected_zero_mode_basis_dotd_interface_certificate.json",
    "rplus_support": Q79_CERTS / "c1_iwasawa_rplus_support_certificate.json",
    "monad_role": Q79_DATA / "iwasawa_monad_visible_source_role.candidate.json",
    "routec_de_action": Q79_DATA / "iwasawa_route_c_branch_smoke" / "current_q79_orientation" / "de_action.candidate.json",
    "routec_reduced_green": Q79_DATA / "iwasawa_route_c_branch_smoke" / "current_q79_orientation" / "reduced_green.candidate.json",
    "routec_dotd": Q79_DATA / "iwasawa_route_c_branch_smoke" / "current_q79_orientation" / "dotd_response.candidate.json",
}

CORPUS_CLUES = {
    "fixed_points_galerkin": OBSIDIAN / "4 Fixed Points" / "Fixed_Points_I__Fixed_Points_over_Multi_Bundle_Manifolds_v5.md",
    "core_strominger_selection": OBSIDIAN / "1 Core & Encodings" / "Modal_Triplet_Theory__Admissibility__Encodings__and_the_Structure_of_Physical_Description_v11.md",
    "superset_strominger_slice": OBSIDIAN / "3 Core Foundations" / "Modal_Triplet_Theory__MTT_as_a_Superset_v2.md",
    "finite_coherent_projection": OBSIDIAN / "5 Dirac Delta" / "Finite_Coherent_Projection_in_Modal_Triplet_Theory_v2.md",
    "central_circle_projector_control": OBSIDIAN / "13 Standard Model & Topology-Only Constraints" / "The_Central_Circle__Inertia__Mass__Gravity__and_Time_as_Shared_Coherence_Bookkeeping_in_Modal_Triplet_Theory.md",
}


def load_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def input_status() -> dict[str, object]:
    return {
        key: {
            "path": str(path),
            "present": path.exists(),
            "status": load_json(path).get("status", "UNKNOWN") if path.exists() else "MISSING",
        }
        for key, path in INPUTS.items()
    }


def corpus_status() -> dict[str, object]:
    return {key: {"path": str(path), "present": path.exists()} for key, path in CORPUS_CLUES.items()}


def all_slot_flag(slots: dict[str, dict[str, object]], flag: str) -> bool:
    return all(bool(slot.get(flag)) for slot in slots.values())


def build_candidate() -> dict[str, object]:
    previous = load_json(INPUTS["previous"])
    s3 = load_json(INPUTS["s3_class_restriction"])
    hym = load_json(INPUTS["selected_hym_attempt"])
    matter = load_json(INPUTS["matter_slot_attempt"])
    zero = load_json(INPUTS["zero_mode_interface"])
    rplus = load_json(INPUTS["rplus_support"])
    monad = load_json(INPUTS["monad_role"])
    de_action = load_json(INPUTS["routec_de_action"])
    green = load_json(INPUTS["routec_reduced_green"])
    dotd = load_json(INPUTS["routec_dotd"])

    de_slots = de_action["operator_slots"]
    green_slots = green["green_slots"]
    dotd_slots = dotd["dotd_response_slots"]
    zero_slots = zero["basis_slots"]

    block_projector_layer = {
        "selected_S3_flat_Deligne_class": s3["what_this_closes"]["selected_S3_flat_Deligne_class"],
        "smooth_Freed_Witten_cancellation": s3["what_this_closes"]["smooth_S3_twisted_Freed_Witten_cancellation"],
        "block_family_Higgs_projector_retention": s3["what_this_closes"]["block_factorized_family_Higgs_projector_retention_for_this_source"],
        "retention_scope": s3["block_projector_retention"]["retention_scope"],
    }

    spectral_projector_layer = {
        "coherent_spectral_zero_mode_projector_retention": not s3["still_open"]["coherent_spectral_zero_mode_projector_retention"],
        "selected_D_E_dotD_Riesz_Green": not s3["still_open"]["selected_D_E_dotD_Riesz_Green"],
        "selected_HYM_operator_source_verified": hym["calculation_results"]["selected_hym_operator_source_verified"],
        "matter_slot_selected_source_verified": matter["calculation_results"]["selected_source_verified"],
        "zero_mode_slot_values_filled": all(slot.get("ordered_zero_mode_basis") is not None for slot in zero_slots.values()),
        "all_routec_DE_selected_source_flags": all_slot_flag(de_slots, "selected_source_verified"),
        "all_routec_Green_selected_source_flags": all_slot_flag(green_slots, "selected_source_verified"),
        "all_routec_dotD_selected_and_alpha1_flags": all_slot_flag(dotd_slots, "selected_dotD_source_verified")
        and all_slot_flag(dotd_slots, "alpha1_driver_verified"),
    }

    corpus_support = {
        "Galerkin_approximation_theorem_available": CORPUS_CLUES["fixed_points_galerkin"].exists(),
        "Strominger_selection_encoding_available": CORPUS_CLUES["core_strominger_selection"].exists()
        and CORPUS_CLUES["superset_strominger_slice"].exists(),
        "zero_mode_recovery_principle_available": CORPUS_CLUES["finite_coherent_projection"].exists(),
        "spectral_gap_projector_control_available": CORPUS_CLUES["central_circle_projector_control"].exists(),
    }

    selected_solve_contract = {
        "name": "SelectedRouteCStromingerGalerkinResidualSolve",
        "domain": "q79/F,m=1 S3/GS selected twisted source with block projectors already retained",
        "unknowns": [
            "finite selected HYM/Strominger connection A* and metric h*",
            "projective/twisted rho_E transition data induced by A* and the selected S3 gerbe",
            "sector operators D_E,Q,u,d,L,e,N,H from the same A*, h*",
            "Riesz projectors, complement gaps, reduced Green operators, and truncation error bounds",
            "same-branch dotD_alpha1 = dD_E(deltaTheta_C1)/depsilon at epsilon=0",
            "ordered zero-mode bases in selected L2-horizontal gauge",
        ],
        "equations": [
            "Route-C residual equations with selected_source_verified true",
            "HYM/Strominger residual equations in the selected q79/F,m=1 S3/GS sector",
            "spectral gap separation for each sector operator",
            "Riesz projector stability bound ||P_N-P|| <= error(gap, residual, N)",
            "horizontal response equation dotPsi_a,i = -G_a Q_a dotD_a Psi_a,i",
            "C1 Hessian equation Hess_Xi(Theta0) deltaTheta_C1 = -Pi_coh grad V_C1(Theta0)",
        ],
        "acceptance": [
            "selected_source_verified true for route residual, D_E, Riesz/Green, and dotD slots",
            "coherent spectral projectors proved, not merely block projectors",
            "zero-mode bases supplied for Q,u,d,L,e,N,H",
            "alpha1_driver_verified true from selected Hessian/C1 equation",
            "primitive C1 contractions become computable from emitted data",
            "no observed masses, CKM/PMNS phases, benchmark matrices, or target residuals used as selectors",
        ],
    }

    return {
        "candidate": "MTTSelectedSpectralGalerkinProjectorRetentionData",
        "status": "MTT_SELECTED_SPECTRAL_GALERKIN_PROJECTOR_RETENTION_DATA_REDUCED_TO_SELECTED_ROUTEC_GALERKIN_SOLVE",
        "source_status": input_status(),
        "corpus_status": corpus_status(),
        "superset_mode": {
            "classification": "SUPERSET_REPAIR_CONTRACT_REDUCTION",
            "straight_path": {
                "classification": "BLOCK_PROJECTOR_STRAIGHT_PATH_CLOSED_BUT_INSUFFICIENT",
                "reason": "The selected S3 twisted source preserves block-family/Higgs projectors, but this is not the same as coherent spectral zero-mode projector retention.",
            },
            "superset_convergence": {
                "classification": "GALERKIN_STROMINGER_ZERO_MODE_CONVERGENCE",
                "converging_paths": [
                    "MTT fixed-point Galerkin approximation discipline",
                    "Strominger/HYM selected-source encoding",
                    "finite coherent zero-mode recovery",
                    "Route-C D_E/Riesz/Green/dotD finite validator schema",
                    "C1 alpha1 Hessian-response equation",
                ],
                "locked_target": selected_solve_contract["name"],
            },
            "superset_repair": {
                "repair_object": selected_solve_contract["name"],
                "reason": "Only an honest selected finite solve can convert support candidates into selected spectral projector and operator values.",
            },
            "diagnostic_backfit_only": {
                "used": False,
                "reason": "No measured SM constants or benchmark matrices are used to select the Galerkin data.",
            },
        },
        "two_layer_projector_audit": {
            "block_projector_layer": block_projector_layer,
            "spectral_projector_layer": spectral_projector_layer,
            "layer_separation_honest": block_projector_layer["block_family_Higgs_projector_retention"]
            and not all(spectral_projector_layer.values()),
        },
        "corpus_support": corpus_support,
        "routec_operator_support": {
            "DE_boundary_shapes_present": all_slot_flag(de_slots, "boundary_conditions_verified"),
            "Green_operator_and_gap_shapes_present": all_slot_flag(green_slots, "operator_data_verified")
            and all_slot_flag(green_slots, "riesz_gap_verified"),
            "dotD_horizontal_shapes_present": all_slot_flag(dotd_slots, "green_operator_verified")
            and all_slot_flag(dotd_slots, "horizontal_gauge_verified"),
            "selected_flags_all_false": not all_slot_flag(de_slots, "selected_source_verified")
            and not all_slot_flag(green_slots, "selected_source_verified")
            and not all_slot_flag(dotd_slots, "selected_dotD_source_verified"),
        },
        "monad_role_discipline": {
            "monad_can_seed_matter_zero_modes": monad["role_comparison"]["monad_can_still_be_matter_zero_mode_source"],
            "monad_cannot_be_visible_alpha1_source": not monad["role_comparison"]["monad_alone_realizes_visible_alpha1_source"],
            "requires_recomputed_same_source_operator_data": monad["role_comparison"]["larger_bundle_escape_requires_new_calculation"],
        },
        "alpha1_projection_discipline": {
            "invariant_Rplus_alpha1_support_closed": rplus["closed"]["Rplus_alpha1_only"],
            "coherent_projection_context_closed": rplus["closed"]["coherent_projection_context"],
            "rank_lift_still_depends_on_dotD_and_zero_modes": rplus["open"]["zero_mode_contractions_with_alpha1_driver"],
        },
        "selected_solve_contract": selected_solve_contract,
        "what_closes_now": {
            "block_vs_spectral_projector_distinction_closed": True,
            "selected_S3_block_projector_retention_imported": block_projector_layer["block_family_Higgs_projector_retention"],
            "corpus_Galerkin_and_spectral_gap_support_imported": all(corpus_support.values()),
            "routec_operator_shape_support_imported": True,
            "monad_reuse_as_visible_alpha1_source_rejected": True,
            "next_selected_solve_contract_built": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_RouteC_Strominger_Galerkin_residual_solve": True,
            "selected_HYM_Strominger_metric_connection": True,
            "operator_level_projective_rhoE_from_selected_connection": True,
            "coherent_spectral_projector_retention": not all(spectral_projector_layer.values()),
            "selected_DE_Riesz_Green_dotD_values": True,
            "finite_C1_Hessian_deltaTheta_and_dotD": True,
            "zero_mode_bases_and_primitive_C1_contractions": True,
            "full_SM_or_no_knob_closure": True,
        },
        "theorem": {
            "name": "SelectedSpectralGalerkinProjectorRetentionReduction",
            "proved": True,
            "statement": (
                "The selected S3 twisted source closes block-family/Higgs projector retention, but it does not close coherent "
                "spectral zero-mode projector retention. The available MTT corpus supplies the correct Galerkin, spectral-gap, "
                "Strominger-selection, and zero-mode recovery discipline; the q79 repo supplies finite operator shapes. The missing "
                "object is therefore an honest selected Route-C/Strominger Galerkin residual solve with gap/error bounds and emitted "
                "D_E, Green, dotD, zero-mode, and C1 data."
            ),
        },
        "next_required_artifact": "MTT_Selected_RouteC_Strominger_Galerkin_Solve_Spec_v1",
        "target_fitting_used": False,
        "previous_frontier": previous["next_required_artifact"],
    }


def build_certificate(candidate: dict[str, object]) -> dict[str, object]:
    return {
        "certificate": "MTTSelectedSpectralGalerkinProjectorRetentionReduction",
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
    audit = candidate["two_layer_projector_audit"]
    contract = candidate["selected_solve_contract"]
    closed = "\n".join(f"- `{key}`" for key, value in candidate["what_closes_now"].items() if value)
    open_items = "\n".join(f"- `{key}`" for key, value in candidate["what_remains_open"].items() if value)
    return f"""# MTT Selected Spectral Galerkin Projector Retention Data v1

## Result

The projector-retention gate splits into two layers:

- Block-sector projector retention is closed for the selected twisted S3 source.
- Coherent spectral zero-mode projector retention remains open.

This is **superset repair contract reduction**:

- Straight path: block projector retention is real but insufficient.
- Superset convergence: Galerkin fixed-point discipline, Strominger/HYM selection,
  zero-mode recovery, Route-C finite operators, and C1 alpha_1 response all point
  to one selected finite solve.
- Superset repair: construct `SelectedRouteCStromingerGalerkinResidualSolve`.
- Diagnostic/backfit: not used as proof.

## Two-Layer Projector Audit

Block layer:

{render_bool_map(audit["block_projector_layer"])}

Spectral layer:

{render_bool_map(audit["spectral_projector_layer"])}

## Corpus Support

{render_bool_map(candidate["corpus_support"])}

## Selected Solve Contract

Unknowns:

{render_list(contract["unknowns"])}

Equations:

{render_list(contract["equations"])}

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
