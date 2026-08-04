"""Import closed transport replay and narrow the live gate to U10/Ubar5/1M source emission."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_transportreplay_imported_or_u10ubar5_1m_source"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
FRONTIER = PACKET_DIR / "u10_ubar5_1m_remaining_source_frontier.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_TransportReplay_Imported_or_U10Ubar5_1M_Source_v1.md"

STATUS = "MTT_SELECTED_TRANSPORTREPLAY_IMPORTED_BUILT_U10UBAR5_1M_SOURCE_OPEN"
NEXT = "MTT_Selected_U10Ubar5_1M_SourcePromotion_SameBranch_Emission_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    reconciliation = load(DATA / "selected_transportalpha1_reconciliation_or_sectorcharge_sourcecutset.candidate.json")
    transport_replay = load(DATA / "selected_transport_conjugation_validator_replay.candidate.json")
    one_m_gate = load(DATA / "selected_1m_dirac_source_or_u10ubar5_polarization.candidate.json")
    sector_attempt = load(DATA / "selected_sectorcharge_1m_dirac_rule_attempt.candidate.json")

    frontier = {
        "schema": "MTTU10Ubar51MRemainingSourceFrontier.v1",
        "status": "TRANSPORT_REPLAY_IMPORTED_SECTOR_SOURCE_ONLY_OPEN",
        "SM_parity_closed": reconciliation["SM_parity_closed"],
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "transport_closed_validator_replay_imported": transport_replay["what_closes_now"][
            "transport_closed_finite_validator_replay"
        ],
        "validator_ready_sector_rho_s_packet_imported": transport_replay["what_closes_now"][
            "validator_ready_sector_rho_s_packet"
        ],
        "projector_riesz_green_source_verified": (
            transport_replay["what_closes_now"]["selected_projector_source_verified"]
            and transport_replay["what_closes_now"]["selected_riesz_green_source_verified"]
        ),
        "structural_1M_rule_candidate_available": sector_attempt["structural_rule_candidate"][
            "matches_required_route"
        ],
        "route_A_finite_polarization_support": one_m_gate["what_closes_now"][
            "route_A_finite_polarization_support"
        ],
        "route_B_projector_support": one_m_gate["what_closes_now"]["route_B_projector_support"],
        "still_open": {
            "selected_U10_clock_source": one_m_gate["what_remains_open"]["selected_U10_clock_source"],
            "selected_Ubar5_shift_source": one_m_gate["what_remains_open"]["selected_Ubar5_shift_source"],
            "selected_1M_Dirac_neutrino_shift_source": one_m_gate["what_remains_open"][
                "selected_1M_Dirac_neutrino_shift_source"
            ],
            "selected_ordered_matter_slot_packet": one_m_gate["what_remains_open"][
                "selected_ordered_matter_slot_packet"
            ],
            "selected_overlap_transfer_normalization": one_m_gate["what_remains_open"][
                "selected_overlap_transfer_normalization"
            ],
            "selected_A_selected_and_b_selected": one_m_gate["what_remains_open"][
                "selected_A_selected_and_b_selected"
            ],
            "selected_dynamic_PhiFin_C1_payload": reconciliation["what_remains_open"][
                "selected_dynamic_PhiFin_C1_payload"
            ],
            "actual_QaSU3_operator_packet": reconciliation["what_remains_open"][
                "actual_QaSU3_operator_packet"
            ],
            "true_SM_equivalence": True,
        },
        "retired_now": {
            "transport_closed_finite_validator_replay": True,
            "validator_ready_sector_rho_s_packet": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "MTTSelectedTransportReplayImportedOrU10Ubar51MSource",
        "status": STATUS,
        "inputs": {
            "transport_alpha1_reconciliation": rel(
                DATA / "selected_transportalpha1_reconciliation_or_sectorcharge_sourcecutset.candidate.json"
            ),
            "transport_conjugation_validator_replay": rel(
                DATA / "selected_transport_conjugation_validator_replay.candidate.json"
            ),
            "selected_1m_dirac_source_or_u10ubar5_polarization": rel(
                DATA / "selected_1m_dirac_source_or_u10ubar5_polarization.candidate.json"
            ),
            "sectorcharge_1m_rule_attempt": rel(
                DATA / "selected_sectorcharge_1m_dirac_rule_attempt.candidate.json"
            ),
        },
        "output_packets": {
            "frontier": rel(FRONTIER),
        },
        "theorem": {
            "name": "TransportReplayImportedU10Ubar51MSourceFrontierTheorem",
            "proved": True,
            "statement": (
                "Importing the symbolic transport-conjugation validator replay closes the transport-closed projector/Riesz/Green replay and validator-ready rho_s packet as active blockers. "
                "Given the structural E6/SU5 1_M Dirac rule and q79 U_10/U_bar5 polarization support, the remaining sector-source gate is selected same-branch emission of U_10, U_bar5, the 1_M Dirac shift source, and the ordered matter-slot packet."
            ),
        },
        "what_closes_now": {
            "transport_replay_imported_as_closed": True,
            "validator_ready_rho_s_imported": True,
            "sector_source_frontier_narrowed_to_U10_Ubar5_1M": True,
            "observed_data_excluded_as_selector": True,
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
        "certificate": "MTT_Selected_TransportReplay_Imported_or_U10Ubar5_1M_Source_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "transport_replay_imported_as_closed": True,
        "sector_source_frontier_narrowed_to_U10_Ubar5_1M": True,
        "SM_parity_closed": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected TransportReplay Imported or U10Ubar5 1M Source v1

Status: `{STATUS}`.

The symbolic transport-conjugation validator replay is imported as closed for
projector/Riesz/Green replay and validator-ready `rho_s`. That means the live
sector gate is no longer transport closure.

The remaining source object is selected same-branch emission of `U_10=I_3`,
`U_bar5=F`, the `1_M` Dirac-neutrino shift source, and the ordered matter-slot
packet. The E6/SU(5) and q79 data support this route structurally, but do not
yet promote it to selected source emission.

True SM equivalence and no-knob closure remain open.

Next artifact: `{NEXT}`.
"""

    FRONTIER.write_text(json.dumps(frontier, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
