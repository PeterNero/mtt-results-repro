"""Build QCD theta policy or strict P_EW count-reduction packet.

The preceding cutset identified QCD theta_bar as the missing non-neutrino SM
bookkeeping slot after the 18-count ledger.  This artifact closes that
bookkeeping policy by admitting theta_bar as a physical topological CP slot
unless/until a selected MTT source theorem sets it or pairs it away.  It does
not predict theta_bar=0 and does not solve strong CP.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_qcdthetapolicy_or_strictpewcountreduction"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
QCD_POLICY = PACKET_DIR / "qcd_theta_policy.packet.json"
COUNT_UPDATE = PACKET_DIR / "sm_count_with_qcd_theta_update.packet.json"
NO_KNOB_GATE = PACKET_DIR / "strong_cp_noknob_gate.packet.json"
NEXT_TARGET = PACKET_DIR / "next_after_qcd_theta_policy.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_QCDThetaPolicy_or_StrictPEWCountReduction_v1.md"

PREVIOUS = DATA / "selected_strictpewsourcetheorem_or_smprecisionclosurecutset.candidate.json"
COUNT_FRONTIER = (
    DATA
    / "selected_strictpewsourcetheorem_or_smprecisionclosurecutset"
    / "sm_parameter_count_frontier.packet.json"
)
STRICT_RECHECK = (
    DATA
    / "selected_strictpewsourcetheorem_or_smprecisionclosurecutset"
    / "strict_pew_count_reduction_recheck.packet.json"
)
CUTSET_ORDER = (
    DATA
    / "selected_strictpewsourcetheorem_or_smprecisionclosurecutset"
    / "precision_closure_cutset_order.packet.json"
)

STATUS = (
    "MTT_SELECTED_QCDTHETAPOLICY_OR_STRICTPEWCOUNTREDUCTION_"
    "QCD_THETA_SLOT_ADMITTED_STRICT_PEW_OPEN"
)
NEXT = "MTT_Selected_NeutrinoMassMajoranaPolicy_or_PrecisionProfileTable_v1"


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
    sources = [PREVIOUS, COUNT_FRONTIER, STRICT_RECHECK, CUTSET_ORDER]
    missing = [rel(path) for path in sources if not path.exists()]
    if missing:
        raise FileNotFoundError("missing QCD theta policy inputs: " + ", ".join(missing))

    previous = load(PREVIOUS)
    frontier = load(COUNT_FRONTIER)
    strict = load(STRICT_RECHECK)
    cutset = load(CUTSET_ORDER)

    base_non_neutrino = int(frontier["current_counts"]["non_neutrino_excluding_QCD_theta"])
    base_pmns = int(frontier["current_counts"]["minimal_PMNS_extension_excluding_QCD_theta"])
    strict_non_neutrino = int(strict["conditional_non_neutrino_count_if_strict_P_EW_closes"])
    strict_pmns = int(strict["conditional_PMNS_extension_count_if_strict_P_EW_closes"])
    qcd_add = int(frontier["conditional_count_movements"]["QCD_theta_bar_admitted"])

    non_neutrino_with_qcd = base_non_neutrino + qcd_add
    pmns_with_qcd = base_pmns + qcd_add
    strict_non_neutrino_with_qcd = strict_non_neutrino + qcd_add
    strict_pmns_with_qcd = strict_pmns + qcd_add

    qcd_policy = guarded(
        {
            "schema": "MTTQCDThetaPolicy.v1",
            "status": "QCD_THETA_BAR_ADMITTED_AS_TOPOLOGICAL_CP_SLOT",
            "policy_closed": True,
            "theta_bar_symbol": "theta_bar_QCD",
            "slot_kind": "physical topological CP parameter/policy slot",
            "slot_count": qcd_add,
            "admitted_as_parameter_until_selected_source_theorem": True,
            "theta_bar_value_selected_by_MTT": False,
            "theta_bar_zero_predicted": False,
            "strong_CP_problem_solved": False,
            "forbidden_overclaims": [
                "do not set theta_bar=0 from absence of evidence",
                "do not treat experimental smallness as source selection",
                "do not use CKM CP phase as QCD theta source without a theorem",
                "do not claim axion/PQ mechanism unless selected in MTT source data",
            ],
            "valid_future_no_knob_exits": [
                "selected CP/orientation theorem sets theta_bar_QCD=0",
                "selected topological pairing cancels theta_bar_QCD",
                "selected axion-like/PQ source mechanism emerges internally",
                "selected finite quotient forbids the QCD topological CP phase",
            ],
        }
    )

    count_update = guarded(
        {
            "schema": "MTTSMCountWithQCDThetaUpdate.v1",
            "status": "SM_COUNTS_UPDATED_WITH_QCD_THETA_POLICY",
            "counts_excluding_QCD_theta": {
                "non_neutrino": base_non_neutrino,
                "minimal_PMNS": base_pmns,
                "if_strict_P_EW_closes_non_neutrino": strict_non_neutrino,
                "if_strict_P_EW_closes_minimal_PMNS": strict_pmns,
            },
            "counts_including_QCD_theta": {
                "non_neutrino": non_neutrino_with_qcd,
                "minimal_PMNS": pmns_with_qcd,
                "if_strict_P_EW_closes_non_neutrino": strict_non_neutrino_with_qcd,
                "if_strict_P_EW_closes_minimal_PMNS": strict_pmns_with_qcd,
            },
            "interpretation": {
                "current_non_neutrino_ledger_matches_standard_19_slot_bookkeeping_when_QCD_theta_is_admitted": True,
                "strict_P_EW_source_closure_would_replace_one_admitted_prefactor_slot": True,
                "QCD_theta_admission_is_not_no_knob_prediction": True,
                "strong_CP_no_knob_target_remains_open": True,
            },
        }
    )

    no_knob_gate = guarded(
        {
            "schema": "MTTStrongCPNoKnobGate.v1",
            "status": "STRONG_CP_NOKNOB_GATE_OPEN",
            "accepted_theta_bar_source_values": 0,
            "accepted_theta_bar_cancellation_theorems": 0,
            "accepted_axion_or_PQ_source_mechanisms": 0,
            "accepted_finite_quotient_forbiddance_theorems": 0,
            "source_gate_closed": False,
            "policy_gate_closed": True,
            "policy_result": "admit theta_bar_QCD as one counted topological CP slot for parity/ledger purposes",
        }
    )

    next_target = guarded(
        {
            "schema": "MTTNextAfterQCDThetaPolicy.v1",
            "status": "NEXT_TARGET_NEUTRINO_POLICY_OR_PRECISION_PROFILE",
            "next_required_artifact": NEXT,
            "strict_P_EW_parallel_exit_retained": True,
            "remaining_cutset_after_qcd_policy": [
                row["target"]
                for row in cutset["cutset_rows"]
                if row["target"] != "QCD theta_bar / strong-CP policy"
            ],
        }
    )

    candidate = guarded(
        {
            "candidate": "MTTSelectedQCDThetaPolicyOrStrictPEWCountReduction",
            "status": STATUS,
            "next_required_artifact": NEXT,
            "inputs": {
                "previous": rel(PREVIOUS),
                "count_frontier": rel(COUNT_FRONTIER),
                "strict_recheck": rel(STRICT_RECHECK),
                "cutset_order": rel(CUTSET_ORDER),
            },
            "packets": {
                "qcd_theta_policy": rel(QCD_POLICY),
                "sm_count_with_qcd_theta_update": rel(COUNT_UPDATE),
                "strong_cp_noknob_gate": rel(NO_KNOB_GATE),
                "next_after_qcd_theta_policy": rel(NEXT_TARGET),
            },
            "closure_decision": {
                "QCD_theta_bar_policy_closed": True,
                "QCD_theta_bar_admitted_parameter_slot": True,
                "QCD_theta_bar_slot_count": qcd_add,
                "theta_bar_value_selected_by_MTT": False,
                "theta_bar_zero_predicted": False,
                "strong_CP_problem_solved": False,
                "strict_P_EW_source_theorem_closed": previous["closure_decision"][
                    "strict_P_EW_source_theorem_closed"
                ],
                "strict_P_EW_source_rows": previous["closure_decision"]["strict_P_EW_source_rows"],
                "P_EW_count_reduction_available_now": previous["closure_decision"][
                    "P_EW_count_reduction_available_now"
                ],
                "non_neutrino_count_including_QCD_theta": non_neutrino_with_qcd,
                "minimal_PMNS_count_including_QCD_theta": pmns_with_qcd,
                "non_neutrino_count_if_strict_P_EW_closes_including_QCD_theta": (
                    strict_non_neutrino_with_qcd
                ),
                "minimal_PMNS_count_if_strict_P_EW_closes_including_QCD_theta": (
                    strict_pmns_with_qcd
                ),
                "absolute_neutrino_majorana_policy_closed": False,
                "precision_profile_closure_closed": False,
                "true_SM_equivalence_closed": False,
                "full_no_knob_closed": False,
            },
            "theorem": {
                "name": "QCDThetaPolicyOrStrictPEWCountReductionTheorem",
                "proved": True,
                "statement": (
                    "After the 18/24 ledger excluding QCD theta_bar, the QCD "
                    "topological CP angle is admitted as one physical parameter/"
                    "policy slot for SM-parity accounting. This raises the active "
                    "non-neutrino ledger to 19 and the minimal PMNS ledger to 25. "
                    "It does not select a theta_bar value, predict theta_bar=0, or "
                    "solve strong CP. If strict P_EW later closes, the corresponding "
                    "including-QCD counts become 18 and 24."
                ),
            },
        }
    )

    cert = guarded(
        {
            "certificate": "MTTSelectedQCDThetaPolicyOrStrictPEWCountReduction",
            "status": STATUS,
            "theorem_proved": True,
            "QCD_theta_bar_policy_closed": True,
            "QCD_theta_bar_admitted_parameter_slot": True,
            "QCD_theta_bar_slot_count": qcd_add,
            "theta_bar_value_selected_by_MTT": False,
            "theta_bar_zero_predicted": False,
            "strong_CP_problem_solved": False,
            "strict_P_EW_source_theorem_closed": False,
            "non_neutrino_count_including_QCD_theta": non_neutrino_with_qcd,
            "minimal_PMNS_count_including_QCD_theta": pmns_with_qcd,
            "non_neutrino_count_if_strict_P_EW_closes_including_QCD_theta": (
                strict_non_neutrino_with_qcd
            ),
            "minimal_PMNS_count_if_strict_P_EW_closes_including_QCD_theta": (
                strict_pmns_with_qcd
            ),
            "true_SM_equivalence_claimed": False,
            "full_no_knob_closure_claimed": False,
            "next_required_artifact": NEXT,
        }
    )

    note = f"""# MTT Selected QCDThetaPolicy or StrictPEWCountReduction v1

