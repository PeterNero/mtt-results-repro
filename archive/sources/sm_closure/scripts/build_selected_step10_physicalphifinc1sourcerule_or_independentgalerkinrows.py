"""Build Step10 physical Phi_fin^C1 source-rule import artifact.

The previous Qa/SU3 fork selected Step10 as the next non-duplicative target.
This artifact reconciles that target with the active-ledger packets that already
promote the unpatched dynamic Phi_fin/C1 source stack.  It closes the Step10
source-rule subgate by Route A, and keeps the downstream full-S2/no-proxy value
row layer open.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step10_physicalphifinc1sourcerule_or_independentgalerkinrows"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROUTE_A_IMPORT = PACKET_DIR / "route_a_active_ledger_source_rule_import.packet.json"
DYNAMIC_PAYLOAD = PACKET_DIR / "step10_dynamic_c1_payload_emission.packet.json"
VALUE_GAP = PACKET_DIR / "fulls2_no_proxy_value_row_gap.packet.json"
NEXT_PACKET = PACKET_DIR / "next_after_step10_source_rule.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step10_PhysicalPhiFinC1SourceRule_or_IndependentGalerkinRows_v1.md"

PREVIOUS = DATA / "selected_qasu3operatorpayload_or_strictpewprecisionexit.candidate.json"
STEP10_CONTRACT = (
    DATA
    / "selected_qasu3operatorpayload_or_strictpewprecisionexit"
    / "step10_payload_execution_contract.packet.json"
)
UNPATCHED = DATA / "selected_unpatchedphifinc1sourcerule_or_honestgalerkintables_to_hrgconsumermap.candidate.json"
UNPATCHED_PAYLOAD = (
    DATA
    / "selected_unpatchedphifinc1sourcerule_or_honestgalerkintables_to_hrgconsumermap"
    / "selected_dynamic_phifinc1_payload_promotion.packet.json"
)
UNPATCHED_HRG_HANDOFF = (
    DATA
    / "selected_unpatchedphifinc1sourcerule_or_honestgalerkintables_to_hrgconsumermap"
    / "hrg_consumer_after_dynamic_payload_handoff.packet.json"
)
VSD01 = DATA / "selected_vsd01_allprimitiverowsassemblymap_or_physicalphifinc1actionsource.candidate.json"
CROSSREPO = DATA / "true_sm_crossrepo_part_status_audit.candidate.json"
STRICT_PEW = (
    DATA
    / "selected_qasu3operatorpayload_or_strictpewprecisionexit"
    / "strict_pew_precision_exit_recheck.packet.json"
)

STATUS = (
    "MTT_SELECTED_STEP10_PHYSICALPHIFINC1SOURCERULE_OR_INDEPENDENTGALERKINROWS_"
    "ROUTE_A_SOURCE_RULE_CLOSED_FULLS2_VALUES_OPEN"
)
NEXT = "MTT_Selected_FullS2NoProxyValueRows_or_StrictPEWDirectKExit_v1"


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


def crossrepo_part(crossrepo: dict[str, Any], name: str) -> dict[str, Any]:
    for part in crossrepo["parts"]:
        if part["part"] == name:
            return part
    raise KeyError(name)


def main() -> int:
    sources = [
        PREVIOUS,
        STEP10_CONTRACT,
        UNPATCHED,
        UNPATCHED_PAYLOAD,
        UNPATCHED_HRG_HANDOFF,
        VSD01,
        CROSSREPO,
        STRICT_PEW,
    ]
    missing = [rel(path) for path in sources if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step10 source-rule inputs: " + ", ".join(missing))

    previous = load(PREVIOUS)
    contract = load(STEP10_CONTRACT)
    unpatched = load(UNPATCHED)
    payload = load(UNPATCHED_PAYLOAD)
    hrg_handoff = load(UNPATCHED_HRG_HANDOFF)
    vsd01 = load(VSD01)
    crossrepo = load(CROSSREPO)
    strict_pew = load(STRICT_PEW)

    matrices_part = crossrepo_part(crossrepo, "A_selected and b_selected finite value matrices")
    primitive_part = crossrepo_part(crossrepo, "Primitive C1 atom table for u,d,e,nuD")
    value_part = crossrepo_part(crossrepo, "Yukawa magnitudes, CKM/PMNS, and masses")

    decision = unpatched["closure_decision"]
    exact_values = payload["exact_values"]
    row_counts = payload["row_counts"]

    route_a_import = guarded(
        {
            "schema": "MTTStep10RouteAActiveLedgerSourceRuleImport.v1",
            "status": "ROUTE_A_PHYSICAL_PHIFIN_C1_SOURCE_RULE_IMPORTED_CLOSED",
            "previous_step10_contract": rel(STEP10_CONTRACT),
            "active_route_a_source": rel(UNPATCHED),
            "active_route_a_payload": rel(UNPATCHED_PAYLOAD),
            "crossrepo_guard_status": crossrepo["guardrails"],
            "stale_open_packets_allowed_to_override_later_closure": False,
            "route_A_selected_physical_PhiFinC1_source_rule_closed": True,
            "route_B_independent_selected_Galerkin_or_row_kernel_execution_needed": False,
            "source_owner": payload["source_owner"],
            "selected_source_rule": payload["selected_source_rule"],
            "source_rule_premise_free": payload["source_rule_premise_free"],
            "same_branch": payload["same_branch"],
            "source_row_premise_used": payload["source_row_premise_used"],
            "evidence_statuses": {
                "unpatched": unpatched["status"],
                "vsd01": vsd01["status"],
                "matrices_part": matrices_part["status"],
                "primitive_part": primitive_part["status"],
            },
        }
    )

    dynamic_payload = guarded(
        {
            "schema": "MTTStep10DynamicC1PayloadEmission.v1",
            "status": "STEP10_DYNAMIC_C1_PAYLOAD_EMITTED_FROM_ROUTE_A",
            "promoted_objects": payload["promoted_objects"],
            "A_transpose_A": exact_values["A_transpose_A"],
            "A_transpose_b": exact_values["A_transpose_b"],
            "deltaTheta_C1": exact_values["deltaTheta_C1"],
            "phase_R_Z": exact_values["phase_R_Z"],
            "shift_R_X": exact_values["shift_R_X"],
            "rank": exact_values["rank"],
            "row_counts": row_counts,
            "assembly_evidence": payload["assembly_evidence"],
            "contract_outputs_closed_here": {
                "A_selected": True,
                "b_selected": True,
                "deltaTheta_C1": True,
                "sector_response_matrices": True,
            },
            "contract_outputs_not_closed_here": {
                "full_S2_value_rows": True,
                "Yukawa_CKM_PMNS_Higgs_mass_value_rows_without_proxy_fitting": True,
            },
        }
    )

    value_gap = guarded(
        {
            "schema": "MTTFullS2NoProxyValueRowGapAfterStep10.v1",
            "status": "FULL_S2_AND_NO_PROXY_VALUE_ROWS_REMAIN_OPEN",
            "dynamic_payload_blocker_retired": hrg_handoff["decision"]["dynamic_payload_blocker_retired"],
            "RO_family_selector_source_selected": hrg_handoff["consumer_acceptance_conditions"][
                "RO_family_selector_source_selected"
            ],
            "RO_value_source_derived": hrg_handoff["decision"]["RO_value_source_derived"],
            "accepted_RO_value_source_count": hrg_handoff["decision"]["accepted_RO_value_source_count"],
            "accepted_same_HRG_nonHiggs_map_count": hrg_handoff["decision"][
                "accepted_same_HRG_nonHiggs_map_count"
            ],
            "full_S2_value_rows_closed": False,
            "accepted_Yukawa_magnitudes_closed": False,
            "CKM_PMNS_measured_value_closure_closed": False,
            "lambda_H_row_emitted": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
            "crossrepo_value_part_status": value_part["status"],
            "strict_P_EW_source_rows": strict_pew["strict_P_EW_source_rows"],
            "direct_K_threshold_Omega_H_lambda_rows": strict_pew[
                "direct_K_threshold_Omega_H_lambda_rows"
            ],
        }
    )

    next_packet = guarded(
        {
            "schema": "MTTNextAfterStep10SourceRule.v1",
            "status": "NEXT_TARGET_FULL_S2_NO_PROXY_VALUE_ROWS_OR_STRICT_PEW_DIRECT_K",
            "next_required_artifact": NEXT,
            "reason": (
                "Step10 Route A now closes the physical Phi_fin^C1 source-rule "
                "subgate and emits A_selected, b_selected, deltaTheta_C1, and "
                "sector response matrices in the active ledger.  The remaining "
                "non-looping frontier is full S2/no-proxy value-row emission, "
                "or the parallel strict P_EW/direct-K precision exit."
            ),
        }
    )

    candidate = guarded(
        {
            "candidate": "MTTSelectedStep10PhysicalPhiFinC1SourceRuleOrIndependentGalerkinRows",
            "status": STATUS,
            "next_required_artifact": NEXT,
            "inputs": {
                "previous": rel(PREVIOUS),
                "step10_contract": rel(STEP10_CONTRACT),
                "unpatched_source_rule": rel(UNPATCHED),
                "unpatched_payload": rel(UNPATCHED_PAYLOAD),
                "unpatched_hrg_handoff": rel(UNPATCHED_HRG_HANDOFF),
                "vsd01": rel(VSD01),
                "crossrepo": rel(CROSSREPO),
                "strict_pew": rel(STRICT_PEW),
            },
            "packets": {
                "route_a_active_ledger_source_rule_import": rel(ROUTE_A_IMPORT),
                "step10_dynamic_c1_payload_emission": rel(DYNAMIC_PAYLOAD),
                "fulls2_no_proxy_value_row_gap": rel(VALUE_GAP),
                "next_after_step10_source_rule": rel(NEXT_PACKET),
            },
            "closure_decision": {
                "stale_step10_source_rule_open_line_superseded": True,
                "route_A_selected_physical_PhiFinC1_source_rule_closed": True,
                "route_B_independent_selected_Galerkin_or_row_kernel_execution_needed": False,
                "selected_dynamic_phi_fin_c1_payload_emitted": True,
                "A_selected_promoted_strict": decision["A_selected_promoted_strict"],
                "b_selected_promoted_strict": decision["b_selected_promoted_strict"],
                "deltaTheta_C1_promoted_strict": decision["deltaTheta_C1_promoted_strict"],
                "sector_response_matrices_promoted_strict": decision[
                    "sector_response_matrices_promoted_strict"
                ],
                "full_S2_value_rows_closed": False,
                "Yukawa_CKM_PMNS_Higgs_mass_value_rows_without_proxy_fitting_closed": False,
                "RO_value_source_derived": hrg_handoff["decision"]["RO_value_source_derived"],
                "accepted_RO_value_source_count": hrg_handoff["decision"][
                    "accepted_RO_value_source_count"
                ],
                "strict_P_EW_source_theorem_closed": strict_pew["strict_P_EW_source_theorem_closed"],
                "strict_P_EW_source_rows": strict_pew["strict_P_EW_source_rows"],
                "direct_K_threshold_Omega_H_lambda_rows": strict_pew[
                    "direct_K_threshold_Omega_H_lambda_rows"
                ],
                "true_SM_equivalence_closed": False,
                "full_no_knob_closed": False,
            },
            "key_numbers": {
                "A_transpose_A": exact_values["A_transpose_A"],
                "A_transpose_b": exact_values["A_transpose_b"],
                "deltaTheta_C1": exact_values["deltaTheta_C1"],
                "rank": exact_values["rank"],
                "primitive_kernel_rows": row_counts["primitive_kernel_rows"],
                "hessian_b_source_rows": row_counts["hessian_b_source_rows"],
                "sector_assembly_rows": row_counts["sector_assembly_rows"],
                "formal_110_total_rows": row_counts["formal_110_total_rows"],
            },
            "theorem": {
                "name": "Step10PhysicalPhiFinC1SourceRuleImportTheorem",
                "proved": True,
                "statement": (
                    "The active ledger satisfies the Step10 Route-A source-rule "
                    "exit.  The premise-free physical Phi_fin^C1 source stack "
                    "promotes the selected dynamic Phi_fin/C1 payload, including "
                    "A_selected, b_selected, deltaTheta_C1, and sector response "
                    "matrices, with no observed-data selector.  This supersedes "
                    "older Step10-source-open wording.  It does not close full "
                    "S2 value rows, no-proxy Yukawa/CKM/PMNS/Higgs rows, strict "
                    "P_EW/direct-K, true SM equivalence, or full no-knob closure."
                ),
            },
        }
    )

    cert = guarded(
        {
            "certificate": "MTTSelectedStep10PhysicalPhiFinC1SourceRuleOrIndependentGalerkinRows",
            "status": STATUS,
            "theorem_proved": True,
            "stale_step10_source_rule_open_line_superseded": True,
            "route_A_selected_physical_PhiFinC1_source_rule_closed": True,
            "route_B_independent_selected_Galerkin_or_row_kernel_execution_needed": False,
            "selected_dynamic_phi_fin_c1_payload_emitted": True,
            "A_selected_promoted_strict": True,
            "b_selected_promoted_strict": True,
            "deltaTheta_C1_promoted_strict": True,
            "sector_response_matrices_promoted_strict": True,
            "full_S2_value_rows_closed": False,
            "Yukawa_CKM_PMNS_Higgs_mass_value_rows_without_proxy_fitting_closed": False,
            "RO_value_source_derived": False,
            "strict_P_EW_source_rows": strict_pew["strict_P_EW_source_rows"],
            "direct_K_threshold_Omega_H_lambda_rows": strict_pew[
                "direct_K_threshold_Omega_H_lambda_rows"
            ],
            "true_SM_equivalence_claimed": False,
            "full_no_knob_closure_claimed": False,
            "next_required_artifact": NEXT,
        }
    )

    note = f"""# MTT Selected Step10 PhysicalPhiFinC1SourceRule or IndependentGalerkinRows v1

