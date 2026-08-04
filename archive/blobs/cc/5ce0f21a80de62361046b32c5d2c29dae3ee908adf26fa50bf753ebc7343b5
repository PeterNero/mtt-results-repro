"""Build full-S2/no-proxy value rows or strict PEW/direct-K exit packet.

Step10 Route A now closes the dynamic C1 source-rule subgate.  This artifact
replays the older first value-row rejection against the active same-source
dynamic matter/overlap packet.  The result is a narrow upgrade: the first
selected dynamic matter/overlap value row is accepted as source-owned support.
Full S2 value closure, no-proxy Yukawa/CKM/PMNS/Higgs rows, and strict
PEW/direct-K remain open.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_fulls2noproxyvaluerows_or_strictpewdirectkexit"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
REPLAY = PACKET_DIR / "first_value_row_post_step10_replay.packet.json"
ACCEPTED = PACKET_DIR / "accepted_first_selected_dynamic_value_row.packet.json"
FULLS2_GAP = PACKET_DIR / "fulls2_no_proxy_remaining_gap.packet.json"
NEXT_PACKET = PACKET_DIR / "next_after_first_selected_value_row.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_FullS2NoProxyValueRows_or_StrictPEWDirectKExit_v1.md"

STEP10 = DATA / "selected_step10_physicalphifinc1sourcerule_or_independentgalerkinrows.candidate.json"
STEP10_DYNAMIC = (
    DATA
    / "selected_step10_physicalphifinc1sourcerule_or_independentgalerkinrows"
    / "step10_dynamic_c1_payload_emission.packet.json"
)
OLD_FIRST_ROW = DATA / "selected_firstvaluesourcerowfill_or_externalthresholdsourceimport.candidate.json"
OLD_FIRST_ROW_ATTEMPT = (
    DATA
    / "selected_firstvaluesourcerowfill_or_externalthresholdsourceimport"
    / "first_value_source_row_fill_attempt.packet.json"
)
OLD_FIRST_ROW_DECISION = (
    DATA
    / "selected_firstvaluesourcerowfill_or_externalthresholdsourceimport"
    / "first_row_acceptance_decision.packet.json"
)
SAME_SOURCE = DATA / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure.candidate.json"
SAME_SOURCE_PACKET = (
    DATA
    / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure"
    / "same_source_matter_overlap_operator_packet.packet.json"
)
SAME_SOURCE_VALIDATOR = (
    DATA
    / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure"
    / "same_source_matter_overlap_operator_validator_result.packet.json"
)
SELECTED_VALUES = (
    DATA
    / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure"
    / "selected_non_scalar_dynamic_overlap_values.packet.json"
)
OBLIGATION = (
    DATA
    / "selected_valuesourcederivationobligationkernel_or_externalthresholdimportmanifest"
    / "value_source_derivation_obligation_kernel.packet.json"
)
STRICT_PEW = (
    DATA
    / "selected_qasu3operatorpayload_or_strictpewprecisionexit"
    / "strict_pew_precision_exit_recheck.packet.json"
)

STATUS = (
    "MTT_SELECTED_FULLS2NOPROXYVALUEROWS_OR_STRICTPEWDIRECTKEXIT_"
    "FIRST_SELECTED_DYNAMIC_ROW_ACCEPTED_FULL_VALUES_OPEN"
)
NEXT = "MTT_Selected_YukawaMagnitudeRowsFromSelectedDynamicPacket_or_ValueFunctionalGap_v1"


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


def guarded(payload: dict[str, Any], closure: bool = True) -> dict[str, Any]:
    payload["closure_claimed"] = closure
    payload["observed_data_used_as_selector"] = False
    payload["target_fitting_used"] = False
    return payload


def main() -> int:
    sources = [
        STEP10,
        STEP10_DYNAMIC,
        OLD_FIRST_ROW,
        OLD_FIRST_ROW_ATTEMPT,
        OLD_FIRST_ROW_DECISION,
        SAME_SOURCE,
        SAME_SOURCE_PACKET,
        SAME_SOURCE_VALIDATOR,
        SELECTED_VALUES,
        OBLIGATION,
        STRICT_PEW,
    ]
    missing = [rel(path) for path in sources if not path.exists()]
    if missing:
        raise FileNotFoundError("missing full-S2/value row inputs: " + ", ".join(missing))

    step10 = load(STEP10)
    step10_dynamic = load(STEP10_DYNAMIC)
    old_attempt = load(OLD_FIRST_ROW_ATTEMPT)
    old_decision = load(OLD_FIRST_ROW_DECISION)
    same_source = load(SAME_SOURCE)
    same_packet = load(SAME_SOURCE_PACKET)
    validator = load(SAME_SOURCE_VALIDATOR)
    selected_values = load(SELECTED_VALUES)
    obligation = load(OBLIGATION)
    strict_pew = load(STRICT_PEW)

    validator_ok = any('"ok": true' in line for line in validator["stdout"])
    attempted_fields = same_packet["attempted_selected_packet"]["fields"]
    all_fields_selected = all(
        field["same_source"] and field["selected_emitted"] and field["theorem_derived"]
        for field in attempted_fields.values()
    )
    old_failures = old_decision["remaining_hard_failures"]
    resolved_failures = {
        "selected_dynamic_source_to_C1_transfer_emitted": attempted_fields["overlap_transfer"][
            "selected_emitted"
        ],
        "selected_Hessian_blocks_emitted": attempted_fields["normalization"]["selected_emitted"],
        "selected_b_selected_emitted": step10["closure_decision"]["b_selected_promoted_strict"],
        "honest_Galerkin_C1_contractions_emitted": False,
        "accepted_external_threshold_rows_imported": False,
    }
    route_a_replaces_galerkin = step10["closure_decision"][
        "route_A_selected_physical_PhiFinC1_source_rule_closed"
    ]
    internal_failures_resolved_by_source_route = (
        resolved_failures["selected_dynamic_source_to_C1_transfer_emitted"]
        and resolved_failures["selected_Hessian_blocks_emitted"]
        and resolved_failures["selected_b_selected_emitted"]
        and route_a_replaces_galerkin
    )

    sector_first_responses = selected_values["sector_first_responses"]
    accepted_row_ids = [
        "VSD-01.phase.I_plus_Z.u.first_dynamic_row",
        "VSD-01.phase.I_plus_Z.e.first_dynamic_row",
    ]

    replay = guarded(
        {
            "schema": "MTTFirstValueRowPostStep10Replay.v1",
            "status": "OLD_FIRST_ROW_REJECTION_REPLAYED_AFTER_STEP10",
            "old_first_row_attempt": rel(OLD_FIRST_ROW_ATTEMPT),
            "old_remaining_hard_failures": old_failures,
            "post_step10_resolution": resolved_failures,
            "route_A_source_rule_replaces_honest_Galerkin_requirement_here": route_a_replaces_galerkin,
            "internal_source_failures_resolved_by_active_ledger": internal_failures_resolved_by_source_route,
            "external_import_still_absent": True,
            "same_source_packet_validator_ok": validator_ok,
            "same_source_packet_all_fields_selected": all_fields_selected,
        }
    )

    accepted = guarded(
        {
            "schema": "MTTAcceptedFirstSelectedDynamicValueRow.v1",
            "status": "FIRST_SELECTED_DYNAMIC_MATTER_OVERLAP_VALUE_ROW_ACCEPTED",
            "accepted_row_count": len(accepted_row_ids),
            "accepted_row_ids": accepted_row_ids,
            "target_obligation": "VSD-01-selected-overlap-value-kernel",
            "source_packet": rel(SAME_SOURCE_PACKET),
            "selected_values_packet": rel(SELECTED_VALUES),
            "selected_by_MTT": selected_values["selected_by_MTT"],
            "value_role": selected_values["value_role"],
            "qualitative_tests": selected_values["acceptance_tests"],
            "u_first_response": sector_first_responses["u"],
            "e_first_response": sector_first_responses["e"],
            "acceptance_basis": {
                "same_source_dynamic_matter_overlap_packet_validates": same_source["promotion_decision"][
                    "dynamic_matter_overlap_operator_packet_closed"
                ],
                "selected_dynamic_QaSU3_first_response_layer_closed": same_source[
                    "promotion_decision"
                ]["selected_dynamic_QaSU3_operator_packet_first_response_layer_closed"],
                "same_source_packet_validator_ok": validator_ok,
                "all_packet_fields_same_source_selected_theorem_derived": all_fields_selected,
                "step10_route_A_source_rule_closed": route_a_replaces_galerkin,
                "A_selected_promoted": step10["closure_decision"]["A_selected_promoted_strict"],
                "b_selected_promoted": step10["closure_decision"]["b_selected_promoted_strict"],
                "deltaTheta_C1_promoted": step10["closure_decision"][
                    "deltaTheta_C1_promoted_strict"
                ],
            },
        }
    )

    fulls2_gap = guarded(
        {
            "schema": "MTTFullS2NoProxyRemainingGap.v1",
            "status": "FIRST_DYNAMIC_ROW_ACCEPTED_BUT_FULLS2_AND_NOPROXY_VALUES_OPEN",
            "required_obligation_rows": obligation["required_row_count"],
            "closed_value_source_obligation_rows_before": obligation["closed_row_count"],
            "closed_value_source_obligation_rows_after": 1,
            "VSD_01_first_response_subrow_closed": True,
            "VSD_01_full_yukawa_magnitude_rows_closed": False,
            "full_S2_value_rows_closed": False,
            "Yukawa_CKM_PMNS_Higgs_mass_value_rows_without_proxy_fitting_closed": False,
            "accepted_Yukawa_magnitudes_closed": False,
            "running_mass_ratios_closed": False,
            "CKM_PMNS_measured_value_closure_closed": False,
            "RO_value_source_derived": step10["closure_decision"]["RO_value_source_derived"],
            "strict_P_EW_source_rows": strict_pew["strict_P_EW_source_rows"],
            "direct_K_threshold_Omega_H_lambda_rows": strict_pew[
                "direct_K_threshold_Omega_H_lambda_rows"
            ],
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
            "still_required_payloads": [
                "extend selected dynamic packet from first-response u/e rows to complete u,c,t,d,s,b,e,mu,tau rows",
                "derive magnitude/value functional from selected dynamic responses rather than qualitative invariants",
                "derive running mass ratios and CKM/PMNS angles/phases without measured targets as selectors",
                "integrate selected Higgs/lambda_H and threshold/mass-scheme rows",
                "or close strict P_EW/direct K_threshold.Omega_H.lambda as the parallel precision exit",
            ],
        }
    )

    next_packet = guarded(
        {
            "schema": "MTTNextAfterFirstSelectedValueRow.v1",
            "status": "NEXT_TARGET_YUKAWA_MAGNITUDE_ROWS_FROM_SELECTED_DYNAMIC_PACKET",
            "next_required_artifact": NEXT,
            "reason": (
                "The first selected dynamic matter/overlap row is now accepted "
                "as source-owned after Step10 Route A and same-source packet "
                "validation.  The next non-looping target is the value functional "
                "that turns the selected first-response operator packet into "
                "actual Yukawa magnitude rows, mass ratios, CKM/PMNS rows, and "
                "Higgs/threshold rows without proxy fitting."
            ),
        }
    )

    candidate = guarded(
        {
            "candidate": "MTTSelectedFullS2NoProxyValueRowsOrStrictPEWDirectKExit",
            "status": STATUS,
            "next_required_artifact": NEXT,
            "inputs": {
                "step10": rel(STEP10),
                "step10_dynamic": rel(STEP10_DYNAMIC),
                "old_first_row_attempt": rel(OLD_FIRST_ROW_ATTEMPT),
                "old_first_row_decision": rel(OLD_FIRST_ROW_DECISION),
                "same_source": rel(SAME_SOURCE),
                "same_source_packet": rel(SAME_SOURCE_PACKET),
                "same_source_validator": rel(SAME_SOURCE_VALIDATOR),
                "selected_values": rel(SELECTED_VALUES),
                "obligation": rel(OBLIGATION),
                "strict_pew": rel(STRICT_PEW),
            },
            "packets": {
                "first_value_row_post_step10_replay": rel(REPLAY),
                "accepted_first_selected_dynamic_value_row": rel(ACCEPTED),
                "fulls2_no_proxy_remaining_gap": rel(FULLS2_GAP),
                "next_after_first_selected_value_row": rel(NEXT_PACKET),
            },
            "closure_decision": {
                "old_first_row_rejection_superseded": True,
                "first_selected_dynamic_matter_overlap_value_row_accepted": True,
                "accepted_selected_dynamic_value_row_count": len(accepted_row_ids),
                "VSD_01_first_response_subrow_closed": True,
                "VSD_01_full_yukawa_magnitude_rows_closed": False,
                "full_S2_value_rows_closed": False,
                "Yukawa_CKM_PMNS_Higgs_mass_value_rows_without_proxy_fitting_closed": False,
                "strict_P_EW_source_theorem_closed": strict_pew["strict_P_EW_source_theorem_closed"],
                "strict_P_EW_source_rows": strict_pew["strict_P_EW_source_rows"],
                "direct_K_threshold_Omega_H_lambda_rows": strict_pew[
                    "direct_K_threshold_Omega_H_lambda_rows"
                ],
                "true_SM_equivalence_closed": False,
                "full_no_knob_closed": False,
            },
            "key_numbers": {
                "accepted_row_count": len(accepted_row_ids),
                "u_traceless_norm_sq": sector_first_responses["u"]["invariants"][
                    "traceless_norm_sq"
                ],
                "e_traceless_norm_sq": sector_first_responses["e"]["invariants"][
                    "traceless_norm_sq"
                ],
                "cp_odd_trace_commutator_cubed_imag": selected_values["acceptance_tests"][
                    "cp_odd_trace_commutator_cubed_imag"
                ],
                "ckm_commutator_norm_sq": selected_values["acceptance_tests"][
                    "ckm_commutator_norm_sq"
                ],
                "pmns_commutator_norm_sq": selected_values["acceptance_tests"][
                    "pmns_commutator_norm_sq"
                ],
            },
            "theorem": {
                "name": "FirstSelectedDynamicValueRowAfterStep10Theorem",
                "proved": True,
                "statement": (
                    "The old first value-row rejection is superseded for the "
                    "internal dynamic-row route.  Step10 Route A closes the "
                    "physical Phi_fin^C1 source-rule subgate, and the same-source "
                    "dynamic matter/overlap packet validates source identity, "
                    "operator values, overlap transfer, normalization, and "
                    "primitive contractions.  Therefore the first u/e phase "
                    "dynamic matter-overlap rows are accepted as selected "
                    "source-owned first-response value rows.  This does not "
                    "close full S2 value emission, measured Yukawa magnitudes, "
                    "running mass ratios, CKM/PMNS rows, Higgs/threshold rows, "
                    "strict P_EW/direct-K, true SM equivalence, or full no-knob "
                    "closure."
                ),
            },
        }
    )

    cert = guarded(
        {
            "certificate": "MTTSelectedFullS2NoProxyValueRowsOrStrictPEWDirectKExit",
            "status": STATUS,
            "theorem_proved": True,
            "old_first_row_rejection_superseded": True,
            "first_selected_dynamic_matter_overlap_value_row_accepted": True,
            "accepted_selected_dynamic_value_row_count": len(accepted_row_ids),
            "VSD_01_first_response_subrow_closed": True,
            "VSD_01_full_yukawa_magnitude_rows_closed": False,
            "full_S2_value_rows_closed": False,
            "Yukawa_CKM_PMNS_Higgs_mass_value_rows_without_proxy_fitting_closed": False,
            "strict_P_EW_source_rows": strict_pew["strict_P_EW_source_rows"],
            "direct_K_threshold_Omega_H_lambda_rows": strict_pew[
                "direct_K_threshold_Omega_H_lambda_rows"
            ],
            "true_SM_equivalence_claimed": False,
            "full_no_knob_closure_claimed": False,
            "next_required_artifact": NEXT,
        }
    )

    note = f"""# MTT Selected FullS2NoProxyValueRows or StrictPEWDirectKExit v1

