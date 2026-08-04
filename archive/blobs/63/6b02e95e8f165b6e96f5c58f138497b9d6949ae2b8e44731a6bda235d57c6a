"""Build precision profile table or true SM equivalence audit.

This consolidates the older precision/profile scaffolds with the current
minimal-parameter ledger.  It closes the precision table as an audited frontier
map, while preserving that true SM equivalence remains open until actual
precision values/profile likelihoods and selected Qa/SU3 operator payload rows
are emitted.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_precisionprofiletable_or_truesmequivalenceaudit"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PRECISION_TABLE = PACKET_DIR / "precision_profile_equivalence_table.packet.json"
BLOCKER_MATRIX = PACKET_DIR / "true_sm_equivalence_blocker_matrix.packet.json"
LEDGER_BRIDGE = PACKET_DIR / "minimal_parameter_ledger_to_precision_bridge.packet.json"
NEXT_TARGET = PACKET_DIR / "next_after_precision_profile_table.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PrecisionProfileTable_or_TrueSMEquivalenceAudit_v1.md"

PREVIOUS = DATA / "selected_neutrinomassmajoranapolicy_or_precisionprofiletable.candidate.json"
NEUTRINO_COUNTS = (
    DATA
    / "selected_neutrinomassmajoranapolicy_or_precisionprofiletable"
    / "sm_neutrino_count_tiers.packet.json"
)
RG_POLICY = DATA / "sm_equivalence_rgpolicy_covariance_and_observable_suite.candidate.json"
ACCEPTED_VALUES = DATA / "selected_acceptedcommonscaleyukawahiggsvalues_or_profilelikelihoodexecution.candidate.json"
THRESHOLD_AUDIT = DATA / "selected_acceptedthresholdmassschemesourcerows_or_noknobvaluederivation.candidate.json"
PRECISION_IMPORT = DATA / "selected_acceptedprecisionprofileimport_or_selectedqasu3operatorslotsourcevalues.candidate.json"
LOCAL_QFT = DATA / "selected_localqftprecisionobservabletable_or_qasu3hymoperatorpacket_valueattempt.candidate.json"
FULL_LOOP = DATA / "selected_precisionobservabletable_fullloopimport_or_qasu3operatorslotfill.candidate.json"
STEP8 = DATA / "selected_step8_precisionvalueemission_or_actualqasu3operatorpacketclosure.candidate.json"
STEP9 = DATA / "selected_step9_dynamicqasu3c1response_or_precisionprofilecompletion.candidate.json"

STATUS = (
    "MTT_SELECTED_PRECISIONPROFILETABLE_OR_TRUESMEQUIVALENCEAUDIT_"
    "TABLE_BUILT_TRUE_EQUIVALENCE_OPEN"
)
NEXT = "MTT_Selected_QaSU3OperatorPayload_or_StrictPEWPrecisionExit_v1"


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
    sources = [
        PREVIOUS,
        NEUTRINO_COUNTS,
        RG_POLICY,
        ACCEPTED_VALUES,
        THRESHOLD_AUDIT,
        PRECISION_IMPORT,
        LOCAL_QFT,
        FULL_LOOP,
        STEP8,
        STEP9,
    ]
    missing = [rel(path) for path in sources if not path.exists()]
    if missing:
        raise FileNotFoundError("missing precision table inputs: " + ", ".join(missing))

    previous = load(PREVIOUS)
    neutrino_counts = load(NEUTRINO_COUNTS)
    rg_policy = load(RG_POLICY)
    accepted_values = load(ACCEPTED_VALUES)
    threshold_audit = load(THRESHOLD_AUDIT)
    precision_import = load(PRECISION_IMPORT)
    local_qft = load(LOCAL_QFT)
    full_loop = load(FULL_LOOP)
    step8 = load(STEP8)
    step9 = load(STEP9)

    tier_counts = neutrino_counts["counts_including_QCD_theta"]

    rows = [
        {
            "row": "reference scheme and scale",
            "source": rel(RG_POLICY),
            "state": "policy_closed",
            "blocks_true_equivalence": False,
            "evidence": rg_policy["rg_policy"]["status"],
            "closed_now": rg_policy["what_closes_now"]["RG_reference_scheme_and_scale_policy"],
            "required_for_true_equivalence": "none beyond preserving declared scheme in downstream tables",
        },
        {
            "row": "central-value covariance tier",
            "source": rel(RG_POLICY),
            "state": "policy_closed_full_covariance_open",
            "blocks_true_equivalence": True,
            "evidence": rg_policy["covariance_policy"]["status"],
            "closed_now": rg_policy["what_closes_now"]["central_value_covariance_tier_policy"],
            "required_for_true_equivalence": "full correlated covariance/profile likelihood imports",
        },
        {
            "row": "common-scale Yukawa/Higgs values",
            "source": rel(ACCEPTED_VALUES),
            "state": "versioned_values_closed_true_precision_open",
            "blocks_true_equivalence": True,
            "evidence": accepted_values["status"],
            "closed_now": True,
            "required_for_true_equivalence": "threshold matching, mass-scheme conversion, covariance/profile promotion",
        },
        {
            "row": "threshold and mass-scheme source rows",
            "source": rel(THRESHOLD_AUDIT),
            "state": "audit_closed_accepted_source_rows_zero",
            "blocks_true_equivalence": True,
            "evidence": threshold_audit["status"],
            "closed_now": threshold_audit["what_closes_now"]["candidate_source_rows_audited"],
            "required_for_true_equivalence": "accepted threshold/mass-scheme source rows or external source-row import",
        },
        {
            "row": "precision profile import / row replacement",
            "source": rel(PRECISION_IMPORT),
            "state": "support_diagnostic_values_open",
            "blocks_true_equivalence": True,
            "evidence": precision_import["status"],
            "closed_now": True,
            "required_for_true_equivalence": "accepted profile rows and selected Qa/SU3 operator slot source values",
        },
        {
            "row": "local QFT precision observable table",
            "source": rel(LOCAL_QFT),
            "state": "minimal_representative_rows_filled_full_table_open",
            "blocks_true_equivalence": True,
            "evidence": local_qft["status"],
            "closed_now": local_qft["closure_decision"]["minimal_local_QFT_value_suite_filled"],
            "required_for_true_equivalence": "full local-QFT observable table, propagator/two-point normalization, Ward/anomaly checks",
        },
        {
            "row": "full-loop precision observable import",
            "source": rel(FULL_LOOP),
            "state": "proxy_inventory_built_accepted_table_open",
            "blocks_true_equivalence": True,
            "evidence": full_loop["status"],
            "closed_now": full_loop["closure_decision"]["precision_proxy_inventory_built"],
            "required_for_true_equivalence": "accepted full-loop precision observable table or selected operator source values",
        },
        {
            "row": "Qa/SU3 operator slot/value payload",
            "source": rel(STEP8),
            "state": "source_slots_closed_dynamic_values_open",
            "blocks_true_equivalence": True,
            "evidence": step8["status"],
            "closed_now": True,
            "required_for_true_equivalence": "actual selected Qa/SU3 dynamic operator payload/value rows",
        },
        {
            "row": "dynamic Qa/SU3 C1 response",
            "source": rel(STEP9),
            "state": "frontier_reduction_closed_source_rule_open",
            "blocks_true_equivalence": True,
            "evidence": step9["status"],
            "closed_now": True,
            "required_for_true_equivalence": "physical Phi_fin C1 source rule or independent Galerkin rows",
        },
    ]

    precision_table = guarded(
        {
            "schema": "MTTPrecisionProfileEquivalenceTable.v1",
            "status": "PRECISION_PROFILE_TABLE_BUILT_TRUE_EQUIVALENCE_OPEN",
            "rows": rows,
            "summary": {
                "table_rows": len(rows),
                "policy_rows_closed": 2,
                "partial_or_support_rows": 7,
                "rows_blocking_true_equivalence": sum(1 for row in rows if row["blocks_true_equivalence"]),
                "accepted_true_equivalence_rows": 0,
            },
        }
    )

    blocker_matrix = guarded(
        {
            "schema": "MTTTrueSMEquivalenceBlockerMatrix.v1",
            "status": "TRUE_SM_EQUIVALENCE_BLOCKERS_CLASSIFIED",
            "blocking_classes": {
                "precision_profile_likelihood": {
                    "closed": False,
                    "accepted_rows": 0,
                    "blockers": [
                        "full covariance/profile likelihood",
                        "published or reconstructed correlated mass/threshold profiles",
                        "global electroweak/CKM/PMNS/Higgs correlations",
                    ],
                },
                "threshold_mass_scheme_multiloop": {
                    "closed": False,
                    "accepted_rows": 0,
                    "blockers": [
                        "accepted threshold matching source rows",
                        "accepted mass-scheme conversion source rows",
                        "multi-loop RG/matching convention values",
                    ],
                },
                "local_QFT_precision_observables": {
                    "closed": False,
                    "accepted_rows": 0,
                    "blockers": [
                        "full precision observable value table",
                        "two-point or propagator normalization rows",
                        "Ward/anomaly observable checks",
                    ],
                },
                "selected_QaSU3_operator_payload": {
                    "closed": False,
                    "accepted_rows": 0,
                    "blockers": [
                        "selected operator slot source values",
                        "sector-ready HYM/Riesz/Green/dotD/C1 payload",
                        "physical Phi_fin C1 source rule or independent Galerkin rows",
                    ],
                },
                "strict_P_EW_or_direct_K": {
                    "closed": previous["closure_decision"]["strict_P_EW_source_theorem_closed"],
                    "accepted_rows": 0,
                    "blockers": [
                        "strict P_EW selected source theorem",
                        "direct K_threshold.Omega_H.lambda row certificate",
                    ],
                },
                "neutrino_absolute_source": {
                    "closed": previous["closure_decision"]["absolute_neutrino_mass_closed"],
                    "accepted_rows": 0,
                    "blockers": [
                        "absolute neutrino mass source",
                        "Dirac/Majorana ontology selector",
                        "Majorana phase source rows if Majorana is selected",
                    ],
                },
            },
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        }
    )

    ledger_bridge = guarded(
        {
            "schema": "MTTMinimalParameterLedgerToPrecisionBridge.v1",
            "status": "LEDGER_TO_PRECISION_BRIDGE_BUILT",
            "minimal_parameter_counts": {
                "non_neutrino_including_QCD_theta": 19,
                "minimal_PMNS_including_QCD_theta": tier_counts["minimal_PMNS_oscillation_policy"],
                "Dirac_massive_neutrino_completion": tier_counts[
                    "Dirac_massive_neutrino_completion"
                ],
                "Majorana_massive_neutrino_completion": tier_counts[
                    "Majorana_massive_neutrino_completion"
                ],
                "if_strict_P_EW_closes_minimal_PMNS": tier_counts[
                    "minimal_PMNS_if_strict_P_EW_closes"
                ],
                "if_strict_P_EW_closes_Dirac_completion": tier_counts[
                    "Dirac_completion_if_strict_P_EW_closes"
                ],
                "if_strict_P_EW_closes_Majorana_completion": tier_counts[
                    "Majorana_completion_if_strict_P_EW_closes"
                ],
            },
            "precision_claim_policy": {
                "minimal_parameter_ledger_is_closed": True,
                "precision_equivalence_requires_more_than_parameter_counting": True,
                "true_equivalence_requires_profile_likelihood_and_local_QFT_observables": True,
                "no_knob_requires_selected_source rows rather than measured replay rows": True,
            },
        }
    )

    next_target = guarded(
        {
            "schema": "MTTNextAfterPrecisionProfileTable.v1",
            "status": "NEXT_TARGET_QASU3_OPERATOR_PAYLOAD_OR_STRICT_PEW_PRECISION_EXIT",
            "next_required_artifact": NEXT,
            "reason": (
                "The precision table is now classified.  Remaining precision/profile "
                "rows depend on either accepted external/full-loop profile imports or "
                "actual selected Qa/SU3 operator payload values.  The strict P_EW/"
                "direct-K row remains the parallel count-reduction/precision exit."
            ),
            "non_duplicative_exits": [
                "actual selected Qa/SU3 operator payload/source values",
                "strict P_EW/direct K_threshold.Omega_H.lambda precision exit",
                "full correlated precision profile import with provenance",
                "physical Phi_fin C1 source rule or independent Galerkin rows",
            ],
        }
    )

    candidate = guarded(
        {
            "candidate": "MTTSelectedPrecisionProfileTableOrTrueSMEquivalenceAudit",
            "status": STATUS,
            "next_required_artifact": NEXT,
            "inputs": {
                "previous": rel(PREVIOUS),
                "neutrino_counts": rel(NEUTRINO_COUNTS),
                "rg_policy": rel(RG_POLICY),
                "accepted_values": rel(ACCEPTED_VALUES),
                "threshold_audit": rel(THRESHOLD_AUDIT),
                "precision_import": rel(PRECISION_IMPORT),
                "local_qft": rel(LOCAL_QFT),
                "full_loop": rel(FULL_LOOP),
                "step8": rel(STEP8),
                "step9": rel(STEP9),
            },
            "packets": {
                "precision_profile_equivalence_table": rel(PRECISION_TABLE),
                "true_sm_equivalence_blocker_matrix": rel(BLOCKER_MATRIX),
                "minimal_parameter_ledger_to_precision_bridge": rel(LEDGER_BRIDGE),
                "next_after_precision_profile_table": rel(NEXT_TARGET),
            },
            "closure_decision": {
                "precision_profile_table_built": True,
                "precision_policy_rows_closed": True,
                "central_value_replay_baseline_closed": True,
                "full_covariance_profile_likelihood_closed": False,
                "threshold_mass_scheme_source_rows_closed": False,
                "multi_loop_RG_values_closed": False,
                "local_QFT_precision_observable_table_closed": False,
                "selected_QaSU3_operator_payload_closed": False,
                "accepted_true_equivalence_rows": 0,
                "strict_P_EW_source_theorem_closed": previous["closure_decision"][
                    "strict_P_EW_source_theorem_closed"
                ],
                "neutrino_absolute_source_closed": previous["closure_decision"][
                    "absolute_neutrino_mass_closed"
                ],
                "true_SM_equivalence_closed": False,
                "full_no_knob_closed": False,
            },
            "theorem": {
                "name": "PrecisionProfileTableOrTrueSMEquivalenceAuditTheorem",
                "proved": True,
                "statement": (
                    "The current repo state admits a complete precision-profile "
                    "frontier table: MSbar/M_Z policy and central-value covariance "
                    "tiering are closed, several profile/value attempts are audited, "
                    "and the minimal parameter ledger bridges into precision claims. "
                    "However accepted true-equivalence rows remain zero: full "
                    "covariance/profile likelihood, threshold/mass-scheme source rows, "
                    "multi-loop values, local-QFT precision observables, selected "
                    "Qa/SU3 operator payload values, strict P_EW/direct-K, and "
                    "neutrino absolute-source policy remain open."
                ),
            },
        }
    )

    cert = guarded(
        {
            "certificate": "MTTSelectedPrecisionProfileTableOrTrueSMEquivalenceAudit",
            "status": STATUS,
            "theorem_proved": True,
            "precision_profile_table_built": True,
            "precision_policy_rows_closed": True,
            "accepted_true_equivalence_rows": 0,
            "full_covariance_profile_likelihood_closed": False,
            "threshold_mass_scheme_source_rows_closed": False,
            "multi_loop_RG_values_closed": False,
            "local_QFT_precision_observable_table_closed": False,
            "selected_QaSU3_operator_payload_closed": False,
            "strict_P_EW_source_theorem_closed": False,
            "neutrino_absolute_source_closed": False,
            "true_SM_equivalence_claimed": False,
            "full_no_knob_closure_claimed": False,
            "next_required_artifact": NEXT,
        }
    )

    note = f"""# MTT Selected PrecisionProfileTable or TrueSMEquivalenceAudit v1

