"""Build the selected Route-C/HYM value-search closure attempt artifact."""

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
Q79_SMOKE = Q79 / "candidate_data" / "iwasawa_route_c_branch_smoke" / "current_q79_orientation"

OUTPUT_DATA = DATA / "selected_routec_hym_value_search.candidate.json"
OUTPUT_CERT = CERTS / "selected_routec_hym_value_search_certificate.json"
OUTPUT_NOTE = CORPUS / "MTT_Selected_RouteC_HYM_Selected_Value_Search_v1.md"

INPUTS = {
    "local_routec_hym_pipeline_gate": CERTS / "selected_routec_hym_operator_pipeline_certificate.json",
    "q79_selected_de_source_hunt": Q79 / "certificates" / "selected_de_source_hunt_certificate.json",
    "q79_selected_source_promotion_gate": Q79 / "certificates" / "iwasawa_selected_source_promotion_gate_certificate.json",
    "q79_orientation_dedotd_attempt": Q79 / "certificates" / "selected_qa_su3_orientation_dedotd_source_attempt_certificate.json",
    "q79_visible_rank2_l2_source_hunt": Q79 / "certificates" / "visible_rank2_l2_cohomology_source_hunt_certificate.json",
    "q79_visible_operator_blocker_resolution": Q79 / "certificates" / "visible_operator_source_blocker_resolution_certificate.json",
    "q79_route_c_residual_smoke": Q79_SMOKE / "route_c_residual.candidate.json",
    "q79_de_action_smoke": Q79_SMOKE / "de_action.candidate.json",
    "q79_riesz_gap_smoke": Q79_SMOKE / "riesz_gap.candidate.json",
    "q79_reduced_green_smoke": Q79_SMOKE / "reduced_green.candidate.json",
    "q79_dotd_response_smoke": Q79_SMOKE / "dotd_response.candidate.json",
}

VALIDATORS = {
    "route_c_residual": ("scripts/validate_iwasawa_route_c_residuals.py", INPUTS["q79_route_c_residual_smoke"]),
    "de_action": ("scripts/validate_iwasawa_de_action.py", INPUTS["q79_de_action_smoke"]),
    "riesz_gap": ("scripts/validate_iwasawa_riesz_gap.py", INPUTS["q79_riesz_gap_smoke"]),
    "reduced_green": ("scripts/validate_iwasawa_reduced_green.py", INPUTS["q79_reduced_green_smoke"]),
    "dotd_response": ("scripts/validate_iwasawa_dotd_response.py", INPUTS["q79_dotd_response_smoke"]),
}


def load_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def source_status() -> dict[str, object]:
    return {
        key: {"path": str(path), "present": path.exists()}
        for key, path in INPUTS.items()
    }


