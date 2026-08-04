"""Build the selected Route-C/Strominger Galerkin solve specification."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")
Q79_CERTS = Q79 / "certificates"
Q79_SCRIPTS = Q79 / "scripts"

OUTPUT_DATA = DATA / "selected_routec_strominger_galerkin_solve_spec.candidate.json"
OUTPUT_CERT = CERTS / "selected_routec_strominger_galerkin_solve_spec_certificate.json"
OUTPUT_NOTE = CORPUS / "MTT_Selected_RouteC_Strominger_Galerkin_Solve_Spec_v1.md"

INPUTS = {
    "previous": DATA / "selected_spectral_galerkin_projector_retention_data.candidate.json",
    "routec_scaffold": Q79_CERTS / "iwasawa_route_c_finite_solve_scaffold_certificate.json",
    "routec_residual_template": Q79_CERTS / "iwasawa_route_c_residuals.template.json",
    "galerkin_protocol": Q79_CERTS / "iwasawa_non_invariant_galerkin_protocol_certificate.json",
    "galerkin_skeleton": Q79_CERTS / "iwasawa_galerkin_basis_skeleton_certificate.json",
    "spectral_galerkin_template": Q79_CERTS / "iwasawa_spectral_galerkin_data.template.json",
    "selected_hym_attempt": Q79_CERTS / "selected_hym_operator_source_attempt_certificate.json",
    "selected_source_promotion_validator": Q79_SCRIPTS / "validate_iwasawa_selected_source_promotion.py",
}


def load_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def input_status() -> dict[str, object]:
    status: dict[str, object] = {}
    for key, path in INPUTS.items():
        entry: dict[str, object] = {"path": str(path), "present": path.exists()}
        if path.exists() and path.suffix == ".json":
            entry["status"] = load_json(path).get("status", "UNKNOWN")
        elif path.exists():
            entry["status"] = "SCRIPT_PRESENT"
        else:
            entry["status"] = "MISSING"
        status[key] = entry
    return status


def run_routec_scaffold(mesh_n: int) -> dict[str, object]:
    proc = subprocess.run(
        [sys.executable, str(Q79_SCRIPTS / "scaffold_iwasawa_route_c_solver.py"), "--mesh-N", str(mesh_n)],
        cwd=Q79,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    return json.loads(proc.stdout)


def build_candidate() -> dict[str, object]:
    previous = load_json(INPUTS["previous"])
    scaffold_cert = load_json(INPUTS["routec_scaffold"])
    residual_template = load_json(INPUTS["routec_residual_template"])
    galerkin_protocol = load_json(INPUTS["galerkin_protocol"])
    galerkin_skeleton = load_json(INPUTS["galerkin_skeleton"])
    spectral_template = load_json(INPUTS["spectral_galerkin_template"])
    hym_attempt = load_json(INPUTS["selected_hym_attempt"])
    scaffold_n1 = run_routec_scaffold(1)

    output_manifest = {
        "route_c_residual": "candidate_data/selected_routec_strominger_galerkin_solve/route_c_residual.candidate.json",
        "rhoE_mesh": "candidate_data/selected_routec_strominger_galerkin_solve/rhoE_mesh.candidate.json",
        "rhoE_metric": "candidate_data/selected_routec_strominger_galerkin_solve/rhoE_metric.candidate.json",
        "sector_maps": "candidate_data/selected_routec_strominger_galerkin_solve/sector_maps.candidate.json",
        "de_action": "candidate_data/selected_routec_strominger_galerkin_solve/de_action.candidate.json",
        "riesz_gap": "candidate_data/selected_routec_strominger_galerkin_solve/riesz_gap.candidate.json",
        "reduced_green": "candidate_data/selected_routec_strominger_galerkin_solve/reduced_green.candidate.json",
        "dotd_response": "candidate_data/selected_routec_strominger_galerkin_solve/dotd_response.candidate.json",
        "spectral_galerkin_data": "candidate_data/selected_routec_strominger_galerkin_solve/spectral_galerkin_data.candidate.json",
        "c1_primitive_contractions": "candidate_data/selected_routec_strominger_galerkin_solve/c1_primitive_contractions.candidate.json",
    }

    residual_acceptance = {
        "residual_slots": residual_template["residuals"],
        "positive_gates": residual_template["positive_gates"],
        "pass_rule": "Every residual value must be present and <= its tolerance; all positive gates must exceed strict lower bounds.",
        "selected_source_rule": "selected_source_verified must be true because the residual solve, not the target data, selects the branch.",
    }

    spectral_acceptance = {
        "cluster_rule": galerkin_protocol["gap_error_certificate"]["computed_cluster"],
        "gap_rule": galerkin_protocol["gap_error_certificate"]["computed_gap"],
        "error_budget": galerkin_protocol["gap_error_certificate"]["total_error_budget"],
        "pass_rule": galerkin_protocol["gap_error_certificate"]["pass_rule"],
        "consequence": galerkin_protocol["gap_error_certificate"]["consequence"],
        "basis_minimum": "The solve must use a quotient-valid basis beyond the left-invariant scalar_count=1 smoke sector.",
    }

    execution_stages = [
        {
            "stage": "S0_selected_source",
            "must_emit": ["source_selected_by_mtt", "fixed q79/F,m=1 S3/GS branch", "no measured-data selector"],
            "validator": "validate_iwasawa_route_c_residuals.py",
        },
        {
            "stage": "S1_basis_and_domain",
            "must_emit": ["basis_B_N", "deck/periodic constraints", "bundle transition/equivariance matrices", "metric quadrature"],
            "validator": "iwasawa_spectral_galerkin_data.template.json success_gates",
        },
        {
            "stage": "S2_connection_metric_rhoE",
            "must_emit": ["A*", "h*", "projective/twisted rho_E induced by selected source"],
            "validators": ["validate_iwasawa_rhoE_mesh.py", "validate_iwasawa_rhoE_metric.py"],
        },
        {
            "stage": "S3_sector_operators",
            "must_emit": ["sector projectors", "D_E action for Q,u,d,L,e,N,H"],
            "validators": ["validate_iwasawa_sector_maps.py", "validate_iwasawa_de_action.py"],
        },
        {
            "stage": "S4_spectral_projectors",
            "must_emit": ["Riesz projectors", "complement gaps", "reduced Green operators", "truncation error bounds"],
            "validators": ["validate_iwasawa_riesz_gap.py", "validate_iwasawa_reduced_green.py"],
        },
        {
            "stage": "S5_alpha1_response",
            "must_emit": ["deltaTheta_C1", "same-branch dotD_alpha1", "horizontal zero-mode responses"],
            "validator": "validate_iwasawa_dotd_response.py",
        },
        {
            "stage": "S6_c1_contractions",
            "must_emit": ["zero-mode bases", "primitive 3x3 contraction terms", "response matrices and C33 tests"],
            "validator": "selected_c1_primitive_contractions.template.json fill contract",
        },
    ]

    return {
        "candidate": "MTTSelectedRouteCStromingerGalerkinSolveSpec",
        "status": "MTT_SELECTED_ROUTEC_STROMINGER_GALERKIN_SOLVE_SPEC_BUILT_VALUES_OPEN",
        "source_status": input_status(),
        "superset_mode": {
            "classification": "SUPERSET_REPAIR_EXECUTABLE_SPEC",
            "straight_path": {
                "classification": "SCAFFOLD_ONLY_VALUES_OPEN",
                "reason": "The finite scaffold and Galerkin protocol are available, but selected values are not yet computed.",
            },
            "superset_convergence": {
                "classification": "ROUTEC_STROMINGER_GALERKIN_EXECUTION_SPEC",
                "locked_target": "one selected q79/F,m=1 S3/GS finite operator payload",
                "converging_inputs": [
                    "Route-C residual scaffold",
                    "non-invariant Galerkin protocol",
                    "selected S3 twisted source support",
                    "rho_E/D_E/Riesz/Green/dotD validators",
                    "C1 alpha1 response contract",
                ],
            },
            "superset_repair": {
                "repair_object": "first selected small-N nonlinear residual solve or symbolic selected ansatz",
                "reason": "The remaining unknown is numerical/symbolic selected data, not another high-level proof interface.",
            },
            "diagnostic_backfit_only": {
                "used": False,
                "reason": "The spec forbids observed masses, mixings, benchmark matrices, and target residuals as selectors.",
            },
        },
        "mesh_scaffold": {
            "mesh_N": scaffold_n1["mesh"]["mesh_N"],
            "counts": scaffold_n1["mesh"],
            "matches_certificate_counts": scaffold_n1["mesh"] == scaffold_cert["mesh_N1_counts"],
            "next_mesh_policy": "N=1 is a scaffold smoke size; actual solve may increase N, but must report error budget and convergence.",
        },
        "basis_protocol": {
            "closed_skeleton": galerkin_skeleton["closed_form_fiber_skeleton"],
            "basis_source_options": galerkin_skeleton["basis_source_options"],
            "still_missing_for_actual_basis": galerkin_skeleton["still_missing_for_actual_B_N"],
            "non_invariant_protocol_values_open": galerkin_protocol["values_still_open"],
            "spectral_template_success_gates": spectral_template["success_gates"],
        },
        "residual_acceptance": residual_acceptance,
        "spectral_acceptance": spectral_acceptance,
        "execution_stages": execution_stages,
        "output_manifest": output_manifest,
        "validator_pipeline": scaffold_cert["downstream_validator_pipeline"],
        "promotion_gate": {
            "script": str(INPUTS["selected_source_promotion_validator"]),
            "target_levels": ["rhoE_source", "de_response"],
            "must_pass_after_outputs_exist": True,
            "reason": "This guardrail prevents identity rhoE, pure-gauge, smoke D_E, or lifted selected flags from becoming proof data.",
        },
        "currently_blocked_by": {
            "selected_hym_operator_source_verified": not hym_attempt["calculation_results"]["selected_hym_operator_source_verified"],
            "route_c_honest_operator_pipeline_pass": not hym_attempt["calculation_results"]["route_c_honest_operator_pipeline_pass"],
            "actual_selected_values": True,
            "basis_B_N_values": True,
            "C1_primitives": True,
        },
        "what_closes_now": {
            "selected_solve_executable_spec_built": True,
            "mesh_N1_accounting_reproduced": scaffold_n1["mesh"] == scaffold_cert["mesh_N1_counts"],
            "residual_acceptance_contract_built": True,
            "spectral_gap_error_contract_built": True,
            "output_manifest_built": True,
            "validator_order_locked": True,
            "promotion_guardrail_linked": INPUTS["selected_source_promotion_validator"].exists(),
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "actual_selected_small_N_solve_or_symbolic_ansatz": True,
            "selected_rhoE_metric_connection_values": True,
            "actual_basis_B_N_and_quadrature": True,
            "selected_DE_Riesz_Green_dotD_outputs": True,
            "spectral_gap_error_numbers": True,
            "zero_mode_bases_and_C1_primitives": True,
            "full_SM_or_no_knob_closure": True,
        },
        "theorem": {
            "name": "SelectedRouteCStromingerGalerkinSolveSpecification",
            "proved": True,
            "statement": (
                "The selected Route-C/Strominger Galerkin solve is now specified as an executable finite contract. "
                "It reuses the q79 finite residual scaffold, non-invariant Galerkin matrix protocol, downstream validators, "
                "Riesz gap/error rule, and C1 response contract. It does not compute selected values; the next step is to run "
                "or symbolically fill the first honest selected small-N solve."
            ),
        },
        "next_required_artifact": "MTT_Selected_RouteC_Strominger_Galerkin_First_Run_v1",
        "target_fitting_used": False,
        "previous_frontier": previous["next_required_artifact"],
    }


def build_certificate(candidate: dict[str, object]) -> dict[str, object]:
    return {
        "certificate": "MTTSelectedRouteCStromingerGalerkinSolveSpec",
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


def render_stages(stages: list[dict[str, object]]) -> str:
    lines: list[str] = []
    for stage in stages:
        lines.append(f"### {stage['stage']}")
        lines.append("Must emit:")
        lines.append(render_list(stage["must_emit"]))  # type: ignore[arg-type]
        validator = stage.get("validator") or ", ".join(stage.get("validators", []))  # type: ignore[arg-type]
        lines.append(f"Validator: `{validator}`")
        lines.append("")
    return "\n".join(lines).rstrip()


def render_note(candidate: dict[str, object]) -> str:
    closed = "\n".join(f"- `{key}`" for key, value in candidate["what_closes_now"].items() if value)
    open_items = "\n".join(f"- `{key}`" for key, value in candidate["what_remains_open"].items() if value)
    return f"""# MTT Selected Route-C/Strominger Galerkin Solve Spec v1

