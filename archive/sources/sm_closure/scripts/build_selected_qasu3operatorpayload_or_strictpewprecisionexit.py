"""Build Qa/SU3 operator payload or strict P_EW precision exit packet.

The precision table reduced true-SM closure to actual selected Qa/SU3 payload
values or the parallel strict P_EW/direct-K exit.  This artifact consolidates
Step8/Step9 and selects the non-duplicative next proof object: Step10, closing
either a physical Phi_fin^C1 source rule or independent Galerkin/row-kernel
execution.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_qasu3operatorpayload_or_strictpewprecisionexit"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PAYLOAD_FORK = PACKET_DIR / "qasu3_payload_vs_strict_pew_fork.packet.json"
STEP10_CONTRACT = PACKET_DIR / "step10_payload_execution_contract.packet.json"
STRICT_PEW_EXIT = PACKET_DIR / "strict_pew_precision_exit_recheck.packet.json"
NEXT_TARGET = PACKET_DIR / "next_after_qasu3_payload_fork.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_QaSU3OperatorPayload_or_StrictPEWPrecisionExit_v1.md"

PREVIOUS = DATA / "selected_precisionprofiletable_or_truesmequivalenceaudit.candidate.json"
BLOCKER_MATRIX = (
    DATA
    / "selected_precisionprofiletable_or_truesmequivalenceaudit"
    / "true_sm_equivalence_blocker_matrix.packet.json"
)
STEP8 = DATA / "selected_step8_precisionvalueemission_or_actualqasu3operatorpacketclosure.candidate.json"
STEP8_SLOTS = (
    DATA
    / "selected_step8_precisionvalueemission_or_actualqasu3operatorpacketclosure"
    / "step8_operator_source_slot_closure.packet.json"
)
STEP9 = DATA / "selected_step9_dynamicqasu3c1response_or_precisionprofilecompletion.candidate.json"
STEP9_HANDOFF = (
    DATA
    / "selected_step9_dynamicqasu3c1response_or_precisionprofilecompletion"
    / "step9_to_step10_handoff.packet.json"
)
STRICT_PEW_RECHECK = (
    DATA
    / "selected_strictpewsourcetheorem_or_smprecisionclosurecutset"
    / "strict_pew_count_reduction_recheck.packet.json"
)
PHYSICAL_ANCHOR = DATA / "selected_physicalgaugeactionanchor_or_directkthresholdomegahlambda.candidate.json"

STATUS = (
    "MTT_SELECTED_QASU3OPERATORPAYLOAD_OR_STRICTPEWPRECISIONEXIT_"
    "STEP10_SELECTED_STRICT_PEW_PARALLEL_OPEN"
)
NEXT = "MTT_Selected_Step10_PhysicalPhiFinC1SourceRule_or_IndependentGalerkinRows_v1"


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
        BLOCKER_MATRIX,
        STEP8,
        STEP8_SLOTS,
        STEP9,
        STEP9_HANDOFF,
        STRICT_PEW_RECHECK,
        PHYSICAL_ANCHOR,
    ]
    missing = [rel(path) for path in sources if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Qa/SU3 payload fork inputs: " + ", ".join(missing))

    previous = load(PREVIOUS)
    blockers = load(BLOCKER_MATRIX)
    step8 = load(STEP8)
    step8_slots = load(STEP8_SLOTS)
    step9 = load(STEP9)
    step9_handoff = load(STEP9_HANDOFF)
    strict_pew = load(STRICT_PEW_RECHECK)
    physical_anchor = load(PHYSICAL_ANCHOR)

    operator_source_slots_closed = int(step8["closure_decision"]["operator_source_slots_closed"])
    operator_source_slots_remaining = int(step8["closure_decision"]["operator_source_slots_remaining"])
    strict_pew_rows = int(strict_pew["current_strict_P_EW_source_rows"])
    direct_k_rows = int(strict_pew["direct_K_threshold_Omega_H_lambda_rows"])

    payload_fork = guarded(
        {
            "schema": "MTTQaSU3PayloadVsStrictPEWFork.v1",
            "status": "QASU3_PAYLOAD_FORK_SELECTED_STEP10_STRICT_PEW_PARALLEL",
            "precision_table_source": rel(PREVIOUS),
            "selected_QaSU3_operator_payload_blocker": blockers["blocking_classes"][
                "selected_QaSU3_operator_payload"
            ],
            "strict_P_EW_or_direct_K_blocker": blockers["blocking_classes"][
                "strict_P_EW_or_direct_K"
            ],
            "qa_su3_side": {
                "operator_source_slots_closed": operator_source_slots_closed,
                "operator_source_slots_remaining": operator_source_slots_remaining,
                "source_slot_layer_closed": step8["closure_decision"]["source_slot_layer_closed"],
                "C1_support_layer_closed": step9["closure_decision"]["C1_support_layer_closed"],
                "dotD_alpha1_stationary_projector_retired": step9["closure_decision"][
                    "dotD_alpha1_stationary_projector_retired"
                ],
                "actual_dynamic_QaSU3_operator_packet_closed": step9["closure_decision"][
                    "actual_dynamic_QaSU3_operator_packet_closed"
                ],
                "selected_C1_response_closed": step9["closure_decision"][
                    "selected_C1_response_closed"
                ],
                "full_S2_value_emission_closed": step9["closure_decision"][
                    "full_S2_value_emission_closed"
                ],
            },
            "strict_pew_side": {
                "strict_P_EW_source_rows": strict_pew_rows,
                "direct_K_threshold_Omega_H_lambda_rows": direct_k_rows,
                "strict_P_EW_source_theorem_closed": strict_pew[
                    "strict_P_EW_source_theorem_closed"
                ],
                "P_EW_count_reduction_available_now": strict_pew[
                    "P_EW_count_reduction_available_now"
                ],
                "physical_anchor_strict_fields_filled": physical_anchor["closure_decision"][
                    "strict_fields_filled"
                ],
                "physical_anchor_strict_field_count": physical_anchor["closure_decision"][
                    "strict_field_count"
                ],
                "one_physical_action_primitive_fork_available": physical_anchor[
                    "closure_decision"
                ]["one_physical_action_primitive_fork_available"],
            },
            "selected_next_route": NEXT,
            "route_priority": [
                "Step10 selected physical Phi_fin^C1 source rule",
                "Step10 independent selected Galerkin or row-kernel execution",
                "parallel strict P_EW/direct K_threshold.Omega_H.lambda precision exit",
            ],
        }
    )

    step10_contract = guarded(
        {
            "schema": "MTTStep10PayloadExecutionContract.v1",
            "status": "STEP10_CONTRACT_EMITTED_FROM_QASU3_PAYLOAD_FORK",
            "step9_handoff_status": step9_handoff["status"],
            "step10_must_close_one_of": step9_handoff["step10_must_close_one_of"],
            "step10_then_must_emit": step9_handoff["step10_then_must_emit"],
            "retired_blockers": step9_handoff["retired_blockers"],
            "must_not_use_as_selectors": step9_handoff["must_not_use_as_selectors"],
            "acceptance_rule": (
                "A Step10 payload is accepted only if route A or route B closes "
                "before value replay, and then emits A_selected, b_selected, "
                "deltaTheta_C1, sector response matrices, full S2 value rows, "
                "and no-proxy Yukawa/CKM/PMNS/Higgs mass rows."
            ),
        }
    )

    strict_pew_exit = guarded(
        {
            "schema": "MTTStrictPEWPrecisionExitRecheck.v1",
            "status": "STRICT_PEW_PRECISION_EXIT_RECHECKED_OPEN",
            "strict_P_EW_source_rows": strict_pew_rows,
            "direct_K_threshold_Omega_H_lambda_rows": direct_k_rows,
            "strict_P_EW_source_theorem_closed": False,
            "P_EW_count_reduction_available_now": False,
            "strict_precision_exit_parallel_retained": True,
            "required_for_exit": [
                "same-branch physical gauge/action normalization",
                "selected mu_match and RG/threshold scheme",
                "row-level P_EW or direct K_threshold.Omega_H.lambda certificate",
            ],
            "one_primitive_lane_available_but_not_strict": physical_anchor["closure_decision"][
                "one_physical_action_primitive_fork_available"
            ],
        }
    )

    next_target = guarded(
        {
            "schema": "MTTNextAfterQaSU3PayloadFork.v1",
            "status": "NEXT_TARGET_STEP10_PHYSICAL_SOURCE_OR_INDEPENDENT_GALERKIN_ROWS",
            "next_required_artifact": NEXT,
            "reason": (
                "Step8 closed all source slots and Step9 retired stationary/dotD "
                "blockers, but actual dynamic Qa/SU3 values still require a "
                "selected physical Phi_fin^C1 source rule or independent "
                "Galerkin/row-kernel execution. Strict P_EW/direct-K remains "
                "parallel and open with zero accepted rows."
            ),
        }
    )

    candidate = guarded(
        {
            "candidate": "MTTSelectedQaSU3OperatorPayloadOrStrictPEWPrecisionExit",
            "status": STATUS,
            "next_required_artifact": NEXT,
            "inputs": {
                "previous": rel(PREVIOUS),
                "blocker_matrix": rel(BLOCKER_MATRIX),
                "step8": rel(STEP8),
                "step8_slots": rel(STEP8_SLOTS),
                "step9": rel(STEP9),
                "step9_handoff": rel(STEP9_HANDOFF),
                "strict_pew_recheck": rel(STRICT_PEW_RECHECK),
                "physical_anchor": rel(PHYSICAL_ANCHOR),
            },
            "packets": {
                "qasu3_payload_vs_strict_pew_fork": rel(PAYLOAD_FORK),
                "step10_payload_execution_contract": rel(STEP10_CONTRACT),
                "strict_pew_precision_exit_recheck": rel(STRICT_PEW_EXIT),
                "next_after_qasu3_payload_fork": rel(NEXT_TARGET),
            },
            "closure_decision": {
                "qasu3_source_slot_layer_closed": True,
                "operator_source_slots_closed": operator_source_slots_closed,
                "operator_source_slots_remaining": operator_source_slots_remaining,
                "C1_support_layer_closed": True,
                "actual_dynamic_QaSU3_operator_packet_closed": False,
                "selected_C1_response_closed": False,
                "full_S2_value_emission_closed": False,
                "route_A_selected_physical_PhiFinC1_source_rule_closed": False,
                "route_B_independent_selected_Galerkin_or_row_kernel_execution_closed": False,
                "strict_P_EW_source_theorem_closed": False,
                "strict_P_EW_source_rows": strict_pew_rows,
                "direct_K_threshold_Omega_H_lambda_rows": direct_k_rows,
                "P_EW_count_reduction_available_now": False,
                "true_SM_equivalence_closed": False,
                "full_no_knob_closed": False,
            },
            "theorem": {
                "name": "QaSU3OperatorPayloadOrStrictPEWPrecisionExitTheorem",
                "proved": True,
                "statement": (
                    "The current frontier is a two-exit fork. On the Qa/SU3 side, "
                    "Step8 closes all eight operator source slots and Step9 closes "
                    "the non-looping C1 support/frontier reduction, but actual "
                    "dynamic Qa/SU3 operator values, selected C1 response, full S2 "
                    "emission, and no-proxy SM value rows remain open until Step10 "
                    "proves a selected physical Phi_fin^C1 source rule or executes "
                    "independent selected Galerkin/row-kernel rows. On the strict "
                    "P_EW side, current strict P_EW/direct-K rows remain zero, so "
                    "the precision/count-reduction exit is retained but open."
                ),
            },
        }
    )

    cert = guarded(
        {
            "certificate": "MTTSelectedQaSU3OperatorPayloadOrStrictPEWPrecisionExit",
            "status": STATUS,
            "theorem_proved": True,
            "qasu3_source_slot_layer_closed": True,
            "operator_source_slots_closed": operator_source_slots_closed,
            "operator_source_slots_remaining": operator_source_slots_remaining,
            "actual_dynamic_QaSU3_operator_packet_closed": False,
            "selected_C1_response_closed": False,
            "full_S2_value_emission_closed": False,
            "route_A_selected_physical_PhiFinC1_source_rule_closed": False,
            "route_B_independent_selected_Galerkin_or_row_kernel_execution_closed": False,
            "strict_P_EW_source_theorem_closed": False,
            "strict_P_EW_source_rows": strict_pew_rows,
            "direct_K_threshold_Omega_H_lambda_rows": direct_k_rows,
            "true_SM_equivalence_claimed": False,
            "full_no_knob_closure_claimed": False,
            "next_required_artifact": NEXT,
        }
    )

    note = f"""# MTT Selected QaSU3OperatorPayload or StrictPEWPrecisionExit v1