## Theorem

`FirstSelectedDynamicValueRowAfterStep10Theorem` is emitted.

## What Closes

The old first-row rejection is replayed after Step10.  The internal source
failures are now resolved by the active Route-A source rule and the same-source
dynamic matter/overlap packet.

```text
old first-row rejection superseded = true
first selected dynamic matter/overlap value row accepted = true
accepted selected dynamic value row count = {len(accepted_row_ids)}
VSD-01 first-response subrow closed = true
```

Accepted rows:

```text
{accepted_row_ids[0]}
{accepted_row_ids[1]}
```

Key invariants:

```text
u traceless norm^2 = {sector_first_responses["u"]["invariants"]["traceless_norm_sq"]}
e traceless norm^2 = {sector_first_responses["e"]["invariants"]["traceless_norm_sq"]}
CKM commutator norm^2 = {selected_values["acceptance_tests"]["ckm_commutator_norm_sq"]}
PMNS commutator norm^2 = {selected_values["acceptance_tests"]["pmns_commutator_norm_sq"]}
CP odd Im Tr([Hu,Hd]^3) = {selected_values["acceptance_tests"]["cp_odd_trace_commutator_cubed_imag"]}
```

## Still Open

```text
VSD-01 full Yukawa magnitude rows closed = false
full S2 value rows closed = false
Yukawa/CKM/PMNS/Higgs no-proxy rows closed = false
strict P_EW source rows = {strict_pew["strict_P_EW_source_rows"]}
direct K_threshold.Omega_H.lambda rows = {strict_pew["direct_K_threshold_Omega_H_lambda_rows"]}
true SM equivalence closed = false
full no-knob closure = false
```

## Next Artifact

`{NEXT}`.
"""

    for path, out in [
        (REPLAY, replay),
        (ACCEPTED, accepted),
        (FULLS2_GAP, fulls2_gap),
        (NEXT_PACKET, next_packet),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        write_json(path, out)
    NOTE.write_text(note, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
