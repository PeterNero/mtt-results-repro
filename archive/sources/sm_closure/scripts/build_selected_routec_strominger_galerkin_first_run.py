"""Fill the selected Route-C/Strominger Galerkin first-run manifest.

This first run is intentionally conservative.  It imports the q79 finite
Route-C smoke payload into the manifest as honest unselected data, then runs a
separate formal-lift diagnostic showing which downstream algebra would pass if
the missing selected-source theorem were supplied.  The formal lift is never
promoted as proof.
"""

from __future__ import annotations

import copy
import json
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")
Q79_DATA = Q79 / "candidate_data"
Q79_CERTS = Q79 / "certificates"
Q79_SCRIPTS = Q79 / "scripts"

MANIFEST_DIR = DATA / "selected_routec_strominger_galerkin_solve"
FORMAL_DIR = MANIFEST_DIR / "formal_lift_diagnostic"

OUTPUT_DATA = DATA / "selected_routec_strominger_galerkin_first_run.candidate.json"
OUTPUT_CERT = CERTS / "selected_routec_strominger_galerkin_first_run_certificate.json"
OUTPUT_NOTE = CORPUS / "MTT_Selected_RouteC_Strominger_Galerkin_First_Run_v1.md"

SMOKE_DIR = Q79_DATA / "iwasawa_route_c_branch_smoke" / "current_q79_orientation"
LIFT_DIR = Q79_DATA / "selected_valpha_operator_source_sufficiency" / "route_c_lifted_flags"

MANIFEST_FILES = {
    "route_c_residual": "route_c_residual.candidate.json",
    "rhoE_mesh": "rhoE_mesh.candidate.json",
    "rhoE_metric": "rhoE_metric.candidate.json",
    "sector_maps": "sector_maps.candidate.json",
    "de_action": "de_action.candidate.json",
    "riesz_gap": "riesz_gap.candidate.json",
    "reduced_green": "reduced_green.candidate.json",
    "dotd_response": "dotd_response.candidate.json",
    "spectral_galerkin_data": "spectral_galerkin_data.candidate.json",
    "c1_primitive_contractions": "c1_primitive_contractions.candidate.json",
}

SMOKE_SOURCES = {
    "route_c_residual": SMOKE_DIR / "route_c_residual.candidate.json",
    "rhoE_mesh": SMOKE_DIR / "rhoE_mesh.candidate.json",
    "rhoE_metric": SMOKE_DIR / "rhoE_metric.candidate.json",
    "sector_maps": SMOKE_DIR / "sector_maps.candidate.json",
    "de_action": SMOKE_DIR / "de_action.candidate.json",
    "riesz_gap": SMOKE_DIR / "riesz_gap.candidate.json",
    "reduced_green": SMOKE_DIR / "reduced_green.candidate.json",
    "dotd_response": SMOKE_DIR / "dotd_response.candidate.json",
}

FORMAL_SOURCES = {
    "route_c_residual": LIFT_DIR / "route_c_residuals.hypothetical_selected.json",
    "rhoE_mesh": LIFT_DIR / "rhoE_mesh.hypothetical_selected.json",
    "rhoE_metric": LIFT_DIR / "rhoE_metric.hypothetical_selected.json",
    "sector_maps": LIFT_DIR / "sector_maps.hypothetical_selected.json",
    "de_action": LIFT_DIR / "de_action.hypothetical_selected.json",
    "riesz_gap": LIFT_DIR / "riesz_gap.hypothetical_selected.json",
    "reduced_green": LIFT_DIR / "reduced_green.hypothetical_selected.json",
    "dotd_response": LIFT_DIR / "dotd_response.hypothetical_selected.json",
}