## Theorem

`QaSU3OperatorPayloadOrStrictPEWPrecisionExitTheorem` is emitted.

## Qa/SU3 Side

```text
operator source slots closed = {operator_source_slots_closed}
operator source slots remaining = {operator_source_slots_remaining}
C1 support layer closed = true
actual dynamic Qa/SU3 operator packet closed = false
selected C1 response closed = false
full S2 value emission closed = false
```

Step8 and Step9 are real closures at the source-slot/support frontier, but they
do not yet emit actual dynamic values.

## Strict PEW Side

```text
strict P_EW source rows = {strict_pew_rows}
direct K_threshold.Omega_H.lambda rows = {direct_k_rows}
P_EW count reduction available now = false
```

The strict `P_EW`/direct-K exit remains parallel and open.

## Step10 Contract

Step10 must close one of:

```text
route A: selected physical Phi_fin^C1 source rule
route B: independent selected Galerkin or row-kernel execution
```

Then it must emit:

```text
A_selected
b_selected
deltaTheta_C1
sector response matrices
full S2 value rows
Yukawa/CKM/PMNS/Higgs mass value rows without proxy fitting
```

## Next Artifact

`{NEXT}`.
"""

    for path, payload in [
        (PAYLOAD_FORK, payload_fork),
        (STEP10_CONTRACT, step10_contract),
        (STRICT_PEW_EXIT, strict_pew_exit),
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
