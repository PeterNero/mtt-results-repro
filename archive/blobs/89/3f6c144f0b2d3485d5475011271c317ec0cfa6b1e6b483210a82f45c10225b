"""Build visible Chern-Weil / D_E-Green import for full-sector payload upgrade.

The previous local artifact fixed the full-sector HYM payload contract and kept
full-sector D_E/Riesz/Green open according to the local Step39 frontier.  The
q79 proof repo has a newer, stronger theorem:

    Q79SelectedTraceEqualsEmitted27ModeDEGapLayerTheorem.

It proves selected trace equality for the emitted 27-mode D_E formula and locks
the D_E gap/Riesz/Green layer.  This artifact imports that result into the SM
closure matrix path.  It upgrades the D_E/Riesz/Green part of the payload while
preserving the guardrail: dotD_alpha1, primitive C1, A_selected, b_selected,
Delta_S2 rows, and strict c_{s,k} rows are still open.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"
CERTS = ROOT / "certificates"
Q79_CERTS = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro\certificates")

SLUG = "selected_visiblechernweildegreenimport_or_fullsectorpayloadupgrade"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_VisibleChernWeilDEGreenImport_or_FullSectorPayloadUpgrade_v1.md"

LOCAL_PAYLOAD = DATA / "selected_fullsectorhymoperatorpayload_or_deltas2rowemission.candidate.json"
LOCAL_PAYLOAD_LEDGER = (
    DATA
    / "selected_fullsectorhymoperatorpayload_or_deltas2rowemission"
    / "fullsector_hym_payload_field_ledger.packet.json"
)
LOCAL_ROW_BRIDGE = (
    DATA
    / "selected_fullsectorhymoperatorpayload_or_deltas2rowemission"
    / "deltas2_row_emission_bridge_after_fullsector_payload.packet.json"
)
Q79_TRACE = Q79_CERTS / "q79_selected_trace_equals_emitted_27mode_operator_or_full_hym_newton_replay_certificate.json"
Q79_DOTD = Q79_CERTS / "q79_selected_dotd_alpha1_c1_response_emission_certificate.json"
Q79_DE_GREEN = Q79_CERTS / "q79_selected_de_green_dotd_source_for_primitive_c1_certificate.json"
Q79_VISIBLE = Q79_CERTS / "q79_selected_visible_bundle_operator_source_or_primitive_c1_contractions_certificate.json"

IMPORT_LEDGER = PACKET_DIR / "visible_chernweil_degreen_import_ledger.packet.json"
PAYLOAD_UPGRADE = PACKET_DIR / "fullsector_payload_upgrade_after_q79_trace.packet.json"
ROW_GATE = PACKET_DIR / "deltas2_row_gate_after_degreen_import.packet.json"
NEXT_PACKET = PACKET_DIR / "next_cutset_after_degreen_import.packet.json"

STATUS = "MTT_SELECTED_VISIBLECHERNWEIL_DEGREEN_IMPORT_BUILT_DOTD_C1_ROWS_OPEN"
NEXT = "Q79_Selected_Alpha1_Tangent_or_Retarded_Overlap_Kernel_v1"


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
    sources = [LOCAL_PAYLOAD, LOCAL_PAYLOAD_LEDGER, LOCAL_ROW_BRIDGE, Q79_TRACE, Q79_DOTD, Q79_DE_GREEN, Q79_VISIBLE]
    missing = [rel(path) for path in sources if not path.exists()]
    if missing:
        raise FileNotFoundError("missing visible Chern-Weil/D_E-Green import inputs: " + ", ".join(missing))

    local_payload = load(LOCAL_PAYLOAD)
    local_ledger = load(LOCAL_PAYLOAD_LEDGER)
    local_row_bridge = load(LOCAL_ROW_BRIDGE)
    q79_trace = load(Q79_TRACE)
    q79_dotd = load(Q79_DOTD)
    q79_de_green = load(Q79_DE_GREEN)
    q79_visible = load(Q79_VISIBLE)

    trace_layer = q79_trace["selected_trace_equality_gap_layer_proof"]
    trace_closes = q79_trace["what_closes_now"]
    dotd_frontier = q79_dotd["dotd_alpha1_frontier"]
    dotd_obstruction = q79_dotd["selected_tangent_or_retarded_kernel_obstruction"]

    de_gap_closed = trace_closes["D_E_source_flags_theorem_derived"] and trace_closes[
        "selected_Riesz_Green_gap_layer_closed"
    ]
    selected_trace_closed = trace_closes["selected_trace_equality_for_emitted_27mode_DE"]
    dotd_source_closed = not q79_dotd["what_remains_open"]["selected_dotD_source_theorem"]
    primitive_c1_closed = not q79_dotd["what_remains_open"]["selected_primitive_C1_contractions"]

    import_ledger = {
        "schema": "MTTVisibleChernWeilDEGreenImportLedger.v1",
        "status": "Q79_DE_GREEN_GAP_LAYER_IMPORTED_DOTD_C1_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "imported_certificates": {
            "q79_trace_equals_27mode_de": rel(Q79_TRACE),
            "q79_de_green_dotd_source_gate": rel(Q79_DE_GREEN),
            "q79_dotd_alpha1_c1_response": rel(Q79_DOTD),
            "q79_visible_operator_or_primitive_c1": rel(Q79_VISIBLE),
        },
        "imported_closed_layers": {
            "selected_trace_equality_for_27mode_DE": selected_trace_closed,
            "D_E_source_flags_theorem_derived": trace_closes["D_E_source_flags_theorem_derived"],
            "D_E_honest_replay_contract_locked": trace_closes["D_E_honest_replay_contract_locked"],
            "selected_Riesz_Green_gap_layer_closed": trace_closes["selected_Riesz_Green_gap_layer_closed"],
            "positive_selected_gap_lower_bound": trace_closes["positive_selected_gap_lower_bound"],
            "selected_eta_N_below_threshold": trace_closes["selected_eta_N_below_threshold"],
        },
        "selected_gap_layer": {
            "basis_id": trace_layer["gap_layer"]["basis_id"],
            "basis_dimension": trace_layer["gap_layer"]["basis_dimension"],
            "selected_eta_N": trace_layer["gap_layer"]["selected_eta_N"],
            "eta_threshold": trace_layer["gap_layer"]["eta_threshold"],
            "selected_gap_lower_bound": trace_layer["gap_layer"]["selected_gap_lower_bound"],
            "selected_green_norm_bound": trace_layer["gap_layer"]["selected_green_norm_bound"],
            "zero_cluster_indices": trace_layer["selected_trace_equality"]["zero_cluster_indices"],
            "family_sectors": trace_layer["selected_trace_equality"]["family_sectors"],
            "H_sector": trace_layer["selected_trace_equality"]["H_sector"],
        },
        "not_imported_as_closed": {
            "dotD_alpha1_source": True,
            "selected_alpha1_tangent_parameter": True,
            "retarded_overlap_derivative_formula": True,
            "primitive_C1_response": True,
            "A_selected": True,
            "b_selected": True,
            "Delta_S2_rows": True,
            "strict_csk_rows": True,
        },
    }

    previous_selected_fields = local_payload["closure_decision"]["selected_payload_field_count"]
    upgraded_closed_layers = [
        "F0_projective_gerbe_rhoE_S3_source",
        "U1_selected_trace_equality_for_27mode_DE",
        "U2_selected_DE_gap_Riesz_Green_layer",
    ]
    still_open_payload_fields = [
        "selected visible Chern-Weil/GS row as full same-source operator row",
        "HYM projector source promotion beyond D_E gap layer",
        "rank2-to-rank3 End0 sector-transfer values for response rows",
        "same-branch dotD_alpha1 source and transport derivative",
        "selected alpha1 tangent or retarded-overlap derivative formula",
        "coherent zero-mode bases/Gram data for C1 response",
        "primitive C1 overlap contractions and 24 primitive 3x3 atoms",
        "selected End0-to-sector functor values",
        "nonlinear/offdiagonal HYM control for full Delta_S2 density",
    ]
    payload_upgrade = {
        "schema": "MTTFullSectorPayloadUpgradeAfterQ79Trace.v1",
        "status": "DEGREEN_LAYER_UPGRADED_FULL_PAYLOAD_STILL_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "previous_local_payload_status": local_payload["status"],
        "previous_selected_payload_field_count": previous_selected_fields,
        "upgraded_closed_layer_count": len(upgraded_closed_layers),
        "upgraded_closed_layers": upgraded_closed_layers,
        "D_E_Riesz_Green_gap_layer_closed": de_gap_closed,
        "dotD_alpha1_source_closed": dotd_source_closed,
        "primitive_C1_closed": primitive_c1_closed,
        "fullsector_payload_closed": False,
        "still_open_payload_fields": still_open_payload_fields,
        "supersedes_local_step39_DE_open_wording": True,
        "does_not_supersede": [
            "dotD_alpha1 source/driver",
            "primitive C1 contractions",
            "End0-to-sector functor values",
            "nonlinear HYM/offdiagonal control",
            "Delta_S2 row emission",
        ],
    }

    row_gate = {
        "schema": "MTTDeltaS2RowGateAfterDEGreenImport.v1",
        "status": "ROW_GATE_STILL_BLOCKED_BY_DOTD_C1_AND_FULL_PAYLOAD",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "D_E_Riesz_Green_gap_layer_closed": de_gap_closed,
        "fullsector_payload_closed": False,
        "previous_delta_s2_row_bridge_status": local_row_bridge["status"],
        "delta_s2_source_rows_emitted_now": 0,
        "phi_sector_n_numeric_rows_emitted_now": 0,
        "strict_csk_source_rows_emitted_now": 0,
        "conditional_if_remaining_payload_closes": {
            "delta_s2_source_rows": 9,
            "phi_sector_n_numeric_rows": 9,
            "strict_csk_source_rows": 9,
        },
        "row_blockers_after_import": [
            "selected dotD_alpha1 source and alpha1 driver",
            "selected primitive C1 contractions",
            "same-source sector response matrices / A_selected / b_selected",
            "End0-to-sector value functor",
            "nonlinear/offdiagonal HYM correction",
        ],
    }

    next_packet = {
        "schema": "MTTNextCutsetAfterDEGreenImport.v1",
        "status": "NEXT_IS_SELECTED_ALPHA1_TANGENT_OR_RETARDED_KERNEL",
        "closure_claimed": True,
        "closed_now": [
            "selected 27-mode D_E trace equality imported from q79",
            "D_E source flags are theorem-derived for the gap layer",
            "selected Riesz/Green gap layer imported",
            "local full-sector payload no longer treats D_E/Riesz/Green gap as open",
        ],
        "still_open": still_open_payload_fields,
        "next_required_artifact": NEXT,
        "q79_next_required_artifact": q79_dotd["next_required_artifact"],
        "minimal_next_contract": dotd_obstruction["minimal_closure_contract"],
        "reason": (
            "D_E/Riesz/Green is a zeroth-order gap layer.  Delta_S2 and C1 response need the "
            "first-variation dotD_alpha1 source, selected alpha1 tangent/retarded derivative, "
            "and primitive C1 contractions from the same q79/F,m=1 branch."
        ),
    }

    candidate = {
        "candidate": "MTTSelectedVisibleChernWeilDEGreenImportOrFullSectorPayloadUpgrade",
        "status": STATUS,
        "closure_claimed": True,
        "strict_delta_s2_source_rows_claimed": False,
        "strict_csk_source_theorem_claimed": False,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "theorem": {
            "name": "VisibleChernWeilDEGreenImportTheorem",
            "proved": True,
            "statement": (
                "The q79 selected trace equality theorem upgrades the local full-sector payload: "
                "the emitted 27-mode D_E formula is selected source data at the gap/Riesz/Green layer. "
                "This supersedes the local Step39 wording that full-sector D_E/Riesz/Green was open. "
                "It does not emit dotD_alpha1, alpha1 driver, primitive C1 contractions, Delta_S2 rows, "
                "or strict c_{s,k} rows."
            ),
        },
        "closure_decision": {
            "DE_Green_import_built": True,
            "selected_trace_equality_for_27mode_DE": selected_trace_closed,
            "D_E_Riesz_Green_gap_layer_closed": de_gap_closed,
            "local_step39_DE_open_wording_superseded": True,
            "dotD_alpha1_source_closed": dotd_source_closed,
            "primitive_C1_closed": primitive_c1_closed,
            "fullsector_payload_closed": False,
            "delta_s2_source_rows_emitted": 0,
            "accepted_phi_sector_n_numeric_row_count": 0,
            "accepted_strict_csk_source_row_count": 0,
            "next_required_artifact": NEXT,
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "packets": {
            "visible_chernweil_degreen_import_ledger": rel(IMPORT_LEDGER),
            "fullsector_payload_upgrade": rel(PAYLOAD_UPGRADE),
            "deltas2_row_gate_after_degreen_import": rel(ROW_GATE),
            "next_cutset": rel(NEXT_PACKET),
        },
    }

    cert = {
        "certificate": "MTTSelectedVisibleChernWeilDEGreenImportOrFullSectorPayloadUpgradeCertificate",
        "status": STATUS,
        "theorem": candidate["theorem"]["name"],
        "DE_Green_import_built": True,
        "selected_trace_equality_for_27mode_DE": selected_trace_closed,
        "D_E_Riesz_Green_gap_layer_closed": de_gap_closed,
        "local_step39_DE_open_wording_superseded": True,
        "dotD_alpha1_source_closed": dotd_source_closed,
        "primitive_C1_closed": primitive_c1_closed,
        "fullsector_payload_closed": False,
        "delta_s2_source_rows_emitted": 0,
        "accepted_phi_sector_n_numeric_row_count": 0,
        "accepted_strict_csk_source_row_count": 0,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected VisibleChernWeilDEGreenImport or FullSectorPayloadUpgrade v1

Status: `{STATUS}`

## Theorem

`VisibleChernWeilDEGreenImportTheorem` is proved.

The q79 selected trace equality theorem is now imported into the SM closure
payload chain.  It proves that the emitted 27-mode `D_E` formula is selected
source data at the gap/Riesz/Green layer.

## What Moves

- selected trace equality for emitted 27-mode `D_E`: `{selected_trace_closed}`
- theorem-derived `D_E` source flags at gap layer: `{trace_closes["D_E_source_flags_theorem_derived"]}`
- selected Riesz/Green gap layer: `{trace_closes["selected_Riesz_Green_gap_layer_closed"]}`
- selected gap lower bound: `{trace_layer["gap_layer"]["selected_gap_lower_bound"]}`
- selected Green norm bound: `{trace_layer["gap_layer"]["selected_green_norm_bound"]}`

This supersedes the older local Step39 wording that full-sector `D_E/Riesz/Green`
was still open at the gap layer.

## What Does Not Move

- selected `dotD_alpha1` source: `{dotd_source_closed}`
- primitive `C1` contractions: `{primitive_c1_closed}`
- accepted `Delta_S2` source rows: `0`
- accepted `Phi_sector_N` numeric rows: `0`
- accepted strict `c_{{s,k}}` source rows: `0`

## Next Artifact

`{NEXT}`.
"""

    write_json(IMPORT_LEDGER, import_ledger)
    write_json(PAYLOAD_UPGRADE, payload_upgrade)
    write_json(ROW_GATE, row_gate)
    write_json(NEXT_PACKET, next_packet)
    write_json(CANDIDATE, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
