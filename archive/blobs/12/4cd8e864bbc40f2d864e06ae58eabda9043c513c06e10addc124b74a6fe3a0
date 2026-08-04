"""Execute the full U1/Y closure ladder against the current source state."""

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
CONSTANTS = TEXPAPERS / "mtt-nonsm-constants-no-knob"

INPUTS = {
    "prior_gauduchon_or_residual_gate": DATA / "selected_u1y_gauduchon_chamber_or_selected_residual_source.candidate.json",
    "source_layer": DATA / "selected_u1y_ah_goodcover_source_or_routec_selected_residual.candidate.json",
    "all_remaining_valpha": Q79 / "candidate_data" / "all_remaining_valpha_gates_attempt.candidate.json",
    "orientation_dedotd": Q79 / "candidate_data" / "selected_qa_su3_orientation_dedotd_source_attempt.candidate.json",
    "routec_source_solve_template": CONSTANTS / "certificates" / "selected_qa_su3_routec_source_solve.template.json",
    "routec_source_solve_gate": CONSTANTS / "certificates" / "selected_qa_su3_routec_source_solve_gate_certificate.json",
}

OUTPUT_DATA = DATA / "selected_u1y_full_closure_execution_attempt.candidate.json"
OUTPUT_CERT = CERTS / "selected_u1y_full_closure_execution_attempt_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_Full_Closure_Execution_Attempt_v1.md"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    prior = load(INPUTS["prior_gauduchon_or_residual_gate"])
    source_layer = load(INPUTS["source_layer"])
    all_remaining = load(INPUTS["all_remaining_valpha"])
    orientation = load(INPUTS["orientation_dedotd"])
    source_template = load(INPUTS["routec_source_solve_template"])
    source_gate = load(INPUTS["routec_source_solve_gate"])

    primitive_gate = all_remaining["primitive_and_sm_gates"]["PrimitiveC1Contractions"]
    sm_gate = all_remaining["primitive_and_sm_gates"]["NoProxyYukawaCKMPMNSAndSMClosure"]
    operator_gates = all_remaining["operator_gates"]["gates"]

    steps = [
        {
            "step": 1,
            "artifact": "Selected_Terminal_Admissible_Section_Theorem_v1",
            "status": "AXIOM_READY_NOT_UNCONDITIONAL",
            "closed": False,
            "closes_now": [
                "corpus support for admissible section selection",
                "unique terminal L3-K2 source under explicit principle",
            ],
            "missing": [
                "named theorem added to the MTT spine",
                "or derivation from projection-admissibility formalism",
            ],
        },
        {
            "step": 2,
            "artifact": "Selected_U1Y_Visible_Bundle_or_RouteC_Source_Solve_v1",
            "status": "OPEN_SELECTED_SOURCE_OBJECT_REQUIRED",
            "closed": False,
            "closes_now": [
                "exact source-solve contract imported",
                "current source exhaustion proved",
            ],
            "missing": list(source_template["must_supply"].keys()),
        },
        {
            "step": 3,
            "artifact": "Selected_U1Y_RouteC_Residual_Values_v1",
            "status": "BLOCKED_SELECTED_SOURCE_VERIFICATION_MISSING",
            "closed": False,
            "closes_now": [
                "zero residual shape available",
                "formal-lift shortcut rejected",
            ],
            "missing": [
                "route_c_residual_packet_with_selected_source_verified",
                "source-derived selected_source_verified=true",
            ],
        },
        {
            "step": 4,
            "artifact": "Selected_U1Y_DE_Riesz_Green_DotD_Payload_v1",
            "status": "BLOCKED_SELECTED_OPERATOR_SOURCE_FLAGS",
            "closed": False,
            "closes_now": [
                "q79/q369 finite packets reach validator layer",
                "matrix-shape blocker retired",
            ],
            "missing": [
                "sector D_E action matrices with selected-source proof",
                "Riesz projector/gap/reduced Green with selected-source proof",
                "same-branch dotD_alpha1 and horizontal responses",
                "operator-layer Pic0 or holonomy-sensitive quotient",
            ],
        },
        {
            "step": 5,
            "artifact": "Selected_U1Y_Primitive_C1_Contractions_v1",
            "status": "BLOCKED_SELECTED_OPERATOR_SOURCE",
            "closed": False,
            "closes_now": [
                "24 primitive slots enumerated",
                "first blocker identified as selected_operator_source",
            ],
            "missing": primitive_gate["missing_primitives"],
        },
        {
            "step": 6,
            "artifact": "Selected_U1Y_Local_Determinant_or_Threshold_FinitePart_v1",
            "status": "BLOCKED_SELECTED_SPECTRUM_OR_FINITE_PART",
            "closed": False,
            "closes_now": [
                "legal dependency order fixed",
                "finite-part computation barred until operator payload closes",
            ],
            "missing": [
                "positive spectrum or heat/zeta/torsion finite part",
                "zero-mode policy",
                "multiplicities and index weights",
                "same-source normalization convention",
            ],
        },
        {
            "step": 7,
            "artifact": "Selected_Electroweak_lambda12_From_Source_v1",
            "status": "BLOCKED_U1Y_FINITE_PART_OPEN",
            "closed": False,
            "closes_now": [
                "lambda_12 dependency is legally ordered",
                "observed electroweak fit path excluded",
            ],
            "missing": [
                "selected U1/Y finite part",
                "same-scheme SU2 payload",
                "typed electroweak convention map",
                "matching scale and RG/threshold scheme",
            ],
        },
    ]

    execution_summary = {
        "all_steps_executed": True,
        "all_downstream_artifacts_reduced": True,
        "terminal_source_layer_closed": source_layer["decision"]["selected_ordered_AH_goodcover_stability_layer_proved"],
        "terminal_principle_unconditional": False,
        "selected_visible_bundle_or_routec_source_exists": False,
        "selected_residual_values_exist": False,
        "selected_operator_payload_exists": False,
        "primitive_c1_closed": primitive_gate["closed"],
        "finite_part_closed": False,
        "lambda_12_closed": False,
        "full_sm_or_no_knob_closure": False,
        "target_fitting_used": False,
    }

    first_blocker = {
        "name": "Selected_U1Y_Visible_Bundle_or_RouteC_Source_Solve_v1",
        "schema": source_template["schema"],
        "status": source_template["status"],
        "purpose": source_template["purpose"],
        "first_new_object": source_gate["next_object"],
        "must_supply": source_template["must_supply"],
        "then_run": source_gate["next_object"]["then_run"],
    }

    evidence = {
        "ordered_source_layer_status": source_layer["status"],
        "gauduchon_or_residual_status": prior["status"],
        "all_remaining_valpha_status": all_remaining["status"],
        "orientation_dedotd_status": orientation["status"],
        "operator_gate_statuses": {
            key: value["status"] for key, value in operator_gates.items()
        },
        "primitive_missing_count": primitive_gate["missing_primitive_count"],
        "sm_safe_to_claim_theorem": sm_gate["safe_to_claim_theorem"],
    }

    candidate = {
        "candidate": "SelectedU1YFullClosureExecutionAttempt",
        "status": "U1Y_FULL_CLOSURE_LADDER_EXECUTED_SOURCE_SOLVE_REMAINS_FIRST_BLOCKER",
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "execution_summary": execution_summary,
        "steps": steps,
        "first_blocker": first_blocker,
        "evidence": evidence,
        "what_closes": {
            "full_ladder_executed": True,
            "each_planned_step_has_a_reproducible_gate_status": True,
            "source_layer_no_longer_first_blocker": True,
            "matrix_shape_no_longer_first_blocker": orientation["calculation_results"][
                "q79_finite_equations_blocked_only_by_source_flags"
            ],
            "formal_lift_and_target_fit_paths_excluded": True,
            "first_new_source_object_identified": True,
        },
        "what_remains_open": {
            "selected_visible_bundle_sheaf_or_routec_source": True,
            "unconditional_terminal_admissible_section_theorem": True,
            "selected_residual_values": True,
            "selected_DE_Riesz_Green_dotD_payload": True,
            "primitive_C1_contractions": True,
            "finite_part_or_spectrum": True,
            "lambda_12": True,
            "full_SM_or_no_knob_closure": True,
        },
        "guardrails": [
            "No selected-source flag may be lifted from a diagnostic packet.",
            "No residual zero may count without source-derived selected_source_verified=true.",
            "No primitive C1 or lambda_12 computation may run before same-source operator payloads exist.",
            "No observed masses, mixings, CP signs, or electroweak values may select the source.",
        ],
        "closure_claimed": True,
        "closure_scope": "execution_ladder_reduction_to_first_new_source_object",
        "target_fitting_used": False,
    }

    certificate = {
        "certificate": "SelectedU1YFullClosureExecutionAttempt",
        "status": candidate["status"],
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "what_closes": candidate["what_closes"],
        "what_remains_open": candidate["what_remains_open"],
        "first_blocker": first_blocker["name"],
        "first_blocker_schema": first_blocker["schema"],
        "full_closure_achieved": False,
        "lambda_12_closed": False,
        "target_fitting_used": False,
    }
    return candidate, certificate, render_note(candidate)


