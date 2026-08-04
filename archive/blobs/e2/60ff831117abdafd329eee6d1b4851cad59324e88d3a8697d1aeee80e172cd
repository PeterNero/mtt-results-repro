"""Build the global true-SM/no-knob ledger after finite-replay Yukawa closure."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"
CERTS = ROOT / "certificates"

SLUG = "selected_truesmnoknobclosure_globalledger_or_remainingnonyukawarows"
OUT = DATA / f"{SLUG}.candidate.json"
PACKET_DIR = DATA / SLUG
LEDGER = PACKET_DIR / "global_true_sm_noknob_ledger.packet.json"
BLOCKERS = PACKET_DIR / "remaining_nonyukawa_blocker_matrix.packet.json"
PLAN = PACKET_DIR / "next_closure_plan_after_yukawa_finite_replay.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_TrueSMNoKnobClosure_GlobalLedger_or_RemainingNonYukawaRows_v1.md"

YUKAWA = DATA / "selected_finalyukawareplayresidualexactness_or_strictsmnoknobclosure.candidate.json"
YUKAWA_DECISION = (
    DATA
    / "selected_finalyukawareplayresidualexactness_or_strictsmnoknobclosure"
    / "strict_sm_noknob_closure_decision.packet.json"
)
MINIMAL = DATA / "selected_fullsmminimalparameterledger_or_strictpewsourcetheorem.candidate.json"
STRICT_PEW = DATA / "selected_strictpewsourcetheorem_or_smprecisionclosurecutset.candidate.json"
QCD = DATA / "selected_qcdthetapolicy_or_strictpewcountreduction.candidate.json"
NEUTRINO = DATA / "selected_neutrinomassmajoranapolicy_or_precisionprofiletable.candidate.json"
PRECISION = DATA / "selected_precisionprofiletable_or_truesmequivalenceaudit.candidate.json"
QASU3 = DATA / "selected_qasu3operatorpayload_or_strictpewprecisionexit.candidate.json"
THRESHOLD = DATA / "selected_thresholdresponsefunctionalderivation_or_profilelikelihoodacquisition.candidate.json"
LOCAL_QFT = DATA / "selected_localqftobservablerows_or_finaltruesmequivalencegap.candidate.json"

STATUS = "MTT_SELECTED_TRUESMNOKNOBCLOSURE_GLOBALLEDGER_BUILT_YUKAWA_FINITE_REPLAY_CLOSED_NONYUKAWA_OPEN"
NEXT = "MTT_Selected_StrictPEWDirectK_or_QaSU3Step10ValueExecution_v1"


def write_json(path: Path, obj: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def main() -> int:
    yukawa = load(YUKAWA)
    yukawa_decision = load(YUKAWA_DECISION)
    minimal = load(MINIMAL)
    strict_pew = load(STRICT_PEW)
    qcd = load(QCD)
    neutrino = load(NEUTRINO)
    precision = load(PRECISION)
    qasu3 = load(QASU3)
    threshold = load(THRESHOLD)
    local_qft = load(LOCAL_QFT)

    finite_yukawa_rows = yukawa_decision["source_row_counts"]["accepted_finite_replay_yukawa_magnitude_rows"]
    finite_tail_rows = yukawa_decision["source_row_counts"]["accepted_finite_tail_source_rows"]
    strict_phase_rows = yukawa_decision["source_row_counts"][
        "accepted_strict_phase_antisymmetry_scalar_source_rows"
    ]

    sectors = {
        "charged_yukawa_magnitudes": {
            "status": "CLOSED_FINITE_REPLAY_STANDARD",
            "accepted_rows": finite_yukawa_rows,
            "source_rows": strict_phase_rows + finite_tail_rows,
            "closed": yukawa_decision["acceptance"]["finite_replay_yukawa_exactness_closed"],
            "guardrail": "Finite projected replay exactness, not analytic zero residual.",
            "source": rel(YUKAWA),
        },
        "strict_P_EW_direct_K_H_lambda": {
            "status": "OPEN_ZERO_STRICT_ROWS",
            "accepted_rows": strict_pew["closure_decision"]["strict_P_EW_source_rows"],
            "direct_K_threshold_Omega_H_lambda_rows": strict_pew["closure_decision"][
                "direct_K_threshold_Omega_H_lambda_rows"
            ],
            "closed": strict_pew["closure_decision"]["strict_P_EW_source_theorem_closed"],
            "why_matters": "Would reduce the active ledger count by one and close the H/lambda strict source exit.",
            "source": rel(STRICT_PEW),
        },
        "qcd_theta": {
            "status": "POLICY_SLOT_ADMITTED_VALUE_OPEN",
            "accepted_rows": 0,
            "policy_closed": qcd["closure_decision"]["QCD_theta_bar_policy_closed"],
            "value_selected": qcd["closure_decision"]["theta_bar_value_selected_by_MTT"],
            "strong_CP_solved": qcd["closure_decision"]["strong_CP_problem_solved"],
            "closed": False,
            "source": rel(QCD),
        },
        "neutrino_absolute_majorana_dirac": {
            "status": "MINIMAL_OSCILLATION_POLICY_CLOSED_ABSOLUTE_VALUES_OPEN",
            "accepted_rows": 0,
            "minimal_PMNS_policy_closed": neutrino["closure_decision"][
                "minimal_PMNS_oscillation_policy_closed"
            ],
            "absolute_mass_closed": neutrino["closure_decision"]["absolute_neutrino_mass_closed"],
            "majorana_policy_selected": neutrino["closure_decision"]["Majorana_policy_selected"],
            "dirac_yukawa_magnitudes_closed": neutrino["closure_decision"][
                "Dirac_neutrino_yukawa_magnitudes_closed"
            ],
            "closed": False,
            "source": rel(NEUTRINO),
        },
        "precision_threshold_mass_scheme_profile": {
            "status": "POLICY_TABLE_BUILT_TRUE_EQUIVALENCE_ROWS_ZERO",
            "accepted_true_equivalence_rows": precision["closure_decision"]["accepted_true_equivalence_rows"],
            "threshold_mass_scheme_source_rows_closed": precision["closure_decision"][
                "threshold_mass_scheme_source_rows_closed"
            ],
            "full_covariance_profile_likelihood_closed": precision["closure_decision"][
                "full_covariance_profile_likelihood_closed"
            ],
            "selected_threshold_response_functional_instantiated": threshold["closure_decision"][
                "selected_threshold_response_functional_instantiated"
            ],
            "external_likelihood_workspace_acquired": threshold["closure_decision"][
                "external_likelihood_workspace_acquired"
            ],
            "closed": False,
            "source": rel(PRECISION),
        },
        "local_qft_precision_observables": {
            "status": "TREE_IDENTITY_TIER_CLOSED_PRECISION_VALUES_OPEN",
            "tree_tier_closed": local_qft["closure_decision"]["tree_QFT_identity_tier_closed"],
            "precision_values_closed": local_qft["closure_decision"][
                "precision_local_QFT_observable_values_closed"
            ],
            "closed": False,
            "source": rel(LOCAL_QFT),
        },
        "qasu3_dynamic_operator_payload": {
            "status": "SOURCE_SLOTS_CLOSED_STEP10_VALUES_OPEN",
            "operator_source_slots_closed": qasu3["closure_decision"]["operator_source_slots_closed"],
            "operator_source_slots_remaining": qasu3["closure_decision"]["operator_source_slots_remaining"],
            "actual_dynamic_QaSU3_operator_packet_closed": qasu3["closure_decision"][
                "actual_dynamic_QaSU3_operator_packet_closed"
            ],
            "selected_C1_response_closed": qasu3["closure_decision"]["selected_C1_response_closed"],
            "full_S2_value_emission_closed": qasu3["closure_decision"]["full_S2_value_emission_closed"],
            "closed": False,
            "source": rel(QASU3),
        },
    }

    remaining_hard_blockers = [
        key for key, value in sectors.items() if key != "charged_yukawa_magnitudes" and not value["closed"]
    ]
    global_closed = len(remaining_hard_blockers) == 0

    ledger = {
        "schema": "MTTGlobalTrueSMNoKnobLedgerAfterYukawaFiniteReplay.v1",
        "status": "YUKAWA_FINITE_REPLAY_CLOSED_NONYUKAWA_LEDGER_OPEN",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "baseline_minimal_parameter_context": {
            "pre_yukawa_update_minimal_ledger_closed": minimal["closure_decision"]["minimal_parameter_ledger_closed"],
            "non_neutrino_count_including_qcd_theta": qcd["closure_decision"][
                "non_neutrino_count_including_QCD_theta"
            ],
            "minimal_PMNS_count_including_qcd_theta": qcd["closure_decision"][
                "minimal_PMNS_count_including_QCD_theta"
            ],
            "dirac_massive_neutrino_count_including_qcd_theta": neutrino["closure_decision"][
                "Dirac_massive_neutrino_count_including_QCD_theta"
            ],
            "majorana_massive_neutrino_count_including_qcd_theta": neutrino["closure_decision"][
                "Majorana_massive_neutrino_count_including_QCD_theta"
            ],
        },
        "sector_status": sectors,
        "accepted_updated_rows": {
            "finite_replay_yukawa_magnitude_rows": finite_yukawa_rows,
            "strict_phase_antisymmetry_scalar_source_rows": strict_phase_rows,
            "finite_tail_source_rows": finite_tail_rows,
            "accepted_precision_true_equivalence_rows": precision["closure_decision"][
                "accepted_true_equivalence_rows"
            ],
            "strict_P_EW_source_rows": strict_pew["closure_decision"]["strict_P_EW_source_rows"],
        },
    }

    blockers = {
        "schema": "MTTRemainingNonYukawaBlockerMatrixAfterYukawaFiniteReplay.v1",
        "status": "NONYUKAWA_BLOCKERS_REMAIN_ORDERED",
        "remaining_hard_blockers": remaining_hard_blockers,
        "ordered_closure_targets": [
            {
                "order": 1,
                "id": "strict_P_EW_or_direct_K_H_lambda",
                "why_first": "It is the count-reduction and Higgs/lambda strict-source fork already named by the current frontier.",
                "current_rows": strict_pew["closure_decision"]["strict_P_EW_source_rows"],
                "next_artifact": "MTT_Selected_StrictPEWDirectK_or_QaSU3Step10ValueExecution_v1",
            },
            {
                "order": 2,
                "id": "QaSU3_Step10_dynamic_value_execution",
                "why_first": "Step8 source slots are closed and Step9 support is closed; actual value execution is the non-looping fork.",
                "operator_source_slots_closed": qasu3["closure_decision"]["operator_source_slots_closed"],
                "actual_dynamic_packet_closed": qasu3["closure_decision"][
                    "actual_dynamic_QaSU3_operator_packet_closed"
                ],
            },
            {
                "order": 3,
                "id": "precision_threshold_response_functional_or_external_workspace",
                "why_first": "True precision equivalence rows are still zero despite the policy table.",
                "accepted_true_equivalence_rows": precision["closure_decision"][
                    "accepted_true_equivalence_rows"
                ],
            },
            {
                "order": 4,
                "id": "neutrino_absolute_mass_and_majorana_or_dirac_completion",
                "why_first": "Minimal oscillation replay is closed, but absolute mass and Majorana/Dirac source policy are not.",
                "absolute_mass_closed": neutrino["closure_decision"]["absolute_neutrino_mass_closed"],
            },
            {
                "order": 5,
                "id": "QCD_theta_value_or_strong_CP_policy",
                "why_first": "Theta is admitted as a slot, but no MTT value or strong-CP solution is selected.",
                "theta_value_selected": qcd["closure_decision"]["theta_bar_value_selected_by_MTT"],
            },
            {
                "order": 6,
                "id": "local_QFT_precision_observables",
                "why_first": "Tree identities are closed; precision correlator/S-matrix/decay rows remain open.",
                "tree_tier_closed": local_qft["closure_decision"]["tree_QFT_identity_tier_closed"],
            },
        ],
        "global_true_sm_no_knob_closed": global_closed,
    }

    plan = {
        "schema": "MTTNextClosurePlanAfterYukawaFiniteReplay.v1",
        "status": "NEXT_TARGET_LOCKED_TO_STRICT_PEW_OR_QASU3_STEP10",
        "do_next": {
            "primary": "Try strict P_EW/direct K_H.lambda source execution and Qa/SU3 Step10 value execution in parallel as the same frontier fork.",
            "artifact": NEXT,
            "success_criteria": [
                "strict P_EW/direct-K row count becomes positive or Step10 emits actual dynamic Qa/SU3 operator values",
                "no observed SM precision values select source rows",
                "precision/profile rows remain separate unless a source-owned R_theta or accepted external workspace is supplied",
            ],
        },
        "do_not_repeat": [
            "Do not reopen Yukawa magnitude source rows unless challenging finite-replay exactness itself.",
            "Do not count minimal-parameter accounting as no-knob source derivation.",
            "Do not promote QCD theta, absolute neutrino mass, or precision profile values by policy alone.",
        ],
    }

    candidate = {
        "candidate": "MTTSelectedTrueSMNoKnobClosureGlobalLedgerOrRemainingNonYukawaRows",
        "status": STATUS,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {
            "final_yukawa_finite_replay": rel(YUKAWA),
            "final_yukawa_decision": rel(YUKAWA_DECISION),
            "minimal_parameter_ledger": rel(MINIMAL),
            "strict_pew_cutset": rel(STRICT_PEW),
            "qcd_theta_policy": rel(QCD),
            "neutrino_policy": rel(NEUTRINO),
            "precision_profile_table": rel(PRECISION),
            "qasu3_operator_payload": rel(QASU3),
            "threshold_response_functional": rel(THRESHOLD),
            "local_qft_observable_rows": rel(LOCAL_QFT),
        },
        "output_packets": {
            "global_true_sm_noknob_ledger": rel(LEDGER),
            "remaining_nonyukawa_blocker_matrix": rel(BLOCKERS),
            "next_closure_plan_after_yukawa_finite_replay": rel(PLAN),
        },
        "theorem": {
            "name": "GlobalTrueSMNoKnobLedgerAfterYukawaFiniteReplayTheorem",
            "proved": True,
            "statement": (
                "After the finite-replay Yukawa magnitude closure, the charged-Yukawa "
                "magnitude source layer is no longer a hard blocker at the current finite "
                "projected source standard. The global true-SM/no-knob ledger remains open "
                "exactly at non-Yukawa rows: strict P_EW/direct-K, Qa/SU3 Step10 value "
                "execution, precision/profile threshold rows, neutrino absolute/Majorana "
                "or Dirac completion, QCD theta value/strong-CP policy, and local-QFT "
                "precision observable rows."
            ),
        },
        "key_numbers": {
            "accepted_finite_replay_yukawa_magnitude_rows": finite_yukawa_rows,
            "accepted_finite_tail_source_rows": finite_tail_rows,
            "accepted_strict_phase_antisymmetry_scalar_source_rows": strict_phase_rows,
            "accepted_precision_true_equivalence_rows": precision["closure_decision"][
                "accepted_true_equivalence_rows"
            ],
            "strict_P_EW_source_rows": strict_pew["closure_decision"]["strict_P_EW_source_rows"],
            "remaining_hard_blocker_count": len(remaining_hard_blockers),
        },
        "closure_decision": {
            "yukawa_finite_replay_magnitudes_closed": True,
            "global_true_SM_no_knob_closure": global_closed,
            "true_SM_equivalence_closed": False,
            "remaining_non_yukawa_blockers_ordered": True,
        },
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_TrueSMNoKnobClosure_GlobalLedger_or_RemainingNonYukawaRows_v1",
        "status": STATUS,
        "candidate": rel(OUT),
        "yukawa_finite_replay_magnitudes_closed": True,
        "accepted_finite_replay_yukawa_magnitude_rows": finite_yukawa_rows,
        "remaining_hard_blocker_count": len(remaining_hard_blockers),
        "remaining_hard_blockers": remaining_hard_blockers,
        "global_true_SM_no_knob_closure": global_closed,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected TrueSMNoKnobClosure GlobalLedger or RemainingNonYukawaRows v1

Status: `{STATUS}`

## New Baseline

Yukawa magnitudes are now closed at the finite projected replay standard:

- finite-replay Yukawa magnitude rows: `{finite_yukawa_rows}`
- strict phase-antisymmetry scalar rows: `{strict_phase_rows}`
- finite tail source rows: `{finite_tail_rows}`

This retires Yukawa magnitudes as the current hard blocker unless the finite
replay standard itself is challenged.

## Remaining Hard Blockers

The global true-SM/no-knob ledger remains open at:

1. strict `P_EW` / direct `K_threshold.Omega_H.lambda`,
2. Qa/SU3 Step10 actual dynamic value execution,
3. precision threshold/profile/covariance rows,
4. neutrino absolute mass plus Dirac/Majorana completion,
5. QCD theta value or strong-CP source policy,
6. local-QFT precision observable rows.

Accepted true-equivalence precision rows remain
`{precision["closure_decision"]["accepted_true_equivalence_rows"]}`, and strict
`P_EW` source rows remain `{strict_pew["closure_decision"]["strict_P_EW_source_rows"]}`.

## Next Target

The next non-looping target is `{NEXT}`:

try the strict `P_EW`/direct-K exit and the Qa/SU3 Step10 value-execution exit
as the same frontier fork.

## Guardrail

This artifact does not claim global true SM no-knob closure.  It records that
Yukawa finite-replay closure is no longer the hard blocker and orders the
remaining non-Yukawa blockers.
"""

    write_json(LEDGER, ledger)
    write_json(BLOCKERS, blockers)
    write_json(PLAN, plan)
    write_json(OUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
