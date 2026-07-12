"""Import q79 selected D_E/Green/dotD source gate for primitive C1."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")

PREVIOUS = DATA / "q79_selected_visible_operator_or_primitive_c1_target_import.candidate.json"
Q79_CERT = Q79 / "certificates" / "q79_selected_de_green_dotd_source_for_primitive_c1_certificate.json"
Q79_CANDIDATE = Q79 / "candidate_data" / "q79_selected_de_green_dotd_source_for_primitive_c1.candidate.json"

OUTPUT_PACKET = DATA / "q79_selected_de_green_dotd_source_gate_import.candidate.json"
OUTPUT_CERT = CERTS / "q79_selected_de_green_dotd_source_gate_import_certificate.json"
OUTPUT_NOTE = CORPUS / "Q79_Selected_DE_Green_DotD_Source_Gate_Import_v1.md"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load_json(PREVIOUS)
    q79_cert = load_json(Q79_CERT)
    q79_candidate = load_json(Q79_CANDIDATE)

    stack = q79_cert["current_routec_stack"]
    primitive = q79_cert["primitive_c1_source_gate"]
    closes = q79_cert["what_closes_now"]
    remains = q79_cert["what_remains_open"]

    original_exit_codes = {
        name: result["exit_code"] for name, result in stack["original_validators"].items()
    }
    diagnostic_exit_codes = {
        name: result["exit_code"]
        for name, result in stack["hypothetical_selected_flags_validators"].items()
    }

    checks = {
        "D0_previous_next_matches_de_green_dotd_gate": previous["verdict"][
            "next_required_artifact"
        ]
        == "Q79_Selected_DE_Green_DotD_Source_for_Primitive_C1_v1",
        "D1_gate_theorem_proved_no_closure": q79_cert["theorem"]["proved"] is True
        and q79_cert["closure_claimed"] is False,
        "D2_honest_stack_rejected_without_selected_source": closes[
            "honest_current_routec_stack_rejected_without_selected_source"
        ]
        is True
        and all(code == 1 for code in original_exit_codes.values()),
        "D3_selected_flags_only_stack_passes_diagnostic": closes[
            "selected_flags_only_routec_stack_passes_as_diagnostic"
        ]
        is True
        and all(code == 0 for code in diagnostic_exit_codes.values())
        and stack["diagnostic_not_proof"] is True,
        "D4_boundary_is_provenance_not_arithmetic": closes[
            "provenance_vs_arithmetic_boundary_sharpened"
        ]
        is True
        and stack["hypothetical_selected_flags_all_pass"] is True,
        "D5_primitive_c1_dependency_map_has_24_atoms": primitive["atom_count"] == 24
        and closes["primitive_c1_24_atom_slot_dependencies_mapped"] is True,
        "D6_next_gate_routec_source_or_typed_de": q79_cert["next_required_artifact"]
        == "Q79_RouteC_Selected_Source_Certificate_or_Typed_DE_Construction_v1",
    }

    proved = all(checks.values())
    return {
        "packet": "Q79_Selected_DE_Green_DotD_Source_Gate_Import_v1",
        "status": (
            "Q79_SELECTED_DE_GREEN_DOTD_SOURCE_GATE_IMPORTED"
            if proved
            else "Q79_SELECTED_DE_GREEN_DOTD_SOURCE_GATE_IMPORT_FAILED"
        ),
        "inputs": {
            "previous": str(PREVIOUS.relative_to(ROOT)),
            "q79_certificate": str(Q79_CERT),
            "q79_candidate": str(Q79_CANDIDATE),
        },
        "theorem": {
            "name": "Q79SelectedDEGreenDotDSourceGateImport",
            "proved": proved,
            "statement": (
                "The q79 selected D_E/Green/dotD gate is imported as a provenance "
                "frontier. The honest Route-C stack is rejected because selected "
                "source provenance is absent; the selected-flags-only diagnostic "
                "stack passes, showing no hidden finite arithmetic obstruction. "
                "This does not compute primitive C1 values."
            ),
        },
        "import_checks": checks,
        "routec_stack": {
            "branch_id": stack["branch_id"],
            "honest_exit_codes": original_exit_codes,
            "diagnostic_exit_codes": diagnostic_exit_codes,
            "original_failures_are_source_or_provenance_flags": stack[
                "original_failures_are_source_or_provenance_flags"
            ],
            "diagnostic_not_proof": stack["diagnostic_not_proof"],
            "interpretation": stack["interpretation"],
        },
        "primitive_c1_source_gate": {
            "atom_count": primitive["atom_count"],
            "sector_slots": primitive["sector_slots"],
            "terms": primitive["terms"],
            "status": primitive["status"],
            "interpretation": primitive["interpretation"],
        },
        "decision": {
            "selected_DE_Green_dotD_source_gate_created": closes[
                "selected_DE_Green_dotD_source_gate_created"
            ],
            "honest_selected_rhoE_DE_Riesz_Green_dotD_not_closed": remains[
                "honest_selected_rhoE_DE_Riesz_Green_dotD"
            ],
            "selected_RouteC_residual_or_typed_DE_construction_not_closed": remains[
                "selected_RouteC_residual_or_typed_DE_construction"
            ],
            "primitive_c1_values_not_computed": remains["all_24_primitive_C1_3x3_matrices"],
            "next_required_artifact": "Q79_RouteC_Selected_Source_Certificate_or_Typed_DE_Construction_v1",
        },
        "guardrails": {
            "does_not_treat_selected_flags_only_as_proof": stack["diagnostic_not_proof"] is True,
            "does_not_claim_selected_operator_source_constructed": q79_cert["guardrails"][
                "claims_selected_operator_source_constructed"
            ]
            is False,
            "does_not_claim_selected_RouteC_residual": q79_cert["guardrails"][
                "claims_selected_RouteC_residual"
            ]
            is False,
            "does_not_claim_primitive_C1_values_computed": q79_cert["guardrails"][
                "claims_primitive_C1_values_computed"
            ]
            is False,
            "does_not_claim_selected_C1_response_matrices": q79_cert["guardrails"][
                "claims_selected_C1_response_matrices"
            ]
            is False,
            "does_not_claim_full_SM_closure": q79_cert["guardrails"][
                "claims_full_sm_closure"
            ]
            is False,
            "does_not_use_observed_or_benchmark_inputs": (
                q79_cert["target_fitting_used"] is False
                and q79_cert["guardrails"]["uses_observed_masses_or_ckm_inputs"] is False
                and q79_cert["guardrails"]["uses_benchmark_flavor_entries"] is False
            ),
        },
        "verdict": {
            "what_closes_now": (
                "The D_E/Green/dotD operator-stack frontier is imported and "
                "separated from primitive C1 values. The blocker is selected "
                "source provenance, not finite validator arithmetic."
            ),
            "what_remains": (
                "Prove Q79_RouteC_Selected_Source_Certificate_or_Typed_DE_"
                "Construction_v1: either a selected Route-C source certificate "
                "for the finite packets, or a typed selected monad/Cech "
                "construction of D_E, Riesz/Green, and dotD."
            ),
            "next_required_artifact": "Q79_RouteC_Selected_Source_Certificate_or_Typed_DE_Construction_v1",
        },
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "Q79SelectedDEGreenDotDSourceGateImport",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "import_checks": packet["import_checks"],
        "decision": packet["decision"],
        "guardrails": packet["guardrails"],
        "verdict": packet["verdict"],
    }


def render_note(cert: dict[str, Any], packet: dict[str, Any]) -> str:
    return f"""# Q79 Selected D_E/Green/dotD Source Gate Import v1

## Result

Status: `{cert["status"]}`

The q79 selected `D_E`/Green/`dotD` source gate is imported as a provenance
frontier. The honest Route-C stack fails because selected source provenance is
absent. The selected-flags-only diagnostic stack passes, showing no hidden
finite arithmetic obstruction, but it is not proof.

## Import Checks

```json
{json.dumps(packet["import_checks"], indent=2, sort_keys=True)}
```

## Route-C Stack

```json
{json.dumps(packet["routec_stack"], indent=2, sort_keys=True)}
```

## Primitive C1 Source Gate

```json
{json.dumps(packet["primitive_c1_source_gate"], indent=2, sort_keys=True)}
```

## Decision

```json
{json.dumps(packet["decision"], indent=2, sort_keys=True)}
```
"""


def main() -> int:
    packet = build_packet()
    cert = build_certificate(packet)
    if "--write" in sys.argv:
        OUTPUT_PACKET.write_text(
            json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        OUTPUT_CERT.write_text(
            json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        OUTPUT_NOTE.write_text(render_note(cert, packet), encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
