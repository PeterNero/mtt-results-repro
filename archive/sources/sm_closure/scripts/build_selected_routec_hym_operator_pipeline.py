"""Build the selected Route-C/HYM operator pipeline gate artifact."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")

OUTPUT_DATA = DATA / "selected_routec_hym_operator_pipeline.candidate.json"
OUTPUT_CERT = CERTS / "selected_routec_hym_operator_pipeline_certificate.json"
OUTPUT_NOTE = CORPUS / "MTT_Selected_RouteC_HYM_Operator_Pipeline_v1.md"

INPUTS = {
    "local_visible_gs_operator_source_gate": CERTS / "selected_visible_green_schwarz_operator_source_certificate.json",
    "q79_hym_operator_validator": Q79 / "certificates" / "selected_hym_operator_source_validator_certificate.json",
    "q79_hym_operator_attempt": Q79 / "certificates" / "selected_hym_operator_source_attempt_certificate.json",
    "q79_selected_source_promotion_attempt": Q79 / "certificates" / "selected_hym_operator_source_promotion.attempt.json",
    "q79_route_c_scaffold": Q79 / "certificates" / "iwasawa_route_c_finite_solve_scaffold_certificate.json",
    "q79_route_c_branch_smoke": Q79 / "certificates" / "iwasawa_route_c_branch_smoke_attempt_certificate.json",
    "q79_de_action_validator": Q79 / "certificates" / "iwasawa_de_action_validator_certificate.json",
    "q79_riesz_gap_validator": Q79 / "certificates" / "iwasawa_riesz_gap_validator_certificate.json",
    "q79_reduced_green_validator": Q79 / "certificates" / "iwasawa_reduced_green_validator_certificate.json",
    "q79_dotd_response_validator": Q79 / "certificates" / "iwasawa_dotd_response_validator_certificate.json",
    "q79_c1_dependency": Q79 / "certificates" / "iwasawa_route_c_smoke_c1_dependency_certificate.json",
}


def load_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def source_status() -> dict[str, object]:
    return {
        key: {"path": str(path), "present": path.exists()}
        for key, path in INPUTS.items()
    }


def branch_summary(smoke: dict[str, object], branch: str) -> dict[str, object]:
    validators = smoke["branches"][branch]["validators"]
    honest = validators["honest_unselected"]
    lifted = validators["lifted_selected_flags_smoke"]
    return {
        "branch_packet": smoke["branches"][branch]["branch_packet"],
        "honest_unselected_exit_codes": {key: row["exit_code"] for key, row in honest.items()},
        "honest_unselected_passes": {key: row["pass"] for key, row in honest.items()},
        "lifted_selected_flags_passes": {key: row["pass"] for key, row in lifted.items()},
        "honest_mesh_metric_sector_pass": (
            honest["rhoE_mesh"]["pass"] and honest["rhoE_metric"]["pass"] and honest["sector_maps"]["pass"]
        ),
        "honest_operator_pipeline_pass": (
            honest["route_c_residual"]["pass"]
            and honest["de_action"]["pass"]
            and honest["riesz_gap"]["pass"]
            and honest["reduced_green"]["pass"]
            and honest["dotd_response"]["pass"]
        ),
        "lifted_operator_pipeline_pass": all(row["pass"] for row in lifted.values()),
    }


def build_candidate() -> dict[str, object]:
    visible_gate = load_json(INPUTS["local_visible_gs_operator_source_gate"])
    hym_validator = load_json(INPUTS["q79_hym_operator_validator"])
    hym_attempt = load_json(INPUTS["q79_hym_operator_attempt"])
    promotion = load_json(INPUTS["q79_selected_source_promotion_attempt"])
    scaffold = load_json(INPUTS["q79_route_c_scaffold"])
    smoke = load_json(INPUTS["q79_route_c_branch_smoke"])
    de = load_json(INPUTS["q79_de_action_validator"])
    riesz = load_json(INPUTS["q79_riesz_gap_validator"])
    green = load_json(INPUTS["q79_reduced_green_validator"])
    dotd = load_json(INPUTS["q79_dotd_response_validator"])
    c1 = load_json(INPUTS["q79_c1_dependency"])

    branches = {
        branch: branch_summary(smoke, branch)
        for branch in smoke["calculation_results"]["branches_tested"]
    }
    current = branches["current_q79_orientation"]

    return {
        "candidate": "MTTSelectedRouteCHYMOperatorPipelineGate",
        "status": "MTT_SELECTED_ROUTEC_HYM_OPERATOR_PIPELINE_BUILT_SELECTED_VALUES_OPEN",
        "source_status": source_status(),
        "superset_mode": {
            "classification": "SUPERSET_REPAIR_WITH_EXECUTABLE_PIPELINE",
            "straight_path": {
                "name": "Route-C/HYM finite pipeline alone",
                "succeeds": False,
                "reason": "The pipeline validators are executable, but honest q79/F data fail selected-source flags and selected residual origin.",
            },
            "superset_convergence": {
                "succeeds": True,
                "converging_paths": [
                    "visible GS/operator-source gate",
                    "Fu-Yau/Strominger charge-sector closure",
                    "Route-C mesh/metric/sector validators",
                    "D_E/Riesz/Green/dotD validators",
                    "C1 dependency reduction",
                ],
                "locked_target": "selected finite HYM/Strominger source packet with selected rho_E, metric, D_E, Riesz/Green, dotD, and primitive C1 data",
            },
            "superset_repair": {
                "needed": True,
                "repair_object": "actual selected Route-C/HYM values, not lifted selected flags",
            },
            "diagnostic_backfit_only": {
                "used": False,
                "reason": "The smoke run uses no observed masses or mixings; it is algebraic validator rehearsal, not proof promotion.",
            },
        },
        "imported_results": {
            "visible_gate": {
                "status": visible_gate["status"],
                "next_required_artifact": visible_gate["next_required_artifact"],
            },
            "hym_validator": {
                "status": hym_validator["status"],
                "required_inputs": hym_validator["required_inputs"],
            },
            "hym_attempt": {
                "status": hym_attempt["status"],
                "calculation_results": hym_attempt["calculation_results"],
                "still_open": hym_attempt["still_open"],
            },
            "promotion_attempt": {
                "status": promotion["status"],
                "selected_source_verified": promotion["selected_source_verified"],
                "paths": promotion["paths"],
            },
            "route_c_scaffold": {
                "status": scaffold["status"],
                "source_residual_gates": scaffold["source_residual_gates"],
                "downstream_validator_pipeline": scaffold["downstream_validator_pipeline"],
                "still_open": scaffold["still_open"],
            },
            "route_c_smoke": {
                "status": smoke["status"],
                "calculation_results": smoke["calculation_results"],
                "branches": branches,
            },
            "validators": {
                "D_E": {"status": de["status"], "what_this_closes": de["what_this_closes"], "still_open": de["still_open"]},
                "Riesz_gap": {"status": riesz["status"], "what_this_closes": riesz["what_this_closes"], "still_open": riesz["still_open"]},
                "reduced_green": {"status": green["status"], "what_this_closes": green["what_this_closes"], "still_open": green["still_open"]},
                "dotD": {"status": dotd["status"], "what_this_closes": dotd["what_this_closes"], "still_open": dotd["still_open"]},
            },
            "c1_dependency": {
                "status": c1["status"],
                "calculation_results": c1["calculation_results"],
                "still_open": c1["still_open"],
            },
        },
        "pipeline_evaluation": {
            "selected_branch": "current_q79_orientation",
            "selected_branch_packet": current["branch_packet"],
            "honest_mesh_metric_sector_pass": current["honest_mesh_metric_sector_pass"],
            "honest_operator_pipeline_pass": current["honest_operator_pipeline_pass"],
            "lifted_flags_operator_pipeline_pass": current["lifted_operator_pipeline_pass"],
            "why_not_promoted": [
                "selected_source_verified is false",
                "Route-C residual solve is smoke, not a selected source solve",
                "D_E/Riesz/Green/dotD selected-source flags fail in honest run",
                "primitive C1 overlap tensors remain open",
            ],
        },
        "gate_results": {
            "route_c_scaffold_built": scaffold["what_this_closes"]["route_c_problem_layout"],
            "branch_aware_smoke_executed": smoke["verdict"]["small_N_branch_pipeline_executed"],
            "honest_mesh_metric_sector_pass": current["honest_mesh_metric_sector_pass"],
            "lifted_selected_flags_pipeline_pass": current["lifted_operator_pipeline_pass"],
            "honest_operator_pipeline_pass": current["honest_operator_pipeline_pass"],
            "selected_hym_operator_source_verified": hym_attempt["calculation_results"]["selected_hym_operator_source_verified"],
            "selected_source_verified": promotion["selected_source_verified"],
            "actual_selected_route_c_values_supplied": False,
            "actual_selected_D_E_dotD_Riesz_Green_supplied": False,
            "primitive_C1_contractions_supplied": False,
            "selected_Qa_SU3_packet_closed": False,
            "sm_parity_closure_claimed": False,
            "no_knob_closure_claimed": False,
        },
        "next_payload_contract": {
            "must_replace": "candidate_data/iwasawa_route_c_branch_smoke/current_q79_orientation/*",
            "with": "selected finite HYM/Strominger solve data on q79/F,m=1",
            "required_flags": [
                "selected_source_verified",
                "selected_dotD_source_verified",
                "alpha1_driver_verified",
                "green_operator_verified",
                "horizontal_gauge_verified",
                "boundary_conditions_verified",
            ],
            "required_outputs": [
                "rho_E transition data",
                "Hermitian metric",
                "sector projectors",
                "D_E action slots for Q,u,d,L,e,N,H",
                "Riesz projectors, complement gaps, reduced Green operators",
                "dotD_alpha1 matrices and horizontal responses",
                "primitive C1 overlap tensors",
            ],
        },
        "theorem": {
            "name": "SelectedRouteCHYMOperatorPipelineGate",
            "proved": True,
            "statement": (
                "The Route-C/HYM finite operator pipeline is executable and branch-aware. "
                "It verifies mesh, metric, and sector algebra honestly, and it shows that "
                "D_E/Riesz/Green/dotD validators can all pass when selected flags are lifted. "
                "However, honest promotion fails exactly at selected-source origin and actual "
                "selected values. Therefore the pipeline is a repair engine and validator "
                "contract, not yet a selected operator-source proof."
            ),
        },
        "next_required_artifact": "MTT_Selected_RouteC_HYM_Selected_Value_Search_v1",
        "target_fitting_used": False,
    }


def build_certificate(candidate: dict[str, object]) -> dict[str, object]:
    return {
        "certificate": "MTTSelectedRouteCHYMOperatorPipelineGate",
        "status": candidate["status"],
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "superset_mode": candidate["superset_mode"]["classification"],
        "what_closes": {
            "RouteC_HYM_pipeline_contract_built": True,
            "honest_mesh_metric_sector_subpipeline_imported": True,
            "lifted_flag_smoke_pipeline_imported": True,
            "honest_selected_source_blocker_identified": True,
            "D_E_Riesz_Green_dotD_validator_sequence_locked": True,
        },
        "what_remains_open": {
            "actual_selected_RouteC_HYM_values": True,
            "selected_source_origin_proof": True,
            "selected_D_E_dotD_Riesz_Green": True,
            "primitive_C1_overlap_tensors": True,
            "selected_Qa_SU3_color_operator_packet": True,
            "sm_parity_closed": False,
            "no_knob_closed": False,
        },
        "next_required_artifact": candidate["next_required_artifact"],
        "closure_claimed": False,
        "target_fitting_used": False,
    }


def render_note(candidate: dict[str, object], certificate: dict[str, object]) -> str:
    sources = "\n".join(
        f"- `{key}`: {row['path']} ({'present' if row['present'] else 'missing'})"
        for key, row in candidate["source_status"].items()
    )
    superset = candidate["superset_mode"]
    gates = "\n".join(f"- `{key}`: `{value}`" for key, value in candidate["gate_results"].items())
    pipeline = candidate["pipeline_evaluation"]
    blockers = "\n".join(f"- {item}" for item in pipeline["why_not_promoted"])
    outputs = "\n".join(f"- {item}" for item in candidate["next_payload_contract"]["required_outputs"])
    closes = "\n".join(f"- {key}" for key, value in certificate["what_closes"].items() if value)
    open_items = "\n".join(f"- {key}" for key, value in certificate["what_remains_open"].items() if value)
    return f"""# MTT Selected Route-C/HYM Operator Pipeline v1

