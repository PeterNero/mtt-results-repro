"""Import q79 selected visible operator or primitive C1 target creation."""

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

PREVIOUS = DATA / "q79_same_source_operator_provenance_frontier_import.candidate.json"
Q79_CERT = (
    Q79
    / "certificates"
    / "q79_selected_visible_bundle_operator_source_or_primitive_c1_contractions_certificate.json"
)
Q79_CANDIDATE = (
    Q79
    / "candidate_data"
    / "q79_selected_visible_bundle_operator_source_or_primitive_c1_contractions.candidate.json"
)

OUTPUT_PACKET = DATA / "q79_selected_visible_operator_or_primitive_c1_target_import.candidate.json"
OUTPUT_CERT = (
    CERTS / "q79_selected_visible_operator_or_primitive_c1_target_import_certificate.json"
)
OUTPUT_NOTE = CORPUS / "Q79_Selected_Visible_Operator_or_Primitive_C1_Target_Import_v1.md"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load_json(PREVIOUS)
    q79_cert = load_json(Q79_CERT)
    q79_candidate = load_json(Q79_CANDIDATE)

    source_lane = q79_cert["source_lane"]
    primitive_lane = q79_cert["primitive_c1_lane"]
    closes = q79_cert["what_closes_now"]
    remains = q79_cert["what_remains_open"]
    missing_scan = q79_cert["selected_missing_data_scan"]

    checks = {
        "T0_previous_next_matches_q79_target": previous["verdict"][
            "next_required_artifact"
        ]
        == "Q79_Selected_Visible_Bundle_Operator_Source_or_Primitive_C1_Contractions_v1",
        "T1_target_creation_theorem_proved_no_closure": q79_cert["theorem"]["proved"] is True
        and q79_cert["closure_claimed"] is False,
        "T2_selected_ordered_and_s3_subvalidators_pass": closes[
            "selected_ordered_source_subvalidator_passes"
        ]
        is True
        and closes["selected_s3_class_subvalidator_passes"] is True,
        "T3_source_lane_open_at_selected_operator_source": source_lane[
            "validator_exit_code"
        ]
        == 2
        and "selected_by_mtt must be true" in source_lane["open_items"]
        and "source_certificate missing" in source_lane["open_items"],
        "T4_primitive_c1_contract_enumerates_24_missing_atoms": primitive_lane[
            "contract_atom_count"
        ]
        == 24
        and primitive_lane["missing_atom_count"] == 24
        and primitive_lane["calculator_exit_code"] == 2,
        "T5_missing_data_scan_confirms_operator_source_first": missing_scan[
            "first_blocking_layer"
        ]
        == "selected_operator_source"
        and missing_scan["can_compute_now"]["actual_selected_C1_matrices"] is False,
        "T6_next_gate_is_DE_Green_DotD_for_primitive_C1": q79_cert[
            "next_required_artifact"
        ]
        == "Q79_Selected_DE_Green_DotD_Source_for_Primitive_C1_v1",
    }

    proved = all(checks.values())
    return {
        "packet": "Q79_Selected_Visible_Operator_or_Primitive_C1_Target_Import_v1",
        "status": (
            "Q79_SELECTED_VISIBLE_OPERATOR_OR_PRIMITIVE_C1_TARGET_IMPORTED"
            if proved
            else "Q79_SELECTED_VISIBLE_OPERATOR_OR_PRIMITIVE_C1_TARGET_IMPORT_FAILED"
        ),
        "inputs": {
            "previous": str(PREVIOUS.relative_to(ROOT)),
            "q79_certificate": str(Q79_CERT),
            "q79_candidate": str(Q79_CANDIDATE),
        },
        "theorem": {
            "name": "Q79SelectedVisibleOperatorOrPrimitiveC1TargetImport",
            "proved": proved,
            "statement": (
                "The next q79 target is imported as a two-lane executable gate. "
                "Lane A needs one selected visible bundle/operator source. Lane "
                "B needs the 24 same-source primitive C1 matrices. Current data "
                "close neither lane, but the exact missing matrix atoms and "
                "source validator failures are now enumerated."
            ),
        },
        "import_checks": checks,
        "source_lane": {
            "validator_status": source_lane["validator_status"],
            "validator_exit_code": source_lane["validator_exit_code"],
            "open_items": source_lane["open_items"],
            "ordered_source_passes": closes["selected_ordered_source_subvalidator_passes"],
            "s3_class_passes": closes["selected_s3_class_subvalidator_passes"],
        },
        "primitive_c1_lane": {
            "contract_atom_count": primitive_lane["contract_atom_count"],
            "missing_atom_count": primitive_lane["missing_atom_count"],
            "missing_atoms": primitive_lane["missing_atoms"],
            "interpretation": primitive_lane["interpretation"],
        },
        "missing_data_scan": missing_scan,
        "decision": {
            "selected_visible_operator_source_not_closed": remains[
                "selected_visible_bundle_operator_source_certificate"
            ],
            "selected_DE_rhoE_Riesz_Green_dotD_not_closed": remains[
                "selected_DE_rhoE_Riesz_Green_dotD"
            ],
            "primitive_c1_matrices_not_closed": remains[
                "all_24_primitive_C1_3x3_matrices"
            ],
            "full_SM_or_no_knob_closure_not_closed": remains[
                "full_SM_or_no_knob_closure"
            ],
            "next_required_artifact": "Q79_Selected_DE_Green_DotD_Source_for_Primitive_C1_v1",
        },
        "guardrails": {
            "does_not_claim_selected_operator_source_constructed": q79_cert[
                "guardrails"
            ]["claims_selected_operator_source_constructed"]
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
                and q79_cert["guardrails"]["uses_observed_masses_or_ckm_inputs"]
                is False
                and q79_cert["guardrails"]["uses_benchmark_flavor_entries"] is False
            ),
        },
        "verdict": {
            "what_closes_now": (
                "The next q79 proof target is executable and atomized: selected "
                "ordered and S3 support pass, while the source lane and all 24 "
                "primitive C1 matrices remain open."
            ),
            "what_remains": (
                "Build Q79_Selected_DE_Green_DotD_Source_for_Primitive_C1_v1: "
                "a same-source selected D_E/rhoE/Riesz/Green/dotD payload strong "
                "enough to supply or legitimately zero the primitive C1 atoms."
            ),
            "next_required_artifact": "Q79_Selected_DE_Green_DotD_Source_for_Primitive_C1_v1",
        },
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "Q79SelectedVisibleOperatorOrPrimitiveC1TargetImport",
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
    return f"""# Q79 Selected Visible Operator or Primitive C1 Target Import v1

## Result

Status: `{cert["status"]}`

The q79 target is now imported as an executable two-lane gate.  Lane A needs
one selected visible bundle/operator source.  Lane B needs 24 selected
same-source primitive `C1` matrices: four sectors times six primitive response
terms.  Current data close neither lane.

## Import Checks

```json
{json.dumps(packet["import_checks"], indent=2, sort_keys=True)}
```

## Source Lane

```json
{json.dumps(packet["source_lane"], indent=2, sort_keys=True)}
```

## Primitive C1 Lane

```json
{json.dumps(packet["primitive_c1_lane"], indent=2, sort_keys=True)}
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
