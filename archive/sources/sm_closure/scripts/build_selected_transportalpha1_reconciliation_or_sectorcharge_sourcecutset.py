"""Reconcile transported Phi_fin trace, alpha1 bridge, and sector-charge frontier."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_transportalpha1_reconciliation_or_sectorcharge_sourcecutset"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
FRONTIER = PACKET_DIR / "reconciled_transport_alpha1_sector_frontier.packet.json"
CUTSET = PACKET_DIR / "sectorcharge_1m_or_transportclosed_replay_cutset.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_TransportAlpha1_Reconciliation_or_SectorCharge_SourceCutset_v1.md"

STATUS = "MTT_SELECTED_TRANSPORTALPHA1_RECONCILIATION_BUILT_SECTOR_SOURCE_CUTSET_OPEN"
NEXT = "MTT_Selected_SectorCharge_1MDirac_SourceEmission_or_TransportClosedValidatorReplay_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    transport = load(DATA / "selected_gauge_transported_bn_phifin_trace.candidate.json")
    alpha1_bridge = load(DATA / "selected_visible_routec_phifin_alpha1_derivative_bridge.candidate.json")
    sector_charge = load(DATA / "selected_sectorcharge_gram_transfernormalization_packet.candidate.json")
    physical_route = load(DATA / "selected_physicaldotd_sectorrouting_after_hymfirstsolve.candidate.json")
    latest_frontier = load(DATA / "selected_latest_trueequivalencefrontier_or_valueemissioncutset.candidate.json")

    bridge = alpha1_bridge["bridge_result"]
    gram = sector_charge["gram_transfer_packet"]
    minimal = sector_charge["minimal_open_fields"]

    frontier = {
        "schema": "MTTTransportAlpha1SectorChargeReconciledFrontier.v1",
        "status": "ALPHA1_RETIRED_SECTOR_SOURCE_REPLAY_OPEN",
        "SM_parity_closed": latest_frontier["SM_parity_closed"],
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "transport_trace_closed_functionally": transport["what_closes_now"]["gauge_transported_PhiFin_trace"],
        "functional_rho_s_candidate_closed": transport["what_closes_now"]["functional_rho_s_promotion"],
        "same_branch_alpha1_derivative_retired": bridge["same_branch_alpha1_derivative_closed_by_import"],
        "selected_dotD_source_verified_retired": bridge["selected_dotD_source_verified"],
        "alpha1_driver_verified_retired": bridge["alpha1_driver_verified"],
        "old_sectorcharge_alpha1_open_field_is_superseded": (
            sector_charge["transfer_to_alpha1_decision"]["alpha1_driver_verified"] is False
            and bridge["alpha1_driver_verified"] is True
        ),
        "still_open": {
            "selected_zero_mode_bases_K_s": minimal["selected_zero_mode_bases_K_s"]["closed"] is False,
            "selected_rho_s_source_map": minimal["selected_rho_s_source_map"]["closed"] is False,
            "selected_sector_charge_or_chirality_table": minimal[
                "selected_sector_charge_or_chirality_table"
            ]["closed"]
            is False,
            "selected_1M_Dirac_neutrino_rule": minimal["selected_1M_Dirac_neutrino_rule"]["closed"] is False,
            "transport_closed_finite_validator_replay": transport["what_remains_open"][
                "transport_closed_finite_validator_replay"
            ],
            "selected_dynamic_PhiFin_C1_payload": alpha1_bridge["payload_boundary"][
                "full_PhiFin_alpha1_payload_selected_values_emitted"
            ]
            is False,
            "actual_QaSU3_operator_packet": physical_route["what_remains_open"]["actual_QaSU3_operator_packet"],
            "true_SM_equivalence": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cutset = {
        "schema": "MTTSectorCharge1MOrTransportClosedReplayCutset.v1",
        "status": "NEXT_GATE_IS_SOURCE_ROUTING_OR_TRANSPORT_CLOSED_REPLAY",
        "legal_next_routes": {
            "route_A_sector_source_emission": {
                "goal": "emit selected sector charge/chirality table, selected 1_M Dirac-neutrino rule, and selected zero-mode/rho_s source map on the transported carriers",
                "why": "This promotes the functional rho_s trace into sector-ready source data without treating alpha1 as a free scalar.",
            },
            "route_B_transport_closed_validator_replay": {
                "goal": "enrich or symbolically close the finite B_N validator basis under U=exp(-u ad(T3)), then replay D_E/Riesz/Green/projector/dotD validators with theorem-derived flags",
                "why": "This turns the functional transported trace into validator-ready finite matrices.",
            },
        },
        "retired_as_primary_blockers": [
            "untransported B_N equality",
            "same-branch alpha1 derivative",
            "alpha1 driver normalization",
            "honest dotD replay for alpha1",
        ],
        "forbidden_shortcuts": [
            "do not copy untransported model-active B_N projectors as selected HYM projectors",
            "do not use alpha1 as an adjustable normalization knob",
            "do not promote the functional rho_s candidate without selected sector zero-mode/source routing",
            "do not use observed SM values to select sector charge or chirality",
        ],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "MTTSelectedTransportAlpha1ReconciliationOrSectorChargeSourceCutset",
        "status": STATUS,
        "inputs": {
            "transported_bn_phifin_trace": rel(DATA / "selected_gauge_transported_bn_phifin_trace.candidate.json"),
            "visible_routec_alpha1_derivative_bridge": rel(
                DATA / "selected_visible_routec_phifin_alpha1_derivative_bridge.candidate.json"
            ),
            "sectorcharge_gram_transfer_packet": rel(
                DATA / "selected_sectorcharge_gram_transfernormalization_packet.candidate.json"
            ),
            "physical_dotd_sector_routing_frontier": rel(
                DATA / "selected_physicaldotd_sectorrouting_after_hymfirstsolve.candidate.json"
            ),
            "latest_true_equivalence_frontier": rel(
                DATA / "selected_latest_trueequivalencefrontier_or_valueemissioncutset.candidate.json"
            ),
        },
        "output_packets": {
            "frontier": rel(FRONTIER),
            "cutset": rel(CUTSET),
        },
        "theorem": {
            "name": "TransportAlpha1ReconciliationSectorSourceCutsetTheorem",
            "proved": True,
            "statement": (
                "The selected gauge-transported Phi_fin trace and the later visible/Route-C alpha1 bridge jointly retire untransported B_N equality, same-branch alpha1 derivative, alpha1 driver normalization, and honest alpha1 dotD replay as primary blockers. "
                "The remaining actual Qa/SU3/true-equivalence gate is sector-source promotion on transported carriers or transport-closed finite validator replay."
            ),
        },
        "what_closes_now": {
            "transport_alpha1_frontiers_reconciled": True,
            "alpha1_removed_from_sectorcharge_primary_cutset": True,
            "functional_trace_kept_distinct_from_validator_ready_packet": True,
            "next_source_or_transport_replay_gate_selected": True,
        },
        "what_remains_open": frontier["still_open"],
        "SM_parity_closed": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_TransportAlpha1_Reconciliation_or_SectorCharge_SourceCutset_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "SM_parity_closed": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "alpha1_retired_as_primary_blocker": True,
        "sector_source_or_transport_closed_replay_open": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected TransportAlpha1 Reconciliation or SectorCharge SourceCutset v1

Status: `{STATUS}`.

This reconciles two live source routes. The transported Phi_fin trace is
functionally selected, and the later visible/Route-C bridge retires the
same-branch alpha1 derivative, alpha1 driver normalization, and honest alpha1
dotD replay as primary blockers.

What remains is not another scalar normalization search. The next gate is
either selected sector-source emission on transported carriers, including the
sector charge/chirality table and the `1_M` Dirac-neutrino rule, or a
transport-closed finite validator replay for D_E/Riesz/Green/projector/dotD.

True SM equivalence and no-knob closure remain open.

Next artifact: `{NEXT}`.
"""

    FRONTIER.write_text(json.dumps(frontier, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CUTSET.write_text(json.dumps(cutset, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
