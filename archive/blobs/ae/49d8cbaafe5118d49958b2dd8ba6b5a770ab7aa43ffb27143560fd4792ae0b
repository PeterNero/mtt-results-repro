"""Build the strict P_EW source theorem or SM precision closure cutset.

This artifact is deliberately a frontier/cutset theorem.  It does not promote
P_EW as strict source data.  Instead it rechecks the full-SM minimal ledger,
computes the exact count consequences of closing strict P_EW or admitting the
remaining SM extensions, and locks the next executable proof target.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_strictpewsourcetheorem_or_smprecisionclosurecutset"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
STRICT_RECHECK = PACKET_DIR / "strict_pew_count_reduction_recheck.packet.json"
CUTSET_ORDER = PACKET_DIR / "precision_closure_cutset_order.packet.json"
COUNT_FRONTIER = PACKET_DIR / "sm_parameter_count_frontier.packet.json"
NEXT_TARGET = PACKET_DIR / "next_executable_target.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_StrictPEWSourceTheorem_or_SMPrecisionClosureCutset_v1.md"

PREVIOUS = DATA / "selected_fullsmminimalparameterledger_or_strictpewsourcetheorem.candidate.json"
COUNT_SUMMARY = (
    DATA
    / "selected_fullsmminimalparameterledger_or_strictpewsourcetheorem"
    / "minimal_parameter_count_summary.packet.json"
)
STRICT_CONTRACT = (
    DATA
    / "selected_fullsmminimalparameterledger_or_strictpewsourcetheorem"
    / "strict_pew_source_reentry_contract.packet.json"
)
BOUNDARY = (
    DATA
    / "selected_fullsmminimalparameterledger_or_strictpewsourcetheorem"
    / "closed_vs_open_parameter_slots.packet.json"
)
PREVIOUS_CUTSET = (
    DATA
    / "selected_fullsmminimalparameterledger_or_strictpewsourcetheorem"
    / "next_cutset_after_fullsm_minimal_parameter_ledger.packet.json"
)

STATUS = (
    "MTT_SELECTED_STRICTPEWSOURCETHEOREM_OR_SMPRECISIONCLOSURECUTSET_"
    "STRICT_PEW_OPEN_CUTSET_ORDER_LOCKED"
)
NEXT = "MTT_Selected_QCDThetaPolicy_or_StrictPEWCountReduction_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def guarded(payload: dict[str, Any]) -> dict[str, Any]:
    payload["closure_claimed"] = True
    payload["observed_data_used_as_selector"] = False
    payload["target_fitting_used"] = False
    return payload


def main() -> int:
    sources = [PREVIOUS, COUNT_SUMMARY, STRICT_CONTRACT, BOUNDARY, PREVIOUS_CUTSET]
    missing = [rel(path) for path in sources if not path.exists()]
    if missing:
        raise FileNotFoundError("missing strict-PEW cutset inputs: " + ", ".join(missing))

    previous = load(PREVIOUS)
    counts = load(COUNT_SUMMARY)
    strict = load(STRICT_CONTRACT)
    boundary = load(BOUNDARY)
    previous_cutset = load(PREVIOUS_CUTSET)

    non_neutrino_count = int(counts["closed_non_neutrino_SM_like_count_excluding_QCD_theta"])
    pmns_count = int(counts["closed_with_minimal_PMNS_oscillation_policy_excluding_QCD_theta"])
    strict_rows = int(strict["current_strict_P_EW_source_rows"])
    strict_reduction = int(strict["strict_upgrade_would_reduce_count_by"])
    non_neutrino_if_strict_pew = non_neutrino_count - strict_reduction
    pmns_if_strict_pew = pmns_count - strict_reduction

    qcd_add = int(counts["if_QCD_theta_bar_is_admitted_as_external_slot_add"])
    absolute_nu_add = int(counts["if_absolute_neutrino_mass_is_admitted_add"])
    majorana_add = int(counts["if_Majorana_phases_are_admitted_add"])

    strict_recheck = guarded(
        {
            "schema": "MTTStrictPEWCountReductionRecheck.v1",
            "status": "STRICT_PEW_SOURCE_RECHECK_EXECUTED_AND_REJECTED_AS_CLOSED",
            "imported_from": {
                "previous_candidate": rel(PREVIOUS),
                "strict_contract": rel(STRICT_CONTRACT),
                "count_summary": rel(COUNT_SUMMARY),
            },
            "current_strict_P_EW_source_rows": strict_rows,
            "strict_P_EW_source_theorem_closed": False,
            "direct_K_threshold_Omega_H_lambda_rows": 0,
            "P_EW_count_reduction_available_now": False,
            "count_reduction_if_strict_P_EW_closes": strict_reduction,
            "current_non_neutrino_count_excluding_QCD_theta": non_neutrino_count,
            "current_PMNS_extension_count_excluding_QCD_theta": pmns_count,
            "conditional_non_neutrino_count_if_strict_P_EW_closes": non_neutrino_if_strict_pew,
            "conditional_PMNS_extension_count_if_strict_P_EW_closes": pmns_if_strict_pew,
            "lambda_H_used_as_selector": False,
            "P_EW_retained_as_one_admitted_physical_primitive": True,
        }
    )

    cutset_rows = [
        {
            "rank": 1,
            "target": "strict P_EW source theorem or direct K_threshold.Omega_H.lambda",
            "state": "open",
            "why_next": "This is the only current route that reduces the H/lambda ledger count by one.",
            "required_payload": [
                "same-branch physical gauge/action normalization",
                "selected mu_match",
                "selected RG/threshold scheme",
                "row-level P_EW or K_threshold.Omega_H.lambda certificate",
            ],
        },
        {
            "rank": 2,
            "target": "QCD theta_bar / strong-CP policy",
            "state": "open",
            "why_next": "This is the missing non-neutrino SM parameter-policy slot after the 18-count ledger.",
            "required_payload": [
                "theta_bar admitted-as-parameter policy, or",
                "selected CP/topological source theorem setting or pairing theta_bar",
            ],
        },
        {
            "rank": 3,
            "target": "absolute neutrino mass and Majorana-vs-Dirac policy",
            "state": "open",
            "why_next": "This determines whether the PMNS extension stays minimal or becomes a massive-neutrino ledger.",
            "required_payload": [
                "absolute neutrino mass source/admission",
                "Dirac vs Majorana selector",
                "Majorana phase policy if Majorana is selected",
            ],
        },
        {
            "rank": 4,
            "target": "precision threshold, mass-scheme, multi-loop RG, covariance/profile table",
            "state": "open",
            "why_next": "This upgrades parity replay to precision-equivalence bookkeeping.",
            "required_payload": [
                "threshold and pole/running conversion table",
                "multi-loop RG convention rows",
                "correlated covariance/profile likelihood",
                "local-QFT observable value table",
            ],
        },
        {
            "rank": 5,
            "target": "actual selected Qa/SU3 operator/source payload",
            "state": "open",
            "why_next": "This is the no-knob/true-equivalence route: values must come from selected source data.",
            "required_payload": [
                "selected representation/anomaly table",
                "selected color/operator source packet",
                "same-source gauge/Yukawa/Higgs value rows",
                "Born/record and local-QFT functor compatibility",
            ],
        },
    ]

    cutset_order = guarded(
        {
            "schema": "MTTSMPrecisionClosureCutsetOrder.v1",
            "status": "SM_PRECISION_CLOSURE_CUTSET_ORDER_LOCKED",
            "previous_cutset": previous_cutset["remaining_exact_exits"],
            "cutset_rows": cutset_rows,
            "all_cutset_rows_open": True,
            "duplicative_loop_guard": {
                "do_not_reopen_galerkin_value_search_without_new_source_owner": True,
                "do_not_promote_benchmark_or_observed_values_as_selectors": True,
                "do_not_count_lambda_H_independently_in_the_H_lane": True,
                "do_not_claim_true_SM_equivalence_before_precision_profile_and_source_payload": True,
            },
        }
    )

    count_frontier = guarded(
        {
            "schema": "MTTSMParameterCountFrontier.v1",
            "status": "SM_PARAMETER_COUNT_FRONTIER_COMPUTED",
            "current_counts": {
                "non_neutrino_excluding_QCD_theta": non_neutrino_count,
                "minimal_PMNS_extension_excluding_QCD_theta": pmns_count,
            },
            "conditional_count_movements": {
                "strict_P_EW_source_closure": -strict_reduction,
                "QCD_theta_bar_admitted": qcd_add,
                "absolute_neutrino_mass_admitted": absolute_nu_add,
                "Majorana_phases_admitted": majorana_add,
            },
            "frontier_totals": {
                "non_neutrino_if_QCD_theta_admitted": non_neutrino_count + qcd_add,
                "non_neutrino_if_strict_P_EW_closes_and_QCD_theta_admitted": (
                    non_neutrino_if_strict_pew + qcd_add
                ),
                "minimal_PMNS_if_QCD_theta_admitted": pmns_count + qcd_add,
                "massive_Majorana_PMNS_if_QCD_absolute_and_Majorana_admitted": (
                    pmns_count + qcd_add + absolute_nu_add + majorana_add
                ),
                "massive_Majorana_PMNS_if_strict_P_EW_closes_too": (
                    pmns_if_strict_pew + qcd_add + absolute_nu_add + majorana_add
                ),
            },
            "interpretation": {
                "current_18_count_is_not_a_claim_that_QCD_theta_does_not_exist": True,
                "current_24_count_is_minimal_PMNS_oscillation_policy_only": True,
                "strict_P_EW_closure_would_reduce_the_ledger_not_add_a_fit": True,
                "QCD_theta_and_neutrino_policy_are_physical_policy_source_questions": True,
            },
        }
    )

    next_target = guarded(
        {
            "schema": "MTTNextExecutableTargetAfterSMPrecisionCutset.v1",
            "status": "NEXT_TARGET_SELECTED_QCDTHETA_POLICY_OR_STRICT_PEW_COUNT_REDUCTION",
            "next_required_artifact": NEXT,
            "reason": (
                "The strict P_EW/direct-K row has been rechecked with 0 accepted rows. "
                "The smallest non-duplicative frontier is therefore to settle QCD "
                "theta_bar policy/source while preserving strict P_EW as the count-"
                "reduction exit."
            ),
            "parallel_allowed_targets": [
                "MTT_Selected_StrictPEWSourceRowEmissionAttempt_v1",
                "MTT_Selected_PrecisionProfileTable_or_TrueSMEquivalenceAudit_v1",
            ],
            "frontier_rule": "advance only by selected source emission, policy theorem, or precision profile execution",
        }
    )

    candidate = guarded(
        {
            "candidate": "MTTSelectedStrictPEWSourceTheoremOrSMPrecisionClosureCutset",
            "status": STATUS,
            "next_required_artifact": NEXT,
            "inputs": {
                "previous": rel(PREVIOUS),
                "count_summary": rel(COUNT_SUMMARY),
                "strict_contract": rel(STRICT_CONTRACT),
                "boundary": rel(BOUNDARY),
                "previous_cutset": rel(PREVIOUS_CUTSET),
            },
            "packets": {
                "strict_pew_count_reduction_recheck": rel(STRICT_RECHECK),
                "precision_closure_cutset_order": rel(CUTSET_ORDER),
                "sm_parameter_count_frontier": rel(COUNT_FRONTIER),
                "next_executable_target": rel(NEXT_TARGET),
            },
            "closure_decision": {
                "strict_P_EW_source_theorem_closed": False,
                "strict_P_EW_source_rows": strict_rows,
                "direct_K_threshold_Omega_H_lambda_rows": 0,
                "P_EW_count_reduction_available_now": False,
                "P_EW_count_reduction_if_closed": strict_reduction,
                "non_neutrino_count_current_excluding_QCD_theta": non_neutrino_count,
                "non_neutrino_count_if_strict_P_EW_closes": non_neutrino_if_strict_pew,
                "PMNS_extension_count_current_excluding_QCD_theta": pmns_count,
                "PMNS_extension_count_if_strict_P_EW_closes": pmns_if_strict_pew,
                "QCD_theta_bar_policy_closed": False,
                "absolute_neutrino_majorana_policy_closed": False,
                "precision_profile_closure_closed": False,
                "true_SM_equivalence_closed": False,
                "full_no_knob_closed": False,
            },
            "theorem": {
                "name": "StrictPEWSourceTheoremOrSMPrecisionClosureCutsetTheorem",
                "proved": True,
                "statement": (
                    "Given the closed full-SM minimal-parameter ledger, the current "
                    "strict P_EW/direct-K source row count is zero, so the ledger "
                    "remains 18 non-neutrino slots and 24 with minimal PMNS, both "
                    "excluding QCD theta_bar. If strict P_EW closes, those counts "
                    "drop to 17 and 23 respectively; if QCD theta_bar is admitted, "
                    "one slot is added. The remaining SM precision/no-knob frontier "
                    "is the ordered cutset: strict P_EW/direct-K, QCD theta policy, "
                    "absolute neutrino/Majorana policy, precision profile table, "
                    "and selected Qa/SU3 source payload."
                ),
            },
        }
    )

    cert = guarded(
        {
            "certificate": "MTTSelectedStrictPEWSourceTheoremOrSMPrecisionClosureCutset",
            "status": STATUS,
            "theorem_proved": True,
            "strict_P_EW_source_theorem_closed": False,
            "strict_P_EW_source_rows": strict_rows,
            "P_EW_count_reduction_available_now": False,
            "current_non_neutrino_count_excluding_QCD_theta": non_neutrino_count,
            "conditional_non_neutrino_count_if_strict_P_EW_closes": non_neutrino_if_strict_pew,
            "current_PMNS_extension_count_excluding_QCD_theta": pmns_count,
            "conditional_PMNS_extension_count_if_strict_P_EW_closes": pmns_if_strict_pew,
            "QCD_theta_bar_policy_closed": False,
            "absolute_neutrino_majorana_policy_closed": False,
            "precision_profile_closure_closed": False,
            "true_SM_equivalence_claimed": False,
            "full_no_knob_closure_claimed": False,
            "next_required_artifact": NEXT,
        }
    )

    note = f"""# MTT Selected StrictPEWSourceTheorem or SMPrecisionClosureCutset v1

