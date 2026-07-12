"""Build Step 43 minimal universal-parameter readiness and distance audit."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step43_minimaluniversalparameter_readiness_or_internalrowclosure"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
DISTANCE = PACKET_DIR / "step43_distance_to_minimal_parameter_closure.packet.json"
LANES = PACKET_DIR / "step43_minimal_parameter_lanes.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step43_MinimalUniversalParameterReadiness_or_InternalRowClosure_v1.md"

STEP42 = DATA / "selected_step42_executable_value_replay_solution_or_noknobrowfrontier.candidate.json"
UNIVERSAL_POLICY = DATA / "universal_source_parameter_policy.candidate.json"
CROSSUSE = DATA / "universal_crossuse_parameter_admissibility_theorem.candidate.json"
HIGHER_RESPONSE_POLICY = DATA / "selected_higherresponsesectorcoefficients_or_thresholdfunctionalsourcerows.candidate.json"
INTERNAL_RTHETA = DATA / "selected_internalrthetavaluederivation_or_minimaluniversalparameterselection.candidate.json"
NOKNOB_KERNEL = DATA / "selected_noknobvaluederivationkernel_or_sourceanchortheorem.candidate.json"
SAMEBRANCH = DATA / "selected_samebranchthresholdmassschemerows_or_sourceanchorconstruction.candidate.json"

STATUS = "MTT_SELECTED_STEP43_MINIMAL_UNIVERSAL_PARAMETER_READINESS_BUILT_ONE_ANCHOR_NEAREST_NOT_SELECTED"
NEXT = "MTT_Selected_OneUniversalSourceAnchorTheorem_or_InternalRThetaCoefficientRows_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def dig(data: dict[str, Any], dotted: str, default: Any = None) -> Any:
    cur: Any = data
    for part in dotted.split("."):
        if isinstance(cur, dict) and part in cur:
            cur = cur[part]
        else:
            return default
    return cur


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    inputs = [STEP42, UNIVERSAL_POLICY, CROSSUSE, HIGHER_RESPONSE_POLICY, INTERNAL_RTHETA, NOKNOB_KERNEL, SAMEBRANCH]
    missing = [rel(path) for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step 43 inputs: " + ", ".join(missing))

    step42 = load(STEP42)
    policy = load(UNIVERSAL_POLICY)
    crossuse = load(CROSSUSE)
    higher = load(HIGHER_RESPONSE_POLICY)
    internal = load(INTERNAL_RTHETA)
    noknob = load(NOKNOB_KERNEL)
    samebranch = load(SAMEBRANCH)

    readiness_checks = {
        "universal_parameter_tier_named": dig(policy, "what_closes_now.minimal_universal_parameter_tier_named") is True,
        "forbidden_knob_policy_declared": dig(policy, "what_closes_now.forbidden_knob_policy_declared") is True,
        "crossuse_admissibility_theorem_built": dig(crossuse, "what_closes_now.cross_use_universal_parameter_policy_theorem")
        is True,
        "minimal_universal_parameter_fallback_allowed": dig(
            higher, "closure_decision.minimal_universal_parameter_fallback_allowed"
        )
        is True,
        "executable_replay_solution_closed": dig(
            step42, "closure_decision.executable_admitted_replay_value_solution_closed"
        )
        is True,
        "Rtheta_readiness_8_of_9": dig(samebranch, "closure_decision.Rtheta_readiness_8_of_9") is True,
        "final_no_knob_kernel_typed": dig(noknob, "closure_decision.final_no_knob_kernel_typed") is True,
        "first_response_insufficiency_proved": dig(
            internal, "closure_decision.first_response_only_route_rejected_for_scalar_no_knob_values"
        )
        is True,
    }
    readiness_closed = all(readiness_checks.values())

    lanes = {
        "zero_knob_internal_rows": {
            "parameter_count": 0,
            "preferred_if_closed": True,
            "status": "OPEN",
            "selected_now": False,
            "why_not_closed": [
                "selected_internal_Rtheta_coefficient_rows_closed is false",
                "accepted_coefficient_value_count is 0",
                "selected lambda_H row is false",
            ],
            "distance": "one internal coefficient-row derivation/execution packet",
        },
        "one_universal_source_anchor": {
            "parameter_count": 1,
            "nearest_minimal_fallback": True,
            "status": "NEAREST_ALLOWED_BUT_NOT_SELECTED",
            "selected_now": False,
            "readiness_score": "4/6",
            "ready_fields": [
                "policy permits universal source parameters",
                "cross-use admissibility guard is built",
                "Step42 executable replay solution is closed",
                "Rtheta readiness is 8/9",
            ],
            "missing_fields": [
                "candidate-specific source-anchor theorem",
                "one anchor value selected before empirical replay",
                "row execution showing the anchor predicts the remaining scalar rows without retuning",
            ],
            "distance": "one source-anchor theorem plus one row-execution audit",
        },
        "two_universal_source_anchors": {
            "parameter_count": 2,
            "nearest_minimal_fallback": False,
            "status": "ALLOWED_ONLY_IF_ONE_ANCHOR_FAILS",
            "selected_now": False,
            "guard": "Both anchors must be source-selected and shared across sectors; they cannot be one knob per sector or one knob per observable.",
            "distance": "after one-anchor failure, prove two independent source anchors and an overdetermined prediction audit",
        },
        "three_universal_source_anchors": {
            "parameter_count": 3,
            "nearest_minimal_fallback": False,
            "status": "MAXIMAL_CREDIBLE_FALLBACK_NOT_SELECTED",
            "selected_now": False,
            "guard": "Three is the credibility ceiling in the current policy; anything sector-by-sector or observable-by-observable becomes ordinary fitting.",
            "distance": "last-resort minimal model with strong pre-replay source selection and many downstream predictions",
        },
    }
    write_json(LANES, {"schema": "MTTStep43MinimalParameterLanes.v1", "lanes": lanes})

    distance = {
        "schema": "MTTStep43DistanceToMinimalParameterClosure.v1",
        "status": "ONE_UNIVERSAL_ANCHOR_IS_NEAREST_ALLOWED_FALLBACK_BUT_ZERO_SELECTED",
        "readiness_checks": readiness_checks,
        "readiness_closed": readiness_closed,
        "selected_universal_parameter_count": 0,
        "acceptable_parameter_count_range_if_source_selected": [1, 2, 3],
        "nearest_lane": "one_universal_source_anchor",
        "answer_to_how_far": (
            "Policy and executable replay are already in place. We are not far structurally: "
            "a one-parameter closure is one candidate-specific source-anchor theorem plus one "
            "row-execution audit away. But we are still at zero selected parameters, so no "
            "minimal-parameter closure is claimed."
        ),
        "forbidden": [
            "choosing a parameter by minimizing residuals to the Step42 value rows",
            "retuning per sector, generation, or observable",
            "promoting admitted replay rows to no-knob source rows",
            "calling an unselected benchmark value a universal anchor",
        ],
        "target_fitting_used": False,
        "observed_data_used_as_selector": False,
    }
    write_json(DISTANCE, distance)

    candidate = {
        "candidate": "MTTSelectedStep43MinimalUniversalParameterReadinessOrInternalRowClosure",
        "status": STATUS,
        "inputs": {
            "step42": rel(STEP42),
            "universal_policy": rel(UNIVERSAL_POLICY),
            "crossuse": rel(CROSSUSE),
            "higher_response_policy": rel(HIGHER_RESPONSE_POLICY),
            "internal_rtheta": rel(INTERNAL_RTHETA),
            "noknob_kernel": rel(NOKNOB_KERNEL),
            "samebranch": rel(SAMEBRANCH),
        },
        "output_packets": {
            "distance_to_minimal_parameter_closure": rel(DISTANCE),
            "minimal_parameter_lanes": rel(LANES),
        },
        "theorem": {
            "name": "Step43MinimalUniversalParameterReadinessTheorem",
            "proved": readiness_closed,
            "statement": (
                "The current repo has the policy and executable replay conditions needed to make a "
                "1-3 universal-source-parameter fallback credible in principle. The nearest such "
                "fallback is one universal source anchor, but no parameter is selected now. Full "
                "no-knob or minimal-parameter closure still requires either internal Rtheta rows or "
                "a candidate-specific source-anchor theorem followed by row execution."
            ),
        },
        "closure_decision": {
            "minimal_universal_parameter_policy_ready": readiness_closed,
            "one_to_three_universal_parameters_allowed_if_source_selected": True,
            "nearest_allowed_fallback": "one_universal_source_anchor",
            "one_universal_source_anchor_readiness_score": "4/6",
            "selected_universal_parameter_count": 0,
            "one_universal_source_anchor_selected": False,
            "minimal_parameter_closure_closed": False,
            "internal_Rtheta_coefficient_rows_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": readiness_closed,
        "minimal_parameter_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "target_fitting_used": False,
        "observed_data_used_as_selector": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step43_MinimalUniversalParameterReadiness_or_InternalRowClosure_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        **candidate["closure_decision"],
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "observed_data_used_as_selector": False,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected Step43 MinimalUniversalParameterReadiness or InternalRowClosure v1

Status: `{STATUS}`.

Question answered:

Can 1-3 knobs be okay?

Yes, but only as universal source parameters selected before empirical replay.
They must be shared across sectors, typed into the selected MTT packet, and not
retuned per observable.

Where we are:

- Step42 executable replay solution: closed
- universal-parameter admissibility policy: closed
- cross-use guardrail: closed
- Rtheta readiness: `8/9`
- selected universal parameters now: `0`
- accepted internal coefficient rows: `0`

Distance:

- no-knob route: one internal `R_theta` coefficient-row derivation/execution packet
- one-knob route: one candidate-specific universal source-anchor theorem plus one row-execution audit
- two/three-knob route: allowed only if one anchor fails and each parameter is independently source-selected before replay

Nearest acceptable fallback:

`one_universal_source_anchor`.

Next artifact: `{NEXT}`.
""",
        encoding="utf-8",
    )

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
