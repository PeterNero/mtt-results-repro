"""Build the MTT empirical equivalence ledger artifact."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

INPUT = DATA / "qm_qft_gr_recovery_interface.candidate.json"
OUTPUT_DATA = DATA / "empirical_equivalence_ledger.candidate.json"
OUTPUT_CERT = CERTS / "empirical_equivalence_ledger_certificate.json"
OUTPUT_NOTE = CORPUS / "MTT_Empirical_Equivalence_Ledger_v1.md"


LEDGER_ROWS = [
    {
        "domain": "QM measurement and records",
        "accepted_reference": "Standard QM Hilbert/observable/Born/record-update practice.",
        "mtt_parity_requirement": "Expose state carrier, observable map, and measurement/record rule with declared conventions.",
        "measured_inputs_allowed": ["experimental records", "state-preparation/calibration data"],
        "must_reproduce": ["Born-probability predictions at parity standard", "record/update behavior for compared experiments"],
        "not_allowed": ["using observed outcome frequencies to select the MTT source"],
        "status": "INTERFACE_DECLARED_EMPIRICAL_AUDIT_OPEN",
        "no_knob_target": "derive Born weights and record selection from MTT admissibility/coherence",
    },
    {
        "domain": "local QFT observables",
        "accepted_reference": "Local operator/correlator/S-matrix practice with renormalization scheme and scale.",
        "mtt_parity_requirement": "Declare local observable functor, gauge action, RG scheme, and parameter slots.",
        "measured_inputs_allowed": ["renormalized couplings", "field masses where SM treats them as measured", "experimental cross sections for comparison"],
        "must_reproduce": ["locality/microcausality interface where relevant", "correlator or scattering predictions after measured inputs"],
        "not_allowed": ["fitting thresholds after residuals", "treating benchmark correlators as selected operator spectra"],
        "status": "INTERFACE_DECLARED_EMPIRICAL_AUDIT_OPEN",
        "no_knob_target": "derive local QFT functor and threshold kernels from selected modal/operator data",
    },
    {
        "domain": "SM gauge and representation sector",
        "accepted_reference": "SM gauge group, chiral representations, anomaly cancellation, and three-family structure.",
        "mtt_parity_requirement": "Declare selected gauge carrier, representation packet, family index, Higgs carrier, and anomaly checks.",
        "measured_inputs_allowed": ["gauge couplings after packet selection", "masses and mixings after representation/basis declaration"],
        "must_reproduce": ["SU3 x SU2 x U1 sector interface", "SM representation content", "anomaly consistency", "three families"],
        "not_allowed": ["using couplings or masses to choose the gauge group, family count, or representations"],
        "status": "INTERFACE_DECLARED_ACTUAL_PACKET_OPEN",
        "no_knob_target": "derive the actual selected SM packet from MTT source data",
    },
    {
        "domain": "Yukawa, CP, and Higgs phenomenology",
        "accepted_reference": "SM uses measured Yukawa matrices, CP phases, Higgs vev/mass/quartic with scheme and scale conventions.",
        "mtt_parity_requirement": "Admit numerical values only as typed downstream slots after SM packet declaration.",
        "measured_inputs_allowed": ["Yukawa matrices", "CKM/PMNS phases and angles", "Higgs potential parameters"],
        "must_reproduce": ["mass and mixing calculations from admitted slots", "basis and phase convention consistency"],
        "not_allowed": ["benchmark matrices as selected source matrices", "target phase fitting as source selection"],
        "status": "PARITY_INPUT_ALLOWED_NO_KNOB_OPEN",
        "no_knob_target": "derive Yukawa, CP, and Higgs parameters from selected overlap/operator kernels",
    },
    {
        "domain": "GR and stress-energy coupling",
        "accepted_reference": "Metric GR with stress-energy coupling, Bianchi consistency, and measured dimensional anchors.",
        "mtt_parity_requirement": "Declare metric/effective metric map, curvature, stress-energy interface, and dimensionful anchor slots.",
        "measured_inputs_allowed": ["Newton scale", "cosmological parameters", "boundary/initial data at parity standard"],
        "must_reproduce": ["GR field-equation interface at parity standard", "stress-energy conservation/Bianchi consistency"],
        "not_allowed": ["claiming physical Newton scale from internal dimensionless normalization"],
        "status": "INTERFACE_DECLARED_EMPIRICAL_AUDIT_OPEN",
        "no_knob_target": "derive metric dynamics and physical absolute normalization from selected source data",
    },
    {
        "domain": "units and dimensionful constants",
        "accepted_reference": "Physics practice separates units, measured dimensional anchors, and dimensionless predictions.",
        "mtt_parity_requirement": "Declare unit registry, conversion rules, uncertainty propagation, and physical anchor slots.",
        "measured_inputs_allowed": ["unit conventions", "dimensionful measured anchors"],
        "must_reproduce": ["consistent dimensional analysis", "no hidden physical scale in conventions"],
        "not_allowed": ["using unit choice as a hidden fitted constant"],
        "status": "PARITY_INPUT_ALLOWED_PHYSICAL_NO_KNOB_OPEN",
        "no_knob_target": "derive physical absolute anchor without measured dimensional input",
    },
]

LEDGER_RULES = [
    "Each empirical comparison must name its accepted reference practice.",
    "Each comparison must state which measured inputs are admitted and why that is SM-parity rather than no-knob closure.",
    "Each comparison must identify what MTT must reproduce after admitted inputs are declared.",
    "Each comparison must list forbidden uses of empirical data.",
    "No row may use empirical success to select source structure after the fact.",
    "No row may claim no-knob closure unless the selected internal calculation is present.",
]

ACCEPTANCE_SUMMARY = {
    "interfaces_ready_for_empirical_audit": True,
    "empirical_values_classified_as_downstream": True,
    "actual_numeric_equivalence_computed": False,
    "actual_selected_sm_packet_supplied": False,
    "no_knob_constants_derived": False,
    "sm_parity_closure_claimed": False,
}


def load_input() -> dict[str, object]:
    return json.loads(INPUT.read_text(encoding="utf-8"))


def build_candidate() -> dict[str, object]:
    input_data = load_input()
    return {
        "candidate": "MTTEmpiricalEquivalenceLedger",
        "status": "EMPIRICAL_EQUIVALENCE_LEDGER_BUILT_ACTUAL_AUDIT_OPEN",
        "input_status": input_data["status"],
        "ledger_rows": LEDGER_ROWS,
        "ledger_rules": LEDGER_RULES,
        "acceptance_summary": ACCEPTANCE_SUMMARY,
        "gate_results": {
            "empirical_domains_listed": True,
            "accepted_reference_practice_declared": True,
            "measured_inputs_classified_downstream": True,
            "must_reproduce_obligations_declared": True,
            "forbidden_empirical_shortcuts_declared": True,
            "actual_numeric_equivalence_computed": False,
            "actual_selected_sm_packet_supplied": False,
            "no_knob_constants_derived": False,
            "sm_parity_closure_claimed": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": "MTT_No_Knob_Upgrade_Backlog_v1",
        "target_fitting_used": False,
    }


def build_certificate(candidate: dict[str, object]) -> dict[str, object]:
    return {
        "certificate": "MTTEmpiricalEquivalenceLedger",
        "status": "MTT_EMPIRICAL_EQUIVALENCE_LEDGER_BUILT_ACTUAL_AUDIT_OPEN",
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "what_closes": {
            "empirical_domain_ledger": True,
            "accepted_reference_practice_registry": True,
            "measured_input_vs_reproduction_boundary": True,
            "forbidden_empirical_shortcut_registry": True,
            "parity_audit_obligation_map": True,
        },
        "what_remains_open": {
            "actual_numeric_empirical_equivalence": True,
            "actual_selected_SM_packet": True,
            "actual_anomaly_calculation": True,
            "actual_QM_QFT_GR_derivation_strengthening": True,
            "no_knob_upgrade_backlog": True,
            "no_knob_constants": True,
            "sm_parity_closed": False,
        },
        "next_required_artifact": candidate["next_required_artifact"],
        "closure_claimed": False,
        "target_fitting_used": False,
    }


def render_note(candidate: dict[str, object], certificate: dict[str, object]) -> str:
    rows = []
    for row in candidate["ledger_rows"]:
        rows.append(
            f"### {row['domain']}\n\n"
            f"- Accepted reference: {row['accepted_reference']}\n"
            f"- MTT parity requirement: {row['mtt_parity_requirement']}\n"
            f"- Measured inputs allowed: {', '.join(row['measured_inputs_allowed'])}\n"
            f"- Must reproduce: {', '.join(row['must_reproduce'])}\n"
            f"- Not allowed: {', '.join(row['not_allowed'])}\n"
            f"- Status: `{row['status']}`\n"
            f"- No-knob target: {row['no_knob_target']}\n"
        )
    rules = "\n".join(f"- {rule}" for rule in candidate["ledger_rules"])
    summary = "\n".join(f"- `{name}`: {value}" for name, value in candidate["acceptance_summary"].items())
    closes = "\n".join(f"- {name}" for name, value in certificate["what_closes"].items() if value)
    open_items = "\n".join(f"- {name}" for name, value in certificate["what_remains_open"].items() if value)
    return f"""# MTT Empirical Equivalence Ledger v1

## Purpose

This artifact records what MTT must match to be at SM-parity with QM, QFT, SM,
GR, and dimensional physics.

It does not compute the actual numerical empirical equivalence yet.  It closes
the audit ledger: what may be measured input, what must be reproduced, what is
forbidden, and what remains open.

## Ledger Rules

{rules}

## Empirical Domains

{chr(10).join(rows)}

## Acceptance Summary

{summary}

## Ledger Theorem

MTT has a complete empirical-equivalence audit interface when every comparison
domain declares accepted reference practice, admitted measured inputs,
reproduction obligations, forbidden empirical shortcuts, and no-knob upgrade
targets.

This artifact builds that ledger.  It does not claim that the actual numerical
checks have been carried out, and it does not claim full SM-parity closure.

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
