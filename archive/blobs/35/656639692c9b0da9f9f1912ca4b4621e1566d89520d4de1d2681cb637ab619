"""Build accepted threshold/mass-scheme source rows or no-knob value-derivation gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_acceptedthresholdmassschemesourcerows_or_noknobvaluederivation"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SOURCE_AUDIT = PACKET_DIR / "accepted_threshold_mass_scheme_source_row_audit.packet.json"
DERIVATION = PACKET_DIR / "no_knob_value_derivation_attempt.packet.json"
PROMOTION = PACKET_DIR / "promotion_decision_after_source_row_audit.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_source_row_audit.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_AcceptedThresholdMassSchemeSourceRows_or_NoKnobValueDerivation_v1.md"

PREVIOUS = DATA / "selected_thresholdmassschemevalues_or_correlatedlikelihoodsourceimport.candidate.json"
PREVIOUS_PROMOTION = (
    DATA
    / "selected_thresholdmassschemevalues_or_correlatedlikelihoodsourceimport"
    / "precision_promotion_after_residuals_and_import.packet.json"
)
RESIDUALS = (
    DATA
    / "selected_thresholdmassschemevalues_or_correlatedlikelihoodsourceimport"
    / "threshold_mass_scheme_residual_values.packet.json"
)
BACKLOG = DATA / "no_knob_upgrade_backlog.candidate.json"
SM_INTERFACE = DATA / "sm_sector_embedding_interface.candidate.json"
SM_LEDGER = DATA / "sm_parity_closure_ledger.candidate.json"
QASU3_PARITY = DATA / "selected_qasu3sourcepacket_or_finalsmparityclosure.candidate.json"
VALUE_PACKET = (
    DATA
    / "selected_acceptedcommonscaleyukawahiggsvalues_or_profilelikelihoodexecution"
    / "versioned_common_scale_yukawa_higgs_values.packet.json"
)

STATUS = (
    "MTT_SELECTED_ACCEPTEDTHRESHOLDMASSSCHEMESOURCEROWS_OR_NOKNOBVALUEDERIVATION_"
    "BUILT_SOURCE_ROW_AUDIT_NO_KNOB_DERIVATION_OPEN"
)
NEXT = "MTT_Selected_ValueSourceDerivationObligationKernel_or_ExternalThresholdImportManifest_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing threshold source-row/no-knob sources: " + ", ".join(missing))


def backlog_by_id(backlog: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {row["id"]: row for row in backlog["backlog_rows"]}


def ledger_row_by_object(ledger: dict[str, Any], name: str) -> dict[str, Any]:
    for row in ledger["ledger"]:
        if row["physics_object"] == name:
            return row
    raise KeyError(name)


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_PROMOTION,
        RESIDUALS,
        BACKLOG,
        SM_INTERFACE,
        SM_LEDGER,
        QASU3_PARITY,
        VALUE_PACKET,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_promotion = load(PREVIOUS_PROMOTION)
    residuals = load(RESIDUALS)
    backlog = load(BACKLOG)
    sm_interface = load(SM_INTERFACE)
    sm_ledger = load(SM_LEDGER)
    qasu3 = load(QASU3_PARITY)
    values = load(VALUE_PACKET)

    rows = backlog_by_id(backlog)
    gauge_threshold = rows["gauge_threshold_no_knob"]
    yukawa_higgs = rows["yukawa_cp_higgs_no_knob"]
    selected_packet = rows["selected_sm_packet"]
    qft_functor = rows["local_qft_functor"]

    candidate_rows = [
        {
            "id": "residual_value_table",
            "source": rel(RESIDUALS),
            "support_present": residuals["summary"]["all_residuals_finite"],
            "row_type": "computed residual audit",
            "can_promote_to_accepted_threshold_mass_scheme_source": False,
            "why_not": [
                "residual rows compare already-admitted replay values",
                "residual rows are not a threshold matching convention",
                "residual rows are not selected MTT source data",
            ],
        },
        {
            "id": "gauge_threshold_no_knob_backlog",
            "source": "no_knob_upgrade_backlog.gauge_threshold_no_knob",
            "support_present": gauge_threshold["corpus_backed"],
            "row_type": "corpus/repo support for threshold kernels",
            "can_promote_to_accepted_threshold_mass_scheme_source": gauge_threshold["closed_now"],
            "why_not": [
                gauge_threshold["upgrade_needed"],
            ],
        },
        {
            "id": "yukawa_higgs_no_knob_backlog",
            "source": "no_knob_upgrade_backlog.yukawa_cp_higgs_no_knob",
            "support_present": yukawa_higgs["corpus_backed"],
            "row_type": "corpus/repo support for Yukawa/Higgs source kernels",
            "can_promote_to_accepted_threshold_mass_scheme_source": yukawa_higgs["closed_now"],
            "why_not": [
                yukawa_higgs["upgrade_needed"],
            ],
        },
        {
            "id": "sm_embedding_measured_slot_policy",
            "source": rel(SM_INTERFACE),
            "support_present": sm_interface["gate_results"][
                "couplings_yukawas_cp_higgs_numbers_are_downstream_slots"
            ],
            "row_type": "policy guardrail",
            "can_promote_to_accepted_threshold_mass_scheme_source": False,
            "why_not": [
                "SM interface explicitly keeps gauge couplings, Yukawa matrices, CP phases, Higgs numerical parameters, and RG thresholds downstream measured slots unless a no-knob source is supplied.",
            ],
        },
        {
            "id": "qasu3_sm_parity_source_rows",
            "source": rel(QASU3_PARITY),
            "support_present": qasu3["closure_decision"]["SM_parity_closed"],
            "row_type": "SM-parity source packet support",
            "can_promote_to_accepted_threshold_mass_scheme_source": False,
            "why_not": [
                "Qa/SU3 closes the parity-interface source packet, not numerical Yukawa/Higgs threshold or mass-scheme conversion rows.",
            ],
        },
        {
            "id": "versioned_value_packet",
            "source": rel(VALUE_PACKET),
            "support_present": values["accepted_as_versioned_common_scale_candidate_values"],
            "row_type": "versioned value/profile packet",
            "can_promote_to_accepted_threshold_mass_scheme_source": False,
            "why_not": [
                "value packet is accepted as first-pass/profile input and SM-parity replay, not a no-knob source derivation.",
            ],
        },
    ]

    promotable = [row for row in candidate_rows if row["can_promote_to_accepted_threshold_mass_scheme_source"]]
    source_audit = {
        "schema": "MTTAcceptedThresholdMassSchemeSourceRowAudit.v1",
        "status": "CANDIDATE_SOURCE_ROWS_AUDITED_NONE_ACCEPTED_FOR_THRESHOLD_MASS_SCHEME",
        "candidate_rows": candidate_rows,
        "candidate_count": len(candidate_rows),
        "support_present_count": sum(1 for row in candidate_rows if row["support_present"]),
        "promotable_count": len(promotable),
        "accepted_threshold_matching_source_rows": [],
        "accepted_mass_scheme_conversion_source_rows": [],
        "accepted_source_rows_present": False,
        "guardrail": sm_interface["embedding_rules"][3],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(SOURCE_AUDIT, source_audit)

    derivation_obligations = [
        {
            "id": "selected_overlap_or_operator_kernel",
            "description": "Emit selected overlap/Higgs/threshold kernel rows from the same branch as the value packet.",
            "closed": False,
            "support": yukawa_higgs["status"],
        },
        {
            "id": "threshold_response_rule",
            "description": "Bridge internal determinant/threshold candidates to physical threshold response without observed-value selection.",
            "closed": False,
            "support": gauge_threshold["status"],
        },
        {
            "id": "selected_sm_packet_attachment",
            "description": "Attach the value-source rows to the selected SM representation/operator packet.",
            "closed": False,
            "support": selected_packet["status"],
        },
        {
            "id": "local_qft_renormalization_functor",
            "description": "Provide a local-QFT functor that types the renormalization/matching rows as observables rather than source selectors.",
            "closed": False,
            "support": qft_functor["status"],
        },
        {
            "id": "accepted_external_source_escape_hatch",
            "description": "Alternatively import accepted external threshold/mass-scheme/profile source rows with provenance and basis map.",
            "closed": False,
            "support": "No imported source row is present in the current repo.",
        },
    ]
    derivation = {
        "schema": "MTTNoKnobValueDerivationAttempt.v1",
        "status": "NO_KNOB_VALUE_DERIVATION_ATTEMPTED_OBLIGATION_KERNEL_OPEN",
        "attempted_derivation": {
            "Yukawa_Higgs_value_source_derivation": False,
            "threshold_matching_value_source_derivation": False,
            "mass_scheme_conversion_value_source_derivation": False,
            "multi_loop_convention_source_derivation": False,
        },
        "obligations": derivation_obligations,
        "closed_obligation_count": sum(1 for row in derivation_obligations if row["closed"]),
        "obligation_count": len(derivation_obligations),
        "why_not_proved_now": [
            "current support identifies mechanisms and candidate routes, but not actual selected source rows",
            "SM embedding policy bars treating measured or benchmark Yukawa/Higgs/threshold values as selected source rows",
            "residual values are finite but downstream, so they cannot derive themselves",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "no_knob_value_derivation_closed": False,
    }
    write_json(DERIVATION, derivation)

    remaining_hard_failures = [
        "accepted_threshold_matching_source_rows",
        "accepted_mass_scheme_conversion_source_rows",
        "no_knob_value_source_derivation",
        "external_correlated_likelihood_or_threshold_source_import",
        "multi_loop_threshold_convention_source_rows",
    ]
    promotion = {
        "schema": "MTTPromotionDecisionAfterSourceRowAudit.v1",
        "status": "SOURCE_ROW_AUDIT_DONE_NO_ACCEPTED_SOURCE_ROWS_TRUE_PRECISION_OPEN",
        "previous_remaining_hard_failures": previous_promotion["remaining_hard_failures"],
        "promotion_tests": {
            "candidate_source_rows_audited": True,
            "support_present_for_no_knob_routes": source_audit["support_present_count"] > 0,
            "accepted_threshold_matching_source_rows": False,
            "accepted_mass_scheme_conversion_source_rows": False,
            "no_knob_value_source_derivation_closed": False,
            "external_correlated_likelihood_or_threshold_source_imported": False,
            "multi_loop_threshold_convention_source_rows": False,
        },
        "remaining_hard_failures": remaining_hard_failures,
        "promotion_decision": {
            "source_row_audit_closed": True,
            "accepted_threshold_mass_scheme_source_layer_closed": False,
            "accepted_for_true_precision_equivalence": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "reason": (
            "All available candidate routes are now typed against the SM embedding policy. Support exists, "
            "but no route emits accepted threshold/mass-scheme source rows or a no-knob derivation of the "
            "Yukawa/Higgs value rows."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(PROMOTION, promotion)

    cutset = {
        "schema": "MTTNextCutsetAfterSourceRowAudit.v1",
        "status": "SOURCE_ROW_AUDIT_DONE_VALUE_DERIVATION_OBLIGATION_KERNEL_REQUIRED",
        "closed_now": [
            "candidate threshold/mass-scheme source rows audited",
            "SM embedding measured-slot guardrail applied to all candidates",
            "no-knob value derivation obligations enumerated",
            "precision promotion rerun after source-row audit",
        ],
        "still_open": [
            "selected overlap/operator threshold kernel rows",
            "threshold response rule from selected branch",
            "accepted mass-scheme conversion source rows",
            "external threshold/likelihood source import with provenance",
            "no-knob MTT derivation of Yukawa/Higgs values",
        ],
        "recommended_next": {
            "artifact": NEXT,
            "reason": (
                "The remaining proof obligation is now atomic: supply a value-source derivation kernel "
                "or an external threshold/import manifest with accepted source rows and provenance."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    yukawa_ledger = ledger_row_by_object(sm_ledger, "Yukawa matrices and masses")
    higgs_ledger = ledger_row_by_object(sm_ledger, "Higgs sector")
    candidate = {
        "candidate": "MTTSelectedAcceptedThresholdMassSchemeSourceRowsOrNoKnobValueDerivation",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "accepted_threshold_mass_scheme_source_row_audit": rel(SOURCE_AUDIT),
            "no_knob_value_derivation_attempt": rel(DERIVATION),
            "promotion_decision_after_source_row_audit": rel(PROMOTION),
            "next_cutset_after_source_row_audit": rel(CUTSET),
        },
        "theorem": {
            "name": "SourceRowAuditAndNoKnobObligationKernelTheorem",
            "proved": True,
            "statement": (
                "The available threshold/mass-scheme/Yukawa/Higgs candidates can be audited against the SM "
                "embedding measured-slot policy. The audit finds support for future no-knob routes, but no "
                "accepted threshold/mass-scheme source rows and no closed no-knob value derivation. Therefore "
                "true precision SM equivalence remains open until a value-source derivation kernel or accepted "
                "external source-row import is supplied."
            ),
        },
        "ledger_context": {
            "yukawa_masses_remaining_gap": yukawa_ledger["remaining_gap"],
            "higgs_remaining_gap": higgs_ledger["remaining_gap"],
        },
        "what_closes_now": {
            "candidate_source_rows_audited": True,
            "no_knob_value_derivation_obligations_enumerated": True,
            "measured_slot_guardrail_applied": True,
            "precision_promotion_rerun_after_source_row_audit": True,
        },
        "what_remains_open": {
            "accepted_threshold_matching_source_rows": True,
            "accepted_mass_scheme_conversion_source_rows": True,
            "no_knob_Yukawa_Higgs_value_source_derivation": True,
            "external_threshold_or_likelihood_source_import": True,
            "multi_loop_threshold_convention_source_rows": True,
            "true_SM_equivalence_closure": True,
            "full_no_knob_closure": True,
        },
        "closure_decision": {
            "source_row_audit_closed": True,
            "accepted_threshold_mass_scheme_source_layer_closed": False,
            "no_knob_value_derivation_closed": False,
            "accepted_for_true_precision_equivalence": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_AcceptedThresholdMassSchemeSourceRows_or_NoKnobValueDerivation_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected AcceptedThresholdMassSchemeSourceRows or NoKnobValueDerivation v1

Status: `{STATUS}`.

This artifact audits candidate threshold/mass-scheme source rows against the SM
embedding measured-slot policy.

```text
candidate rows audited = {source_audit["candidate_count"]}
support-present rows   = {source_audit["support_present_count"]}
promotable rows        = {source_audit["promotable_count"]}
```

Result:

```text
accepted threshold/mass-scheme source rows: false
no-knob value derivation closed: false
true SM equivalence: open
```

The useful closure is the obligation kernel: the next artifact must either emit
selected value-source derivation rows or import accepted external source rows
with provenance and a basis map.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
