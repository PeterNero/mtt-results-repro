"""Build active-ledger dotD/C1 supersession and value-layer frontier.

The local full-sector payload chain was advanced by importing q79's selected
D_E/Riesz/Green gap layer.  The next named q79-only target still treats alpha1
and dotD as open.  The active SM ledger is stronger: Step40 imports same-branch
alpha1/dotD replay, and Step24 closes the dynamic C1/primitive first-response
source layer, including A_selected, b_selected, and deltaTheta_C1.

This artifact reconciles those timelines.  It prevents stale q79-only open
packets from overriding later verified active-ledger closures, then moves the
frontier to selected value-functional rows.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"
CERTS = ROOT / "certificates"

SLUG = "selected_activeledger_dotdc1supersession_or_valuelayerfrontier"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_ActiveLedger_dotDC1Supersession_or_ValueLayerFrontier_v1.md"

DEGREEN_IMPORT = DATA / "selected_visiblechernweildegreenimport_or_fullsectorpayloadupgrade.candidate.json"
STEP40 = DATA / "selected_step40_dotdtransport_alpha1import_or_primitivec1frontier.candidate.json"
STEP40_IMPORT = (
    DATA
    / "selected_step40_dotdtransport_alpha1import_or_primitivec1frontier"
    / "step40_dotd_transport_alpha1_import.packet.json"
)
STEP24 = DATA / "selected_step24_dynamicgate_reconciliation_or_valuelayercutset.candidate.json"
STEP24_CLOSED = (
    DATA
    / "selected_step24_dynamicgate_reconciliation_or_valuelayercutset"
    / "step24_selected_dynamic_bhessian_closure.packet.json"
)
STEP24_CUTSET = (
    DATA
    / "selected_step24_dynamicgate_reconciliation_or_valuelayercutset"
    / "step24_value_layer_cutset.packet.json"
)
Q79_DOTD = Path(
    r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro\certificates\q79_selected_dotd_alpha1_c1_response_emission_certificate.json"
)
Q79_DEGREEN = Path(
    r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro\certificates\q79_selected_trace_equals_emitted_27mode_operator_or_full_hym_newton_replay_certificate.json"
)

SUPERSESSION = PACKET_DIR / "active_ledger_supersession_decision.packet.json"
CLOSED_SOURCE_LAYER = PACKET_DIR / "closed_source_layer_after_step24.packet.json"
VALUE_FRONTIER = PACKET_DIR / "value_layer_frontier_after_source_closure.packet.json"
NEXT_PACKET = PACKET_DIR / "next_cutset_value_functional_rows.packet.json"

STATUS = "MTT_SELECTED_ACTIVELEDGER_DOTDC1SUPERSESSION_BUILT_VALUE_LAYER_FRONTIER_OPEN"
NEXT = "MTT_Selected_ThresholdResponseFunctionalRowEmission_or_ExternalSourceRowImport_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    sources = [DEGREEN_IMPORT, STEP40, STEP40_IMPORT, STEP24, STEP24_CLOSED, STEP24_CUTSET, Q79_DOTD, Q79_DEGREEN]
    missing = [rel(path) for path in sources if not path.exists()]
    if missing:
        raise FileNotFoundError("missing active-ledger dotD/C1 supersession inputs: " + ", ".join(missing))

    degreen = load(DEGREEN_IMPORT)
    step40 = load(STEP40)
    step40_import = load(STEP40_IMPORT)
    step24 = load(STEP24)
    step24_closed = load(STEP24_CLOSED)
    step24_cutset = load(STEP24_CUTSET)
    q79_dotd = load(Q79_DOTD)
    q79_degreen = load(Q79_DEGREEN)

    step40_decision = step40["closure_decision"]
    step24_decision = step24["closure_decision"]
    step24_items = step24_closed["step24_closed_items"]

    dotd_closed = (
        step40_decision["selected_dotD_transport_derivative_formula_closed"]
        and step40_decision["selected_alpha1_driver_normalization_closed"]
        and step40_decision["same_branch_dotD_alpha1_values_closed"]
        and step40_decision["honest_dotD_alpha1_replay_closed"]
    )
    c1_first_response_closed = (
        step24_decision["selected_dynamic_overlap_tensor_or_transfer_functor"]
        and step24_decision["selected_primitive_C1_contractions_first_response_layer"]
        and step24_decision["selected_A_selected_promoted"]
        and step24_decision["selected_b_selected_promoted"]
        and step24_decision["selected_deltaTheta_C1_promoted"]
    )
    source_layer_closed = dotd_closed and c1_first_response_closed

    supersession = {
        "schema": "MTTActiveLedgerDotDC1SupersessionDecision.v1",
        "status": "STALE_Q79_ONLY_DOTD_OPEN_WORDING_SUPERSEDED",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "stale_packet": rel(Q79_DOTD),
        "stale_packet_status": q79_dotd["status"],
        "stale_open_claims": {
            "selected_dotD_source_theorem": q79_dotd["what_remains_open"]["selected_dotD_source_theorem"],
            "same_branch_alpha1_driver_theorem": q79_dotd["what_remains_open"]["same_branch_alpha1_driver_theorem"],
            "selected_primitive_C1_contractions": q79_dotd["what_remains_open"]["selected_primitive_C1_contractions"],
            "A_selected": q79_dotd["what_remains_open"]["A_selected"],
            "b_selected": q79_dotd["what_remains_open"]["b_selected"],
        },
        "superseding_packets": {
            "step40_dotd_alpha1_import": rel(STEP40),
            "step24_dynamic_gate_reconciliation": rel(STEP24),
            "degreen_import_context": rel(DEGREEN_IMPORT),
        },
        "superseded_now": {
            "selected_dotD_source_theorem": dotd_closed,
            "same_branch_alpha1_driver_theorem": dotd_closed,
            "honest_dotD_replay_without_lifted_flags": dotd_closed,
            "selected_primitive_C1_contractions_first_response_layer": c1_first_response_closed,
            "A_selected": step24_decision["selected_A_selected_promoted"],
            "b_selected": step24_decision["selected_b_selected_promoted"],
            "deltaTheta_C1": step24_decision["selected_deltaTheta_C1_promoted"],
        },
        "guardrail": (
            "This is an active-ledger supersession, not a q79-only proof rewrite. "
            "The closure is valid in the SM closure ledger because Step40 and Step24 are verified there."
        ),
    }

    closed_source_layer = {
        "schema": "MTTClosedSourceLayerAfterStep24.v1",
        "status": "SOURCE_LAYER_CLOSED_VALUE_FUNCTIONAL_ROWS_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closed_inputs": {
            "selected_27mode_DE_trace_equality": degreen["closure_decision"]["selected_trace_equality_for_27mode_DE"],
            "selected_DE_Riesz_Green_gap_layer": degreen["closure_decision"]["D_E_Riesz_Green_gap_layer_closed"],
            "selected_dotD_alpha1_transport_formula": step40_decision[
                "selected_dotD_transport_derivative_formula_closed"
            ],
            "selected_alpha1_driver_normalization": step40_decision[
                "selected_alpha1_driver_normalization_closed"
            ],
            "honest_dotD_alpha1_replay": step40_decision["honest_dotD_alpha1_replay_closed"],
            "selected_source_to_C1_transfer_map": step24_decision["selected_source_to_C1_transfer_map_emitted"],
            "selected_dynamic_overlap_tensor": step24_decision[
                "selected_dynamic_overlap_tensor_or_transfer_functor"
            ],
            "selected_primitive_C1_first_response_layer": step24_decision[
                "selected_primitive_C1_contractions_first_response_layer"
            ],
            "selected_A_selected": step24_decision["selected_A_selected_promoted"],
            "selected_b_selected": step24_decision["selected_b_selected_promoted"],
            "selected_deltaTheta_C1": step24_decision["selected_deltaTheta_C1_promoted"],
            "selected_Hessian_source_normalization": step24_decision[
                "selected_Hessian_source_normalization_promoted"
            ],
        },
        "formal_rows": {
            "formal_110_rows_executed": step24_closed["vsd01_assembly"]["row_evidence"][
                "formal_110_rows_executed"
            ],
            "formal_110_total_rows": step24_closed["vsd01_assembly"]["row_evidence"][
                "formal_110_row_counts"
            ]["total_rows"],
            "all_72_primitive_rows_exact": step24_closed["vsd01_assembly"]["row_evidence"][
                "all_72_primitive_rows_exact"
            ],
            "formal_110_max_abs_error": step24_closed["vsd01_assembly"]["row_evidence"][
                "formal_110_max_abs_error"
            ],
        },
        "source_layer_closed": source_layer_closed,
    }

    value_frontier = {
        "schema": "MTTValueLayerFrontierAfterSourceClosure.v1",
        "status": "VALUE_FUNCTIONAL_ROWS_OPEN_AFTER_SOURCE_LAYER_CLOSURE",
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "active_frontier_now": step24_cutset["active_frontier_now"],
        "source_layer_closed": step24_cutset["current_value_frontier"]["source_layer_closed"],
        "value_layer_required_rows": step24_cutset["current_value_frontier"]["value_layer_required_rows"],
        "value_layer_accepted_source_rows": step24_cutset["current_value_frontier"][
            "value_layer_accepted_source_rows"
        ],
        "accepted_true_value_source_row_emitted": step24_cutset["current_value_frontier"][
            "accepted_true_value_source_row_emitted"
        ],
        "still_open": step24_cutset["still_open"],
        "not_a_source_promotion_blocker_anymore": [
            "selected D_E/Riesz/Green gap layer",
            "selected dotD_alpha1 and alpha1 driver",
            "selected primitive C1 first-response layer",
            "A_selected, b_selected, deltaTheta_C1",
        ],
    }

    next_packet = {
        "schema": "MTTNextCutsetValueFunctionalRows.v1",
        "status": "NEXT_IS_THRESHOLD_RESPONSE_OR_EXTERNAL_ROW_IMPORT",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closed_now": [
            "q79 D_E/Riesz/Green gap layer imported",
            "active-ledger selected dotD_alpha1 and alpha1 driver imported",
            "active-ledger primitive C1 first-response layer imported",
            "active-ledger A_selected, b_selected, and deltaTheta_C1 imported",
            "old q79-only dotD/C1 open wording superseded for this repo",
        ],
        "still_open": [
            "selected threshold response functional rows",
            "selected Yukawa/Higgs value functional",
            "accepted threshold/mass-scheme source rows",
            "accepted Yukawa magnitudes for true precision",
            "CKM/PMNS measured value closure",
            "full correlated likelihood source",
            "full no-knob closure",
            "true SM equivalence closure",
        ],
        "next_required_artifact": NEXT,
        "why": "The source/operator layer is closed in the active ledger; accepted value-functional rows remain zero.",
    }

    candidate = {
        "candidate": "MTTSelectedActiveLedgerDotDC1SupersessionOrValueLayerFrontier",
        "status": STATUS,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "ActiveLedgerDotDC1SupersessionTheorem",
            "proved": True,
            "statement": (
                "In the verified active SM ledger, q79-only dotD/C1-open wording is superseded by Step40 and Step24. "
                "Step40 closes selected dotD_alpha1, alpha1 driver normalization, and honest dotD replay. "
                "Step24 closes the dynamic C1/primitive first-response layer, A_selected, b_selected, and deltaTheta_C1. "
                "Therefore the current frontier is selected value-functional rows, not source-promotion, Galerkin replay, or primitive C1 construction."
            ),
        },
        "closure_decision": {
            "active_ledger_supersession_built": True,
            "DE_Green_gap_layer_closed": degreen["closure_decision"]["D_E_Riesz_Green_gap_layer_closed"],
            "dotD_alpha1_closed_by_active_ledger": dotd_closed,
            "primitive_C1_first_response_layer_closed_by_active_ledger": c1_first_response_closed,
            "A_selected_closed_by_active_ledger": step24_decision["selected_A_selected_promoted"],
            "b_selected_closed_by_active_ledger": step24_decision["selected_b_selected_promoted"],
            "deltaTheta_C1_closed_by_active_ledger": step24_decision["selected_deltaTheta_C1_promoted"],
            "source_layer_closed": source_layer_closed,
            "accepted_value_functional_rows_closed": step24_decision["accepted_value_functional_rows_closed"],
            "accepted_Yukawa_magnitudes_closed": step24_decision["accepted_Yukawa_magnitudes_closed"],
            "accepted_threshold_mass_scheme_source_rows_closed": step24_decision[
                "accepted_threshold_mass_scheme_source_rows_closed"
            ],
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "packets": {
            "active_ledger_supersession_decision": rel(SUPERSESSION),
            "closed_source_layer_after_step24": rel(CLOSED_SOURCE_LAYER),
            "value_layer_frontier_after_source_closure": rel(VALUE_FRONTIER),
            "next_cutset": rel(NEXT_PACKET),
        },
    }

    cert = {
        "certificate": "MTTSelectedActiveLedgerDotDC1SupersessionOrValueLayerFrontierCertificate",
        "status": STATUS,
        "theorem": candidate["theorem"]["name"],
        "active_ledger_supersession_built": True,
        "DE_Green_gap_layer_closed": degreen["closure_decision"]["D_E_Riesz_Green_gap_layer_closed"],
        "dotD_alpha1_closed_by_active_ledger": dotd_closed,
        "primitive_C1_first_response_layer_closed_by_active_ledger": c1_first_response_closed,
        "A_selected_closed_by_active_ledger": step24_decision["selected_A_selected_promoted"],
        "b_selected_closed_by_active_ledger": step24_decision["selected_b_selected_promoted"],
        "deltaTheta_C1_closed_by_active_ledger": step24_decision["selected_deltaTheta_C1_promoted"],
        "source_layer_closed": source_layer_closed,
        "accepted_value_functional_rows_closed": step24_decision["accepted_value_functional_rows_closed"],
        "accepted_Yukawa_magnitudes_closed": step24_decision["accepted_Yukawa_magnitudes_closed"],
        "accepted_threshold_mass_scheme_source_rows_closed": step24_decision[
            "accepted_threshold_mass_scheme_source_rows_closed"
        ],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected ActiveLedger dotDC1Supersession or ValueLayerFrontier v1

Status: `{STATUS}`

## Theorem

`ActiveLedgerDotDC1SupersessionTheorem` is proved.

The active SM ledger supersedes the older q79-only `dotD_alpha1/C1` open
wording.  Step40 and Step24 are verified in this repo and move the frontier out
of source-promotion/Galerkin replay.

## Closed In Active Ledger

- selected `D_E/Riesz/Green` gap layer: `{degreen["closure_decision"]["D_E_Riesz_Green_gap_layer_closed"]}`
- selected `dotD_alpha1` and alpha1 driver: `{dotd_closed}`
- honest `dotD_alpha1` replay: `{step40_decision["honest_dotD_alpha1_replay_closed"]}`
- primitive `C1` first-response layer: `{c1_first_response_closed}`
- `A_selected`: `{step24_decision["selected_A_selected_promoted"]}`
- `b_selected`: `{step24_decision["selected_b_selected_promoted"]}`
- `deltaTheta_C1`: `{step24_decision["selected_deltaTheta_C1_promoted"]}`

## Still Open

- accepted value-functional rows: `{step24_decision["accepted_value_functional_rows_closed"]}`
- accepted Yukawa magnitudes: `{step24_decision["accepted_Yukawa_magnitudes_closed"]}`
- accepted threshold/mass-scheme source rows: `{step24_decision["accepted_threshold_mass_scheme_source_rows_closed"]}`
- true SM equivalence: `False`
- full no-knob closure: `False`

## Next Artifact

`{NEXT}`.
"""

    write_json(SUPERSESSION, supersession)
    write_json(CLOSED_SOURCE_LAYER, closed_source_layer)
    write_json(VALUE_FRONTIER, value_frontier)
    write_json(NEXT_PACKET, next_packet)
    write_json(CANDIDATE, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