## Result

The selected Route-C/Strominger Galerkin solve is now an executable spec, not a
loose wish.

This is **superset repair executable spec**:

- Straight path: scaffold only; selected values remain open.
- Superset convergence: Route-C residuals, Galerkin basis protocol,
  rho_E/D_E/Riesz/Green/dotD validators, and C1 response all lock one target.
- Superset repair: run or symbolically fill the first selected small-N solve.
- Diagnostic/backfit: not used as proof.

## Mesh Scaffold

{render_bool_map(candidate["mesh_scaffold"]["counts"])}

Matches q79 scaffold certificate: `{candidate["mesh_scaffold"]["matches_certificate_counts"]}`.

## Residual Acceptance

- pass rule: {candidate["residual_acceptance"]["pass_rule"]}
- selected source rule: {candidate["residual_acceptance"]["selected_source_rule"]}

## Spectral Acceptance

- cluster rule: {candidate["spectral_acceptance"]["cluster_rule"]}
- gap rule: {candidate["spectral_acceptance"]["gap_rule"]}
- error budget: {candidate["spectral_acceptance"]["error_budget"]}
- pass rule: {candidate["spectral_acceptance"]["pass_rule"]}
- consequence: {candidate["spectral_acceptance"]["consequence"]}
- basis minimum: {candidate["spectral_acceptance"]["basis_minimum"]}

## Execution Stages

{render_stages(candidate["execution_stages"])}

## Output Manifest

{render_bool_map(candidate["output_manifest"])}

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