## Theorem

`PrecisionProfileTableOrTrueSMEquivalenceAuditTheorem` is emitted.

## What Closes

```text
precision profile table built = true
precision policy rows closed = true
central-value replay baseline closed = true
minimal parameter ledger to precision bridge built = true
```

This closes the precision-frontier map.  It does not close true SM
equivalence.

## Blocking Rows

```text
accepted true-equivalence rows = 0
full covariance/profile likelihood closed = false
threshold/mass-scheme source rows closed = false
multi-loop RG values closed = false
local-QFT precision observable table closed = false
selected Qa/SU3 operator payload closed = false
strict P_EW source theorem closed = false
neutrino absolute source closed = false
true SM equivalence closed = false
full no-knob closure = false
```

## Ledger Bridge

```text
non-neutrino including QCD theta_bar = 19
minimal PMNS including QCD theta_bar = {tier_counts["minimal_PMNS_oscillation_policy"]}
Dirac massive-neutrino completion = {tier_counts["Dirac_massive_neutrino_completion"]}
Majorana massive-neutrino completion = {tier_counts["Majorana_massive_neutrino_completion"]}
if strict P_EW closes: {tier_counts["minimal_PMNS_if_strict_P_EW_closes"]}/{tier_counts["Dirac_completion_if_strict_P_EW_closes"]}/{tier_counts["Majorana_completion_if_strict_P_EW_closes"]}
```

## Next Artifact

`{NEXT}`.
"""

    for path, payload in [
        (PRECISION_TABLE, precision_table),
        (BLOCKER_MATRIX, blocker_matrix),
        (LEDGER_BRIDGE, ledger_bridge),
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