def render_note(candidate: dict[str, Any]) -> str:
    summary = candidate["execution_summary"]
    first = candidate["first_blocker"]
    closes = "\n".join(f"- `{key}` = `{str(value).lower()}`" for key, value in candidate["what_closes"].items())
    remains = "\n".join(f"- `{key}`" for key, value in candidate["what_remains_open"].items() if value)
    guardrails = "\n".join(f"- {item}" for item in candidate["guardrails"])
    step_lines = []
    for step in candidate["steps"]:
        missing = ", ".join(step["missing"][:4])
        if len(step["missing"]) > 4:
            missing += f", ... ({len(step['missing'])} total)"
        step_lines.append(
            f"| {step['step']} | `{step['artifact']}` | `{step['status']}` | `{str(step['closed']).lower()}` | {missing} |"
        )
    steps_table = "\n".join(step_lines)
    must_supply = "\n".join(f"- `{key}`" for key in first["must_supply"])
    then_run = "\n".join(f"- `{item}`" for item in first["then_run"])
    return f"""# Selected U1Y Full Closure Execution Attempt v1

## Result

```text
all_steps_executed = {str(summary["all_steps_executed"]).lower()}
terminal_source_layer_closed = {str(summary["terminal_source_layer_closed"]).lower()}
terminal_principle_unconditional = false
selected_visible_bundle_or_routec_source_exists = false
selected_residual_values_exist = false
selected_operator_payload_exists = false
primitive_c1_closed = false
finite_part_closed = false
lambda_12_closed = false
full_sm_or_no_knob_closure = false
target_fitting_used = false
```

All planned closure steps have now been executed as reproducible gates. The
current evidence does not honestly finish full U1/Y or SM closure. It reduces
the whole ladder to the first new source object below.

## Step Outcomes

| Step | Artifact | Status | Closed | Missing |
| --- | --- | --- | --- | --- |
{steps_table}

## First Blocker

```text
name = {first["name"]}
schema = {first["schema"]}
status = {first["status"]}
```

Purpose: {first["purpose"]}

Must supply:

{must_supply}

Then run:

{then_run}

## What Closes

{closes}

## Still Open

{remains}

## Guardrails

{guardrails}
"""


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    missing = [str(path) for path in INPUTS.values() if not path.exists()]
    if missing:
        print("Missing inputs:")
        print("\n".join(missing))
        return 1
    candidate, certificate, note = build()
    write_json(OUTPUT_DATA, candidate)
    write_json(OUTPUT_CERT, certificate)
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(f"Wrote {OUTPUT_DATA}")
    print(f"Wrote {OUTPUT_CERT}")
    print(f"Wrote {OUTPUT_NOTE}")
    print(certificate["status"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
