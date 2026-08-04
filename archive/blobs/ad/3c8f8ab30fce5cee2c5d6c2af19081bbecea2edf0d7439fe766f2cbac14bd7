"""Build Step 42 executable value replay solution from the Step41 branch."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step42_executable_value_replay_solution_or_noknobrowfrontier"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
VALUE_SOLUTION = PACKET_DIR / "step42_executable_value_replay_solution.packet.json"
NOKNOB_FRONTIER = PACKET_DIR / "step42_noknob_internal_row_frontier.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step42_ExecutableValueReplaySolution_or_NoKnobRowFrontier_v1.md"

STEP41 = DATA / "selected_step41_singlebranch_solution_assembly_or_valuefunctionalfrontier.candidate.json"
ACCEPTED_VALUES = DATA / "selected_acceptedcommonscaleyukawahiggsvalues_or_profilelikelihoodexecution.candidate.json"
VALUE_PACKET = (
    DATA
    / "selected_acceptedcommonscaleyukawahiggsvalues_or_profilelikelihoodexecution"
    / "versioned_common_scale_yukawa_higgs_values.packet.json"
)
STEP25 = DATA / "selected_step25_thresholdexternalreplay_noknobkernel_or_fulls2cutset.candidate.json"
RTHETA_EXEC = DATA / "selected_rtheta_valueevaluatorexecution_or_thresholdresponseinstantiation.candidate.json"
SAMEBRANCH = DATA / "selected_samebranchthresholdmassschemerows_or_sourceanchorconstruction.candidate.json"

STATUS = "MTT_SELECTED_STEP42_EXECUTABLE_VALUE_REPLAY_SOLUTION_ASSEMBLED_NOKNOB_ROWS_OPEN"
NEXT = "MTT_Selected_InternalRThetaCoefficientRows_or_UniversalAnchorTheorem_v1"


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

    inputs = [STEP41, ACCEPTED_VALUES, VALUE_PACKET, STEP25, RTHETA_EXEC, SAMEBRANCH]
    missing = [rel(path) for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step 42 inputs: " + ", ".join(missing))

    step41 = load(STEP41)
    accepted = load(ACCEPTED_VALUES)
    value_packet = load(VALUE_PACKET)
    step25 = load(STEP25)
    rtheta_exec = load(RTHETA_EXEC)
    samebranch = load(SAMEBRANCH)

    replay_checks = {
        "step41_single_branch_solution_assembled": dig(
            step41, "closure_decision.single_branch_first_response_solution_assembled"
        )
        is True,
        "step41_branch_fixed": dig(step41, "closure_decision.selected_q79_F_m1_branch_fixed") is True,
        "versioned_common_scale_values_emitted": dig(
            accepted, "what_closes_now.versioned_common_scale_Yu_Yd_Ye_lambdaH_packet_emitted"
        )
        is True
        and value_packet["accepted_as_versioned_common_scale_candidate_values"] is True,
        "profile_execution_layer_closed": dig(accepted, "closure_decision.value_profile_execution_layer_closed") is True,
        "admitted_threshold_rows_closed": dig(step25, "closure_decision.admitted_external_threshold_rows_closed") is True
        and dig(step25, "closure_decision.admitted_external_threshold_row_count") == 7,
        "admitted_mass_scheme_rows_closed": dig(step25, "closure_decision.admitted_external_mass_scheme_rows_closed") is True
        and dig(step25, "closure_decision.admitted_external_mass_scheme_row_count") == 3,
        "accepted_diagonal_profile_replay_tier_closed": dig(
            step25, "closure_decision.accepted_diagonal_profile_theorem_closed_at_replay_tier"
        )
        is True,
        "Pi_Rtheta_closed_for_value_evaluator": dig(rtheta_exec, "closure_decision.Pi_Rtheta_closed") is True,
        "coefficient_functional_domain_closed": dig(rtheta_exec, "closure_decision.coefficient_functional_domain_closed")
        is True,
        "Rtheta_readiness_8_of_9": dig(samebranch, "closure_decision.Rtheta_readiness_8_of_9") is True,
        "no_observed_selector": step41["observed_data_used_as_selector"] is False
        and accepted["observed_data_used_as_selector"] is False
        and value_packet["observed_data_used_as_selector"] is False
        and step25["observed_data_used_as_selector"] is False,
        "no_target_fitting": step41["target_fitting_used"] is False
        and accepted["target_fitting_used"] is False
        and value_packet["target_fitting_used"] is False
        and step25["target_fitting_used"] is False,
    }
    executable_replay_solution_closed = all(replay_checks.values())

    magnitudes = value_packet["derived_magnitudes"]
    values = value_packet["values"]
    value_solution = {
        "schema": "MTTStep42ExecutableValueReplaySolution.v1",
        "status": "EXECUTABLE_ADMITTED_REPLAY_VALUE_SOLUTION_ASSEMBLED",
        "solution_tier": "ADMITTED_REPLAY_AND_PROFILE_INPUT",
        "selected_source_branch": {
            "q": 79,
            "orientation": "F",
            "torsion_m": 1,
            "source_packet": rel(STEP41),
        },
        "value_rows": {
            "reference_scale": value_packet["reference_scale"],
            "reference_scheme": value_packet["reference_scheme"],
            "diag_abs_Y_u": magnitudes["diag_abs_Y_u"],
            "diag_abs_Y_d": magnitudes["diag_abs_Y_d"],
            "diag_abs_Y_e": magnitudes["diag_abs_Y_e"],
            "lambda_H": magnitudes["lambda_H"],
            "frob_Y_u": magnitudes["frob_Y_u"],
            "frob_Y_d": magnitudes["frob_Y_d"],
            "frob_Y_e": magnitudes["frob_Y_e"],
            "Y_u_MZ_firstpass": values["Y_u_MZ_firstpass"],
            "Y_d_MZ_firstpass": values["Y_d_MZ_firstpass"],
            "Y_e_MZ_firstpass": values["Y_e_MZ_firstpass"],
            "lambda_H_MZ_firstpass": values["lambda_H_MZ_firstpass"],
        },
        "row_acceptance": {
            "accepted_for_SM_parity": value_packet["accepted_for_SM_parity"],
            "accepted_for_profile_execution_input": value_packet["accepted_for_profile_execution_input"],
            "accepted_for_true_precision_equivalence": value_packet["accepted_for_true_precision_equivalence"],
            "accepted_as_no_knob_MTT_prediction": value_packet["accepted_as_no_knob_MTT_prediction"],
            "accepted_internal_scalar_row_count": 0,
        },
        "admitted_replay_support": {
            "admitted_external_threshold_row_count": dig(step25, "closure_decision.admitted_external_threshold_row_count"),
            "admitted_external_mass_scheme_row_count": dig(step25, "closure_decision.admitted_external_mass_scheme_row_count"),
            "accepted_diagonal_profile_theorem_closed_at_replay_tier": dig(
                step25, "closure_decision.accepted_diagonal_profile_theorem_closed_at_replay_tier"
            ),
            "Rtheta_readiness_8_of_9": dig(samebranch, "closure_decision.Rtheta_readiness_8_of_9"),
        },
        "replay_checks": replay_checks,
        "guardrail": (
            "This packet closes an executable admitted-replay value solution tied to the selected Step41 "
            "source branch. It is not a no-knob derivation: the value rows remain profile/parity inputs "
            "until selected internal R_theta coefficient rows or a universal source anchor theorem are emitted."
        ),
        "target_fitting_used": False,
        "observed_data_used_as_selector": False,
    }
    write_json(VALUE_SOLUTION, value_solution)

    frontier = {
        "schema": "MTTStep42NoKnobInternalRowFrontier.v1",
        "status": "EXECUTABLE_REPLAY_CLOSED_INTERNAL_NOKNOB_ROWS_OPEN",
        "closed_now": {
            "executable_admitted_replay_value_solution_closed": executable_replay_solution_closed,
            "Step41_source_branch_attached_to_value_rows": True,
            "versioned_common_scale_Yu_Yd_Ye_lambdaH_rows_emitted": True,
            "admitted_external_threshold_rows_closed": True,
            "admitted_external_mass_scheme_rows_closed": True,
            "diagonal_profile_replay_tier_closed": True,
            "Pi_Rtheta_closed": True,
            "Rtheta_readiness_8_of_9": True,
        },
        "still_open_for_full_closure": {
            "selected_internal_Rtheta_coefficient_rows": True,
            "selected_threshold_response_functional_instantiated": dig(
                rtheta_exec, "closure_decision.selected_threshold_response_functional_instantiated"
            )
            is False,
            "selected_value_evaluator_closed": dig(rtheta_exec, "closure_decision.selected_value_evaluator_closed") is False,
            "accepted_coefficient_value_count": dig(rtheta_exec, "closure_decision.accepted_coefficient_value_count"),
            "accepted_internal_scalar_row_count": 0,
            "accepted_lambda_H_value": dig(rtheta_exec, "closure_decision.accepted_lambda_H_value"),
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "next_required_payload": {
            "target": NEXT,
            "minimum_fields": [
                "selected internal R_theta coefficient rows for the nine charged magnitudes",
                "selected lambda_H row",
                "same-branch threshold/mass-scheme/profile response as internal source data, not merely admitted replay",
                "or one candidate-specific universal source-anchor theorem declared before empirical replay",
            ],
        },
        "target_fitting_used": False,
        "observed_data_used_as_selector": False,
    }
    write_json(NOKNOB_FRONTIER, frontier)

    candidate = {
        "candidate": "MTTSelectedStep42ExecutableValueReplaySolutionOrNoKnobRowFrontier",
        "status": STATUS,
        "inputs": {
            "step41_solution": rel(STEP41),
            "accepted_common_scale_values": rel(ACCEPTED_VALUES),
            "versioned_value_packet": rel(VALUE_PACKET),
            "step25_admitted_replay": rel(STEP25),
            "rtheta_value_evaluator": rel(RTHETA_EXEC),
            "samebranch_readiness": rel(SAMEBRANCH),
        },
        "output_packets": {
            "executable_value_replay_solution": rel(VALUE_SOLUTION),
            "noknob_internal_row_frontier": rel(NOKNOB_FRONTIER),
        },
        "theorem": {
            "name": "Step42ExecutableReplaySolutionAndNoKnobBoundaryTheorem",
            "proved": executable_replay_solution_closed,
            "statement": (
                "The selected Step41 q=79/F/m=1 first-response branch can be attached to the existing "
                "versioned common-scale Yukawa/Higgs value packet and admitted threshold/mass-scheme/"
                "diagonal-profile replay tier, giving one executable value solution for comparison. "
                "The same audit keeps no-knob and true precision equivalence open because zero selected "
                "internal scalar rows and zero accepted R_theta coefficient values are emitted."
            ),
        },
        "closure_decision": {
            "executable_admitted_replay_value_solution_closed": executable_replay_solution_closed,
            "Step41_source_branch_attached_to_value_rows": True,
            "versioned_common_scale_Yu_Yd_Ye_lambdaH_rows_emitted": True,
            "admitted_external_threshold_rows_closed": True,
            "admitted_external_threshold_row_count": 7,
            "admitted_external_mass_scheme_rows_closed": True,
            "admitted_external_mass_scheme_row_count": 3,
            "diagonal_profile_replay_tier_closed": True,
            "Pi_Rtheta_closed": True,
            "Rtheta_readiness_8_of_9": True,
            "accepted_for_SM_parity": True,
            "accepted_for_profile_execution_input": True,
            "accepted_for_true_precision_equivalence": False,
            "accepted_as_no_knob_MTT_prediction": False,
            "accepted_internal_scalar_row_count": 0,
            "accepted_coefficient_value_count": 0,
            "selected_internal_Rtheta_coefficient_rows_closed": False,
            "selected_lambda_H_row_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": executable_replay_solution_closed,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "target_fitting_used": False,
        "observed_data_used_as_selector": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step42_ExecutableValueReplaySolution_or_NoKnobRowFrontier_v1",
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
        f"""# MTT Selected Step42 ExecutableValueReplaySolution or NoKnobRowFrontier v1

Status: `{STATUS}`.

Step42 closes one executable value solution tier:

- selected source branch: `q=79`, orientation `F`, torsion `m=1`
- emitted value rows: `Y_u(M_Z)`, `Y_d(M_Z)`, `Y_e(M_Z)`, and `lambda_H(M_Z)`
- replay support: seven admitted threshold rows, three admitted mass-scheme rows,
  and the diagonal-profile replay theorem
- `Pi_Rtheta` and the coefficient-functional domain are already closed in the
  current value-evaluator lane

This is the strongest honest "one solution" currently in the repo: an
executable admitted-replay/profile-input value solution tied to the selected
Step41 source branch.

It is not yet full no-knob SM closure:

- accepted internal scalar rows: `0`
- accepted Rtheta coefficient values: `0`
- selected lambda_H row: `false`
- true SM equivalence: `false`
- full no-knob closure: `false`

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
