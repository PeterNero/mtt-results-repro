"""Build the MTT core axioms and measured-parameter interface artifact."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

LEDGER = DATA / "sm_parity_closure_ledger.candidate.json"
OUTPUT_DATA = DATA / "core_axioms_measured_parameter_interface.candidate.json"
OUTPUT_CERT = CERTS / "core_axioms_measured_parameter_interface_certificate.json"
OUTPUT_NOTE = CORPUS / "MTT_Core_Axioms_and_Measured_Parameter_Interface_v1.md"


PARAMETER_CLASSES = {
    "MEASURED_PARITY_INPUT": {
        "role": "A value admitted at the same standard as SM/QFT/GR measured parameters.",
        "allowed": [
            "May feed downstream sector computations after declaration.",
            "May be used to compare MTT recovery with empirical physics.",
        ],
        "forbidden": [
            "May not select the source, branch, representation packet, operator packet, or topology.",
            "May not be cited as a no-knob derivation.",
        ],
    },
    "SELECTED_SOURCE_DATA": {
        "role": "Internal MTT/corpus data selected before empirical parameter use.",
        "allowed": [
            "May select sectors, operators, admissible branches, and representation packets.",
            "May be upgraded into no-knob derivations when actual maps are supplied.",
        ],
        "forbidden": [
            "May not be chosen because it matches a measured residual.",
        ],
    },
    "DIAGNOSTIC_FIXTURE": {
        "role": "Prototype, validator, benchmark, or identity map used to test machinery.",
        "allowed": [
            "May test code paths, algebraic identities, and audit behavior.",
        ],
        "forbidden": [
            "May not count as physical data.",
            "May not be promoted into a parity prediction or no-knob proof.",
        ],
    },
    "NO_KNOB_TARGET": {
        "role": "A future derivation obligation replacing a measured parity input.",
        "allowed": [
            "May record the intended internal selector, kernel, determinant, or overlap source.",
        ],
        "forbidden": [
            "May not be marked closed until the actual selected computation is present.",
        ],
    },
}

SLOT_SCHEMA_REQUIRED_FIELDS = [
    "name",
    "sector",
    "kind",
    "value_domain",
    "units",
    "convention",
    "uncertainty",
    "provenance",
    "allowed_use",
    "forbidden_use",
    "no_knob_target",
    "downstream_artifacts",
]

MEASURED_PARAMETER_ADMISSION_RULES = [
    "The slot must be declared before any downstream computation that uses it.",
    "The slot must be typed by sector and kind.",
    "The value domain, units, convention, uncertainty, and provenance must be explicit.",
    "The value may be used only for SM-parity recovery or empirical comparison.",
    "The value may not select a source, branch, operator packet, topology, quotient, or representation.",
    "The value may not be reused as evidence for no-knob closure.",
    "Every measured slot must carry a no-knob replacement target.",
    "Diagnostic fixtures and identity validators must be excluded from physical parameter slots.",
]

FORBIDDEN_SHORTCUTS = [
    "source selection by measured constants",
    "branch or quotient selection by target residual",
    "post-hoc fitting after observing the desired output",
    "direct q79/S3 import as a Qa/SU3 proof source",
    "generic existence theorem replacing actual maps",
    "identity rho_E or diagnostic validator treated as physical data",
    "benchmark Yukawa, CKM, PMNS, threshold, or mass entries treated as selected matrices",
]

AXIOMS = {
    "sector_axiom": "An MTT sector S is a typed modal package with carriers, maps, admissibility data, and declared interfaces.",
    "admissibility_axiom": "Adm(S) is checked before measured parity inputs are admitted; measured values cannot establish Adm(S).",
    "selection_axiom": "Sel(S) or Sigma_S records source data selected by MTT/corpus structure, not by empirical target fitting.",
    "observable_axiom": "Obs_S maps selected sector data and admitted parameters to observables with explicit conventions.",
    "measured_parameter_axiom": "Param_S contains typed slots whose measured values may enter only as SM-parity inputs.",
    "non_selection_axiom": "Measured parity inputs are downstream data and cannot choose source, topology, quotient, operator packet, or branch.",
    "upgrade_axiom": "Every measured parity input has a no-knob upgrade target that remains open until the selected internal computation is supplied.",
}

SECTOR_INTERFACES = {
    "QM": {
        "interface": "Hilbert/state, observable, Born/record, and update slots.",
        "parity_policy": "Measurement rules may be axiomatized for SM-parity; no-knob target is record/Born selection from admissibility.",
    },
    "QFT": {
        "interface": "Field content, gauge action, local operator algebra, renormalized parameter slots, and scale conventions.",
        "parity_policy": "Renormalized couplings may be measured parity inputs after sector selection.",
    },
    "SM": {
        "interface": "Gauge group, representation packet, Higgs carrier, Yukawa matrices, mixing matrices, CP phases, and RG scheme.",
        "parity_policy": "Gauge/Yukawa/CP/Higgs values may be measured inputs only after the SM sector embedding is declared.",
    },
    "GR": {
        "interface": "Metric, connection/curvature, stress-energy coupling, Newton scale, cosmological/boundary slots.",
        "parity_policy": "Dimensionful anchors may be measured for parity while physical absolute normalization remains a no-knob target.",
    },
    "Units": {
        "interface": "Unit system, conversion anchors, dimensional conventions, and uncertainty propagation.",
        "parity_policy": "Dimensionful values require units and provenance; unit choices cannot be hidden knobs.",
    },
}

EXAMPLE_SLOTS = [
    {
        "name": "alpha_i(mu)",
        "sector": "SM/QFT",
        "kind": "gauge coupling",
        "value_domain": "positive real running parameter",
        "units": "dimensionless",
        "convention": "renormalization scheme and scale required",
        "uncertainty": "required for measured value",
        "provenance": "external measurement or future no-knob source",
        "allowed_use": "SM-parity running and comparison after sector declaration",
        "forbidden_use": "selecting the gauge packet or threshold kernel",
        "no_knob_target": "selected threshold/local determinant spectrum",
        "downstream_artifacts": ["MTT_SM_Sector_Embedding_Interface_v1", "MTT_Empirical_Equivalence_Ledger_v1"],
    },
    {
        "name": "Y_u, Y_d, Y_e",
        "sector": "SM",
        "kind": "Yukawa matrix",
        "value_domain": "complex matrices with stated basis convention",
        "units": "dimensionless in standard normalization",
        "convention": "basis, phase, RG scale, and scheme required",
        "uncertainty": "required for measured entries",
        "provenance": "external mass/mixing extraction or future selected overlap kernel",
        "allowed_use": "SM-parity masses and mixings after representation packet declaration",
        "forbidden_use": "constructing the representation packet or family count",
        "no_knob_target": "selected overlap/operator kernels",
        "downstream_artifacts": ["MTT_SM_Sector_Embedding_Interface_v1"],
    },
    {
        "name": "G_N",
        "sector": "GR/Units",
        "kind": "dimensionful anchor",
        "value_domain": "positive real with unit convention",
        "units": "m^3 kg^-1 s^-2 or equivalent",
        "convention": "unit system and conversion anchors required",
        "uncertainty": "required for measured value",
        "provenance": "external measurement or future selected modal-gap anchor",
        "allowed_use": "SM-parity gravitational normalization",
        "forbidden_use": "claiming physical no-knob absolute scale",
        "no_knob_target": "modal gap or selected dimensional anchor",
        "downstream_artifacts": ["MTT_QM_QFT_GR_Recovery_Interface_v1"],
    },
]


def load_ledger() -> dict[str, object]:
    return json.loads(LEDGER.read_text(encoding="utf-8"))


def build_candidate() -> dict[str, object]:
    ledger = load_ledger()
    return {
        "candidate": "MTTCoreAxiomsMeasuredParameterInterface",
        "status": "CORE_AXIOMS_MEASURED_PARAMETER_INTERFACE_BUILT_SM_PARITY_OPEN",
        "input_status": ledger["status"],
        "axioms": AXIOMS,
        "parameter_classes": PARAMETER_CLASSES,
        "slot_schema_required_fields": SLOT_SCHEMA_REQUIRED_FIELDS,
        "measured_parameter_admission_rules": MEASURED_PARAMETER_ADMISSION_RULES,
        "forbidden_shortcuts": FORBIDDEN_SHORTCUTS,
        "sector_interfaces": SECTOR_INTERFACES,
        "example_slots": EXAMPLE_SLOTS,
        "gate_results": {
            "core_axioms_stated": True,
            "measured_parameter_interface_defined": True,
            "measured_inputs_do_not_select_sources": True,
            "no_knob_upgrade_targets_required": True,
            "diagnostic_fixtures_excluded": True,
            "sm_parity_closure_claimed": False,
            "no_knob_closure_claimed": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": "MTT_SM_Sector_Embedding_Interface_v1",
        "target_fitting_used": False,
    }


def build_certificate(candidate: dict[str, object]) -> dict[str, object]:
    return {
        "certificate": "MTTCoreAxiomsMeasuredParameterInterface",
        "status": "MTT_CORE_AXIOMS_MEASURED_PARAMETER_INTERFACE_BUILT_SM_PARITY_OPEN",
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "what_closes": {
            "core_axiom_scaffold": True,
            "measured_parameter_admission_policy": True,
            "parameter_slot_schema": True,
            "forbidden_shortcuts": True,
            "no_knob_upgrade_obligation": True,
        },
        "what_remains_open": {
            "SM_sector_embedding_theorem": True,
            "QM_QFT_GR_recovery_theorem": True,
            "empirical_equivalence_ledger": True,
            "no_knob_constants": True,
            "sm_parity_closed": False,
        },
        "next_required_artifact": candidate["next_required_artifact"],
        "closure_claimed": False,
        "target_fitting_used": False,
    }


def render_note(candidate: dict[str, object], certificate: dict[str, object]) -> str:
    axioms = "\n".join(f"- `{name}`: {text}" for name, text in candidate["axioms"].items())
    rules = "\n".join(f"- {rule}" for rule in candidate["measured_parameter_admission_rules"])
    shortcuts = "\n".join(f"- {shortcut}" for shortcut in candidate["forbidden_shortcuts"])
    classes = "\n".join(
        f"- `{name}`: {body['role']}" for name, body in candidate["parameter_classes"].items()
    )
    sectors = "\n".join(
        f"- `{name}`: {body['interface']} Policy: {body['parity_policy']}"
        for name, body in candidate["sector_interfaces"].items()
    )
    schema = ", ".join(candidate["slot_schema_required_fields"])
    closes = "\n".join(f"- {name}" for name, value in certificate["what_closes"].items() if value)
    open_items = "\n".join(f"- {name}" for name, value in certificate["what_remains_open"].items() if value)
    return f"""# MTT Core Axioms and Measured-Parameter Interface v1

## Purpose

This artifact closes the SM-parity measured-input policy.  It does not close
SM-parity itself, and it does not claim no-knob derivation of constants.

SM-parity means MTT may admit measured values at the same standard used by
SM/QFT/GR, but only as typed downstream data.  No-knob closure remains the
stronger target: every measured value must keep a replacement target from
selected internal MTT data.

## Core Axioms

{axioms}

## Parameter Classes

{classes}

## Slot Schema

Every measured parity slot must declare:

```text
{schema}
```

## Admission Rules

{rules}

## Forbidden Shortcuts

{shortcuts}

## Sector Interfaces

{sectors}

## Theorem

The measured-parameter interface is admissible for SM-parity iff each measured
value is declared as a typed slot before downstream use, carries units,
convention, uncertainty, provenance, and a no-knob upgrade target, and is not
used to select the MTT source, topology, quotient, operator packet, branch, or
representation.

Therefore this artifact permits measured constants as SM-parity data while
blocking target fitting and blocking their reuse as no-knob proof.

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
