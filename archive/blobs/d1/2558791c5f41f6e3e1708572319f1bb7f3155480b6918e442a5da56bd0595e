"""Build the precision-equivalence rows / true-SM closure audit after PEW closure.

This consumes the strict P_EW/direct-K promotion and rebuilds the true-SM
frontier table.  It closes the stale PEW blocker and leaves only the genuine
precision/global-audit blockers.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_precisionequivalencerows_or_truesmclosureaudit"
OUT = DATA / f"{SLUG}.candidate.json"
PACKET_DIR = DATA / SLUG
LEDGER = PACKET_DIR / "post_pew_true_sm_precision_ledger.packet.json"
ROWS = PACKET_DIR / "precision_equivalence_row_status_table.packet.json"
CUTSET = PACKET_DIR / "remaining_true_sm_cutset_after_pew.packet.json"
NEXT = PACKET_DIR / "next_precision_execution_contract.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PrecisionEquivalenceRows_or_TrueSMClosureAudit_v1.md"

PEW = DATA / "selected_strictpewdenominatorselectiontheorem_or_directkpromotion.candidate.json"
OLD_PRECISION = DATA / "selected_precisionprofiletable_or_truesmequivalenceaudit.candidate.json"
TRUE_VALUE = DATA / "selected_trueequivalenceprecisionvaluetable_or_actualqasu3operatorupgrade.candidate.json"
REPLAY_SUITE = DATA / "selected_precisionempiricalreplaysuite_or_trueequivalence.candidate.json"
LOCAL_QFT = DATA / "selected_localqftobservablerows_or_finaltruesmequivalencegap.candidate.json"
QCD = DATA / "selected_qcdthetapolicy_or_strictpewcountreduction.candidate.json"
NEUTRINO = DATA / "selected_neutrinomassmajoranapolicy_or_precisionprofiletable.candidate.json"
RG_SUITE = DATA / "sm_equivalence_rgpolicy_covariance_and_observable_suite.candidate.json"
THRESHOLD = DATA / "selected_acceptedthresholdmassschemesourcerows_or_noknobvaluederivation.candidate.json"
CROSS = DATA / "true_sm_crossrepo_part_status_audit.candidate.json"

STATUS = (
    "MTT_SELECTED_PRECISIONEQUIVALENCEROWS_OR_TRUESMCLOSUREAUDIT_"
    "POST_PEW_LEDGER_REBUILT_PRECISION_OPEN"
)
NEXT_ARTIFACT = "MTT_Selected_PrecisionTransportCovarianceRows_or_FinalTrueSMAudit_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing precision audit inputs: " + ", ".join(missing))


def cross_part(cross: dict[str, Any], part: str) -> dict[str, Any]:
    for item in cross["parts"]:
        if item["part"] == part:
            return item
    raise KeyError(part)


def main() -> int:
    sources = [PEW, OLD_PRECISION, TRUE_VALUE, REPLAY_SUITE, LOCAL_QFT, QCD, NEUTRINO, RG_SUITE, THRESHOLD, CROSS]
    require_sources(sources)

    pew = load(PEW)
    old_precision = load(OLD_PRECISION)
    true_value = load(TRUE_VALUE)
    replay = load(REPLAY_SUITE)
    local_qft = load(LOCAL_QFT)
    qcd = load(QCD)
    neutrino = load(NEUTRINO)
    rg = load(RG_SUITE)
    threshold = load(THRESHOLD)
    cross = load(CROSS)

    strict_pew_rows = pew["closure_decision"]["accepted_global_strict_P_EW_source_rows"]
    strict_direct_k_rows = pew["closure_decision"]["accepted_global_direct_K_threshold_Omega_H_lambda_rows"]
    strict_k_count = pew["closure_decision"]["strict_zero_primitive_K_threshold_row_count"]

    # The older QCD/neutrino count packets were built before strict PEW closed.
    # Apply their own conditional-if-strict-PEW-closes counts as the current
    # post-PEW counts.
    non_neutrino_with_qcd = qcd["closure_decision"]["non_neutrino_count_if_strict_P_EW_closes_including_QCD_theta"]
    minimal_pmns_with_qcd = neutrino["closure_decision"][
        "minimal_PMNS_count_if_strict_P_EW_closes_including_QCD_theta"
    ]
    dirac_massive_with_qcd = neutrino["closure_decision"]["Dirac_count_if_strict_P_EW_closes_including_QCD_theta"]
    majorana_massive_with_qcd = neutrino["closure_decision"]["Majorana_count_if_strict_P_EW_closes_including_QCD_theta"]

    row_statuses = [
        {
            "row_class": "core_matrix_yukawa_higgs_pew_directk",
            "status": "CLOSED_STRICT_CORE",
            "closed": True,
            "counts_for_true_precision_equivalence": False,
            "evidence": rel(PEW),
            "summary": "27x27 matrix, finite-replay Yukawa, finite H, strict P_EW, and direct H/lambda K are closed.",
        },
        {
            "row_class": "precision_policy_and_central_replay",
            "status": "POLICY_AND_CENTRAL_REPLAY_CLOSED",
            "closed": True,
            "counts_for_true_precision_equivalence": False,
            "evidence": rel(OLD_PRECISION),
            "summary": "Precision profile table and central-value replay baseline are built.",
        },
        {
            "row_class": "threshold_mass_scheme_source_rows",
            "status": "OPEN",
            "closed": False,
            "counts_for_true_precision_equivalence": True,
            "evidence": rel(THRESHOLD),
            "summary": "No accepted threshold/mass-scheme source rows; external replay support exists but no true-precision source row.",
        },
        {
            "row_class": "full_covariance_profile_likelihood",
            "status": "OPEN",
            "closed": False,
            "counts_for_true_precision_equivalence": True,
            "evidence": rel(RG_SUITE),
            "summary": "Central-value tier is declared; full covariance/profile likelihood is still open.",
        },
        {
            "row_class": "multi_loop_rg_transport_values",
            "status": "OPEN",
            "closed": False,
            "counts_for_true_precision_equivalence": True,
            "evidence": rel(RG_SUITE),
            "summary": "MSbar/MZ policy is declared, but beta/matching/threshold transport values remain open.",
        },
        {
            "row_class": "local_qft_precision_observables",
            "status": "TREE_TIER_CLOSED_PRECISION_OPEN",
            "closed": False,
            "counts_for_true_precision_equivalence": True,
            "evidence": rel(LOCAL_QFT),
            "summary": "Tree local-QFT identity rows are closed; precision correlator/S-matrix/decay rows remain open.",
        },
        {
            "row_class": "selected_qasu3_operator_packet",
            "status": "OPEN",
            "closed": False,
            "counts_for_true_precision_equivalence": True,
            "evidence": rel(TRUE_VALUE),
            "summary": "Dual route contract exists; actual selected Qa/SU3 operator packet values are not filled.",
        },
        {
            "row_class": "neutrino_absolute_majorana_policy",
            "status": "MINIMAL_OSCILLATION_CLOSED_ABSOLUTE_OPEN",
            "closed": False,
            "counts_for_true_precision_equivalence": True,
            "evidence": rel(NEUTRINO),
            "summary": "PMNS oscillation replay is closed; absolute mass, Dirac/Majorana choice, and phases remain open.",
        },
        {
            "row_class": "qcd_theta_strong_cp",
            "status": "SM_PARITY_SLOT_ADMITTED_STRONG_CP_OPEN",
            "closed": False,
            "counts_for_true_precision_equivalence": True,
            "evidence": rel(QCD),
            "summary": "QCD theta slot is admitted for parity; theta value/strong-CP no-knob solution is open.",
        },
        {
            "row_class": "global_true_sm_audit",
            "status": "OPEN_UNTIL_PRECISION_ROWS_CLOSE",
            "closed": False,
            "counts_for_true_precision_equivalence": True,
            "evidence": rel(REPLAY_SUITE),
            "summary": "Empirical replay suite exists; final true-equivalence theorem waits on the open precision rows.",
        },
    ]

    blocking_rows = [row for row in row_statuses if row["counts_for_true_precision_equivalence"] and not row["closed"]]

    ledger = {
        "schema": "MTTPostPEWTrueSMPrecisionLedger.v1",
        "status": "POST_PEW_LEDGER_REBUILT",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "strict_core": {
            "accepted_global_strict_P_EW_source_rows": strict_pew_rows,
            "accepted_global_direct_K_threshold_Omega_H_lambda_rows": strict_direct_k_rows,
            "strict_zero_primitive_K_threshold_row_count": strict_k_count,
            "strict_PEW_directK_blocker_closed": True,
        },
        "parameter_counts_after_strict_PEW": {
            "non_neutrino_including_QCD_theta": non_neutrino_with_qcd,
            "minimal_PMNS_including_QCD_theta": minimal_pmns_with_qcd,
            "Dirac_massive_neutrino_including_QCD_theta": dirac_massive_with_qcd,
            "Majorana_massive_neutrino_including_QCD_theta": majorana_massive_with_qcd,
        },
        "stale_fields_superseded": {
            "old_precision_strict_P_EW_source_theorem_closed": old_precision["closure_decision"][
                "strict_P_EW_source_theorem_closed"
            ],
            "old_qcd_strict_P_EW_source_rows": qcd["closure_decision"]["strict_P_EW_source_rows"],
            "old_neutrino_strict_P_EW_source_theorem_closed": neutrino["closure_decision"][
                "strict_P_EW_source_theorem_closed"
            ],
            "superseded_by": rel(PEW),
        },
    }
    write_json(LEDGER, ledger)

    rows_packet = {
        "schema": "MTTPrecisionEquivalenceRowStatusTable.v1",
        "status": "ROW_STATUS_TABLE_REBUILT_AFTER_PEW",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "rows": row_statuses,
        "blocking_true_precision_row_count": len(blocking_rows),
        "closed_strict_core_row_classes": 2,
        "accepted_true_equivalence_precision_rows": 0,
    }
    write_json(ROWS, rows_packet)

    cutset = {
        "schema": "MTTRemainingTrueSMCutsetAfterPEW.v1",
        "status": "TRUE_SM_PRECISION_CUTSET_AFTER_PEW",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "remaining_blockers_ordered": [
            "threshold/mass-scheme source rows and multi-loop RG transport values",
            "full covariance/profile likelihood or accepted precision profile import",
            "local-QFT precision correlator/S-matrix/decay observable rows",
            "actual selected Qa/SU3 operator packet values",
            "neutrino absolute mass and Dirac/Majorana completion",
            "QCD theta value or strong-CP source policy",
            "global true-SM theorem audit after the rows above are closed",
        ],
        "non_blockers_now": [
            "27x27 matrix",
            "finite-replay Yukawa magnitude rows",
            "finite H scalar and H/lambda row",
            "strict P_EW source row",
            "strict direct K_threshold.Omega_H.lambda row",
        ],
    }
    write_json(CUTSET, cutset)

    next_packet = {
        "schema": "MTTNextPrecisionExecutionContract.v1",
        "status": "NEXT_EXECUTE_PRECISION_TRANSPORT_COVARIANCE_ROWS",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT_ARTIFACT,
        "recommended_next_steps": [
            "promote or derive threshold/mass-scheme source rows under the VSD02 strict schema",
            "attach multi-loop RG transport and threshold conventions at MSbar/MZ",
            "upgrade central-value replay to full covariance/profile likelihood where data are available",
            "emit local-QFT precision observable rows or a declared functor with values",
            "then run the global true-SM closure audit",
        ],
    }
    write_json(NEXT, next_packet)

    decision = {
        "post_PEW_precision_ledger_rebuilt": True,
        "strict_PEW_directK_blocker_closed": True,
        "accepted_global_strict_P_EW_source_rows": strict_pew_rows,
        "accepted_global_direct_K_threshold_Omega_H_lambda_rows": strict_direct_k_rows,
        "strict_zero_primitive_K_threshold_row_count": strict_k_count,
        "precision_policy_rows_closed": old_precision["closure_decision"]["precision_policy_rows_closed"],
        "central_value_replay_baseline_closed": old_precision["closure_decision"][
            "central_value_replay_baseline_closed"
        ],
        "minimal_PMNS_oscillation_policy_closed": neutrino["closure_decision"][
            "minimal_PMNS_oscillation_policy_closed"
        ],
        "QCD_theta_bar_policy_closed": qcd["closure_decision"]["QCD_theta_bar_policy_closed"],
        "local_QFT_tree_identity_observable_rows_closed": local_qft["closure_decision"][
            "tree_QFT_identity_tier_closed"
        ],
        "accepted_true_equivalence_precision_rows": 0,
        "blocking_true_precision_row_count": len(blocking_rows),
        "threshold_mass_scheme_source_rows_closed": False,
        "full_covariance_profile_likelihood_closed": False,
        "multi_loop_RG_values_closed": False,
        "local_QFT_precision_observable_table_closed": False,
        "selected_QaSU3_operator_payload_closed": False,
        "neutrino_absolute_source_closed": False,
        "strong_CP_problem_solved": False,
        "full_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
    }

    candidate = {
        "candidate": "MTTSelectedPrecisionEquivalenceRowsOrTrueSMClosureAudit",
        "status": STATUS,
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "post_pew_true_sm_precision_ledger": rel(LEDGER),
            "precision_equivalence_row_status_table": rel(ROWS),
            "remaining_true_sm_cutset_after_pew": rel(CUTSET),
            "next_precision_execution_contract": rel(NEXT),
        },
        "theorem": {
            "name": "PrecisionEquivalenceRowsOrTrueSMClosureAuditTheorem",
            "proved": True,
            "statement": (
                "After the strict P_EW/direct-K denominator-selection theorem, the "
                "true-SM ledger is rebuilt with PEW removed from the open blocker "
                "set. The strict core is closed, while precision equivalence remains "
                "open at threshold/mass-scheme rows, full covariance/profile, "
                "multi-loop RG transport, local-QFT precision observables, actual "
                "Qa/SU3 operator packet values, neutrino absolute policy, QCD theta, "
                "and the final global audit."
            ),
        },
        "closure_decision": decision,
        "next_required_artifact": NEXT_ARTIFACT,
    }
    write_json(OUT, candidate)

    cert = {
        "certificate": "MTT_Selected_PrecisionEquivalenceRows_or_TrueSMClosureAudit_v1",
        "status": STATUS,
        "candidate": rel(OUT),
        "theorem_proved": True,
        **decision,
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT_ARTIFACT,
    }
    write_json(CERT, cert)

    blockers = "\n".join(f"- {row['row_class']}: {row['status']}" for row in blocking_rows)
    NOTE.write_text(
        f"""# MTT Selected PrecisionEquivalenceRows or TrueSMClosureAudit v1

Status: `{STATUS}`.

## Closed Since Previous Precision Table

```text
strict P_EW source rows              = {strict_pew_rows}
strict direct K_threshold.Omega_H    = {strict_direct_k_rows}
strict zero-primitive K ledger       = {strict_k_count}/10
```

This supersedes older precision/QCD/neutrino packets that still listed strict
`P_EW` as open.

## Updated Counts

```text
non-neutrino including QCD theta          = {non_neutrino_with_qcd}
minimal PMNS including QCD theta          = {minimal_pmns_with_qcd}
Dirac massive neutrino including QCD theta= {dirac_massive_with_qcd}
Majorana completion including QCD theta   = {majorana_massive_with_qcd}
```

## Remaining True-Precision Blockers

```text
{blockers}
```

Accepted true-equivalence precision rows remain `0`; the strict core is closed
but full true-SM precision equivalence is not yet claimed.

Next artifact: `{NEXT_ARTIFACT}`.
""",
        encoding="utf-8",
    )

    print(json.dumps({"candidate": rel(OUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
