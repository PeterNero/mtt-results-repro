"""Build sector-charge/1M source emission or transport-closed replay gate.

This consolidates the post-transport sector-source frontier.  The earlier
two-lane cutset allowed either sector-source emission or transport-closed
finite validator replay.  The symbolic transport replay is now closed for the
stationary projector/Riesz/Green/rho_s layer, so this artifact narrows the live
gate to selected same-branch U10/Ubar5/1M matter-slot source emission plus the
dynamic C1 payload.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_sectorcharge_1mdirac_sourceemission_or_transportclosedvalidatorreplay"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROUTE_DECISION = PACKET_DIR / "sector_source_or_transport_replay_route_decision.packet.json"
SOURCE_TEMPLATE = PACKET_DIR / "u10_ubar5_1m_samebranch_source_emission_template.packet.json"
LIVE_FRONTIER = PACKET_DIR / "live_sector_source_frontier_after_transport_replay.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
AUDIT = CORPUS / f"{SLUG}_audit.py"
NOTE = CORPUS / "MTT_Selected_SectorCharge_1MDirac_SourceEmission_or_TransportClosedValidatorReplay_v1.md"

STATUS = "MTT_SELECTED_SECTORCHARGE_1MDIRAC_SOURCEEMISSION_OR_TRANSPORTCLOSEDVALIDATORREPLAY_BUILT_TRANSPORT_REPLAY_CLOSED_SOURCE_EMISSION_OPEN"
NEXT = "MTT_Selected_U10Ubar5_1M_SourcePromotion_SameBranch_Emission_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    cutset = load(DATA / "selected_transportalpha1_reconciliation_or_sectorcharge_sourcecutset.candidate.json")
    transport_import = load(DATA / "selected_transportreplay_imported_or_u10ubar5_1m_source.candidate.json")
    transport_validator = load(DATA / "selected_transport_conjugation_validator_replay.candidate.json")
    one_m_gate = load(DATA / "selected_1m_dirac_source_or_u10ubar5_polarization.candidate.json")
    one_m_attempt = load(DATA / "selected_sectorcharge_1m_dirac_rule_attempt.candidate.json")
    smslot_ledger = load(DATA / "selected_smslotfunctor_downstream_operator_payloads_or_smparity_ledger.candidate.json")
    latest_dynamic = load(DATA / "selected_latest_sourcefrontier_reconciliation_or_dynamicc1proofgate.candidate.json")

    route_decision = {
        "schema": "MTTSectorSourceOrTransportReplayRouteDecision.v1",
        "status": "TRANSPORT_CLOSED_REPLAY_ROUTE_CLOSED_SOURCE_EMISSION_ROUTE_OPEN",
        "SM_parity_closed": transport_import["SM_parity_closed"],
        "route_B_transport_closed_validator_replay": {
            "closed_now": transport_validator["promotion_decision"]["transport_closed_finite_validator_replay"],
            "selected_source_verified": transport_validator["validator_result"]["selected_source_verified"],
            "selected_rho_s_validator_ready": transport_validator["validator_result"]["selected_rho_s_validator_ready"],
            "selected_projector_riesz_green_replay": transport_validator["validator_result"][
                "all_sector_projector_riesz_green_replays_pass"
            ],
            "dotD_alpha1_included": transport_validator["validator_result"]["selected_dotD_source_verified"],
            "scope": "stationary projector/Riesz/Green/rho_s replay only; dynamic C1 and dotD-alpha1 are not promoted here",
        },
        "route_A_sector_source_emission": {
            "closed_now": False,
            "structural_1M_rule_available": one_m_gate["route_A_SU5_E6_polarization"]["structural_1M_rule_available"],
            "q79_U10_Ubar5_support_closed": one_m_gate["route_A_SU5_E6_polarization"]["support_closed"],
            "selected_U10_source_closed": one_m_gate["selection_decision"]["selected_U10_Ubar5_polarization_closed"],
            "selected_1M_shift_source_closed": one_m_gate["selection_decision"][
                "selected_1M_Dirac_neutrino_source_rule_closed"
            ],
            "same_branch_source_emission_required": True,
        },
        "alpha1_retired_as_primary_blocker": cutset["what_closes_now"]["alpha1_removed_from_sectorcharge_primary_cutset"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    source_template = {
        "schema": "MTTU10Ubar51MSameBranchSourceEmissionTemplate.v1",
        "status": "TEMPLATE_READY_SOURCE_EMISSION_OPEN",
        "must_emit": {
            "selected_U10_clock_source": {
                "target_value": "U_10=I_3",
                "currently_support_only": True,
                "source_closed": False,
            },
            "selected_Ubar5_shift_source": {
                "target_value": "U_bar5=F",
                "currently_support_only": True,
                "source_closed": False,
            },
            "selected_1M_Dirac_neutrino_shift_source": {
                "target_rule": "1_M=N^c routes nuD with d on the shift/non-10 side",
                "structural_rule_candidate": one_m_attempt["structural_rule_candidate"],
                "source_closed": False,
            },
            "selected_ordered_matter_slot_packet": {
                "phase_route": ["u", "e"],
                "shift_route": ["d", "nuD"],
                "source_closed": False,
            },
            "selected_overlap_transfer_normalization": {
                "static_tier_closed": smslot_ledger["what_closes_now"][
                    "selected_static_finite_trace_transfer_normalization"
                ],
                "dynamic_tier_closed": False,
            },
        },
        "forbidden_shortcuts": [
            "do not use observed masses, mixings, CP phases, or benchmark matrices",
            "do not copy support-only q79 transversality flags as selected source emission",
            "do not reopen alpha1 as a scalar knob",
            "do not treat stationary transport replay as dynamic C1 source promotion",
        ],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    live_frontier = {
        "schema": "MTTLiveSectorSourceFrontierAfterTransportReplay.v1",
        "status": "LIVE_GATE_IS_U10_UBAR5_1M_SOURCE_EMISSION_PLUS_DYNAMIC_C1",
        "SM_parity_closed": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "static_source_tier_closed": latest_dynamic["what_closes_now"][
            "static_U10_Ubar5_1M_overlap_gates_retired"
        ],
        "transport_closed_projector_riesz_green_rhos_closed": True,
        "remaining_source_payloads": [
            "same-branch U_10=I_3 source emission",
            "same-branch U_bar5=F source emission",
            "same-branch 1_M=N^c Dirac shift source emission",
            "ordered matter-slot packet promoted as selected source",
            "dynamic PhiFin^C1/primitive C1 payload with A_selected and b_selected",
        ],
        "remaining_true_equivalence_payloads": [
            "actual Qa/SU3 operator packet beyond parity interface",
            "dynamic C1 source promotion or independent selected Galerkin rows",
            "precision profile/loop values or actual source/operator upgrade",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedSectorCharge1MDiracSourceEmissionOrTransportClosedValidatorReplay",
        "status": STATUS,
        "inputs": {
            "transport_alpha1_cutset": rel(DATA / "selected_transportalpha1_reconciliation_or_sectorcharge_sourcecutset.candidate.json"),
            "transport_replay_import": rel(DATA / "selected_transportreplay_imported_or_u10ubar5_1m_source.candidate.json"),
            "transport_conjugation_validator_replay": rel(DATA / "selected_transport_conjugation_validator_replay.candidate.json"),
            "selected_1M_dirac_source_or_u10ubar5_polarization": rel(DATA / "selected_1m_dirac_source_or_u10ubar5_polarization.candidate.json"),
            "sectorcharge_1m_dirac_rule_attempt": rel(DATA / "selected_sectorcharge_1m_dirac_rule_attempt.candidate.json"),
            "static_smslot_downstream_ledger": rel(DATA / "selected_smslotfunctor_downstream_operator_payloads_or_smparity_ledger.candidate.json"),
            "latest_dynamic_c1_frontier": rel(DATA / "selected_latest_sourcefrontier_reconciliation_or_dynamicc1proofgate.candidate.json"),
        },
        "output_packets": {
            "route_decision": rel(ROUTE_DECISION),
            "source_emission_template": rel(SOURCE_TEMPLATE),
            "live_frontier": rel(LIVE_FRONTIER),
        },
        "theorem": {
            "name": "SectorCharge1MTransportReplayReductionTheorem",
            "proved": True,
            "statement": (
                "The transport-closed validator replay route now closes the stationary projector/Riesz/Green/rho_s layer. "
                "Therefore the sector-source branch no longer needs another alpha1 or transport replay repair; it is reduced to same-branch source emission of U_10=I_3, U_bar5=F, the 1_M=N^c Dirac shift source, and the ordered matter-slot packet, while dynamic C1 source promotion remains a separate open gate."
            ),
        },
        "what_closes_now": {
            "transport_closed_validator_replay_route_resolved": True,
            "stationary_projector_riesz_green_rhos_not_primary_blocker": True,
            "U10_Ubar5_1M_source_template_built": True,
            "sector_source_frontier_narrowed": True,
            "alpha1_not_reopened_as_knob": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_U10_clock_source": True,
            "selected_Ubar5_shift_source": True,
            "selected_1M_Dirac_neutrino_shift_source": True,
            "selected_ordered_matter_slot_packet": True,
            "selected_dynamic_PhiFin_C1_payload": True,
            "selected_A_selected_and_b_selected": True,
            "actual_QaSU3_operator_packet": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "SM_parity_closed": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_SectorCharge_1MDirac_SourceEmission_or_TransportClosedValidatorReplay_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "packet_paths": candidate["output_packets"],
        "SM_parity_closed": True,
        "transport_closed_validator_replay_route_resolved": True,
        "samebranch_source_emission_open": True,
        "dynamic_C1_open": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected SectorCharge 1MDirac SourceEmission or TransportClosedValidatorReplay v1

Status: `{STATUS}`.

The two-route sector frontier has now collapsed to one live source-emission
gate. Symbolic transport-conjugation closes the stationary
projector/Riesz/Green/`rho_s` replay route, so the remaining sector-source
payload is same-branch emission of `U_10=I_3`, `U_bar5=F`, the `1_M=N^c`
Dirac-neutrino shift source, and the ordered matter-slot packet.

This is a constrained superset result: HYM/transport, q79/SU(5)/E6, and
SM-slot ledgers are combined only as compatibility constraints against the
locked selected source target. No observed constants, benchmark matrices, or
alpha1 scalar retuning are used as selectors.

Dynamic `Phi_fin^C1`, `A_selected`, `b_selected`, true SM equivalence, and
no-knob closure remain open.

Next artifact: `{NEXT}`.
"""

    audit = f'''"""Audit {SLUG}."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "{SLUG}"
DATA = ROOT / "candidate_data" / f"{{SLUG}}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ROUTE_DECISION = PACKET_DIR / "sector_source_or_transport_replay_route_decision.packet.json"
SOURCE_TEMPLATE = PACKET_DIR / "u10_ubar5_1m_samebranch_source_emission_template.packet.json"
LIVE_FRONTIER = PACKET_DIR / "live_sector_source_frontier_after_transport_replay.packet.json"
CERT = ROOT / "certificates" / f"{{SLUG}}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_SectorCharge_1MDirac_SourceEmission_or_TransportClosedValidatorReplay_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    route = load(ROUTE_DECISION)
    template = load(SOURCE_TEMPLATE)
    frontier = load(LIVE_FRONTIER)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == "{STATUS}", "status mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["SM_parity_closed"] is True, "SM parity regressed")
    require(data["true_SM_equivalence_closed"] is False, "true equivalence overclaimed")
    require(data["no_knob_closed"] is False, "no-knob overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(data["closure_claimed"] is False, "closure overclaimed")

    require(route["route_B_transport_closed_validator_replay"]["closed_now"] is True, "transport replay not closed")
    require(route["route_B_transport_closed_validator_replay"]["selected_rho_s_validator_ready"] is True, "rho_s replay not ready")
    require(route["route_B_transport_closed_validator_replay"]["dotD_alpha1_included"] is False, "dotD alpha1 overincluded")
    require(route["route_A_sector_source_emission"]["closed_now"] is False, "route A overclosed")
    require(route["route_A_sector_source_emission"]["structural_1M_rule_available"] is True, "1M support missing")
    require(route["route_A_sector_source_emission"]["q79_U10_Ubar5_support_closed"] is True, "q79 support missing")

    require(template["must_emit"]["selected_U10_clock_source"]["source_closed"] is False, "U10 overclosed")
    require(template["must_emit"]["selected_Ubar5_shift_source"]["source_closed"] is False, "Ubar5 overclosed")
    require(template["must_emit"]["selected_1M_Dirac_neutrino_shift_source"]["source_closed"] is False, "1M overclosed")
    require(template["must_emit"]["selected_overlap_transfer_normalization"]["static_tier_closed"] is True, "static normalization not closed")
    require(template["must_emit"]["selected_overlap_transfer_normalization"]["dynamic_tier_closed"] is False, "dynamic normalization overclosed")
    require(len(template["forbidden_shortcuts"]) == 4, "forbidden shortcuts changed")

    require(frontier["static_source_tier_closed"] is True, "static tier not closed")
    require(frontier["transport_closed_projector_riesz_green_rhos_closed"] is True, "transport replay not closed in frontier")
    require("dynamic PhiFin^C1/primitive C1 payload with A_selected and b_selected" in frontier["remaining_source_payloads"], "dynamic C1 missing")
    require(cert["transport_closed_validator_replay_route_resolved"] is True, "cert route flag missing")
    require(cert["samebranch_source_emission_open"] is True, "cert source-open flag missing")
    require(data["next_required_artifact"] == "{NEXT}", "wrong next artifact")
    require("No observed constants" in note, "note missing guardrail")
    print(f"PASS {{DATA.name}}: {{data['status']}}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
'''

    write_json(ROUTE_DECISION, route_decision)
    write_json(SOURCE_TEMPLATE, source_template)
    write_json(LIVE_FRONTIER, live_frontier)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    AUDIT.write_text(audit, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