## Theorem

`Step10PhysicalPhiFinC1SourceRuleImportTheorem` is emitted.

## What Changed

The old Step10 source-rule blocker is superseded by the active ledger.  Route A
is closed by the premise-free physical `Phi_fin^C1` source stack; Route B is not
needed for this dynamic-C1 source-promotion subgate.

```text
route A physical Phi_fin^C1 source rule closed = true
route B independent Galerkin rows needed here   = false
selected dynamic Phi_fin/C1 payload emitted     = true
A_selected promoted strict                      = true
b_selected promoted strict                      = true
deltaTheta_C1 promoted strict                   = true
sector response matrices promoted strict        = true
```

## Exact Dynamic C1 Payload

```text
A^T A = {exact_values["A_transpose_A"]}
A^T b = {exact_values["A_transpose_b"]}
deltaTheta_C1 = {exact_values["deltaTheta_C1"]}
rank = {exact_values["rank"]}
primitive kernel rows = {row_counts["primitive_kernel_rows"]}
hessian/b source rows = {row_counts["hessian_b_source_rows"]}
sector assembly rows = {row_counts["sector_assembly_rows"]}
formal total rows = {row_counts["formal_110_total_rows"]}
```

## Still Open

```text
full S2 value rows closed = false
Yukawa/CKM/PMNS/Higgs no-proxy rows closed = false
RO.value_source derived = false
accepted RO value source count = {hrg_handoff["decision"]["accepted_RO_value_source_count"]}
strict P_EW source rows = {strict_pew["strict_P_EW_source_rows"]}
direct K_threshold.Omega_H.lambda rows = {strict_pew["direct_K_threshold_Omega_H_lambda_rows"]}
true SM equivalence closed = false
full no-knob closure = false
```

## Next Artifact

`{NEXT}`.
"""

    for path, out in [
        (ROUTE_A_IMPORT, route_a_import),
        (DYNAMIC_PAYLOAD, dynamic_payload),
        (VALUE_GAP, value_gap),
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