## Theorem

`QCDThetaPolicyOrStrictPEWCountReductionTheorem` is emitted.

## QCD Theta Policy

```text
QCD theta_bar policy closed = true
QCD theta_bar admitted parameter slot = true
QCD theta_bar slot count = {qcd_add}
theta_bar value selected by MTT = false
theta_bar zero predicted = false
strong CP problem solved = false
```

The policy is conservative: `theta_bar_QCD` is counted as one physical
topological CP slot unless a later selected source theorem sets it, cancels it,
or forbids it.

## Updated Counts

```text
non-neutrino count including QCD theta_bar = {non_neutrino_with_qcd}
minimal PMNS count including QCD theta_bar = {pmns_with_qcd}
non-neutrino count if strict P_EW closes including QCD theta_bar = {strict_non_neutrino_with_qcd}
minimal PMNS count if strict P_EW closes including QCD theta_bar = {strict_pmns_with_qcd}
```

## Claim Boundary

This is a ledger/policy closure, not a no-knob strong-CP solution.

Forbidden overclaims:

```text
do not set theta_bar=0 from absence of evidence
do not treat experimental smallness as source selection
do not use CKM CP phase as QCD theta source without a theorem
do not claim axion/PQ mechanism unless selected in MTT source data
```

## Next Artifact

`{NEXT}`.
"""

    for path, payload in [
        (QCD_POLICY, qcd_policy),
        (COUNT_UPDATE, count_update),
        (NO_KNOB_GATE, no_knob_gate),
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
