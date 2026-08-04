"""Build Phi_sector_N source-value inventory / no-knob csk rows gate.

The previous packet closed the common-circle trace engine

    c_{s,k} = Tr_N(P_s B_k H_cen Phi_sector_N).

This packet attacks the remaining value object directly.  It imports every
currently accepted nearby source feed that could plausibly emit Phi_sector_N:
common-circle trace execution, source-normalized sector projection weights,
first dynamic matter/overlap rows, full-S2/dynamic payload attempts, and the
threshold-response functional attempts.

The result is intentionally strict: unit-normalized projection weights and
first dynamic rows are accepted as support, but they are not magnitude-bearing
Phi_sector_N values and cannot be promoted to the nine c_{s,k} rows.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"
CERTS = ROOT / "certificates"

SLUG = "selected_phisectornsourcevalues_or_noknobcskrows"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PhiSectorNSourceValues_or_NoKnobCSKRows_v1.md"

COMMON_CIRCLE_EXEC = DATA / "selected_commoncirclesectorresponseexecution_or_csktracerows.candidate.json"
PHI_CONTRACT = (
    DATA
    / "selected_commoncirclesectorresponseexecution_or_csktracerows"
    / "phi_sector_n_source_value_contract.packet.json"
)
TRACE_ROWS = (
    DATA
    / "selected_commoncirclesectorresponseexecution_or_csktracerows"
    / "formal_csk_trace_rows_and_policy_replay_guard.packet.json"
)
SOURCE_WEIGHTS = (
    DATA
    / "selected_thresholdresponserows_or_sectorprojectionweightsexecution"
    / "source_normalized_sector_projection_weights.packet.json"
)
FIRST_DYNAMIC_ROW = (
    DATA
    / "selected_thresholdresponserows_or_sectorprojectionweightsexecution"
    / "first_dynamic_row_repromotion.packet.json"
)
THRESHOLD_DECISION = (
    DATA
    / "selected_thresholdresponserows_or_sectorprojectionweightsexecution"
    / "threshold_rows_or_projection_weights_decision.packet.json"
)
THRESHOLD_FUNCTIONAL = (
    DATA
    / "selected_higherresponsesectorcoefficients_or_thresholdfunctionalsourcerows"
    / "selected_threshold_response_functional_execution_attempt.packet.json"
)
FULLS2 = DATA / "selected_fulls2noproxyvaluerows_or_strictpewdirectkexit.candidate.json"
DYNAMIC_PAYLOAD = DATA / "selected_dynamicphifinc1payloadrows_or_higherresponseexecution.candidate.json"
SAME_SOURCE_DYNAMIC = (
    DATA
    / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure"
    / "selected_non_scalar_dynamic_overlap_values.packet.json"
)

INVENTORY_PACKET = PACKET_DIR / "phisectorn_candidate_source_inventory.packet.json"
PROMOTION_PACKET = PACKET_DIR / "phisectorn_value_promotion_decision.packet.json"
TRACE_ACCEPTANCE_PACKET = PACKET_DIR / "csk_trace_acceptance_after_phisectorn_inventory.packet.json"
NEXT_PACKET = PACKET_DIR / "next_cutset_after_phisectorn_inventory.packet.json"

STATUS = (
    "MTT_SELECTED_PHISECTORNVALUES_OR_NOKNOBCSKROWS_"
    "SOURCE_INVENTORY_CLOSED_VALUES_OPEN"
)
NEXT = "MTT_Selected_SectorResponseDensitySourceTheorem_or_NoKnobCSKRowEmission_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    sources = [
        COMMON_CIRCLE_EXEC,
        PHI_CONTRACT,
        TRACE_ROWS,
        SOURCE_WEIGHTS,
        FIRST_DYNAMIC_ROW,
        THRESHOLD_DECISION,
        THRESHOLD_FUNCTIONAL,
        FULLS2,
        DYNAMIC_PAYLOAD,
        SAME_SOURCE_DYNAMIC,
    ]
    missing = [rel(path) for path in sources if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Phi_sector_N source inventory inputs: " + ", ".join(missing))

    common = load(COMMON_CIRCLE_EXEC)
    phi_contract = load(PHI_CONTRACT)
    trace_rows = load(TRACE_ROWS)
    source_weights = load(SOURCE_WEIGHTS)
    first_dynamic = load(FIRST_DYNAMIC_ROW)
    threshold_decision = load(THRESHOLD_DECISION)
    threshold_functional = load(THRESHOLD_FUNCTIONAL)
    fulls2 = load(FULLS2)
    dynamic_payload = load(DYNAMIC_PAYLOAD)
    same_source_dynamic = load(SAME_SOURCE_DYNAMIC)

    weight_rows = source_weights["sector_weights"]
    source_normalized_count = sum(
        1
        for row in weight_rows
        if row["source_normalized_weight"] == 1.0 and row["magnitude_bearing_weight"] is None
    )
    first_dynamic_selected = bool(first_dynamic["accepted_as_selected_source_normalized_projection_row_now"])
    first_dynamic_magnitude = bool(first_dynamic["accepted_as_magnitude_or_threshold_source_row"])
    threshold_source_rows = int(threshold_functional["accepted_source_row_count"])
    fulls2_closure = fulls2.get("closure", fulls2.get("closure_decision", {}))
    dynamic_payload_closure = dynamic_payload.get("closure", dynamic_payload.get("closure_decision", {}))
    fulls2_dynamic_rows = int(fulls2_closure["accepted_selected_dynamic_value_row_count"])
    dynamic_payload_rows = int(dynamic_payload_closure["accepted_dynamic_payload_row_count"])

    source_inventory = {
        "schema": "MTTPhiSectorNSourceInventory.v1",
        "status": "PHI_SECTOR_N_SOURCE_INVENTORY_CLOSED_NO_NUMERIC_VALUES",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs_checked": {
            "common_circle_trace_execution": rel(COMMON_CIRCLE_EXEC),
            "phi_sector_n_contract": rel(PHI_CONTRACT),
            "formal_csk_trace_rows": rel(TRACE_ROWS),
            "source_normalized_sector_projection_weights": rel(SOURCE_WEIGHTS),
            "first_dynamic_row_repromotion": rel(FIRST_DYNAMIC_ROW),
            "threshold_decision": rel(THRESHOLD_DECISION),
            "threshold_functional": rel(THRESHOLD_FUNCTIONAL),
            "full_s2_gate": rel(FULLS2),
            "dynamic_payload_gate": rel(DYNAMIC_PAYLOAD),
            "same_source_dynamic_overlap_values": rel(SAME_SOURCE_DYNAMIC),
        },
        "accepted_support": [
            {
                "support_id": "common_circle_trace_engine",
                "accepted": common["closure_decision"]["formal_csk_trace_rows_executed"],
                "what_it_supplies": "H_cen, sector projectors, family dual trace basis, formal row execution",
                "why_not_phi_sector_n_value": "Trace engine supplies the evaluator, not the sector response density values.",
            },
            {
                "support_id": "source_normalized_sector_projection_weights",
                "accepted": source_weights["source_projection_weights_closed"],
                "row_count": source_normalized_count,
                "what_it_supplies": "unit source-normalized u/e phase and d/nuD shift projection weights",
                "why_not_phi_sector_n_value": "All emitted weights are unit-normalized and explicitly non-magnitude-bearing.",
            },
            {
                "support_id": "first_dynamic_matter_overlap_rows",
                "accepted": first_dynamic_selected,
                "row_count": 2 if first_dynamic_selected else 0,
                "what_it_supplies": "selected first dynamic phase-response support for u/e",
                "why_not_phi_sector_n_value": "The packet rejects use as a magnitude or threshold source row.",
            },
            {
                "support_id": "full_s2_first_dynamic_rows",
                "accepted": fulls2_closure["first_selected_dynamic_matter_overlap_value_row_accepted"],
                "row_count": fulls2_dynamic_rows,
                "what_it_supplies": "accepted selected dynamic subrows",
                "why_not_phi_sector_n_value": "Full S2 Yukawa/CKM/PMNS/Higgs value rows remain open.",
            },
        ],
        "rejected_or_open_feeds": [
            {
                "feed_id": "threshold_response_functional",
                "accepted_source_row_count": threshold_source_rows,
                "closed": threshold_functional["selected_threshold_response_functional_closed"],
                "blocking_reason": "No selected response functional maps dynamic packet to magnitude/threshold rows.",
            },
            {
                "feed_id": "dynamic_phi_fin_c1_payload_rows",
                "accepted_dynamic_payload_row_count": dynamic_payload_rows,
                "closed": dynamic_payload_closure["no_knob_value_derivation_closed"],
                "blocking_reason": "Support candidates exist, but accepted scalar/dynamic payload rows are zero.",
            },
            {
                "feed_id": "same_source_dynamic_overlap_values",
                "status": same_source_dynamic["status"],
                "blocking_reason": "It emits first dynamic overlap structure, not nine sector-resolving Phi_sector_N coefficients.",
            },
        ],
        "counts": {
            "phi_sector_n_required_numeric_values": phi_contract["row_count"],
            "phi_sector_n_numeric_values_emitted": 0,
            "accepted_phi_sector_n_source_values": 0,
            "accepted_source_normalized_projection_rows": source_normalized_count,
            "accepted_first_dynamic_support_rows": 2 if first_dynamic_selected else 0,
            "accepted_magnitude_bearing_projection_rows": 0,
            "accepted_threshold_response_source_rows": threshold_source_rows,
            "accepted_dynamic_payload_rows": dynamic_payload_rows,
        },
    }

    promotion_rows = []
    for row in phi_contract["rows"]:
        promotion_rows.append(
            {
                "row_id": row["row_id"],
                "sector": row["sector"],
                "coefficient": row["coefficient"],
                "source_value_emitted": False,
                "accepted_as_strict_source": False,
                "policy_replay_value_quarantined": row["policy_replay_value_for_later_comparison"],
                "best_current_support": [
                    "common-circle trace engine",
                    "source-normalized projection skeleton",
                    "first dynamic overlap support",
                ],
                "blocking_reason": (
                    "No selected sector-resolving finite response density value "
                    "Phi_sector_N.s.ck is emitted before policy replay."
                ),
            }
        )

    promotion_decision = {
        "schema": "MTTPhiSectorNValuePromotionDecision.v1",
        "status": "PHI_SECTOR_N_VALUE_PROMOTION_REJECTED_STRICT_VALUES_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "source_inventory": rel(INVENTORY_PACKET),
        "required_row_count": phi_contract["row_count"],
        "accepted_strict_phi_sector_n_row_count": 0,
        "accepted_policy_replay_row_count": 0,
        "rows": promotion_rows,
        "guardrail": {
            "unit_projection_weights_promoted_to_magnitudes": False,
            "first_dynamic_rows_promoted_to_csk_coefficients": False,
            "policy_values_promoted_to_source": False,
            "observed_yukawa_or_ckm_values_used_as_selectors": False,
        },
    }

    trace_acceptance = {
        "schema": "MTTCSKTraceAcceptanceAfterPhiSectorNInventory.v1",
        "status": "FORMAL_TRACE_ENGINE_READY_STRICT_CSK_ROWS_STILL_ZERO",
        "closure_claimed": True,
        "formal_trace_row_count": trace_rows["formal_trace_row_count"],
        "formal_trace_rows_executed": trace_rows["formal_trace_rows_executed"],
        "accepted_strict_phi_sector_n_row_count": 0,
        "accepted_strict_csk_source_row_count": 0,
        "policy_replay_rows_accepted_as_source": False,
        "would_close_if_next_artifact_emits": [
            "nine selected Phi_sector_N.s.ck finite response density values",
            "row-level certificates independent of policy replay and observed values",
            "trace re-execution showing c_{s,k}=Tr_N(P_s B_k H_cen Phi_sector_N)",
        ],
    }

    next_packet = {
        "schema": "MTTNextCutsetAfterPhiSectorNInventory.v1",
        "status": "NEXT_IS_SECTOR_RESPONSE_DENSITY_SOURCE_THEOREM",
        "closure_claimed": True,
        "closed_now": [
            "all nearby source feeds inventoried",
            "source-normalized projection weights separated from magnitude-bearing rows",
            "first dynamic support rows separated from csk coefficient source values",
            "policy replay values kept quarantined",
            "strict missing object reduced to selected sector response density values",
        ],
        "still_open": [
            "selected sector-resolving finite response density Phi_sector_N",
            "nine numeric Phi_sector_N.s.ck row certificates",
            "strict no-knob c_{s,k} row emission",
            "Yukawa magnitude prediction from MTT alone",
        ],
        "next_required_artifact": NEXT,
        "ordered_attack": [
            "derive Phi_sector_N as a same-source finite response density inside A_N",
            "emit the nine row values from selected HYM/Strominger/threshold response data",
            "rerun the existing common-circle trace engine",
            "accept c_{s,k} only if every row has a source certificate before replay",
        ],
    }

    candidate = {
        "candidate": "MTTSelectedPhiSectorNSourceValuesOrNoKnobCSKRows",
        "status": STATUS,
        "closure_claimed": True,
        "strict_phi_sector_n_values_claimed": False,
        "strict_csk_source_theorem_claimed": False,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "PhiSectorNSourceValueInventoryTheorem",
            "proved": True,
            "statement": (
                "Given the current selected source corpus, the common-circle trace engine and "
                "source-normalized projection support are closed, but no accepted packet emits "
                "the nine selected numeric Phi_sector_N values required to promote the formal "
                "c_{s,k} rows to strict no-knob source rows."
            ),
        },
        "closure_decision": {
            "common_circle_trace_engine_closed": True,
            "source_inventory_closed": True,
            "source_normalized_sector_projection_weights_closed": source_weights[
                "source_projection_weights_closed"
            ],
            "first_dynamic_support_rows_accepted": 2 if first_dynamic_selected else 0,
            "first_dynamic_rows_magnitude_bearing": first_dynamic_magnitude,
            "threshold_response_functional_closed": threshold_functional[
                "selected_threshold_response_functional_closed"
            ],
            "Phi_sector_N_required_numeric_value_count": phi_contract["row_count"],
            "Phi_sector_N_numeric_values_emitted": False,
            "accepted_Phi_sector_N_source_value_count": 0,
            "accepted_strict_csk_source_row_count": 0,
            "policy_replay_rows_accepted_as_source": False,
            "strict_csk_source_theorem_closed": False,
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "packets": {
            "source_inventory": rel(INVENTORY_PACKET),
            "promotion_decision": rel(PROMOTION_PACKET),
            "trace_acceptance": rel(TRACE_ACCEPTANCE_PACKET),
            "next_cutset": rel(NEXT_PACKET),
        },
    }

    cert = {
        "certificate": "MTTSelectedPhiSectorNSourceValuesOrNoKnobCSKRowsCertificate",
        "status": STATUS,
        "theorem": candidate["theorem"]["name"],
        "source_inventory_closed": True,
        "source_normalized_sector_projection_weights_closed": True,
        "first_dynamic_support_rows_accepted": 2 if first_dynamic_selected else 0,
        "accepted_magnitude_bearing_projection_rows": 0,
        "accepted_threshold_response_source_rows": threshold_source_rows,
        "Phi_sector_N_required_numeric_value_count": phi_contract["row_count"],
        "Phi_sector_N_numeric_values_emitted": False,
        "accepted_Phi_sector_N_source_value_count": 0,
        "accepted_strict_csk_source_row_count": 0,
        "policy_replay_rows_accepted_as_source": False,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected PhiSectorNSourceValues or NoKnobCSKRows v1

Status: `{STATUS}`

## Theorem

`PhiSectorNSourceValueInventoryTheorem` is proved.

The current source corpus closes the common-circle trace engine and support
skeleton:

- `H_cen`, sector projectors, and family dual trace rows are already selected.
- source-normalized sector projection weights are selected for the phase/shift
  lanes.
- the first dynamic matter/overlap support rows are accepted as source-normalized
  support.

But none of those rows is a magnitude-bearing sector response density.  The
selected threshold response functional emits `0` source rows, dynamic payload
emission emits `0` accepted payload rows, and `Phi_sector_N` numeric values
remain unemitted.

## Counts

- required `Phi_sector_N` values: `{phi_contract["row_count"]}`
- accepted strict `Phi_sector_N` values: `0`
- accepted strict `c_{{s,k}}` source rows: `0`
- accepted source-normalized projection rows: `{source_normalized_count}`
- accepted first dynamic support rows: `{2 if first_dynamic_selected else 0}`
- accepted magnitude-bearing projection rows: `0`

## Boundary

The nine policy coefficients remain quarantined as replay/comparison data.
Promoting them, or promoting unit projection weights, would reintroduce the
same measured-value/policy shortcut this proof chain is trying to remove.

## Next Artifact

`{NEXT}`.
"""

    write_json(INVENTORY_PACKET, source_inventory)
    write_json(PROMOTION_PACKET, promotion_decision)
    write_json(TRACE_ACCEPTANCE_PACKET, trace_acceptance)
    write_json(NEXT_PACKET, next_packet)
    write_json(CANDIDATE, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