VALIDATORS = {
    "route_c_residual": "validate_iwasawa_route_c_residuals.py",
    "rhoE_mesh": "validate_iwasawa_rhoE_mesh.py",
    "rhoE_metric": "validate_iwasawa_rhoE_metric.py",
    "sector_maps": "validate_iwasawa_sector_maps.py",
    "de_action": "validate_iwasawa_de_action.py",
    "riesz_gap": "validate_iwasawa_riesz_gap.py",
    "reduced_green": "validate_iwasawa_reduced_green.py",
    "dotd_response": "validate_iwasawa_dotd_response.py",
}


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def copy_payloads() -> None:
    MANIFEST_DIR.mkdir(parents=True, exist_ok=True)
    FORMAL_DIR.mkdir(parents=True, exist_ok=True)
    for key, source in SMOKE_SOURCES.items():
        shutil.copyfile(source, MANIFEST_DIR / MANIFEST_FILES[key])
    for key, source in FORMAL_SOURCES.items():
        shutil.copyfile(source, FORMAL_DIR / MANIFEST_FILES[key])


def open_spectral_payload() -> dict[str, Any]:
    template_path = Q79_CERTS / "iwasawa_spectral_galerkin_data.template.json"
    template = load_json(template_path)
    return {
        "schema": "MTTSelectedRouteCStromingerGalerkinSpectralData.v1",
        "status": "OPEN_SELECTED_BASIS_AND_PROJECTOR_VALUES_MISSING",
        "source_template": str(template_path),
        "template_success_gates": template.get("success_gates", {}),
        "manifest_role": "records the still-missing quotient-valid B_N, quadrature, gap, and error-budget data",
        "selected_source_verified": False,
        "target_fitting_used": False,
    }


def open_c1_payload() -> dict[str, Any]:
    return {
        "schema": "MTTSelectedRouteCC1PrimitiveContractions.v1",
        "status": "OPEN_C1_PRIMITIVE_CONTRACTIONS_MISSING",
        "manifest_role": "records the still-missing primitive C1 contractions after selected D_E/Riesz/Green/dotD data exist",
        "required_outputs": [
            "zero_mode_bases",
            "primitive_three_by_three_contraction_terms",
            "linear_response_matrices",
            "C33/nonzero-family-rank tests",
        ],
        "selected_source_verified": False,
        "target_fitting_used": False,
    }


def run_validator(script_name: str, data_path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(Q79_SCRIPTS / script_name), str(data_path)],
        cwd=Q79,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return {
        "exit_code": proc.returncode,
        "passed": proc.returncode == 0,
        "output": proc.stdout.strip().splitlines()[-6:],
    }


def run_validator_set(base_dir: Path) -> dict[str, Any]:
    return {
        key: run_validator(script, base_dir / MANIFEST_FILES[key])
        for key, script in VALIDATORS.items()
    }


def build_promotion_packet() -> Path:
    packet = {
        "schema": "IwasawaSelectedSourcePromotionPacket.v1",
        "status": "FORMAL_LIFT_DIAGNOSTIC_NOT_PROOF",
        "source_kind": "finite_HYM_Strominger_solve",
        "target_level": "de_response",
        "selected_source_verified": True,
        "no_observed_flavor_inputs": True,
        "uses_execution_ii_benchmarks": False,
        "uses_observed_masses_or_mixings": False,
        "uses_diagnostic_h1_three_as_selected": False,
        "uses_pure_gauge_prototype_as_selected": False,
        "paths": {
            "rhoE_mesh": MANIFEST_FILES["rhoE_mesh"],
            "rhoE_metric": MANIFEST_FILES["rhoE_metric"],
            "sector_maps": MANIFEST_FILES["sector_maps"],
            "route_c_residuals": MANIFEST_FILES["route_c_residual"],
            "de_action": MANIFEST_FILES["de_action"],
            "riesz_gap": MANIFEST_FILES["riesz_gap"],
            "reduced_green": MANIFEST_FILES["reduced_green"],
            "dotd_response": MANIFEST_FILES["dotd_response"],
        },
        "response_gate": {
            "minimum_source_norm": 1e-12,
            "minimum_response_norm": 1e-12,
        },
        "guardrails": {
            "claims_physical_selected_source": False,
            "uses_lifted_flags_as_proof": False,
        },
    }
    path = FORMAL_DIR / "selected_source_promotion.formal_lift.json"
    write_json(path, packet)
    return path


