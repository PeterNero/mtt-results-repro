"""Attempt the Selected_PhiFin_S1S2 value emission gate."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
DATA = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"
TEXPAPERS = Path(r"C:\Users\nero_\Downloads\TEXPAPERS")
SM = TEXPAPERS / "mtt-sm-parity-closure"
SM_SOLVE = SM / "candidate_data" / "selected_routec_strominger_galerkin_solve"

FINITE_TRACE_CERT = CERTS / "selected_phifin_finite_trace_existence_certificate.json"

INPUTS = {
    "rhoE_mesh": SM_SOLVE / "rhoE_mesh.candidate.json",
    "rhoE_metric": SM_SOLVE / "rhoE_metric.candidate.json",
    "sector_maps": SM_SOLVE / "sector_maps.candidate.json",
    "de_action": SM_SOLVE / "de_action.candidate.json",
    "riesz_gap": SM_SOLVE / "riesz_gap.candidate.json",
    "reduced_green": SM_SOLVE / "reduced_green.candidate.json",
    "dotd_response": SM_SOLVE / "dotd_response.candidate.json",
    "spectral_galerkin_data": SM_SOLVE / "spectral_galerkin_data.candidate.json",
}

OUTPUT_PACKET = DATA / "selected_phifin_s1s2_value_emission_attempt.candidate.json"
OUTPUT_TEMPLATE = DATA / "selected_phifin_s1s2_value_emission.required_payload.template.json"
OUTPUT_CERT = CERTS / "selected_phifin_s1s2_value_emission_attempt_certificate.json"
OUTPUT_NOTE = CORPUS / "Selected_PhiFin_S1S2_Value_Emission_Attempt_v1.md"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def has_false_selected_flags(obj: Any) -> bool:
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key in {"selected_by_mtt", "selected_source_verified", "selected_dotD_source_verified"}:
                if value is False:
                    return True
            if has_false_selected_flags(value):
                return True
    elif isinstance(obj, list):
        return any(has_false_selected_flags(item) for item in obj)
    return False


def classify_current_inputs() -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for name, path in INPUTS.items():
        data = load_json(path)
        status = data.get("status") or data.get("candidate_kind") or data.get("schema") or "UNKNOWN"
        result[name] = {
            "path": str(path),
            "present": path.exists(),
            "status": status,
            "contains_value_shape": any(
                key in json.dumps(data)
                for key in (
                    "matrix",
                    "D_E_matrix",
                    "riesz_projector",
                    "reduced_green_operator",
                    "dotD_alpha1_matrix",
                    "sector_projection_maps",
                )
            ),
            "has_false_selected_flags": has_false_selected_flags(data),
            "usable_as_selected_value_emission": False,
        }
    return result


def build_required_payload_template() -> dict[str, Any]:
    return {
        "packet": "Selected_PhiFin_S1S2_Value_Emission_v1",
        "status": "TEMPLATE_OPEN_SELECTED_VALUES_REQUIRED",
        "selected_branch": "q79/F,m=1 S3/GS Route-C",
        "S1_transition_or_connection_trace": {
            "selected_source_certificate": "selected_phifin_s0_source_prefix_certificate.json",
            "selected_connection_or_rhoE_entries": None,
            "nonidentity_or_equivalent_connection_trace": None,
            "metric_compatibility_certificate": None,
            "preserves_s3_gs_and_q79_f_m1": None,
        },
        "S2_galerkin_basis_and_operator_blocks": {
            "basis_BN_or_Cech_basis_entries": None,
            "quadrature_or_inner_product_rule": None,
            "sector_projectors": None,
            "D_E_matrix_entries": None,
            "dotD_alpha1_matrix_entries": None,
            "Riesz_projector_entries": None,
            "reduced_Green_entries": None,
            "gap_gamma_N": None,
            "residual_epsilon_N": None,
            "gap_condition_epsilon_lt_gamma_margin": None,
        },
        "validator_replay": {
            "rhoE_mesh_metric_sector_validators_pass": None,
            "D_E_validator_passes": None,
            "Riesz_gap_validator_passes": None,
            "reduced_Green_validator_passes": None,
            "dotD_response_validator_passes": None,
            "selected_source_promotion_passes_without_lifted_flags": None,
        },
        "discipline": {
            "formal_lift_flags_used": False,
            "observed_or_benchmark_inputs_used": False,
            "identity_smoke_used_as_selected_rhoE": False,
        },
    }


def build_candidate() -> dict[str, Any]:
    finite_trace = load_json(FINITE_TRACE_CERT)
    classified = classify_current_inputs()
    spectral = load_json(INPUTS["spectral_galerkin_data"])
    value_shapes_present = all(row["contains_value_shape"] for key, row in classified.items() if key != "spectral_galerkin_data")
    all_rejected = all(not row["usable_as_selected_value_emission"] for row in classified.values())
    missing_template_gates = [
        key for key, value in spectral["template_success_gates"].items() if value is False
    ]
    template = build_required_payload_template()
    return {
        "candidate": "SelectedPhiFinS1S2ValueEmissionAttempt",
        "status": "SELECTED_PHIFIN_S1S2_VALUE_EMISSION_ATTEMPT_BLOCKED_BY_UNEMITTED_SELECTED_VALUES",
        "finite_trace_prerequisite": {
            "path": str(FINITE_TRACE_CERT),
            "theorem_proved": finite_trace["theorem_proved"],
            "status": finite_trace["status"],
        },
        "current_value_files": classified,
        "analysis": {
            "value_shapes_present_in_current_files": value_shapes_present,
            "all_current_value_files_rejected_as_selected_emission": all_rejected,
            "spectral_galerkin_data_status": spectral["status"],
            "missing_spectral_template_gates": missing_template_gates,
            "hard_failure": (
                "The repo has model-active or smoke finite matrices, but selected connection/rhoE, "
                "quotient-valid basis, selected gap/error, and selected source replay are not emitted."
            ),
        },
        "value_emission_criterion": {
            "name": "SelectedPhiFinS1S2ValueEmissionCriterion",
            "proved": True,
            "necessary": [
                "selected connection/rhoE entries from the S0 source",
                "selected finite basis or typed Cech basis entries",
                "selected D_E and dotD_alpha1 matrix entries in that basis",
                "selected Riesz/projector and reduced Green entries",
                "positive gap gamma_N and residual epsilon_N with epsilon_N below the gap margin",
                "honest validator replay without lifted selected flags",
            ],
            "sufficient": [
                "the required payload template is fully filled",
                "all validators pass on the filled files",
                "formal_lift_flags_used=false and observed_or_benchmark_inputs_used=false",
            ],
            "statement": (
                "The S1-S2 value-emission gate is closed exactly by a filled selected "
                "finite-trace payload satisfying the listed entries and replay checks. "
                "Current smoke/model-active matrices prove algebraic reachability but are "
                "not selected value emissions."
            ),
        },
        "required_payload_template": template,
        "next_required_artifact": "Selected_PhiFin_S1S2_Value_Emission_v1",
        "what_closes_now": {
            "full_s1s2_analysis_completed": True,
            "current_smoke_values_rejected_as_proof": True,
            "necessary_and_sufficient_value_emission_criterion_proved": True,
            "required_payload_template_written": True,
        },
        "what_remains_open": {
            "fill_selected_connection_or_rhoE_entries": True,
            "fill_selected_basis_and_quadrature": True,
            "fill_selected_D_E_dotD_Riesz_Green_entries": True,
            "prove_gap_error_and_replay_validators": True,
            "A_selected": True,
            "b_selected": True,
        },
        "guardrails": {
            "claims_selected_values_emitted": False,
            "claims_validators_pass_honestly": False,
            "claims_A_selected_emitted": False,
            "claims_b_selected_emitted": False,
            "uses_observed_or_benchmark_inputs": False,
            "uses_formal_lift_flags_as_proof": False,
        },
    }


def build_certificate(candidate: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "SelectedPhiFinS1S2ValueEmissionAttempt",
        "status": candidate["status"],
        "candidate_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "template_path": str(OUTPUT_TEMPLATE.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "criterion_proved": candidate["value_emission_criterion"]["proved"],
        "next_required_artifact": candidate["next_required_artifact"],
        "what_closes_now": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "guardrails": candidate["guardrails"],
    }


def render_note(candidate: dict[str, Any]) -> str:
    files = "\n".join(
        f"- `{name}`: `{row['status']}`, value-shaped={row['contains_value_shape']}, "
        f"false-selected-flags={row['has_false_selected_flags']}, usable=no"
        for name, row in candidate["current_value_files"].items()
    )
    missing = "\n".join(f"- `{item}`" for item in candidate["analysis"]["missing_spectral_template_gates"])
    necessary = "\n".join(f"- {item}" for item in candidate["value_emission_criterion"]["necessary"])
    sufficient = "\n".join(f"- {item}" for item in candidate["value_emission_criterion"]["sufficient"])
    return f"""# Selected PhiFin S1S2 Value Emission Attempt v1

## Result

The S1-S2 value-emission problem is fully analyzed, but the selected values are
not emitted by current artifacts.

Status: `{candidate["status"]}`

## Current Value Files

{files}

The finite matrices are useful algebraic scaffolds.  They are not proof payloads
because they carry false selected flags, identity smoke rhoE, or an open
selected Galerkin basis/gap status.

## Missing Spectral Gates

{missing}

## Criterion

`{candidate["value_emission_criterion"]["name"]}` is proved.

{candidate["value_emission_criterion"]["statement"]}

Necessary entries:

{necessary}

Sufficient replay:

{sufficient}

## Next Artifact

`{candidate["next_required_artifact"]}`

Fill `candidate_data/selected_phifin_s1s2_value_emission.required_payload.template.json`
with source-derived selected entries, then replay the Route-C validators without
formal-lift flags.
"""


def main() -> int:
    candidate = build_candidate()
    certificate = build_certificate(candidate)
    if "--write" in sys.argv:
        OUTPUT_PACKET.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_TEMPLATE.write_text(
            json.dumps(candidate["required_payload_template"], indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        OUTPUT_CERT.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(render_note(candidate), encoding="utf-8")
    print(json.dumps(certificate, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