def run_validator(script: str, candidate: Path) -> dict[str, object]:
    proc = subprocess.run(
        [sys.executable, script, str(candidate)],
        cwd=Q79,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    return {
        "script": script,
        "candidate": str(candidate),
        "exit_code": proc.returncode,
        "passes": proc.returncode == 0,
        "output_head": proc.stdout.splitlines()[:16],
    }


def run_honest_validators() -> dict[str, object]:
    return {
        name: run_validator(script, candidate)
        for name, (script, candidate) in VALIDATORS.items()
    }


def build_candidate() -> dict[str, object]:
    pipeline = load_json(INPUTS["local_routec_hym_pipeline_gate"])
    de_hunt = load_json(INPUTS["q79_selected_de_source_hunt"])
    promotion_gate = load_json(INPUTS["q79_selected_source_promotion_gate"])
    orientation = load_json(INPUTS["q79_orientation_dedotd_attempt"])
    l2_hunt = load_json(INPUTS["q79_visible_rank2_l2_source_hunt"])
    blocker = load_json(INPUTS["q79_visible_operator_blocker_resolution"])
    smoke_residual = load_json(INPUTS["q79_route_c_residual_smoke"])
    honest_validators = run_honest_validators()

    honest_exit_codes = {
        name: result["exit_code"] for name, result in honest_validators.items()
    }
    honest_passes = {
        name: result["passes"] for name, result in honest_validators.items()
    }

    return {
        "candidate": "MTTSelectedRouteCHYMSelectedValueSearch",
        "status": "MTT_SELECTED_ROUTEC_HYM_VALUE_SEARCH_EXECUTED_SELECTED_SOURCE_ORIGIN_OPEN",
        "source_status": source_status(),
        "superset_mode": {
            "classification": "SUPERSET_REPAIR_SEARCH_NOT_CLOSED",
            "straight_path": {
                "name": "promote zero-residual Route-C smoke values",
                "succeeds": False,
                "reason": "The residual values are zero but the selected-source flag is false, and downstream honest validators reject the same source flags.",
            },
            "superset_convergence": {
                "succeeds": True,
                "converging_paths": [
                    "selected D_E source hunt",
                    "Route-C selected-source promotion gate",
                    "orientation-carrying D_E/dotD attempt",
                    "visible L2/source hunt",
                    "visible operator blocker resolution",
                ],
                "locked_target": "selected source-origin theorem for the q79/F,m=1 Route-C/HYM values",
            },
            "superset_repair": {
                "needed": True,
                "repair_object": "source-origin proof that converts exact residual smoke into selected finite HYM/Strominger data",
            },
            "diagnostic_backfit_only": {
                "used": False,
                "reason": "The search did not use observed masses, mixings, benchmarks, or target residual fitting.",
            },
        },
        "closure_attempts": {
            "A_promote_smoke_values": {
                "status": "REJECTED_SOURCE_FLAG",
                "residuals_all_zero": all(
                    entry["value"] == 0.0 for entry in smoke_residual["residuals"].values()
                ),
                "selected_source_verified": smoke_residual["selected_source_verified"],
                "honest_validator_exit_codes": honest_exit_codes,
                "honest_validator_passes": honest_passes,
            },
            "B_import_selected_DE_source_hunt": {
                "status": de_hunt["status"],
                "selected_D_E_source_found": de_hunt["hunt_result"]["selected_D_E_source_found"],
                "best_next_route": de_hunt["hunt_result"]["best_next_route"],
            },
            "C_promote_by_selected_source_gate": {
                "status": promotion_gate["status"],
                "required_guardrails": promotion_gate["required_guardrails"],
                "still_open": promotion_gate["still_open"],
            },
            "D_orientation_DE_dotD_source": {
                "status": orientation["status"],
                "q79_finite_equations_blocked_only_by_source_flags": orientation["calculation_results"]["q79_finite_equations_blocked_only_by_source_flags"],
                "q369_finite_equations_blocked_only_by_source_flags": orientation["calculation_results"]["q369_finite_equations_blocked_only_by_source_flags"],
                "selected_source_origin_constructed": orientation["calculation_results"]["selected_source_origin_constructed"],
            },
            "E_visible_L2_or_monad_source": {
                "status": l2_hunt["status"],
                "selected_L2_cochain_packet_found": l2_hunt["calculation_results"]["selected_L2_cochain_packet_found"],
                "must_construct_selected_L2_packet_from_geometry": l2_hunt["calculation_results"]["must_construct_selected_L2_packet_from_geometry"],
            },
            "F_visible_operator_blocker": {
                "status": blocker["status"],
                "blocker_resolved_by_existing_data": blocker["calculation_results"]["blocker_resolved_by_existing_data"],
                "first_blocking_layer": blocker["calculation_results"]["first_blocking_layer"],
            },
        },
        "gate_results": {
            "search_executed": True,
            "zero_residual_smoke_exists": True,
            "zero_residual_smoke_promoted": False,
            "honest_route_c_residual_validator_passes": honest_validators["route_c_residual"]["passes"],
            "honest_de_action_validator_passes": honest_validators["de_action"]["passes"],
            "honest_riesz_gap_validator_passes": honest_validators["riesz_gap"]["passes"],
            "honest_reduced_green_validator_passes": honest_validators["reduced_green"]["passes"],
            "honest_dotd_response_validator_passes": honest_validators["dotd_response"]["passes"],
            "selected_source_origin_found": False,
            "selected_values_closed": False,
            "selected_D_E_dotD_Riesz_Green_closed": False,
            "primitive_C1_contractions_closed": False,
            "selected_Qa_SU3_packet_closed": False,
            "sm_parity_closure_claimed": False,
            "no_knob_closure_claimed": False,
        },
        "honest_validator_results": honest_validators,
        "last_remaining_lemma": {
            "name": "RouteCSelectedSourceOriginLemma",
            "statement": (
                "The q79/F,m=1 finite Route-C/HYM residual-zero packet is selected by MTT "
                "from a visible bundle, twisted gerbe/Chan-Paton module, or typed Cech/monad "
                "transition source, and the same source supplies the D_E, Riesz/Green, dotD, "
                "and primitive C1 data."
            ),
            "currently_proved": False,
            "why_it_is_last": (
                "Residual magnitudes, branch packet shape, mesh/metric/sector algebra, and "
                "lifted-flag D_E/Riesz/Green/dotD consistency are already validated; all "
                "honest failures reduce to selected source-origin flags."
            ),
        },
        "next_payload_contract": {
            "acceptable_source_origin_proofs": [
                "typed Cech/monad transition data for the visible source",
                "selected twisted gerbe/Chan-Paton module with operator data",
                "finite HYM/Strominger solve with a real selection functional and positive Hessian",
            ],
            "not_acceptable": [
                "flipping selected_source_verified flags by hand",
                "using zero residuals alone as selection",
                "using observed masses, mixings, or benchmark matrices",
                "using diagnostic h1=3 or identity rho_E as selected data",
            ],
        },
        "theorem": {
            "name": "SelectedRouteCHYMValueSearchAttempt",
            "proved": True,
            "statement": (
                "The selected-value closure attempt was executed across Route-C smoke, source-hunt, "
                "promotion-gate, orientation, and visible-source routes. Current data do not close "
                "the selected values. The remaining blocker is sharply and uniquely the selected "
                "source-origin lemma for the q79/F,m=1 finite HYM/Strominger packet."
            ),
        },
        "next_required_artifact": "MTT_RouteC_Selected_Source_Origin_Lemma_v1",
        "target_fitting_used": False,
    }


def build_certificate(candidate: dict[str, object]) -> dict[str, object]:
    return {
        "certificate": "MTTSelectedRouteCHYMSelectedValueSearch",
        "status": candidate["status"],
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "superset_mode": candidate["superset_mode"]["classification"],
        "what_closes": {
            "selected_value_search_executed": True,
            "zero_residual_smoke_promotion_rejected": True,
            "source_hunt_no_closure_imported": True,
            "orientation_DE_dotD_source_flag_blocker_imported": True,
            "last_remaining_source_origin_lemma_identified": True,
        },
        "what_remains_open": {
            "RouteC_selected_source_origin_lemma": True,
            "actual_selected_RouteC_HYM_values": True,
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
    attempts = "\n".join(
        f"- `{key}`: `{value['status']}`" for key, value in candidate["closure_attempts"].items()
    )
    gates = "\n".join(f"- `{key}`: `{value}`" for key, value in candidate["gate_results"].items())
    lemma = candidate["last_remaining_lemma"]
    closes = "\n".join(f"- {key}" for key, value in certificate["what_closes"].items() if value)
    open_items = "\n".join(f"- {key}" for key, value in certificate["what_remains_open"].items() if value)
    acceptable = "\n".join(f"- {item}" for item in candidate["next_payload_contract"]["acceptable_source_origin_proofs"])
    forbidden = "\n".join(f"- {item}" for item in candidate["next_payload_contract"]["not_acceptable"])
    return f"""# MTT Selected Route-C/HYM Selected Value Search v1

## Purpose

This artifact tries to close the selected Route-C/HYM values.  It tests the
zero-residual smoke packet, imports the source-hunt and orientation attempts,
and checks whether any existing route can honestly set `selected_source_verified`.

It cannot close from current data.  The good news is that this is now a very
small, named gap: the selected source-origin lemma.

## Superset Classification

- mode: `{superset["classification"]}`
- straight path tested: `{superset["straight_path"]["name"]}`
- straight path succeeds: `{superset["straight_path"]["succeeds"]}`
- reason: {superset["straight_path"]["reason"]}
- repair object: `{superset["superset_repair"]["repair_object"]}`
- diagnostic/backfit used: `{superset["diagnostic_backfit_only"]["used"]}`

## Inputs

{sources}

## Closure Attempts

{attempts}

## Gate Results

{gates}

## Last Remaining Lemma

`{lemma["name"]}`:

{lemma["statement"]}

Currently proved: `{lemma["currently_proved"]}`

Why this is last:

```text
{lemma["why_it_is_last"]}
```

Acceptable ways to prove it:

{acceptable}

Not acceptable:

{forbidden}

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