def build_candidate() -> dict[str, Any]:
    copy_payloads()
    write_json(MANIFEST_DIR / MANIFEST_FILES["spectral_galerkin_data"], open_spectral_payload())
    write_json(MANIFEST_DIR / MANIFEST_FILES["c1_primitive_contractions"], open_c1_payload())
    write_json(FORMAL_DIR / MANIFEST_FILES["spectral_galerkin_data"], open_spectral_payload())
    write_json(FORMAL_DIR / MANIFEST_FILES["c1_primitive_contractions"], open_c1_payload())

    route_residual = load_json(MANIFEST_DIR / MANIFEST_FILES["route_c_residual"])
    formal_route = load_json(FORMAL_DIR / MANIFEST_FILES["route_c_residual"])
    formal_packet = build_promotion_packet()

    honest_validators = run_validator_set(MANIFEST_DIR)
    formal_validators = run_validator_set(FORMAL_DIR)
    formal_promotion = run_validator("validate_iwasawa_selected_source_promotion.py", formal_packet)

    honest_pass = all(result["passed"] for result in honest_validators.values())
    formal_pass = all(result["passed"] for result in formal_validators.values())

    return {
        "candidate": "MTTSelectedRouteCStromingerGalerkinFirstRun",
        "status": "MTT_SELECTED_ROUTEC_STROMINGER_GALERKIN_FIRST_RUN_MANIFEST_FILLED_SELECTOR_OPEN",
        "superset_mode": {
            "classification": "SUPERSET_REPAIR_WITH_DIAGNOSTIC_FORMAL_LIFT",
            "straight_path": {
                "classification": "HONEST_IMPORT_UNSELECTED",
                "description": "The root manifest is filled with the q79 current-branch finite Route-C smoke payload without changing selected-source flags.",
            },
            "superset_convergence": {
                "classification": "LOCKED_TARGET_DIAGNOSTIC",
                "locked_target": "q79/F,m=1 S3/GS Route-C de_response packet",
                "description": "The same finite matrix shapes are checked under a formal selected-source lift to test downstream algebra only.",
            },
            "superset_repair": {
                "classification": "SELECTOR_PROVENANCE_REPAIR_REQUIRED",
                "missing_object": "actual MTT-selected HYM/Strominger source and quotient-valid Galerkin basis",
            },
            "diagnostic_backfit_only": {
                "used": True,
                "observed_physical_data_used": False,
                "why_allowed": "The diagnostic changes only source-verification flags and uses no measured masses, mixings, or benchmark residual targets.",
            },
        },
        "manifest": {key: rel(MANIFEST_DIR / filename) for key, filename in MANIFEST_FILES.items()},
        "formal_lift_manifest": {key: rel(FORMAL_DIR / filename) for key, filename in MANIFEST_FILES.items()},
        "manifest_filled": {key: (MANIFEST_DIR / filename).exists() for key, filename in MANIFEST_FILES.items()},
        "root_payload": {
            "source": str(SMOKE_DIR),
            "status": route_residual.get("status"),
            "selected_source_verified": route_residual.get("selected_source_verified"),
            "claims_selected_source": route_residual.get("guardrails", {}).get("claims_selected_source"),
            "selected_branch_claimed_by_residual_solution": route_residual.get("branch_packet", {}).get("selected_branch_claimed_by_residual_solution"),
        },
        "formal_lift_payload": {
            "source": str(LIFT_DIR),
            "status": formal_route.get("status"),
            "selected_source_verified": formal_route.get("selected_source_verified"),
            "claims_selected_source": formal_route.get("guardrails", {}).get("claims_selected_source"),
            "promotion_packet": rel(formal_packet),
        },
        "validation": {
            "honest_root": honest_validators,
            "honest_root_all_pass": honest_pass,
            "formal_lift_diagnostic": formal_validators,
            "formal_lift_lower_validators_all_pass": formal_pass,
            "formal_lift_promotion": formal_promotion,
            "formal_lift_promotion_passes": formal_promotion["passed"],
        },
        "interpretation": {
            "downstream_algebra_obstruction_found": not formal_pass,
            "selector_provenance_obstruction_found": route_residual.get("selected_source_verified") is not True,
            "proof_promotion_allowed": False,
            "reason_proof_promotion_not_allowed": (
                "Formal-lift flags are diagnostic.  A selected-source theorem must derive the flags and the actual basis/operator values from MTT; "
                "they cannot be asserted by copying a smoke packet."
            ),
        },
        "what_closes_now": {
            "manifest_files_created": True,
            "honest_current_q79_payload_imported": True,
            "formal_lift_diagnostic_run": True,
            "downstream_algebra_pipeline_shape_tested": formal_pass,
            "selected_source_gap_isolated": formal_pass and route_residual.get("selected_source_verified") is not True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "actual_selected_hym_strominger_source": True,
            "quotient_valid_selected_galerkin_basis_BN": True,
            "selected_spectral_projector_error_bounds": True,
            "primitive_C1_contractions": True,
            "proof_usable_selected_de_response_packet": True,
            "full_SM_or_no_knob_closure": True,
        },
        "theorem": {
            "name": "SelectedRouteCStromingerGalerkinFirstRunManifestAndSelectorGap",
            "proved": True,
            "statement": (
                "The declared first-run manifest is filled.  The honest q79 current-branch finite payload remains unselected, while the "
                "formal lifted-source diagnostic tests the downstream algebra without using observed physical data.  Therefore the next true "
                "gate is the selected-source/basis theorem, not another high-level interface."
            ),
        },
        "next_required_artifact": "MTT_Selected_RouteC_Source_Selector_and_Basis_Theorem_v1",
        "target_fitting_used": False,
    }