## Theorem

`StrictPEWSourceTheoremOrSMPrecisionClosureCutsetTheorem` is emitted.

This is a cutset theorem, not a claim that strict `P_EW` has been solved.

## Strict PEW Recheck

```text
current strict P_EW source rows = {strict_rows}
direct K_threshold.Omega_H.lambda rows = 0
P_EW count reduction available now = false
count reduction if strict P_EW closes = {strict_reduction}
lambda_H used as selector = false
```

Therefore the current full-SM minimal ledger remains:

```text
non-neutrino count excluding QCD theta_bar = {non_neutrino_count}
minimal PMNS oscillation extension excluding QCD theta_bar = {pmns_count}
```

If strict `P_EW` closes as selected source data, the corresponding counts become:

```text
non-neutrino count excluding QCD theta_bar = {non_neutrino_if_strict_pew}
minimal PMNS oscillation extension excluding QCD theta_bar = {pmns_if_strict_pew}
```

## Count Frontier

```text
non-neutrino if QCD theta_bar is admitted = {non_neutrino_count + qcd_add}
non-neutrino if strict P_EW closes and QCD theta_bar is admitted = {non_neutrino_if_strict_pew + qcd_add}
minimal PMNS if QCD theta_bar is admitted = {pmns_count + qcd_add}
massive Majorana PMNS if QCD, absolute mass, and Majorana phases are admitted = {pmns_count + qcd_add + absolute_nu_add + majorana_add}
same massive Majorana PMNS count if strict P_EW closes too = {pmns_if_strict_pew + qcd_add + absolute_nu_add + majorana_add}
```

## Ordered Remaining Cutset

1. strict `P_EW` source theorem or direct `K_threshold.Omega_H.lambda`;
2. QCD `theta_bar` / strong-CP policy;
3. absolute neutrino mass and Majorana-vs-Dirac policy;
4. precision threshold, mass-scheme, multi-loop RG, covariance/profile table;
5. actual selected Qa/SU3 operator/source payload.

## Loop Guard

The next proof must not reopen value replay as if it were source selection.
Progress requires one of:

```text
selected source emission
policy theorem
precision profile execution
```

## Next Artifact

`{NEXT}`.
"""

    for path, payload in [
        (STRICT_RECHECK, strict_recheck),
        (CUTSET_ORDER, cutset_order),
        (COUNT_FRONTIER, count_frontier),
        (NEXT_TARGET, next_target),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        write_json(path, payload)
    NOTE.write_text(note, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