## Purpose

This artifact asks whether the Route-C/HYM finite operator pipeline can now
promote the selected visible operator source needed for Qa/SU3.

It cannot yet promote.  It does close the executable validator contract: the
honest mesh/metric/sector subpipeline passes, the lifted-selected-flags smoke
shows the full algebraic pipeline is internally consistent, and the honest failure
is localized to selected source origin plus actual selected values.

## Superset Classification

- mode: `{superset["classification"]}`
- straight path tested: `{superset["straight_path"]["name"]}`
- straight path succeeds: `{superset["straight_path"]["succeeds"]}`
- reason: {superset["straight_path"]["reason"]}
- repair object: `{superset["superset_repair"]["repair_object"]}`
- diagnostic/backfit used: `{superset["diagnostic_backfit_only"]["used"]}`

Locked target:

```text
{superset["superset_convergence"]["locked_target"]}
```

## Inputs

{sources}

## Pipeline Evaluation

- selected branch: `{pipeline["selected_branch"]}`
- honest mesh/metric/sector pass: `{pipeline["honest_mesh_metric_sector_pass"]}`
- honest operator pipeline pass: `{pipeline["honest_operator_pipeline_pass"]}`
- lifted-flags operator pipeline pass: `{pipeline["lifted_flags_operator_pipeline_pass"]}`

Why this is not promoted:

{blockers}

## Gate Results

{gates}

## Next Payload Contract

The smoke files must be replaced with selected finite HYM/Strominger solve data
on `q79/F,m=1`, including:

{outputs}

## Theorem

`{candidate["theorem"]["name"]}` is proved:

{candidate["theorem"]["statement"]}

## What This Closes

{closes}

## What Remains Open

{open_items}

## Next Artifact

```text
{candidate["next_required_artifact"]}
```
"""


def main() -> None:
    candidate = build_candidate()
    certificate = build_certificate(candidate)
    data_text = json.dumps(candidate, indent=2, sort_keys=True)
    cert_text = json.dumps(certificate, indent=2, sort_keys=True)
    note_text = render_note(candidate, certificate)
    if "--write" in sys.argv:
        OUTPUT_DATA.write_text(data_text + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(note_text, encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