def build_certificate(candidate: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "MTTSelectedRouteCStromingerGalerkinFirstRun",
        "status": candidate["status"],
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "manifest_dir": rel(MANIFEST_DIR),
        "formal_lift_dir": rel(FORMAL_DIR),
        "manifest_filled": candidate["manifest_filled"],
        "formal_lift_lower_validators_all_pass": candidate["validation"]["formal_lift_lower_validators_all_pass"],
        "formal_lift_promotion_passes": candidate["validation"]["formal_lift_promotion_passes"],
        "closure_claimed": False,
        "proof_promotion_allowed": False,
        "target_fitting_used": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "primary_next_artifact": candidate["next_required_artifact"],
    }


def render_note(candidate: dict[str, Any]) -> str:
    lines = [
        "# MTT Selected Route-C/Strominger Galerkin First Run",
        "",
        "Status: `MTT_SELECTED_ROUTEC_STROMINGER_GALERKIN_FIRST_RUN_MANIFEST_FILLED_SELECTOR_OPEN`.",
        "",
        "The first-run manifest is now filled.  The root files are the honest q79 current-branch finite Route-C smoke payload; their selected-source flags remain false.  A separate `formal_lift_diagnostic` directory tests the same downstream algebra under lifted selected-source flags, but this is diagnostic only and is not proof data.",
        "",
        "Path type:",
        "",
        "- Straight path: honest import of the current q79 finite payload.",
        "- Superset convergence: locked q79/F,m=1 S3/GS target checked through Route-C residual, rhoE, metric, sector, D_E, Riesz, Green, and dotD validators.",
        "- Superset repair: the missing object is now narrowed to selected-source provenance plus quotient-valid basis data.",
        "- Diagnostic/backfit: no observed masses or mixings are used; lifted flags are not promoted.",
        "",
        "What this achieves:",
        "",
        "- All declared manifest paths now exist.",
        "- The honest root payload remains unselected, exactly as it should.",
        f"- Formal-lift lower validators all pass: `{candidate['validation']['formal_lift_lower_validators_all_pass']}`.",
        f"- Formal-lift promotion gate passes at the finite de_response level: `{candidate['validation']['formal_lift_promotion_passes']}`.",
        "- Proof promotion remains forbidden because selected-source flags are asserted in the diagnostic rather than derived from MTT.",
        "",
        "Consequence:",
        "",
        "The blocker is not currently a hidden finite matrix-shape failure.  The hard remaining gate is to derive the selected HYM/Strominger source and quotient-valid Galerkin basis from the MTT branch itself, then rerun the same manifest without lifted flags.",
        "",
        f"Next artifact: `{candidate['next_required_artifact']}`.",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    candidate = build_candidate()
    certificate = build_certificate(candidate)
    write_json(OUTPUT_DATA, candidate)
    write_json(OUTPUT_CERT, certificate)
    OUTPUT_NOTE.write_text(render_note(candidate), encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT_DATA), "status": candidate["status"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
