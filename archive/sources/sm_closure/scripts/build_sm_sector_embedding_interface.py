"""Build the MTT SM sector embedding interface artifact."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

INPUT = DATA / "core_axioms_measured_parameter_interface.candidate.json"
OUTPUT_DATA = DATA / "sm_sector_embedding_interface.candidate.json"
OUTPUT_CERT = CERTS / "sm_sector_embedding_interface_certificate.json"
OUTPUT_NOTE = CORPUS / "MTT_SM_Sector_Embedding_Interface_v1.md"


SELECTED_PACKET_FIELDS = {
    "sector_name": "SM",
    "gauge_carrier": "SU3 x SU2 x U1 or a selected MTT packet mapped to that gauge carrier.",
    "representation_packet": "Typed fermion and Higgs representation content, including conjugates and chirality convention.",
    "family_index": "A declared three-family index or selected internal replacement.",
    "operator_packet": "Covariant derivative, kinetic operators, Higgs/Yukawa operator slots, gauge curvature, and anomaly operators.",
    "anomaly_conditions": "Gauge, mixed, and gravitational anomaly cancellation checks.",
    "locality_limit": "The rule or functor by which the modal packet presents local QFT observables.",
    "renormalization_interface": "Scale, scheme, running-parameter slots, and matching conventions.",
    "measured_slot_boundary": "The exact point after which measured couplings, Yukawas, phases, and Higgs parameters may enter.",
}

EMBEDDING_RULES = [
    "The SM sector packet must be selected before measured SM numerical values are admitted.",
    "Gauge group and representation content are selected source data, not measured parity inputs.",
    "Family count is selected source data for SM-parity; measured masses cannot establish it.",
    "Gauge couplings, Yukawa matrices, CP phases, Higgs potential parameters, and RG thresholds are downstream measured slots unless a no-knob source is supplied.",
    "The selected packet must declare anomaly and consistency checks before empirical comparison.",
    "The embedding must expose local QFT observables through an explicit observable map Obs_SM.",
    "Every measured SM slot must inherit the slot schema from the measured-parameter interface.",
]

SM_REQUIRED_COMPONENTS = {
    "gauge_group": {
        "status": "SELECTED_SOURCE_DATA_REQUIRED",
        "parity_role": "Must be declared as the SM gauge carrier before measured couplings enter.",
        "no_knob_target": "derive SU3 x SU2 x U1 from selected modal/topological/operator packet",
    },
    "fermion_representations": {
        "status": "SELECTED_SOURCE_DATA_REQUIRED",
        "parity_role": "Must list chiral representation content and conjugation conventions.",
        "no_knob_target": "derive representation packet and anomaly cancellation from selected topology/monad/section data",
    },
    "three_generations": {
        "status": "SELECTED_SOURCE_DATA_REQUIRED",
        "parity_role": "May be asserted as SM-parity source structure, but not inferred from masses.",
        "no_knob_target": "derive family index from selected internal packet",
    },
    "higgs_carrier": {
        "status": "SELECTED_SOURCE_DATA_REQUIRED",
        "parity_role": "Must define Higgs representation and electroweak breaking interface.",
        "no_knob_target": "derive Higgs projector/carrier from selected MTT source",
    },
    "gauge_couplings": {
        "status": "MEASURED_PARITY_INPUT_ALLOWED_AFTER_PACKET_SELECTION",
        "parity_role": "Measured running parameters with scheme and scale.",
        "no_knob_target": "derive threshold kernels and absolute normalization from selected operator data",
    },
    "yukawa_matrices": {
        "status": "MEASURED_PARITY_INPUT_ALLOWED_AFTER_PACKET_SELECTION",
        "parity_role": "Measured complex matrices with basis, phase, scale, and uncertainty.",
        "no_knob_target": "derive from selected overlap/operator kernels",
    },
    "cp_phases": {
        "status": "MEASURED_PARITY_INPUT_ALLOWED_AFTER_PACKET_SELECTION",
        "parity_role": "Measured phase data only after representation and mixing conventions are declared.",
        "no_knob_target": "derive finite character-to-physical phase map from selected source",
    },
    "higgs_parameters": {
        "status": "MEASURED_PARITY_INPUT_ALLOWED_AFTER_PACKET_SELECTION",
        "parity_role": "Measured vev, mass, quartic, and potential terms with RG convention.",
        "no_knob_target": "derive Higgs potential and thresholds from selected source",
    },
}

FORBIDDEN_IMPORTS = [
    "using measured masses to choose the family index",
    "using gauge coupling values to choose SU3 x SU2 x U1",
    "using CKM or PMNS targets to choose the representation packet",
    "using q79 numeric success as a direct proof of Qa/SU3 color embedding",
    "using anomaly cancellation as a generic existence claim without listing the actual representation packet",
    "treating benchmark matrices as selected Yukawa or CP source matrices",
]

ACCEPTANCE_TESTS = [
    "SM packet fields are all declared.",
    "Gauge group, representations, family count, and Higgs carrier are classified as selected source data.",
    "Couplings, Yukawas, CP phases, and Higgs numerical parameters are downstream measured parity inputs.",
    "Measured values are barred from source selection.",
    "Anomaly checks and local-QFT observable map are required before empirical equivalence.",
    "Full SM-parity closure is not claimed by this interface alone.",
]


def load_input() -> dict[str, object]:
    return json.loads(INPUT.read_text(encoding="utf-8"))


def build_candidate() -> dict[str, object]:
    input_data = load_input()
    return {
        "candidate": "MTTSMSectorEmbeddingInterface",
        "status": "SM_SECTOR_EMBEDDING_INTERFACE_BUILT_RECOVERY_OPEN",
        "input_status": input_data["status"],
        "selected_packet_fields": SELECTED_PACKET_FIELDS,
        "embedding_rules": EMBEDDING_RULES,
        "sm_required_components": SM_REQUIRED_COMPONENTS,
        "forbidden_imports": FORBIDDEN_IMPORTS,
        "acceptance_tests": ACCEPTANCE_TESTS,
        "measured_parameter_interface_inherited": True,
        "gate_results": {
            "sm_packet_declared": True,
            "source_data_separated_from_measured_slots": True,
            "gauge_representation_family_higgs_are_source_data": True,
            "couplings_yukawas_cp_higgs_numbers_are_downstream_slots": True,
            "measured_values_do_not_select_sm_packet": True,
            "anomaly_and_observable_map_required": True,
            "sm_parity_closure_claimed": False,
            "no_knob_closure_claimed": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": "MTT_QM_QFT_GR_Recovery_Interface_v1",
        "target_fitting_used": False,
    }


def build_certificate(candidate: dict[str, object]) -> dict[str, object]:
    return {
        "certificate": "MTTSMSectorEmbeddingInterface",
        "status": "MTT_SM_SECTOR_EMBEDDING_INTERFACE_BUILT_RECOVERY_OPEN",
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "what_closes": {
            "selected_sm_packet_schema": True,
            "source_vs_measured_sm_boundary": True,
            "downstream_sm_parameter_slot_policy": True,
            "forbidden_sm_imports": True,
            "sm_embedding_acceptance_tests": True,
        },
        "what_remains_open": {
            "actual_selected_representation_packet": True,
            "anomaly_calculation_certificate": True,
            "local_QFT_observable_functor": True,
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
    packet = "\n".join(f"- `{name}`: {text}" for name, text in candidate["selected_packet_fields"].items())
    rules = "\n".join(f"- {rule}" for rule in candidate["embedding_rules"])
    components = "\n".join(
        f"- `{name}`: {body['status']}. {body['parity_role']} No-knob target: {body['no_knob_target']}."
        for name, body in candidate["sm_required_components"].items()
    )
    forbidden = "\n".join(f"- {item}" for item in candidate["forbidden_imports"])
    tests = "\n".join(f"- {item}" for item in candidate["acceptance_tests"])
    closes = "\n".join(f"- {name}" for name, value in certificate["what_closes"].items() if value)
    open_items = "\n".join(f"- {name}" for name, value in certificate["what_remains_open"].items() if value)
    return f"""# MTT SM Sector Embedding Interface v1

## Purpose

This artifact defines the SM sector boundary for SM-parity closure.  It says
what must be selected as source structure before any measured SM numerical
values are allowed to enter.

It does not prove the actual selected representation packet, anomaly
calculation, local-QFT functor, or no-knob constants.  It closes the interface
that prevents measured couplings, masses, and phases from selecting the sector
they are later used to compare.

## Selected SM Packet

{packet}

## Embedding Rules

{rules}

## Required Components

{components}

## Forbidden Imports

{forbidden}

## Acceptance Tests

{tests}

## Interface Theorem

An MTT sector can be used as an SM-parity sector only after it declares a
selected SM packet containing gauge carrier, representation packet, family
index, Higgs carrier, operator packet, anomaly requirements, locality limit,
renormalization interface, and measured-slot boundary.

Measured values may then enter only downstream as typed parity slots inherited
from the measured-parameter interface.  They may not select the SM packet.

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
